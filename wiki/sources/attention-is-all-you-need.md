---
type: source
title: "Attention Is All You Need"
date: 2026-05-28
tags: [paper, architecture, attention, transformer, machine-translation]
source-type: arxiv-paper
source-url: https://arxiv.org/abs/1706.03762
author: [Ashish Vaswani, Noam Shazeer, Niki Parmar, Jakob Uszkoreit, Llion Jones, Aidan N. Gomez, Lukasz Kaiser, Illia Polosukhin]
published: 2017-06-12
confidence: confirmed
---

# Attention Is All You Need

The 2017 paper that introduced the **[[transformer]]**, a sequence-transduction architecture built entirely from attention, dispensing with recurrence and convolution — the architectural ancestor of essentially every modern LLM.

> Authors: [[Ashish Vaswani]], [[Noam Shazeer]], [[Niki Parmar]], [[Jakob Uszkoreit]], [[Llion Jones]], [[Aidan N. Gomez]], [[Lukasz Kaiser]], [[Illia Polosukhin]] (Google Brain / Google Research / [[University of Toronto]]). arXiv:1706.03762.

## The core claim

Prior best sequence-transduction models were recurrent or convolutional encoder-decoders connected by an attention mechanism. This paper removes everything except the attention: the [[transformer]] is "based solely on attention mechanisms, dispensing with recurrence and convolutions entirely." The payoff is **parallelizability** (no sequential dependency along the sequence) and **shorter path length** between any two positions, which together make training faster and long-range dependencies easier to learn.

## Key contributions

- **[[self-attention]]** as the sole sequence-mixing primitive, via *scaled dot-product attention*: `Attention(Q,K,V) = softmax(QKᵀ/√d_k)·V`. The `1/√d_k` factor keeps dot products from growing large and pushing softmax into low-gradient regions.
- **[[multi-head-attention]]** — h parallel attention heads operating on learned low-dimensional projections, letting the model attend to different representation subspaces at once.
- **[[positional-encoding]]** — fixed sinusoidal signals added to inputs to inject order, since attention is otherwise permutation-invariant.
- A complexity argument (Table 1) for why self-attention beats recurrence and convolution on **sequential operations** and **maximum path length**.

## Architecture (base model)

Encoder-decoder, both stacks of **N = 6** identical layers. See [[transformer]] for the full breakdown.

| Hyperparameter | Base | Big |
|---|---|---|
| d_model | 512 | 1024 |
| layers (N) | 6 | 6 |
| heads (h) | 8 | 16 |
| d_k = d_v | 64 | 64 |
| d_ff | 2048 | 4096 |
| dropout | 0.1 | 0.3 |

Each sublayer is wrapped as `LayerNorm(x + Sublayer(x))` (residual connection then layer norm).

## Why self-attention (Table 1)

| Layer type | Complexity per layer | Sequential ops | Max path length |
|---|---|---|---|
| **Self-Attention** | O(n²·d) | **O(1)** | **O(1)** |
| Recurrent | O(n·d²) | O(n) | O(n) |
| Convolutional | O(k·n·d²) | O(1) | O(log_k n) |

Self-attention connects all positions with a constant number of sequential operations and a constant maximum path length — that is the architecture's central advantage. The cost is **O(n²·d)** per-layer compute, quadratic in sequence length `n`; this is the seed of the entire later literature on efficient/long-context attention.

## Training setup

- **Data:** WMT 2014 EN-DE (~4.5M sentence pairs, 37K BPE vocab); WMT 2014 EN-FR (36M sentences, 32K word-piece vocab).
- **Hardware:** 8× NVIDIA P100 GPUs, single machine. Base = 100K steps ≈ 12 hours; big = 300K steps ≈ 3.5 days.
- **Optimizer:** Adam (β₁=0.9, β₂=0.98, ε=10⁻⁹) with a warmup schedule: `lrate = d_model^(-0.5) · min(step^(-0.5), step·warmup^(-1.5))`, warmup_steps = 4000.
- **Regularization:** residual dropout P_drop = 0.1 (0.3 for big/parsing); **label smoothing** ε_ls = 0.1 (hurts perplexity but improves BLEU and accuracy).

## Results

| Task (newstest2014) | Base BLEU | Big BLEU | Prior SOTA |
|---|---|---|---|
| EN→DE | 27.3 | **28.4** | beats prior best (incl. ensembles) by >2 BLEU |
| EN→FR | 38.1 | **41.8** | new single-model SOTA, <1/4 the training cost |

Big-model training cost ≈ **2.3×10¹⁹ FLOPs** — a small fraction of prior SOTA models.

**Generalization:** a 4-layer transformer (d_model=1024) on English constituency parsing (Penn Treebank WSJ) reached **91.3 F1** (WSJ-only) and **92.7 F1** (semi-supervised), competitive with task-specific models despite minimal tuning.

## Key ablations (Table 3)

- **Heads:** single head is 0.9 BLEU worse than 8; too many heads also degrades. Quality is non-monotonic in h.
- **Key dimension:** reducing d_k hurts — dot-product compatibility benefits from sufficient dimensionality.
- **Model size:** bigger is better (consistent across rows).
- **Dropout:** essential — removing it drops ~1.2 BLEU.
- **Positional encoding:** learned positional embeddings perform nearly identically (25.7 vs 25.8 BLEU) to sinusoidal. <span title="claim">`confidence: confirmed` but note the sinusoidal "extrapolates to longer sequences" benefit was hypothesized, not demonstrated here.</span>

## Notable nuances / caveats

- The justification that `1/√d_k` "counteracts vanishing softmax gradients" is asserted with an intuition, not a formal proof — widely accepted but worth flagging (`confidence: confirmed` claim, informal derivation).
- The sinusoidal-vs-learned choice was largely a wash empirically; the stated motivation (extrapolation to longer sequences) was a hypothesis.
- Results are on machine translation + parsing only — the leap to general language modeling came later (GPT, BERT), not in this paper.

## Connections

- Introduces → [[transformer]], [[self-attention]], [[multi-head-attention]], [[positional-encoding]].
- Downstream (dangling, for future ingests): [[layer-normalization]], [[residual-connections]], [[encoder-decoder]], [[byte-pair-encoding]], [[label-smoothing]], [[learning-rate-warmup]], the O(n²) cost motivating [[efficient-attention]] / [[long-context]].
