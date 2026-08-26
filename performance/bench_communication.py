#!/usr/bin/env python3
"""
torch.distributed Communication Performance Benchmark

Backend-agnostic: this benchmarks the torch.distributed collective interfaces
(all_reduce / all_gather / reduce_scatter / broadcast / reduce / all_to_all).
The actual communication backend is whatever torch.distributed uses on this
machine — nccl on NVIDIA CUDA, hccl on Ascend NPU, gloo on CPU — auto-detected
from the device type, or forced with --backend.

Metric conventions follow nccl-tests (the measurement standard, independent of
which backend runs underneath):
  bandwidth = (data_size / time) * correction_factor
  (normalized one-way link bandwidth, independent of rank count, comparable
  to the one-way peak of the interconnect, e.g. NVLink/HCCS)

Data size definition per op (matches nccl-tests):
  AllReduce    : send buffer size S  (= recv buffer size)
  AllGather    : total output size   = n * per-rank input
  ReduceScatter: total input size    = n * per-rank output
  Broadcast    : message size S
  Reduce       : message size S      (single root receives)
  AllToAll     : total send size     = n * per-peer chunk
  AllToAllv    : total send size     = sum of per-peer chunks (unequal)

correction factors (nccl-tests formula):
  AllReduce    : 2*(n-1)/n
  AllGather    : (n-1)/n
  ReduceScatter: (n-1)/n
  Broadcast    : 1
  Reduce       : 1
  AllToAll     : (n-1)/n
  AllToAllv    : (n-1)/n

Usage:
  Run with torchrun, one process per device. nproc_per_node = number of devices.

    # All ops, single 512 MB size, 8 devices (default dtype=bfloat16)
    torchrun --nproc_per_node=8 performance/bench_communication.py --size-mb 512

    # Only AllReduce + AllGather, 1 GB, more iterations
    torchrun --nproc_per_node=8 performance/bench_communication.py \\
        --size-mb 1024 --ops allreduce allgather --iterations 200

    # Force a specific torch.distributed backend (default: auto — nccl/hccl/gloo
    # by detected device type)
    torchrun --nproc_per_node=8 performance/bench_communication.py --backend nccl

    # Multi-node: set --nnodes, --nproc_per_node, and a shared --rdzv endpoint
    # (rank 0 host):  torchrun --nnodes=2 --nproc_per_node=8 --rdzv_backend=c10d \\
    #                 --rdzv_endpoint=<rank0_ip>:29500 performance/bench_communication.py
    # (rank 1 host):  torchrun --nnodes=2 --nproc_per_node=8 --rdzv_backend=c10d \\
    #                 --rdzv_endpoint=<rank0_ip>:29500 performance/bench_communication.py

  Results print to the terminal (rank 0). Backend-specific environment
  variables work as usual (NCCL_* for nccl, HCCL_* for hccl).

  --ops with "all" runs every op; otherwise pass a subset (allreduce,
  allgather, reducescatter, broadcast, reduce, alltoall, alltoallv).
"""

import argparse
import os
import time
from dataclasses import dataclass
from typing import Callable, Dict, List, Tuple

import torch
import torch.distributed as dist

# device type -> default torch.distributed backend on that device
DEFAULT_BACKEND = {"cuda": "nccl", "npu": "hccl", "cpu": "gloo"}


def detect_device_type() -> str:
    """cuda > npu > cpu, so the script runs unchanged on NVIDIA or Ascend."""
    if torch.cuda.is_available():
        return "cuda"
    npu = getattr(torch, "npu", None)
    if npu is not None:
        try:
            if npu.is_available():
                return "npu"
        except Exception:
            pass
    return "cpu"


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


