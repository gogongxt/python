# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Llama-3.2-3B-Instruct`

# 模型配置

- **模型类型**: `LlamaConfig`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 3072
- **层数**: 28
- **注意力头数**: 24
- **词表大小**: 128256
- **中间层大小**: 8192

<details><summary>完整配置</summary>

```
LlamaConfig {
  "architectures": [
    "LlamaForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 128000,
  "dtype": "bfloat16",
  "eos_token_id": [
    128001,
    128008,
    128009
  ],
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 3072,
  "initializer_range": 0.02,
  "intermediate_size": 8192,
  "max_position_embeddings": 131072,
  "mlp_bias": false,
  "model_type": "llama",
  "num_attention_heads": 24,
  "num_hidden_layers": 28,
  "num_key_value_heads": 8,
  "pad_token_id": null,
  "pretraining_tp": 1,
  "rms_norm_eps": 1e-05,
  "rope_parameters": {
    "factor": 32.0,
    "high_freq_factor": 4.0,
    "low_freq_factor": 1.0,
    "original_max_position_embeddings": 8192,
    "rope_theta": 500000.0,
    "rope_type": "llama3"
  },
  "tie_word_embeddings": true,
  "transformers_version": "5.7.0",
  "use_cache": true,
  "vocab_size": 128256
}

```

</details>

# 模型结构

**模型类**: `LlamaModel`

```
LlamaModel(
  (embed_tokens): Embedding(128256, 3072)
  (layers): ModuleList(
    (0-27): 28 x LlamaDecoderLayer(
      (self_attn): LlamaAttention(
        (q_proj): Linear(in_features=3072, out_features=3072, bias=False)
        (k_proj): Linear(in_features=3072, out_features=1024, bias=False)
        (v_proj): Linear(in_features=3072, out_features=1024, bias=False)
        (o_proj): Linear(in_features=3072, out_features=3072, bias=False)
      )
      (mlp): LlamaMLP(
        (gate_proj): Linear(in_features=3072, out_features=8192, bias=False)
        (up_proj): Linear(in_features=3072, out_features=8192, bias=False)
        (down_proj): Linear(in_features=8192, out_features=3072, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): LlamaRMSNorm((3072,), eps=1e-05)
      (post_attention_layernorm): LlamaRMSNorm((3072,), eps=1e-05)
    )
  )
  (norm): LlamaRMSNorm((3072,), eps=1e-05)
  (rotary_emb): LlamaRotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 2 个 `safetensors` 文件
- **文件总大小**: 5.98 GB
- **权重张量数**: 254
- **参数总量**: 3,212,749,824
- **张量累计大小**: 5.98 GB
- **压缩**: 254 → 11 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `model.embed_tokens.weight` | `[128256, 3072]` | `torch.bfloat16` | 751.50 MB | model-00001-of-00002.safetensors |
| `model.layers.0-27.input_layernorm.weight` (×28 layers) | `[3072]` | `torch.bfloat16` | 168.00 KB | Multi Files |
| `model.layers.0-27.mlp.down_proj.weight` (×28 layers) | `[3072, 8192]` | `torch.bfloat16` | 1.31 GB | Multi Files |
| `model.layers.0-27.mlp.gate_proj.weight` (×28 layers) | `[8192, 3072]` | `torch.bfloat16` | 1.31 GB | Multi Files |
| `model.layers.0-27.mlp.up_proj.weight` (×28 layers) | `[8192, 3072]` | `torch.bfloat16` | 1.31 GB | Multi Files |
| `model.layers.0-27.post_attention_layernorm.weight` (×28 layers) | `[3072]` | `torch.bfloat16` | 168.00 KB | Multi Files |
| `model.layers.0-27.self_attn.k_proj.weight` (×28 layers) | `[1024, 3072]` | `torch.bfloat16` | 168.00 MB | Multi Files |
| `model.layers.0-27.self_attn.o_proj.weight` (×28 layers) | `[3072, 3072]` | `torch.bfloat16` | 504.00 MB | Multi Files |
| `model.layers.0-27.self_attn.q_proj.weight` (×28 layers) | `[3072, 3072]` | `torch.bfloat16` | 504.00 MB | Multi Files |
| `model.layers.0-27.self_attn.v_proj.weight` (×28 layers) | `[1024, 3072]` | `torch.bfloat16` | 168.00 MB | Multi Files |
| `model.norm.weight` | `[3072]` | `torch.bfloat16` | 6.00 KB | model-00002-of-00002.safetensors |

</details>

