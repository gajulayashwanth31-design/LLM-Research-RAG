---
paper: "Attention Is All You Need"
year: 2017
domain: "Large Language Models"
subdomain: "Transformer Architecture"
difficulty: "Intermediate"
document_type: "Key Concepts"
keywords:
  - Transformer
  - Self-Attention
  - Multi-Head Attention
  - Encoder
  - Decoder
generated_from: "Original Research Paper"
---

# Key Concepts

---

# Transformer

## What is it?

The Transformer is a sequence-to-sequence neural network architecture introduced in the paper *Attention Is All You Need*. It is the first architecture that performs sequence transduction tasks using only attention mechanisms, completely eliminating recurrent neural networks (RNNs) and convolutional neural networks (CNNs).

The Transformer follows an encoder-decoder architecture and is designed to process all tokens in a sequence simultaneously, enabling highly parallel computation during training.

---

## Why was it introduced?

Prior sequence models such as RNNs, LSTMs, and GRUs process input tokens sequentially. This sequential computation limits parallelization, increases training time, and makes learning long-range dependencies difficult.

Although attention mechanisms improved encoder-decoder models, they were still used alongside recurrent architectures.

The Transformer was introduced to determine whether attention mechanisms alone were sufficient for sequence modeling.

---

## How does it work?

The Transformer consists of two main components:

- Encoder Stack
- Decoder Stack

Each encoder layer contains:

- Multi-Head Self-Attention
- Feed Forward Network

Each decoder layer contains:

- Masked Multi-Head Self-Attention
- Encoder-Decoder Attention
- Feed Forward Network

Residual connections and layer normalization are applied after every sub-layer.

Since there is no recurrence, positional information is added using positional encodings.

The model processes all input tokens simultaneously, producing contextual representations through repeated attention operations.

---

## Advantages

- Eliminates recurrent computation.
- Enables highly parallel training.
- Captures long-range dependencies efficiently.
- Shortens information flow between distant tokens.
- Achieves state-of-the-art translation performance.
- Scales effectively to large datasets.

---

## Limitations

- Self-attention requires quadratic computation with respect to sequence length.
- Memory consumption increases significantly for long sequences.
- Computational cost grows rapidly as sequence length increases.

---

## Important Points

- First architecture based entirely on attention mechanisms.
- Does not use RNNs.
- Does not use CNNs.
- Processes all tokens simultaneously.
- Forms the foundation of nearly all modern Large Language Models.

---

## Keywords

Transformer

Attention

Encoder

Decoder

Parallel Training

Sequence Modeling

---

# Self-Attention

## What is it?

Self-Attention is an attention mechanism in which every token in an input sequence computes relationships with every other token in the same sequence.

Instead of processing words independently, each token builds a contextual representation by attending to all other tokens.

In the Transformer, the Queries (Q), Keys (K), and Values (V) are all derived from the same input sequence.

---

## Why was it introduced?

Traditional recurrent models struggle to capture relationships between distant words because information must pass through many hidden states.

Self-Attention allows every token to directly access information from every other token regardless of their distance in the sequence.

This greatly improves contextual understanding while enabling parallel computation.

---

## How does it work?

For every input token:

1. Generate Query vector.
2. Generate Key vector.
3. Generate Value vector.

The Query of one token is compared with the Keys of all tokens.

The similarity scores determine how much attention should be given to each Value vector.

The weighted combination of Value vectors becomes the contextual representation of that token.

Since every token performs this computation simultaneously, the entire sequence is processed in parallel.

---

## Advantages

- Captures long-distance dependencies.
- Enables contextual understanding.
- Eliminates sequential computation.
- Supports parallel processing.
- Improves representation learning.

---

## Limitations

- Requires quadratic memory.
- Computationally expensive for very long sequences.
- Every token attends to every other token, increasing computation as sequence length grows.

---

## Important Points

- Queries, Keys, and Values come from the same sequence.
- Every token attends to all other tokens.
- Produces contextual token representations.
- Forms the foundation of the Transformer architecture.

---

## Keywords

Self-Attention

Context

Query

Key

Value

Dependency

Contextual Representation

---

# Scaled Dot-Product Attention

## What is it?

Scaled Dot-Product Attention is the core attention mechanism introduced in the Transformer. It computes the importance of every token in a sequence with respect to another token by comparing their Query and Key vectors. The resulting attention weights are then used to compute a weighted combination of the Value vectors.

The attention function is defined as:

