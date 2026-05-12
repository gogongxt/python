# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/DeepSeek-V4-Flash`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/DeepSeek-V4-Flash/config.json`

```json

{
  "architectures": [
    "DeepseekV4ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 0,
  "eos_token_id": 1,
  "hc_eps": 1e-06,
  "hc_mult": 4,
  "hc_sinkhorn_iters": 20,
  "head_dim": 512,
  "hidden_act": "silu",
  "hidden_size": 4096,
  "index_head_dim": 128,
  "index_n_heads": 64,
  "index_topk": 512,
  "initializer_range": 0.02,
  "max_position_embeddings": 1048576,
  "model_type": "deepseek_v4",
  "moe_intermediate_size": 2048,
  "n_routed_experts": 256,
  "n_shared_experts": 1,
  "norm_topk_prob": true,
  "num_attention_heads": 64,
  "num_experts_per_tok": 6,
  "num_hidden_layers": 43,
  "num_hash_layers": 3,
  "num_key_value_heads": 1,
  "num_nextn_predict_layers": 1,
  "o_groups": 8,
  "o_lora_rank": 1024,
  "q_lora_rank": 1024,
  "qk_rope_head_dim": 64,
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "e4m3",
    "quant_method": "fp8",
    "scale_fmt": "ue8m0",
    "weight_block_size": [
      128,
      128
    ]
  },
  "rms_norm_eps": 1e-06,
  "rope_scaling": {
    "beta_fast": 32,
    "beta_slow": 1,
    "factor": 16,
    "original_max_position_embeddings": 65536,
    "type": "yarn"
  },
  "rope_theta": 10000,
  "routed_scaling_factor": 1.5,
  "scoring_func": "sqrtsoftplus",
  "sliding_window": 128,
  "swiglu_limit": 10.0,
  "tie_word_embeddings": false,
  "topk_method": "noaux_tc",
  "torch_dtype": "bfloat16",
  "transformers_version": "4.57.1",
  "use_cache": true,
  "vocab_size": 129280,
  "compress_rope_theta": 160000,
  "compress_ratios": [0, 0, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 0]
}

```
</details>

<details><summary>Transformers 配置</summary>

