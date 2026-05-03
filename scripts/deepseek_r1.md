# 模型信息报告

- **模型路径**: `/nfs/volume-1615-2/models/DeepSeek-R1`

# 模型配置

- **模型类型**: `DeepseekV3Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 7168
- **层数**: 61
- **注意力头数**: 128
- **词表大小**: 129280
- **中间层大小**: 18432

<details><summary>完整配置</summary>

```
DeepseekV3Config {
  "architectures": [
    "DeepseekV3ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "auto_map": {
    "AutoConfig": "configuration_deepseek.DeepseekV3Config",
    "AutoModel": "modeling_deepseek.DeepseekV3Model",
    "AutoModelForCausalLM": "modeling_deepseek.DeepseekV3ForCausalLM"
  },
  "aux_loss_alpha": 0.001,
  "bos_token_id": 0,
  "dtype": "bfloat16",
  "eos_token_id": 1,
  "ep_size": 1,
  "first_k_dense_replace": 3,
  "head_dim": 64,
  "hidden_act": "silu",
  "hidden_size": 7168,
  "initializer_range": 0.02,
  "intermediate_size": 18432,
  "kv_lora_rank": 512,
  "max_position_embeddings": 163840,
  "model_type": "deepseek_v3",
  "moe_intermediate_size": 2048,
  "moe_layer_freq": 1,
  "n_group": 8,
  "n_routed_experts": 256,
  "n_shared_experts": 1,
  "norm_topk_prob": true,
  "num_attention_heads": 128,
  "num_experts_per_tok": 8,
  "num_hidden_layers": 61,
  "num_key_value_heads": 128,
  "num_nextn_predict_layers": 1,
  "pretraining_tp": 1,
  "q_lora_rank": 1536,
  "qk_head_dim": 192,
  "qk_nope_head_dim": 128,
  "qk_rope_head_dim": 64,
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
  "rope_interleave": true,
  "rope_scaling": {
    "beta_fast": 32.0,
    "beta_slow": 1.0,
    "factor": 40.0,
    "mscale": 1.0,
    "mscale_all_dim": 1.0,
    "original_max_position_embeddings": 4096,
    "rope_type": "yarn",
    "type": "yarn"
  },
  "rope_theta": 10000,
  "routed_scaling_factor": 2.5,
  "scoring_func": "sigmoid",
  "seq_aux": true,
  "tie_word_embeddings": false,
  "topk_group": 4,
  "topk_method": "noaux_tc",
  "transformers_version": "4.57.1",
  "use_cache": true,
  "v_head_dim": 128,
  "vocab_size": 129280
}

