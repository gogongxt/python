# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen3.5-4B`

# 模型配置

- **模型类型**: `Qwen3_5Config`
- **数据类型**: `None`
- **隐藏层大小**: N/A
- **层数**: N/A
- **注意力头数**: N/A
- **词表大小**: N/A
- **中间层大小**: N/A

<details><summary>完整配置</summary>

```
Qwen3_5Config {
  "architectures": [
    "Qwen3_5ForConditionalGeneration"
  ],
  "image_token_id": 248056,
  "model_type": "qwen3_5",
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
    "hidden_size": 2560,
    "initializer_range": 0.02,
    "intermediate_size": 9216,
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
    "model_type": "qwen3_5_text",
    "mtp_num_hidden_layers": 1,
    "mtp_use_dedicated_embeddings": false,
    "num_attention_heads": 16,
    "num_hidden_layers": 32,
    "num_key_value_heads": 4,
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
    "tie_word_embeddings": true,
    "use_cache": true,
    "vocab_size": 248320
  },
  "tie_word_embeddings": true,
  "transformers_version": "5.7.0",
  "video_token_id": 248057,
  "vision_config": {
    "deepstack_visual_indexes": [],
    "depth": 24,
    "hidden_act": "gelu_pytorch_tanh",
    "hidden_size": 1024,
    "in_channels": 3,
    "initializer_range": 0.02,
    "intermediate_size": 4096,
    "model_type": "qwen3_5_vision",
    "num_heads": 16,
    "num_position_embeddings": 2304,
    "out_hidden_size": 2560,
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
      (proj): Conv3d(3, 1024, kernel_size=(2, 16, 16), stride=(2, 16, 16))
    )
    (pos_embed): Embedding(2304, 1024)
    (rotary_pos_emb): Qwen3_5VisionRotaryEmbedding()
    (blocks): ModuleList(
      (0-23): 24 x Qwen3_5VisionBlock(
        (norm1): LayerNorm((1024,), eps=1e-06, elementwise_affine=True)
        (norm2): LayerNorm((1024,), eps=1e-06, elementwise_affine=True)
        (attn): Qwen3_5VisionAttention(
          (qkv): Linear(in_features=1024, out_features=3072, bias=True)
          (proj): Linear(in_features=1024, out_features=1024, bias=True)
        )
        (mlp): Qwen3_5VisionMLP(
          (linear_fc1): Linear(in_features=1024, out_features=4096, bias=True)
          (linear_fc2): Linear(in_features=4096, out_features=1024, bias=True)
          (act_fn): GELUTanh()
        )
      )
    )
    (merger): Qwen3_5VisionPatchMerger(
      (norm): LayerNorm((1024,), eps=1e-06, elementwise_affine=True)
      (linear_fc1): Linear(in_features=4096, out_features=4096, bias=True)
      (act_fn): GELU(approximate='none')
      (linear_fc2): Linear(in_features=4096, out_features=2560, bias=True)
    )
  )
  (language_model): Qwen3_5TextModel(
    (embed_tokens): Embedding(248320, 2560)
    (layers): ModuleList(
      (0-2): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (in_proj_qkv): Linear(in_features=2560, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2560, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2560, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2560, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (3): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=2560, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (v_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (4-6): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (in_proj_qkv): Linear(in_features=2560, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2560, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2560, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2560, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (7): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=2560, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (v_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (8-10): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (in_proj_qkv): Linear(in_features=2560, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2560, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2560, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2560, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (11): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=2560, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (v_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (12-14): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (in_proj_qkv): Linear(in_features=2560, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2560, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2560, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2560, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (15): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=2560, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (v_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (16-18): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (in_proj_qkv): Linear(in_features=2560, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2560, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2560, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2560, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (19): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=2560, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (v_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (20-22): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (in_proj_qkv): Linear(in_features=2560, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2560, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2560, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2560, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (23): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=2560, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (v_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (24-26): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (in_proj_qkv): Linear(in_features=2560, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2560, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2560, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2560, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (27): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=2560, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (v_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (28-30): 3 x Qwen3_5DecoderLayer(
        (linear_attn): Qwen3_5GatedDeltaNet(
          (act): SiLUActivation()
          (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
          (norm): Qwen3_5RMSNormGated()
          (out_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (in_proj_qkv): Linear(in_features=2560, out_features=8192, bias=False)
          (in_proj_z): Linear(in_features=2560, out_features=4096, bias=False)
          (in_proj_b): Linear(in_features=2560, out_features=32, bias=False)
          (in_proj_a): Linear(in_features=2560, out_features=32, bias=False)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
      (31): Qwen3_5DecoderLayer(
        (self_attn): Qwen3_5Attention(
          (q_proj): Linear(in_features=2560, out_features=8192, bias=False)
          (k_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (v_proj): Linear(in_features=2560, out_features=1024, bias=False)
          (o_proj): Linear(in_features=4096, out_features=2560, bias=False)
          (q_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
          (k_norm): Qwen3_5RMSNorm((256,), eps=1e-06)
        )
        (mlp): Qwen3_5MLP(
          (gate_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (up_proj): Linear(in_features=2560, out_features=9216, bias=False)
          (down_proj): Linear(in_features=9216, out_features=2560, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
        (post_attention_layernorm): Qwen3_5RMSNorm((2560,), eps=1e-06)
      )
    )
    (norm): Qwen3_5RMSNorm((2560,), eps=1e-06)
    (rotary_emb): Qwen3_5TextRotaryEmbedding()
  )
)
```

