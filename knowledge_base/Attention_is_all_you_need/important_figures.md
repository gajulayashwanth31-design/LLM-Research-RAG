---
paper: "Attention Is All You Need"
year: 2017
domain: "Large Language Models"
subdomain: "Transformer Architecture"
difficulty: "Intermediate"
document_type: "Important Figures"
keywords:
  - Transformer
  - Architecture
  - Attention
generated_from: "Original Research Paper"
---

# Important Figures

---

# Figure 1 — Transformer Architecture

## Purpose

Figure 1 presents the complete architecture of the Transformer model, illustrating both the encoder and decoder stacks and the flow of information between them.

---

## Components Shown

### Input Processing

- Input Tokens
- Input Embeddings
- Positional Encoding

---

### Encoder Stack

The encoder consists of six identical layers.

Each layer contains:

- Multi-Head Self-Attention
- Add & Normalize (Residual Connection + Layer Normalization)
- Feed Forward Network
- Add & Normalize

---

### Decoder Stack

The decoder also consists of six identical layers.

Each decoder layer contains:

- Masked Multi-Head Self-Attention
- Add & Normalize
- Encoder-Decoder Attention
- Add & Normalize
- Feed Forward Network
- Add & Normalize

---

### Output Layer

The decoder output passes through:

- Linear Layer
- Softmax

to predict the next token in the output sequence.

---

## Key Observations

- The encoder and decoder have symmetric stacked architectures.
- Every encoder layer has two sub-layers.
- Every decoder layer has three sub-layers.
- Residual Connections and Layer Normalization surround every sub-layer.
- Positional Encoding is added before entering both encoder and decoder stacks.
- The architecture contains no recurrent or convolutional layers.

---

## Why It Is Important

This figure provides a complete overview of the Transformer architecture and demonstrates how attention mechanisms replace recurrence while preserving the encoder-decoder framework.

It is the most frequently referenced figure in the paper and serves as the foundation for understanding the remainder of the architecture. :contentReference[oaicite:2]{index=2}

---

# Figure 2 — Scaled Dot-Product Attention and Multi-Head Attention

## Purpose

Figure 2 illustrates the internal operation of the Transformer’s attention mechanism.

It consists of two diagrams:

- Scaled Dot-Product Attention
- Multi-Head Attention

---

## Left Diagram — Scaled Dot-Product Attention

The figure shows the computation of attention using:

- Query Matrix (Q)
- Key Matrix (K)
- Value Matrix (V)

The computation follows these steps:

1. Compute QKᵀ.
2. Scale by √dk.
3. Apply Softmax.
4. Multiply by the Value matrix.
5. Produce contextual output vectors.

---

## Right Diagram — Multi-Head Attention

The second diagram illustrates how multiple attention heads operate in parallel.

Each attention head:

- Receives independently projected Queries, Keys, and Values.
- Computes Scaled Dot-Product Attention.
- Produces an output representation.

The outputs of all attention heads are:

- Concatenated.
- Passed through a final linear projection.

This produces the final Multi-Head Attention output.

---

## Key Observations

- Multiple attention heads operate independently.
- Each head learns different relationships among tokens.
- Concatenation combines information from multiple representation subspaces.
- Scaling prevents extremely large attention scores.

---

## Why It Is Important

This figure introduces the two core innovations of the paper:

- Scaled Dot-Product Attention
- Multi-Head Attention

Together, these mechanisms form the computational core of the Transformer architecture and enable efficient learning of contextual relationships between tokens. :contentReference[oaicite:3]{index=3}

---

# Summary

The paper contains two primary architectural figures.

| Figure | Topic | Importance |
|---------|-------|------------|
| Figure 1 | Complete Transformer Architecture | Overall understanding of the model |
| Figure 2 | Attention Mechanisms | Explains the core computation performed inside the Transformer |

Both figures are fundamental for understanding the Transformer and are referenced throughout the architecture sections of the paper.