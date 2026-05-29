---
type: concept
title: Neural Network (Feedforward / MLP)
date: 2026-05-29
tags: [architecture, neural-network, mlp, deep-learning, foundations]
confidence: confirmed
---

# Neural Network (Feedforward / MLP)

A neural network is a parameterized function built from layers of **neurons**, where each neuron's **activation** is a weighted sum of the previous layer's activations plus a bias, passed through an **[[activation-function]]** — the foundational architecture underlying modern deep learning, including the [[transformer]].

## Neurons, layers, activations

A **neuron** holds a single number, its **activation** (in the basic case, squished to [0,1]). Neurons are organized into **layers**:
- **Input layer** — activations set directly by the data (e.g. 784 pixel values for a 28×28 [[mnist]] digit).
- **Hidden layers** — intermediate layers; their count and width are design choices.
- **Output layer** — activations interpreted as the answer (e.g. 10 neurons for digit classes).

In a **fully-connected** (dense) layer, every neuron connects to every neuron in the previous layer. This plain feedforward network is also called a **multilayer perceptron (MLP)**.

## The forward pass

Each non-input neuron computes:

**a⁽ˡ⁾ = f(W⁽ˡ⁾·a⁽ˡ⁻¹⁾ + b⁽ˡ⁾)**

where `W` is the weight matrix (each row = one neuron's incoming connections), `b` the bias vector, and `f` an [[activation-function]] applied componentwise. Stacking these per-layer transitions propagates activations from input to output. The whole network is therefore **just a function** — a fixed number of inputs to a fixed number of outputs — albeit one with many thousands of parameters.

- **Weights** encode *what pattern* a neuron responds to. Visualized as a grid, positive/negative weights in a center/surround arrangement make a neuron act as an **edge detector**.
- **Bias** encodes *how high* the weighted sum must be before the neuron activates — a threshold.

## Parameters and "learning"

The parameters are all the weights and biases. The small [[mnist]] network in [[but-what-is-a-neural-network]] has **~13,000** of them (e.g. 784×16 + 16 for just the first transition). **Learning** = finding parameter values that make the network solve the task — covered by [[backpropagation]] and [[gradient-descent]] (not on this page yet).

## Why layers? (abstraction hierarchy)

The standard intuition: successive layers capture increasing levels of abstraction — pixels → edges → subcomponents (loops, lines) → digits — and this layered abstraction generalizes across perception tasks (e.g. audio → phonemes → words). This motivates depth.

## Disputed

**Does a trained network's hidden layer actually learn the clean edge/subcomponent detectors the layered structure hopes for?** [[but-what-is-a-neural-network]] presents the edges→loops→digits story explicitly as a *hope* used to motivate the architecture, and flags that whether the trained network does this is "another question" — later 3Blue1Brown material shows the learned weights look far messier than tidy edge detectors. So: the abstraction hierarchy is a useful *design intuition*, `confidence: contested` as a literal *description* of what trained networks represent. See [[contradictions]].

## Connections

- Built from → [[activation-function]] ([[activation-function#Sigmoid|sigmoid]], [[activation-function#ReLU|relu]]).
- Trained by → [[backpropagation]], [[gradient-descent]] (dangling; future ingests).
- Introduced in the wiki via → [[but-what-is-a-neural-network]] ([[3blue1brown]]).
- Generalizes to → [[transformer]] (its feed-forward sublayers are MLPs; attention adds learned input-dependent mixing on top of this base).
