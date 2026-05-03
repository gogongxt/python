# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/user/gogongxt/models/Qwen3-8B-FP8`

# 模型配置

- **模型类型**: `Qwen3Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 4096
- **层数**: 36
- **注意力头数**: 32
- **词表大小**: 151936
- **中间层大小**: 12288

<details><summary>完整配置</summary>

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
  "hidden_size": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 12288,
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
  "max_position_embeddings": 40960,
  "max_window_layers": 36,
  "model_type": "qwen3",
  "num_attention_heads": 32,
  "num_hidden_layers": 36,
  "num_key_value_heads": 8,
  "pad_token_id": null,
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "e4m3",
    "quant_method": "fp8",
    "weight_block_size": [
      128,
      128
    ]
  },
  "rms_norm_eps": 1e-06,
  "rope_parameters": {
    "rope_theta": 1000000,
    "rope_type": "default"
  },
  "sliding_window": null,
  "tie_word_embeddings": false,
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
  (embed_tokens): Embedding(151936, 4096)
  (layers): ModuleList(
    (0-35): 36 x Qwen3DecoderLayer(
      (self_attn): Qwen3Attention(
        (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
        (k_proj): Linear(in_features=4096, out_features=1024, bias=False)
        (v_proj): Linear(in_features=4096, out_features=1024, bias=False)
        (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
        (q_norm): Qwen3RMSNorm((128,), eps=1e-06)
        (k_norm): Qwen3RMSNorm((128,), eps=1e-06)
      )
      (mlp): Qwen3MLP(
        (gate_proj): Linear(in_features=4096, out_features=12288, bias=False)
        (up_proj): Linear(in_features=4096, out_features=12288, bias=False)
        (down_proj): Linear(in_features=12288, out_features=4096, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): Qwen3RMSNorm((4096,), eps=1e-06)
      (post_attention_layernorm): Qwen3RMSNorm((4096,), eps=1e-06)
    )
  )
  (norm): Qwen3RMSNorm((4096,), eps=1e-06)
  (rotary_emb): Qwen3RotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 2 个 `safetensors` 文件
- **文件总大小**: 8.79 GB
- **权重张量数**: 651
- **参数总量**: 8,191,159,296
- **张量累计大小**: 8.79 GB
- **压缩**: 651 → 21 行 (合并相同 shape/dtype 的 experts 和 layers)

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[151936, 4096]` | `torch.bfloat16` | 1.16 GB | model-00002-of-00002.safetensors |
| `model.embed_tokens.weight` | `[151936, 4096]` | `torch.bfloat16` | 1.16 GB | model-00001-of-00002.safetensors |
| `model.layers.0-35.input_layernorm.weight` (×36 layers) | `[4096]` | `torch.bfloat16` | 288.00 KB | Multi Files |
| `model.layers.0-35.mlp.down_proj.weight` (×36 layers) | `[4096, 12288]` | `torch.float8_e4m3fn` | 1.69 GB | Multi Files |
| `model.layers.0-35.mlp.down_proj.weight_scale_inv` (×36 layers) | `[32, 96]` | `torch.bfloat16` | 216.00 KB | Multi Files |
| `model.layers.0-35.mlp.gate_proj.weight` (×36 layers) | `[12288, 4096]` | `torch.float8_e4m3fn` | 1.69 GB | Multi Files |
| `model.layers.0-35.mlp.gate_proj.weight_scale_inv` (×36 layers) | `[96, 32]` | `torch.bfloat16` | 216.00 KB | Multi Files |
| `model.layers.0-35.mlp.up_proj.weight` (×36 layers) | `[12288, 4096]` | `torch.float8_e4m3fn` | 1.69 GB | Multi Files |
| `model.layers.0-35.mlp.up_proj.weight_scale_inv` (×36 layers) | `[96, 32]` | `torch.bfloat16` | 216.00 KB | Multi Files |
| `model.layers.0-35.post_attention_layernorm.weight` (×36 layers) | `[4096]` | `torch.bfloat16` | 288.00 KB | Multi Files |
| `model.layers.0-35.self_attn.k_norm.weight` (×36 layers) | `[128]` | `torch.bfloat16` | 9.00 KB | Multi Files |
| `model.layers.0-35.self_attn.k_proj.weight` (×36 layers) | `[1024, 4096]` | `torch.float8_e4m3fn` | 144.00 MB | Multi Files |
| `model.layers.0-35.self_attn.k_proj.weight_scale_inv` (×36 layers) | `[8, 32]` | `torch.bfloat16` | 18.00 KB | Multi Files |
| `model.layers.0-35.self_attn.o_proj.weight` (×36 layers) | `[4096, 4096]` | `torch.float8_e4m3fn` | 576.00 MB | Multi Files |
| `model.layers.0-35.self_attn.o_proj.weight_scale_inv` (×36 layers) | `[32, 32]` | `torch.bfloat16` | 72.00 KB | Multi Files |
| `model.layers.0-35.self_attn.q_norm.weight` (×36 layers) | `[128]` | `torch.bfloat16` | 9.00 KB | Multi Files |
| `model.layers.0-35.self_attn.q_proj.weight` (×36 layers) | `[4096, 4096]` | `torch.float8_e4m3fn` | 576.00 MB | Multi Files |
| `model.layers.0-35.self_attn.q_proj.weight_scale_inv` (×36 layers) | `[32, 32]` | `torch.bfloat16` | 72.00 KB | Multi Files |
| `model.layers.0-35.self_attn.v_proj.weight` (×36 layers) | `[1024, 4096]` | `torch.float8_e4m3fn` | 144.00 MB | Multi Files |
| `model.layers.0-35.self_attn.v_proj.weight_scale_inv` (×36 layers) | `[8, 32]` | `torch.bfloat16` | 18.00 KB | Multi Files |
| `model.norm.weight` | `[4096]` | `torch.bfloat16` | 8.00 KB | model-00002-of-00002.safetensors |

</details>

