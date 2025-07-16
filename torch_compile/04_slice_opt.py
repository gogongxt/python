import torch
import torch.fx as fx
import operator


def move_slicing_before_matmul(gm: fx.GraphModule):
    """
    此函数实现了一个迭代的 PyTorch FX 图优化过程。
    它会反复寻找 `matmul` 操作后紧跟 `getitem` (slicing) 的模式，
    并将切片操作尽可能地向上移动到 `matmul` 计算链的最前端。

    例如，它会将:
        y = torch.matmul(w, x)
        z = torch.matmul(y, v)
        output = z[:10]
    优化为:
        sliced_w = w[:10]
        y = torch.matmul(sliced_w, x)
        z = torch.matmul(y, v)
        output = z

    这种迭代优化可以显著减少中间计算的张量大小，从而提升效率。
    """
    graph = gm.graph

    # 使用一个 while 循环来反复应用优化，直到图中不再发生任何变化。
    # 这种方法被称为“不动点”算法。
    while True:
        changed_in_pass = False
        # 迭代图的节点副本，因为我们会在循环中修改图结构
        for node in list(graph.nodes):
            # 节点可能在之前的迭代中已被删除
            if node not in graph.nodes:
                continue

            # --- 模式匹配 ---
            # 寻找 getitem(matmul(...)) 模式
            if (
                node.op == "call_function"
                and node.target == operator.getitem
                and len(node.args) == 2
                and isinstance(node.args[1], slice)
            ):
                matmul_node = node.args[0]
                if (
                    isinstance(matmul_node, fx.Node)
                    and matmul_node.op == "call_function"
                    and matmul_node.target == torch.matmul
                ):
                    print(
                        f"\n找到模式：在 matmul 节点 '{matmul_node.name}' 后有切片节点 '{node.name}'。应用优化。"
                    )

                    # --- 图变换 ---
                    lhs, rhs = matmul_node.args
                    slice_obj = node.args[1]

                    with graph.inserting_before(matmul_node):
                        # 1. 创建新的 getitem 节点，对 matmul 的第一个输入进行切片
                        sliced_lhs = graph.call_function(
                            operator.getitem, (lhs, slice_obj)
                        )
                        # 2. 创建新的 matmul 节点，使用切片后的输入
                        new_matmul = graph.call_function(
                            torch.matmul, (sliced_lhs, rhs)
                        )

                    # 将原始切片节点的所有使用者，输入全部替换为新的 matmul 节点的输出
                    node.replace_all_uses_with(new_matmul)

                    # 删除旧的、无用的节点
                    graph.erase_node(node)
                    graph.erase_node(matmul_node)

                    # 标记在这一轮中图已发生改变，并中断内部循环
                    # 以便从头开始重新扫描整个图
                    changed_in_pass = True
                    break

        # 如果在一整轮扫描后图没有发生任何变化，则优化完成，退出循环
        if not changed_in_pass:
            break

    # --- 完成 ---
    graph.lint()
    gm.recompile()

    return gm


# 注册我们的自定义后端
from torch._dynamo import register_backend


@register_backend
def slice_optimizer(gm: fx.GraphModule, example_inputs):
    print("\n--- 进入自定义后端: slice_optimizer ---")
    print("--- 优化前的图 ---")
    gm.graph.print_tabular()

    transformed_gm = move_slicing_before_matmul(gm)

    print("\n--- 优化后的图 ---")
    transformed_gm.graph.print_tabular()
    transformed_gm.print_readable()
    print("--- 退出自定义后端 ---")
    # return transformed_gm
    print("--- 使用inductor后端再进行优化 ---")
    inductor_backend = torch._dynamo.lookup_backend("inductor")
    return inductor_backend(transformed_gm, example_inputs)


# --------------------------------------------------------------------------
# 性能基准测试
# --------------------------------------------------------------------------
import time
import numpy as np


def test_function_complex(w, x, v, u, s):
    """一个更长的 matmul 链，以凸显优化效果"""
    y = torch.matmul(w, x)
    z = torch.matmul(y, v)
    a = torch.matmul(z, u)
    b = torch.matmul(a, s)
    return b[:16]


