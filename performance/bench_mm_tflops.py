#!/usr/bin/env python3
"""
Matrix-multiply (GEMM) peak-TFLOPS benchmark for NVIDIA Blackwell GPUs (sm_120, e.g. RTX 6000D)
and Ascend 910C NPUs. Backend is auto-detected: if torch_npu is importable and reports an
available NPU the script runs on NPU, otherwise on CUDA.

Measures dense tensor-core GEMM throughput as INDEPENDENT tests — one per dtype/format, each
with its own operator, its own data prep and its own shape sweep:

  * bf16          -> torch.matmul               (cuBLAS bf16 / CANN bf16 tensor cores)
  * fp16          -> torch.matmul               (cuBLAS fp16 / CANN fp16 tensor cores)
  * fp8  e4m3     -> torch._scaled_mm           (cuBLASLt 2nd-gen FP8 path, fp16 accumulate)
                  — CUDA only; RESERVED on NPU (no torch._scaled_mm there)
  * int8          -> torch._int_mm              (cuBLASLt int8 IMMA tensor cores, int32 accumulate)
                  or torch_npu.npu_quant_matmul (910C int8 tensor cores: int8 x int8, one fp32
                    scale per output column, dequant to bf16 output). Counted FLOPs use the
                    same 2*M*N*K formula, so for int8 the figure is technically integer TOPS
                    reported in the same unit as the float cases.
  * nvfp4 e2m1    -> torch._scaled_mm           (cuBLASLt NVFP4 block-scaled FP4 tensor cores:
                  packed float4_e2m1fn_x2 operands + e4m3 block scales, 1 scale per 16 K-elems,
                  K-blocks padded to x4 and rows to x128 — the swizzled 128x4 layout, flat).
                  Needs CUDA >= 12.8 on Blackwell. Plain tensorwise/rowwise scales are rejected
                  with "Invalid scaling configuration" — that is an argument-shape issue, not a
                  missing kernel. CUDA only; RESERVED on NPU.
  * mxfp4 e2m1    -> RESERVED (not measured). torch already has the recipe
                  (F.scaled_mm + ScalingType.BlockWise1x32 + e8m0 scales, 1 scale per 32
                  K-elems) but cuBLASLt ships MXFP4 kernels for B200/B300 only — on SM120 it
                  raises NotImplementedError. Implement by mirroring case_nvfp4 once mature.

bf16 and fp16 are deliberately TWO SEPARATE benchmarks, not one shared "half-precision" case:
same operator, but each dtype exercises its own tensor-core path and may pick different kernels/shapes,
so each is built, swept and reported on its own. fp4 likewise comes in two formats — nvfp4 (e4m3
scales, 16-elem blocks) and mxfp4 (e8m0 scales, 32-elem blocks) — kept as separate cases. Use
--dtype to run just one.

Geometry: M=N=K is swept over several shapes and the BEST result is kept for each dtype, since
BF16/FP16 like a mid square (~4096^3) while FP8/INT8 like a "tall" shape on this class of card.

Memory safety on partially-occupied devices (e.g. an NPU whose HBM is ~90% held by a running
service): each shape is skipped unless it fits in MEM_BUDGET_FRAC of the device's *free* memory
per mem_get_info, and the allocator cache is emptied between shapes so nothing accumulates.

TFLOPS = 2*M*N*K / time  (dense, no sparsity).

Usage:
    CUDA_VISIBLE_DEVICES=0 python bench_mm_tflops.py
    ASCEND_RT_VISIBLE_DEVICES=0 python bench_mm_tflops.py              # Ascend NPU
    python bench_mm_tflops.py --dtype bf16                             # only the bf16 test
    python bench_mm_tflops.py --dtype fp16,int8 --iters 20             # fp16 + int8 only
"""

import argparse
import textwrap

import torch

try:  # registers the NPU backend; its presence selects the NPU code path
    import torch_npu  # noqa: F401
    _NPU = torch.npu.is_available()
