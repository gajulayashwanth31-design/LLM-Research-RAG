---
paper: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
year: 2022
domain: "Large Language Models"
subdomain: "Prompting and Reasoning"
difficulty: "Intermediate"
document_type: "Limitations"
keywords:
  - Chain-of-Thought Prompting
  - Reasoning Errors
  - Model Scale
  - Prompt Sensitivity
  - Annotation Cost
  - Reliability
  - Deployment Cost
generated_from: "Original Research Paper"
---

# Limitations

## Requires Large Models

### Description

Strong chain-of-thought benefits primarily appear when sufficiently large language models are used.

Small models often fail to generate logically useful chains of thought.

### Evidence

The paper observes that models below approximately the 100B scale often produce fluent but illogical chains of thought.

### Implication

Chain-of-thought prompting can be difficult to apply effectively to small language models.

# High Computational Cost

## Description

Large language models require significant computational resources.

Chain-of-thought prompting also generates additional tokens.

### Implication

Inference can be more expensive than standard prompting.

### Deployment

The paper notes that the emergence of strong chain-of-thought reasoning at large model scales makes real-world serving costly.

# Chain of Thought Is Not Guaranteed to Be Correct

## Description

A generated reasoning sequence can contain errors.

A model can produce:

- Correct reasoning and correct answer
- Incorrect reasoning and incorrect answer
- Incorrect reasoning but correct final answer

### Evidence

In the paper's qualitative analysis, some examples with correct final answers contain reasoning that is not fully correct.

# Incorrect Reasoning Paths

## Description

The model may generate a plausible-looking but incorrect reasoning process.

### Problem

A fluent chain of thought should not automatically be interpreted as a correct logical proof.

### Implication

Chain-of-thought output requires evaluation when correctness matters.

# Arithmetic Errors

## Description

A model may produce a logically reasonable chain of thought but perform an arithmetic operation incorrectly.

### Example

The model can identify the correct intermediate quantities but calculate an operation incorrectly.

### Mitigation

The paper experiments with an external calculator.

# External Calculator Dependency

## Description

For arithmetic tasks, an external calculator can improve performance.

### Trade-off

The system becomes more complex because reasoning and computation are handled by different components.

# Prompt Sensitivity

## Description

Performance depends on the demonstrations used in the prompt.

### Evidence

Different annotators and different exemplar sets produce different results.

### Implication

There is no single universally optimal chain-of-thought prompt.

# Annotator Variation

## Description

Different people can create different reasoning demonstrations for the same problem.

### Finding

Performance varies between annotators.

### Important Observation

Despite this variation, the different chain-of-thought prompts generally outperform standard prompting.

# Exemplar Sensitivity

## Description

Changing the few-shot examples can change performance.

### Implication

Careful selection of demonstrations remains important.

# Prompt Engineering Still Matters

## Description

The paper explicitly notes that prompt engineering can substantially affect performance.

### Evidence

The authors report tasks where some chain-of-thought prompts work well while others do not.

### Implication

Chain-of-thought prompting does not eliminate the need for prompt design.

# Model-Specific Transfer

## Description

The same chain-of-thought prompts do not always produce the same improvements across different models.

### Finding

The paper observes that gains do not transfer perfectly among LaMDA, GPT-3, and PaLM.

### Possible Factors

The authors suggest that differences in:

- Pre-training data
- Model architecture

may influence the effectiveness of chain-of-thought prompting.

# Annotation Cost

## Few-Shot Setting

For the few-shot experiments in the paper, only a small number of demonstrations are required.

## Fine-Tuning Setting

Creating large datasets containing high-quality chain-of-thought annotations could be expensive.

### Implication

Scaling rationale annotation to large training datasets can be difficult.

# Reasoning Does Not Necessarily Reflect Internal Computation

## Description

Chain-of-thought provides a visible sequence of reasoning steps.

However, the paper explicitly states that this does not establish that the neural network's internal computation is actually identical to the generated reasoning.

### Implication

Generated explanations should not automatically be treated as a faithful description of internal model computation.

# Variable Computation Is Not Enough

## Description

One hypothesis is that chain-of-thought works simply because it gives the model additional output tokens.

The authors test this using a variable-computation-only condition.

### Finding

Variable computation alone performs approximately like standard prompting.

### Implication

The benefit appears to involve the content of the intermediate reasoning, not merely longer output.

# Equation-Only Reasoning Is Not Always Enough

## Description

Equation-only prompting improves some arithmetic tasks.

However, it performs poorly on some semantically difficult tasks.

### GSM8K

For GSM8K, directly converting the problem into a single equation can be difficult.

### Reason

The problem may require understanding several semantic relationships before an appropriate equation can be constructed.

### Implication

Natural-language intermediate reasoning can provide useful semantic decomposition.

# Limited Benefit on Simple Tasks

## Description

Chain-of-thought prompting is most useful for challenging multi-step reasoning.

### Simple Problems

Tasks requiring only one or two reasoning steps may show little improvement.

### Example

The paper reports small gains on simple subsets of MAWPS.

# Limited Benefit When Baseline Is Already Strong

## Description

If standard prompting already performs near the maximum possible level, there is limited room for improvement.

### Implication

The absolute gain from chain-of-thought can be small even if the method remains useful.

# Reasoning Length Limitations

## Description

The paper demonstrates out-of-domain length generalization on symbolic tasks.

However, performance still decreases when the reasoning sequence becomes substantially more difficult.

### Implication

Chain-of-thought does not provide unlimited reasoning capability.

# Factual Reliability

## Description

The paper notes that incorrect reasoning paths can produce incorrect answers.

### Implication

Chain-of-thought prompting should not be interpreted as a guarantee of factual or logical correctness.

# Serving Cost

## Description

Large models are expensive to serve.

Chain-of-thought additionally produces intermediate tokens.

### Implication

Reasoning-heavy prompts can increase:

- Inference latency
- Token usage
- Computational cost

# Overall Limitation

Chain-of-thought prompting is a powerful elicitation technique, but its effectiveness depends on:

- Model scale
- Prompt quality
- Task difficulty
- Demonstration selection
- Reasoning reliability

The paper therefore presents chain-of-thought prompting as a method for eliciting reasoning capabilities rather than a guaranteed reasoning algorithm.