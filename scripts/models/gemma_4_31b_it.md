# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/gemma-4-31B-it`

# 模型配置

- **模型类型**: `Gemma4Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: N/A
- **层数**: N/A
- **注意力头数**: N/A
- **词表大小**: N/A
- **中间层大小**: N/A

<details><summary>完整配置</summary>

```
Gemma4Config {
  "architectures": [
    "Gemma4ForConditionalGeneration"
  ],
  "audio_config": null,
  "audio_token_id": 258881,
  "boa_token_id": 256000,
  "boi_token_id": 255999,
  "dtype": "bfloat16",
  "eoa_token_id": 258883,
  "eoa_token_index": 258883,
  "eoi_token_id": 258882,
  "eos_token_id": [
    1,
    106
  ],
  "image_token_id": 258880,
  "initializer_range": 0.02,
  "model_type": "gemma4",
  "text_config": {
    "attention_bias": false,
    "attention_dropout": 0.0,
    "attention_k_eq_v": true,
    "bos_token_id": 2,
    "dtype": "bfloat16",
    "enable_moe_block": false,
    "eos_token_id": 1,
    "expert_intermediate_size": null,
    "final_logit_softcapping": 30.0,
    "global_head_dim": 512,
    "head_dim": 256,
    "hidden_activation": "gelu_pytorch_tanh",
    "hidden_size": 5376,
    "hidden_size_per_layer_input": 0,
    "initializer_range": 0.02,
    "intermediate_size": 21504,
    "layer_types": [
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "full_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "full_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "full_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "full_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "full_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "full_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "full_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "full_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "full_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "sliding_attention",
      "full_attention"
    ],
    "max_position_embeddings": 262144,
    "model_type": "gemma4_text",
    "moe_intermediate_size": null,
    "num_attention_heads": 32,
    "num_experts": null,
    "num_global_key_value_heads": 4,
    "num_hidden_layers": 60,
    "num_key_value_heads": 16,
    "num_kv_shared_layers": 0,
    "pad_token_id": 0,
    "rms_norm_eps": 1e-06,
    "rope_parameters": {
      "full_attention": {
        "partial_rotary_factor": 0.25,
        "rope_theta": 1000000.0,
        "rope_type": "proportional"
      },
      "sliding_attention": {
        "rope_theta": 10000.0,
        "rope_type": "default"
      }
    },
    "sliding_window": 1024,
    "tie_word_embeddings": true,
    "top_k_experts": null,
    "use_bidirectional_attention": "vision",
    "use_cache": true,
    "use_double_wide_mlp": false,
    "vocab_size": 262144,
    "vocab_size_per_layer_input": 262144
  },
  "tie_word_embeddings": true,
  "transformers_version": "5.7.0",
  "video_token_id": 258884,
  "vision_config": {
    "_name_or_path": "",
    "architectures": null,
    "attention_bias": false,
    "attention_dropout": 0.0,
    "chunk_size_feed_forward": 0,
    "default_output_length": 280,
    "dtype": "bfloat16",
    "global_head_dim": 72,
    "head_dim": 72,
    "hidden_activation": "gelu_pytorch_tanh",
    "hidden_size": 1152,
    "id2label": {
      "0": "LABEL_0",
      "1": "LABEL_1"
    },
    "initializer_range": 0.02,
    "intermediate_size": 4304,
    "is_encoder_decoder": false,
    "label2id": {
      "LABEL_0": 0,
      "LABEL_1": 1
    },
    "max_position_embeddings": 131072,
    "model_type": "gemma4_vision",
    "num_attention_heads": 16,
    "num_hidden_layers": 27,
    "num_key_value_heads": 16,
    "output_attentions": false,
    "output_hidden_states": false,
    "patch_size": 16,
    "pooling_kernel_size": 3,
    "position_embedding_size": 10240,
    "problem_type": null,
    "return_dict": true,
    "rms_norm_eps": 1e-06,
    "rope_parameters": {
      "rope_theta": 100.0,
      "rope_type": "default"
    },
    "standardize": true,
    "use_clipped_linears": false
  },
  "vision_soft_tokens_per_image": 280
}

