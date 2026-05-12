# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen3.6-27B`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/Qwen3.6-27B/config.json`

```json

{
    "architectures": [
        "Qwen3_5ForConditionalGeneration"
    ],
    "image_token_id": 248056,
    "language_model_only": false,
    "model_type": "qwen3_5",
    "text_config": {
        "attention_bias": false,
        "attention_dropout": 0.0,
        "attn_output_gate": true,
        "bos_token_id": 248044,
        "dtype": "bfloat16",
        "eos_token_id": 248044,
        "full_attention_interval": 4,
        "head_dim": 256,
        "hidden_act": "silu",
        "hidden_size": 5120,
        "initializer_range": 0.02,
        "intermediate_size": 17408,
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
        "linear_num_value_heads": 48,
        "linear_value_head_dim": 128,
        "mamba_ssm_dtype": "float32",
        "max_position_embeddings": 262144,
        "model_type": "qwen3_5_text",
        "mtp_num_hidden_layers": 1,
        "mtp_use_dedicated_embeddings": false,
        "num_attention_heads": 24,
        "num_hidden_layers": 64,
        "num_key_value_heads": 4,
        "output_gate_type": "swish",
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
        "tie_word_embeddings": false,
        "use_cache": true,
        "vocab_size": 248320
    },
    "tie_word_embeddings": false,
    "transformers_version": "4.57.1",
    "video_token_id": 248057,
    "vision_config": {
        "deepstack_visual_indexes": [],
        "depth": 27,
        "hidden_act": "gelu_pytorch_tanh",
        "hidden_size": 1152,
        "in_channels": 3,
        "initializer_range": 0.02,
        "intermediate_size": 4304,
        "model_type": "qwen3_5",
        "num_heads": 16,
        "num_position_embeddings": 2304,
        "out_hidden_size": 5120,
        "patch_size": 16,
        "spatial_merge_size": 2,
        "temporal_patch_size": 2
    },
    "vision_end_token_id": 248054,
    "vision_start_token_id": 248053
}
```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `Qwen3_5Config`
- **数据类型**: `None`
- **隐藏层大小**: N/A
- **层数**: N/A
- **注意力头数**: N/A
- **词表大小**: N/A
- **中间层大小**: N/A

