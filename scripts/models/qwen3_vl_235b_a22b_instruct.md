# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen3-VL-235B-A22B-Instruct`

# 模型配置

- **模型类型**: `Qwen3VLMoeConfig`
- **数据类型**: `None`
- **隐藏层大小**: N/A
- **层数**: N/A
- **注意力头数**: N/A
- **词表大小**: N/A
- **中间层大小**: N/A

<details><summary>完整配置</summary>

```
Qwen3VLMoeConfig {
  "architectures": [
    "Qwen3VLMoeForConditionalGeneration"
  ],
  "image_token_id": 151655,
  "model_type": "qwen3_vl_moe",
  "text_config": {
    "attention_bias": false,
    "attention_dropout": 0.0,
    "bos_token_id": 151643,
    "decoder_sparse_step": 1,
    "dtype": "bfloat16",
    "eos_token_id": 151645,
    "head_dim": 128,
    "hidden_act": "silu",
    "hidden_size": 4096,
    "initializer_range": 0.02,
    "intermediate_size": 12288,
    "max_position_embeddings": 262144,
    "mlp_only_layers": [],
    "model_type": "qwen3_vl_moe_text",
    "moe_intermediate_size": 1536,
    "norm_topk_prob": true,
    "num_attention_heads": 64,
    "num_experts_per_tok": 8,
    "num_hidden_layers": 94,
    "num_key_value_heads": 4,
    "num_local_experts": 128,
    "pad_token_id": null,
    "rms_norm_eps": 1e-06,
    "rope_parameters": {
      "mrope_interleaved": true,
      "mrope_section": [
        24,
        20,
        20
      ],
      "rope_theta": 5000000,
      "rope_type": "default"
    },
    "router_aux_loss_coef": 0.001,
    "sliding_window": null,
    "tie_word_embeddings": true,
    "use_cache": true,
    "vocab_size": 151936
  },
  "tie_word_embeddings": false,
  "transformers_version": "5.7.0",
  "video_token_id": 151656,
  "vision_config": {
    "deepstack_visual_indexes": [
      8,
      16,
      24
    ],
    "depth": 27,
    "hidden_act": "gelu_pytorch_tanh",
    "hidden_size": 1152,
    "in_channels": 3,
    "initializer_range": 0.02,
    "intermediate_size": 4304,
    "model_type": "qwen3_vl_moe_vision",
    "num_heads": 16,
    "num_position_embeddings": 2304,
    "out_hidden_size": 4096,
    "patch_size": 16,
    "spatial_merge_size": 2,
    "temporal_patch_size": 2
  },
  "vision_end_token_id": 151653,
  "vision_start_token_id": 151652
}

```

</details>

# 模型结构

**模型类**: `Qwen3VLMoeModel`