except ImportError:
    torch_npu = None
    _NPU = False

DEV = "npu" if _NPU else "cuda"

# A shape only runs if its worst-case resident bytes fit in this fraction of free device memory.
# The estimate below double-counts on purpose (fp32 randn() intermediate + converted operand all
# treated as live at once), so the guard errs on the safe side.
MEM_BUDGET_FRAC = 0.5


def devapi():
    return torch.npu if _NPU else torch.cuda


def shape_bytes(M, N, K):
    # Worst case across dtypes: half-precision operands each need a fp32 intermediate + the
    # converted copy, plus the output.
    return (M * K + K * N) * 6 + M * N * 2


# Shapes swept per dtype. Large square + "tall" GEMMs; whichever saturates tensor cores wins.
SHAPES = [
    (4096, 4096, 4096),
    (8192, 8192, 8192),
    (8192, 4096, 8192),
    (16384, 8192, 8192),
    (8192, 2048, 8192),
    (16384, 4096, 16384),
]


def time_shape(fn, M, N, K, warmup, iters):
    api = devapi()
    for _ in range(warmup):
        fn()
    api.synchronize()
    s = api.Event(enable_timing=True)
    e = api.Event(enable_timing=True)
    ts = []
    for _ in range(iters):
        s.record()
        fn()
        e.record()
        api.synchronize()
        ts.append(s.elapsed_time(e))
    ts.sort()
    best_s = ts[0] * 1e-3
    return (2.0 * M * N * K) / best_s / 1e12


# --- Independent test 1: bf16 dense GEMM (tensor cores) -----------------------------------
def case_bf16():
    op = "torch.matmul"

    def prepare(M, N, K):
        a = torch.randn(M, K, device=DEV, dtype=torch.float32).to(torch.bfloat16)
        b = torch.randn(K, N, device=DEV, dtype=torch.float32).to(torch.bfloat16)
        return lambda: a @ b

    return op, prepare, None


# --- Independent test 2: fp16 dense GEMM (tensor cores) -----------------------------------
def case_fp16():
    op = "torch.matmul"

    def prepare(M, N, K):
        a = torch.randn(M, K, device=DEV, dtype=torch.float32).to(torch.float16)
        b = torch.randn(K, N, device=DEV, dtype=torch.float32).to(torch.float16)
        return lambda: a @ b

    return op, prepare, None


# --- fp8 e4m3 dense GEMM (cuBLASLt 2nd-gen FP8 path, fp16 accumulate) — CUDA only ----------
def case_fp8():
    op = "torch._scaled_mm"
    if _NPU:
        return op, None, "cuBLASLt FP8 path: torch._scaled_mm is CUDA-only; no FP8 GEMM recipe probed on NPU."

    def prepare(M, N, K):
        a = torch.randn(M, K, device=DEV, dtype=torch.float32).to(torch.float8_e4m3fn)
        b0 = torch.randn(K, N, device=DEV, dtype=torch.float32).to(torch.float8_e4m3fn)
        b = b0.t().contiguous().t()  # fp8 scaled_mm wants stride(0)==1
        sa = torch.ones(M, 1, device=DEV, dtype=torch.float32) * 0.1
        sb = torch.ones(1, N, device=DEV, dtype=torch.float32) * 0.1
        return lambda: torch._scaled_mm(a, b, sa, sb, out_dtype=torch.float16)

    return op, prepare, None


