#!/usr/bin/env python3
"""
模型信息查看工具 - 查看 LLM 模型配置和权重信息
"""

import argparse
import importlib
import logging
import os
import re
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from glob import glob
from typing import Dict, List, Optional, Tuple

from tqdm import tqdm


def natural_sort_key(s: str) -> List:
    return [
        int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", s)
    ]


def format_number(num: int) -> str:
    return f"{num:,}"


logger = logging.getLogger("model_inspector")

_BOLD = "\033[1m"
_YELLOW = "\033[33m"
_RED = "\033[31m"
_GREEN = "\033[32m"
_RESET = "\033[0m"


class _ColorFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        msg = record.getMessage()
        if record.levelno >= logging.ERROR:
            return f"{_BOLD}{_RED}✗ {msg}{_RESET}"
        if record.levelno >= logging.WARNING:
            return f"{_BOLD}{_YELLOW}⚠ {msg}{_RESET}"
        return f"{_GREEN}{msg}{_RESET}"


def _setup_logging() -> None:
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(_ColorFormatter())
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)


# safetensors dtype → (torch dtype 字符串, 每个元素字节数)
# 新 dtype 出现时在此添加即可
_ST_DTYPE_INFO = {
    "BOOL": ("torch.bool", 1),
    "U8": ("torch.uint8", 1),
    "I8": ("torch.int8", 1),
    "I16": ("torch.int16", 2),
    "I32": ("torch.int32", 4),
    "I64": ("torch.int64", 8),
    "F16": ("torch.float16", 2),
    "BF16": ("torch.bfloat16", 2),
    "F32": ("torch.float32", 4),
    "F64": ("torch.float64", 8),
    "F8_E4M3": ("torch.float8_e4m3fn", 1),
    "F8_E5M2": ("torch.float8_e5m2", 1),
    "F8_E8M0": ("torch.float8_e8m0fnu", 1),
    "U16": ("torch.uint16", 2),
    "U32": ("torch.uint32", 4),
    "U64": ("torch.uint64", 8),
}


def _format_bytes(nbytes: int) -> str:
    if nbytes < 1024:
        return f"{nbytes} B"
    if nbytes < 1024**2:
        return f"{nbytes / 1024:.2f} KB"
    if nbytes < 1024**3:
        return f"{nbytes / 1024 ** 2:.2f} MB"
    return f"{nbytes / 1024 ** 3:.2f} GB"


def format_size(numel: int, dtype) -> str:
    if isinstance(dtype, str) and dtype in _ST_DTYPE_INFO:
        element_size = _ST_DTYPE_INFO[dtype][1]
    else:
        import torch

        if isinstance(dtype, str):
            dtype = getattr(torch, dtype.replace("torch.", ""))
        element_size = (
            torch.finfo(dtype).bits // 8
            if dtype.is_floating_point
            else torch.iinfo(dtype).bits // 8
        )
    size_kb = (numel * element_size) / 1024
    if size_kb < 1:
        return f"{size_kb * 1024:.2f} B"
    if size_kb < 1024:
        return f"{size_kb:.2f} KB"
    size_mb = size_kb / 1024
    if size_mb < 1024:
        return f"{size_mb:.2f} MB"
    return f"{size_mb / 1024:.2f} GB"


def _try_instantiate_from_config(config):
    """Try to instantiate a model from config, using Auto classes first,
    then falling back to the architectures listed in config."""
    import torch
    from transformers import AutoModel, AutoModelForCausalLM

    with torch.device("meta"):
        # 1. Try Auto classes
        for auto_cls in (AutoModel, AutoModelForCausalLM):
            try:
                return auto_cls.from_config(config)
            except ValueError:
                continue

        # 2. Try architectures from config
        architectures = getattr(config, "architectures", None) or []
        config_module = type(config).__module__
        for arch_name in architectures:
            try:
                mod = importlib.import_module(config_module.rsplit(".", 1)[0])
                cls = getattr(mod, arch_name, None)
                if cls is None:
                    continue
                from_config_fn = getattr(cls, "from_config", None) or getattr(
                    cls, "_from_config", None
                )
                if from_config_fn is not None:
                    return from_config_fn(config)
            except Exception:
                continue

    return None


