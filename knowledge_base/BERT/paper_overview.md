---
paper: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
year: 2019
domain: "Large Language Models"
subdomain: "Transformer Architecture"
difficulty: "Intermediate"
document_type: "Paper Overview"
keywords:
  - BERT
  - Bidirectional Transformers
  - Language Model Pre-training
  - Masked Language Modeling
  - Next Sentence Prediction
  - Fine-tuning
  - Natural Language Understanding
generated_from: "Original Research Paper"
---

# Paper Overview

## Paper Summary

BERT stands for Bidirectional Encoder Representations from Transformers.

The paper introduces BERT as a language representation model that pre-trains deep bidirectional representations from unlabeled text.

Unlike earlier language representation models that use unidirectional language models, BERT jointly conditions on both left and right context in all layers.

The resulting pre-trained model can be fine-tuned with only one additional output layer for a wide range of downstream natural language processing tasks.

The paper demonstrates that BERT can achieve strong results without requiring substantial task-specific architectural modifications.

The authors report new state-of-the-art results on eleven NLP tasks.

These tasks include sentence-level and token-level tasks such as natural language inference, question answering, sentiment analysis, and named entity recognition.

## Main Idea

The central idea of BERT is to combine large-scale unsupervised pre-training with downstream task-specific fine-tuning.

The model first learns general language representations from unlabeled text.

It is then initialized with the pre-trained parameters and fine-tuned using labeled data from a particular downstream task.

The same pre-trained BERT model can therefore be adapted to multiple tasks.

The major architectural distinction is that BERT uses a bidirectional Transformer encoder.

The major training distinction is that BERT uses two pre-training objectives:

1. Masked Language Modeling
2. Next Sentence Prediction

# Problem Addressed

## Language Representation Learning

Many NLP tasks benefit from representations learned from large amounts of unlabeled text.

Examples include:

- Natural language inference
- Paraphrasing
- Question answering
- Named entity recognition
- Sentiment analysis

Instead of learning language representations separately for every downstream task, language model pre-training attempts to learn general representations that can be transferred to multiple tasks.

## Existing Pre-training Approaches

Before BERT, two major strategies were commonly used for applying pre-trained language representations to downstream tasks.

These were:

1. Feature-based approaches
2. Fine-tuning approaches

## Feature-Based Approaches

Feature-based methods use pre-trained representations as additional features inside a task-specific architecture.

ELMo is an example of this approach.

The downstream task still contains a task-specific model architecture.

The pre-trained representations are incorporated into that architecture as features.

## Fine-Tuning Approaches

Fine-tuning approaches initialize a model using pre-trained parameters and then fine-tune those parameters directly on the downstream task.

OpenAI GPT is an example discussed in the paper.

Fine-tuning approaches require fewer task-specific parameters than feature-based approaches.

## Limitation of Existing Language Models

The paper identifies a major limitation in the language models used for pre-training.

Standard language models are unidirectional.

A left-to-right language model predicts a token using only previous tokens.

A right-to-left language model predicts a token using only tokens on its right.

This restricts the context available during pre-training.

## Problem for Token-Level Tasks

The unidirectional restriction can be especially harmful for token-level tasks.

Question answering is an important example.

When answering a question using a passage, a token representation may need information from both directions.

A model that can only use left context cannot fully exploit the surrounding context.

## Problem with Simple Bidirectional Concatenation

One possible solution is to train separate left-to-right and right-to-left models and concatenate their representations.

ELMo uses this type of approach.

However, the paper describes this as a shallow concatenation of independently trained models.

The authors argue that a deep bidirectional representation is more powerful.

## BERT's Solution

BERT removes the unidirectionality constraint by using a masked language model objective.

Instead of predicting every token from only its left context, BERT randomly masks some input tokens.

The model then predicts the original values of the masked tokens.

Because the surrounding tokens can provide information from both directions, this enables deep bidirectional pre-training.

# Motivation

## Need for Bidirectional Context

Natural language understanding often requires information from both sides of a token.

A word can have different meanings depending on its surrounding context.

A bidirectional representation can incorporate information from both left and right context.

## Need for General-Purpose Representations

The goal is to learn a representation that can be transferred to many different NLP tasks.

Rather than designing a completely different architecture for each task, the same pre-trained representation should provide a strong starting point.

## Need for Minimal Task-Specific Architecture

The paper aims to reduce the amount of task-specific architecture engineering required after pre-training.

BERT uses a unified architecture across downstream tasks.

Most tasks require only an additional output layer.

# Main Contributions

## Contribution 1: Bidirectional Pre-training

The paper demonstrates the importance of deep bidirectional pre-training.

BERT uses masked language modeling to enable bidirectional representations.

This differs from OpenAI GPT's unidirectional language model.

