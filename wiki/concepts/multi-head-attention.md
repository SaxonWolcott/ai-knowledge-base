---
type: concept
title: Multi-Head Attention
date: 2026-05-28
tags: [attention, architecture, mechanism]
confidence: confirmed
---

# Multi-Head Attention

Running [[self-attention]] **h times in parallel** on different learned linear projections of the input, then concatenating and re-projecting the results. Introduced in [[attention-is-all-you-need]] as the attention block of the [[transformer]].

## How it works

Instead of one attention function over full d_model-dimensional queries/keys/values:

1. Linearly project Q, K, V `h` times into lower-dimensional spaces (each of size d_k, d_k, d_v) with separate learned matrices.
2. Apply scaled dot-product [[self-attention]] independently in each of the `h` heads.
3. Concatenate the `h` outputs and project once more with `Wᴼ`.

In the base [[transformer]]: **h = 8** heads, with d_k = d_v = d_model/h = **64**. Because each head is low-dimensional, the total cost is similar to single full-dimensional attention.

## Why multiple heads

> "Multi-head attention allows the model to jointly attend to information from different representation subspaces at different positions."

A single attention head averages over positions, which can blur distinct relationships; splitting into heads lets different heads specialize (e.g., syntactic vs positional vs coreference patterns).

## Ablation evidence

From Table 3 of [[attention-is-all-you-need]]: head count is **non-monotonic** — a single head is ~0.9 BLEU worse than 8 heads, but using too many heads also degrades quality. Eight was the sweet spot for the base model; the "big" model used 16.

## See also

- [[self-attention]] · [[transformer]]
- Source: [[attention-is-all-you-need]]
- Dangling / future: [[attention-head-interpretability]]
