# 模型信息报告

- **模型路径**: `/nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-V3.2`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llab-cold/model/deepseek-ai/DeepSeek-V3.2/config.json`

```json

{
  "architectures": [
    "DeepseekV32ForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 0,
  "eos_token_id": 1,
  "ep_size": 1,
  "first_k_dense_replace": 3,
  "hidden_act": "silu",
  "hidden_size": 7168,
  "index_head_dim": 128,
  "index_n_heads": 64,
  "index_topk": 2048,
  "initializer_range": 0.02,
  "intermediate_size": 18432,
  "kv_lora_rank": 512,
  "max_position_embeddings": 163840,
  "model_type": "deepseek_v32",
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
  "q_lora_rank": 1536,
  "qk_nope_head_dim": 128,
  "qk_rope_head_dim": 64,
  "quantization_config": {
    "activation_scheme": "dynamic",
    "fmt": "e4m3",
    "quant_method": "fp8",
    "scale_fmt": "ue8m0",
    "weight_block_size": [
      128,
      128
    ]
  },
  "rms_norm_eps": 1e-06,
  "rope_scaling": {
    "beta_fast": 32,
    "beta_slow": 1,
    "factor": 40,
    "mscale": 1.0,
    "mscale_all_dim": 1.0,
    "original_max_position_embeddings": 4096,
    "type": "yarn"
  },
  "rope_theta": 10000,
  "routed_scaling_factor": 2.5,
  "scoring_func": "sigmoid",
  "tie_word_embeddings": false,
  "topk_group": 4,
  "topk_method": "noaux_tc",
  "torch_dtype": "bfloat16",
  "transformers_version": "4.44.2",
  "use_cache": true,
  "v_head_dim": 128,
  "vocab_size": 129280
}

```
</details>

<details><summary>Transformers 配置</summary>

**错误**: Transformers 解析配置失败 - `The checkpoint you are trying to load has model type `deepseek_v32` but Transformers does not recognize this architecture. This could be because of an issue with the checkpoint, or because your version of Transformers is out of date.

You can update Transformers with the command `pip install --upgrade transformers`. If this does not work, and the checkpoint is very new, then there may not be a release version that supports this model yet. In this case, you can get the most up-to-date code by installing Transformers from source with the command `pip install git+https://github.com/huggingface/transformers.git``

</details>

# 模型结构

**错误**: 解析模型结构失败

# 权重统计

- **权重文件**: 163 个 `safetensors` 文件
- **文件总大小**: 642.13 GB
- **权重张量数**: 92,425
- **参数总量**: 685,396,921,376
- **张量累计大小**: 642.12 GB
- **压缩**: 92425 → 50 行

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
| `model.layers.0-61.input_layernorm.weight` (×62 layers) | `[7168]` | `torch.float32` | 1.70 MB | Multi Files |
| `model.layers.0-61.post_attention_layernorm.weight` (×62 layers) | `[7168]` | `torch.float32` | 1.70 MB | Multi Files |
| `model.layers.0-61.self_attn.indexer.k_norm.bias` (×62 layers) | `[128]` | `torch.float32` | 31.00 KB | Multi Files |
| `model.layers.0-61.self_attn.indexer.k_norm.weight` (×62 layers) | `[128]` | `torch.float32` | 31.00 KB | Multi Files |
| `model.layers.0-61.self_attn.indexer.weights_proj.weight` (×62 layers) | `[64, 7168]` | `torch.bfloat16` | 54.25 MB | Multi Files |
| `model.layers.0-61.self_attn.indexer.wk.weight` (×62 layers) | `[128, 7168]` | `torch.float8_e4m3fn` | 54.25 MB | Multi Files |
| `model.layers.0-61.self_attn.indexer.wk.weight_scale_inv` (×62 layers) | `[1, 56]` | `torch.float32` | 13.56 KB | Multi Files |
| `model.layers.0-61.self_attn.indexer.wq_b.weight` (×62 layers) | `[8192, 1536]` | `torch.float8_e4m3fn` | 744.00 MB | Multi Files |
| `model.layers.0-61.self_attn.indexer.wq_b.weight_scale_inv` (×62 layers) | `[64, 12]` | `torch.float32` | 186.00 KB | Multi Files |
| `model.layers.0-61.self_attn.kv_a_layernorm.weight` (×62 layers) | `[512]` | `torch.float32` | 124.00 KB | Multi Files |
| `model.layers.0-61.self_attn.kv_a_proj_with_mqa.weight` (×62 layers) | `[576, 7168]` | `torch.float8_e4m3fn` | 244.12 MB | Multi Files |
| `model.layers.0-61.self_attn.kv_a_proj_with_mqa.weight_scale_inv` (×62 layers) | `[5, 56]` | `torch.float32` | 67.81 KB | Multi Files |
| `model.layers.0-61.self_attn.kv_b_proj.weight` (×62 layers) | `[32768, 512]` | `torch.float8_e4m3fn` | 992.00 MB | Multi Files |
| `model.layers.0-61.self_attn.kv_b_proj.weight_scale_inv` (×62 layers) | `[256, 4]` | `torch.float32` | 248.00 KB | Multi Files |
| `model.layers.0-61.self_attn.o_proj.weight` (×62 layers) | `[7168, 16384]` | `torch.float8_e4m3fn` | 6.78 GB | Multi Files |
| `model.layers.0-61.self_attn.o_proj.weight_scale_inv` (×62 layers) | `[56, 128]` | `torch.float32` | 1.70 MB | Multi Files |
| `model.layers.0-61.self_attn.q_a_layernorm.weight` (×62 layers) | `[1536]` | `torch.float32` | 372.00 KB | Multi Files |
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
| `model.layers.61.eh_proj.weight` | `[7168, 14336]` | `torch.bfloat16` | 196.00 MB | model-00163-of-000163.safetensors |
| `model.layers.61.embed_tokens.weight` | `[129280, 7168]` | `torch.bfloat16` | 1.73 GB | model-00163-of-000163.safetensors |
| `model.layers.61.enorm.weight` | `[7168]` | `torch.float32` | 28.00 KB | model-00163-of-000163.safetensors |
| `model.layers.61.hnorm.weight` | `[7168]` | `torch.float32` | 28.00 KB | model-00163-of-000163.safetensors |
| `model.layers.61.shared_head.head.weight` | `[129280, 7168]` | `torch.bfloat16` | 1.73 GB | model-00163-of-000163.safetensors |
| `model.layers.61.shared_head.norm.weight` | `[7168]` | `torch.float32` | 28.00 KB | model-00163-of-000163.safetensors |
| `model.norm.weight` | `[7168]` | `torch.float32` | 28.00 KB | model-00160-of-000163.safetensors |

</details>

