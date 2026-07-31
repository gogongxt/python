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
   - 0x15b3 → Mellanox RDMA 网卡

   统计"GPU 可用的 RDMA 网卡"需同时满足三个条件：
   (a) 是 RDMA 卡 —— 有 /sys/class/infiniband/ 入口（InfiniBand 或 RoCE 均可，
       两者都提供 RDMA 语义，NCCL 都能用）
   (b) 端口物理接线 —— phys_state 含 "LinkUp"，排除未连线端口
       （未连线时 rate 文件返回驱动默认值，无意义）
   (c) GPUDirect RDMA 已启用 —— nvidia_peermem 内核模块已加载（机器级开关，
       未加载则整机 RDMA 卡对 GPU 都不可用，无法做 GPU↔网卡 P2P 直通）

   NVIDIA 设备按 PCI class 进一步过滤：只保留 GPU（0x030000 VGA /
   0x030200 3D controller），排除同 vendor 的 NVSwitch（0x068000 Bridge）。

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
import subprocess


def _norm_bdf(bdf):
    """归一化 PCI BDF 为小写 "bb:dd.f"（去掉 domain 前缀）。

    nvidia-smi 给 "00000000:BA:00.0"，sysfs 给 "0000:ba:00.0"，
    domain 位数不一致，统一剥掉 domain 以保证两侧键可匹配。
    """
    bdf = bdf.lower()
    parts = bdf.split(":")
    # 形如 [domain, bus, dev.fn] 或 [bus, dev.fn]，取最后两段
    return ":".join(parts[-2:])


def get_gpu_index_map():
    """返回 {norm_bdf: cuda_index}，通过 nvidia-smi 查询。

    CUDA 的 GPU 编号（0,1,2,...）由驱动按 PCI bus 升序分配，
    与 glob("/sys/bus/pci/devices/*") 的 readdir 顺序无关。
    没装 nvidia-smi 或查询失败时返回空 dict，调用方回退到按 PCI 地址排序。
    """
    try:
        out = subprocess.check_output(
            ["nvidia-smi", "--query-gpu=index,pci.bus_id", "--format=csv,noheader"],
            stderr=subprocess.DEVNULL,
            text=True,
            timeout=15,
        )
    except Exception:
        return {}
    m = {}
    for line in out.strip().splitlines():
        parts = [p.strip() for p in line.split(",")]
        if len(parts) < 2:
            continue
        try:
            idx = int(parts[0])
        except ValueError:
            continue
        m[_norm_bdf(parts[1])] = idx
    return m


def get_vendor(dev_path):
    try:
        return open(os.path.join(dev_path, "vendor")).read().strip()
    except Exception:
        return None


# GPU display device 的 PCI class，用于排除同属 vendor 0x10de 的 NVSwitch
# 0x030000 = VGA controller, 0x030200 = 3D controller
GPU_PCI_CLASSES = {"0x030000", "0x030200"}


def is_gpu(dev_path):
    """vendor 0x10de 同时包含 GPU 和 NVSwitch（class 0x068000 Bridge），
    后者不是 GPU，不应参与 IB 匹配。按 class 过滤。"""
    if get_vendor(dev_path) != "0x10de":
        return False
    try:
        cls = open(os.path.join(dev_path, "class")).read().strip().lower()
    except Exception:
        return False
    # class 形如 0x030200，取前 8 个字符做匹配
    return cls[:8] in GPU_PCI_CLASSES


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


def get_ib_port_info(dev_path):
    """读取 RDMA 网卡首个端口的属性。

    返回 dict:
      {"link_layer": "InfiniBand"|"Ethernet"|...,
       "phys_state": "5: LinkUp"|...,   # 物理连接状态
       "rate": "400 Gb/sec (4X NDR)"|...}
    读不到时各字段为 "unknown"。

    通过 /sys/class/infiniband/<dev>/ports/<n>/{link_layer,phys_state,rate} 获取。
    """
    empty = {"link_layer": "unknown", "phys_state": "unknown", "rate": "unknown"}
    ib_name = get_ib_name(dev_path)
    if not ib_name:
        return empty
    ports_dir = f"/sys/class/infiniband/{ib_name}/ports"
    try:
        ports = sorted(os.listdir(ports_dir), key=int)
    except Exception:
        return empty
    if not ports:
        return empty
    port_dir = os.path.join(ports_dir, ports[0])
    info = dict(empty)
    for key in ("link_layer", "phys_state", "rate"):
        try:
            info[key] = open(os.path.join(port_dir, key)).read().strip()
        except Exception:
            pass
    return info


