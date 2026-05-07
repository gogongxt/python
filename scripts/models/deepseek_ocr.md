# 模型信息报告

- **模型路径**: `/nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-OCR`

# 模型配置

- **错误**: 读取模型配置失败 - `The repository /nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-OCR contains custom code which must be executed to correctly load the model. You can inspect the repository content at /nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-OCR .
 You can inspect the repository content at https://hf.co//nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-OCR.
Please pass the argument `trust_remote_code=True` to allow custom code to be run.`

<details><summary>原始 config.json</summary>

`/nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-OCR/config.json`

```json

{
 "_name_or_path": "deepseek-ai/DeepSeek-OCR",
  "candidate_resolutions": [
  [
   1024,
   1024
  ]
 ],
 "global_view_pos": "head",
  "architectures": [
      "DeepseekOCRForCausalLM"
    ],
  "auto_map": {
    "AutoConfig": "modeling_deepseekocr.DeepseekOCRConfig",
    "AutoModel": "modeling_deepseekocr.DeepseekOCRForCausalLM"
  },
 "language_config": {
    "architectures": [
      "DeepseekV2ForCausalLM"
    ],
    "auto_map": {
      "AutoConfig": "configuration_deepseekv2.DeepseekV2Config",
      "AutoModel": "modeling_deepseek.DeepseekV2Model",
      "AutoModelForCausalLM": "modeling_deepseek.DeepseekV2ForCausalLM"
    },
    "bos_token_id": 0,
    "eos_token_id": 1,
    "first_k_dense_replace": 1,
    "hidden_size": 1280,
    "intermediate_size": 6848,
    "kv_lora_rank": null,
    "lm_head": true,
    "max_position_embeddings": 8192,
    "moe_intermediate_size": 896,
    "n_group": 1,
    "n_routed_experts": 64,
    "n_shared_experts": 2,
    "num_attention_heads": 10,
    "num_experts_per_tok": 6,
    "num_hidden_layers": 12,
    "num_key_value_heads": 10,
    "q_lora_rank": null,
    "qk_nope_head_dim": 0,
    "qk_rope_head_dim": 0,
    "rm_head": false,
    "topk_group": 1,
    "topk_method": "greedy",
    "torch_dtype": "bfloat16",
    "use_mla": false,
    "v_head_dim": 0,
    "vocab_size": 129280
  },
 "model_type": "deepseek_vl_v2",
 "projector_config": {
  "input_dim": 2048,
  "model_type": "mlp_projector",
  "n_embed": 1280,
  "projector_type": "linear"
 },
 "tile_tag": "2D",
 "torch_dtype": "bfloat16",
 "transformers_version": "4.46.3",
 "vision_config": {
  "image_size": 1024,
  "mlp_ratio": 3.7362,
  "model_name": "deeplip_b_l",
  "model_type": "vision",
  "width": {
   "clip-l-14-224": {
    "heads": 16,
    "image_size": 224,
    "layers": 24,
    "patch_size": 14,
    "width": 1024
   },
   "sam_vit_b": {
    "downsample_channels": [
     512,
     1024
    ],
    "global_attn_indexes": [
     2,
     5,
     8,
     11
    ],
    "heads": 12,
    "layers": 12,
    "width": 768
   }
  }
 },
  "bos_token_id": 0,
  "eos_token_id": 1,
  "first_k_dense_replace": 1,
  "hidden_size": 1280,
  "intermediate_size": 6848,
  "kv_lora_rank": null,
  "lm_head": true,
  "max_position_embeddings": 8192,
  "moe_intermediate_size": 896,
  "n_group": 1,
  "n_routed_experts": 64,
  "n_shared_experts": 2,
  "num_attention_heads": 10,
  "num_experts_per_tok": 6,
  "num_hidden_layers": 12,
  "num_key_value_heads": 10,
  "q_lora_rank": null,
  "qk_nope_head_dim": 0,
  "qk_rope_head_dim": 0,
  "rm_head": false,
  "topk_group": 1,
  "topk_method": "greedy",
  "use_mla": false,
  "v_head_dim": 0,
  "vocab_size": 129280
}
```
</details>

# 模型结构

