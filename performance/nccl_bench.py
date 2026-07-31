#!/usr/bin/env python3
"""
NCCL Communication Performance Benchmark

Follows nccl-tests conventions:
  bandwidth = (data_size / time) * correction_factor
  (归一化后的单向链路带宽,与 rank 数无关,用于对标 NVLink 单向峰值)

Data size definition per op (matches nccl-tests):
  AllReduce    : send buffer size S  (= recv buffer size)
  AllGather    : total output size   = n * per-rank input
  ReduceScatter: total input size    = n * per-rank output
  Broadcast    : message size S
  Reduce       : message size S      (single root receives)
  AllToAll     : total send size     = n * per-peer chunk
  AllToAllv    : total send size     = sum of per-peer chunks (unequal)

correction factors:
  AllReduce    : 2*(n-1)/n
  AllGather    : (n-1)/n
  ReduceScatter: (n-1)/n
  Broadcast    : 1
  Reduce       : 1
  AllToAll     : (n-1)/n
  AllToAllv    : (n-1)/n

Usage:
  Run with torchrun, one process per GPU. nproc_per_node = number of GPUs.

    # All ops, single 512 MB size, 8 GPUs (default dtype=bfloat16)
    torchrun --nproc_per_node=8 performance/nccl_bench.py --size-mb 512

    # Use the env that has PyTorch + NCCL installed
    torchrun \\
        --nproc_per_node=8 performance/nccl_bench.py --size-mb 512

    # Only AllReduce + AllGather, 1 GB, more iterations
    torchrun --nproc_per_node=8 performance/nccl_bench.py \\
        --size-mb 1024 --ops allreduce allgather --iterations 200

    # Multi-node: set --nnodes, --nproc_per_node, and a shared --rdzv endpoint
    # (rank 0 host):  torchrun --nnodes=2 --nproc_per_node=8 --rdzv_backend=c10d \
    #                 --rdzv_endpoint=<rank0_ip>:29500 performance/nccl_bench.py
    # (rank 1 host):  torchrun --nnodes=2 --nproc_per_node=8 --rdzv_backend=c10d \
    #                 --rdzv_endpoint=<rank0_ip>:29500 performance/nccl_bench.py

  Results (one entry per op) are written to --output as JSON. nccl-tests
  environment variables (NCCL_DEBUG, NCCL_NET, etc.) work as usual.

  --ops with "all" runs every op; otherwise pass a subset (allreduce,
  allgather, reducescatter, broadcast, reduce, alltoall, alltoallv).
"""

import argparse
import json
import os
from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple

import torch
import torch.distributed as dist


@dataclass
class BenchmarkResult:
    op_name: str
    data_size_bytes: int  # nccl-tests definition of "data size"
    avg_time_ms: float
    bandwidth_GBps: float  # (data_size / time) * correction_factor
    num_warmup: int
    num_iterations: int

    def __str__(self) -> str:
        return (
            f"{self.op_name:15s} | "
            f"{self.data_size_bytes / 1024**2:8.2f} MB | "
            f"{self.avg_time_ms:8.3f} ms | "
            f"Bandwidth {self.bandwidth_GBps:7.2f} GB/s"
        )


# ---------------------------------------------------------------------------
# correction factors (nccl-tests formula)
# ---------------------------------------------------------------------------


def correction_factor(op_name: str, n: int) -> float:
    if op_name == "AllReduce":
        return 2.0 * (n - 1) / n
    elif op_name in ("AllGather", "ReduceScatter", "AllToAll", "AllToAllv"):
        return (n - 1) / n
    elif op_name in ("Broadcast", "Reduce"):
        return 1.0
    return 1.0


# ---------------------------------------------------------------------------
# Core benchmark runner
# ---------------------------------------------------------------------------


