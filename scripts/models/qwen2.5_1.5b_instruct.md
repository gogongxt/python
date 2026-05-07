# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen2.5-1.5B-Instruct`

# 模型配置

- **模型类型**: `Qwen2Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 1536
- **层数**: 28
- **注意力头数**: 12
- **词表大小**: 151936
- **中间层大小**: 8960

<details><summary>完整配置</summary>

```
Qwen2Config {
  "architectures": [
    "Qwen2ForCausalLM"
  ],
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "dtype": "bfloat16",
  "eos_token_id": 151645,
  "hidden_act": "silu",
  "hidden_size": 1536,
  "initializer_range": 0.02,
  "intermediate_size": 8960,
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
    "full_attention"
  ],
  "max_position_embeddings": 32768,
  "max_window_layers": 21,
  "model_type": "qwen2",
  "num_attention_heads": 12,
  "num_hidden_layers": 28,
  "num_key_value_heads": 2,
  "pad_token_id": null,
  "rms_norm_eps": 1e-06,
  "rope_parameters": {
    "rope_theta": 1000000.0,
    "rope_type": "default"
  },
  "sliding_window": null,
  "tie_word_embeddings": true,
  "transformers_version": "5.7.0",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 151936
}

```

</details>

# 模型结构

**模型类**: `Qwen2Model`

```
Qwen2Model(
  (embed_tokens): Embedding(151936, 1536)
  (layers): ModuleList(
    (0-27): 28 x Qwen2DecoderLayer(
      (self_attn): Qwen2Attention(
        (q_proj): Linear(in_features=1536, out_features=1536, bias=True)
        (k_proj): Linear(in_features=1536, out_features=256, bias=True)
        (v_proj): Linear(in_features=1536, out_features=256, bias=True)
        (o_proj): Linear(in_features=1536, out_features=1536, bias=False)
      )
      (mlp): Qwen2MLP(
        (gate_proj): Linear(in_features=1536, out_features=8960, bias=False)
        (up_proj): Linear(in_features=1536, out_features=8960, bias=False)
        (down_proj): Linear(in_features=8960, out_features=1536, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): Qwen2RMSNorm((1536,), eps=1e-06)
      (post_attention_layernorm): Qwen2RMSNorm((1536,), eps=1e-06)
    )
  )
  (norm): Qwen2RMSNorm((1536,), eps=1e-06)
  (rotary_emb): Qwen2RotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 1 个 `safetensors` 文件
- **文件总大小**: 2.88 GB
- **权重张量数**: 338
- **参数总量**: 1,543,714,304
- **张量累计大小**: 2.88 GB
- **压缩**: 338 → 14 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `model.embed_tokens.weight` | `[151936, 1536]` | `torch.bfloat16` | 445.12 MB | model.safetensors |
| `model.layers.0-27.input_layernorm.weight` (×28 layers) | `[1536]` | `torch.bfloat16` | 84.00 KB | model.safetensors |
| `model.layers.0-27.mlp.down_proj.weight` (×28 layers) | `[1536, 8960]` | `torch.bfloat16` | 735.00 MB | model.safetensors |
| `model.layers.0-27.mlp.gate_proj.weight` (×28 layers) | `[8960, 1536]` | `torch.bfloat16` | 735.00 MB | model.safetensors |
| `model.layers.0-27.mlp.up_proj.weight` (×28 layers) | `[8960, 1536]` | `torch.bfloat16` | 735.00 MB | model.safetensors |
| `model.layers.0-27.post_attention_layernorm.weight` (×28 layers) | `[1536]` | `torch.bfloat16` | 84.00 KB | model.safetensors |
| `model.layers.0-27.self_attn.k_proj.bias` (×28 layers) | `[256]` | `torch.bfloat16` | 14.00 KB | model.safetensors |
| `model.layers.0-27.self_attn.k_proj.weight` (×28 layers) | `[256, 1536]` | `torch.bfloat16` | 21.00 MB | model.safetensors |
| `model.layers.0-27.self_attn.o_proj.weight` (×28 layers) | `[1536, 1536]` | `torch.bfloat16` | 126.00 MB | model.safetensors |
| `model.layers.0-27.self_attn.q_proj.bias` (×28 layers) | `[1536]` | `torch.bfloat16` | 84.00 KB | model.safetensors |
| `model.layers.0-27.self_attn.q_proj.weight` (×28 layers) | `[1536, 1536]` | `torch.bfloat16` | 126.00 MB | model.safetensors |
| `model.layers.0-27.self_attn.v_proj.bias` (×28 layers) | `[256]` | `torch.bfloat16` | 14.00 KB | model.safetensors |
| `model.layers.0-27.self_attn.v_proj.weight` (×28 layers) | `[256, 1536]` | `torch.bfloat16` | 21.00 MB | model.safetensors |
| `model.norm.weight` | `[1536]` | `torch.bfloat16` | 3.00 KB | model.safetensors |

</details>