def inspect_structure(model_path: str, out) -> None:
    from transformers import AutoConfig

    logger.info("[2/3] 解析模型结构...")
    print("# 模型结构\n", file=out)

    # 先尝试 trust_remote_code=False（使用 transformers 内置类，更稳定），
    # 失败后回退到 trust_remote_code=True（使用模型自定义代码）
    config = None
    model = None
    for trust in (False, True):
        try:
            config = AutoConfig.from_pretrained(model_path, trust_remote_code=trust)
            model = _try_instantiate_from_config(config)
            if model is not None:
                break
        except Exception:
            continue

    try:
        if model is not None:
            print(f"**模型类**: `{type(model).__name__}`\n", file=out)
            print("```\n" + str(model) + "\n```\n", file=out)
            logger.info("[2/3] 模型结构解析完成 ✓")
        elif config is not None:
            print(
                f"**模型类**: `{type(config).__name__}` (当前 transformers 版本不支持实例化)\n",
                file=out,
            )
            logger.warning(
                "[2/3] 模型结构解析完成 (无法实例化模型结构，仅输出配置信息)"
            )
        else:
            print("**错误**: 解析模型结构失败\n", file=out)
            logger.error("[2/3] 模型结构解析失败: 无法加载配置")
    except Exception as e:
        print(f"**错误**: 解析模型结构失败 - `{e}`\n", file=out)
        logger.error("[2/3] 模型结构解析失败: %s", e)


def inspect_config(model_path: str, out) -> None:
    from transformers import AutoConfig

    logger.info("[1/3] 读取模型配置...")
    print("# 模型配置\n", file=out)
    # 始终输出原始 config.json
    config_json_path = os.path.join(model_path, "config.json")
    if os.path.exists(config_json_path):
        print("<details><summary>原始 config.json</summary>\n", file=out)
        print(f"`{config_json_path}`\n\n```json\n", file=out)
        with open(config_json_path, "r", encoding="utf-8") as f:
            print(f.read(), file=out)
        print("```\n</details>\n", file=out)

    # 输出 transformers 解析后的配置
    print("<details><summary>Transformers 配置</summary>\n", file=out)
    try:
        config = AutoConfig.from_pretrained(model_path, trust_remote_code=True)
        print(f"- **模型类型**: `{type(config).__name__}`", file=out)
        print(f"- **数据类型**: `{getattr(config, 'dtype', 'float16')}`", file=out)
        missing_fields = []
        for label, attr in [
            ("隐藏层大小", "hidden_size"),
            ("层数", "num_hidden_layers"),
            ("注意力头数", "num_attention_heads"),
            ("词表大小", "vocab_size"),
            ("中间层大小", "intermediate_size"),
        ]:
            val = getattr(config, attr, None)
            if val is not None:
                print(f"- **{label}**: {val}", file=out)
            else:
                print(f"- **{label}**: N/A", file=out)
                missing_fields.append(attr)
        print(file=out)
        print(f"```\n{config}\n```\n", file=out)
        if missing_fields:
            logger.warning(
                "[1/3] 模型配置读取完成 (部分字段缺失: %s)", ", ".join(missing_fields)
            )
        else:
            logger.info("[1/3] 模型配置读取完成 ✓")
    except Exception as e:
        print(f"**错误**: Transformers 解析配置失败 - `{e}`\n", file=out)
        logger.error("[1/3] Transformers 解析配置失败: %s", e)
    print("</details>\n", file=out)


