# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/GLM-5.1`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/GLM-5.1/config.json`

```json

{
  "architectures": [
    "GlmMoeDsaForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "dtype": "bfloat16",
  "eos_token_id": [
    154820,
    154827,
    154829
  ],
  "ep_size": 1,
  "first_k_dense_replace": 3,
  "hidden_act": "silu",
  "head_dim": 64,
  "hidden_size": 6144,
  "index_head_dim": 128,
  "index_n_heads": 32,
  "index_topk": 2048,
  "indexer_rope_interleave": true,
  "initializer_range": 0.02,
  "intermediate_size": 12288,
  "kv_lora_rank": 512,
  "max_position_embeddings": 202752,
  "moe_intermediate_size": 2048,
  "moe_layer_freq": 1,
  "model_type": "glm_moe_dsa",
  "n_group": 1,
  "n_routed_experts": 256,
  "n_shared_experts": 1,
  "norm_topk_prob": true,
  "num_attention_heads": 64,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 78,
  "num_key_value_heads": 64,
  "num_nextn_predict_layers": 1,
  "pad_token_id": 154820,
  "pretraining_tp": 1,
  "q_lora_rank": 2048,
  "qk_head_dim": 256,
  "qk_nope_head_dim": 192,
  "qk_rope_head_dim": 64,
  "rms_norm_eps": 1e-05,
  "rope_interleave": true,
  "rope_parameters": {
    "rope_theta": 1000000,
    "rope_type": "default"
  },
  "routed_scaling_factor": 2.5,
  "scoring_func": "sigmoid",
  "tie_word_embeddings": false,
  "topk_group": 1,
  "topk_method": "noaux_tc",
  "transformers_version": "5.4.0",
  "use_cache": true,
  "v_head_dim": 256,
  "vocab_size": 154880
}

```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `GlmMoeDsaConfig`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 6144
- **层数**: 78
- **注意力头数**: 64
- **词表大小**: 154880
- **中间层大小**: 12288

