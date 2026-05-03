# 模型信息报告

- **模型路径**: `/nfs/ofs-llm-ssd/user/gogongxt/models/llama-2-7b`

# 模型配置

- **模型类型**: `LlamaConfig`
- **数据类型**: `torch.float16`
- **隐藏层大小**: 4096
- **层数**: 32
- **注意力头数**: 32
- **词表大小**: 32000
- **中间层大小**: 11008

<details><summary>完整配置</summary>

```
LlamaConfig {
  "architectures": [
    "LlamaForCausalLM"
  ],
  "attention_bias": false,
  "attention_dropout": 0.0,
  "bos_token_id": 1,
  "dtype": "float16",
  "eos_token_id": 2,
  "head_dim": 128,
  "hidden_act": "silu",
  "hidden_size": 4096,
  "initializer_range": 0.02,
  "intermediate_size": 11008,
  "max_position_embeddings": 4096,
  "mlp_bias": false,
  "model_type": "llama",
  "num_attention_heads": 32,
  "num_hidden_layers": 32,
  "num_key_value_heads": 32,
  "pretraining_tp": 1,
  "rms_norm_eps": 1e-05,
  "rope_scaling": null,
  "rope_theta": 10000.0,
  "tie_word_embeddings": false,
  "transformers_version": "4.57.1",
  "use_cache": true,
  "vocab_size": 32000
}

```

</details>

# 模型结构

- **模型类**: `LlamaModel`
- **参数总量**: 6,607,343,616

```
LlamaModel(
  (embed_tokens): Embedding(32000, 4096)
  (layers): ModuleList(
    (0-31): 32 x LlamaDecoderLayer(
      (self_attn): LlamaAttention(
        (q_proj): Linear(in_features=4096, out_features=4096, bias=False)
        (k_proj): Linear(in_features=4096, out_features=4096, bias=False)
        (v_proj): Linear(in_features=4096, out_features=4096, bias=False)
        (o_proj): Linear(in_features=4096, out_features=4096, bias=False)
      )
      (mlp): LlamaMLP(
        (gate_proj): Linear(in_features=4096, out_features=11008, bias=False)
        (up_proj): Linear(in_features=4096, out_features=11008, bias=False)
        (down_proj): Linear(in_features=11008, out_features=4096, bias=False)
        (act_fn): SiLUActivation()
      )
      (input_layernorm): LlamaRMSNorm((4096,), eps=1e-05)
      (post_attention_layernorm): LlamaRMSNorm((4096,), eps=1e-05)
    )
  )
  (norm): LlamaRMSNorm((4096,), eps=1e-05)
  (rotary_emb): LlamaRotaryEmbedding()
)
```

# 权重统计

- **权重文件**: 2 个 `safetensors` 文件
- **权重张量数**: 323
- **参数总量**: 6,738,417,664

<details><summary>详细权重列表</summary>