def _format_indices(indices: List[int]) -> str:
    """Format a list of integer indices into a compact string.

    Finds maximal arithmetic sub-sequences (constant gap between consecutive
    elements) and formats each with dashes (step=1) or dots (step>1).

    Examples:
        [0, 1, 3, 5, ..., 59] → ``0-1,3,5,...,57,59``
        [2, 4, 6, ..., 42]    → ``2,4,...,40,42``
        [2, 4, 6]             → ``2,4,6``
        [0, 1, 2, 3, 4, 5]    → ``0-5``
    """
    if len(indices) <= 1:
        return ",".join(str(i) for i in indices)

    # 1. Compute gaps and find step-change positions
    gaps = [indices[i] - indices[i - 1] for i in range(1, len(indices))]
    # When gaps[i] != gaps[i-1], a new step starts at position i+1 in `indices`.
    # So the previous run ends at position i, and the new run starts at i+1.
    # Position i (the shared element) belongs to the previous run.
    step_starts = [0]  # start positions of each run in `indices`
    for i in range(1, len(gaps)):
        if gaps[i] != gaps[i - 1]:
            step_starts.append(i + 1)  # new run starts at indices[i+1]
    step_starts.append(len(indices))

    # 2. Build runs: indices[lo..hi) (exclusive hi), then merge 1-element runs
    raw_runs: List[Tuple[int, int, int]] = []  # (start, end, step)
    for k in range(len(step_starts) - 1):
        lo = step_starts[k]
        hi = step_starts[k + 1]  # exclusive
        start = indices[lo]
        end = indices[hi - 1]
        if hi - lo >= 2:
            step = indices[lo + 1] - start
        elif k + 1 < len(step_starts) - 1:
            step = indices[step_starts[k + 1]] - start
        else:
            step = 1
        raw_runs.append((start, end, step))

    runs: List[Tuple[int, int, int]] = list(raw_runs)

    # Merge 1-element runs into adjacent runs whose step they continue.
    i = len(runs) - 2
    while i >= 0:
        s, e, st = runs[i]
        count = (e - s) // st + 1
        if count == 1:
            ns, ne, nst = runs[i + 1]
            if s + nst == ns:
                runs[i + 1] = (s, ne, nst)
                del runs[i]
        i -= 1

    # Prefer contiguous (step=1) runs: if a run's last element is exactly
    # next_run.start - 1, peel it off to extend the following step=1 run.
    i = len(runs) - 2
    while i >= 0:
        s, e, st = runs[i]
        count = (e - s) // st + 1
        ns, ne, nst = runs[i + 1]
        if nst == 1 and count > 1 and e + 1 == ns:
            # Peel last element: shorten this run, expand the next
            runs[i] = (s, e - st, st)
            runs[i + 1] = (e, ne, 1)
        i -= 1

    # 3. Format each run
    def _fmt_run(start: int, end: int, step: int) -> str:
        count = (end - start) // step + 1
        if step == 1:
            if count == 1:
                return str(start)
            return f"{start}-{end}"
        # step > 1
        if count <= 6:
            return ",".join(str(start + step * j) for j in range(count))
        return f"{start},{start + step},...,{end - step},{end}"

    parts = [_fmt_run(s, e, st) for s, e, st in runs]

    # 4. If single run, return directly; if short, join; if long, abbreviate
    if len(parts) == 1:
        return parts[0]
    joined = ",".join(parts)
    return joined


def _find_numeric_segments(name: str) -> List[int]:
    """Return indices of purely-numeric segments in a dot-separated name."""
    return [i for i, seg in enumerate(name.split(".")) if seg.isdigit()]


def _compress_weights(
    all_weights: List[Tuple[str, Tuple, int, str, str]],
) -> List[Tuple[str, Tuple, int, str, str, str]]:
    """Compress weight list by merging identical numeric-indexed segments.

    For each dot-separated name, finds segments that are pure digits (e.g.
    ``blocks.24`` → 24 is numeric).  Merges from rightmost numeric position
    inward so that inner groups (e.g. experts) are collapsed before outer
    groups (e.g. layers/blocks).

    Returns list of (display_name, shape, numel, dtype, fname, note).
    """
    items: List[Tuple[str, Tuple, int, str, str, str]] = [
        (name, shape, numel, dtype, fname, "")
        for name, shape, numel, dtype, fname in all_weights
    ]

    # Collect all numeric segment positions across all names
    seg_positions: set = set()
    for name, *_ in items:
        seg_positions.update(_find_numeric_segments(name))

    # Process from rightmost position inward (inner groups first)
    for pos in sorted(seg_positions, reverse=True):
        groups: Dict[Tuple[str, str], List[Tuple[int, Tuple, int, str, str, str]]] = {}
        ungrouped: List[Tuple[str, Tuple, int, str, str, str]] = []

        for item in items:
            name = item[0]
            segs = name.split(".")
            if pos < len(segs) and segs[pos].isdigit():
                prefix = ".".join(segs[:pos]) + "." if pos > 0 else ""
                suffix = "." + ".".join(segs[pos + 1 :]) if pos + 1 < len(segs) else ""
                groups.setdefault((prefix, suffix), []).append(
                    (int(segs[pos]), *item[1:])
                )
            else:
                ungrouped.append(item)

        merged: List[Tuple[str, Tuple, int, str, str, str]] = []
        for (prefix, suffix), entries in groups.items():
            entries.sort(key=lambda x: x[0])
            # Sub-group by (shape, dtype, note) so alternating patterns merge
            sig_groups: Dict[Tuple, List] = {}
            for e in entries:
                sig = (e[1], e[3], e[5])  # (shape, dtype, note)
                sig_groups.setdefault(sig, []).append(e)

            for (shape, dtype, note), sub_entries in sig_groups.items():
                if len(sub_entries) == 1:
                    idx, sh, numel, dt, fname, nt = sub_entries[0]
                    merged.append((f"{prefix}{idx}{suffix}", sh, numel, dt, fname, nt))
                    continue
                indices = [x[0] for x in sub_entries]
                range_str = _format_indices(indices)
                merged_name = f"{prefix}{range_str}{suffix}"
                single_numel = sub_entries[0][2]
                total_numel = single_numel * len(indices)
                segs = merged_name.split(".")
                label = segs[pos - 1] if pos > 0 else "items"
                new_note = f"×{len(indices)} {label}"
                if note:
                    new_note = f"{new_note}, {note}"
                fnames = {x[4] for x in sub_entries}
                fname = "Multi Files" if len(fnames) > 1 else sub_entries[0][4]
                merged.append((merged_name, shape, total_numel, dtype, fname, new_note))

        items = ungrouped + merged
        items.sort(key=lambda x: natural_sort_key(x[0]))

    return items


