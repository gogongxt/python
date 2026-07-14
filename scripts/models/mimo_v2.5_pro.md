# 模型信息报告

- **模型路径**: `/nfs/ofs-luban-data/model/XiaomiMiMo/MiMo-V2.5-Pro`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-luban-data/model/XiaomiMiMo/MiMo-V2.5-Pro/config.json`

```json

{
  "architectures": [
    "MiMoV2ForCausalLM"
  ],
  "auto_map": {
    "AutoConfig": "configuration_mimo_v2.MiMoV2Config",
    "AutoModel": "modeling_mimo_v2.MiMoV2Model",
    "AutoModelForCausalLM": "modeling_mimo_v2.MiMoV2ForCausalLM"
  },
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "e4m3",
    "quant_method": "fp8",
    "weight_block_size": [
      128,
      128
    ],
    "ignored_layers": [
      "model.layers.0.self_attn.o_proj",
      "model.layers.1.self_attn.o_proj",
      "model.layers.2.self_attn.o_proj",
      "model.layers.3.self_attn.o_proj",
      "model.layers.4.self_attn.o_proj",
      "model.layers.5.self_attn.o_proj",
      "model.layers.6.self_attn.o_proj",
      "model.layers.7.self_attn.o_proj",
      "model.layers.8.self_attn.o_proj",
      "model.layers.9.self_attn.o_proj",
      "model.layers.10.self_attn.o_proj",
      "model.layers.11.self_attn.o_proj",
      "model.layers.12.self_attn.o_proj",
      "model.layers.13.self_attn.o_proj",
      "model.layers.14.self_attn.o_proj",
      "model.layers.15.self_attn.o_proj",
      "model.layers.16.self_attn.o_proj",
      "model.layers.17.self_attn.o_proj",
      "model.layers.18.self_attn.o_proj",
      "model.layers.19.self_attn.o_proj",
      "model.layers.20.self_attn.o_proj",
      "model.layers.21.self_attn.o_proj",
      "model.layers.22.self_attn.o_proj",
      "model.layers.23.self_attn.o_proj",
      "model.layers.24.self_attn.o_proj",
      "model.layers.25.self_attn.o_proj",
      "model.layers.26.self_attn.o_proj",
      "model.layers.27.self_attn.o_proj",
      "model.layers.28.self_attn.o_proj",
      "model.layers.29.self_attn.o_proj",
      "model.layers.30.self_attn.o_proj",
      "model.layers.31.self_attn.o_proj",
      "model.layers.32.self_attn.o_proj",
      "model.layers.33.self_attn.o_proj",
      "model.layers.34.self_attn.o_proj",
      "model.layers.35.self_attn.o_proj",
      "model.layers.36.self_attn.o_proj",
      "model.layers.37.self_attn.o_proj",
      "model.layers.38.self_attn.o_proj",
      "model.layers.39.self_attn.o_proj",
      "model.layers.40.self_attn.o_proj",
      "model.layers.41.self_attn.o_proj",
      "model.layers.42.self_attn.o_proj",
      "model.layers.43.self_attn.o_proj",
      "model.layers.44.self_attn.o_proj",
      "model.layers.45.self_attn.o_proj",
      "model.layers.46.self_attn.o_proj",
      "model.layers.47.self_attn.o_proj",
      "model.layers.48.self_attn.o_proj",
      "model.layers.49.self_attn.o_proj",
      "model.layers.50.self_attn.o_proj",
      "model.layers.51.self_attn.o_proj",
      "model.layers.52.self_attn.o_proj",
      "model.layers.53.self_attn.o_proj",
      "model.layers.54.self_attn.o_proj",
      "model.layers.55.self_attn.o_proj",
      "model.layers.56.self_attn.o_proj",
      "model.layers.57.self_attn.o_proj",
      "model.layers.58.self_attn.o_proj",
      "model.layers.59.self_attn.o_proj",
      "model.layers.60.self_attn.o_proj",
      "model.layers.61.self_attn.o_proj",
      "model.layers.62.self_attn.o_proj",
      "model.layers.63.self_attn.o_proj",
      "model.layers.64.self_attn.o_proj",
      "model.layers.65.self_attn.o_proj",
      "model.layers.66.self_attn.o_proj",
      "model.layers.67.self_attn.o_proj",
      "model.layers.68.self_attn.o_proj",
      "model.layers.69.self_attn.o_proj",
      "model.decoder.self_attn.o_proj"
    ]
  },
  "add_full_attention_sink_bias": false,
  "add_swa_attention_sink_bias": true,
  "attention_bias": false,
  "attention_chunk_size": 128,
  "attention_dropout": 0.0,
  "attention_projection_layout": "fused_qkv",
  "attention_value_scale": 0.612,
  "head_dim": 192,
  "hidden_act": "silu",
  "hidden_size": 6144,
  "hybrid_layer_pattern": [
    0, 1, 1, 1, 1, 1, 1,
    0, 1, 1, 1, 1, 1, 1, 1,
    0, 1, 1, 1, 1, 1, 1, 1,
    0, 1, 1, 1, 1, 1, 1, 1,
    0, 1, 1, 1, 1, 1, 1, 1,
    0, 1, 1, 1, 1, 1, 1, 1,
    0, 1, 1, 1, 1, 1, 1, 1,
    0, 1, 1, 1, 1, 1, 1,
    0, 1, 1, 1, 1, 1, 1,
    0
  ],
  "initializer_range": 0.02,
  "intermediate_size": 16384,
  "layernorm_epsilon": 1e-05,
  "max_position_embeddings": 1048576,
  "model_type": "mimo_v2",
  "moe_intermediate_size": 2048,
  "moe_layer_freq": [
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1
  ],
  "n_group": 1,
  "n_routed_experts": 384,
  "n_shared_experts": null,
  "norm_topk_prob": true,
  "num_attention_heads": 128,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 70,
  "num_key_value_heads": 8,
  "partial_rotary_factor": 0.334,
  "rope_theta": 10000000,
  "routed_scaling_factor": null,
  "scoring_func": "sigmoid",
  "sliding_window": 128,
  "sliding_window_size": 128,
  "swa_head_dim": 192,
  "swa_num_attention_heads": 128,
  "swa_num_key_value_heads": 8,
  "swa_rope_theta": 10000,
  "swa_v_head_dim": 128,
  "tie_word_embeddings": false,
  "topk_group": 1,
  "topk_method": "noaux_tc",
  "torch_dtype": "bfloat16",
  "transformers_version": "4.57.1",
  "use_cache": true,
  "v_head_dim": 128,
  "vocab_size": 152576
}
```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `MiMoV2Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 6144
- **层数**: 70
- **注意力头数**: 128
- **词表大小**: 152576
- **中间层大小**: 16384

