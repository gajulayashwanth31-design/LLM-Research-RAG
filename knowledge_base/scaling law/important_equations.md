---
paper: "Scaling Laws for Neural Language Models"
year: 2020
domain: "Large Language Models"
subdomain: "Scaling Laws"
difficulty: "Advanced"
document_type: "Important Equations"
keywords:
  - Power Laws
  - Model Size Scaling
  - Dataset Scaling
  - Compute Scaling
  - Overfitting
  - Critical Batch Size
  - Optimal Compute
generated_from: "Original Research Paper"
---

# Model Size Scaling

## Equation

L(N) = (Nc / N)^αN

## Parameters

- L(N) = language-model loss
- N = number of non-embedding parameters
- Nc = characteristic parameter scale
- αN = model-size scaling exponent

## Empirical Values

αN ≈ 0.076

Nc ≈ 8.8 × 10^13 non-embedding parameters.

## Interpretation

Increasing model size reduces loss according to a power law.

# Dataset Size Scaling

## Equation

L(D) = (Dc / D)^αD

## Parameters

- D = dataset size in tokens
- Dc = characteristic dataset scale
- αD = dataset scaling exponent

## Empirical Values

αD ≈ 0.095

Dc ≈ 5.4 × 10^13 tokens.

## Interpretation

Increasing dataset size improves performance with diminishing returns.

# Compute Scaling

## Equation

L(Cmin) = (Cmin,c / Cmin)^αCmin

## Parameters

- Cmin = minimum compute required to reach the target loss
- Cmin,c = characteristic compute scale
- αCmin = compute scaling exponent

## Empirical Values

αCmin ≈ 0.050

Cmin,c ≈ 3.1 × 10^8 PF-days.

# Naive Compute Scaling

## Equation

L(C) = (Cc / C)^αC

## Empirical Values

αC ≈ 0.057

Cc ≈ 1.6 × 10^7 PF-days.

## Important Note

The paper distinguishes this empirically observed fixed-batch compute scaling from Cmin-based scaling.

The authors recommend Cmin for compute-efficiency predictions because it accounts for batch-size efficiency.

# Critical Batch Size

## Equation

Bcrit(L) = B* / L^(1/αB)

## Parameters

- Bcrit(L) = critical batch size at loss L
- B* = characteristic batch-size scale
- αB = batch-size scaling exponent

## Empirical Values

B* ≈ 2 × 10^8 tokens

αB ≈ 0.21

## Interpretation

The useful batch size increases as training loss decreases.

# Parameter Scaling With Compute

## Equation

Nopt ∝ Cmin^0.73

## Interpretation

The compute-efficient model size grows rapidly with available compute.

A tenfold increase in compute corresponds approximately to a fivefold increase in optimal model size.

# Batch Size Scaling With Compute

## Equation

B ∝ Cmin^0.24

## Interpretation

Optimal batch size grows with compute, enabling greater parallelism.

# Training Step Scaling

## Equation

Smin ∝ Cmin^0.03

## Interpretation

The number of serial optimization steps grows extremely slowly with available compute.

This means that most additional compute should not be spent on dramatically increasing serial training time.

# Dataset Scaling With Compute

## Equation

Dopt ∝ Cmin^0.27

## Interpretation

The amount of data required by compute-efficient training grows much more slowly than model size.

# Model-Dataset Scaling

## Relationship

D ∝ N^(αN/αD)

## Approximation

D ∝ N^0.74

## Interpretation

Dataset size should increase sublinearly with model size to maintain similar overfitting behavior.

# Joint Model-Dataset Loss

## Equation

L(N,D) =
[(Nc/N)^(αN/αD) + Dc/D]^αD

## Purpose

This equation models the simultaneous dependence of loss on model size and dataset size.

## Infinite Dataset

As D approaches infinity:

L(N,D) → L(N)

## Infinite Model

As N becomes sufficiently large:

L(N,D) → L(D)

# Overfitting

## Relative Overfitting

The paper defines:

δL(N,D) = L(N,D) / L(N,∞) - 1

## Interpretation

δL measures the relative increase in loss caused by having finite training data.

# Approximate Data Requirement

## Equation

D ≳ (5 × 10^3) N^0.74

## Purpose

This provides an approximate relationship for avoiding significant overfitting.

## Interpretation

Dataset size needs to increase sublinearly with model size.

# Training-Time Scaling

## Equation

L(N,S) =
(Nc/N)^αN
+
(Sc/Smin(S))^αS

## Parameters

- S = number of observed training steps
- Smin(S) = batch-size-adjusted minimum steps
- Sc = characteristic step scale
- αS = training-step scaling exponent

## Empirical Values

Sc ≈ 2.1 × 10^3 steps

αS ≈ 0.76

# Batch-Size Trade-Off

## Equation

(S/Smin - 1)(E/Emin - 1) = 1

## Variables

- S = number of training steps
- Smin = minimum number of steps
- E = number of training examples processed
- Emin = minimum number of examples required

## Interpretation

The equation captures the trade-off between processing more examples and using more optimization steps.

# Critical Batch Size Definition

## Equation

Bcrit(L) = Emin / Smin

## Interpretation

The critical batch size is the ratio between the minimum amount of data that must be processed and the minimum number of optimization steps required to reach a fixed loss.

# Minimum Steps Adjustment

## Equation

Smin(S) =
S / [1 + Bcrit(L)/B]

## Purpose

This converts the observed number of steps at a given batch size into an estimate of the minimum possible steps at very large batch size.

# Minimum Compute Adjustment

## Equation

Cmin(C) =
C / [1 + B/Bcrit(L)]

## Purpose

This estimates the minimum compute required to reach a given loss when using a sufficiently small batch size.

# Training Compute

## Equation

C ≈ 6NBS

## Variables

- N = non-embedding parameters
- B = batch size
- S = number of optimization steps

## Interpretation

Training compute grows linearly with model size, batch size, and training steps.

# Transformer Parameter Count

## Equation

N ≈ 2 dmodel nlayer (2dattn + dff)

For the standard configuration:

dattn = dff/4 = dmodel

Therefore:

N ≈ 12 nlayer dmodel^2

# Forward Compute

## Equation

Cforward ≈ 2N + 2nlayer nctx dmodel

## Interpretation

Forward computation consists primarily of parameter-dependent operations plus a context-dependent component.

# Compute-Efficient Loss

## Equation

αCmin =
1 / (1/αS + 1/αB + 1/αN)

## Approximation

αCmin ≈ 0.054 from the analytical prediction.

The empirical fit is approximately 0.050.

# Optimal Model Size From Loss Scaling

## Equation

N(Cmin) ∝ Cmin^(αCmin/αN)

## Approximation

N(Cmin) ∝ Cmin^0.71

The empirical relationship is approximately:

N(Cmin) ∝ Cmin^0.73

# Optimal Number of Steps

## Relationship

Smin ∝ Cmin^(αCmin/αS)

## Approximation

Smin ∝ Cmin^0.03

## Interpretation

Serial training depth changes very slowly as compute increases.

# One-Epoch Data Requirement

## Equation

D(Cmin) ≈ 2Cmin / [6N(Cmin)]

## Approximation

D(Cmin) ≈
4 × 10^10 × (Cmin / PF-day)^0.26 tokens

## Interpretation

If training never reuses data, productive dataset size grows slowly with compute.

# Data-Limited Compute Scaling

## Relationship

When training becomes data-limited:

L(D(Cmin)) ∝ Cmin^-0.03

This is slower than the compute-efficient scaling:

L(Cmin) ∝ Cmin^-0.050

## Implication

Eventually, data availability can become the limiting factor.