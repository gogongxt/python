# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen3.5-35B-A3B`

# 模型配置

- **模型类型**: `Qwen3_5MoeConfig`
- **数据类型**: `None`
- **隐藏层大小**: N/A
- **层数**: N/A
- **注意力头数**: N/A
- **词表大小**: N/A
- **中间层大小**: N/A

<details><summary>完整配置</summary>

```
Qwen3_5MoeConfig {
  "architectures": [
    "Qwen3_5MoeForConditionalGeneration"
  ],
  "image_token_id": 248056,
  "model_type": "qwen3_5_moe",
  "text_config": {
    "attention_bias": false,
    "attention_dropout": 0.0,
    "attn_output_gate": true,
    "bos_token_id": null,
    "dtype": "bfloat16",
    "eos_token_id": 248044,
    "full_attention_interval": 4,
    "head_dim": 256,
    "hidden_act": "silu",
    "hidden_size": 2048,
    "initializer_range": 0.02,
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
      "full_attention"
    ],
    "linear_conv_kernel_dim": 4,
    "linear_key_head_dim": 128,
    "linear_num_key_heads": 16,
    "linear_num_value_heads": 32,
    "linear_value_head_dim": 128,
    "mamba_ssm_dtype": "float32",
    "max_position_embeddings": 262144,
    "mlp_only_layers": [],
    "model_type": "qwen3_5_moe_text",
    "moe_intermediate_size": 512,
    "mtp_num_hidden_layers": 1,
    "mtp_use_dedicated_embeddings": false,
    "num_attention_heads": 16,
    "num_experts": 256,
    "num_experts_per_tok": 8,
    "num_hidden_layers": 40,
    "num_key_value_heads": 2,
    "output_router_logits": false,
    "pad_token_id": null,
    "partial_rotary_factor": 0.25,
    "rms_norm_eps": 1e-06,
    "rope_parameters": {
      "mrope_interleaved": true,
      "mrope_section": [
        11,
        11,
        10
      ],
      "partial_rotary_factor": 0.25,
      "rope_theta": 10000000,
      "rope_type": "default"
    },
    "router_aux_loss_coef": 0.001,
    "shared_expert_intermediate_size": 512,
    "tie_word_embeddings": false,
    "use_cache": true,
    "vocab_size": 248320
  },
  "tie_word_embeddings": false,
  "transformers_version": "5.7.0",
  "video_token_id": 248057,
  "vision_config": {
    "deepstack_visual_indexes": [],
    "depth": 27,
    "hidden_act": "gelu_pytorch_tanh",
    "hidden_size": 1152,
    "in_channels": 3,
    "initializer_range": 0.02,
    "intermediate_size": 4304,
    "model_type": "qwen3_5_moe_vision",
    "num_heads": 16,
    "num_position_embeddings": 2304,
    "out_hidden_size": 2048,
    "patch_size": 16,
    "spatial_merge_size": 2,
    "temporal_patch_size": 2
  },
  "vision_end_token_id": 248054,
  "vision_start_token_id": 248053
}

```

</details>

# 模型结构

**模型类**: `Qwen3_5MoeModel`

