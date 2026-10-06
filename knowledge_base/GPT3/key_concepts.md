---
paper: "Language Models are Few-Shot Learners"
year: 2020
domain: "Large Language Models"
subdomain: "Autoregressive Language Models"
difficulty: "Intermediate"
document_type: "Key Concepts"
keywords:
  - GPT-3
  - In-Context Learning
  - Few-Shot Learning
  - Scaling
  - Zero-Shot Learning
  - One-Shot Learning
  - Autoregressive Language Modeling
generated_from: "Original Research Paper"
---

# GPT-3

## What is GPT-3?

GPT-3 is a 175-billion-parameter autoregressive language model introduced to study whether scaling language models improves task-agnostic performance.

## Core Idea

GPT-3 performs downstream tasks without gradient updates or task-specific fine-tuning.

Instead, task descriptions and demonstrations are provided as text in the model context.

# In-Context Learning

## What is it?

In-context learning is the ability of a language model to perform a task based on information supplied in its input context without changing its parameters.

## Why is it important?

It reduces dependence on task-specific training datasets and allows a single pretrained model to perform many different tasks.

# Zero-Shot Learning

## Definition

The model receives only a natural-language description of the task.

No examples are provided.

## Key Property

No gradient updates and no task-specific demonstrations are used.

# One-Shot Learning

## Definition

The model receives one demonstration of the task in addition to the task description.

## Purpose

The example helps communicate the expected input-output format.

# Few-Shot Learning

## Definition

The model receives multiple task demonstrations in its context.

## Typical Setting

GPT-3 experiments typically use approximately 10 to 100 demonstrations when they fit inside the 2048-token context window.

# Scaling

## Definition

Scaling refers to increasing model capacity and studying the resulting changes in performance.

## GPT-3 Scaling Experiment

The paper trains models from 125 million to 175 billion parameters.

## Finding

Performance generally improves smoothly with model size.

# Autoregressive Language Modeling

## Definition

GPT-3 predicts the next token based on the preceding context.

## Role in GPT-3

The same language-modeling objective is used for pretraining rather than creating separate task-specific objectives.

# Task-Agnostic Learning

## Definition

A task-agnostic model does not require a separate architecture or training procedure for every downstream task.

## GPT-3

GPT-3 uses text prompts and demonstrations to specify different tasks.

# Context Window

## Definition

The context window is the maximum amount of input context available to the model.

## GPT-3

The GPT-3 models use a 2048-token context window.

## Importance

The context window limits how many demonstrations can be supplied during few-shot learning.

# Model Scaling

## Model Range

The paper trains eight models:

- 125M
- 350M
- 760M
- 1.3B
- 2.7B
- 6.7B
- 13B
- 175B

## Observation

Larger models generally show stronger zero-shot, one-shot, and few-shot performance.

# Closed-Book Question Answering

## Definition

The model answers questions without retrieving external documents.

## GPT-3

GPT-3 demonstrates that large models can answer broad factual questions using information encoded in their parameters.

# Benchmark Contamination

## Definition

Benchmark contamination occurs when evaluation examples or related content appear in the model's pretraining data.

## Why it matters

Contamination can make benchmark performance appear better than the model's true generalization ability.

# Data Deduplication

## Purpose

GPT-3 uses fuzzy document-level deduplication to reduce redundancy.

## Additional Purpose

Deduplication helps preserve held-out validation sets as more reliable measures of overfitting.

# Scaling Laws

## Observation

Validation loss follows a smooth power-law trend with training compute.

## Downstream Relationship

The paper observes corresponding improvements across many downstream tasks.

# Model Parallelism

## Definition

Model parallelism distributes different parts of a model across multiple GPUs.

## GPT-3

Large GPT-3 models use model parallelism across both model width and depth.

# Transformer Architecture

## Basis

GPT-3 uses the same general architecture as GPT-2.

## Attention

GPT-3 uses alternating dense and locally banded sparse attention patterns.

# Training Dataset

## Major Sources

GPT-3 is trained using a mixture containing:

- Filtered Common Crawl
- WebText2
- Books1
- Books2
- Wikipedia

## Training Size

All models are trained for 300 billion tokens.

# Few-Shot Scaling

## Observation

Few-shot performance often improves more rapidly with model size than zero-shot performance.

## Interpretation

The authors suggest that larger models may be more proficient at using contextual demonstrations.

# Synthetic Text Generation

## Finding

GPT-3 can generate news-style articles that human evaluators sometimes have difficulty distinguishing from human-written articles.

## Significance

This demonstrates the strength of large-scale autoregressive text generation while also motivating concerns about misuse.

# Limitations

## Main Limitations

GPT-3 still exhibits:

- Long-form coherence problems
- Repetition
- Contradictions
- Weaknesses in some reasoning tasks
- Weaknesses in some NLI tasks
- Calibration issues
- Interpretability limitations
- Bias from training data
- High computational requirements

# Broader Impact

## Beneficial Uses

Potential applications include:

- Writing assistance
- Code completion
- Grammar assistance
- Search
- Question answering
- Game narrative generation

## Risks

The paper discusses:

- Misinformation
- Spam
- Phishing
- Social engineering
- Fraudulent academic writing
- Bias
- Fairness
- Energy usage