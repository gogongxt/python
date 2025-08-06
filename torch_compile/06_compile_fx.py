import torch
import torch.nn as nn
from torch.fx import GraphModule

# 1. 同样使用这个简单模型
class SimpleModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = nn.Linear(10, 20)
        self.relu = nn.ReLU()

    def forward(self, x):
        # torch.compile可以直接处理张量输出，无需元组
        return self.relu(self.linear(x))

# 2. 定义一个自定义 backend 函数
#    它接收一个 fx.GraphModule 和 example_inputs
def print_graph_backend(graph_module: GraphModule, example_inputs: list):
    print("\n--- Graph from Custom Backend ---")
    graph_module.print_tabular()
    
    # 为了让编译后的模型能够实际运行，我们需要返回一个可执行的函数。
    # 这里我们直接返回原始图的可执行版本。
    # 对于实际的后端，这里会返回一个优化后图的可执行版本。
    from torch._functorch.aot_autograd import aot_module_simplified
    return aot_module_simplified(
        graph_module,
        example_inputs,
    )

# 3. 准备模型和输入
model = SimpleModel().eval()
example_inputs = [torch.randn(4, 10)]

# 4. 调用 torch.compile 并传入自定义 backend
print("\nCompiling with custom backend...")
compiled_model = torch.compile(model, backend=print_graph_backend)
print("Compilation complete.")

# 5. 运行编译后的函数
print("\nRunning the compiled function...")
compiled_model(*example_inputs)
print("Run complete.")