It also differs from ELMo's shallow combination of independently trained left-to-right and right-to-left language models.

## Contribution 2: Reduced Task-Specific Engineering

The paper shows that pre-trained representations can reduce the need for heavily engineered task-specific architectures.

BERT uses a unified Transformer-based architecture across different downstream tasks.

## Contribution 3: State-of-the-Art Results

The paper reports state-of-the-art results on eleven NLP tasks.

Examples include:

- GLUE
- MultiNLI
- SQuAD v1.1
- SQuAD v2.0
- SWAG
- CoNLL-2003 NER

# Related Work

## Unsupervised Feature-Based Approaches

The paper describes a long history of learning general-purpose word representations.

Earlier methods include:

- Non-neural word representations
- Neural word embeddings
- Context-sensitive representations

Pre-trained word embeddings improved NLP systems compared with embeddings learned from scratch.

## Word Embeddings

Earlier language representation approaches learned representations at the word level.

Language modeling objectives and other objectives were used to obtain word representations.

These approaches were later extended to sentence and paragraph representations.

## ELMo

ELMo produces contextual representations using separate left-to-right and right-to-left language models.

The representations from the two directions are combined.

ELMo is feature-based rather than deeply bidirectional.

The contextual representations are incorporated into task-specific architectures.

## Fine-Tuning Language Models

More recent work pre-trained sentence or document encoders using unlabeled text and then fine-tuned them on downstream tasks.

OpenAI GPT is one example.

GPT uses a left-to-right Transformer language model.

## Transfer Learning

The paper also discusses transfer learning in supervised settings.

Transfer learning had already demonstrated benefits in areas such as natural language inference and machine translation.

Computer vision had similarly demonstrated the usefulness of transferring representations from large pre-trained models.

# BERT Framework

## Two-Stage Framework

BERT consists of two major stages:

1. Pre-training
2. Fine-tuning

## Pre-training

During pre-training, BERT is trained using unlabeled text.

The model learns general language representations through two pre-training tasks.

These tasks are:

- Masked Language Modeling
- Next Sentence Prediction

## Fine-tuning

During fine-tuning, the pre-trained BERT parameters are used to initialize a downstream model.

The model is then trained using labeled data from the downstream task.

All BERT parameters are fine-tuned.

## Separate Fine-Tuned Models

Each downstream task receives a separate fine-tuned model.

However, the models are all initialized from the same pre-trained BERT parameters.

## Unified Architecture

A distinctive feature of BERT is the similarity between the pre-training architecture and the downstream architecture.

Apart from output layers, the same basic architecture is used.

This allows BERT to be adapted to different tasks with minimal architectural modification.

# Model Architecture

## Transformer Encoder

BERT is a multi-layer bidirectional Transformer encoder.

Its architecture is based on the original Transformer implementation.

The model consists of multiple Transformer blocks.

The paper denotes:

- L = number of layers
- H = hidden size
- A = number of self-attention heads

## BERTBASE

BERTBASE uses:

- 12 Transformer layers
- Hidden size of 768
- 12 attention heads
- 110 million parameters

## BERTLARGE

BERTLARGE uses:

- 24 Transformer layers
- Hidden size of 1024
- 16 attention heads
- 340 million parameters

## Feed-Forward Size

The feed-forward/filter size is set to 4H.

For BERTBASE:

4 × 768 = 3072

For BERTLARGE:

4 × 1024 = 4096

## BERT and GPT

BERTBASE was chosen to have approximately the same model size as OpenAI GPT.

This allows the authors to compare the two approaches.

The major architectural difference is the attention pattern.

BERT uses bidirectional self-attention.

GPT uses constrained self-attention where each token can only attend to tokens on its left.

# Input and Output Representation

## Single Sentence

BERT can represent a single sentence as one token sequence.

The sequence begins with `[CLS]`.

The final hidden representation corresponding to `[CLS]` can be used for classification.

## Sentence Pair

BERT can also represent two text segments as a single sequence.

For example:

- Question + Answer
- Premise + Hypothesis
- Question + Passage

The two segments are packed into one sequence.

## Definition of Sentence

In the paper, a "sentence" does not necessarily mean a grammatical sentence.

It can represent an arbitrary span of contiguous text.

## Definition of Sequence

A sequence refers to the input token sequence given to BERT.

It can contain:

- One sentence
- Two sentences packed together

## WordPiece

BERT uses WordPiece embeddings.

The vocabulary contains 30,000 tokens.

WordPiece allows text to be represented using subword units.

## [CLS]

`[CLS]` is a special classification token.

It is placed at the beginning of every input sequence.

The final hidden representation corresponding to `[CLS]` is denoted by C.

For classification tasks, C is used as the aggregate sequence representation.

## [SEP]

`[SEP]` is a special separator token.

It separates two text segments.

For example:

