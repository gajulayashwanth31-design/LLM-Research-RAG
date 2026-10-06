---
paper: "Language Models are Few-Shot Learners"
year: 2020
domain: "Large Language Models"
subdomain: "Autoregressive Language Models"
difficulty: "Intermediate"
document_type: "Terminology"
keywords:
  - GPT-3
  - Few-Shot Learning
  - In-Context Learning
  - Transformer
  - Scaling
  - Language Modeling
generated_from: "Original Research Paper"
---

# GPT-3

## Definition

A 175-billion-parameter autoregressive language model introduced in the paper to study large-scale in-context learning.

# In-Context Learning

## Definition

Performing a task using task information and demonstrations provided in the input context without updating model parameters.

# Zero-Shot Learning

## Definition

Performing a task from a natural-language task description without demonstrations.

# One-Shot Learning

## Definition

Performing a task using exactly one demonstration together with the task description.

# Few-Shot Learning

## Definition

Performing a task using multiple demonstrations supplied in the context without gradient updates.

# Fine-Tuning

## Definition

Updating a pretrained model's parameters using a task-specific supervised dataset.

# Autoregressive Language Model

## Definition

A language model that predicts the next token conditioned on preceding tokens.

# Meta-Learning

## Definition

A learning framework in which a model develops broad skills during training and uses those skills to adapt rapidly to new tasks.

# Task-Agnostic

## Definition

A system that is not trained specifically for one downstream task.

# Context Window

## Definition

The sequence of tokens available to the model as conditioning information.

# Scaling

## Definition

Increasing model capacity, training data, or compute and studying the resulting effect on performance.

# Model Parallelism

## Definition

Distributing different portions of a neural network across multiple computational devices.

# Sparse Attention

## Definition

An attention mechanism that restricts attention patterns instead of using unrestricted dense attention everywhere.

# Dense Attention

## Definition

An attention pattern where tokens can attend broadly across the available sequence.

# Language Modeling

## Definition

Predicting tokens in a sequence according to a language-modeling objective.

# Perplexity

## Definition

A metric used to evaluate language-modeling performance.

Lower perplexity indicates better predictive performance.

# Closed-Book Question Answering

## Definition

Question answering where the model must answer using information stored in its parameters rather than retrieved external documents.

# Open-Domain Question Answering

## Definition

Question answering over a broad knowledge domain, often using external retrieval systems.

# Data Contamination

## Definition

The presence of evaluation or benchmark information in the model's training data.

# Fuzzy Deduplication

## Definition

A deduplication procedure that identifies highly similar documents rather than requiring exact duplicate matches.

# Benchmark

## Definition

A dataset or evaluation suite used to measure model performance on a particular task.

# Natural Language Inference

## Definition

A task involving determining the relationship between pieces of text, such as whether one statement entails another.

# Common Sense Reasoning

## Definition

Reasoning about ordinary physical, social, or practical situations.

# Language Model Scaling Law

## Definition

The observed relationship between model performance and quantities such as model size and training compute.

# Model Capacity

## Definition

The representational capacity of a model, commonly associated with its number of trainable parameters.

# Token

## Definition

A unit processed by the language model as part of its input and output sequence.

# Contextual Demonstration

## Definition

An example of a task input and expected output supplied to the model as part of the context.