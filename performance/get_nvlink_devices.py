#!/usr/bin/env python3
"""
NVLink 设备检测脚本
==================

检测本机 GPU 的 NVLink 互联信息：
  1. 每张 GPU 有几条 NVLink 链路、每条链路的状态与速率
  2. NVLink 代际（NVLink 1.0/2.0/3.0/4.0/5.0）
  3. 单 GPU 聚合带宽与双向带宽（GB/s）
  4. 每条链路对端的 GPU（peer GPU index / NVSwitch）

数据来源
--------
- `nvidia-smi nvlink -s`     链路状态与单链路速率（如 "25 GB/s"）
- `nvidia-smi nvlink -p`     每条链路对端 PCI bus ID
- `nvidia-smi nvlink -R`      对端 PCI bus ID + 对端 Link ID
- `nvidia-smi -q -d NVLINK`  带宽模式 / 链路代际（部分驱动支持）
- `nvidia-smi --query-gpu`   GPU index / name / compute capability / pci bus id

NVLink 代际判定（nvidia-smi 无直接的 "version" 字段，按架构推断）
--------------------------------------------------------------
  compute_cap 6.0  (P100)   → NVLink 1.0   单链路 20 GB/s  4 链路  160 GB/s
  compute_cap 7.0  (V100)   → NVLink 2.0   单链路 25 GB/s  6 链路  300 GB/s  (NVSwitch 1.0)
  compute_cap 8.0  (A100)   → NVLink 3.0   单链路 25 GB/s 12 链路  600 GB/s
  compute_cap 9.0  (H200)   → NVLink 4.0   单链路 25 GB/s 18 链路  900 GB/s  (SHARP)
  compute_cap 10.0 (B200)   → NVLink 5.0   单链路 50 GB/s 18 链路  1.8 TB/s  (NVL72)
  Rubin (Vera)              → NVLink 6.0                           3.6 TB/s  (NVLink Switch 6)

注：单链路速率为单向峰值。聚合单向 = 单链路速率 × 链路数；双向 = 单向 × 2。
    nvidia-smi nvlink -s 报的速率是单向 (如 25 / 26.562 GB/s)。

注意命名陷阱：NVLink 代际号比 GPU 架构"晚一代" ——
  V100(Volta)=NVLink 2.0, A100(Ampere)=NVLink 3.0, H200(Hopper)=NVLink 4.0, B200(Blackwell)=NVLink 5.0。
  不要把 V100 误标成 NVLink 1.0 (那是 P100/Pascal)。

用法
----
  python3 get_nvlink_devices.py            # 全量详情
  python3 get_nvlink_devices.py --simple    # 只输出代际与聚合带宽摘要
  python3 get_nvlink_devices.py --json     # JSON 格式输出（便于程序读取）
"""

import argparse
import json
import re
import subprocess
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# NVLink 代际表（按 compute capability 判定，兜底用单链路速率）
# ---------------------------------------------------------------------------


@dataclass
class NVLinkGen:
    name: str  # "NVLink 2.0"
    year: int  # 发布年份
    arch: str  # GPU 架构 / 代表型号
    modulation: str  # 信号调制 (NRZ / PAM-4)
    pairs: str  # 每链路差分对数 (Sub-link / Diff-pair)
    per_link_gbs: float  # 标称单链路单向速率 GB/s (双向 ×2)
    max_links: int  # 该代单 GPU 最多链路数
    note: str = ""  # 备注


# 按 compute capability 判定代际
# 注意: NVLink 代际号比 GPU 架构"晚一代" —— V100=2.0, A100=3.0, H200=4.0, B200=5.0
_NVLINK_BY_CC: Dict[float, NVLinkGen] = {
    6.0: NVLinkGen(
        "NVLink 1.0", 2016, "Pascal (P100)", "NRZ", "8 (Sub-link)", 20.0, 4, "首次引入"
    ),
    7.0: NVLinkGen(
        "NVLink 2.0",
        2017,
        "Volta (V100)",
        "NRZ",
        "8 (Sub-link)",
        25.0,
        6,
        "引入 NVSwitch 1.0",
    ),
    8.0: NVLinkGen(
        "NVLink 3.0",
        2020,
        "Ampere (A100)",
        "NRZ",
        "4 (Sub-link)",
        25.0,
        12,
        "信号对减半, 链路数翻倍",
    ),
    9.0: NVLinkGen(
        "NVLink 4.0",
        2022,
        "Hopper (H200)",
        "PAM-4",
        "2 (Diff-pair)",
        25.0,
        18,
        "引入 SHARP",
    ),
    10.0: NVLinkGen(
        "NVLink 5.0",
        2024,
        "Blackwell (B200)",
        "PAM-4",
        "2 (Diff-pair)",
        50.0,
        18,
        "支持 NVL72 机架级扩展",
    ),
}