`[CLS] Sentence A [SEP] Sentence B [SEP]`

## Segment Embeddings

Each token receives a learned segment embedding.

The segment embedding indicates whether the token belongs to:

- Sentence A
- Sentence B

## Position Embeddings

Each token also receives a position embedding.

This provides information about the token's position in the sequence.

## Token Embeddings

Each token receives its token embedding.

## Combined Input Representation

The input representation of each token is constructed by summing:

- Token embedding
- Segment embedding
- Position embedding

# Pre-training

## Purpose of Pre-training

The purpose of pre-training is to learn general language representations from unlabeled text.

The model is trained before being adapted to downstream tasks.

## Pre-training Tasks

BERT uses two unsupervised pre-training tasks:

1. Masked Language Modeling
2. Next Sentence Prediction

# Masked Language Modeling

## Motivation

A conventional bidirectional language model cannot directly predict a word while simultaneously allowing the word to see itself through both directions.

The model could indirectly access the target token.

This would make the prediction task trivial.

## Masking Solution

BERT randomly masks some input tokens.

The model then predicts the original vocabulary identity of the masked tokens.

The model therefore has to infer the missing information from its context.

## Bidirectional Context

Because the model can use context on both sides of a masked token, MLM enables deep bidirectional representations.

## Masking Rate

BERT selects 15% of WordPiece tokens in each sequence for prediction.

## 80/10/10 Strategy

For a selected token:

- 80% of the time it is replaced with `[MASK]`
- 10% of the time it is replaced with a random token
- 10% of the time it remains unchanged

## Reason for Mixed Masking

The `[MASK]` token appears during pre-training but does not appear during downstream fine-tuning.

This creates a mismatch between pre-training and fine-tuning.

The mixed masking strategy reduces this mismatch.

## `[MASK]` Replacement

In the majority of cases, the selected token is replaced with `[MASK]`.

Example:

`my dog is hairy`

becomes:

`my dog is [MASK]`

The model predicts:

`hairy`

## Random Replacement

In 10% of selected cases, the target token is replaced with a random token.

Example:

`my dog is hairy`

may become:

`my dog is apple`

The model is still trained to predict the original token.

## Unchanged Token

In 10% of selected cases, the target token remains unchanged.

The model is still trained to predict the target token.

## Prediction

The final hidden representation corresponding to the selected position is passed through an output softmax over the vocabulary.

## Training Objective

The model predicts the original token using cross-entropy loss.

## MLM Trade-off

Only 15% of tokens are predicted during each training batch.

A conventional left-to-right language model predicts every token.

Therefore, MLM can require more pre-training steps to converge.

The paper reports that MLM converges somewhat slower than a left-to-right model.

However, the empirical improvements from MLM outweigh the increased training cost.

# Next Sentence Prediction

## Motivation

Many downstream tasks require understanding relationships between two sentences.

Examples include:

- Question answering
- Natural language inference

A standard language model does not directly train the model to understand relationships between two sentence segments.

## NSP Objective

BERT introduces a binary next sentence prediction task.

The task determines whether sentence B is the actual next sentence following sentence A.

## Positive Example

50% of training examples contain:

Sentence A

followed by

The actual next sentence B.

The label is:

`IsNext`

## Negative Example

50% of training examples contain:

Sentence A

followed by

A randomly selected sentence from the corpus.

The label is:

`NotNext`

## [CLS] Representation

The final hidden representation C corresponding to `[CLS]` is used for NSP prediction.

## Purpose of NSP

NSP provides a pre-training signal related to relationships between sentence pairs.

The paper reports that NSP is beneficial for downstream question answering and natural language inference.

# Pre-training Data

## BooksCorpus

The first component of the pre-training corpus is BooksCorpus.

It contains approximately:

800 million words.

## English Wikipedia

The second component is English Wikipedia.

The paper uses approximately:

2,500 million words.

## Total Corpus

The combined corpus contains approximately:

3.3 billion words.

## Wikipedia Processing

For Wikipedia, the authors extract text passages.

They ignore:

- Lists
- Tables
- Headers

## Document-Level Corpus

The authors emphasize that a document-level corpus is important.

A document-level corpus allows the model to obtain long contiguous sequences.

The authors contrast this with a shuffled sentence-level corpus such as the Billion Word Benchmark.

## Importance of Contiguous Text

Long contiguous sequences are useful for generating the sentence pairs required by the pre-training procedure.

# Pre-training Input Construction

## Sampling Text

Each training input sequence is generated by sampling two spans of text from the corpus.

The paper refers to these spans as "sentences."

They can be much longer than ordinary linguistic sentences.

They can also be shorter.

## Sentence A

The first sampled span receives the segment A embedding.

## Sentence B

The second sampled span receives the segment B embedding.

## NSP Sampling

50% of the time:

B is the actual next span following A.

50% of the time:

B is a random span from the corpus.

## Maximum Sequence Length

The combined length of the two spans is at most 512 tokens.

## WordPiece Before Masking

The input is first processed using WordPiece tokenization.

The MLM masking procedure is then applied.

## Masking

15% of token positions are selected uniformly for prediction.

No special consideration is given to partial WordPiece tokens.

# Pre-training Configuration

## Batch Size

The training batch contains:

256 sequences.

With sequences of up to 512 tokens, this corresponds to:

256 × 512 = 128,000 tokens per batch.

## Training Steps

BERT is trained for:

1,000,000 steps.

The paper states that this corresponds to approximately 40 epochs over the 3.3 billion word corpus.

## Optimizer

BERT uses Adam.

## Learning Rate

The learning rate is:

1e-4.

## Adam Parameters

The paper uses:

β1 = 0.9

β2 = 0.999

## Weight Decay

The L2 weight decay is:

0.01

## Learning Rate Warmup

The learning rate is warmed up during the first:

10,000 steps.

## Learning Rate Decay

After warmup, the learning rate is linearly decayed.

## Dropout

A dropout probability of:

0.1

is used on all layers.

## Activation Function

BERT uses GELU rather than the standard ReLU.

The choice follows OpenAI GPT.

## Training Loss

The training loss is the sum of:

- Mean masked language model likelihood
- Mean next sentence prediction likelihood

# Computational Requirements

## BERTBASE Training

BERTBASE was trained using:

- 4 Cloud TPU machines
- 16 TPU chips total

The pre-training took approximately:

4 days.

## BERTLARGE Training

BERTLARGE was trained using:

- 16 Cloud TPU machines
- 64 TPU chips total

The pre-training also took approximately:

4 days.

# Sequence Length Strategy

## Computational Problem

Longer sequences are disproportionately expensive because Transformer attention has quadratic complexity with respect to sequence length.

## Short Sequence Training

BERT is trained using sequence length:

128

for 90% of the training steps.

## Long Sequence Training

Sequence length:

512

is used for the remaining 10% of training steps.

## Reason

The shorter sequences reduce training cost.

The final 10% of training uses longer sequences so that the model can learn positional embeddings for longer inputs.

# Fine-tuning

## Fine-tuning Procedure

Fine-tuning starts from the pre-trained BERT parameters.

The model is then trained using labeled downstream-task data.

## Parameter Updates

All BERT parameters are fine-tuned.

## Task-Specific Output Layer

Each task adds a task-specific output layer.

The number of newly introduced parameters is therefore relatively small.

## Single-Sentence Tasks

For a single-sentence task, the sentence is represented as a BERT sequence.

The `[CLS]` representation is generally used for classification.

## Sentence-Pair Tasks

For a sentence-pair task, the two sentences are packed into one sequence.

The segment embeddings distinguish sentence A from sentence B.

## Token-Level Tasks

For token-level tasks, the representations of individual tokens are used.

Examples include:

- Named entity recognition
- Question answering

## Classification Tasks

For classification tasks, the final hidden representation of `[CLS]` is passed to a classification layer.

## Question Answering

For question answering, the question and passage are packed into a single sequence.

The model predicts the start and end positions of the answer span.

# Fine-tuning Hyperparameters

## Batch Size

The authors find the following batch sizes generally useful:

- 16
- 32

## Learning Rate

The following learning rates are considered:

- 5e-5
- 3e-5
- 2e-5

## Number of Epochs

The following number of epochs are considered:

- 2
- 3
- 4

## Dropout

Dropout remains:

0.1

## Dataset Size

Large datasets are less sensitive to hyperparameter selection.

Small datasets are more sensitive.

## Hyperparameter Search

Because fine-tuning is relatively fast, the authors recommend searching over the possible hyperparameters and selecting the model with the best development-set performance.

# Downstream Task Representation

## General Pattern

The same BERT architecture can support different task formats.

The paper maps downstream inputs to the same sentence-A/sentence-B representation.

## Paraphrasing

For paraphrasing:

Sentence A = first sentence

Sentence B = second sentence

## Natural Language Inference

For entailment:

Sentence A = hypothesis/premise component

Sentence B = corresponding paired sentence

## Question Answering

For question answering:

Sentence A = question

Sentence B = passage

## Text Classification

For single-text classification:

Sentence A = input text

Sentence B = empty

## Sequence Tagging

For sequence tagging, token representations are passed to a token-level classifier.

# GLUE Benchmark

## Overview

GLUE is a collection of diverse natural language understanding tasks.

BERT is evaluated on multiple GLUE datasets.

## MNLI

MNLI stands for Multi-Genre Natural Language Inference.

The task uses sentence pairs.

The model predicts whether the second sentence is:

- Entailment
- Contradiction
- Neutral

## QQP

QQP stands for Quora Question Pairs.

The task determines whether two questions are semantically equivalent.

## QNLI

QNLI is a question-answering-derived natural language inference task.

The task uses question-sentence pairs.

The model determines whether the sentence contains the answer to the question.

## SST-2

SST-2 is a binary sentiment classification task.

The inputs are sentences from movie reviews.

The goal is to classify sentiment.

## CoLA

CoLA stands for Corpus of Linguistic Acceptability.

The task determines whether an English sentence is linguistically acceptable.

## STS-B

STS-B measures semantic textual similarity.

Sentence pairs receive similarity scores from 1 to 5.

## MRPC

MRPC stands for Microsoft Research Paraphrase Corpus.

The task determines whether two sentences are semantically equivalent.

## RTE

RTE stands for Recognizing Textual Entailment.

It is a binary entailment task.

It contains substantially less training data than MNLI.

## WNLI

WNLI stands for Winograd Natural Language Inference.

The paper notes issues with the construction of this dataset.

The authors therefore exclude it from their main comparison with OpenAI GPT and predict the majority class.

# GLUE Fine-tuning

## Input Representation

For GLUE tasks, a single sentence or sentence pair is represented using the standard BERT input representation.

## Classification Representation

The final hidden vector corresponding to `[CLS]` is used as the aggregate representation.

## Classification Parameters

The classification layer uses:

W ∈ R^(K × H)

where:

K = number of labels

H = hidden size

## Classification Loss

The model uses a standard classification loss based on:

log(softmax(CW^T))

# GLUE Results

## Overall Result

BERTLARGE achieves a GLUE score of:

80.5

This represents a substantial improvement over the previous state of the art reported in the paper.

## MNLI

BERT obtains a strong improvement on the MNLI task.

The paper reports:

86.7% accuracy on the matched development setting.

## Comparison with OpenAI GPT

The paper reports that BERTLARGE achieves a GLUE score of 80.5.

OpenAI GPT is reported at 72.8 on the official leaderboard at the time of writing.

## Effect of Model Size

BERTLARGE significantly outperforms BERTBASE across the evaluated GLUE tasks.

The improvement is particularly notable for tasks with limited training data.

# SQuAD v1.1

## Dataset

SQuAD v1.1 contains approximately:

100,000 question-answer pairs.

The questions are associated with passages from Wikipedia.

## Task

Given:

- A question
- A passage

the model must predict the answer text span.

## Input Format

The question is assigned the A embedding.

The passage is assigned the B embedding.

Both are packed into a single sequence.

## Start Vector

A learned start vector S is introduced during fine-tuning.

## End Vector

A learned end vector E is introduced during fine-tuning.

## Start Probability

The probability that token i is the start of the answer is computed from:

S · Ti

followed by a softmax over the tokens in the paragraph.

## End Probability

An analogous procedure is used for the answer end position.

## Span Score

A candidate span from position i to position j receives the score:

S · Ti + E · Tj

The maximum-scoring valid span is selected.

## Training Objective

The training objective is the sum of the log-likelihoods of the correct start and end positions.

## Reported Result

The paper reports that BERT achieves substantial improvements over previous systems.

The BERTLARGE single model with additional TriviaQA fine-tuning achieves:

85.1 EM

91.8 F1

The ensemble achieves:

87.4 EM

93.2 F1

# SQuAD v2.0

## Difference from SQuAD v1.1

SQuAD v2.0 includes questions that do not have an answer in the passage.

## No-Answer Representation

The model represents a question with no answer using the `[CLS]` token.

The start and end positions are both assigned to `[CLS]`.

## Null Score

The no-answer score is computed from:

S · C + E · C

where C is the final hidden representation of `[CLS]`.

## Answer Score

The best non-null answer span is compared against the no-answer score.

## Threshold

A threshold τ is selected using the development set.

A non-null answer is predicted when its score exceeds the no-answer score by the threshold.

## Result

BERTLARGE achieves:

80.0 EM

83.1 F1

on the SQuAD v2.0 test set in the paper.

# SWAG

## Dataset

SWAG stands for:

Situations With Adversarial Generations.

The dataset contains approximately:

113,000 sentence-pair completion examples.

## Task

Given a sentence, the model selects the most plausible continuation from four choices.

## Input Construction

For each candidate continuation, the original sentence and candidate continuation are represented as:

Sentence A + Sentence B

## Classification

The `[CLS]` representation is used to produce a score for each candidate.

The scores are normalized using a softmax layer.

## Result

BERTLARGE achieves:

86.6% development accuracy

86.3% test accuracy

The paper reports substantial improvements over the compared baselines.

# CoNLL-2003 Named Entity Recognition

## Task

The CoNLL-2003 task evaluates named entity recognition.

