# 模型信息报告

- **模型路径**: `/nfs/ofs-luban-data/model/moonshotai/Kimi-K3`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-luban-data/model/moonshotai/Kimi-K3/config.json`

```json

{
  "architectures": [
    "KimiK3ForConditionalGeneration"
  ],
  "auto_map": {
    "AutoConfig": "configuration_kimi_k3.KimiK3Config",
    "AutoModel": "modeling_kimi_k3.KimiK3ForConditionalGeneration",
    "AutoModelForCausalLM": "modeling_kimi_k3.KimiK3ForConditionalGeneration"
  },
  "bos_token_id": 163584,
  "dtype": "bfloat16",
  "eos_token_id": 163586,
  "ignore_index": -100,
  "image_placeholder": "<|kimi_image_placeholder|>",
  "media_placeholder_token_id": 163605,
  "model_type": "kimi_k3",
  "pad_token_id": 163839,
  "text_config": {
    "_name_or_path": "",
    "activation_situ_beta": 4.0,
    "activation_situ_linear_beta": 25.0,
    "add_cross_attention": false,
    "architectures": [
      "KimiLinearForCausalLM"
    ],
    "attn_res_block_size": 12,
    "auto_map": {
      "AutoConfig": "configuration_kimi_k3.KimiLinearConfig",
      "AutoModel": "modeling_kimi_linear.KimiLinearModel",
      "AutoModelForCausalLM": "modeling_kimi_linear.KimiLinearForCausalLM"
    },
    "bad_words_ids": null,
    "begin_suppress_tokens": null,
    "bos_token_id": 163584,
    "chunk_size_feed_forward": 0,
    "cross_attention_hidden_size": null,
    "decoder_start_token_id": null,
    "diversity_penalty": 0.0,
    "do_sample": false,
    "dtype": "bfloat16",
    "early_stopping": false,
    "encoder_no_repeat_ngram_size": 0,
    "eos_token_id": 163586,
    "exponential_decay_length_penalty": null,
    "finetuning_task": null,
    "first_k_dense_replace": 1,
    "forced_bos_token_id": null,
    "forced_eos_token_id": null,
    "hidden_act": "situ",
    "hidden_size": 7168,
    "id2label": {
      "0": "LABEL_0",
      "1": "LABEL_1"
    },
    "initializer_range": 0.02,
    "intermediate_size": 33792,
    "is_decoder": false,
    "is_encoder_decoder": false,
    "kv_lora_rank": 512,
    "label2id": {
      "LABEL_0": 0,
      "LABEL_1": 1
    },
    "latent_moe_use_norm": true,
    "length_penalty": 1.0,
    "linear_attn_config": {
      "full_attn_layers": [
        4,
        8,
        12,
        16,
        20,
        24,
        28,
        32,
        36,
        40,
        44,
        48,
        52,
        56,
        60,
        64,
        68,
        72,
        76,
        80,
        84,
        88,
        92,
        93
      ],
      "gate_lower_bound": -5.0,
      "head_dim": 128,
      "kda_layers": [
        1,
        2,
        3,
        5,
        6,
        7,
        9,
        10,
        11,
        13,
        14,
        15,
        17,
        18,
        19,
        21,
        22,
        23,
        25,
        26,
        27,
        29,
        30,
        31,
        33,
        34,
        35,
        37,
        38,
        39,
        41,
        42,
        43,
        45,
        46,
        47,
        49,
        50,
        51,
        53,
        54,
        55,
        57,
        58,
        59,
        61,
        62,
        63,
        65,
        66,
        67,
        69,
        70,
        71,
        73,
        74,
        75,
        77,
        78,
        79,
        81,
        82,
        83,
        85,
        86,
        87,
        89,
        90,
        91
      ],
      "num_heads": 96,
      "short_conv_kernel_size": 4,
      "use_full_rank_gate": true
    },
    "max_length": 20,
    "max_position_embeddings": 1048576,
    "min_length": 0,
    "mla_use_nope": true,
    "mla_use_output_gate": true,
    "model_type": "kimi_linear",
    "moe_intermediate_size": 3072,
    "moe_layer_freq": 1,
    "moe_renormalize": true,
    "moe_router_activation_func": "sigmoid",
    "no_repeat_ngram_size": 0,
    "num_attention_heads": 96,
    "num_beam_groups": 1,
    "num_beams": 1,
    "num_expert_group": 1,
    "num_experts": 896,
    "num_experts_per_token": 16,
    "num_hidden_layers": 93,
    "num_key_value_heads": 96,
    "num_nextn_predict_layers": 0,
    "num_return_sequences": 1,
    "num_shared_experts": 2,
    "output_attentions": false,
    "output_hidden_states": false,
    "output_scores": false,
    "pad_token_id": 163839,
    "prefix": null,
    "problem_type": null,
    "pruned_heads": {},
    "q_lora_rank": 1536,
    "qk_nope_head_dim": 128,
    "qk_rope_head_dim": 64,
    "quantization_config": {
      "config_groups": {
        "group_0": {
          "format": "mxfp4-pack-quantized",
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
            "scale_dtype": "torch.uint8",
            "strategy": "group",
            "symmetric": true,
            "type": "float",
            "zp_dtype": null
          }
        }
      },
      "format": "mxfp4-pack-quantized",
      "global_compression_ratio": null,
      "ignore": [
        "re:.*self_attn.*",
        "re:.*shared_experts.*",
        "re:.*mlp\\.(gate|up|gate_up|down)_proj.*",
        "re:.*lm_head.*",
        "re:.*vision_tower.*",
        "re:.*mm_projector.*"
      ],
      "kv_cache_scheme": null,
      "quant_method": "compressed-tensors",
      "quantization_status": "compressed"
    },
    "remove_invalid_values": false,
    "repetition_penalty": 1.0,
    "return_dict": true,
    "return_dict_in_generate": false,
    "rms_norm_eps": 1e-05,
    "routed_expert_hidden_size": 3584,
    "routed_scaling_factor": 1.0,
    "sep_token_id": null,
    "suppress_tokens": null,
    "task_specific_params": null,
    "temperature": 1.0,
    "tf_legacy_loss": false,
    "tie_encoder_decoder": false,
    "tie_word_embeddings": false,
    "tokenizer_class": null,
    "top_k": 50,
    "top_p": 1.0,
    "topk_group": 1,
    "topk_method": "noaux_tc",
    "torchscript": false,
    "transformers_version": "4.56.2",
    "typical_p": 1.0,
    "use_bfloat16": false,
    "use_cache": true,
    "use_grouped_topk": true,
    "v_head_dim": 128,
    "vocab_size": 163840
  },
  "tie_word_embeddings": false,
  "vision_config": {
    "_attn_implementation": "flash_attention_2",
    "activation_func": "gelu_pytorch_tanh",
    "attn_bias": false,
    "init_pos_emb_height": 64,
    "init_pos_emb_time": 4,
    "init_pos_emb_width": 64,
    "linear_bias": false,
    "merge_kernel_size": [
      2,
      2
    ],
    "merge_type": "sd2_tpool",
    "mlp_type": "mlp2",
    "mm_hidden_size": 1024,
    "mm_projector_type": "patchmergerv2",
    "norm_type": "rmsnorm",
    "patch_embed_proj_bias": false,
    "patch_size": 14,
    "pos_emb_interpolation_mode": "bilinear",
    "pos_emb_type": "divided_fixed",
    "projector_hidden_act": "gelu",
    "projector_ln_eps": 1e-05,
    "qkv_hidden_size": 1536,
    "text_hidden_size": 7168,
    "vt_hidden_size": 1024,
    "vt_intermediate_size": 4096,
    "vt_num_attention_heads": 12,
    "vt_num_hidden_layers": 27
  }
}
```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `KimiK3Config`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: N/A
- **层数**: N/A
- **注意力头数**: N/A
- **词表大小**: N/A
- **中间层大小**: N/A

```
KimiK3Config {
  "architectures": [
    "KimiK3ForConditionalGeneration"
  ],
  "auto_map": {
    "AutoConfig": "configuration_kimi_k3.KimiK3Config",
    "AutoModel": "modeling_kimi_k3.KimiK3ForConditionalGeneration",
    "AutoModelForCausalLM": "modeling_kimi_k3.KimiK3ForConditionalGeneration"
  },
  "bos_token_id": 163584,
  "dtype": "bfloat16",
  "eos_token_id": 163586,
  "ignore_index": -100,
  "image_placeholder": "<|kimi_image_placeholder|>",
  "media_placeholder_token_id": 163605,
  "model_type": "kimi_k3",
  "pad_token_id": 163839,
  "quantization_config": {
    "config_groups": {
      "group_0": {
        "format": "mxfp4-pack-quantized",
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
          "scale_dtype": "torch.uint8",
          "strategy": "group",
          "symmetric": true,
          "type": "float",
          "zp_dtype": null
        }
      }
    },
    "format": "mxfp4-pack-quantized",
    "global_compression_ratio": null,
    "ignore": [
      "re:.*self_attn.*",
      "re:.*shared_experts.*",
      "re:.*mlp\\.(gate|up|gate_up|down)_proj.*",
      "re:.*lm_head.*",
      "re:.*vision_tower.*",
      "re:.*mm_projector.*"
    ],
    "kv_cache_scheme": null,
    "quant_method": "compressed-tensors",
    "quantization_status": "compressed"
  },
  "text_config": {
    "_name_or_path": "",
    "activation_situ_beta": 4.0,
    "activation_situ_linear_beta": 25.0,
    "add_cross_attention": false,
    "architectures": [
      "KimiLinearForCausalLM"
    ],
    "attn_res_block_size": 12,
    "auto_map": {
      "AutoConfig": "configuration_kimi_k3.KimiLinearConfig",
      "AutoModel": "modeling_kimi_linear.KimiLinearModel",
      "AutoModelForCausalLM": "modeling_kimi_linear.KimiLinearForCausalLM"
    },
    "bos_token_id": 163584,
    "chunk_size_feed_forward": 0,
    "cross_attention_hidden_size": null,
    "decoder_start_token_id": null,
    "dtype": "bfloat16",
    "eos_token_id": 163586,
    "finetuning_task": null,
    "first_k_dense_replace": 1,
    "head_dim": 74,
    "hidden_act": "situ",
    "hidden_size": 7168,
    "id2label": {
      "0": "LABEL_0",
      "1": "LABEL_1"
    },
    "initializer_range": 0.02,
    "intermediate_size": 33792,
    "is_decoder": false,
    "is_encoder_decoder": false,
    "kv_lora_rank": 512,
    "label2id": {
      "LABEL_0": 0,
      "LABEL_1": 1
    },
    "latent_moe_use_norm": true,
    "linear_attn_config": {
      "full_attn_layers": [
        4,
        8,
        12,
        16,
        20,
        24,
        28,
        32,
        36,
        40,
        44,
        48,
        52,
        56,
        60,
        64,
        68,
        72,
        76,
        80,
        84,
        88,
        92,
        93
      ],
      "gate_lower_bound": -5.0,
      "head_dim": 128,
      "kda_layers": [
        1,
        2,
        3,
        5,
        6,
        7,
        9,
        10,
        11,
        13,
        14,
        15,
        17,
        18,
        19,
        21,
        22,
        23,
        25,
        26,
        27,
        29,
        30,
        31,
        33,
        34,
        35,
        37,
        38,
        39,
        41,
        42,
        43,
        45,
        46,
        47,
        49,
        50,
        51,
        53,
        54,
        55,
        57,
        58,
        59,
        61,
        62,
        63,
        65,
        66,
        67,
        69,
        70,
        71,
        73,
        74,
        75,
        77,
        78,
        79,
        81,
        82,
        83,
        85,
        86,
        87,
        89,
        90,
        91
      ],
      "num_heads": 96,
      "short_conv_kernel_size": 4,
      "use_full_rank_gate": true
    },
    "max_position_embeddings": 1048576,
    "mla_use_nope": true,
    "mla_use_output_gate": true,
    "model_type": "kimi_linear",
    "moe_intermediate_size": 3072,
    "moe_layer_freq": 1,
    "moe_renormalize": true,
    "moe_router_activation_func": "sigmoid",
    "num_attention_heads": 96,
    "num_expert_group": 1,
    "num_experts": 896,
    "num_experts_per_token": 16,
    "num_hidden_layers": 93,
    "num_key_value_heads": 96,
    "num_nextn_predict_layers": 0,
    "num_shared_experts": 2,
    "output_attentions": false,
    "output_hidden_states": false,
    "pad_token_id": 163839,
    "prefix": null,
    "problem_type": null,
    "pruned_heads": {},
    "q_lora_rank": 1536,
    "qk_nope_head_dim": 128,
    "qk_rope_head_dim": 64,
    "quantization_config": {
      "config_groups": {
        "group_0": {
          "format": "mxfp4-pack-quantized",
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
            "scale_dtype": "torch.uint8",
            "strategy": "group",
            "symmetric": true,
            "type": "float",
            "zp_dtype": null
          }
        }
      },
      "format": "mxfp4-pack-quantized",
      "global_compression_ratio": null,
      "ignore": [
        "re:.*self_attn.*",
        "re:.*shared_experts.*",
        "re:.*mlp\\.(gate|up|gate_up|down)_proj.*",
        "re:.*lm_head.*",
        "re:.*vision_tower.*",
        "re:.*mm_projector.*"
      ],
      "kv_cache_scheme": null,
      "quant_method": "compressed-tensors",
      "quantization_status": "compressed"
    },
    "return_dict": true,
    "rms_norm_eps": 1e-05,
    "rope_parameters": {
      "rope_theta": 10000.0,
      "rope_type": "default"
    },
    "rope_theta": 10000.0,
    "routed_expert_hidden_size": 3584,
    "routed_scaling_factor": 1.0,
    "sep_token_id": null,
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
    "use_grouped_topk": true,
    "v_head_dim": 128,
    "vocab_size": 163840
  },
  "tie_word_embeddings": false,
  "transformers_version": "5.12.1",
  "vision_config": {
    "_name_or_path": "",
    "activation_func": "gelu_pytorch_tanh",
    "architectures": null,
    "attn_bias": false,
    "chunk_size_feed_forward": 0,
    "dtype": null,
    "id2label": {
      "0": "LABEL_0",
      "1": "LABEL_1"
    },
    "init_pos_emb_height": 64,
    "init_pos_emb_time": 4,
    "init_pos_emb_width": 64,
    "is_encoder_decoder": false,
    "label2id": {
      "LABEL_0": 0,
      "LABEL_1": 1
    },
    "linear_bias": false,
    "merge_kernel_size": [
      2,
      2
    ],
    "merge_type": "sd2_tpool",
    "mlp_type": "mlp2",
    "mm_hidden_size": 1024,
    "mm_projector_type": "patchmergerv2",
    "model_type": "",
    "norm_type": "rmsnorm",
    "output_attentions": false,
    "output_hidden_states": false,
    "patch_embed_proj_bias": false,
    "patch_size": 14,
    "pos_emb_interpolation_mode": "bilinear",
    "pos_emb_type": "divided_fixed",
    "problem_type": null,
    "projector_hidden_act": "gelu",
    "projector_ln_eps": 1e-05,
    "qkv_hidden_size": 1536,
    "return_dict": true,
    "text_hidden_size": 7168,
    "vt_hidden_size": 1024,
    "vt_intermediate_size": 4096,
    "vt_num_attention_heads": 12,
    "vt_num_hidden_layers": 27
  }
}

