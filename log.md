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
