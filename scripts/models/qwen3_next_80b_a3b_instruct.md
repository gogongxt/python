# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/models/opensource/Qwen3-Next-80B-A3B-Instruct`

# 模型配置

<details><summary>原始 config.json</summary>

`/nfs/ofs-llm-ssd/models/opensource/Qwen3-Next-80B-A3B-Instruct/config.json`

```json

{
  "architectures": [
    "Qwen3NextForCausalLM"
  ],
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "decoder_sparse_step": 1,
  "eos_token_id": 151645,
  "full_attention_interval": 4,
  "head_dim": 256,
  "hidden_act": "silu",
  "hidden_size": 2048,
  "initializer_range": 0.02,
  "intermediate_size": 5120,
  "linear_conv_kernel_dim": 4,
  "linear_key_head_dim": 128,
  "linear_num_key_heads": 16,
  "linear_num_value_heads": 32,
  "linear_value_head_dim": 128,
  "max_position_embeddings": 262144,
  "mlp_only_layers": [],
  "model_type": "qwen3_next",
  "moe_intermediate_size": 512,
  "norm_topk_prob": true,
  "num_attention_heads": 16,
  "num_experts": 512,
  "num_experts_per_tok": 10,
  "num_hidden_layers": 48,
  "num_key_value_heads": 2,
  "output_router_logits": false,
  "partial_rotary_factor": 0.25,
  "rms_norm_eps": 1e-06,
  "rope_scaling": null,
  "rope_theta": 10000000,
  "router_aux_loss_coef": 0.001,
  "shared_expert_intermediate_size": 512,
  "tie_word_embeddings": false,
  "torch_dtype": "bfloat16",
  "transformers_version": "4.57.0.dev0",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 151936
}

```
</details>

<details><summary>Transformers 配置</summary>

- **模型类型**: `Qwen3NextConfig`
- **数据类型**: `torch.bfloat16`
- **隐藏层大小**: 2048
- **层数**: 48
- **注意力头数**: 16
- **词表大小**: 151936
- **中间层大小**: 5120

```
Qwen3NextConfig {
  "architectures": [
    "Qwen3NextForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 151643,
  "decoder_sparse_step": 1,
  "dtype": "bfloat16",
  "eos_token_id": 151645,
  "head_dim": 256,
  "hidden_act": "silu",
  "hidden_size": 2048,
  "initializer_range": 0.02,
  "intermediate_size": 5120,
  "layer_types": [
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention",
    "linear_attention",
    "linear_attention",
    "linear_attention",
    "full_attention"
  ],
  "linear_conv_kernel_dim": 4,
  "linear_key_head_dim": 128,
  "linear_num_key_heads": 16,
  "linear_num_value_heads": 32,
  "linear_value_head_dim": 128,
  "max_position_embeddings": 262144,
  "mlp_only_layers": [],
  "model_type": "qwen3_next",
  "moe_intermediate_size": 512,
  "norm_topk_prob": true,
  "num_attention_heads": 16,
  "num_experts": 512,
  "num_experts_per_tok": 10,
  "num_hidden_layers": 48,
  "num_key_value_heads": 2,
  "output_router_logits": false,
  "pad_token_id": null,
  "partial_rotary_factor": 0.25,
  "rms_norm_eps": 1e-06,
  "rope_parameters": {
    "partial_rotary_factor": 0.25,
    "rope_theta": 10000000,
    "rope_type": "default"
  },
  "router_aux_loss_coef": 0.001,
  "shared_expert_intermediate_size": 512,
  "tie_word_embeddings": false,
  "transformers_version": "5.7.0",
  "use_cache": true,
  "use_sliding_window": false,
  "vocab_size": 151936
}

```

</details>

# 模型结构

**模型类**: `Qwen3NextModel`

