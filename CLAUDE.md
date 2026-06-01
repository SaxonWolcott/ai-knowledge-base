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
├─ scripts/            # helper scripts (e.g. clean_vtt.py — VTT→Markdown transcript cleaner)
│  └─ templates/      # query-kit.css + query-skeleton.html (HTML export kit — §8)
├─ query-responses/    # query export renders (md/html); gitignored, derived — NOT the wiki
├─ raw/               # immutable sources
│  ├─ clips/          # Obsidian Web Clipper saves
│  └─ youtube/<id>/   # per-video: raw .vtt, transcript.md, metadata.json (slim), frames/
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
YouTube source pages additionally add: `channel:`, `video-id:`, `duration:`,
`transcript: auto | manual`, and `visuals: captured | partial | none` (whether frames were
grabbed for the video's visual moments — see `/ingest-youtube`).
Apply `confidence: confirmed | contested | unverified` to a page or an individual claim
wherever credibility matters (especially anything sourced from a tweet).

## 6. Linking

- Link **liberally** with `[[wikilinks]]` (Obsidian style). Every entity/concept mention
  that has (or deserves) a page should be linked.
- **Dangling links are allowed** and encouraged as TODO markers — `[[constitutional-ai]]`
  before that page exists flags it as worth writing. Lint surfaces these. A dangling link is a
  promise that the concept **deserves its own page** that doesn't exist yet.
- **Page links vs. heading links — pick by intent, because a dangling link auto-creates an
  empty page in Obsidian when clicked:**
  - **Page link `[[thing]]`** — use when `thing` is (or should become) its own page. If it
    doesn't exist yet, that's an intentional TODO.
  - **Heading link `[[page#Heading|display text]]`** — use when the concept deliberately lives
    as a *section* of an existing page, not as its own page. It navigates to that section and
    creates nothing. Example: sigmoid/relu live as sections of `activation-function`, so link
    `[[activation-function#Sigmoid|sigmoid]]`, **not** `[[sigmoid]]`. Never leave a bare
    dangling link for something you've decided is a section — that falsely signals "write this
    page."
- Prefer linking to a page over re-explaining a concept inline.

## 7. Source-type / credibility table (drives ingest treatment)

| Source type        | Signal | Credibility            | Ingest treatment |
|--------------------|--------|------------------------|------------------|
| arXiv paper        | high   | high (but unreviewed)  | Full `sources/` page; extract claims, methods, ablations. |
| Lab blog / release | high   | high but promotional   | `sources/` page; flag marketing/unverified-benchmark claims. |
| Analysis / Substack| medium | varies                 | `sources/` page; attribute opinions to the author. |
| **YouTube video**  | high   | varies by format       | Full `sources/` page via `/ingest-youtube` (transcript-first, visuals opt-in). Credibility tracks the format: lab/conference **talk** ≈ lab blog (high but promotional); **paper walkthrough** inherits the paper's credibility; speculative **talking-head** take ≈ tweet-tier → attribute opinions to the speaker. Always record the `visuals:` flag. |
| **Tweet**          | low    | low                    | **No source page.** Append a `confidence: unverified` claim to the relevant concept/entity page, attributed to the author + link. |

This table is the heart of the wiki's judgment — a tweet is a flagged claim, not a page; a
video is transcript-first with visuals captured only where the transcript can't stand alone.

## 8. Operations

### Ingest (two modes — see `/ingest`)
`/ingest <source>` runs **Mode A** (interactive, single source) — the default below.
`/ingest` with **no argument** runs **Mode B** (autonomous batch) — ingest every new source
in `raw/` in one pass, making all editorial decisions yourself with no discussion gate. It
first **materializes the YouTube inbox** (`raw/youtube/inbox.md`, a queue of pasted video URLs
— the only source type needing a fetch step, since clips arrive finished): fetch the
transcript for any link not yet in `raw/youtube/<id>/`, then treat it as a new source. Detect
"new" by what's absent from `index.md` Sources + `log.md` ingest entries; log contradictions
to `contradictions.md` rather than escalating; write one `log.md` ingest entry per source plus
**one short `ingest-batch` summary line**; end with a terminal report surfacing the judgment
calls worth my review. The steps below describe Mode A; Mode B follows the same integration
(step 4) but skips step 3's discussion.

#### Mode A — interactive single source
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
   - **YouTube video** — `WebFetch` can't read video. Use **`/ingest-youtube`**, which pulls
     the transcript with `yt-dlp` (transcript-first; visuals captured as `ffmpeg` frames only
     for moments the transcript can't convey). A YouTube URL handed to `/ingest` should be
     redirected there. Full mechanics live in that command, not here.
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
3. **Mark the grounding (training-derived signal).** The wiki is compiled from `raw/` sources,
   and an answer should rest on it. When a claim leans materially on your **training knowledge**
   rather than a wiki page/source, don't suppress it — *flag* it: append a dagger `†` to the
   claim, and add one short note at the end of the answer that (a) names which parts are
   training-derived and (b) nudges — *the wiki is thin here; want me to research and ingest a
   source so this becomes compiled knowledge?* Three states:
   - **Fully wiki-grounded** → cite pages/sources as usual; no marker.
   - **Hybrid** → cite the grounded parts; dagger the training-derived ones + footer note.
   - **Wiki silent** → lead with the note ("the wiki doesn't cover this; the following is from
     my training, not compiled knowledge"), then answer, then the research offer — never present
     training facts as wiki knowledge.
   This applies to query **answers**; pages themselves stay strictly source-grounded.
4. **Offer to file good answers back** as a `comparison`/`synthesis` page so the exploration
   compounds — and if filed, update `index.md` and `log.md`.

#### Output formats (two independent axes — don't conflate them)
A query answer has two separate decisions: **how to render it** and **whether it becomes wiki
knowledge**. Keep them apart.

- **Persist-as-knowledge** is step 4 above: filing a `synthesis`/`comparison` page is the
  *canonical* act of compounding the wiki — integrated, `[[linked]]`, indexed, logged, living
  in `AI Knowledge Base/`. This is unchanged and is **not** the same as a markdown export.
- **Render format** is the delivery tier, and its outputs live in `query-responses/` (gitignored,
  derived) — **never** in `AI Knowledge Base/`, so they don't pollute the graph with unlinked
  duplicates that `/lint` would flag.

Three render tiers:
1. **In-chat** (default) — synthesize directly in the response. Simple; always available.
2. **Markdown export** — write `query-responses/<kebab-question>.md` for reading in Obsidian/
   browser when terminal output is hard to parse. A *reading copy*, not a synthesis page.
3. **HTML export** (opt-in, higher effort/cost) — write `query-responses/<kebab-question>.html`.
   Reserve for answers where **visuals earn the cost**: diagrams, comparison tables, or embedded
   YouTube frames from `raw/youtube/<id>/frames/`.

**Selecting a tier:** honor a `--md` / `--html` arg if given; otherwise answer in-chat, then
*offer* the exports. The synthesis-page offer (step 4) stays separate and intent-based.

**HTML conventions** (see `scripts/templates/`):
- **Self-contained single file** — inline `scripts/templates/query-kit.css`; **inline SVG** for
  any diagram (no CDN/JS libs — must render offline and when shared). Embed frames via relative
  `raw/youtube/<id>/frames/` paths, or base64 if the file will travel.
- **Thin shared kit, bespoke everything else** — use the kit's 5 wiki-semantic components
  (citation, `confidence` badge, `## Disputed` callout, video-frame figure, training-derived
  grounding note) for consistency and correct semantics; design layout, visual direction, and
  diagrams *freshly per answer*. The kit is recurring chrome, not a page template.
- **`[[wikilinks]]` render as styled plain text** (portable, non-clickable) — Obsidian linking
  doesn't work in a browser.
- **QA checklist before done:** citations resolve to real pages/sources; every embedded image
  path exists; `confidence` badges present on contested claims; `## Disputed` content rendered as
  callouts; any training-derived claim carries a `†` and a grounding note; file renders offline
  (no network requests).

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

**Current (Phase 1):** main agent only + four slash commands (`/ingest`, `/ingest-youtube`,
`/query`, `/lint`) + built-in `WebSearch`/`WebFetch`. One helper script (`scripts/clean_vtt.py`,
added for YouTube transcript cleanup — see below). No subagents, MCP, or hooks.

**Added:**
- **`/ingest-youtube` + `scripts/clean_vtt.py`** — YouTube is a primary knowledge source for
  the human. Transcript-first (`yt-dlp`, free, true `raw/` artifact); visuals captured as
  `ffmpeg` frames only for moments the transcript can't convey, decided interactively
  (two-gate model: format sets sensitivity, caption signals trigger). `clean_vtt.py` exists
  because deduping/cleaning rolling auto-sub VTT in-context is tedious and non-deterministic
  (§12's "when manual gets tedious" trigger). Gemini multimodal was rejected — derived (not
  raw) output + a billed dependency; revisit only if frame-grabbing proves insufficient.
- **Query output tiers + HTML kit (`scripts/templates/query-kit.css` + `query-skeleton.html`)**
  — terminal markdown is hard to parse for substantial answers, so `/query` can now export a
  markdown or HTML reading copy to `query-responses/` (gitignored, derived — distinct from a
  canonical synthesis page; see §8). The HTML kit is a *thin* set of design tokens + 4
  wiki-semantic components that get inlined into self-contained, offline single files; per-answer
  layout/diagrams stay bespoke. **Deferred trigger:** add an HTML *generator script* only if
  hand-assembling exports gets tedious (filling HTML is model work, not script work for now).

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
- **YouTube is transcript-first, visuals on-demand** (§7, `/ingest-youtube`) — the transcript
  is a true immutable `raw/` artifact; visuals are an opt-in escalation, captured as frames
  only where the transcript can't stand alone. The judgment of *when* to look at the visuals
  (two-gate model: format = sensitivity dial, caption signals = per-moment trigger, the key
  one being "information referenced but absent from the words") is curated interactively, same
  spirit as credibility-weighted tweet ingest. Gemini multimodal rejected: derived not raw,
  plus a billed dependency.
- **Interactive ingest is the per-source default; autonomous batch is the bulk path** —
  Mode A (`/ingest <source>`) discusses before writing, chosen for learning and control. But
  batching the *interaction* doesn't help: it just defers per-source Q&A to long after reading,
  when context has decayed. So Mode B (`/ingest`, no arg) trades that learning loop for
  throughput — ingest all new `raw/` sources autonomously, make every call yourself, and
  surface the judgment calls in a final report (the review surface in lieu of live discussion).
  Batching also *improves* synthesis: sources ingested together can be cross-referenced and
  their mutual contradictions resolved in one pass, which the one-at-a-time flow can't do.
- **Main-agent-only Phase 1** — subagents buy context isolation + parallelism, not token
  savings; a paper-reader subagent would strip raw material out of interactive discussion,
  and lint fan-out only pays off at scale. See §12 for when to revisit.
- **Query output: render format and persistence are two independent axes** (§8) — filing a
  synthesis page (compound the wiki) is orthogonal to how an answer is rendered (in-chat / md /
  html). Exports are *reading copies* in `query-responses/`, gitignored and kept out of the graph
  so they don't read as canonical knowledge or trip `/lint`'s orphan/duplicate checks. HTML uses
  a **thin component kit, not a rigid template** — standardizing only the recurring wiki-semantic
  chrome (citations, confidence badges, `## Disputed` callouts, video-frame figures, training-
  derived grounding notes) keeps docs consistent and semantically correct while leaving per-answer
  layout and *especially bespoke diagrams* fully expressive (the whole point of the higher-cost
  HTML tier). HTML is opt-in and reserved for answers where visuals earn the cost.
- **Grounding signal: flag training-derived claims, don't suppress them** (§8 Query) — the wiki's
  value is that knowledge is *compiled from `raw/` sources*, but the model's parametric knowledge
  is still useful for explanation and for answering where the wiki is thin. Rather than ban it
  (too strict — kills useful synthesis) or let it pass invisibly (the real hallucination risk —
  ungrounded, undated, knowledge-cutoff-bound claims masquerading as compiled knowledge), we
  *mark* it: a `†` on the claim plus a footer note. The note does double duty — honest disclosure
  **and** a lint-style nudge to go research+ingest a source, turning a wiki gap into an action.
  Scope is **query answers only**; pages stay strictly source-grounded (a marked-up page would
  blur the raw/wiki boundary the architecture rests on). Mirrors the spirit of credibility-
  weighted tweet ingest and `confidence:` — surface epistemic state, don't hide it.
