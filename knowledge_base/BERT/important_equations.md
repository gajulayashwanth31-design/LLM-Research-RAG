---
paper: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
year: 2019
domain: "Large Language Models"
subdomain: "Transformer Architecture"
difficulty: "Intermediate"
document_type: "Important Equations"
keywords:
  - BERT
  - Bidirectional Transformers
  - Language Model Pre-training
  - Masked Language Modeling
  - Next Sentence Prediction
  - Fine-tuning
  - Natural Language Understanding
generated_from: "Original Research Paper"
---

# Input Representation

## Token Representation

For each input token, BERT constructs its input representation by summing three embeddings:

\[
E_i = E_i^{token} + E_i^{segment} + E_i^{position}
\]

Where:

- \(E_i^{token}\) = token embedding
- \(E_i^{segment}\) = segment embedding
- \(E_i^{position}\) = position embedding

# SQuAD Question Answering

## Start Position Probability

For a token \(i\), the probability of it being the start of the answer span is computed using the dot product between its hidden representation \(T_i\) and the learned start vector \(S\):

\[
P_i =
\frac{e^{S \cdot T_i}}
{\sum_j e^{S \cdot T_j}}
\]

## End Position Probability

An analogous equation is used for predicting the probability that a token is the end of the answer span, using the learned end vector \(E\).

## Candidate Answer Span Score

For a candidate span beginning at position \(i\) and ending at position \(j\):

\[
s_{i,j} = S \cdot T_i + E \cdot T_j
\]

The maximum-scoring span satisfying \(j \geq i\) is selected.

# SQuAD 2.0

## No-Answer Score

For questions without an answer span, BERT uses the `[CLS]` token.

The no-answer score is:

\[
s_{null} = S \cdot C + E \cdot C
\]

where \(C\) is the final hidden representation of `[CLS]`.

## Answer Decision

A non-null answer is predicted when:

\[
\hat{s}_{i,j} > s_{null} + \tau
\]

where \(\tau\) is selected using the development set.

# GLUE Classification

## Classification Representation

For GLUE classification tasks, the final hidden representation \(C\) corresponding to `[CLS]` is used as the aggregate sequence representation.

The classification layer uses weights:

\[
W \in \mathbb{R}^{K \times H}
\]

where:

- \(K\) = number of labels
- \(H\) = hidden size

The paper computes a standard classification loss using:

\[
\log(\operatorname{softmax}(CW^T))
\]

# Model Dimensions

## Feed-Forward Size

The feed-forward/filter size is set to:

\[
4H
\]

Therefore:

- For \(H=768\): \(4H=3072\)
- For \(H=1024\): \(4H=4096\)

# No-Answer Span

## Best Non-Null Span

For SQuAD 2.0, the best non-null span is:

\[
\hat{s}_{i,j} =
\max_{j \geq i}
(S \cdot T_i + E \cdot T_j)
\]

This is compared with the no-answer score.