class CommBenchmark:

    def __init__(self, backend: str = None):
        self.backend = backend  # None -> auto from detected device type
        self.device_type = detect_device_type()
        self.rank = -1
        self.world_size = -1
        self.device = None
        self._initialized = False

    @property
    def accel(self):
        """torch.cuda / torch.npu handle (set_device/Event/synchronize); None on cpu."""
        return getattr(torch, self.device_type, None) if self.device_type != "cpu" else None

    def init_distributed(self):
        if self._initialized:
            return
        if "RANK" not in os.environ or "WORLD_SIZE" not in os.environ:
            raise RuntimeError(
                "Run with torchrun: torchrun --nproc_per_node=N "
                "performance/bench_communication.py"
            )
        self.rank = int(os.environ["RANK"])
        self.world_size = int(os.environ["WORLD_SIZE"])
        local_rank = int(os.environ.get("LOCAL_RANK", 0))
        if self.device_type == "cpu":
            self.device = torch.device("cpu")
        else:
            self.device = torch.device(f"{self.device_type}:{local_rank}")
            self.accel.set_device(self.device)
        if self.backend is None:
            self.backend = DEFAULT_BACKEND[self.device_type]
        if not dist.is_initialized():
            dist.init_process_group(backend=self.backend)
        self._initialized = True
        print(f"[Rank {self.rank}] device={self.device}, backend={self.backend}, "
              f"world_size={self.world_size}")

    def cleanup(self):
        if dist.is_initialized():
            dist.destroy_process_group()

    def _time_op(
        self, op_func: Callable, num_warmup: int, num_iterations: int
    ) -> float:
        """Return average time in ms using device Events (wall clock on cpu),
        with cross-rank synchronization."""
        for _ in range(num_warmup):
            op_func()
        # Sync all ranks after warmup so timing starts cleanly
        dist.barrier()

        if self.accel is not None:
            self.accel.synchronize()
            start = self.accel.Event(enable_timing=True)
            end = self.accel.Event(enable_timing=True)
            start.record()
            for _ in range(num_iterations):
                op_func()
            end.record()
            self.accel.synchronize()
            # Barrier ensures all ranks finish before rank 0 reads the result
            dist.barrier()
            return start.elapsed_time(end) / num_iterations

        # cpu/gloo fallback: no device events, use wall clock across ranks
        dist.barrier()
        t0 = time.perf_counter()
        for _ in range(num_iterations):
            op_func()
        dist.barrier()
        return (time.perf_counter() - t0) * 1e3 / num_iterations

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
            f"  Communication Benchmark  |  backend={self.backend}  |  "
            f"device={self.device_type}  |  world_size={self.world_size}  |  "
            f"dtype={dtype}  |  warmup={num_warmup}  iters={num_iters}"
        )
        log("=" * 95)
        log("Notes:")
        log(
            "  Bandwidth = (data_size / time) * correction factor -- normalized one-way link"
        )
        log(
            "  bandwidth, independent of rank count; directly comparable to one-way link"
        )
        log(
            "  speed, e.g. H200 NVLink18 one-way = 450 GB/s"
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
        description="torch.distributed communication benchmark (nccl-tests metric "
                    "conventions; backend auto-detected: nccl/hccl/gloo)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
examples:
  # All ops, 512 MB, 8 devices (default dtype=bfloat16)
  torchrun --nproc_per_node=8 performance/bench_communication.py --size-mb 512

  # Only AllReduce + AllGather, 1 GB, more iterations
  torchrun --nproc_per_node=8 performance/bench_communication.py \\
      --size-mb 1024 --ops allreduce allgather --iterations 200

  # Force a backend (default: auto — nccl on cuda, hccl on npu, gloo on cpu)
  torchrun --nproc_per_node=8 performance/bench_communication.py --backend nccl
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
        "--backend",
        default=None,
        help="torch.distributed backend (nccl/hccl/gloo/...). Default: auto by "
             "device type — nccl on cuda, hccl on npu, gloo on cpu.",
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
    args = parser.parse_args()

    dtype = {
        "float16": torch.float16,
        "bfloat16": torch.bfloat16,
        "float32": torch.float32,
        "float64": torch.float64,
    }[args.dtype]
    itemsize = torch.tensor([], dtype=dtype).element_size()

    counts = [int(args.size_mb * 1024**2 / itemsize)]

    bench = CommBenchmark(backend=args.backend)
    bench.init_distributed()

    try:
        if bench.rank == 0:
            try:
                dev_name = (bench.accel.get_device_name(bench.device)
                            if bench.accel is not None else "CPU")
            except Exception:
                dev_name = bench.device_type
            # Display the per-rank input size (AllGather/ReduceScatter data_size will be n× larger)
            sizes_mb = [f"{c * itemsize / 1024**2:.2f}MB" for c in counts]
            print(f"\nDevice: {dev_name} x {bench.world_size}  (backend={bench.backend})")
            print(f"Per-rank input sizes: {sizes_mb}")

        bench.run(
            counts=counts,
            dtype=dtype,
            num_warmup=args.warmup,
            num_iters=args.iterations,
            ops=args.ops,
        )
    finally:
        bench.cleanup()


if __name__ == "__main__":
    main()
