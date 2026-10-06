---
paper: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
year: 2022
domain: "Large Language Models"
subdomain: "Prompting and Reasoning"
difficulty: "Intermediate"
document_type: "Paper Statistics"
keywords:
  - Chain-of-Thought Prompting
  - Large Language Models
  - Model Scaling
  - Benchmarks
  - Experimental Results
  - GSM8K
  - PaLM
  - LaMDA
generated_from: "Original Research Paper"
---

# Paper Statistics

## Paper Information

### Title

Chain-of-Thought Prompting Elicits Reasoning in Large Language Models

### Authors

Jason Wei

Xuezhi Wang

Dale Schuurmans

Maarten Bosma

Brian Ichter

Fei Xia

Ed H. Chi

Quoc V. Le

Denny Zhou

### Organization

Google Research, Brain Team

### Conference

36th Conference on Neural Information Processing Systems

NeurIPS 2022

### arXiv Identifier

arXiv:2201.11903

### Attached Version

The attached paper is version 6.

The attached PDF is dated:

10 January 2023.

# Core Method

## Method Name

Chain-of-Thought Prompting

## Prompt Type

Few-shot prompting

## Training Required

No model fine-tuning is required for the main method.

## Core Input Structure

The demonstrations contain:

Input

+

Chain of thought

+

Output

# Model Families

## GPT-3

The paper evaluates GPT-3 at multiple scales.

The largest evaluated GPT-3 model has approximately:

175B parameters.

## LaMDA

The paper evaluates LaMDA at:

420M

2B

8B

68B

137B

parameters.

## PaLM

The paper evaluates PaLM at:

8B

62B

540B

parameters.

## UL2

The paper evaluates:

UL2 20B

## Codex

The paper evaluates:

Codex

using:

code-davinci-002

# Arithmetic Benchmarks

## Number of Benchmarks

Five arithmetic reasoning benchmarks are evaluated.

## Benchmarks

1. GSM8K
2. SVAMP
3. ASDiv
4. AQuA
5. MAWPS

# Commonsense Benchmarks

## Number of Benchmarks

Five commonsense reasoning datasets are evaluated.

## Benchmarks

1. CommonsenseQA
2. StrategyQA
3. Date Understanding
4. Sports Understanding
5. SayCan

# Symbolic Tasks

## Number of Main Symbolic Tasks

Two symbolic reasoning tasks are evaluated.

## Tasks

1. Last Letter Concatenation
2. Coin Flip

# Arithmetic Prompting

## Standard Prompting

The model receives input-output demonstrations.

## Chain-of-Thought Prompting

The model receives input-reasoning-output demonstrations.

## Main Arithmetic Demonstrations

The authors manually create:

8

few-shot chain-of-thought exemplars for most arithmetic benchmarks.

## AQuA

AQuA uses:

4

few-shot exemplars.

# PaLM 540B Results

## GSM8K

Standard prompting:

17.9%

Chain-of-thought prompting:

56.9%

Improvement:

39.0 percentage points

## SVAMP

Standard prompting:

69.4%

Chain-of-thought prompting:

79.0%

Improvement:

9.6 percentage points

## ASDiv

Standard prompting:

72.1%

Chain-of-thought prompting:

73.9%

Improvement:

1.8 percentage points

## AQuA

Standard prompting:

25.2%

Chain-of-thought prompting:

35.8%

Improvement:

10.6 percentage points

## MAWPS

Standard prompting:

79.2%

Chain-of-thought prompting:

93.3%

Improvement:

14.1 percentage points

# Codex 175B-Class Results

## GSM8K

Standard prompting:

19.7%

Chain-of-thought prompting:

63.1%

Improvement:

43.4 percentage points

## SVAMP

Standard prompting:

69.9%

Chain-of-thought prompting:

76.4%

Improvement:

6.5 percentage points

## ASDiv

Standard prompting:

74.0%

Chain-of-thought prompting:

80.4%

Improvement:

6.4 percentage points

## AQuA

Standard prompting:

29.5%

