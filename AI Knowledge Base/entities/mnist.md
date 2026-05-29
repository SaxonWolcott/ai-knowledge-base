---
type: entity
title: MNIST
date: 2026-05-29
tags: [dataset, benchmark, vision, digits, foundations]
confidence: confirmed
---

# MNIST

The classic handwritten-digit dataset — **28×28 grayscale images** of digits 0–9 — used as the canonical "hello world" for introducing image classification and [[neural-network]]s.

## In this wiki

MNIST is the running example in [[but-what-is-a-neural-network]]: each image is flattened into **784** input activations (one per pixel, grayscale value as the activation), and the network outputs 10 numbers (one per digit class). Its small, fixed input size is what makes the ~13,000-parameter demo network tractable to reason about by hand.

## Connections

- Input to → [[neural-network]] (784-neuron input layer in the [[but-what-is-a-neural-network]] example).
- Source → [[but-what-is-a-neural-network]] ([[3blue1brown]]).
- Related / dangling (future): other vision benchmarks, the original LeCun et al. digit-recognition work.
