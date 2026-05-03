# 模型信息报告

- **模型路径**: `/nfs/volume-1615-2/models/Qwen3-Coder-30B-A3B-Instruct`

# 模型配置

- **模型类型**: `Qwen3MoeConfig`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 2048
- **层数**: 48
- **注意力头数**: 32
- **词表大小**: 151936
- **中间层大小**: 5472

<details><summary>完整配置</summary>

```
Qwen3MoeConfig {
  "architectures": [
    "Qwen3MoeForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "decoder_sparse_step": 1,
  "dtype": "bfloat16",
  "eos_token_id": 151645,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 2048,
  "initializer_range": 0.02,
  "intermediate_size": 5472,
  "max_position_embeddings": 262144,
  "max_window_layers": 28,
  "mlp_only_layers": [],
  "model_type": "qwen3_moe",
  "moe_intermediate_size": 768,
  "norm_topk_prob": true,
  "num_attention_heads": 32,
  "num_experts": 128,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 48,
  "num_key_value_heads": 4,
  "output_router_logits": false,
  "qkv_bias": false,
  "rms_norm_eps": 1e-06,
  "rope_scaling": null,
  "rope_theta": 10000000,
  "router_aux_loss_coef": 0.0,
  "shared_expert_intermediate_size": 0,
  "sliding_window": null,
  "tie_word_embeddings": false,
  "transformers_version": "4.57.1",
  "use_cache": true,
  "use_qk_norm": true,
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
        (gate): Linear(in_features=2048, out_features=128, bias=False)
        (experts): ModuleList(
          (0-127): 128 x Qwen3MoeMLP(
            (gate_proj): Linear(in_features=2048, out_features=768, bias=False)
            (up_proj): Linear(in_features=2048, out_features=768, bias=False)
            (down_proj): Linear(in_features=768, out_features=2048, bias=False)
            (act_fn): SiLUActivation()
          )
        )
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

- **权重文件**: 16 个 `safetensors` 文件
- **文件总大小**: 56.87 GB
- **权重张量数**: 18,867
- **参数总量**: 30,532,122,624
- **张量累计大小**: 56.87 GB
- **压缩**: 18867 → 15 行 (合并相同 shape/dtype 的 experts 和 layers)

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[151936, 2048]` | `torch.bfloat16` | 593.50 MB | model-00016-of-00016.safetensors |
| `model.embed_tokens.weight` | `[151936, 2048]` | `torch.bfloat16` | 593.50 MB | model-00001-of-00016.safetensors |
| `model.layers.0-47.input_layernorm.weight` (×48 layers) | `[2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `model.layers.0-47.mlp.experts.0-127.down_proj.weight` (×48 layers, ×128 experts) | `[2048, 768]` | `torch.bfloat16` | 18.00 GB | Multi Files |
| `model.layers.0-47.mlp.experts.0-127.gate_proj.weight` (×48 layers, ×128 experts) | `[768, 2048]` | `torch.bfloat16` | 18.00 GB | Multi Files |
| `model.layers.0-47.mlp.experts.0-127.up_proj.weight` (×48 layers, ×128 experts) | `[768, 2048]` | `torch.bfloat16` | 18.00 GB | Multi Files |
| `model.layers.0-47.mlp.gate.weight` (×48 layers) | `[128, 2048]` | `torch.bfloat16` | 24.00 MB | Multi Files |
| `model.layers.0-47.post_attention_layernorm.weight` (×48 layers) | `[2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `model.layers.0-47.self_attn.k_norm.weight` (×48 layers) | `[128]` | `torch.bfloat16` | 12.00 KB | Multi Files |
| `model.layers.0-47.self_attn.k_proj.weight` (×48 layers) | `[512, 2048]` | `torch.bfloat16` | 96.00 MB | Multi Files |
| `model.layers.0-47.self_attn.o_proj.weight` (×48 layers) | `[2048, 4096]` | `torch.bfloat16` | 768.00 MB | Multi Files |
| `model.layers.0-47.self_attn.q_norm.weight` (×48 layers) | `[128]` | `torch.bfloat16` | 12.00 KB | Multi Files |
| `model.layers.0-47.self_attn.q_proj.weight` (×48 layers) | `[4096, 2048]` | `torch.bfloat16` | 768.00 MB | Multi Files |
| `model.layers.0-47.self_attn.v_proj.weight` (×48 layers) | `[512, 2048]` | `torch.bfloat16` | 96.00 MB | Multi Files |
| `model.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00016-of-00016.safetensors |

</details>

