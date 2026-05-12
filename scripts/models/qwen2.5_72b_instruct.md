# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen2.5-72B-Instruct`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/Qwen2.5-72B-Instruct/config.json`

```json

{
  "architectures": [
    "Qwen2ForCausalLM"
  ],
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "eos_token_id": 151645,
  "hidden_act": "silu",
  "hidden_size": 8192,
  "initializer_range": 0.02,
  "intermediate_size": 29568,
  "max_position_embeddings": 32768,
  "max_window_layers": 70,
  "model_type": "qwen2",
  "num_attention_heads": 64,
  "num_hidden_layers": 80,
  "num_key_value_heads": 8,
  "rms_norm_eps": 1e-06,
  "rope_theta": 1000000.0,
  "sliding_window": 131072,
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
- **隐藏层大小**: 8192
- **层数**: 80
- **注意力头数**: 64
- **词表大小**: 152064
- **中间层大小**: 29568

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
  "hidden_size": 8192,
  "initializer_range": 0.02,
  "intermediate_size": 29568,
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
  "num_attention_heads": 64,
  "num_hidden_layers": 80,
  "num_key_value_heads": 8,
  "pad_token_id": null,
  "rms_norm_eps": 1e-06,
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
  (embed_tokens): Embedding(152064, 8192)
  (layers): ModuleList(
    (0-79): 80 x Qwen2DecoderLayer(
      (self_attn): Qwen2Attention(
        (q_proj): Linear(in_features=8192, out_features=8192, bias=True)
        (k_proj): Linear(in_features=8192, out_features=1024, bias=True)
        (v_proj): Linear(in_features=8192, out_features=1024, bias=True)
        (o_proj): Linear(in_features=8192, out_features=8192, bias=False)
      )
      (mlp): Qwen2MLP(
        (gate_proj): Linear(in_features=8192, out_features=29568, bias=False)
        (up_proj): Linear(in_features=8192, out_features=29568, bias=False)
        (down_proj): Linear(in_features=29568, out_features=8192, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): Qwen2RMSNorm((8192,), eps=1e-06)
      (post_attention_layernorm): Qwen2RMSNorm((8192,), eps=1e-06)
    )
  )
  (norm): Qwen2RMSNorm((8192,), eps=1e-06)
  (rotary_emb): Qwen2RotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 37 个 `safetensors` 文件
- **文件总大小**: 135.43 GB
- **权重张量数**: 963
- **参数总量**: 72,706,203,648
- **张量累计大小**: 135.43 GB
- **压缩**: 963 → 15 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[152064, 8192]` | `torch.bfloat16` | 2.32 GB | model-00037-of-00037.safetensors |
| `model.embed_tokens.weight` | `[152064, 8192]` | `torch.bfloat16` | 2.32 GB | model-00001-of-00037.safetensors |
| `model.layers.0-79.input_layernorm.weight` (×80 layers) | `[8192]` | `torch.bfloat16` | 1.25 MB | Multi Files |
| `model.layers.0-79.mlp.down_proj.weight` (×80 layers) | `[8192, 29568]` | `torch.bfloat16` | 36.09 GB | Multi Files |
| `model.layers.0-79.mlp.gate_proj.weight` (×80 layers) | `[29568, 8192]` | `torch.bfloat16` | 36.09 GB | Multi Files |
| `model.layers.0-79.mlp.up_proj.weight` (×80 layers) | `[29568, 8192]` | `torch.bfloat16` | 36.09 GB | Multi Files |
| `model.layers.0-79.post_attention_layernorm.weight` (×80 layers) | `[8192]` | `torch.bfloat16` | 1.25 MB | Multi Files |
| `model.layers.0-79.self_attn.k_proj.bias` (×80 layers) | `[1024]` | `torch.bfloat16` | 160.00 KB | Multi Files |
| `model.layers.0-79.self_attn.k_proj.weight` (×80 layers) | `[1024, 8192]` | `torch.bfloat16` | 1.25 GB | Multi Files |
| `model.layers.0-79.self_attn.o_proj.weight` (×80 layers) | `[8192, 8192]` | `torch.bfloat16` | 10.00 GB | Multi Files |
| `model.layers.0-79.self_attn.q_proj.bias` (×80 layers) | `[8192]` | `torch.bfloat16` | 1.25 MB | Multi Files |
| `model.layers.0-79.self_attn.q_proj.weight` (×80 layers) | `[8192, 8192]` | `torch.bfloat16` | 10.00 GB | Multi Files |
| `model.layers.0-79.self_attn.v_proj.bias` (×80 layers) | `[1024]` | `torch.bfloat16` | 160.00 KB | Multi Files |
| `model.layers.0-79.self_attn.v_proj.weight` (×80 layers) | `[1024, 8192]` | `torch.bfloat16` | 1.25 GB | Multi Files |
| `model.norm.weight` | `[8192]` | `torch.bfloat16` | 16.00 KB | model-00037-of-00037.safetensors |

</details>

