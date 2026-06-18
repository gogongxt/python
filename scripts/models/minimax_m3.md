# 模型信息报告

- **模型路径**: `/nfs/ofs-luban-data/model/MiniMax/MiniMax-M3`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-luban-data/model/MiniMax/MiniMax-M3/config.json`

```json

{
  "architectures": [
    "MiniMaxM3SparseForConditionalGeneration"
  ],
  "auto_map": {
    "AutoConfig": "configuration_minimax_m3_vl.MiniMaxM3VLConfig"
  },
  "model_type": "minimax_m3_vl",
  "text_config": {
    "hidden_size": 6144,
    "intermediate_size": 3072,
    "num_hidden_layers": 60,
    "num_attention_heads": 64,
    "num_key_value_heads": 4,
    "head_dim": 128,
    "vocab_size": 200064,
    "max_position_embeddings": 1048576,
    "rms_norm_eps": 1e-06,
    "use_gemma_norm": true,
    "attention_output_gate": false,
    "rope_theta": 5000000,
    "rotary_dim": 64,
    "partial_rotary_factor": 0.5,
    "hidden_act": "swigluoai",
    "use_qk_norm": true,
    "tie_word_embeddings": false,
    "dense_intermediate_size": 12288,
    "shared_intermediate_size": 3072,
    "num_local_experts": 128,
    "num_experts_per_tok": 4,
    "n_shared_experts": 1,
    "scoring_func": "sigmoid",
    "use_routing_bias": true,
    "moe_layer_freq": [
      0,
      0,
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
      1
    ],
    "qk_norm_type": "per_head",
    "num_mtp_modules": 7,
    "num_nextn_predict_layers": 1,
    "swiglu_alpha": 1.702,
    "swiglu_limit": 7.0,
    "routed_scaling_factor": 2.0,
    "sparse_attention_config": {
      "use_sparse_attention": true,
      "sparse_index_dim": 128,
      "sparse_num_index_heads": 4,
      "sparse_topk_blocks": 16,
      "sparse_block_size": 128,
      "sparse_disable_index_value": [
        0,
        0,
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
        1
      ],
      "sparse_score_type": "max",
      "sparse_init_block": 0,
      "sparse_local_block": 1,
      "sparse_attention_freq": [
        0,
        0,
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
        1
      ]
    },
    "architectures": [
      "MiniMaxM3SparseForCausalLM"
    ]
  },
  "vision_config": {
    "hidden_size": 1280,
    "num_attention_heads": 16,
    "num_hidden_layers": 32,
    "intermediate_size": 5120,
    "patch_size": 14,
    "image_size": 2016,
    "projection_dim": 6144,
    "position_embedding_type": "rope",
    "rope_mode": "3d",
    "rope_theta": 10000.0,
    "attention_dropout": 0.0,
    "hidden_act": "gelu",
    "initializer_factor": 1.0,
    "initializer_range": 0.02,
    "layer_norm_eps": 1e-05,
    "model_type": "clip_vision_model",
    "num_channels": 3,
    "vocab_size": 32000,
    "img_token_compression_config": {
      "image_token_compression_method": "patch_merge",
      "spatial_merge_size": 2,
      "temporal_patch_size": 2
    },
    "vision_segment_max_frames": 4
  },
  "img_token_compression_config": {
    "image_token_compression_method": "patch_merge",
    "spatial_merge_size": 2,
    "temporal_patch_size": 2
  },
  "image_grid_pinpoints": "[(336, 336), (336, 672), (336, 1008), (336, 1344), (336, 1680), (336, 2016), (672, 336), (672, 672), (672, 1008), (672, 1344), (672, 1680), (672, 2016), (1008, 336), (1008, 672), (1008, 1008), (1008, 1344), (1008, 1680), (1008, 2016), (1344, 336), (1344, 672), (1344, 1008), (1344, 1344), (1344, 1680), (1344, 2016), (1680, 336), (1680, 672), (1680, 1008), (1680, 1344), (1680, 1680), (1680, 2016), (2016, 336), (2016, 672), (2016, 1008), (2016, 1344), (2016, 1680), (2016, 2016)]",
  "image_seq_length": 576,
  "image_token_index": 200025,
  "video_token_index": 200026,
  "multimodal_projector_bias": true,
  "num_reward_heads": 0,
  "process_image_mode": "dynamic_res",
  "projector_hidden_act": "gelu",
  "vision_feature_layer": -1,
  "vision_feature_select_strategy": "full",
  "torch_dtype": "bfloat16",
  "transformers_version": "4.52.4",
  "projector_hidden_size": 6144
}