# 全部代际 (含 GH200/Rubin), 用于开头打印参考表
_ALL_NVLINK_GENS: List[NVLinkGen] = [
    NVLinkGen(
        "NVLink 1.0", 2016, "Pascal (P100)", "NRZ", "8 (Sub-link)", 20.0, 4, "首次引入"
    ),
    NVLinkGen(
        "NVLink 2.0",
        2017,
        "Volta (V100)",
        "NRZ",
        "8 (Sub-link)",
        25.0,
        6,
        "引入 NVSwitch 1.0",
    ),
    NVLinkGen(
        "NVLink 3.0",
        2020,
        "Ampere (A100)",
        "NRZ",
        "4 (Sub-link)",
        25.0,
        12,
        "信号对减半, 链路数翻倍",
    ),
    NVLinkGen(
        "NVLink 4.0",
        2022,
        "Hopper (H200)",
        "PAM-4",
        "2 (Diff-pair)",
        25.0,
        18,
        "引入 SHARP; H200 均 900 GB/s",
    ),
    NVLinkGen(
        "NVLink 5.0",
        2024,
        "Blackwell (B200)",
        "PAM-4",
        "2 (Diff-pair)",
        50.0,
        18,
        "支持 NVL72 机架级扩展",
    ),
    NVLinkGen(
        "NVLink 6.0",
        2026,
        "Rubin (Vera)",
        "-",
        "-",
        0.0,
        0,
        "NVLink Switch 6, RAS 增强; 3.6 TB/s",
    ),
]


def _fmt_bw(gbs: float) -> str:
    """带宽: >=1000 用 TB/s, 否则 GB/s。"""
    if gbs <= 0:
        return "-"
    if gbs >= 1000:
        return f"{gbs / 1000:.2f} TB/s"
    return f"{gbs:.0f} GB/s"


def print_nvlink_reference():
    """打印 NVLink 各代际规格参考表。"""
    W = 120
    print("=" * W)
    print("NVLink Generation Reference  (单链路速率为单向, 双向聚合 = 单链路×链路数×2)")
    print("=" * W)
    hdr = (
        f"{'Gen':<10}{'Year':>6} {'Arch':<20}{'Mod':<7}{'Pairs':<16}"
        f"{'Per-link':>11}{'Links':>7}{'Bi-Aggregate':>16}  Note"
    )
    print(hdr)
    print("-" * W)
    for g in _ALL_NVLINK_GENS:
        bi = g.per_link_gbs * g.max_links * 2
        per = f"{g.per_link_gbs:.0f} GB/s" if g.per_link_gbs > 0 else "-"
        links = str(g.max_links) if g.max_links > 0 else "-"
        print(
            f"{g.name:<10}{g.year:>6} {g.arch:<20}{g.modulation:<7}{g.pairs:<16}"
            f"{per:>11}{links:>7}{_fmt_bw(bi):>16}  {g.note}"
        )
    print("-" * W)
    print(
        "注: 代际号比 GPU 架构晚一代 —— V100=2.0, A100=3.0, H200=4.0, B200=5.0 (别把 V100 当 1.0)。"
    )
    print(
        "    Bi-Aggregate 为该代满配单 GPU 双向峰值; 实际以本机活动链路数为准 (见下)。\n"
    )


