---
paper: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
year: 2022
domain: "Large Language Models"
subdomain: "Prompting and Reasoning"
difficulty: "Intermediate"
document_type: "Applications"
keywords:
  - Chain-of-Thought Prompting
  - Reasoning
  - Arithmetic Reasoning
  - Commonsense Reasoning
  - Symbolic Reasoning
  - Question Answering
  - Robot Planning
  - Few-Shot Learning
generated_from: "Original Research Paper"
---

# Applications

## Arithmetic Problem Solving

### Description

Chain-of-thought prompting can be used to improve performance on multi-step arithmetic word problems.

The model is shown examples containing intermediate calculations before the final answer.

### Demonstrated Benchmarks

The paper evaluates:

- GSM8K
- SVAMP
- ASDiv
- AQuA
- MAWPS

### Example

A problem involving several quantities can be decomposed into:

1. Extract relevant quantities.
2. Perform an intermediate calculation.
3. Use the intermediate result in another calculation.
4. Produce the final answer.

# Mathematical Word Problems

## GSM8K

GSM8K is a challenging benchmark of mathematical word problems.

The paper demonstrates particularly strong improvements from chain-of-thought prompting on this benchmark.

### PaLM 540B

The paper reports:

Standard prompting: 17.9%

Chain-of-thought prompting: 56.9%

The chain-of-thought result establishes a new state of the art in the paper.

# Commonsense Question Answering

## CommonsenseQA

Chain-of-thought prompting is evaluated on CommonsenseQA.

The task requires understanding questions involving general world knowledge.

### Use of Reasoning

Intermediate reasoning can help connect the information in the question with the commonsense knowledge required to select an answer.

# Multi-Hop Reasoning

## StrategyQA

StrategyQA requires the model to infer a multi-hop strategy before reaching an answer.

Chain-of-thought prompting is therefore particularly relevant to this task.

### Result

PaLM 540B with chain-of-thought prompting achieves:

75.6%

compared with:

69.4%

for the prior state of the art reported in the paper.

# Date Reasoning

## Date Understanding

The paper evaluates chain-of-thought prompting on date-related reasoning problems.

The model must infer a date from contextual information.

### Reasoning Process

The model can explicitly perform intermediate date calculations before producing the final answer.

# Sports Reasoning

## Sports Understanding

The task requires determining whether a statement involving sports is plausible.

### Result

The paper reports:

95.4%

for PaLM 540B with chain-of-thought prompting.

This compares with:

84%

for an unaided sports enthusiast.

# Robot Instruction Planning

## SayCan

SayCan maps natural-language instructions to sequences of robot actions.

The paper uses chain-of-thought examples for this task.

### Example Structure

A natural-language instruction can be decomposed into:

1. Identify the object.
2. Locate the object.
3. Pick the object.
4. Locate the user.
5. Place the object.

### Importance

This demonstrates that chain-of-thought prompting is not limited to mathematical problems.

# Symbolic Manipulation

## Last Letter Concatenation

The model must manipulate symbols according to a simple rule.

For example:

Lady Gaga

→ y + a

→ ya

### Purpose

The task tests whether chain-of-thought prompting can help models perform symbolic operations.

# State Tracking

## Coin Flip

The model tracks the state of a coin after a sequence of flip and no-flip operations.

### Reasoning

The model can explicitly track the state after each operation.

### Importance

This demonstrates chain-of-thought prompting for symbolic state transitions.

# Length Generalization

## Out-of-Domain Symbolic Tasks

The paper evaluates cases where test problems contain more reasoning steps than the few-shot demonstrations.

### Result

Chain-of-thought prompting improves performance on these longer reasoning sequences.

### Application

This suggests that chain-of-thought examples can teach a reasoning procedure rather than merely memorizing the exact number of steps shown.

# Few-Shot Reasoning

## General Application

Chain-of-thought prompting allows a single language model to perform multiple reasoning tasks through prompting.

The model does not require task-specific fine-tuning.

## Benefit

The same model checkpoint can be used across different tasks by changing the demonstrations in the prompt.

# Reasoning with External Tools

## External Calculator

The paper combines generated reasoning with an external calculator for arithmetic operations.

### Workflow

Language model:

Generate reasoning and equations.

↓

External calculator:

Evaluate equations.

↓

Language model reasoning:

Use calculated results in subsequent steps.

### Benefit

This reduces errors caused by incorrect arithmetic operations.

# Prompt-Based Reasoning Systems

## General Pattern

The experiments suggest a general pattern for reasoning-oriented LLM systems:

Task examples

↓

Reasoning demonstrations

↓

Test input

↓

Generated chain of thought

↓

Final answer

# When Chain-of-Thought Is Most Useful

## Challenging Tasks

The method is most useful when the task requires multiple reasoning steps.

## Large Models

Strong gains generally require sufficiently large language models.

## Flat Scaling Tasks

The method is particularly useful when standard prompting has a relatively flat scaling curve.

## Less Useful Cases

Benefits can be smaller when:

- The task is simple.
- Only one or two reasoning steps are required.
- Standard prompting already performs very well.
- The model is too small to reliably generate useful reasoning.

# Practical Application

## Educational Reasoning

The paper demonstrates that intermediate reasoning can help models solve complex problems.

This suggests potential use in systems where solving a problem requires explicit intermediate steps.

## Mathematical Assistance

A language model can be prompted to decompose mathematical word problems before producing the final result.

## Decision Support

The same pattern can potentially be used when decisions require multiple reasoning steps.

## Planning

The SayCan experiment demonstrates the application of intermediate reasoning to action planning.

# Important Limitation

The paper does not claim that chain-of-thought guarantees correct reasoning.

Generated reasoning can contain errors.

Therefore, chain-of-thought should not automatically be treated as a guaranteed proof of correctness.
