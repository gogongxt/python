# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/MiniMax-M2.7`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/MiniMax-M2.7/config.json`

```json

{
  "architectures": [
    "MiniMaxM2ForCausalLM"
  ],
  "attn_type_list": [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
  ],
  "auto_map": {
    "AutoConfig": "configuration_minimax_m2.MiniMaxM2Config",
    "AutoModelForCausalLM": "modeling_minimax_m2.MiniMaxM2ForCausalLM"
  },
  "dtype": "bfloat16",
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 3072,
  "intermediate_size": 1536,
  "max_position_embeddings": 204800,
  "model_type": "minimax_m2",
  "mtp_transformer_layers": 1,
  "num_attention_heads": 48,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 62,
  "num_key_value_heads": 8,
  "num_local_experts": 256,
  "num_mtp_modules": 3,
  "qk_norm_type": "per_layer",
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "float8_e4m3fn",
    "quant_method": "fp8",
    "weight_block_size": [
      128,
      128
    ],
    "modules_to_not_convert": [
      "gate",
      "e_score_correction_bias",
      "lm_head"
    ]
  },
  "rms_norm_eps": 1e-06,
  "rope_theta": 5000000,
  "rotary_dim": 64,
  "scoring_func": "sigmoid",
  "shared_intermediate_size": 0,
  "tie_word_embeddings": false,
  "transformers_version": "4.46.1",
  "use_cache": true,
  "use_mtp": true,
  "use_qk_norm": true,
  "use_routing_bias": true,
  "vocab_size": 200064
}

```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `MiniMaxM2Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 3072
- **层数**: 62
- **注意力头数**: 48
- **词表大小**: 200064
- **中间层大小**: 1536

```
MiniMaxM2Config {
  "architectures": [
    "MiniMaxM2ForCausalLM"
  ],
  "attention_dropout": 0.0,
  "attn_type_list": [
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
  ],
  "auto_map": {
    "AutoConfig": "configuration_minimax_m2.MiniMaxM2Config",
    "AutoModelForCausalLM": "modeling_minimax_m2.MiniMaxM2ForCausalLM"
  },
  "bos_token_id": 1,
  "dtype": "bfloat16",
  "eos_token_id": 2,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 3072,
  "initializer_range": 0.02,
  "intermediate_size": 1536,
  "max_position_embeddings": 204800,
  "model_type": "minimax_m2",
  "mtp_transformer_layers": 1,
  "num_attention_heads": 48,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 62,
  "num_key_value_heads": 8,
  "num_local_experts": 256,
  "num_mtp_modules": 3,
  "output_router_logits": false,
  "pad_token_id": null,
  "partial_rotary_factor": 0.5,
  "qk_norm_type": "per_layer",
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "float8_e4m3fn",
    "modules_to_not_convert": [
      "gate",
      "e_score_correction_bias",
      "lm_head"
    ],
    "quant_method": "fp8",
    "weight_block_size": [
      128,
      128
    ]
  },
  "rms_norm_eps": 1e-06,
  "rope_theta": 5000000,
  "rotary_dim": 64,
  "router_aux_loss_coef": 0.001,
  "router_jitter_noise": 0.0,
  "scoring_func": "sigmoid",
  "shared_intermediate_size": 0,
  "sliding_window": null,
  "tie_word_embeddings": false,
  "transformers_version": "5.7.0",
  "use_cache": true,
  "use_mtp": true,
  "use_qk_norm": true,
  "use_routing_bias": true,
  "vocab_size": 200064
}

