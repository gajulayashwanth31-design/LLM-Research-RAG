---
paper: "Language Models are Few-Shot Learners"
year: 2020
domain: "Large Language Models"
subdomain: "Autoregressive Language Models"
difficulty: "Intermediate"
document_type: "Paper Statistics"
keywords:
  - GPT-3
  - Model Size
  - Training Data
  - Parameters
  - Architecture
  - Scaling
generated_from: "Original Research Paper"
---

# GPT-3 Model

## Parameter Count

175 billion trainable parameters.

## Layers

96 Transformer layers.

## Model Dimension

12,288.

## Attention Heads

96.

## Attention Head Dimension

128.

## Context Window

2048 tokens.

## Feed-Forward Dimension

The feed-forward dimension is four times the model dimension.

# Model Family

## GPT-3 Small

- Parameters: 125M
- Layers: 12
- Model dimension: 768
- Attention heads: 12
- Head dimension: 64
- Batch size: 0.5M tokens
- Learning rate: 6.0 × 10^-4

## GPT-3 Medium

- Parameters: 350M
- Layers: 24
- Model dimension: 1024
- Attention heads: 16
- Head dimension: 64
- Batch size: 0.5M tokens
- Learning rate: 3.0 × 10^-4

## GPT-3 Large

- Parameters: 760M
- Layers: 24
- Model dimension: 1536
- Attention heads: 16
- Head dimension: 96
- Batch size: 0.5M tokens
- Learning rate: 2.5 × 10^-4

## GPT-3 XL

- Parameters: 1.3B
- Layers: 24
- Model dimension: 2048
- Attention heads: 24
- Head dimension: 128
- Batch size: 1M tokens
- Learning rate: 2.0 × 10^-4

## GPT-3 2.7B

- Parameters: 2.7B
- Layers: 32
- Model dimension: 2560
- Attention heads: 32
- Head dimension: 80
- Batch size: 1M tokens
- Learning rate: 1.6 × 10^-4

## GPT-3 6.7B

- Parameters: 6.7B
- Layers: 32
- Model dimension: 4096
- Attention heads: 32
- Head dimension: 128
- Batch size: 2M tokens
- Learning rate: 1.2 × 10^-4

## GPT-3 13B

- Parameters: 13B
- Layers: 40
- Model dimension: 5140
- Attention heads: 40
- Head dimension: 128
- Batch size: 2M tokens
- Learning rate: 1.0 × 10^-4

## GPT-3 175B

- Parameters: 175B
- Layers: 96
- Model dimension: 12288
- Attention heads: 96
- Head dimension: 128
- Batch size: 3.2M tokens
- Learning rate: 0.6 × 10^-4

# Training

## Total Training Tokens

300 billion tokens.

## Training Hardware

The models were trained on V100 GPUs.

## Model Parallelism

Model parallelism is used within matrix multiplications and across Transformer layers.

# Training Dataset

## Filtered Common Crawl

- Quantity: 410B tokens
- Training weight: 60%
- Approximate epochs at 300B training tokens: 0.44

## WebText2

- Quantity: 19B tokens
- Training weight: 22%
- Approximate epochs: 2.9

## Books1

- Quantity: 12B tokens
- Training weight: 8%
- Approximate epochs: 1.9

## Books2

- Quantity: 55B tokens
- Training weight: 8%
- Approximate epochs: 0.43

## Wikipedia

- Quantity: 3B tokens
- Training weight: 3%
- Approximate epochs: 3.4

# Dataset Processing

## Common Crawl

The Common Crawl data was filtered using similarity to high-quality reference corpora.

## Deduplication

Fuzzy document-level deduplication was performed within and across datasets.

## Additional Data

The final training mixture includes WebText2, Books1, Books2, and English Wikipedia.

# Evaluation

## Main Settings

GPT-3 is evaluated in:

- Zero-shot
- One-shot
- Few-shot

## Typical Demonstrations

Few-shot evaluation commonly uses approximately 10 to 100 examples, constrained by the 2048-token context window.

# Major Evaluation Categories

The paper evaluates:

- Language modeling
- Cloze and completion
- Closed-book question answering
- Translation
- Winograd-style tasks
- Common-sense reasoning
- Reading comprehension
- SuperGLUE
- Natural language inference
- Synthetic and qualitative tasks

# Selected Results

## Penn Tree Bank

GPT-3 achieves a zero-shot perplexity of 20.5.

## LAMBADA

GPT-3 achieves:

- Zero-shot accuracy: 76.2%
- One-shot accuracy: 72.5%
- Few-shot accuracy: 86.4%

## TriviaQA

GPT-3 achieves:

- Zero-shot: 64.3%
- One-shot: 68.0%
- Few-shot: 71.2%

## WebQuestions

GPT-3 achieves:

- Zero-shot: 14.4%
- One-shot: 25.3%
- Few-shot: 41.5%

## Natural Questions

GPT-3 achieves:

- Zero-shot: 14.6%
- One-shot: 23.0%
- Few-shot: 29.9%

## Winogrande

GPT-3 achieves:

- Zero-shot: 70.2%
- One-shot: 73.2%
- Few-shot: 77.7%

# Scaling Findings

## Validation Loss

Validation loss follows an approximately smooth power-law trend with training compute.

## Downstream Tasks

Performance generally improves as model capacity increases.

## In-Context Learning

Larger models generally make more effective use of contextual demonstrations.

# Data Contamination

## Contamination Analysis

The paper constructs cleaned versions of benchmarks to investigate potential training-test overlap.

## General Finding

Most benchmarks show only small performance changes after removing potentially contaminated examples.

## Flagged Results

PIQA and Winograd results receive additional caution because contamination analysis found potential overlap effects.

# Paper Scope

## Main Contribution

The paper demonstrates that scaling autoregressive language models can substantially improve task-agnostic few-shot performance.

## Central Finding

A sufficiently large language model can perform many NLP tasks from instructions and demonstrations without task-specific gradient updates.

## Main Qualification

The paper also demonstrates that scaling does not eliminate weaknesses in reasoning, coherence, evaluation reliability, bias, or computational cost.
