---
paper: "Language Models are Few-Shot Learners"
year: 2020
domain: "Large Language Models"
subdomain: "Autoregressive Language Models"
difficulty: "Intermediate"
document_type: "Important Figures"
keywords:
  - GPT-3
  - In-Context Learning
  - Scaling
  - Few-Shot Learning
  - Transformer
generated_from: "Original Research Paper"
---

# Figure 1.1 — Language Model Meta-Learning

## Purpose

Figure 1.1 illustrates the paper's view of language-model meta-learning.

The model develops broad skills during unsupervised pre-training.

At inference time, the model uses those skills to adapt to a task specified through context.

## Key Idea

The figure distinguishes the training process from the inference-time in-context learning process.

The model parameters remain fixed during the inner adaptation process.

# Figure 1.2 — In-Context Learning and Model Scale

## Purpose

Figure 1.2 demonstrates that larger models make increasingly effective use of contextual information.

It plots performance against the number of examples supplied in the context.

## Key Observation

The larger GPT-3 model shows a steeper in-context learning curve.

This indicates that increasing model size improves the ability to learn from contextual examples.

# Figure 1.3 — Aggregate Benchmark Performance

## Purpose

Figure 1.3 aggregates performance across accuracy-based benchmarks.

## Key Observation

Zero-shot performance improves with model size.

Few-shot performance increases more rapidly.

The figure supports the paper's central claim that larger models become increasingly capable of in-context learning.

# Figure 2.1 — Zero-Shot, One-Shot, Few-Shot and Fine-Tuning

## Purpose

Figure 2.1 contrasts four ways of applying language models:

- Fine-tuning
- Zero-shot
- One-shot
- Few-shot

## Key Difference

Fine-tuning updates model parameters.

Zero-shot, one-shot, and few-shot settings use only forward passes during evaluation.

## Few-Shot

Several examples are included in the context.

## One-Shot

One example is included.

## Zero-Shot

Only a natural-language task description is provided.

# Figure 3.1 — Smooth Scaling of Performance With Compute

## Purpose

Figure 3.1 shows validation loss as a function of training compute.

## Key Observation

Validation loss follows an approximately smooth power-law trend.

The relationship continues over a large range of model sizes and compute budgets.

# Figure 3.2 — LAMBADA Scaling

## Purpose

Figure 3.2 shows LAMBADA performance as model capacity increases.

## Key Observation

Few-shot performance improves strongly with model size.

The largest model substantially improves over earlier state-of-the-art results.

# Figure 3.3 — TriviaQA Scaling

## Purpose

Figure 3.3 shows TriviaQA performance as model size increases.

## Key Observation

Performance increases smoothly with model capacity.

One-shot and few-shot settings provide substantial improvements over zero-shot behavior.

# Figure 3.4 — Translation Scaling

## Purpose

Figure 3.4 shows few-shot translation performance across multiple language pairs.

## Key Observation

Performance generally improves as model capacity increases.

Translation into English is stronger than translation from English in several language pairs.

# Figure 3.5 — Winogrande Scaling

## Purpose

Figure 3.5 shows zero-shot, one-shot, and few-shot performance on Winogrande as model size increases.

## Key Observation

Few-shot performance benefits from increasing model capacity.

# Figure 4.2 — Benchmark Contamination Analysis

## Purpose

Figure 4.2 compares benchmark performance before and after removing potentially contaminated examples.

## Key Observation

Performance changes negligibly on most benchmarks.

Some benchmarks are flagged for further investigation because contamination may affect their reported results.

# Figure 2.2 — Training Compute

## Purpose

Figure 2.2 compares the compute used to train the different GPT-3 model sizes.

## Key Observation

Training compute increases dramatically as model size increases.

The largest models require substantially more computational resources.