# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Meta-Llama-3-8B-Instruct`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/Meta-Llama-3-8B-Instruct/config.json`

```json

{
  "architectures": [
    "LlamaForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 128000,
  "eos_token_id": 128001,
  "hidden_act": "silu",
  "hidden_size": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 14336,
  "max_position_embeddings": 8192,
  "model_type": "llama",
  "num_attention_heads": 32,
  "num_hidden_layers": 32,
  "num_key_value_heads": 8,
  "pretraining_tp": 1,
  "rms_norm_eps": 1e-05,
  "rope_scaling": null,
  "rope_theta": 500000.0,
  "tie_word_embeddings": false,
  "torch_dtype": "bfloat16",
  "transformers_version": "4.40.0.dev0",
  "use_cache": true,
  "vocab_size": 128256
}

```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `LlamaConfig`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 4096
- **层数**: 32
- **注意力头数**: 32
- **词表大小**: 128256
- **中间层大小**: 14336

```
LlamaConfig {
  "architectures": [
    "LlamaForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 128000,
  "dtype": "bfloat16",
  "eos_token_id": 128001,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 14336,
  "max_position_embeddings": 8192,
  "mlp_bias": false,
  "model_type": "llama",
  "num_attention_heads": 32,
  "num_hidden_layers": 32,
  "num_key_value_heads": 8,
  "pad_token_id": null,
  "pretraining_tp": 1,
  "rms_norm_eps": 1e-05,
  "rope_parameters": {
    "rope_theta": 500000.0,
    "rope_type": "default"
  },
  "tie_word_embeddings": false,
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
  (embed_tokens): Embedding(128256, 4096)
  (layers): ModuleList(
    (0-31): 32 x LlamaDecoderLayer(
      (self_attn): LlamaAttention(
        (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
        (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
        (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
        (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
      )
      (mlp): LlamaMLP(
        (gate_proj): Linear(in_features=4096, out_features=14336, bias=False)
        (up_proj): Linear(in_features=4096, out_features=14336, bias=False)
        (down_proj): Linear(in_features=14336, out_features=4096, bias=False)
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

- **权重文件**: 4 个 `safetensors` 文件
- **文件总大小**: 14.96 GB
- **权重张量数**: 291
- **参数总量**: 8,030,261,248
- **张量累计大小**: 14.96 GB
- **压缩**: 291 → 12 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[128256, 4096]` | `torch.bfloat16` | 1002.00 MB | model-00004-of-00004.safetensors |
| `model.embed_tokens.weight` | `[128256, 4096]` | `torch.bfloat16` | 1002.00 MB | model-00001-of-00004.safetensors |
| `model.layers.0-31.input_layernorm.weight` (×32 layers) | `[4096]` | `torch.bfloat16` | 256.00 KB | Multi Files |
| `model.layers.0-31.mlp.down_proj.weight` (×32 layers) | `[4096, 14336]` | `torch.bfloat16` | 3.50 GB | Multi Files |
| `model.layers.0-31.mlp.gate_proj.weight` (×32 layers) | `[14336, 4096]` | `torch.bfloat16` | 3.50 GB | Multi Files |
| `model.layers.0-31.mlp.up_proj.weight` (×32 layers) | `[14336, 4096]` | `torch.bfloat16` | 3.50 GB | Multi Files |
| `model.layers.0-31.post_attention_layernorm.weight` (×32 layers) | `[4096]` | `torch.bfloat16` | 256.00 KB | Multi Files |
| `model.layers.0-31.self_attn.k_proj.weight` (×32 layers) | `[1024, 4096]` | `torch.bfloat16` | 256.00 MB | Multi Files |
| `model.layers.0-31.self_attn.o_proj.weight` (×32 layers) | `[4096, 4096]` | `torch.bfloat16` | 1.00 GB | Multi Files |
| `model.layers.0-31.self_attn.q_proj.weight` (×32 layers) | `[4096, 4096]` | `torch.bfloat16` | 1.00 GB | Multi Files |
| `model.layers.0-31.self_attn.v_proj.weight` (×32 layers) | `[1024, 4096]` | `torch.bfloat16` | 256.00 MB | Multi Files |
| `model.norm.weight` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00004-of-00004.safetensors |

</details>

