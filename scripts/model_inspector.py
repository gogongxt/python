#!/usr/bin/env python3
"""
统一的模型信息查看工具
整合了模型配置查看和权重查看功能，模型只加载一次
"""

import argparse
import os
import re
import sys
from contextlib import contextmanager
from glob import glob
from typing import Any, Dict, List, Optional, Tuple

from safetensors import safe_open
from tabulate import tabulate
from tqdm import tqdm
from transformers import AutoConfig, AutoModel

# Workaround for older transformers versions that don't have PytorchGELUTanh
try:
    from transformers.activations import PytorchGELUTanh
except ImportError:
    from transformers import activations

    try:
        from transformers.activations import GELUTanh

        activations.PytorchGELUTanh = GELUTanh
    except ImportError:
        # If GELUTanh doesn't exist either, create a dummy class
        import torch.nn as nn

        class PytorchGELUTanh(nn.Module):
            def forward(self, x):
                return x * torch.sigmoid(1.702 * x)

        activations.PytorchGELUTanh = PytorchGELUTanh


@contextmanager
def output_manager(output_file: Optional[str] = None):
    """管理输出目标：文件或终端"""
    if output_file:
        original_stdout = sys.stdout
        with open(output_file, "w", encoding="utf-8") as f:
            sys.stdout = f
            yield
        sys.stdout = original_stdout
        print(f"信息已输出到文件: {output_file}")
    else:
        yield


def natural_sort_key(s: str) -> List:
    """
    自然排序键函数，将字符串中的数字部分转换为整数进行比较
    例如：'model.layers.10' -> ['model.layers.', 10]
    """
    return [
        int(text) if text.isdigit() else text.lower() for text in re.split(r"(\d+)", s)
    ]


def format_number(num: int) -> str:
    """格式化大数字，添加逗号分隔符"""
    return f"{num:,}"


def format_size(shape: Tuple[int, ...], dtype: str = "float16") -> str:
    """
    计算并格式化参数大小
    """
    # 支持更多数据类型
    if dtype == "float32":
        element_size = 4
    elif dtype in ["float16", "bfloat16", "fp16", "bf16"]:
        element_size = 2
    elif dtype == "int8":
        element_size = 1
    elif dtype == "int4":
        element_size = 0.5
    else:
        element_size = 2  # 默认假设为16位
    total_elements = 1
    for dim in shape:
        total_elements *= dim
    size_mb = (total_elements * element_size) / (1024 * 1024)

    if size_mb < 1024:
        return f"{size_mb:.2f} MB"
    else:
        return f"{size_mb / 1024:.2f} GB"


def print_model_config(model_path: str) -> bool:
    """打印模型配置信息"""
    print("\n" + "=" * 80)
    print("📋 模型配置信息")
    print("=" * 80)

    try:
        config = AutoConfig.from_pretrained(model_path)
        print(f"✅ 配置加载成功")
        print(f"\n模型类型: {type(config).__name__}")
        print(f"\n详细配置:")
        print("-" * 40)
        print(config)
        return True
    except Exception as e:
        print(f"❌ 加载配置失败: {e}")
        return False


def print_model_structure(model_path: str) -> bool:
    """打印模型结构和参数统计"""
    print("\n" + "=" * 80)
    print("🏗️  模型结构信息")
    print("=" * 80)

    try:
        # 获取配置以读取dtype
        config = AutoConfig.from_pretrained(model_path)
        model_dtype = getattr(config, "dtype", "float16")

        model = AutoModel.from_pretrained(model_path)
        print(f"✅ 模型加载成功")
        print(f"\n模型类型: {type(model).__name__}")
        print(f"数据类型: {model_dtype}")
        print(f"\n模型结构:")
        print("-" * 40)
        print(model)

        # 参数统计
        total_params = sum(p.numel() for p in model.parameters())
        trainable_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
        frozen_params = total_params - trainable_params

        print(f"\n📊 参数统计:")
        print("-" * 40)
        print(f"总参数量:     {format_number(total_params)}")
        print(
            f"可训练参数:   {format_number(trainable_params)} ({trainable_params/total_params*100:.1f}%)"
        )
        print(
            f"冻结参数:     {format_number(frozen_params)} ({frozen_params/total_params*100:.1f}%)"
        )

        # 根据配置中的dtype计算实际大小
        element_size = (
            4
            if model_dtype == "float32"
            else 2 if model_dtype in ["float16", "bfloat16"] else 1
        )
        model_size_gb = total_params * element_size / (1024**3)
        print(f"实际大小({model_dtype}): {model_size_gb:.2f} GB")

        return True, model, model_dtype
    except Exception as e:
        print(f"❌ 加载模型失败: {e}")
        return False, None, None


