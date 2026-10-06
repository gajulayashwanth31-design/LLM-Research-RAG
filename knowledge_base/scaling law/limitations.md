---
paper: "Scaling Laws for Neural Language Models"
year: 2020
domain: "Large Language Models"
subdomain: "Scaling Laws"
difficulty: "Advanced"
document_type: "Limitations"
keywords:
  - Scaling Laws
  - Caveats
  - Extrapolation
  - Compute
  - Dataset
  - Optimization
generated_from: "Original Research Paper"
---

# Lack of Theoretical Foundation

## Main Limitation

The paper does not provide a solid theoretical explanation for the observed scaling laws.

## Consequence

It is difficult to determine precisely when the empirical relationships can be trusted outside the studied regime.

# Extrapolation Risk

## Scaling Law Validity

The observed power laws cannot be assumed to continue indefinitely.

The authors explicitly expect the scaling behavior to eventually flatten or change.

## Large-Scale Extrapolation

Predictions far beyond the experimental regime may therefore be unreliable.

# Model-Size Scaling

## Limitation

The theoretical origin of the model-size scaling relationship remains unclear.

The authors describe the scaling with model size and compute as particularly mysterious.

# Dataset Scaling

## Limitation

The behavior of the dataset-size scaling law at very large model sizes is not theoretically understood.

# Critical Batch Size

## Limitation

The authors are not especially confident in predictions of Bcrit at loss values far outside the range studied.

## Consequence

Changes in Bcrit could alter the predicted trade-off between data parallelism and serial training time.

# Small-Data Regime

## Limitation

The smallest datasets were not studied thoroughly.

The fitted L(N,D) relationship performs poorly for the smallest dataset sizes.

## Reason

For the smallest datasets, an epoch could correspond to only approximately 40 parameter-update steps.

This may represent a qualitatively different regime.

# Regularization

## Limitation

The authors did not systematically optimize regularization while varying model and dataset size.

## Consequence

Different regularization strategies could potentially change the quantitative or qualitative scaling behavior.

# Data Augmentation

## Limitation

Data augmentation was not systematically investigated.

## Consequence

Better augmentation methods could alter scaling relationships in some regimes.

# Compute Approximation

## Limitation

The paper approximates training compute as:

C ≈ 6NBS

This estimate does not include all context-dependent computation.

## Consequence

The compute scaling relationships may become inaccurate when context length becomes sufficiently large.

# Context Length

## Limitation

The context-dependent contribution becomes more significant when:

nctx ≳ 12 dmodel

## Consequence

The simplified compute estimate may become less reliable for very long contexts.

# Hyperparameter Tuning

## Limitation

The authors tuned learning rates and learning-rate schedules but may not have exhaustively optimized every hyperparameter.

Potentially important variables include:

- Initialization scale
- Momentum
- Other optimization parameters

# Learning Rate

## Limitation

The optimal learning rate can depend on the target loss.

## Convergence

Near convergence, a smaller learning rate may be required to avoid divergence.

## Short Training

For short compute-limited runs, a larger learning rate might be beneficial.

The authors did not fully investigate this possibility.

# Dataset Dependence

## Limitation

The fitted numerical constants are associated with the WebText2 dataset.

## Tokenization Dependence

The characteristic scales Nc and Dc depend on vocabulary size and tokenization.

They therefore do not have fundamental universal meanings.

# Architecture Dependence

## Limitation

The main experiments focus primarily on decoder-only Transformers.

Although LSTMs and Universal Transformers are also investigated, the results do not establish that every architecture follows exactly the same scaling laws.

# Natural Language Dependence

## Limitation

It is unknown which observed relationships depend specifically on the structure of natural-language data.

## Future Work

The authors propose testing similar relationships on images, audio, and video.

# Capability Interpretation

## Limitation

The primary metric is language-model loss.

A smooth reduction in loss does not necessarily guarantee smooth improvement in downstream capabilities.

## Qualitative Changes

The authors note that quantitative improvement in loss could potentially hide qualitative changes in capability.

# Diminishing Returns

## Limitation

Power-law scaling means that larger models require increasingly more resources for progressively smaller improvements.

## Implication

Scaling is not equivalent to unlimited efficient improvement.

# Data-Limited Regime

## Limitation

The paper predicts that compute-efficient training may eventually become data-limited.

The scaling laws themselves may break down before reaching the predicted intersection.

# Hardware Constraints

## Limitation

The theoretically compute-efficient strategy may not always be practically optimal because hardware availability imposes constraints.

## Example

Larger models can require substantial model parallelism.

# Serial Training

## Limitation

The framework favors large models and relatively few serial steps.

However, early training dynamics are not captured well by the simple power-law model.

# Empirical Nature

## Main Caveat

The paper's equations are empirical fits.

They should not be interpreted as fundamental laws of neural-network learning.

# Generalization

## Limitation

The paper observes strong transfer relationships across several text distributions.

However, this does not establish universal generalization behavior across all possible data distributions.

# Future Research

## Theoretical Understanding

A theoretical framework is needed to derive the observed scaling relationships.

## Other Modalities

Scaling laws should be tested on:

- Images
- Audio
- Video

## Capability Studies

Future work should investigate whether continued loss improvements consistently translate into useful downstream capability improvements.