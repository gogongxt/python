import argparse
import json
import logging
import os
import resource
import shutil
import sys
import tempfile
from concurrent.futures import ProcessPoolExecutor, as_completed

from safetensors import safe_open
from safetensors.torch import save as save_safetensors
from tqdm import tqdm

GB = 1 << 30


def _read_safetensor_keys(filepath):
    """Read all key names from a safetensors file (lightweight, no tensor data)."""
    keys = []
    with safe_open(filepath, framework="pt") as f:
        keys = list(f.keys())
    return keys


def _read_and_save_shard(args):
    """Read kept weights from a safetensors file and save as a shard directly.

    By saving inside the worker process we avoid:
    1. Transferring large tensors via IPC (only lightweight key lists cross processes).
    2. Serialising tensors on the main thread — save_safetensors now runs in
       parallel across workers.
    """
    filepath, kept_keys, output_dir, shard_index = args
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

    if not result:
        return [], skipped, None, 0

    saved_keys = list(result.keys())
    shard_filename = f"shard_{shard_index}.safetensors.tmp"
    shard_path = os.path.join(output_dir, shard_filename)
    buf = save_safetensors(result, {"format": "pt"})
    with open(shard_path, "wb") as fw:
        fw.write(buf)
    del buf, result

    shard_size = os.path.getsize(shard_path)
    return saved_keys, skipped, shard_filename, shard_size


def _is_layer_key(key, layers):
    """Check if a key belongs to a kept layer.

    Supports both HuggingFace style (``model.layers.X``) and bare style
    (``layers.X``) used by some models like DeepSeek-V4.
    Returns the layer index if it is a layer key, else None.
    """
    for prefix in ("model.layers.", "layers."):
        if key.startswith(prefix):
            rest = key[len(prefix) :]
            layer_str = rest.split(".")[0]
            if layer_str.isdigit():
                return int(layer_str)
    return None


def _collect_kept_keys(model_path, layers):
    """Scan model index or single safetensors file to determine kept keys and source files."""
    index_filename = "model.safetensors.index.json"
    index_path = os.path.join(model_path, index_filename)

    if os.path.exists(index_path):
        with open(index_path) as f:
            data = json.load(f)
        original_metadata = data.get("metadata", {})
        model_files = set()
        kept_keys = set()
        for key, filename in data["weight_map"].items():
            layer_idx = _is_layer_key(key, layers)
            if layer_idx is not None and layer_idx >= layers:
                continue
            kept_keys.add(key)
            model_files.add(filename)
        return kept_keys, model_files, index_filename, original_metadata

    # Single safetensors file without index
    single_file = os.path.join(model_path, "model.safetensors")
    if not os.path.exists(single_file):
        raise FileNotFoundError(
            f"Neither {index_filename} nor model.safetensors found in {model_path}"
        )
    keys = _read_safetensor_keys(single_file)
    kept_keys = set()
    for key in keys:
        layer_idx = _is_layer_key(key, layers)
        if layer_idx is not None and layer_idx >= layers:
            continue
        kept_keys.add(key)
    return kept_keys, {"model.safetensors"}, None, {}


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
        "--num-workers",
        type=int,
        default=4,
        help="number of processes for reading weights",
    )
    args = parser.parse_args()
    # Raise fd limit for multi-process tensor loading
    soft, hard = resource.getrlimit(resource.RLIMIT_NOFILE)
    if soft < hard:
        resource.setrlimit(resource.RLIMIT_NOFILE, (hard, hard))
        logging.info(f"Raised fd limit from {soft} to {hard}")
    if os.path.exists(args.output_path):
        raise FileExistsError(f"Output path already exists: {args.output_path}")

    # Use a temp dir first; rename to final path only on success
    tmp_output = tempfile.mkdtemp(
        dir=os.path.dirname(args.output_path),
        prefix=".model_reduce_tmp_",
    )
    try:
        _do_convert(args, tmp_output)
        os.rename(tmp_output, args.output_path)
    except BaseException:
        # Clean up partial output on any failure (including KeyboardInterrupt)
        if os.path.isdir(tmp_output):
            shutil.rmtree(tmp_output, ignore_errors=True)
        raise