Attention(Q, K, V) = Softmax((QKᵀ) / √dk) V

where:

- Q = Query matrix
- K = Key matrix
- V = Value matrix
- dk = Dimension of the key vectors

The scaling factor √dk is a key innovation introduced in this paper. :contentReference[oaicite:0]{index=0}

---

## Why was it introduced?

The authors compare two commonly used attention mechanisms:

- Additive Attention
- Dot-Product Attention

Although dot-product attention is computationally faster due to efficient matrix multiplication, it performs poorly when the dimensionality of the key vectors becomes large.

As dk increases, the dot products also become larger, causing the Softmax function to enter regions where gradients become extremely small.

To solve this problem, the authors divide the attention scores by √dk before applying Softmax, stabilizing training and improving optimization. :contentReference[oaicite:1]{index=1}

---

## How does it work?

The computation follows four steps:

1. Compute the dot product between Queries and Keys.
2. Scale the result by dividing by √dk.
3. Apply the Softmax function to obtain attention weights.
4. Multiply the attention weights with the Value vectors to obtain the output representation.

This allows every token to determine how much information it should gather from every other token in the sequence. :contentReference[oaicite:2]{index=2}

---

## Advantages

- Computationally efficient.
- Easy to parallelize.
- Stable training due to scaling.
- Can be implemented efficiently using matrix multiplication.
- Produces contextual representations for every token.

---

## Limitations

- Computational complexity grows quadratically with sequence length.
- Memory requirements become large for long sequences.

---

## Important Points

- Introduced specifically in this paper.
- Uses scaling by √dk.
- Forms the foundation of Multi-Head Attention.
- Replaces additive attention in the Transformer architecture.

---

## Keywords

Scaled Dot-Product Attention

Softmax

Query

Key

Value

Scaling Factor

Attention Scores

---

# Multi-Head Attention

## What is it?

Multi-Head Attention extends Scaled Dot-Product Attention by computing several independent attention operations in parallel.

Instead of using one attention mechanism over the full embedding space, the Transformer projects the Queries, Keys, and Values into multiple lower-dimensional subspaces. Each attention head learns different relationships among tokens.

The outputs from all heads are concatenated and projected to produce the final representation. 

---

## Why was it introduced?

A single attention head tends to average different relationships into one representation.

The authors observed that allowing multiple attention heads enables the model to jointly attend to information from different representation subspaces and different positions in the sequence.

This improves the model's representational capacity without significantly increasing computational cost. :contentReference[oaicite:4]{index=4}

---

## How does it work?

The process consists of the following steps:

1. Linearly project Queries, Keys, and Values into multiple lower-dimensional spaces.
2. Compute Scaled Dot-Product Attention independently for each head.
3. Concatenate the outputs of all heads.
4. Apply a final linear projection to obtain the output representation.

In the base Transformer model:

- Number of attention heads = 8
- dk = 64
- dv = 64

The reduced dimension of each head keeps the overall computational cost comparable to a single-head attention mechanism. :contentReference[oaicite:5]{index=5}

---

## Advantages

- Learns multiple relationships simultaneously.
- Improves representation quality.
- Captures syntactic and semantic information more effectively.
- Maintains computational efficiency through lower-dimensional projections.

---

## Limitations

- More parameters than a single-head attention mechanism.
- Still inherits the quadratic complexity of self-attention.

---

## Important Points

- Introduced in this paper.
- Uses multiple parallel attention heads.
- Outputs from all heads are concatenated.
- One of the defining innovations of the Transformer.

---

## Keywords

Multi-Head Attention

Attention Heads

Parallel Attention

Representation Subspaces

Concatenation

---

# Query, Key and Value (Q, K, V)

## What are they?

Queries (Q), Keys (K), and Values (V) are vector representations used by the attention mechanism.

Each input token is transformed into three different vectors through learned linear projections:

- Query (Q)
- Key (K)
- Value (V)

These vectors allow the model to determine how tokens should interact with one another during attention computation. :contentReference[oaicite:6]{index=6}

---

## Why were they introduced?

The attention mechanism requires a way to compare tokens and determine their relevance.

The Query vector represents what information a token is looking for.

The Key vector represents what information a token contains.

The Value vector contains the information that will be passed to other tokens if selected by the attention mechanism.

Together, these three representations enable flexible and context-dependent information exchange across the sequence.

---

## How do they work?

For a given token:

- The Query vector is compared with the Key vectors of all tokens.
- Similarity scores are computed using dot products.
- Softmax converts these scores into attention weights.
- The weights are used to compute a weighted combination of the Value vectors.

The resulting output becomes the contextual representation of the token.

---

## Advantages

- Enables dynamic interaction between tokens.
- Allows context-dependent representations.
- Supports efficient matrix-based computation.

---

## Limitations

- Requires additional projection matrices.
- Computational cost increases with sequence length because every Query interacts with every Key.

---

## Important Points

- Every token has its own Query, Key, and Value vectors.
- Q, K, and V are learned through linear transformations.
- They are fundamental building blocks of the Transformer attention mechanism.

---

## Keywords

Query

Key

Value

Projection Matrix

Attention

Context Representation

---

# Encoder

## What is it?

The encoder is the first major component of the Transformer architecture. It receives the input sequence and transforms it into contextual representations that capture the relationships among all input tokens.

The Transformer encoder is composed of **6 identical layers**. :contentReference[oaicite:7]{index=7}

---

## Why was it introduced?

The encoder creates rich contextual representations of the input sequence.

Instead of relying on recurrent hidden states, it uses self-attention to model dependencies between every pair of tokens, regardless of their distance.

These contextual representations are later used by the decoder to generate the output sequence.

---

## How does it work?

Each encoder layer contains:

1. Multi-Head Self-Attention
2. Position-wise Feed-Forward Network

Residual connections and layer normalization are applied after each sub-layer.

The output of one encoder layer becomes the input to the next encoder layer, gradually producing increasingly contextualized representations. :contentReference[oaicite:8]{index=8}

---

## Advantages

- Fully parallel computation.
- Better modeling of long-range dependencies.
- Produces contextual token representations.
- Simpler than recurrent encoder architectures.

---

## Limitations

- Computational cost increases with sequence length because of self-attention.
- Memory usage grows quadratically for long inputs.

---

## Important Points

- Contains six identical layers.
- Uses Multi-Head Self-Attention.
- Produces contextual embeddings for the decoder.

---

## Keywords

Encoder

Context Representation

Input Sequence

Self-Attention

Feed-Forward Network

# Decoder

## What is it?

The decoder is the second major component of the Transformer architecture. Its purpose is to generate the output sequence one token at a time using information from both the previously generated tokens and the encoder's output.

Like the encoder, the decoder consists of **6 identical layers**. However, each decoder layer contains an additional attention mechanism that allows it to attend to the encoder's representations. :contentReference[oaicite:2]{index=2}

---

## Why was it introduced?

After the encoder converts the input sequence into contextual representations, the decoder uses those representations to produce the target sequence.

Unlike the encoder, the decoder must generate tokens sequentially during inference because each new token depends on the tokens already generated.

---

## How does it work?

Each decoder layer consists of three sub-layers:

1. Masked Multi-Head Self-Attention
2. Encoder-Decoder Attention
3. Position-wise Feed Forward Network

Residual connections and layer normalization are applied after every sub-layer.

During generation:

- The decoder first attends to previously generated output tokens.
- It then attends to the encoder's output representations.
- Finally, it predicts the next token using a linear layer followed by Softmax. 

---

## Advantages

- Generates context-aware output sequences.
- Uses both previously generated tokens and encoder information.
- Integrates naturally with the encoder-decoder framework.

---

## Limitations

- Token generation remains autoregressive during inference.
- Inference cannot be fully parallelized because future tokens are unknown.

---

## Important Points

- Contains six identical layers.
- Includes Masked Self-Attention.
- Includes Encoder-Decoder Attention.
- Predicts one token at a time.

---

## Keywords

Decoder

Autoregressive Generation

Masked Attention

Encoder Output

---

# Positional Encoding

## What is it?

Positional Encoding is a mechanism that injects information about token positions into the input embeddings.

Since the Transformer contains neither recurrence nor convolution, it has no inherent understanding of word order. Positional Encoding provides this missing positional information. :contentReference[oaicite:4]{index=4}

---

## Why was it introduced?

Self-attention treats all input tokens simultaneously.

Without positional information, the model would process sentences such as:

- "Dog bites man"
- "Man bites dog"

as identical sets of words.

Positional Encoding enables the Transformer to distinguish token order while preserving parallel computation.

---

## How does it work?

The paper uses sinusoidal functions with different frequencies.

For every token position, sine and cosine values are computed across different embedding dimensions.

These positional vectors are added directly to the token embeddings before entering the encoder and decoder.

