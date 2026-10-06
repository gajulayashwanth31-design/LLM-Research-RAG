---
paper: "Language Models are Few-Shot Learners"
year: 2020
domain: "Large Language Models"
subdomain: "Autoregressive Language Models"
difficulty: "Intermediate"
document_type: "Limitations"
keywords:
  - GPT-3
  - Limitations
  - Data Contamination
  - Bias
  - Interpretability
  - Calibration
  - Computational Cost
generated_from: "Original Research Paper"
---

# Text Generation Limitations

## Long-Range Coherence

GPT-3 can lose coherence when generating sufficiently long passages.

Generated text may contain contradictions or unrelated statements.

## Repetition

GPT-3 samples can sometimes repeat semantic content at the document level.

# Reasoning Limitations

## Common Sense Physics

The paper reports difficulty with some common-sense physical reasoning questions.

Strong performance on certain benchmark datasets does not imply complete physical understanding.

## Comparison Tasks

GPT-3 performs poorly on some comparison tasks.

Some tasks remain near chance even in one-shot or few-shot settings.

# Natural Language Inference Limitations

## ANLI

ANLI remains particularly difficult for GPT-3.

Few-shot performance does not consistently approach strong task-specific systems.

# Reading Comprehension

## Task Variation

GPT-3 performs strongly on some reading-comprehension datasets but poorly on others.

The paper specifically identifies datasets such as RACE and QuAC as challenging.

# Calibration

## Prediction Reliability

GPT-3 is not necessarily well calibrated on novel inputs.

The paper observes greater variance in model performance than in human performance on some benchmarks.

# Interpretability

## Black-Box Behavior

GPT-3's decisions are not easily interpretable.

The large number of parameters and distributed representations make direct explanation of individual predictions difficult.

# Bias

## Training Data Bias

GPT-3 inherits biases present in the data used to train it.

These biases can influence generated content.

## Stereotyped Content

The paper highlights the possibility of generating stereotyped or prejudiced content.

# Data Contamination

## Benchmark Overlap

Training on large internet-scale corpora can introduce overlap with evaluation benchmarks.

This can make benchmark results difficult to interpret.

## Filtering Limitations

The authors attempted to remove overlaps but a bug resulted in only partial removal.

Retraining the model was not feasible because of the cost.

# Computational Cost

## Training Resources

Training the largest GPT-3 model requires substantial computational resources.

Large-scale models therefore have significant infrastructure requirements.

## Energy Usage

The paper discusses energy efficiency as part of the broader impacts of large language models.

# Evaluation Limitations

## Benchmark Dependence

Performance on individual benchmarks does not necessarily establish general language understanding.

## Contamination

Some benchmark results may be affected by training-data overlap.

## Task Formatting

Few-shot performance can depend on the exact way task instructions and demonstrations are formatted.

# Broader Impact Risks

## Misinformation

Highly capable text generation can potentially increase the scale and effectiveness of misinformation.

## Spam

Language models can reduce the cost of generating large quantities of text.

## Phishing

Improved text generation can potentially assist phishing and social-engineering activities.

## Fraudulent Academic Writing

The paper identifies fraudulent academic writing as a potential misuse.

## Social Engineering

Generated text can potentially be used to construct convincing social-engineering messages.

# Generalization

## Distribution Shift

GPT-3 can perform strongly on some tasks while struggling when task formats or distributions differ substantially from those represented during training.

# Future Research

## Improved Evaluation

More robust evaluation methods are required to account for benchmark contamination and distinguish memorization from generalization.

## Better Reasoning

Future systems need stronger reasoning and common-sense capabilities.

## Safer Deployment

The risks associated with high-quality synthetic text require additional study and mitigation.