Chain-of-thought prompting:

45.3%

Improvement:

15.8 percentage points

## MAWPS

Standard prompting:

78.7%

Chain-of-thought prompting:

92.6%

Improvement:

13.9 percentage points

# LaMDA 137B Results

## GSM8K

Standard prompting:

6.5%

Chain-of-thought prompting:

14.3%

Improvement:

7.8 percentage points

## SVAMP

Standard prompting:

29.5%

Chain-of-thought prompting:

37.5%

Improvement:

8.0 percentage points

## ASDiv

Standard prompting:

40.1%

Chain-of-thought prompting:

46.6%

Improvement:

6.5 percentage points

## AQuA

Standard prompting:

25.5%

Chain-of-thought prompting:

20.6%

Change:

-4.9 percentage points

## MAWPS

Standard prompting:

43.2%

Chain-of-thought prompting:

57.9%

Improvement:

14.7 percentage points

# Commonsense Results

## StrategyQA

PaLM 540B with chain-of-thought prompting:

75.6%

Prior state of the art:

69.4%

## Sports Understanding

PaLM 540B with chain-of-thought prompting:

95.4%

Unaided sports enthusiast:

84%

# Symbolic Results

## Last Letter Concatenation

PaLM 540B with chain-of-thought prompting achieves very high in-domain solve rates.

## Coin Flip

PaLM 540B with chain-of-thought prompting achieves approximately:

100%

on the in-domain evaluation.

## Out-of-Domain

Chain-of-thought prompting also improves performance on symbolic tasks with longer reasoning sequences than those shown in the demonstrations.

# Robustness Results

## Different Annotator

Different annotators produce different results.

However, the different chain-of-thought prompts generally outperform standard prompting.

## Exemplar Variation

Different exemplar sets also produce variation.

The method remains generally beneficial.

## Prompt Order

The paper evaluates different orders of few-shot exemplars.

The effectiveness of chain-of-thought prompting remains robust overall.

# Ablation Variants

## Standard Prompting

Direct input-output prompting.

## Equation Only

The model produces an equation before the final answer.

## Variable Compute Only

The model produces additional tokens without meaningful reasoning content.

## Reasoning After Answer

The reasoning is provided after the answer rather than before it.

## Main Finding

None of the ablations reproduces the complete benefits of standard chain-of-thought prompting across the difficult reasoning tasks studied.

# Qualitative Error Analysis

## Correct-Answer Analysis

The authors inspect:

50

random examples where LaMDA 137B gives the correct final answer.

Nearly all generated reasoning chains are also logically and mathematically correct.

Two examples reach the correct answer coincidentally despite incorrect reasoning.

## Incorrect-Answer Analysis

The authors inspect:

50

random examples where the model produces an incorrect answer.

## Almost-Correct Chains

Approximately:

46%

of the incorrect-answer chains are almost correct apart from minor errors.

## Major Errors

Approximately:

54%

contain major errors involving semantic understanding or coherence.

# External Calculator

## Purpose

To correct arithmetic computation errors in generated reasoning.

## Method

Generated equations are evaluated using a Python-based external calculator.

## Result

The external calculator substantially improves performance on many arithmetic benchmarks.

# Main Experimental Conclusions

## Model Scale

Strong chain-of-thought gains appear primarily at large model scales.

## Task Complexity

The benefits are larger for tasks requiring multiple reasoning steps.

## Natural Language Reasoning

Natural-language intermediate reasoning provides benefits beyond simply generating additional tokens.

## Robustness

The method remains effective across different annotators and exemplar sets, although performance varies.

## Generalization

Chain-of-thought prompting improves symbolic reasoning on longer out-of-domain sequences.

# Main Quantitative Takeaway

The strongest single example in the paper is the GSM8K result for PaLM 540B:

Standard prompting:

17.9%

Chain-of-thought prompting:

56.9%

This corresponds to:

+39.0 percentage points

and demonstrates the substantial improvement obtained from chain-of-thought prompting on a challenging multi-step reasoning benchmark.