---
paper: "Attention Is All You Need"
year: 2017
domain: "Large Language Models"
subdomain: "Transformer Architecture"
difficulty: "Intermediate"
document_type: "Important Equations"
keywords:
  - Attention
  - Multi-Head Attention
  - Positional Encoding
generated_from: "Original Research Paper"
---

# Important Equations

---

# Equation 1 — Scaled Dot-Product Attention

## Equation

Attention(Q, K, V) = Softmax((QKᵀ) / √dk) V

---

## Variables

| Symbol | Meaning |
|---------|---------|
| Q | Query Matrix |
| K | Key Matrix |
| V | Value Matrix |
| dk | Dimension of Key vectors |

---

## Meaning

This equation computes attention by measuring the similarity between Query and Key vectors.

The similarity scores are scaled by √dk before applying the Softmax function.

The resulting attention weights are multiplied with the Value vectors to produce contextual representations.

---

## Why It Is Important

This is the core computation performed by every attention head in the Transformer.

It replaces recurrent computations with direct interactions between all tokens.

---

## Applications

- Self-Attention
- Encoder-Decoder Attention
- Multi-Head Attention

---

# Equation 2 — Multi-Head Attention

## Equation

MultiHead(Q,K,V) = Concat(head₁,...,headₕ)Wᴼ

where

headᵢ = Attention(QWᵢQ, KWᵢK, VWᵢV)

---

## Variables

| Symbol | Meaning |
|---------|---------|
| headᵢ | Output of the i-th attention head |
| WQ | Query projection matrix |
| WK | Key projection matrix |
| WV | Value projection matrix |
| WO | Final output projection matrix |
| h | Number of attention heads |

---

## Meaning

Queries, Keys, and Values are projected into multiple lower-dimensional spaces.

Each attention head independently computes Scaled Dot-Product Attention.

The outputs are concatenated and projected to form the final representation.

---

## Why It Is Important

Multi-Head Attention allows the model to learn different relationships simultaneously.

Instead of one attention distribution, the model learns several specialized attention patterns.

---

## Applications

- Encoder Self-Attention
- Decoder Self-Attention
- Encoder-Decoder Attention

---

# Equation 3 — Position-wise Feed Forward Network

## Equation

FFN(x) = max(0, xW₁ + b₁)W₂ + b₂

---

## Variables

| Symbol | Meaning |
|---------|---------|
| x | Input representation |
| W₁ | First weight matrix |
| b₁ | First bias vector |
| W₂ | Second weight matrix |
| b₂ | Second bias vector |

---

## Meaning

Each token representation is passed through:

1. Linear layer
2. ReLU activation
3. Second linear layer

The same feed-forward network is applied independently to every token.

---

## Why It Is Important

The Feed Forward Network introduces non-linearity and enriches token representations after attention has aggregated contextual information.

---

## Applications

- Encoder layers
- Decoder layers

---

# Equation 4 — Residual Connection with Layer Normalization

## Equation

LayerNorm(x + Sublayer(x))

---

## Variables

| Symbol | Meaning |
|---------|---------|
| x | Input to the sub-layer |
| Sublayer(x) | Output of the attention or feed-forward network |

---

## Meaning

The input is added directly to the output of a sub-layer.

The combined representation is then normalized using Layer Normalization.

---

## Why It Is Important

Residual Connections improve gradient flow, while Layer Normalization stabilizes training.

Together they enable deep Transformer models to train effectively.

---

## Applications

- Every encoder sub-layer
- Every decoder sub-layer

---

# Equation 5 — Positional Encoding

## Equation

PE(pos,2i) = sin(pos / 10000^(2i/dmodel))

PE(pos,2i+1) = cos(pos / 10000^(2i/dmodel))

---

## Variables

| Symbol | Meaning |
|---------|---------|
| pos | Position of the token |
| i | Embedding dimension index |
| dmodel | Embedding dimension (512 in the base model) |

---

## Meaning

Even dimensions use sine functions.

Odd dimensions use cosine functions.

Together they generate unique positional vectors that are added to token embeddings.

---

## Why It Is Important

Since the Transformer contains neither recurrence nor convolution, positional encoding provides information about token order.

---

## Applications

- Encoder input
- Decoder input

---

# Equation 6 — Learning Rate Schedule

## Equation

lrate = dmodel^(-0.5) × min(step_num^(-0.5), step_num × warmup_steps^(-1.5))

---

## Variables

| Symbol | Meaning |
|---------|---------|
| lrate | Learning rate |
| dmodel | Model embedding dimension |
| step_num | Current training step |
| warmup_steps | Number of warmup steps (4000) |

---

## Meaning

The learning rate increases linearly during the warmup phase.

After warmup, it decreases proportionally to the inverse square root of the training step.

---

## Why It Is Important

This learning rate schedule stabilizes optimization during the early stages of training and improves convergence.

---

## Applications

- Transformer training

---

# Summary

| Equation | Purpose |
|----------|---------|
| Scaled Dot-Product Attention | Compute attention scores |
| Multi-Head Attention | Learn multiple attention patterns |
| Feed Forward Network | Transform token representations |
| Residual + LayerNorm | Stabilize deep network training |
| Positional Encoding | Encode token positions |
| Learning Rate Schedule | Optimize training process |