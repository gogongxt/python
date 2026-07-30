#!/usr/bin/env python3
"""
GPU ↔ RDMA 网卡拓扑匹配原理
============================

服务器中 GPU 和 RDMA 网卡 (InfiniBand) 都是 PCI 设备，它们通过 PCI 桥 (PCI Bridge)
层层相连，形成树状拓扑。物理距离越近的设备，共享的 PCI 祖先节点越深（越靠近叶子）。

本脚本通过以下步骤找出每张 GPU "最近" 的 RDMA 网卡：

1. 设备发现
   遍历 /sys/bus/pci/devices/*，通过 vendor ID 识别设备类型：
   - 0x10de → NVIDIA 设备（GPU 和 NVSwitch 都是此 vendor）
   - 0x15b3 → Mellanox InfiniBand 网卡

2. 构建 PCI 祖先链
   对每个设备，沿 /sys/devices/pci... 的 realpath 逐级向上回溯，
   收集路径上所有符合 BDF 格式 (DDDD:BB:DD.F) 的 PCI 桥节点地址。
   例如某 GPU 的祖先链可能是：
     [0000:17:00.0, 0000:16:00.0, 0000:00:01.0]
   越靠后的元素越接近 PCI Root。

3. 最深公共祖先匹配
   对每个 NVIDIA 设备，遍历所有未被占用的 IB 网卡，计算两者祖先链的交集，
   取交集中"最深"（最靠近设备）的那个桥节点作为共享根。
   用 score = len(gpu_ancestors) - index(shared) 量化深度，
   score 越大说明共享桥离 GPU 越近，物理距离越短。
   每个 NVIDIA 设备匹配 score 最高的 IB 网卡，且每张 IB 网卡只匹配一次。

========================================================================
示例 1：理想拓扑（每组 GPU+IB 共享同一 PCIe Switch）
========================================================================

  CPU
   └─ PCIe Root Port
       └─ PCIe Switch (Bridge A)
           ├─ Bridge B ── GPU0
           ├─ Bridge C ── GPU1
           ├─ Bridge D ── GPU2
           └─ Bridge E ── IB0 (mlx5_0)
       └─ PCIe Switch (Bridge F)
           ├─ Bridge G ── GPU3
           ├─ Bridge H ── GPU4
           ├─ Bridge I ── GPU5
           └─ Bridge J ── IB1 (mlx5_1)

GPU0~2 与 IB0 共享 Bridge A，GPU3~5 与 IB1 共享 Bridge F，
因此 GPU0~2 匹配到 mlx5_0，GPU3~5 匹配到 mlx5_1。

========================================================================
示例 2：真实拓扑 — 机器 (H20-3e × 8 GPU)
========================================================================

每对 GPU + IB 通过同一 PCIe Switch 下的兄弟桥连接，4 个 NVSwitch 无附近 IB。
NVSwitch 的 PCI class 是 0x068000（Bridge），脚本按 vendor 0x10de 将其一并检测。

  Root Port 00:0a.0
   └─ Bridge 01:00.0
       ├─ 02:00.0 ── NVSwitch 03:00.0   (无附近 IB)
       ├─ 02:01.0 ── NVSwitch 04:00.0   (无附近 IB)
       ├─ 02:02.0 ── NVSwitch 05:00.0   (无附近 IB)
       └─ 02:03.0 ── NVSwitch 06:00.0   (无附近 IB)

  Root Port 15:01.0
   └─ Bridge 16:00.0
       ├─ 17:00.0 ── GPU[0]  18:00.0
       └─ 17:01.0 ── IB      mlx5_5    (共享: 15:01.0, score=3)

  Root Port 35:01.0
   └─ Bridge 36:00.0
       ├─ 37:00.0 ── GPU[1]  38:00.0
       └─ 37:01.0 ── IB      mlx5_4    (共享: 35:01.0, score=3)

  Root Port 45:01.0
   └─ Bridge 46:00.0
       ├─ 47:00.0 ── IB      mlx5_3
       └─ 47:01.0 ── GPU[2]  49:00.0   (共享: 45:01.0, score=3)

  Root Port 55:01.0
   └─ Bridge 56:00.0
       ├─ 57:00.0 ── IB      mlx5_2
       └─ 57:01.0 ── GPU[3]  59:00.0   (共享: 55:01.0, score=3)

  Root Port 97:01.0
   └─ Bridge 98:00.0
       ├─ 99:00.0 ── IB      mlx5_7
       └─ 99:01.0 ── GPU[4]  9b:00.0   (共享: 97:01.0, score=3)

  Root Port b7:01.0
   └─ Bridge b8:00.0
       ├─ b9:00.0 ── IB      mlx5_6
       └─ b9:01.0 ── GPU[5]  bb:00.0   (共享: b7:01.0, score=3)

  Root Port c7:01.0
   └─ Bridge c8:00.0
       ├─ c9:00.0 ── IB      mlx5_9
       └─ c9:01.0 ── GPU[6]  ca:00.0   (共享: c7:01.0, score=3)

  Root Port d7:01.0
   └─ Bridge d8:00.0
       ├─ d9:00.0 ── IB      mlx5_8
       └─ d9:01.0 ── GPU[7]  da:00.0   (共享: d7:01.0, score=3)

匹配结果：GPU[0]→mlx5_5, GPU[1]→mlx5_4, GPU[2]→mlx5_3, GPU[3]→mlx5_2,
          GPU[4]→mlx5_7, GPU[5]→mlx5_6, GPU[6]→mlx5_9, GPU[7]→mlx5_8
IB 列表：mlx5_2,mlx5_3,mlx5_4,mlx5_5,mlx5_6,mlx5_7,mlx5_8,mlx5_9

========================================================================
示例 3：复杂拓扑 — 机器 (H200 × 8 GPU)
========================================================================

本例展示三个复杂场景：
  (a) 4 个 NVSwitch 所在分支没有任何 IB，它们匹配失败（无附近 IB）
  (b) mlx5_3/mlx5_4 共享同一深层桥 (48:01.0)，但该桥下没有 GPU
  (c) GPU[1] 和 GPU[2] 通过竞争分配到不同的 IB

  Root Port 00:10.0
   └─ Bridge 03:00.0
       ├─ 04:00.0 ── NVSwitch 05:00.0   (无附近 IB)
       ├─ 04:01.0 ── NVSwitch 06:00.0   (无附近 IB)
       ├─ 04:02.0 ── NVSwitch 07:00.0   (无附近 IB)
       └─ 04:03.0 ── NVSwitch 08:00.0   (无附近 IB)

  Root Port 15:01.0
   └─ Bridge 16:00.0
       ├─ 17:00.0 ── GPU[0]  18:00.0
       └─ 17:01.0 ── IB      mlx5_0    (共享: 15:01.0, score=3)

  Root Port 26:01.0
   └─ Bridge 27:00.0
       ├─ 28:00.0 ── IB      mlx5_1
       └─ 28:01.0 ── GPU[1]  2a:00.0   (共享: 26:01.0, score=3)

  Root Port 37:01.0
   └─ Bridge 38:00.0
       ├─ 39:00.0 ── GPU[2]  3a:00.0
       └─ 39:01.0 ── IB      mlx5_2    (共享: 37:01.0, score=3)

  Root Port 48:01.0
   └─ Bridge 49:00.0
       └─ Bridge 4a:0c.0
           └─ Bridge 54:00.0
               └─ Bridge 55:00.0
                   ├─ 56:00.0 ── IB  mlx5_3   (深达 5 层，但附近无 GPU)
                   └─ 56:00.1 ── IB  mlx5_4   (同上)

  Root Port 59:01.0
   └─ Bridge 5a:00.0
       ├─ 5b:00.0 ── IB      mlx5_5
       └─ 5b:01.0 ── GPU[3]  5d:00.0   (共享: 59:01.0, score=3)

  Root Port 97:01.0
   └─ Bridge 98:00.0
       ├─ 99:00.0 ── GPU[4]  9a:00.0
       └─ 99:01.0 ── IB      mlx5_6    (共享: 97:01.0, score=3)

  Root Port a7:01.0
   └─ Bridge a8:00.0
       ├─ a9:00.0 ── IB      mlx5_7
       └─ a9:01.0 ── GPU[5]  ab:00.0   (共享: a7:01.0, score=3)

  Root Port b7:01.0
   └─ Bridge b8:00.0
       ├─ b9:00.0 ── GPU[6]  ba:00.0
       └─ b9:01.0 ── IB      mlx5_8    (共享: b7:01.0, score=3)

  Root Port d7:01.0
   └─ Bridge d8:00.0
       ├─ d9:00.0 ── IB      mlx5_9
       └─ d9:01.0 ── GPU[7]  db:00.0   (共享: d7:01.0, score=3)

匹配过程（按 PCI 地址排序逐个匹配，IB 先到先得）：

  NVSwitch 05:00.0 → 遍历所有 IB，均无公共祖先 → 无匹配
  NVSwitch 06:00.0 → 同上
  NVSwitch 07:00.0 → 同上
  NVSwitch 08:00.0 → 同上
  GPU[0] 18:00.0   → 与 mlx5_0 共享 15:01.0 (score=3) → 匹配 mlx5_0 ✓
  GPU[1] 2a:00.0   → 与 mlx5_1 共享 26:01.0 (score=3) → 匹配 mlx5_1 ✓
  GPU[2] 3a:00.0   → 与 mlx5_2 共享 37:01.0 (score=3) → 匹配 mlx5_2 ✓
  GPU[3] 5d:00.0   → 与 mlx5_5 共享 59:01.0 (score=3) → 匹配 mlx5_5 ✓
  GPU[4] 9a:00.0   → 与 mlx5_6 共享 97:01.0 (score=3) → 匹配 mlx5_6 ✓
  GPU[5] ab:00.0   → 与 mlx5_7 共享 a7:01.0 (score=3) → 匹配 mlx5_7 ✓
  GPU[6] ba:00.0   → 与 mlx5_8 共享 b7:01.0 (score=3) → 匹配 mlx5_8 ✓
  GPU[7] db:00.0   → 与 mlx5_9 共享 d7:01.0 (score=3) → 匹配 mlx5_9 ✓

注意：mlx5_3 和 mlx5_4 虽然存在于系统中，但它们的 PCI 分支下没有 GPU，
因此未被任何 GPU 匹配。实际可用 IB 列表只有 8 个。

IB 列表：mlx5_0,mlx5_1,mlx5_2,mlx5_5,mlx5_6,mlx5_7,mlx5_8,mlx5_9
"""

