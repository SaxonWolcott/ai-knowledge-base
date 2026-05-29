# AI/LLM Knowledge Wiki — Maintainer Schema

This file is the **schema**: it configures you (Claude Code) as the disciplined maintainer
of this wiki. Read it at the start of every session. It defines the structure, conventions,
and the exact workflows to follow when ingesting sources, answering queries, and linting.

You own the wiki. The human owns sourcing, direction, and questions. You do the
summarizing, cross-referencing, filing, and bookkeeping — the work that makes a knowledge
base useful over time. The human reads; you write.

---

## 1. Purpose

A personal, compounding knowledge base about **AI and LLMs** — papers, lab blog posts,
analyses, release notes, and tweets — built on Andrej Karpathy's LLM-Wiki / Memex pattern
(see `llm-wiki.md`). Unlike RAG, knowledge is **compiled once and kept current**, not
re-derived per query. Every source you ingest makes the wiki richer; cross-references and
contradictions are resolved at ingest time, not rediscovered at query time.

It serves three goals simultaneously: (1) a genuinely useful second brain for tracking the
field, (2) a self-demonstrating portfolio artifact, and (3) a way to learn the LLM-wiki
pattern by operating it.

## 2. Architecture (three layers)

- **`raw/` — immutable sources.** The source of truth. Read from it; **never modify it.**
- **The wiki (`AI Knowledge Base/` + special pages) — LLM-owned.** Everything you create and maintain:
  entity pages, concept pages, source summaries, comparison/synthesis pages, and the special
  files (`index.md`, `log.md`, `overview.md`, `contradictions.md`).
- **The schema (this file) — config.** Co-evolved with the human. When a convention proves
  useful, write it here so future sessions follow it.

## 3. Directory layout

```
knowledge-base/
├─ CLAUDE.md            # this schema
├─ index.md            # content catalog (by category)
├─ log.md              # append-only chronological history
├─ overview.md         # living "state of the field" synthesis
├─ contradictions.md   # registry of disputed claims (links out)
├─ llm-wiki.md         # reference: the pattern this wiki implements
├─ raw/               # immutable sources
└─ AI Knowledge Base/  # the wiki (folder renamed from wiki/ in Obsidian)
   ├─ entities/        # real-world things
   ├─ concepts/        # ideas about how AI works
   └─ sources/         # one summary page per substantial source
```

## 4. Page types & conventions

