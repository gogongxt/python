import torch
import torch.nn as nn
import torch._dynamo as dynamo
import torch._inductor.config as inductor_config
import os

# 打印 PyTorch 版本
print(f"PyTorch Version: {torch.__version__}")
print("-" * 30)


# 1. 定义一个包含可融合操作序列的简单模型
# 这个模型执行: y = relu(x * w + b)
# 这是一个非常常见的模式，包含乘法、加法和激活函数，是融合的绝佳候选者。
class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x, w, b):
        y = torch.mul(x, w)  # 操作1: 乘法
        z = torch.add(y, b)  # 操作2: 加法
        o = torch.relu(z)  # 操作3: ReLU激活
        return o


# 检查是否有可用的 GPU
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")
print("-" * 30)


# 创建模型实例和一些用于演示的张量
model = SimpleModel().to(device)
x = torch.randn(16, device=device)
w = torch.randn(16, device=device)
b = torch.randn(16, device=device)


# =================================================================
# 步骤 2: 打印融合前的计算图
# =================================================================
print("--- 1. 融合前的计算图 (Graph Before Fusion) ---")
print("使用 torch._dynamo.explain() 来捕获原始模型的 FX Graph...")

# --- 代码修正处 ---
explanation_before = dynamo.explain(model)(x, w, b)

print("\n[捕获到的计算图详情]")
print(explanation_before)


# =================================================================
# 步骤 3: 使用 torch.compile 编译模型
# =================================================================
print("\n" + "-" * 30)
print("--- 2. 使用 torch.compile 编译模型 ---")
# 'inductor' 是 PyTorch 2.0 的默认后端，它负责代码生成和优化（包括融合）
compiled_model = torch.compile(
    model,
    backend="inductor",
)
print("模型已成功编译。")
# 注意：真正的编译发生在第一次运行模型时 (JIT - Just-In-Time)
print("正在首次运行编译后的模型以触发 JIT 编译...")
output = compiled_model(x, w, b)
print("首次运行完成。")


# =================================================================
# 步骤 4: 打印融合后的计算图
# =================================================================
print("\n" + "-" * 30)
print("--- 3. 融合后的计算图 (Graph After Fusion) ---")
print("再次使用 torch._dynamo.explain() 来查看编译后模型的图...")

# --- 代码修正处 ---
# 同样，这里也直接接收 ExplainOutput 对象
explanation_after = dynamo.explain(compiled_model)(x, w, b)

print("\n[编译和融合后的计算图详情]")
# 直接打印 explanation 对象
print(explanation_after)

print("\n" + "-" * 30)
print("--- 结果分析 ---")
