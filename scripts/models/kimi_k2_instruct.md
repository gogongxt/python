# 模型信息报告

- **模型路径**: `/nfs/ofs-llab-cold/model/moonshotai/Kimi-K2-Instruct`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llab-cold/model/moonshotai/Kimi-K2-Instruct/config.json`

```json

{
  "architectures": [
    "DeepseekV3ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "auto_map": {
    "AutoConfig": "configuration_deepseek.DeepseekV3Config",
    "AutoModel": "modeling_deepseek.DeepseekV3Model",
    "AutoModelForCausalLM": "modeling_deepseek.DeepseekV3ForCausalLM"
  },
  "aux_loss_alpha": 0.001,
  "bos_token_id": 163584,
  "eos_token_id": 163585,
  "first_k_dense_replace": 1,
  "hidden_act": "silu",
  "hidden_size": 7168,
  "initializer_range": 0.02,
  "intermediate_size": 18432,
  "kv_lora_rank": 512,
  "max_position_embeddings": 131072,
  "model_type": "kimi_k2",
  "moe_intermediate_size": 2048,
  "moe_layer_freq": 1,
  "n_group": 1,
  "n_routed_experts": 384,
  "n_shared_experts": 1,
  "norm_topk_prob": true,
  "num_attention_heads": 64,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 61,
  "num_key_value_heads": 64,
  "num_nextn_predict_layers": 0,
  "pretraining_tp": 1,
  "q_lora_rank": 1536,
  "qk_nope_head_dim": 128,
  "qk_rope_head_dim": 64,
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "e4m3",
    "quant_method": "fp8",
    "weight_block_size": [
      128,
      128
    ]
  },
  "rms_norm_eps": 1e-06,
  "rope_theta": 50000.0,
  "routed_scaling_factor": 2.827,
  "rope_scaling": {
    "beta_fast": 1.0,
    "beta_slow": 1.0,
    "factor": 32.0,
    "mscale": 1.0,
    "mscale_all_dim": 1.0,
    "original_max_position_embeddings": 4096,
    "type": "yarn"
  },
  "scoring_func": "sigmoid",
  "seq_aux": true,
  "tie_word_embeddings": false,
  "topk_group": 1,
  "topk_method": "noaux_tc",
  "torch_dtype": "bfloat16",
  "transformers_version": "4.48.3",
  "use_cache": true,
  "v_head_dim": 128,
  "vocab_size": 163840
}
```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `DeepseekV3Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 7168
- **层数**: 61
- **注意力头数**: 64
- **词表大小**: 163840
- **中间层大小**: 18432

```
DeepseekV3Config {
  "architectures": [
    "DeepseekV3ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "auto_map": {
    "AutoConfig": "configuration_deepseek.DeepseekV3Config",
    "AutoModel": "modeling_deepseek.DeepseekV3Model",
    "AutoModelForCausalLM": "modeling_deepseek.DeepseekV3ForCausalLM"
  },
  "aux_loss_alpha": 0.001,
  "bos_token_id": 163584,
  "dtype": "bfloat16",
  "eos_token_id": 163585,
  "ep_size": 1,
  "first_k_dense_replace": 1,
  "hidden_act": "silu",
  "hidden_size": 7168,
  "initializer_range": 0.02,
  "intermediate_size": 18432,
  "kv_lora_rank": 512,
  "max_position_embeddings": 131072,
  "model_type": "deepseek_v3",
  "moe_intermediate_size": 2048,
  "moe_layer_freq": 1,
  "n_group": 1,
  "n_routed_experts": 384,
  "n_shared_experts": 1,
  "norm_topk_prob": true,
  "num_attention_heads": 64,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 61,
  "num_key_value_heads": 64,
  "num_nextn_predict_layers": 0,
  "pad_token_id": null,
  "pretraining_tp": 1,
  "q_lora_rank": 1536,
  "qk_nope_head_dim": 128,
  "qk_rope_head_dim": 64,
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "e4m3",
    "quant_method": "fp8",
    "weight_block_size": [
      128,
      128
    ]
  },
  "rms_norm_eps": 1e-06,
  "rope_parameters": {
    "beta_fast": 1.0,
    "beta_slow": 1.0,
    "factor": 32.0,
    "mscale": 1.0,
    "mscale_all_dim": 1.0,
    "original_max_position_embeddings": 4096,
    "rope_theta": 50000.0,
    "rope_type": "yarn",
    "type": "yarn"
  },
  "rope_theta": 50000.0,
  "routed_scaling_factor": 2.827,
  "scoring_func": "sigmoid",
  "seq_aux": true,
  "tie_word_embeddings": false,
  "topk_group": 1,
  "topk_method": "noaux_tc",
  "transformers_version": "5.7.0",
  "use_cache": true,
  "v_head_dim": 128,
  "vocab_size": 163840
}

```

