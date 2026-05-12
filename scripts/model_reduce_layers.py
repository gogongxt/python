import argparse
import json
import logging
import os
import resource
import shutil
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed

from safetensors import safe_open
from safetensors.torch import load as load_safetensors
from safetensors.torch import save as save_safetensors
from tqdm import tqdm

GB = 1 << 30


def _read_safetensor_keys(filepath):
    """Read all key names from a safetensors file (lightweight, no tensor data)."""
    keys = []
    with safe_open(filepath, framework="pt") as f:
        keys = list(f.keys())
    return keys


def _read_kept_weights(args):
    """Read kept weights from a single safetensors file (worker function)."""
    filepath, kept_keys = args
    result = {}
    skipped = []
    with safe_open(filepath, framework="pt") as f:
        for key in f.keys():
            if key not in kept_keys:
                continue
            try:
                tensor = f.get_tensor(key)
                # Ensure contiguous CPU tensor to release shared memory
                if not tensor.is_contiguous():
                    tensor = tensor.contiguous()
                result[key] = tensor
            except (KeyError, RuntimeError, ValueError):
                skipped.append(key)
    return result, skipped


def shard_weights(weights, max_shard_size):
    """Split weights into shards by total byte size."""
    shards = []
    current = {}
    current_size = 0
    for key, tensor in weights.items():
        tensor_size = tensor.nelement() * tensor.element_size()
        if current and current_size + tensor_size > max_shard_size:
            shards.append(current)
            current = {}
            current_size = 0
        current[key] = tensor
        current_size += tensor_size
    if current:
        shards.append(current)
    return shards


def main():
    logging.basicConfig(
        stream=sys.stdout,
        level=logging.INFO,
        format="[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s",
    )
    parser = argparse.ArgumentParser(
        description="Reduce model layers for debugging",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--model-path", help="source model path")
    parser.add_argument("--output-path", help="destination model path")
    parser.add_argument(
        "--layers", type=int, default=1, help="number of layers to keep"
    )
    parser.add_argument(
        "--max-shard-size",
        type=int,
        default=4,
        help="max shard size in GB",
    )
    parser.add_argument(
        "--num-workers",
        type=int,
        default=8,
        help="number of processes for reading weights",
    )
    args = parser.parse_args()
    # Raise fd limit for multi-process tensor loading
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    if soft < hard:
        resource.setrlimit(resource.RLIMIT_NOFILE, (hard, hard))
        logging.info(f"Raised fd limit from {soft} to {hard}")
    assert not os.path.exists(args.output_path)
    os.makedirs(args.output_path)
    # config.json
    config_filename = "config.json"
    src_path = os.path.join(args.model_path, config_filename)
    dst_path = os.path.join(args.output_path, config_filename)
    with open(src_path) as f, open(dst_path, "w") as fw:
        config = json.load(f)
        assert config["num_hidden_layers"] >= args.layers
        config["num_hidden_layers"] = args.layers
        json.dump(config, fw)
    # model files
    index_filename = "model.safetensors.index.json"
    src_path = os.path.join(args.model_path, index_filename)
    dst_path = os.path.join(args.output_path, index_filename)
    model_files = set()
    kept_keys = set()
    with open(src_path) as f:
        data = json.load(f)
    for key in data["weight_map"]:
        if key.startswith("model.layers."):
            layer = int(key.split(".")[2])
            if layer >= args.layers:
                continue
        kept_keys.add(key)
        model_files.add(data["weight_map"][key])
    # load kept weights (multi-process)
    weights = {}
    skipped_keys = []
    file_paths = [(os.path.join(args.model_path, fn), kept_keys) for fn in model_files]
    actual_workers = min(args.num_workers, len(file_paths))
    logging.info(f"Loading weights with {actual_workers} processes...")
    with ProcessPoolExecutor(max_workers=actual_workers) as executor:
        futures = {executor.submit(_read_kept_weights, fp): fp for fp in file_paths}
        pbar = tqdm(total=len(file_paths), desc="Reading weights", unit="file")
        for future in as_completed(futures):
            filepath = futures[future]
            try:
                result, skipped = future.result()
                weights.update(result)
                skipped_keys.extend(skipped)
            except Exception as e:
                logging.error(f"Failed to read {filepath}: {e}")
            pbar.update(1)
        pbar.close()
    if skipped_keys:
        logging.warning(
            f"Skipped {len(skipped_keys)} tensors with unsupported dtype: {skipped_keys[:5]}..."
        )
        for key in skipped_keys:
            kept_keys.discard(key)
    logging.info(f"Get {len(weights)} tensors")
    # shard and save
    max_shard_bytes = args.max_shard_size * GB
    shards = shard_weights(weights, max_shard_bytes)
    num_shards = len(shards)
    num_digits = len(str(num_shards))
    weight_map = {}
    for i, shard in enumerate(shards, 1):
        shard_filename = (
            f"model-{i:0{num_digits}d}-of-{num_shards:0{num_digits}d}.safetensors"
        )
        for key in shard:
            weight_map[key] = shard_filename
        try:
            buf = save_safetensors(shard, {"format": "pt"})
        except Exception as e:
            msg = str(e)
            if len(msg) > 500:
                msg = msg[:500] + f"... ({len(msg)} chars total)"
            logging.error(f"Failed to save {shard_filename}: {msg}")
            raise
        with open(os.path.join(args.output_path, shard_filename), "wb") as fw:
            fw.write(buf)
        logging.info(f"Saved {shard_filename} ({len(buf) / GB:.2f} GB)")
    with open(dst_path, "w") as fw:
        json.dump({"metadata": {}, "weight_map": weight_map}, fw)
    # Other files and directories
    for filename in os.listdir(args.model_path):
        src_path = os.path.join(args.model_path, filename)
        dst_path = os.path.join(args.output_path, filename)
        if (
            filename == config_filename
            or filename == index_filename
            or filename.endswith(".safetensors")
        ):
            continue
        if os.path.isdir(src_path):
            shutil.copytree(src_path, dst_path)
            logging.info(f"directory {filename} copied.")
        else:
            shutil.copy(src_path, dst_path)
            logging.info(f"{filename} copied.")


if __name__ == "__main__":
    main()
