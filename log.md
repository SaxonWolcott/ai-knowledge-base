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
