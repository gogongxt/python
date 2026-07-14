# 模型信息报告

- **模型路径**: `/nfs/ofs-luban-data/model/XiaomiMiMo/MiMo-V2.5`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-luban-data/model/XiaomiMiMo/MiMo-V2.5/config.json`

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
  "attention_bias": false,
  "attention_chunk_size": 128,
  "attention_dropout": 0.0,
  "attention_value_scale": 0.707,
  "attention_projection_layout": "fused_qkv",
  "add_full_attention_sink_bias": false,
  "add_swa_attention_sink_bias": true,
  "audio_config": {
    "add_post_norm": true,
    "audio_channels": 20,
    "audio_segment_size": 6000,
    "group_size": 4,
    "input_full_attention": true,
    "input_local_attn_heads": 16,
    "input_local_dim": 1024,
    "input_local_head_dim": 64,
    "input_local_hidden_dropout": 0.0,
    "input_local_intermediate_size": 4096,
    "input_local_layers": 6,
    "out_hidden_size": 4096,
    "partial_rotary_factor": 1.0,
    "projection_layers": 2,
    "rope_theta": 640000,
    "speech_vocab_size": "1280",
    "speech_zeroemb_idx": "1024"
  },
  "swa_num_key_value_heads": 8,
  "swa_num_attention_heads": 64,
  "swa_head_dim": 192,
  "swa_v_head_dim": 128,
  "dtype": "bfloat16",
  "eos_token_id": 151645,
  "head_dim": 192,
  "hidden_act": "silu",
  "hidden_size": 4096,
  "hybrid_block_size": null,
  "hybrid_layer_pattern": [
    0,
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
    0,
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
    0,
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
    0,
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
    0
  ],
  "image_token_id": 151655,
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
    1
  ],
  "n_group": 1,
  "n_routed_experts": 256,
  "n_shared_experts": null,
  "norm_topk_prob": true,
  "num_attention_heads": 64,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 48,
  "num_key_value_heads": 4,
  "pad_token_id": 151643,
  "partial_rotary_factor": 0.334,
  "processor_config": {
    "audio_avg_pooler": 2,
    "audio_channels": 20,
    "audio_end_token_id": 151674,
    "audio_fmax": null,
    "audio_fmin": 0,
    "audio_group_size": 4,
    "audio_hop_length": 240,
    "audio_input_id_per_second": 25.0,
    "audio_kernel_size": 3,
    "audio_n_mels": 128,
    "audio_nfft": 960,
    "audio_sampling_rate": 24000,
    "audio_segment_size": 6000,
    "audio_start_token_id": 151673,
    "audio_stride_size": 2,
    "audio_token_id": 151669,
    "audio_window_size": 960,
    "audio_zeroemb_idx": [
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024
    ],
    "fps": 1.0,
    "image_max_pixels": 8388608,
    "image_min_pixels": 8192,
    "image_token_id": 151655,
    "max_frames": 3600,
    "merge_size": 2,
    "min_frames": null,
    "num_frames": null,
    "pad_token_id": 151643,
    "patch_size": 16,
    "rope_type": "rope",
    "temporal_compression_ratio": 1,
    "temporal_patch_size": 2,
    "use_per_grid_t_timestamps": false,
    "use_video_timestamps": true,
    "video_audio_interleave_length": 0.0,
    "video_end_token_id": 151671,
    "video_max_pixels": 8388608,
    "video_min_pixels": 8192,
    "video_process_num_threads": 16,
    "video_start_token_id": 151670,
    "video_token_id": 151656,
    "video_tokens_per_second": 2,
    "video_total_max_pixels": 268435456,
    "vision_end_token_id": 151653,
    "vision_start_token_id": 151652
  },
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "e4m3",
    "quant_method": "fp8",
    "store_dtype": "fp8",
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
      "model.decoder.self_attn.o_proj"
    ],
    "weight_block_size": [
      128,
      128
    ]
  },
  "rope_scaling": {
    "rope_type": "default",
    "type": "default"
  },
  "rope_theta": 10000000,
  "routed_scaling_factor": null,
  "scoring_func": "sigmoid",
  "sliding_window": 128,
  "sliding_window_size": 128,
  "swa_rope_theta": 10000,
  "tie_word_embeddings": false,
  "topk_group": 1,
  "topk_method": "noaux_tc",
  "transformers_version": "4.57.1",
  "use_cache": true,
  "v_head_dim": 128,
  "video_token_id": 151656,
  "vision_config": {
    "depth": 28,
    "fullatt_block_indexes": [
      0,
      9,
      18,
      27
    ],
    "hidden_act": "silu",
    "hidden_size": 1280,
    "in_chans": 3,
    "intermediate_size": 4608,
    "num_heads": 32,
    "num_key_value_heads": 8,
    "num_query_groups": 4,
    "out_hidden_size": 4096,
    "patch_size": 16,
    "spatial_merge_size": 2,
    "spatial_patch_size": 16,
    "temporal_patch_size": 2,
    "tokens_per_second": 2,
    "use_sink": true,
    "visual_token_window_size": 64,
    "vit_window_attn_types": [
      -1,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      1,
      -1,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      1,
      -1,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      1,
      -1
    ],
    "window_size": 128
  },
  "vision_end_token_id": 151653,
  "vision_model_type": "mimovl",
  "vision_start_token_id": 151652,
  "vocab_size": 152576
}
```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `MiMoV2Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 4096
- **层数**: 48
- **注意力头数**: 64
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
  "attention_value_scale": 0.707,
  "audio_config": {
    "add_post_norm": true,
    "audio_channels": 20,
    "audio_segment_size": 6000,
    "group_size": 4,
    "input_full_attention": true,
    "input_local_attn_heads": 16,
    "input_local_dim": 1024,
    "input_local_head_dim": 64,
    "input_local_hidden_dropout": 0.0,
    "input_local_intermediate_size": 4096,
    "input_local_layers": 6,
    "out_hidden_size": 4096,
    "partial_rotary_factor": 1.0,
    "projection_layers": 2,
    "rope_theta": 640000,
    "speech_vocab_size": "1280",
    "speech_zeroemb_idx": "1024"
  },
  "audio_end_token_id": 151674,
  "audio_start_token_id": 151673,
  "audio_token_id": 151669,
  "auto_map": {
    "AutoConfig": "configuration_mimo_v2.MiMoV2Config",
    "AutoModel": "modeling_mimo_v2.MiMoV2Model",
    "AutoModelForCausalLM": "modeling_mimo_v2.MiMoV2ForCausalLM"
  },
  "dtype": "bfloat16",
  "eos_token_id": 151645,
  "head_dim": 192,
  "hidden_act": "silu",
  "hidden_size": 4096,
  "hybrid_block_size": null,
  "hybrid_layer_pattern": [
    0,
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
    0,
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
    0,
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
    0,
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
    0
  ],
  "image_token_id": 151655,
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
    1
  ],
  "n_group": 1,
  "n_routed_experts": 256,
  "n_shared_experts": null,
  "norm_topk_prob": true,
  "num_attention_heads": 64,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 48,
  "num_key_value_heads": 4,
  "pad_token_id": 151643,
  "partial_rotary_factor": 0.334,
  "processor_config": {
    "audio_avg_pooler": 2,
    "audio_channels": 20,
    "audio_end_token_id": 151674,
    "audio_fmax": null,
    "audio_fmin": 0,
    "audio_group_size": 4,
    "audio_hop_length": 240,
    "audio_input_id_per_second": 25.0,
    "audio_kernel_size": 3,
    "audio_n_mels": 128,
    "audio_nfft": 960,
    "audio_sampling_rate": 24000,
    "audio_segment_size": 6000,
    "audio_start_token_id": 151673,
    "audio_stride_size": 2,
    "audio_token_id": 151669,
    "audio_window_size": 960,
    "audio_zeroemb_idx": [
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024,
      1024
    ],
    "fps": 1.0,
    "image_max_pixels": 8388608,
    "image_min_pixels": 8192,
    "image_token_id": 151655,
    "max_frames": 3600,
    "merge_size": 2,
    "min_frames": null,
    "num_frames": null,
    "pad_token_id": 151643,
    "patch_size": 16,
    "rope_type": "rope",
    "temporal_compression_ratio": 1,
    "temporal_patch_size": 2,
    "use_per_grid_t_timestamps": false,
    "use_video_timestamps": true,
    "video_audio_interleave_length": 0.0,
    "video_end_token_id": 151671,
    "video_max_pixels": 8388608,
    "video_min_pixels": 8192,
    "video_process_num_threads": 16,
    "video_start_token_id": 151670,
    "video_token_id": 151656,
    "video_tokens_per_second": 2,
    "video_total_max_pixels": 268435456,
    "vision_end_token_id": 151653,
    "vision_start_token_id": 151652
  },
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
      "model.decoder.self_attn.o_proj"
    ],
    "quant_method": "fp8",
    "store_dtype": "fp8",
    "weight_block_size": [
      128,
      128
    ]
  },
  "rope_parameters": {
    "partial_rotary_factor": 0.334,
    "rope_theta": 10000000,
    "rope_type": "default",
    "type": "default"
  },
  "rope_theta": 10000000,
  "routed_scaling_factor": null,
  "scoring_func": "sigmoid",
  "sliding_window": 128,
  "sliding_window_size": 128,
  "swa_head_dim": 192,
  "swa_num_attention_heads": 64,
  "swa_num_key_value_heads": 8,
  "swa_rope_theta": 10000,
  "swa_v_head_dim": 128,
  "tie_word_embeddings": false,
  "topk_group": 1,
  "topk_method": "noaux_tc",
  "transformers_version": "5.7.0",
  "use_cache": true,
  "v_head_dim": 128,
  "video_token_id": 151656,
  "vision_config": {
    "depth": 28,
    "fullatt_block_indexes": [
      0,
      9,
      18,
      27
    ],
    "hidden_act": "silu",
    "hidden_size": 1280,
    "in_chans": 3,
    "intermediate_size": 4608,
    "num_heads": 32,
    "num_key_value_heads": 8,
    "num_query_groups": 4,
    "out_hidden_size": 4096,
    "patch_size": 16,
    "spatial_merge_size": 2,
    "spatial_patch_size": 16,
    "temporal_patch_size": 2,
    "tokens_per_second": 2,
    "use_sink": true,
    "visual_token_window_size": 64,
    "vit_window_attn_types": [
      -1,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      1,
      -1,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      1,
      -1,
      0,
      0,
      0,
      0,
      1,
      1,
      1,
      1,
      -1
    ],
    "window_size": 128
  },
  "vision_end_token_id": 151653,
  "vision_model_type": "mimovl",
  "vision_start_token_id": 151652,
  "vocab_size": 152576
}

```

