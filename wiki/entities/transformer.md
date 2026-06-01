---
type: entity
title: Transformer
date: 2026-05-28
tags: [architecture, attention, model]
confidence: confirmed
---

# Transformer

The neural-network architecture, introduced in [[attention-is-all-you-need]] (Vaswani et al., 2017), that performs sequence transduction using **attention alone** — no recurrence, no convolution. It is the architectural foundation of essentially every modern large language model.

## Shape

An encoder-decoder, each a stack of **N = 6** identical layers in the original base model.

- **Encoder layer** = [[multi-head-attention]] ([[self-attention]]) sublayer → position-wise feed-forward sublayer. Each sublayer wrapped as `LayerNorm(x + Sublayer(x))`.
- **Decoder layer** = *masked* [[self-attention]] (causal — a position may only attend to earlier positions) → encoder-decoder *cross-attention* (queries from the decoder, keys/values from the encoder output) → feed-forward. Same residual + layer-norm wrapping.
- **Inputs:** token embeddings + [[positional-encoding]] (since attention is permutation-invariant, order must be injected).
- **Output:** linear projection + softmax over the vocabulary; the input/output embedding and pre-softmax weight matrices are tied.

## The three uses of attention

1. **Encoder self-attention** — each position attends to all positions in the previous encoder layer.
2. **Decoder masked self-attention** — each position attends only to earlier (and current) positions, preserving autoregressive ordering.
3. **Encoder-decoder cross-attention** — decoder queries attend over the full encoder output.

## Base hyperparameters

d_model = 512, layers = 6, heads = 8, d_k = d_v = 64, d_ff = 2048, dropout = 0.1. The "big" variant: d_model = 1024, heads = 16, d_ff = 4096, dropout = 0.3.

## Why it matters

The design choice that mattered was replacing sequential recurrence with attention: this gives **O(1) sequential operations** and **O(1) maximum path length** between any two tokens (vs O(n) for RNNs), making the architecture highly parallelizable and good at long-range dependencies. Its one structural cost is **O(n²·d)** compute per layer — quadratic in sequence length — which motivates much of the later [[efficient-attention]] / [[long-context]] literature.

The original transformer was an encoder-decoder for translation. Later models specialized the halves: **decoder-only** stacks (GPT family) for generative language modeling, **encoder-only** stacks (BERT) for representation learning. See [[attention-is-all-you-need]] for the originating results.

## See also

- [[self-attention]] · [[multi-head-attention]] · [[positional-encoding]]
- Originating source: [[attention-is-all-you-need]]
- Dangling / future: [[gpt]], [[bert]], [[decoder-only]], [[encoder-decoder]], [[layer-normalization]], [[residual-connections]]