def infer_nvlink_gen(compute_cap: float) -> NVLinkGen:
    """根据 compute capability 推断 NVLink 代际。

    NVLink 代际号比 GPU 架构晚一代: P100(6.0)=1.0, V100(7.0)=2.0, A100(8.0)=3.0,
    H200(9.0)=4.0, B200(10.0)=5.0。

    H200 为 cc 9.0、同属 NVLink 4.0, 单链路 25 GB/s, 双向聚合 900 GB/s。
    """
    # 兜底：未在表中的 cc，按主版本号就近向下取最近的代际
    if compute_cap in _NVLINK_BY_CC:
        return _NVLINK_BY_CC[compute_cap]
    major = int(compute_cap)
    for cc in sorted(_NVLINK_BY_CC, reverse=True):
        if major >= int(cc):
            return _NVLINK_BY_CC[cc]
    return NVLinkGen("Unknown", 0, "Unknown", "?", "?", 0.0, 0, "")


# ---------------------------------------------------------------------------
# nvidia-smi 调用封装
# ---------------------------------------------------------------------------


def _run(cmd: List[str]) -> str:
    """运行命令并返回 stdout，失败返回空串。"""
    try:
        r = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=30,
        )
        return r.stdout if r.returncode == 0 else ""
    except Exception:
        return ""


def _gpu_count() -> int:
    out = _run(["nvidia-smi", "--query-gpu=index", "--format=csv,noheader"])
    return len([l for l in out.splitlines() if l.strip()]) if out else 0


def _query_gpu(fields: List[str]) -> List[str]:
    """返回每张 GPU 指定字段的值列表（按 index 顺序）。"""
    out = _run(
        [
            "nvidia-smi",
            "--query-gpu=" + ",".join(fields),
            "--format=csv,noheader,nounits",
        ]
    )
    return [l.strip() for l in out.splitlines() if l.strip()]


def _parse_link_status(text: str) -> List[Tuple[int, str]]:
    """解析 `nvidia-smi nvlink -s -i N` 输出，返回 [(link_id, rate_str)]。

    形如:  Link 0: 25 GB/s  或  Link 0: Inactive
    """
    links = []
    for line in text.splitlines():
        m = re.match(r"\s*Link\s+(\d+):\s*(.+?)\s*$", line)
        if m:
            links.append((int(m.group(1)), m.group(2).strip()))
    return links


# PCI bus ID: 可选 domain(4+ hex) + bus:dev.func，整体不含空格
_PCI_RE = r"(?:[0-9a-fA-F]{4,}:)?[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\.[0-9a-fA-F]"


def _parse_remote_peer(text: str) -> Dict[int, str]:
    """解析 `nvidia-smi nvlink -p -i N`，返回 {link_id: remote_pci}。

    形如:  Link 0: 00000000:88:00.0
    注意：'Link 0:' 中的冒号不能被 PCI 字符类吞掉，用精确 PCI 正则匹配。
    """
    peers = {}
    for line in text.splitlines():
        m = re.match(r"\s*Link\s+(\d+):\s*(" + _PCI_RE + r")\s*$", line)
        if m:
            peers[int(m.group(1))] = m.group(2).strip()
    return peers


def _parse_remote_link_info(text: str) -> Dict[int, Tuple[str, str]]:
    """解析 `nvidia-smi nvlink -R -i N`，返回 {link_id: (remote_pci, remote_link)}.

    形如:  Link 0: Remote Device 00000000:88:00.0: Link 11
    """
    out = {}
    for line in text.splitlines():
        m = re.match(
            r"\s*Link\s+(\d+):\s*Remote Device\s+(" + _PCI_RE + r"):\s*Link\s+(\d+)",
            line,
        )
        if m:
            out[int(m.group(1))] = (m.group(2).strip(), int(m.group(3)))
    return out


# ---------------------------------------------------------------------------
# 检测核心
# ---------------------------------------------------------------------------


@dataclass
class LinkInfo:
    link_id: int
    state: str  # "Active" / "Inactive"
    rate_gbs: (
        float  # 单链路单向原始速率 GB/s (nvidia-smi 报告值, 如 26.562)，Inactive 为 0
    )
    peer_pci: str  # 对端 PCI bus ID，无则 ""
    peer_link: int  # 对端 Link ID，-1 表示未知