The task requires token-level predictions.

## Input

BERT uses a case-preserving WordPiece model.

The maximum available document context is included.

## Output

The representation of the first sub-token is used as the input to the token-level classifier.

## Fine-tuning Result

BERTLARGE achieves:

96.6 development F1

92.8 test F1

## Feature-Based Result

The authors also evaluate a feature-based approach.

Different representations from BERT are extracted without fine-tuning all BERT parameters.

## Best Feature-Based Representation

Concatenating representations from the top four hidden layers performs best among the feature-based approaches reported.

Its performance is close to full fine-tuning.

# Comparison with Existing Models

## BERT vs OpenAI GPT

BERT and GPT are both fine-tuning approaches.

However, their pre-training architectures differ.

## GPT

GPT uses:

- Left-to-right Transformer
- Unidirectional language modeling
- BooksCorpus

## BERT

BERT uses:

- Bidirectional Transformer
- Masked language modeling
- Next sentence prediction
- BooksCorpus + Wikipedia

## Training Corpus Difference

GPT uses approximately:

800M words from BooksCorpus.

BERT uses:

800M words from BooksCorpus

plus

2,500M words from Wikipedia.

## Special Token Difference

GPT introduces `[SEP]`, `[CLS]`, and sentence A/B embeddings during fine-tuning.

BERT learns these components during pre-training.

## Batch Size Difference

GPT uses a batch size of approximately:

32,000 words.

BERT uses:

128,000 words.

## Fine-tuning Learning Rate

GPT uses the same learning rate of:

5e-5

for its fine-tuning experiments.

BERT selects a task-specific learning rate from a set of candidate values.

## Core BERT Argument

The authors argue that bidirectionality and the two pre-training tasks account for the majority of BERT's empirical improvements.

# BERT vs ELMo

## ELMo Architecture

ELMo uses independently trained:

- Left-to-right LSTM
- Right-to-left LSTM

The resulting representations are combined.

## BERT Architecture

BERT uses a bidirectional Transformer.

Both left and right context are jointly available throughout the representation.

## Feature-Based vs Fine-Tuning

ELMo is primarily a feature-based approach.

BERT is a fine-tuning approach.

## Representation Difference

ELMo combines independently trained directional representations.

BERT learns a single deep bidirectional representation.

# Ablation Studies

## Purpose

The paper performs ablation studies to understand which components of BERT are responsible for its performance.

The experiments investigate:

- Next Sentence Prediction
- Bidirectionality
- Model size
- Fine-tuning versus feature-based approaches
- Number of training steps
- Masking strategies

# Effect of Pre-training Tasks

## No NSP

The first ablation removes the Next Sentence Prediction task.

The model remains bidirectional and uses MLM.

## LTR and No NSP

The second ablation removes both NSP and bidirectional MLM.

The model instead uses a left-to-right language model.

## Results

Removing NSP hurts performance on several tasks.

The paper reports decreases on:

- QNLI
- MNLI
- SQuAD

## Bidirectional vs Left-to-Right

The left-to-right model performs worse than the bidirectional MLM model across the evaluated tasks.

The performance difference is particularly large on tasks such as MRPC and SQuAD.

## SQuAD Explanation

A left-to-right model does not have access to right-side context when producing token representations.

This makes token-level question answering more difficult.

## BiLSTM Addition

The authors add a randomly initialized BiLSTM on top of the left-to-right model.

This improves the SQuAD results.

However, the results remain substantially worse than the bidirectional pre-trained models.

The BiLSTM also hurts performance on GLUE tasks.

# Effect of Model Size

## Experiment

The authors vary:

- Number of layers
- Hidden size
- Number of attention heads

while keeping other training settings consistent.

## Main Finding

Larger BERT models consistently improve downstream accuracy.

The improvement occurs across the evaluated datasets.

## Small Dataset Observation

The improvement is notable even for datasets with relatively little labeled training data.

## BERTBASE

BERTBASE contains:

110M parameters.

## BERTLARGE

BERTLARGE contains:

340M parameters.

## Larger Models

The experiments show that increasing the model size can continue to improve performance.

# Fine-tuning vs Feature-Based Approach

## Fine-tuning Approach

The standard BERT approach adds a task-specific output layer.

All BERT parameters are then fine-tuned jointly.

## Feature-Based Approach

The feature-based approach extracts fixed representations from BERT.

Those representations are then provided to another model.

## Why Feature-Based Methods Can Be Useful

The paper identifies two advantages.

First, not all tasks are easily represented by a Transformer encoder architecture.

Such tasks may require an additional task-specific architecture.

Second, expensive representations can be pre-computed once.

This can make it cheaper to run multiple experiments using the same representations.

## NER Experiment

The authors compare fine-tuning and feature-based approaches on CoNLL-2003 NER.