```
Qwen3NextModel(
  (embed_tokens): Embedding(151936, 2048)
  (layers): ModuleList(
    (0-2): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (3): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (4-6): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (7): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (8-10): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (11): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (12-14): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (15): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (16-18): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (19): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (20-22): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (23): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (24-26): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (27): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (28-30): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (31): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (32-34): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (35): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (36-38): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (39): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (40-42): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (43): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (44-46): 3 x Qwen3NextDecoderLayer(
      (linear_attn): Qwen3NextGatedDeltaNet(
        (act): SiLUActivation()
        (conv1d): Conv1d(8192, 8192, kernel_size=(4,), stride=(1,), padding=(3,), groups=8192, bias=False)
        (in_proj_qkvz): Linear(in_features=2048, out_features=12288, bias=False)
        (in_proj_ba): Linear(in_features=2048, out_features=64, bias=False)
        (norm): Qwen3NextRMSNormGated()
        (out_proj): Linear(in_features=4096, out_features=2048, bias=False)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
    (47): Qwen3NextDecoderLayer(
      (self_attn): Qwen3NextAttention(
        (q_proj): Linear(in_features=2048, out_features=8192, bias=False)
        (k_proj): Linear(in_features=2048, out_features=512, bias=False)
        (v_proj): Linear(in_features=2048, out_features=512, bias=False)
        (o_proj): Linear(in_features=4096, out_features=2048, bias=False)
        (q_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
        (k_norm): Qwen3NextRMSNorm((256,), eps=1e-06)
      )
      (mlp): Qwen3NextSparseMoeBlock(
        (gate): Qwen3NextTopKRouter()
        (experts): Qwen3NextExperts(
          (act_fn): SiLUActivation()
        )
        (shared_expert): Qwen3NextMLP(
          (gate_proj): Linear(in_features=2048, out_features=512, bias=False)
          (up_proj): Linear(in_features=2048, out_features=512, bias=False)
          (down_proj): Linear(in_features=512, out_features=2048, bias=False)
          (act_fn): SiLUActivation()
        )
        (shared_expert_gate): Linear(in_features=2048, out_features=1, bias=False)
      )
      (input_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
      (post_attention_layernorm): Qwen3NextRMSNorm((2048,), eps=1e-06)
    )
  )
  (norm): Qwen3NextRMSNorm((2048,), eps=1e-06)
  (rotary_emb): Qwen3NextRotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 41 个 `safetensors` 文件
- **文件总大小**: 151.49 GB
- **权重张量数**: 75,944
- **参数总量**: 81,324,862,720
- **张量累计大小**: 151.48 GB
- **压缩**: 75944 → 46 行

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[151936, 2048]` | `torch.bfloat16` | 593.50 MB | model-00040-of-00041.safetensors |
| `model.embed_tokens.weight` | `[151936, 2048]` | `torch.bfloat16` | 593.50 MB | model-00001-of-00041.safetensors |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46.linear_attn.A_log` (×36 layers) | `[32]` | `torch.bfloat16` | 2.25 KB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46.linear_attn.conv1d.weight` (×36 layers) | `[8192, 1, 4]` | `torch.bfloat16` | 2.25 MB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46.linear_attn.dt_bias` (×36 layers) | `[32]` | `torch.bfloat16` | 2.25 KB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46.linear_attn.in_proj_ba.weight` (×36 layers) | `[64, 2048]` | `torch.bfloat16` | 9.00 MB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46.linear_attn.in_proj_qkvz.weight` (×36 layers) | `[12288, 2048]` | `torch.bfloat16` | 1.69 GB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46.linear_attn.norm.weight` (×36 layers) | `[128]` | `torch.bfloat16` | 9.00 KB | Multi Files |
| `model.layers.0-2,4-6,8-10,12-14,16-18,20-22,24-26,28-30,32-34,36-38,40-42,44-46.linear_attn.out_proj.weight` (×36 layers) | `[2048, 4096]` | `torch.bfloat16` | 576.00 MB | Multi Files |
| `model.layers.0-47.input_layernorm.weight` (×48 layers) | `[2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `model.layers.0-47.mlp.experts.0-511.down_proj.weight` (×48 layers, ×512 experts) | `[2048, 512]` | `torch.bfloat16` | 48.00 GB | Multi Files |
| `model.layers.0-47.mlp.experts.0-511.gate_proj.weight` (×48 layers, ×512 experts) | `[512, 2048]` | `torch.bfloat16` | 48.00 GB | Multi Files |
| `model.layers.0-47.mlp.experts.0-511.up_proj.weight` (×48 layers, ×512 experts) | `[512, 2048]` | `torch.bfloat16` | 48.00 GB | Multi Files |
| `model.layers.0-47.mlp.gate.weight` (×48 layers) | `[512, 2048]` | `torch.bfloat16` | 96.00 MB | Multi Files |
| `model.layers.0-47.mlp.shared_expert.down_proj.weight` (×48 layers) | `[2048, 512]` | `torch.bfloat16` | 96.00 MB | Multi Files |
| `model.layers.0-47.mlp.shared_expert.gate_proj.weight` (×48 layers) | `[512, 2048]` | `torch.bfloat16` | 96.00 MB | Multi Files |
| `model.layers.0-47.mlp.shared_expert.up_proj.weight` (×48 layers) | `[512, 2048]` | `torch.bfloat16` | 96.00 MB | Multi Files |
| `model.layers.0-47.mlp.shared_expert_gate.weight` (×48 layers) | `[1, 2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `model.layers.0-47.post_attention_layernorm.weight` (×48 layers) | `[2048]` | `torch.bfloat16` | 192.00 KB | Multi Files |
| `model.layers.3,7,...,43,47.self_attn.k_norm.weight` (×12 layers) | `[256]` | `torch.bfloat16` | 6.00 KB | Multi Files |
| `model.layers.3,7,...,43,47.self_attn.k_proj.weight` (×12 layers) | `[512, 2048]` | `torch.bfloat16` | 24.00 MB | Multi Files |
| `model.layers.3,7,...,43,47.self_attn.o_proj.weight` (×12 layers) | `[2048, 4096]` | `torch.bfloat16` | 192.00 MB | Multi Files |
| `model.layers.3,7,...,43,47.self_attn.q_norm.weight` (×12 layers) | `[256]` | `torch.bfloat16` | 6.00 KB | Multi Files |
| `model.layers.3,7,...,43,47.self_attn.q_proj.weight` (×12 layers) | `[8192, 2048]` | `torch.bfloat16` | 384.00 MB | Multi Files |
| `model.layers.3,7,...,43,47.self_attn.v_proj.weight` (×12 layers) | `[512, 2048]` | `torch.bfloat16` | 24.00 MB | Multi Files |
| `model.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00040-of-00041.safetensors |
| `mtp.fc.weight` | `[2048, 4096]` | `torch.bfloat16` | 16.00 MB | model-00041-of-00041.safetensors |
| `mtp.layers.0.input_layernorm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00041-of-00041.safetensors |
| `mtp.layers.0.mlp.experts.0-511.down_proj.weight` (×512 experts) | `[2048, 512]` | `torch.bfloat16` | 1.00 GB | model-00041-of-00041.safetensors |
| `mtp.layers.0.mlp.experts.0-511.gate_proj.weight` (×512 experts) | `[512, 2048]` | `torch.bfloat16` | 1.00 GB | model-00041-of-00041.safetensors |
| `mtp.layers.0.mlp.experts.0-511.up_proj.weight` (×512 experts) | `[512, 2048]` | `torch.bfloat16` | 1.00 GB | model-00041-of-00041.safetensors |
| `mtp.layers.0.mlp.gate.weight` | `[512, 2048]` | `torch.bfloat16` | 2.00 MB | model-00041-of-00041.safetensors |
| `mtp.layers.0.mlp.shared_expert.down_proj.weight` | `[2048, 512]` | `torch.bfloat16` | 2.00 MB | model-00041-of-00041.safetensors |
| `mtp.layers.0.mlp.shared_expert.gate_proj.weight` | `[512, 2048]` | `torch.bfloat16` | 2.00 MB | model-00041-of-00041.safetensors |
| `mtp.layers.0.mlp.shared_expert.up_proj.weight` | `[512, 2048]` | `torch.bfloat16` | 2.00 MB | model-00041-of-00041.safetensors |
| `mtp.layers.0.mlp.shared_expert_gate.weight` | `[1, 2048]` | `torch.bfloat16` | 4.00 KB | model-00041-of-00041.safetensors |
| `mtp.layers.0.post_attention_layernorm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00041-of-00041.safetensors |
| `mtp.layers.0.self_attn.k_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00041-of-00041.safetensors |
| `mtp.layers.0.self_attn.k_proj.weight` | `[512, 2048]` | `torch.bfloat16` | 2.00 MB | model-00041-of-00041.safetensors |
| `mtp.layers.0.self_attn.o_proj.weight` | `[2048, 4096]` | `torch.bfloat16` | 16.00 MB | model-00041-of-00041.safetensors |
| `mtp.layers.0.self_attn.q_norm.weight` | `[256]` | `torch.bfloat16` | 512.00 B | model-00041-of-00041.safetensors |
| `mtp.layers.0.self_attn.q_proj.weight` | `[8192, 2048]` | `torch.bfloat16` | 32.00 MB | model-00041-of-00041.safetensors |
| `mtp.layers.0.self_attn.v_proj.weight` | `[512, 2048]` | `torch.bfloat16` | 2.00 MB | model-00041-of-00041.safetensors |
| `mtp.norm.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00041-of-00041.safetensors |
| `mtp.pre_fc_norm_embedding.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00041-of-00041.safetensors |
| `mtp.pre_fc_norm_hidden.weight` | `[2048]` | `torch.bfloat16` | 4.00 KB | model-00041-of-00041.safetensors |

</details>

