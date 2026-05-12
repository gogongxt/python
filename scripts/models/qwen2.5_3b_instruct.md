# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen2.5-3B-Instruct`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/Qwen2.5-3B-Instruct/config.json`

```json

{
  "architectures": [
    "Qwen2ForCausalLM"
  ],
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "eos_token_id": 151645,
  "hidden_act": "silu",
  "hidden_size": 2048,
  "initializer_range": 0.02,
  "intermediate_size": 11008,
  "max_position_embeddings": 32768,
  "max_window_layers": 70,
  "model_type": "qwen2",
  "num_attention_heads": 16,
  "num_hidden_layers": 36,
  "num_key_value_heads": 2,
  "rms_norm_eps": 1e-06,
  "rope_theta": 1000000.0,
  "sliding_window": 32768,
  "tie_word_embeddings": true,
  "torch_dtype": "bfloat16",
  "transformers_version": "4.43.1",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 151936
}

```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `Qwen2Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 2048
- **层数**: 36
- **注意力头数**: 16
- **词表大小**: 151936
- **中间层大小**: 11008

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
  "hidden_size": 2048,
  "initializer_range": 0.02,
  "intermediate_size": 11008,
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
  "max_position_embeddings": 32768,
  "max_window_layers": 70,
  "model_type": "qwen2",
  "num_attention_heads": 16,
  "num_hidden_layers": 36,
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
  (embed_tokens): Embedding(151936, 2048)
  (layers): ModuleList(
    (0-35): 36 x Qwen2DecoderLayer(
      (self_attn): Qwen2Attention(
        (q_proj): Linear(in_features=2048, out_features=2048, bias=True)
        (k_proj): Linear(in_features=2048, out_features=256, bias=True)
        (v_proj): Linear(in_features=2048, out_features=256, bias=True)
        (o_proj): Linear(in_features=2048, out_features=2048, bias=False)
      )
      (mlp): Qwen2MLP(
        (gate_proj): Linear(in_features=2048, out_features=11008, bias=False)
        (up_proj): Linear(in_features=2048, out_features=11008, bias=False)
        (down_proj): Linear(in_features=11008, out_features=2048, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): Qwen2RMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen2RMSNorm((2048,), eps=1e-06)
    )
  )
  (norm): Qwen2RMSNorm((2048,), eps=1e-06)
  (rotary_emb): Qwen2RotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 2 个 `safetensors` 文件
- **文件总大小**: 5.75 GB
- **权重张量数**: 434
- **参数总量**: 3,085,938,688
- **张量累计大小**: 5.75 GB
- **压缩**: 434 → 14 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `model.embed_tokens.weight` | `[151936, 2048]` | `torch.bfloat16` | 593.50 MB | model-00001-of-00002.safetensors |
| `model.layers.0-35.input_layernorm.weight` (×36 layers) | `[2048]` | `torch.bfloat16` | 144.00 KB | Multi Files |
| `model.layers.0-35.mlp.down_proj.weight` (×36 layers) | `[2048, 11008]` | `torch.bfloat16` | 1.51 GB | Multi Files |
| `model.layers.0-35.mlp.gate_proj.weight` (×36 layers) | `[11008, 2048]` | `torch.bfloat16` | 1.51 GB | Multi Files |
| `model.layers.0-35.mlp.up_proj.weight` (×36 layers) | `[11008, 2048]` | `torch.bfloat16` | 1.51 GB | Multi Files |
| `model.layers.0-35.post_attention_layernorm.weight` (×36 layers) | `[2048]` | `torch.bfloat16` | 144.00 KB | Multi Files |
| `model.layers.0-35.self_attn.k_proj.bias` (×36 layers) | `[256]` | `torch.bfloat16` | 18.00 KB | Multi Files |
| `model.layers.0-35.self_attn.k_proj.weight` (×36 layers) | `[256, 2048]` | `torch.bfloat16` | 36.00 MB | Multi Files |
| `model.layers.0-35.self_attn.o_proj.weight` (×36 layers) | `[2048, 2048]` | `torch.bfloat16` | 288.00 MB | Multi Files |
| `model.layers.0-35.self_attn.q_proj.bias` (×36 layers) | `[2048]` | `torch.bfloat16` | 144.00 KB | Multi Files |
| `model.layers.0-35.self_attn.q_proj.weight` (×36 layers) | `[2048, 2048]` | `torch.bfloat16` | 288.00 MB | Multi Files |
| `model.layers.0-35.self_attn.v_proj.bias` (×36 layers) | `[256]` | `torch.bfloat16` | 18.00 KB | Multi Files |
| `model.layers.0-35.self_attn.v_proj.weight` (×36 layers) | `[256, 2048]` | `torch.bfloat16` | 36.00 MB | Multi Files |
| `model.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00002-of-00002.safetensors |

</details>

