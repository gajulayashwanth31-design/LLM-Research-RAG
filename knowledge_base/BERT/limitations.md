---
paper: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
year: 2019
domain: "Large Language Models"
subdomain: "Transformer Architecture"
difficulty: "Intermediate"
document_type: "Limitations"
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

# Limitations

## Pre-training and Fine-tuning Mismatch

A limitation of the Masked Language Model objective is that the `[MASK]` token appears during pre-training but does not appear during fine-tuning.

This creates a mismatch between the pre-training and fine-tuning stages.

The paper mitigates this by using a masking strategy where selected tokens are:

- Replaced by `[MASK]` 80% of the time
- Replaced by a random token 10% of the time
- Left unchanged 10% of the time

## MLM Predicts Only a Subset of Tokens

BERT's masked language model predicts only the selected 15% of tokens in each training sequence.

The paper notes that this can result in slower convergence compared with a left-to-right model that predicts every token.

The authors report that the empirical improvements of MLM outweigh the additional training cost.

## High Pre-training Cost

BERT requires substantial computational resources for pre-training.

The paper reports:

- BERTBASE was trained using 4 Cloud TPU machines in a Pod configuration, corresponding to 16 TPU chips.
- BERTLARGE was trained using 16 Cloud TPU machines, corresponding to 64 TPU chips.
- Each pre-training run took approximately 4 days.

## Quadratic Attention Cost

Longer sequences are disproportionately expensive because Transformer attention has quadratic complexity with respect to sequence length.

To reduce training cost, the authors pre-train using sequence length 128 for 90% of the steps and sequence length 512 for the remaining 10%.

## Encoder Architecture Restriction

The paper notes that not all downstream tasks can be easily represented using a Transformer encoder architecture.

Some tasks may therefore require an additional task-specific model architecture.

## Feature-based Approach Trade-offs

The paper discusses cases where a feature-based approach can be advantageous.

One reason is that expensive representations can be pre-computed once and then reused with cheaper models for multiple experiments.

## Model Size and Fine-tuning Stability

The paper reports that BERTLARGE fine-tuning can sometimes be unstable on small datasets.

The authors therefore use multiple random restarts and select the best model based on development-set performance.

## Sentence Representation Caveat

The paper notes that the `[CLS]` representation is not necessarily a meaningful sentence representation before fine-tuning because it was trained using the NSP objective.