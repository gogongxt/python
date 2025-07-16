import torch

# ['cudagraphs', 'inductor', 'onnxrt', 'openxla', 'tvm']
print(torch.compiler.list_backends())


# ===============================
# test1
# ===============================
def foo1(x, y):
    a = torch.sin(x)
    b = torch.cos(y)
    return a + b


opt_foo1 = torch.compile(foo1)
print(opt_foo1(torch.randn(10, 10), torch.randn(10, 10)))


# ===============================
# test2
# ===============================
@torch.compile
def foo2(x, y):
    a = torch.sin(x)
    b = torch.cos(y)
    return a + b


print(foo2(torch.randn(10, 10), torch.randn(10, 10)))


# ===============================
# test3
# ===============================
t = torch.randn(10, 100)


class MyModule(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.lin = torch.nn.Linear(100, 10)

    def forward(self, x):
        return torch.nn.functional.relu(self.lin(x))


mod = MyModule()
mod.compile()
print(mod(t))
## or:
# opt_mod = torch.compile(mod)
# print(opt_mod(t))
