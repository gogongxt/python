# 模型信息报告

- **模型路径**: `/nfs/volume-1615-2/models/Qwen3-Omni-30B-A3B-Instruct`

# 模型配置

- **模型类型**: `Qwen3OmniMoeConfig`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: N/A
- **层数**: N/A
- **注意力头数**: N/A
- **词表大小**: N/A
- **中间层大小**: N/A

<details><summary>完整配置</summary>

```
Qwen3OmniMoeConfig {
  "architectures": [
    "Qwen3OmniMoeForConditionalGeneration"
  ],
  "assistant_token_id": 77091,
  "code2wav_config": {
    "attention_bias": false,
    "attention_dropout": 0.0,
    "codebook_dim": 512,
    "codebook_size": 2048,
    "decoder_dim": 1536,
    "hidden_act": "silu",
    "hidden_size": 1024,
    "initializer_range": 0.02,
    "intermediate_size": 3072,
    "layer_scale_initial_scale": 0.01,
    "max_position_embeddings": 8000,
    "model_type": "",
    "num_attention_heads": 16,
    "num_hidden_layers": 8,
    "num_key_value_heads": 16,
    "num_quantizers": 16,
    "num_semantic_quantizers": 1,
    "rms_norm_eps": 1e-05,
    "rope_parameters": {
      "rope_theta": 10000,
      "rope_type": "default"
    },
    "semantic_codebook_size": 4096,
    "sliding_window": 72,
    "upsample_rates": [
      8,
      5,
      4,
      3
    ],
    "upsampling_ratios": [
      2,
      2
    ],
    "vector_quantization_hidden_dimension": 512
  },
  "dtype": "bfloat16",
  "enable_audio_output": true,
  "im_end_token_id": 151645,
  "im_start_token_id": 151644,
  "initializer_range": 0.02,
  "model_type": "qwen3_omni_moe",
  "system_token_id": 8948,
  "talker_config": {
    "accept_hidden_layer": 24,
    "audio_end_token_id": 151670,
    "audio_start_token_id": 151669,
    "audio_token_id": 151675,
    "code_predictor_config": {
      "_name_or_path": "",
      "add_cross_attention": false,
      "architectures": null,
      "attention_bias": false,
      "attention_dropout": 0,
      "bos_token_id": null,
      "chunk_size_feed_forward": 0,
      "cross_attention_hidden_size": null,
      "decoder_start_token_id": null,
      "dtype": null,
      "eos_token_id": null,
      "finetuning_task": null,
      "head_dim": 128,
      "hidden_act": "silu",
      "hidden_size": 1024,
      "id2label": {
        "0": "LABEL_0",
        "1": "LABEL_1"
      },
      "initializer_range": 0.02,
      "intermediate_size": 3072,
      "is_decoder": false,
      "is_encoder_decoder": false,
      "label2id": {
        "LABEL_0": 0,
        "LABEL_1": 1
      },
      "layer_types": [
        "full_attention",
        "full_attention",
        "full_attention",
        "full_attention",
        "full_attention"
      ],
      "max_position_embeddings": 32768,
      "max_window_layers": 28,
      "model_type": "qwen3_omni_moe_talker_code_predictor",
      "num_attention_heads": 16,
      "num_code_groups": 16,
      "num_hidden_layers": 5,
      "num_key_value_heads": 8,
      "output_attentions": false,
      "output_hidden_states": false,
      "pad_token_id": null,
      "prefix": null,
      "problem_type": null,
      "pruned_heads": {},
      "return_dict": true,
      "rms_norm_eps": 1e-06,
      "rope_parameters": {
        "rope_theta": 1000000,
        "rope_type": "default"
      },
      "sep_token_id": null,
      "sliding_window": null,
      "task_specific_params": null,
      "tf_legacy_loss": false,
      "tie_encoder_decoder": false,
      "tie_word_embeddings": false,
      "tokenizer_class": null,
      "torchscript": false,
      "use_bfloat16": false,
      "use_cache": true,
      "use_sliding_window": false,
      "vocab_size": 2048
    },
    "codec_bos_id": 2149,
    "codec_eos_token_id": 2150,
    "codec_nothink_id": 2155,
    "codec_pad_id": 2148,
    "codec_think_bos_id": 2156,
    "codec_think_eos_id": 2157,
    "image_token_id": 151655,
    "initializer_range": 0.02,
    "model_type": "",
    "num_code_groups": 16,
    "output_router_logits": false,
    "position_id_per_seconds": 13,
    "seconds_per_chunk": 2,
    "spatial_merge_size": 2,
    "speaker_id": {
      "aiden": 2303,
      "chelsie": 2301,
      "ethan": 2302
    },
    "text_config": {
      "_name_or_path": "",
      "architectures": null,
      "attention_bias": false,
      "attention_dropout": 0,
      "bos_token_id": null,
      "chunk_size_feed_forward": 0,
      "decoder_sparse_step": 1,
      "dtype": null,
      "eos_token_id": null,
      "head_dim": 128,
      "hidden_act": "silu",
      "hidden_size": 1024,
      "id2label": {
        "0": "LABEL_0",
        "1": "LABEL_1"
      },
      "initializer_range": 0.02,
      "intermediate_size": 2048,
      "is_encoder_decoder": false,
      "label2id": {
        "LABEL_0": 0,
        "LABEL_1": 1
      },
      "max_position_embeddings": 65536,
      "mlp_only_layers": [],
      "model_type": "qwen3_omni_moe_talker_text",
      "moe_intermediate_size": 384,
      "norm_topk_prob": true,
      "num_attention_heads": 16,
      "num_experts_per_tok": 6,
      "num_hidden_layers": 20,
      "num_key_value_heads": 2,
      "num_local_experts": 128,
      "output_attentions": false,
      "output_hidden_states": false,
      "output_router_logits": false,
      "pad_token_id": null,
      "problem_type": null,
      "return_dict": true,
      "rms_norm_eps": 1e-06,
      "rope_parameters": {
        "interleaved": true,
        "mrope_section": [
          24,
          20,
          20
        ],
        "rope_theta": 1000000,
        "rope_type": "default",
        "type": "default"
      },
      "router_aux_loss_coef": 0.001,
      "shared_expert_intermediate_size": 768,
      "sliding_window": null,
      "tie_word_embeddings": false,
      "use_cache": true,
      "use_sliding_window": false,
      "vocab_size": 3072
    },
    "thinker_hidden_size": 2048,
    "tie_word_embeddings": false,
    "video_token_id": 151656,
    "vision_start_token_id": 151652
  },
  "thinker_config": {
    "audio_config": {
      "_name_or_path": "",
      "activation_dropout": 0,
      "activation_function": "gelu",
      "add_cross_attention": false,
      "architectures": null,
      "attention_dropout": 0,
      "bos_token_id": null,
      "chunk_size_feed_forward": 0,
      "conv_chunksize": 500,
      "cross_attention_hidden_size": null,
      "d_model": 1280,
      "decoder_start_token_id": null,
      "downsample_hidden_size": 480,
      "dropout": 0,
      "dtype": null,
      "encoder_attention_heads": 20,
      "encoder_ffn_dim": 5120,
      "encoder_layers": 32,
      "eos_token_id": null,
      "finetuning_task": null,
      "id2label": {
        "0": "LABEL_0",
        "1": "LABEL_1"
      },
      "initializer_range": 0.02,
      "is_decoder": false,
      "is_encoder_decoder": false,
      "label2id": {
        "LABEL_0": 0,
        "LABEL_1": 1
      },
      "max_source_positions": 1500,
      "model_type": "qwen3_omni_moe_audio_encoder",
      "n_window": 50,
      "n_window_infer": 800,
      "num_mel_bins": 128,
      "output_attentions": false,
      "output_dim": 2048,
      "output_hidden_states": false,
      "pad_token_id": null,
      "prefix": null,
      "problem_type": null,
      "pruned_heads": {},
      "return_dict": true,
      "scale_embedding": false,
      "sep_token_id": null,
      "task_specific_params": null,
      "tf_legacy_loss": false,
      "tie_encoder_decoder": false,
      "tie_word_embeddings": true,
      "tokenizer_class": null,
      "torchscript": false,
      "use_bfloat16": false
    },
    "audio_end_token_id": 151670,
    "audio_start_token_id": 151669,
    "audio_token_id": 151675,
    "dtype": "bfloat16",
    "image_token_id": 151655,
    "initializer_range": 0.02,
    "model_type": "qwen3_omni_moe_thinker",
    "position_id_per_seconds": 13,
    "seconds_per_chunk": 2,
    "text_config": {
      "_name_or_path": "",
      "add_cross_attention": false,
      "architectures": null,
      "attention_bias": false,
      "attention_dropout": 0.0,
      "bos_token_id": null,
      "chunk_size_feed_forward": 0,
      "cross_attention_hidden_size": null,
      "decoder_sparse_step": 1,
      "decoder_start_token_id": null,
      "dtype": null,
      "eos_token_id": null,
      "finetuning_task": null,
      "head_dim": 128,
      "hidden_act": "silu",
      "hidden_size": 2048,
      "id2label": {
        "0": "LABEL_0",
        "1": "LABEL_1"
      },
      "initializer_range": 0.02,
      "intermediate_size": 768,
      "is_decoder": false,
      "is_encoder_decoder": false,
      "label2id": {
        "LABEL_0": 0,
        "LABEL_1": 1
      },
      "max_position_embeddings": 65536,
      "mlp_only_layers": [],
      "model_type": "qwen3_omni_moe_text",
      "moe_intermediate_size": 768,
      "norm_topk_prob": true,
      "num_attention_heads": 32,
      "num_experts": 128,
      "num_experts_per_tok": 8,
      "num_hidden_layers": 48,
      "num_key_value_heads": 4,
      "output_attentions": false,
      "output_hidden_states": false,
      "output_router_logits": false,
      "pad_token_id": null,
      "prefix": null,
      "problem_type": null,
      "pruned_heads": {},
      "return_dict": true,
      "rms_norm_eps": 1e-06,
      "rope_parameters": {
        "interleaved": true,
        "mrope_interleaved": true,
        "mrope_section": [
          24,
          20,
          20
        ],
        "rope_theta": 1000000,
        "rope_type": "default",
        "type": "default"
      },
      "router_aux_loss_coef": 0.001,
      "sep_token_id": null,
      "shared_expert_intermediate_size": 0,
      "sliding_window": null,
      "task_specific_params": null,
      "tf_legacy_loss": false,
      "tie_encoder_decoder": false,
      "tie_word_embeddings": false,
      "tokenizer_class": null,
      "torchscript": false,
      "use_bfloat16": false,
      "use_cache": true,
      "use_qk_norm": true,
      "use_sliding_window": false,
      "vocab_size": 152064
    },
    "tie_word_embeddings": false,
    "user_token_id": 872,
    "video_token_id": 151656,
    "vision_config": {
      "_name_or_path": "",
      "add_cross_attention": false,
      "apply_vit_abs_pos_embed": true,
      "architectures": null,
      "bos_token_id": null,
      "chunk_size_feed_forward": 0,
      "cross_attention_hidden_size": null,
      "decoder_start_token_id": null,
      "deepstack_visual_indexes": [
        8,
        16,
        24
      ],
      "depth": 27,
      "dtype": null,
      "eos_token_id": null,
      "finetuning_task": null,
      "hidden_act": "gelu_pytorch_tanh",
      "hidden_size": 1152,
      "id2label": {
        "0": "LABEL_0",
        "1": "LABEL_1"
      },
      "image_size": 768,
      "in_channels": 3,
      "in_chans": 3,
      "initializer_range": 0.02,
      "intermediate_size": 4304,
      "is_decoder": false,
      "is_encoder_decoder": false,
      "label2id": {
        "LABEL_0": 0,
        "LABEL_1": 1
      },
      "model_type": "qwen3_omni_moe_vision_encoder",
      "num_heads": 16,
      "num_position_embeddings": 2304,
      "out_hidden_size": 2048,
      "output_attentions": false,
      "output_hidden_states": false,
      "pad_token_id": null,
      "patch_size": 16,
      "prefix": null,
      "problem_type": null,
      "pruned_heads": {},
      "return_dict": true,
      "sep_token_id": null,
      "spatial_merge_size": 2,
      "spatial_patch_size": 16,
      "task_specific_params": null,
      "temporal_patch_size": 2,
      "tf_legacy_loss": false,
      "tie_encoder_decoder": false,
      "tie_word_embeddings": true,
      "tokenizer_class": null,
      "tokens_per_second": 2,
      "torchscript": false,
      "use_bfloat16": false
    },
    "vision_end_token_id": 151653,
    "vision_start_token_id": 151652
  },
  "transformers_version": "5.7.0",
  "tts_bos_token_id": 151672,
  "tts_eos_token_id": 151673,
  "tts_pad_token_id": 151671,
  "user_token_id": 872
}

```

