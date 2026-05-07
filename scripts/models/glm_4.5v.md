# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/GLM-4.5V`

# 模型配置

- **模型类型**: `Glm4vMoeConfig`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: N/A
- **层数**: N/A
- **注意力头数**: N/A
- **词表大小**: N/A
- **中间层大小**: N/A

<details><summary>完整配置</summary>

```
Glm4vMoeConfig {
  "architectures": [
    "Glm4vMoeForConditionalGeneration"
  ],
  "dtype": "bfloat16",
  "image_end_token_id": 151340,
  "image_start_token_id": 151339,
  "image_token_id": 151363,
  "model_type": "glm4v_moe",
  "text_config": {
    "attention_bias": true,
    "attention_dropout": 0.0,
    "bos_token_id": null,
    "dtype": "bfloat16",
    "eos_token_id": [
      151329,
      151336,
      151338
    ],
    "first_k_dense_replace": 1,
    "head_dim": 128,
    "hidden_act": "silu",
    "hidden_size": 4096,
    "image_end_token_id": 151340,
    "image_start_token_id": 151339,
    "image_token_id": 151363,
    "initializer_range": 0.02,
    "intermediate_size": 10944,
    "max_position_embeddings": 65536,
    "model_type": "glm4v_moe_text",
    "moe_intermediate_size": 1408,
    "n_group": 1,
    "n_routed_experts": 128,
    "n_shared_experts": 1,
    "norm_topk_prob": true,
    "num_attention_heads": 96,
    "num_experts_per_tok": 8,
    "num_hidden_layers": 46,
    "num_key_value_heads": 8,
    "pad_token_id": 151329,
    "partial_rotary_factor": 0.5,
    "rms_norm_eps": 1e-05,
    "rope_parameters": {
      "mrope_section": [
        8,
        12,
        12
      ],
      "partial_rotary_factor": 0.5,
      "rope_theta": 10000.0,
      "rope_type": "default"
    },
    "routed_scaling_factor": 1.0,
    "router_aux_loss_coef": 0.0001,
    "tie_word_embeddings": false,
    "topk_group": 1,
    "use_cache": true,
    "use_qk_norm": false,
    "vocab_size": 151552
  },
  "tie_word_embeddings": false,
  "transformers_version": "5.7.0",
  "video_end_token_id": 151342,
  "video_start_token_id": 151341,
  "video_token_id": 151364,
  "vision_config": {
    "attention_bias": false,
    "attention_dropout": 0.0,
    "depth": 24,
    "hidden_act": "silu",
    "hidden_size": 1536,
    "image_size": 336,
    "in_channels": 3,
    "initializer_range": 0.02,
    "intermediate_size": 10944,
    "model_type": "glm4v_moe_vision",
    "num_heads": 12,
    "out_hidden_size": 4096,
    "patch_size": 14,
    "rms_norm_eps": 1e-05,
    "spatial_merge_size": 2,
    "temporal_patch_size": 2
  }
}

```

</details>

# 模型结构

**模型类**: `Glm4vMoeModel`