**错误**: 解析模型结构失败 - `The repository /nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-OCR contains custom code which must be executed to correctly load the model. You can inspect the repository content at /nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-OCR .
 You can inspect the repository content at https://hf.co//nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-OCR.
Please pass the argument `trust_remote_code=True` to allow custom code to be run.`

# 权重统计

- **权重文件**: 1 个 `safetensors` 文件
- **文件总大小**: 6.21 GB
- **权重张量数**: 2,710
- **参数总量**: 3,336,106,240
- **张量累计大小**: 6.21 GB
- **压缩**: 2710 → 86 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[129280, 1280]` | `torch.bfloat16` | 315.62 MB | model-00001-of-000001.safetensors |
| `model.embed_tokens.weight` | `[129280, 1280]` | `torch.bfloat16` | 315.62 MB | model-00001-of-000001.safetensors |
| `model.image_newline` | `[1280]` | `torch.bfloat16` | 2.50 KB | model-00001-of-000001.safetensors |
| `model.layers.0-11.input_layernorm.weight` (×12 layers) | `[1280]` | `torch.bfloat16` | 30.00 KB | model-00001-of-000001.safetensors |
| `model.layers.0-11.post_attention_layernorm.weight` (×12 layers) | `[1280]` | `torch.bfloat16` | 30.00 KB | model-00001-of-000001.safetensors |
| `model.layers.0-11.self_attn.k_proj.weight` (×12 layers) | `[1280, 1280]` | `torch.bfloat16` | 37.50 MB | model-00001-of-000001.safetensors |
| `model.layers.0-11.self_attn.o_proj.weight` (×12 layers) | `[1280, 1280]` | `torch.bfloat16` | 37.50 MB | model-00001-of-000001.safetensors |
| `model.layers.0-11.self_attn.q_proj.weight` (×12 layers) | `[1280, 1280]` | `torch.bfloat16` | 37.50 MB | model-00001-of-000001.safetensors |
| `model.layers.0-11.self_attn.v_proj.weight` (×12 layers) | `[1280, 1280]` | `torch.bfloat16` | 37.50 MB | model-00001-of-000001.safetensors |
| `model.layers.0.mlp.down_proj.weight` (×1 layers) | `[1280, 6848]` | `torch.bfloat16` | 16.72 MB | model-00001-of-000001.safetensors |
| `model.layers.0.mlp.gate_proj.weight` (×1 layers) | `[6848, 1280]` | `torch.bfloat16` | 16.72 MB | model-00001-of-000001.safetensors |
| `model.layers.0.mlp.up_proj.weight` (×1 layers) | `[6848, 1280]` | `torch.bfloat16` | 16.72 MB | model-00001-of-000001.safetensors |
| `model.layers.1-11.mlp.experts.0-63.down_proj.weight` (×11 layers, ×64 experts) | `[1280, 896]` | `torch.bfloat16` | 1.50 GB | model-00001-of-000001.safetensors |
| `model.layers.1-11.mlp.experts.0-63.gate_proj.weight` (×11 layers, ×64 experts) | `[896, 1280]` | `torch.bfloat16` | 1.50 GB | model-00001-of-000001.safetensors |
| `model.layers.1-11.mlp.experts.0-63.up_proj.weight` (×11 layers, ×64 experts) | `[896, 1280]` | `torch.bfloat16` | 1.50 GB | model-00001-of-000001.safetensors |
| `model.layers.1-11.mlp.gate.weight` (×11 layers) | `[64, 1280]` | `torch.bfloat16` | 1.72 MB | model-00001-of-000001.safetensors |
| `model.layers.1-11.mlp.shared_experts.down_proj.weight` (×11 layers) | `[1280, 1792]` | `torch.bfloat16` | 48.12 MB | model-00001-of-000001.safetensors |
| `model.layers.1-11.mlp.shared_experts.gate_proj.weight` (×11 layers) | `[1792, 1280]` | `torch.bfloat16` | 48.12 MB | model-00001-of-000001.safetensors |
| `model.layers.1-11.mlp.shared_experts.up_proj.weight` (×11 layers) | `[1792, 1280]` | `torch.bfloat16` | 48.12 MB | model-00001-of-000001.safetensors |
| `model.norm.weight` | `[1280]` | `torch.bfloat16` | 2.50 KB | model-00001-of-000001.safetensors |
| `model.projector.layers.bias` | `[1280]` | `torch.bfloat16` | 2.50 KB | model-00001-of-000001.safetensors |
| `model.projector.layers.weight` | `[1280, 2048]` | `torch.bfloat16` | 5.00 MB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0-11.attn.proj.bias` (×12 blocks) | `[768]` | `torch.bfloat16` | 18.00 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0-11.attn.proj.weight` (×12 blocks) | `[768, 768]` | `torch.bfloat16` | 13.50 MB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0-11.attn.qkv.bias` (×12 blocks) | `[2304]` | `torch.bfloat16` | 54.00 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0-11.attn.qkv.weight` (×12 blocks) | `[2304, 768]` | `torch.bfloat16` | 40.50 MB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0-11.mlp.lin1.bias` (×12 blocks) | `[3072]` | `torch.bfloat16` | 72.00 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0-11.mlp.lin1.weight` (×12 blocks) | `[3072, 768]` | `torch.bfloat16` | 54.00 MB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0-11.mlp.lin2.bias` (×12 blocks) | `[768]` | `torch.bfloat16` | 18.00 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0-11.mlp.lin2.weight` (×12 blocks) | `[768, 3072]` | `torch.bfloat16` | 54.00 MB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0-11.norm1.bias` (×12 blocks) | `[768]` | `torch.bfloat16` | 18.00 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0-11.norm1.weight` (×12 blocks) | `[768]` | `torch.bfloat16` | 18.00 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0-11.norm2.bias` (×12 blocks) | `[768]` | `torch.bfloat16` | 18.00 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0-11.norm2.weight` (×12 blocks) | `[768]` | `torch.bfloat16` | 18.00 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0.attn.rel_pos_h` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.0.attn.rel_pos_w` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.1.attn.rel_pos_h` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.1.attn.rel_pos_w` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.2.attn.rel_pos_h` | `[127, 64]` | `torch.bfloat16` | 15.88 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.2.attn.rel_pos_w` | `[127, 64]` | `torch.bfloat16` | 15.88 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.3.attn.rel_pos_h` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.3.attn.rel_pos_w` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.4.attn.rel_pos_h` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.4.attn.rel_pos_w` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.5.attn.rel_pos_h` | `[127, 64]` | `torch.bfloat16` | 15.88 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.5.attn.rel_pos_w` | `[127, 64]` | `torch.bfloat16` | 15.88 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.6.attn.rel_pos_h` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.6.attn.rel_pos_w` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.7.attn.rel_pos_h` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.7.attn.rel_pos_w` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.8.attn.rel_pos_h` | `[127, 64]` | `torch.bfloat16` | 15.88 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.8.attn.rel_pos_w` | `[127, 64]` | `torch.bfloat16` | 15.88 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.9.attn.rel_pos_h` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.9.attn.rel_pos_w` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.10.attn.rel_pos_h` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.10.attn.rel_pos_w` | `[27, 64]` | `torch.bfloat16` | 3.38 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.11.attn.rel_pos_h` | `[127, 64]` | `torch.bfloat16` | 15.88 KB | model-00001-of-000001.safetensors |
| `model.sam_model.blocks.11.attn.rel_pos_w` | `[127, 64]` | `torch.bfloat16` | 15.88 KB | model-00001-of-000001.safetensors |
| `model.sam_model.neck.0.weight` | `[256, 768, 1, 1]` | `torch.bfloat16` | 384.00 KB | model-00001-of-000001.safetensors |
| `model.sam_model.neck.1-3.bias` (×2 neck) | `[256]` | `torch.bfloat16` | 1.00 KB | model-00001-of-000001.safetensors |
| `model.sam_model.neck.1.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-000001.safetensors |
| `model.sam_model.neck.2.weight` | `[256, 256, 3, 3]` | `torch.bfloat16` | 1.12 MB | model-00001-of-000001.safetensors |
| `model.sam_model.neck.3.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00001-of-000001.safetensors |
| `model.sam_model.net_2.weight` | `[512, 256, 3, 3]` | `torch.bfloat16` | 2.25 MB | model-00001-of-000001.safetensors |
| `model.sam_model.net_3.weight` | `[1024, 512, 3, 3]` | `torch.bfloat16` | 9.00 MB | model-00001-of-000001.safetensors |
| `model.sam_model.patch_embed.proj.bias` | `[768]` | `torch.bfloat16` | 1.50 KB | model-00001-of-000001.safetensors |
| `model.sam_model.patch_embed.proj.weight` | `[768, 3, 16, 16]` | `torch.bfloat16` | 1.12 MB | model-00001-of-000001.safetensors |
| `model.sam_model.pos_embed` | `[1, 64, 64, 768]` | `torch.bfloat16` | 6.00 MB | model-00001-of-000001.safetensors |
| `model.view_seperator` | `[1280]` | `torch.bfloat16` | 2.50 KB | model-00001-of-000001.safetensors |
| `model.vision_model.embeddings.class_embedding` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00001-of-000001.safetensors |
| `model.vision_model.embeddings.patch_embedding.weight` | `[1024, 3, 14, 14]` | `torch.bfloat16` | 1.15 MB | model-00001-of-000001.safetensors |
| `model.vision_model.embeddings.position_embedding.weight` | `[257, 1024]` | `torch.bfloat16` | 514.00 KB | model-00001-of-000001.safetensors |
| `model.vision_model.pre_layrnorm.bias` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00001-of-000001.safetensors |
| `model.vision_model.pre_layrnorm.weight` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00001-of-000001.safetensors |
| `model.vision_model.transformer.layers.0-23.layer_norm1.bias` (×24 layers) | `[1024]` | `torch.bfloat16` | 48.00 KB | model-00001-of-000001.safetensors |
| `model.vision_model.transformer.layers.0-23.layer_norm1.weight` (×24 layers) | `[1024]` | `torch.bfloat16` | 48.00 KB | model-00001-of-000001.safetensors |
| `model.vision_model.transformer.layers.0-23.layer_norm2.bias` (×24 layers) | `[1024]` | `torch.bfloat16` | 48.00 KB | model-00001-of-000001.safetensors |
| `model.vision_model.transformer.layers.0-23.layer_norm2.weight` (×24 layers) | `[1024]` | `torch.bfloat16` | 48.00 KB | model-00001-of-000001.safetensors |
| `model.vision_model.transformer.layers.0-23.mlp.fc1.bias` (×24 layers) | `[4096]` | `torch.bfloat16` | 192.00 KB | model-00001-of-000001.safetensors |
| `model.vision_model.transformer.layers.0-23.mlp.fc1.weight` (×24 layers) | `[4096, 1024]` | `torch.bfloat16` | 192.00 MB | model-00001-of-000001.safetensors |
| `model.vision_model.transformer.layers.0-23.mlp.fc2.bias` (×24 layers) | `[1024]` | `torch.bfloat16` | 48.00 KB | model-00001-of-000001.safetensors |
| `model.vision_model.transformer.layers.0-23.mlp.fc2.weight` (×24 layers) | `[1024, 4096]` | `torch.bfloat16` | 192.00 MB | model-00001-of-000001.safetensors |
| `model.vision_model.transformer.layers.0-23.self_attn.out_proj.bias` (×24 layers) | `[1024]` | `torch.bfloat16` | 48.00 KB | model-00001-of-000001.safetensors |
| `model.vision_model.transformer.layers.0-23.self_attn.out_proj.weight` (×24 layers) | `[1024, 1024]` | `torch.bfloat16` | 48.00 MB | model-00001-of-000001.safetensors |
| `model.vision_model.transformer.layers.0-23.self_attn.qkv_proj.bias` (×24 layers) | `[3072]` | `torch.bfloat16` | 144.00 KB | model-00001-of-000001.safetensors |
| `model.vision_model.transformer.layers.0-23.self_attn.qkv_proj.weight` (×24 layers) | `[3072, 1024]` | `torch.bfloat16` | 144.00 MB | model-00001-of-000001.safetensors |

</details>

