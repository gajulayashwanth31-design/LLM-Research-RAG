---
paper: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
year: 2019
domain: "Large Language Models"
subdomain: "Transformer Architecture"
difficulty: "Intermediate"
document_type: "Terminology"
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

# BERT

## BERT

Bidirectional Encoder Representations from Transformers. A language representation model based on a multi-layer bidirectional Transformer encoder.

## Bidirectional Representation

A representation that incorporates both left and right context when representing tokens.

# Pre-training

## Pre-training

Training BERT on large amounts of unlabeled text before adapting it to downstream supervised tasks.

# Fine-tuning

## Fine-tuning

Training the pre-trained BERT model on labeled data for a specific downstream task while updating the model parameters.

# Masked Language Model

## Masked Language Model

A pre-training objective where selected input tokens are hidden or replaced and the model predicts their original values.

## MLM

Abbreviation for Masked Language Model.

# Next Sentence Prediction

## Next Sentence Prediction

A pre-training task where BERT predicts whether one text segment is the actual next segment following another segment.

## NSP

Abbreviation for Next Sentence Prediction.

# Transformer Encoder

## Transformer Encoder

The Transformer architecture used by BERT. BERT uses multiple Transformer encoder blocks with bidirectional self-attention.

# WordPiece

## WordPiece

A subword tokenization method used by BERT with a 30,000-token vocabulary.

# [CLS]

## [CLS] Token

A special token placed at the beginning of every BERT input sequence. Its final hidden representation is used as the aggregate sequence representation for classification tasks.

# [SEP]

## [SEP] Token

A special separator token used to separate two input segments, such as a question and a passage.

# Segment Embedding

## Segment Embedding

A learned embedding indicating whether a token belongs to sentence A or sentence B.

# Position Embedding

## Position Embedding

An embedding representing the position of a token in the input sequence.

# Token Embedding

## Token Embedding

The learned representation corresponding to an input token.

# Hidden Size

## Hidden Size

The dimensionality of the hidden representation in BERT. The paper denotes it by H.

# Attention Heads

## Attention Heads

The number of self-attention heads in each Transformer block. The paper denotes this number by A.

# Transformer Layers

## Transformer Layers

The number of Transformer blocks in BERT. The paper denotes this number by L.

# BERTBASE

## BERTBASE

A BERT configuration with:

- 12 Transformer layers
- Hidden size 768
- 12 attention heads
- 110M parameters

# BERTLARGE

## BERTLARGE

A BERT configuration with:

- 24 Transformer layers
- Hidden size 1024
- 16 attention heads
- 340M parameters

# GLUE

## GLUE

A benchmark containing diverse natural language understanding tasks used to evaluate BERT.

# SQuAD

## SQuAD

The Stanford Question Answering Dataset used in the paper to evaluate BERT on question answering.

# SWAG

## SWAG

Situations With Adversarial Generations, a dataset used to evaluate grounded commonsense inference.

# NER

## Named Entity Recognition

A token-level task evaluated using BERT in the paper through the CoNLL-2003 dataset.

# Feature-based Approach

## Feature-based Approach

An approach where fixed representations are extracted from a pre-trained model and supplied to another task-specific model.

# Fine-tuning Approach

## Fine-tuning Approach

An approach where the pre-trained model parameters are updated directly using downstream task data.

# GELU

## GELU

The activation function used by BERT instead of the standard ReLU, following OpenAI GPT.

# WordPiece Token

## WordPiece Token

A subword unit produced by WordPiece tokenization. The paper's examples include tokens such as `play` and `##ing`.