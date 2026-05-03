# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/user/gogongxt/models/llama-2-7b`

# 模型配置

- **模型类型**: `LlamaConfig`
- **数据类型**: `torch.float16`
- **隐藏层大小**: 4096
- **层数**: 32
- **注意力头数**: 32
- **词表大小**: 32000
- **中间层大小**: 11008

<details><summary>完整配置</summary>

```
LlamaConfig {
  "architectures": [
    "LlamaForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 1,
  "dtype": "float16",
  "eos_token_id": 2,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 11008,
  "max_position_embeddings": 4096,
  "mlp_bias": false,
  "model_type": "llama",
  "num_attention_heads": 32,
  "num_hidden_layers": 32,
  "num_key_value_heads": 32,
  "pad_token_id": null,
  "pretraining_tp": 1,
  "rms_norm_eps": 1e-05,
  "rope_parameters": {
    "rope_theta": 10000.0,
    "rope_type": "default"
  },
  "tie_word_embeddings": false,
  "transformers_version": "5.7.0",
  "use_cache": true,
  "vocab_size": 32000
}

```

</details>

# 模型结构

**模型类**: `LlamaModel`

```
LlamaModel(
  (embed_tokens): Embedding(32000, 4096)
  (layers): ModuleList(
    (0-31): 32 x LlamaDecoderLayer(
      (self_attn): LlamaAttention(
        (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
        (k_proj): Linear(in_features=4096, out_features=4096, bias=False)
        (v_proj): Linear(in_features=4096, out_features=4096, bias=False)
        (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
      )
      (mlp): LlamaMLP(
        (gate_proj): Linear(in_features=4096, out_features=11008, bias=False)
        (up_proj): Linear(in_features=4096, out_features=11008, bias=False)
        (down_proj): Linear(in_features=11008, out_features=4096, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): LlamaRMSNorm((4096,), eps=1e-05)
      (post_attention_layernorm): LlamaRMSNorm((4096,), eps=1e-05)
    )
  )
  (norm): LlamaRMSNorm((4096,), eps=1e-05)
  (rotary_emb): LlamaRotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 2 个 `safetensors` 文件
- **文件总大小**: 12.55 GB
- **权重张量数**: 323
- **参数总量**: 6,738,417,664
- **张量累计大小**: 12.55 GB
- **压缩**: 323 → 13 行 (合并相同 shape/dtype 的 experts 和 layers)

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[32000, 4096]` | `torch.float16` | 250.00 MB | model-00002-of-00002.safetensors |
| `model.embed_tokens.weight` | `[32000, 4096]` | `torch.float16` | 250.00 MB | model-00001-of-00002.safetensors |
| `model.layers.0-31.input_layernorm.weight` (×32 layers) | `[4096]` | `torch.float16` | 256.00 KB | Multi Files |
| `model.layers.0-31.mlp.down_proj.weight` (×32 layers) | `[4096, 11008]` | `torch.float16` | 2.69 GB | Multi Files |
| `model.layers.0-31.mlp.gate_proj.weight` (×32 layers) | `[11008, 4096]` | `torch.float16` | 2.69 GB | Multi Files |
| `model.layers.0-31.mlp.up_proj.weight` (×32 layers) | `[11008, 4096]` | `torch.float16` | 2.69 GB | Multi Files |
| `model.layers.0-31.post_attention_layernorm.weight` (×32 layers) | `[4096]` | `torch.float16` | 256.00 KB | Multi Files |
| `model.layers.0-31.self_attn.k_proj.weight` (×32 layers) | `[4096, 4096]` | `torch.float16` | 1.00 GB | Multi Files |
| `model.layers.0-31.self_attn.o_proj.weight` (×32 layers) | `[4096, 4096]` | `torch.float16` | 1.00 GB | Multi Files |
| `model.layers.0-31.self_attn.q_proj.weight` (×32 layers) | `[4096, 4096]` | `torch.float16` | 1.00 GB | Multi Files |
| `model.layers.0-31.self_attn.rotary_emb.inv_freq` (×32 layers) | `[64]` | `torch.float32` | 8.00 KB | Multi Files |
| `model.layers.0-31.self_attn.v_proj.weight` (×32 layers) | `[4096, 4096]` | `torch.float16` | 1.00 GB | Multi Files |
| `model.norm.weight` | `[4096]` | `torch.float16` | 8.00 KB | model-00002-of-00002.safetensors |

</details>

