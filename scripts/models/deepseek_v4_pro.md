# 模型信息报告

- **模型路径**: `/nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-V4-Pro`

# 模型配置

- **错误**: 读取模型配置失败 - `The checkpoint you are trying to load has model type `deepseek_v4` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.

You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transformers.git``

<details><summary>原始 config.json</summary>

`/nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-V4-Pro/config.json`

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
  "hidden_size": 7168,
  "index_head_dim": 128,
  "index_n_heads": 64,
  "index_topk": 1024,
  "initializer_range": 0.02,
  "max_position_embeddings": 1048576,
  "model_type": "deepseek_v4",
  "moe_intermediate_size": 3072,
  "n_routed_experts": 384,
  "n_shared_experts": 1,
  "norm_topk_prob": true,
  "num_attention_heads": 128,
  "num_experts_per_tok": 6,
  "num_hidden_layers": 61,
  "num_hash_layers": 3,
  "num_key_value_heads": 1,
  "num_nextn_predict_layers": 1,
  "o_groups": 16,
  "o_lora_rank": 1024,
  "q_lora_rank": 1536,
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
  "routed_scaling_factor": 2.5,
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
  "compress_ratios": [128, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 128, 4, 0]
}

```
</details>

# 模型结构

**错误**: 解析模型结构失败 - `The checkpoint you are trying to load has model type `deepseek_v4` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.

You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transformers.git``

# 权重统计

- **权重文件**: 64 个 `safetensors` 文件
- **文件总大小**: 805.33 GB
- **权重张量数**: 145,116
- **参数总量**: 861,608,274,846
- **张量累计大小**: 805.32 GB
- **压缩**: 145116 → 278 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `embed.weight` | `[129280, 7168]` | `torch.bfloat16` | 1.73 GB | model-00001-of-00064.safetensors |
| `hc_head_base` | `[4]` | `torch.float32` | 16.00 B | model-00063-of-00064.safetensors |
| `hc_head_fn` | `[4, 28672]` | `torch.float32` | 448.00 KB | model-00063-of-00064.safetensors |
| `hc_head_scale` | `[1]` | `torch.float32` | 4.00 B | model-00063-of-00064.safetensors |
| `head.weight` | `[129280, 7168]` | `torch.bfloat16` | 1.73 GB | model-00063-of-00064.safetensors |
| `layers.0-2.ffn.gate.tid2eid` (×3 layers) | `[129280, 6]` | `torch.int64` | 17.75 MB | Multi Files |
| `layers.0-60.attn.attn_sink` (×61 layers) | `[128]` | `torch.float32` | 30.50 KB | Multi Files |
| `layers.0-60.attn.compressor.norm.weight` (×61 layers) | `[512]` | `torch.bfloat16` | 61.00 KB | Multi Files |
| `layers.0-60.attn.kv_norm.weight` (×61 layers) | `[512]` | `torch.bfloat16` | 61.00 KB | Multi Files |
| `layers.0-60.attn.q_norm.weight` (×61 layers) | `[1536]` | `torch.bfloat16` | 183.00 KB | Multi Files |
| `layers.0-60.attn.wkv.scale` (×61 layers) | `[4, 56]` | `torch.float8_e8m0fnu` | 13.34 KB | Multi Files |
| `layers.0-60.attn.wkv.weight` (×61 layers) | `[512, 7168]` | `torch.float8_e4m3fn` | 213.50 MB | Multi Files |
| `layers.0-60.attn.wo_a.scale` (×61 layers) | `[128, 32]` | `torch.float8_e8m0fnu` | 244.00 KB | Multi Files |
| `layers.0-60.attn.wo_a.weight` (×61 layers) | `[16384, 4096]` | `torch.float8_e4m3fn` | 3.81 GB | Multi Files |
| `layers.0-60.attn.wo_b.scale` (×61 layers) | `[56, 128]` | `torch.float8_e8m0fnu` | 427.00 KB | Multi Files |
| `layers.0-60.attn.wo_b.weight` (×61 layers) | `[7168, 16384]` | `torch.float8_e4m3fn` | 6.67 GB | Multi Files |
| `layers.0-60.attn.wq_a.scale` (×61 layers) | `[12, 56]` | `torch.float8_e8m0fnu` | 40.03 KB | Multi Files |
| `layers.0-60.attn.wq_a.weight` (×61 layers) | `[1536, 7168]` | `torch.float8_e4m3fn` | 640.50 MB | Multi Files |
| `layers.0-60.attn.wq_b.scale` (×61 layers) | `[512, 12]` | `torch.float8_e8m0fnu` | 366.00 KB | Multi Files |
| `layers.0-60.attn.wq_b.weight` (×61 layers) | `[65536, 1536]` | `torch.float8_e4m3fn` | 5.72 GB | Multi Files |
| `layers.0-60.attn_norm.weight` (×61 layers) | `[7168]` | `torch.bfloat16` | 854.00 KB | Multi Files |
| `layers.0-60.ffn.experts.0-383.w1.scale` (×61 layers, ×384 experts) | `[3072, 224]` | `torch.float8_e8m0fnu` | 15.01 GB | Multi Files |
| `layers.0-60.ffn.experts.0-383.w1.weight` (×61 layers, ×384 experts) | `[3072, 3584]` | `torch.int8` | 240.19 GB | Multi Files |
| `layers.0-60.ffn.experts.0-383.w2.scale` (×61 layers, ×384 experts) | `[7168, 96]` | `torch.float8_e8m0fnu` | 15.01 GB | Multi Files |
| `layers.0-60.ffn.experts.0-383.w2.weight` (×61 layers, ×384 experts) | `[7168, 1536]` | `torch.int8` | 240.19 GB | Multi Files |
| `layers.0-60.ffn.experts.0-383.w3.scale` (×61 layers, ×384 experts) | `[3072, 224]` | `torch.float8_e8m0fnu` | 15.01 GB | Multi Files |
| `layers.0-60.ffn.experts.0-383.w3.weight` (×61 layers, ×384 experts) | `[3072, 3584]` | `torch.int8` | 240.19 GB | Multi Files |
| `layers.0-60.ffn.gate.weight` (×61 layers) | `[384, 7168]` | `torch.bfloat16` | 320.25 MB | Multi Files |
| `layers.0-60.ffn.shared_experts.w1.scale` (×61 layers) | `[24, 56]` | `torch.float8_e8m0fnu` | 80.06 KB | Multi Files |
| `layers.0-60.ffn.shared_experts.w1.weight` (×61 layers) | `[3072, 7168]` | `torch.float8_e4m3fn` | 1.25 GB | Multi Files |
| `layers.0-60.ffn.shared_experts.w2.scale` (×61 layers) | `[56, 24]` | `torch.float8_e8m0fnu` | 80.06 KB | Multi Files |
| `layers.0-60.ffn.shared_experts.w2.weight` (×61 layers) | `[7168, 3072]` | `torch.float8_e4m3fn` | 1.25 GB | Multi Files |
| `layers.0-60.ffn.shared_experts.w3.scale` (×61 layers) | `[24, 56]` | `torch.float8_e8m0fnu` | 80.06 KB | Multi Files |
| `layers.0-60.ffn.shared_experts.w3.weight` (×61 layers) | `[3072, 7168]` | `torch.float8_e4m3fn` | 1.25 GB | Multi Files |
| `layers.0-60.ffn_norm.weight` (×61 layers) | `[7168]` | `torch.bfloat16` | 854.00 KB | Multi Files |
| `layers.0-60.hc_attn_base` (×61 layers) | `[24]` | `torch.float32` | 5.72 KB | Multi Files |
| `layers.0-60.hc_attn_fn` (×61 layers) | `[24, 28672]` | `torch.float32` | 160.12 MB | Multi Files |
| `layers.0-60.hc_attn_scale` (×61 layers) | `[3]` | `torch.float32` | 732.00 B | Multi Files |
| `layers.0-60.hc_ffn_base` (×61 layers) | `[24]` | `torch.float32` | 5.72 KB | Multi Files |
| `layers.0-60.hc_ffn_fn` (×61 layers) | `[24, 28672]` | `torch.float32` | 160.12 MB | Multi Files |
| `layers.0-60.hc_ffn_scale` (×61 layers) | `[3]` | `torch.float32` | 732.00 B | Multi Files |
| `layers.0.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00002-of-00064.safetensors |
| `layers.0.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00002-of-00064.safetensors |
| `layers.0.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00002-of-00064.safetensors |
| `layers.1.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00003-of-00064.safetensors |
| `layers.1.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00003-of-00064.safetensors |
| `layers.1.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00003-of-00064.safetensors |
| `layers.2-60.attn.indexer.compressor.ape` (×30 layers) | `[4, 256]` | `torch.float32` | 120.00 KB | Multi Files |
| `layers.2-60.attn.indexer.compressor.norm.weight` (×30 layers) | `[128]` | `torch.bfloat16` | 7.50 KB | Multi Files |
| `layers.2-60.attn.indexer.compressor.wgate.weight` (×30 layers) | `[256, 7168]` | `torch.bfloat16` | 105.00 MB | Multi Files |
| `layers.2-60.attn.indexer.compressor.wkv.weight` (×30 layers) | `[256, 7168]` | `torch.bfloat16` | 105.00 MB | Multi Files |
| `layers.2-60.attn.indexer.weights_proj.weight` (×30 layers) | `[64, 7168]` | `torch.bfloat16` | 26.25 MB | Multi Files |
| `layers.2-60.attn.indexer.wq_b.scale` (×30 layers) | `[64, 12]` | `torch.float8_e8m0fnu` | 22.50 KB | Multi Files |
| `layers.2-60.attn.indexer.wq_b.weight` (×30 layers) | `[8192, 1536]` | `torch.float8_e4m3fn` | 360.00 MB | Multi Files |
| `layers.2.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00004-of-00064.safetensors |
| `layers.2.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00004-of-00064.safetensors |
| `layers.2.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00004-of-00064.safetensors |
| `layers.3-60.ffn.gate.bias` (×58 layers) | `[384]` | `torch.float32` | 87.00 KB | Multi Files |
| `layers.3.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00005-of-00064.safetensors |
| `layers.3.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00005-of-00064.safetensors |
| `layers.3.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00005-of-00064.safetensors |
| `layers.4.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00006-of-00064.safetensors |
| `layers.4.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00006-of-00064.safetensors |
| `layers.4.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00006-of-00064.safetensors |
| `layers.5.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00007-of-00064.safetensors |
| `layers.5.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00007-of-00064.safetensors |
| `layers.5.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00007-of-00064.safetensors |
| `layers.6.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00008-of-00064.safetensors |
| `layers.6.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00008-of-00064.safetensors |
| `layers.6.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00008-of-00064.safetensors |
| `layers.7.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00009-of-00064.safetensors |
| `layers.7.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00009-of-00064.safetensors |
| `layers.7.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00009-of-00064.safetensors |
| `layers.8.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00010-of-00064.safetensors |
| `layers.8.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00010-of-00064.safetensors |
| `layers.8.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00010-of-00064.safetensors |
| `layers.9.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00011-of-00064.safetensors |
| `layers.9.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00011-of-00064.safetensors |
| `layers.9.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00011-of-00064.safetensors |
| `layers.10.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00012-of-00064.safetensors |
| `layers.10.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00012-of-00064.safetensors |
| `layers.10.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00012-of-00064.safetensors |
| `layers.11.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00013-of-00064.safetensors |
| `layers.11.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00013-of-00064.safetensors |
| `layers.11.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00013-of-00064.safetensors |
| `layers.12.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00014-of-00064.safetensors |
| `layers.12.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00014-of-00064.safetensors |
| `layers.12.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00014-of-00064.safetensors |
| `layers.13.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00015-of-00064.safetensors |
| `layers.13.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00015-of-00064.safetensors |
| `layers.13.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00015-of-00064.safetensors |
| `layers.14.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00016-of-00064.safetensors |
| `layers.14.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00016-of-00064.safetensors |
| `layers.14.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00016-of-00064.safetensors |
| `layers.15.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00017-of-00064.safetensors |
| `layers.15.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00017-of-00064.safetensors |
| `layers.15.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00017-of-00064.safetensors |
| `layers.16.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00018-of-00064.safetensors |
| `layers.16.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00018-of-00064.safetensors |
| `layers.16.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00018-of-00064.safetensors |
| `layers.17.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00019-of-00064.safetensors |
| `layers.17.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00019-of-00064.safetensors |
| `layers.17.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00019-of-00064.safetensors |
| `layers.18.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00020-of-00064.safetensors |
| `layers.18.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00020-of-00064.safetensors |
| `layers.18.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00020-of-00064.safetensors |
| `layers.19.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00021-of-00064.safetensors |
| `layers.19.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00021-of-00064.safetensors |
| `layers.19.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00021-of-00064.safetensors |
| `layers.20.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00022-of-00064.safetensors |
| `layers.20.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00022-of-00064.safetensors |
| `layers.20.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00022-of-00064.safetensors |
| `layers.21.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00023-of-00064.safetensors |
| `layers.21.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00023-of-00064.safetensors |
| `layers.21.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00023-of-00064.safetensors |
| `layers.22.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00024-of-00064.safetensors |
| `layers.22.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00024-of-00064.safetensors |
| `layers.22.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00024-of-00064.safetensors |
| `layers.23.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00025-of-00064.safetensors |
| `layers.23.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00025-of-00064.safetensors |
| `layers.23.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00025-of-00064.safetensors |
| `layers.24.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00026-of-00064.safetensors |
| `layers.24.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00026-of-00064.safetensors |
| `layers.24.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00026-of-00064.safetensors |
| `layers.25.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00027-of-00064.safetensors |
| `layers.25.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00027-of-00064.safetensors |
| `layers.25.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00027-of-00064.safetensors |
| `layers.26.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00028-of-00064.safetensors |
| `layers.26.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00028-of-00064.safetensors |
| `layers.26.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00028-of-00064.safetensors |
| `layers.27.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00029-of-00064.safetensors |
| `layers.27.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00029-of-00064.safetensors |
| `layers.27.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00029-of-00064.safetensors |
| `layers.28.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00030-of-00064.safetensors |
| `layers.28.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00030-of-00064.safetensors |
| `layers.28.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00030-of-00064.safetensors |
| `layers.29.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00031-of-00064.safetensors |
| `layers.29.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00031-of-00064.safetensors |
| `layers.29.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00031-of-00064.safetensors |
| `layers.30.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00032-of-00064.safetensors |
| `layers.30.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00032-of-00064.safetensors |
| `layers.30.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00032-of-00064.safetensors |
| `layers.31.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00033-of-00064.safetensors |
| `layers.31.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00033-of-00064.safetensors |
| `layers.31.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00033-of-00064.safetensors |
| `layers.32.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00034-of-00064.safetensors |
| `layers.32.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00034-of-00064.safetensors |
| `layers.32.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00034-of-00064.safetensors |
| `layers.33.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00035-of-00064.safetensors |
| `layers.33.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00035-of-00064.safetensors |
| `layers.33.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00035-of-00064.safetensors |
| `layers.34.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00036-of-00064.safetensors |
| `layers.34.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00036-of-00064.safetensors |
| `layers.34.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00036-of-00064.safetensors |
| `layers.35.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00037-of-00064.safetensors |
| `layers.35.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00037-of-00064.safetensors |
| `layers.35.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00037-of-00064.safetensors |
| `layers.36.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00038-of-00064.safetensors |
| `layers.36.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00038-of-00064.safetensors |
| `layers.36.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00038-of-00064.safetensors |
| `layers.37.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00039-of-00064.safetensors |
| `layers.37.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00039-of-00064.safetensors |
| `layers.37.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00039-of-00064.safetensors |
| `layers.38.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00040-of-00064.safetensors |
| `layers.38.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00040-of-00064.safetensors |
| `layers.38.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00040-of-00064.safetensors |
| `layers.39.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00041-of-00064.safetensors |
| `layers.39.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00041-of-00064.safetensors |
| `layers.39.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00041-of-00064.safetensors |
| `layers.40.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00042-of-00064.safetensors |
| `layers.40.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00042-of-00064.safetensors |
| `layers.40.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00042-of-00064.safetensors |
| `layers.41.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00043-of-00064.safetensors |
| `layers.41.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00043-of-00064.safetensors |
| `layers.41.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00043-of-00064.safetensors |
| `layers.42.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00044-of-00064.safetensors |
| `layers.42.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00044-of-00064.safetensors |
| `layers.42.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00044-of-00064.safetensors |
| `layers.43.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00045-of-00064.safetensors |
| `layers.43.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00045-of-00064.safetensors |
| `layers.43.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00045-of-00064.safetensors |
| `layers.44.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00046-of-00064.safetensors |
| `layers.44.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00046-of-00064.safetensors |
| `layers.44.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00046-of-00064.safetensors |
| `layers.45.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00047-of-00064.safetensors |
| `layers.45.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00047-of-00064.safetensors |
| `layers.45.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00047-of-00064.safetensors |
| `layers.46.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00048-of-00064.safetensors |
| `layers.46.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00048-of-00064.safetensors |
| `layers.46.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00048-of-00064.safetensors |
| `layers.47.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00049-of-00064.safetensors |
| `layers.47.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00049-of-00064.safetensors |
| `layers.47.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00049-of-00064.safetensors |
| `layers.48.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00050-of-00064.safetensors |
| `layers.48.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00050-of-00064.safetensors |
| `layers.48.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00050-of-00064.safetensors |
| `layers.49.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00051-of-00064.safetensors |
| `layers.49.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00051-of-00064.safetensors |
| `layers.49.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00051-of-00064.safetensors |
| `layers.50.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00052-of-00064.safetensors |
| `layers.50.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00052-of-00064.safetensors |
| `layers.50.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00052-of-00064.safetensors |
| `layers.51.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00053-of-00064.safetensors |
| `layers.51.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00053-of-00064.safetensors |
| `layers.51.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00053-of-00064.safetensors |
| `layers.52.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00054-of-00064.safetensors |
| `layers.52.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00054-of-00064.safetensors |
| `layers.52.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00054-of-00064.safetensors |
| `layers.53.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00055-of-00064.safetensors |
| `layers.53.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00055-of-00064.safetensors |
| `layers.53.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00055-of-00064.safetensors |
| `layers.54.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00056-of-00064.safetensors |
| `layers.54.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00056-of-00064.safetensors |
| `layers.54.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00056-of-00064.safetensors |
| `layers.55.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00057-of-00064.safetensors |
| `layers.55.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00057-of-00064.safetensors |
| `layers.55.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00057-of-00064.safetensors |
| `layers.56.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00058-of-00064.safetensors |
| `layers.56.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00058-of-00064.safetensors |
| `layers.56.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00058-of-00064.safetensors |
| `layers.57.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00059-of-00064.safetensors |
| `layers.57.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00059-of-00064.safetensors |
| `layers.57.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00059-of-00064.safetensors |
| `layers.58.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00060-of-00064.safetensors |
| `layers.58.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00060-of-00064.safetensors |
| `layers.58.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00060-of-00064.safetensors |
| `layers.59.attn.compressor.ape` | `[128, 512]` | `torch.float32` | 256.00 KB | model-00061-of-00064.safetensors |
| `layers.59.attn.compressor.wgate.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00061-of-00064.safetensors |
| `layers.59.attn.compressor.wkv.weight` | `[512, 7168]` | `torch.bfloat16` | 7.00 MB | model-00061-of-00064.safetensors |
| `layers.60.attn.compressor.ape` | `[4, 1024]` | `torch.float32` | 16.00 KB | model-00062-of-00064.safetensors |
| `layers.60.attn.compressor.wgate.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00062-of-00064.safetensors |
| `layers.60.attn.compressor.wkv.weight` | `[1024, 7168]` | `torch.bfloat16` | 14.00 MB | model-00062-of-00064.safetensors |
| `mtp.0.attn.attn_sink` (×1 mtp) | `[128]` | `torch.float32` | 512.00 B | model-00064-of-00064.safetensors |
| `mtp.0.attn.kv_norm.weight` (×1 mtp) | `[512]` | `torch.bfloat16` | 1.00 KB | model-00064-of-00064.safetensors |
| `mtp.0.attn.q_norm.weight` (×1 mtp) | `[1536]` | `torch.bfloat16` | 3.00 KB | model-00064-of-00064.safetensors |
| `mtp.0.attn.wkv.scale` (×1 mtp) | `[4, 56]` | `torch.float8_e8m0fnu` | 224.00 B | model-00064-of-00064.safetensors |
| `mtp.0.attn.wkv.weight` (×1 mtp) | `[512, 7168]` | `torch.float8_e4m3fn` | 3.50 MB | model-00064-of-00064.safetensors |
| `mtp.0.attn.wo_a.scale` (×1 mtp) | `[128, 32]` | `torch.float8_e8m0fnu` | 4.00 KB | model-00064-of-00064.safetensors |
| `mtp.0.attn.wo_a.weight` (×1 mtp) | `[16384, 4096]` | `torch.float8_e4m3fn` | 64.00 MB | model-00064-of-00064.safetensors |
| `mtp.0.attn.wo_b.scale` (×1 mtp) | `[56, 128]` | `torch.float8_e8m0fnu` | 7.00 KB | model-00064-of-00064.safetensors |
| `mtp.0.attn.wo_b.weight` (×1 mtp) | `[7168, 16384]` | `torch.float8_e4m3fn` | 112.00 MB | model-00064-of-00064.safetensors |
| `mtp.0.attn.wq_a.scale` (×1 mtp) | `[12, 56]` | `torch.float8_e8m0fnu` | 672.00 B | model-00064-of-00064.safetensors |
| `mtp.0.attn.wq_a.weight` (×1 mtp) | `[1536, 7168]` | `torch.float8_e4m3fn` | 10.50 MB | model-00064-of-00064.safetensors |
| `mtp.0.attn.wq_b.scale` (×1 mtp) | `[512, 12]` | `torch.float8_e8m0fnu` | 6.00 KB | model-00064-of-00064.safetensors |
| `mtp.0.attn.wq_b.weight` (×1 mtp) | `[65536, 1536]` | `torch.float8_e4m3fn` | 96.00 MB | model-00064-of-00064.safetensors |
| `mtp.0.attn_norm.weight` (×1 mtp) | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00064-of-00064.safetensors |
| `mtp.0.e_proj.scale` (×1 mtp) | `[56, 56]` | `torch.float8_e8m0fnu` | 3.06 KB | model-00064-of-00064.safetensors |
| `mtp.0.e_proj.weight` (×1 mtp) | `[7168, 7168]` | `torch.float8_e4m3fn` | 49.00 MB | model-00064-of-00064.safetensors |
| `mtp.0.enorm.weight` (×1 mtp) | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.experts.0-383.w1.scale` (×1 mtp, ×384 experts) | `[3072, 224]` | `torch.float8_e8m0fnu` | 252.00 MB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.experts.0-383.w1.weight` (×1 mtp, ×384 experts) | `[3072, 3584]` | `torch.int8` | 3.94 GB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.experts.0-383.w2.scale` (×1 mtp, ×384 experts) | `[7168, 96]` | `torch.float8_e8m0fnu` | 252.00 MB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.experts.0-383.w2.weight` (×1 mtp, ×384 experts) | `[7168, 1536]` | `torch.int8` | 3.94 GB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.experts.0-383.w3.scale` (×1 mtp, ×384 experts) | `[3072, 224]` | `torch.float8_e8m0fnu` | 252.00 MB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.experts.0-383.w3.weight` (×1 mtp, ×384 experts) | `[3072, 3584]` | `torch.int8` | 3.94 GB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.gate.bias` (×1 mtp) | `[384]` | `torch.float32` | 1.50 KB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.gate.weight` (×1 mtp) | `[384, 7168]` | `torch.bfloat16` | 5.25 MB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.shared_experts.w1.scale` (×1 mtp) | `[24, 56]` | `torch.float8_e8m0fnu` | 1.31 KB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.shared_experts.w1.weight` (×1 mtp) | `[3072, 7168]` | `torch.float8_e4m3fn` | 21.00 MB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.shared_experts.w2.scale` (×1 mtp) | `[56, 24]` | `torch.float8_e8m0fnu` | 1.31 KB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.shared_experts.w2.weight` (×1 mtp) | `[7168, 3072]` | `torch.float8_e4m3fn` | 21.00 MB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.shared_experts.w3.scale` (×1 mtp) | `[24, 56]` | `torch.float8_e8m0fnu` | 1.31 KB | model-00064-of-00064.safetensors |
| `mtp.0.ffn.shared_experts.w3.weight` (×1 mtp) | `[3072, 7168]` | `torch.float8_e4m3fn` | 21.00 MB | model-00064-of-00064.safetensors |
| `mtp.0.ffn_norm.weight` (×1 mtp) | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00064-of-00064.safetensors |
| `mtp.0.h_proj.scale` (×1 mtp) | `[56, 56]` | `torch.float8_e8m0fnu` | 3.06 KB | model-00064-of-00064.safetensors |
| `mtp.0.h_proj.weight` (×1 mtp) | `[7168, 7168]` | `torch.float8_e4m3fn` | 49.00 MB | model-00064-of-00064.safetensors |
| `mtp.0.hc_attn_base` (×1 mtp) | `[24]` | `torch.float32` | 96.00 B | model-00064-of-00064.safetensors |
| `mtp.0.hc_attn_fn` (×1 mtp) | `[24, 28672]` | `torch.float32` | 2.62 MB | model-00064-of-00064.safetensors |
| `mtp.0.hc_attn_scale` (×1 mtp) | `[3]` | `torch.float32` | 12.00 B | model-00064-of-00064.safetensors |
| `mtp.0.hc_ffn_base` (×1 mtp) | `[24]` | `torch.float32` | 96.00 B | model-00064-of-00064.safetensors |
| `mtp.0.hc_ffn_fn` (×1 mtp) | `[24, 28672]` | `torch.float32` | 2.62 MB | model-00064-of-00064.safetensors |
| `mtp.0.hc_ffn_scale` (×1 mtp) | `[3]` | `torch.float32` | 12.00 B | model-00064-of-00064.safetensors |
| `mtp.0.hc_head_base` (×1 mtp) | `[4]` | `torch.float32` | 16.00 B | model-00064-of-00064.safetensors |
| `mtp.0.hc_head_fn` (×1 mtp) | `[4, 28672]` | `torch.float32` | 448.00 KB | model-00064-of-00064.safetensors |
| `mtp.0.hc_head_scale` (×1 mtp) | `[1]` | `torch.float32` | 4.00 B | model-00064-of-00064.safetensors |
| `mtp.0.hnorm.weight` (×1 mtp) | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00064-of-00064.safetensors |
| `mtp.0.norm.weight` (×1 mtp) | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00064-of-00064.safetensors |
| `norm.weight` | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00063-of-00064.safetensors |

</details>