def _read_safetensor_file(
    filepath: str,
) -> List[Tuple[str, Tuple[int, ...], int, str, str]]:
    """读取单个 safetensors 文件的元数据（不加载张量数据），返回权重信息列表。

    仅解析文件头部的 JSON 元数据，避免将完整张量加载到内存，
    适用于大模型并发读取场景，不会因 OOM 导致进程被杀。
    """
    import json
    import struct

    fname = os.path.basename(filepath)
    results = []

    with open(filepath, "rb") as f:
        # safetensors 格式: 前8字节为 header 长度(little-endian uint64),
        # 随后是 JSON 格式的元数据, 包含每个张量的 dtype/shape/data_offsets
        header_size = struct.unpack("<Q", f.read(8))[0]
        header = json.loads(f.read(header_size))

    for name, meta in header.items():
        if name == "__metadata__":
            continue
        st_dtype = meta["dtype"]
        dtype_str = _ST_DTYPE_INFO.get(st_dtype, (st_dtype,))[0]
        shape = tuple(meta["shape"])
        numel = 1
        for s in shape:
            numel *= s
        results.append((name, shape, numel, dtype_str, fname))

    return results


def _read_bin_file(
    filepath: str,
) -> List[Tuple[str, Tuple[int, ...], int, str, str]]:
    """读取单个 bin 文件，返回权重信息列表。"""
    import torch

    fname = os.path.basename(filepath)
    results = []
    checkpoint = torch.load(filepath, map_location="cpu", weights_only=True)
    for name, tensor in checkpoint.items():
        if hasattr(tensor, "shape"):
            numel = tensor.numel()
            results.append((name, tuple(tensor.shape), numel, str(tensor.dtype), fname))
    return results