```
Qwen3_5Config {
  "architectures": [
    "Qwen3_5ForConditionalGeneration"
  ],
  "image_token_id": 248056,
  "language_model_only": false,
  "model_type": "qwen3_5",
  "text_config": {
    "attention_bias": false,
    "attention_dropout": 0.0,
    "attn_output_gate": true,
    "bos_token_id": 248044,
    "dtype": "bfloat16",
    "eos_token_id": 248044,
    "full_attention_interval": 4,
    "head_dim": 256,
    "hidden_act": "silu",
    "hidden_size": 5120,
    "initializer_range": 0.02,
    "intermediate_size": 17408,
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
    "linear_num_value_heads": 48,
    "linear_value_head_dim": 128,
    "mamba_ssm_dtype": "float32",
    "max_position_embeddings": 262144,
    "model_type": "qwen3_5_text",
    "mtp_num_hidden_layers": 1,
    "mtp_use_dedicated_embeddings": false,
    "num_attention_heads": 24,
    "num_hidden_layers": 64,
    "num_key_value_heads": 4,
    "output_gate_type": "swish",
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
    "model_type": "qwen3_5_vision",
    "num_heads": 16,
    "num_position_embeddings": 2304,
    "out_hidden_size": 5120,
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

**模型类**: `Qwen3_5Model`

```
Qwen3_5Model(
  (visual): Qwen3_5VisionModel(
    (patch_embed): Qwen3_5VisionPatchEmbed(
      (proj): Conv3d(3, 1152, kernel_size=(2, 16, 16), stride=(2, 16, 16))
    )
    (pos_embed): Embedding(2304, 1152)
    (rotary_pos_emb): Qwen3_5VisionRotaryEmbedding()
    (blocks): ModuleList(
      (0-26): 27 x Qwen3_5VisionBlock(
        (norm1): LayerNorm((1152,), eps=1e-06, elementwise_affine=True)
        (norm2): LayerNorm((1152,), eps=1e-06, elementwise_affine=True)
        (attn): Qwen3_5VisionAttention(
          (qkv): Linear(in_features=1152, out_features=3456, bias=True)
          (proj): Linear(in_features=1152, out_features=1152, bias=True)
        )
        (mlp): Qwen3_5VisionMLP(
          (linear_fc1): Linear(in_features=1152, out_features=4304, bias=True)
          (linear_fc2): Linear(in_features=4304, out_features=1152, bias=True)
          (act_fn): GELUTanh()
        )
      )
    )
    (merger): Qwen3_5VisionPatchMerger(
      (norm): LayerNorm((1152,), eps=1e-06, elementwise_affine=True)
      (linear_fc1): Linear(in_features=4608, out_features=4608, bias=True)
      (act_fn): GELU(approximate='none')
      (linear_fc2): Linear(in_features=4608, out_features=5120, bias=True)
    )
  )
  (language_model): Qwen3_5TextModel(
    (embed_tokens): Embedding(248320, 5120)
    (layers): ModuleList(
      (0-2): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (3): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (4-6): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (7): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (8-10): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (11): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (12-14): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (15): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (16-18): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (19): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (20-22): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (23): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (24-26): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (27): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (28-30): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (31): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (32-34): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (35): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (36-38): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (39): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (40-42): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (43): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (44-46): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (47): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (48-50): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (51): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (52-54): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (55): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (56-58): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (59): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (60-62): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(10240, 10240, kernel_size=(4,), stride=(1,), padding=(3,), groups=10240, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (in_proj_qkv): Linear(in_features=5120, out_features=10240, bias=False)
          (in_proj_z): Linear(in_features=5120, out_features=6144, bias=False)
          (in_proj_b): Linear(in_features=5120, out_features=48, bias=False)
          (in_proj_a): Linear(in_features=5120, out_features=48, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
      (63): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=5120, out_features=12288, bias=False)
          (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
          (o_proj): Linear(in_features=6144, out_features=5120, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
          (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((5120,), eps=1e-06)
      )
    )
    (norm): Qwen3_5RMSNorm((5120,), eps=1e-06)
    (rotary_emb): Qwen3_5TextRotaryEmbedding()
  )
)
```

# 权重统计

- **权重文件**: 15 个 `safetensors` 文件
- **文件总大小**: 51.75 GB
- **权重张量数**: 1,199
- **参数总量**: 27,781,427,952
- **张量累计大小**: 51.75 GB
- **压缩**: 1199 → 59 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[248320, 5120]` | `torch.bfloat16` | 2.37 GB | model-00008-of-00015.safetensors |
| `model.language_model.embed_tokens.weight` | `[248320, 5120]` | `torch.bfloat16` | 2.37 GB | model-00001-of-00015.safetensors |
| `model.language_model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62.linear_attn.A_log` (×48 layers) | `[48]` | `torch.bfloat16` | 4.50 KB | Multi Files |
| `model.language_model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62.linear_attn.conv1d.weight` (×48 layers) | `[10240, 1, 4]` | `torch.bfloat16` | 3.75 MB | Multi Files |
| `model.language_model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62.linear_attn.dt_bias` (×48 layers) | `[48]` | `torch.bfloat16` | 4.50 KB | Multi Files |
| `model.language_model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62.linear_attn.in_proj_a.weight` (×48 layers) | `[48, 5120]` | `torch.bfloat16` | 22.50 MB | Multi Files |
| `model.language_model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62.linear_attn.in_proj_b.weight` (×48 layers) | `[48, 5120]` | `torch.bfloat16` | 22.50 MB | Multi Files |
| `model.language_model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62.linear_attn.in_proj_qkv.weight` (×48 layers) | `[10240, 5120]` | `torch.bfloat16` | 4.69 GB | Multi Files |
| `model.language_model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62.linear_attn.in_proj_z.weight` (×48 layers) | `[6144, 5120]` | `torch.bfloat16` | 2.81 GB | Multi Files |
| `model.language_model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62.linear_attn.norm.weight` (×48 layers) | `[128]` | `torch.bfloat16` | 12.00 KB | Multi Files |
| `model.language_model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62.linear_attn.out_proj.weight` (×48 layers) | `[5120, 6144]` | `torch.bfloat16` | 2.81 GB | Multi Files |
| `model.language_model.layers.0-63.input_layernorm.weight` (×64 layers) | `[5120]` | `torch.bfloat16` | 640.00 KB | Multi Files |
| `model.language_model.layers.0-63.mlp.down_proj.weight` (×64 layers) | `[5120, 17408]` | `torch.bfloat16` | 10.62 GB | Multi Files |
| `model.language_model.layers.0-63.mlp.gate_proj.weight` (×64 layers) | `[17408, 5120]` | `torch.bfloat16` | 10.62 GB | Multi Files |
| `model.language_model.layers.0-63.mlp.up_proj.weight` (×64 layers) | `[17408, 5120]` | `torch.bfloat16` | 10.62 GB | Multi Files |
| `model.language_model.layers.0-63.post_attention_layernorm.weight` (×64 layers) | `[5120]` | `torch.bfloat16` | 640.00 KB | Multi Files |
| `model.language_model.layers.3,7,...,59,63.self_attn.k_norm.weight` (×16 layers) | `[256]` | `torch.bfloat16` | 8.00 KB | Multi Files |
| `model.language_model.layers.3,7,...,59,63.self_attn.k_proj.weight` (×16 layers) | `[1024, 5120]` | `torch.bfloat16` | 160.00 MB | Multi Files |
| `model.language_model.layers.3,7,...,59,63.self_attn.o_proj.weight` (×16 layers) | `[5120, 6144]` | `torch.bfloat16` | 960.00 MB | Multi Files |
| `model.language_model.layers.3,7,...,59,63.self_attn.q_norm.weight` (×16 layers) | `[256]` | `torch.bfloat16` | 8.00 KB | Multi Files |
| `model.language_model.layers.3,7,...,59,63.self_attn.q_proj.weight` (×16 layers) | `[12288, 5120]` | `torch.bfloat16` | 1.88 GB | Multi Files |
| `model.language_model.layers.3,7,...,59,63.self_attn.v_proj.weight` (×16 layers) | `[1024, 5120]` | `torch.bfloat16` | 160.00 MB | Multi Files |
| `model.language_model.norm.weight` | `[5120]` | `torch.bfloat16` | 10.00 KB | model-00015-of-00015.safetensors |
| `model.visual.blocks.0-26.attn.proj.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00008-of-00015.safetensors |
| `model.visual.blocks.0-26.attn.proj.weight` (×27 blocks) | `[1152, 1152]` | `torch.bfloat16` | 68.34 MB | model-00008-of-00015.safetensors |
| `model.visual.blocks.0-26.attn.qkv.bias` (×27 blocks) | `[3456]` | `torch.bfloat16` | 182.25 KB | model-00008-of-00015.safetensors |
| `model.visual.blocks.0-26.attn.qkv.weight` (×27 blocks) | `[3456, 1152]` | `torch.bfloat16` | 205.03 MB | Multi Files |
| `model.visual.blocks.0-26.mlp.linear_fc1.bias` (×27 blocks) | `[4304]` | `torch.bfloat16` | 226.97 KB | model-00008-of-00015.safetensors |
| `model.visual.blocks.0-26.mlp.linear_fc1.weight` (×27 blocks) | `[4304, 1152]` | `torch.bfloat16` | 255.34 MB | model-00007-of-00015.safetensors |
| `model.visual.blocks.0-26.mlp.linear_fc2.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00008-of-00015.safetensors |
| `model.visual.blocks.0-26.mlp.linear_fc2.weight` (×27 blocks) | `[1152, 4304]` | `torch.bfloat16` | 255.34 MB | model-00007-of-00015.safetensors |
| `model.visual.blocks.0-26.norm1.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00008-of-00015.safetensors |
| `model.visual.blocks.0-26.norm1.weight` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00008-of-00015.safetensors |
| `model.visual.blocks.0-26.norm2.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00008-of-00015.safetensors |
| `model.visual.blocks.0-26.norm2.weight` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00008-of-00015.safetensors |
| `model.visual.merger.linear_fc1.bias` | `[4608]` | `torch.bfloat16` | 9.00 KB | model-00008-of-00015.safetensors |
| `model.visual.merger.linear_fc1.weight` | `[4608, 4608]` | `torch.bfloat16` | 40.50 MB | model-00007-of-00015.safetensors |
| `model.visual.merger.linear_fc2.bias` | `[5120]` | `torch.bfloat16` | 10.00 KB | model-00008-of-00015.safetensors |
| `model.visual.merger.linear_fc2.weight` | `[5120, 4608]` | `torch.bfloat16` | 45.00 MB | model-00007-of-00015.safetensors |
| `model.visual.merger.norm.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00008-of-00015.safetensors |
| `model.visual.merger.norm.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00008-of-00015.safetensors |
| `model.visual.patch_embed.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00008-of-00015.safetensors |
| `model.visual.patch_embed.proj.weight` | `[1152, 3, 2, 16, 16]` | `torch.bfloat16` | 3.38 MB | model-00008-of-00015.safetensors |
| `model.visual.pos_embed.weight` | `[2304, 1152]` | `torch.bfloat16` | 5.06 MB | model-00008-of-00015.safetensors |
| `mtp.fc.weight` | `[5120, 10240]` | `torch.bfloat16` | 100.00 MB | model-00013-of-00015.safetensors |
| `mtp.layers.0.input_layernorm.weight` | `[5120]` | `torch.bfloat16` | 10.00 KB | model-00015-of-00015.safetensors |
| `mtp.layers.0.mlp.down_proj.weight` | `[5120, 17408]` | `torch.bfloat16` | 170.00 MB | model-00013-of-00015.safetensors |
| `mtp.layers.0.mlp.gate_proj.weight` | `[17408, 5120]` | `torch.bfloat16` | 170.00 MB | model-00013-of-00015.safetensors |
| `mtp.layers.0.mlp.up_proj.weight` | `[17408, 5120]` | `torch.bfloat16` | 170.00 MB | model-00013-of-00015.safetensors |
| `mtp.layers.0.post_attention_layernorm.weight` | `[5120]` | `torch.bfloat16` | 10.00 KB | model-00015-of-00015.safetensors |
| `mtp.layers.0.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00015-of-00015.safetensors |
| `mtp.layers.0.self_attn.k_proj.weight` | `[1024, 5120]` | `torch.bfloat16` | 10.00 MB | model-00013-of-00015.safetensors |
| `mtp.layers.0.self_attn.o_proj.weight` | `[5120, 6144]` | `torch.bfloat16` | 60.00 MB | model-00015-of-00015.safetensors |
| `mtp.layers.0.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00015-of-00015.safetensors |
| `mtp.layers.0.self_attn.q_proj.weight` | `[12288, 5120]` | `torch.bfloat16` | 120.00 MB | model-00013-of-00015.safetensors |
| `mtp.layers.0.self_attn.v_proj.weight` | `[1024, 5120]` | `torch.bfloat16` | 10.00 MB | model-00013-of-00015.safetensors |
| `mtp.norm.weight` | `[5120]` | `torch.bfloat16` | 10.00 KB | model-00015-of-00015.safetensors |
| `mtp.pre_fc_norm_embedding.weight` | `[5120]` | `torch.bfloat16` | 10.00 KB | model-00015-of-00015.safetensors |
| `mtp.pre_fc_norm_hidden.weight` | `[5120]` | `torch.bfloat16` | 10.00 KB | model-00015-of-00015.safetensors |

</details>

