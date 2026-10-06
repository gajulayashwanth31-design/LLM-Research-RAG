---
paper: "Scaling Laws for Neural Language Models"
year: 2020
domain: "Large Language Models"
subdomain: "Scaling Laws"
difficulty: "Advanced"
document_type: "Paper Overview"
keywords:
  - Scaling Laws
  - Neural Language Models
  - Model Size
  - Dataset Size
  - Compute
  - Power Laws
  - Sample Efficiency
  - Optimal Compute Allocation
  - Transformer
  - Overfitting
  - Critical Batch Size
generated_from: "Original Research Paper"
---

# Paper Overview

## Paper Summary

"Scaling Laws for Neural Language Models" studies how the performance of neural language models changes as the scale of the model, training dataset, and computational budget increases.

The paper focuses primarily on autoregressive Transformer language models.

The main performance metric is cross-entropy loss.

The central result is that language-model loss follows remarkably smooth power-law relationships with several important scale variables.

These variables include:

- Model size
- Dataset size
- Training compute
- Training steps
- Context length

The authors investigate these relationships across very large ranges of scale.

Some observed trends span more than six orders of magnitude, and some of the experiments cover more than seven orders of magnitude in scale.

The paper finds that performance depends strongly on the overall scale of the model but only weakly on many architectural shape parameters when the total number of non-embedding parameters is held approximately fixed.

The main model-size variable is N, the number of non-embedding parameters.

The main dataset-size variable is D, the number of training tokens.

The main compute variable is C or Cmin, representing training computation.

The paper shows that each of these quantities follows an approximate power-law relationship with loss when the other quantities are not acting as bottlenecks.

The paper also studies overfitting.

When model size and dataset size are increased together, performance continues to improve predictably.

However, increasing one while keeping the other fixed eventually leads to diminishing returns.

The authors develop an empirical equation that jointly describes the dependence of loss on model size and dataset size.

The paper also studies training-time scaling.

Learning curves can be modeled using power laws involving model size and the number of training steps.

This allows the authors to estimate how much performance would be obtained by continuing training.

A particularly important result concerns the allocation of a fixed compute budget.

The paper finds that compute-efficient training should place most additional compute into increasing model size rather than dramatically increasing the number of serial training steps.

Larger models are more sample-efficient.

They can reach a particular level of performance using fewer optimization steps and fewer training examples than smaller models.

The paper therefore argues that compute-efficient training involves training relatively large models on a comparatively modest amount of data and stopping before conventional convergence.

# Problem Addressed

## Understanding Language Model Scaling

Language-model performance depends on many variables.

These include architecture, model size, training data, optimization, training time, and computational resources.

Without a quantitative understanding of these relationships, deciding how to allocate resources when training larger models is difficult.

The paper aims to empirically characterize these relationships.

## Resource Allocation

Training increasingly large language models requires substantial computation.

Researchers must decide how to distribute a fixed compute budget among:

- Model parameters
- Training data
- Batch size
- Number of optimization steps

The paper seeks to determine which allocation provides the best performance.

## Model Size Versus Dataset Size

A larger model has greater capacity.

However, a model that is too large relative to its training dataset can overfit.

Conversely, a large dataset does not necessarily improve performance if the model lacks sufficient capacity.

The paper studies the interaction between model size and dataset size.

## Training Time

Training a model for longer generally improves performance.

However, longer training consumes additional compute.

The authors investigate whether it is more efficient to train a smaller model for longer or a larger model for fewer steps.

# Motivation

## Rapid Growth of Language Models

Before this work, language models had already shown strong improvements as model sizes increased.

The authors wanted to determine whether these improvements followed predictable mathematical relationships.

## Predictability

If language-model performance follows stable scaling laws, researchers can estimate the expected performance of models that have not yet been trained.

This could make large-scale model development more systematic.

## Compute-Efficient Training

The amount of available computation is often the primary practical constraint.

Understanding the optimal allocation of a fixed compute budget can therefore have a large impact on the performance obtained from a training run.

# Main Research Questions

## Model Size

How does language-model loss change as the number of parameters increases?

## Dataset Size

How does loss change as the amount of training data increases?

