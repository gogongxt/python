# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen3-235B-A22B-Instruct-2507`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/Qwen3-235B-A22B-Instruct-2507/config.json`

```json

{
  "architectures": [
    "Qwen3MoeForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "decoder_sparse_step": 1,
  "eos_token_id": 151645,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 12288,
  "max_position_embeddings": 262144,
  "max_window_layers": 94,
  "mlp_only_layers": [],
  "model_type": "qwen3_moe",
  "moe_intermediate_size": 1536,
  "norm_topk_prob": true,
  "num_attention_heads": 64,
  "num_experts": 128,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 94,
  "num_key_value_heads": 4,
  "output_router_logits": false,
  "rms_norm_eps": 1e-06,
  "rope_scaling": null,
  "rope_theta": 5000000,
  "router_aux_loss_coef": 0.001,
  "sliding_window": null,
  "tie_word_embeddings": false,
  "torch_dtype": "bfloat16",
  "transformers_version": "4.51.0",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 151936
}
```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `Qwen3MoeConfig`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 4096
- **层数**: 94
- **注意力头数**: 64
- **词表大小**: 151936
- **中间层大小**: 12288

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
  "hidden_size": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 12288,
  "max_position_embeddings": 262144,
  "max_window_layers": 94,
  "mlp_only_layers": [],
  "model_type": "qwen3_moe",
  "moe_intermediate_size": 1536,
  "norm_topk_prob": true,
  "num_attention_heads": 64,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 94,
  "num_key_value_heads": 4,
  "num_local_experts": 128,
  "output_router_logits": false,
  "pad_token_id": null,
  "rms_norm_eps": 1e-06,
  "rope_parameters": {
    "rope_theta": 5000000,
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
  (embed_tokens): Embedding(151936, 4096)
  (layers): ModuleList(
    (0-93): 94 x Qwen3MoeDecoderLayer(
      (self_attn): Qwen3MoeAttention(
        (q_proj): Linear(in_features=4096, out_features=8192, bias=False)
        (k_proj): Linear(in_features=4096, out_features=512, bias=False)
        (v_proj): Linear(in_features=4096, out_features=512, bias=False)
        (o_proj): Linear(in_features=8192, out_features=4096, bias=False)
        (q_norm): Qwen3MoeRMSNorm((128,), eps=1e-06)
        (k_norm): Qwen3MoeRMSNorm((128,), eps=1e-06)
      )
      (mlp): Qwen3MoeSparseMoeBlock(
        (experts): Qwen3MoeExperts(
          (act_fn): SiLUActivation()
        )
        (gate): Qwen3MoeTopKRouter()
      )
      (input_layernorm): Qwen3MoeRMSNorm((4096,), eps=1e-06)
      (post_attention_layernorm): Qwen3MoeRMSNorm((4096,), eps=1e-06)
    )
  )
  (norm): Qwen3MoeRMSNorm((4096,), eps=1e-06)
  (rotary_emb): Qwen3MoeRotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 1 个 `safetensors` 文件
- **文件总大小**: 3.72 GB
- **权重张量数**: 214
- **参数总量**: 1,995,964,672
- **张量累计大小**: 3.72 GB
- **压缩**: 214 → 10 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `model.embed_tokens.weight` | `[151936, 4096]` | `torch.bfloat16` | 1.16 GB | model-00001-of-00118.safetensors |
| `model.layers.0.mlp.experts.0-68.down_proj.weight` (×69 experts) | `[4096, 1536]` | `torch.bfloat16` | 828.00 MB | model-00001-of-00118.safetensors |
| `model.layers.0.mlp.experts.0-68.gate_proj.weight` (×69 experts) | `[1536, 4096]` | `torch.bfloat16` | 828.00 MB | model-00001-of-00118.safetensors |
| `model.layers.0.mlp.experts.0-68.up_proj.weight` (×69 experts) | `[1536, 4096]` | `torch.bfloat16` | 828.00 MB | model-00001-of-00118.safetensors |
| `model.layers.0.self_attn.k_norm.weight` | `[128]` | `torch.bfloat16` | 256.00 B | model-00001-of-00118.safetensors |
| `model.layers.0.self_attn.k_proj.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00001-of-00118.safetensors |
| `model.layers.0.self_attn.o_proj.weight` | `[4096, 8192]` | `torch.bfloat16` | 64.00 MB | model-00001-of-00118.safetensors |
| `model.layers.0.self_attn.q_norm.weight` | `[128]` | `torch.bfloat16` | 256.00 B | model-00001-of-00118.safetensors |
| `model.layers.0.self_attn.q_proj.weight` | `[8192, 4096]` | `torch.bfloat16` | 64.00 MB | model-00001-of-00118.safetensors |
| `model.layers.0.self_attn.v_proj.weight` | `[512, 4096]` | `torch.bfloat16` | 4.00 MB | model-00001-of-00118.safetensors |

</details>

