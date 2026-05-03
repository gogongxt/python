# 模型信息报告

- **模型路径**: `/nfs/volume-1615-2/models/Qwen3-32B`

# 模型配置

- **模型类型**: `Qwen3Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 5120
- **层数**: 64
- **注意力头数**: 64
- **词表大小**: 151936
- **中间层大小**: 25600

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
  "intermediate_size": 25600,
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
  "max_window_layers": 64,
  "model_type": "qwen3",
  "num_attention_heads": 64,
  "num_hidden_layers": 64,
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
  (embed_tokens): Embedding(151936, 5120)
  (layers): ModuleList(
    (0-63): 64 x Qwen3DecoderLayer(
      (self_attn): Qwen3Attention(
        (q_proj): Linear(in_features=5120, out_features=8192, bias=False)
        (k_proj): Linear(in_features=5120, out_features=1024, bias=False)
        (v_proj): Linear(in_features=5120, out_features=1024, bias=False)
        (o_proj): Linear(in_features=8192, out_features=5120, bias=False)
        (q_norm): Qwen3RMSNorm((128,), eps=1e-06)
        (k_norm): Qwen3RMSNorm((128,), eps=1e-06)
      )
      (mlp): Qwen3MLP(
        (gate_proj): Linear(in_features=5120, out_features=25600, bias=False)
        (up_proj): Linear(in_features=5120, out_features=25600, bias=False)
        (down_proj): Linear(in_features=25600, out_features=5120, bias=False)
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

- **权重文件**: 17 个 `safetensors` 文件
- **文件总大小**: 61.02 GB
- **权重张量数**: 707
- **参数总量**: 32,762,123,264
- **张量累计大小**: 61.02 GB
- **压缩**: 707 → 14 行 (合并相同 shape/dtype 的 experts 和 layers)

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[151936, 5120]` | `torch.bfloat16` | 1.45 GB | model-00017-of-00017.safetensors |
| `model.embed_tokens.weight` | `[151936, 5120]` | `torch.bfloat16` | 1.45 GB | model-00001-of-00017.safetensors |
| `model.layers.0-63.input_layernorm.weight` (×64 layers) | `[5120]` | `torch.bfloat16` | 640.00 KB | Multi Files |
| `model.layers.0-63.mlp.down_proj.weight` (×64 layers) | `[5120, 25600]` | `torch.bfloat16` | 15.62 GB | Multi Files |
| `model.layers.0-63.mlp.gate_proj.weight` (×64 layers) | `[25600, 5120]` | `torch.bfloat16` | 15.62 GB | Multi Files |
| `model.layers.0-63.mlp.up_proj.weight` (×64 layers) | `[25600, 5120]` | `torch.bfloat16` | 15.62 GB | Multi Files |
| `model.layers.0-63.post_attention_layernorm.weight` (×64 layers) | `[5120]` | `torch.bfloat16` | 640.00 KB | Multi Files |
| `model.layers.0-63.self_attn.k_norm.weight` (×64 layers) | `[128]` | `torch.bfloat16` | 16.00 KB | Multi Files |
| `model.layers.0-63.self_attn.k_proj.weight` (×64 layers) | `[1024, 5120]` | `torch.bfloat16` | 640.00 MB | Multi Files |
| `model.layers.0-63.self_attn.o_proj.weight` (×64 layers) | `[5120, 8192]` | `torch.bfloat16` | 5.00 GB | Multi Files |
| `model.layers.0-63.self_attn.q_norm.weight` (×64 layers) | `[128]` | `torch.bfloat16` | 16.00 KB | Multi Files |
| `model.layers.0-63.self_attn.q_proj.weight` (×64 layers) | `[8192, 5120]` | `torch.bfloat16` | 5.00 GB | Multi Files |
| `model.layers.0-63.self_attn.v_proj.weight` (×64 layers) | `[1024, 5120]` | `torch.bfloat16` | 640.00 MB | Multi Files |
| `model.norm.weight` | `[5120]` | `torch.bfloat16` | 10.00 KB | model-00017-of-00017.safetensors |

</details>

