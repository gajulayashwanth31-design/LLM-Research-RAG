---
paper: "Language Models are Few-Shot Learners"
year: 2020
domain: "Large Language Models"
subdomain: "Autoregressive Language Models"
difficulty: "Intermediate"
document_type: "Paper Overview"
keywords:
  - GPT-3
  - Few-Shot Learning
  - In-Context Learning
  - Autoregressive Language Models
  - Scaling
  - Transformer
  - Zero-Shot Learning
  - One-Shot Learning
generated_from: "Original Research Paper"
---

# Paper Overview

## Paper Summary

"Language Models are Few-Shot Learners" introduces GPT-3, a 175-billion-parameter autoregressive language model designed to investigate how increasing model scale affects task performance without task-specific gradient updates.

The central idea of the paper is that sufficiently large language models can perform many tasks directly from natural-language instructions and a small number of demonstrations provided in the input context.

Unlike the conventional pre-training followed by fine-tuning paradigm, GPT-3 is evaluated without updating its parameters for individual downstream tasks.

The model receives a task description and, depending on the evaluation setting, zero, one, or several examples of the task.

The model then generates the desired output through ordinary forward-pass language modeling.

The paper calls this behavior "in-context learning."

GPT-3 is trained as an autoregressive language model and contains 175 billion parameters, approximately an order of magnitude larger than previous non-sparse language models discussed in the paper.

The authors train eight model sizes ranging from 125 million to 175 billion parameters.

This allows them to study how language-model performance changes as model capacity increases.

The experiments cover a broad collection of NLP tasks, including language modeling, cloze tasks, question answering, translation, commonsense reasoning, reading comprehension, natural language inference, and synthetic tasks designed to test rapid adaptation and reasoning.

The paper reports that performance generally improves with model size.

The improvements are particularly noticeable in few-shot settings, where larger models become increasingly capable of learning task patterns from demonstrations in the context.

At the same time, GPT-3 does not solve every task.

The paper identifies weaknesses in areas such as natural language inference, some reading comprehension tasks, common-sense reasoning, and long-form text coherence.

The authors also investigate contamination of evaluation benchmarks caused by training on large web-scale datasets.

The paper concludes that scaling language models can substantially improve task-agnostic few-shot performance, but also emphasizes limitations, methodological concerns, computational costs, bias, misuse risks, and the need for further research.

# Problem Addressed

## Limitations of Task-Specific Fine-Tuning

Prior NLP systems increasingly relied on large-scale pre-training followed by task-specific fine-tuning.

This approach substantially improved performance across many NLP benchmarks.

However, strong performance usually required a labeled dataset containing thousands or even hundreds of thousands of examples for each task.

A separate fine-tuning process was therefore required whenever the desired task changed.

This creates a practical limitation because collecting high-quality labeled data for every possible language task is expensive and sometimes impractical.

The paper argues that humans can often perform a new language task after receiving only a short instruction or a few demonstrations.

The authors therefore investigate whether language models can acquire similar flexibility.

## Task-Specific Dataset Requirement

Fine-tuning requires a new task-specific dataset for every downstream task.

This makes the overall system less flexible.

A model trained for one task does not automatically adapt to another task without additional supervised training.

The paper investigates whether the model can instead infer the desired task from the input itself.

This motivates the study of zero-shot, one-shot, and few-shot learning.

## Generalization Concerns

The paper also discusses concerns about the pre-training plus fine-tuning paradigm.

A large model can absorb a substantial amount of information during pre-training.

However, fine-tuning on a narrow task distribution can cause the model to specialize heavily in that distribution.

This may lead to poor out-of-distribution generalization.

The authors also note that large models may exploit spurious correlations in task-specific datasets.

Such behavior can make benchmark performance appear stronger than actual general-purpose task understanding.

# Motivation

## Human-Like Adaptability

Humans can often understand a new language task from a short natural-language instruction.

In many cases, only a few examples are required.

The paper argues that achieving similar flexibility would make NLP systems more broadly useful.

A system capable of switching between tasks using instructions and examples would not require a separate fine-tuning pipeline for every task.

## Meta-Learning Perspective

The paper frames in-context learning as a form of meta-learning.

During pre-training, the language model develops broad skills and pattern-recognition abilities.

At inference time, the model uses the text provided in its context to rapidly adapt to the desired task.

The parameters are not updated during this inner adaptation process.

Instead, the model conditions its predictions on the task description and demonstrations.

## Scaling Hypothesis

Previous work had shown that increasing language-model capacity often improves performance.

The authors hypothesize that in-context learning ability may also improve with model scale.

They therefore train models ranging from 125 million to 175 billion parameters.

