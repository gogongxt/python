#!/usr/bin/env python3
"""
模型信息查看工具 - 查看 LLM 模型配置和权重信息
"""

import argparse
import os
import re
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from glob import glob
from typing import Dict, List, Optional, Tuple

import torch
from safetensors import safe_open
from tqdm import tqdm
from transformers import AutoConfig, AutoModel


def natural_sort_key(s: str) -> List:
    return [
        int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", s)
    ]


def format_number(num: int) -> str:
    return f"{num:,}"


def format_size(numel: int, dtype) -> str:
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


def inspect_structure(model_path: str, out) -> None:
    print("[2/3] 解析模型结构...", file=sys.stderr)
    config = AutoConfig.from_pretrained(model_path)
    with torch.device("meta"):
        model = AutoModel.from_config(config)
    total_params = sum(p.numel() for p in model.parameters())
    print("# 模型结构\n", file=out)
    print(f"- **模型类**: `{type(model).__name__}`", file=out)
    print(f"- **参数总量**: {format_number(total_params)}\n", file=out)
    print("```\n" + str(model) + "\n```\n", file=out)
    print("[2/3] 模型结构解析完成 ✓", file=sys.stderr)


def inspect_config(model_path: str, out) -> None:
    print("[1/3] 读取模型配置...", file=sys.stderr)
    config = AutoConfig.from_pretrained(model_path)
    print("# 模型配置\n", file=out)
    print(f"- **模型类型**: `{type(config).__name__}`", file=out)
    print(f"- **数据类型**: `{getattr(config, 'dtype', 'float16')}`", file=out)
    print(f"- **隐藏层大小**: {getattr(config, 'hidden_size', 'N/A')}", file=out)
    print(f"- **层数**: {getattr(config, 'num_hidden_layers', 'N/A')}", file=out)
    print(
        f"- **注意力头数**: {getattr(config, 'num_attention_heads', 'N/A')}", file=out
    )
    print(f"- **词表大小**: {getattr(config, 'vocab_size', 'N/A')}", file=out)
    print(f"- **中间层大小**: {getattr(config, 'intermediate_size', 'N/A')}", file=out)
    print(file=out)
    print("<details><summary>完整配置</summary>\n", file=out)
    print(f"```\n{config}\n```\n", file=out)
    print("</details>\n", file=out)
    print("[1/3] 模型配置读取完成 ✓", file=sys.stderr)


# Patterns for grouping: (compiled regex, template for merged name)
_EXPERT_RE = re.compile(r"^(.+experts\.)(\d+)(\..+)$")
_LAYER_RE = re.compile(r"^(.+layers\.)(\d+)(\..+)$")


def _compress_weights(
    all_weights: List[Tuple[str, Tuple, int, str, str]],
) -> List[Tuple[str, Tuple, int, str, str, str]]:
    """Compress weight list by merging identical experts and layers.

    Returns list of (display_name, shape, numel, dtype, fname, note).
    """
    # First pass: group experts within each layer
    # Key: (prefix, suffix) -> list of (expert_idx, weight_info)
    expert_groups: Dict[
        Tuple[str, str], List[Tuple[int, Tuple, int, str, str]]
    ] = {}
    non_expert: List[Tuple[str, Tuple, int, str, str]] = []

    for name, shape, numel, dtype, fname in all_weights:
        m = _EXPERT_RE.match(name)
        if m:
            prefix, idx_str, suffix = m.group(1), m.group(2), m.group(3)
            expert_groups.setdefault((prefix, suffix), []).append(
                (int(idx_str), shape, numel, dtype, fname)
            )
        else:
            non_expert.append((name, shape, numel, dtype, fname))

    # Merge expert groups where all experts share same shape+dtype
    merged_experts: List[Tuple[str, Tuple, int, str, str, str]] = []
    for (prefix, suffix), items in expert_groups.items():
        items.sort(key=lambda x: x[0])
        # Check if all share same shape and dtype
        first_shape, first_dtype = items[0][1], items[0][3]
        if all(s == first_shape and d == first_dtype for _, s, _, d, _ in items):
            indices = [x[0] for x in items]
            range_str = (
                str(indices[0]) if len(indices) == 1 else f"{indices[0]}-{indices[-1]}"
            )
            merged_name = f"{prefix}{range_str}{suffix}"
            single_numel = items[0][2]
            total_numel = single_numel * len(indices)
            note = f"×{len(indices)} experts"
            # Use fname from first item
            fnames = {x[4] for x in items}
            fname = "Multi Files" if len(fnames) > 1 else items[0][4]
            merged_experts.append(
                (merged_name, first_shape, total_numel, first_dtype, fname, note)
            )
        else:
            # Not uniform — emit each individually
            for idx, shape, numel, dtype, fname in items:
                orig_name = f"{prefix}{idx}{suffix}"
                merged_experts.append((orig_name, shape, numel, dtype, fname, ""))

    # Combine with non-expert weights and sort by original name logic
    combined: List[Tuple[str, Tuple, int, str, str, str]] = []
    for name, shape, numel, dtype, fname in non_expert:
        combined.append((name, shape, numel, dtype, fname, ""))
    combined.extend(merged_experts)
    combined.sort(key=lambda x: natural_sort_key(x[0]))

    # Second pass: group layers
    layer_groups: Dict[
        Tuple[str, str], List[Tuple[int, Tuple, int, str, str, str]]
    ] = {}
    non_layer: List[Tuple[str, Tuple, int, str, str, str]] = []

    for item in combined:
        name = item[0]
        m = _LAYER_RE.match(name)
        if m:
            prefix, idx_str, suffix = m.group(1), m.group(2), m.group(3)
            layer_groups.setdefault((prefix, suffix), []).append(
                (int(idx_str), *item[1:])
            )
        else:
            non_layer.append(item)

    result: List[Tuple[str, Tuple, int, str, str, str]] = []
    for (prefix, suffix), items in layer_groups.items():
        items.sort(key=lambda x: x[0])
        # Check uniformity: shape, dtype, and note must match
        first_shape, first_dtype, first_note = items[0][1], items[0][3], items[0][5]
        uniform = all(
            s == first_shape and d == first_dtype and n == first_note
            for _, s, _, d, _, n in items
        )
        if uniform:
            indices = [x[0] for x in items]
            range_str = (
                str(indices[0]) if len(indices) == 1 else f"{indices[0]}-{indices[-1]}"
            )
            merged_name = f"{prefix}{range_str}{suffix}"
            single_numel = items[0][2]
            total_numel = single_numel * len(indices)
            layer_note = f"×{len(indices)} layers"
            if first_note:
                note = f"{first_note}, {layer_note}"
            else:
                note = layer_note
            fnames = {x[4] for x in items}
            fname = "Multi Files" if len(fnames) > 1 else items[0][4]
            result.append(
                (merged_name, first_shape, total_numel, first_dtype, fname, note)
            )
        else:
            for idx, shape, numel, dtype, fname, note in items:
                orig_name = f"{prefix}{idx}{suffix}"
                result.append((orig_name, shape, numel, dtype, fname, note))

    # Re-add non-layer items
    result.extend(non_layer)
    result.sort(key=lambda x: natural_sort_key(x[0]))
    return result