</details>

# 模型结构

**模型类**: `MiMoV2Config` (当前 transformers 版本不支持实例化)

# 权重统计

- **权重文件**: 17 个 `safetensors` 文件
- **文件总大小**: 293.40 GB
- **权重张量数**: 73,081
- **参数总量**: 310,775,040,000
- **张量累计大小**: 293.40 GB
- **压缩**: 73081 → 74 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `audio_encoder.input_local_transformer.layers.0-5.input_layernorm.weight` (×6 layers) | `[1024]` | `torch.bfloat16` | 12.00 KB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.input_local_transformer.layers.0-5.mlp.down_proj.weight` (×6 layers) | `[1024, 4096]` | `torch.bfloat16` | 48.00 MB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.input_local_transformer.layers.0-5.mlp.gate_proj.weight` (×6 layers) | `[4096, 1024]` | `torch.bfloat16` | 48.00 MB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.input_local_transformer.layers.0-5.mlp.up_proj.weight` (×6 layers) | `[4096, 1024]` | `torch.bfloat16` | 48.00 MB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.input_local_transformer.layers.0-5.post_attention_layernorm.weight` (×6 layers) | `[1024]` | `torch.bfloat16` | 12.00 KB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.input_local_transformer.layers.0-5.self_attn.k_proj.bias` (×6 layers) | `[1024]` | `torch.bfloat16` | 12.00 KB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.input_local_transformer.layers.0-5.self_attn.k_proj.weight` (×6 layers) | `[1024, 1024]` | `torch.bfloat16` | 12.00 MB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.input_local_transformer.layers.0-5.self_attn.o_proj.weight` (×6 layers) | `[1024, 1024]` | `torch.bfloat16` | 12.00 MB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.input_local_transformer.layers.0-5.self_attn.q_proj.bias` (×6 layers) | `[1024]` | `torch.bfloat16` | 12.00 KB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.input_local_transformer.layers.0-5.self_attn.q_proj.weight` (×6 layers) | `[1024, 1024]` | `torch.bfloat16` | 12.00 MB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.input_local_transformer.layers.0-5.self_attn.v_proj.bias` (×6 layers) | `[1024]` | `torch.bfloat16` | 12.00 KB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.input_local_transformer.layers.0-5.self_attn.v_proj.weight` (×6 layers) | `[1024, 1024]` | `torch.bfloat16` | 12.00 MB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.input_local_transformer.norm.weight` | `[1024]` | `torch.bfloat16` | 2.00 KB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.projection.mlp.0.weight` | `[16384, 4096]` | `torch.bfloat16` | 128.00 MB | model_pp0_ep0_shard1.safetensors |
| `audio_encoder.projection.mlp.2.weight` | `[4096, 16384]` | `torch.bfloat16` | 128.00 MB | model_pp0_ep0_shard1.safetensors |
| `lm_head.weight` | `[152576, 4096]` | `torch.bfloat16` | 1.16 GB | model_pp0_ep0_shard1.safetensors |
| `model.embed_tokens.weight` | `[152576, 4096]` | `torch.bfloat16` | 1.16 GB | model_pp0_ep0_shard1.safetensors |
| `model.layers.0,5,11,17,...,41,47.self_attn.qkv_proj.weight` (×9 layers) | `[13568, 4096]` | `torch.float8_e4m3fn` | 477.00 MB | model_pp0_ep0_shard1.safetensors |
| `model.layers.0,5,11,17,...,41,47.self_attn.qkv_proj.weight_scale_inv` (×9 layers) | `[108, 32]` | `torch.float32` | 121.50 KB | model_pp0_ep0_shard1.safetensors |
| `model.layers.0-47.input_layernorm.weight` (×48 layers) | `[4096]` | `torch.bfloat16` | 384.00 KB | model_pp0_ep0_shard1.safetensors |
| `model.layers.0-47.post_attention_layernorm.weight` (×48 layers) | `[4096]` | `torch.bfloat16` | 384.00 KB | model_pp0_ep0_shard1.safetensors |
| `model.layers.0-47.self_attn.o_proj.weight` (×48 layers) | `[4096, 8192]` | `torch.bfloat16` | 3.00 GB | model_pp0_ep0_shard1.safetensors |
| `model.layers.0.mlp.down_proj.weight` | `[4096, 16384]` | `torch.float8_e4m3fn` | 64.00 MB | model_pp0_ep0_shard1.safetensors |
| `model.layers.0.mlp.down_proj.weight_scale_inv` | `[32, 128]` | `torch.float32` | 16.00 KB | model_pp0_ep0_shard1.safetensors |
| `model.layers.0.mlp.gate_proj.weight` | `[16384, 4096]` | `torch.float8_e4m3fn` | 64.00 MB | model_pp0_ep0_shard1.safetensors |
| `model.layers.0.mlp.gate_proj.weight_scale_inv` | `[128, 32]` | `torch.float32` | 16.00 KB | model_pp0_ep0_shard1.safetensors |
| `model.layers.0.mlp.up_proj.weight` | `[16384, 4096]` | `torch.float8_e4m3fn` | 64.00 MB | model_pp0_ep0_shard1.safetensors |
| `model.layers.0.mlp.up_proj.weight_scale_inv` | `[128, 32]` | `torch.float32` | 16.00 KB | model_pp0_ep0_shard1.safetensors |
| `model.layers.1-4,6-10,12-16,18-22,24-28,30-34,36-40,42-46.self_attn.attention_sink_bias` (×39 layers) | `[64]` | `torch.bfloat16` | 4.88 KB | model_pp0_ep0_shard1.safetensors |
| `model.layers.1-4,6-10,12-16,18-22,24-28,30-34,36-40,42-46.self_attn.qkv_proj.weight` (×39 layers) | `[14848, 4096]` | `torch.float8_e4m3fn` | 2.21 GB | model_pp0_ep0_shard1.safetensors |
| `model.layers.1-4,6-10,12-16,18-22,24-28,30-34,36-40,42-46.self_attn.qkv_proj.weight_scale_inv` (×39 layers) | `[116, 32]` | `torch.float32` | 565.50 KB | model_pp0_ep0_shard1.safetensors |
| `model.layers.1-47.mlp.experts.0-255.down_proj.weight` (×47 layers, ×256 experts) | `[4096, 2048]` | `torch.float8_e4m3fn` | 94.00 GB | Multi Files |
| `model.layers.1-47.mlp.experts.0-255.down_proj.weight_scale_inv` (×47 layers, ×256 experts) | `[32, 16]` | `torch.float32` | 23.50 MB | Multi Files |
| `model.layers.1-47.mlp.experts.0-255.gate_proj.weight` (×47 layers, ×256 experts) | `[2048, 4096]` | `torch.float8_e4m3fn` | 94.00 GB | Multi Files |
| `model.layers.1-47.mlp.experts.0-255.gate_proj.weight_scale_inv` (×47 layers, ×256 experts) | `[16, 32]` | `torch.float32` | 23.50 MB | Multi Files |
| `model.layers.1-47.mlp.experts.0-255.up_proj.weight` (×47 layers, ×256 experts) | `[2048, 4096]` | `torch.float8_e4m3fn` | 94.00 GB | Multi Files |
| `model.layers.1-47.mlp.experts.0-255.up_proj.weight_scale_inv` (×47 layers, ×256 experts) | `[16, 32]` | `torch.float32` | 23.50 MB | Multi Files |
| `model.layers.1-47.mlp.gate.e_score_correction_bias` (×47 layers) | `[256]` | `torch.float32` | 47.00 KB | model_pp0_ep0_shard1.safetensors |
| `model.layers.1-47.mlp.gate.weight` (×47 layers) | `[256, 4096]` | `torch.float32` | 188.00 MB | model_pp0_ep0_shard1.safetensors |
| `model.mtp.layers.0-2.eh_proj.weight` (×3 layers) | `[4096, 8192]` | `torch.bfloat16` | 192.00 MB | model_mtp.safetensors |
| `model.mtp.layers.0-2.enorm.weight` (×3 layers) | `[4096]` | `torch.bfloat16` | 24.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.final_layernorm.weight` (×3 layers) | `[4096]` | `torch.bfloat16` | 24.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.hnorm.weight` (×3 layers) | `[4096]` | `torch.bfloat16` | 24.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.input_layernorm.weight` (×3 layers) | `[4096]` | `torch.bfloat16` | 24.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.mlp.down_proj.weight` (×3 layers) | `[4096, 16384]` | `torch.float8_e4m3fn` | 192.00 MB | model_mtp.safetensors |
| `model.mtp.layers.0-2.mlp.down_proj.weight_scale_inv` (×3 layers) | `[32, 128]` | `torch.float32` | 48.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.mlp.gate_proj.weight` (×3 layers) | `[16384, 4096]` | `torch.float8_e4m3fn` | 192.00 MB | model_mtp.safetensors |
| `model.mtp.layers.0-2.mlp.gate_proj.weight_scale_inv` (×3 layers) | `[128, 32]` | `torch.float32` | 48.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.mlp.up_proj.weight` (×3 layers) | `[16384, 4096]` | `torch.float8_e4m3fn` | 192.00 MB | model_mtp.safetensors |
| `model.mtp.layers.0-2.mlp.up_proj.weight_scale_inv` (×3 layers) | `[128, 32]` | `torch.float32` | 48.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.pre_mlp_layernorm.weight` (×3 layers) | `[4096]` | `torch.bfloat16` | 24.00 KB | model_mtp.safetensors |
| `model.mtp.layers.0-2.self_attn.attention_sink_bias` (×3 layers) | `[64]` | `torch.bfloat16` | 384.00 B | model_mtp.safetensors |
| `model.mtp.layers.0-2.self_attn.o_proj.weight` (×3 layers) | `[4096, 8192]` | `torch.bfloat16` | 192.00 MB | model_mtp.safetensors |
| `model.mtp.layers.0-2.self_attn.qkv_proj.weight` (×3 layers) | `[14848, 4096]` | `torch.float8_e4m3fn` | 174.00 MB | model_mtp.safetensors |
| `model.mtp.layers.0-2.self_attn.qkv_proj.weight_scale_inv` (×3 layers) | `[116, 32]` | `torch.float32` | 43.50 KB | model_mtp.safetensors |
| `model.norm.weight` | `[4096]` | `torch.bfloat16` | 8.00 KB | model_pp0_ep0_shard1.safetensors |
| `speech_embeddings.0-19.weight` (×20 speech_embeddings) | `[1280, 1024]` | `torch.bfloat16` | 50.00 MB | model_pp0_ep0_shard1.safetensors |
| `visual.blocks.0-27.attn.proj.bias` (×28 blocks) | `[1280]` | `torch.bfloat16` | 70.00 KB | model_pp0_ep0_shard1.safetensors |
| `visual.blocks.0-27.attn.proj.weight` (×28 blocks) | `[1280, 2048]` | `torch.bfloat16` | 140.00 MB | model_pp0_ep0_shard1.safetensors |
| `visual.blocks.0-27.attn.qkv.bias` (×28 blocks) | `[3072]` | `torch.bfloat16` | 168.00 KB | model_pp0_ep0_shard1.safetensors |
| `visual.blocks.0-27.attn.qkv.weight` (×28 blocks) | `[3072, 1280]` | `torch.bfloat16` | 210.00 MB | model_pp0_ep0_shard1.safetensors |
| `visual.blocks.0-27.mlp.down_proj.bias` (×28 blocks) | `[1280]` | `torch.bfloat16` | 70.00 KB | model_pp0_ep0_shard1.safetensors |
| `visual.blocks.0-27.mlp.down_proj.weight` (×28 blocks) | `[1280, 4608]` | `torch.bfloat16` | 315.00 MB | model_pp0_ep0_shard1.safetensors |
| `visual.blocks.0-27.mlp.gate_proj.bias` (×28 blocks) | `[4608]` | `torch.bfloat16` | 252.00 KB | model_pp0_ep0_shard1.safetensors |
| `visual.blocks.0-27.mlp.gate_proj.weight` (×28 blocks) | `[4608, 1280]` | `torch.bfloat16` | 315.00 MB | model_pp0_ep0_shard1.safetensors |
| `visual.blocks.0-27.mlp.up_proj.bias` (×28 blocks) | `[4608]` | `torch.bfloat16` | 252.00 KB | model_pp0_ep0_shard1.safetensors |
| `visual.blocks.0-27.mlp.up_proj.weight` (×28 blocks) | `[4608, 1280]` | `torch.bfloat16` | 315.00 MB | model_pp0_ep0_shard1.safetensors |
| `visual.blocks.0-27.norm1.weight` (×28 blocks) | `[1280]` | `torch.bfloat16` | 70.00 KB | model_pp0_ep0_shard1.safetensors |
| `visual.blocks.0-27.norm2.weight` (×28 blocks) | `[1280]` | `torch.bfloat16` | 70.00 KB | model_pp0_ep0_shard1.safetensors |
| `visual.blocks.1-8,10-17,19-26.attn.sinks` (×24 blocks) | `[32]` | `torch.bfloat16` | 1.50 KB | model_pp0_ep0_shard1.safetensors |
| `visual.merger.ln_q.weight` | `[1280]` | `torch.bfloat16` | 2.50 KB | model_pp0_ep0_shard1.safetensors |
| `visual.merger.mlp.0.weight` | `[5120, 5120]` | `torch.bfloat16` | 50.00 MB | model_pp0_ep0_shard1.safetensors |
| `visual.merger.mlp.2.weight` | `[4096, 5120]` | `torch.bfloat16` | 40.00 MB | model_pp0_ep0_shard1.safetensors |
| `visual.patch_embed.proj.weight` | `[1280, 3, 2, 16, 16]` | `torch.bfloat16` | 3.75 MB | model_pp0_ep0_shard1.safetensors |

</details>