The authors also experimented with learned positional embeddings and observed nearly identical performance, choosing sinusoidal encodings because they may generalize better to longer sequences. 

---

## Advantages

- Preserves sequence order.
- Does not require recurrent computation.
- Generalizes to longer sequences.
- Computationally efficient.

---

## Limitations

- Fixed sinusoidal encoding may not capture every positional relationship.
- Position information is added rather than learned dynamically in the proposed model.

---

## Important Points

- Added before the first encoder layer.
- Same dimensionality as token embeddings.
- Uses sine and cosine functions.

---

## Keywords

Positional Encoding

Sinusoidal Encoding

Sequence Order

Token Position

---

# Feed Forward Network (FFN)

## What is it?

The Position-wise Feed Forward Network is the second major sub-layer in every encoder layer and the third sub-layer in every decoder layer.

Unlike attention, which models relationships between different tokens, the FFN processes each token independently after contextual information has been incorporated. :contentReference[oaicite:6]{index=6}

---

## Why was it introduced?

Attention mechanisms combine contextual information across tokens.

The Feed Forward Network then applies non-linear transformations to enrich the representation of each individual token.

This increases the expressive power of the model.

---

## How does it work?

The FFN consists of two linear transformations with a ReLU activation between them.

Mathematically:

FFN(x) = max(0, xW₁ + b₁)W₂ + b₂

The same FFN is applied independently to every token position.

For the base Transformer:

- Input dimension = 512
- Hidden dimension = 2048
- Output dimension = 512 :contentReference[oaicite:7]{index=7}

---

## Advantages

- Introduces non-linearity.
- Enhances token representations.
- Easy to parallelize.
- Same computation applied to every position.

---

## Limitations

- Does not directly model interactions between different tokens.
- Increases the number of model parameters.

---

## Important Points

- Present in every encoder layer.
- Present in every decoder layer.
- Operates independently on each token.
- Uses ReLU activation.

---

## Keywords

Feed Forward Network

FFN

Linear Layer

ReLU

Position-wise Computation

# Residual Connections

## What are they?

Residual Connections, also known as skip connections, are shortcut paths that allow the input of a sub-layer to be added directly to its output before applying Layer Normalization.

Instead of learning a completely new transformation, the model learns a residual function over the input.

In the Transformer, every attention sub-layer and feed-forward sub-layer is surrounded by a residual connection.

---

## Why were they introduced?

As neural networks become deeper, training becomes more difficult due to problems such as vanishing gradients.

Residual connections improve gradient flow through the network, making optimization easier and allowing deeper architectures to converge more effectively.

The Transformer applies residual connections after every sub-layer to stabilize training. :contentReference[oaicite:0]{index=0}

---

## How do they work?

For every sub-layer, the output is computed as:

```
LayerNorm(x + Sublayer(x))
```

where:

- **x** is the input to the sub-layer.
- **Sublayer(x)** is the output of the attention or feed-forward network.

The input is added to the sub-layer output before normalization.

---

## Advantages

- Improves gradient flow.
- Makes optimization easier.
- Enables deeper networks.
- Preserves useful information from previous layers.

---

## Limitations

- Adds extra computation due to the addition operation.
- Does not completely solve optimization issues without normalization.

---

## Important Points

- Applied after every attention sub-layer.
- Applied after every feed-forward sub-layer.
- Always followed by Layer Normalization.

---

## Keywords

Residual Connection

Skip Connection

Gradient Flow

Deep Networks

---

# Layer Normalization

## What is it?

Layer Normalization is a normalization technique applied after each residual connection in the Transformer.

Unlike Batch Normalization, Layer Normalization computes normalization statistics across the feature dimensions of each individual token rather than across the batch.

The paper applies Layer Normalization after every residual connection. :contentReference[oaicite:1]{index=1}

---

## Why was it introduced?

As networks become deeper, the distribution of activations changes during training.

Layer Normalization stabilizes these activations, making optimization more stable and accelerating convergence.

---

## How does it work?

For every sub-layer:

1. Compute the sub-layer output.
2. Add the residual connection.
3. Normalize the resulting vector.

Mathematically:

```
LayerNorm(x + Sublayer(x))
```

---

## Advantages

- Stabilizes training.
- Accelerates convergence.
- Works well with variable batch sizes.
- Improves optimization.

---

## Limitations

- Adds additional computation.
- Does not reduce the quadratic complexity of attention.

---

## Important Points

- Applied after every residual connection.
- Used in both encoder and decoder.
- Essential for stable Transformer training.