```

</details>

# 模型结构

**模型类**: `DeepseekV3Model`

```
DeepseekV3Model(
  (embed_tokens): Embedding(129280, 7168)
  (layers): ModuleList(
    (0-2): 3 x DeepseekV3DecoderLayer(
      (self_attn): DeepseekV3Attention(
        (q_a_proj): Linear(in_features=7168, out_features=1536, bias=False)
        (q_a_layernorm): DeepseekV3RMSNorm((1536,), eps=1e-06)
        (q_b_proj): Linear(in_features=1536, out_features=24576, bias=False)
        (kv_a_proj_with_mqa): Linear(in_features=7168, out_features=576, bias=False)
        (kv_a_layernorm): DeepseekV3RMSNorm((512,), eps=1e-06)
        (kv_b_proj): Linear(in_features=512, out_features=32768, bias=False)
        (o_proj): Linear(in_features=16384, out_features=7168, bias=False)
      )
      (mlp): DeepseekV3MLP(
        (gate_proj): Linear(in_features=7168, out_features=18432, bias=False)
        (up_proj): Linear(in_features=7168, out_features=18432, bias=False)
        (down_proj): Linear(in_features=18432, out_features=7168, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): DeepseekV3RMSNorm((7168,), eps=1e-06)
      (post_attention_layernorm): DeepseekV3RMSNorm((7168,), eps=1e-06)
    )
    (3-60): 58 x DeepseekV3DecoderLayer(
      (self_attn): DeepseekV3Attention(
        (q_a_proj): Linear(in_features=7168, out_features=1536, bias=False)
        (q_a_layernorm): DeepseekV3RMSNorm((1536,), eps=1e-06)
        (q_b_proj): Linear(in_features=1536, out_features=24576, bias=False)
        (kv_a_proj_with_mqa): Linear(in_features=7168, out_features=576, bias=False)
        (kv_a_layernorm): DeepseekV3RMSNorm((512,), eps=1e-06)
        (kv_b_proj): Linear(in_features=512, out_features=32768, bias=False)
        (o_proj): Linear(in_features=16384, out_features=7168, bias=False)
      )
      (mlp): DeepseekV3MoE(
        (experts): ModuleList(
          (0-255): 256 x DeepseekV3MLP(
            (gate_proj): Linear(in_features=7168, out_features=2048, bias=False)
            (up_proj): Linear(in_features=7168, out_features=2048, bias=False)
            (down_proj): Linear(in_features=2048, out_features=7168, bias=False)
            (act_fn): SiLUActivation()
          )
        )
        (gate): DeepseekV3TopkRouter()
        (shared_experts): DeepseekV3MLP(
          (gate_proj): Linear(in_features=7168, out_features=2048, bias=False)
          (up_proj): Linear(in_features=7168, out_features=2048, bias=False)
          (down_proj): Linear(in_features=2048, out_features=7168, bias=False)
          (act_fn): SiLUActivation()
        )
      )
      (input_layernorm): DeepseekV3RMSNorm((7168,), eps=1e-06)
      (post_attention_layernorm): DeepseekV3RMSNorm((7168,), eps=1e-06)
    )
  )
  (norm): DeepseekV3RMSNorm((7168,), eps=1e-06)
  (rotary_emb): DeepseekV3RotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 163 个 `safetensors` 文件
- **文件总大小**: 641.30 GB
- **权重张量数**: 91,991
- **参数总量**: 684,531,386,000
- **张量累计大小**: 641.29 GB
- **压缩**: 91991 → 43 行 (合并相同 shape/dtype 的 experts 和 layers)

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[129280, 7168]` | `torch.bfloat16` | 1.73 GB | model-00160-of-000163.safetensors |
| `model.embed_tokens.weight` | `[129280, 7168]` | `torch.bfloat16` | 1.73 GB | model-00001-of-000163.safetensors |
| `model.layers.0-2.mlp.down_proj.weight` (×3 layers) | `[7168, 18432]` | `torch.float8_e4m3fn` | 378.00 MB | model-00001-of-000163.safetensors |
| `model.layers.0-2.mlp.down_proj.weight_scale_inv` (×3 layers) | `[56, 144]` | `torch.float32` | 94.50 KB | model-00001-of-000163.safetensors |
| `model.layers.0-2.mlp.gate_proj.weight` (×3 layers) | `[18432, 7168]` | `torch.float8_e4m3fn` | 378.00 MB | model-00001-of-000163.safetensors |
| `model.layers.0-2.mlp.gate_proj.weight_scale_inv` (×3 layers) | `[144, 56]` | `torch.float32` | 94.50 KB | model-00001-of-000163.safetensors |
| `model.layers.0-2.mlp.up_proj.weight` (×3 layers) | `[18432, 7168]` | `torch.float8_e4m3fn` | 378.00 MB | model-00001-of-000163.safetensors |
| `model.layers.0-2.mlp.up_proj.weight_scale_inv` (×3 layers) | `[144, 56]` | `torch.float32` | 94.50 KB | model-00001-of-000163.safetensors |
| `model.layers.0-61.input_layernorm.weight` (×62 layers) | `[7168]` | `torch.bfloat16` | 868.00 KB | Multi Files |
| `model.layers.0-61.post_attention_layernorm.weight` (×62 layers) | `[7168]` | `torch.bfloat16` | 868.00 KB | Multi Files |
| `model.layers.0-61.self_attn.kv_a_layernorm.weight` (×62 layers) | `[512]` | `torch.bfloat16` | 62.00 KB | Multi Files |
| `model.layers.0-61.self_attn.kv_a_proj_with_mqa.weight` (×62 layers) | `[576, 7168]` | `torch.float8_e4m3fn` | 244.12 MB | Multi Files |
| `model.layers.0-61.self_attn.kv_a_proj_with_mqa.weight_scale_inv` (×62 layers) | `[5, 56]` | `torch.float32` | 67.81 KB | Multi Files |
| `model.layers.0-61.self_attn.kv_b_proj.weight` (×62 layers) | `[32768, 512]` | `torch.float8_e4m3fn` | 992.00 MB | Multi Files |
| `model.layers.0-61.self_attn.kv_b_proj.weight_scale_inv` (×62 layers) | `[256, 4]` | `torch.float32` | 248.00 KB | Multi Files |
| `model.layers.0-61.self_attn.o_proj.weight` (×62 layers) | `[7168, 16384]` | `torch.float8_e4m3fn` | 6.78 GB | Multi Files |
| `model.layers.0-61.self_attn.o_proj.weight_scale_inv` (×62 layers) | `[56, 128]` | `torch.float32` | 1.70 MB | Multi Files |
| `model.layers.0-61.self_attn.q_a_layernorm.weight` (×62 layers) | `[1536]` | `torch.bfloat16` | 186.00 KB | Multi Files |
| `model.layers.0-61.self_attn.q_a_proj.weight` (×62 layers) | `[1536, 7168]` | `torch.float8_e4m3fn` | 651.00 MB | Multi Files |
| `model.layers.0-61.self_attn.q_a_proj.weight_scale_inv` (×62 layers) | `[12, 56]` | `torch.float32` | 162.75 KB | Multi Files |
| `model.layers.0-61.self_attn.q_b_proj.weight` (×62 layers) | `[24576, 1536]` | `torch.float8_e4m3fn` | 2.18 GB | Multi Files |
| `model.layers.0-61.self_attn.q_b_proj.weight_scale_inv` (×62 layers) | `[192, 12]` | `torch.float32` | 558.00 KB | Multi Files |
| `model.layers.3-61.mlp.experts.0-255.down_proj.weight` (×59 layers, ×256 experts) | `[7168, 2048]` | `torch.float8_e4m3fn` | 206.50 GB | Multi Files |
| `model.layers.3-61.mlp.experts.0-255.down_proj.weight_scale_inv` (×59 layers, ×256 experts) | `[56, 16]` | `torch.float32` | 51.62 MB | Multi Files |
| `model.layers.3-61.mlp.experts.0-255.gate_proj.weight` (×59 layers, ×256 experts) | `[2048, 7168]` | `torch.float8_e4m3fn` | 206.50 GB | Multi Files |
| `model.layers.3-61.mlp.experts.0-255.gate_proj.weight_scale_inv` (×59 layers, ×256 experts) | `[16, 56]` | `torch.float32` | 51.62 MB | Multi Files |
| `model.layers.3-61.mlp.experts.0-255.up_proj.weight` (×59 layers, ×256 experts) | `[2048, 7168]` | `torch.float8_e4m3fn` | 206.50 GB | Multi Files |
| `model.layers.3-61.mlp.experts.0-255.up_proj.weight_scale_inv` (×59 layers, ×256 experts) | `[16, 56]` | `torch.float32` | 51.62 MB | Multi Files |
| `model.layers.3-61.mlp.gate.e_score_correction_bias` (×59 layers) | `[256]` | `torch.float32` | 59.00 KB | Multi Files |
| `model.layers.3-61.mlp.gate.weight` (×59 layers) | `[256, 7168]` | `torch.bfloat16` | 206.50 MB | Multi Files |
| `model.layers.3-61.mlp.shared_experts.down_proj.weight` (×59 layers) | `[7168, 2048]` | `torch.float8_e4m3fn` | 826.00 MB | Multi Files |
| `model.layers.3-61.mlp.shared_experts.down_proj.weight_scale_inv` (×59 layers) | `[56, 16]` | `torch.float32` | 206.50 KB | Multi Files |
| `model.layers.3-61.mlp.shared_experts.gate_proj.weight` (×59 layers) | `[2048, 7168]` | `torch.float8_e4m3fn` | 826.00 MB | Multi Files |
| `model.layers.3-61.mlp.shared_experts.gate_proj.weight_scale_inv` (×59 layers) | `[16, 56]` | `torch.float32` | 206.50 KB | Multi Files |
| `model.layers.3-61.mlp.shared_experts.up_proj.weight` (×59 layers) | `[2048, 7168]` | `torch.float8_e4m3fn` | 826.00 MB | Multi Files |
| `model.layers.3-61.mlp.shared_experts.up_proj.weight_scale_inv` (×59 layers) | `[16, 56]` | `torch.float32` | 206.50 KB | Multi Files |
| `model.layers.61.eh_proj.weight` (×1 layers) | `[7168, 14336]` | `torch.bfloat16` | 196.00 MB | model-00163-of-000163.safetensors |
| `model.layers.61.embed_tokens.weight` (×1 layers) | `[129280, 7168]` | `torch.bfloat16` | 1.73 GB | model-00163-of-000163.safetensors |
| `model.layers.61.enorm.weight` (×1 layers) | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00163-of-000163.safetensors |
| `model.layers.61.hnorm.weight` (×1 layers) | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00163-of-000163.safetensors |
| `model.layers.61.shared_head.head.weight` (×1 layers) | `[129280, 7168]` | `torch.bfloat16` | 1.73 GB | model-00163-of-000163.safetensors |
| `model.layers.61.shared_head.norm.weight` (×1 layers) | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00163-of-000163.safetensors |
| `model.norm.weight` | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00160-of-000163.safetensors |

</details>

