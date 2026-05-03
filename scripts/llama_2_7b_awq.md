# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/user/gogongxt/models/Llama-2-7B-AWQ`

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
  "pad_token_id": 0,
  "pretraining_tp": 1,
  "quantization_config": {
    "bits": 4,
    "group_size": 128,
    "quant_method": "awq",
    "version": "gemm",
    "zero_point": true
  },
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
  (embed_tokens): Embedding(32000, 4096, padding_idx=0)
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

- **权重文件**: 1 个 `safetensors` 文件
- **文件总大小**: 3.62 GB
- **权重张量数**: 739
- **参数总量**: 1,128,828,928
- **张量累计大小**: 3.62 GB
- **压缩**: 739 → 26 行 (合并相同 shape/dtype 的 experts 和 layers)

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[32000, 4096]` | `torch.float16` | 250.00 MB | model.safetensors |
| `model.embed_tokens.weight` | `[32000, 4096]` | `torch.float16` | 250.00 MB | model.safetensors |
| `model.layers.0-31.input_layernorm.weight` (×32 layers) | `[4096]` | `torch.float16` | 256.00 KB | model.safetensors |
| `model.layers.0-31.mlp.down_proj.qweight` (×32 layers) | `[11008, 512]` | `torch.int32` | 688.00 MB | model.safetensors |
| `model.layers.0-31.mlp.down_proj.qzeros` (×32 layers) | `[86, 512]` | `torch.int32` | 5.38 MB | model.safetensors |
| `model.layers.0-31.mlp.down_proj.scales` (×32 layers) | `[86, 4096]` | `torch.float16` | 21.50 MB | model.safetensors |
| `model.layers.0-31.mlp.gate_proj.qweight` (×32 layers) | `[4096, 1376]` | `torch.int32` | 688.00 MB | model.safetensors |
| `model.layers.0-31.mlp.gate_proj.qzeros` (×32 layers) | `[32, 1376]` | `torch.int32` | 5.38 MB | model.safetensors |
| `model.layers.0-31.mlp.gate_proj.scales` (×32 layers) | `[32, 11008]` | `torch.float16` | 21.50 MB | model.safetensors |
| `model.layers.0-31.mlp.up_proj.qweight` (×32 layers) | `[4096, 1376]` | `torch.int32` | 688.00 MB | model.safetensors |
| `model.layers.0-31.mlp.up_proj.qzeros` (×32 layers) | `[32, 1376]` | `torch.int32` | 5.38 MB | model.safetensors |
| `model.layers.0-31.mlp.up_proj.scales` (×32 layers) | `[32, 11008]` | `torch.float16` | 21.50 MB | model.safetensors |
| `model.layers.0-31.post_attention_layernorm.weight` (×32 layers) | `[4096]` | `torch.float16` | 256.00 KB | model.safetensors |
| `model.layers.0-31.self_attn.k_proj.qweight` (×32 layers) | `[4096, 512]` | `torch.int32` | 256.00 MB | model.safetensors |
| `model.layers.0-31.self_attn.k_proj.qzeros` (×32 layers) | `[32, 512]` | `torch.int32` | 2.00 MB | model.safetensors |
| `model.layers.0-31.self_attn.k_proj.scales` (×32 layers) | `[32, 4096]` | `torch.float16` | 8.00 MB | model.safetensors |
| `model.layers.0-31.self_attn.o_proj.qweight` (×32 layers) | `[4096, 512]` | `torch.int32` | 256.00 MB | model.safetensors |
| `model.layers.0-31.self_attn.o_proj.qzeros` (×32 layers) | `[32, 512]` | `torch.int32` | 2.00 MB | model.safetensors |
| `model.layers.0-31.self_attn.o_proj.scales` (×32 layers) | `[32, 4096]` | `torch.float16` | 8.00 MB | model.safetensors |
| `model.layers.0-31.self_attn.q_proj.qweight` (×32 layers) | `[4096, 512]` | `torch.int32` | 256.00 MB | model.safetensors |
| `model.layers.0-31.self_attn.q_proj.qzeros` (×32 layers) | `[32, 512]` | `torch.int32` | 2.00 MB | model.safetensors |
| `model.layers.0-31.self_attn.q_proj.scales` (×32 layers) | `[32, 4096]` | `torch.float16` | 8.00 MB | model.safetensors |
| `model.layers.0-31.self_attn.v_proj.qweight` (×32 layers) | `[4096, 512]` | `torch.int32` | 256.00 MB | model.safetensors |
| `model.layers.0-31.self_attn.v_proj.qzeros` (×32 layers) | `[32, 512]` | `torch.int32` | 2.00 MB | model.safetensors |
| `model.layers.0-31.self_attn.v_proj.scales` (×32 layers) | `[32, 4096]` | `torch.float16` | 8.00 MB | model.safetensors |
| `model.norm.weight` | `[4096]` | `torch.float16` | 8.00 KB | model.safetensors |

</details>