## Compute

How does loss change as the amount of training computation increases?

## Model Shape

How important are architectural choices such as depth, width, number of attention heads, and feed-forward dimension when total parameter count is fixed?

## Overfitting

How does overfitting depend jointly on model size and dataset size?

## Training Time

How does loss change as the number of optimization steps increases?

## Batch Size

How should batch size be chosen to balance training speed and computational efficiency?

## Compute Allocation

How should a fixed compute budget be divided between model size, data, batch size, and training steps?

# Experimental Setup

## Primary Architecture

The main experiments use decoder-only Transformer language models.

The Transformer architecture is used because it provides a scalable language-modeling architecture and allows models over a wide range of sizes to be compared.

## Language Modeling Objective

The models are trained using autoregressive language modeling.

The objective is the cross-entropy loss averaged over tokens.

## Context Length

The principal experiments use a context length of 1024 tokens.

Some experiments use shorter contexts.

## Dataset

The primary training dataset is WebText2.

WebText2 is an extended version of the WebText dataset.

## WebText2 Construction

The original WebText dataset consists of outbound links from Reddit.

The links used in WebText had received at least 3 karma.

The WebText2 extension adds links from January through October 2018.

The 3-karma threshold is used as a heuristic for whether users found the linked content useful or interesting.

## WebText2 Size

The dataset contains approximately:

- 20.3 million documents
- 96 GB of text
- 1.62 × 10^10 words
- 2.29 × 10^10 tokens after tokenization

Approximately 6.6 × 10^8 tokens are reserved for testing.

## Tokenization

The models use a reversible tokenizer.

The vocabulary size is:

50,257 tokens.

The tokenizer is based on byte-pair encoding.

# Important Variables

## Loss

L represents the cross-entropy loss.

The loss is generally averaged over tokens in the context.

Lower loss corresponds to better language-model performance.

## Model Size

N represents the number of non-embedding parameters.

Embedding and positional parameters are excluded from N.

This definition produces cleaner scaling relationships.

## Dataset Size

D represents the number of training tokens.

## Compute

C represents estimated non-embedding training compute.

The paper approximates compute as:

C ≈ 6NBS

where:

- N = non-embedding parameter count
- B = batch size
- S = number of training steps

## Critical Batch Size

Bcrit represents the batch size that approximately balances compute efficiency and training-time efficiency.

## Minimum Compute

Cmin represents an estimate of the minimum compute needed to reach a target loss when using a sufficiently small batch size.

## Minimum Steps

Smin represents the minimum number of optimization steps needed to reach a target loss when using a sufficiently large batch size.

# Model Size Scaling

## Basic Relationship

When dataset size is sufficiently large and models are trained to convergence, test loss follows an approximate power law in model size.

The relationship is:

L(N) = (Nc / N)^αN

The fitted exponent is approximately:

αN ≈ 0.076.

## Interpretation

Increasing model size improves performance.

However, the improvement exhibits diminishing returns.

Doubling model size does not halve the loss.

Instead, the loss decreases according to a small power-law exponent.

## Range of Evidence

The experiments cover models from very small networks to models with more than one billion non-embedding parameters.

The observed relationship remains approximately smooth across the studied range.

# Dataset Size Scaling

## Basic Relationship

For sufficiently large models trained on finite datasets, test loss follows an approximate power law in dataset size.

The relationship is:

L(D) = (Dc / D)^αD

The fitted exponent is approximately:

αD ≈ 0.095.

## Interpretation

Increasing dataset size improves performance.

However, dataset scaling also exhibits diminishing returns.

The model must have sufficient capacity to benefit from additional data.

## Dataset Bottleneck

If model capacity is fixed while dataset size continues increasing, performance eventually becomes model-limited.

Additional data produces progressively smaller improvements.

# Compute Scaling

## Basic Relationship

When model size and dataset size are sufficiently large and compute is allocated efficiently, loss follows an approximate power law in training compute.

The relationship is:

L(Cmin) = (Cmin,c / Cmin)^αCmin

The paper reports:

αCmin ≈ 0.050.

## Interpretation

Increasing compute improves performance.

However, the small exponent means that substantial additional computation is required for relatively modest improvements in loss.