def _do_convert(args, output_path):
    config_filename = "config.json"

    # config.json
    src_path = os.path.join(args.model_path, config_filename)
    dst_path = os.path.join(output_path, config_filename)
    with open(src_path) as f, open(dst_path, "w") as fw:
        config = json.load(f)
        num_layers_key = None
        for k in ("num_hidden_layers", "n_layer", "num_layers"):
            if k in config:
                num_layers_key = k
                break
        if num_layers_key is None:
            raise KeyError(
                "Cannot find layer count key in config.json "
                "(tried num_hidden_layers, n_layer, num_layers)"
            )
        if config[num_layers_key] < args.layers:
            raise ValueError(
                f"Requested {args.layers} layers but model only has {config[num_layers_key]}"
            )
        config[num_layers_key] = args.layers
        json.dump(config, fw, indent=2, ensure_ascii=False)

    # Determine kept keys and source files
    kept_keys, model_files, index_filename, original_metadata = _collect_kept_keys(
        args.model_path, args.layers
    )
    logging.info(f"Keeping {len(kept_keys)} tensors from {len(model_files)} file(s)")

    # Each source file is processed independently: read kept tensors and save
    # as a shard inside the worker process.  Only lightweight key-lists and
    # filenames cross the IPC boundary — no large tensor serialisation on the
    # main thread, and writes happen in parallel.
    file_args = [
        (os.path.join(args.model_path, fn), kept_keys, output_path, i)
        for i, fn in enumerate(model_files)
    ]
    actual_workers = min(args.num_workers, len(file_args))
    logging.info(f"Reading & saving weights with {actual_workers} worker(s)...")

    tmp_shard_info = []  # (tmp_filename, [keys], size)
    skipped_keys = []

    with ProcessPoolExecutor(max_workers=actual_workers) as executor:
        futures = {executor.submit(_read_and_save_shard, fa): fa[0] for fa in file_args}
        pbar = tqdm(total=len(file_args), desc="Reading+writing", unit="file")
        for future in as_completed(futures):
            filepath = futures[future]
            try:
                saved_keys, skipped, shard_filename, shard_size = future.result()
            except Exception as e:
                logging.error(f"Failed to process {filepath}: {e}")
                raise
            skipped_keys.extend(skipped)
            if shard_filename is not None:
                tmp_shard_info.append((shard_filename, saved_keys, shard_size))
                logging.info(
                    f"Saved shard from {os.path.basename(filepath)} "
                    f"({shard_size / GB:.2f} GB, {len(saved_keys)} tensors)"
                )
            pbar.update(1)
        pbar.close()

    if skipped_keys:
        logging.warning(
            f"Skipped {len(skipped_keys)} tensors with unsupported dtype: {skipped_keys[:5]}..."
        )

    # Sort shards by their original order (shard_index embedded in filename)
    tmp_shard_info.sort(key=lambda x: x[0])
    num_shards = len(tmp_shard_info)
    num_digits = len(str(num_shards)) if num_shards else 1
    logging.info(f"Total {num_shards} shard(s)")

    # Rename tmp files to final HuggingFace-style names and build weight_map
    weight_map = {}
    for i, (tmp_name, keys, _size) in enumerate(tmp_shard_info):
        final_filename = (
            f"model-{i + 1:0{num_digits}d}-of-{num_shards:0{num_digits}d}.safetensors"
        )
        os.rename(
            os.path.join(output_path, tmp_name),
            os.path.join(output_path, final_filename),
        )
        for key in keys:
            weight_map[key] = final_filename

    # Write index file
    if index_filename is not None:
        dst_index = os.path.join(output_path, index_filename)
        with open(dst_index, "w") as fw:
            json.dump({"metadata": original_metadata, "weight_map": weight_map}, fw)

    # Other files and directories
    for filename in os.listdir(args.model_path):
        src_path = os.path.join(args.model_path, filename)
        dst_path = os.path.join(output_path, filename)
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
