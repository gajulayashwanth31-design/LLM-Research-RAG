---
paper: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
year: 2022
domain: "Large Language Models"
subdomain: "Prompting and Reasoning"
difficulty: "Intermediate"
document_type: "Terminology"
keywords:
  - Chain-of-Thought Prompting
  - Few-Shot Prompting
  - In-Context Learning
  - Reasoning
  - Emergent Ability
  - Model Scale
  - Rationale
  - Exemplar
  - Benchmark
  - Ablation
generated_from: "Original Research Paper"
---

# Chain-of-Thought Prompting

## Definition

A prompting method in which few-shot examples contain intermediate natural-language reasoning steps between the input and final output.

# Chain of Thought

## Definition

A series of intermediate reasoning steps that lead to a final output.

# Standard Prompting

## Definition

Few-shot prompting where demonstrations contain inputs and final outputs without explicit intermediate reasoning.

# Few-Shot Prompting

## Definition

A prompting method where a small number of demonstrations are provided to the language model before the test input.

# In-Context Learning

## Definition

Learning task behavior from examples provided in the input context without updating model parameters.

# Exemplar

## Definition

A demonstration example included in a prompt to show the model how to perform a task.

# Rationale

## Definition

An explanation or reasoning sequence that describes intermediate steps leading to an answer.

# Reasoning

## Definition

The process of combining information through intermediate steps to reach a conclusion.

# Arithmetic Reasoning

## Definition

Reasoning involving mathematical operations and multi-step numerical calculations.

# Commonsense Reasoning

## Definition

Reasoning that depends on general knowledge about physical and human interactions.

# Symbolic Reasoning

## Definition

Reasoning involving symbolic manipulation or explicit state transitions.

# Emergent Ability

## Definition

A capability that becomes apparent when a model reaches sufficiently large scale.

# Model Scale

## Definition

The size of a language model, commonly represented by the number of parameters.

# Scaling Curve

## Definition

The relationship between model scale and task performance.

# Multi-Step Reasoning

## Definition

Reasoning that requires several intermediate operations or decisions before reaching the final answer.

# Length Generalization

## Definition

The ability to solve examples requiring longer reasoning sequences than those observed in the demonstrations.

# In-Domain Evaluation

## Definition

Evaluation where the test examples have reasoning characteristics similar to the few-shot demonstrations.

# Out-of-Domain Evaluation

## Definition

Evaluation where the test examples require characteristics not present in the demonstrations, such as longer reasoning sequences.

# Ablation Study

## Definition

An experiment where part of a proposed method is removed or modified to determine its contribution.

# Equation-Only Prompting

## Definition

A prompting variant where the model produces an equation as an intermediate step without natural-language reasoning.

# Variable Compute

## Definition

The hypothesis that chain-of-thought helps because it allows the model to perform additional computation through additional generated tokens.

# External Calculator

## Definition

An external computational tool used to evaluate equations generated inside a chain of thought.

# Prompt Engineering

## Definition

The process of designing and selecting prompts or demonstrations to improve model performance.

# Prompt Sensitivity

## Definition

The dependence of model performance on the particular demonstrations, ordering, or wording used in the prompt.

# Robustness

## Definition

The degree to which the effectiveness of a prompting method remains consistent under changes such as different annotators or exemplars.

# Benchmark

## Definition

A dataset or evaluation suite used to measure model performance on a particular task.

# Solve Rate

## Definition

The percentage of evaluated problems that the model solves correctly.

# GSM8K

## Definition

A benchmark of grade-school mathematical word problems used in the paper to evaluate arithmetic reasoning.

# SVAMP

## Definition

A mathematical word problem dataset containing varied problem structures.

# ASDiv

## Definition

A diverse arithmetic word problem dataset used to evaluate mathematical reasoning.

# AQuA

## Definition

A multiple-choice dataset of algebraic word problems.

# MAWPS

## Definition

A benchmark containing mathematical word problems used to evaluate arithmetic reasoning.

# CommonsenseQA

## Definition

A commonsense question-answering benchmark involving questions that require general world knowledge.

# StrategyQA

## Definition

A benchmark requiring models to infer a multi-hop strategy to answer questions.

# Date Understanding

## Definition

A reasoning task requiring the model to infer dates from contextual information.

# Sports Understanding

## Definition

A task requiring the model to determine whether sports-related statements are plausible.

# SayCan

## Definition

A task involving mapping natural-language instructions to sequences of robot actions.

# PaLM

## Definition

A large language model family evaluated in the paper at multiple scales.

# LaMDA

## Definition

A language model family evaluated at several model sizes in the paper.

# GPT-3

## Definition

A large language model family evaluated in the arithmetic reasoning experiments.

# Codex

## Definition

A language model based on GPT-style technology evaluated in the paper for reasoning tasks.

# UL2

## Definition

A language model evaluated at 20B parameters in the arithmetic reasoning experiments.

# State-of-the-Art

## Definition

The best reported performance among the comparison systems considered for a particular benchmark at the time of the paper.

# Natural-Language Intermediate Steps

## Definition

Reasoning steps expressed using ordinary language rather than only formal equations or symbolic representations.

# Reasoning Path

## Definition

The sequence of intermediate reasoning steps generated between the input and final answer.

# Fine-Tuning

## Definition

Updating model parameters using task-specific training data.

The main chain-of-thought experiments in this paper do not fine-tune the language models.

# Off-the-Shelf Language Model

## Definition

A pre-existing language model used directly without additional task-specific parameter training.

# Emergent Reasoning

## Definition

The emergence of substantially stronger reasoning behavior as model scale increases.

# Chain-of-Thought Annotation

## Definition

The process of creating demonstrations containing intermediate reasoning steps.

# Reasoning Error

## Definition

An incorrect intermediate step in a generated chain of thought.

# Semantic Error

## Definition

An error caused by misunderstanding the meaning or relationships in the input problem.

# Arithmetic Error

## Definition

An incorrect mathematical operation within an otherwise meaningful reasoning process.