## Fine-tuning Result

BERTLARGE:

96.6 Dev F1

92.8 Test F1

BERTBASE:

96.4 Dev F1

92.4 Test F1

## Feature-Based Results

The paper evaluates:

- Embeddings
- Second-to-last hidden layer
- Last hidden layer
- Weighted sum of last four hidden layers
- Concatenation of last four hidden layers
- Weighted sum of all 12 layers

## Best Feature-Based Method

Concatenating the last four hidden layers produces the strongest feature-based result reported.

It reaches:

96.1 Dev F1

This is only 0.3 F1 below the fine-tuned BERTLARGE result on the development set.

## Conclusion

BERT can be useful under both:

- Fine-tuning
- Feature-based transfer

# Effect of Number of Training Steps

## Question

The authors investigate whether BERT really requires the large amount of pre-training used in the main experiments.

## 500K vs 1M Steps

BERTBASE trained for 1M steps achieves almost:

1.0 percentage point

additional MNLI development accuracy compared with 500K steps.

## Conclusion

The large amount of pre-training contributes meaningfully to downstream performance.

# MLM vs Left-to-Right Convergence

## Convergence Speed

MLM converges slightly slower than a left-to-right language model.

The reason is that MLM predicts only 15% of tokens in each batch.

A left-to-right model predicts every token.

## Accuracy

Despite slower convergence, the MLM model begins outperforming the left-to-right model almost immediately in terms of absolute accuracy.

## Overall Finding

The improved representation quality of MLM outweighs its slower convergence.

# Masking Strategy Ablation

## Purpose

The authors investigate different strategies for replacing selected tokens during MLM pre-training.

The main BERT strategy is:

- 80% `[MASK]`
- 10% random token
- 10% unchanged

## Alternative Strategy

The authors compare this with:

- 100% `[MASK]`
- Other combinations of MASK, SAME, and RND

## Fine-tuning Robustness

Fine-tuning is surprisingly robust to different masking strategies.

The differences between strategies are relatively small for some downstream tasks.

## Feature-Based Sensitivity

The feature-based approach is more sensitive to the masking strategy.

Using only the `[MASK]` strategy performs poorly for feature-based NER.

## Random Replacement

Using only random replacement also performs worse than the mixed strategy.

## Purpose of Mixed Strategy

The mixed strategy reduces the mismatch between pre-training and fine-tuning.

# Training Procedure Findings

## Importance of Large-Scale Pre-training

The experiments show that increasing the number of pre-training steps improves downstream performance.

## Importance of Bidirectionality

The bidirectional MLM model performs substantially better than the left-to-right alternative on several tasks.

## Importance of NSP

Removing NSP decreases performance on tasks involving sentence relationships.

## Importance of Model Size

Larger models produce better results across the evaluated tasks.

# Practical Characteristics

## Minimal Downstream Architecture

BERT requires only a small task-specific output component for many downstream tasks.

## Shared Pre-trained Parameters

The same pre-trained parameters can initialize models for different tasks.

## End-to-End Fine-tuning

The complete BERT model can be fine-tuned jointly with the task-specific output layer.

## Transfer to Small Datasets

The paper shows that larger pre-trained representations can provide strong improvements even when downstream datasets contain relatively little labeled data.

# Limitations and Trade-offs

## Pre-training/Fine-tuning Mismatch

The `[MASK]` token is present during MLM pre-training but absent during downstream fine-tuning.

This creates a mismatch.

The 80/10/10 masking strategy is introduced to reduce this issue.

## MLM Training Efficiency

MLM predicts only a subset of tokens.

Therefore, fewer prediction targets are available in each training step than in a standard left-to-right language model.

This causes somewhat slower convergence.

## Attention Computational Cost

Transformer attention has quadratic complexity with respect to sequence length.

Long sequences are therefore disproportionately expensive.

## Large Computational Requirement

BERT requires substantial compute resources for pre-training.

The reported training setup uses multiple Cloud TPU machines for several days.

## Fine-tuning Instability

The paper observes that BERTLARGE fine-tuning can sometimes be unstable on small datasets.

The authors use multiple random restarts in such cases.

## Architecture Restriction

Not every downstream task can be easily represented using only a Transformer encoder.

Some tasks may require additional task-specific architecture.

## Feature-Based Trade-off

Although fine-tuning is the primary approach, feature extraction can be useful when representations need to be pre-computed and reused.

# Overall Experimental Findings

## Finding 1: Bidirectional Pre-training Matters

The experiments demonstrate that deep bidirectional representations provide substantial benefits over left-to-right pre-training.

## Finding 2: MLM Enables Bidirectionality

The masked language modeling objective provides a way to train a deep bidirectional Transformer without allowing the target token to directly reveal itself.

## Finding 3: NSP Helps Sentence-Level Understanding