- **entities/** — real-world things: models (`gpt-5.md`), labs (`anthropic.md`), people,
  datasets, benchmarks, products/tools.
- **concepts/** — ideas about how AI works: architectures (`mixture-of-experts.md`),
  training methods (`rlhf.md`, `dpo.md`), inference techniques, agents, evaluation,
  interpretability, safety.
- **sources/** — one summary page per substantial source (paper, blog post, analysis).
- **comparison / synthesis pages** — created from queries (e.g. `gpt5-vs-claude-opus.md`).
  File good query answers here so explorations compound (see §8 Query).

Conventions:
- **Filenames:** kebab-case, descriptive, no dates in the name.
- **New page vs. append:** create a new page when a thing/idea deserves to be linked to from
  elsewhere; otherwise add a section to the most relevant existing page. When unsure, prefer
  appending — orphans are worse than dense pages.
- Every page opens with frontmatter (§5) and a one-sentence definition line.

## 5. Frontmatter spec (YAML — enables Obsidian Dataview)

Every page starts with:
```yaml
---
type: entity | concept | source | comparison | synthesis | special
title: Human Readable Title
date: YYYY-MM-DD            # created/last-major-update
tags: [model, lab, ...]
---
```
Source pages add: `source-type:`, `source-url:`, `author:`, `published:`.
Apply `confidence: confirmed | contested | unverified` to a page or an individual claim
wherever credibility matters (especially anything sourced from a tweet).

## 6. Linking

- Link **liberally** with `[[wikilinks]]` (Obsidian style). Every entity/concept mention
  that has (or deserves) a page should be linked.
- **Dangling links are allowed** and encouraged as TODO markers — `[[constitutional-ai]]`
  before that page exists flags it as worth writing. Lint surfaces these.
- Prefer linking to a page over re-explaining a concept inline.

## 7. Source-type / credibility table (drives ingest treatment)

| Source type        | Signal | Credibility            | Ingest treatment |
|--------------------|--------|------------------------|------------------|
| arXiv paper        | high   | high (but unreviewed)  | Full `sources/` page; extract claims, methods, ablations. |
| Lab blog / release | high   | high but promotional   | `sources/` page; flag marketing/unverified-benchmark claims. |
| Analysis / Substack| medium | varies                 | `sources/` page; attribute opinions to the author. |
| **Tweet**          | low    | low                    | **No source page.** Append a `confidence: unverified` claim to the relevant concept/entity page, attributed to the author + link. |

This table is the heart of the wiki's judgment — a tweet is a flagged claim, not a page.

## 8. Operations

### Ingest (INTERACTIVE — the default)
1. Locate the source. Sources reach `raw/` by one of three paths:
   - **Already clipped** — the human may have used the **Obsidian Web Clipper** browser
     extension to save the page as markdown into `raw/`. This is the preferred path for
     paywalled, login-gated, or JavaScript-heavy pages that programmatic fetching can't
     reach. Check `raw/` for the file before fetching anything.
   - **URL given to you** — for open, simple pages (e.g. arXiv), `WebFetch` it and save a
     markdown copy to `raw/` yourself (filename = kebab-case title). If `WebFetch` is blocked
     or returns junk, tell the human to clip it with the Web Clipper instead.
   - **Tweet** — save the text to `raw/tweets/` or just work from the pasted text; no `raw/`
     file required for a one-liner.
2. Read it fully.
3. **Discuss key takeaways with the human and wait for direction before writing pages.**
   Surface: what's new, what it connects to, what it contradicts, what's worth a page.
4. On approval, integrate (a single source may touch 10–15 pages):
   - Write/update the `sources/` summary page (skip for tweets — see §7).
   - Create/update relevant **entity** and **concept** pages; add `[[links]]`.
   - Update `index.md` (§9).
   - Append an entry to `log.md` (§10).
   - If it contradicts an existing claim, document the dispute inline under a `## Disputed`
     section on the concept page **and** add a one-liner to `contradictions.md` (§11).
5. Briefly report which pages you touched.

### Query
1. Read `index.md` first to find relevant pages, then drill into them.
2. Synthesize an answer with `[[links]]` / citations to the pages and sources used.
3. **Offer to file good answers back** as a `comparison`/`synthesis` page so the exploration
   compounds — and if filed, update `index.md` and `log.md`.

### Lint (health check — report, don't auto-fix without approval)
Scan for: orphan pages (no inbound links), dangling `[[links]]` worth creating, stale/
superseded claims, unresolved contradictions, concepts mentioned but lacking a page, missing
cross-references, and data gaps fillable via `WebSearch`. Suggest new questions to
investigate and sources to find. Present findings as a list; act only on approval. Append a
lint entry to `log.md`.

## 9. Index conventions (`index.md`)

Content-oriented catalog, organized by category (**Entities / Concepts / Sources /
Analysis**). Each entry = `[[link]]` + a one-line summary, optionally with date/source-count.
Update it on **every** ingest. When answering a query, read it first.

## 10. Log conventions (`log.md`)

Append-only, chronological. Each entry begins with a consistent prefix so it's greppable:
```
## [YYYY-MM-DD] ingest | Source Title
## [YYYY-MM-DD] query  | The question
## [YYYY-MM-DD] lint   | summary of findings
```
`grep "^## \[" log.md` (or the Grep tool) yields a timeline. Keep entries to 1–3 lines.

## 11. Contradictions registry (`contradictions.md`)

A lightweight dashboard, **not** a content store. Each line is a one-liner that links out to
the concept page where the dispute is documented in full under its `## Disputed` section.
Example: `- [[rlhf]] — does RLHF degrade calibration? Paper A says yes, Paper B's ablation says no.`
When a dispute is resolved by a newer source, move it to a `## Resolved` section with the
resolution.

## 12. Tooling status & roadmap

**Current (Phase 1):** main agent only + three slash commands (`/ingest`, `/query`,
`/lint`) + built-in `WebSearch`/`WebFetch`. No subagents, MCP, scripts, or hooks.

**Deferred — add only when the wiki demands it (record the trigger):**
- **Lint fan-out subagent (`model: haiku`)** — when the wiki passes ~100 pages or `/lint`
  gets slow. Lint is read-only + parallelizable, the ideal subagent job; Haiku is cheap and
  enough for orphan/contradiction scans. (Note: Claude Code can only set a subagent to
  `haiku|sonnet|opus|inherit` — it cannot route a single subagent to OpenRouter/non-Claude.)
- **`qmd` MCP hybrid search** — when `index.md` outgrows itself (hundreds of pages) and
  catalog-based lookup stops being enough.
- **Helper CLI scripts** — orphan/dangling-link checker, frontmatter validator, recent-log
  viewer — when manual checking via Grep/Glob gets tedious.
- **settings.json hooks** (auto-log, lint nudges) — once the schema/workflow is stable.

Avoid building these prematurely — Karpathy's point is the index + a good schema goes far.

## 13. Design decisions (the "why", preserved across sessions)

- **Topic is AI/LLMs itself** — collapses "useful to me", "portfolio piece", and "learn the
  pattern" into one artifact.
- **Three backbone page types** (entities / concepts / sources) + ad-hoc comparison/synthesis
  from queries. `index`, `log`, `overview` are Karpathy's; `contradictions` is an added
  lightweight registry.
- **`open-questions.md` was considered and rejected** — too easily becomes stale busywork;
  do not create it.
- **Tweets are claims, not pages** (§7) — credibility-weighted ingest is the wiki's core
  judgment and the most interesting thing to get right.
- **Interactive ingest** — chosen for learning and control; you discuss before writing.
- **Main-agent-only Phase 1** — subagents buy context isolation + parallelism, not token
  savings; a paper-reader subagent would strip raw material out of interactive discussion,
  and lint fan-out only pays off at scale. See §12 for when to revisit.