```
Glm4vMoeModel(
  (visual): Glm4vMoeVisionModel(
    (embeddings): Glm4vMoeVisionEmbeddings(
      (position_embedding): Embedding(576, 1536)
    )
    (patch_embed): Glm4vMoeVisionPatchEmbed(
      (proj): Conv3d(3, 1536, kernel_size=(2, 14, 14), stride=(2, 14, 14))
    )
    (rotary_pos_emb): Glm4vMoeVisionRotaryEmbedding()
    (blocks): ModuleList(
      (0-23): 24 x Glm4vMoeVisionBlock(
        (norm1): Glm4vMoeRMSNorm((1536,), eps=1e-05)
        (norm2): Glm4vMoeRMSNorm((1536,), eps=1e-05)
        (attn): Glm4vMoeVisionAttention(
          (qkv): Linear(in_features=1536, out_features=4608, bias=False)
          (proj): Linear(in_features=1536, out_features=1536, bias=False)
        )
        (mlp): Glm4vMoeisionMlp(
          (gate_proj): Linear(in_features=1536, out_features=4096, bias=False)
          (up_proj): Linear(in_features=1536, out_features=4096, bias=False)
          (down_proj): Linear(in_features=4096, out_features=1536, bias=False)
          (act_fn): SiLUActivation()
        )
      )
    )
    (merger): Glm4vMoeVisionPatchMerger(
      (proj): Linear(in_features=4096, out_features=4096, bias=False)
      (post_projection_norm): LayerNorm((4096,), eps=1e-05, elementwise_affine=True)
      (gate_proj): Linear(in_features=4096, out_features=10944, bias=False)
      (up_proj): Linear(in_features=4096, out_features=10944, bias=False)
      (down_proj): Linear(in_features=10944, out_features=4096, bias=False)
      (act1): GELU(approximate='none')
      (act_fn): SiLUActivation()
    )
    (post_conv_layernorm): Glm4vMoeRMSNorm((1536,), eps=1e-05)
    (downsample): Conv2d(1536, 4096, kernel_size=(2, 2), stride=(2, 2))
    (post_layernorm): Glm4vMoeRMSNorm((1536,), eps=1e-05)
  )
  (language_model): Glm4vMoeTextModel(
    (embed_tokens): Embedding(151552, 4096, padding_idx=151329)
    (layers): ModuleList(
      (0): Glm4vMoeTextDecoderLayer(
        (self_attn): Glm4vMoeTextAttention(
          (q_proj): Linear(in_features=4096, out_features=12288, bias=True)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=True)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=True)
          (o_proj): Linear(in_features=12288, out_features=4096, bias=False)
        )
        (mlp): Glm4vMoeTextMLP(
          (gate_proj): Linear(in_features=4096, out_features=10944, bias=False)
          (up_proj): Linear(in_features=4096, out_features=10944, bias=False)
          (down_proj): Linear(in_features=10944, out_features=4096, bias=False)
          (act_fn): SiLUActivation()
        )
        (input_layernorm): Glm4vMoeTextRMSNorm((4096,), eps=1e-05)
        (post_attention_layernorm): Glm4vMoeTextRMSNorm((4096,), eps=1e-05)
      )
      (1-45): 45 x Glm4vMoeTextDecoderLayer(
        (self_attn): Glm4vMoeTextAttention(
          (q_proj): Linear(in_features=4096, out_features=12288, bias=True)
          (k_proj): Linear(in_features=4096, out_features=1024, bias=True)
          (v_proj): Linear(in_features=4096, out_features=1024, bias=True)
          (o_proj): Linear(in_features=12288, out_features=4096, bias=False)
        )
        (mlp): Glm4vMoeTextMoE(
          (experts): Glm4vMoeTextNaiveMoe(
            (act_fn): SiLUActivation()
          )
          (gate): Glm4vMoeTextTopkRouter()
          (shared_experts): Glm4vMoeTextMLP(
            (gate_proj): Linear(in_features=4096, out_features=1408, bias=False)
            (up_proj): Linear(in_features=4096, out_features=1408, bias=False)
            (down_proj): Linear(in_features=1408, out_features=4096, bias=False)
            (act_fn): SiLUActivation()
          )
        )
        (input_layernorm): Glm4vMoeTextRMSNorm((4096,), eps=1e-05)
        (post_attention_layernorm): Glm4vMoeTextRMSNorm((4096,), eps=1e-05)
      )
    )
    (norm): Glm4vMoeRMSNorm((4096,), eps=1e-05)
    (rotary_emb): Glm4vMoeTextRotaryEmbedding()
  )
)
```

# 权重统计