```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `MiniMaxM3VLConfig`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: N/A
- **层数**: N/A
- **注意力头数**: N/A
- **词表大小**: N/A
- **中间层大小**: N/A

```
MiniMaxM3VLConfig {
  "architectures": [
    "MiniMaxM3SparseForConditionalGeneration"
  ],
  "auto_map": {
    "AutoConfig": "configuration_minimax_m3_vl.MiniMaxM3VLConfig"
  },
  "dtype": "bfloat16",
  "image_grid_pinpoints": "[(336, 336), (336, 672), (336, 1008), (336, 1344), (336, 1680), (336, 2016), (672, 336), (672, 672), (672, 1008), (672, 1344), (672, 1680), (672, 2016), (1008, 336), (1008, 672), (1008, 1008), (1008, 1344), (1008, 1680), (1008, 2016), (1344, 336), (1344, 672), (1344, 1008), (1344, 1344), (1344, 1680), (1344, 2016), (1680, 336), (1680, 672), (1680, 1008), (1680, 1344), (1680, 1680), (1680, 2016), (2016, 336), (2016, 672), (2016, 1008), (2016, 1344), (2016, 1680), (2016, 2016)]",
  "image_seq_length": 576,
  "image_token_index": 200025,
  "img_token_compression_config": {
    "image_token_compression_method": "patch_merge",
    "spatial_merge_size": 2,
    "temporal_patch_size": 2
  },
  "model_type": "minimax_m3_vl",
  "multimodal_projector_bias": true,
  "num_reward_heads": 0,
  "process_image_mode": "dynamic_res",
  "projector_hidden_act": "gelu",
  "projector_hidden_size": 6144,
  "text_config": {
    "_name_or_path": "",
    "architectures": [
      "MiniMaxM3SparseForCausalLM"
    ],
    "attention_output_gate": false,
    "chunk_size_feed_forward": 0,
    "dense_intermediate_size": 12288,
    "dtype": null,
    "head_dim": 128,
    "hidden_act": "swigluoai",
    "hidden_size": 6144,
    "id2label": {
      "0": "LABEL_0",
      "1": "LABEL_1"
    },
    "intermediate_size": 3072,
    "is_encoder_decoder": false,
    "label2id": {
      "LABEL_0": 0,
      "LABEL_1": 1
    },
    "max_position_embeddings": 1048576,
    "model_type": "",
    "moe_layer_freq": [
      0,
      0,
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
      1
    ],
    "n_shared_experts": 1,
    "num_attention_heads": 64,
    "num_experts_per_tok": 4,
    "num_hidden_layers": 60,
    "num_key_value_heads": 4,
    "num_local_experts": 128,
    "num_mtp_modules": 7,
    "num_nextn_predict_layers": 1,
    "output_attentions": false,
    "output_hidden_states": false,
    "partial_rotary_factor": 0.5,
    "problem_type": null,
    "qk_norm_type": "per_head",
    "return_dict": true,
    "rms_norm_eps": 1e-06,
    "rope_theta": 5000000,
    "rotary_dim": 64,
    "routed_scaling_factor": 2.0,
    "scoring_func": "sigmoid",
    "shared_intermediate_size": 3072,
    "sparse_attention_config": {
      "sparse_attention_freq": [
        0,
        0,
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
        1
      ],
      "sparse_block_size": 128,
      "sparse_disable_index_value": [
        0,
        0,
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
        1
      ],
      "sparse_index_dim": 128,
      "sparse_init_block": 0,
      "sparse_local_block": 1,
      "sparse_num_index_heads": 4,
      "sparse_score_type": "max",
      "sparse_topk_blocks": 16,
      "use_sparse_attention": true
    },
    "swiglu_alpha": 1.702,
    "swiglu_limit": 7.0,
    "tie_word_embeddings": false,
    "use_gemma_norm": true,
    "use_qk_norm": true,
    "use_routing_bias": true,
    "vocab_size": 200064
  },
  "transformers_version": "5.7.0",
  "video_token_index": 200026,
  "vision_config": {
    "_name_or_path": "",
    "architectures": null,
    "attention_dropout": 0.0,
    "chunk_size_feed_forward": 0,
    "dtype": null,
    "hidden_act": "gelu",
    "hidden_size": 1280,
    "id2label": {
      "0": "LABEL_0",
      "1": "LABEL_1"
    },
    "image_size": 2016,
    "img_token_compression_config": {
      "image_token_compression_method": "patch_merge",
      "spatial_merge_size": 2,
      "temporal_patch_size": 2
    },
    "initializer_factor": 1.0,
    "initializer_range": 0.02,
    "intermediate_size": 5120,
    "is_encoder_decoder": false,
    "label2id": {
      "LABEL_0": 0,
      "LABEL_1": 1
    },
    "layer_norm_eps": 1e-05,
    "model_type": "",
    "num_attention_heads": 16,
    "num_channels": 3,
    "num_hidden_layers": 32,
    "output_attentions": false,
    "output_hidden_states": false,
    "patch_size": 14,
    "position_embedding_type": "rope",
    "problem_type": null,
    "projection_dim": 6144,
    "return_dict": true,
    "rope_mode": "3d",
    "rope_theta": 10000.0,
    "vision_segment_max_frames": 4,
    "vocab_size": 32000
  },
  "vision_feature_layer": -1,
  "vision_feature_select_strategy": "full"
}