```

</details>

# 模型结构

**模型类**: `MiniMaxM2Model`

```
MiniMaxM2Model(
  (embed_tokens): Embedding(200064, 3072)
  (layers): ModuleList(
    (0-61): 62 x MiniMaxM2DecoderLayer(
      (self_attn): MiniMaxM2Attention(
        (q_proj): Linear(in_features=3072, out_features=6144, bias=False)
        (k_proj): Linear(in_features=3072, out_features=1024, bias=False)
        (v_proj): Linear(in_features=3072, out_features=1024, bias=False)
        (o_proj): Linear(in_features=6144, out_features=3072, bias=False)
        (q_norm): MiniMaxM2RMSNorm((6144,), eps=1e-06)
        (k_norm): MiniMaxM2RMSNorm((1024,), eps=1e-06)
      )
      (mlp): MiniMaxM2SparseMoeBlock(
        (gate): MiniMaxM2TopKRouter()
        (experts): MiniMaxM2Experts(
          (act_fn): SiLUActivation()
        )
      )
      (input_layernorm): MiniMaxM2RMSNorm((3072,), eps=1e-06)
      (post_attention_layernorm): MiniMaxM2RMSNorm((3072,), eps=1e-06)
    )
  )
  (norm): MiniMaxM2RMSNorm((3072,), eps=1e-06)
  (rotary_emb): MiniMaxM2RotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 125 个 `safetensors` 文件
- **文件总大小**: 214.33 GB
- **权重张量数**: 96,103
- **参数总量**: 228,703,644,928
- **张量累计大小**: 214.32 GB
- **压缩**: 96103 → 23 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[200064, 3072]` | `torch.bfloat16` | 1.14 GB | model-00124-of-00130.safetensors |
| `model.embed_tokens.weight` | `[200064, 3072]` | `torch.bfloat16` | 1.14 GB | model-00000-of-00130.safetensors |
| `model.layers.0-61.block_sparse_moe.e_score_correction_bias` (×62 layers) | `[256]` | `torch.float32` | 62.00 KB | Multi Files |
| `model.layers.0-61.block_sparse_moe.experts.0-255.w1.weight` (×62 layers, ×256 experts) | `[1536, 3072]` | `torch.float8_e4m3fn` | 69.75 GB | Multi Files |
| `model.layers.0-61.block_sparse_moe.experts.0-255.w1.weight_scale_inv` (×62 layers, ×256 experts) | `[12, 24]` | `torch.float32` | 17.44 MB | Multi Files |
| `model.layers.0-61.block_sparse_moe.experts.0-255.w2.weight` (×62 layers, ×256 experts) | `[3072, 1536]` | `torch.float8_e4m3fn` | 69.75 GB | Multi Files |
| `model.layers.0-61.block_sparse_moe.experts.0-255.w2.weight_scale_inv` (×62 layers, ×256 experts) | `[24, 12]` | `torch.float32` | 17.44 MB | Multi Files |
| `model.layers.0-61.block_sparse_moe.experts.0-255.w3.weight` (×62 layers, ×256 experts) | `[1536, 3072]` | `torch.float8_e4m3fn` | 69.75 GB | Multi Files |
| `model.layers.0-61.block_sparse_moe.experts.0-255.w3.weight_scale_inv` (×62 layers, ×256 experts) | `[12, 24]` | `torch.float32` | 17.44 MB | Multi Files |
| `model.layers.0-61.block_sparse_moe.gate.weight` (×62 layers) | `[256, 3072]` | `torch.float32` | 186.00 MB | Multi Files |
| `model.layers.0-61.input_layernorm.weight` (×62 layers) | `[3072]` | `torch.bfloat16` | 372.00 KB | Multi Files |
| `model.layers.0-61.post_attention_layernorm.weight` (×62 layers) | `[3072]` | `torch.bfloat16` | 372.00 KB | Multi Files |
| `model.layers.0-61.self_attn.k_norm.weight` (×62 layers) | `[1024]` | `torch.bfloat16` | 124.00 KB | Multi Files |
| `model.layers.0-61.self_attn.k_proj.weight` (×62 layers) | `[1024, 3072]` | `torch.float8_e4m3fn` | 186.00 MB | Multi Files |
| `model.layers.0-61.self_attn.k_proj.weight_scale_inv` (×62 layers) | `[8, 24]` | `torch.float32` | 46.50 KB | Multi Files |
| `model.layers.0-61.self_attn.o_proj.weight` (×62 layers) | `[3072, 6144]` | `torch.float8_e4m3fn` | 1.09 GB | Multi Files |
| `model.layers.0-61.self_attn.o_proj.weight_scale_inv` (×62 layers) | `[24, 48]` | `torch.float32` | 279.00 KB | Multi Files |
| `model.layers.0-61.self_attn.q_norm.weight` (×62 layers) | `[6144]` | `torch.bfloat16` | 744.00 KB | Multi Files |
| `model.layers.0-61.self_attn.q_proj.weight` (×62 layers) | `[6144, 3072]` | `torch.float8_e4m3fn` | 1.09 GB | Multi Files |
| `model.layers.0-61.self_attn.q_proj.weight_scale_inv` (×62 layers) | `[48, 24]` | `torch.float32` | 279.00 KB | Multi Files |
| `model.layers.0-61.self_attn.v_proj.weight` (×62 layers) | `[1024, 3072]` | `torch.float8_e4m3fn` | 186.00 MB | Multi Files |
| `model.layers.0-61.self_attn.v_proj.weight_scale_inv` (×62 layers) | `[8, 24]` | `torch.float32` | 46.50 KB | Multi Files |
| `model.norm.weight` | `[3072]` | `torch.bfloat16` | 6.00 KB | model-00124-of-00130.safetensors |

</details>

