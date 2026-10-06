---
paper: "Scaling Laws for Neural Language Models"
year: 2020
domain: "Large Language Models"
subdomain: "Scaling Laws"
difficulty: "Advanced"
document_type: "Terminology"
keywords:
  - Scaling Laws
  - Neural Language Models
  - Compute
  - Optimization
  - Power Laws
generated_from: "Original Research Paper"
---

# Cross-Entropy Loss

## Definition

The average negative log-likelihood used as the primary performance metric for the language models.

# Model Size

## Definition

The number of non-embedding parameters in a model.

The paper denotes model size by N.

# Dataset Size

## Definition

The number of training tokens.

The paper denotes dataset size by D.

# Training Compute

## Definition

The estimated total non-embedding computation used during training.

The paper denotes it by C.

# Cmin

## Definition

The estimated minimum compute required to reach a target loss when training with a sufficiently small batch size.

# Smin

## Definition

The estimated minimum number of training steps required to reach a target loss when training with a sufficiently large batch size.

# Critical Batch Size

## Definition

The batch size that approximately balances training-time efficiency and compute efficiency.

The paper denotes it as Bcrit.

# Power Law

## Definition

A mathematical relationship in which one quantity changes as a power of another quantity.

# Scaling Exponent

## Definition

The exponent α in a relationship such as:

L ∝ X^-α

# Sample Efficiency

## Definition

The ability to achieve a target level of performance using relatively few training examples.

# Overfitting

## Definition

The degradation in test performance that occurs when model capacity increases relative to available training data.

# Early Stopping

## Definition

Stopping optimization before full convergence to achieve better performance under a limited-data or limited-compute condition.

# Compute-Efficient Training

## Definition

Training that minimizes loss for a fixed amount of computational resources.

# Compute-Efficient Frontier

## Definition

The set of model and training configurations that provide approximately optimal performance for their compute budget.

# Model Shape

## Definition

The distribution of parameters across architectural dimensions such as depth and width.

# Depth

## Definition

The number of Transformer layers.

# Width

## Definition

The dimension of the model's residual stream.

# Attention Heads

## Definition

The number of parallel attention heads in each Transformer layer.

# Feed-Forward Dimension

## Definition

The dimensionality of the intermediate feed-forward network inside a Transformer layer.

# Context Length

## Definition

The number of tokens available in the input context.

# Batch Size

## Definition

The number of training tokens processed before an optimization update.

# Optimization Step

## Definition

One parameter-update operation during training.

# Gradient Noise Scale

## Definition

A measure related to the noise in stochastic gradient estimates and used to predict useful batch sizes.

# Data Bottleneck

## Definition

A regime in which available training data limits further gains from increasing model capacity.

# Capacity-Limited

## Definition

A regime in which the model is too small to fully exploit the available dataset.

# Convergence

## Definition

The point at which additional training produces little or no improvement in the measured objective.

# Infinite-Data Limit

## Definition

The hypothetical regime in which the available dataset is sufficiently large that dataset size does not constrain performance.

# Infinite-Model Limit

## Definition

The hypothetical regime in which model capacity is sufficiently large that model size does not constrain performance.

# Training Curve

## Definition

A curve showing model loss as training progresses.

# Token

## Definition

A unit of text processed by the language model.

# PF-Day

## Definition

A unit of computational work.

One PF-day corresponds to 10^15 floating-point operations per second sustained for 24 hours.

# Non-Embedding Parameters

## Definition

Model parameters excluding vocabulary and positional embedding parameters.

# Autoregressive Modeling

## Definition

Predicting each token conditioned on preceding tokens.

# Transformer

## Definition

The neural architecture used for the primary scaling experiments.

# LSTM

## Definition

A recurrent neural-network architecture used as a comparison model.

# Universal Transformer

## Definition

A Transformer variant that reuses parameters across recurrent processing steps.

# WebText2

## Definition

The primary language-model training dataset used in the study.

# Tokenization

## Definition

The process of converting raw text into tokens.

The models use byte-pair encoding with a vocabulary of 50,257 tokens.
