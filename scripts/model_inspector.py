#!/usr/bin/env python3
"""
模型信息查看工具 - 查看 LLM 模型配置和权重信息
"""

import argparse
import os
import re
import sys
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


def format_size(numel: int, dtype: torch.dtype) -> str:
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


def inspect_weights(model_path: str, out) -> None:
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

    print(
        f"[3/3] 找到 {len(weight_files)} 个 {file_type} 文件，开始读取...",
        file=sys.stderr,
    )

    # 扫描权重
    all_weights: List[Tuple[str, Tuple, int, torch.dtype, str]] = []
    total_params = 0

    file_pbar = tqdm(
        weight_files,
        desc="读取权重文件",
        unit="file",
        file=sys.stderr,
    )
    for filepath in file_pbar:
        fname = os.path.basename(filepath)
        file_pbar.set_postfix_str(fname)
        if use_safetensors:
            with safe_open(filepath, "pt", "cpu") as f:
                keys = list(f.keys())
                tensor_pbar = tqdm(
                    keys,
                    desc=f"  张量",
                    unit="tensor",
                    file=sys.stderr,
                    leave=False,
                )
                for name in tensor_pbar:
                    tensor = f.get_tensor(name)
                    numel = tensor.numel()
                    all_weights.append((name, tensor.shape, numel, tensor.dtype, fname))
                    total_params += numel
                    tensor_pbar.set_postfix_str(
                        f"已扫描 {format_number(total_params)} 参数"
                    )
                tensor_pbar.close()
        else:
            checkpoint = torch.load(filepath, map_location="cpu", weights_only=True)
            items = [(n, t) for n, t in checkpoint.items() if hasattr(t, "shape")]
            tensor_pbar = tqdm(
                items,
                desc=f"  张量",
                unit="tensor",
                file=sys.stderr,
                leave=False,
            )
            for name, tensor in tensor_pbar:
                numel = tensor.numel()
                all_weights.append((name, tensor.shape, numel, tensor.dtype, fname))
                total_params += numel
                tensor_pbar.set_postfix_str(
                    f"已扫描 {format_number(total_params)} 参数"
                )
            tensor_pbar.close()
    file_pbar.close()

    all_weights.sort(key=lambda x: natural_sort_key(x[0]))

    # 输出统计
    print("# 权重统计\n", file=out)
    print(f"- **权重文件**: {len(weight_files)} 个 `{file_type}` 文件", file=out)
    print(f"- **权重张量数**: {len(all_weights)}", file=out)
    print(f"- **参数总量**: {format_number(total_params)}", file=out)
    print(file=out)

    # 详细权重列表
    print("<details><summary>详细权重列表</summary>\n", file=out)
    print("| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |", file=out)
    print("| --- | --- | --- | --- | --- |", file=out)
    for name, shape, numel, dtype, fname in all_weights:
        print(
            f"| `{name}` | `{list(shape)}` | `{dtype}` | {format_size(numel, dtype)} | {fname} |",
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
    inspect_weights(args.model_path, out)

    content = buf.getvalue()

    if args.output_file:
        with open(args.output_file, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"已输出到: {args.output_file}")
    else:
        print(content)


if __name__ == "__main__":
    main()
