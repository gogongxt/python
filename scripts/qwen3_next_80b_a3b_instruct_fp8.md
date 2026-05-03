# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/user/gogongxt/models/Qwen3-Next-80B-A3B-Instruct-FP8`

# 模型配置

- **模型类型**: `Qwen3NextConfig`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 2048
- **层数**: 48
- **注意力头数**: 16
- **词表大小**: 151936
- **中间层大小**: 5120

<details><summary>完整配置</summary>

```
Qwen3NextConfig {
  "architectures": [
    "Qwen3NextForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "decoder_sparse_step": 1,
  "dtype": "bfloat16",
  "eos_token_id": 151645,
  "head_dim": 256,
  "hidden_act": "silu",
  "hidden_size": 2048,
  "initializer_range": 0.02,
  "intermediate_size": 5120,
  "layer_types": [
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention"
  ],
  "linear_conv_kernel_dim": 4,
  "linear_key_head_dim": 128,
  "linear_num_key_heads": 16,
  "linear_num_value_heads": 32,
  "linear_value_head_dim": 128,
  "max_position_embeddings": 262144,
  "mlp_only_layers": [],
  "model_type": "qwen3_next",
  "moe_intermediate_size": 512,
  "norm_topk_prob": true,
  "num_attention_heads": 16,
  "num_experts": 512,
  "num_experts_per_tok": 10,
  "num_hidden_layers": 48,
  "num_key_value_heads": 2,
  "output_router_logits": false,
  "pad_token_id": null,
  "partial_rotary_factor": 0.25,
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "e4m3",
    "modules_to_not_convert": [
      "lm_head",
      "model.layers.0.input_layernorm",
      "model.layers.0.linear_attn.A_log",
      "model.layers.0.linear_attn.conv1d",
      "model.layers.0.linear_attn.dt_bias",
      "model.layers.0.linear_attn.in_proj_ba",
      "model.layers.0.linear_attn.norm",
      "model.layers.0.mlp.gate",
      "model.layers.0.mlp.shared_expert_gate",
      "model.layers.0.post_attention_layernorm",
      "model.layers.1.input_layernorm",
      "model.layers.1.linear_attn.A_log",
      "model.layers.1.linear_attn.conv1d",
      "model.layers.1.linear_attn.dt_bias",
      "model.layers.1.linear_attn.in_proj_ba",
      "model.layers.1.linear_attn.norm",
      "model.layers.1.mlp.gate",
      "model.layers.1.mlp.shared_expert_gate",
      "model.layers.1.post_attention_layernorm",
      "model.layers.2.input_layernorm",
      "model.layers.2.linear_attn.A_log",
      "model.layers.2.linear_attn.conv1d",
      "model.layers.2.linear_attn.dt_bias",
      "model.layers.2.linear_attn.in_proj_ba",
      "model.layers.2.linear_attn.norm",
      "model.layers.2.mlp.gate",
      "model.layers.2.mlp.shared_expert_gate",
      "model.layers.2.post_attention_layernorm",
      "model.layers.3.input_layernorm",
      "model.layers.3.mlp.gate",
      "model.layers.3.mlp.shared_expert_gate",
      "model.layers.3.post_attention_layernorm",
      "model.layers.3.self_attn.k_norm",
      "model.layers.3.self_attn.q_norm",
      "model.layers.4.input_layernorm",
      "model.layers.4.linear_attn.A_log",
      "model.layers.4.linear_attn.conv1d",
      "model.layers.4.linear_attn.dt_bias",
      "model.layers.4.linear_attn.in_proj_ba",
      "model.layers.4.linear_attn.norm",
      "model.layers.4.mlp.gate",
      "model.layers.4.mlp.shared_expert_gate",
      "model.layers.4.post_attention_layernorm",
      "model.layers.5.input_layernorm",
      "model.layers.5.linear_attn.A_log",
      "model.layers.5.linear_attn.conv1d",
      "model.layers.5.linear_attn.dt_bias",
      "model.layers.5.linear_attn.in_proj_ba",
      "model.layers.5.linear_attn.norm",
      "model.layers.5.mlp.gate",
      "model.layers.5.mlp.shared_expert_gate",
      "model.layers.5.post_attention_layernorm",
      "model.layers.6.input_layernorm",
      "model.layers.6.linear_attn.A_log",
      "model.layers.6.linear_attn.conv1d",
      "model.layers.6.linear_attn.dt_bias",
      "model.layers.6.linear_attn.in_proj_ba",
      "model.layers.6.linear_attn.norm",
      "model.layers.6.mlp.gate",
      "model.layers.6.mlp.shared_expert_gate",
      "model.layers.6.post_attention_layernorm",
      "model.layers.7.input_layernorm",
      "model.layers.7.mlp.gate",
      "model.layers.7.mlp.shared_expert_gate",
      "model.layers.7.post_attention_layernorm",
      "model.layers.7.self_attn.k_norm",
      "model.layers.7.self_attn.q_norm",
      "model.layers.8.input_layernorm",
      "model.layers.8.linear_attn.A_log",
      "model.layers.8.linear_attn.conv1d",
      "model.layers.8.linear_attn.dt_bias",
      "model.layers.8.linear_attn.in_proj_ba",
      "model.layers.8.linear_attn.norm",
      "model.layers.8.mlp.gate",
      "model.layers.8.mlp.shared_expert_gate",
      "model.layers.8.post_attention_layernorm",
      "model.layers.9.input_layernorm",
      "model.layers.9.linear_attn.A_log",
      "model.layers.9.linear_attn.conv1d",
      "model.layers.9.linear_attn.dt_bias",
      "model.layers.9.linear_attn.in_proj_ba",
      "model.layers.9.linear_attn.norm",
      "model.layers.9.mlp.gate",
      "model.layers.9.mlp.shared_expert_gate",
      "model.layers.9.post_attention_layernorm",
      "model.layers.10.input_layernorm",
      "model.layers.10.linear_attn.A_log",
      "model.layers.10.linear_attn.conv1d",
      "model.layers.10.linear_attn.dt_bias",
      "model.layers.10.linear_attn.in_proj_ba",
      "model.layers.10.linear_attn.norm",
      "model.layers.10.mlp.gate",
      "model.layers.10.mlp.shared_expert_gate",
      "model.layers.10.post_attention_layernorm",
      "model.layers.11.input_layernorm",
      "model.layers.11.mlp.gate",
      "model.layers.11.mlp.shared_expert_gate",
      "model.layers.11.post_attention_layernorm",
      "model.layers.11.self_attn.k_norm",
      "model.layers.11.self_attn.q_norm",
      "model.layers.12.input_layernorm",
      "model.layers.12.linear_attn.A_log",
      "model.layers.12.linear_attn.conv1d",
      "model.layers.12.linear_attn.dt_bias",
      "model.layers.12.linear_attn.in_proj_ba",
      "model.layers.12.linear_attn.norm",
      "model.layers.12.mlp.gate",
      "model.layers.12.mlp.shared_expert_gate",
      "model.layers.12.post_attention_layernorm",
      "model.layers.13.input_layernorm",
      "model.layers.13.linear_attn.A_log",
      "model.layers.13.linear_attn.conv1d",
      "model.layers.13.linear_attn.dt_bias",
      "model.layers.13.linear_attn.in_proj_ba",
      "model.layers.13.linear_attn.norm",
      "model.layers.13.mlp.gate",
      "model.layers.13.mlp.shared_expert_gate",
      "model.layers.13.post_attention_layernorm",
      "model.layers.14.input_layernorm",
      "model.layers.14.linear_attn.A_log",
      "model.layers.14.linear_attn.conv1d",
      "model.layers.14.linear_attn.dt_bias",
      "model.layers.14.linear_attn.in_proj_ba",
      "model.layers.14.linear_attn.norm",
      "model.layers.14.mlp.gate",
      "model.layers.14.mlp.shared_expert_gate",
      "model.layers.14.post_attention_layernorm",
      "model.layers.15.input_layernorm",
      "model.layers.15.mlp.gate",
      "model.layers.15.mlp.shared_expert_gate",
      "model.layers.15.post_attention_layernorm",
      "model.layers.15.self_attn.k_norm",
      "model.layers.15.self_attn.q_norm",
      "model.layers.16.input_layernorm",
      "model.layers.16.linear_attn.A_log",
      "model.layers.16.linear_attn.conv1d",
      "model.layers.16.linear_attn.dt_bias",
      "model.layers.16.linear_attn.in_proj_ba",
      "model.layers.16.linear_attn.norm",
      "model.layers.16.mlp.gate",
      "model.layers.16.mlp.shared_expert_gate",
      "model.layers.16.post_attention_layernorm",
      "model.layers.17.input_layernorm",
      "model.layers.17.linear_attn.A_log",
      "model.layers.17.linear_attn.conv1d",
      "model.layers.17.linear_attn.dt_bias",
      "model.layers.17.linear_attn.in_proj_ba",
      "model.layers.17.linear_attn.norm",
      "model.layers.17.mlp.gate",
      "model.layers.17.mlp.shared_expert_gate",
      "model.layers.17.post_attention_layernorm",
      "model.layers.18.input_layernorm",
      "model.layers.18.linear_attn.A_log",
      "model.layers.18.linear_attn.conv1d",
      "model.layers.18.linear_attn.dt_bias",
      "model.layers.18.linear_attn.in_proj_ba",
      "model.layers.18.linear_attn.norm",
      "model.layers.18.mlp.gate",
      "model.layers.18.mlp.shared_expert_gate",
      "model.layers.18.post_attention_layernorm",
      "model.layers.19.input_layernorm",
      "model.layers.19.mlp.gate",
      "model.layers.19.mlp.shared_expert_gate",
      "model.layers.19.post_attention_layernorm",
      "model.layers.19.self_attn.k_norm",
      "model.layers.19.self_attn.q_norm",
      "model.layers.20.input_layernorm",
      "model.layers.20.linear_attn.A_log",
      "model.layers.20.linear_attn.conv1d",
      "model.layers.20.linear_attn.dt_bias",
      "model.layers.20.linear_attn.in_proj_ba",
      "model.layers.20.linear_attn.norm",
      "model.layers.20.mlp.gate",
      "model.layers.20.mlp.shared_expert_gate",
      "model.layers.20.post_attention_layernorm",
      "model.layers.21.input_layernorm",
      "model.layers.21.linear_attn.A_log",
      "model.layers.21.linear_attn.conv1d",
      "model.layers.21.linear_attn.dt_bias",
      "model.layers.21.linear_attn.in_proj_ba",
      "model.layers.21.linear_attn.norm",
      "model.layers.21.mlp.gate",
      "model.layers.21.mlp.shared_expert_gate",
      "model.layers.21.post_attention_layernorm",
      "model.layers.22.input_layernorm",
      "model.layers.22.linear_attn.A_log",
      "model.layers.22.linear_attn.conv1d",
      "model.layers.22.linear_attn.dt_bias",
      "model.layers.22.linear_attn.in_proj_ba",
      "model.layers.22.linear_attn.norm",
      "model.layers.22.mlp.gate",
      "model.layers.22.mlp.shared_expert_gate",
      "model.layers.22.post_attention_layernorm",
      "model.layers.23.input_layernorm",
      "model.layers.23.mlp.gate",
      "model.layers.23.mlp.shared_expert_gate",
      "model.layers.23.post_attention_layernorm",
      "model.layers.23.self_attn.k_norm",
      "model.layers.23.self_attn.q_norm",
      "model.layers.24.input_layernorm",
      "model.layers.24.linear_attn.A_log",
      "model.layers.24.linear_attn.conv1d",
      "model.layers.24.linear_attn.dt_bias",
      "model.layers.24.linear_attn.in_proj_ba",
      "model.layers.24.linear_attn.norm",
      "model.layers.24.mlp.gate",
      "model.layers.24.mlp.shared_expert_gate",
      "model.layers.24.post_attention_layernorm",
      "model.layers.25.input_layernorm",
      "model.layers.25.linear_attn.A_log",
      "model.layers.25.linear_attn.conv1d",
      "model.layers.25.linear_attn.dt_bias",
      "model.layers.25.linear_attn.in_proj_ba",
      "model.layers.25.linear_attn.norm",
      "model.layers.25.mlp.gate",
      "model.layers.25.mlp.shared_expert_gate",
      "model.layers.25.post_attention_layernorm",
      "model.layers.26.input_layernorm",
      "model.layers.26.linear_attn.A_log",
      "model.layers.26.linear_attn.conv1d",
      "model.layers.26.linear_attn.dt_bias",
      "model.layers.26.linear_attn.in_proj_ba",
      "model.layers.26.linear_attn.norm",
      "model.layers.26.mlp.gate",
      "model.layers.26.mlp.shared_expert_gate",
      "model.layers.26.post_attention_layernorm",
      "model.layers.27.input_layernorm",
      "model.layers.27.mlp.gate",
      "model.layers.27.mlp.shared_expert_gate",
      "model.layers.27.post_attention_layernorm",
      "model.layers.27.self_attn.k_norm",
      "model.layers.27.self_attn.q_norm",
      "model.layers.28.input_layernorm",
      "model.layers.28.linear_attn.A_log",
      "model.layers.28.linear_attn.conv1d",
      "model.layers.28.linear_attn.dt_bias",
      "model.layers.28.linear_attn.in_proj_ba",
      "model.layers.28.linear_attn.norm",
      "model.layers.28.mlp.gate",
      "model.layers.28.mlp.shared_expert_gate",
      "model.layers.28.post_attention_layernorm",
      "model.layers.29.input_layernorm",
      "model.layers.29.linear_attn.A_log",
      "model.layers.29.linear_attn.conv1d",
      "model.layers.29.linear_attn.dt_bias",
      "model.layers.29.linear_attn.in_proj_ba",
      "model.layers.29.linear_attn.norm",
      "model.layers.29.mlp.gate",
      "model.layers.29.mlp.shared_expert_gate",
      "model.layers.29.post_attention_layernorm",
      "model.layers.30.input_layernorm",
      "model.layers.30.linear_attn.A_log",
      "model.layers.30.linear_attn.conv1d",
      "model.layers.30.linear_attn.dt_bias",
      "model.layers.30.linear_attn.in_proj_ba",
      "model.layers.30.linear_attn.norm",
      "model.layers.30.mlp.gate",
      "model.layers.30.mlp.shared_expert_gate",
      "model.layers.30.post_attention_layernorm",
      "model.layers.31.input_layernorm",
      "model.layers.31.mlp.gate",
      "model.layers.31.mlp.shared_expert_gate",
      "model.layers.31.post_attention_layernorm",
      "model.layers.31.self_attn.k_norm",
      "model.layers.31.self_attn.q_norm",
      "model.layers.32.input_layernorm",
      "model.layers.32.linear_attn.A_log",
      "model.layers.32.linear_attn.conv1d",
      "model.layers.32.linear_attn.dt_bias",
      "model.layers.32.linear_attn.in_proj_ba",
      "model.layers.32.linear_attn.norm",
      "model.layers.32.mlp.gate",
      "model.layers.32.mlp.shared_expert_gate",
      "model.layers.32.post_attention_layernorm",
      "model.layers.33.input_layernorm",
      "model.layers.33.linear_attn.A_log",
      "model.layers.33.linear_attn.conv1d",
      "model.layers.33.linear_attn.dt_bias",
      "model.layers.33.linear_attn.in_proj_ba",
      "model.layers.33.linear_attn.norm",
      "model.layers.33.mlp.gate",
      "model.layers.33.mlp.shared_expert_gate",
      "model.layers.33.post_attention_layernorm",
      "model.layers.34.input_layernorm",
      "model.layers.34.linear_attn.A_log",
      "model.layers.34.linear_attn.conv1d",
      "model.layers.34.linear_attn.dt_bias",
      "model.layers.34.linear_attn.in_proj_ba",
      "model.layers.34.linear_attn.norm",
      "model.layers.34.mlp.gate",
      "model.layers.34.mlp.shared_expert_gate",
      "model.layers.34.post_attention_layernorm",
      "model.layers.35.input_layernorm",
      "model.layers.35.mlp.gate",
      "model.layers.35.mlp.shared_expert_gate",
      "model.layers.35.post_attention_layernorm",
      "model.layers.35.self_attn.k_norm",
      "model.layers.35.self_attn.q_norm",
      "model.layers.36.input_layernorm",
      "model.layers.36.linear_attn.A_log",
      "model.layers.36.linear_attn.conv1d",
      "model.layers.36.linear_attn.dt_bias",
      "model.layers.36.linear_attn.in_proj_ba",
      "model.layers.36.linear_attn.norm",
      "model.layers.36.mlp.gate",
      "model.layers.36.mlp.shared_expert_gate",
      "model.layers.36.post_attention_layernorm",
      "model.layers.37.input_layernorm",
      "model.layers.37.linear_attn.A_log",
      "model.layers.37.linear_attn.conv1d",
      "model.layers.37.linear_attn.dt_bias",
      "model.layers.37.linear_attn.in_proj_ba",
      "model.layers.37.linear_attn.norm",
      "model.layers.37.mlp.gate",
      "model.layers.37.mlp.shared_expert_gate",
      "model.layers.37.post_attention_layernorm",
      "model.layers.38.input_layernorm",
      "model.layers.38.linear_attn.A_log",
      "model.layers.38.linear_attn.conv1d",
      "model.layers.38.linear_attn.dt_bias",
      "model.layers.38.linear_attn.in_proj_ba",
      "model.layers.38.linear_attn.norm",
      "model.layers.38.mlp.gate",
      "model.layers.38.mlp.shared_expert_gate",
      "model.layers.38.post_attention_layernorm",
      "model.layers.39.input_layernorm",
      "model.layers.39.mlp.gate",
      "model.layers.39.mlp.shared_expert_gate",
      "model.layers.39.post_attention_layernorm",
      "model.layers.39.self_attn.k_norm",
      "model.layers.39.self_attn.q_norm",
      "model.layers.40.input_layernorm",
      "model.layers.40.linear_attn.A_log",
      "model.layers.40.linear_attn.conv1d",
      "model.layers.40.linear_attn.dt_bias",
      "model.layers.40.linear_attn.in_proj_ba",
      "model.layers.40.linear_attn.norm",
      "model.layers.40.mlp.gate",
      "model.layers.40.mlp.shared_expert_gate",
      "model.layers.40.post_attention_layernorm",
      "model.layers.41.input_layernorm",
      "model.layers.41.linear_attn.A_log",
      "model.layers.41.linear_attn.conv1d",
      "model.layers.41.linear_attn.dt_bias",
      "model.layers.41.linear_attn.in_proj_ba",
      "model.layers.41.linear_attn.norm",
      "model.layers.41.mlp.gate",
      "model.layers.41.mlp.shared_expert_gate",
      "model.layers.41.post_attention_layernorm",
      "model.layers.42.input_layernorm",
      "model.layers.42.linear_attn.A_log",
      "model.layers.42.linear_attn.conv1d",
      "model.layers.42.linear_attn.dt_bias",
      "model.layers.42.linear_attn.in_proj_ba",
      "model.layers.42.linear_attn.norm",
      "model.layers.42.mlp.gate",
      "model.layers.42.mlp.shared_expert_gate",
      "model.layers.42.post_attention_layernorm",
      "model.layers.43.input_layernorm",
      "model.layers.43.mlp.gate",
      "model.layers.43.mlp.shared_expert_gate",
      "model.layers.43.post_attention_layernorm",
      "model.layers.43.self_attn.k_norm",
      "model.layers.43.self_attn.q_norm",
      "model.layers.44.input_layernorm",
      "model.layers.44.linear_attn.A_log",
      "model.layers.44.linear_attn.conv1d",
      "model.layers.44.linear_attn.dt_bias",
      "model.layers.44.linear_attn.in_proj_ba",
      "model.layers.44.linear_attn.norm",
      "model.layers.44.mlp.gate",
      "model.layers.44.mlp.shared_expert_gate",
      "model.layers.44.post_attention_layernorm",
      "model.layers.45.input_layernorm",
      "model.layers.45.linear_attn.A_log",
      "model.layers.45.linear_attn.conv1d",
      "model.layers.45.linear_attn.dt_bias",
      "model.layers.45.linear_attn.in_proj_ba",
      "model.layers.45.linear_attn.norm",
      "model.layers.45.mlp.gate",
      "model.layers.45.mlp.shared_expert_gate",
      "model.layers.45.post_attention_layernorm",
      "model.layers.46.input_layernorm",
      "model.layers.46.linear_attn.A_log",
      "model.layers.46.linear_attn.conv1d",
      "model.layers.46.linear_attn.dt_bias",
      "model.layers.46.linear_attn.in_proj_ba",
      "model.layers.46.linear_attn.norm",
      "model.layers.46.mlp.gate",
      "model.layers.46.mlp.shared_expert_gate",
      "model.layers.46.post_attention_layernorm",
      "model.layers.47.input_layernorm",
      "model.layers.47.mlp.gate",
      "model.layers.47.mlp.shared_expert_gate",
      "model.layers.47.post_attention_layernorm",
      "model.layers.47.self_attn.k_norm",
      "model.layers.47.self_attn.q_norm",
      "mtp.fc",
      "mtp.layers.0.input_layernorm",
      "mtp.layers.0.mlp.gate",
      "mtp.layers.0.mlp.shared_expert_gate",
      "mtp.layers.0.post_attention_layernorm",
      "mtp.layers.0.self_attn.k_norm",
      "mtp.layers.0.self_attn.q_norm",
      "mtp.norm",
      "mtp.pre_fc_norm_embedding",
      "mtp.pre_fc_norm_hidden"
    ],
    "quant_method": "fp8",
    "weight_block_size": [
      128,
      128
    ]
  },
  "rms_norm_eps": 1e-06,
  "rope_parameters": {
    "partial_rotary_factor": 0.25,
    "rope_theta": 10000000,
    "rope_type": "default"
  },
  "router_aux_loss_coef": 0.001,
  "shared_expert_intermediate_size": 512,
  "tie_word_embeddings": false,
  "transformers_version": "5.7.0",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 151936
}

```

