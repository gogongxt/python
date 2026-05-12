# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen3-0.6B`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/Qwen3-0.6B/config.json`

```json

{
  "architectures": [
    "Qwen3ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "eos_token_id": 151645,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": 3072,
  "max_position_embeddings": 40960,
  "max_window_layers": 28,
  "model_type": "qwen3",
  "num_attention_heads": 16,
  "num_hidden_layers": 28,
  "num_key_value_heads": 8,
  "rms_norm_eps": 1e-06,
  "rope_scaling": null,
  "rope_theta": 1000000,
  "sliding_window": null,
  "tie_word_embeddings": true,
  "torch_dtype": "bfloat16",
  "transformers_version": "4.51.0",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 151936
}

```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `Qwen3Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 1024
- **层数**: 28
- **注意力头数**: 16
- **词表大小**: 151936
- **中间层大小**: 3072

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
  "hidden_size": 1024,
  "initializer_range": 0.02,
  "intermediate_size": 3072,
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
  "max_position_embeddings": 40960,
  "max_window_layers": 28,
  "model_type": "qwen3",
  "num_attention_heads": 16,
  "num_hidden_layers": 28,
  "num_key_value_heads": 8,
  "pad_token_id": null,
  "rms_norm_eps": 1e-06,
  "rope_parameters": {
    "rope_theta": 1000000,
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

**模型类**: `Qwen3Model`

```
Qwen3Model(
  (embed_tokens): Embedding(151936, 1024)
  (layers): ModuleList(
    (0-27): 28 x Qwen3DecoderLayer(
      (self_attn): Qwen3Attention(
        (q_proj): Linear(in_features=1024, out_features=2048, bias=False)
        (k_proj): Linear(in_features=1024, out_features=1024, bias=False)
        (v_proj): Linear(in_features=1024, out_features=1024, bias=False)
        (o_proj): Linear(in_features=2048, out_features=1024, bias=False)
        (q_norm): Qwen3RMSNorm((128,), eps=1e-06)
        (k_norm): Qwen3RMSNorm((128,), eps=1e-06)
      )
      (mlp): Qwen3MLP(
        (gate_proj): Linear(in_features=1024, out_features=3072, bias=False)
        (up_proj): Linear(in_features=1024, out_features=3072, bias=False)
        (down_proj): Linear(in_features=3072, out_features=1024, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): Qwen3RMSNorm((1024,), eps=1e-06)
      (post_attention_layernorm): Qwen3RMSNorm((1024,), eps=1e-06)
    )
  )
  (norm): Qwen3RMSNorm((1024,), eps=1e-06)
  (rotary_emb): Qwen3RotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 1 个 `safetensors` 文件
- **文件总大小**: 1.40 GB
- **权重张量数**: 311
- **参数总量**: 751,632,384
- **张量累计大小**: 1.40 GB
- **压缩**: 311 → 14 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[151936, 1024]` | `torch.bfloat16` | 296.75 MB | model.safetensors |
| `model.embed_tokens.weight` | `[151936, 1024]` | `torch.bfloat16` | 296.75 MB | model.safetensors |
| `model.layers.0-27.input_layernorm.weight` (×28 layers) | `[1024]` | `torch.bfloat16` | 56.00 KB | model.safetensors |
| `model.layers.0-27.mlp.down_proj.weight` (×28 layers) | `[1024, 3072]` | `torch.bfloat16` | 168.00 MB | model.safetensors |
| `model.layers.0-27.mlp.gate_proj.weight` (×28 layers) | `[3072, 1024]` | `torch.bfloat16` | 168.00 MB | model.safetensors |
| `model.layers.0-27.mlp.up_proj.weight` (×28 layers) | `[3072, 1024]` | `torch.bfloat16` | 168.00 MB | model.safetensors |
| `model.layers.0-27.post_attention_layernorm.weight` (×28 layers) | `[1024]` | `torch.bfloat16` | 56.00 KB | model.safetensors |
| `model.layers.0-27.self_attn.k_norm.weight` (×28 layers) | `[128]` | `torch.bfloat16` | 7.00 KB | model.safetensors |
| `model.layers.0-27.self_attn.k_proj.weight` (×28 layers) | `[1024, 1024]` | `torch.bfloat16` | 56.00 MB | model.safetensors |
| `model.layers.0-27.self_attn.o_proj.weight` (×28 layers) | `[1024, 2048]` | `torch.bfloat16` | 112.00 MB | model.safetensors |
| `model.layers.0-27.self_attn.q_norm.weight` (×28 layers) | `[128]` | `torch.bfloat16` | 7.00 KB | model.safetensors |
| `model.layers.0-27.self_attn.q_proj.weight` (×28 layers) | `[2048, 1024]` | `torch.bfloat16` | 112.00 MB | model.safetensors |
| `model.layers.0-27.self_attn.v_proj.weight` (×28 layers) | `[1024, 1024]` | `torch.bfloat16` | 56.00 MB | model.safetensors |
| `model.norm.weight` | `[1024]` | `torch.bfloat16` | 2.00 KB | model.safetensors |

</details>

