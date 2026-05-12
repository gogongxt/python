# 模型信息报告

- **模型路径**: `/nfs/ofs-llab-cold/model/moonshotai/Kimi-Linear-48B-A3B-Instruct`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llab-cold/model/moonshotai/Kimi-Linear-48B-A3B-Instruct/config.json`

```json

{
  "architectures": [
    "KimiLinearForCausalLM"
  ],
  "auto_map": {
    "AutoConfig": "configuration_kimi.KimiLinearConfig",
    "AutoModel": "modeling_kimi.KimiLinearModel",
    "AutoModelForCausalLM": "modeling_kimi.KimiLinearForCausalLM"
  },
  "bos_token_id": 163584,
  "dtype": "bfloat16",
  "eos_token_id": 163586,
  "first_k_dense_replace": 1,
  "head_dim": 72,
  "hidden_act": "silu",
  "hidden_size": 2304,
  "initializer_range": 0.02,
  "intermediate_size": 9216,
  "kv_lora_rank": 512,
  "linear_attn_config": {
    "full_attn_layers": [
      4,
      8,
      12,
      16,
      20,
      24,
      27
    ],
    "head_dim": 128,
    "kda_layers": [
      1,
      2,
      3,
      5,
      6,
      7,
      9,
      10,
      11,
      13,
      14,
      15,
      17,
      18,
      19,
      21,
      22,
      23,
      25,
      26
    ],
    "num_heads": 32,
    "short_conv_kernel_size": 4
  },
  "mla_use_nope": true,
  "model_max_length": 1048576,
  "model_type": "kimi_linear",
  "moe_intermediate_size": 1024,
  "moe_layer_freq": 1,
  "moe_renormalize": true,
  "moe_router_activation_func": "sigmoid",
  "num_attention_heads": 32,
  "num_expert_group": 1,
  "num_experts": 256,
  "num_experts_per_token": 8,
  "num_hidden_layers": 27,
  "num_key_value_heads": 32,
  "num_nextn_predict_layers": 0,
  "num_shared_experts": 1,
  "pad_token_id": 163839,
  "q_lora_rank": null,
  "qk_nope_head_dim": 128,
  "qk_rope_head_dim": 64,
  "rms_norm_eps": 1e-05,
  "rope_scaling": null,
  "rope_theta": 10000.0,
  "routed_scaling_factor": 2.446,
  "tie_word_embeddings": false,
  "topk_group": 1,
  "transformers_version": "4.57.1",
  "use_cache": true,
  "use_grouped_topk": true,
  "v_head_dim": 128,
  "vocab_size": 163840
}

```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `KimiLinearConfig`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 2304
- **层数**: 27
- **注意力头数**: 32
- **词表大小**: 163840
- **中间层大小**: 9216

```
KimiLinearConfig {
  "architectures": [
    "KimiLinearForCausalLM"
  ],
  "auto_map": {
    "AutoConfig": "configuration_kimi.KimiLinearConfig",
    "AutoModel": "modeling_kimi.KimiLinearModel",
    "AutoModelForCausalLM": "modeling_kimi.KimiLinearForCausalLM"
  },
  "bos_token_id": 163584,
  "dtype": "bfloat16",
  "eos_token_id": 163586,
  "first_k_dense_replace": 1,
  "head_dim": 72,
  "hidden_act": "silu",
  "hidden_size": 2304,
  "initializer_range": 0.02,
  "intermediate_size": 9216,
  "kv_lora_rank": 512,
  "linear_attn_config": {
    "full_attn_layers": [
      4,
      8,
      12,
      16,
      20,
      24,
      27
    ],
    "head_dim": 128,
    "kda_layers": [
      1,
      2,
      3,
      5,
      6,
      7,
      9,
      10,
      11,
      13,
      14,
      15,
      17,
      18,
      19,
      21,
      22,
      23,
      25,
      26
    ],
    "num_heads": 32,
    "short_conv_kernel_size": 4
  },
  "mla_use_nope": true,
  "model_max_length": 1048576,
  "model_type": "kimi_linear",
  "moe_intermediate_size": 1024,
  "moe_layer_freq": 1,
  "moe_renormalize": true,
  "moe_router_activation_func": "sigmoid",
  "num_attention_heads": 32,
  "num_expert_group": 1,
  "num_experts": 256,
  "num_experts_per_token": 8,
  "num_hidden_layers": 27,
  "num_key_value_heads": 32,
  "num_nextn_predict_layers": 0,
  "num_shared_experts": 1,
  "pad_token_id": 163839,
  "q_lora_rank": null,
  "qk_nope_head_dim": 128,
  "qk_rope_head_dim": 64,
  "rms_norm_eps": 1e-05,
  "rope_parameters": {
    "rope_theta": 10000.0,
    "rope_type": "default"
  },
  "rope_theta": 10000.0,
  "routed_scaling_factor": 2.446,
  "tie_word_embeddings": false,
  "topk_group": 1,
  "transformers_version": "5.7.0",
  "use_cache": true,
  "use_grouped_topk": true,
  "v_head_dim": 128,
  "vocab_size": 163840
}