```
GlmMoeDsaConfig {
  "architectures": [
    "GlmMoeDsaForCausalLM"
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
  "ep_size": 1,
  "first_k_dense_replace": 3,
  "hidden_act": "silu",
  "hidden_size": 6144,
  "index_head_dim": 128,
  "index_n_heads": 32,
  "index_topk": 2048,
  "indexer_rope_interleave": true,
  "indexer_types": [
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full",
    "full"
  ],
  "initializer_range": 0.02,
  "intermediate_size": 12288,
  "kv_lora_rank": 512,
  "max_position_embeddings": 202752,
  "mlp_layer_types": [
    "dense",
    "dense",
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
  "model_type": "glm_moe_dsa",
  "moe_intermediate_size": 2048,
  "moe_layer_freq": 1,
  "n_group": 1,
  "n_routed_experts": 256,
  "n_shared_experts": 1,
  "norm_topk_prob": true,
  "num_attention_heads": 64,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 78,
  "num_key_value_heads": 64,
  "num_nextn_predict_layers": 1,
  "pad_token_id": 154820,
  "pretraining_tp": 1,
  "q_lora_rank": 2048,
  "qk_head_dim": 256,
  "qk_nope_head_dim": 192,
  "qk_rope_head_dim": 64,
  "rms_norm_eps": 1e-05,
  "rope_interleave": true,
  "rope_parameters": {
    "rope_theta": 1000000,
    "rope_type": "default"
  },
  "routed_scaling_factor": 2.5,
  "scoring_func": "sigmoid",
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

**模型类**: `GlmMoeDsaModel`

```
GlmMoeDsaModel(
  (embed_tokens): Embedding(154880, 6144, padding_idx=154820)
  (layers): ModuleList(
    (0-2): 3 x GlmMoeDsaDecoderLayer(
      (self_attn): GlmMoeDsaAttention(
        (q_a_proj): Linear(in_features=6144, out_features=2048, bias=False)
        (q_a_layernorm): GlmMoeDsaRMSNorm((2048,), eps=1e-06)
        (q_b_proj): Linear(in_features=2048, out_features=16384, bias=False)
        (kv_a_proj_with_mqa): Linear(in_features=6144, out_features=576, bias=False)
        (kv_a_layernorm): GlmMoeDsaRMSNorm((512,), eps=1e-06)
        (kv_b_proj): Linear(in_features=512, out_features=28672, bias=False)
        (o_proj): Linear(in_features=16384, out_features=6144, bias=False)
        (indexer): GlmMoeDsaIndexer(
          (wq_b): Linear(in_features=2048, out_features=4096, bias=False)
          (wk): Linear(in_features=6144, out_features=128, bias=False)
          (k_norm): LayerNorm((128,), eps=1e-06, elementwise_affine=True)
          (weights_proj): Linear(in_features=6144, out_features=32, bias=False)
        )
      )
      (mlp): GlmMoeDsaMLP(
        (gate_proj): Linear(in_features=6144, out_features=12288, bias=False)
        (up_proj): Linear(in_features=6144, out_features=12288, bias=False)
        (down_proj): Linear(in_features=12288, out_features=6144, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): GlmMoeDsaRMSNorm((6144,), eps=1e-05)
      (post_attention_layernorm): GlmMoeDsaRMSNorm((6144,), eps=1e-05)
    )
    (3-77): 75 x GlmMoeDsaDecoderLayer(
      (self_attn): GlmMoeDsaAttention(
        (q_a_proj): Linear(in_features=6144, out_features=2048, bias=False)
        (q_a_layernorm): GlmMoeDsaRMSNorm((2048,), eps=1e-06)
        (q_b_proj): Linear(in_features=2048, out_features=16384, bias=False)
        (kv_a_proj_with_mqa): Linear(in_features=6144, out_features=576, bias=False)
        (kv_a_layernorm): GlmMoeDsaRMSNorm((512,), eps=1e-06)
        (kv_b_proj): Linear(in_features=512, out_features=28672, bias=False)
        (o_proj): Linear(in_features=16384, out_features=6144, bias=False)
        (indexer): GlmMoeDsaIndexer(
          (wq_b): Linear(in_features=2048, out_features=4096, bias=False)
          (wk): Linear(in_features=6144, out_features=128, bias=False)
          (k_norm): LayerNorm((128,), eps=1e-06, elementwise_affine=True)
          (weights_proj): Linear(in_features=6144, out_features=32, bias=False)
        )
      )
      (mlp): GlmMoeDsaMoE(
        (experts): GlmMoeDsaNaiveMoe(
          (act_fn): SiLUActivation()
        )
        (gate): GlmMoeDsaTopkRouter()
        (shared_experts): GlmMoeDsaMLP(
          (gate_proj): Linear(in_features=6144, out_features=2048, bias=False)
          (up_proj): Linear(in_features=6144, out_features=2048, bias=False)
          (down_proj): Linear(in_features=2048, out_features=6144, bias=False)
          (act_fn): SiLUActivation()
        )
      )
      (input_layernorm): GlmMoeDsaRMSNorm((6144,), eps=1e-05)
      (post_attention_layernorm): GlmMoeDsaRMSNorm((6144,), eps=1e-05)
    )
  )
  (norm): GlmMoeDsaRMSNorm((6144,), eps=1e-05)
  (rotary_emb): GlmMoeDsaRotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 282 个 `safetensors` 文件
- **文件总大小**: 1404.19 GB
- **权重张量数**: 59,870
- **参数总量**: 753,864,139,008
- **张量累计大小**: 1404.18 GB
- **压缩**: 59870 → 32 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[154880, 6144]` | `torch.bfloat16` | 1.77 GB | model-00001-of-00282.safetensors |
| `model.embed_tokens.weight` | `[154880, 6144]` | `torch.bfloat16` | 1.77 GB | model-00001-of-00282.safetensors |
| `model.layers.0-2.mlp.down_proj.weight` (×3 layers) | `[6144, 12288]` | `torch.bfloat16` | 432.00 MB | Multi Files |
| `model.layers.0-2.mlp.gate_proj.weight` (×3 layers) | `[12288, 6144]` | `torch.bfloat16` | 432.00 MB | Multi Files |
| `model.layers.0-2.mlp.up_proj.weight` (×3 layers) | `[12288, 6144]` | `torch.bfloat16` | 432.00 MB | Multi Files |
| `model.layers.0-78.input_layernorm.weight` (×79 layers) | `[6144]` | `torch.bfloat16` | 948.00 KB | Multi Files |
| `model.layers.0-78.post_attention_layernorm.weight` (×79 layers) | `[6144]` | `torch.bfloat16` | 948.00 KB | Multi Files |
| `model.layers.0-78.self_attn.indexer.k_norm.bias` (×79 layers) | `[128]` | `torch.bfloat16` | 19.75 KB | Multi Files |
| `model.layers.0-78.self_attn.indexer.k_norm.weight` (×79 layers) | `[128]` | `torch.bfloat16` | 19.75 KB | Multi Files |
| `model.layers.0-78.self_attn.indexer.weights_proj.weight` (×79 layers) | `[32, 6144]` | `torch.bfloat16` | 29.62 MB | Multi Files |
| `model.layers.0-78.self_attn.indexer.wk.weight` (×79 layers) | `[128, 6144]` | `torch.bfloat16` | 118.50 MB | Multi Files |
| `model.layers.0-78.self_attn.indexer.wq_b.weight` (×79 layers) | `[4096, 2048]` | `torch.bfloat16` | 1.23 GB | Multi Files |
| `model.layers.0-78.self_attn.kv_a_layernorm.weight` (×79 layers) | `[512]` | `torch.bfloat16` | 79.00 KB | Multi Files |
| `model.layers.0-78.self_attn.kv_a_proj_with_mqa.weight` (×79 layers) | `[576, 6144]` | `torch.bfloat16` | 533.25 MB | Multi Files |
| `model.layers.0-78.self_attn.kv_b_proj.weight` (×79 layers) | `[28672, 512]` | `torch.bfloat16` | 2.16 GB | Multi Files |
| `model.layers.0-78.self_attn.o_proj.weight` (×79 layers) | `[6144, 16384]` | `torch.bfloat16` | 14.81 GB | Multi Files |
| `model.layers.0-78.self_attn.q_a_layernorm.weight` (×79 layers) | `[2048]` | `torch.bfloat16` | 316.00 KB | Multi Files |
| `model.layers.0-78.self_attn.q_a_proj.weight` (×79 layers) | `[2048, 6144]` | `torch.bfloat16` | 1.85 GB | Multi Files |
| `model.layers.0-78.self_attn.q_b_proj.weight` (×79 layers) | `[16384, 2048]` | `torch.bfloat16` | 4.94 GB | Multi Files |
| `model.layers.3-78.mlp.experts.0-255.down_proj.weight` (×76 layers, ×256 experts) | `[6144, 2048]` | `torch.bfloat16` | 456.00 GB | Multi Files |
| `model.layers.3-78.mlp.experts.0-255.gate_proj.weight` (×76 layers, ×256 experts) | `[2048, 6144]` | `torch.bfloat16` | 456.00 GB | Multi Files |
| `model.layers.3-78.mlp.experts.0-255.up_proj.weight` (×76 layers, ×256 experts) | `[2048, 6144]` | `torch.bfloat16` | 456.00 GB | Multi Files |
| `model.layers.3-78.mlp.gate.e_score_correction_bias` (×76 layers) | `[256]` | `torch.float32` | 76.00 KB | Multi Files |
| `model.layers.3-78.mlp.gate.weight` (×76 layers) | `[256, 6144]` | `torch.bfloat16` | 228.00 MB | Multi Files |
| `model.layers.3-78.mlp.shared_experts.down_proj.weight` (×76 layers) | `[6144, 2048]` | `torch.bfloat16` | 1.78 GB | Multi Files |
| `model.layers.3-78.mlp.shared_experts.gate_proj.weight` (×76 layers) | `[2048, 6144]` | `torch.bfloat16` | 1.78 GB | Multi Files |
| `model.layers.3-78.mlp.shared_experts.up_proj.weight` (×76 layers) | `[2048, 6144]` | `torch.bfloat16` | 1.78 GB | Multi Files |
| `model.layers.78.eh_proj.weight` | `[6144, 12288]` | `torch.bfloat16` | 144.00 MB | model-00271-of-00282.safetensors |
| `model.layers.78.enorm.weight` | `[6144]` | `torch.bfloat16` | 12.00 KB | model-00271-of-00282.safetensors |
| `model.layers.78.hnorm.weight` | `[6144]` | `torch.bfloat16` | 12.00 KB | model-00271-of-00282.safetensors |
| `model.layers.78.shared_head.norm.weight` | `[6144]` | `torch.bfloat16` | 12.00 KB | model-00274-of-00282.safetensors |
| `model.norm.weight` | `[6144]` | `torch.bfloat16` | 12.00 KB | model-00282-of-00282.safetensors |

</details>