# --- int8 dense GEMM (int8 tensor cores, int32 accumulate) --------------------------------
def case_int8():
    if _NPU:
        # Verified 910C recipe: a (M,K) int8 @ b (K,N) int8 on int8 tensor cores, ONE fp32 scale
        # per OUTPUT COLUMN — scale shape is (N,), not (K,) and not (1,N): square-matrix probes
        # can't distinguish those, rectangular ones reject everything but (N,). The dequant
        # output comes via output_dtype=torch.bfloat16 (matches a float reference to bf16
        # rounding, ~0.3% max rel err).
        op = "torch_npu.npu_quant_matmul"

        def prepare(M, N, K):
            a = torch.randint(-128, 127, (M, K), device=DEV, dtype=torch.int8)
            b = torch.randint(-128, 127, (K, N), device=DEV, dtype=torch.int8)
            s = torch.ones(N, device=DEV, dtype=torch.float32) * 0.01
            return lambda: torch_npu.npu_quant_matmul(a, b, s, output_dtype=torch.bfloat16)

        return op, prepare, None

    op = "torch._int_mm"

    def prepare(M, N, K):
        a = torch.randint(-128, 127, (M, K), device=DEV, dtype=torch.int8)
        b = torch.randint(-128, 127, (K, N), device=DEV, dtype=torch.int8)
        return lambda: torch._int_mm(a, b)

    return op, prepare, None


