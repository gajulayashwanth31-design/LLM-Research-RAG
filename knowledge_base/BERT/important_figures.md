---
paper: "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding"
year: 2019
domain: "Large Language Models"
subdomain: "Transformer Architecture"
difficulty: "Intermediate"
document_type: "Important Figures"
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

# Figure 1

## Overall Pre-training and Fine-Tuning Procedures

Figure 1 illustrates the overall BERT framework.

The left side shows pre-training using:

- Masked Language Modeling
- Next Sentence Prediction
- Unlabeled sentence pairs

The right side shows fine-tuning for downstream tasks such as:

- SQuAD question answering
- MNLI
- NER

The same pre-trained BERT parameters are used to initialize models for different downstream tasks.

During fine-tuning, all BERT parameters are fine-tuned.

The figure also shows the use of `[CLS]` as a special token at the beginning of the input and `[SEP]` as a separator token.

# Figure 2

## BERT Input Representation

Figure 2 illustrates how BERT constructs an input representation.

For every input token, three embeddings are summed:

1. Token embedding
2. Segment embedding
3. Position embedding

The example contains two segments separated using `[SEP]`.

The figure demonstrates how different segment embeddings distinguish tokens belonging to sentence A and sentence B.

# Figure 3

## Comparison of Pre-training Architectures

Figure 3 compares:

- BERT
- OpenAI GPT
- ELMo

BERT uses a bidirectional Transformer.

OpenAI GPT uses a left-to-right Transformer.

ELMo uses the concatenation of independently trained left-to-right and right-to-left LSTMs.

The figure emphasizes that BERT representations are jointly conditioned on both left and right context in all layers.

It also distinguishes BERT and GPT as fine-tuning approaches from ELMo's feature-based approach.