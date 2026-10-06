---
paper: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
year: 2022
domain: "Large Language Models"
subdomain: "Prompting and Reasoning"
difficulty: "Intermediate"
document_type: "Paper Overview"
keywords:
  - Chain-of-Thought Prompting
  - Large Language Models
  - Few-Shot Prompting
  - In-Context Learning
  - Reasoning
  - Emergent Abilities
  - Arithmetic Reasoning
  - Commonsense Reasoning
  - Symbolic Reasoning
generated_from: "Original Research Paper"
---

# Paper Overview

## Paper Summary

The paper "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" studies a prompting technique called chain-of-thought prompting.

The central idea is to provide a language model with few-shot examples that contain not only the input and final answer, but also a sequence of intermediate reasoning steps.

The authors define a chain of thought as a series of intermediate natural language reasoning steps that lead to the final output.

Instead of prompting a model with only:

input → output

the proposed method uses:

input → chain of thought → output

The paper investigates whether sufficiently large language models can use these examples to perform complex reasoning tasks.

## Main Finding

The paper finds that chain-of-thought prompting can substantially improve the reasoning ability of large language models.

The improvements are demonstrated across three broad categories:

- Arithmetic reasoning
- Commonsense reasoning
- Symbolic reasoning

The improvements can be particularly large when the language model is sufficiently large and the task requires multiple reasoning steps.

## Main Result

The paper reports that chain-of-thought prompting can unlock reasoning capabilities that are not apparent under standard prompting.

For example, PaLM 540B with chain-of-thought prompting achieves state-of-the-art performance on the GSM8K benchmark of mathematical word problems.

The paper reports that eight chain-of-thought exemplars are sufficient to obtain strong improvements in several experiments.

## Research Question

The main question investigated by the paper is:

Can large language models perform substantially better on difficult reasoning tasks when few-shot prompts contain intermediate reasoning steps?

## Motivation

Large language models had demonstrated strong few-shot learning capabilities.

However, scaling model size alone had not been sufficient to obtain high performance on challenging reasoning tasks.

Arithmetic, commonsense, and symbolic reasoning remained difficult even for large models.

The authors investigate whether the problem is partly related to how the model is prompted.

## Standard Few-Shot Prompting

Traditional few-shot prompting provides examples consisting of inputs and outputs.

The model is expected to infer the task from these examples and directly produce an answer.

For example:

Question → Answer

The model does not receive an explicit intermediate solution process.

## Chain-of-Thought Prompting

Chain-of-thought prompting augments each few-shot example with intermediate reasoning.

The structure becomes:

Question → Reasoning Steps → Answer

The reasoning steps are written in natural language.

## Example

A standard prompt may contain:

Question:
Roger has 5 tennis balls. He buys 2 cans containing 3 balls each. How many balls does he have?

Answer:
11

A chain-of-thought prompt instead contains:

Question:
Roger has 5 tennis balls. He buys 2 cans containing 3 balls each. How many balls does he have?

Reasoning:
Roger started with 5 balls.
Two cans contain 6 additional balls.
5 + 6 = 11.

Answer:
11

The paper investigates whether examples structured in this way help models solve new problems.

# Problem Addressed

## Difficulty of Reasoning Tasks

Large language models can perform many tasks through prompting.

However, difficult reasoning tasks may require multiple intermediate operations.

Examples include:

- Multi-step arithmetic
- Commonsense reasoning
- Symbolic manipulation
- State tracking
- Multi-hop reasoning

## Limitation of Standard Prompting

Standard few-shot prompting provides input-output examples.

For difficult reasoning problems, directly mapping an input to the final output may be challenging.

The model must internally determine the intermediate steps needed to reach the answer.

## Scaling Alone Is Not Always Enough

The paper notes that increasing language model size provides many benefits.

However, scaling alone does not always result in strong performance on difficult reasoning tasks.

Some reasoning tasks have relatively flat scaling curves under standard prompting.

## Cost of Fine-Tuning Reasoning Models

One way to teach models reasoning is to create datasets containing natural language rationales and fine-tune a model.

However, creating large numbers of high-quality rationales is expensive and complicated.

The authors therefore investigate whether reasoning can instead be elicited through prompting.

# Existing Approaches

## Rationale-Augmented Training

Prior work had trained models to generate natural language rationales or intermediate steps.

These approaches can improve reasoning.

However, they require datasets containing high-quality reasoning annotations.

## Fine-Tuning

Another approach is to fine-tune a pretrained language model on examples containing reasoning steps.

This requires additional training data and computation.

## Neuro-Symbolic Approaches

Some previous methods use formal languages or symbolic representations for reasoning.

These approaches can provide structured intermediate computation.

