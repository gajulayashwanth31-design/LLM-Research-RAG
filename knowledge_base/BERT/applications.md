---
paper: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
year: 2019
domain: "Large Language Models"
subdomain: "Transformer Architecture"
difficulty: "Intermediate"
document_type: "Applications"
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

# Downstream Applications

## Question Answering

BERT is evaluated on the SQuAD v1.1 and SQuAD v2.0 question answering tasks.

For SQuAD, the question and passage are packed into a single input sequence.

The question is assigned the A segment embedding and the passage is assigned the B segment embedding.

BERT predicts the start and end positions of the answer span.

## Natural Language Inference

BERT is evaluated on natural language inference tasks including MNLI and QNLI.

Sentence pairs can be represented as a single sequence and processed using BERT's self-attention mechanism.

## Named Entity Recognition

BERT is evaluated on the CoNLL-2003 Named Entity Recognition task.

For token-level prediction, token representations are passed to a task-specific classifier.

## Sentiment Analysis

The paper includes SST-2 as one of the GLUE tasks.

For classification tasks, the final hidden representation of `[CLS]` is used as the aggregate representation.

## Paraphrase Detection

BERT can process sentence pairs for paraphrase-related tasks.

Sentence A and sentence B are packed into a single sequence and processed jointly using self-attention.

## Text Classification

BERT can be fine-tuned for classification tasks by using the `[CLS]` representation as input to a task-specific output layer.

## Sequence Tagging

BERT supports token-level sequence tagging tasks by using the representations of individual tokens as inputs to an output layer.

## Commonsense Inference

BERT is evaluated on SWAG, which tests grounded commonsense inference.

The task requires selecting the most plausible continuation of a given sentence from multiple choices.

## GLUE Benchmark

BERT is evaluated on the GLUE benchmark, which contains diverse natural language understanding tasks including:

- MNLI
- QQP
- QNLI
- SST-2
- CoLA
- STS-B
- MRPC
- RTE