The experiments are designed to determine whether larger models become increasingly capable of performing new tasks directly from context.

# Existing Paradigm

## Pre-training and Fine-Tuning

The traditional paradigm consists of two major stages.

First, a language model is pre-trained on large amounts of unlabeled text.

Second, its parameters are fine-tuned on a labeled dataset for a specific downstream task.

Fine-tuning can produce strong benchmark performance.

However, it requires task-specific data and weight updates.

## Task-Specific Architectures

Earlier NLP approaches often required architectures designed specifically for individual tasks.

The development of pre-trained Transformer language models reduced this requirement.

Models could increasingly be adapted to downstream tasks using the same general architecture.

The remaining limitation was the continued need for task-specific fine-tuning.

## GPT-3's Alternative

GPT-3 investigates whether the need for task-specific gradient updates can be removed.

Instead of modifying model weights, task information is supplied through text.

The model is expected to infer the desired task from the context and generate the appropriate completion.

# In-Context Learning

## Definition

In-context learning refers to the ability of a pretrained language model to perform a task based on information supplied in its input context.

The model receives a task description and optionally one or more examples.

No gradient updates are performed.

The model simply predicts the next tokens conditioned on the supplied context.

## Task Specification Through Text

The input can contain a natural-language description of the task.

For example, a task can be represented by a description followed by examples of inputs and desired outputs.

The model uses the resulting sequence as conditioning information.

This allows different tasks to be represented within the same language-model interface.

## Inner Loop

The paper describes the inference-time adaptation process as the inner loop of meta-learning.

The model parameters remain fixed.

The task-specific information is provided through the input sequence.

The model then produces an answer based on the context.

# Zero-Shot Learning

## Definition

In zero-shot learning, the model receives a natural-language instruction describing the task.

No demonstrations are provided.

The model must determine the desired behavior from the instruction and produce the appropriate output.

## Advantages

Zero-shot learning requires no task-specific examples.

It is therefore highly convenient.

It also avoids directly conditioning on a small set of potentially unrepresentative examples.

## Challenges

Zero-shot learning is the most difficult of the three evaluated in-context settings.

Some tasks have formats that are difficult to infer from instructions alone.

A natural-language description may not fully specify the expected output format.

# One-Shot Learning

## Definition

One-shot learning provides the model with one demonstration in addition to the task description.

The demonstration gives the model an example of the expected input-output relationship.

The model then receives a new input and predicts its output.

## Motivation

The authors distinguish one-shot learning because one example can resemble how humans communicate certain tasks.

A single demonstration can clarify the intended format or behavior.

## Comparison With Zero-Shot

One-shot learning generally performs better than zero-shot learning on many tasks.

However, the improvement varies depending on the task.

The model must still infer the underlying task from extremely limited information.

# Few-Shot Learning

## Definition

Few-shot learning provides several demonstrations of a task in the model's context.

No model parameters are updated.

The demonstrations act as conditioning information.

## Number of Demonstrations

The paper typically uses between approximately 10 and 100 demonstrations, depending on the task and the available context window.

GPT-3 has a context window of 2048 tokens.

The number of demonstrations is therefore limited by the available context length.

## Scaling Behavior

Few-shot performance improves substantially with model size on many tasks.

The paper observes that the gap between zero-shot, one-shot, and few-shot performance often increases with model capacity.

This suggests that larger models make more effective use of contextual demonstrations.

# Fine-Tuning

## Definition

Fine-tuning updates the parameters of a pretrained language model using a supervised dataset for a particular task.

This was the dominant paradigm for achieving strong performance on many NLP benchmarks.

## Advantages

Fine-tuning often produces strong task-specific performance.

It can exploit large amounts of labeled task-specific data.

## Disadvantages

Fine-tuning requires a separate labeled dataset for each task.

It requires gradient updates and additional training.

It can also lead to poor out-of-distribution generalization and exploitation of spurious correlations.

## GPT-3 Evaluation Choice

The main GPT-3 experiments do not fine-tune the model.

The authors focus on zero-shot, one-shot, and few-shot task-agnostic evaluation.

They note that GPT-3 could in principle be fine-tuned, but leave that investigation for future work.

# GPT-3 Architecture

## Autoregressive Transformer

GPT-3 is an autoregressive language model based on the GPT-2 architecture.

It predicts tokens sequentially based on previously observed context.

The model uses a Transformer architecture.

## GPT-2 Architecture Basis

GPT-3 retains the modified initialization, pre-normalization, and reversible tokenization described for GPT-2.

The major architectural scaling occurs through increasing model size.

## Attention Pattern