**错误**: Transformers 解析配置失败 - `The checkpoint you are trying to load has model type `deepseek_v4` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.

You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transformers.git``

</details>

# 模型结构

**错误**: 解析模型结构失败

# 权重统计

- **权重文件**: 46 个 `safetensors` 文件
- **文件总大小**: 148.66 GB
- **权重张量数**: 69,187
- **参数总量**: 158,069,433,298
- **张量累计大小**: 148.65 GB
- **压缩**: 69187 → 101 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `embed.weight` | `[129280, 4096]` | `torch.bfloat16` | 1010.00 MB | model-00001-of-00046.safetensors |
| `hc_head_base` | `[4]` | `torch.float32` | 16.00 B | model-00045-of-00046.safetensors |
| `hc_head_fn` | `[4, 16384]` | `torch.float32` | 256.00 KB | model-00045-of-00046.safetensors |
| `hc_head_scale` | `[1]` | `torch.float32` | 4.00 B | model-00045-of-00046.safetensors |
| `head.weight` | `[129280, 4096]` | `torch.bfloat16` | 1010.00 MB | model-00045-of-00046.safetensors |
| `layers.0-2.ffn.gate.tid2eid` (×3 layers) | `[129280, 6]` | `torch.int64` | 17.75 MB | Multi Files |
| `layers.0-42.attn.attn_sink` (×43 layers) | `[64]` | `torch.float32` | 10.75 KB | Multi Files |
| `layers.0-42.attn.kv_norm.weight` (×43 layers) | `[512]` | `torch.bfloat16` | 43.00 KB | Multi Files |
| `layers.0-42.attn.q_norm.weight` (×43 layers) | `[1024]` | `torch.bfloat16` | 86.00 KB | Multi Files |
| `layers.0-42.attn.wkv.scale` (×43 layers) | `[4, 32]` | `torch.float8_e8m0fnu` | 5.38 KB | Multi Files |
| `layers.0-42.attn.wkv.weight` (×43 layers) | `[512, 4096]` | `torch.float8_e4m3fn` | 86.00 MB | Multi Files |
| `layers.0-42.attn.wo_a.scale` (×43 layers) | `[64, 32]` | `torch.float8_e8m0fnu` | 86.00 KB | Multi Files |
| `layers.0-42.attn.wo_a.weight` (×43 layers) | `[8192, 4096]` | `torch.float8_e4m3fn` | 1.34 GB | Multi Files |
| `layers.0-42.attn.wo_b.scale` (×43 layers) | `[32, 64]` | `torch.float8_e8m0fnu` | 86.00 KB | Multi Files |
| `layers.0-42.attn.wo_b.weight` (×43 layers) | `[4096, 8192]` | `torch.float8_e4m3fn` | 1.34 GB | Multi Files |
| `layers.0-42.attn.wq_a.scale` (×43 layers) | `[8, 32]` | `torch.float8_e8m0fnu` | 10.75 KB | Multi Files |
| `layers.0-42.attn.wq_a.weight` (×43 layers) | `[1024, 4096]` | `torch.float8_e4m3fn` | 172.00 MB | Multi Files |
| `layers.0-42.attn.wq_b.scale` (×43 layers) | `[256, 8]` | `torch.float8_e8m0fnu` | 86.00 KB | Multi Files |
| `layers.0-42.attn.wq_b.weight` (×43 layers) | `[32768, 1024]` | `torch.float8_e4m3fn` | 1.34 GB | Multi Files |
| `layers.0-42.attn_norm.weight` (×43 layers) | `[4096]` | `torch.bfloat16` | 344.00 KB | Multi Files |
| `layers.0-42.ffn.experts.0-255.w1.scale` (×43 layers, ×256 experts) | `[2048, 128]` | `torch.float8_e8m0fnu` | 2.69 GB | Multi Files |
| `layers.0-42.ffn.experts.0-255.w1.weight` (×43 layers, ×256 experts) | `[2048, 2048]` | `torch.int8` | 43.00 GB | Multi Files |
| `layers.0-42.ffn.experts.0-255.w2.scale` (×43 layers, ×256 experts) | `[4096, 64]` | `torch.float8_e8m0fnu` | 2.69 GB | Multi Files |
| `layers.0-42.ffn.experts.0-255.w2.weight` (×43 layers, ×256 experts) | `[4096, 1024]` | `torch.int8` | 43.00 GB | Multi Files |
| `layers.0-42.ffn.experts.0-255.w3.scale` (×43 layers, ×256 experts) | `[2048, 128]` | `torch.float8_e8m0fnu` | 2.69 GB | Multi Files |
| `layers.0-42.ffn.experts.0-255.w3.weight` (×43 layers, ×256 experts) | `[2048, 2048]` | `torch.int8` | 43.00 GB | Multi Files |
| `layers.0-42.ffn.gate.weight` (×43 layers) | `[256, 4096]` | `torch.bfloat16` | 86.00 MB | Multi Files |
| `layers.0-42.ffn.shared_experts.w1.scale` (×43 layers) | `[16, 32]` | `torch.float8_e8m0fnu` | 21.50 KB | Multi Files |
| `layers.0-42.ffn.shared_experts.w1.weight` (×43 layers) | `[2048, 4096]` | `torch.float8_e4m3fn` | 344.00 MB | Multi Files |
| `layers.0-42.ffn.shared_experts.w2.scale` (×43 layers) | `[32, 16]` | `torch.float8_e8m0fnu` | 21.50 KB | Multi Files |
| `layers.0-42.ffn.shared_experts.w2.weight` (×43 layers) | `[4096, 2048]` | `torch.float8_e4m3fn` | 344.00 MB | Multi Files |
| `layers.0-42.ffn.shared_experts.w3.scale` (×43 layers) | `[16, 32]` | `torch.float8_e8m0fnu` | 21.50 KB | Multi Files |
| `layers.0-42.ffn.shared_experts.w3.weight` (×43 layers) | `[2048, 4096]` | `torch.float8_e4m3fn` | 344.00 MB | Multi Files |
| `layers.0-42.ffn_norm.weight` (×43 layers) | `[4096]` | `torch.bfloat16` | 344.00 KB | Multi Files |
| `layers.0-42.hc_attn_base` (×43 layers) | `[24]` | `torch.float32` | 4.03 KB | Multi Files |
| `layers.0-42.hc_attn_fn` (×43 layers) | `[24, 16384]` | `torch.float32` | 64.50 MB | Multi Files |
| `layers.0-42.hc_attn_scale` (×43 layers) | `[3]` | `torch.float32` | 516.00 B | Multi Files |
| `layers.0-42.hc_ffn_base` (×43 layers) | `[24]` | `torch.float32` | 4.03 KB | Multi Files |
| `layers.0-42.hc_ffn_fn` (×43 layers) | `[24, 16384]` | `torch.float32` | 64.50 MB | Multi Files |
| `layers.0-42.hc_ffn_scale` (×43 layers) | `[3]` | `torch.float32` | 516.00 B | Multi Files |
| `layers.2,4,...,40,42.attn.compressor.ape` (×21 layers) | `[4, 1024]` | `torch.float32` | 336.00 KB | Multi Files |
| `layers.2,4,...,40,42.attn.compressor.wgate.weight` (×21 layers) | `[1024, 4096]` | `torch.bfloat16` | 168.00 MB | Multi Files |
| `layers.2,4,...,40,42.attn.compressor.wkv.weight` (×21 layers) | `[1024, 4096]` | `torch.bfloat16` | 168.00 MB | Multi Files |
| `layers.2,4,...,40,42.attn.indexer.compressor.ape` (×21 layers) | `[4, 256]` | `torch.float32` | 84.00 KB | Multi Files |
| `layers.2,4,...,40,42.attn.indexer.compressor.norm.weight` (×21 layers) | `[128]` | `torch.bfloat16` | 5.25 KB | Multi Files |
| `layers.2,4,...,40,42.attn.indexer.compressor.wgate.weight` (×21 layers) | `[256, 4096]` | `torch.bfloat16` | 42.00 MB | Multi Files |
| `layers.2,4,...,40,42.attn.indexer.compressor.wkv.weight` (×21 layers) | `[256, 4096]` | `torch.bfloat16` | 42.00 MB | Multi Files |
| `layers.2,4,...,40,42.attn.indexer.weights_proj.weight` (×21 layers) | `[64, 4096]` | `torch.bfloat16` | 10.50 MB | Multi Files |
| `layers.2,4,...,40,42.attn.indexer.wq_b.scale` (×21 layers) | `[64, 8]` | `torch.float8_e8m0fnu` | 10.50 KB | Multi Files |
| `layers.2,4,...,40,42.attn.indexer.wq_b.weight` (×21 layers) | `[8192, 1024]` | `torch.float8_e4m3fn` | 168.00 MB | Multi Files |
| `layers.2-42.attn.compressor.norm.weight` (×41 layers) | `[512]` | `torch.bfloat16` | 41.00 KB | Multi Files |
| `layers.3,5,...,39,41.attn.compressor.ape` (×20 layers) | `[128, 512]` | `torch.float32` | 5.00 MB | Multi Files |
| `layers.3,5,...,39,41.attn.compressor.wgate.weight` (×20 layers) | `[512, 4096]` | `torch.bfloat16` | 80.00 MB | Multi Files |
| `layers.3,5,...,39,41.attn.compressor.wkv.weight` (×20 layers) | `[512, 4096]` | `torch.bfloat16` | 80.00 MB | Multi Files |
| `layers.3-42.ffn.gate.bias` (×40 layers) | `[256]` | `torch.float32` | 40.00 KB | Multi Files |
| `mtp.0.attn.attn_sink` | `[64]` | `torch.float32` | 256.00 B | model-00046-of-00046.safetensors |
| `mtp.0.attn.kv_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00046-of-00046.safetensors |
| `mtp.0.attn.q_norm.weight` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00046-of-00046.safetensors |
| `mtp.0.attn.wkv.scale` | `[4, 32]` | `torch.float8_e8m0fnu` | 128.00 B | model-00046-of-00046.safetensors |
| `mtp.0.attn.wkv.weight` | `[512, 4096]` | `torch.float8_e4m3fn` | 2.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.attn.wo_a.scale` | `[64, 32]` | `torch.float8_e8m0fnu` | 2.00 KB | model-00046-of-00046.safetensors |
| `mtp.0.attn.wo_a.weight` | `[8192, 4096]` | `torch.float8_e4m3fn` | 32.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.attn.wo_b.scale` | `[32, 64]` | `torch.float8_e8m0fnu` | 2.00 KB | model-00046-of-00046.safetensors |
| `mtp.0.attn.wo_b.weight` | `[4096, 8192]` | `torch.float8_e4m3fn` | 32.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.attn.wq_a.scale` | `[8, 32]` | `torch.float8_e8m0fnu` | 256.00 B | model-00046-of-00046.safetensors |
| `mtp.0.attn.wq_a.weight` | `[1024, 4096]` | `torch.float8_e4m3fn` | 4.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.attn.wq_b.scale` | `[256, 8]` | `torch.float8_e8m0fnu` | 2.00 KB | model-00046-of-00046.safetensors |
| `mtp.0.attn.wq_b.weight` | `[32768, 1024]` | `torch.float8_e4m3fn` | 32.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.attn_norm.weight` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00046-of-00046.safetensors |
| `mtp.0.e_proj.scale` | `[32, 32]` | `torch.float8_e8m0fnu` | 1.00 KB | model-00046-of-00046.safetensors |
| `mtp.0.e_proj.weight` | `[4096, 4096]` | `torch.float8_e4m3fn` | 16.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.enorm.weight` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00046-of-00046.safetensors |
| `mtp.0.ffn.experts.0-255.w1.scale` (×256 experts) | `[2048, 128]` | `torch.float8_e8m0fnu` | 64.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.ffn.experts.0-255.w1.weight` (×256 experts) | `[2048, 2048]` | `torch.int8` | 1.00 GB | model-00046-of-00046.safetensors |
| `mtp.0.ffn.experts.0-255.w2.scale` (×256 experts) | `[4096, 64]` | `torch.float8_e8m0fnu` | 64.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.ffn.experts.0-255.w2.weight` (×256 experts) | `[4096, 1024]` | `torch.int8` | 1.00 GB | model-00046-of-00046.safetensors |
| `mtp.0.ffn.experts.0-255.w3.scale` (×256 experts) | `[2048, 128]` | `torch.float8_e8m0fnu` | 64.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.ffn.experts.0-255.w3.weight` (×256 experts) | `[2048, 2048]` | `torch.int8` | 1.00 GB | model-00046-of-00046.safetensors |
| `mtp.0.ffn.gate.bias` | `[256]` | `torch.float32` | 1.00 KB | model-00046-of-00046.safetensors |
| `mtp.0.ffn.gate.weight` | `[256, 4096]` | `torch.bfloat16` | 2.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.ffn.shared_experts.w1.scale` | `[16, 32]` | `torch.float8_e8m0fnu` | 512.00 B | model-00046-of-00046.safetensors |
| `mtp.0.ffn.shared_experts.w1.weight` | `[2048, 4096]` | `torch.float8_e4m3fn` | 8.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.ffn.shared_experts.w2.scale` | `[32, 16]` | `torch.float8_e8m0fnu` | 512.00 B | model-00046-of-00046.safetensors |
| `mtp.0.ffn.shared_experts.w2.weight` | `[4096, 2048]` | `torch.float8_e4m3fn` | 8.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.ffn.shared_experts.w3.scale` | `[16, 32]` | `torch.float8_e8m0fnu` | 512.00 B | model-00046-of-00046.safetensors |
| `mtp.0.ffn.shared_experts.w3.weight` | `[2048, 4096]` | `torch.float8_e4m3fn` | 8.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.ffn_norm.weight` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00046-of-00046.safetensors |
| `mtp.0.h_proj.scale` | `[32, 32]` | `torch.float8_e8m0fnu` | 1.00 KB | model-00046-of-00046.safetensors |
| `mtp.0.h_proj.weight` | `[4096, 4096]` | `torch.float8_e4m3fn` | 16.00 MB | model-00046-of-00046.safetensors |
| `mtp.0.hc_attn_base` | `[24]` | `torch.float32` | 96.00 B | model-00046-of-00046.safetensors |
| `mtp.0.hc_attn_fn` | `[24, 16384]` | `torch.float32` | 1.50 MB | model-00046-of-00046.safetensors |
| `mtp.0.hc_attn_scale` | `[3]` | `torch.float32` | 12.00 B | model-00046-of-00046.safetensors |
| `mtp.0.hc_ffn_base` | `[24]` | `torch.float32` | 96.00 B | model-00046-of-00046.safetensors |
| `mtp.0.hc_ffn_fn` | `[24, 16384]` | `torch.float32` | 1.50 MB | model-00046-of-00046.safetensors |
| `mtp.0.hc_ffn_scale` | `[3]` | `torch.float32` | 12.00 B | model-00046-of-00046.safetensors |
| `mtp.0.hc_head_base` | `[4]` | `torch.float32` | 16.00 B | model-00046-of-00046.safetensors |
| `mtp.0.hc_head_fn` | `[4, 16384]` | `torch.float32` | 256.00 KB | model-00046-of-00046.safetensors |
| `mtp.0.hc_head_scale` | `[1]` | `torch.float32` | 4.00 B | model-00046-of-00046.safetensors |
| `mtp.0.hnorm.weight` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00046-of-00046.safetensors |
| `mtp.0.norm.weight` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00046-of-00046.safetensors |
| `norm.weight` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00045-of-00046.safetensors |

</details>