</details>

# 模型结构

**模型类**: `Qwen3OmniMoeForConditionalGeneration`

```
Qwen3OmniMoeForConditionalGeneration(
  (thinker): Qwen3OmniMoeThinkerForConditionalGeneration(
    (audio_tower): Qwen3OmniMoeAudioEncoder(
      (positional_embedding): SinusoidsPositionEmbedding()
      (layers): ModuleList(
        (0-31): 32 x Qwen3OmniMoeAudioEncoderLayer(
          (self_attn): Qwen3OmniMoeAudioAttention(
            (k_proj): Linear(in_features=1280, out_features=1280, bias=True)
            (v_proj): Linear(in_features=1280, out_features=1280, bias=True)
            (q_proj): Linear(in_features=1280, out_features=1280, bias=True)
            (out_proj): Linear(in_features=1280, out_features=1280, bias=True)
          )
          (self_attn_layer_norm): LayerNorm((1280,), eps=1e-05, elementwise_affine=True)
          (activation_fn): GELUActivation()
          (fc1): Linear(in_features=1280, out_features=5120, bias=True)
          (fc2): Linear(in_features=5120, out_features=1280, bias=True)
          (final_layer_norm): LayerNorm((1280,), eps=1e-05, elementwise_affine=True)
        )
      )
      (ln_post): LayerNorm((1280,), eps=1e-05, elementwise_affine=True)
      (conv2d1): Conv2d(1, 480, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
      (conv2d2): Conv2d(480, 480, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
      (conv2d3): Conv2d(480, 480, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1))
      (conv_out): Linear(in_features=7680, out_features=1280, bias=False)
      (proj1): Linear(in_features=1280, out_features=1280, bias=True)
      (act): GELUActivation()
      (proj2): Linear(in_features=1280, out_features=2048, bias=True)
    )
    (visual): Qwen3OmniMoeVisionEncoder(
      (merger_list): ModuleList(
        (0-2): 3 x Qwen3OmniMoeVisionPatchMerger(
          (ln_q): LayerNorm((4608,), eps=1e-06, elementwise_affine=True)
          (mlp): ModuleList(
            (0): Linear(in_features=4608, out_features=4608, bias=True)
            (1): GELU(approximate='none')
            (2): Linear(in_features=4608, out_features=2048, bias=True)
          )
        )
      )
      (patch_embed): Qwen3OmniMoeVisionPatchEmbed(
        (proj): Conv3d(3, 1152, kernel_size=(2, 16, 16), stride=(2, 16, 16))
      )
      (pos_embed): Embedding(2304, 1152)
      (rotary_pos_emb): Qwen3OmniMoeVisionRotaryEmbedding()
      (blocks): ModuleList(
        (0-26): 27 x Qwen3OmniMoeVisionBlock(
          (norm1): LayerNorm((1152,), eps=1e-06, elementwise_affine=True)
          (norm2): LayerNorm((1152,), eps=1e-06, elementwise_affine=True)
          (attn): Qwen3OmniMoeVisionAttention(
            (qkv): Linear(in_features=1152, out_features=3456, bias=True)
            (proj): Linear(in_features=1152, out_features=1152, bias=True)
          )
          (mlp): Qwen3OmniMoeVisionMLP(
            (linear_fc1): Linear(in_features=1152, out_features=4304, bias=True)
            (linear_fc2): Linear(in_features=4304, out_features=1152, bias=True)
            (act_fn): GELUTanh()
          )
        )
      )
      (merger): Qwen3OmniMoeVisionPatchMerger(
        (ln_q): LayerNorm((1152,), eps=1e-06, elementwise_affine=True)
        (mlp): ModuleList(
          (0): Linear(in_features=4608, out_features=4608, bias=True)
          (1): GELU(approximate='none')
          (2): Linear(in_features=4608, out_features=2048, bias=True)
        )
      )
    )
    (model): Qwen3OmniMoeThinkerTextModel(
      (embed_tokens): Embedding(152064, 2048)
      (layers): ModuleList(
        (0-47): 48 x Qwen3OmniMoeThinkerTextDecoderLayer(
          (self_attn): Qwen3OmniMoeThinkerTextAttention(
            (q_proj): Linear(in_features=2048, out_features=4096, bias=False)
            (k_proj): Linear(in_features=2048, out_features=512, bias=False)
            (v_proj): Linear(in_features=2048, out_features=512, bias=False)
            (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
            (q_norm): Qwen3OmniMoeThinkerTextRMSNorm((128,), eps=1e-06)
            (k_norm): Qwen3OmniMoeThinkerTextRMSNorm((128,), eps=1e-06)
          )
          (mlp): Qwen3OmniMoeThinkerTextSparseMoeBlock(
            (experts): Qwen3OmniMoeThinkerTextExperts(
              (act_fn): SiLUActivation()
            )
            (gate): Qwen3OmniMoeThinkerTextTopKRouter()
          )
          (input_layernorm): Qwen3OmniMoeThinkerTextRMSNorm((2048,), eps=1e-06)
          (post_attention_layernorm): Qwen3OmniMoeThinkerTextRMSNorm((2048,), eps=1e-06)
        )
      )
      (norm): Qwen3OmniMoeTextRMSNorm((2048,), eps=1e-06)
      (rotary_emb): Qwen3OmniMoeThinkerTextRotaryEmbedding()
    )
    (lm_head): Linear(in_features=2048, out_features=152064, bias=False)
  )
  (talker): Qwen3OmniMoeTalkerForConditionalGeneration(
    (model): Qwen3OmniMoeTalkerModel(
      (layers): ModuleList(
        (0-19): 20 x Qwen3OmniMoeTalkerDecoderLayer(
          (self_attn): Qwen3OmniMoeThinkerTextAttention(
            (q_proj): Linear(in_features=1024, out_features=2048, bias=False)
            (k_proj): Linear(in_features=1024, out_features=256, bias=False)
            (v_proj): Linear(in_features=1024, out_features=256, bias=False)
            (o_proj): Linear(in_features=2048, out_features=1024, bias=False)
            (q_norm): Qwen3OmniMoeThinkerTextRMSNorm((128,), eps=1e-06)
            (k_norm): Qwen3OmniMoeThinkerTextRMSNorm((128,), eps=1e-06)
          )
          (mlp): Qwen3OmniMoeTalkerTextSparseMoeBlock(
            (gate): Qwen3OmniMoeTalkerTextTopKRouter()
            (experts): Qwen3OmniMoeTalkerTextExperts(
              (act_fn): SiLUActivation()
            )
            (shared_expert): Qwen3OmniMoeTalkerTextMLP(
              (gate_proj): Linear(in_features=1024, out_features=768, bias=False)
              (up_proj): Linear(in_features=1024, out_features=768, bias=False)
              (down_proj): Linear(in_features=768, out_features=1024, bias=False)
              (act_fn): SiLUActivation()
            )
            (shared_expert_gate): Linear(in_features=1024, out_features=1, bias=False)
          )
          (input_layernorm): Qwen3OmniMoeThinkerTextRMSNorm((1024,), eps=1e-06)
          (post_attention_layernorm): Qwen3OmniMoeThinkerTextRMSNorm((1024,), eps=1e-06)
        )
      )
      (norm): Qwen3OmniMoeTextRMSNorm((1024,), eps=1e-06)
      (rotary_emb): Qwen3OmniMoeTalkerRotaryEmbedding()
      (codec_embedding): Embedding(3072, 1024)
    )
    (text_projection): Qwen3OmniMoeTalkerResizeMLP(
      (linear_fc1): Linear(in_features=2048, out_features=2048, bias=True)
      (linear_fc2): Linear(in_features=2048, out_features=1024, bias=True)
      (act_fn): SiLUActivation()
    )
    (hidden_projection): Qwen3OmniMoeTalkerResizeMLP(
      (linear_fc1): Linear(in_features=2048, out_features=2048, bias=True)
      (linear_fc2): Linear(in_features=2048, out_features=1024, bias=True)
      (act_fn): SiLUActivation()
    )
    (codec_head): Linear(in_features=1024, out_features=3072, bias=False)
    (code_predictor): Qwen3OmniMoeTalkerCodePredictorModelForConditionalGeneration(
      (model): Qwen3OmniMoeTalkerCodePredictorModel(
        (layers): ModuleList(
          (0-4): 5 x Qwen3OmniMoeTalkerCodePredictorDecoderLayer(
            (self_attn): Qwen3OmniMoeTalkerCodePredictorAttention(
              (q_proj): Linear(in_features=1024, out_features=2048, bias=False)
              (k_proj): Linear(in_features=1024, out_features=1024, bias=False)
              (v_proj): Linear(in_features=1024, out_features=1024, bias=False)
              (o_proj): Linear(in_features=2048, out_features=1024, bias=False)
              (q_norm): Qwen3OmniMoeRMSNorm((128,), eps=1e-06)
              (k_norm): Qwen3OmniMoeRMSNorm((128,), eps=1e-06)
            )
            (mlp): Qwen3OmniMoeMLP(
              (gate_proj): Linear(in_features=1024, out_features=3072, bias=False)
              (up_proj): Linear(in_features=1024, out_features=3072, bias=False)
              (down_proj): Linear(in_features=3072, out_features=1024, bias=False)
              (act_fn): SiLUActivation()
            )
            (input_layernorm): Qwen3OmniMoeRMSNorm((1024,), eps=1e-06)
            (post_attention_layernorm): Qwen3OmniMoeRMSNorm((1024,), eps=1e-06)
          )
        )
        (norm): Qwen3OmniMoeRMSNorm((1024,), eps=1e-06)
        (rotary_emb): Qwen3OmniMoeRotaryEmbedding()
        (codec_embedding): ModuleList(
          (0-14): 15 x Embedding(2048, 1024)
        )
      )
      (lm_head): ModuleList(
        (0-14): 15 x Linear(in_features=1024, out_features=2048, bias=False)
      )
    )
  )
  (code2wav): Qwen3OmniMoeCode2Wav(
    (pre_transformer): Qwen3OmniMoeCode2WavTransformerModel(
      (layers): ModuleList(
        (0-7): 8 x Qwen3OmniMoeCode2WavTransformerLayer(
          (self_attn): Qwen3OmniMoeCode2WavAttention(
            (q_proj): Linear(in_features=1024, out_features=1024, bias=False)
            (k_proj): Linear(in_features=1024, out_features=1024, bias=False)
            (v_proj): Linear(in_features=1024, out_features=1024, bias=False)
            (o_proj): Linear(in_features=1024, out_features=1024, bias=False)
            (q_norm): Identity()
            (k_norm): Identity()
          )
          (mlp): Qwen3OmniMoeCode2WavMlp(
            (gate_proj): Linear(in_features=1024, out_features=3072, bias=False)
            (up_proj): Linear(in_features=1024, out_features=3072, bias=False)
            (down_proj): Linear(in_features=3072, out_features=1024, bias=False)
            (act_fn): SiLUActivation()
          )
          (input_layernorm): Qwen3OmniMoeCode2WavRMSNorm((1024,), eps=1e-05)
          (post_attention_layernorm): Qwen3OmniMoeCode2WavRMSNorm((1024,), eps=1e-05)
          (self_attn_layer_scale): Qwen3OmniMoeCode2WavLayerScale()
          (mlp_layer_scale): Qwen3OmniMoeCode2WavLayerScale()
        )
      )
      (norm): Qwen3OmniMoeRMSNorm((1024,), eps=1e-05)
      (rotary_emb): Qwen3OmniMoeRotaryEmbedding()
    )
    (code_embedding): Embedding(32768, 1024)
    (upsample): ModuleList(
      (0-1): 2 x ModuleList(
        (0): Qwen3OmniMoeCausalTransConvNet(
          (conv): ConvTranspose1d(1024, 1024, kernel_size=(2,), stride=(2,))
        )
        (1): Qwen3OmniMoeConvNeXtBlock(
          (dwconv): Qwen3OmniMoeCausalConvNet(
            (conv): Conv1d(1024, 1024, kernel_size=(7,), stride=(1,), groups=1024)
          )
          (norm): LayerNorm((1024,), eps=1e-06, elementwise_affine=True)
          (pwconv1): Linear(in_features=1024, out_features=4096, bias=True)
          (act): GELU(approximate='none')
          (pwconv2): Linear(in_features=4096, out_features=1024, bias=True)
        )
      )
    )
    (decoder): ModuleList(
      (0): Qwen3OmniMoeCausalConvNet(
        (conv): Conv1d(1024, 1536, kernel_size=(7,), stride=(1,))
      )
      (1): Qwen3OmniMoeCode2WavDecoderBlock(
        (block): ModuleList(
          (0): SnakeBeta()
          (1): Qwen3OmniMoeCausalTransConvNet(
            (conv): ConvTranspose1d(1536, 768, kernel_size=(16,), stride=(8,))
          )
          (2): Qwen3OmniMoeCode2WavDecoderResidualUnit(
            (act1): SnakeBeta()
            (conv1): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(768, 768, kernel_size=(7,), stride=(1,))
            )
            (act2): SnakeBeta()
            (conv2): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(768, 768, kernel_size=(1,), stride=(1,))
            )
          )
          (3): Qwen3OmniMoeCode2WavDecoderResidualUnit(
            (act1): SnakeBeta()
            (conv1): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(768, 768, kernel_size=(7,), stride=(1,), dilation=(3,))
            )
            (act2): SnakeBeta()
            (conv2): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(768, 768, kernel_size=(1,), stride=(1,))
            )
          )
          (4): Qwen3OmniMoeCode2WavDecoderResidualUnit(
            (act1): SnakeBeta()
            (conv1): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(768, 768, kernel_size=(7,), stride=(1,), dilation=(9,))
            )
            (act2): SnakeBeta()
            (conv2): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(768, 768, kernel_size=(1,), stride=(1,))
            )
          )
        )
      )
      (2): Qwen3OmniMoeCode2WavDecoderBlock(
        (block): ModuleList(
          (0): SnakeBeta()
          (1): Qwen3OmniMoeCausalTransConvNet(
            (conv): ConvTranspose1d(768, 384, kernel_size=(10,), stride=(5,))
          )
          (2): Qwen3OmniMoeCode2WavDecoderResidualUnit(
            (act1): SnakeBeta()
            (conv1): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(384, 384, kernel_size=(7,), stride=(1,))
            )
            (act2): SnakeBeta()
            (conv2): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(384, 384, kernel_size=(1,), stride=(1,))
            )
          )
          (3): Qwen3OmniMoeCode2WavDecoderResidualUnit(
            (act1): SnakeBeta()
            (conv1): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(384, 384, kernel_size=(7,), stride=(1,), dilation=(3,))
            )
            (act2): SnakeBeta()
            (conv2): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(384, 384, kernel_size=(1,), stride=(1,))
            )
          )
          (4): Qwen3OmniMoeCode2WavDecoderResidualUnit(
            (act1): SnakeBeta()
            (conv1): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(384, 384, kernel_size=(7,), stride=(1,), dilation=(9,))
            )
            (act2): SnakeBeta()
            (conv2): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(384, 384, kernel_size=(1,), stride=(1,))
            )
          )
        )
      )
      (3): Qwen3OmniMoeCode2WavDecoderBlock(
        (block): ModuleList(
          (0): SnakeBeta()
          (1): Qwen3OmniMoeCausalTransConvNet(
            (conv): ConvTranspose1d(384, 192, kernel_size=(8,), stride=(4,))
          )
          (2): Qwen3OmniMoeCode2WavDecoderResidualUnit(
            (act1): SnakeBeta()
            (conv1): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(192, 192, kernel_size=(7,), stride=(1,))
            )
            (act2): SnakeBeta()
            (conv2): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(192, 192, kernel_size=(1,), stride=(1,))
            )
          )
          (3): Qwen3OmniMoeCode2WavDecoderResidualUnit(
            (act1): SnakeBeta()
            (conv1): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(192, 192, kernel_size=(7,), stride=(1,), dilation=(3,))
            )
            (act2): SnakeBeta()
            (conv2): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(192, 192, kernel_size=(1,), stride=(1,))
            )
          )
          (4): Qwen3OmniMoeCode2WavDecoderResidualUnit(
            (act1): SnakeBeta()
            (conv1): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(192, 192, kernel_size=(7,), stride=(1,), dilation=(9,))
            )
            (act2): SnakeBeta()
            (conv2): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(192, 192, kernel_size=(1,), stride=(1,))
            )
          )
        )
      )
      (4): Qwen3OmniMoeCode2WavDecoderBlock(
        (block): ModuleList(
          (0): SnakeBeta()
          (1): Qwen3OmniMoeCausalTransConvNet(
            (conv): ConvTranspose1d(192, 96, kernel_size=(6,), stride=(3,))
          )
          (2): Qwen3OmniMoeCode2WavDecoderResidualUnit(
            (act1): SnakeBeta()
            (conv1): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(96, 96, kernel_size=(7,), stride=(1,))
            )
            (act2): SnakeBeta()
            (conv2): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(96, 96, kernel_size=(1,), stride=(1,))
            )
          )
          (3): Qwen3OmniMoeCode2WavDecoderResidualUnit(
            (act1): SnakeBeta()
            (conv1): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(96, 96, kernel_size=(7,), stride=(1,), dilation=(3,))
            )
            (act2): SnakeBeta()
            (conv2): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(96, 96, kernel_size=(1,), stride=(1,))
            )
          )
          (4): Qwen3OmniMoeCode2WavDecoderResidualUnit(
            (act1): SnakeBeta()
            (conv1): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(96, 96, kernel_size=(7,), stride=(1,), dilation=(9,))
            )
            (act2): SnakeBeta()
            (conv2): Qwen3OmniMoeCausalConvNet(
              (conv): Conv1d(96, 96, kernel_size=(1,), stride=(1,))
            )
          )
        )
      )
      (5): SnakeBeta()
      (6): Qwen3OmniMoeCausalConvNet(
        (conv): Conv1d(96, 1, kernel_size=(7,), stride=(1,))
      )
    )
  )
)
```