The NSP objective improves performance on tasks involving relationships between sentence pairs.

## Finding 4: Larger Models Perform Better

Increasing layers, hidden size, and attention heads generally improves downstream task performance.

## Finding 5: Pre-training Scale Matters

Longer pre-training improves downstream results.

## Finding 6: Minimal Task-Specific Architecture Is Possible

Many NLP tasks can be solved by adding only a small output layer on top of BERT.

## Finding 7: Transfer Learning Works Across Task Types

The same pre-trained representation can support:

- Sentence classification
- Sentence-pair classification
- Question answering
- Sequence tagging
- Natural language inference
- Sentiment analysis
- Commonsense reasoning

# Overall Significance

## General Language Representation

BERT demonstrates that a single deeply bidirectional Transformer encoder can learn general-purpose language representations.

## Transfer Learning

The paper strengthens the case for large-scale unsupervised pre-training followed by supervised fine-tuning.

## Unified NLP Architecture

BERT provides a common architecture that can be adapted to many NLP tasks.

## Reduction of Task-Specific Engineering

The results show that strong pre-trained representations can replace many heavily engineered task-specific architectures.

## Bidirectional Context

The paper establishes deep bidirectional context as a major advantage for language understanding tasks.

## Pre-training and Fine-tuning Paradigm

The paper presents a practical two-stage paradigm:

Pre-training on large unlabeled corpora

followed by

Fine-tuning on task-specific labeled data.

# Key Takeaways

## Takeaway 1

BERT is a multi-layer bidirectional Transformer encoder.

## Takeaway 2

BERT differs from GPT primarily in its bidirectional pre-training approach.

## Takeaway 3

Masked Language Modeling enables deep bidirectional pre-training.

## Takeaway 4

Next Sentence Prediction provides a sentence-pair pre-training objective.

## Takeaway 5

BERT can represent both single sentences and sentence pairs using a unified input format.

## Takeaway 6

The `[CLS]` representation is used for many sequence-level classification tasks.

## Takeaway 7

Individual token representations are used for token-level tasks such as NER and question answering.

## Takeaway 8

BERT uses WordPiece tokenization with a 30,000-token vocabulary.

## Takeaway 9

BERTBASE contains 110M parameters.

## Takeaway 10

BERTLARGE contains 340M parameters.

## Takeaway 11

Larger models and longer pre-training generally improve downstream performance.

## Takeaway 12

BERT achieves strong performance across eleven NLP tasks.

## Takeaway 13

BERT demonstrates that one pre-trained representation can transfer across many different NLP task types.

## Takeaway 14

The main costs of BERT include large pre-training compute requirements and the quadratic sequence-length cost of Transformer attention.

# Paper Workflow

## Overall Pipeline

The complete BERT workflow can be summarized as:

Unlabeled text

↓

WordPiece tokenization

↓

Input sequence construction

↓

Masked Language Modeling

+

Next Sentence Prediction

↓

BERT pre-training

↓

Pre-trained BERT parameters

↓

Task-specific input/output representation

↓

Task-specific output layer

↓

Fine-tuning

↓

Downstream NLP task

# Conceptual Architecture

## Pre-training Stage

The pre-training stage receives unlabeled text.

The text is converted into WordPiece tokens.

Two text spans are combined into an input sequence.

The sequence contains:

- `[CLS]`
- Sentence A
- `[SEP]`
- Sentence B
- `[SEP]`

Token, segment, and position embeddings are combined.

The resulting representation is passed through the Transformer encoder.

The model is trained using:

- Masked Language Modeling
- Next Sentence Prediction

## Fine-tuning Stage

The pre-trained BERT parameters are reused.

The input is adapted to the downstream task.

A task-specific output layer is added.

All BERT parameters are fine-tuned using labeled data.

# BERT Architecture Comparison

## BERT

- Bidirectional Transformer encoder
- MLM
- NSP
- Fine-tuning approach

## OpenAI GPT

- Left-to-right Transformer
- Unidirectional language modeling
- Fine-tuning approach

## ELMo

- Left-to-right LSTM
- Right-to-left LSTM
- Feature-based approach
- Shallow combination of directional representations

# Final Summary

BERT introduces a bidirectional Transformer-based language representation model trained on large amounts of unlabeled text.

Its central innovation is the use of masked language modeling to train a deep bidirectional representation without allowing the target token to directly reveal itself.

The model additionally uses next sentence prediction to learn relationships between pairs of text segments.

After pre-training, BERT can be fine-tuned for many downstream NLP tasks with only limited task-specific architecture.

The experiments show that bidirectional pre-training, large model capacity, and extensive pre-training substantially improve downstream performance.

The paper demonstrates the effectiveness of a unified pre-training and fine-tuning framework across sentence-level and token-level NLP tasks.