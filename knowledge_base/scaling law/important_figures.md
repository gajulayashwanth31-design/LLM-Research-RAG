---
paper: "Scaling Laws for Neural Language Models"
year: 2020
domain: "Large Language Models"
subdomain: "Scaling Laws"
difficulty: "Advanced"
document_type: "Important Figures"
keywords:
  - Scaling Laws
  - Power Laws
  - Compute Scaling
  - Model Scaling
  - Overfitting
  - Batch Size
generated_from: "Original Research Paper"
---

# Figure 1 — Basic Scaling Laws

## Purpose

Figure 1 shows language-model test loss as a function of:

- Compute
- Dataset size
- Model size

## Key Observation

Performance improves smoothly as each scale variable increases when the other variables are not bottlenecks.

## Main Message

Model size, dataset size, and compute exhibit approximate power-law relationships with language-model loss.

# Figure 2 — Model Size and Sample Efficiency

## Purpose

Figure 2 shows training curves for models ranging from approximately 10^3 to 10^9 non-embedding parameters.

## Left Plot

Larger models reach a given loss using fewer processed tokens.

## Right Plot

The optimal model size increases smoothly with the compute budget.

## Key Observation

Larger models require fewer samples to achieve the same performance.

# Figure 3 — Allocation of Increasing Compute

## Purpose

Figure 3 illustrates how a large increase in compute should be allocated.

## Key Observation

As compute increases:

- Model size increases dramatically.
- Dataset size increases relatively slowly.
- Batch size increases substantially.
- Serial training steps increase only slightly.

## Main Message

Compute-efficient scaling favors larger models rather than simply training smaller models for much longer.

# Figure 4 — Joint Model/Dataset and Model/Training-Step Scaling

## Left

The early-stopped test loss varies predictably with model size and dataset size.

## Right

After an initial transient, learning curves across model sizes can be described by a common power-law relationship involving training steps.

## Importance

The figure motivates the joint equations L(N,D) and L(N,S).

# Figure 5 — Model Shape Independence

## Purpose

Figure 5 varies architectural shape while holding the total number of non-embedding parameters approximately fixed.

The experiments vary:

- Feed-forward ratio
- Model aspect ratio
- Attention-head dimension

## Key Observation

Loss changes only slightly over a wide range of model shapes.

## Main Message

Overall model scale matters substantially more than precise depth/width configuration within reasonable limits.

# Figure 6 — Embedding Parameters and Model Depth

## Left

When embedding parameters are included in total parameter count, performance appears to depend strongly on model depth.

## Right

When embedding parameters are excluded, models with different depths approximately converge onto the same scaling relationship.

## Main Message

Non-embedding parameter count provides a cleaner measure of model size.

# Figure 7 — Transformer Versus LSTM

## Purpose

Figure 7 compares Transformer and LSTM language models.

## Left Plot

Transformer models increasingly outperform LSTMs as model size increases.

## Right Plot

The difference is particularly clear for tokens appearing later in the context.

## Key Observation

Transformers make better use of long contexts.

# Figure 8 — Generalization Across Data Distributions

## Purpose

Figure 8 evaluates models trained on WebText2 against multiple other data distributions.

## Left Plot

Loss on different distributions improves smoothly with model size.

## Right Plot

Generalization performance is strongly correlated with the model's training-distribution performance.

## Key Observation

There is a relatively small and slowly growing loss offset between training and other distributions.

# Figure 9 — Overfitting

## Purpose

Figure 9 studies loss as a function of model size and dataset size.

## Left Plot

When dataset size is sufficiently large, performance continues improving as model size increases.

With smaller datasets, increasing model size eventually causes overfitting.

## Right Plot

The degree of overfitting depends predictably on a combination of model size and dataset size.

# Figure 10 — Critical Batch Size

## Purpose

Figure 10 measures critical batch size as a function of training loss.

## Key Observation

The critical batch size follows a power-law relationship with loss.

## Important Finding

Critical batch size depends primarily on the achieved loss rather than directly on model size.

# Figure 11 — Performance Versus Compute and Steps

## Left

Test loss is shown as a function of compute for different model sizes.

## Right

Test loss is shown as a function of training steps.

## Key Observation

For a fixed compute budget, there is an approximately optimal model size.

# Figure 12 — Robustness of Optimal Model Size

## Purpose

Figure 12 examines the performance penalty from using a model that is not exactly optimal.

## Key Observation

Models between approximately 0.6× and 2.2× the optimal model size require only around 20% more compute.

## Practical Meaning

The compute-efficient optimum is not extremely narrow.

# Figure 13 — Compute-Efficient Loss Scaling

## Purpose

Figure 13 compares empirical compute scaling with the scaling obtained after adjusting for batch-size efficiency.

## Key Observation

The adjusted Cmin relationship provides a cleaner power law.

## Main Result

The authors expect Cmin-based scaling to provide the more reliable extrapolation to larger compute.

# Figure 14 — Optimal Model Size and Training Steps

## Left Plot

Optimal model size increases rapidly with compute.

The empirical relationship is approximately:

N ∝ Cmin^0.73

## Right Plot

The batch-adjusted number of training steps grows very slowly.

The empirical relationship is approximately:

Smin ∝ Cmin^0.03

## Main Message

Additional compute should primarily increase model size rather than serial training time.

# Figure 15 — Data Requirements

## Purpose

Figure 15 examines how much data is required as compute increases.

## Key Observation

Data requirements grow substantially more slowly than optimal model size.

## Implication

Compute-efficient training is dominated by model scaling rather than proportional dataset scaling.

# Figure 16 — Early Stopping

## Left Plot

The early stopping step is related to the degree of overfitting.

## Right Plot

Train and test loss are shown for models trained on datasets of different sizes.

## Key Observation

Test loss initially follows the behavior of an unrestricted-data run and diverges once the model begins to overfit.

# Figure 17 — Universal Transformers

## Purpose

Figure 17 compares standard Transformers with recurrent Transformers.

## Key Observation

Parameter reuse can improve performance as a function of model size.

However, recurrent Transformers require additional compute per parameter.

# Figure 18 — Batch Size Trade-Off

## Purpose

Figure 18 demonstrates the relationship between training steps and the number of examples processed at a fixed target loss.

## Key Observation

The trade-off follows the relationship:

(S/Smin - 1)(E/Emin - 1) = 1

This relationship motivates the definition of the critical batch size.

# Figure 19 — Sample Efficiency

## Purpose

Figure 19 demonstrates that larger models reach a particular performance level with fewer data examples.

## Main Message

Model scaling improves sample efficiency.

# Figure 20 — Supplemental Scaling Results

## Purpose

The supplemental figures examine additional scaling relationships and verify the robustness of the main empirical trends.

## Main Message

The paper's scaling behavior remains broadly consistent across the additional experiments, while the authors identify several regimes where extrapolation should be treated cautiously.