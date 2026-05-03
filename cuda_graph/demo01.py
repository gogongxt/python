import torch
import time

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 参数设置 (增加迭代次数以更好地观察性能)
num_iterations = 100
num_operations = 1000  # 相当于减少了这个数值对应到的kernel launch气泡时间
vector_size = 1024

# 创建唯一的原始输入数据
original_vectors = [
    torch.randn(vector_size, device=device) for _ in range(num_operations)
]
scalars = torch.randn(num_operations, device=device)

# --- 预热 ---
warmup_vectors = [v.clone() for v in original_vectors]
warmup_outputs = [torch.empty_like(v) for v in original_vectors]
for _ in range(3):
    for i in range(num_operations):
        warmup_outputs[i] = warmup_vectors[i] * scalars[i]
if torch.cuda.is_available():
    torch.cuda.synchronize()

# --- 1. 传统方式 ---
# 为传统方法创建独立的输入和输出列表
vectors_trad_input = [v.clone() for v in original_vectors]
vectors_trad_output = [torch.empty_like(v) for v in original_vectors]

start_time = time.time()
for _ in range(num_iterations):
    for i in range(num_operations):
        # 每次都从原始输入进行计算，将结果写入输出列表
        # 这确保了每次迭代的工作都与Graph的replay相同
        vectors_trad_output[i] = vectors_trad_input[i] * scalars[i]

if torch.cuda.is_available():
    torch.cuda.synchronize()
elapsed_no_graph = (time.time() - start_time) * 1000
print(f"传统方式: {elapsed_no_graph:.2f} ms")

# 保存传统方式结果作为参考
reference = vectors_trad_output

# --- 2. 使用CUDA Graph方式  ---
graph = torch.cuda.CUDAGraph()

# 静态输入和输出
static_inputs = [v.clone() for v in original_vectors]
static_outputs = [torch.empty_like(v) for v in vectors_trad_input]

# 捕获阶段
with torch.cuda.graph(graph):
    for i in range(num_operations):
        static_outputs[i] = static_inputs[i] * scalars[i]

# 执行阶段
start_time = time.time()
for _ in range(num_iterations):
    graph.replay()

if torch.cuda.is_available():
    torch.cuda.synchronize()
elapsed_with_graph = (time.time() - start_time) * 1000
print(f"使用CUDA Graph: {elapsed_with_graph:.2f} ms")

# 计算加速比
if elapsed_with_graph > 0:
    speedup = elapsed_no_graph / elapsed_with_graph
    print(f"加速比: {speedup:.2f}x")
else:
    print("CUDA Graph 执行时间过短，无法计算加速比。")

# 比较结果
all_close = all(
    torch.allclose(ref, out, atol=1e-6) for ref, out in zip(reference, static_outputs)
)
print("结果一致性检查:", all_close)

# 如果不一致，打印差异
if not all_close:
    print("\n发现不一致，打印第一个差异项：")
    for i, (ref, out) in enumerate(zip(reference, static_outputs)):
        if not torch.allclose(ref, out, atol=1e-6):
            print(f"操作 {i} 差异:")
            print("  参考 (传统方式):", ref[:5])
            print("  输出 (Graph):   ", out[:5])
            print("  最大绝对差异:   ", torch.abs(ref - out).max().item())
            break