GPT-3 uses alternating dense and locally banded sparse attention patterns in its Transformer layers.

This attention design is similar to the Sparse Transformer approach described in the paper.

## Context Window

All GPT-3 model sizes use a context window of 2048 tokens.

The context window is important for in-context learning because demonstrations must fit inside the model's input sequence.

# Model Sizes

## Eight Model Configurations

The authors train eight model sizes.

They range from 125 million parameters to 175 billion parameters.

The models are:

- GPT-3 Small: 125M parameters
- GPT-3 Medium: 350M parameters
- GPT-3 Large: 760M parameters
- GPT-3 XL: 1.3B parameters
- GPT-3 2.7B: 2.7B parameters
- GPT-3 6.7B: 6.7B parameters
- GPT-3 13B: 13B parameters
- GPT-3 175B: 175B parameters

The largest model is referred to simply as GPT-3.

## GPT-3 175B

GPT-3 contains 175 billion trainable parameters.

It has 96 Transformer layers.

Its model dimension is 12,288.

It uses 96 attention heads.

The dimension of each attention head is 128.

The feed-forward layer is four times the model dimension.

## Scaling Experiment

Training multiple model sizes allows the authors to study how performance changes as model capacity increases.

The models cover approximately three orders of magnitude in parameter count.

The paper reports relatively smooth scaling behavior across many tasks.

# Training Dataset

## Common Crawl

A large fraction of GPT-3's training data comes from Common Crawl.

The authors note that raw Common Crawl contains nearly a trillion words.

However, unfiltered or lightly filtered Common Crawl has lower average quality than curated datasets.

The authors therefore apply several filtering and deduplication procedures.

## Dataset Filtering

The first major filtering step selects Common Crawl content based on similarity to high-quality reference corpora.

This is intended to improve the average quality of the training data.

## Deduplication

The authors perform fuzzy deduplication at the document level.

Deduplication is performed both within individual datasets and across datasets.

This reduces redundancy and helps preserve the integrity of held-out validation sets.

## Additional Curated Data

The training mixture also includes high-quality reference corpora.

These include:

- WebText2
- Books1
- Books2
- English Wikipedia

The additional datasets increase the diversity and quality of the training mixture.

# Training Data Mixture

## Final Dataset Composition

The training mixture consists of:

- Filtered Common Crawl: 410 billion tokens
- WebText2: 19 billion tokens
- Books1: 12 billion tokens
- Books2: 55 billion tokens
- Wikipedia: 3 billion tokens

The training mixture is intentionally not sampled strictly in proportion to dataset size.

Higher-quality datasets are sampled more frequently.

## Training Weights

The approximate mixture weights reported in the paper are:

- Common Crawl: 60%
- WebText2: 22%
- Books1: 8%
- Books2: 8%
- Wikipedia: 3%

Because the sampling weights are not proportional to dataset size, some datasets are seen multiple times while others are seen less than once.

# Training Process

## Training Tokens

All eight GPT-3 models are trained for a total of 300 billion tokens.

The models differ in parameter count but are trained using the same overall token budget.

## Batch Size

Batch size increases with model size.

The largest GPT-3 model uses a batch size of approximately 3.2 million tokens.

## Learning Rate

The learning rate decreases as model size increases.

GPT-3 175B uses a learning rate of 0.6 × 10^-4.

## Optimization

The models are trained using gradient-based optimization.

The training setup uses large-scale GPU infrastructure.

The largest models require model parallelism to fit within available memory.

## Model Parallelism

The authors use model parallelism both within matrix multiplications and across Transformer layers.

The models are partitioned across GPUs along depth and width dimensions.

This reduces memory requirements and data-transfer costs.

# Scaling Laws

## Validation Loss

The paper observes that language-model performance follows a power-law trend with training compute.

The scaling trend continues over a large increase in compute.

The authors observe only small deviations from the predicted power-law relationship.

## Downstream Performance

Improvements in validation loss correspond to improvements across many downstream language tasks.

This suggests that scaling is not merely improving performance on the training distribution.

Larger models generally achieve stronger zero-shot, one-shot, and few-shot results.

## Meta-Learning Ability

The gap between zero-shot, one-shot, and few-shot performance often increases with model size.

This suggests that larger models may be more proficient at using contextual demonstrations.

# Evaluation Framework

## Evaluation Settings

Every task is evaluated under three primary settings:

- Zero-shot
- One-shot
- Few-shot

The model parameters remain unchanged during evaluation.

## Few-Shot Demonstrations

For few-shot evaluation, examples are sampled from the task's training set.

The examples are inserted into the model context.

The model then receives a new task instance and predicts the completion.

## Context Limitation

