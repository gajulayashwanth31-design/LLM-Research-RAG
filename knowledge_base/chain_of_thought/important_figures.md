---
paper: "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models"
year: 2022
domain: "Large Language Models"
subdomain: "Prompting and Reasoning"
difficulty: "Intermediate"
document_type: "Important Figures"
keywords:
  - Chain-of-Thought Prompting
  - Few-Shot Prompting
  - Model Scaling
  - Arithmetic Reasoning
  - Commonsense Reasoning
  - Symbolic Reasoning
  - Ablation
generated_from: "Original Research Paper"
---

# Important Figures

## Figure 1: Standard Prompting vs Chain-of-Thought Prompting

### Purpose

Figure 1 provides the basic motivation for chain-of-thought prompting.

It compares standard prompting with chain-of-thought prompting on arithmetic problems.

### Standard Prompting

The model receives:

Question

followed by:

Answer

The model must directly produce the final answer.

### Chain-of-Thought Prompting

The model receives demonstrations containing:

Question

Reasoning

Answer

### Main Observation

The chain-of-thought example demonstrates intermediate reasoning steps.

The figure illustrates how these intermediate steps can allow a model to arrive at the correct answer when standard prompting produces an incorrect answer.

### Importance

This figure introduces the central idea of the paper.

# Figure 2: PaLM 540B on GSM8K

### Purpose

Figure 2 compares the performance of different approaches on the GSM8K mathematical word problem benchmark.

### Compared Systems

The figure includes:

- Finetuned GPT-3 175B
- Prior best
- PaLM 540B with standard prompting
- PaLM 540B with chain-of-thought prompting

### Main Observation

PaLM 540B with chain-of-thought prompting achieves a substantial improvement over standard prompting.

### Importance

The figure demonstrates one of the paper's major results:

Chain-of-thought prompting can produce state-of-the-art reasoning performance without task-specific fine-tuning.

# Figure 3: Chain-of-Thought Examples

### Purpose

Figure 3 presents examples of input, chain of thought, and output triples.

### Task Categories

The examples cover:

- Arithmetic reasoning
- Commonsense reasoning
- Symbolic reasoning
- Robot instruction planning

### Arithmetic Examples

The figure includes examples involving:

- Math word problems
- Multiple-choice arithmetic
- Date understanding

### Commonsense Examples

Examples include:

- CommonsenseQA
- Sports reasoning
- Strategy-style reasoning

### Symbolic Examples

Examples include:

- Last letter concatenation
- Coin flip state tracking

### SayCan

The figure also illustrates natural-language reasoning for robot action planning.

### Importance

The figure demonstrates that the same prompting format can be applied to different reasoning domains.

# Figure 4: Arithmetic Scaling Curves

### Purpose

Figure 4 shows how chain-of-thought prompting affects arithmetic reasoning performance as model scale increases.

### Benchmarks

The figure includes:

- GSM8K
- SVAMP
- MAWPS

### Models

Results are shown for:

- LaMDA
- GPT
- PaLM

### Main Observation

Chain-of-thought prompting becomes increasingly effective as model size increases.

### Emergent Behavior

The figure supports the paper's claim that chain-of-thought reasoning is an emergent capability of model scale.

### Complexity Effect

The largest gains appear on more challenging reasoning problems.

# Figure 5: Prompting Ablation Study

### Purpose

Figure 5 compares chain-of-thought prompting with several alternative prompting strategies.

### Methods

The figure compares:

- Standard prompting
- Equation-only prompting
- Variable-compute-only prompting
- Reasoning-after-answer
- Chain-of-thought prompting

### Main Finding

The alternatives do not reproduce the full benefit of chain-of-thought prompting.

### Interpretation

The result suggests that the content and ordering of natural-language intermediate reasoning are important.

# Figure 6: Robustness to Different Prompts

### Purpose

Figure 6 evaluates whether chain-of-thought prompting depends on particular examples or annotators.

### Variations

The experiments include:

- Different annotators
- Concise reasoning style
- Different exemplars

### Main Observation

Performance varies across prompts.

However, the different chain-of-thought prompts generally outperform standard prompting.

### Importance

The figure demonstrates that the method is not dependent on one exact reasoning style.

# Figure 7: Commonsense Reasoning

### Purpose

Figure 7 evaluates chain-of-thought prompting on commonsense reasoning tasks.

### Benchmarks

The figure includes:

- CommonsenseQA
- StrategyQA
- Date Understanding
- Sports Understanding
- SayCan

### Model

The figure primarily presents results for PaLM.

### Main Finding

Scaling the model improves standard prompting performance.

Chain-of-thought prompting produces additional gains.

### Strong Results

The largest improvements generally occur for PaLM 540B.

# Figure 8: Symbolic Reasoning

### Purpose

Figure 8 evaluates chain-of-thought prompting on symbolic reasoning tasks.

### Tasks

The figure includes:

- Last Letter Concatenation
- Coin Flip

### Evaluation Settings

Both in-domain and out-of-domain reasoning lengths are evaluated.

### Main Finding

Chain-of-thought prompting facilitates generalization to longer reasoning sequences.

### Importance

The figure provides evidence that chain-of-thought prompting can improve length generalization.

# Figure Summary

## Overall Pattern

The figures collectively demonstrate:

1. The basic chain-of-thought prompting mechanism.
2. Strong arithmetic improvements.
3. Emergent behavior with model scale.
4. Benefits across commonsense reasoning.
5. Benefits across symbolic reasoning.
6. Robustness across prompt variations.
7. The importance of natural-language intermediate reasoning.