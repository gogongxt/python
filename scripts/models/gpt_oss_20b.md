# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/gpt-oss-20b`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/gpt-oss-20b/config.json`

```json

{
  "architectures": [
    "GptOssForCausalLM"
  ],
  "attention_bias": true,
  "attention_dropout": 0.0,
  "eos_token_id": 200002,
  "experts_per_token": 4,
  "head_dim": 64,
  "hidden_act": "silu",
  "hidden_size": 2880,
  "initial_context_length": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 2880,
  "layer_types": [
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention"
  ],
  "max_position_embeddings": 131072,
  "model_type": "gpt_oss",
  "num_attention_heads": 64,
  "num_experts_per_tok": 4,
  "num_hidden_layers": 24,
  "num_key_value_heads": 8,
  "num_local_experts": 32,
  "output_router_logits": false,
  "pad_token_id": 199999,
  "quantization_config": {
    "modules_to_not_convert": [
      "model.layers.*.self_attn",
      "model.layers.*.mlp.router",
      "model.embed_tokens",
      "lm_head"
    ],
    "quant_method": "mxfp4"
  },
  "rms_norm_eps": 1e-05,
  "rope_scaling": {
    "beta_fast": 32.0,
    "beta_slow": 1.0,
    "factor": 32.0,
    "original_max_position_embeddings": 4096,
    "rope_type": "yarn",
    "truncate": false
  },
  "rope_theta": 150000,
  "router_aux_loss_coef": 0.9,
  "sliding_window": 128,
  "swiglu_limit": 7.0,
  "tie_word_embeddings": false,
  "transformers_version": "4.55.0.dev0",
  "use_cache": true,
  "vocab_size": 201088
}

```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `GptOssConfig`
- **数据类型**: `None`
- **隐藏层大小**: 2880
- **层数**: 24
- **注意力头数**: 64
- **词表大小**: 201088
- **中间层大小**: 2880

```
GptOssConfig {
  "architectures": [
    "GptOssForCausalLM"
  ],
  "attention_bias": true,
  "attention_dropout": 0.0,
  "bos_token_id": null,
  "eos_token_id": 200002,
  "experts_per_token": 4,
  "head_dim": 64,
  "hidden_act": "silu",
  "hidden_size": 2880,
  "initial_context_length": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 2880,
  "layer_types": [
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention",
    "sliding_attention",
    "full_attention"
  ],
  "max_position_embeddings": 131072,
  "model_type": "gpt_oss",
  "num_attention_heads": 64,
  "num_experts_per_tok": 4,
  "num_hidden_layers": 24,
  "num_key_value_heads": 8,
  "num_local_experts": 32,
  "output_router_logits": false,
  "pad_token_id": 199999,
  "quantization_config": {
    "modules_to_not_convert": [
      "model.layers.*.self_attn",
      "model.layers.*.mlp.router",
      "model.embed_tokens",
      "lm_head"
    ],
    "quant_method": "mxfp4"
  },
  "rms_norm_eps": 1e-05,
  "rope_parameters": {
    "beta_fast": 32.0,
    "beta_slow": 1.0,
    "factor": 32.0,
    "original_max_position_embeddings": 4096,
    "rope_theta": 150000,
    "rope_type": "yarn",
    "truncate": false
  },
  "router_aux_loss_coef": 0.9,
  "sliding_window": 128,
  "swiglu_limit": 7.0,
  "tie_word_embeddings": false,
  "transformers_version": "5.7.0",
  "use_cache": true,
  "vocab_size": 201088
}

```

</details>

# 模型结构

**模型类**: `GptOssModel`

