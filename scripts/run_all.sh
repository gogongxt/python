#!/usr/bin/env bash

# 模型路径数组
models=(
  "/nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-V3"
  "/nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-R1"
  "/nfs/ofs-llm-ssd/models/opensource/DeepSeek-R1-Distill-Qwen-7B"
  "/nfs/ofs-llm-ssd/models/opensource/DeepSeek-V3.1"
  "/nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-V3.2"
  "/nfs/ofs-llm-ssd/models/opensource/DeepSeek-V4-Flash"
  "/nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-V4-Pro"
  "/nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-OCR"

  "/nfs/ofs-llm-ssd/models/opensource/GLM-4.5-FP8"
  "/nfs/ofs-llm-ssd/models/opensource/GLM-4.5V"
  "/nfs/ofs-llm-ssd/models/opensource/GLM-4.7-Flash"
  "/nfs/ofs-llm-ssd/models/opensource/GLM-5.1"
  "/nfs/ofs-llab-cold/model/zai-org/GLM-5.1-FP8"
  "/nfs/ofs-llm-ssd/models/opensource/GLM-5.1-w8a8"
  "/nfs/ofs-luban-data/model/ZhipuAI/GLM-5.2"
  "/nfs/ofs-luban-data/model/ZhipuAI/GLM-5.2-FP8"

  "/nfs/ofs-llm-ssd/models/opensource/QwQ-32B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen2-0.5B-Instruct"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen2-7B-Instruct"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen2.5-0.5B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen2.5-1.5B-Instruct"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen2.5-3B-Instruct"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen2.5-72B-Instruct"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen2.5-7B-Instruct"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen2.5-Coder-7B-Instruct"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-0.6B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-14B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-235B-A22B-Instruct-2507"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-235B-A22B-Instruct-2507-FP8"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-30B-A3B-Instruct-2507"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-30B-A3B-Thinking-2507"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-30B-A3B-Thinking-2507-FP8"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-32B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-8B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-Embedding-0.6B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-Embedding-8B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-Next-80B-A3B-Instruct"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-Reranker-0.6B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-Reranker-8B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-VL-235B-A22B-Instruct"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-VL-30B-A3B-Instruct"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3-VL-8B-Instruct"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3.5-0.8B-Base"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3.5-27B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3.5-35B-A3B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3.5-4B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3.6-27B"
  "/nfs/ofs-llm-ssd/models/opensource/Qwen3.6-35B-A3B"

  "/nfs/ofs-llab-cold/model/moonshotai/Kimi-K2-Instruct"
  "/nfs/ofs-llab-cold/model/moonshotai/Kimi-Linear-48B-A3B-Instruct"
  "/nfs/ofs-llab-cold/model/moonshotai/Kimi-K2.5"
  "/nfs/ofs-luban-data/model/moonshotai/Kimi-K2.6"

  "/nfs/ofs-llm-ssd/models/opensource/gpt-oss-20b"
  "/nfs/ofs-llm-ssd/models/opensource/gpt-oss-20b-bf16"

  "/nfs/ofs-llm-ssd/models/opensource/Llama-3.2-3B-Instruct"
  "/nfs/ofs-llm-ssd/models/opensource/Meta-Llama-3-8B-Instruct"
  "/nfs/ofs-llm-ssd/models/opensource/Meta-Llama-3.1-8B-Instruct"

  "/nfs/ofs-llm-ssd/models/opensource/MiniMax-M2.7"
  "/nfs/ofs-luban-data/model/MiniMax/MiniMax-M3"
  "/nfs/ofs-luban-data/model/MiniMax/MiniMax-M3-MXFP8"

  "/nfs/ofs-luban-data/model/XiaomiMiMo/MiMo-V2.5"
  "/nfs/ofs-luban-data/model/XiaomiMiMo/MiMo-V2.5-Pro"

  "/nfs/ofs-llm-ssd/models/opensource/gemma-4-31B-it"
)

export HF_TRUST_REMOTE_CODE=True

# 并发数（可按 CPU/内存 调整）
MAX_WORKERS=${MAX_WORKERS:-16}

run_one() {
  local model_path="$1"
  echo "========================================"
  echo "Processing model: ${model_path}"
  echo "========================================"
  python3 model_inspector.py -f --num-workers 1 --model-path "${model_path}"
  echo
}
export -f run_one

printf '%s\n' "${models[@]}" | xargs -P "${MAX_WORKERS}" -I {} bash -c 'run_one "$@"' _ {}

echo "All models processed."