def inspect_weights(
    model_path: str, out, compress: bool = True, num_workers: int = 4
) -> None:
    import torch

    logger.info("[3/3] 扫描权重文件...")
    # 查找权重文件
    safetensor_files = sorted(glob(os.path.join(model_path, "*.safetensors")))
    bin_files = sorted(glob(os.path.join(model_path, "*.bin")))

    if not safetensor_files and not bin_files:
        logger.error(
            "[3/3] 在 `%s` 中未找到权重文件 (.safetensors 或 .bin)", model_path
        )
        print(
            f"**错误**: 在 `{model_path}` 中未找到权重文件 (.safetensors 或 .bin)",
            file=out,
        )
        return

    use_safetensors = bool(safetensor_files)
    weight_files = safetensor_files if use_safetensors else bin_files
    file_type = "safetensors" if use_safetensors else "bin"
    read_fn = _read_safetensor_file if use_safetensors else _read_bin_file

    actual_workers = min(num_workers, len(weight_files))
    logger.info(
        "[3/3] 找到 %d 个 %s 文件，使用 %d 进程并发读取...",
        len(weight_files),
        file_type,
        actual_workers,
    )

    # 多进程并发读取权重文件
    all_weights: List[Tuple[str, Tuple, int, str, str]] = []
    total_params = 0

    with ProcessPoolExecutor(max_workers=actual_workers) as executor:
        futures = {executor.submit(read_fn, fp): fp for fp in weight_files}
        pbar = tqdm(
            total=len(weight_files), desc="读取权重文件", unit="file", file=sys.stderr
        )
        for future in as_completed(futures):
            filepath = futures[future]
            fname = os.path.basename(filepath)
            try:
                results = future.result()
            except Exception as e:
                logger.warning("读取 %s 失败: %s", fname, e)
                pbar.update(1)
                continue
            all_weights.extend(results)
            total_params += sum(r[2] for r in results)
            pbar.update(1)
        pbar.close()

    all_weights.sort(key=lambda x: natural_sort_key(x[0]))

    raw_count = len(all_weights)

    # 输出统计
    total_file_size = sum(os.path.getsize(fp) for fp in weight_files)

    def _element_size(dtype):
        if isinstance(dtype, str) and dtype in _ST_DTYPE_INFO:
            return _ST_DTYPE_INFO[dtype][1]
        if isinstance(dtype, str) and dtype.startswith("torch."):
            dtype = getattr(torch, dtype.replace("torch.", ""))
        return (
            torch.finfo(dtype).bits // 8
            if dtype.is_floating_point
            else torch.iinfo(dtype).bits // 8
        )

    _es_cache: Dict[str, int] = {}
    total_tensor_size = 0
    for _, _, numel, dt, _ in all_weights:
        if dt not in _es_cache:
            _es_cache[dt] = _element_size(dt)
        total_tensor_size += numel * _es_cache[dt]

    print("# 权重统计\n", file=out)
    print(f"- **权重文件**: {len(weight_files)} 个 `{file_type}` 文件", file=out)
    print(f"- **文件总大小**: {_format_bytes(total_file_size)}", file=out)
    print(f"- **权重张量数**: {format_number(len(all_weights))}", file=out)
    print(f"- **参数总量**: {format_number(total_params)}", file=out)
    print(f"- **张量累计大小**: {_format_bytes(total_tensor_size)}", file=out)

    if compress:
        compressed = _compress_weights(all_weights)
        print(
            f"- **压缩**: {raw_count} → {len(compressed)} 行",
            file=out,
        )
        display_weights = compressed
    else:
        display_weights = [
            (name, shape, numel, dtype, fname, "")
            for name, shape, numel, dtype, fname in all_weights
        ]

    print(file=out)

    # 详细权重列表
    print("<details><summary>详细权重列表</summary>\n", file=out)
    print("| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |", file=out)
    print("| --- | --- | --- | --- | --- |", file=out)
    for name, shape, numel, dtype, fname, note in display_weights:
        display_name = f"`{name}`"
        if note:
            display_name += f" ({note})"
        print(
            f"| {display_name} | `{list(shape)}` | `{dtype}` | {format_size(numel, dtype)} | {fname} |",
            file=out,
        )
    print("\n</details>\n", file=out)
    logger.info("[3/3] 权重扫描完成 ✓")


def main():
    parser = argparse.ArgumentParser(description="模型信息查看工具")
    parser.add_argument("--model-path", type=str, required=True, help="模型路径")
    parser.add_argument(
        "--output-file", type=str, default=None, help="输出 Markdown 文件路径（可选）"
    )
    parser.add_argument(
        "--overwrite", "-f", action="store_true", help="覆盖已存在的输出文件"
    )
    parser.add_argument(
        "--no-compress",
        action="store_true",
        help="不压缩 experts/layers 权重行（默认压缩）",
    )
    parser.add_argument(
        "--num-workers",
        type=int,
        default=4,
        help="并发读取权重文件的进程数（默认 8）",
    )
    args = parser.parse_args()

    _setup_logging()

    # 先检查模型路径是否存在
    if not os.path.isdir(args.model_path):
        logger.error("模型路径 '%s' 不存在或不是有效目录", args.model_path)
        sys.exit(1)

    # 确定输出文件路径并检查
    output_file = args.output_file
    if not output_file:
        folder_name = os.path.basename(args.model_path.rstrip("/"))
        output_file = os.path.join(
            "models", folder_name.lower().replace("-", "_") + ".md"
        )

    if os.path.exists(output_file) and not args.overwrite:
        logger.error(
            "输出文件 '%s' 已存在，使用 --overwrite 或 -f 参数覆盖", output_file
        )
        sys.exit(1)

    from io import StringIO

    buf = StringIO()
    out = buf

    print(f"# 模型信息报告\n", file=out)
    print(f"- **模型路径**: `{args.model_path}`\n", file=out)

    inspect_config(args.model_path, out)
    inspect_structure(args.model_path, out)
    inspect_weights(
        args.model_path,
        out,
        compress=not args.no_compress,
        num_workers=args.num_workers,
    )

    content = buf.getvalue()

    # 确保输出目录存在
    output_dir = os.path.dirname(output_file)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"已输出到: {output_file}")


if __name__ == "__main__":
    main()