def print_model_weights(model_path: str) -> bool:
    """打印模型权重信息"""
    print("\n" + "=" * 80)
    print("⚖️  模型权重信息")
    print("=" * 80)

    # 查找权重文件
    files = list(glob(os.path.join(model_path, "*.safetensors")))
    bin_files = list(glob(os.path.join(model_path, "*.bin")))

    if not files and not bin_files:
        print(f"❌ 在 {model_path} 中未找到权重文件 (.safetensors 或 .bin)")
        return False

    # 优先使用 safetensors
    if files:
        weight_files = files
        file_type = "safetensors"
    else:
        weight_files = bin_files
        file_type = "bin"

    print(f"📁 找到 {len(weight_files)} 个 {file_type} 文件")

    # 收集所有权重信息
    all_weights = []
    total_size = 0

    print("\n🔍 扫描权重文件...")
    for file in tqdm(weight_files, desc="文件"):
        try:
            if file_type == "safetensors":
                with safe_open(file, "pt", "cpu") as f:
                    for weight_name in f.keys():
                        tensor = f.get_tensor(weight_name)
                        shape = tensor.shape
                        dtype = str(tensor.dtype)
                        size = tensor.numel()
                        all_weights.append(
                            (weight_name, shape, size, dtype, os.path.basename(file))
                        )
                        total_size += size
            else:  # bin files
                import torch

                checkpoint = torch.load(file, map_location="cpu")
                for weight_name, tensor in checkpoint.items():
                    if hasattr(tensor, "shape"):
                        shape = tensor.shape
                        dtype = str(tensor.dtype)
                        size = tensor.numel()
                        all_weights.append(
                            (weight_name, shape, size, dtype, os.path.basename(file))
                        )
                        total_size += size
        except Exception as e:
            print(f"⚠️  跳过文件 {file}: {e}")
            continue

    if not all_weights:
        print("❌ 未找到有效权重")
        return False

    # 排序权重
    all_weights.sort(key=lambda x: natural_sort_key(x[0]))

    print(f"\n📈 权重统计:")
    print("-" * 40)
    print(f"权重总数:     {len(all_weights)}")
    print(f"参数总数:     {format_number(total_size)}")
    print(f"模型总大小:   {format_size((total_size,))}")

    # 按层分析
    layer_stats = {}
    for weight_name, shape, size, dtype, file_name in all_weights:
        # 提取层名（例如：model.layers.0.self.query.weight -> model.layers.0）
        parts = weight_name.split(".")
        if len(parts) >= 3 and parts[1].isdigit():
            layer_name = f"{parts[0]}.{parts[1]}"
        else:
            layer_name = parts[0] if len(parts) == 1 else ".".join(parts[:2])

        if layer_name not in layer_stats:
            layer_stats[layer_name] = {"count": 0, "params": 0}
        layer_stats[layer_name]["count"] += 1
        layer_stats[layer_name]["params"] += size

    # 显示详细权重列表
    print(f"\n📝 详细权重列表:")
    print("-" * 80)

    # 准备表格数据
    table_data = []
    for weight_name, shape, size, dtype, file_name in all_weights:
        table_data.append(
            [weight_name, str(shape), dtype, format_size((size,), dtype), file_name]
        )

    # 使用 tabulate 打印表格
    headers = ["权重名称", "形状", "类型", "大小", "文件"]
    print(tabulate(table_data, headers=headers, tablefmt="psql"))

    return True


def main():
    parser = argparse.ArgumentParser(
        description="统一的模型信息查看工具 - 查看模型配置、结构和权重信息",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  %(prog)s --model-path /path/to/model                    # 显示所有信息
  %(prog)s --model-path /path/to/model --output-file info.txt  # 输出到文件
        """,
    )

    parser.add_argument(
        "--model-path",
        type=str,
        required=True,
        help="模型路径（本地路径或HuggingFace模型名称）",
    )

    parser.add_argument(
        "--output-file",
        type=str,
        default=None,
        help="输出文件路径（可选，默认输出到终端）",
    )

    args = parser.parse_args()

    # 验证路径
    if os.path.exists(args.model_path):
        # 本地路径，检查是否存在
        if not os.path.isdir(args.model_path):
            print(f"❌ 错误：路径 '{args.model_path}' 不是有效的目录")
            sys.exit(1)

    with output_manager(args.output_file):
        print(f"🤖 模型信息查看工具")
        print(f"📍 模型路径: {args.model_path}")
        print(
            f"🕒 查看时间: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        success = True

        # 显示所有信息
        # 1. 配置信息
        config_success = print_model_config(args.model_path)

        # 2. 模型结构
        structure_success, model, model_dtype = print_model_structure(args.model_path)

        # 3. 权重信息
        if structure_success:
            weight_success = print_model_weights(args.model_path)
            success = config_success and structure_success and weight_success
        else:
            success = config_success and structure_success

        if success:
            print(f"\n✅ 信息查看完成！")
        else:
            print(f"\n❌ 信息查看失败！")
            sys.exit(1)


if __name__ == "__main__":
    main()