class NcclBenchmark:

    def __init__(self, backend: str = "nccl"):
        self.backend = backend
        self.rank = -1
        self.world_size = -1
        self.device = None
        self._initialized = False

    def init_distributed(self):
        if self._initialized:
            return
        if "RANK" not in os.environ or "WORLD_SIZE" not in os.environ:
            raise RuntimeError("Run with torchrun: torchrun --nproc_per_node=N nccl.py")
        self.rank = int(os.environ["RANK"])
        self.world_size = int(os.environ["WORLD_SIZE"])
        local_rank = int(os.environ.get("LOCAL_RANK", 0))
        self.device = torch.device(f"cuda:{local_rank}")
        torch.cuda.set_device(self.device)
        if not dist.is_initialized():
            dist.init_process_group(backend=self.backend)
        self._initialized = True
        print(f"[Rank {self.rank}] device={self.device}, world_size={self.world_size}")

    def cleanup(self):
        if dist.is_initialized():
            dist.destroy_process_group()

    def _time_op(
        self, op_func: Callable, num_warmup: int, num_iterations: int
    ) -> float:
        """Return average time in ms using CUDA Events, with cross-rank synchronization."""
        for _ in range(num_warmup):
            op_func()
        # Sync all ranks after warmup so timing starts cleanly
        dist.barrier()
        torch.cuda.synchronize()

        start = torch.cuda.Event(enable_timing=True)
        end = torch.cuda.Event(enable_timing=True)
        start.record()
        for _ in range(num_iterations):
            op_func()
        end.record()
        torch.cuda.synchronize()
        # Barrier ensures all ranks finish before rank 0 reads the result
        dist.barrier()
        return start.elapsed_time(end) / num_iterations

    def _make_result(
        self,
        op_name: str,
        data_size_bytes: int,
        avg_time_ms: float,
        num_warmup: int,
        num_iterations: int,
    ) -> BenchmarkResult:
        # bandwidth: GB/s using 1e9 bytes per GB (matches nccl-tests)
        raw_bw = (data_size_bytes / 1e9) / (avg_time_ms / 1e3)
        bandwidth = raw_bw * correction_factor(op_name, self.world_size)
        return BenchmarkResult(
            op_name=op_name,
            data_size_bytes=data_size_bytes,
            avg_time_ms=avg_time_ms,
            bandwidth_GBps=bandwidth,
            num_warmup=num_warmup,
            num_iterations=num_iterations,
        )

    # ------------------------------------------------------------------
    # Per-op benchmarks — data_size follows nccl-tests convention
    # ------------------------------------------------------------------

    def bench_allreduce(
        self, count: int, dtype: torch.dtype, num_warmup: int, num_iters: int
    ) -> BenchmarkResult:
        """data_size = send buffer = count * itemsize"""
        t = torch.randn(count, dtype=dtype, device=self.device)
        avg_ms = self._time_op(
            lambda: dist.all_reduce(t, op=dist.ReduceOp.SUM), num_warmup, num_iters
        )
        return self._make_result("AllReduce", t.nbytes, avg_ms, num_warmup, num_iters)

    def bench_allgather(
        self, count: int, dtype: torch.dtype, num_warmup: int, num_iters: int
    ) -> BenchmarkResult:
        """data_size = total output = n * per-rank input; count = per-rank elements"""
        n = self.world_size
        inp = torch.randn(count, dtype=dtype, device=self.device)
        out = torch.empty(count * n, dtype=dtype, device=self.device)
        avg_ms = self._time_op(
            lambda: dist.all_gather_into_tensor(out, inp), num_warmup, num_iters
        )
        return self._make_result("AllGather", out.nbytes, avg_ms, num_warmup, num_iters)

    def bench_reducescatter(
        self, count: int, dtype: torch.dtype, num_warmup: int, num_iters: int
    ) -> BenchmarkResult:
        """data_size = total input = n * per-rank output; count = per-rank elements"""
        n = self.world_size
        inp = torch.randn(count * n, dtype=dtype, device=self.device)
        out = torch.empty(count, dtype=dtype, device=self.device)
        avg_ms = self._time_op(
            lambda: dist.reduce_scatter_tensor(out, inp), num_warmup, num_iters
        )
        return self._make_result(
            "ReduceScatter", inp.nbytes, avg_ms, num_warmup, num_iters
        )

    def bench_broadcast(
        self, count: int, dtype: torch.dtype, num_warmup: int, num_iters: int
    ) -> BenchmarkResult:
        """data_size = message size = count * itemsize"""
        t = torch.randn(count, dtype=dtype, device=self.device)
        avg_ms = self._time_op(lambda: dist.broadcast(t, src=0), num_warmup, num_iters)
        return self._make_result("Broadcast", t.nbytes, avg_ms, num_warmup, num_iters)

    def bench_reduce(
        self, count: int, dtype: torch.dtype, num_warmup: int, num_iters: int
    ) -> BenchmarkResult:
        """data_size = message size = count * itemsize (single root receives)"""
        t = torch.randn(count, dtype=dtype, device=self.device)
        avg_ms = self._time_op(
            lambda: dist.reduce(t, dst=0, op=dist.ReduceOp.SUM), num_warmup, num_iters
        )
        return self._make_result("Reduce", t.nbytes, avg_ms, num_warmup, num_iters)

    def bench_alltoall(
        self, count: int, dtype: torch.dtype, num_warmup: int, num_iters: int
    ) -> BenchmarkResult:
        """data_size = total send = n * per-peer chunk; count = per-rank total elements"""
        n = self.world_size
        # Round down to a multiple of n so each rank sends equal chunks
        aligned = max((count // n) * n, n)
        inp = torch.randn(aligned, dtype=dtype, device=self.device)
        out = torch.empty(aligned, dtype=dtype, device=self.device)
        avg_ms = self._time_op(
            lambda: dist.all_to_all_single(out, inp), num_warmup, num_iters
        )
        return self._make_result("AllToAll", inp.nbytes, avg_ms, num_warmup, num_iters)

    def bench_alltoallv(
        self, count: int, dtype: torch.dtype, num_warmup: int, num_iters: int
    ) -> BenchmarkResult:
        """Variable-length all-to-all. data_size = total send = sum of per-peer chunks.

        Build a consistent send matrix M[r][i] = elements rank r sends to rank i.
        Rank r's input_split_sizes  = row r of M.
        Rank i's output_split_sizes = column i of M (what it receives from each rank).
        Using M[r][i] = base + ((r + i) % n) * unit yields unequal per-peer chunks
        while keeping every rank's total send == total recv (a permutation of one multiset).
        """
        n = self.world_size
        # unit chosen so sum(send_splits) = unit * n*(n+1)/2 ≈ count,
        # keeping AllToAllv data_size on the same scale as the other ops.
        unit = max(count // (n * (n + 1) // 2), 1)
        r = self.rank
        send_splits = [unit + ((r + i) % n) * unit for i in range(n)]
        recv_splits = [unit + ((src + r) % n) * unit for src in range(n)]

        inp = torch.randn(sum(send_splits), dtype=dtype, device=self.device)
        out = torch.empty(sum(recv_splits), dtype=dtype, device=self.device)
        avg_ms = self._time_op(
            lambda: dist.all_to_all_single(
                out, inp, output_split_sizes=recv_splits, input_split_sizes=send_splits
            ),
            num_warmup,
            num_iters,
        )
        return self._make_result("AllToAllv", inp.nbytes, avg_ms, num_warmup, num_iters)

    # ------------------------------------------------------------------
    # Full benchmark sweep
    # ------------------------------------------------------------------

    def run(
        self,
        counts: List[int],
        dtype: torch.dtype = torch.bfloat16,
        num_warmup: int = 10,
        num_iters: int = 100,
        ops: List[str] = None,
    ) -> Dict[str, List[BenchmarkResult]]:

        op_registry: List[Tuple[str, Callable]] = [
            ("AllReduce", self.bench_allreduce),
            ("AllGather", self.bench_allgather),
            ("ReduceScatter", self.bench_reducescatter),
            ("Broadcast", self.bench_broadcast),
            ("Reduce", self.bench_reduce),
            ("AllToAll", self.bench_alltoall),
            ("AllToAllv", self.bench_alltoallv),
        ]
        if ops and "all" not in ops:
            op_registry = [(n, f) for n, f in op_registry if n.lower() in ops]

        results: Dict[str, List[BenchmarkResult]] = {n: [] for n, _ in op_registry}

        def log(msg):
            if self.rank == 0:
                print(msg)

        log("\n" + "=" * 95)
        log(
            f"  NCCL Benchmark  |  world_size={self.world_size}  |  dtype={dtype}  |  "
            f"warmup={num_warmup}  iters={num_iters}"
        )
        log("=" * 95)
        log("字段说明:")
        log(
            "  Bandwidth = (data_size / 耗时) × 校正因子   归一化后的单向链路带宽,与 rank 数无关"
        )
        log(
            "  注:单向口径,可以直接对比 NVLink 单向速度，例如H200 nv18 单向速度是450GB/s "
        )
        log("")
        log(
            f"{'Op':15s} | {'DataSize(MB)':>12s} | {'Time(ms)':>10s} | "
            f"{'Bandwidth(GB/s)':>15s}"
        )
        log("-" * 60)

        for count in counts:
            for op_name, bench_fn in op_registry:
                # Barrier before each op to prevent cross-op timing contamination
                dist.barrier()
                r = bench_fn(count, dtype, num_warmup, num_iters)
                results[op_name].append(r)
                log(
                    f"{r.op_name:15s} | {r.data_size_bytes / 1024**2:12.2f} | "
                    f"{r.avg_time_ms:10.3f} | {r.bandwidth_GBps:15.2f}"
                )
            log("-" * 60)

        log("Benchmark complete.\n")
        return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="NCCL benchmark (nccl-tests conventions)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
examples:
  # All ops, 512 MB, 8 GPUs (default dtype=bfloat16)
  torchrun --nproc_per_node=8 performance/nccl_bench.py --size-mb 512

  # Use the env with PyTorch + NCCL
  torchrun --nproc_per_node=8 performance/nccl_bench.py --size-mb 512

  # Only AllReduce + AllGather, 1 GB, more iterations
  torchrun --nproc_per_node=8 performance/nccl_bench.py \\
      --size-mb 1024 --ops allreduce allgather --iterations 200
""",
    )
    parser.add_argument(
        "--size-mb",
        type=float,
        default=1024.0,
        help="Single data size in MB to benchmark (no size sweep).",
    )
    parser.add_argument("--warmup", type=int, default=10)
    parser.add_argument("--iterations", type=int, default=100)
    parser.add_argument(
        "--dtype",
        default="bfloat16",
        choices=["float16", "bfloat16", "float32", "float64"],
    )
    parser.add_argument(
        "--ops",
        nargs="+",
        default=["all"],
        choices=[
            "all",
            "allreduce",
            "allgather",
            "reducescatter",
            "broadcast",
            "reduce",
            "alltoall",
            "alltoallv",
        ],
    )
    parser.add_argument("--output", default="nccl_benchmark_results.json")
    args = parser.parse_args()

    dtype = {
        "float16": torch.float16,
        "bfloat16": torch.bfloat16,
        "float32": torch.float32,
        "float64": torch.float64,
    }[args.dtype]
    itemsize = torch.tensor([], dtype=dtype).element_size()

    counts = [int(args.size_mb * 1024**2 / itemsize)]

    bench = NcclBenchmark()
    bench.init_distributed()

    try:
        if bench.rank == 0:
            gpu = torch.cuda.get_device_name(0)
            # Display the per-rank input size (AllGather/ReduceScatter data_size will be n× larger)
            sizes_mb = [f"{c * itemsize / 1024**2:.2f}MB" for c in counts]
            print(f"\nGPU: {gpu} x {bench.world_size}")
            print(f"Per-rank input sizes: {sizes_mb}")

        results = bench.run(
            counts=counts,
            dtype=dtype,
            num_warmup=args.warmup,
            num_iters=args.iterations,
            ops=args.ops,
        )

        if bench.rank == 0:
            json_out = {}
            for op, rs in results.items():
                json_out[op] = [
                    {
                        "data_size_MB": r.data_size_bytes / 1024**2,
                        "avg_time_ms": r.avg_time_ms,
                        "bandwidth_GBps": r.bandwidth_GBps,
                    }
                    for r in rs
                ]
            with open(args.output, "w") as f:
                json.dump(json_out, f, indent=2)
            print(f"Results saved to {args.output}")
    finally:
        bench.cleanup()


if __name__ == "__main__":
    main()