@dataclass
class GPUInfo:
    index: int
    name: str
    pci: str
    compute_cap: float
    nvlink_gen: NVLinkGen
    links: List[LinkInfo] = field(default_factory=list)

    @property
    def active_links(self) -> List[LinkInfo]:
        return [l for l in self.links if l.state == "Active"]

    @property
    def total_links(self) -> int:
        return len(self.links)

    @property
    def active_link_count(self) -> int:
        return len(self.active_links)

    @property
    def per_link_gbs(self) -> float:
        """实际测得的活动单链路速率（取首条活动链路, nvidia-smi 报告值）。无活动链路返回 0。"""
        for l in self.active_links:
            return l.rate_gbs
        return 0.0

    @property
    def aggregate_gbs(self) -> float:
        """单向聚合带宽 = 活动链路数 × 单链路速率（GB/s）。

        单链路速率取 nvidia-smi 报告的原始值（如 A800 25、H200 26.562 GB/s, 单向）。
        官方标称带宽通常指双向：单向 × 2（见 bidirectional_gbs）。
        """
        per = self.per_link_gbs or self.nvlink_gen.per_link_gbs
        return per * self.active_link_count

    @property
    def bidirectional_gbs(self) -> float:
        """双向聚合带宽 = 单向聚合 × 2（GB/s）。对齐 NVIDIA 官方标称口径。"""
        return self.aggregate_gbs * 2

    def to_dict(self) -> dict:
        return {
            "index": self.index,
            "name": self.name,
            "pci": self.pci,
            "compute_cap": f"{self.compute_cap}",
            "nvlink_gen": self.nvlink_gen.name,
            "total_links": self.total_links,
            "active_links": self.active_link_count,
            "per_link_gbps": round(self.per_link_gbs, 3),
            "aggregate_gbps": round(self.aggregate_gbs, 3),
            "bidirectional_gbps": round(self.bidirectional_gbs, 3),
            "links": [
                {
                    "link": l.link_id,
                    "state": l.state,
                    "rate_gbps": l.rate_gbs,
                    "peer_pci": l.peer_pci,
                    "peer_link": l.peer_link,
                }
                for l in self.links
            ],
        }


def _norm_pci(p: str) -> str:
    """归一化 PCI 地址：去前导 0000 域段、转小写，便于比较。

    '00000000:88:00.0' -> '88:00.0'
    '0000:4A:00.0'    -> '4a:00.0'
    """
    p = p.lower().strip()
    # 形如 dddd:dd:dd.d 去掉首段
    m = re.match(r"^(?:[0-9a-f]{4,}:)?([0-9a-f]{2}:[0-9a-f]{2}\.[0-9a-f])$", p)
    return m.group(1) if m else p


def detect() -> List[GPUInfo]:
    gpus: List[GPUInfo] = []

    n = _gpu_count()
    if n == 0:
        return gpus

    # 取 GPU 基本属性
    names = _query_gpu(["name"])
    caps = _query_gpu(["compute_cap"])
    pcis = _query_gpu(["pci.bus_id"])

    for i in range(n):
        name = names[i] if i < len(names) else ""
        cc = float(caps[i]) if i < len(caps) and caps[i] else 0.0
        pci = pcis[i] if i < len(pcis) else ""

        nvgen = infer_nvlink_gen(cc)

        status = _run(["nvidia-smi", "nvlink", "-s", "-i", str(i)])
        peer = _parse_remote_peer(_run(["nvidia-smi", "nvlink", "-p", "-i", str(i)]))
        rlink = _parse_remote_link_info(
            _run(["nvidia-smi", "nvlink", "-R", "-i", str(i)])
        )

        links: List[LinkInfo] = []
        for lid, rate_str in _parse_link_status(status):
            if rate_str.lower() in ("inactive", "disabled", "down", ""):
                state, rate = "Inactive", 0.0
            else:
                state = "Active"
                m = re.search(r"([\d.]+)\s*GB/s", rate_str)
                rate = float(m.group(1)) if m else 0.0
            pci_p = peer.get(lid, "")
            rl = rlink.get(lid)
            rl_id = rl[1] if rl else -1
            links.append(LinkInfo(lid, state, rate, pci_p, rl_id))

        gpus.append(GPUInfo(i, name, pci, cc, nvgen, links))

    # 二次扫描：把对端 PCI 地址解析为 GPU index（同机内 peer）
    _resolve_peers(gpus)
    return gpus