```
Qwen3VLMoeModel(
  (visual): Qwen3VLMoeVisionModel(
    (patch_embed): Qwen3VLMoeVisionPatchEmbed(
      (proj): Conv3d(3, 1152, kernel_size=(2, 16, 16), stride=(2, 16, 16))
    )
    (pos_embed): Embedding(2304, 1152)
    (rotary_pos_emb): Qwen3VLMoeVisionRotaryEmbedding()
    (blocks): ModuleList(
      (0-26): 27 x Qwen3VLMoeVisionBlock(
        (norm1): LayerNorm((1152,), eps=1e-06, elementwise_affine=True)
        (norm2): LayerNorm((1152,), eps=1e-06, elementwise_affine=True)
        (attn): Qwen3VLMoeVisionAttention(
          (qkv): Linear(in_features=1152, out_features=3456, bias=True)
          (proj): Linear(in_features=1152, out_features=1152, bias=True)
        )
        (mlp): Qwen3VLMoeVisionMLP(
          (linear_fc1): Linear(in_features=1152, out_features=4304, bias=True)
          (linear_fc2): Linear(in_features=4304, out_features=1152, bias=True)
          (act_fn): GELUTanh()
        )
      )
    )
    (merger): Qwen3VLMoeVisionPatchMerger(
      (norm): LayerNorm((1152,), eps=1e-06, elementwise_affine=True)
      (linear_fc1): Linear(in_features=4608, out_features=4608, bias=True)
      (act_fn): GELU(approximate='none')
      (linear_fc2): Linear(in_features=4608, out_features=4096, bias=True)
    )
    (deepstack_merger_list): ModuleList(
      (0-2): 3 x Qwen3VLMoeVisionPatchMerger(
        (norm): LayerNorm((4608,), eps=1e-06, elementwise_affine=True)
        (linear_fc1): Linear(in_features=4608, out_features=4608, bias=True)
        (act_fn): GELU(approximate='none')
        (linear_fc2): Linear(in_features=4608, out_features=4096, bias=True)
      )
    )
  )
  (language_model): Qwen3VLMoeTextModel(
    (embed_tokens): Embedding(151936, 4096)
    (layers): ModuleList(
      (0-93): 94 x Qwen3VLMoeTextDecoderLayer(
        (self_attn): Qwen3VLMoeTextAttention(
          (q_proj): Linear(in_features=4096, out_features=8192, bias=False)
          (k_proj): Linear(in_features=4096, out_features=512, bias=False)
          (v_proj): Linear(in_features=4096, out_features=512, bias=False)
          (o_proj): Linear(in_features=8192, out_features=4096, bias=False)
          (q_norm): Qwen3VLMoeTextRMSNorm((128,), eps=1e-06)
          (k_norm): Qwen3VLMoeTextRMSNorm((128,), eps=1e-06)
        )
        (mlp): Qwen3VLMoeTextSparseMoeBlock(
          (experts): Qwen3VLMoeTextExperts(
            (act_fn): SiLUActivation()
          )
          (gate): Qwen3VLMoeTextTopKRouter()
        )
        (input_layernorm): Qwen3VLMoeTextRMSNorm((4096,), eps=1e-06)
        (post_attention_layernorm): Qwen3VLMoeTextRMSNorm((4096,), eps=1e-06)
      )
    )
    (norm): Qwen3VLMoeTextRMSNorm((4096,), eps=1e-06)
    (rotary_emb): Qwen3VLMoeTextRotaryEmbedding()
  )
)
```

# 权重统计