```

</details>

# 模型结构

**模型类**: `KimiLinearConfig` (当前 transformers 版本不支持实例化)

# 权重统计

- **权重文件**: 20 个 `safetensors` 文件
- **文件总大小**: 91.50 GB
- **权重张量数**: 20,493
- **参数总量**: 49,122,681,728
- **张量累计大小**: 91.50 GB
- **压缩**: 20493 → 35 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[163840, 2304]` | `torch.bfloat16` | 720.00 MB | model-00020-of-00020.safetensors |
| `model.embed_tokens.weight` | `[163840, 2304]` | `torch.bfloat16` | 720.00 MB | model-00001-of-00020.safetensors |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.A_log` (×20 layers) | `[1, 1, 32, 1]` | `torch.float32` | 2.50 KB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.b_proj.weight` (×20 layers) | `[32, 2304]` | `torch.bfloat16` | 2.81 MB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.dt_bias` (×20 layers) | `[4096]` | `torch.float32` | 320.00 KB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.f_a_proj.weight` (×20 layers) | `[128, 2304]` | `torch.bfloat16` | 11.25 MB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.f_b_proj.weight` (×20 layers) | `[4096, 128]` | `torch.bfloat16` | 20.00 MB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.g_a_proj.weight` (×20 layers) | `[128, 2304]` | `torch.bfloat16` | 11.25 MB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.g_b_proj.weight` (×20 layers) | `[4096, 128]` | `torch.bfloat16` | 20.00 MB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.k_conv1d.weight` (×20 layers) | `[4096, 1, 4]` | `torch.bfloat16` | 640.00 KB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.k_proj.weight` (×20 layers) | `[4096, 2304]` | `torch.bfloat16` | 360.00 MB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.o_norm.weight` (×20 layers) | `[128]` | `torch.bfloat16` | 5.00 KB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.q_conv1d.weight` (×20 layers) | `[4096, 1, 4]` | `torch.bfloat16` | 640.00 KB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.q_proj.weight` (×20 layers) | `[4096, 2304]` | `torch.bfloat16` | 360.00 MB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.v_conv1d.weight` (×20 layers) | `[4096, 1, 4]` | `torch.bfloat16` | 640.00 KB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-25.self_attn.v_proj.weight` (×20 layers) | `[4096, 2304]` | `torch.bfloat16` | 360.00 MB | Multi Files |
| `model.layers.0-26.input_layernorm.weight` (×27 layers) | `[2304]` | `torch.bfloat16` | 121.50 KB | Multi Files |
| `model.layers.0-26.post_attention_layernorm.weight` (×27 layers) | `[2304]` | `torch.bfloat16` | 121.50 KB | Multi Files |
| `model.layers.0-26.self_attn.o_proj.weight` (×27 layers) | `[2304, 4096]` | `torch.bfloat16` | 486.00 MB | Multi Files |
| `model.layers.0.mlp.down_proj.weight` | `[2304, 9216]` | `torch.bfloat16` | 40.50 MB | model-00001-of-00020.safetensors |
| `model.layers.0.mlp.gate_proj.weight` | `[9216, 2304]` | `torch.bfloat16` | 40.50 MB | model-00001-of-00020.safetensors |
| `model.layers.0.mlp.up_proj.weight` | `[9216, 2304]` | `torch.bfloat16` | 40.50 MB | model-00001-of-00020.safetensors |
| `model.layers.1-26.block_sparse_moe.experts.0-255.w1.weight` (×26 layers, ×256 experts) | `[1024, 2304]` | `torch.bfloat16` | 29.25 GB | Multi Files |
| `model.layers.1-26.block_sparse_moe.experts.0-255.w2.weight` (×26 layers, ×256 experts) | `[2304, 1024]` | `torch.bfloat16` | 29.25 GB | Multi Files |
| `model.layers.1-26.block_sparse_moe.experts.0-255.w3.weight` (×26 layers, ×256 experts) | `[1024, 2304]` | `torch.bfloat16` | 29.25 GB | Multi Files |
| `model.layers.1-26.block_sparse_moe.gate.e_score_correction_bias` (×26 layers) | `[256]` | `torch.bfloat16` | 13.00 KB | Multi Files |
| `model.layers.1-26.block_sparse_moe.gate.weight` (×26 layers) | `[256, 2304]` | `torch.bfloat16` | 29.25 MB | Multi Files |
| `model.layers.1-26.block_sparse_moe.shared_experts.down_proj.weight` (×26 layers) | `[2304, 1024]` | `torch.bfloat16` | 117.00 MB | Multi Files |
| `model.layers.1-26.block_sparse_moe.shared_experts.gate_proj.weight` (×26 layers) | `[1024, 2304]` | `torch.bfloat16` | 117.00 MB | Multi Files |
| `model.layers.1-26.block_sparse_moe.shared_experts.up_proj.weight` (×26 layers) | `[1024, 2304]` | `torch.bfloat16` | 117.00 MB | Multi Files |
| `model.layers.3,7,11,15,19,23,26.self_attn.kv_a_layernorm.weight` (×7 layers) | `[512]` | `torch.bfloat16` | 7.00 KB | Multi Files |
| `model.layers.3,7,11,15,19,23,26.self_attn.kv_a_proj_with_mqa.weight` (×7 layers) | `[576, 2304]` | `torch.bfloat16` | 17.72 MB | Multi Files |
| `model.layers.3,7,11,15,19,23,26.self_attn.kv_b_proj.weight` (×7 layers) | `[8192, 512]` | `torch.bfloat16` | 56.00 MB | Multi Files |
| `model.layers.3,7,11,15,19,23,26.self_attn.q_proj.weight` (×7 layers) | `[6144, 2304]` | `torch.bfloat16` | 189.00 MB | Multi Files |
| `model.norm.weight` | `[2304]` | `torch.bfloat16` | 4.50 KB | model-00020-of-00020.safetensors |

</details>