## Importance

The compute scaling relationship provides a way to estimate performance as available computational resources increase.

# Model Shape

## Shape Parameters

The authors vary architectural parameters including:

- Number of layers
- Model width
- Number of attention heads
- Feed-forward dimension

## Main Finding

When total non-embedding parameter count is held fixed, model performance depends only weakly on these shape parameters over a broad range.

## Depth and Width

A wide range of depth-to-width configurations can achieve similar loss.

The paper therefore finds that total model scale is substantially more important than the precise shape of the model within reasonable limits.

# Why Exclude Embeddings?

## Embedding Parameters

Transformer models contain vocabulary and positional embedding parameters.

The authors exclude these from the model-size variable N.

## Reason

When embedding parameters are included, the scaling relationship appears to depend more strongly on model depth.

When embedding parameters are excluded, models with different depths fall onto a much cleaner common scaling trend.

## Result

Non-embedding parameter count provides a more useful measure of model scale for the experiments.

# Transformer Parameter Scaling

## Model Parameters

The paper approximates the number of non-embedding parameters as:

N ≈ 2 dmodel nlayer (2 dattn + dff)

For the standard configuration:

dattn = dff / 4 = dmodel

This gives:

N ≈ 12 nlayer dmodel^2

## Variables

- nlayer = number of Transformer layers
- dmodel = residual-stream dimension
- dff = feed-forward dimension
- dattn = attention output dimension

# Compute Estimation

## Forward Pass

The approximate forward-pass computation is:

Cforward ≈ 2N + 2nlayer nctx dmodel

The first term is associated with parameter-dependent computation.

The second term represents context-dependent computation.

## Training Compute

Accounting approximately for the forward and backward passes gives:

C ≈ 6N

floating-point operations per training token.

Therefore:

C ≈ 6NBS

for a training run with batch size B and S optimization steps.

# Training Procedure

## Optimizer

Most experiments use Adam.

The largest models above approximately one billion parameters use Adafactor because of memory constraints.

## Number of Steps

Unless otherwise specified, models are trained for:

2.5 × 10^5 steps.

## Batch Size

The standard training setup uses:

512 sequences × 1024 tokens.

## Learning Rate Schedule

The standard schedule consists of:

- 3000-step linear warmup
- Cosine decay to zero

## Learning Rate

The authors experiment with multiple learning rates and schedules.

They find that converged results are largely independent of the learning-rate schedule within the settings they investigated.

# Generalization Across Data Distributions

## Experimental Setup

Models are trained on WebText2.

They are then evaluated on other text distributions.

These include:

- Books
- Wikipedia
- Common Crawl
- Other Internet text

## Finding

Performance on other distributions improves smoothly as model size increases.

## Constant Offset

The loss on other distributions tends to remain above the WebText2 loss by a relatively small and slowly changing offset.

## Training Phase

Generalization to other distributions depends strongly on the validation loss achieved on the training distribution.

It does not strongly depend on whether the model has reached convergence.

# LSTM Comparison

## Motivation

The authors compare Transformer language models with LSTMs.

This tests whether the observed scaling behavior is specific to Transformers.

## Result

LSTMs perform competitively for tokens appearing early in the context.

However, their performance degrades relative to Transformers for tokens appearing later in the context.

## Long Contexts

Transformers make better use of long contexts.

As model size increases, Transformers increasingly outperform LSTMs on later-context prediction.

# Universal Transformers

## Comparison

The paper also compares standard Transformers with recurrent or Universal Transformer variants.

## Parameter Reuse

Universal Transformers reuse parameters across processing steps.

## Findings

They can perform slightly better as a function of parameter count.

However, this comes with increased compute per parameter.

# Dataset Size and Model Size Together

## Joint Scaling

Model size and dataset size cannot be treated as completely independent variables.

If one is increased while the other is fixed, the system eventually reaches a bottleneck.

## Diminishing Returns

Increasing dataset size without increasing model capacity eventually gives diminishing returns.

Increasing model capacity without increasing data eventually produces overfitting.

## Balanced Scaling

The paper finds that model and dataset size should grow together.

The required dataset size grows sublinearly with model size.