```
Qwen3_5MoeModel(
  (visual): Qwen3_5MoeVisionModel(
    (patch_embed): Qwen3_5MoeVisionPatchEmbed(
      (proj): Conv3d(3, 1152, kernel_size=(2, 16, 16), stride=(2, 16, 16))
    )
    (pos_embed): Embedding(2304, 1152)
    (rotary_pos_emb): Qwen3_5MoeVisionRotaryEmbedding()
    (blocks): ModuleList(
      (0-26): 27 x Qwen3_5MoeVisionBlock(
        (norm1): LayerNorm((1152,), eps=1e-06, elementwise_affine=True)
        (norm2): LayerNorm((1152,), eps=1e-06, elementwise_affine=True)
        (attn): Qwen3_5MoeVisionAttention(
          (qkv): Linear(in_features=1152, out_features=3456, bias=True)
          (proj): Linear(in_features=1152, out_features=1152, bias=True)
        )
        (mlp): Qwen3_5MoeVisionMLP(
          (linear_fc1): Linear(in_features=1152, out_features=4304, bias=True)
          (linear_fc2): Linear(in_features=4304, out_features=1152, bias=True)
          (act_fn): GELUTanh()
        )
      )
    )
    (merger): Qwen3_5MoeVisionPatchMerger(
      (norm): LayerNorm((1152,), eps=1e-06, elementwise_affine=True)
      (linear_fc1): Linear(in_features=4608, out_features=4608, bias=True)
      (act_fn): GELU(approximate='none')
      (linear_fc2): Linear(in_features=4608, out_features=2048, bias=True)
    )
  )
  (language_model): Qwen3_5MoeTextModel(
    (embed_tokens): Embedding(248320, 2048)
    (layers): ModuleList(
      (0-2): 3 x Qwen3_5MoeDecoderLayer(
        (linear_attn): Qwen3_5MoeGatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5MoeRMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (in_proj_qkv): Linear(in_features=2048, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2048, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2048, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2048, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (3): Qwen3_5MoeDecoderLayer(
        (self_attn): Qwen3_5MoeAttention(
          (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2048, out_features=512, bias=False)
          (v_proj): Linear(in_features=2048, out_features=512, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (q_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (4-6): 3 x Qwen3_5MoeDecoderLayer(
        (linear_attn): Qwen3_5MoeGatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5MoeRMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (in_proj_qkv): Linear(in_features=2048, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2048, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2048, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2048, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (7): Qwen3_5MoeDecoderLayer(
        (self_attn): Qwen3_5MoeAttention(
          (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2048, out_features=512, bias=False)
          (v_proj): Linear(in_features=2048, out_features=512, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (q_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (8-10): 3 x Qwen3_5MoeDecoderLayer(
        (linear_attn): Qwen3_5MoeGatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5MoeRMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (in_proj_qkv): Linear(in_features=2048, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2048, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2048, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2048, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (11): Qwen3_5MoeDecoderLayer(
        (self_attn): Qwen3_5MoeAttention(
          (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2048, out_features=512, bias=False)
          (v_proj): Linear(in_features=2048, out_features=512, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (q_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (12-14): 3 x Qwen3_5MoeDecoderLayer(
        (linear_attn): Qwen3_5MoeGatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5MoeRMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (in_proj_qkv): Linear(in_features=2048, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2048, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2048, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2048, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (15): Qwen3_5MoeDecoderLayer(
        (self_attn): Qwen3_5MoeAttention(
          (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2048, out_features=512, bias=False)
          (v_proj): Linear(in_features=2048, out_features=512, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (q_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (16-18): 3 x Qwen3_5MoeDecoderLayer(
        (linear_attn): Qwen3_5MoeGatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5MoeRMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (in_proj_qkv): Linear(in_features=2048, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2048, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2048, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2048, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (19): Qwen3_5MoeDecoderLayer(
        (self_attn): Qwen3_5MoeAttention(
          (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2048, out_features=512, bias=False)
          (v_proj): Linear(in_features=2048, out_features=512, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (q_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (20-22): 3 x Qwen3_5MoeDecoderLayer(
        (linear_attn): Qwen3_5MoeGatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5MoeRMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (in_proj_qkv): Linear(in_features=2048, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2048, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2048, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2048, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (23): Qwen3_5MoeDecoderLayer(
        (self_attn): Qwen3_5MoeAttention(
          (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2048, out_features=512, bias=False)
          (v_proj): Linear(in_features=2048, out_features=512, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (q_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (24-26): 3 x Qwen3_5MoeDecoderLayer(
        (linear_attn): Qwen3_5MoeGatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5MoeRMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (in_proj_qkv): Linear(in_features=2048, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2048, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2048, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2048, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (27): Qwen3_5MoeDecoderLayer(
        (self_attn): Qwen3_5MoeAttention(
          (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2048, out_features=512, bias=False)
          (v_proj): Linear(in_features=2048, out_features=512, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (q_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (28-30): 3 x Qwen3_5MoeDecoderLayer(
        (linear_attn): Qwen3_5MoeGatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5MoeRMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (in_proj_qkv): Linear(in_features=2048, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2048, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2048, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2048, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (31): Qwen3_5MoeDecoderLayer(
        (self_attn): Qwen3_5MoeAttention(
          (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2048, out_features=512, bias=False)
          (v_proj): Linear(in_features=2048, out_features=512, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (q_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (32-34): 3 x Qwen3_5MoeDecoderLayer(
        (linear_attn): Qwen3_5MoeGatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5MoeRMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (in_proj_qkv): Linear(in_features=2048, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2048, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2048, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2048, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (35): Qwen3_5MoeDecoderLayer(
        (self_attn): Qwen3_5MoeAttention(
          (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2048, out_features=512, bias=False)
          (v_proj): Linear(in_features=2048, out_features=512, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (q_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (36-38): 3 x Qwen3_5MoeDecoderLayer(
        (linear_attn): Qwen3_5MoeGatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5MoeRMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (in_proj_qkv): Linear(in_features=2048, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2048, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2048, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2048, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
      (39): Qwen3_5MoeDecoderLayer(
        (self_attn): Qwen3_5MoeAttention(
          (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2048, out_features=512, bias=False)
          (v_proj): Linear(in_features=2048, out_features=512, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
          (q_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5MoeRMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MoeSparseMoeBlock(
          (gate): Qwen3_5MoeTopKRouter()
          (experts): Qwen3_5MoeExperts(
            (act_fn): SiLUActivation()
          )
          (shared_expert): Qwen3_5MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
            (up_proj): Linear(in_features=2048, out_features=512, bias=False)
            (down_proj): Linear(in_features=512, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
          (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
        )
        (input_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
      )
    )
    (norm): Qwen3_5MoeRMSNorm((2048,), eps=1e-06)
    (rotary_emb): Qwen3_5MoeTextRotaryEmbedding()
  )
)
```

