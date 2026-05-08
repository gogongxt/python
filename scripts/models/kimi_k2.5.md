# 模型信息报告

- **模型路径**: `/nfs/ofs-llab-cold/model/moonshotai/Kimi-K2.5`

# 模型配置

- **模型类型**: `KimiK25Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: N/A
- **层数**: N/A
- **注意力头数**: N/A
- **词表大小**: N/A
- **中间层大小**: N/A

<details><summary>完整配置</summary>

```
KimiK25Config {
  "architectures": [
    "KimiK25ForConditionalGeneration"
  ],
  "auto_map": {
    "AutoConfig": "configuration_kimi_k25.KimiK25Config",
    "AutoModel": "modeling_kimi_k25.KimiK25ForConditionalGeneration",
    "AutoModelForCausalLM": "modeling_kimi_k25.KimiK25ForConditionalGeneration"
  },
  "bos_token_id": 163584,
  "dtype": "bfloat16",
  "eos_token_id": 163585,
  "ignore_index": -100,
  "media_placeholder_token_id": 163605,
  "model_type": "kimi_k25",
  "pad_token_id": 163839,
  "quantization_config": {
    "config_groups": {
      "group_0": {
        "input_activations": null,
        "output_activations": null,
        "targets": [
          "Linear"
        ],
        "weights": {
          "actorder": null,
          "block_structure": null,
          "dynamic": false,
          "group_size": 32,
          "num_bits": 4,
          "observer": "minmax",
          "observer_kwargs": {},
          "strategy": "group",
          "symmetric": true,
          "type": "int"
        }
      }
    },
    "format": "pack-quantized",
    "ignore": [
      "lm_head",
      "re:.*self_attn.*",
      "re:.*shared_experts.*",
      "re:.*mlp\\.(gate|up|gate_up|down)_proj.*"
    ],
    "kv_cache_scheme": null,
    "quant_method": "compressed-tensors",
    "quantization_status": "compressed"
  },
  "text_config": {
    "_name_or_path": "",
    "add_cross_attention": false,
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
    "bos_token_id": 163584,
    "chunk_size_feed_forward": 0,
    "cross_attention_hidden_size": null,
    "decoder_start_token_id": null,
    "dtype": "bfloat16",
    "eos_token_id": 163585,
    "ep_size": 1,
    "finetuning_task": null,
    "first_k_dense_replace": 1,
    "hidden_act": "silu",
    "hidden_size": 7168,
    "id2label": {
      "0": "LABEL_0",
      "1": "LABEL_1"
    },
    "initializer_range": 0.02,
    "intermediate_size": 18432,
    "is_decoder": false,
    "is_encoder_decoder": false,
    "kv_lora_rank": 512,
    "label2id": {
      "LABEL_0": 0,
      "LABEL_1": 1
    },
    "max_position_embeddings": 262144,
    "model_type": "deepseek_v3",
    "moe_intermediate_size": 2048,
    "moe_layer_freq": 1,
    "n_group": 1,
    "n_routed_experts": 384,
    "n_shared_experts": 1,
    "norm_topk_prob": true,
    "num_attention_heads": 64,
    "num_experts_per_tok": 8,
    "num_hidden_layers": 61,
    "num_key_value_heads": 64,
    "num_nextn_predict_layers": 0,
    "output_attentions": false,
    "output_hidden_states": false,
    "pad_token_id": 163839,
    "prefix": null,
    "pretraining_tp": 1,
    "problem_type": null,
    "pruned_heads": {},
    "q_lora_rank": 1536,
    "qk_nope_head_dim": 128,
    "qk_rope_head_dim": 64,
    "quantization_config": {
      "config_groups": {
        "group_0": {
          "input_activations": null,
          "output_activations": null,
          "targets": [
            "Linear"
          ],
          "weights": {
            "actorder": null,
            "block_structure": null,
            "dynamic": false,
            "group_size": 32,
            "num_bits": 4,
            "observer": "minmax",
            "observer_kwargs": {},
            "strategy": "group",
            "symmetric": true,
            "type": "int"
          }
        }
      },
      "format": "pack-quantized",
      "ignore": [
        "lm_head",
        "re:.*self_attn.*",
        "re:.*shared_experts.*",
        "re:.*mlp\\.(gate|up|gate_up|down)_proj.*"
      ],
      "kv_cache_scheme": null,
      "quant_method": "compressed-tensors",
      "quantization_status": "compressed"
    },
    "return_dict": true,
    "rms_norm_eps": 1e-05,
    "rope_parameters": {
      "beta_fast": 32.0,
      "beta_slow": 1.0,
      "factor": 64.0,
      "mscale": 1.0,
      "mscale_all_dim": 1.0,
      "original_max_position_embeddings": 4096,
      "rope_theta": 50000.0,
      "rope_type": "yarn",
      "type": "yarn"
    },
    "rope_theta": 50000.0,
    "routed_scaling_factor": 2.827,
    "scoring_func": "sigmoid",
    "sep_token_id": null,
    "seq_aux": true,
    "task_specific_params": null,
    "tf_legacy_loss": false,
    "tie_encoder_decoder": false,
    "tie_word_embeddings": false,
    "tokenizer_class": null,
    "topk_group": 1,
    "topk_method": "noaux_tc",
    "torchscript": false,
    "use_bfloat16": false,
    "use_cache": true,
    "v_head_dim": 128,
    "vocab_size": 163840
  },
  "tie_word_embeddings": false,
  "transformers_version": "5.7.0",
  "use_unified_vision_chunk": true,
  "video_placeholder": "<|kimi_k25_video_placeholder|>",
  "vision_config": {
    "init_pos_emb_height": 64,
    "init_pos_emb_time": 4,
    "init_pos_emb_width": 64,
    "merge_kernel_size": [
      2,
      2
    ],
    "merge_type": "sd2_tpool",
    "mm_hidden_size": 1152,
    "mm_projector_type": "patchmerger",
    "model_type": "",
    "patch_size": 14,
    "pos_emb_type": "divided_fixed",
    "projector_hidden_act": "gelu",
    "projector_ln_eps": 1e-05,
    "text_hidden_size": 7168,
    "video_attn_type": "spatial_temporal",
    "vt_hidden_size": 1152,
    "vt_intermediate_size": 4304,
    "vt_num_attention_heads": 16,
    "vt_num_hidden_layers": 27
  }
}