# Overfitting

## Definition

Overfitting occurs when increasing model capacity no longer improves test performance because the available training data is insufficient.

## Scaling Behavior

The paper finds that the degree of overfitting depends predictably on a combination of model size and dataset size.

## Model-Dataset Relationship

The relevant scaling suggests:

D ∝ N^0.74

for approximately maintaining the same level of overfitting.

## Interpretation

If model size increases by approximately 8×, dataset size only needs to increase by approximately 5× to avoid a similar performance penalty.

# Joint Loss Equation

## L(N,D)

The paper proposes a joint equation:

L(N,D) =
[(Nc/N)^(αN/αD) + Dc/D]^αD

This equation combines model-size and dataset-size effects.

## Purpose

The equation describes how test loss changes when both model size and dataset size vary.

## Infinite-Data Limit

As dataset size approaches infinity, the equation approaches the model-size scaling law.

## Infinite-Model Limit

As model size becomes sufficiently large, the equation approaches the dataset-size scaling law.

# Training-Time Scaling

## Learning Curves

The paper finds that learning curves follow predictable power-law behavior after an initial transient period.

## Joint Model-Size and Training-Step Equation

The proposed relationship is:

L(N,S) =
(Nc/N)^αN
+
(Sc/Smin(S))^αS

where:

- S = observed training steps
- Smin(S) = estimated minimum steps after adjusting for batch size
- Sc ≈ 2.1 × 10^3
- αS ≈ 0.76

## Prediction

Early portions of training curves can be used to estimate the loss that would be reached with substantially longer training.

# Critical Batch Size

## Definition

The critical batch size is the approximate batch size at which the tradeoff between training speed and compute efficiency becomes balanced.

## Small Batch Sizes

When batch size is below Bcrit, increasing batch size can improve training speed with relatively little loss in compute efficiency.

## Large Batch Sizes

When batch size exceeds Bcrit, increasing the batch size produces diminishing returns in compute efficiency.

## Power Law

The paper finds:

Bcrit(L) ≈ B* / L^(1/αB)

with:

B* ≈ 2 × 10^8 tokens

and:

αB ≈ 0.21.

## Dependence on Loss

The critical batch size depends primarily on the loss achieved rather than directly on model size.

# Compute-Efficient Training

## Main Question

Given a fixed amount of compute, what model size and training strategy produce the lowest possible loss?

## Optimal Model Size

The paper finds:

Nopt ∝ Cmin^0.73

## Optimal Batch Size

The optimal batch size grows approximately as:

B ∝ Cmin^0.24

## Training Steps

The number of optimization steps grows very slowly:

Smin ∝ Cmin^0.03

## Dataset Size

The amount of data grows approximately as:

D ∝ Cmin^0.27

for one-epoch compute-efficient training.

## Central Result

Most additional compute should be allocated to increasing model size.

Only modest increases in dataset size are required.

The number of serial optimization steps should increase very slowly.

# Sample Efficiency

## Definition

Sample efficiency describes how much data is required to achieve a particular level of performance.

## Scaling Result

Larger models are more sample-efficient than smaller models.

## Consequence

A larger model can reach a particular loss using fewer training examples.

## Importance

This challenges the intuition that compute-efficient training should primarily involve training a smaller model on a very large dataset until convergence.

# Early Stopping

## Compute-Efficient Training

Compute-efficient training often stops significantly before the model reaches conventional convergence.

## Reason

For a fixed compute budget, training a larger model for fewer steps can produce better performance than training a smaller model for many more steps.

## Trade-Off

Larger models require more computation per training step but can reach useful loss levels in substantially fewer steps.

# Optimal Allocation Result

## Model Size

Model size grows rapidly with available compute.

## Dataset Size

Dataset size grows much more slowly.

## Batch Size

Batch size can grow substantially to exploit parallel hardware.

## Serial Training Steps

The number of serial steps grows very slowly.

## Overall Strategy

As compute increases:

1. Increase model size substantially.
2. Increase dataset size moderately.
3. Increase batch size.
4. Avoid unnecessarily long serial training.

# Compute-Efficient Frontier

## Definition