```

</details>

# 模型结构

**模型类**: `Gemma4Model`

```
Gemma4Model(
  (vision_tower): Gemma4VisionModel(
    (patch_embedder): Gemma4VisionPatchEmbedder(
      (input_proj): Linear(in_features=768, out_features=1152, bias=False)
    )
    (encoder): Gemma4VisionEncoder(
      (rotary_emb): Gemma4VisionRotaryEmbedding()
      (layers): ModuleList(
        (0-26): 27 x Gemma4VisionEncoderLayer(
          (self_attn): Gemma4VisionAttention(
            (q_proj): Gemma4ClippableLinear(
              (linear): Linear(in_features=1152, out_features=1152, bias=False)
            )
            (k_proj): Gemma4ClippableLinear(
              (linear): Linear(in_features=1152, out_features=1152, bias=False)
            )
            (v_proj): Gemma4ClippableLinear(
              (linear): Linear(in_features=1152, out_features=1152, bias=False)
            )
            (o_proj): Gemma4ClippableLinear(
              (linear): Linear(in_features=1152, out_features=1152, bias=False)
            )
            (q_norm): Gemma4RMSNorm()
            (k_norm): Gemma4RMSNorm()
            (v_norm): Gemma4RMSNorm()
          )
          (mlp): Gemma4VisionMLP(
            (gate_proj): Gemma4ClippableLinear(
              (linear): Linear(in_features=1152, out_features=4304, bias=False)
            )
            (up_proj): Gemma4ClippableLinear(
              (linear): Linear(in_features=1152, out_features=4304, bias=False)
            )
            (down_proj): Gemma4ClippableLinear(
              (linear): Linear(in_features=4304, out_features=1152, bias=False)
            )
            (act_fn): GELUTanh()
          )
          (input_layernorm): Gemma4RMSNorm()
          (post_attention_layernorm): Gemma4RMSNorm()
          (pre_feedforward_layernorm): Gemma4RMSNorm()
          (post_feedforward_layernorm): Gemma4RMSNorm()
        )
      )
    )
    (pooler): Gemma4VisionPooler()
  )
  (language_model): Gemma4TextModel(
    (embed_tokens): Gemma4TextScaledWordEmbedding(262144, 5376, padding_idx=0)
    (layers): ModuleList(
      (0-4): 5 x Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=8192, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (v_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (o_proj): Linear(in_features=8192, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (5): Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=16384, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=2048, bias=False)
          (o_proj): Linear(in_features=16384, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (6-10): 5 x Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=8192, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (v_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (o_proj): Linear(in_features=8192, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (11): Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=16384, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=2048, bias=False)
          (o_proj): Linear(in_features=16384, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (12-16): 5 x Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=8192, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (v_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (o_proj): Linear(in_features=8192, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (17): Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=16384, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=2048, bias=False)
          (o_proj): Linear(in_features=16384, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (18-22): 5 x Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=8192, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (v_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (o_proj): Linear(in_features=8192, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (23): Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=16384, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=2048, bias=False)
          (o_proj): Linear(in_features=16384, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (24-28): 5 x Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=8192, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (v_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (o_proj): Linear(in_features=8192, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (29): Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=16384, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=2048, bias=False)
          (o_proj): Linear(in_features=16384, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (30-34): 5 x Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=8192, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (v_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (o_proj): Linear(in_features=8192, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (35): Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=16384, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=2048, bias=False)
          (o_proj): Linear(in_features=16384, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (36-40): 5 x Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=8192, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (v_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (o_proj): Linear(in_features=8192, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (41): Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=16384, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=2048, bias=False)
          (o_proj): Linear(in_features=16384, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (42-46): 5 x Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=8192, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (v_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (o_proj): Linear(in_features=8192, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (47): Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=16384, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=2048, bias=False)
          (o_proj): Linear(in_features=16384, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (48-52): 5 x Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=8192, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (v_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (o_proj): Linear(in_features=8192, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (53): Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=16384, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=2048, bias=False)
          (o_proj): Linear(in_features=16384, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (54-58): 5 x Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=8192, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (v_proj): Linear(in_features=5376, out_features=4096, bias=False)
          (o_proj): Linear(in_features=8192, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
      (59): Gemma4TextDecoderLayer(
        (self_attn): Gemma4TextAttention(
          (q_proj): Linear(in_features=5376, out_features=16384, bias=False)
          (q_norm): Gemma4RMSNorm()
          (k_norm): Gemma4RMSNorm()
          (v_norm): Gemma4RMSNorm()
          (k_proj): Linear(in_features=5376, out_features=2048, bias=False)
          (o_proj): Linear(in_features=16384, out_features=5376, bias=False)
        )
        (mlp): Gemma4TextMLP(
          (gate_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (up_proj): Linear(in_features=5376, out_features=21504, bias=False)
          (down_proj): Linear(in_features=21504, out_features=5376, bias=False)
          (act_fn): GELUTanh()
        )
        (input_layernorm): Gemma4RMSNorm()
        (post_attention_layernorm): Gemma4RMSNorm()
        (pre_feedforward_layernorm): Gemma4RMSNorm()
        (post_feedforward_layernorm): Gemma4RMSNorm()
      )
    )
    (norm): Gemma4RMSNorm()
    (rotary_emb): Gemma4TextRotaryEmbedding()
  )
  (embed_vision): Gemma4MultimodalEmbedder(
    (embedding_projection): Linear(in_features=1152, out_features=5376, bias=False)
    (embedding_pre_projection_norm): Gemma4RMSNorm()
  )
)
```

# 权重统计

- **权重文件**: 2 个 `safetensors` 文件
- **文件总大小**: 58.25 GB
- **权重张量数**: 1,188
- **参数总量**: 31,273,088,876
- **张量累计大小**: 58.25 GB
- **压缩**: 1188 → 329 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `model.embed_vision.embedding_projection.weight` | `[5376, 1152]` | `torch.bfloat16` | 11.81 MB | model-00001-of-00002.safetensors |
| `model.language_model.embed_tokens.weight` | `[262144, 5376]` | `torch.bfloat16` | 2.62 GB | model-00001-of-00002.safetensors |
| `model.language_model.layers.0-58.self_attn.v_proj.weight` (×50 layers) | `[4096, 5376]` | `torch.bfloat16` | 2.05 GB | model-00001-of-00002.safetensors |
| `model.language_model.layers.0-59.input_layernorm.weight` (×60 layers) | `[5376]` | `torch.bfloat16` | 630.00 KB | Multi Files |
| `model.language_model.layers.0-59.layer_scalar` (×60 layers) | `[1]` | `torch.bfloat16` | 120.00 B | Multi Files |
| `model.language_model.layers.0-59.mlp.down_proj.weight` (×60 layers) | `[5376, 21504]` | `torch.bfloat16` | 12.92 GB | Multi Files |
| `model.language_model.layers.0-59.mlp.gate_proj.weight` (×60 layers) | `[21504, 5376]` | `torch.bfloat16` | 12.92 GB | Multi Files |
| `model.language_model.layers.0-59.mlp.up_proj.weight` (×60 layers) | `[21504, 5376]` | `torch.bfloat16` | 12.92 GB | Multi Files |
| `model.language_model.layers.0-59.post_attention_layernorm.weight` (×60 layers) | `[5376]` | `torch.bfloat16` | 630.00 KB | Multi Files |
| `model.language_model.layers.0-59.post_feedforward_layernorm.weight` (×60 layers) | `[5376]` | `torch.bfloat16` | 630.00 KB | Multi Files |
| `model.language_model.layers.0-59.pre_feedforward_layernorm.weight` (×60 layers) | `[5376]` | `torch.bfloat16` | 630.00 KB | Multi Files |
| `model.language_model.layers.0.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.0.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.0.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.0.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.0.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.1.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.1.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.1.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.1.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.1.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.2.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.2.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.2.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.2.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.2.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.3.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.3.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.3.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.3.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.3.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.4.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.4.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.4.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.4.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.4.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.5.self_attn.k_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.5.self_attn.k_proj.weight` | `[2048, 5376]` | `torch.bfloat16` | 21.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.5.self_attn.o_proj.weight` | `[5376, 16384]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.5.self_attn.q_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.5.self_attn.q_proj.weight` | `[16384, 5376]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.6.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.6.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.6.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.6.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.6.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.7.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.7.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.7.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.7.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.7.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.8.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.8.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.8.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.8.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.8.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.9.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.9.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.9.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.9.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.9.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.10.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.10.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.10.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.10.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.10.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.11.self_attn.k_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.11.self_attn.k_proj.weight` | `[2048, 5376]` | `torch.bfloat16` | 21.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.11.self_attn.o_proj.weight` | `[5376, 16384]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.11.self_attn.q_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.11.self_attn.q_proj.weight` | `[16384, 5376]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.12.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.12.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.12.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.12.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.12.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.13.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.13.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.13.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.13.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.13.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.14.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.14.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.14.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.14.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.14.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.15.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.15.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.15.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.15.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.15.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.16.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.16.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.16.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.16.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.16.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.17.self_attn.k_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.17.self_attn.k_proj.weight` | `[2048, 5376]` | `torch.bfloat16` | 21.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.17.self_attn.o_proj.weight` | `[5376, 16384]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.17.self_attn.q_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.17.self_attn.q_proj.weight` | `[16384, 5376]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.18.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.18.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.18.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.18.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.18.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.19.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.19.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.19.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.19.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.19.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.20.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.20.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.20.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.20.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.20.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.21.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.21.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.21.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.21.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.21.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.22.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.22.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.22.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.22.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.22.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.23.self_attn.k_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.23.self_attn.k_proj.weight` | `[2048, 5376]` | `torch.bfloat16` | 21.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.23.self_attn.o_proj.weight` | `[5376, 16384]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.23.self_attn.q_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.23.self_attn.q_proj.weight` | `[16384, 5376]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.24.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.24.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.24.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.24.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.24.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.25.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.25.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.25.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.25.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.25.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.26.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.26.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.26.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.26.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.26.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.27.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.27.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.27.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.27.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.27.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.28.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.28.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.28.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.28.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.28.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.29.self_attn.k_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.29.self_attn.k_proj.weight` | `[2048, 5376]` | `torch.bfloat16` | 21.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.29.self_attn.o_proj.weight` | `[5376, 16384]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.29.self_attn.q_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.29.self_attn.q_proj.weight` | `[16384, 5376]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.30.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.30.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.30.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.30.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.30.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.31.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.31.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.31.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.31.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.31.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.32.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.32.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.32.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.32.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.32.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.33.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.33.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.33.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.33.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.33.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.34.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.34.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.34.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.34.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.34.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.35.self_attn.k_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.35.self_attn.k_proj.weight` | `[2048, 5376]` | `torch.bfloat16` | 21.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.35.self_attn.o_proj.weight` | `[5376, 16384]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.35.self_attn.q_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.35.self_attn.q_proj.weight` | `[16384, 5376]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.36.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.36.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.36.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.36.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.36.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.37.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.37.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.37.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.37.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.37.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.38.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.38.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.38.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.38.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.38.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.39.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.39.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.39.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.39.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.39.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.40.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.40.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.40.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.40.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.40.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.41.self_attn.k_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.41.self_attn.k_proj.weight` | `[2048, 5376]` | `torch.bfloat16` | 21.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.41.self_attn.o_proj.weight` | `[5376, 16384]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.41.self_attn.q_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.41.self_attn.q_proj.weight` | `[16384, 5376]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.42.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.42.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.42.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.42.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.42.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.43.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.43.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.43.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.43.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.43.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.44.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.44.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.44.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.44.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.44.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.45.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.45.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.45.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.45.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.45.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.46.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.46.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.46.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.46.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.46.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.47.self_attn.k_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.47.self_attn.k_proj.weight` | `[2048, 5376]` | `torch.bfloat16` | 21.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.47.self_attn.o_proj.weight` | `[5376, 16384]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.47.self_attn.q_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.47.self_attn.q_proj.weight` | `[16384, 5376]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.48.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.48.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.48.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.48.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.48.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.49.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.49.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.49.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.49.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.49.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.50.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.50.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.50.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.50.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.50.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.51.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.51.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.51.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.51.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.51.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.52.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.52.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.52.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.52.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.52.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.53.self_attn.k_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.53.self_attn.k_proj.weight` | `[2048, 5376]` | `torch.bfloat16` | 21.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.53.self_attn.o_proj.weight` | `[5376, 16384]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.53.self_attn.q_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.53.self_attn.q_proj.weight` | `[16384, 5376]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.54.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.54.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.54.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.54.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.54.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.55.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.55.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.55.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.55.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.55.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.56.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.56.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.56.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.56.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.56.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.57.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.57.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.57.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.57.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.57.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.58.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.58.self_attn.k_proj.weight` | `[4096, 5376]` | `torch.bfloat16` | 42.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.58.self_attn.o_proj.weight` | `[5376, 8192]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.58.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-00002.safetensors |
| `model.language_model.layers.58.self_attn.q_proj.weight` | `[8192, 5376]` | `torch.bfloat16` | 84.00 MB | model-00001-of-00002.safetensors |
| `model.language_model.layers.59.self_attn.k_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.59.self_attn.k_proj.weight` | `[2048, 5376]` | `torch.bfloat16` | 21.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.59.self_attn.o_proj.weight` | `[5376, 16384]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.layers.59.self_attn.q_norm.weight` | `[512]` | `torch.bfloat16` | 1.00 KB | model-00002-of-00002.safetensors |
| `model.language_model.layers.59.self_attn.q_proj.weight` | `[16384, 5376]` | `torch.bfloat16` | 168.00 MB | model-00002-of-00002.safetensors |
| `model.language_model.norm.weight` | `[5376]` | `torch.bfloat16` | 10.50 KB | model-00001-of-00002.safetensors |
| `model.vision_tower.encoder.layers.0-26.input_layernorm.weight` (×27 layers) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00001-of-00002.safetensors |
| `model.vision_tower.encoder.layers.0-26.mlp.down_proj.linear.weight` (×27 layers) | `[1152, 4304]` | `torch.bfloat16` | 255.34 MB | model-00001-of-00002.safetensors |
| `model.vision_tower.encoder.layers.0-26.mlp.gate_proj.linear.weight` (×27 layers) | `[4304, 1152]` | `torch.bfloat16` | 255.34 MB | model-00001-of-00002.safetensors |
| `model.vision_tower.encoder.layers.0-26.mlp.up_proj.linear.weight` (×27 layers) | `[4304, 1152]` | `torch.bfloat16` | 255.34 MB | model-00001-of-00002.safetensors |
| `model.vision_tower.encoder.layers.0-26.post_attention_layernorm.weight` (×27 layers) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00001-of-00002.safetensors |
| `model.vision_tower.encoder.layers.0-26.post_feedforward_layernorm.weight` (×27 layers) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00001-of-00002.safetensors |
| `model.vision_tower.encoder.layers.0-26.pre_feedforward_layernorm.weight` (×27 layers) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00001-of-00002.safetensors |
| `model.vision_tower.encoder.layers.0-26.self_attn.k_norm.weight` (×27 layers) | `[72]` | `torch.bfloat16` | 3.80 KB | model-00001-of-00002.safetensors |
| `model.vision_tower.encoder.layers.0-26.self_attn.k_proj.linear.weight` (×27 layers) | `[1152, 1152]` | `torch.bfloat16` | 68.34 MB | model-00001-of-00002.safetensors |
| `model.vision_tower.encoder.layers.0-26.self_attn.o_proj.linear.weight` (×27 layers) | `[1152, 1152]` | `torch.bfloat16` | 68.34 MB | model-00001-of-00002.safetensors |
| `model.vision_tower.encoder.layers.0-26.self_attn.q_norm.weight` (×27 layers) | `[72]` | `torch.bfloat16` | 3.80 KB | model-00001-of-00002.safetensors |
| `model.vision_tower.encoder.layers.0-26.self_attn.q_proj.linear.weight` (×27 layers) | `[1152, 1152]` | `torch.bfloat16` | 68.34 MB | model-00001-of-00002.safetensors |
| `model.vision_tower.encoder.layers.0-26.self_attn.v_proj.linear.weight` (×27 layers) | `[1152, 1152]` | `torch.bfloat16` | 68.34 MB | model-00001-of-00002.safetensors |
| `model.vision_tower.patch_embedder.input_proj.weight` | `[1152, 768]` | `torch.bfloat16` | 1.69 MB | model-00001-of-00002.safetensors |
| `model.vision_tower.patch_embedder.position_embedding_table` | `[2, 10240, 1152]` | `torch.bfloat16` | 45.00 MB | model-00001-of-00002.safetensors |
| `model.vision_tower.std_bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00002.safetensors |
| `model.vision_tower.std_scale` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00002.safetensors |

</details>