However, they are different from the natural-language reasoning approach explored in this paper.

## Few-Shot Prompting

Few-shot prompting allows a model to perform a new task by providing a small number of input-output examples.

This avoids training a separate model for every task.

However, traditional few-shot prompting performs poorly on some difficult reasoning tasks.

# Proposed Approach

## Chain-of-Thought Prompting

The paper combines the advantages of rationale-based reasoning and few-shot prompting.

The model receives a few examples containing:

- Input
- Chain of thought
- Output

The model then generates a chain of thought for a new input before producing its final answer.

## No Fine-Tuning

A key characteristic of the experiments is that the models are prompted rather than fine-tuned.

The authors use off-the-shelf language models.

No language model is fine-tuned in the process of writing the paper.

## Few-Shot Setting

The proposed method works through in-context learning.

The reasoning examples are included directly in the prompt.

## Natural Language Intermediate Steps

The intermediate reasoning is expressed in natural language.

This allows the same general approach to be applied across different reasoning domains.

# Properties of Chain-of-Thought Prompting

## Decomposition

Chain of thought allows a difficult problem to be decomposed into intermediate steps.

This can make multi-step reasoning more manageable for the model.

## Additional Computation

A chain of thought can contain multiple intermediate tokens.

This provides the model with additional computation for problems that require more reasoning steps.

## Interpretability

The generated reasoning steps provide an interpretable view of the model's behavior.

They can suggest how the model arrived at an answer.

The authors note that this does not fully characterize the internal computations of the model.

## Broad Applicability

Because chain of thought is expressed using natural language, the approach can potentially be used for many reasoning tasks.

The paper demonstrates this on:

- Arithmetic reasoning
- Commonsense reasoning
- Symbolic reasoning

## Ease of Elicitation

For sufficiently large models, chain-of-thought reasoning can be elicited simply by including chain-of-thought examples in the prompt.

# Arithmetic Reasoning

## Motivation

Arithmetic word problems are challenging for language models even though they are relatively straightforward for humans.

The paper evaluates whether chain-of-thought prompting can improve performance on such problems.

## Benchmarks

The arithmetic experiments use five benchmarks:

1. GSM8K
2. SVAMP
3. ASDiv
4. AQuA
5. MAWPS

## Standard Prompting

The baseline uses few-shot input-output examples.

The model receives a question and directly produces an answer.

## Chain-of-Thought Prompting

The proposed method augments the few-shot examples with reasoning steps.

The model is encouraged to generate intermediate computations before the final answer.

## Eight Exemplars

For most arithmetic datasets, the authors manually construct eight chain-of-thought exemplars.

The same set is used across the arithmetic benchmarks, except AQuA.

## AQuA

AQuA is a multiple-choice algebraic word problem dataset.

The authors use four exemplars for AQuA.

## Models

The arithmetic experiments evaluate several language models.

These include:

- GPT-3
- LaMDA
- PaLM
- UL2
- Codex

## Model Scaling

The experiments evaluate different model sizes.

For example, PaLM is evaluated at:

- 8B
- 62B
- 540B

LaMDA is evaluated at multiple scales including:

- 420M
- 2B
- 8B
- 68B
- 137B

## Emergent Behavior

One of the major findings is that chain-of-thought prompting behaves as an emergent capability of model scale.

Small models do not consistently benefit from chain-of-thought prompting.

Large models can show substantial gains.

## GSM8K

GSM8K contains challenging mathematical word problems.

The largest models show particularly large improvements from chain-of-thought prompting.

PaLM 540B with chain-of-thought prompting achieves new state-of-the-art performance on GSM8K in the paper.

## Problem Complexity

The benefits of chain-of-thought prompting are larger for more complicated problems.

For example, the improvement is particularly large on GSM8K.

For simple subsets of MAWPS that require only one reasoning step, improvements are much smaller.

# Commonsense Reasoning

## Motivation

Commonsense reasoning requires understanding physical and human interactions.

It can involve background knowledge and multi-step reasoning.

## Benchmarks

The paper evaluates five commonsense reasoning datasets:

1. CommonsenseQA
2. StrategyQA
3. Date Understanding
4. Sports Understanding
5. SayCan

## CommonsenseQA

CommonsenseQA contains questions requiring commonsense knowledge.

The questions can involve complex semantics.

## StrategyQA

StrategyQA requires models to infer a multi-hop strategy to answer questions.

## Date Understanding

The Date Understanding task requires inferring a date from a given context.

## Sports Understanding

Sports Understanding requires determining whether a sports-related statement is plausible or implausible.

## SayCan

SayCan involves mapping natural-language instructions to sequences of robot actions.

## Results