The compute-efficient frontier represents the best performance achievable for a given amount of training compute.

## Optimal Model

Every compute budget has an associated approximately optimal model size.

## Robustness

The optimum is not extremely narrow.

Models between approximately 0.6× and 2.2× the optimal size can be trained with only around 20% additional compute.

## Practical Implication

The exact optimal model size is not always necessary.

A moderately suboptimal model can still provide near-optimal compute efficiency.

# Data Requirements

## Single-Epoch Constraint

If compute-efficient training never reuses data, the amount of data that can be productively processed grows approximately as:

D(Cmin) ∝ Cmin^0.26

## Comparison

This growth is substantially slower than the growth of optimal model size.

## Future Bottleneck

The paper predicts that eventually compute-efficient training may become data-limited even without reusing training examples.

# Scaling Limits

## Diminishing Returns

Power-law scaling means that improvements become progressively smaller as scale increases.

## Eventual Breakdown

The authors do not claim that the observed power laws continue indefinitely.

At sufficiently large scales, the laws must eventually change or flatten.

## Estimated Intersection

The authors estimate that the compute-efficient and data-limited scaling curves could intersect around:

- Compute: ~10^4 PF-days
- Model size: ~10^12 parameters
- Dataset size: ~10^12 tokens
- Loss: ~1.7 nats/token

These values are highly uncertain.

The authors explicitly state that the scaling laws may break down before this point.

# Discussion

## Predictive Framework

The scaling equations go beyond merely describing empirical observations.

They can be used to predict:

- Loss from model size
- Loss from dataset size
- Loss from compute
- Degree of overfitting
- Early stopping
- Critical batch size
- Optimal model size
- Data requirements

## Analogy

The authors compare the scaling relationships to an equation such as the ideal gas law.

The analogy is that a relatively simple relationship can describe macroscopic behavior despite complicated underlying microscopic details.

## Universality

The authors speculate that similar scaling laws may apply to other generative modeling problems.

However, they explicitly state that it is unknown which findings are specific to natural language and which may be universal.

# Potential Extensions

## Other Modalities

The authors suggest testing the scaling relationships on:

- Images
- Audio
- Video

## Theoretical Understanding

The paper calls for a theoretical framework explaining the observed scaling laws.

## Capability Scaling

Another important open question is whether continued reductions in language-model loss always translate into meaningful improvements on downstream capabilities.

# Practical Implications

## Model Development

When deciding between a larger model and more training steps, the paper suggests that larger models are often preferable under compute-efficient conditions.

## Dataset Planning

Dataset size should increase with model size, but not proportionally.

## Hardware Planning

Increasing model size creates a need for efficient model parallelism and distributed training.

## Training Strategy

Batch size should be selected according to the critical batch size associated with the target loss.

# Overall Significance

## Empirical Discovery

The paper establishes that neural language-model performance follows surprisingly smooth scaling relationships across model size, dataset size, and compute.

## Predictability

The relationships allow researchers to estimate the performance of larger models without necessarily training every possible configuration.

## Large Models

The paper provides evidence that larger models can be more sample-efficient and more compute-efficient than smaller models trained to convergence.

## Foundation for Later Work

The results provide a quantitative framework for thinking about how language-model training should scale as available computation increases.

# Conclusion

The paper demonstrates that Transformer language-model loss can be described using simple empirical power laws.

The most important scaling variables are:

- Model size N
- Dataset size D
- Training compute C
- Training steps S

The authors find strong dependence on these quantities and weak dependence on many architectural shape parameters when overall parameter count is controlled.

Model size and dataset size interact predictably through the proposed L(N,D) relationship.

Training curves can also be modeled using L(N,S).

The critical batch size follows a power law in the achieved loss.

Most importantly, compute-efficient training favors substantially larger models, moderate increases in dataset size, larger batch sizes, and relatively few serial optimization steps.

The authors therefore conclude that larger models are substantially more sample-efficient than smaller models.

However, the paper also emphasizes that the scaling laws are empirical rather than theoretically derived.

Their range of validity is uncertain, particularly outside the regimes studied in the experiments.

Future work must determine which scaling relationships are universal and which depend specifically on natural language and the experimental setup.