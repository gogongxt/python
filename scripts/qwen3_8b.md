# 模型信息报告

- **模型路径**: `/nfs/volume-1615-2/models/Qwen3-8B/`

# 模型配置

- **模型类型**: `Qwen3Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 4096
- **层数**: 36
- **注意力头数**: 32
- **词表大小**: 151936
- **中间层大小**: 12288

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
  "hidden_size": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 12288,
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
    "full_attention"
  ],
  "max_position_embeddings": 40960,
  "max_window_layers": 36,
  "model_type": "qwen3",
  "num_attention_heads": 32,
  "num_hidden_layers": 36,
  "num_key_value_heads": 8,
  "rms_norm_eps": 1e-06,
  "rope_scaling": null,
  "rope_theta": 1000000,
  "sliding_window": null,
  "tie_word_embeddings": false,
  "transformers_version": "4.57.1",
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
  (embed_tokens): Embedding(151936, 4096)
  (layers): ModuleList(
    (0-35): 36 x Qwen3DecoderLayer(
      (self_attn): Qwen3Attention(
        (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
        (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
        (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
        (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
        (q_norm): Qwen3RMSNorm((128,), eps=1e-06)
        (k_norm): Qwen3RMSNorm((128,), eps=1e-06)
      )
      (mlp): Qwen3MLP(
        (gate_proj): Linear(in_features=4096, out_features=12288, bias=False)
        (up_proj): Linear(in_features=4096, out_features=12288, bias=False)
        (down_proj): Linear(in_features=12288, out_features=4096, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): Qwen3RMSNorm((4096,), eps=1e-06)
      (post_attention_layernorm): Qwen3RMSNorm((4096,), eps=1e-06)
    )
  )
  (norm): Qwen3RMSNorm((4096,), eps=1e-06)
  (rotary_emb): Qwen3RotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 5 个 `safetensors` 文件
- **文件总大小**: 15.26 GB
- **权重张量数**: 399
- **参数总量**: 8,190,735,360
- **张量累计大小**: 15.26 GB
- **压缩**: 399 → 14 行 (合并相同 shape/dtype 的 experts 和 layers)

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[151936, 4096]` | `torch.bfloat16` | 1.16 GB | model-00005-of-00005.safetensors |
| `model.embed_tokens.weight` | `[151936, 4096]` | `torch.bfloat16` | 1.16 GB | model-00001-of-00005.safetensors |
| `model.layers.0-35.input_layernorm.weight` (×36 layers) | `[4096]` | `torch.bfloat16` | 288.00 KB | Multi Files |
| `model.layers.0-35.mlp.down_proj.weight` (×36 layers) | `[4096, 12288]` | `torch.bfloat16` | 3.38 GB | Multi Files |
| `model.layers.0-35.mlp.gate_proj.weight` (×36 layers) | `[12288, 4096]` | `torch.bfloat16` | 3.38 GB | Multi Files |
| `model.layers.0-35.mlp.up_proj.weight` (×36 layers) | `[12288, 4096]` | `torch.bfloat16` | 3.38 GB | Multi Files |
| `model.layers.0-35.post_attention_layernorm.weight` (×36 layers) | `[4096]` | `torch.bfloat16` | 288.00 KB | Multi Files |
| `model.layers.0-35.self_attn.k_norm.weight` (×36 layers) | `[128]` | `torch.bfloat16` | 9.00 KB | Multi Files |
| `model.layers.0-35.self_attn.k_proj.weight` (×36 layers) | `[1024, 4096]` | `torch.bfloat16` | 288.00 MB | Multi Files |
| `model.layers.0-35.self_attn.o_proj.weight` (×36 layers) | `[4096, 4096]` | `torch.bfloat16` | 1.12 GB | Multi Files |
| `model.layers.0-35.self_attn.q_norm.weight` (×36 layers) | `[128]` | `torch.bfloat16` | 9.00 KB | Multi Files |
| `model.layers.0-35.self_attn.q_proj.weight` (×36 layers) | `[4096, 4096]` | `torch.bfloat16` | 1.12 GB | Multi Files |
| `model.layers.0-35.self_attn.v_proj.weight` (×36 layers) | `[1024, 4096]` | `torch.bfloat16` | 288.00 MB | Multi Files |
| `model.norm.weight` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00004-of-00005.safetensors |

</details>

