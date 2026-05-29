---
type: special
title: Log
date: 2026-05-28
tags: [log]
---

# Log

Append-only chronological record of what happened to the wiki. Each entry starts with a
consistent prefix so it's greppable: `grep "^## \[" log.md`.

## [2026-05-28] scaffold | wiki initialized

Created the wiki skeleton: `CLAUDE.md` schema, `index.md`, `log.md`, `overview.md`,
`contradictions.md`, the `raw/` and `wiki/{entities,concepts,sources}/` directories, and the
`/ingest`, `/query`, `/lint` slash commands. No sources ingested yet.

## [2026-05-28] ingest | Attention Is All You Need

First source. Created `sources/attention-is-all-you-need.md`, `entities/transformer.md`, and
concepts `self-attention`, `multi-head-attention`, `positional-encoding`. Authors + lab left as
dangling links (TODO markers) for lint to surface. No contradictions. Updated `index.md`.

## [2026-05-28] query  | Summarize transformers with as little jargon as possible

Filed answer as synthesis page `synthesis/transformers-explained-simply.md` (entry-level
explainer). Updated `index.md` (Analysis). Also: noted `wiki/` was renamed to `AI Knowledge
Base/` in Obsidian and updated `CLAUDE.md` §2/§3 to match.

## [2026-05-29] schema  | Added YouTube ingest path

Built `/ingest-youtube` (transcript-first via `yt-dlp`; visuals opt-in via `ffmpeg` frames,
two-gate model) + `scripts/clean_vtt.py` (VTT→Markdown cleaner). Updated `CLAUDE.md` §3/§5/§7/
§8/§12/§13 and `.gitignore` (ignore transient `raw/youtube/**/video.*`). First implementation
of the deferred "helper CLI scripts" item in §12.

## [2026-05-29] ingest | But what is a Neural Network? (3Blue1Brown, DL Ch.1)

First YouTube ingest (id `aircAruvnKk`). Manual captions → `transcript.md`; captured 5 frames
(architecture, edge-cascade, weight grid, sigmoid curve, matrix-vector form), video discarded.
Created `sources/but-what-is-a-neural-network`, concepts `neural-network` + `activation-function`
(sigmoid/relu as sections), entities `3blue1brown` + `mnist`. Logged a contradiction: the
edges→subcomponents "hope" is contested as a literal description of learned representations.
Updated `index.md` and `contradictions.md`. Dangling TODOs left: `backpropagation`,
`gradient-descent`, `sigmoid`, `relu`, `softmax`.
