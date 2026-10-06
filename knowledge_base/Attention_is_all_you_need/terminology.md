---
paper: "Attention Is All You Need"
year: 2017
domain: "Large Language Models"
subdomain: "Transformer Architecture"
difficulty: "Intermediate"
document_type: "Terminology"
keywords:
  - Transformer
  - Attention
  - Encoder
  - Decoder
generated_from: "Original Research Paper"
---

# Terminology

---

# Attention

## Definition

A mechanism that computes the importance of different input elements by assigning weights to them, allowing the model to focus on the most relevant information.

## Where Used
Throughout the Transformer architecture.

## Related Terms

Self-Attention

Multi-Head Attention

Encoder-Decoder Attention

---

# Self-Attention

## Definition

An attention mechanism in which the Queries, Keys, and Values are generated from the same input sequence.

## Where Used

Encoder layers and decoder self-attention layers.

## Related Terms

Attention

Query

Key

Value

---

# Scaled Dot-Product Attention

## Definition

The attention mechanism proposed in the paper that computes attention weights using the scaled dot product of Queries and Keys before applying Softmax.

## Where Used

Inside every attention head.

## Related Terms

Query

Key

Value

Softmax

---

# Multi-Head Attention

## Definition

A mechanism that performs multiple attention operations in parallel using different learned projections of Queries, Keys, and Values.

## Where Used

Encoder Self-Attention

Decoder Self-Attention

Encoder-Decoder Attention

## Related Terms

Attention

Self-Attention

Scaled Dot-Product Attention

---

# Query (Q)

## Definition

A learned vector representing the information a token is seeking from other tokens.

## Where Used

Attention computation.

## Related Terms

Key

Value

Attention

---

# Key (K)

## Definition

A learned vector representing the information available in a token for comparison during attention computation.

## Where Used

Attention computation.

## Related Terms

Query

Value

Attention

---

# Value (V)

## Definition

A learned vector containing the information passed to other tokens after attention weights are computed.

## Where Used

Attention computation.

## Related Terms

Query

Key

Attention

---

# Encoder

## Definition

The component of the Transformer that converts an input sequence into contextual representations.

## Where Used

First half of the Transformer architecture.

## Related Terms

Decoder

Self-Attention

Feed Forward Network

---

# Decoder

## Definition

The component that generates the output sequence using previous outputs and encoder representations.

## Where Used

Second half of the Transformer architecture.

## Related Terms

Encoder

Masked Self-Attention

Encoder-Decoder Attention

---

# Masked Self-Attention

## Definition

A decoder self-attention mechanism that prevents positions from attending to future tokens.

## Where Used

Decoder layers.

## Related Terms

Decoder

Self-Attention

Masking

---

# Encoder-Decoder Attention

## Definition

An attention mechanism where Queries originate from the decoder while Keys and Values originate from the encoder.

## Where Used

Decoder layers.

## Related Terms

Cross Attention

Encoder

Decoder

---

# Positional Encoding

## Definition

A positional representation added to token embeddings so the Transformer can understand token order.

## Where Used

Input embeddings of both encoder and decoder.

## Related Terms

Embedding

Sinusoidal Encoding

---

# Feed Forward Network (FFN)

## Definition

A position-wise neural network consisting of two linear transformations separated by a ReLU activation.

## Where Used

Every encoder and decoder layer.

## Related Terms

Linear Layer

ReLU

---

# Residual Connection

## Definition

A shortcut connection that adds the input of a sub-layer to its output before Layer Normalization.

## Where Used

Every encoder and decoder sub-layer.

## Related Terms

Layer Normalization

Skip Connection

---

# Layer Normalization

## Definition

A normalization technique applied after residual connections to stabilize training.

## Where Used

Every encoder and decoder sub-layer.

## Related Terms

Residual Connection

Normalization

---

# Embedding

## Definition

A dense vector representation of a token used as input to the Transformer.

## Where Used

Input layer and output layer.

## Related Terms

Token

Vocabulary

Positional Encoding

---

# Softmax

## Definition

A mathematical function that converts logits into probabilities over the vocabulary.

## Where Used

Final decoder output layer.

## Related Terms

Probability Distribution

Vocabulary

---

# Beam Search

## Definition

A decoding algorithm that keeps multiple candidate output sequences during inference to improve generation quality.

## Where Used

Inference.

## Related Terms

Decoder

Softmax

Inference

---

# Byte Pair Encoding (BPE)

## Definition

A tokenization algorithm that builds a vocabulary by repeatedly merging frequent symbol pairs.

## Where Used

Training data preprocessing for the English-German dataset.

## Related Terms

Vocabulary

Tokenization

---

# Label Smoothing

## Definition

A regularization technique that replaces one-hot target labels with slightly smoothed probability distributions.

## Where Used

Training.

## Related Terms

Regularization

Softmax

---

# Dropout

## Definition

A regularization technique that randomly disables neurons during training to reduce overfitting.

## Where Used

Embeddings, attention layers, and feed-forward networks.

## Related Terms

Regularization

Residual Connection

---

# BLEU Score

## Definition

An automatic evaluation metric that measures the similarity between machine-generated translations and reference translations.

## Where Used

Machine translation evaluation.

## Related Terms

Evaluation Metric

Machine Translation

---

# Autoregressive Generation

## Definition

A sequence generation process where each output token is predicted using previously generated tokens.

## Where Used

Decoder during inference.

## Related Terms

Decoder

Masked Self-Attention

Beam Search