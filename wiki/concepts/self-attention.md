---
type: concept
title: Self-Attention
date: 2026-05-28
tags: [attention, architecture, mechanism]
confidence: confirmed
---

# Self-Attention

A sequence-mixing operation in which every position attends to every other position in the *same* sequence, producing a representation of each token as a weighted blend of all tokens. It is the core primitive of the [[transformer]], introduced in [[attention-is-all-you-need]].

## Scaled dot-product attention

The transformer's attention is defined over queries `Q`, keys `K`, and values `V`:

```
Attention(Q, K, V) = softmax( Q·Kᵀ / √d_k ) · V
```

- Each query is compared to every key by dot product → a compatibility score.
- Scores are scaled by **`1/√d_k`**, softmax-normalized into weights, and used to take a weighted sum of the values.
- In *self*-attention, Q, K, and V are all linear projections of the same input sequence.

### Why the `1/√d_k` scaling

For large `d_k`, dot products grow large in magnitude (variance scales with d_k), pushing softmax into saturated regions where gradients are tiny. Dividing by `√d_k` rescales them back to unit-ish variance, keeping gradients healthy. (`confidence: confirmed` — this is the universally accepted justification, though the paper argues it by intuition rather than formal proof.)

Dot-product attention is used over additive attention because it is far faster and more memory-efficient in practice (matrix multiplication), and the scaling closes the quality gap that otherwise appears at large d_k.

## Masking (causal self-attention)

In the decoder, self-attention is **masked**: a position may only attend to itself and earlier positions (future scores set to −∞ before softmax). This preserves autoregressive ordering and is what makes decoder-only language models generate left-to-right. See [[transformer]] for the three places attention is applied.

## Why it beats recurrence (Table 1, [[attention-is-all-you-need]])

| | Sequential ops | Max path length |
|---|---|---|
| Self-attention | O(1) | O(1) |
| Recurrent | O(n) | O(n) |

Connecting all positions in **constant** sequential depth and **constant** path length is what makes self-attention parallelizable and good at long-range dependencies. The tradeoff is **O(n²·d)** compute per layer — quadratic in sequence length — the cost that later [[efficient-attention]] / [[long-context]] work tries to reduce.

## See also

- [[multi-head-attention]] — running self-attention in parallel subspaces
- [[transformer]] · [[positional-encoding]]
- Source: [[attention-is-all-you-need]]
