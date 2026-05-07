# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen3-14B`

# 模型配置

- **模型类型**: `Qwen3Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 5120
- **层数**: 40
- **注意力头数**: 40
- **词表大小**: 151936
- **中间层大小**: 17408

<details><summary>完整配置</summary>

```
Qwen3Config {
  "architectures": [
    "Qwen3ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "dtype": "bfloat16",
  "eos_token_id": 151645,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 5120,
  "initializer_range": 0.02,
  "intermediate_size": 17408,
  "layer_types": [
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention",
    "full_attention"
  ],
  "max_position_embeddings": 40960,
  "max_window_layers": 40,
  "model_type": "qwen3",
  "num_attention_heads": 40,
  "num_hidden_layers": 40,
  "num_key_value_heads": 8,
  "pad_token_id": null,
  "rms_norm_eps": 1e-06,
  "rope_parameters": {
    "rope_theta": 1000000,
    "rope_type": "default"
  },
  "sliding_window": null,
  "tie_word_embeddings": false,
  "transformers_version": "5.7.0",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 151936
}

```

</details>

# 模型结构

**模型类**: `Qwen3Model`

```
Qwen3Model(
  (embed_tokens): Embedding(151936, 5120)
  (layers): ModuleList(
    (0-39): 40 x Qwen3DecoderLayer(
      (self_attn): Qwen3Attention(
        (q_proj): Linear(in_features=5120, out_features=5120, bias=False)
        (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
        (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
        (o_proj): Linear(in_features=5120, out_features=5120, bias=False)
        (q_norm): Qwen3RMSNorm((128,), eps=1e-06)
        (k_norm): Qwen3RMSNorm((128,), eps=1e-06)
      )
      (mlp): Qwen3MLP(
        (gate_proj): Linear(in_features=5120, out_features=17408, bias=False)
        (up_proj): Linear(in_features=5120, out_features=17408, bias=False)
        (down_proj): Linear(in_features=17408, out_features=5120, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): Qwen3RMSNorm((5120,), eps=1e-06)
      (post_attention_layernorm): Qwen3RMSNorm((5120,), eps=1e-06)
    )
  )
  (norm): Qwen3RMSNorm((5120,), eps=1e-06)
  (rotary_emb): Qwen3RotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 8 个 `safetensors` 文件
- **文件总大小**: 27.51 GB
- **权重张量数**: 443
- **参数总量**: 14,768,307,200
- **张量累计大小**: 27.51 GB
- **压缩**: 443 → 14 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[151936, 5120]` | `torch.bfloat16` | 1.45 GB | model-00008-of-00008.safetensors |
| `model.embed_tokens.weight` | `[151936, 5120]` | `torch.bfloat16` | 1.45 GB | model-00001-of-00008.safetensors |
| `model.layers.0-39.input_layernorm.weight` (×40 layers) | `[5120]` | `torch.bfloat16` | 400.00 KB | Multi Files |
| `model.layers.0-39.mlp.down_proj.weight` (×40 layers) | `[5120, 17408]` | `torch.bfloat16` | 6.64 GB | Multi Files |
| `model.layers.0-39.mlp.gate_proj.weight` (×40 layers) | `[17408, 5120]` | `torch.bfloat16` | 6.64 GB | Multi Files |
| `model.layers.0-39.mlp.up_proj.weight` (×40 layers) | `[17408, 5120]` | `torch.bfloat16` | 6.64 GB | Multi Files |
| `model.layers.0-39.post_attention_layernorm.weight` (×40 layers) | `[5120]` | `torch.bfloat16` | 400.00 KB | Multi Files |
| `model.layers.0-39.self_attn.k_norm.weight` (×40 layers) | `[128]` | `torch.bfloat16` | 10.00 KB | Multi Files |
| `model.layers.0-39.self_attn.k_proj.weight` (×40 layers) | `[1024, 5120]` | `torch.bfloat16` | 400.00 MB | Multi Files |
| `model.layers.0-39.self_attn.o_proj.weight` (×40 layers) | `[5120, 5120]` | `torch.bfloat16` | 1.95 GB | Multi Files |
| `model.layers.0-39.self_attn.q_norm.weight` (×40 layers) | `[128]` | `torch.bfloat16` | 10.00 KB | Multi Files |
| `model.layers.0-39.self_attn.q_proj.weight` (×40 layers) | `[5120, 5120]` | `torch.bfloat16` | 1.95 GB | Multi Files |
| `model.layers.0-39.self_attn.v_proj.weight` (×40 layers) | `[1024, 5120]` | `torch.bfloat16` | 400.00 MB | Multi Files |
| `model.norm.weight` | `[5120]` | `torch.bfloat16` | 10.00 KB | model-00008-of-00008.safetensors |

</details>