def get_ib_rate(dev_path):
    """读取 RDMA 网卡首个端口的速率，格式如 "400 Gb/sec (4X NDR)"。"""
    return get_ib_port_info(dev_path)["rate"]


def is_port_link_up(dev_path):
    """端口是否物理接线并 LinkUp。

    phys_state 形如 "5: LinkUp"。端口未接线(Disabled/Polling)时返回 False，
    此时 rate 文件返回的是驱动默认值（无意义），不应纳入统计。
    """
    return "LinkUp" in get_ib_port_info(dev_path)["phys_state"]


def is_gpudirect_enabled():
    """整机是否启用了 GPUDirect RDMA（GPU↔网卡 P2P 直通）。

    判据：nvidia_peermem 内核模块已加载。该模块让 RDMA 子系统直接映射 GPU
    显存，是 GPU 通过 RDMA 网卡通信的必需内核组件。模块是机器级开关——
    要么整机加载(所有 RDMA 卡对 GPU 可用)，要么整机未加载(都不可用)。
    """
    try:
        with open("/proc/modules") as f:
            for line in f:
                if line.startswith("nvidia_peermem ") or line.startswith(
                    "nv_peer_mem "
                ):
                    return True
    except Exception:
        pass
    return False


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
    # GPUDirect RDMA 是机器级开关：nvidia_peermem 未加载则整机 RDMA 卡对 GPU
    # 都不可用，无需逐卡判断。
    gpudirect = is_gpudirect_enabled()
    for dev_path in glob.glob("/sys/bus/pci/devices/*"):
        if is_gpu(dev_path):  # 仅 NVIDIA GPU，排除 NVSwitch
            gpus.append(
                {
                    "path": dev_path,
                    "pci": os.path.basename(dev_path),
                    "numa": get_numa(dev_path),
                    "ancestors": pci_ancestors(dev_path),
                }
            )
        elif get_vendor(dev_path) == "0x15b3":  # Mellanox RDMA 卡
            ib_name = get_ib_name(dev_path)
            # 统计"GPU 可用的 RDMA 网卡"需同时满足：
            #   (1) 是 RDMA 卡（有 infiniband/ 目录，IB 或 RoCE 均可）
            #   (2) 端口物理接线 LinkUp（排除未连线端口的无效速率）
            #   (3) 整机 GPUDirect RDMA 已启用（nvidia_peermem 已加载）
            if ib_name and is_port_link_up(dev_path) and gpudirect:
                ibs.append(
                    {
                        "path": dev_path,
                        "pci": os.path.basename(dev_path),
                        "ib_name": ib_name,
                        "rate": get_ib_rate(dev_path),
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
    if not gpus:
        # 真正无设备：连 GPU 都没有
        return [], set()
    # 注意：有 GPU 但无 IB 时走下面的正常循环，每个 GPU 会标 (no nearby IB found)，
    # 而不是在这里误报 "No GPU or IB devices found."
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
    # CUDA GPU 编号来自 nvidia-smi（驱动按 PCI bus 升序），与 readdir 顺序无关；
    # 查询失败时回退到按 PCI 地址排序（与驱动分配顺序一致）。
    idx_map = get_gpu_index_map()

    def gpu_sort_key(item):
        gpu = item[0]
        idx = idx_map.get(_norm_bdf(gpu["pci"]))
        return (0, idx) if idx is not None else (1, gpu["pci"])

    matched_sorted = sorted(matched, key=gpu_sort_key)
    print("Detected GPU ↔ IB Topology (by PCI ancestry):\n")
    for gpu, ib, shared in matched_sorted:
        idx = idx_map.get(_norm_bdf(gpu["pci"]))
        label = f"GPU{idx}" if idx is not None else f"GPU {gpu['pci']}"
        if ib:
            print(
                f"{label}  {gpu['pci']} ↔ IB {ib['ib_name']} "
                f"[{ib.get('rate', 'unknown')}] (shared bridge: {shared})"
            )
        else:
            print(f"{label}  {gpu['pci']} ↔ (no nearby IB found)")
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