```

</details>

# 模型结构

**模型类**: `KimiK3Config` (当前 transformers 版本不支持实例化)

# 权重统计

- **权重文件**: 96 个 `safetensors` 文件
- **文件总大小**: 1453.74 GB
- **权重张量数**: 497,220
- **参数总量**: 1,503,647,073,024
- **张量累计大小**: 1453.66 GB
- **压缩**: 497220 → 60 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `language_model.lm_head.weight` | `[163840, 7168]` | `torch.bfloat16` | 2.19 GB | model-00094-of-000096.safetensors |
| `language_model.model.embed_tokens.weight` | `[163840, 7168]` | `torch.bfloat16` | 2.19 GB | model-00094-of-000096.safetensors |
| `language_model.model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62,64-66,68-70,72-74,76-78,80-82,84-86,88-90.self_attn.A_log` (×69 layers) | `[128]` | `torch.float32` | 34.50 KB | Multi Files |
| `language_model.model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62,64-66,68-70,72-74,76-78,80-82,84-86,88-90.self_attn.b_proj.weight` (×69 layers) | `[96, 7168]` | `torch.bfloat16` | 90.56 MB | Multi Files |
| `language_model.model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62,64-66,68-70,72-74,76-78,80-82,84-86,88-90.self_attn.dt_bias` (×69 layers) | `[12288]` | `torch.float32` | 3.23 MB | Multi Files |
| `language_model.model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62,64-66,68-70,72-74,76-78,80-82,84-86,88-90.self_attn.f_a_proj.weight` (×69 layers) | `[128, 7168]` | `torch.bfloat16` | 120.75 MB | Multi Files |
| `language_model.model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62,64-66,68-70,72-74,76-78,80-82,84-86,88-90.self_attn.f_b_proj.weight` (×69 layers) | `[12288, 128]` | `torch.bfloat16` | 207.00 MB | Multi Files |
| `language_model.model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62,64-66,68-70,72-74,76-78,80-82,84-86,88-90.self_attn.k_conv1d.weight` (×69 layers) | `[12288, 1, 4]` | `torch.float32` | 12.94 MB | Multi Files |
| `language_model.model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62,64-66,68-70,72-74,76-78,80-82,84-86,88-90.self_attn.k_proj.weight` (×69 layers) | `[12288, 7168]` | `torch.bfloat16` | 11.32 GB | Multi Files |
| `language_model.model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62,64-66,68-70,72-74,76-78,80-82,84-86,88-90.self_attn.o_norm.weight` (×69 layers) | `[128]` | `torch.float32` | 34.50 KB | Multi Files |
| `language_model.model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62,64-66,68-70,72-74,76-78,80-82,84-86,88-90.self_attn.q_conv1d.weight` (×69 layers) | `[12288, 1, 4]` | `torch.float32` | 12.94 MB | Multi Files |
| `language_model.model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62,64-66,68-70,72-74,76-78,80-82,84-86,88-90.self_attn.q_proj.weight` (×69 layers) | `[12288, 7168]` | `torch.bfloat16` | 11.32 GB | Multi Files |
| `language_model.model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62,64-66,68-70,72-74,76-78,80-82,84-86,88-90.self_attn.v_conv1d.weight` (×69 layers) | `[12288, 1, 4]` | `torch.float32` | 12.94 MB | Multi Files |
| `language_model.model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46,48-50,52-54,56-58,60-62,64-66,68-70,72-74,76-78,80-82,84-86,88-90.self_attn.v_proj.weight` (×69 layers) | `[12288, 7168]` | `torch.bfloat16` | 11.32 GB | Multi Files |
| `language_model.model.layers.0-92.input_layernorm.weight` (×93 layers) | `[7168]` | `torch.bfloat16` | 1.27 MB | Multi Files |
| `language_model.model.layers.0-92.mlp_res_norm.weight` (×93 layers) | `[7168]` | `torch.bfloat16` | 1.27 MB | Multi Files |
| `language_model.model.layers.0-92.mlp_res_proj.weight` (×93 layers) | `[1, 7168]` | `torch.bfloat16` | 1.27 MB | Multi Files |
| `language_model.model.layers.0-92.post_attention_layernorm.weight` (×93 layers) | `[7168]` | `torch.bfloat16` | 1.27 MB | Multi Files |
| `language_model.model.layers.0-92.self_attention_res_norm.weight` (×93 layers) | `[7168]` | `torch.bfloat16` | 1.27 MB | Multi Files |
| `language_model.model.layers.0-92.self_attention_res_proj.weight` (×93 layers) | `[1, 7168]` | `torch.bfloat16` | 1.27 MB | Multi Files |
| `language_model.model.layers.0-92.self_attn.g_proj.weight` (×93 layers) | `[12288, 7168]` | `torch.bfloat16` | 15.26 GB | Multi Files |
| `language_model.model.layers.0-92.self_attn.o_proj.weight` (×93 layers) | `[7168, 12288]` | `torch.bfloat16` | 15.26 GB | Multi Files |
| `language_model.model.layers.0.mlp.down_proj.weight` | `[7168, 33792]` | `torch.bfloat16` | 462.00 MB | model-00001-of-000096.safetensors |
| `language_model.model.layers.0.mlp.gate_proj.weight` | `[33792, 7168]` | `torch.bfloat16` | 462.00 MB | model-00001-of-000096.safetensors |
| `language_model.model.layers.0.mlp.up_proj.weight` | `[33792, 7168]` | `torch.bfloat16` | 462.00 MB | model-00001-of-000096.safetensors |
| `language_model.model.layers.1-92.block_sparse_moe.experts.0-895.w1.weight_packed` (×92 layers, ×896 experts) | `[3072, 1792]` | `torch.uint8` | 422.62 GB | Multi Files |
| `language_model.model.layers.1-92.block_sparse_moe.experts.0-895.w1.weight_scale` (×92 layers, ×896 experts) | `[3072, 112]` | `torch.uint8` | 26.41 GB | Multi Files |
| `language_model.model.layers.1-92.block_sparse_moe.experts.0-895.w2.weight_packed` (×92 layers, ×896 experts) | `[3584, 1536]` | `torch.uint8` | 422.62 GB | Multi Files |
| `language_model.model.layers.1-92.block_sparse_moe.experts.0-895.w2.weight_scale` (×92 layers, ×896 experts) | `[3584, 96]` | `torch.uint8` | 26.41 GB | Multi Files |
| `language_model.model.layers.1-92.block_sparse_moe.experts.0-895.w3.weight_packed` (×92 layers, ×896 experts) | `[3072, 1792]` | `torch.uint8` | 422.62 GB | Multi Files |
| `language_model.model.layers.1-92.block_sparse_moe.experts.0-895.w3.weight_scale` (×92 layers, ×896 experts) | `[3072, 112]` | `torch.uint8` | 26.41 GB | Multi Files |
| `language_model.model.layers.1-92.block_sparse_moe.gate.e_score_correction_bias` (×92 layers) | `[896]` | `torch.float32` | 322.00 KB | Multi Files |
| `language_model.model.layers.1-92.block_sparse_moe.gate.weight` (×92 layers) | `[896, 7168]` | `torch.bfloat16` | 1.10 GB | Multi Files |
| `language_model.model.layers.1-92.block_sparse_moe.routed_expert_down_proj.weight` (×92 layers) | `[3584, 7168]` | `torch.bfloat16` | 4.40 GB | Multi Files |
| `language_model.model.layers.1-92.block_sparse_moe.routed_expert_norm.weight` (×92 layers) | `[3584]` | `torch.bfloat16` | 644.00 KB | Multi Files |
| `language_model.model.layers.1-92.block_sparse_moe.routed_expert_up_proj.weight` (×92 layers) | `[7168, 3584]` | `torch.bfloat16` | 4.40 GB | Multi Files |
| `language_model.model.layers.1-92.block_sparse_moe.shared_experts.down_proj.weight` (×92 layers) | `[7168, 6144]` | `torch.bfloat16` | 7.55 GB | Multi Files |
| `language_model.model.layers.1-92.block_sparse_moe.shared_experts.gate_proj.weight` (×92 layers) | `[6144, 7168]` | `torch.bfloat16` | 7.55 GB | Multi Files |
| `language_model.model.layers.1-92.block_sparse_moe.shared_experts.up_proj.weight` (×92 layers) | `[6144, 7168]` | `torch.bfloat16` | 7.55 GB | Multi Files |
| `language_model.model.layers.3,7,...,83,87,91-92.self_attn.kv_a_layernorm.weight` (×24 layers) | `[512]` | `torch.bfloat16` | 24.00 KB | Multi Files |
| `language_model.model.layers.3,7,...,83,87,91-92.self_attn.kv_a_proj_with_mqa.weight` (×24 layers) | `[576, 7168]` | `torch.bfloat16` | 189.00 MB | Multi Files |
| `language_model.model.layers.3,7,...,83,87,91-92.self_attn.kv_b_proj.weight` (×24 layers) | `[24576, 512]` | `torch.bfloat16` | 576.00 MB | Multi Files |
| `language_model.model.layers.3,7,...,83,87,91-92.self_attn.q_a_layernorm.weight` (×24 layers) | `[1536]` | `torch.bfloat16` | 72.00 KB | Multi Files |
| `language_model.model.layers.3,7,...,83,87,91-92.self_attn.q_a_proj.weight` (×24 layers) | `[1536, 7168]` | `torch.bfloat16` | 504.00 MB | Multi Files |
| `language_model.model.layers.3,7,...,83,87,91-92.self_attn.q_b_proj.weight` (×24 layers) | `[18432, 1536]` | `torch.bfloat16` | 1.27 GB | Multi Files |
| `language_model.model.norm.weight` | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00094-of-000096.safetensors |
| `language_model.model.output_attn_res_norm.weight` | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00094-of-000096.safetensors |
| `language_model.model.output_attn_res_proj.weight` | `[1, 7168]` | `torch.bfloat16` | 14.00 KB | model-00094-of-000096.safetensors |
| `mm_projector.post_norm.weight` | `[7168]` | `torch.bfloat16` | 14.00 KB | model-00095-of-000096.safetensors |
| `mm_projector.proj.0.weight` | `[4096, 4096]` | `torch.bfloat16` | 32.00 MB | model-00095-of-000096.safetensors |
| `mm_projector.proj.2.weight` | `[7168, 4096]` | `torch.bfloat16` | 56.00 MB | model-00095-of-000096.safetensors |
| `vision_tower.encoder.blocks.0-26.mlp.fc0.weight` (×27 blocks) | `[4096, 1024]` | `torch.bfloat16` | 216.00 MB | model-00096-of-000096.safetensors |
| `vision_tower.encoder.blocks.0-26.mlp.fc1.weight` (×27 blocks) | `[1024, 4096]` | `torch.bfloat16` | 216.00 MB | model-00096-of-000096.safetensors |
| `vision_tower.encoder.blocks.0-26.norm0.weight` (×27 blocks) | `[1024]` | `torch.bfloat16` | 54.00 KB | model-00096-of-000096.safetensors |
| `vision_tower.encoder.blocks.0-26.norm1.weight` (×27 blocks) | `[1024]` | `torch.bfloat16` | 54.00 KB | model-00096-of-000096.safetensors |
| `vision_tower.encoder.blocks.0-26.wo.weight` (×27 blocks) | `[1024, 1536]` | `torch.bfloat16` | 81.00 MB | model-00096-of-000096.safetensors |
| `vision_tower.encoder.blocks.0-26.wqkv.weight` (×27 blocks) | `[4608, 1024]` | `torch.bfloat16` | 243.00 MB | model-00096-of-000096.safetensors |
| `vision_tower.encoder.final_layernorm.weight` | `[1024]` | `torch.bfloat16` | 2.00 KB | model-00096-of-000096.safetensors |
| `vision_tower.patch_embed.pos_emb.weight` | `[64, 64, 1024]` | `torch.bfloat16` | 8.00 MB | model-00096-of-000096.safetensors |
| `vision_tower.patch_embed.proj.weight` | `[1024, 3, 14, 14]` | `torch.bfloat16` | 1.15 MB | model-00096-of-000096.safetensors |

</details>