def _read_safetensor_file(
    filepath: str,
) -> List[Tuple[str, Tuple[int, ...], int, str, str]]:
    """读取单个 safetensors 文件，返回权重信息列表。"""
    fname = os.path.basename(filepath)
    results = []
    with safe_open(filepath, "pt", "cpu") as f:
        for name in f.keys():
            tensor = f.get_tensor(name)
            numel = tensor.numel()
            results.append((name, tuple(tensor.shape), numel, str(tensor.dtype), fname))
    return results


def _read_bin_file(
    filepath: str,
) -> List[Tuple[str, Tuple[int, ...], int, str, str]]:
    """读取单个 bin 文件，返回权重信息列表。"""
    fname = os.path.basename(filepath)
    results = []
    checkpoint = torch.load(filepath, map_location="cpu", weights_only=True)
    for name, tensor in checkpoint.items():
        if hasattr(tensor, "shape"):
            numel = tensor.numel()
            results.append((name, tuple(tensor.shape), numel, str(tensor.dtype), fname))
    return results


def inspect_weights(
    model_path: str, out, compress: bool = True, num_workers: int = 16
) -> None:
    print("[3/3] 扫描权重文件...", file=sys.stderr)
    # 查找权重文件
    safetensor_files = sorted(glob(os.path.join(model_path, "*.safetensors")))
    bin_files = sorted(glob(os.path.join(model_path, "*.bin")))

    if not safetensor_files and not bin_files:
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
    print(
        f"[3/3] 找到 {len(weight_files)} 个 {file_type} 文件，"
        f"使用 {actual_workers} 进程并发读取...",
        file=sys.stderr,
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
                print(f"读取 {fname} 失败: {e}", file=sys.stderr)
                pbar.update(1)
                continue
            all_weights.extend(results)
            total_params += sum(r[2] for r in results)
            pbar.update(1)
        pbar.close()

    all_weights.sort(key=lambda x: natural_sort_key(x[0]))

    raw_count = len(all_weights)

    # 输出统计
    print("# 权重统计\n", file=out)
    print(f"- **权重文件**: {len(weight_files)} 个 `{file_type}` 文件", file=out)
    print(f"- **权重张量数**: {format_number(len(all_weights))}", file=out)
    print(f"- **参数总量**: {format_number(total_params)}", file=out)

    if compress:
        compressed = _compress_weights(all_weights)
        print(
            f"- **压缩**: {raw_count} → {len(compressed)} 行 (合并相同 shape/dtype 的 experts 和 layers)",
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
    print("[3/3] 权重扫描完成 ✓", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="模型信息查看工具")
    parser.add_argument("--model-path", type=str, required=True, help="模型路径")
    parser.add_argument(
        "--output-file", type=str, default=None, help="输出 Markdown 文件路径（可选）"
    )
    parser.add_argument(
        "--no-compress",
        action="store_true",
        help="不压缩 experts/layers 权重行（默认压缩）",
    )
    parser.add_argument(
        "--num-workers",
        type=int,
        default=16,
        help="并发读取权重文件的进程数（默认 8）",
    )
    args = parser.parse_args()

    if os.path.exists(args.model_path) and not os.path.isdir(args.model_path):
        print(f"错误：'{args.model_path}' 不是有效的目录", file=sys.stderr)
        sys.exit(1)

    from io import StringIO

    buf = StringIO()
    out = buf

    print(f"# 模型信息报告\n", file=out)
    print(f"- **模型路径**: `{args.model_path}`\n", file=out)

    inspect_config(args.model_path, out)
    inspect_structure(args.model_path, out)
    inspect_weights(args.model_path, out, compress=not args.no_compress, num_workers=args.num_workers)

    content = buf.getvalue()

    if args.output_file:
        with open(args.output_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"已输出到: {args.output_file}")
    else:
        print(content)


if __name__ == "__main__":
    main()