Scaling the model improves standard prompting performance.

Chain-of-thought prompting provides further improvements.

The largest gains are generally observed with PaLM 540B.

## StrategyQA

The paper reports PaLM 540B with chain-of-thought prompting achieving:

75.6%

compared with:

69.4%

for the prior state of the art reported in the paper.

## Sports Understanding

PaLM 540B with chain-of-thought prompting reaches:

95.4%

compared with:

84%

for an unaided sports enthusiast.

## CSQA

The improvement on CSQA is comparatively smaller.

This demonstrates that chain-of-thought prompting does not produce equally large gains on every task.

# Symbolic Reasoning

## Motivation

The paper also investigates symbolic reasoning tasks.

These tasks are deliberately simple for humans but can be challenging for language models.

## Last Letter Concatenation

The first symbolic task asks the model to concatenate the last letters of words.

For example:

Amy Brown

becomes:

yn

## Coin Flip

The second task tracks the state of a coin after a sequence of people either flip or do not flip it.

The model must determine whether the coin remains heads up.

## In-Domain Evaluation

The model is evaluated on examples containing the same number of reasoning steps as the demonstrations.

## Out-of-Domain Evaluation

The OOD setting contains longer reasoning sequences than those present in the few-shot examples.

## Length Generalization

The paper finds that chain-of-thought prompting facilitates generalization to longer symbolic reasoning sequences.

## PaLM 540B

With PaLM 540B, chain-of-thought prompting achieves very high solve rates on the symbolic tasks.

The paper reports almost 100% solve rates on the in-domain symbolic evaluations.

## OOD Results

Standard prompting performs poorly on the OOD tasks.

Chain-of-thought prompting produces upward scaling curves and enables better performance on longer reasoning sequences.

# Ablation Studies

## Purpose

The paper investigates why chain-of-thought prompting works.

Several alternative prompting strategies are evaluated.

The main ablations are:

- Equation-only prompting
- Variable-compute-only prompting
- Reasoning-after-answer prompting

## Equation-Only Prompting

In equation-only prompting, the model is encouraged to produce an equation before the final answer.

The natural-language reasoning steps are removed.

## Results

Equation-only prompting helps on some datasets.

However, it does not provide the same improvement as full chain-of-thought prompting on challenging datasets such as GSM8K.

## Interpretation

The authors suggest that some questions are too semantically challenging to translate directly into a single mathematical equation.

Natural-language intermediate reasoning allows the model to process different parts of the problem sequentially.

## Variable Compute Only

The authors investigate whether chain-of-thought works simply because it produces additional tokens and therefore allows more computation.

The model is prompted to produce a sequence of dots corresponding approximately to the required computation.

## Result

Variable computation alone performs approximately like the baseline.

This suggests that simply producing additional tokens is not sufficient.

The content of the intermediate reasoning matters.

## Reasoning After Answer

Another possibility is that chain-of-thought examples merely activate knowledge learned during pre-training.

To test this, the authors place the reasoning after the answer.

## Result

Reasoning after the answer performs approximately like standard prompting.

This suggests that the sequential reasoning process represented in the chain of thought is important.

# Robustness

## Different Annotators

The authors investigate whether chain-of-thought prompting depends on a particular author's writing style.

Different annotators independently create chain-of-thought demonstrations.

## Results

Different annotators produce different performance levels.

However, the different chain-of-thought prompts generally outperform standard prompting.

## Concise Reasoning

The authors also test intentionally concise chain-of-thought demonstrations.

The method continues to outperform standard prompting.

## Different Exemplars

The authors test different sets of few-shot exemplars.

The performance varies, as expected for prompting methods.

However, chain-of-thought prompting remains generally better than standard prompting.

## Exemplar Order

The paper also investigates different orders of the few-shot exemplars.

The results indicate that chain-of-thought prompting remains effective under different exemplar arrangements.

# Model-Scale Dependence

## Small Models

Small models generally do not benefit substantially from chain-of-thought prompting.

Some smaller models produce fluent but illogical chains of thought.

## Large Models

The benefits become significant as model size increases.

The paper identifies chain-of-thought reasoning as an emergent capability of sufficiently large models.

## Approximately 100B Parameters

The paper observes that strong chain-of-thought gains generally emerge around the scale of approximately 100B parameters.

## Scaling Curves

For several difficult reasoning tasks, standard prompting has relatively flat scaling curves.

Chain-of-thought prompting produces increasing performance as model scale grows.

# Qualitative Analysis

## Correct Answers

The authors manually examine 50 random GSM8K examples where LaMDA 137B produces the correct final answer.

Almost all generated chains of thought are also logically and mathematically correct.

Two examples arrive at the correct answer coincidentally despite incorrect reasoning.

