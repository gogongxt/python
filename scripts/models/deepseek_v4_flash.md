# 模型信息报告

- **模型路径**: `/nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-V4-Flash`

# 模型配置

- **错误**: 读取模型配置失败 - `The checkpoint you are trying to load has model type `deepseek_v4` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.

You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transformers.git``

<details><summary>原始 config.json</summary>

`/nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-V4-Flash/config.json`

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

# 模型结构

**错误**: 解析模型结构失败 - `The checkpoint you are trying to load has model type `deepseek_v4` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.

You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transformers.git``

# 权重统计

- **权重文件**: 26 个 `safetensors` 文件
- **文件总大小**: 84.32 GB
- **权重张量数**: 39,302
- **参数总量**: 89,721,579,782
- **张量累计大小**: 84.31 GB
- **压缩**: 39302 → 114 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `embed.weight` | `[129280, 4096]` | `torch.bfloat16` | 1010.00 MB | model-00001-of-00046.safetensors |
| `layers.0-2.ffn.gate.tid2eid` (×3 layers) | `[129280, 6]` | `torch.int64` | 17.75 MB | Multi Files |
| `layers.0-25.attn.attn_sink` (×25 layers) | `[64]` | `torch.float32` | 6.25 KB | Multi Files |
| `layers.0-25.attn.kv_norm.weight` (×25 layers) | `[512]` | `torch.bfloat16` | 25.00 KB | Multi Files |
| `layers.0-25.attn.q_norm.weight` (×25 layers) | `[1024]` | `torch.bfloat16` | 50.00 KB | Multi Files |
| `layers.0-25.attn.wkv.scale` (×25 layers) | `[4, 32]` | `torch.float8_e8m0fnu` | 3.12 KB | Multi Files |
| `layers.0-25.attn.wkv.weight` (×25 layers) | `[512, 4096]` | `torch.float8_e4m3fn` | 50.00 MB | Multi Files |
| `layers.0-25.attn.wo_a.scale` (×25 layers) | `[64, 32]` | `torch.float8_e8m0fnu` | 50.00 KB | Multi Files |
| `layers.0-25.attn.wo_a.weight` (×25 layers) | `[8192, 4096]` | `torch.float8_e4m3fn` | 800.00 MB | Multi Files |
| `layers.0-25.attn.wo_b.scale` (×25 layers) | `[32, 64]` | `torch.float8_e8m0fnu` | 50.00 KB | Multi Files |
| `layers.0-25.attn.wo_b.weight` (×25 layers) | `[4096, 8192]` | `torch.float8_e4m3fn` | 800.00 MB | Multi Files |
| `layers.0-25.attn.wq_a.scale` (×25 layers) | `[8, 32]` | `torch.float8_e8m0fnu` | 6.25 KB | Multi Files |
| `layers.0-25.attn.wq_a.weight` (×25 layers) | `[1024, 4096]` | `torch.float8_e4m3fn` | 100.00 MB | Multi Files |
| `layers.0-25.attn.wq_b.scale` (×25 layers) | `[256, 8]` | `torch.float8_e8m0fnu` | 50.00 KB | Multi Files |
| `layers.0-25.attn.wq_b.weight` (×25 layers) | `[32768, 1024]` | `torch.float8_e4m3fn` | 800.00 MB | Multi Files |
| `layers.0-25.attn_norm.weight` (×25 layers) | `[4096]` | `torch.bfloat16` | 200.00 KB | Multi Files |
| `layers.0-25.ffn.experts.0-255.w1.scale` (×25 layers, ×256 experts) | `[2048, 128]` | `torch.float8_e8m0fnu` | 1.56 GB | Multi Files |
| `layers.0-25.ffn.experts.0-255.w1.weight` (×25 layers, ×256 experts) | `[2048, 2048]` | `torch.int8` | 25.00 GB | Multi Files |
| `layers.0-25.ffn.experts.0-255.w2.scale` (×25 layers, ×256 experts) | `[4096, 64]` | `torch.float8_e8m0fnu` | 1.56 GB | Multi Files |
| `layers.0-25.ffn.experts.0-255.w2.weight` (×25 layers, ×256 experts) | `[4096, 1024]` | `torch.int8` | 25.00 GB | Multi Files |
| `layers.0-25.ffn.experts.0-255.w3.scale` (×25 layers, ×256 experts) | `[2048, 128]` | `torch.float8_e8m0fnu` | 1.56 GB | Multi Files |
| `layers.0-25.ffn.experts.0-255.w3.weight` (×25 layers, ×256 experts) | `[2048, 2048]` | `torch.int8` | 25.00 GB | Multi Files |
| `layers.0-25.ffn.gate.weight` (×25 layers) | `[256, 4096]` | `torch.bfloat16` | 50.00 MB | Multi Files |
| `layers.0-25.ffn.shared_experts.w1.scale` (×25 layers) | `[16, 32]` | `torch.float8_e8m0fnu` | 12.50 KB | Multi Files |
| `layers.0-25.ffn.shared_experts.w1.weight` (×25 layers) | `[2048, 4096]` | `torch.float8_e4m3fn` | 200.00 MB | Multi Files |
| `layers.0-25.ffn.shared_experts.w2.scale` (×25 layers) | `[32, 16]` | `torch.float8_e8m0fnu` | 12.50 KB | Multi Files |
| `layers.0-25.ffn.shared_experts.w2.weight` (×25 layers) | `[4096, 2048]` | `torch.float8_e4m3fn` | 200.00 MB | Multi Files |
| `layers.0-25.ffn.shared_experts.w3.scale` (×25 layers) | `[16, 32]` | `torch.float8_e8m0fnu` | 12.50 KB | Multi Files |
| `layers.0-25.ffn.shared_experts.w3.weight` (×25 layers) | `[2048, 4096]` | `torch.float8_e4m3fn` | 200.00 MB | Multi Files |
| `layers.0-25.ffn_norm.weight` (×25 layers) | `[4096]` | `torch.bfloat16` | 200.00 KB | Multi Files |
| `layers.0-25.hc_attn_base` (×25 layers) | `[24]` | `torch.float32` | 2.34 KB | Multi Files |
| `layers.0-25.hc_attn_fn` (×25 layers) | `[24, 16384]` | `torch.float32` | 37.50 MB | Multi Files |
| `layers.0-25.hc_attn_scale` (×25 layers) | `[3]` | `torch.float32` | 300.00 B | Multi Files |
| `layers.0-25.hc_ffn_base` (×25 layers) | `[24]` | `torch.float32` | 2.34 KB | Multi Files |
| `layers.0-25.hc_ffn_fn` (×25 layers) | `[24, 16384]` | `torch.float32` | 37.50 MB | Multi Files |
| `layers.0-25.hc_ffn_scale` (×25 layers) | `[3]` | `torch.float32` | 300.00 B | Multi Files |
| `layers.2-24.attn.indexer.compressor.ape` (×12 layers) | `[4, 256]` | `torch.float32` | 48.00 KB | Multi Files |
| `layers.2-24.attn.indexer.compressor.norm.weight` (×12 layers) | `[128]` | `torch.bfloat16` | 3.00 KB | Multi Files |
| `layers.2-24.attn.indexer.compressor.wgate.weight` (×12 layers) | `[256, 4096]` | `torch.bfloat16` | 24.00 MB | Multi Files |
| `layers.2-24.attn.indexer.compressor.wkv.weight` (×12 layers) | `[256, 4096]` | `torch.bfloat16` | 24.00 MB | Multi Files |
| `layers.2-24.attn.indexer.weights_proj.weight` (×12 layers) | `[64, 4096]` | `torch.bfloat16` | 6.00 MB | Multi Files |
| `layers.2-24.attn.indexer.wq_b.scale` (×12 layers) | `[64, 8]` | `torch.float8_e8m0fnu` | 6.00 KB | Multi Files |
| `layers.2-24.attn.indexer.wq_b.weight` (×12 layers) | `[8192, 1024]` | `torch.float8_e4m3fn` | 96.00 MB | Multi Files |
| `layers.2-25.attn.compressor.norm.weight` (×23 layers) | `[512]` | `torch.bfloat16` | 23.00 KB | Multi Files |
| `layers.2.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00004-of-00046.safetensors |
| `layers.2.attn.compressor.wgate.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00004-of-00046.safetensors |
| `layers.2.attn.compressor.wkv.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00004-of-00046.safetensors |
| `layers.3-25.ffn.gate.bias` (×22 layers) | `[256]` | `torch.float32` | 22.00 KB | Multi Files |
| `layers.3.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00005-of-00046.safetensors |
| `layers.3.attn.compressor.wgate.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00005-of-00046.safetensors |
| `layers.3.attn.compressor.wkv.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00005-of-00046.safetensors |
| `layers.4.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00006-of-00046.safetensors |
| `layers.4.attn.compressor.wgate.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00006-of-00046.safetensors |
| `layers.4.attn.compressor.wkv.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00006-of-00046.safetensors |
| `layers.5.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00007-of-00046.safetensors |
| `layers.5.attn.compressor.wgate.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00007-of-00046.safetensors |
| `layers.5.attn.compressor.wkv.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00007-of-00046.safetensors |
| `layers.6.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00008-of-00046.safetensors |
| `layers.6.attn.compressor.wgate.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00008-of-00046.safetensors |
| `layers.6.attn.compressor.wkv.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00008-of-00046.safetensors |
| `layers.7.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00009-of-00046.safetensors |
| `layers.7.attn.compressor.wgate.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00009-of-00046.safetensors |
| `layers.7.attn.compressor.wkv.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00009-of-00046.safetensors |
| `layers.8.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00010-of-00046.safetensors |
| `layers.8.attn.compressor.wgate.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00010-of-00046.safetensors |
| `layers.8.attn.compressor.wkv.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00010-of-00046.safetensors |
| `layers.9.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00011-of-00046.safetensors |
| `layers.9.attn.compressor.wgate.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00011-of-00046.safetensors |
| `layers.9.attn.compressor.wkv.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00011-of-00046.safetensors |
| `layers.10.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00012-of-00046.safetensors |
| `layers.10.attn.compressor.wgate.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00012-of-00046.safetensors |
| `layers.10.attn.compressor.wkv.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00012-of-00046.safetensors |
| `layers.11.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00013-of-00046.safetensors |
| `layers.11.attn.compressor.wgate.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00013-of-00046.safetensors |
| `layers.11.attn.compressor.wkv.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00013-of-00046.safetensors |
| `layers.12.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00014-of-00046.safetensors |
| `layers.12.attn.compressor.wgate.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00014-of-00046.safetensors |
| `layers.12.attn.compressor.wkv.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00014-of-00046.safetensors |
| `layers.13.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00015-of-00046.safetensors |
| `layers.13.attn.compressor.wgate.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00046.safetensors |
| `layers.13.attn.compressor.wkv.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00046.safetensors |
| `layers.14.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00016-of-00046.safetensors |
| `layers.14.attn.compressor.wgate.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00016-of-00046.safetensors |
| `layers.14.attn.compressor.wkv.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00016-of-00046.safetensors |
| `layers.15.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00017-of-00046.safetensors |
| `layers.15.attn.compressor.wgate.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00017-of-00046.safetensors |
| `layers.15.attn.compressor.wkv.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00017-of-00046.safetensors |
| `layers.16.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00018-of-00046.safetensors |
| `layers.16.attn.compressor.wgate.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00018-of-00046.safetensors |
| `layers.16.attn.compressor.wkv.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00018-of-00046.safetensors |
| `layers.17.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00019-of-00046.safetensors |
| `layers.17.attn.compressor.wgate.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00019-of-00046.safetensors |
| `layers.17.attn.compressor.wkv.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00019-of-00046.safetensors |
| `layers.18.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00020-of-00046.safetensors |
| `layers.18.attn.compressor.wgate.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00020-of-00046.safetensors |
| `layers.18.attn.compressor.wkv.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00020-of-00046.safetensors |
| `layers.19.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00021-of-00046.safetensors |
| `layers.19.attn.compressor.wgate.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00021-of-00046.safetensors |
| `layers.19.attn.compressor.wkv.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00021-of-00046.safetensors |
| `layers.20.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00022-of-00046.safetensors |
| `layers.20.attn.compressor.wgate.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00022-of-00046.safetensors |
| `layers.20.attn.compressor.wkv.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00022-of-00046.safetensors |
| `layers.22.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00024-of-00046.safetensors |
| `layers.22.attn.compressor.wgate.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00024-of-00046.safetensors |
| `layers.22.attn.compressor.wkv.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00024-of-00046.safetensors |
| `layers.23.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00025-of-00046.safetensors |
| `layers.23.attn.compressor.wgate.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00025-of-00046.safetensors |
| `layers.23.attn.compressor.wkv.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00025-of-00046.safetensors |
| `layers.24.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00026-of-00046.safetensors |
| `layers.24.attn.compressor.wgate.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00026-of-00046.safetensors |
| `layers.24.attn.compressor.wkv.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00026-of-00046.safetensors |
| `layers.25.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00027-of-00046.safetensors |
| `layers.25.attn.compressor.wgate.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00027-of-00046.safetensors |
| `layers.25.attn.compressor.wkv.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00027-of-00046.safetensors |

</details>

