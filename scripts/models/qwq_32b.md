# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/QwQ-32B`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/QwQ-32B/config.json`

```json

{
  "architectures": [
    "Qwen2ForCausalLM"
  ],
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "eos_token_id": 151645,
  "hidden_act": "silu",
  "hidden_size": 5120,
  "initializer_range": 0.02,
  "intermediate_size": 27648,
  "max_position_embeddings": 131072,
  "max_window_layers": 64,
  "model_type": "qwen2",
  "num_attention_heads": 40,
  "num_hidden_layers": 64,
  "num_key_value_heads": 8,
  "rms_norm_eps": 1e-05,
  "rope_theta": 1000000.0,
  "sliding_window": 32768,
  "tie_word_embeddings": false,
  "torch_dtype": "bfloat16",
  "transformers_version": "4.43.1",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 152064
}

```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `Qwen2Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 5120
- **层数**: 64
- **注意力头数**: 40
- **词表大小**: 152064
- **中间层大小**: 27648

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
  "hidden_size": 5120,
  "initializer_range": 0.02,
  "intermediate_size": 27648,
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
  "max_position_embeddings": 131072,
  "max_window_layers": 64,
  "model_type": "qwen2",
  "num_attention_heads": 40,
  "num_hidden_layers": 64,
  "num_key_value_heads": 8,
  "pad_token_id": null,
  "rms_norm_eps": 1e-05,
  "rope_parameters": {
    "rope_theta": 1000000.0,
    "rope_type": "default"
  },
  "sliding_window": null,
  "tie_word_embeddings": false,
  "transformers_version": "5.7.0",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 152064
}

```

</details>

# 模型结构

**模型类**: `Qwen2Model`

```
Qwen2Model(
  (embed_tokens): Embedding(152064, 5120)
  (layers): ModuleList(
    (0-63): 64 x Qwen2DecoderLayer(
      (self_attn): Qwen2Attention(
        (q_proj): Linear(in_features=5120, out_features=5120, bias=True)
        (k_proj): Linear(in_features=5120, out_features=1024, bias=True)
        (v_proj): Linear(in_features=5120, out_features=1024, bias=True)
        (o_proj): Linear(in_features=5120, out_features=5120, bias=False)
      )
      (mlp): Qwen2MLP(
        (gate_proj): Linear(in_features=5120, out_features=27648, bias=False)
        (up_proj): Linear(in_features=5120, out_features=27648, bias=False)
        (down_proj): Linear(in_features=27648, out_features=5120, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): Qwen2RMSNorm((5120,), eps=1e-05)
      (post_attention_layernorm): Qwen2RMSNorm((5120,), eps=1e-05)
    )
  )
  (norm): Qwen2RMSNorm((5120,), eps=1e-05)
  (rotary_emb): Qwen2RotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 14 个 `safetensors` 文件
- **文件总大小**: 61.03 GB
- **权重张量数**: 771
- **参数总量**: 32,763,876,352
- **张量累计大小**: 61.03 GB
- **压缩**: 771 → 15 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[152064, 5120]` | `torch.bfloat16` | 1.45 GB | model-00014-of-00014.safetensors |
| `model.embed_tokens.weight` | `[152064, 5120]` | `torch.bfloat16` | 1.45 GB | model-00001-of-00014.safetensors |
| `model.layers.0-63.input_layernorm.weight` (×64 layers) | `[5120]` | `torch.bfloat16` | 640.00 KB | Multi Files |
| `model.layers.0-63.mlp.down_proj.weight` (×64 layers) | `[5120, 27648]` | `torch.bfloat16` | 16.88 GB | Multi Files |
| `model.layers.0-63.mlp.gate_proj.weight` (×64 layers) | `[27648, 5120]` | `torch.bfloat16` | 16.88 GB | Multi Files |
| `model.layers.0-63.mlp.up_proj.weight` (×64 layers) | `[27648, 5120]` | `torch.bfloat16` | 16.88 GB | Multi Files |
| `model.layers.0-63.post_attention_layernorm.weight` (×64 layers) | `[5120]` | `torch.bfloat16` | 640.00 KB | Multi Files |
| `model.layers.0-63.self_attn.k_proj.bias` (×64 layers) | `[1024]` | `torch.bfloat16` | 128.00 KB | Multi Files |
| `model.layers.0-63.self_attn.k_proj.weight` (×64 layers) | `[1024, 5120]` | `torch.bfloat16` | 640.00 MB | Multi Files |
| `model.layers.0-63.self_attn.o_proj.weight` (×64 layers) | `[5120, 5120]` | `torch.bfloat16` | 3.12 GB | Multi Files |
| `model.layers.0-63.self_attn.q_proj.bias` (×64 layers) | `[5120]` | `torch.bfloat16` | 640.00 KB | Multi Files |
| `model.layers.0-63.self_attn.q_proj.weight` (×64 layers) | `[5120, 5120]` | `torch.bfloat16` | 3.12 GB | Multi Files |
| `model.layers.0-63.self_attn.v_proj.bias` (×64 layers) | `[1024]` | `torch.bfloat16` | 128.00 KB | Multi Files |
| `model.layers.0-63.self_attn.v_proj.weight` (×64 layers) | `[1024, 5120]` | `torch.bfloat16` | 640.00 MB | Multi Files |
| `model.norm.weight` | `[5120]` | `torch.bfloat16` | 10.00 KB | model-00014-of-00014.safetensors |

</details>

