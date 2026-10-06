---
paper: "Language Models are Few-Shot Learners"
year: 2020
domain: "Large Language Models"
subdomain: "Autoregressive Language Models"
difficulty: "Intermediate"
document_type: "Important Equations"
keywords:
  - Language Modeling
  - Cross Entropy
  - Perplexity
  - Scaling Laws
  - Probability
generated_from: "Original Research Paper"
---

# Autoregressive Language Modeling

## Next-Token Prediction

GPT-3 models the probability of a token sequence autoregressively.

For a sequence of tokens x_1, x_2, ..., x_n, the sequence probability can be decomposed as:

P(x_1, x_2, ..., x_n) = ∏ P(x_i | x_1, ..., x_{i-1})

The model therefore predicts each token conditioned on the tokens that precede it.

# Language Modeling Loss

## Cross-Entropy

The language-modeling objective minimizes the negative log-likelihood of the observed token sequence.

A general form is:

L = -Σ log P(x_i | x_1, ..., x_{i-1})

The model is trained to assign high probability to the observed continuation.

# Perplexity

## Definition

Perplexity is derived from the average negative log-likelihood of the sequence.

For N tokens:

PPL = exp(-1/N Σ log P(x_i | x_<i))

Lower perplexity indicates better language-model prediction.

# Conditional Completion Probability

## Definition

During in-context evaluation, the model assigns probabilities to possible completions conditioned on the context.

P(completion | context)

For multiple-choice tasks, the likelihood of each candidate completion can be compared.

# Per-Token Likelihood

## Definition

For most multiple-choice evaluations, the paper compares per-token likelihood rather than raw completion likelihood.

This normalizes the likelihood with respect to completion length.

# Scaling Relationship

## Power-Law Behavior

The paper observes that validation loss follows an approximate power-law relationship with training compute.

The paper illustrates this relationship through the empirical scaling curve:

L(C) ∝ C^α

where:

- L represents validation loss
- C represents training compute
- α represents the observed scaling exponent

The paper primarily presents this relationship empirically rather than proposing it as a task-specific training objective.

# Multiple-Choice Evaluation

## Completion Comparison

For a multiple-choice task, the model is given a context and candidate completions.

The likelihood of each completion is evaluated.

The candidate with the highest normalized likelihood can be selected as the prediction.

# Beam Search

## Free-Form Generation

For free-form completion tasks, the paper uses beam search.

The reported setup uses:

- Beam width = 4
- Length penalty α = 0.6

The exact evaluation metric depends on the dataset.

# Evaluation Metrics

## F1

Used for tasks where overlap between predicted and reference answers is important.

## BLEU

Used for translation evaluation.

## Exact Match

Used for tasks where the predicted answer must exactly match the expected answer.