The number of demonstrations is limited by the 2048-token context window.

Typically, between 10 and 100 examples can fit depending on the task.

## Prompting

Some tasks use natural-language task descriptions.

The paper also studies task-specific formatting and prompting choices.

Detailed task phrasing and specifications are provided in the paper's appendix.

# Evaluation Tasks

## Language Modeling

GPT-3 is evaluated on traditional language-modeling tasks.

The Penn Tree Bank is used as an important clean language-modeling benchmark because several other datasets had substantial overlap with the training data.

GPT-3 achieves a zero-shot perplexity of 20.5 on PTB.

## Cloze and Completion

The model is evaluated on tasks requiring prediction of missing words or completion of text.

LAMBADA tests long-range dependencies by requiring prediction of the final word of a sentence after reading substantial context.

GPT-3 achieves strong improvements on LAMBADA, especially in the few-shot setting.

## Closed-Book Question Answering

Closed-book question answering evaluates whether the model can answer factual questions using information encoded in its parameters.

The evaluation does not provide external retrieved documents.

The paper evaluates Natural Questions, WebQuestions, and TriviaQA.

GPT-3 improves substantially from zero-shot to few-shot settings on these tasks.

## Translation

GPT-3 is evaluated on translation between English, French, German, and Romanian.

The training data remains predominantly English.

The paper reports that GPT-3 performs substantially better when translating into English than when translating from English into the other studied languages.

Few-shot demonstrations improve translation performance.

## Winograd-Style Tasks

The paper evaluates Winograd schemas and Winogrande.

These tasks require resolving ambiguous references using contextual and commonsense information.

GPT-3 performs strongly on the original Winograd dataset.

Performance on the more difficult Winogrande dataset improves as more demonstrations are provided.

## Common Sense Reasoning

GPT-3 is evaluated on PIQA, ARC, and OpenBookQA.

These datasets test aspects of physical, scientific, and commonsense reasoning.

The model performs competitively on some tasks but remains below strong task-specific systems on others.

## Reading Comprehension

GPT-3 is evaluated on reading comprehension datasets.

Performance is mixed.

Some tasks show strong scaling while others remain difficult even for the largest model.

## SuperGLUE

GPT-3 is evaluated on the SuperGLUE benchmark suite.

The results show that larger models generally improve with additional demonstrations.

However, performance varies considerably across individual tasks.

## Natural Language Inference

GPT-3 is also evaluated on natural language inference tasks.

The paper identifies NLI as an area where GPT-3 remains relatively weak.

ANLI is particularly challenging.

## Synthetic Tasks

The authors design additional tasks specifically to probe in-context learning.

These tasks test abilities such as:

- Word unscrambling
- Symbol manipulation
- Arithmetic
- Novel word usage
- On-the-fly adaptation
- Text synthesis

These experiments are intended to determine whether GPT-3 can rapidly infer task behavior from demonstrations.

# Key Experimental Findings

## Overall Scaling

GPT-3 generally improves as model size increases.

The improvement is observed across zero-shot, one-shot, and few-shot settings.

## Few-Shot Improvement

Few-shot learning often benefits more strongly from scaling than zero-shot learning.

Large models make increasingly effective use of demonstrations.

## Closed-Book Knowledge

GPT-3 can answer broad factual questions without retrieving external documents.

Performance improves smoothly with model size.

## Translation

Few-shot demonstrations substantially improve translation performance.

GPT-3 performs particularly well when translating into English.

## Reasoning

GPT-3 demonstrates useful performance on several reasoning-oriented tasks.

However, its performance is inconsistent.

Strong performance on one reasoning benchmark does not imply general reasoning ability.

## Synthetic Text

GPT-3 can generate long-form text that human evaluators sometimes find difficult to distinguish from human-written text.

The paper evaluates this behavior through human quality assessments of synthetic news articles.

# Data Contamination

## Motivation

Training GPT-3 on large internet-scale datasets creates the possibility that evaluation benchmarks may already appear in the training corpus.

This creates a risk of contamination.

A model could perform well on a benchmark partly because it has encountered similar content during training.

## Detection

The authors search for overlaps between the training data and evaluation datasets.

They construct cleaned versions of benchmarks by conservatively removing potentially contaminated examples.

## 13-Gram Overlap

For many datasets, examples are flagged when they have a 13-gram overlap with the pre-training data.

For shorter examples, the entire example can be considered.

The procedure is intentionally conservative.

## Findings

Potential contamination is found in a number of benchmarks.

For most datasets, however, the difference between original and clean evaluation results is small.

Some datasets require additional caution.

The paper marks certain results with an asterisk where contamination may have affected the evaluation.