| 权重名称 | 形状 | 数据类型 | 大小 | 文件 |
| --- | --- | --- | --- | --- |
| `lm_head.weight` | `[32000, 4096]` | `torch.float16` | 250.00 MB | model-00002-of-00002.safetensors |
| `model.embed_tokens.weight` | `[32000, 4096]` | `torch.float16` | 250.00 MB | model-00001-of-00002.safetensors |
| `model.layers.0.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.0.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.0.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.0.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.0.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.0.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.0.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.0.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.0.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.0.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.1.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.1.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.1.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.1.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.1.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.1.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.1.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.1.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.1.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.1.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.2.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.2.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.2.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.2.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.2.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.2.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.2.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.2.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.2.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.2.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.3.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.3.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.3.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.3.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.3.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.3.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.3.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.3.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.3.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.3.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.4.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.4.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.4.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.4.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.4.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.4.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.4.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.4.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.4.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.4.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.5.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.5.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.5.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.5.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.5.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.5.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.5.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.5.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.5.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.5.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.6.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.6.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.6.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.6.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.6.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.6.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.6.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.6.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.6.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.6.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.7.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.7.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.7.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.7.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.7.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.7.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.7.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.7.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.7.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.7.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.8.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.8.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.8.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.8.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.8.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.8.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.8.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.8.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.8.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.8.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.9.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.9.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.9.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.9.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.9.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.9.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.9.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.9.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.9.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.9.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.10.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.10.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.10.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.10.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.10.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.10.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.10.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.10.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.10.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.10.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.11.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.11.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.11.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.11.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.11.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.11.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.11.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.11.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.11.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.11.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.12.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.12.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.12.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.12.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.12.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.12.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.12.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.12.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.12.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.12.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.13.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.13.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.13.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.13.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.13.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.13.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.13.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.13.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.13.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.13.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.14.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.14.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.14.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.14.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.14.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.14.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.14.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.14.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.14.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.14.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.15.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.15.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.15.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.15.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.15.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.15.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.15.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.15.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.15.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.15.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.16.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.16.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.16.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.16.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.16.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.16.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.16.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.16.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.16.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.16.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.17.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.17.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.17.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.17.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.17.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.17.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.17.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.17.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.17.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.17.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.18.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.18.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.18.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.18.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.18.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.18.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.18.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.18.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.18.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.18.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.19.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.19.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.19.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.19.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.19.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.19.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.19.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.19.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.19.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.19.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.20.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.20.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.20.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.20.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.20.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.20.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.20.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.20.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.20.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.20.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.21.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.21.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.21.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.21.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.21.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.21.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.21.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.21.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.21.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.21.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.22.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.22.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.22.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.22.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.22.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.22.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.22.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.22.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.22.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.22.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.23.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.23.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.23.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.23.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00001-of-00002.safetensors |
| `model.layers.23.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00001-of-00002.safetensors |
| `model.layers.23.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.23.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.23.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.23.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00001-of-00002.safetensors |
| `model.layers.23.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00001-of-00002.safetensors |
| `model.layers.24.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.24.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.24.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.24.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.24.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.24.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.24.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.24.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.24.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00002-of-00002.safetensors |
| `model.layers.24.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.25.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.25.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.25.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.25.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.25.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.25.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.25.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.25.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.25.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00002-of-00002.safetensors |
| `model.layers.25.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.26.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.26.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.26.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.26.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.26.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.26.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.26.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.26.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.26.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00002-of-00002.safetensors |
| `model.layers.26.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.27.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.27.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.27.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.27.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.27.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.27.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.27.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.27.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.27.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00002-of-00002.safetensors |
| `model.layers.27.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.28.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.28.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.28.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.28.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.28.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.28.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.28.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.28.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.28.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00002-of-00002.safetensors |
| `model.layers.28.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.29.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.29.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.29.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.29.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.29.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.29.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.29.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.29.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.29.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00002-of-00002.safetensors |
| `model.layers.29.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.30.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.30.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.30.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.30.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.30.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.30.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.30.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.30.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.30.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00002-of-00002.safetensors |
| `model.layers.30.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.31.input_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.31.mlp.down_proj.weight` | `[4096, 11008]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.31.mlp.gate_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.31.mlp.up_proj.weight` | `[11008, 4096]` | `torch.float16` | 86.00 MB | model-00002-of-00002.safetensors |
| `model.layers.31.post_attention_layernorm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |
| `model.layers.31.self_attn.k_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.31.self_attn.o_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.31.self_attn.q_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.layers.31.self_attn.rotary_emb.inv_freq` | `[64]` | `torch.float32` | 0.00 MB | model-00002-of-00002.safetensors |
| `model.layers.31.self_attn.v_proj.weight` | `[4096, 4096]` | `torch.float16` | 32.00 MB | model-00002-of-00002.safetensors |
| `model.norm.weight` | `[4096]` | `torch.float16` | 0.01 MB | model-00002-of-00002.safetensors |

</details>

