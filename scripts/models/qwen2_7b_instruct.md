# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen2-7B-Instruct`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/Qwen2-7B-Instruct/config.json`

```json

{
  "architectures": [
    "Qwen2ForCausalLM"
  ],
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "eos_token_id": 151645,
  "hidden_act": "silu",
  "hidden_size": 3584,
  "initializer_range": 0.02,
  "intermediate_size": 18944,
  "max_position_embeddings": 32768,
  "max_window_layers": 28,
  "model_type": "qwen2",
  "num_attention_heads": 28,
  "num_hidden_layers": 28,
  "num_key_value_heads": 4,
  "rms_norm_eps": 1e-06,
  "rope_theta": 1000000.0,
  "sliding_window": 131072,
  "tie_word_embeddings": false,
  "torch_dtype": "bfloat16",
  "transformers_version": "4.41.2",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 152064
}

```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `Qwen2Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 3584
- **层数**: 28
- **注意力头数**: 28
- **词表大小**: 152064
- **中间层大小**: 18944

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
  "hidden_size": 3584,
  "initializer_range": 0.02,
  "intermediate_size": 18944,
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
  "max_window_layers": 28,
  "model_type": "qwen2",
  "num_attention_heads": 28,
  "num_hidden_layers": 28,
  "num_key_value_heads": 4,
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
  (embed_tokens): Embedding(152064, 3584)
  (layers): ModuleList(
    (0-27): 28 x Qwen2DecoderLayer(
      (self_attn): Qwen2Attention(
        (q_proj): Linear(in_features=3584, out_features=3584, bias=True)
        (k_proj): Linear(in_features=3584, out_features=512, bias=True)
        (v_proj): Linear(in_features=3584, out_features=512, bias=True)
        (o_proj): Linear(in_features=3584, out_features=3584, bias=False)
      )
      (mlp): Qwen2MLP(
        (gate_proj): Linear(in_features=3584, out_features=18944, bias=False)
        (up_proj): Linear(in_features=3584, out_features=18944, bias=False)
        (down_proj): Linear(in_features=18944, out_features=3584, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): Qwen2RMSNorm((3584,), eps=1e-06)
      (post_attention_layernorm): Qwen2RMSNorm((3584,), eps=1e-06)
    )
  )
  (norm): Qwen2RMSNorm((3584,), eps=1e-06)
  (rotary_emb): Qwen2RotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 4 个 `safetensors` 文件
- **文件总大小**: 14.19 GB
- **权重张量数**: 339
- **参数总量**: 7,615,616,512
- **张量累计大小**: 14.19 GB
- **压缩**: 339 → 15 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[152064, 3584]` | `torch.bfloat16` | 1.02 GB | model-00004-of-00004.safetensors |
| `model.embed_tokens.weight` | `[152064, 3584]` | `torch.bfloat16` | 1.02 GB | model-00001-of-00004.safetensors |
| `model.layers.0-27.input_layernorm.weight` (×28 layers) | `[3584]` | `torch.bfloat16` | 196.00 KB | Multi Files |
| `model.layers.0-27.mlp.down_proj.weight` (×28 layers) | `[3584, 18944]` | `torch.bfloat16` | 3.54 GB | Multi Files |
| `model.layers.0-27.mlp.gate_proj.weight` (×28 layers) | `[18944, 3584]` | `torch.bfloat16` | 3.54 GB | Multi Files |
| `model.layers.0-27.mlp.up_proj.weight` (×28 layers) | `[18944, 3584]` | `torch.bfloat16` | 3.54 GB | Multi Files |
| `model.layers.0-27.post_attention_layernorm.weight` (×28 layers) | `[3584]` | `torch.bfloat16` | 196.00 KB | Multi Files |
| `model.layers.0-27.self_attn.k_proj.bias` (×28 layers) | `[512]` | `torch.bfloat16` | 28.00 KB | Multi Files |
| `model.layers.0-27.self_attn.k_proj.weight` (×28 layers) | `[512, 3584]` | `torch.bfloat16` | 98.00 MB | Multi Files |
| `model.layers.0-27.self_attn.o_proj.weight` (×28 layers) | `[3584, 3584]` | `torch.bfloat16` | 686.00 MB | Multi Files |
| `model.layers.0-27.self_attn.q_proj.bias` (×28 layers) | `[3584]` | `torch.bfloat16` | 196.00 KB | Multi Files |
| `model.layers.0-27.self_attn.q_proj.weight` (×28 layers) | `[3584, 3584]` | `torch.bfloat16` | 686.00 MB | Multi Files |
| `model.layers.0-27.self_attn.v_proj.bias` (×28 layers) | `[512]` | `torch.bfloat16` | 28.00 KB | Multi Files |
| `model.layers.0-27.self_attn.v_proj.weight` (×28 layers) | `[512, 3584]` | `torch.bfloat16` | 98.00 MB | Multi Files |
| `model.norm.weight` | `[3584]` | `torch.bfloat16` | 7.00 KB | model-00004-of-00004.safetensors |

</details>