```

</details>

# 模型结构

**模型类**: `MiniMaxM3VLConfig` (当前 transformers 版本不支持实例化)

# 权重统计

- **权重文件**: 59 个 `safetensors` 文件
- **文件总大小**: 795.51 GB
- **权重张量数**: 23,416
- **参数总量**: 427,040,140,160
- **张量累计大小**: 795.51 GB
- **压缩**: 23416 → 53 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `language_model.lm_head.weight` | `[200064, 6144]` | `torch.bfloat16` | 2.29 GB | model-00001-of-00059.safetensors |
| `language_model.model.embed_tokens.weight` | `[200064, 6144]` | `torch.bfloat16` | 2.29 GB | model-00001-of-00059.safetensors |
| `language_model.model.layers.0-2.mlp.down_proj.weight` (×3 layers) | `[6144, 12288]` | `torch.bfloat16` | 432.00 MB | Multi Files |
| `language_model.model.layers.0-2.mlp.gate_proj.weight` (×3 layers) | `[12288, 6144]` | `torch.bfloat16` | 432.00 MB | Multi Files |
| `language_model.model.layers.0-2.mlp.up_proj.weight` (×3 layers) | `[12288, 6144]` | `torch.bfloat16` | 432.00 MB | Multi Files |
| `language_model.model.layers.0-59.input_layernorm.weight` (×60 layers) | `[6144]` | `torch.bfloat16` | 720.00 KB | Multi Files |
| `language_model.model.layers.0-59.post_attention_layernorm.weight` (×60 layers) | `[6144]` | `torch.bfloat16` | 720.00 KB | Multi Files |
| `language_model.model.layers.0-59.self_attn.k_norm.weight` (×60 layers) | `[128]` | `torch.bfloat16` | 15.00 KB | Multi Files |
| `language_model.model.layers.0-59.self_attn.k_proj.weight` (×60 layers) | `[512, 6144]` | `torch.bfloat16` | 360.00 MB | Multi Files |
| `language_model.model.layers.0-59.self_attn.o_proj.weight` (×60 layers) | `[6144, 8192]` | `torch.bfloat16` | 5.62 GB | Multi Files |
| `language_model.model.layers.0-59.self_attn.q_norm.weight` (×60 layers) | `[128]` | `torch.bfloat16` | 15.00 KB | Multi Files |
| `language_model.model.layers.0-59.self_attn.q_proj.weight` (×60 layers) | `[8192, 6144]` | `torch.bfloat16` | 5.62 GB | Multi Files |
| `language_model.model.layers.0-59.self_attn.v_proj.weight` (×60 layers) | `[512, 6144]` | `torch.bfloat16` | 360.00 MB | Multi Files |
| `language_model.model.layers.3-59.block_sparse_moe.e_score_correction_bias` (×57 layers) | `[128]` | `torch.float32` | 28.50 KB | Multi Files |
| `language_model.model.layers.3-59.block_sparse_moe.experts.0-127.w1.weight` (×57 layers, ×128 experts) | `[3072, 6144]` | `torch.bfloat16` | 256.50 GB | Multi Files |
| `language_model.model.layers.3-59.block_sparse_moe.experts.0-127.w2.weight` (×57 layers, ×128 experts) | `[6144, 3072]` | `torch.bfloat16` | 256.50 GB | Multi Files |
| `language_model.model.layers.3-59.block_sparse_moe.experts.0-127.w3.weight` (×57 layers, ×128 experts) | `[3072, 6144]` | `torch.bfloat16` | 256.50 GB | Multi Files |
| `language_model.model.layers.3-59.block_sparse_moe.gate.weight` (×57 layers) | `[128, 6144]` | `torch.float32` | 171.00 MB | Multi Files |
| `language_model.model.layers.3-59.block_sparse_moe.shared_experts.down_proj.weight` (×57 layers) | `[6144, 3072]` | `torch.bfloat16` | 2.00 GB | Multi Files |
| `language_model.model.layers.3-59.block_sparse_moe.shared_experts.gate_proj.weight` (×57 layers) | `[3072, 6144]` | `torch.bfloat16` | 2.00 GB | Multi Files |
| `language_model.model.layers.3-59.block_sparse_moe.shared_experts.up_proj.weight` (×57 layers) | `[3072, 6144]` | `torch.bfloat16` | 2.00 GB | Multi Files |
| `language_model.model.layers.3-59.self_attn.index_k_norm.weight` (×57 layers) | `[128]` | `torch.bfloat16` | 14.25 KB | Multi Files |
| `language_model.model.layers.3-59.self_attn.index_k_proj.weight` (×57 layers) | `[128, 6144]` | `torch.bfloat16` | 85.50 MB | Multi Files |
| `language_model.model.layers.3-59.self_attn.index_q_norm.weight` (×57 layers) | `[128]` | `torch.bfloat16` | 14.25 KB | Multi Files |
| `language_model.model.layers.3-59.self_attn.index_q_proj.weight` (×57 layers) | `[512, 6144]` | `torch.bfloat16` | 342.00 MB | Multi Files |
| `language_model.model.norm.weight` | `[6144]` | `torch.bfloat16` | 12.00 KB | model-00001-of-00059.safetensors |
| `multi_modal_projector.linear_1.bias` | `[6144]` | `torch.bfloat16` | 12.00 KB | model-00059-of-00059.safetensors |
| `multi_modal_projector.linear_1.weight` | `[6144, 1280]` | `torch.bfloat16` | 15.00 MB | model-00026-of-00059.safetensors |
| `multi_modal_projector.linear_2.bias` | `[6144]` | `torch.bfloat16` | 12.00 KB | model-00026-of-00059.safetensors |
| `multi_modal_projector.linear_2.weight` | `[6144, 6144]` | `torch.bfloat16` | 72.00 MB | model-00026-of-00059.safetensors |
| `patch_merge_mlp.linear_1.bias` | `[6144]` | `torch.bfloat16` | 12.00 KB | model-00026-of-00059.safetensors |
| `patch_merge_mlp.linear_1.weight` | `[6144, 24576]` | `torch.bfloat16` | 288.00 MB | model-00026-of-00059.safetensors |
| `patch_merge_mlp.linear_2.bias` | `[6144]` | `torch.bfloat16` | 12.00 KB | model-00026-of-00059.safetensors |
| `patch_merge_mlp.linear_2.weight` | `[6144, 6144]` | `torch.bfloat16` | 72.00 MB | model-00026-of-00059.safetensors |
| `vision_tower.vision_model.embeddings.patch_embedding.weight` | `[1280, 3, 2, 14, 14]` | `torch.float32` | 5.74 MB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.layer_norm1.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.layer_norm1.weight` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.layer_norm2.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.layer_norm2.weight` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.mlp.fc1.bias` (×32 layers) | `[5120]` | `torch.bfloat16` | 320.00 KB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.mlp.fc1.weight` (×32 layers) | `[5120, 1280]` | `torch.bfloat16` | 400.00 MB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.mlp.fc2.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.mlp.fc2.weight` (×32 layers) | `[1280, 5120]` | `torch.bfloat16` | 400.00 MB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.self_attn.k_proj.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.self_attn.k_proj.weight` (×32 layers) | `[1280, 1280]` | `torch.bfloat16` | 100.00 MB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.self_attn.out_proj.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.self_attn.out_proj.weight` (×32 layers) | `[1280, 1280]` | `torch.bfloat16` | 100.00 MB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.self_attn.q_proj.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.self_attn.q_proj.weight` (×32 layers) | `[1280, 1280]` | `torch.bfloat16` | 100.00 MB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.self_attn.v_proj.bias` (×32 layers) | `[1280]` | `torch.bfloat16` | 80.00 KB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.encoder.layers.0-31.self_attn.v_proj.weight` (×32 layers) | `[1280, 1280]` | `torch.bfloat16` | 100.00 MB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.pre_layrnorm.bias` | `[1280]` | `torch.bfloat16` | 2.50 KB | model-00059-of-00059.safetensors |
| `vision_tower.vision_model.pre_layrnorm.weight` | `[1280]` | `torch.bfloat16` | 2.50 KB | model-00059-of-00059.safetensors |

</details>