import glob
import os
import re


def get_vendor(dev_path):
    try:
        return open(os.path.join(dev_path, "vendor")).read().strip()
    except Exception:
        return None


def get_numa(dev_path):
    try:
        v = int(open(os.path.join(dev_path, "numa_node")).read().strip())
        return v if v >= 0 else 0
    except Exception:
        return 0


def get_ib_name(dev_path):
    ib_dir = os.path.join(dev_path, "infiniband")
    if os.path.isdir(ib_dir):
        names = os.listdir(ib_dir)
        if names:
            return names[0]
    return None


def pci_ancestors(dev_path):
    """返回该 PCI 设备的所有上级 PCI 桥节点（BDF 地址列表）"""
    path = os.path.realpath(dev_path)
    parts = []
    while True:
        parent = os.path.dirname(path)
        if parent == path or not parent.startswith("/sys/devices/pci"):
            break
        name = os.path.basename(parent)
        if re.match(r"[0-9a-f]{4}:[0-9a-f]{2}:[0-9a-f]{2}\.[0-9a-f]", name):
            parts.append(name)
        path = parent
    return parts


def detect_devices():
    gpus, ibs = [], []
    for dev_path in glob.glob("/sys/bus/pci/devices/*"):
        vendor = get_vendor(dev_path)
        if vendor == "0x10de":  # NVIDIA GPU
            gpus.append(
                {
                    "path": dev_path,
                    "pci": os.path.basename(dev_path),
                    "numa": get_numa(dev_path),
                    "ancestors": pci_ancestors(dev_path),
                }
            )
        elif vendor == "0x15b3":  # Mellanox IB
            ib_name = get_ib_name(dev_path)
            if ib_name:
                ibs.append(
                    {
                        "path": dev_path,
                        "pci": os.path.basename(dev_path),
                        "ib_name": ib_name,
                        "numa": get_numa(dev_path),
                        "ancestors": pci_ancestors(dev_path),
                    }
                )
    return gpus, ibs