```
MiMoV2Config {
  "add_full_attention_sink_bias": false,
  "add_swa_attention_sink_bias": true,
  "architectures": [
    "MiMoV2ForCausalLM"
  ],
  "attention_bias": false,
  "attention_chunk_size": 128,
  "attention_dropout": 0.0,
  "attention_projection_layout": "fused_qkv",
  "attention_value_scale": 0.612,
  "auto_map": {
    "AutoConfig": "configuration_mimo_v2.MiMoV2Config",
    "AutoModel": "modeling_mimo_v2.MiMoV2Model",
    "AutoModelForCausalLM": "modeling_mimo_v2.MiMoV2ForCausalLM"
  },
  "dtype": "bfloat16",
  "head_dim": 192,
  "hidden_act": "silu",
  "hidden_size": 6144,
  "hybrid_block_size": null,
  "hybrid_layer_pattern": [
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    0
  ],
  "initializer_range": 0.02,
  "intermediate_size": 16384,
  "layernorm_epsilon": 1e-05,
  "max_position_embeddings": 1048576,
  "model_type": "mimo_v2",
  "moe_intermediate_size": 2048,
  "moe_layer_freq": [
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
  ],
  "n_group": 1,
  "n_routed_experts": 384,
  "n_shared_experts": null,
  "norm_topk_prob": true,
  "num_attention_heads": 128,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 70,
  "num_key_value_heads": 8,
  "partial_rotary_factor": 0.334,
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "e4m3",
    "ignored_layers": [
      "model.layers.0.self_attn.o_proj",
      "model.layers.1.self_attn.o_proj",
      "model.layers.2.self_attn.o_proj",
      "model.layers.3.self_attn.o_proj",
      "model.layers.4.self_attn.o_proj",
      "model.layers.5.self_attn.o_proj",
      "model.layers.6.self_attn.o_proj",
      "model.layers.7.self_attn.o_proj",
      "model.layers.8.self_attn.o_proj",
      "model.layers.9.self_attn.o_proj",
      "model.layers.10.self_attn.o_proj",
      "model.layers.11.self_attn.o_proj",
      "model.layers.12.self_attn.o_proj",
      "model.layers.13.self_attn.o_proj",
      "model.layers.14.self_attn.o_proj",
      "model.layers.15.self_attn.o_proj",
      "model.layers.16.self_attn.o_proj",
      "model.layers.17.self_attn.o_proj",
      "model.layers.18.self_attn.o_proj",
      "model.layers.19.self_attn.o_proj",
      "model.layers.20.self_attn.o_proj",
      "model.layers.21.self_attn.o_proj",
      "model.layers.22.self_attn.o_proj",
      "model.layers.23.self_attn.o_proj",
      "model.layers.24.self_attn.o_proj",
      "model.layers.25.self_attn.o_proj",
      "model.layers.26.self_attn.o_proj",
      "model.layers.27.self_attn.o_proj",
      "model.layers.28.self_attn.o_proj",
      "model.layers.29.self_attn.o_proj",
      "model.layers.30.self_attn.o_proj",
      "model.layers.31.self_attn.o_proj",
      "model.layers.32.self_attn.o_proj",
      "model.layers.33.self_attn.o_proj",
      "model.layers.34.self_attn.o_proj",
      "model.layers.35.self_attn.o_proj",
      "model.layers.36.self_attn.o_proj",
      "model.layers.37.self_attn.o_proj",
      "model.layers.38.self_attn.o_proj",
      "model.layers.39.self_attn.o_proj",
      "model.layers.40.self_attn.o_proj",
      "model.layers.41.self_attn.o_proj",
      "model.layers.42.self_attn.o_proj",
      "model.layers.43.self_attn.o_proj",
      "model.layers.44.self_attn.o_proj",
      "model.layers.45.self_attn.o_proj",
      "model.layers.46.self_attn.o_proj",
      "model.layers.47.self_attn.o_proj",
      "model.layers.48.self_attn.o_proj",
      "model.layers.49.self_attn.o_proj",
      "model.layers.50.self_attn.o_proj",
      "model.layers.51.self_attn.o_proj",
      "model.layers.52.self_attn.o_proj",
      "model.layers.53.self_attn.o_proj",
      "model.layers.54.self_attn.o_proj",
      "model.layers.55.self_attn.o_proj",
      "model.layers.56.self_attn.o_proj",
      "model.layers.57.self_attn.o_proj",
      "model.layers.58.self_attn.o_proj",
      "model.layers.59.self_attn.o_proj",
      "model.layers.60.self_attn.o_proj",
      "model.layers.61.self_attn.o_proj",
      "model.layers.62.self_attn.o_proj",
      "model.layers.63.self_attn.o_proj",
      "model.layers.64.self_attn.o_proj",
      "model.layers.65.self_attn.o_proj",
      "model.layers.66.self_attn.o_proj",
      "model.layers.67.self_attn.o_proj",
      "model.layers.68.self_attn.o_proj",
      "model.layers.69.self_attn.o_proj",
      "model.decoder.self_attn.o_proj"
    ],
    "quant_method": "fp8",
    "weight_block_size": [
      128,
      128
    ]
  },
  "rope_parameters": {
    "partial_rotary_factor": 0.334,
    "rope_theta": 10000000,
    "rope_type": "default"
  },
  "rope_theta": 10000000,
  "routed_scaling_factor": null,
  "scoring_func": "sigmoid",
  "sliding_window": 128,
  "sliding_window_size": 128,
  "swa_head_dim": 192,
  "swa_num_attention_heads": 128,
  "swa_num_key_value_heads": 8,
  "swa_rope_theta": 10000,
  "swa_v_head_dim": 128,
  "tie_word_embeddings": false,
  "topk_group": 1,
  "topk_method": "noaux_tc",
  "transformers_version": "5.7.0",
  "use_cache": true,
  "v_head_dim": 128,
  "vocab_size": 152576
}

```

