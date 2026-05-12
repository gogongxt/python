# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen2.5-0.5B`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/Qwen2.5-0.5B/config.json`

```json

{
  "architectures": [
    "Qwen2ForCausalLM"
  ],
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "eos_token_id": 151643,
  "hidden_act": "silu",
  "hidden_size": 896,
  "initializer_range": 0.02,
  "intermediate_size": 4864,
  "max_position_embeddings": 32768,
  "max_window_layers": 24,
  "model_type": "qwen2",
  "num_attention_heads": 14,
  "num_hidden_layers": 24,
  "num_key_value_heads": 2,
  "rms_norm_eps": 1e-06,
  "rope_theta": 1000000.0,
  "sliding_window": 32768,
  "tie_word_embeddings": true,
  "torch_dtype": "bfloat16",
  "transformers_version": "4.40.1",
  "use_cache": true,
  "use_mrope": false,
  "use_sliding_window": false,
  "vocab_size": 151936
}

```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `Qwen2Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 896
- **层数**: 24
- **注意力头数**: 14
- **词表大小**: 151936
- **中间层大小**: 4864

```
Qwen2Config {
  "architectures": [
    "Qwen2ForCausalLM"
  ],
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "dtype": "bfloat16",
  "eos_token_id": 151643,
  "hidden_act": "silu",
  "hidden_size": 896,
  "initializer_range": 0.02,
  "intermediate_size": 4864,
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
    "full_attention"
  ],
  "max_position_embeddings": 32768,
  "max_window_layers": 24,
  "model_type": "qwen2",
  "num_attention_heads": 14,
  "num_hidden_layers": 24,
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
  "use_mrope": false,
  "use_sliding_window": false,
  "vocab_size": 151936
}

```

</details>

# 模型结构

**模型类**: `Qwen2Model`

```
Qwen2Model(
  (embed_tokens): Embedding(151936, 896)
  (layers): ModuleList(
    (0-23): 24 x Qwen2DecoderLayer(
      (self_attn): Qwen2Attention(
        (q_proj): Linear(in_features=896, out_features=896, bias=True)
        (k_proj): Linear(in_features=896, out_features=128, bias=True)
        (v_proj): Linear(in_features=896, out_features=128, bias=True)
        (o_proj): Linear(in_features=896, out_features=896, bias=False)
      )
      (mlp): Qwen2MLP(
        (gate_proj): Linear(in_features=896, out_features=4864, bias=False)
        (up_proj): Linear(in_features=896, out_features=4864, bias=False)
        (down_proj): Linear(in_features=4864, out_features=896, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): Qwen2RMSNorm((896,), eps=1e-06)
      (post_attention_layernorm): Qwen2RMSNorm((896,), eps=1e-06)
    )
  )
  (norm): Qwen2RMSNorm((896,), eps=1e-06)
  (rotary_emb): Qwen2RotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 1 个 `safetensors` 文件
- **文件总大小**: 942.32 MB
- **权重张量数**: 290
- **参数总量**: 494,032,768
- **张量累计大小**: 942.29 MB
- **压缩**: 290 → 14 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `model.embed_tokens.weight` | `[151936, 896]` | `torch.bfloat16` | 259.66 MB | model.safetensors |
| `model.layers.0-23.input_layernorm.weight` (×24 layers) | `[896]` | `torch.bfloat16` | 42.00 KB | model.safetensors |
| `model.layers.0-23.mlp.down_proj.weight` (×24 layers) | `[896, 4864]` | `torch.bfloat16` | 199.50 MB | model.safetensors |
| `model.layers.0-23.mlp.gate_proj.weight` (×24 layers) | `[4864, 896]` | `torch.bfloat16` | 199.50 MB | model.safetensors |
| `model.layers.0-23.mlp.up_proj.weight` (×24 layers) | `[4864, 896]` | `torch.bfloat16` | 199.50 MB | model.safetensors |
| `model.layers.0-23.post_attention_layernorm.weight` (×24 layers) | `[896]` | `torch.bfloat16` | 42.00 KB | model.safetensors |
| `model.layers.0-23.self_attn.k_proj.bias` (×24 layers) | `[128]` | `torch.bfloat16` | 6.00 KB | model.safetensors |
| `model.layers.0-23.self_attn.k_proj.weight` (×24 layers) | `[128, 896]` | `torch.bfloat16` | 5.25 MB | model.safetensors |
| `model.layers.0-23.self_attn.o_proj.weight` (×24 layers) | `[896, 896]` | `torch.bfloat16` | 36.75 MB | model.safetensors |
| `model.layers.0-23.self_attn.q_proj.bias` (×24 layers) | `[896]` | `torch.bfloat16` | 42.00 KB | model.safetensors |
| `model.layers.0-23.self_attn.q_proj.weight` (×24 layers) | `[896, 896]` | `torch.bfloat16` | 36.75 MB | model.safetensors |
| `model.layers.0-23.self_attn.v_proj.bias` (×24 layers) | `[128]` | `torch.bfloat16` | 6.00 KB | model.safetensors |
| `model.layers.0-23.self_attn.v_proj.weight` (×24 layers) | `[128, 896]` | `torch.bfloat16` | 5.25 MB | model.safetensors |
| `model.norm.weight` | `[896]` | `torch.bfloat16` | 1.75 KB | model.safetensors |

</details>