# --- nvfp4 e2m1 GEMM (cuBLASLt block-scaled FP4, e4m3 scales, 16-elem blocks) — CUDA only --
def case_nvfp4():
    op = "torch._scaled_mm(nvfp4)"
    if _NPU:
        return op, None, "cuBLASLt NVFP4 block-scaled path: CUDA-only operator."

    # NVFP4 recipe cuBLASLt expects: a/b packed float4_e2m1fn_x2 (2 fp4 per byte, so
    # the packed K is K//2), scales e4m3 with 1 scale per 16 *unpacked* K-elements,
    # K-blocks padded to a multiple of 4 and rows padded to 128 (the swizzled 128x4
    # layout, passed as a flat contiguous tensor). K must be divisible by 16.

    def sf_numel(rows, K):
        kb = (K + 15) // 16
        kb = (kb + 3) // 4 * 4
        return 128 * ((rows + 127) // 128) * kb

    def prepare(M, N, K):
        pk = K // 2  # packed columns: 2 fp4 per byte
        a = torch.randint(0, 256, (M, pk), device=DEV, dtype=torch.uint8).view(
            torch.float4_e2m1fn_x2)
        b0 = torch.randint(0, 256, (N, pk), device=DEV, dtype=torch.uint8).view(
            torch.float4_e2m1fn_x2)
        b = b0.t()  # (pk, N) column-major, as _scaled_mm wants
        sa = torch.ones(sf_numel(M, K), device=DEV, dtype=torch.float32).to(
            torch.float8_e4m3fn)
        sb = torch.ones(sf_numel(N, K), device=DEV, dtype=torch.float32).to(
            torch.float8_e4m3fn)
        return lambda: torch._scaled_mm(a, b, sa, sb, out_dtype=torch.bfloat16)

    return op, prepare, None


# --- mxfp4 e2m1 GEMM (e8m0 scales, 32-elem blocks) — RESERVED, see docstring ---------------
def case_mxfp4():
    # Not implemented on purpose for now: torch 2.11 exposes the recipe via
    # F.scaled_mm(mat_a, mat_b, sa, ScalingType.BlockWise1x32, sb, ScalingType.BlockWise1x32,
    # swizzle_a/b=SwizzleType.SWIZZLE_32_4_4) with e8m0 scales, but cuBLASLt only ships MXFP4
    # kernels for B200/B300 — on SM120 (this class of GPU) it raises
    # "NotImplementedError: MXFP4 scaling only supported in CUDA for B200/B300".
    # When support matures: mirror case_nvfp4, swapping e4m3->e8m0 scales and block 16->32.
    op = "torch._scaled_mm(mxfp4)"
    note = ("torch API has the recipe (F.scaled_mm BlockWise1x32 + e8m0 scales), but cuBLASLt "
            "ships MXFP4 kernels for B200/B300 only; likewise not available on NPU. Enable "
            "once support matures.")
    return op, None, note


# One self-contained benchmark per dtype/format; bf16/fp16 and nvfp4/mxfp4 are each
# intentionally separate entries.
CASES = {
    "bf16": case_bf16,
    "fp16": case_fp16,
    "fp8": case_fp8,
    "int8": case_int8,
    "nvfp4": case_nvfp4,
    "mxfp4": case_mxfp4,
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--warmup", type=int, default=8)
    ap.add_argument("--iters", type=int, default=20)
    ap.add_argument("--dtype", default="all",
                    help=f"comma-separated tests to run: {', '.join(CASES)}, or 'all' (default)")
    args = ap.parse_args()

    if args.dtype.strip().lower() == "all":
        selected = list(CASES)
    else:
        selected = [d.strip().lower() for d in args.dtype.split(",") if d.strip()]
        unknown = [d for d in selected if d not in CASES]
        if unknown:
            ap.error(f"unknown dtype(s) {unknown}; choices: {', '.join(CASES)} or 'all'")

    api = devapi()
    free_b, total_b = api.mem_get_info(0)
    budget = free_b * MEM_BUDGET_FRAC

    print("=" * 78)
    print("GEMM peak-TFLOPS benchmark")
    if _NPU:
        print(f"NPU    : {torch.npu.get_device_name(0)}  (torch_npu {torch_npu.__version__}, "
              f"{total_b / 2**30:.0f}GB HBM, {free_b / 2**30:.1f}GB free)")
        print(f"torch  : {torch.__version__}")
    else:
        prop = torch.cuda.get_device_properties(0)
        cap = (prop.major, prop.minor)
        print(f"GPU    : {torch.cuda.get_device_name(0)}  (SM {cap[0]}.{cap[1]}, "
              f"{prop.multi_processor_count} SMs, {prop.L2_cache_size // (1024**2)}MB L2, "
              f"{free_b / 2**30:.1f}GB free)")
        print(f"torch  : {torch.__version__}   cuda={torch.version.cuda}")
    print(f"tests  : {' '.join(selected)}   warmup={args.warmup}  iters={args.iters}   "
          f"shape budget: {budget / 2**30:.1f}GB")
    print("=" * 78)
    print(f"{'dtype':7}{'operator':26}{'best shape':>18}{'meas TF':>10}")
    print("-" * 78)

    for dtype in selected:
        op, prepare, note = CASES[dtype]()
        if prepare is None:  # reserved case: recipe known, kernels/ops not on this backend
            print(f"{dtype:<7}{op:<26}{'—':>18}{'RESERVED':>10}")
            print(textwrap.fill(note, width=78, initial_indent=" " * 14,
                                subsequent_indent=" " * 14))
            continue
        best_tf, best_shape = -1.0, None
        last_err = None
        skipped = []
        for M, N, K in SHAPES:
            need = shape_bytes(M, N, K)
            if need > budget:
                skipped.append(f"{M}x{N}x{K} (~{need / 2**30:.1f}GB > {budget / 2**30:.1f}GB)")
                continue
            fn = None
            try:
                fn = prepare(M, N, K)
                tf = time_shape(fn, M, N, K, args.warmup, args.iters)
                if tf > best_tf:
                    best_tf, best_shape = tf, (M, N, K)
            except Exception as e:
                last_err = e
            finally:
                fn = None  # drop this shape's operands before the next (small-HBM devices)
                api.empty_cache()

        if best_shape is None:
            print(f"{dtype:<7}{op:<26}{'—':>18}{'FAILED':>10}")
            if last_err is not None:
                print(f"            ({type(last_err).__name__}: {str(last_err)[:80]})")
            continue
        print(f"{dtype:<7}{op:<26}{str(best_shape):>18}{best_tf:>10.1f}")
        if skipped:
            print(f"            (skipped {', '.join(skipped)})")

    print("-" * 78)
    print("measured = best kernel time across swept shapes (dense, no sparsity).")


if __name__ == "__main__":
    main()