```
GptOssModel(
  (embed_tokens): Embedding(201088, 2880, padding_idx=199999)
  (layers): ModuleList(
    (0-23): 24 x GptOssDecoderLayer(
      (self_attn): GptOssAttention(
        (q_proj): Linear(in_features=2880, out_features=4096, bias=True)
        (k_proj): Linear(in_features=2880, out_features=512, bias=True)
        (v_proj): Linear(in_features=2880, out_features=512, bias=True)
        (o_proj): Linear(in_features=4096, out_features=2880, bias=True)
      )
      (mlp): GptOssMLP(
        (router): GptOssTopKRouter()
        (experts): GptOssExperts()
      )
      (input_layernorm): GptOssRMSNorm((2880,), eps=1e-05)
      (post_attention_layernorm): GptOssRMSNorm((2880,), eps=1e-05)
    )
  )
  (norm): GptOssRMSNorm((2880,), eps=1e-05)
  (rotary_emb): GptOssRotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 3 个 `safetensors` 文件
- **文件总大小**: 12.82 GB
- **权重张量数**: 459
- **参数总量**: 11,956,805,184
- **张量累计大小**: 12.82 GB
- **压缩**: 459 → 22 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[201088, 2880]` | `torch.bfloat16` | 1.08 GB | model-00002-of-00002.safetensors |
| `model.embed_tokens.weight` | `[201088, 2880]` | `torch.bfloat16` | 1.08 GB | model-00002-of-00002.safetensors |
| `model.layers.0-23.input_layernorm.weight` (×24 layers) | `[2880]` | `torch.bfloat16` | 135.00 KB | Multi Files |
| `model.layers.0-23.mlp.experts.down_proj_bias` (×24 layers) | `[32, 2880]` | `torch.bfloat16` | 4.22 MB | Multi Files |
| `model.layers.0-23.mlp.experts.down_proj_blocks` (×24 layers) | `[32, 2880, 90, 16]` | `torch.uint8` | 2.97 GB | Multi Files |
| `model.layers.0-23.mlp.experts.down_proj_scales` (×24 layers) | `[32, 2880, 90]` | `torch.uint8` | 189.84 MB | Multi Files |
| `model.layers.0-23.mlp.experts.gate_up_proj_bias` (×24 layers) | `[32, 5760]` | `torch.bfloat16` | 8.44 MB | Multi Files |
| `model.layers.0-23.mlp.experts.gate_up_proj_blocks` (×24 layers) | `[32, 5760, 90, 16]` | `torch.uint8` | 5.93 GB | Multi Files |
| `model.layers.0-23.mlp.experts.gate_up_proj_scales` (×24 layers) | `[32, 5760, 90]` | `torch.uint8` | 379.69 MB | Multi Files |
| `model.layers.0-23.mlp.router.bias` (×24 layers) | `[32]` | `torch.bfloat16` | 1.50 KB | Multi Files |
| `model.layers.0-23.mlp.router.weight` (×24 layers) | `[32, 2880]` | `torch.bfloat16` | 4.22 MB | Multi Files |
| `model.layers.0-23.post_attention_layernorm.weight` (×24 layers) | `[2880]` | `torch.bfloat16` | 135.00 KB | Multi Files |
| `model.layers.0-23.self_attn.k_proj.bias` (×24 layers) | `[512]` | `torch.bfloat16` | 24.00 KB | Multi Files |
| `model.layers.0-23.self_attn.k_proj.weight` (×24 layers) | `[512, 2880]` | `torch.bfloat16` | 67.50 MB | Multi Files |
| `model.layers.0-23.self_attn.o_proj.bias` (×24 layers) | `[2880]` | `torch.bfloat16` | 135.00 KB | Multi Files |
| `model.layers.0-23.self_attn.o_proj.weight` (×24 layers) | `[2880, 4096]` | `torch.bfloat16` | 540.00 MB | Multi Files |
| `model.layers.0-23.self_attn.q_proj.bias` (×24 layers) | `[4096]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `model.layers.0-23.self_attn.q_proj.weight` (×24 layers) | `[4096, 2880]` | `torch.bfloat16` | 540.00 MB | Multi Files |
| `model.layers.0-23.self_attn.sinks` (×24 layers) | `[64]` | `torch.bfloat16` | 3.00 KB | Multi Files |
| `model.layers.0-23.self_attn.v_proj.bias` (×24 layers) | `[512]` | `torch.bfloat16` | 24.00 KB | Multi Files |
| `model.layers.0-23.self_attn.v_proj.weight` (×24 layers) | `[512, 2880]` | `torch.bfloat16` | 67.50 MB | Multi Files |
| `model.norm.weight` | `[2880]` | `torch.bfloat16` | 5.62 KB | model-00002-of-00002.safetensors |

</details>

