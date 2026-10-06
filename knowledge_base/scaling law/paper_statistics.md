---
paper: "Scaling Laws for Neural Language Models"
year: 2020
domain: "Large Language Models"
subdomain: "Scaling Laws"
difficulty: "Advanced"
document_type: "Paper Statistics"
keywords:
  - Scaling Laws
  - Model Size
  - Dataset Size
  - Compute
  - Power Law
  - Transformer
generated_from: "Original Research Paper"
---

# Paper Information

## Title

Scaling Laws for Neural Language Models

## Authors

Jared Kaplan

Sam McCandlish

Tom Henighan

Tom B. Brown

Benjamin Chess

Rewon Child

Scott Gray

Alec Radford

Jeffrey Wu

Dario Amodei

## Publication

arXiv:2001.08361v1

## Date

23 January 2020

# Primary Dataset

## Dataset

WebText2

## Documents

20.3 million documents

## Raw Text

96 GB

## Words

1.62 × 10^10 words

## Tokens

2.29 × 10^10 tokens

## Reserved Test Tokens

6.6 × 10^8 tokens

# Tokenization

## Method

Byte-pair encoding

## Vocabulary

50,257 tokens

# Main Context Length

## Context

1024 tokens

# Standard Training Setup

## Optimizer

Adam

## Large Models

Models above approximately 1 billion parameters use Adafactor because of memory constraints.

## Training Steps

2.5 × 10^5 steps

## Batch

512 sequences of 1024 tokens

## Warmup

3000 steps

## Learning Rate Schedule

Linear warmup followed by cosine decay to zero

# Model Scaling Experiments

## Model Size Range

768 to approximately 1.5 billion non-embedding parameters.

## Dataset Size Range

22 million to 23 billion tokens.

## Architectural Variables

The experiments vary:

- Depth
- Width
- Attention heads
- Feed-forward dimension
- Context length
- Batch size

# Main Model-Size Scaling

## Exponent

αN ≈ 0.076

## Characteristic Scale

Nc ≈ 8.8 × 10^13 non-embedding parameters

# Dataset Scaling

## Exponent

αD ≈ 0.095

## Characteristic Scale

Dc ≈ 5.4 × 10^13 tokens

# Naive Compute Scaling

## Exponent

αC ≈ 0.057

## Characteristic Scale

Cc ≈ 1.6 × 10^7 PF-days

# Compute-Efficient Scaling

## Exponent

αCmin ≈ 0.050

## Characteristic Scale

Cmin,c ≈ 3.1 × 10^8 PF-days

# Batch Scaling

## Exponent

αB ≈ 0.21

## Characteristic Scale

B* ≈ 2.1 × 10^8 tokens

# Training-Step Scaling

## Exponent

αS ≈ 0.76

## Characteristic Scale

Sc ≈ 2.1 × 10^3 steps

# Model-Size/Dataset Relationship

## Scaling

D ∝ N^0.74

## Interpretation

Dataset size should grow sublinearly with model size to maintain similar overfitting behavior.

# Compute-Efficient Model Scaling

## Optimal Model Size

Nopt ∝ Cmin^0.73

## Approximate Scale

Ne ≈ 1.3 × 10^9 parameters

# Compute-Efficient Batch Scaling

## Relationship

B ≈ Bcrit

## Compute Scaling

B ∝ Cmin^0.24

## Approximate Scale

Be ≈ 2.0 × 10^6 tokens

# Compute-Efficient Training Steps

## Relationship

Smin ∝ Cmin^0.03

## Approximate Scale

Se ≈ 5.4 × 10^3 steps

# Compute-Efficient Dataset Scaling

## Relationship

Dopt ∝ Cmin^0.27

## Approximate Scale

De ≈ 2 × 10^10 tokens

# Critical Batch Size

## Formula

Bcrit(L) ≈ B* / L^(1/αB)

## Parameters

B* ≈ 2 × 10^8 tokens

αB ≈ 0.21

# Transformer Parameter Count

## Formula

N ≈ 2dmodel nlayer (2dattn + dff)

## Standard Configuration

dattn = dff/4 = dmodel

## Simplified Formula

N ≈ 12 nlayer dmodel^2

# Training Compute

## Formula

C ≈ 6NBS

# Major Empirical Findings

## Model Size

Performance improves as model size increases.

## Dataset Size

Performance improves as dataset size increases.

## Compute

Performance improves as training compute increases.

## Model Shape

Performance depends relatively weakly on architectural shape when total non-embedding parameter count is fixed.

## Sample Efficiency

Larger models require fewer samples to reach the same performance.

## Overfitting

Model and dataset size interact predictably.

## Compute Allocation

Most additional compute should be allocated to increasing model size.

## Serial Steps

The optimal number of serial training steps increases very slowly.

# Main Experimental Comparisons

## Transformer

Primary architecture used for scaling experiments.

## LSTM

Used to compare long-context scaling behavior.

## Universal Transformer

Used to investigate parameter reuse.

# Major Figures

## Figure 1

Basic scaling relationships.

## Figure 2

Sample efficiency and optimal model size.

## Figure 3

Allocation of increasing compute.

## Figure 4

Joint model/data and model/steps scaling.

## Figure 5

Model-shape independence.

## Figure 6

Embedding parameters and model depth.

## Figure 7

Transformer versus LSTM.

## Figure 8

Generalization across data distributions.

## Figure 9

Overfitting.

## Figure 10

Critical batch size.

## Figure 11

Performance versus compute and training steps.

## Figure 12

Robustness of optimal model size.

## Figure 13

Compute-efficient scaling.

## Figure 14

Optimal model size and training steps.

## Figure 16

Early stopping.

## Figure 18

Batch-size trade-off.

## Figure 19

Sample efficiency.

# Key Numerical Conclusions

## Loss Scaling

Loss follows approximate power laws in model size, dataset size, and compute.

## Model Growth

Optimal model size grows approximately as:

Cmin^0.73

## Data Growth

Optimal dataset size grows approximately as:

Cmin^0.27

## Batch Growth

Optimal batch size grows approximately as:

Cmin^0.24

## Serial Step Growth

Optimal serial steps grow approximately as:

Cmin^0.03

# Main Conclusion

The paper concludes that increasingly compute-efficient language-model training should primarily increase model size while increasing data and batch size more moderately and keeping the number of serial optimization steps relatively stable.