</details>

# 模型结构

**模型类**: `MiMoV2Config` (当前 transformers 版本不支持实例化)

# 权重统计

- **权重文件**: 34 个 `safetensors` 文件
- **文件总大小**: 962.42 GB
- **权重张量数**: 159,581
- **参数总量**: 1,023,244,718,976
- **张量累计大小**: 962.40 GB
- **压缩**: 159581 → 39 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[152576, 6144]` | `torch.bfloat16` | 1.75 GB | model_pp0_ep0_shard1.safetensors |
| `model.embed_tokens.weight` | `[152576, 6144]` | `torch.bfloat16` | 1.75 GB | model_pp0_ep0_shard0.safetensors |
| `model.layers.0-69.input_layernorm.weight` (×70 layers) | `[6144]` | `torch.bfloat16` | 840.00 KB | Multi Files |
| `model.layers.0-69.post_attention_layernorm.weight` (×70 layers) | `[6144]` | `torch.bfloat16` | 840.00 KB | Multi Files |
| `model.layers.0-69.self_attn.o_proj.weight` (×70 layers) | `[6144, 16384]` | `torch.bfloat16` | 13.12 GB | Multi Files |
| `model.layers.0-69.self_attn.qkv_proj.weight` (×70 layers) | `[27136, 6144]` | `torch.float8_e4m3fn` | 10.87 GB | Multi Files |
| `model.layers.0-69.self_attn.qkv_proj.weight_scale_inv` (×70 layers) | `[216, 48]` | `torch.float32` | 2.77 MB | Multi Files |
| `model.layers.0.mlp.down_proj.weight` | `[6144, 16384]` | `torch.float8_e4m3fn` | 96.00 MB | model_pp0_ep0_shard0.safetensors |
| `model.layers.0.mlp.down_proj.weight_scale_inv` | `[48, 128]` | `torch.float32` | 24.00 KB | model_pp0_ep0_shard0.safetensors |
| `model.layers.0.mlp.gate_proj.weight` | `[16384, 6144]` | `torch.float8_e4m3fn` | 96.00 MB | model_pp0_ep0_shard0.safetensors |
| `model.layers.0.mlp.gate_proj.weight_scale_inv` | `[128, 48]` | `torch.float32` | 24.00 KB | model_pp0_ep0_shard0.safetensors |
| `model.layers.0.mlp.up_proj.weight` | `[16384, 6144]` | `torch.float8_e4m3fn` | 96.00 MB | model_pp0_ep0_shard0.safetensors |
| `model.layers.0.mlp.up_proj.weight_scale_inv` | `[128, 48]` | `torch.float32` | 24.00 KB | model_pp0_ep0_shard0.safetensors |
| `model.layers.1-6,8-14,16-22,24-30,32-38,40-46,48-54,56-61,63-68.self_attn.attention_sink_bias` (×60 layers) | `[128]` | `torch.bfloat16` | 15.00 KB | Multi Files |
| `model.layers.1-69.mlp.experts.0-383.down_proj.weight` (×69 layers, ×384 experts) | `[6144, 2048]` | `torch.float8_e4m3fn` | 310.50 GB | Multi Files |
| `model.layers.1-69.mlp.experts.0-383.down_proj.weight_scale_inv` (×69 layers, ×384 experts) | `[48, 16]` | `torch.float32` | 77.62 MB | Multi Files |
| `model.layers.1-69.mlp.experts.0-383.gate_proj.weight` (×69 layers, ×384 experts) | `[2048, 6144]` | `torch.float8_e4m3fn` | 310.50 GB | Multi Files |
| `model.layers.1-69.mlp.experts.0-383.gate_proj.weight_scale_inv` (×69 layers, ×384 experts) | `[16, 48]` | `torch.float32` | 77.62 MB | Multi Files |
| `model.layers.1-69.mlp.experts.0-383.up_proj.weight` (×69 layers, ×384 experts) | `[2048, 6144]` | `torch.float8_e4m3fn` | 310.50 GB | Multi Files |
| `model.layers.1-69.mlp.experts.0-383.up_proj.weight_scale_inv` (×69 layers, ×384 experts) | `[16, 48]` | `torch.float32` | 77.62 MB | Multi Files |
| `model.layers.1-69.mlp.gate.e_score_correction_bias` (×69 layers) | `[384]` | `torch.float32` | 103.50 KB | Multi Files |
| `model.layers.1-69.mlp.gate.weight` (×69 layers) | `[384, 6144]` | `torch.float32` | 621.00 MB | Multi Files |
| `model.mtp.layers.0-2.eh_proj.weight` (×3 layers) | `[6144, 12288]` | `torch.bfloat16` | 432.00 MB | model_mtp.safetensors |
| `model.mtp.layers.0-2.enorm.weight` (×3 layers) | `[6144]` | `torch.bfloat16` | 36.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.final_layernorm.weight` (×3 layers) | `[6144]` | `torch.bfloat16` | 36.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.hnorm.weight` (×3 layers) | `[6144]` | `torch.bfloat16` | 36.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.input_layernorm.weight` (×3 layers) | `[6144]` | `torch.bfloat16` | 36.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.mlp.down_proj.weight` (×3 layers) | `[6144, 16384]` | `torch.float8_e4m3fn` | 288.00 MB | model_mtp.safetensors |
| `model.mtp.layers.0-2.mlp.down_proj.weight_scale_inv` (×3 layers) | `[48, 128]` | `torch.float32` | 72.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.mlp.gate_proj.weight` (×3 layers) | `[16384, 6144]` | `torch.float8_e4m3fn` | 288.00 MB | model_mtp.safetensors |
| `model.mtp.layers.0-2.mlp.gate_proj.weight_scale_inv` (×3 layers) | `[128, 48]` | `torch.float32` | 72.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.mlp.up_proj.weight` (×3 layers) | `[16384, 6144]` | `torch.float8_e4m3fn` | 288.00 MB | model_mtp.safetensors |
| `model.mtp.layers.0-2.mlp.up_proj.weight_scale_inv` (×3 layers) | `[128, 48]` | `torch.float32` | 72.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.pre_mlp_layernorm.weight` (×3 layers) | `[6144]` | `torch.bfloat16` | 36.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.self_attn.attention_sink_bias` (×3 layers) | `[128]` | `torch.bfloat16` | 768.00 B | model_mtp.safetensors |
| `model.mtp.layers.0-2.self_attn.o_proj.weight` (×3 layers) | `[6144, 16384]` | `torch.bfloat16` | 576.00 MB | model_mtp.safetensors |
| `model.mtp.layers.0-2.self_attn.qkv_proj.weight` (×3 layers) | `[27136, 6144]` | `torch.float8_e4m3fn` | 477.00 MB | model_mtp.safetensors |
| `model.mtp.layers.0-2.self_attn.qkv_proj.weight_scale_inv` (×3 layers) | `[216, 48]` | `torch.float32` | 121.50 KB | model_mtp.safetensors |
| `model.norm.weight` | `[6144]` | `torch.bfloat16` | 12.00 KB | model_pp0_ep0_shard1.safetensors |

</details>

