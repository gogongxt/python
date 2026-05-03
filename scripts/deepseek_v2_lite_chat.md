# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/user/gogongxt/models/DeepSeek-V2-Lite-Chat`

# 模型配置

- **模型类型**: `DeepseekV2Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 2048
- **层数**: 27
- **注意力头数**: 16
- **词表大小**: 102400
- **中间层大小**: 10944

<details><summary>完整配置</summary>

```
DeepseekV2Config {
  "architectures": [
    "DeepseekV2ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "auto_map": {
    "AutoConfig": "configuration_deepseek.DeepseekV2Config",
    "AutoModel": "modeling_deepseek.DeepseekV2Model",
    "AutoModelForCausalLM": "modeling_deepseek.DeepseekV2ForCausalLM"
  },
  "aux_loss_alpha": 0.001,
  "bos_token_id": 100000,
  "dtype": "bfloat16",
  "eos_token_id": 100001,
  "first_k_dense_replace": 1,
  "head_dim": 64,
  "hidden_act": "silu",
  "hidden_size": 2048,
  "initializer_range": 0.02,
  "intermediate_size": 10944,
  "kv_lora_rank": 512,
  "max_position_embeddings": 163840,
  "mlp_bias": false,
  "model_type": "deepseek_v2",
  "moe_intermediate_size": 1408,
  "moe_layer_freq": 1,
  "n_group": 1,
  "n_routed_experts": 64,
  "n_shared_experts": 2,
  "norm_topk_prob": false,
  "num_attention_heads": 16,
  "num_experts_per_tok": 6,
  "num_hidden_layers": 27,
  "num_key_value_heads": 16,
  "pad_token_id": null,
  "pretraining_tp": 1,
  "q_lora_rank": null,
  "qk_nope_head_dim": 128,
  "qk_rope_head_dim": 64,
  "rms_norm_eps": 1e-06,
  "rope_parameters": {
    "beta_fast": 32,
    "beta_slow": 1,
    "factor": 40,
    "mscale": 0.707,
    "mscale_all_dim": 0.707,
    "original_max_position_embeddings": 4096,
    "rope_theta": 10000,
    "rope_type": "yarn",
    "type": "yarn"
  },
  "routed_scaling_factor": 1.0,
  "scoring_func": "softmax",
  "seq_aux": true,
  "tie_word_embeddings": false,
  "topk_group": 1,
  "topk_method": "greedy",
  "transformers_version": "5.7.0",
  "use_cache": true,
  "v_head_dim": 128,
  "vocab_size": 102400
}

