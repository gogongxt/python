#!/usr/bin/env python3
"""
NCCL Communication Performance Benchmark

Follows nccl-tests conventions:
  algbw  = data_size / time          (application throughput)
  busbw  = algbw * correction_factor (hardware link utilization)

Data size definition per op (matches nccl-tests):
  AllReduce    : send buffer size S  (= recv buffer size)
  AllGather    : total output size   = n * per-rank input
  ReduceScatter: total input size    = n * per-rank output
  Broadcast    : message size S
  AllToAll     : total send size     = n * per-peer chunk

busbw correction factors:
  AllReduce    : 2*(n-1)/n
  AllGather    : (n-1)/n
  ReduceScatter: (n-1)/n
  Broadcast    : 1
  AllToAll     : (n-1)/n
"""

import argparse
import json
import os
from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple

import numpy as np
import torch
import torch.distributed as dist


@dataclass
class BenchmarkResult:
    op_name: str
    data_size_bytes: int  # nccl-tests definition of "data size"
    avg_time_ms: float
    algbw_GBps: float  # data_size / time
    busbw_GBps: float  # algbw * correction factor
    num_warmup: int
    num_iterations: int

    def __str__(self) -> str:
        return (
            f"{self.op_name:15s} | "
            f"{self.data_size_bytes / 1024**2:8.2f} MB | "
            f"{self.avg_time_ms:8.3f} ms | "
            f"algbw {self.algbw_GBps:7.2f} GB/s | "
            f"busbw {self.busbw_GBps:7.2f} GB/s"
        )


# ---------------------------------------------------------------------------
# busbw correction factors (nccl-tests formula)
# ---------------------------------------------------------------------------


def busbw_factor(op_name: str, n: int) -> float:
    if op_name == "AllReduce":
        return 2.0 * (n - 1) / n
    elif op_name in ("AllGather", "ReduceScatter", "AllToAll"):
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
        # algbw: GB/s using 1e9 bytes per GB (matches nccl-tests)
        algbw = (data_size_bytes / 1e9) / (avg_time_ms / 1e3)
        busbw = algbw * busbw_factor(op_name, self.world_size)
        return BenchmarkResult(
            op_name=op_name,
            data_size_bytes=data_size_bytes,
            avg_time_ms=avg_time_ms,
            algbw_GBps=algbw,
            busbw_GBps=busbw,
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
            ("AllToAll", self.bench_alltoall),
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
        log(
            f"{'Op':15s} | {'DataSize(MB)':>12s} | {'Time(ms)':>10s} | "
            f"{'algbw(GB/s)':>12s} | {'busbw(GB/s)':>12s}"
        )
        log("-" * 70)

        for count in counts:
            for op_name, bench_fn in op_registry:
                # Barrier before each op to prevent cross-op timing contamination
                dist.barrier()
                r = bench_fn(count, dtype, num_warmup, num_iters)
                results[op_name].append(r)
                log(
                    f"{r.op_name:15s} | {r.data_size_bytes / 1024**2:12.2f} | "
                    f"{r.avg_time_ms:10.3f} | {r.algbw_GBps:12.2f} | {r.busbw_GBps:12.2f}"
                )
            log("-" * 70)

        log("Benchmark complete.\n")
        return results


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="NCCL benchmark (nccl-tests conventions)"
    )
    parser.add_argument("--min-size-mb", type=float, default=1.0)
    parser.add_argument("--max-size-mb", type=float, default=512.0)
    parser.add_argument("--num-sizes", type=int, default=10)
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
            "alltoall",
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

    min_count = int(args.min_size_mb * 1024**2 / itemsize)
    max_count = int(args.max_size_mb * 1024**2 / itemsize)
    counts = [
        int(x)
        for x in np.logspace(np.log10(min_count), np.log10(max_count), args.num_sizes)
    ]

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
                        "algbw_GBps": r.algbw_GBps,
                        "busbw_GBps": r.busbw_GBps,
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
