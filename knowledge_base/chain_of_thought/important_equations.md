---
paper: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
year: 2022
domain: "Large Language Models"
subdomain: "Prompting and Reasoning"
difficulty: "Intermediate"
document_type: "Important Equations"
keywords:
  - Chain-of-Thought Prompting
  - Mathematical Reasoning
  - Arithmetic Reasoning
  - GSM8K
  - External Calculator
  - Accuracy
generated_from: "Original Research Paper"
---

# Important Equations

## No Central Model Equation

The paper does not introduce a new neural network architecture or a central mathematical training objective.

The main contribution is a prompting method.

Therefore, the important mathematical expressions in the paper primarily appear as intermediate reasoning steps in arithmetic problems and as quantitative evaluation results.

# Chain-of-Thought Arithmetic Representation

## General Structure

A chain-of-thought arithmetic solution can be represented conceptually as:

Input → Intermediate reasoning steps → Final answer

The intermediate reasoning may contain multiple mathematical operations.

# Tennis Ball Example

## Problem

Roger starts with 5 tennis balls.

He buys 2 cans.

Each can contains 3 tennis balls.

## Intermediate Calculation

Additional balls:

2 × 3 = 6

## Final Calculation

Total balls:

5 + 6 = 11

## Final Answer

11

# Apple Example

## Problem

A cafeteria has 23 apples.

20 apples are used.

6 additional apples are bought.

## Intermediate Calculation

Remaining apples:

23 - 20 = 3

Additional apples:

3 + 6 = 9

## Final Answer

9

# Last Letter Concatenation

## Problem

The task asks for the last letters of:

Lady Gaga

## Intermediate Steps

Last letter of Lady:

y

Last letter of Gaga:

a

## Concatenation

y + a = ya

## Final Answer

ya

# Coin Flip Reasoning

## Initial State

The coin starts:

Heads

## Operation

Maybelle flips the coin once.

The number of flips is:

1

## State Transition

An odd number of flips changes:

Heads → Tails

## Final Answer

No, the coin is not still heads up.

# Percentage Reasoning Example

## Problem

A player scores 4 points in the first 20 minutes.

In the second 20 minutes, the player scores 25% more.

## Intermediate Calculation

Second-period score:

4 × 1.25 = 5

## Total

4 + 5 = 9

## Final Answer

9

# Chain-of-Thought as a Sequence

## Conceptual Representation

A reasoning demonstration can be represented as:

(x, r, y)

where:

x = input

r = chain of thought

y = final output

## Prompt Structure

A few-shot chain-of-thought prompt therefore contains examples of:

(input, reasoning, output)

followed by a new input for which the model must generate:

reasoning + output

# Standard Prompting

## Representation

Standard prompting uses:

(input, output)

The model directly maps the input to the answer.

# Chain-of-Thought Prompting

## Representation

Chain-of-thought prompting uses:

(input, chain of thought, output)

The additional reasoning sequence is the central difference from standard prompting.

# Accuracy

## Definition

The paper reports performance primarily as accuracy or solve rate.

Conceptually:

Accuracy = Correct Predictions / Total Predictions

## Percentage Form

Accuracy can be expressed as:

Accuracy (%) = (Correct Predictions / Total Predictions) × 100

# Performance Improvement

## Absolute Improvement

When comparing standard prompting with chain-of-thought prompting:

Improvement = CoT Performance - Standard Performance

For example, on GSM8K with PaLM 540B:

Chain of Thought = 56.9%

Standard Prompting = 17.9%

Therefore:

56.9 - 17.9 = 39.0 percentage points

# External Calculator

## Arithmetic Evaluation

When a chain of thought contains an equation, the equation can be evaluated by an external calculator.

For example:

4 × 1.25 = 5

The calculator returns:

5

The result can then be propagated into subsequent reasoning steps.

# Equation-Only Prompting

## Concept

Equation-only prompting asks the model to produce an equation before the final answer.

The paper uses this as an ablation.

## Difference from Chain of Thought

Equation-only:

Input → Equation → Answer

Chain of thought:

Input → Natural-language reasoning → Equations and reasoning → Answer

# Variable Compute

## Conceptual Representation

The variable-compute ablation gives the model additional output tokens without providing meaningful reasoning content.

The paper tests whether additional computation alone explains the gains.

## Result

The method performs approximately like standard prompting.

This suggests that the semantic content of intermediate reasoning is important.

# Model Scaling

## Conceptual Relationship

The paper investigates the relationship:

Model Scale ↑ → Chain-of-Thought Capability ↑

The relationship is not linear or uniformly beneficial across all model sizes.

Strong gains appear primarily for sufficiently large models.

# Reasoning Length

## In-Domain

The number of reasoning steps is similar to the demonstrations.

## Out-of-Domain

The test problem requires more reasoning steps than the demonstrations.

The paper finds that chain-of-thought prompting can improve performance on these longer reasoning sequences.

# Key Quantitative Example

## PaLM 540B on GSM8K

Standard prompting:

17.9%

Chain-of-thought prompting:

56.9%

Improvement:

39.0 percentage points

## Interpretation

The result demonstrates the large effect of chain-of-thought prompting on a challenging multi-step reasoning benchmark at sufficiently large model scale.

# Important Quantitative Finding

## PaLM 540B

For arithmetic reasoning, chain-of-thought prompting substantially improves performance over standard prompting on several benchmarks.

For GSM8K, the paper reports:

17.9% → 56.9%

For SVAMP:

69.4% → 79.0%

For ASDiv:

72.1% → 73.9%

For AQuA:

25.2% → 35.8%

For MAWPS:

79.2% → 93.3%

These results illustrate that the magnitude of improvement depends on the task.