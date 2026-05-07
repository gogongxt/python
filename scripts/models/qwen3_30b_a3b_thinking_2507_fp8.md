# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen3-30B-A3B-Thinking-2507-FP8`

# 模型配置

- **模型类型**: `Qwen3MoeConfig`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 2048
- **层数**: 48
- **注意力头数**: 32
- **词表大小**: 151936
- **中间层大小**: 6144

<details><summary>完整配置</summary>

```
Qwen3MoeConfig {
  "architectures": [
    "Qwen3MoeForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "decoder_sparse_step": 1,
  "dtype": "bfloat16",
  "eos_token_id": 151645,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 2048,
  "initializer_range": 0.02,
  "intermediate_size": 6144,
  "max_position_embeddings": 262144,
  "max_window_layers": 48,
  "mlp_only_layers": [],
  "model_type": "qwen3_moe",
  "moe_intermediate_size": 768,
  "norm_topk_prob": true,
  "num_attention_heads": 32,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 48,
  "num_key_value_heads": 4,
  "num_local_experts": 128,
  "output_router_logits": false,
  "pad_token_id": null,
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "e4m3",
    "modules_to_not_convert": [
      "lm_head",
      "model.layers.0.input_layernorm",
      "model.layers.0.mlp.gate",
      "model.layers.0.post_attention_layernorm",
      "model.layers.1.input_layernorm",
      "model.layers.1.mlp.gate",
      "model.layers.1.post_attention_layernorm",
      "model.layers.2.input_layernorm",
      "model.layers.2.mlp.gate",
      "model.layers.2.post_attention_layernorm",
      "model.layers.3.input_layernorm",
      "model.layers.3.mlp.gate",
      "model.layers.3.post_attention_layernorm",
      "model.layers.4.input_layernorm",
      "model.layers.4.mlp.gate",
      "model.layers.4.post_attention_layernorm",
      "model.layers.5.input_layernorm",
      "model.layers.5.mlp.gate",
      "model.layers.5.post_attention_layernorm",
      "model.layers.6.input_layernorm",
      "model.layers.6.mlp.gate",
      "model.layers.6.post_attention_layernorm",
      "model.layers.7.input_layernorm",
      "model.layers.7.mlp.gate",
      "model.layers.7.post_attention_layernorm",
      "model.layers.8.input_layernorm",
      "model.layers.8.mlp.gate",
      "model.layers.8.post_attention_layernorm",
      "model.layers.9.input_layernorm",
      "model.layers.9.mlp.gate",
      "model.layers.9.post_attention_layernorm",
      "model.layers.10.input_layernorm",
      "model.layers.10.mlp.gate",
      "model.layers.10.post_attention_layernorm",
      "model.layers.11.input_layernorm",
      "model.layers.11.mlp.gate",
      "model.layers.11.post_attention_layernorm",
      "model.layers.12.input_layernorm",
      "model.layers.12.mlp.gate",
      "model.layers.12.post_attention_layernorm",
      "model.layers.13.input_layernorm",
      "model.layers.13.mlp.gate",
      "model.layers.13.post_attention_layernorm",
      "model.layers.14.input_layernorm",
      "model.layers.14.mlp.gate",
      "model.layers.14.post_attention_layernorm",
      "model.layers.15.input_layernorm",
      "model.layers.15.mlp.gate",
      "model.layers.15.post_attention_layernorm",
      "model.layers.16.input_layernorm",
      "model.layers.16.mlp.gate",
      "model.layers.16.post_attention_layernorm",
      "model.layers.17.input_layernorm",
      "model.layers.17.mlp.gate",
      "model.layers.17.post_attention_layernorm",
      "model.layers.18.input_layernorm",
      "model.layers.18.mlp.gate",
      "model.layers.18.post_attention_layernorm",
      "model.layers.19.input_layernorm",
      "model.layers.19.mlp.gate",
      "model.layers.19.post_attention_layernorm",
      "model.layers.20.input_layernorm",
      "model.layers.20.mlp.gate",
      "model.layers.20.post_attention_layernorm",
      "model.layers.21.input_layernorm",
      "model.layers.21.mlp.gate",
      "model.layers.21.post_attention_layernorm",
      "model.layers.22.input_layernorm",
      "model.layers.22.mlp.gate",
      "model.layers.22.post_attention_layernorm",
      "model.layers.23.input_layernorm",
      "model.layers.23.mlp.gate",
      "model.layers.23.post_attention_layernorm",
      "model.layers.24.input_layernorm",
      "model.layers.24.mlp.gate",
      "model.layers.24.post_attention_layernorm",
      "model.layers.25.input_layernorm",
      "model.layers.25.mlp.gate",
      "model.layers.25.post_attention_layernorm",
      "model.layers.26.input_layernorm",
      "model.layers.26.mlp.gate",
      "model.layers.26.post_attention_layernorm",
      "model.layers.27.input_layernorm",
      "model.layers.27.mlp.gate",
      "model.layers.27.post_attention_layernorm",
      "model.layers.28.input_layernorm",
      "model.layers.28.mlp.gate",
      "model.layers.28.post_attention_layernorm",
      "model.layers.29.input_layernorm",
      "model.layers.29.mlp.gate",
      "model.layers.29.post_attention_layernorm",
      "model.layers.30.input_layernorm",
      "model.layers.30.mlp.gate",
      "model.layers.30.post_attention_layernorm",
      "model.layers.31.input_layernorm",
      "model.layers.31.mlp.gate",
      "model.layers.31.post_attention_layernorm",
      "model.layers.32.input_layernorm",
      "model.layers.32.mlp.gate",
      "model.layers.32.post_attention_layernorm",
      "model.layers.33.input_layernorm",
      "model.layers.33.mlp.gate",
      "model.layers.33.post_attention_layernorm",
      "model.layers.34.input_layernorm",
      "model.layers.34.mlp.gate",
      "model.layers.34.post_attention_layernorm",
      "model.layers.35.input_layernorm",
      "model.layers.35.mlp.gate",
      "model.layers.35.post_attention_layernorm",
      "model.layers.36.input_layernorm",
      "model.layers.36.mlp.gate",
      "model.layers.36.post_attention_layernorm",
      "model.layers.37.input_layernorm",
      "model.layers.37.mlp.gate",
      "model.layers.37.post_attention_layernorm",
      "model.layers.38.input_layernorm",
      "model.layers.38.mlp.gate",
      "model.layers.38.post_attention_layernorm",
      "model.layers.39.input_layernorm",
      "model.layers.39.mlp.gate",
      "model.layers.39.post_attention_layernorm",
      "model.layers.40.input_layernorm",
      "model.layers.40.mlp.gate",
      "model.layers.40.post_attention_layernorm",
      "model.layers.41.input_layernorm",
      "model.layers.41.mlp.gate",
      "model.layers.41.post_attention_layernorm",
      "model.layers.42.input_layernorm",
      "model.layers.42.mlp.gate",
      "model.layers.42.post_attention_layernorm",
      "model.layers.43.input_layernorm",
      "model.layers.43.mlp.gate",
      "model.layers.43.post_attention_layernorm",
      "model.layers.44.input_layernorm",
      "model.layers.44.mlp.gate",
      "model.layers.44.post_attention_layernorm",
      "model.layers.45.input_layernorm",
      "model.layers.45.mlp.gate",
      "model.layers.45.post_attention_layernorm",
      "model.layers.46.input_layernorm",
      "model.layers.46.mlp.gate",
      "model.layers.46.post_attention_layernorm",
      "model.layers.47.input_layernorm",
      "model.layers.47.mlp.gate",
      "model.layers.47.post_attention_layernorm"
    ],
    "quant_method": "fp8",
    "weight_block_size": [
      128,
      128
    ]
  },
  "rms_norm_eps": 1e-06,
  "rope_parameters": {
    "rope_theta": 10000000,
    "rope_type": "default"
  },
  "router_aux_loss_coef": 0.001,
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

**模型类**: `Qwen3MoeModel`

```
Qwen3MoeModel(
  (embed_tokens): Embedding(151936, 2048)
  (layers): ModuleList(
    (0-47): 48 x Qwen3MoeDecoderLayer(
      (self_attn): Qwen3MoeAttention(
        (q_proj): Linear(in_features=2048, out_features=4096, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3MoeRMSNorm((128,), eps=1e-06)
        (k_norm): Qwen3MoeRMSNorm((128,), eps=1e-06)
      )
      (mlp): Qwen3MoeSparseMoeBlock(
        (experts): Qwen3MoeExperts(
          (act_fn): SiLUActivation()
        )
        (gate): Qwen3MoeTopKRouter()
      )
      (input_layernorm): Qwen3MoeRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3MoeRMSNorm((2048,), eps=1e-06)
    )
  )
  (norm): Qwen3MoeRMSNorm((2048,), eps=1e-06)
  (rotary_emb): Qwen3MoeRotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 4 个 `safetensors` 文件
- **文件总大小**: 29.03 GB
- **权重张量数**: 37,491
- **参数总量**: 30,533,947,392
- **张量累计大小**: 29.03 GB
- **压缩**: 37491 → 22 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[151936, 2048]` | `torch.bfloat16` | 593.50 MB | model-00004-of-00004.safetensors |
| `model.embed_tokens.weight` | `[151936, 2048]` | `torch.bfloat16` | 593.50 MB | model-00001-of-00004.safetensors |
| `model.layers.0-47.input_layernorm.weight` (×48 layers) | `[2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `model.layers.0-47.mlp.experts.0-127.down_proj.weight` (×48 layers, ×128 experts) | `[2048, 768]` | `torch.float8_e4m3fn` | 9.00 GB | Multi Files |
| `model.layers.0-47.mlp.experts.0-127.down_proj.weight_scale_inv` (×48 layers, ×128 experts) | `[16, 6]` | `torch.bfloat16` | 1.12 MB | Multi Files |
| `model.layers.0-47.mlp.experts.0-127.gate_proj.weight` (×48 layers, ×128 experts) | `[768, 2048]` | `torch.float8_e4m3fn` | 9.00 GB | Multi Files |
| `model.layers.0-47.mlp.experts.0-127.gate_proj.weight_scale_inv` (×48 layers, ×128 experts) | `[6, 16]` | `torch.bfloat16` | 1.12 MB | Multi Files |
| `model.layers.0-47.mlp.experts.0-127.up_proj.weight` (×48 layers, ×128 experts) | `[768, 2048]` | `torch.float8_e4m3fn` | 9.00 GB | Multi Files |
| `model.layers.0-47.mlp.experts.0-127.up_proj.weight_scale_inv` (×48 layers, ×128 experts) | `[6, 16]` | `torch.bfloat16` | 1.12 MB | Multi Files |
| `model.layers.0-47.mlp.gate.weight` (×48 layers) | `[128, 2048]` | `torch.bfloat16` | 24.00 MB | Multi Files |
| `model.layers.0-47.post_attention_layernorm.weight` (×48 layers) | `[2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `model.layers.0-47.self_attn.k_norm.weight` (×48 layers) | `[128]` | `torch.bfloat16` | 12.00 KB | Multi Files |
| `model.layers.0-47.self_attn.k_proj.weight` (×48 layers) | `[512, 2048]` | `torch.float8_e4m3fn` | 48.00 MB | Multi Files |
| `model.layers.0-47.self_attn.k_proj.weight_scale_inv` (×48 layers) | `[4, 16]` | `torch.bfloat16` | 6.00 KB | Multi Files |
| `model.layers.0-47.self_attn.o_proj.weight` (×48 layers) | `[2048, 4096]` | `torch.float8_e4m3fn` | 384.00 MB | Multi Files |
| `model.layers.0-47.self_attn.o_proj.weight_scale_inv` (×48 layers) | `[16, 32]` | `torch.bfloat16` | 48.00 KB | Multi Files |
| `model.layers.0-47.self_attn.q_norm.weight` (×48 layers) | `[128]` | `torch.bfloat16` | 12.00 KB | Multi Files |
| `model.layers.0-47.self_attn.q_proj.weight` (×48 layers) | `[4096, 2048]` | `torch.float8_e4m3fn` | 384.00 MB | Multi Files |
| `model.layers.0-47.self_attn.q_proj.weight_scale_inv` (×48 layers) | `[32, 16]` | `torch.bfloat16` | 48.00 KB | Multi Files |
| `model.layers.0-47.self_attn.v_proj.weight` (×48 layers) | `[512, 2048]` | `torch.float8_e4m3fn` | 48.00 MB | Multi Files |
| `model.layers.0-47.self_attn.v_proj.weight_scale_inv` (×48 layers) | `[4, 16]` | `torch.bfloat16` | 6.00 KB | Multi Files |
| `model.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00004-of-00004.safetensors |

</details>