</details>

# 模型结构

**模型类**: `Qwen3NextModel`

```
Qwen3NextModel(
  (embed_tokens): Embedding(151936, 2048)
  (layers): ModuleList(
    (0-2): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (3): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (4-6): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (7): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (8-10): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (11): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (12-14): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (15): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (16-18): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (19): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (20-22): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (23): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (24-26): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (27): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (28-30): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (31): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (32-34): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (35): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (36-38): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (39): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (40-42): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (43): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (44-46): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (47): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
  )
  (norm): Qwen3NextRMSNorm((2048,), eps=1e-06)
  (rotary_emb): Qwen3NextRotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 8 个 `safetensors` 文件
- **文件总大小**: 76.42 GB
- **权重张量数**: 151,479
- **参数总量**: 81,329,784,384
- **张量累计大小**: 76.40 GB
- **压缩**: 151479 → 68 行 (合并相同 shape/dtype 的 experts 和 layers)

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[151936, 2048]` | `torch.bfloat16` | 593.50 MB | model-00001-of-00008.safetensors |
| `model.embed_tokens.weight` | `[151936, 2048]` | `torch.bfloat16` | 593.50 MB | model-00001-of-00008.safetensors |
| `model.layers.0-46.linear_attn.A_log` (×36 layers) | `[32]` | `torch.bfloat16` | 2.25 KB | Multi Files |
| `model.layers.0-46.linear_attn.conv1d.weight` (×36 layers) | `[8192, 1, 4]` | `torch.bfloat16` | 2.25 MB | Multi Files |
| `model.layers.0-46.linear_attn.dt_bias` (×36 layers) | `[32]` | `torch.bfloat16` | 2.25 KB | Multi Files |
| `model.layers.0-46.linear_attn.in_proj_ba.weight` (×36 layers) | `[64, 2048]` | `torch.bfloat16` | 9.00 MB | Multi Files |
| `model.layers.0-46.linear_attn.in_proj_qkvz.weight` (×36 layers) | `[12288, 2048]` | `torch.float8_e4m3fn` | 864.00 MB | Multi Files |
| `model.layers.0-46.linear_attn.in_proj_qkvz.weight_scale_inv` (×36 layers) | `[96, 16]` | `torch.float32` | 216.00 KB | Multi Files |
| `model.layers.0-46.linear_attn.norm.weight` (×36 layers) | `[128]` | `torch.bfloat16` | 9.00 KB | Multi Files |
| `model.layers.0-46.linear_attn.out_proj.weight` (×36 layers) | `[2048, 4096]` | `torch.float8_e4m3fn` | 288.00 MB | Multi Files |
| `model.layers.0-46.linear_attn.out_proj.weight_scale_inv` (×36 layers) | `[16, 32]` | `torch.float32` | 72.00 KB | Multi Files |
| `model.layers.0-47.input_layernorm.weight` (×48 layers) | `[2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `model.layers.0-47.mlp.experts.0-511.down_proj.weight` (×48 layers, ×512 experts) | `[2048, 512]` | `torch.float8_e4m3fn` | 24.00 GB | Multi Files |
| `model.layers.0-47.mlp.experts.0-511.down_proj.weight_scale_inv` (×48 layers, ×512 experts) | `[16, 4]` | `torch.float32` | 6.00 MB | Multi Files |
| `model.layers.0-47.mlp.experts.0-511.gate_proj.weight` (×48 layers, ×512 experts) | `[512, 2048]` | `torch.float8_e4m3fn` | 24.00 GB | Multi Files |
| `model.layers.0-47.mlp.experts.0-511.gate_proj.weight_scale_inv` (×48 layers, ×512 experts) | `[4, 16]` | `torch.float32` | 6.00 MB | Multi Files |
| `model.layers.0-47.mlp.experts.0-511.up_proj.weight` (×48 layers, ×512 experts) | `[512, 2048]` | `torch.float8_e4m3fn` | 24.00 GB | Multi Files |
| `model.layers.0-47.mlp.experts.0-511.up_proj.weight_scale_inv` (×48 layers, ×512 experts) | `[4, 16]` | `torch.float32` | 6.00 MB | Multi Files |
| `model.layers.0-47.mlp.gate.weight` (×48 layers) | `[512, 2048]` | `torch.bfloat16` | 96.00 MB | Multi Files |
| `model.layers.0-47.mlp.shared_expert.down_proj.weight` (×48 layers) | `[2048, 512]` | `torch.float8_e4m3fn` | 48.00 MB | Multi Files |
| `model.layers.0-47.mlp.shared_expert.down_proj.weight_scale_inv` (×48 layers) | `[16, 4]` | `torch.float32` | 12.00 KB | Multi Files |
| `model.layers.0-47.mlp.shared_expert.gate_proj.weight` (×48 layers) | `[512, 2048]` | `torch.float8_e4m3fn` | 48.00 MB | Multi Files |
| `model.layers.0-47.mlp.shared_expert.gate_proj.weight_scale_inv` (×48 layers) | `[4, 16]` | `torch.float32` | 12.00 KB | Multi Files |
| `model.layers.0-47.mlp.shared_expert.up_proj.weight` (×48 layers) | `[512, 2048]` | `torch.float8_e4m3fn` | 48.00 MB | Multi Files |
| `model.layers.0-47.mlp.shared_expert.up_proj.weight_scale_inv` (×48 layers) | `[4, 16]` | `torch.float32` | 12.00 KB | Multi Files |
| `model.layers.0-47.mlp.shared_expert_gate.weight` (×48 layers) | `[1, 2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `model.layers.0-47.post_attention_layernorm.weight` (×48 layers) | `[2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `model.layers.3-47.self_attn.k_norm.weight` (×12 layers) | `[256]` | `torch.bfloat16` | 6.00 KB | Multi Files |
| `model.layers.3-47.self_attn.k_proj.weight` (×12 layers) | `[512, 2048]` | `torch.float8_e4m3fn` | 12.00 MB | Multi Files |
| `model.layers.3-47.self_attn.k_proj.weight_scale_inv` (×12 layers) | `[4, 16]` | `torch.float32` | 3.00 KB | Multi Files |
| `model.layers.3-47.self_attn.o_proj.weight` (×12 layers) | `[2048, 4096]` | `torch.float8_e4m3fn` | 96.00 MB | Multi Files |
| `model.layers.3-47.self_attn.o_proj.weight_scale_inv` (×12 layers) | `[16, 32]` | `torch.float32` | 24.00 KB | Multi Files |
| `model.layers.3-47.self_attn.q_norm.weight` (×12 layers) | `[256]` | `torch.bfloat16` | 6.00 KB | Multi Files |
| `model.layers.3-47.self_attn.q_proj.weight` (×12 layers) | `[8192, 2048]` | `torch.float8_e4m3fn` | 192.00 MB | Multi Files |
| `model.layers.3-47.self_attn.q_proj.weight_scale_inv` (×12 layers) | `[64, 16]` | `torch.float32` | 48.00 KB | Multi Files |
| `model.layers.3-47.self_attn.v_proj.weight` (×12 layers) | `[512, 2048]` | `torch.float8_e4m3fn` | 12.00 MB | Multi Files |
| `model.layers.3-47.self_attn.v_proj.weight_scale_inv` (×12 layers) | `[4, 16]` | `torch.float32` | 3.00 KB | Multi Files |
| `model.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00008-of-00008.safetensors |
| `mtp.fc.weight` | `[2048, 4096]` | `torch.bfloat16` | 16.00 MB | model-00008-of-00008.safetensors |
| `mtp.layers.0.input_layernorm.weight` (×1 layers) | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.experts.0-511.down_proj.weight` (×1 layers, ×512 experts) | `[2048, 512]` | `torch.float8_e4m3fn` | 512.00 MB | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.experts.0-511.down_proj.weight_scale_inv` (×1 layers, ×512 experts) | `[16, 4]` | `torch.float32` | 128.00 KB | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.experts.0-511.gate_proj.weight` (×1 layers, ×512 experts) | `[512, 2048]` | `torch.float8_e4m3fn` | 512.00 MB | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.experts.0-511.gate_proj.weight_scale_inv` (×1 layers, ×512 experts) | `[4, 16]` | `torch.float32` | 128.00 KB | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.experts.0-511.up_proj.weight` (×1 layers, ×512 experts) | `[512, 2048]` | `torch.float8_e4m3fn` | 512.00 MB | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.experts.0-511.up_proj.weight_scale_inv` (×1 layers, ×512 experts) | `[4, 16]` | `torch.float32` | 128.00 KB | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.gate.weight` (×1 layers) | `[512, 2048]` | `torch.bfloat16` | 2.00 MB | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.shared_expert.down_proj.weight` (×1 layers) | `[2048, 512]` | `torch.float8_e4m3fn` | 1.00 MB | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.shared_expert.down_proj.weight_scale_inv` (×1 layers) | `[16, 4]` | `torch.float32` | 256.00 B | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.shared_expert.gate_proj.weight` (×1 layers) | `[512, 2048]` | `torch.float8_e4m3fn` | 1.00 MB | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.shared_expert.gate_proj.weight_scale_inv` (×1 layers) | `[4, 16]` | `torch.float32` | 256.00 B | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.shared_expert.up_proj.weight` (×1 layers) | `[512, 2048]` | `torch.float8_e4m3fn` | 1.00 MB | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.shared_expert.up_proj.weight_scale_inv` (×1 layers) | `[4, 16]` | `torch.float32` | 256.00 B | model-00008-of-00008.safetensors |
| `mtp.layers.0.mlp.shared_expert_gate.weight` (×1 layers) | `[1, 2048]` | `torch.bfloat16` | 4.00 KB | model-00008-of-00008.safetensors |
| `mtp.layers.0.post_attention_layernorm.weight` (×1 layers) | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00008-of-00008.safetensors |
| `mtp.layers.0.self_attn.k_norm.weight` (×1 layers) | `[256]` | `torch.bfloat16` | 512.00 B | model-00008-of-00008.safetensors |
| `mtp.layers.0.self_attn.k_proj.weight` (×1 layers) | `[512, 2048]` | `torch.float8_e4m3fn` | 1.00 MB | model-00008-of-00008.safetensors |
| `mtp.layers.0.self_attn.k_proj.weight_scale_inv` (×1 layers) | `[4, 16]` | `torch.float32` | 256.00 B | model-00008-of-00008.safetensors |
| `mtp.layers.0.self_attn.o_proj.weight` (×1 layers) | `[2048, 4096]` | `torch.float8_e4m3fn` | 8.00 MB | model-00008-of-00008.safetensors |
| `mtp.layers.0.self_attn.o_proj.weight_scale_inv` (×1 layers) | `[16, 32]` | `torch.float32` | 2.00 KB | model-00008-of-00008.safetensors |
| `mtp.layers.0.self_attn.q_norm.weight` (×1 layers) | `[256]` | `torch.bfloat16` | 512.00 B | model-00008-of-00008.safetensors |
| `mtp.layers.0.self_attn.q_proj.weight` (×1 layers) | `[8192, 2048]` | `torch.float8_e4m3fn` | 16.00 MB | model-00008-of-00008.safetensors |
| `mtp.layers.0.self_attn.q_proj.weight_scale_inv` (×1 layers) | `[64, 16]` | `torch.float32` | 4.00 KB | model-00008-of-00008.safetensors |
| `mtp.layers.0.self_attn.v_proj.weight` (×1 layers) | `[512, 2048]` | `torch.float8_e4m3fn` | 1.00 MB | model-00008-of-00008.safetensors |
| `mtp.layers.0.self_attn.v_proj.weight_scale_inv` (×1 layers) | `[4, 16]` | `torch.float32` | 256.00 B | model-00008-of-00008.safetensors |
| `mtp.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00008-of-00008.safetensors |
| `mtp.pre_fc_norm_embedding.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00008-of-00008.safetensors |
| `mtp.pre_fc_norm_hidden.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00008-of-00008.safetensors |

</details>

