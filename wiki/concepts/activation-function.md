---
type: concept
title: Activation Function
date: 2026-05-29
tags: [neural-network, activation-function, sigmoid, relu, nonlinearity]
confidence: confirmed
---

# Activation Function

The nonlinear function applied to a neuron's weighted-sum-plus-bias in a [[neural-network]] — it both bounds/shapes the output and supplies the **nonlinearity** without which a stack of layers would collapse into a single linear map.

In the forward pass `a = f(W·x + b)`, the activation function is `f`. Two appear in the wiki's founding source [[but-what-is-a-neural-network]]: the historically dominant **sigmoid** and the modern default **ReLU**.

## Sigmoid

The **sigmoid** (logistic) function:

**σ(x) = 1 / (1 + e⁻ˣ)**

squishes the entire real line into (0,1): very negative inputs → ~0, very positive → ~1, with a smooth increase around 0. So a sigmoid activation reads as "how positive is the weighted sum." Historically motivated by the biological analogy of a neuron being inactive vs. active.

**Drawback:** its gradients saturate (flatten) for large-magnitude inputs, which makes deep networks hard to train — the motivation for moving away from it.

## ReLU

The **rectified linear unit**:

**ReLU(x) = max(0, x)**

Below a threshold the neuron is off (0); above it, it passes the value through (identity). Per the Lisha Li interview in [[but-what-is-a-neural-network]]: "relatively few modern networks actually use sigmoid anymore… ReLU seems to be much easier to train" for very deep networks — people "just tried ReLU and it happened to work very well." `confidence: confirmed` as the field's broad default circa the late 2010s onward.

## Why nonlinearity matters

Without a nonlinear `f`, composing linear layers (`W₂(W₁x) = (W₂W₁)x`) yields just another linear function — depth would buy nothing. The activation function is what lets stacked layers represent complex, non-linear decision boundaries.

## Connections

- Component of → [[neural-network]] (applied in the forward pass).
- Introduced via → [[but-what-is-a-neural-network]] ([[3blue1brown]]).
- Related / dangling (future): [[softmax]] (output-layer normalization), [[gelu]], the [[transformer]]'s feed-forward activations.
