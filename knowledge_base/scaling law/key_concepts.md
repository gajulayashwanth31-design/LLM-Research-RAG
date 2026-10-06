---
paper: "Scaling Laws for Neural Language Models"
year: 2020
domain: "Large Language Models"
subdomain: "Scaling Laws"
difficulty: "Advanced"
document_type: "Key Concepts"
keywords:
  - Scaling Laws
  - Power Laws
  - Model Size
  - Dataset Size
  - Compute
  - Sample Efficiency
  - Overfitting
  - Critical Batch Size
generated_from: "Original Research Paper"
---

# Scaling Laws

## Definition

Scaling laws describe empirical relationships between language-model performance and quantities such as model size, dataset size, training compute, and training time.

## Central Finding

Language-model loss follows smooth power-law trends across broad ranges of scale.

# Model Size

## Definition

Model size N is the number of non-embedding parameters.

## Scaling

Loss decreases approximately as a power law as model size increases.

# Dataset Size

## Definition

Dataset size D is the number of training tokens.

## Scaling

Loss decreases approximately as a power law as dataset size increases.

# Compute

## Definition

Training compute C represents the estimated non-embedding computation used during training.

## Approximation

C ≈ 6NBS

where N is model size, B is batch size, and S is training steps.

# Power Law

## Definition

A power law has the general form:

Y ∝ X^α

In the paper, loss typically decreases as:

L(X) ∝ X^-α

# Cross-Entropy Loss

## Definition

The main performance metric used throughout the paper.

Lower cross-entropy indicates better language-model performance.

# Sample Efficiency

## Definition

Sample efficiency measures how much data is required to reach a particular level of performance.

## Finding

Larger models are more sample-efficient.

# Overfitting

## Definition

Overfitting occurs when increasing model capacity without sufficient additional data produces diminishing test performance.

## Scaling

The paper finds that overfitting depends predictably on the relationship between N and D.

# Model-Dataset Trade-Off

## Definition

Model size and dataset size must be increased together to avoid bottlenecks.

## Finding

The required dataset size grows sublinearly with model size.

# Compute-Efficient Training

## Definition

Training that achieves the lowest loss for a fixed compute budget.

## Finding

Compute-efficient training favors large models trained for relatively few serial steps.

# Critical Batch Size

## Definition

Bcrit is the approximate batch size that provides a good trade-off between compute efficiency and training speed.

## Dependence

Bcrit primarily depends on the achieved loss.

# Early Stopping

## Definition

Stopping training before conventional convergence when doing so gives better use of a fixed compute budget.

## Scaling Result

Compute-efficient training should often stop substantially before convergence.

# Training Steps

## Definition

S is the number of parameter-update steps.

## Scaling

Training loss follows a predictable power-law relationship with training steps after an initial transient.

# Minimum Steps

## Definition

Smin is the estimated minimum number of optimization steps needed to reach a target loss when using a very large batch.

# Minimum Compute

## Definition

Cmin is the estimated minimum computation needed to reach a target loss when using a sufficiently small batch.

# Transformer Shape

## Definition

Shape refers to architectural quantities such as:

- Depth
- Width
- Attention heads
- Feed-forward dimension

## Finding

Performance depends weakly on shape when total non-embedding parameter count is fixed.

# Non-Embedding Parameters

## Definition

Parameters excluding vocabulary and positional embedding parameters.

## Importance

The paper finds cleaner scaling relationships when embeddings are excluded from model size.

# Generalization

## Definition

Performance on data distributions different from the training distribution.

## Finding

Generalization improves smoothly with model size.

# Learning Curve

## Definition

The relationship between model loss and training progress.

## Scaling

Learning curves can be modeled using power-law equations after an initial transient period.

# Compute-Efficient Frontier

## Definition

The set of model configurations that achieve near-optimal performance for a given compute budget.

# Diminishing Returns

## Definition

The reduction in incremental performance improvement as scale increases.

## Cause

Power-law scaling means that increasingly large resource increases are required for equivalent improvements.

# Data Bottleneck

## Definition

A situation where the model is large enough that additional model capacity provides little benefit because the dataset is insufficient.

# Model Bottleneck

## Definition

A situation where the dataset is large but the model lacks sufficient capacity to exploit additional data.

# Training Bottleneck

## Definition

A situation where model and data are sufficient but available computation or training time limits performance.

# WebText2

## Definition

The main training dataset used in the experiments.

It is an extended version of WebText based on outbound Reddit links.

# Autoregressive Language Modeling

## Definition

Predicting the next token from preceding context.

# Context Length

## Definition

The number of tokens available to the model as context.

## Main Setting

Most experiments use a 1024-token context.

# LSTM Comparison

## Finding

Transformers increasingly outperform LSTMs for later positions in long contexts.

# Universal Transformer

## Definition

A recurrent Transformer architecture that reuses parameters across processing steps.

## Finding

It can be slightly more parameter-efficient but requires additional computation per parameter.