## Incorrect Answers

The authors also examine 50 examples where the model produces an incorrect final answer.

46% of the generated chains of thought are almost correct but contain minor errors.

Examples of minor errors include:

- Calculator errors
- Symbol mapping errors
- Missing one reasoning step

The remaining 54% contain major errors in semantic understanding or coherence.

## Effect of Scaling

The authors compare errors made by PaLM 62B with those made by PaLM 540B.

Scaling to 540B fixes a substantial portion of:

- Missing-step errors
- Semantic-understanding errors

# External Calculator

## Motivation

Some generated chains of thought contain correct reasoning but incorrect arithmetic operations.

To address arithmetic mistakes, the authors experiment with an external calculator.

## Procedure

The equations generated inside the chain of thought are passed to a Python-based calculator.

The calculated results are then propagated to later equations when multiple equations occur in the reasoning chain.

## Effect

Adding an external calculator substantially improves chain-of-thought performance on many arithmetic benchmarks.

## Interpretation

This separates reasoning errors from arithmetic computation errors.

The language model can generate the reasoning structure while an external tool handles arithmetic operations.

# Applications Demonstrated

## Arithmetic Problem Solving

Chain-of-thought prompting improves performance on multi-step arithmetic word problems.

## Commonsense Reasoning

The approach improves several commonsense reasoning tasks.

## Symbolic Manipulation

The approach supports symbolic tasks such as:

- Last-letter concatenation
- Coin-state tracking

## Robot Instruction Planning

The SayCan experiment demonstrates mapping natural-language instructions to sequences of robot actions.

## Question Answering

The paper's broader motivation includes reasoning-oriented question answering.

# Conditions for Effectiveness

## Challenging Task

The task should require multiple reasoning steps.

## Large Language Model

A sufficiently large language model is generally required for substantial benefits.

## Flat Standard-Prompting Scaling Curve

The method is especially useful when standard prompting does not improve substantially with model scale.

## Simple Tasks

For tasks that require only one or two reasoning steps, the benefit can be small.

## High Baseline Performance

If standard prompting already achieves very high performance, there may be limited room for improvement.

# Limitations

## Reasoning Does Not Guarantee Correctness

A generated chain of thought can contain incorrect reasoning.

A correct final answer can occasionally result from incorrect intermediate reasoning.

## Model Scale Requirement

Strong chain-of-thought capabilities emerge primarily at large model scales.

This makes the method expensive for smaller deployments.

## Annotation Cost

Although few-shot prompting requires only a small number of demonstrations, manually creating high-quality chain-of-thought annotations can still be costly.

This becomes especially problematic for large-scale fine-tuning datasets.

## Prompt Sensitivity

The exact choice of chain-of-thought examples affects performance.

Different annotators and exemplar sets can produce different results.

## Model-Specific Behavior

The same chain-of-thought prompts do not always transfer equally well between different language models.

The paper observes that gains do not transfer perfectly across models.

## Incorrect Reasoning Paths

There is no guarantee that generated reasoning is correct.

Incorrect reasoning can lead to incorrect answers.

## Interpretability Limitation

Although chains of thought provide a window into model behavior, they do not necessarily reveal the actual internal computation performed by the neural network.

## Serving Cost

Because strong chain-of-thought reasoning requires large models and produces additional tokens, deployment can be expensive.

# Discussion

## Broader Capability

The paper argues that standard prompting may only reveal a lower bound on the capabilities of large language models.

Chain-of-thought prompting expands the set of tasks that sufficiently large models can solve.

## Emergent Reasoning

The relationship between model scale and chain-of-thought performance is one of the central findings.

Reasoning capability becomes substantially stronger as models become sufficiently large.

## Natural Language Reasoning

The use of natural-language intermediate steps distinguishes this method from approaches that rely entirely on formal symbolic representations.

## Future Directions

The paper raises questions about:

- How reasoning improves with further scaling
- What other prompting methods can unlock additional capabilities
- How to induce reasoning in smaller models
- How to generate high-quality chain-of-thought demonstrations automatically

# Conclusion

The paper demonstrates that chain-of-thought prompting is a simple method for eliciting multi-step reasoning from sufficiently large language models.

The method augments few-shot demonstrations with intermediate natural-language reasoning steps.

Across arithmetic, commonsense, and symbolic reasoning tasks, chain-of-thought prompting often substantially outperforms standard prompting.

The benefits are strongest for challenging multi-step tasks and sufficiently large language models.

The paper identifies chain-of-thought reasoning as an emergent capability associated with model scale.

The work demonstrates that prompting alone, without fine-tuning, can unlock capabilities that are difficult to observe with standard prompting.