## Methodological Importance

The contamination study highlights a major challenge in evaluating large language models trained on broad web corpora.

Benchmark performance must be interpreted together with knowledge of training-data overlap.

# Limitations

## Text Coherence

GPT-3 can generate high-quality text but sometimes loses coherence over sufficiently long passages.

Generated documents may repeat ideas, contradict themselves, or contain non-sequitur passages.

## Common Sense Physics

The paper reports that GPT-3 has difficulty with certain common-sense physical reasoning questions.

Good benchmark performance in one domain does not guarantee robust physical understanding.

## Weak Task Performance

GPT-3 performs poorly on some comparison and inference tasks.

Examples discussed in the paper include WIC and ANLI.

Some reading comprehension tasks also remain challenging.

## Calibration

The paper notes that GPT-3 is not necessarily well calibrated on novel inputs.

Its performance can have substantially higher variance than human performance.

## Interpretability

GPT-3's decisions are not easily interpretable.

The model's internal reasoning process is difficult to inspect directly.

## Bias

GPT-3 inherits biases present in its training data.

This can result in stereotyped or prejudiced generated content.

## Computational Cost

Training a 175-billion-parameter model requires enormous computational resources.

Large-scale model training therefore has significant infrastructure and energy requirements.

# Broader Impacts

## Beneficial Applications

The paper identifies several possible beneficial applications of language models.

Examples include:

- Writing assistance
- Code completion
- Grammar assistance
- Search-engine response improvement
- Question answering
- Game narrative generation

## Misuse

Improved text generation can also lower barriers to harmful activities.

The paper discusses potential misuse including:

- Misinformation
- Spam
- Phishing
- Social engineering
- Fraudulent academic writing
- Abuse of legal or governmental processes

## Synthetic Text

Because GPT-3 can produce text that is sometimes difficult for humans to distinguish from human-written text, the paper identifies synthetic content as a significant societal concern.

## Fairness and Representation

The paper discusses how biases in training data can appear in model outputs.

Bias, fairness, and representation are therefore important considerations when deploying large language models.

## Energy Usage

The paper also discusses the energy efficiency of increasingly large language models.

The computational cost of scaling is an important consideration alongside model capability.

# Comparison With Previous Models

## GPT-2

GPT-3 builds on the GPT-2 architecture.

The major difference is scale.

GPT-3 increases model size dramatically and evaluates whether this scaling produces stronger in-context learning.

## BERT

BERT is based on a bidirectional Transformer encoder and was primarily evaluated using pre-training followed by task-specific fine-tuning.

GPT-3 instead uses an autoregressive Transformer and investigates task performance without fine-tuning.

## Fine-Tuned Systems

GPT-3's few-shot results are compared against systems trained using task-specific fine-tuning.

The paper shows that GPT-3 can approach or sometimes exceed prior fine-tuned systems on certain tasks.

However, it remains substantially weaker on other tasks.

# Overall Significance

## Scaling as a Capability Driver

One of the main findings is that increasing language-model scale can substantially improve task performance.

The relationship is observed across many different tasks and evaluation settings.

## In-Context Learning

GPT-3 demonstrates that a large autoregressive language model can perform many tasks through conditioning on textual examples without gradient updates.

This provides evidence that useful task adaptation can occur entirely within the model context.

## Unified Task Interface

Tasks can be represented as sequences of text.

This provides a common interface for very different NLP problems.

Translation, question answering, classification, reasoning, and generation can all be represented as language-model completion problems.

## Remaining Challenges

The paper does not claim that scaling completely solves NLP.

GPT-3 continues to show weaknesses in reasoning, coherence, calibration, fairness, and robustness.

The authors therefore present scaling and in-context learning as important progress rather than a complete solution.

# Conclusion

GPT-3 demonstrates that scaling autoregressive language models can substantially improve zero-shot, one-shot, and few-shot performance.

The model contains 175 billion parameters and is trained on 300 billion tokens from a mixture of filtered Common Crawl, WebText2, Books1, Books2, and Wikipedia.

Unlike traditional fine-tuning approaches, the main experiments do not update model parameters for individual tasks.

Instead, task descriptions and demonstrations are supplied directly through the context.

The results show strong and often smoothly scaling performance across a wide range of NLP tasks.

The strongest gains are frequently observed in few-shot settings.

At the same time, GPT-3 has important limitations, including weaknesses on several reasoning and comprehension tasks, long-form coherence problems, data contamination concerns, interpretability limitations, bias, and substantial computational requirements.

The paper therefore establishes large-scale in-context learning as a major capability of autoregressive language models while also identifying important areas for future research.