def find_shared_root(gpu, ib):
    """计算 GPU 和 IB 共享的最深层 PCI 祖先节点"""
    # 找到共同的祖先节点
    shared_ancestors = []
    for g_anc in gpu["ancestors"]:
        if g_anc in ib["ancestors"]:
            shared_ancestors.append(g_anc)
    # 返回最后一个共同的祖先（最接近设备的）
    return shared_ancestors[-1] if shared_ancestors else None


def _find_matched_ib_names():
    """核心匹配逻辑：返回 GPU 匹配到的 IB 设备名集合和匹配详情"""
    gpus, ibs = detect_devices()
    if not gpus or not ibs:
        return [], set()
    matched = []
    used_ibs = set()
    for gpu in gpus:
        best_ib = None
        best_shared = None
        best_score = -1
        for ib in ibs:
            if ib["ib_name"] in used_ibs:
                continue
            shared = find_shared_root(gpu, ib)
            if shared:
                try:
                    score = len(gpu["ancestors"]) - gpu["ancestors"].index(shared)
                except ValueError:
                    score = 0
                if score > best_score:
                    best_ib = ib
                    best_shared = shared
                    best_score = score
        if best_ib:
            matched.append((gpu, best_ib, best_shared))
            used_ibs.add(best_ib["ib_name"])
        else:
            matched.append((gpu, None, None))
    return matched, used_ibs