# 权重统计

- **权重文件**: 2 个 `safetensors` 文件
- **文件总大小**: 8.68 GB
- **权重张量数**: 738
- **参数总量**: 4,659,865,088
- **张量累计大小**: 8.68 GB
- **压缩**: 738 → 58 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `model.language_model.embed_tokens.weight` | `[248320, 2560]` | `torch.bfloat16` | 1.18 GB | model.safetensors-00001-of-00002.safetensors |
| `model.language_model.layers.0-30.linear_attn.A_log` (×24 layers) | `[32]` | `torch.float32` | 3.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.0-30.linear_attn.conv1d.weight` (×24 layers) | `[8192, 1, 4]` | `torch.bfloat16` | 1.50 MB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.0-30.linear_attn.dt_bias` (×24 layers) | `[32]` | `torch.bfloat16` | 1.50 KB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.0-30.linear_attn.in_proj_a.weight` (×24 layers) | `[32, 2560]` | `torch.bfloat16` | 3.75 MB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.0-30.linear_attn.in_proj_b.weight` (×24 layers) | `[32, 2560]` | `torch.bfloat16` | 3.75 MB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.0-30.linear_attn.in_proj_qkv.weight` (×24 layers) | `[8192, 2560]` | `torch.bfloat16` | 960.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.0-30.linear_attn.in_proj_z.weight` (×24 layers) | `[4096, 2560]` | `torch.bfloat16` | 480.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.0-30.linear_attn.norm.weight` (×24 layers) | `[128]` | `torch.float32` | 12.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.0-30.linear_attn.out_proj.weight` (×24 layers) | `[2560, 4096]` | `torch.bfloat16` | 480.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.0-31.input_layernorm.weight` (×32 layers) | `[2560]` | `torch.bfloat16` | 160.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.0-31.mlp.down_proj.weight` (×32 layers) | `[2560, 9216]` | `torch.bfloat16` | 1.41 GB | Multi Files |
| `model.language_model.layers.0-31.mlp.gate_proj.weight` (×32 layers) | `[9216, 2560]` | `torch.bfloat16` | 1.41 GB | Multi Files |
| `model.language_model.layers.0-31.mlp.up_proj.weight` (×32 layers) | `[9216, 2560]` | `torch.bfloat16` | 1.41 GB | Multi Files |
| `model.language_model.layers.0-31.post_attention_layernorm.weight` (×32 layers) | `[2560]` | `torch.bfloat16` | 160.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.3-31.self_attn.k_norm.weight` (×8 layers) | `[256]` | `torch.bfloat16` | 4.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.3-31.self_attn.k_proj.weight` (×8 layers) | `[1024, 2560]` | `torch.bfloat16` | 40.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.3-31.self_attn.o_proj.weight` (×8 layers) | `[2560, 4096]` | `torch.bfloat16` | 160.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.3-31.self_attn.q_norm.weight` (×8 layers) | `[256]` | `torch.bfloat16` | 4.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.3-31.self_attn.q_proj.weight` (×8 layers) | `[8192, 2560]` | `torch.bfloat16` | 320.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.layers.3-31.self_attn.v_proj.weight` (×8 layers) | `[1024, 2560]` | `torch.bfloat16` | 40.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.language_model.norm.weight` | `[2560]` | `torch.bfloat16` | 5.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.blocks.0-23.attn.proj.bias` (×24 blocks) | `[1024]` | `torch.bfloat16` | 48.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.blocks.0-23.attn.proj.weight` (×24 blocks) | `[1024, 1024]` | `torch.bfloat16` | 48.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.blocks.0-23.attn.qkv.bias` (×24 blocks) | `[3072]` | `torch.bfloat16` | 144.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.blocks.0-23.attn.qkv.weight` (×24 blocks) | `[3072, 1024]` | `torch.bfloat16` | 144.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.blocks.0-23.mlp.linear_fc1.bias` (×24 blocks) | `[4096]` | `torch.bfloat16` | 192.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.blocks.0-23.mlp.linear_fc1.weight` (×24 blocks) | `[4096, 1024]` | `torch.bfloat16` | 192.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.blocks.0-23.mlp.linear_fc2.bias` (×24 blocks) | `[1024]` | `torch.bfloat16` | 48.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.blocks.0-23.mlp.linear_fc2.weight` (×24 blocks) | `[1024, 4096]` | `torch.bfloat16` | 192.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.blocks.0-23.norm1.bias` (×24 blocks) | `[1024]` | `torch.bfloat16` | 48.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.blocks.0-23.norm1.weight` (×24 blocks) | `[1024]` | `torch.bfloat16` | 48.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.blocks.0-23.norm2.bias` (×24 blocks) | `[1024]` | `torch.bfloat16` | 48.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.blocks.0-23.norm2.weight` (×24 blocks) | `[1024]` | `torch.bfloat16` | 48.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.merger.linear_fc1.bias` | `[4096]` | `torch.bfloat16` | 8.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.merger.linear_fc1.weight` | `[4096, 4096]` | `torch.bfloat16` | 32.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.merger.linear_fc2.bias` | `[2560]` | `torch.bfloat16` | 5.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.merger.linear_fc2.weight` | `[2560, 4096]` | `torch.bfloat16` | 20.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.merger.norm.bias` | `[1024]` | `torch.bfloat16` | 2.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.merger.norm.weight` | `[1024]` | `torch.bfloat16` | 2.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.patch_embed.proj.bias` | `[1024]` | `torch.bfloat16` | 2.00 KB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.patch_embed.proj.weight` | `[1024, 3, 2, 16, 16]` | `torch.bfloat16` | 3.00 MB | model.safetensors-00002-of-00002.safetensors |
| `model.visual.pos_embed.weight` | `[2304, 1024]` | `torch.bfloat16` | 4.50 MB | model.safetensors-00002-of-00002.safetensors |
| `mtp.fc.weight` | `[2560, 5120]` | `torch.bfloat16` | 25.00 MB | model.safetensors-00002-of-00002.safetensors |
| `mtp.layers.0.input_layernorm.weight` (×1 layers) | `[2560]` | `torch.bfloat16` | 5.00 KB | model.safetensors-00002-of-00002.safetensors |
| `mtp.layers.0.mlp.down_proj.weight` (×1 layers) | `[2560, 9216]` | `torch.bfloat16` | 45.00 MB | model.safetensors-00001-of-00002.safetensors |
| `mtp.layers.0.mlp.gate_proj.weight` (×1 layers) | `[9216, 2560]` | `torch.bfloat16` | 45.00 MB | model.safetensors-00001-of-00002.safetensors |
| `mtp.layers.0.mlp.up_proj.weight` (×1 layers) | `[9216, 2560]` | `torch.bfloat16` | 45.00 MB | model.safetensors-00001-of-00002.safetensors |
| `mtp.layers.0.post_attention_layernorm.weight` (×1 layers) | `[2560]` | `torch.bfloat16` | 5.00 KB | model.safetensors-00002-of-00002.safetensors |
| `mtp.layers.0.self_attn.k_norm.weight` (×1 layers) | `[256]` | `torch.bfloat16` | 512.00 B | model.safetensors-00002-of-00002.safetensors |
| `mtp.layers.0.self_attn.k_proj.weight` (×1 layers) | `[1024, 2560]` | `torch.bfloat16` | 5.00 MB | model.safetensors-00002-of-00002.safetensors |
| `mtp.layers.0.self_attn.o_proj.weight` (×1 layers) | `[2560, 4096]` | `torch.bfloat16` | 20.00 MB | model.safetensors-00002-of-00002.safetensors |
| `mtp.layers.0.self_attn.q_norm.weight` (×1 layers) | `[256]` | `torch.bfloat16` | 512.00 B | model.safetensors-00002-of-00002.safetensors |
| `mtp.layers.0.self_attn.q_proj.weight` (×1 layers) | `[8192, 2560]` | `torch.bfloat16` | 40.00 MB | model.safetensors-00002-of-00002.safetensors |
| `mtp.layers.0.self_attn.v_proj.weight` (×1 layers) | `[1024, 2560]` | `torch.bfloat16` | 5.00 MB | model.safetensors-00002-of-00002.safetensors |
| `mtp.norm.weight` | `[2560]` | `torch.bfloat16` | 5.00 KB | model.safetensors-00002-of-00002.safetensors |
| `mtp.pre_fc_norm_embedding.weight` | `[2560]` | `torch.bfloat16` | 5.00 KB | model.safetensors-00002-of-00002.safetensors |
| `mtp.pre_fc_norm_hidden.weight` | `[2560]` | `torch.bfloat16` | 5.00 KB | model.safetensors-00002-of-00002.safetensors |

</details>

