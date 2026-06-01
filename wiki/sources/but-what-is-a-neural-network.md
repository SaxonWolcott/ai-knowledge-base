---
type: source
title: "But what is a Neural Network? | Deep Learning Chapter 1"
date: 2026-05-29
tags: [video, neural-network, mlp, activation-function, mnist, education]
source-type: youtube-lecture
source-url: https://www.youtube.com/watch?v=aircAruvnKk
author: [Grant Sanderson]
channel: 3Blue1Brown
video-id: aircAruvnKk
published: 2017-10-05
duration: "18:40"
transcript: manual
visuals: captured
confidence: confirmed
---

# But what is a Neural Network? | Deep Learning Chapter 1

The opening video of [[3blue1brown]]'s deep-learning series — a from-scratch, animation-driven explanation of what a plain [[neural-network]] *is*, built around recognizing handwritten [[mnist]] digits, "not as a buzzword but as a piece of math."

> [[3blue1brown]] (Grant Sanderson), 2017-10-05, 18:40. Chapter 1 of the *Deep Learning* series; covers **structure** only — learning ([[backpropagation]], [[gradient-descent]]) is deferred to later chapters. Closing interview with Lisha Li (Amplify Partners). Visuals captured as frames; the rest of the field intuition is carried by the transcript.

## The setup

A digit is a 28×28 grayscale image = **784 pixels**. Writing a hand-coded program to map those pixels to a label 0–9 goes "from comically trivial to dauntingly difficult" — the motivation for learning the function instead. The video builds the **simplest plain-vanilla** feedforward network, explicitly a prerequisite for understanding modern variants.

## Structure: neurons and layers

A **neuron** is just "a thing that holds a number" between 0 and 1, called its **activation**. The network is layered:
- **Input layer:** 784 neurons, one per pixel (activation = grayscale value).
- **Two hidden layers** of 16 neurons each (an admittedly arbitrary choice — "16 was just a nice number to fit on the screen").
- **Output layer:** 10 neurons; the brightest is the network's guess.

Activations in one layer determine the next, loosely analogous to biological neurons firing.

![[05-05_architecture.jpg]]
*The 784→16→16→10 fully-connected structure, an input "2" feeding activations forward to the output layer (~5:05).*

## Why layers? (the motivating *hope*)

The aspiration: hidden layers detect a **hierarchy of abstractions**. A 9 = loop on top + line; a loop in turn = a set of little **edges**. So the second-to-last layer might fire on subcomponents (loops, lines), and the layer before it on edges, which combine up into digits. The same edges/abstraction idea generalizes to other image tasks and even speech.

> ⚠️ `confidence: contested` — Grant frames this explicitly as a **hope**, not what the trained network is shown to do: "Whether or not this is what our final network actually does is another question." Recorded here so the wiki doesn't treat the edge-detector story as established. See `## Disputed` on [[neural-network]].

![[07-10_cascade.jpg]]
*The abstraction hope: a loop decomposes into colored edges, a line into an edge (~7:10).*

## Mechanism: weights, bias, activation function

Each neuron computes a **weighted sum** of the previous layer's activations (one weight per connection), adds a **bias**, then passes the result through an **[[activation-function]]** to squish it back into [0,1].
- **Weights** can be visualized as a pixel grid — green = positive, red = negative. A neuron acts as an **edge detector** when it has positive weights in a region and negative weights around it, so the sum is largest for a bright stripe on a dark surround.
- **Bias** sets the threshold: how large the weighted sum must be before the neuron meaningfully activates.

![[09-50_weightgrid.jpg]]
*Weighted sum w₁a₁+…+wₙaₙ with weights as a green/red grid localized over a region of the image (~9:50).*

The video uses the **[[activation-function#Sigmoid|sigmoid]]** function σ(x)=1/(1+e⁻ˣ); the closing interview notes modern networks mostly use **[[activation-function#ReLU|relu]]** instead (much easier to train deep networks).

![[10-48_sigmoid.jpg]]
*The sigmoid / logistic curve squishing the real line into [0,1] (~10:48).*

## Scale and the linear-algebra view

The first→second layer connection alone is 784×16 weights + 16 biases; all told the network has **~13,000 weights and biases**. "Learning" means finding values for all of them.

The per-layer transition compresses to a single expression:

**a⁽¹⁾ = σ(W·a⁽⁰⁾ + b)**

— activations as a column vector, weights as a matrix (each row = one next-layer neuron's connections), bias as a vector, sigmoid applied componentwise. This is why "so much of machine learning just comes down to having a good grasp of linear algebra," and why matrix-multiply-optimized libraries make the code fast.

![[14-35_matrix.jpg]]
*The compact form σ(W·a + b) with the weight matrix × activation vector laid out (~14:35).*

## Key framings worth keeping

- A neuron is better thought of as a **function** of the previous layer's outputs; the whole network is "just a function" — 784 numbers in, 10 out — "an absurdly complicated function" with ~13,000 parameters.
- Building intuition for what weights/biases *mean* beats treating the network as a black box, both for debugging and for challenging assumptions about why it works.

## Connections

- Defines → [[neural-network]], [[activation-function]] (incl. [[activation-function#Sigmoid|sigmoid]], [[activation-function#ReLU|relu]]), the input dataset [[mnist]].
- Author/source → [[3blue1brown]] (Grant Sanderson).
- Upstream of the wiki's transformer content: the feed-forward sublayers of a [[transformer]] are MLPs, and the matrix-vector framing here is the same linear algebra behind attention's projections.
- Deferred to later chapters (dangling, for future ingests): [[backpropagation]], [[gradient-descent]], cost/loss functions.