def _resolve_peers(gpus: List[GPUInfo]):
    """将每条链路的对端 PCI 解析为 GPU index 或 NVSwitch。

    SXM4/SXM5 平台 GPU 经 NVSwitch 全互联，链路对端是 NVSwitch（vendor 0x10de、
    PCI class 0x068000 Bridge），不是另一张 GPU；直接相连拓扑（如部分 PCIe 卡）下，
    对端才是另一张 GPU。这里按对端 PCI 是否命中本机 GPU 表来区分。
    """
    pci_map = {_norm_pci(g.pci): g.index for g in gpus}
    for g in gpus:
        for l in g.links:
            if not l.peer_pci:
                continue
            peer_gpu = pci_map.get(_norm_pci(l.peer_pci))
            if peer_gpu is not None:
                l.peer_pci = f"GPU{peer_gpu} ({l.peer_pci})"
            else:
                l.peer_pci = f"NVSwitch ({l.peer_pci})"


# ---------------------------------------------------------------------------
# 输出
# ---------------------------------------------------------------------------


def _fmt_gbs(v: float) -> str:
    return f"{v:.2f} GB/s" if v else "N/A"


def print_detail(gpus: List[GPUInfo]):
    if not gpus:
        print("No GPU / NVLink devices found.")
        return

    print_nvlink_reference()
    print("=" * 78)
    print("NVLink Device Detection")
    print("=" * 78)

    for g in gpus:
        print(f"\nGPU {g.index}: {g.name}  (PCI {g.pci}, CC {g.compute_cap})")
        print(f"  NVLink Gen      : {g.nvlink_gen.name}")
        print(f"  Links           : {g.active_link_count}/{g.total_links} active")
        print(f"  Per-link speed  : {_fmt_gbs(g.per_link_gbs)}  (unidirectional)")
        print(f"  Aggregate BW    : {_fmt_gbs(g.aggregate_gbs)}  unidirectional")
        print(
            f"                  : {_fmt_gbs(g.bidirectional_gbs)}  bidirectional (peak)"
        )
        print(f"  Link details:")
        for l in g.links:
            peer = l.peer_pci or "-"
            rlink = f"Link {l.peer_link}" if l.peer_link >= 0 else ""
            print(
                f"    Link {l.link_id:2d}: {l.state:8s} "
                f"{_fmt_gbs(l.rate_gbs):14s} peer {peer} {rlink}"
            )

    print("\n" + "=" * 78)
    print("Summary")
    print("=" * 78)
    for g in gpus:
        print(
            f"GPU{g.index} [{g.name:24s}] {g.nvlink_gen.name:12s} "
            f"{g.active_link_count}/{g.total_links} links  "
            f"{_fmt_gbs(g.aggregate_gbs)} / {_fmt_gbs(g.bidirectional_gbs)} (uni/bi)"
        )
    total = sum(g.aggregate_gbs for g in gpus)
    total_bi = sum(g.bidirectional_gbs for g in gpus)
    print(
        f"\nTotal aggregate NVLink bandwidth (all GPUs): "
        f"{total:.2f} GB/s uni  /  {total_bi:.2f} GB/s bi"
    )


def print_simple(gpus: List[GPUInfo]):
    """摘要：每张 GPU 一行 代际/链路数/聚合带宽。"""
    if not gpus:
        print("")
        return
    for g in gpus:
        print(
            f"GPU{g.index} {g.name} {g.nvlink_gen.name} "
            f"{g.active_link_count}/{g.total_links}links "
            f"{g.bidirectional_gbs:.2f}GB/s(bi)"
        )


def main():
    p = argparse.ArgumentParser(description="检测 GPU NVLink 互联信息")
    p.add_argument("--simple", action="store_true", help="只输出代际与聚合带宽摘要")
    p.add_argument("--json", action="store_true", help="JSON 格式输出")
    args = p.parse_args()

    gpus = detect()

    if args.json:
        print(json.dumps([g.to_dict() for g in gpus], indent=2, ensure_ascii=False))
    elif args.simple:
        print_simple(gpus)
    else:
        print_detail(gpus)


if __name__ == "__main__":
    main()
