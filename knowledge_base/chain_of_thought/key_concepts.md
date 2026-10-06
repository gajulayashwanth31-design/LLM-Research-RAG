---
paper: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
year: 2022
domain: "Large Language Models"
subdomain: "Prompting and Reasoning"
difficulty: "Intermediate"
document_type: "Key Concepts"
keywords:
  - Chain-of-Thought Prompting
  - Few-Shot Prompting
  - In-Context Learning
  - Reasoning
  - Emergent Abilities
  - Model Scaling
  - Arithmetic Reasoning
  - Commonsense Reasoning
  - Symbolic Reasoning
generated_from: "Original Research Paper"
---

# Chain-of-Thought Prompting

## What is it?

Chain-of-thought prompting is a prompting technique where few-shot examples contain intermediate reasoning steps in addition to the input and final output.

The model is therefore shown examples of:

input → reasoning → output

rather than only:

input → output

## Why was it introduced?

Traditional few-shot prompting can struggle with tasks that require multiple reasoning steps.

The authors investigate whether explicitly showing intermediate reasoning in the demonstrations allows sufficiently large language models to solve such tasks more effectively.

## Main Idea

The model is given several examples containing:

- Input
- Chain of thought
- Final answer

The model then generates a chain of thought for a new input before producing its answer.

# Standard Prompting

## Definition

Standard few-shot prompting provides input-output examples.

The model receives demonstrations showing what type of output should be produced.

## Example Structure

The basic structure is:

Question

Answer

## Limitation

The model must infer the intermediate reasoning process without being shown explicit reasoning demonstrations.

This can be difficult for multi-step problems.

# Few-Shot Prompting

## Definition

Few-shot prompting provides a small number of examples inside the model's input context.

The examples demonstrate the desired task behavior.

## Advantage

The same language model can potentially perform many tasks without being separately fine-tuned.

## Limitation

Traditional few-shot prompting may not provide enough guidance for difficult reasoning tasks.

# Chain-of-Thought Demonstration

## Structure

A chain-of-thought demonstration contains:

Input

Intermediate reasoning steps

Final output

## Purpose

The demonstration provides the model with an example of how a problem can be decomposed into intermediate steps.

# Intermediate Reasoning Steps

## Definition

Intermediate reasoning steps are natural-language statements produced between the input and final answer.

## Role

They provide a sequence through which the model can progressively transform the problem into the final answer.

## Example

For a mathematical problem:

Initial quantity = 5

Additional quantity = 2 × 3 = 6

Total = 5 + 6 = 11

Final answer = 11

# Emergent Ability

## Definition

The paper describes chain-of-thought prompting as an emergent ability of model scale.

The method does not consistently improve performance for small models.

Substantial improvements appear when models become sufficiently large.

## Model Scale

The experiments suggest that strong chain-of-thought gains generally emerge around the scale of approximately 100B parameters.

# Arithmetic Reasoning

## Definition

Arithmetic reasoning involves solving mathematical word problems through multiple operations.

## Benchmarks

The paper evaluates:

- GSM8K
- SVAMP
- ASDiv
- AQuA
- MAWPS

## Importance

Arithmetic problems provide a controlled setting for testing multi-step reasoning.

# Commonsense Reasoning

## Definition

Commonsense reasoning involves using knowledge about physical and human interactions to reach conclusions.

## Benchmarks

The paper evaluates:

- CommonsenseQA
- StrategyQA
- Date Understanding
- Sports Understanding
- SayCan

# Symbolic Reasoning

## Definition

Symbolic reasoning requires manipulating symbols or states according to explicit rules.

## Tasks

The paper evaluates:

- Last letter concatenation
- Coin flip state tracking

## Length Generalization

The paper evaluates both in-domain and out-of-domain reasoning lengths.

The OOD setting contains more reasoning steps than the demonstrations.

# In-Context Learning

## Definition

The language model learns the task from examples included directly in the prompt.

No parameter updates are required.

## Role in the Paper

Chain-of-thought prompting is implemented as an in-context learning technique.

The model receives reasoning demonstrations without fine-tuning.

# Model Scaling

## Definition

Model scaling refers to increasing the size of the language model.

The paper evaluates multiple model families and sizes.

## Main Observation

Chain-of-thought prompting becomes substantially more effective as model scale increases.

# PaLM 540B

## Role

PaLM 540B is one of the largest models evaluated in the paper.

It demonstrates some of the strongest chain-of-thought improvements.

## GSM8K