- **权重文件**: 46 个 `safetensors` 文件
- **文件总大小**: 200.63 GB
- **权重张量数**: 18,106
- **参数总量**: 107,710,933,120
- **张量累计大小**: 200.63 GB
- **压缩**: 18106 → 43 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[151552, 4096]` | `torch.bfloat16` | 1.16 GB | model-00046-of-00046.safetensors |
| `model.language_model.embed_tokens.weight` | `[151552, 4096]` | `torch.bfloat16` | 1.16 GB | model-00046-of-00046.safetensors |
| `model.language_model.layers.0-45.input_layernorm.weight` (×46 layers) | `[4096]` | `torch.bfloat16` | 368.00 KB | Multi Files |
| `model.language_model.layers.0-45.post_attention_layernorm.weight` (×46 layers) | `[4096]` | `torch.bfloat16` | 368.00 KB | Multi Files |
| `model.language_model.layers.0-45.self_attn.k_proj.bias` (×46 layers) | `[1024]` | `torch.bfloat16` | 92.00 KB | Multi Files |
| `model.language_model.layers.0-45.self_attn.k_proj.weight` (×46 layers) | `[1024, 4096]` | `torch.bfloat16` | 368.00 MB | Multi Files |
| `model.language_model.layers.0-45.self_attn.o_proj.weight` (×46 layers) | `[4096, 12288]` | `torch.bfloat16` | 4.31 GB | Multi Files |
| `model.language_model.layers.0-45.self_attn.q_proj.bias` (×46 layers) | `[12288]` | `torch.bfloat16` | 1.08 MB | Multi Files |
| `model.language_model.layers.0-45.self_attn.q_proj.weight` (×46 layers) | `[12288, 4096]` | `torch.bfloat16` | 4.31 GB | Multi Files |
| `model.language_model.layers.0-45.self_attn.v_proj.bias` (×46 layers) | `[1024]` | `torch.bfloat16` | 92.00 KB | Multi Files |
| `model.language_model.layers.0-45.self_attn.v_proj.weight` (×46 layers) | `[1024, 4096]` | `torch.bfloat16` | 368.00 MB | Multi Files |
| `model.language_model.layers.0.mlp.down_proj.weight` (×1 layers) | `[4096, 10944]` | `torch.bfloat16` | 85.50 MB | model-00001-of-00046.safetensors |
| `model.language_model.layers.0.mlp.gate_proj.weight` (×1 layers) | `[10944, 4096]` | `torch.bfloat16` | 85.50 MB | model-00001-of-00046.safetensors |
| `model.language_model.layers.0.mlp.up_proj.weight` (×1 layers) | `[10944, 4096]` | `torch.bfloat16` | 85.50 MB | model-00001-of-00046.safetensors |
| `model.language_model.layers.1-45.mlp.experts.0-127.down_proj.weight` (×45 layers, ×128 experts) | `[4096, 1408]` | `torch.bfloat16` | 61.88 GB | Multi Files |
| `model.language_model.layers.1-45.mlp.experts.0-127.gate_proj.weight` (×45 layers, ×128 experts) | `[1408, 4096]` | `torch.bfloat16` | 61.88 GB | Multi Files |
| `model.language_model.layers.1-45.mlp.experts.0-127.up_proj.weight` (×45 layers, ×128 experts) | `[1408, 4096]` | `torch.bfloat16` | 61.88 GB | Multi Files |
| `model.language_model.layers.1-45.mlp.gate.e_score_correction_bias` (×45 layers) | `[128]` | `torch.float32` | 22.50 KB | Multi Files |
| `model.language_model.layers.1-45.mlp.gate.weight` (×45 layers) | `[128, 4096]` | `torch.bfloat16` | 45.00 MB | Multi Files |
| `model.language_model.layers.1-45.mlp.shared_experts.down_proj.weight` (×45 layers) | `[4096, 1408]` | `torch.bfloat16` | 495.00 MB | Multi Files |
| `model.language_model.layers.1-45.mlp.shared_experts.gate_proj.weight` (×45 layers) | `[1408, 4096]` | `torch.bfloat16` | 495.00 MB | Multi Files |
| `model.language_model.layers.1-45.mlp.shared_experts.up_proj.weight` (×45 layers) | `[1408, 4096]` | `torch.bfloat16` | 495.00 MB | Multi Files |
| `model.language_model.norm.weight` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00046-of-00046.safetensors |
| `model.visual.blocks.0-23.attn.proj.weight` (×24 blocks) | `[1536, 1536]` | `torch.bfloat16` | 108.00 MB | Multi Files |
| `model.visual.blocks.0-23.attn.qkv.weight` (×24 blocks) | `[4608, 1536]` | `torch.bfloat16` | 324.00 MB | Multi Files |
| `model.visual.blocks.0-23.mlp.down_proj.weight` (×24 blocks) | `[1536, 4096]` | `torch.bfloat16` | 288.00 MB | Multi Files |
| `model.visual.blocks.0-23.mlp.gate_proj.weight` (×24 blocks) | `[4096, 1536]` | `torch.bfloat16` | 288.00 MB | Multi Files |
| `model.visual.blocks.0-23.mlp.up_proj.weight` (×24 blocks) | `[4096, 1536]` | `torch.bfloat16` | 288.00 MB | Multi Files |
| `model.visual.blocks.0-23.norm1.weight` (×24 blocks) | `[1536]` | `torch.bfloat16` | 72.00 KB | Multi Files |
| `model.visual.blocks.0-23.norm2.weight` (×24 blocks) | `[1536]` | `torch.bfloat16` | 72.00 KB | Multi Files |
| `model.visual.downsample.bias` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00046-of-00046.safetensors |
| `model.visual.downsample.weight` | `[4096, 1536, 2, 2]` | `torch.bfloat16` | 48.00 MB | model-00046-of-00046.safetensors |
| `model.visual.embeddings.position_embedding.weight` | `[576, 1536]` | `torch.bfloat16` | 1.69 MB | model-00046-of-00046.safetensors |
| `model.visual.merger.down_proj.weight` | `[4096, 10944]` | `torch.bfloat16` | 85.50 MB | model-00046-of-00046.safetensors |
| `model.visual.merger.gate_proj.weight` | `[10944, 4096]` | `torch.bfloat16` | 85.50 MB | model-00046-of-00046.safetensors |
| `model.visual.merger.post_projection_norm.bias` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00046-of-00046.safetensors |
| `model.visual.merger.post_projection_norm.weight` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00046-of-00046.safetensors |
| `model.visual.merger.proj.weight` | `[4096, 4096]` | `torch.bfloat16` | 32.00 MB | model-00046-of-00046.safetensors |
| `model.visual.merger.up_proj.weight` | `[10944, 4096]` | `torch.bfloat16` | 85.50 MB | model-00046-of-00046.safetensors |
| `model.visual.patch_embed.proj.bias` | `[1536]` | `torch.bfloat16` | 3.00 KB | model-00046-of-00046.safetensors |
| `model.visual.patch_embed.proj.weight` | `[1536, 3, 2, 14, 14]` | `torch.bfloat16` | 3.45 MB | model-00046-of-00046.safetensors |
| `model.visual.post_conv_layernorm.weight` | `[1536]` | `torch.bfloat16` | 3.00 KB | model-00046-of-00046.safetensors |
| `model.visual.post_layernorm.weight` | `[1536]` | `torch.bfloat16` | 3.00 KB | model-00046-of-00046.safetensors |

</details>

