---
type: special
title: Index
date: 2026-05-28
tags: [index]
---

# Index

Content catalog of the wiki. Each entry links to a page with a one-line summary. Read this
first when answering a query. Updated on every ingest. Organized by category.

## Entities

_Real-world things: models, labs, people, datasets, benchmarks, products._

- [[transformer]] — attention-only sequence architecture (Vaswani et al. 2017); foundation of modern LLMs.
- [[3blue1brown]] — Grant Sanderson's YouTube channel; animation-driven math/deep-learning explainers.
- [[mnist]] — classic 28×28 handwritten-digit dataset (784 pixels); the "hello world" of image classification.

## Concepts

_Ideas about how AI works: architectures, training, inference, agents, eval, interpretability, safety._

- [[neural-network]] — feedforward / MLP: layers of neurons, weighted-sum + bias + activation; the base architecture under modern deep learning.
- [[activation-function]] — the per-neuron nonlinearity ([[activation-function#Sigmoid|sigmoid]], [[activation-function#ReLU|relu]]); without it, stacked layers collapse to one linear map.
- [[self-attention]] — scaled dot-product attention; every position attends to every other. Core transformer primitive.
- [[multi-head-attention]] — h parallel attention heads over projected subspaces (h=8 in base transformer).
- [[positional-encoding]] — sinusoidal signal injecting token order into permutation-invariant attention.

## Sources

_One summary page per substantial source._

- [[but-what-is-a-neural-network]] — 3Blue1Brown, Deep Learning Ch.1 (2017). Structure of a feedforward net on MNIST digits. (YouTube)
- [[attention-is-all-you-need]] — Vaswani et al. 2017, arXiv:1706.03762. Introduces the transformer. (arXiv paper)

## Analysis

_Comparison and synthesis pages created from queries._

- [[transformers-explained-simply]] — plain-language transformer explainer for an entry-level AI developer. (synthesis)