# 权重统计

- **权重文件**: 15 个 `safetensors` 文件
- **文件总大小**: 65.68 GB
- **权重张量数**: 28,010
- **参数总量**: 35,259,818,545
- **张量累计大小**: 65.68 GB
- **压缩**: 28010 → 617 行 (合并相同 shape/dtype 的 experts 和 layers)

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `code2wav.code_embedding.weight` | `[32768, 1024]` | `torch.bfloat16` | 64.00 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.0.conv.bias` | `[1536]` | `torch.bfloat16` | 3.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.0.conv.weight` | `[1536, 1024, 7]` | `torch.bfloat16` | 21.00 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.0.alpha` | `[1536]` | `torch.bfloat16` | 3.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.0.beta` | `[1536]` | `torch.bfloat16` | 3.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.1.conv.bias` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.1.conv.weight` | `[1536, 768, 16]` | `torch.bfloat16` | 36.00 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.2.act1.alpha` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.2.act1.beta` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.2.act2.alpha` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.2.act2.beta` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.2.conv1.conv.bias` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.2.conv1.conv.weight` | `[768, 768, 7]` | `torch.bfloat16` | 7.88 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.2.conv2.conv.bias` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.2.conv2.conv.weight` | `[768, 768, 1]` | `torch.bfloat16` | 1.12 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.3.act1.alpha` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.3.act1.beta` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.3.act2.alpha` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.3.act2.beta` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.3.conv1.conv.bias` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.3.conv1.conv.weight` | `[768, 768, 7]` | `torch.bfloat16` | 7.88 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.3.conv2.conv.bias` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.3.conv2.conv.weight` | `[768, 768, 1]` | `torch.bfloat16` | 1.12 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.4.act1.alpha` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.4.act1.beta` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.4.act2.alpha` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.4.act2.beta` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.4.conv1.conv.bias` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.4.conv1.conv.weight` | `[768, 768, 7]` | `torch.bfloat16` | 7.88 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.4.conv2.conv.bias` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.1.block.4.conv2.conv.weight` | `[768, 768, 1]` | `torch.bfloat16` | 1.12 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.0.alpha` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.0.beta` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.1.conv.bias` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.1.conv.weight` | `[768, 384, 10]` | `torch.bfloat16` | 5.62 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.2.act1.alpha` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.2.act1.beta` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.2.act2.alpha` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.2.act2.beta` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.2.conv1.conv.bias` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.2.conv1.conv.weight` | `[384, 384, 7]` | `torch.bfloat16` | 1.97 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.2.conv2.conv.bias` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.2.conv2.conv.weight` | `[384, 384, 1]` | `torch.bfloat16` | 288.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.3.act1.alpha` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.3.act1.beta` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.3.act2.alpha` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.3.act2.beta` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.3.conv1.conv.bias` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.3.conv1.conv.weight` | `[384, 384, 7]` | `torch.bfloat16` | 1.97 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.3.conv2.conv.bias` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.3.conv2.conv.weight` | `[384, 384, 1]` | `torch.bfloat16` | 288.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.4.act1.alpha` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.4.act1.beta` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.4.act2.alpha` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.4.act2.beta` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.4.conv1.conv.bias` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.4.conv1.conv.weight` | `[384, 384, 7]` | `torch.bfloat16` | 1.97 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.4.conv2.conv.bias` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.2.block.4.conv2.conv.weight` | `[384, 384, 1]` | `torch.bfloat16` | 288.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.0.alpha` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.0.beta` | `[384]` | `torch.bfloat16` | 768.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.1.conv.bias` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.1.conv.weight` | `[384, 192, 8]` | `torch.bfloat16` | 1.12 MB | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.2.act1.alpha` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.2.act1.beta` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.2.act2.alpha` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.2.act2.beta` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.2.conv1.conv.bias` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.2.conv1.conv.weight` | `[192, 192, 7]` | `torch.bfloat16` | 504.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.2.conv2.conv.bias` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.2.conv2.conv.weight` | `[192, 192, 1]` | `torch.bfloat16` | 72.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.3.act1.alpha` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.3.act1.beta` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.3.act2.alpha` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.3.act2.beta` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.3.conv1.conv.bias` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.3.conv1.conv.weight` | `[192, 192, 7]` | `torch.bfloat16` | 504.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.3.conv2.conv.bias` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.3.conv2.conv.weight` | `[192, 192, 1]` | `torch.bfloat16` | 72.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.4.act1.alpha` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.4.act1.beta` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.4.act2.alpha` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.4.act2.beta` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.4.conv1.conv.bias` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.4.conv1.conv.weight` | `[192, 192, 7]` | `torch.bfloat16` | 504.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.4.conv2.conv.bias` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.3.block.4.conv2.conv.weight` | `[192, 192, 1]` | `torch.bfloat16` | 72.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.0.alpha` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.0.beta` | `[192]` | `torch.bfloat16` | 384.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.1.conv.bias` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.1.conv.weight` | `[192, 96, 6]` | `torch.bfloat16` | 216.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.2.act1.alpha` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.2.act1.beta` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.2.act2.alpha` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.2.act2.beta` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.2.conv1.conv.bias` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.2.conv1.conv.weight` | `[96, 96, 7]` | `torch.bfloat16` | 126.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.2.conv2.conv.bias` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.2.conv2.conv.weight` | `[96, 96, 1]` | `torch.bfloat16` | 18.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.3.act1.alpha` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.3.act1.beta` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.3.act2.alpha` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.3.act2.beta` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.3.conv1.conv.bias` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.3.conv1.conv.weight` | `[96, 96, 7]` | `torch.bfloat16` | 126.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.3.conv2.conv.bias` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.3.conv2.conv.weight` | `[96, 96, 1]` | `torch.bfloat16` | 18.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.4.act1.alpha` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.4.act1.beta` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.4.act2.alpha` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.4.act2.beta` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.4.conv1.conv.bias` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.4.conv1.conv.weight` | `[96, 96, 7]` | `torch.bfloat16` | 126.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.4.conv2.conv.bias` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.4.block.4.conv2.conv.weight` | `[96, 96, 1]` | `torch.bfloat16` | 18.00 KB | model-00015-of-00015.safetensors |
| `code2wav.decoder.5.alpha` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.5.beta` | `[96]` | `torch.bfloat16` | 192.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.6.conv.bias` | `[1]` | `torch.bfloat16` | 2.00 B | model-00015-of-00015.safetensors |
| `code2wav.decoder.6.conv.weight` | `[1, 96, 7]` | `torch.bfloat16` | 1.31 KB | model-00015-of-00015.safetensors |
| `code2wav.pre_transformer.layers.0-7.input_layernorm.weight` (×8 layers) | `[1024]` | `torch.bfloat16` | 16.00 KB | model-00015-of-00015.safetensors |
| `code2wav.pre_transformer.layers.0-7.mlp.down_proj.weight` (×8 layers) | `[1024, 3072]` | `torch.bfloat16` | 48.00 MB | model-00015-of-00015.safetensors |
| `code2wav.pre_transformer.layers.0-7.mlp.gate_proj.weight` (×8 layers) | `[3072, 1024]` | `torch.bfloat16` | 48.00 MB | model-00015-of-00015.safetensors |
| `code2wav.pre_transformer.layers.0-7.mlp.up_proj.weight` (×8 layers) | `[3072, 1024]` | `torch.bfloat16` | 48.00 MB | model-00015-of-00015.safetensors |
| `code2wav.pre_transformer.layers.0-7.mlp_layer_scale.scale` (×8 layers) | `[1024]` | `torch.bfloat16` | 16.00 KB | model-00015-of-00015.safetensors |
| `code2wav.pre_transformer.layers.0-7.post_attention_layernorm.weight` (×8 layers) | `[1024]` | `torch.bfloat16` | 16.00 KB | model-00015-of-00015.safetensors |
| `code2wav.pre_transformer.layers.0-7.self_attn.k_proj.weight` (×8 layers) | `[1024, 1024]` | `torch.bfloat16` | 16.00 MB | model-00015-of-00015.safetensors |
| `code2wav.pre_transformer.layers.0-7.self_attn.o_proj.weight` (×8 layers) | `[1024, 1024]` | `torch.bfloat16` | 16.00 MB | model-00015-of-00015.safetensors |
| `code2wav.pre_transformer.layers.0-7.self_attn.q_proj.weight` (×8 layers) | `[1024, 1024]` | `torch.bfloat16` | 16.00 MB | model-00015-of-00015.safetensors |
| `code2wav.pre_transformer.layers.0-7.self_attn.v_proj.weight` (×8 layers) | `[1024, 1024]` | `torch.bfloat16` | 16.00 MB | model-00015-of-00015.safetensors |
| `code2wav.pre_transformer.layers.0-7.self_attn_layer_scale.scale` (×8 layers) | `[1024]` | `torch.bfloat16` | 16.00 KB | model-00015-of-00015.safetensors |
| `code2wav.pre_transformer.norm.weight` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.0.0.conv.bias` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.0.0.conv.weight` | `[1024, 1024, 2]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `code2wav.upsample.0.1.dwconv.conv.bias` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.0.1.dwconv.conv.weight` | `[1024, 1, 7]` | `torch.bfloat16` | 14.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.0.1.gamma` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.0.1.norm.bias` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.0.1.norm.weight` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.0.1.pwconv1.bias` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.0.1.pwconv1.weight` | `[4096, 1024]` | `torch.bfloat16` | 8.00 MB | model-00015-of-00015.safetensors |
| `code2wav.upsample.0.1.pwconv2.bias` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.0.1.pwconv2.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00015-of-00015.safetensors |
| `code2wav.upsample.1.0.conv.bias` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.1.0.conv.weight` | `[1024, 1024, 2]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `code2wav.upsample.1.1.dwconv.conv.bias` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.1.1.dwconv.conv.weight` | `[1024, 1, 7]` | `torch.bfloat16` | 14.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.1.1.gamma` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.1.1.norm.bias` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.1.1.norm.weight` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.1.1.pwconv1.bias` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.1.1.pwconv1.weight` | `[4096, 1024]` | `torch.bfloat16` | 8.00 MB | model-00015-of-00015.safetensors |
| `code2wav.upsample.1.1.pwconv2.bias` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00015-of-00015.safetensors |
| `code2wav.upsample.1.1.pwconv2.weight` | `[1024, 4096]` | `torch.bfloat16` | 8.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.0.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.1.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.2.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.3.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.4.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.5.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.6.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.7.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.8.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.9.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.10.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.11.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.12.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.13.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.lm_head.14.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.0.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00014-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.1.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.2.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.3.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.4.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.5.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.6.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.7.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.8.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.9.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.10.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.11.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.12.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.13.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.codec_embedding.14.weight` | `[2048, 1024]` | `torch.bfloat16` | 4.00 MB | model-00015-of-00015.safetensors |
| `talker.code_predictor.model.layers.0-4.input_layernorm.weight` (×5 layers) | `[1024]` | `torch.bfloat16` | 10.00 KB | model-00014-of-00015.safetensors |
| `talker.code_predictor.model.layers.0-4.mlp.down_proj.weight` (×5 layers) | `[1024, 3072]` | `torch.bfloat16` | 30.00 MB | model-00014-of-00015.safetensors |
| `talker.code_predictor.model.layers.0-4.mlp.gate_proj.weight` (×5 layers) | `[3072, 1024]` | `torch.bfloat16` | 30.00 MB | model-00014-of-00015.safetensors |
| `talker.code_predictor.model.layers.0-4.mlp.up_proj.weight` (×5 layers) | `[3072, 1024]` | `torch.bfloat16` | 30.00 MB | model-00014-of-00015.safetensors |
| `talker.code_predictor.model.layers.0-4.post_attention_layernorm.weight` (×5 layers) | `[1024]` | `torch.bfloat16` | 10.00 KB | model-00014-of-00015.safetensors |
| `talker.code_predictor.model.layers.0-4.self_attn.k_norm.weight` (×5 layers) | `[128]` | `torch.bfloat16` | 1.25 KB | model-00014-of-00015.safetensors |
| `talker.code_predictor.model.layers.0-4.self_attn.k_proj.weight` (×5 layers) | `[1024, 1024]` | `torch.bfloat16` | 10.00 MB | model-00014-of-00015.safetensors |
| `talker.code_predictor.model.layers.0-4.self_attn.o_proj.weight` (×5 layers) | `[1024, 2048]` | `torch.bfloat16` | 20.00 MB | model-00014-of-00015.safetensors |
| `talker.code_predictor.model.layers.0-4.self_attn.q_norm.weight` (×5 layers) | `[128]` | `torch.bfloat16` | 1.25 KB | model-00014-of-00015.safetensors |
| `talker.code_predictor.model.layers.0-4.self_attn.q_proj.weight` (×5 layers) | `[2048, 1024]` | `torch.bfloat16` | 20.00 MB | model-00014-of-00015.safetensors |
| `talker.code_predictor.model.layers.0-4.self_attn.v_proj.weight` (×5 layers) | `[1024, 1024]` | `torch.bfloat16` | 10.00 MB | model-00014-of-00015.safetensors |
| `talker.code_predictor.model.norm.weight` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00014-of-00015.safetensors |
| `talker.codec_head.weight` | `[3072, 1024]` | `torch.bfloat16` | 6.00 MB | model-00014-of-00015.safetensors |
| `talker.hidden_projection.linear_fc1.bias` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00014-of-00015.safetensors |
| `talker.hidden_projection.linear_fc1.weight` | `[2048, 2048]` | `torch.bfloat16` | 8.00 MB | model-00014-of-00015.safetensors |
| `talker.hidden_projection.linear_fc2.bias` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00014-of-00015.safetensors |
| `talker.hidden_projection.linear_fc2.weight` | `[1024, 2048]` | `torch.bfloat16` | 4.00 MB | model-00014-of-00015.safetensors |
| `talker.model.codec_embedding.weight` | `[3072, 1024]` | `torch.bfloat16` | 6.00 MB | model-00014-of-00015.safetensors |
| `talker.model.layers.0-19.input_layernorm.weight` (×20 layers) | `[1024]` | `torch.bfloat16` | 40.00 KB | Multi Files |
| `talker.model.layers.0-19.mlp.experts.0-127.down_proj.weight` (×20 layers, ×128 experts) | `[1024, 384]` | `torch.bfloat16` | 1.88 GB | Multi Files |
| `talker.model.layers.0-19.mlp.experts.0-127.gate_proj.weight` (×20 layers, ×128 experts) | `[384, 1024]` | `torch.bfloat16` | 1.88 GB | Multi Files |
| `talker.model.layers.0-19.mlp.experts.0-127.up_proj.weight` (×20 layers, ×128 experts) | `[384, 1024]` | `torch.bfloat16` | 1.88 GB | Multi Files |
| `talker.model.layers.0-19.mlp.gate.weight` (×20 layers) | `[128, 1024]` | `torch.bfloat16` | 5.00 MB | Multi Files |
| `talker.model.layers.0-19.mlp.shared_expert.down_proj.weight` (×20 layers) | `[1024, 768]` | `torch.bfloat16` | 30.00 MB | Multi Files |
| `talker.model.layers.0-19.mlp.shared_expert.gate_proj.weight` (×20 layers) | `[768, 1024]` | `torch.bfloat16` | 30.00 MB | Multi Files |
| `talker.model.layers.0-19.mlp.shared_expert.up_proj.weight` (×20 layers) | `[768, 1024]` | `torch.bfloat16` | 30.00 MB | Multi Files |
| `talker.model.layers.0-19.mlp.shared_expert_gate.weight` (×20 layers) | `[1, 1024]` | `torch.bfloat16` | 40.00 KB | Multi Files |
| `talker.model.layers.0-19.post_attention_layernorm.weight` (×20 layers) | `[1024]` | `torch.bfloat16` | 40.00 KB | Multi Files |
| `talker.model.layers.0-19.self_attn.k_norm.weight` (×20 layers) | `[128]` | `torch.bfloat16` | 5.00 KB | Multi Files |
| `talker.model.layers.0-19.self_attn.k_proj.weight` (×20 layers) | `[256, 1024]` | `torch.bfloat16` | 10.00 MB | Multi Files |
| `talker.model.layers.0-19.self_attn.o_proj.weight` (×20 layers) | `[1024, 2048]` | `torch.bfloat16` | 80.00 MB | Multi Files |
| `talker.model.layers.0-19.self_attn.q_norm.weight` (×20 layers) | `[128]` | `torch.bfloat16` | 5.00 KB | Multi Files |
| `talker.model.layers.0-19.self_attn.q_proj.weight` (×20 layers) | `[2048, 1024]` | `torch.bfloat16` | 80.00 MB | Multi Files |
| `talker.model.layers.0-19.self_attn.v_proj.weight` (×20 layers) | `[256, 1024]` | `torch.bfloat16` | 10.00 MB | Multi Files |
| `talker.model.norm.weight` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00014-of-00015.safetensors |
| `talker.text_projection.linear_fc1.bias` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00014-of-00015.safetensors |
| `talker.text_projection.linear_fc1.weight` | `[2048, 2048]` | `torch.bfloat16` | 8.00 MB | model-00014-of-00015.safetensors |
| `talker.text_projection.linear_fc2.bias` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00014-of-00015.safetensors |
| `talker.text_projection.linear_fc2.weight` | `[1024, 2048]` | `torch.bfloat16` | 4.00 MB | model-00014-of-00015.safetensors |
| `thinker.audio_tower.conv2d1.bias` | `[480]` | `torch.bfloat16` | 960.00 B | model-00001-of-00015.safetensors |
| `thinker.audio_tower.conv2d1.weight` | `[480, 1, 3, 3]` | `torch.bfloat16` | 8.44 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.conv2d2.bias` | `[480]` | `torch.bfloat16` | 960.00 B | model-00001-of-00015.safetensors |
| `thinker.audio_tower.conv2d2.weight` | `[480, 480, 3, 3]` | `torch.bfloat16` | 3.96 MB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.conv2d3.bias` | `[480]` | `torch.bfloat16` | 960.00 B | model-00001-of-00015.safetensors |
| `thinker.audio_tower.conv2d3.weight` | `[480, 480, 3, 3]` | `torch.bfloat16` | 3.96 MB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.conv_out.weight` | `[1280, 7680]` | `torch.bfloat16` | 18.75 MB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.fc1.bias` (×32 layers) | `[5120]` | `torch.bfloat16` | 320.00 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.fc1.weight` (×32 layers) | `[5120, 1280]` | `torch.bfloat16` | 400.00 MB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.fc2.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.fc2.weight` (×32 layers) | `[1280, 5120]` | `torch.bfloat16` | 400.00 MB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.final_layer_norm.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.final_layer_norm.weight` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.self_attn.k_proj.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.self_attn.k_proj.weight` (×32 layers) | `[1280, 1280]` | `torch.bfloat16` | 100.00 MB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.self_attn.out_proj.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.self_attn.out_proj.weight` (×32 layers) | `[1280, 1280]` | `torch.bfloat16` | 100.00 MB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.self_attn.q_proj.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.self_attn.q_proj.weight` (×32 layers) | `[1280, 1280]` | `torch.bfloat16` | 100.00 MB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.self_attn.v_proj.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.self_attn.v_proj.weight` (×32 layers) | `[1280, 1280]` | `torch.bfloat16` | 100.00 MB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.self_attn_layer_norm.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.layers.0-31.self_attn_layer_norm.weight` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.ln_post.bias` | `[1280]` | `torch.bfloat16` | 2.50 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.ln_post.weight` | `[1280]` | `torch.bfloat16` | 2.50 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.proj1.bias` | `[1280]` | `torch.bfloat16` | 2.50 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.proj1.weight` | `[1280, 1280]` | `torch.bfloat16` | 3.12 MB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.proj2.bias` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00001-of-00015.safetensors |
| `thinker.audio_tower.proj2.weight` | `[2048, 1280]` | `torch.bfloat16` | 5.00 MB | model-00001-of-00015.safetensors |
| `thinker.lm_head.weight` | `[152064, 2048]` | `torch.bfloat16` | 594.00 MB | model-00013-of-00015.safetensors |
| `thinker.model.embed_tokens.weight` | `[152064, 2048]` | `torch.bfloat16` | 594.00 MB | model-00001-of-00015.safetensors |
| `thinker.model.layers.0-47.input_layernorm.weight` (×48 layers) | `[2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `thinker.model.layers.0-47.mlp.experts.0-127.down_proj.weight` (×48 layers, ×128 experts) | `[2048, 768]` | `torch.bfloat16` | 18.00 GB | Multi Files |
| `thinker.model.layers.0-47.mlp.experts.0-127.gate_proj.weight` (×48 layers, ×128 experts) | `[768, 2048]` | `torch.bfloat16` | 18.00 GB | Multi Files |
| `thinker.model.layers.0-47.mlp.experts.0-127.up_proj.weight` (×48 layers, ×128 experts) | `[768, 2048]` | `torch.bfloat16` | 18.00 GB | Multi Files |
| `thinker.model.layers.0-47.mlp.gate.weight` (×48 layers) | `[128, 2048]` | `torch.bfloat16` | 24.00 MB | Multi Files |
| `thinker.model.layers.0-47.post_attention_layernorm.weight` (×48 layers) | `[2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `thinker.model.layers.0-47.self_attn.k_norm.weight` (×48 layers) | `[128]` | `torch.bfloat16` | 12.00 KB | Multi Files |
| `thinker.model.layers.0-47.self_attn.k_proj.weight` (×48 layers) | `[512, 2048]` | `torch.bfloat16` | 96.00 MB | Multi Files |
| `thinker.model.layers.0-47.self_attn.o_proj.weight` (×48 layers) | `[2048, 4096]` | `torch.bfloat16` | 768.00 MB | Multi Files |
| `thinker.model.layers.0-47.self_attn.q_norm.weight` (×48 layers) | `[128]` | `torch.bfloat16` | 12.00 KB | Multi Files |
| `thinker.model.layers.0-47.self_attn.q_proj.weight` (×48 layers) | `[4096, 2048]` | `torch.bfloat16` | 768.00 MB | Multi Files |
| `thinker.model.layers.0-47.self_attn.v_proj.weight` (×48 layers) | `[512, 2048]` | `torch.bfloat16` | 96.00 MB | Multi Files |
| `thinker.model.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00013-of-00015.safetensors |
| `thinker.visual.blocks.0.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.0.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.0.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.0.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.0.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.0.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.0.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.0.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.0.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.0.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.0.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.0.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.1.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.1.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.1.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.1.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.1.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.1.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.1.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.1.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.1.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.1.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.1.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.1.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.2.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.2.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.2.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.2.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.2.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.2.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.2.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.2.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.2.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.2.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.2.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.2.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.3.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.3.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.3.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.3.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.3.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.3.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.3.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.3.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.3.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.3.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.3.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.3.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.4.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.4.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.4.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.4.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.4.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.4.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.4.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.4.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.4.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.4.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.4.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.4.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.5.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.5.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.5.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.5.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.5.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.5.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.5.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.5.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.5.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.5.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.5.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.5.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.6.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.6.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.6.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.6.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.6.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.6.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.6.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.6.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.6.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.6.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.6.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.6.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.7.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.7.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.7.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.7.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.7.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.7.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.7.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.7.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.7.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.7.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.7.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.7.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.8.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.8.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.8.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.8.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.8.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.8.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.8.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.8.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.8.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.8.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.8.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.8.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.9.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.9.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.9.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.9.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.9.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.9.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.9.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.9.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.9.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.9.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.9.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.9.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.10.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.10.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.10.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.10.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.10.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.10.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.10.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.10.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.10.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.10.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.10.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.10.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.11.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.11.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.11.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.11.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.11.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.11.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.11.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.11.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.11.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.11.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.11.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.11.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.12.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.12.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.12.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.12.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.12.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.12.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.12.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.12.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.12.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.12.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.12.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.12.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.13.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.13.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.13.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.13.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.13.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.13.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.13.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.13.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.13.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.13.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.13.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.13.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.14.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.14.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.14.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.14.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.14.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.14.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.14.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.14.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.14.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.14.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.14.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.14.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.15.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.15.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.15.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.15.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.15.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.15.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.15.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.15.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.15.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.15.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.15.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.15.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.16.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.16.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.16.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.16.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.16.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.16.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.16.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.16.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.16.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.16.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.16.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.16.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.17.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.17.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.17.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.17.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.17.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.17.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.17.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.17.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.17.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.17.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.17.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.17.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.18.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.18.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.18.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.18.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.18.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.18.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.18.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.18.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.18.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.18.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.18.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.18.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.19.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.19.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.19.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.19.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.19.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.19.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.19.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.19.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.19.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.19.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.19.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.19.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.20.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.20.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.20.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.20.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.20.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.20.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.20.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.20.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.20.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.20.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.20.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.20.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.21.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.21.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.21.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.21.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.21.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.21.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.21.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.21.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.21.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.21.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.21.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.21.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.22.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.22.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.22.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.22.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.22.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.22.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.22.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.22.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.22.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.22.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.22.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.22.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.23.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.23.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.23.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.23.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.23.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.23.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.23.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.23.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.23.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.23.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.23.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.23.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.24.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.24.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.24.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.24.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.24.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.24.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.24.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.24.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.24.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.24.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.24.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.24.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.25.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.25.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.25.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.25.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.25.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.25.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.25.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.25.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.25.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.25.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.25.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.25.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.26.attn.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.26.attn.proj.weight` | `[1152, 1152]` | `torch.bfloat16` | 2.53 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.26.attn.qkv.bias` | `[3456]` | `torch.bfloat16` | 6.75 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.26.attn.qkv.weight` | `[3456, 1152]` | `torch.bfloat16` | 7.59 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.26.mlp.linear_fc1.bias` | `[4304]` | `torch.bfloat16` | 8.41 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.26.mlp.linear_fc1.weight` | `[4304, 1152]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.26.mlp.linear_fc2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.26.mlp.linear_fc2.weight` | `[1152, 4304]` | `torch.bfloat16` | 9.46 MB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.26.norm1.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.26.norm1.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.26.norm2.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.blocks.26.norm2.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger.ln_q.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger.ln_q.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger.mlp.0.bias` | `[4608]` | `torch.bfloat16` | 9.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger.mlp.0.weight` | `[4608, 4608]` | `torch.bfloat16` | 40.50 MB | model-00001-of-00015.safetensors |
| `thinker.visual.merger.mlp.2.bias` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger.mlp.2.weight` | `[2048, 4608]` | `torch.bfloat16` | 18.00 MB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.0.ln_q.bias` | `[4608]` | `torch.bfloat16` | 9.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.0.ln_q.weight` | `[4608]` | `torch.bfloat16` | 9.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.0.mlp.0.bias` | `[4608]` | `torch.bfloat16` | 9.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.0.mlp.0.weight` | `[4608, 4608]` | `torch.bfloat16` | 40.50 MB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.0.mlp.2.bias` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.0.mlp.2.weight` | `[2048, 4608]` | `torch.bfloat16` | 18.00 MB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.1.ln_q.bias` | `[4608]` | `torch.bfloat16` | 9.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.1.ln_q.weight` | `[4608]` | `torch.bfloat16` | 9.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.1.mlp.0.bias` | `[4608]` | `torch.bfloat16` | 9.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.1.mlp.0.weight` | `[4608, 4608]` | `torch.bfloat16` | 40.50 MB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.1.mlp.2.bias` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.1.mlp.2.weight` | `[2048, 4608]` | `torch.bfloat16` | 18.00 MB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.2.ln_q.bias` | `[4608]` | `torch.bfloat16` | 9.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.2.ln_q.weight` | `[4608]` | `torch.bfloat16` | 9.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.2.mlp.0.bias` | `[4608]` | `torch.bfloat16` | 9.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.2.mlp.0.weight` | `[4608, 4608]` | `torch.bfloat16` | 40.50 MB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.2.mlp.2.bias` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00001-of-00015.safetensors |
| `thinker.visual.merger_list.2.mlp.2.weight` | `[2048, 4608]` | `torch.bfloat16` | 18.00 MB | model-00001-of-00015.safetensors |
| `thinker.visual.patch_embed.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00015.safetensors |
| `thinker.visual.patch_embed.proj.weight` | `[1152, 3, 2, 16, 16]` | `torch.bfloat16` | 3.38 MB | model-00001-of-00015.safetensors |
| `thinker.visual.pos_embed.weight` | `[2304, 1152]` | `torch.bfloat16` | 5.06 MB | model-00001-of-00015.safetensors |

</details>