- **权重文件**: 96 个 `safetensors` 文件
- **文件总大小**: 438.97 GB
- **权重张量数**: 1,388
- **参数总量**: 235,670,022,896
- **张量累计大小**: 438.97 GB
- **压缩**: 1388 → 41 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[151936, 4096]` | `torch.bfloat16` | 1.16 GB | model-00096-of-00096.safetensors |
| `model.language_model.embed_tokens.weight` | `[151936, 4096]` | `torch.bfloat16` | 1.16 GB | model-00001-of-00096.safetensors |
| `model.language_model.layers.0-93.input_layernorm.weight` (×94 layers) | `[4096]` | `torch.bfloat16` | 752.00 KB | Multi Files |
| `model.language_model.layers.0-93.mlp.experts.down_proj` (×94 layers) | `[128, 1536, 4096]` | `torch.bfloat16` | 141.00 GB | Multi Files |
| `model.language_model.layers.0-93.mlp.experts.gate_up_proj` (×94 layers) | `[128, 4096, 3072]` | `torch.bfloat16` | 282.00 GB | Multi Files |
| `model.language_model.layers.0-93.mlp.gate.weight` (×94 layers) | `[128, 4096]` | `torch.bfloat16` | 94.00 MB | Multi Files |
| `model.language_model.layers.0-93.post_attention_layernorm.weight` (×94 layers) | `[4096]` | `torch.bfloat16` | 752.00 KB | Multi Files |
| `model.language_model.layers.0-93.self_attn.k_norm.weight` (×94 layers) | `[128]` | `torch.bfloat16` | 23.50 KB | Multi Files |
| `model.language_model.layers.0-93.self_attn.k_proj.weight` (×94 layers) | `[512, 4096]` | `torch.bfloat16` | 376.00 MB | Multi Files |
| `model.language_model.layers.0-93.self_attn.o_proj.weight` (×94 layers) | `[4096, 8192]` | `torch.bfloat16` | 5.88 GB | Multi Files |
| `model.language_model.layers.0-93.self_attn.q_norm.weight` (×94 layers) | `[128]` | `torch.bfloat16` | 23.50 KB | Multi Files |
| `model.language_model.layers.0-93.self_attn.q_proj.weight` (×94 layers) | `[8192, 4096]` | `torch.bfloat16` | 5.88 GB | Multi Files |
| `model.language_model.layers.0-93.self_attn.v_proj.weight` (×94 layers) | `[512, 4096]` | `torch.bfloat16` | 376.00 MB | Multi Files |
| `model.language_model.norm.weight` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00095-of-00096.safetensors |
| `model.visual.blocks.0-26.attn.proj.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00001-of-00096.safetensors |
| `model.visual.blocks.0-26.attn.proj.weight` (×27 blocks) | `[1152, 1152]` | `torch.bfloat16` | 68.34 MB | model-00001-of-00096.safetensors |
| `model.visual.blocks.0-26.attn.qkv.bias` (×27 blocks) | `[3456]` | `torch.bfloat16` | 182.25 KB | model-00001-of-00096.safetensors |
| `model.visual.blocks.0-26.attn.qkv.weight` (×27 blocks) | `[3456, 1152]` | `torch.bfloat16` | 205.03 MB | model-00001-of-00096.safetensors |
| `model.visual.blocks.0-26.mlp.linear_fc1.bias` (×27 blocks) | `[4304]` | `torch.bfloat16` | 226.97 KB | model-00001-of-00096.safetensors |
| `model.visual.blocks.0-26.mlp.linear_fc1.weight` (×27 blocks) | `[4304, 1152]` | `torch.bfloat16` | 255.34 MB | model-00001-of-00096.safetensors |
| `model.visual.blocks.0-26.mlp.linear_fc2.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00001-of-00096.safetensors |
| `model.visual.blocks.0-26.mlp.linear_fc2.weight` (×27 blocks) | `[1152, 4304]` | `torch.bfloat16` | 255.34 MB | model-00001-of-00096.safetensors |
| `model.visual.blocks.0-26.norm1.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00001-of-00096.safetensors |
| `model.visual.blocks.0-26.norm1.weight` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00001-of-00096.safetensors |
| `model.visual.blocks.0-26.norm2.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00001-of-00096.safetensors |
| `model.visual.blocks.0-26.norm2.weight` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00001-of-00096.safetensors |
| `model.visual.deepstack_merger_list.0-2.linear_fc1.bias` (×3 deepstack_merger_list) | `[4608]` | `torch.bfloat16` | 27.00 KB | model-00001-of-00096.safetensors |
| `model.visual.deepstack_merger_list.0-2.linear_fc1.weight` (×3 deepstack_merger_list) | `[4608, 4608]` | `torch.bfloat16` | 121.50 MB | model-00001-of-00096.safetensors |
| `model.visual.deepstack_merger_list.0-2.linear_fc2.bias` (×3 deepstack_merger_list) | `[4096]` | `torch.bfloat16` | 24.00 KB | model-00001-of-00096.safetensors |
| `model.visual.deepstack_merger_list.0-2.linear_fc2.weight` (×3 deepstack_merger_list) | `[4096, 4608]` | `torch.bfloat16` | 108.00 MB | model-00001-of-00096.safetensors |
| `model.visual.deepstack_merger_list.0-2.norm.bias` (×3 deepstack_merger_list) | `[4608]` | `torch.bfloat16` | 27.00 KB | model-00001-of-00096.safetensors |
| `model.visual.deepstack_merger_list.0-2.norm.weight` (×3 deepstack_merger_list) | `[4608]` | `torch.bfloat16` | 27.00 KB | model-00001-of-00096.safetensors |
| `model.visual.merger.linear_fc1.bias` | `[4608]` | `torch.bfloat16` | 9.00 KB | model-00001-of-00096.safetensors |
| `model.visual.merger.linear_fc1.weight` | `[4608, 4608]` | `torch.bfloat16` | 40.50 MB | model-00001-of-00096.safetensors |
| `model.visual.merger.linear_fc2.bias` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00001-of-00096.safetensors |
| `model.visual.merger.linear_fc2.weight` | `[4096, 4608]` | `torch.bfloat16` | 36.00 MB | model-00001-of-00096.safetensors |
| `model.visual.merger.norm.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00096.safetensors |
| `model.visual.merger.norm.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00096.safetensors |
| `model.visual.patch_embed.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00001-of-00096.safetensors |
| `model.visual.patch_embed.proj.weight` | `[1152, 3, 2, 16, 16]` | `torch.bfloat16` | 3.38 MB | model-00001-of-00096.safetensors |
| `model.visual.pos_embed.weight` | `[2304, 1152]` | `torch.bfloat16` | 5.06 MB | model-00001-of-00096.safetensors |

</details>

