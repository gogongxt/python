# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/GLM-4.7-Flash`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/GLM-4.7-Flash/config.json`

```json

{
  "architectures": [
    "Glm4MoeLiteForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "pad_token_id": 154820,
  "eos_token_id": [
    154820,
    154827,
    154829
  ],
  "hidden_act": "silu",
  "hidden_size": 2048,
  "intermediate_size": 10240,
  "max_position_embeddings": 202752,
  "model_type": "glm4_moe_lite",
  "moe_intermediate_size": 1536,
  "topk_method": "noaux_tc",
  "norm_topk_prob": true,
  "num_attention_heads": 20,
  "n_group": 1,
  "topk_group": 1,
  "n_routed_experts": 64,
  "n_shared_experts": 1,
  "routed_scaling_factor": 1.8,
  "num_experts_per_tok": 4,
  "first_k_dense_replace": 1,
  "num_hidden_layers": 47,
  "num_key_value_heads": 20,
  "num_nextn_predict_layers": 1,
  "partial_rotary_factor": 1.0,
  "rms_norm_eps": 1e-05,
  "rope_scaling": null,
  "rope_theta": 1000000,
  "tie_word_embeddings": false,
  "dtype": "bfloat16",
  "transformers_version": "5.0.0rc0",
  "q_lora_rank": 768,
  "kv_lora_rank": 512,
  "qk_nope_head_dim": 192,
  "qk_rope_head_dim": 64,
  "v_head_dim": 256,
  "vocab_size": 154880
}

```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `Glm4MoeLiteConfig`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 2048
- **层数**: 47
- **注意力头数**: 20
- **词表大小**: 154880
- **中间层大小**: 10240

```
Glm4MoeLiteConfig {
  "architectures": [
    "Glm4MoeLiteForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 0,
  "dtype": "bfloat16",
  "eos_token_id": [
    154820,
    154827,
    154829
  ],
  "first_k_dense_replace": 1,
  "hidden_act": "silu",
  "hidden_size": 2048,
  "initializer_range": 0.02,
  "intermediate_size": 10240,
  "kv_lora_rank": 512,
  "max_position_embeddings": 202752,
  "mlp_layer_types": [
    "dense",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse",
    "sparse"
  ],
  "model_type": "glm4_moe_lite",
  "moe_intermediate_size": 1536,
  "n_group": 1,
  "n_routed_experts": 64,
  "n_shared_experts": 1,
  "norm_topk_prob": true,
  "num_attention_heads": 20,
  "num_experts_per_tok": 4,
  "num_hidden_layers": 47,
  "num_key_value_heads": 20,
  "num_nextn_predict_layers": 1,
  "pad_token_id": 154820,
  "partial_rotary_factor": 1.0,
  "pretraining_tp": 1,
  "q_lora_rank": 768,
  "qk_head_dim": 256,
  "qk_nope_head_dim": 192,
  "qk_rope_head_dim": 64,
  "rms_norm_eps": 1e-05,
  "rope_interleave": true,
  "rope_parameters": {
    "partial_rotary_factor": 1.0,
    "rope_theta": 1000000,
    "rope_type": "default"
  },
  "routed_scaling_factor": 1.8,
  "tie_word_embeddings": false,
  "topk_group": 1,
  "topk_method": "noaux_tc",
  "transformers_version": "5.7.0",
  "use_cache": true,
  "v_head_dim": 256,
  "vocab_size": 154880
}

```

</details>

# 模型结构

**模型类**: `Glm4MoeLiteModel`