```

</details>

# 模型结构

**模型类**: `KimiK25Config` (当前 transformers 版本不支持实例化)

# 权重统计

- **权重文件**: 64 个 `safetensors` 文件
- **文件总大小**: 554.30 GB
- **权重张量数**: 208,550
- **参数总量**: 170,738,182,128
- **张量累计大小**: 554.27 GB
- **压缩**: 208550 → 52 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `language_model.lm_head.weight` | `[163840, 7168]` | `torch.bfloat16` | 2.19 GB | model-00062-of-000064.safetensors |
| `language_model.model.embed_tokens.weight` | `[163840, 7168]` | `torch.bfloat16` | 2.19 GB | model-00062-of-000064.safetensors |
| `language_model.model.layers.0-60.input_layernorm.weight` (×61 layers) | `[7168]` | `torch.bfloat16` | 854.00 KB | Multi Files |
| `language_model.model.layers.0-60.post_attention_layernorm.weight` (×61 layers) | `[7168]` | `torch.bfloat16` | 854.00 KB | Multi Files |
| `language_model.model.layers.0-60.self_attn.kv_a_layernorm.weight` (×61 layers) | `[512]` | `torch.bfloat16` | 61.00 KB | Multi Files |
| `language_model.model.layers.0-60.self_attn.kv_a_proj_with_mqa.weight` (×61 layers) | `[576, 7168]` | `torch.bfloat16` | 480.38 MB | Multi Files |
| `language_model.model.layers.0-60.self_attn.kv_b_proj.weight` (×61 layers) | `[16384, 512]` | `torch.bfloat16` | 976.00 MB | Multi Files |
| `language_model.model.layers.0-60.self_attn.o_proj.weight` (×61 layers) | `[7168, 8192]` | `torch.bfloat16` | 6.67 GB | Multi Files |
| `language_model.model.layers.0-60.self_attn.q_a_layernorm.weight` (×61 layers) | `[1536]` | `torch.bfloat16` | 183.00 KB | Multi Files |
| `language_model.model.layers.0-60.self_attn.q_a_proj.weight` (×61 layers) | `[1536, 7168]` | `torch.bfloat16` | 1.25 GB | Multi Files |
| `language_model.model.layers.0-60.self_attn.q_b_proj.weight` (×61 layers) | `[12288, 1536]` | `torch.bfloat16` | 2.14 GB | Multi Files |
| `language_model.model.layers.0.mlp.down_proj.weight` (×1 layers) | `[7168, 18432]` | `torch.bfloat16` | 252.00 MB | model-00001-of-000064.safetensors |
| `language_model.model.layers.0.mlp.gate_proj.weight` (×1 layers) | `[18432, 7168]` | `torch.bfloat16` | 252.00 MB | model-00001-of-000064.safetensors |
| `language_model.model.layers.0.mlp.up_proj.weight` (×1 layers) | `[18432, 7168]` | `torch.bfloat16` | 252.00 MB | model-00001-of-000064.safetensors |
| `language_model.model.layers.1-60.mlp.experts.0-383.down_proj.weight_packed` (×60 layers, ×384 experts) | `[7168, 256]` | `torch.int32` | 157.50 GB | Multi Files |
| `language_model.model.layers.1-60.mlp.experts.0-383.down_proj.weight_scale` (×60 layers, ×384 experts) | `[7168, 64]` | `torch.bfloat16` | 19.69 GB | Multi Files |
| `language_model.model.layers.1-60.mlp.experts.0-383.down_proj.weight_shape` (×60 layers, ×384 experts) | `[2]` | `torch.int32` | 180.00 KB | Multi Files |
| `language_model.model.layers.1-60.mlp.experts.0-383.gate_proj.weight_packed` (×60 layers, ×384 experts) | `[2048, 896]` | `torch.int32` | 157.50 GB | Multi Files |
| `language_model.model.layers.1-60.mlp.experts.0-383.gate_proj.weight_scale` (×60 layers, ×384 experts) | `[2048, 224]` | `torch.bfloat16` | 19.69 GB | Multi Files |
| `language_model.model.layers.1-60.mlp.experts.0-383.gate_proj.weight_shape` (×60 layers, ×384 experts) | `[2]` | `torch.int32` | 180.00 KB | Multi Files |
| `language_model.model.layers.1-60.mlp.experts.0-383.up_proj.weight_packed` (×60 layers, ×384 experts) | `[2048, 896]` | `torch.int32` | 157.50 GB | Multi Files |
| `language_model.model.layers.1-60.mlp.experts.0-383.up_proj.weight_scale` (×60 layers, ×384 experts) | `[2048, 224]` | `torch.bfloat16` | 19.69 GB | Multi Files |
| `language_model.model.layers.1-60.mlp.experts.0-383.up_proj.weight_shape` (×60 layers, ×384 experts) | `[2]` | `torch.int32` | 180.00 KB | Multi Files |
| `language_model.model.layers.1-60.mlp.gate.e_score_correction_bias` (×60 layers) | `[384]` | `torch.float32` | 90.00 KB | Multi Files |
| `language_model.model.layers.1-60.mlp.gate.weight` (×60 layers) | `[384, 7168]` | `torch.bfloat16` | 315.00 MB | Multi Files |
| `language_model.model.layers.1-60.mlp.shared_experts.down_proj.weight` (×60 layers) | `[7168, 2048]` | `torch.bfloat16` | 1.64 GB | Multi Files |
| `language_model.model.layers.1-60.mlp.shared_experts.gate_proj.weight` (×60 layers) | `[2048, 7168]` | `torch.bfloat16` | 1.64 GB | Multi Files |
| `language_model.model.layers.1-60.mlp.shared_experts.up_proj.weight` (×60 layers) | `[2048, 7168]` | `torch.bfloat16` | 1.64 GB | Multi Files |
| `language_model.model.norm.weight` | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00062-of-000064.safetensors |
| `mm_projector.pre_norm.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00063-of-000064.safetensors |
| `mm_projector.pre_norm.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00063-of-000064.safetensors |
| `mm_projector.proj.0.bias` | `[4608]` | `torch.bfloat16` | 9.00 KB | model-00063-of-000064.safetensors |
| `mm_projector.proj.0.weight` | `[4608, 4608]` | `torch.bfloat16` | 40.50 MB | model-00063-of-000064.safetensors |
| `mm_projector.proj.2.bias` | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00063-of-000064.safetensors |
| `mm_projector.proj.2.weight` | `[7168, 4608]` | `torch.bfloat16` | 63.00 MB | model-00063-of-000064.safetensors |
| `vision_tower.encoder.blocks.0-26.mlp.fc0.bias` (×27 blocks) | `[4304]` | `torch.bfloat16` | 226.97 KB | model-00064-of-000064.safetensors |
| `vision_tower.encoder.blocks.0-26.mlp.fc0.weight` (×27 blocks) | `[4304, 1152]` | `torch.bfloat16` | 255.34 MB | model-00064-of-000064.safetensors |
| `vision_tower.encoder.blocks.0-26.mlp.fc1.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00064-of-000064.safetensors |
| `vision_tower.encoder.blocks.0-26.mlp.fc1.weight` (×27 blocks) | `[1152, 4304]` | `torch.bfloat16` | 255.34 MB | model-00064-of-000064.safetensors |
| `vision_tower.encoder.blocks.0-26.norm0.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00064-of-000064.safetensors |
| `vision_tower.encoder.blocks.0-26.norm0.weight` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00064-of-000064.safetensors |
| `vision_tower.encoder.blocks.0-26.norm1.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00064-of-000064.safetensors |
| `vision_tower.encoder.blocks.0-26.norm1.weight` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00064-of-000064.safetensors |
| `vision_tower.encoder.blocks.0-26.wo.bias` (×27 blocks) | `[1152]` | `torch.bfloat16` | 60.75 KB | model-00064-of-000064.safetensors |
| `vision_tower.encoder.blocks.0-26.wo.weight` (×27 blocks) | `[1152, 1152]` | `torch.bfloat16` | 68.34 MB | model-00064-of-000064.safetensors |
| `vision_tower.encoder.blocks.0-26.wqkv.bias` (×27 blocks) | `[3456]` | `torch.bfloat16` | 182.25 KB | model-00064-of-000064.safetensors |
| `vision_tower.encoder.blocks.0-26.wqkv.weight` (×27 blocks) | `[3456, 1152]` | `torch.bfloat16` | 205.03 MB | model-00064-of-000064.safetensors |
| `vision_tower.encoder.final_layernorm.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00064-of-000064.safetensors |
| `vision_tower.encoder.final_layernorm.weight` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00064-of-000064.safetensors |
| `vision_tower.patch_embed.pos_emb.weight` | `[64, 64, 1152]` | `torch.bfloat16` | 9.00 MB | model-00064-of-000064.safetensors |
| `vision_tower.patch_embed.proj.bias` | `[1152]` | `torch.bfloat16` | 2.25 KB | model-00064-of-000064.safetensors |
| `vision_tower.patch_embed.proj.weight` | `[1152, 3, 14, 14]` | `torch.bfloat16` | 1.29 MB | model-00064-of-000064.safetensors |

</details>