def run_benchmark():
    """
    运行基准测试，比较三种模式的性能：
    1. 原始 Eager 模式
    2. 普通 torch.compile 模式
    3. 自定义优化后的模式
    """
    print("\n\n" + "=" * 60)
    print("场景: 性能基准测试 (4层 matmul 链)")
    print("=" * 60)

    # --- 1. 设置测试参数和输入数据 ---
    WARMUP_RUNS = 2
    N_RUNS = 10

    w = torch.randn(400, 300)
    x = torch.randn(300, 400)
    v = torch.randn(400, 500)
    u = torch.randn(500, 300)
    s = torch.randn(300, 400)

    inputs = [w, x, v, u, s]

    # --- 2. 测试未优化的 Eager 模式性能 ---
    print("\n--- 正在测试未优化的 Eager 模式性能 ---")
    eager_times = []
    for _ in range(WARMUP_RUNS):
        _ = test_function_complex(*inputs)

    for _ in range(N_RUNS):
        start_time = time.perf_counter()
        _ = test_function_complex(*inputs)
        end_time = time.perf_counter()
        eager_times.append((end_time - start_time) * 1000)

    avg_eager_time = np.mean(eager_times)
    print(f"Eager 模式运行 {N_RUNS} 次，平均时间: {avg_eager_time:.4f} ms")

    # --- 3. 测试普通 torch.compile 模式性能 ---
    print("\n--- 正在测试普通 torch.compile 模式性能 ---")
    default_optimized_fn = torch.compile(test_function_complex, backend="inductor")

    default_optimized_times = []
    for _ in range(WARMUP_RUNS):
        _ = default_optimized_fn(*inputs)

    for _ in range(N_RUNS):
        start_time = time.perf_counter()
        _ = default_optimized_fn(*inputs)
        end_time = time.perf_counter()
        default_optimized_times.append((end_time - start_time) * 1000)

    avg_default_optimized_time = np.mean(default_optimized_times)
    print(
        f"普通编译模式运行 {N_RUNS} 次，平均时间: {avg_default_optimized_time:.4f} ms"
    )

    # --- 4. 测试自定义优化后的函数性能 ---
    print("\n--- 正在测试自定义优化后的模式性能 ---")
    custom_optimized_fn = torch.compile(
        test_function_complex, backend="slice_optimizer"
    )

    custom_optimized_times = []
    for _ in range(WARMUP_RUNS):
        _ = custom_optimized_fn(*inputs)

    for _ in range(N_RUNS):
        start_time = time.perf_counter()
        _ = custom_optimized_fn(*inputs)
        end_time = time.perf_counter()
        custom_optimized_times.append((end_time - start_time) * 1000)

    avg_custom_optimized_time = np.mean(custom_optimized_times)
    print(
        f"自定义优化模式运行 {N_RUNS} 次，平均时间: {avg_custom_optimized_time:.4f} ms"
    )

    # --- 5. 验证结果并报告性能 ---
    print("\n--- 验证结果一致性 ---")
    original_result = test_function_complex(*inputs)
    default_result = default_optimized_fn(*inputs)
    custom_result = custom_optimized_fn(*inputs)

    # print(f"{original_result=}")
    # print(f"{default_result=}")
    # print(f"{custom_result=}")
    assert torch.allclose(original_result, default_result), "普通编译结果验证失败！"
    assert torch.allclose(
        original_result, custom_result, rtol=1e-2, atol=1e-2
    ), "自定义优化结果验证失败！"
    print("✅ 所有结果验证成功！")

    print("\n--- 性能对比 ---")
    print(f"Eager 模式平均时间: {avg_eager_time:.4f} ms")
    print(f"普通编译模式平均时间: {avg_default_optimized_time:.4f} ms")
    print(f"自定义优化模式平均时间: {avg_custom_optimized_time:.4f} ms")

    default_speedup = avg_eager_time / avg_default_optimized_time
    custom_speedup = avg_eager_time / avg_custom_optimized_time
    print(f"\n🚀 普通编译性能提升: {default_speedup:.2f} 倍")
    print(f"🚀 自定义优化性能提升: {custom_speedup:.2f} 倍")


if __name__ == "__main__":
    run_benchmark()
