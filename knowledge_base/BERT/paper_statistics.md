---
paper: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
year: 2019
domain: "Large Language Models"
subdomain: "Transformer Architecture"
difficulty: "Intermediate"
document_type: "Paper Statistics"
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

# Paper Statistics
now
## Paper Information

- Title: BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
- Authors: Jacob Devlin, Ming-Wei Chang, Kenton Lee, Kristina Toutanova
- Organization: Google AI Language
- Year: 2019
- arXiv identifier: 1810.04805v2
- Pages in provided PDF: 16

# Model Statistics

## BERTBASE

- Transformer layers: 12
- Hidden size: 768
- Attention heads: 12
- Total parameters: 110M

## BERTLARGE

- Transformer layers: 24
- Hidden size: 1024
- Attention heads: 16
- Total parameters: 340M

## Feed-Forward Size

The feed-forward/filter size is 4H.

- BERTBASE: 3072
- BERTLARGE: 4096

# Vocabulary

## WordPiece Vocabulary

BERT uses a WordPiece vocabulary containing 30,000 tokens.

# Pre-training Data

## BooksCorpus

Approximately 800M words.

## English Wikipedia

Approximately 2,500M words.

## Total Pre-training Corpus

Approximately 3.3 billion words.

# Pre-training Configuration

## Masking

- 15% of WordPiece tokens selected for prediction
- 80% replaced by `[MASK]`
- 10% replaced by a random token
- 10% kept unchanged

## Next Sentence Prediction

- 50% IsNext examples
- 50% NotNext examples

## Maximum Training Sequence

The combined length of the two sampled text spans is at most 512 tokens.

## Batch Size

256 sequences.

Each sequence can contain up to 512 tokens, corresponding to:

256 × 512 = 128,000 tokens per batch.

## Training Steps

1,000,000 steps.

This corresponds to approximately 40 epochs over the 3.3 billion word corpus.

## Optimizer

Adam.

## Learning Rate

1e-4.

## Adam Parameters

- β1 = 0.9
- β2 = 0.999

## Weight Decay

0.01.

## Warmup

Learning-rate warmup over the first 10,000 steps.

## Dropout

0.1 on all layers.

## Activation Function

GELU.

# Sequence-Length Training Strategy

## Short Sequences

Sequence length 128 is used for 90% of the pre-training steps.

## Long Sequences

Sequence length 512 is used for the remaining 10% of the steps.

The authors use this strategy because longer sequences are disproportionately expensive due to the quadratic cost of attention.

# Pre-training Compute

## BERTBASE

- 4 Cloud TPUs in Pod configuration
- 16 TPU chips total
- Approximately 4 days of pre-training

## BERTLARGE

- 16 Cloud TPUs
- 64 TPU chips total
- Approximately 4 days of pre-training

# Reported Results

## GLUE

BERTLARGE achieves:

- GLUE score: 80.5
- MNLI accuracy: 86.7/85.9

BERTBASE achieves an average score of 79.6 when excluding WNLI.

## SQuAD v1.1

BERTLARGE ensemble with TriviaQA achieves:

- Test EM: 87.4
- Test F1: 93.2

BERTLARGE single model with TriviaQA achieves:

- Test EM: 85.1
- Test F1: 91.8

## SQuAD v2.0

BERTLARGE single model achieves:

- Test EM: 80.0
- Test F1: 83.1

## SWAG

BERTLARGE achieves:

- Dev accuracy: 86.6
- Test accuracy: 86.3

## CoNLL-2003 NER

BERTLARGE fine-tuning achieves:

- Dev F1: 96.6
- Test F1: 92.8

# Number of Evaluated Tasks

The paper reports results on 11 NLP tasks.