```
Glm4MoeLiteModel(
  (embed_tokens): Embedding(154880, 2048, padding_idx=154820)
  (layers): ModuleList(
    (0): Glm4MoeLiteDecoderLayer(
      (self_attn): Glm4MoeLiteAttention(
        (q_a_proj): Linear(in_features=2048, out_features=768, bias=False)
        (q_a_layernorm): Glm4MoeLiteRMSNorm((768,), eps=1e-06)
        (q_b_proj): Linear(in_features=768, out_features=5120, bias=False)
        (kv_a_proj_with_mqa): Linear(in_features=2048, out_features=576, bias=False)
        (kv_a_layernorm): Glm4MoeLiteRMSNorm((512,), eps=1e-06)
        (kv_b_proj): Linear(in_features=512, out_features=8960, bias=False)
        (o_proj): Linear(in_features=5120, out_features=2048, bias=False)
      )
      (mlp): Glm4MoeLiteMLP(
        (gate_proj): Linear(in_features=2048, out_features=10240, bias=False)
        (up_proj): Linear(in_features=2048, out_features=10240, bias=False)
        (down_proj): Linear(in_features=10240, out_features=2048, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): Glm4MoeLiteRMSNorm((2048,), eps=1e-05)
      (post_attention_layernorm): Glm4MoeLiteRMSNorm((2048,), eps=1e-05)
    )
    (1-46): 46 x Glm4MoeLiteDecoderLayer(
      (self_attn): Glm4MoeLiteAttention(
        (q_a_proj): Linear(in_features=2048, out_features=768, bias=False)
        (q_a_layernorm): Glm4MoeLiteRMSNorm((768,), eps=1e-06)
        (q_b_proj): Linear(in_features=768, out_features=5120, bias=False)
        (kv_a_proj_with_mqa): Linear(in_features=2048, out_features=576, bias=False)
        (kv_a_layernorm): Glm4MoeLiteRMSNorm((512,), eps=1e-06)
        (kv_b_proj): Linear(in_features=512, out_features=8960, bias=False)
        (o_proj): Linear(in_features=5120, out_features=2048, bias=False)
      )
      (mlp): Glm4MoeLiteMoE(
        (experts): Glm4MoeLiteNaiveMoe(
          (act_fn): SiLUActivation()
        )
        (gate): Glm4MoeLiteTopkRouter()
        (shared_experts): Glm4MoeLiteMLP(
          (gate_proj): Linear(in_features=2048, out_features=1536, bias=False)
          (up_proj): Linear(in_features=2048, out_features=1536, bias=False)
          (down_proj): Linear(in_features=1536, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
      )
      (input_layernorm): Glm4MoeLiteRMSNorm((2048,), eps=1e-05)
      (post_attention_layernorm): Glm4MoeLiteRMSNorm((2048,), eps=1e-05)
    )
  )
  (norm): Glm4MoeLiteRMSNorm((2048,), eps=1e-05)
  (rotary_emb): Glm4MoeLiteRotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 48 个 `safetensors` 文件
- **文件总大小**: 58.16 GB
- **权重张量数**: 9,703
- **参数总量**: 31,221,488,576
- **张量累计大小**: 58.15 GB
- **压缩**: 9703 → 29 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[154880, 2048]` | `torch.bfloat16` | 605.00 MB | model-00047-of-00048.safetensors |
| `model.embed_tokens.weight` | `[154880, 2048]` | `torch.bfloat16` | 605.00 MB | model-00001-of-00048.safetensors |
| `model.layers.0-47.input_layernorm.weight` (×48 layers) | `[2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `model.layers.0-47.post_attention_layernorm.weight` (×48 layers) | `[2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `model.layers.0-47.self_attn.kv_a_layernorm.weight` (×48 layers) | `[512]` | `torch.bfloat16` | 48.00 KB | Multi Files |
| `model.layers.0-47.self_attn.kv_a_proj_with_mqa.weight` (×48 layers) | `[576, 2048]` | `torch.bfloat16` | 108.00 MB | Multi Files |
| `model.layers.0-47.self_attn.kv_b_proj.weight` (×48 layers) | `[8960, 512]` | `torch.bfloat16` | 420.00 MB | Multi Files |
| `model.layers.0-47.self_attn.o_proj.weight` (×48 layers) | `[2048, 5120]` | `torch.bfloat16` | 960.00 MB | Multi Files |
| `model.layers.0-47.self_attn.q_a_layernorm.weight` (×48 layers) | `[768]` | `torch.bfloat16` | 72.00 KB | Multi Files |
| `model.layers.0-47.self_attn.q_a_proj.weight` (×48 layers) | `[768, 2048]` | `torch.bfloat16` | 144.00 MB | Multi Files |
| `model.layers.0-47.self_attn.q_b_proj.weight` (×48 layers) | `[5120, 768]` | `torch.bfloat16` | 360.00 MB | Multi Files |
| `model.layers.0.mlp.down_proj.weight` | `[2048, 10240]` | `torch.bfloat16` | 40.00 MB | model-00001-of-00048.safetensors |
| `model.layers.0.mlp.gate_proj.weight` | `[10240, 2048]` | `torch.bfloat16` | 40.00 MB | model-00001-of-00048.safetensors |
| `model.layers.0.mlp.up_proj.weight` | `[10240, 2048]` | `torch.bfloat16` | 40.00 MB | model-00001-of-00048.safetensors |
| `model.layers.1-47.mlp.experts.0-63.down_proj.weight` (×47 layers, ×64 experts) | `[2048, 1536]` | `torch.bfloat16` | 17.62 GB | Multi Files |
| `model.layers.1-47.mlp.experts.0-63.gate_proj.weight` (×47 layers, ×64 experts) | `[1536, 2048]` | `torch.bfloat16` | 17.62 GB | Multi Files |
| `model.layers.1-47.mlp.experts.0-63.up_proj.weight` (×47 layers, ×64 experts) | `[1536, 2048]` | `torch.bfloat16` | 17.62 GB | Multi Files |
| `model.layers.1-47.mlp.gate.e_score_correction_bias` (×47 layers) | `[64]` | `torch.float32` | 11.75 KB | Multi Files |
| `model.layers.1-47.mlp.gate.weight` (×47 layers) | `[64, 2048]` | `torch.bfloat16` | 11.75 MB | Multi Files |
| `model.layers.1-47.mlp.shared_experts.down_proj.weight` (×47 layers) | `[2048, 1536]` | `torch.bfloat16` | 282.00 MB | Multi Files |
| `model.layers.1-47.mlp.shared_experts.gate_proj.weight` (×47 layers) | `[1536, 2048]` | `torch.bfloat16` | 282.00 MB | Multi Files |
| `model.layers.1-47.mlp.shared_experts.up_proj.weight` (×47 layers) | `[1536, 2048]` | `torch.bfloat16` | 282.00 MB | Multi Files |
| `model.layers.47.eh_proj.weight` | `[2048, 4096]` | `torch.bfloat16` | 16.00 MB | model-00048-of-00048.safetensors |
| `model.layers.47.embed_tokens.weight` | `[154880, 2048]` | `torch.bfloat16` | 605.00 MB | model-00001-of-00048.safetensors |
| `model.layers.47.enorm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00048-of-00048.safetensors |
| `model.layers.47.hnorm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00048-of-00048.safetensors |
| `model.layers.47.shared_head.head.weight` | `[154880, 2048]` | `torch.bfloat16` | 605.00 MB | model-00047-of-00048.safetensors |
| `model.layers.47.shared_head.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00048-of-00048.safetensors |
| `model.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00047-of-00048.safetensors |

</details>

