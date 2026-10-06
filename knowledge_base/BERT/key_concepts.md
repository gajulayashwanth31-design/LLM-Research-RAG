---
paper: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
year: 2019
domain: "Large Language Models"
subdomain: "Transformer Architecture"
difficulty: "Intermediate"
document_type: "Key Concepts"
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

## What is it?

BERT stands for Bidirectional Encoder Representations from Transformers.

It is a language representation model based on a multi-layer bidirectional Transformer encoder.

BERT is designed to learn representations by jointly conditioning on both left and right context in all layers.

## Why was it introduced?

Traditional language models used during pre-training were generally unidirectional.

For example, a left-to-right model allows each token to attend only to tokens to its left.

This restriction can be harmful for token-level tasks such as question answering, where information from both directions is important.

BERT addresses this limitation using masked language modeling, which allows the model to learn bidirectional representations.

# BERT Architecture

## What is it?

BERT uses a multi-layer bidirectional Transformer encoder.

The architecture is based on the original Transformer implementation.

The paper reports two primary model sizes:

- BERTBASE: 12 layers, hidden size 768, 12 attention heads, 110M parameters
- BERTLARGE: 24 layers, hidden size 1024, 16 attention heads, 340M parameters

The feed-forward/filter size is set to 4H.

## Bidirectional Self-Attention

Unlike OpenAI GPT in the comparison presented by the paper, BERT uses bidirectional self-attention.

Each token can use context from both the left and right sides of the sequence.

GPT uses constrained self-attention where tokens can only attend to context on their left.

# Input Representation

## What is it?

BERT can represent either a single sentence or a pair of sentences as one token sequence.

The input uses WordPiece embeddings with a 30,000-token vocabulary.

Each sequence begins with a special `[CLS]` token.

The `[SEP]` token is used to separate sentence pairs.

Each token representation is constructed by summing:

- Token embedding
- Segment embedding
- Position embedding

## [CLS] Token

The `[CLS]` token is placed at the beginning of every input sequence.

Its final hidden representation is used as an aggregate sequence representation for classification tasks.

## [SEP] Token

The `[SEP]` token separates sentence A and sentence B when a pair of sentences is provided.

# Masked Language Model

## What is it?

Masked Language Modeling (MLM) is the first pre-training objective used by BERT.

A percentage of input tokens is selected and the model is trained to predict the original tokens using their surrounding context.

This allows BERT to learn representations using both left and right context.

## How does it work?

BERT selects 15% of WordPiece tokens for prediction.

For each selected token:

- 80% of the time, it is replaced with `[MASK]`
- 10% of the time, it is replaced with a random token
- 10% of the time, it remains unchanged

The model then predicts the original token.

## Why is MLM needed?

A standard bidirectional language model would allow a word to indirectly see itself during prediction.

MLM avoids this problem by hiding selected tokens before prediction.

It therefore enables deep bidirectional pre-training.

# Next Sentence Prediction

## What is it?

Next Sentence Prediction (NSP) is the second pre-training objective.

It trains BERT to understand relationships between two text segments.

## How does it work?

Two text segments, A and B, are provided.

- 50% of the time, B is the actual next sentence following A.
- 50% of the time, B is a randomly selected sentence from the corpus.

The model predicts either:

- `IsNext`
- `NotNext`

The `[CLS]` representation is used for the NSP prediction.

# Pre-training

## What is it?

BERT pre-training is performed on unlabeled text using two objectives:

1. Masked Language Modeling
2. Next Sentence Prediction

The pre-trained parameters are later used to initialize models for downstream tasks.

## Pre-training Data

The paper uses:

- BooksCorpus: approximately 800M words
- English Wikipedia: approximately 2,500M words

The authors emphasize the importance of using a document-level corpus to obtain long contiguous sequences.

# Fine-Tuning

## What is it?

Fine-tuning initializes BERT using its pre-trained parameters and then trains all parameters using labeled data for a downstream task.

Each downstream task receives its own fine-tuned model.

## How does it work?

Task-specific inputs and outputs are connected to the shared BERT architecture.

For classification tasks, the `[CLS]` representation is passed to an output layer.

For token-level tasks such as question answering and sequence tagging, token representations are passed to task-specific output layers.

# WordPiece Tokenization

## What is it?

BERT uses WordPiece embeddings with a vocabulary of 30,000 tokens.

WordPiece allows words to be represented using smaller subword units.

The paper's examples include tokens such as `play` and `##ing`.

# Transfer Learning

## What is it?

BERT transfers knowledge learned during unsupervised pre-training to supervised downstream tasks.

The same pre-trained parameters can initialize models for multiple different tasks.

This reduces the need to design separate heavily engineered architectures for each task.