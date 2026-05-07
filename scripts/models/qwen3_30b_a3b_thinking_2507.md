# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen3-30B-A3B-Thinking-2507`

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

- **权重文件**: 8 个 `safetensors` 文件
- **文件总大小**: 27.08 GB
- **权重张量数**: 8,979
- **参数总量**: 14,535,986,688
- **张量累计大小**: 27.08 GB
- **压缩**: 8979 → 17 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[151936, 2048]` | `torch.bfloat16` | 593.50 MB | model-00016-of-00016.safetensors |
| `model.layers.25-47.input_layernorm.weight` (×23 layers) | `[2048]` | `torch.bfloat16` | 92.00 KB | Multi Files |
| `model.layers.25-47.mlp.gate.weight` (×23 layers) | `[128, 2048]` | `torch.bfloat16` | 11.50 MB | Multi Files |
| `model.layers.25-47.post_attention_layernorm.weight` (×23 layers) | `[2048]` | `torch.bfloat16` | 92.00 KB | Multi Files |
| `model.layers.25.mlp.experts.18-127.down_proj.weight` (×1 layers, ×110 experts) | `[2048, 768]` | `torch.bfloat16` | 330.00 MB | model-00009-of-00016.safetensors |
| `model.layers.25.mlp.experts.19-127.gate_proj.weight` (×1 layers, ×109 experts) | `[768, 2048]` | `torch.bfloat16` | 327.00 MB | model-00009-of-00016.safetensors |
| `model.layers.25.mlp.experts.19-127.up_proj.weight` (×1 layers, ×109 experts) | `[768, 2048]` | `torch.bfloat16` | 327.00 MB | model-00009-of-00016.safetensors |
| `model.layers.26-47.mlp.experts.0-127.down_proj.weight` (×22 layers, ×128 experts) | `[2048, 768]` | `torch.bfloat16` | 8.25 GB | Multi Files |
| `model.layers.26-47.mlp.experts.0-127.gate_proj.weight` (×22 layers, ×128 experts) | `[768, 2048]` | `torch.bfloat16` | 8.25 GB | Multi Files |
| `model.layers.26-47.mlp.experts.0-127.up_proj.weight` (×22 layers, ×128 experts) | `[768, 2048]` | `torch.bfloat16` | 8.25 GB | Multi Files |
| `model.layers.26-47.self_attn.k_norm.weight` (×22 layers) | `[128]` | `torch.bfloat16` | 5.50 KB | Multi Files |
| `model.layers.26-47.self_attn.k_proj.weight` (×22 layers) | `[512, 2048]` | `torch.bfloat16` | 44.00 MB | Multi Files |
| `model.layers.26-47.self_attn.o_proj.weight` (×22 layers) | `[2048, 4096]` | `torch.bfloat16` | 352.00 MB | Multi Files |
| `model.layers.26-47.self_attn.q_norm.weight` (×22 layers) | `[128]` | `torch.bfloat16` | 5.50 KB | Multi Files |
| `model.layers.26-47.self_attn.q_proj.weight` (×22 layers) | `[4096, 2048]` | `torch.bfloat16` | 352.00 MB | Multi Files |
| `model.layers.26-47.self_attn.v_proj.weight` (×22 layers) | `[512, 2048]` | `torch.bfloat16` | 44.00 MB | Multi Files |
| `model.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00016-of-00016.safetensors |

</details>