PaLM 540B with chain-of-thought prompting achieves state-of-the-art performance on GSM8K according to the paper.

# LaMDA

## Role

LaMDA is evaluated at several model sizes.

The experiments use LaMDA to study scaling, ablations, robustness, and qualitative reasoning behavior.

## LaMDA 137B

LaMDA 137B is particularly important in the detailed ablation and robustness experiments.

# GPT-3

## Role

GPT-3 is evaluated as one of the large language model families.

The experiments include different GPT-3 sizes.

## Large-Scale Effect

GPT-3 175B shows substantial gains from chain-of-thought prompting on difficult arithmetic reasoning tasks.

# Codex

## Role

Codex is evaluated in the arithmetic experiments.

The paper uses code-davinci-002.

## Result

Codex also benefits substantially from chain-of-thought prompting at large scale.

# UL2

## Role

UL2 20B is included in the arithmetic reasoning experiments.

It shows smaller improvements than the largest models.

# Arithmetic Chain of Thought

## Process

A mathematical word problem is decomposed into natural-language reasoning steps.

The intermediate steps may contain equations.

The final answer is produced after the reasoning sequence.

# Equation-Only Prompting

## Definition

The model is prompted to produce a mathematical equation as an intermediate step instead of a natural-language chain of thought.

## Finding

Equation-only prompting can help on some tasks.

However, it does not provide the same benefits as full natural-language chain-of-thought prompting on challenging semantic problems such as GSM8K.

# Variable Computation

## Idea

One hypothesis is that chain of thought works simply because it allows the model to generate more tokens.

The authors test this by asking the model to generate a sequence of dots representing additional computation.

## Result

Variable computation alone performs approximately like standard prompting.

Therefore, simply increasing output length is not sufficient.

# Reasoning After Answer

## Idea

Another hypothesis is that chain-of-thought demonstrations simply activate knowledge from pre-training.

The authors test this by placing the reasoning after the final answer.

## Result

The method performs approximately like standard prompting.

This suggests that the sequential reasoning represented before the final answer is important.

# External Calculator

## Motivation

Language models can make arithmetic mistakes even when their reasoning structure is correct.

## Method

The equations generated inside the chain of thought are evaluated using an external Python calculator.

## Result

The external calculator significantly improves performance on many arithmetic benchmarks.

# Robustness to Annotators

## Definition

Different people can write different chain-of-thought demonstrations for the same task.

## Finding

Performance varies across annotators.

However, different chain-of-thought prompts generally outperform standard prompting.

# Prompt Sensitivity

## Definition

The effectiveness of few-shot prompting depends partly on the examples included in the prompt.

## Finding

Different exemplar sets and orders can change performance.

Chain-of-thought prompting remains generally beneficial despite this variation.

# Length Generalization

## Definition

Length generalization means solving problems requiring more reasoning steps than those shown in the demonstrations.

## Finding

Chain-of-thought prompting improves out-of-domain symbolic reasoning where the test examples require longer reasoning chains.

# Reasoning Decomposition

## Definition

A complex problem is broken into smaller intermediate steps.

## Role

The decomposition provides a structured path from the original input to the final answer.

# Natural-Language Reasoning

## Importance

The paper uses natural language for intermediate reasoning rather than requiring a formal symbolic language.

## Benefit

Natural language makes the approach applicable across multiple reasoning domains.

# Reasoning Correctness

## Important Observation

A generated chain of thought is not guaranteed to be correct.

The paper finds examples where:

- The reasoning is correct and the answer is correct.
- The reasoning contains minor errors.
- The reasoning contains major semantic errors.
- The final answer is correct despite incorrect reasoning.

# Task Difficulty

## Importance

The method is particularly useful for tasks requiring multiple reasoning steps.

## Simple Tasks

Tasks requiring only one or two reasoning steps show smaller gains.

# Conditions for Strong Gains

The paper suggests chain-of-thought prompting is most useful when:

1. The task is challenging.
2. The task requires multi-step reasoning.
3. A sufficiently large language model is used.
4. Standard prompting has a relatively flat scaling curve.

# Chain-of-Thought Limitations

## Scale Requirement

Strong gains generally require large models.

## Annotation Requirement

High-quality chain-of-thought demonstrations can require human effort.

## Prompt Sensitivity

Different demonstrations can produce different performance.

## Incorrect Reasoning

Generated reasoning can contain errors.

## Deployment Cost

Large models and longer reasoning sequences increase serving cost.