# 权重统计

- **权重文件**: 14 个 `safetensors` 文件
- **文件总大小**: 66.97 GB
- **权重张量数**: 1,811
- **参数总量**: 35,951,822,704
- **张量累计大小**: 66.97 GB
- **压缩**: 1811 → 68 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[248320, 2048]` | `torch.bfloat16` | 970.00 MB | model.safetensors-00009-of-00014.safetensors |
| `model.language_model.embed_tokens.weight` | `[248320, 2048]` | `torch.bfloat16` | 970.00 MB | model.safetensors-00009-of-00014.safetensors |
| `model.language_model.layers.0-38.linear_attn.A_log` (×30 layers) | `[32]` | `torch.float32` | 3.75 KB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.0-38.linear_attn.conv1d.weight` (×30 layers) | `[8192, 1, 4]` | `torch.bfloat16` | 1.88 MB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.0-38.linear_attn.dt_bias` (×30 layers) | `[32]` | `torch.bfloat16` | 1.88 KB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.0-38.linear_attn.in_proj_a.weight` (×30 layers) | `[32, 2048]` | `torch.bfloat16` | 3.75 MB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.0-38.linear_attn.in_proj_b.weight` (×30 layers) | `[32, 2048]` | `torch.bfloat16` | 3.75 MB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.0-38.linear_attn.in_proj_qkv.weight` (×30 layers) | `[8192, 2048]` | `torch.bfloat16` | 960.00 MB | model.safetensors-00013-of-00014.safetensors |
| `model.language_model.layers.0-38.linear_attn.in_proj_z.weight` (×30 layers) | `[4096, 2048]` | `torch.bfloat16` | 480.00 MB | model.safetensors-00013-of-00014.safetensors |
| `model.language_model.layers.0-38.linear_attn.norm.weight` (×30 layers) | `[128]` | `torch.float32` | 15.00 KB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.0-38.linear_attn.out_proj.weight` (×30 layers) | `[2048, 4096]` | `torch.bfloat16` | 480.00 MB | model.safetensors-00013-of-00014.safetensors |
| `model.language_model.layers.0-39.input_layernorm.weight` (×40 layers) | `[2048]` | `torch.bfloat16` | 160.00 KB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.0-39.mlp.experts.down_proj` (×40 layers) | `[256, 2048, 512]` | `torch.bfloat16` | 20.00 GB | Multi Files |
| `model.language_model.layers.0-39.mlp.experts.gate_up_proj` (×40 layers) | `[256, 1024, 2048]` | `torch.bfloat16` | 40.00 GB | Multi Files |
| `model.language_model.layers.0-39.mlp.gate.weight` (×40 layers) | `[256, 2048]` | `torch.bfloat16` | 40.00 MB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.0-39.mlp.shared_expert.down_proj.weight` (×40 layers) | `[2048, 512]` | `torch.bfloat16` | 80.00 MB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.0-39.mlp.shared_expert.gate_proj.weight` (×40 layers) | `[512, 2048]` | `torch.bfloat16` | 80.00 MB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.0-39.mlp.shared_expert.up_proj.weight` (×40 layers) | `[512, 2048]` | `torch.bfloat16` | 80.00 MB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.0-39.mlp.shared_expert_gate.weight` (×40 layers) | `[1, 2048]` | `torch.bfloat16` | 160.00 KB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.0-39.post_attention_layernorm.weight` (×40 layers) | `[2048]` | `torch.bfloat16` | 160.00 KB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.3-39.self_attn.k_norm.weight` (×10 layers) | `[256]` | `torch.bfloat16` | 5.00 KB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.3-39.self_attn.k_proj.weight` (×10 layers) | `[512, 2048]` | `torch.bfloat16` | 20.00 MB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.3-39.self_attn.o_proj.weight` (×10 layers) | `[2048, 4096]` | `torch.bfloat16` | 160.00 MB | model.safetensors-00013-of-00014.safetensors |
| `model.language_model.layers.3-39.self_attn.q_norm.weight` (×10 layers) | `[256]` | `torch.bfloat16` | 5.00 KB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.layers.3-39.self_attn.q_proj.weight` (×10 layers) | `[8192, 2048]` | `torch.bfloat16` | 320.00 MB | model.safetensors-00013-of-00014.safetensors |
| `model.language_model.layers.3-39.self_attn.v_proj.weight` (×10 layers) | `[512, 2048]` | `torch.bfloat16` | 20.00 MB | model.safetensors-00014-of-00014.safetensors |
| `model.language_model.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.blocks.0-26.attn.proj.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.blocks.0-26.attn.proj.weight` (×27 blocks) | `[1152, 1152]` | `torch.bfloat16` | 68.34 MB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.blocks.0-26.attn.qkv.bias` (×27 blocks) | `[3456]` | `torch.bfloat16` | 182.25 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.blocks.0-26.attn.qkv.weight` (×27 blocks) | `[3456, 1152]` | `torch.bfloat16` | 205.03 MB | Multi Files |
| `model.visual.blocks.0-26.mlp.linear_fc1.bias` (×27 blocks) | `[4304]` | `torch.bfloat16` | 226.97 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.blocks.0-26.mlp.linear_fc1.weight` (×27 blocks) | `[4304, 1152]` | `torch.bfloat16` | 255.34 MB | model.safetensors-00013-of-00014.safetensors |
| `model.visual.blocks.0-26.mlp.linear_fc2.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.blocks.0-26.mlp.linear_fc2.weight` (×27 blocks) | `[1152, 4304]` | `torch.bfloat16` | 255.34 MB | model.safetensors-00013-of-00014.safetensors |
| `model.visual.blocks.0-26.norm1.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.blocks.0-26.norm1.weight` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.blocks.0-26.norm2.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.blocks.0-26.norm2.weight` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.merger.linear_fc1.bias` | `[4608]` | `torch.bfloat16` | 9.00 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.merger.linear_fc1.weight` | `[4608, 4608]` | `torch.bfloat16` | 40.50 MB | model.safetensors-00013-of-00014.safetensors |
| `model.visual.merger.linear_fc2.bias` | `[2048]` | `torch.bfloat16` | 4.00 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.merger.linear_fc2.weight` | `[2048, 4608]` | `torch.bfloat16` | 18.00 MB | model.safetensors-00013-of-00014.safetensors |
| `model.visual.merger.norm.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.merger.norm.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.patch_embed.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.patch_embed.proj.weight` | `[1152, 3, 2, 16, 16]` | `torch.bfloat16` | 3.38 MB | model.safetensors-00014-of-00014.safetensors |
| `model.visual.pos_embed.weight` | `[2304, 1152]` | `torch.bfloat16` | 5.06 MB | model.safetensors-00014-of-00014.safetensors |
| `mtp.fc.weight` | `[2048, 4096]` | `torch.bfloat16` | 16.00 MB | model.safetensors-00013-of-00014.safetensors |
| `mtp.layers.0.input_layernorm.weight` (×1 layers) | `[2048]` | `torch.bfloat16` | 4.00 KB | model.safetensors-00014-of-00014.safetensors |
| `mtp.layers.0.mlp.experts.0-255.down_proj.weight` (×1 layers, ×256 experts) | `[2048, 512]` | `torch.bfloat16` | 512.00 MB | model.safetensors-00014-of-00014.safetensors |
| `mtp.layers.0.mlp.experts.0-255.gate_proj.weight` (×1 layers, ×256 experts) | `[512, 2048]` | `torch.bfloat16` | 512.00 MB | model.safetensors-00014-of-00014.safetensors |
| `mtp.layers.0.mlp.experts.0-255.up_proj.weight` (×1 layers, ×256 experts) | `[512, 2048]` | `torch.bfloat16` | 512.00 MB | model.safetensors-00014-of-00014.safetensors |
| `mtp.layers.0.mlp.gate.weight` (×1 layers) | `[256, 2048]` | `torch.bfloat16` | 1.00 MB | model.safetensors-00014-of-00014.safetensors |
| `mtp.layers.0.mlp.shared_expert.down_proj.weight` (×1 layers) | `[2048, 512]` | `torch.bfloat16` | 2.00 MB | model.safetensors-00014-of-00014.safetensors |
| `mtp.layers.0.mlp.shared_expert.gate_proj.weight` (×1 layers) | `[512, 2048]` | `torch.bfloat16` | 2.00 MB | model.safetensors-00014-of-00014.safetensors |
| `mtp.layers.0.mlp.shared_expert.up_proj.weight` (×1 layers) | `[512, 2048]` | `torch.bfloat16` | 2.00 MB | model.safetensors-00014-of-00014.safetensors |
| `mtp.layers.0.mlp.shared_expert_gate.weight` (×1 layers) | `[1, 2048]` | `torch.bfloat16` | 4.00 KB | model.safetensors-00014-of-00014.safetensors |
| `mtp.layers.0.post_attention_layernorm.weight` (×1 layers) | `[2048]` | `torch.bfloat16` | 4.00 KB | model.safetensors-00014-of-00014.safetensors |
| `mtp.layers.0.self_attn.k_norm.weight` (×1 layers) | `[256]` | `torch.bfloat16` | 512.00 B | model.safetensors-00014-of-00014.safetensors |
| `mtp.layers.0.self_attn.k_proj.weight` (×1 layers) | `[512, 2048]` | `torch.bfloat16` | 2.00 MB | model.safetensors-00014-of-00014.safetensors |
| `mtp.layers.0.self_attn.o_proj.weight` (×1 layers) | `[2048, 4096]` | `torch.bfloat16` | 16.00 MB | model.safetensors-00013-of-00014.safetensors |
| `mtp.layers.0.self_attn.q_norm.weight` (×1 layers) | `[256]` | `torch.bfloat16` | 512.00 B | model.safetensors-00014-of-00014.safetensors |
| `mtp.layers.0.self_attn.q_proj.weight` (×1 layers) | `[8192, 2048]` | `torch.bfloat16` | 32.00 MB | model.safetensors-00013-of-00014.safetensors |
| `mtp.layers.0.self_attn.v_proj.weight` (×1 layers) | `[512, 2048]` | `torch.bfloat16` | 2.00 MB | model.safetensors-00014-of-00014.safetensors |
| `mtp.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model.safetensors-00014-of-00014.safetensors |
| `mtp.pre_fc_norm_embedding.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model.safetensors-00014-of-00014.safetensors |
| `mtp.pre_fc_norm_hidden.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model.safetensors-00014-of-00014.safetensors |

</details>