---

## Keywords

Layer Normalization

Normalization

Residual Connection

Optimization

---

# Masked Self-Attention

## What is it?

Masked Self-Attention is a modified version of self-attention used only in the decoder.

It prevents each output position from attending to future positions during training.

This preserves the autoregressive property of sequence generation. :contentReference[oaicite:2]{index=2}

---

## Why was it introduced?

During training, the complete target sentence is already available.

Without masking, the decoder could "see" future words and learn to predict the next token using information that would not be available during inference.

Masking prevents this information leakage.

---

## How does it work?

Before applying the Softmax function, illegal attention positions are assigned a value of **−∞**.

After Softmax:

- Future positions receive zero probability.
- Each token attends only to previous tokens and itself.

This ensures causal generation. :contentReference[oaicite:3]{index=3}

---

## Advantages

- Prevents information leakage.
- Preserves autoregressive decoding.
- Enables teacher-forcing during training.

---

## Limitations

- Decoder inference remains sequential.
- Cannot fully parallelize token generation during inference.

---

## Important Points

- Used only in the decoder.
- Masks future tokens.
- Implemented before Softmax.

---

## Keywords

Masked Attention

Causal Attention

Decoder

Autoregressive Generation

---

# Encoder-Decoder Attention

## What is it?

Encoder-Decoder Attention is the second attention mechanism inside every decoder layer.

Unlike self-attention, the Queries come from the decoder, while the Keys and Values come from the encoder outputs.

This allows the decoder to use information from the input sequence while generating the output. :contentReference[oaicite:4]{index=4}

---

## Why was it introduced?

The decoder must know which parts of the input sequence are relevant when generating each output token.

Encoder-Decoder Attention provides this connection between the encoded input representation and the decoder.

---

## How does it work?

For each decoder position:

- Query comes from the decoder.
- Keys come from the encoder.
- Values come from the encoder.

Attention determines which encoder representations are most useful for generating the next output token.

---

## Advantages

- Connects input and output sequences.
- Enables context-aware generation.
- Improves translation quality.

---

## Limitations

- Adds additional attention computation.
- Still depends on self-attention complexity.

---

## Important Points

- Present only in the decoder.
- Queries originate from decoder.
- Keys and Values originate from encoder.

---

## Keywords

Encoder-Decoder Attention

Cross Attention

Context

Sequence-to-Sequence

---

# Embeddings

## What are they?

Embeddings are dense vector representations of input and output tokens.

The Transformer converts each token into a vector of dimension **dmodel = 512** before any attention computation begins.

The paper shares the same weight matrix between the input embeddings, output embeddings, and the pre-softmax linear transformation. The embedding vectors are multiplied by √dmodel before positional encodings are added. :contentReference[oaicite:5]{index=5}

---

## Why were they introduced?

Neural networks cannot process discrete words directly.

Embeddings convert discrete tokens into continuous numerical representations that capture semantic information.

---

## How do they work?

1. Convert token IDs into dense vectors.
2. Scale embeddings by √dmodel.
3. Add positional encodings.
4. Feed the resulting vectors into the encoder or decoder.

---

## Advantages

- Dense semantic representation.
- Learned during training.
- Shared weights reduce model parameters.

---

## Limitations

- Require training data to learn meaningful representations.
- Similar words may not always be perfectly separated.

---

## Important Points

- Dimension = 512.
- Shared embedding weights.
- Combined with positional encodings.

---

## Keywords

Embedding

Token Representation

Word Embedding

Shared Weights

---

# Softmax Layer

## What is it?

The Softmax layer is the final component of the decoder.

It converts the output logits into a probability distribution over the vocabulary, allowing the model to predict the next token. :contentReference[oaicite:6]{index=6}

---

## Why was it introduced?

The decoder produces continuous-valued outputs.

These outputs must be transformed into probabilities so that the most likely next token can be selected.

---

## How does it work?

The decoder output passes through:

1. Linear Transformation
2. Softmax Function

The token with the highest probability is selected during decoding.

---

## Advantages

- Produces valid probability distributions.
- Enables next-token prediction.
- Supports beam search during inference.

---

## Limitations

- Computationally expensive for very large vocabularies.
- Probability calculation scales with vocabulary size.

---

## Important Points

- Final layer of the Transformer.
- Converts logits into probabilities.
- Used during every decoding step.

---

## Keywords

Softmax

Probability Distribution

Vocabulary

Next Token Prediction