def match_gpu_ib():
    matched, matched_ibs = _find_matched_ib_names()
    if not matched:
        print("No GPU or IB devices found.")
        return ""
    print("Detected GPU ↔ IB Topology (by PCI ancestry):\n")
    for gpu, ib, shared in matched:
        if ib:
            print(f"GPU {gpu['pci']} ↔ IB {ib['ib_name']} (shared bridge: {shared})")
        else:
            print(f"GPU {gpu['pci']} ↔ (no nearby IB found)")
    all_ib_names = ",".join(sorted(matched_ibs))
    print(f"\nIB devices (GPU-attached): {all_ib_names}")
    return all_ib_names


def get_gpu_attached_ib_devices():
    """
    返回GPU连接的RDMA网卡列表字符串
    Returns:
        str: 逗号分隔的RDMA网卡名称，如 "mlx5_2,mlx5_3,mlx5_4,mlx5_5"
             如果没有找到设备返回空字符串
    """
    _, matched_ibs = _find_matched_ib_names()
    return ",".join(sorted(matched_ibs)) if matched_ibs else ""


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="检测GPU连接的RDMA网卡")
    parser.add_argument(
        "--simple",
        action="store_true",
        help="简单输出模式：只返回逗号分隔的RDMA网卡列表",
    )
    args = parser.parse_args()

    if args.simple:
        print(get_gpu_attached_ib_devices())
    else:
        match_gpu_ib()
