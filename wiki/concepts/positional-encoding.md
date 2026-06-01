---
type: concept
title: Positional Encoding
date: 2026-05-28
tags: [attention, architecture, mechanism]
confidence: confirmed
---

# Positional Encoding

A signal added to token embeddings to inject information about token **order**, needed because [[self-attention]] is permutation-invariant and otherwise has no notion of position. Introduced in [[attention-is-all-you-need]] for the [[transformer]].

## Sinusoidal encoding (the original)

The paper adds fixed (non-learned) sinusoids of geometrically increasing wavelength to the input embeddings:

```
PE(pos, 2i)   = sin( pos / 10000^(2i/d_model) )
PE(pos, 2i+1) = cos( pos / 10000^(2i/d_model) )
```

Each dimension corresponds to a sinusoid; wavelengths form a geometric progression from 2π to ~10000·2π. The stated motivation: for any fixed offset `k`, `PE(pos+k)` is a *linear function* of `PE(pos)`, so the model can easily learn to attend by **relative** position. A secondary hypothesis was that fixed sinusoids might **extrapolate to longer sequences** than seen in training (hypothesized, not demonstrated in the paper — `confidence: confirmed` for the method, `unverified` for the extrapolation benefit).

## Learned vs sinusoidal

Table 3 ablation: **learned** positional embeddings perform nearly identically (25.7 vs 25.8 BLEU). The authors chose sinusoidal mainly for the possible length-extrapolation property, not a measured quality gain.

## Why it matters

Position handling became its own research thread — later models largely moved away from absolute additive encodings toward relative and rotary schemes. Those are out of scope for this source but worth their own pages.

## See also

- [[self-attention]] · [[transformer]]
- Source: [[attention-is-all-you-need]]
- Dangling / future: [[rotary-position-embedding]] (RoPE), [[relative-position-encoding]], [[alibi]]
