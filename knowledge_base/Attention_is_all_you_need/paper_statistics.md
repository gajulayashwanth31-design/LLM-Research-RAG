---
paper: "Attention Is All You Need"
year: 2017
domain: "Large Language Models"
subdomain: "Transformer Architecture"
difficulty: "Intermediate"        
document_type: "Paper Statistics"
keywords:
  - Transformer
  - Machine Translation
  - Evaluation
generated_from: "Original Research Paper"
---

# Paper Statistics

---

## General Information

| Attribute | Value |
|----------|-------|
| Title | Attention Is All You Need |
| Publication Year | 2017 |
| Paper Type | Foundational Research Paper |
| Domain | Large Language Models |
| Subdomain | Transformer Architecture |
| Primary Task | Neural Machine Translation |

---

## Authors

- Ashish Vaswani
- Noam Shazeer
- Niki Parmar
- Jakob Uszkoreit
- Llion Jones
- Aidan N. Gomez
- Łukasz Kaiser
- Illia Polosukhin

---

## Model Configuration

| Parameter | Base Model | Big Model |
|-----------|------------|-----------|
| Encoder Layers | 6 | 6 |
| Decoder Layers | 6 | 6 |
| Embedding Dimension (dmodel) | 512 | 1024 |
| Feed Forward Dimension | 2048 | 4096 |
| Number of Attention Heads | 8 | 16 |
| Query Dimension (dk) | 64 | 64 |
| Value Dimension (dv) | 64 | 64 |
| Dropout | 0.1 | 0.3 |

---

## Datasets Used

### WMT 2014 English-German

- Approximately **4.5 million** sentence pairs
- Shared Byte Pair Encoding (BPE) vocabulary
- Approximately **37,000** tokens

---

### WMT 2014 English-French

- Approximately **36 million** sentence pairs
- Word-piece vocabulary
- Approximately **32,000** tokens

---

### English Constituency Parsing

Used to demonstrate that the Transformer architecture generalizes beyond machine translation.

---

## Evaluation Metrics

The paper evaluates the Transformer using the following metrics:

- BLEU Score
- Perplexity
- Parsing Accuracy (for constituency parsing experiments)

---

## Optimizer

- Adam Optimizer

Parameters:

- β₁ = 0.9
- β₂ = 0.98
- ε = 10⁻⁹

---

## Learning Rate Strategy

- Linear warm-up
- Warm-up steps = 4000
- Inverse square-root learning rate decay after warm-up

---

## Regularization

- Dropout
- Residual Connections
- Layer Normalization
- Label Smoothing (ε = 0.1)

---

## Batch Information

Training batches contained approximately:

- 25,000 source tokens
- 25,000 target tokens

Batching was performed using similar sequence lengths to improve computational efficiency.

---

## Hardware

The models were trained using:

- 8 NVIDIA P100 GPUs

Training Time:

| Model | Training Time |
|---------|--------------|
| Base Transformer | Approximately 12 hours |
| Transformer (Big) | Approximately 3.5 days |

---

## Beam Search Configuration

| Parameter | Value |
|-----------|-------|
| Beam Size | 4 |
| Length Penalty | 0.6 |

---

## Experimental Results

### English → German

| Model | BLEU Score |
|---------|-----------|
| Transformer (Base) | 27.3 |
| Transformer (Big) | 28.4 |

---

### English → French

| Model | BLEU Score |
|---------|-----------|
| Transformer (Big) | 41.8 |

---

## Architectural Components

The Transformer architecture consists of:

- Encoder
- Decoder
- Multi-Head Attention
- Scaled Dot-Product Attention
- Feed Forward Network
- Positional Encoding
- Residual Connections
- Layer Normalization
- Softmax Output Layer

---

## Key Innovations

- First sequence transduction model based entirely on attention.
- Eliminated recurrence.
- Eliminated convolution.
- Introduced Scaled Dot-Product Attention.
- Introduced Multi-Head Attention.
- Introduced sinusoidal Positional Encoding.
- Enabled highly parallel training.

---

## Computational Characteristics

### Advantages

- Highly parallelizable.
- Faster training than RNN-based models.
- Better long-range dependency modeling.
- Improved GPU utilization.

---

### Limitations

- O(n²) self-attention complexity.
- High memory consumption for long sequences.
- Sequential autoregressive decoding during inference.

---

## Impact

The Transformer architecture introduced in this paper became the foundation for nearly all modern Transformer-based models, including:

- BERT
- GPT series
- T5
- Vision Transformer (ViT)
- LLaMA
- PaLM
- Gemini
- Claude
- Mistral
- Qwen

---

## Quick Facts

| Property | Value |
|-----------|-------|
| Architecture | Encoder–Decoder Transformer |
| Core Mechanism | Self-Attention |
| Attention Heads (Base) | 8 |
| Encoder Layers | 6 |
| Decoder Layers | 6 |
| Embedding Size | 512 |
| FFN Hidden Size | 2048 |
| Optimizer | Adam |
| Warm-up Steps | 4000 |
| Hardware | 8 NVIDIA P100 GPUs |
| Main Evaluation Metric | BLEU Score |
| Best EN-DE BLEU | 28.4 |
| Best EN-FR BLEU | 41.8 |