</details>

# 模型结构

**模型类**: `DeepseekV3Config` (当前 transformers 版本不支持实例化)

# 权重统计

- **权重文件**: 61 个 `safetensors` 文件
- **文件总大小**: 958.51 GB
- **权重张量数**: 139,644
- **参数总量**: 1,026,470,731,056
- **张量累计大小**: 958.49 GB
- **压缩**: 139644 → 38 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[163840, 7168]` | `torch.bfloat16` | 2.19 GB | model-61-of-61.safetensors |
| `model.embed_tokens.weight` | `[163840, 7168]` | `torch.bfloat16` | 2.19 GB | model-1-of-61.safetensors |
| `model.layers.0-60.input_layernorm.weight` (×61 layers) | `[7168]` | `torch.bfloat16` | 854.00 KB | Multi Files |
| `model.layers.0-60.post_attention_layernorm.weight` (×61 layers) | `[7168]` | `torch.bfloat16` | 854.00 KB | Multi Files |
| `model.layers.0-60.self_attn.kv_a_layernorm.weight` (×61 layers) | `[512]` | `torch.bfloat16` | 61.00 KB | Multi Files |
| `model.layers.0-60.self_attn.kv_a_proj_with_mqa.weight` (×61 layers) | `[576, 7168]` | `torch.float8_e4m3fn` | 240.19 MB | Multi Files |
| `model.layers.0-60.self_attn.kv_a_proj_with_mqa.weight_scale_inv` (×61 layers) | `[5, 56]` | `torch.float32` | 66.72 KB | Multi Files |
| `model.layers.0-60.self_attn.kv_b_proj.weight` (×61 layers) | `[16384, 512]` | `torch.float8_e4m3fn` | 488.00 MB | Multi Files |
| `model.layers.0-60.self_attn.kv_b_proj.weight_scale_inv` (×61 layers) | `[128, 4]` | `torch.float32` | 122.00 KB | Multi Files |
| `model.layers.0-60.self_attn.o_proj.weight` (×61 layers) | `[7168, 8192]` | `torch.float8_e4m3fn` | 3.34 GB | Multi Files |
| `model.layers.0-60.self_attn.o_proj.weight_scale_inv` (×61 layers) | `[56, 64]` | `torch.float32` | 854.00 KB | Multi Files |
| `model.layers.0-60.self_attn.q_a_layernorm.weight` (×61 layers) | `[1536]` | `torch.bfloat16` | 183.00 KB | Multi Files |
| `model.layers.0-60.self_attn.q_a_proj.weight` (×61 layers) | `[1536, 7168]` | `torch.float8_e4m3fn` | 640.50 MB | Multi Files |
| `model.layers.0-60.self_attn.q_a_proj.weight_scale_inv` (×61 layers) | `[12, 56]` | `torch.float32` | 160.12 KB | Multi Files |
| `model.layers.0-60.self_attn.q_b_proj.weight` (×61 layers) | `[12288, 1536]` | `torch.float8_e4m3fn` | 1.07 GB | Multi Files |
| `model.layers.0-60.self_attn.q_b_proj.weight_scale_inv` (×61 layers) | `[96, 12]` | `torch.float32` | 274.50 KB | Multi Files |
| `model.layers.0-60.self_attn.rotary_emb.inv_freq` (×61 layers) | `[56]` | `torch.bfloat16` | 6.67 KB | Multi Files |
| `model.layers.0.mlp.down_proj.weight` | `[7168, 18432]` | `torch.float8_e4m3fn` | 126.00 MB | model-1-of-61.safetensors |
| `model.layers.0.mlp.down_proj.weight_scale_inv` | `[56, 144]` | `torch.float32` | 31.50 KB | model-1-of-61.safetensors |
| `model.layers.0.mlp.gate_proj.weight` | `[18432, 7168]` | `torch.float8_e4m3fn` | 126.00 MB | model-1-of-61.safetensors |
| `model.layers.0.mlp.gate_proj.weight_scale_inv` | `[144, 56]` | `torch.float32` | 31.50 KB | model-1-of-61.safetensors |
| `model.layers.0.mlp.up_proj.weight` | `[18432, 7168]` | `torch.float8_e4m3fn` | 126.00 MB | model-1-of-61.safetensors |
| `model.layers.0.mlp.up_proj.weight_scale_inv` | `[144, 56]` | `torch.float32` | 31.50 KB | model-1-of-61.safetensors |
| `model.layers.1-60.mlp.experts.0-383.down_proj.weight` (×60 layers, ×384 experts) | `[7168, 2048]` | `torch.float8_e4m3fn` | 315.00 GB | Multi Files |
| `model.layers.1-60.mlp.experts.0-383.down_proj.weight_scale_inv` (×60 layers, ×384 experts) | `[56, 16]` | `torch.float32` | 78.75 MB | Multi Files |
| `model.layers.1-60.mlp.experts.0-383.gate_proj.weight` (×60 layers, ×384 experts) | `[2048, 7168]` | `torch.float8_e4m3fn` | 315.00 GB | Multi Files |
| `model.layers.1-60.mlp.experts.0-383.gate_proj.weight_scale_inv` (×60 layers, ×384 experts) | `[16, 56]` | `torch.float32` | 78.75 MB | Multi Files |
| `model.layers.1-60.mlp.experts.0-383.up_proj.weight` (×60 layers, ×384 experts) | `[2048, 7168]` | `torch.float8_e4m3fn` | 315.00 GB | Multi Files |
| `model.layers.1-60.mlp.experts.0-383.up_proj.weight_scale_inv` (×60 layers, ×384 experts) | `[16, 56]` | `torch.float32` | 78.75 MB | Multi Files |
| `model.layers.1-60.mlp.gate.e_score_correction_bias` (×60 layers) | `[384]` | `torch.float32` | 90.00 KB | Multi Files |
| `model.layers.1-60.mlp.gate.weight` (×60 layers) | `[384, 7168]` | `torch.bfloat16` | 315.00 MB | Multi Files |
| `model.layers.1-60.mlp.shared_experts.down_proj.weight` (×60 layers) | `[7168, 2048]` | `torch.float8_e4m3fn` | 840.00 MB | Multi Files |
| `model.layers.1-60.mlp.shared_experts.down_proj.weight_scale_inv` (×60 layers) | `[56, 16]` | `torch.float32` | 210.00 KB | Multi Files |
| `model.layers.1-60.mlp.shared_experts.gate_proj.weight` (×60 layers) | `[2048, 7168]` | `torch.float8_e4m3fn` | 840.00 MB | Multi Files |
| `model.layers.1-60.mlp.shared_experts.gate_proj.weight_scale_inv` (×60 layers) | `[16, 56]` | `torch.float32` | 210.00 KB | Multi Files |
| `model.layers.1-60.mlp.shared_experts.up_proj.weight` (×60 layers) | `[2048, 7168]` | `torch.float8_e4m3fn` | 840.00 MB | Multi Files |
| `model.layers.1-60.mlp.shared_experts.up_proj.weight_scale_inv` (×60 layers) | `[16, 56]` | `torch.float32` | 210.00 KB | Multi Files |
| `model.norm.weight` | `[7168]` | `torch.bfloat16` | 14.00 KB | model-61-of-61.safetensors |

</details>