```

</details>

# 模型结构

**模型类**: `DeepseekV2Model`

```
DeepseekV2Model(
  (embed_tokens): Embedding(102400, 2048)
  (layers): ModuleList(
    (0): DeepseekV2DecoderLayer(
      (self_attn): DeepseekV2Attention(
        (q_proj): Linear(in_features=2048, out_features=3072, bias=False)
        (kv_a_proj_with_mqa): Linear(in_features=2048, out_features=576, bias=False)
        (kv_a_layernorm): DeepseekV2RMSNorm((512,), eps=1e-06)
        (kv_b_proj): Linear(in_features=512, out_features=4096, bias=False)
        (o_proj): Linear(in_features=2048, out_features=2048, bias=False)
      )
      (mlp): DeepseekV2MLP(
        (gate_proj): Linear(in_features=2048, out_features=10944, bias=False)
        (up_proj): Linear(in_features=2048, out_features=10944, bias=False)
        (down_proj): Linear(in_features=10944, out_features=2048, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): DeepseekV2RMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): DeepseekV2RMSNorm((2048,), eps=1e-06)
    )
    (1-26): 26 x DeepseekV2DecoderLayer(
      (self_attn): DeepseekV2Attention(
        (q_proj): Linear(in_features=2048, out_features=3072, bias=False)
        (kv_a_proj_with_mqa): Linear(in_features=2048, out_features=576, bias=False)
        (kv_a_layernorm): DeepseekV2RMSNorm((512,), eps=1e-06)
        (kv_b_proj): Linear(in_features=512, out_features=4096, bias=False)
        (o_proj): Linear(in_features=2048, out_features=2048, bias=False)
      )
      (mlp): DeepseekV2Moe(
        (experts): DeepseekV2Experts(
          (act_fn): SiLUActivation()
        )
        (gate): Linear(in_features=2048, out_features=64, bias=False)
        (shared_experts): DeepseekV2MLP(
          (gate_proj): Linear(in_features=2048, out_features=2816, bias=False)
          (up_proj): Linear(in_features=2048, out_features=2816, bias=False)
          (down_proj): Linear(in_features=2816, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
      )
      (input_layernorm): DeepseekV2RMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): DeepseekV2RMSNorm((2048,), eps=1e-06)
    )
  )
  (norm): DeepseekV2RMSNorm((2048,), eps=1e-06)
  (rotary_emb): DeepseekV2RotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 4 个 `safetensors` 文件
- **文件总大小**: 29.26 GB
- **权重张量数**: 5,291
- **参数总量**: 15,706,484,224
- **张量累计大小**: 29.26 GB
- **压缩**: 5291 → 20 行 (合并相同 shape/dtype 的 experts 和 layers)

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[102400, 2048]` | `torch.bfloat16` | 400.00 MB | model-00001-of-000004.safetensors |
| `model.embed_tokens.weight` | `[102400, 2048]` | `torch.bfloat16` | 400.00 MB | model-00001-of-000004.safetensors |
| `model.layers.0-26.input_layernorm.weight` (×27 layers) | `[2048]` | `torch.bfloat16` | 108.00 KB | Multi Files |
| `model.layers.0-26.post_attention_layernorm.weight` (×27 layers) | `[2048]` | `torch.bfloat16` | 108.00 KB | Multi Files |
| `model.layers.0-26.self_attn.kv_a_layernorm.weight` (×27 layers) | `[512]` | `torch.bfloat16` | 27.00 KB | Multi Files |
| `model.layers.0-26.self_attn.kv_a_proj_with_mqa.weight` (×27 layers) | `[576, 2048]` | `torch.bfloat16` | 60.75 MB | Multi Files |
| `model.layers.0-26.self_attn.kv_b_proj.weight` (×27 layers) | `[4096, 512]` | `torch.bfloat16` | 108.00 MB | Multi Files |
| `model.layers.0-26.self_attn.o_proj.weight` (×27 layers) | `[2048, 2048]` | `torch.bfloat16` | 216.00 MB | Multi Files |
| `model.layers.0-26.self_attn.q_proj.weight` (×27 layers) | `[3072, 2048]` | `torch.bfloat16` | 324.00 MB | Multi Files |
| `model.layers.0.mlp.down_proj.weight` (×1 layers) | `[2048, 10944]` | `torch.bfloat16` | 42.75 MB | model-00001-of-000004.safetensors |
| `model.layers.0.mlp.gate_proj.weight` (×1 layers) | `[10944, 2048]` | `torch.bfloat16` | 42.75 MB | model-00001-of-000004.safetensors |
| `model.layers.0.mlp.up_proj.weight` (×1 layers) | `[10944, 2048]` | `torch.bfloat16` | 42.75 MB | model-00001-of-000004.safetensors |
| `model.layers.1-26.mlp.experts.0-63.down_proj.weight` (×26 layers, ×64 experts) | `[2048, 1408]` | `torch.bfloat16` | 8.94 GB | Multi Files |
| `model.layers.1-26.mlp.experts.0-63.gate_proj.weight` (×26 layers, ×64 experts) | `[1408, 2048]` | `torch.bfloat16` | 8.94 GB | Multi Files |
| `model.layers.1-26.mlp.experts.0-63.up_proj.weight` (×26 layers, ×64 experts) | `[1408, 2048]` | `torch.bfloat16` | 8.94 GB | Multi Files |
| `model.layers.1-26.mlp.gate.weight` (×26 layers) | `[64, 2048]` | `torch.bfloat16` | 6.50 MB | Multi Files |
| `model.layers.1-26.mlp.shared_experts.down_proj.weight` (×26 layers) | `[2048, 2816]` | `torch.bfloat16` | 286.00 MB | Multi Files |
| `model.layers.1-26.mlp.shared_experts.gate_proj.weight` (×26 layers) | `[2816, 2048]` | `torch.bfloat16` | 286.00 MB | Multi Files |
| `model.layers.1-26.mlp.shared_experts.up_proj.weight` (×26 layers) | `[2816, 2048]` | `torch.bfloat16` | 286.00 MB | Multi Files |
| `model.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00001-of-000004.safetensors |

</details>

