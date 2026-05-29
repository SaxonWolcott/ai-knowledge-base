---
description: Ingest a source into the wiki (interactive single source, or autonomous batch)
---

Ingest into the wiki by following the **Ingest** workflow in `CLAUDE.md` (§8). This command
has **two modes**, chosen by whether you were given an argument.

Argument: $ARGUMENTS

## Mode A — single source, INTERACTIVE (an argument is present)

`$ARGUMENTS` names a source (a file in `raw/`, a URL, or a tweet). Run the established
interactive flow: read the source fully, then **discuss the key takeaways with me and wait
for my direction before writing any pages.**

- If it's a URL, `WebFetch` it and save a markdown copy to `raw/` first. If `WebFetch` is
  blocked or returns junk, tell me to clip it with the Web Clipper.
- If it's a YouTube URL, this is the wrong command — redirect me to `/ingest-youtube`.
- If it's a tweet, treat it as a credibility-weighted claim per §7 — no source page.

## Mode B — batch, AUTONOMOUS (no argument)

Ingest **every new source in `raw/`** in one pass, **making all the editorial decisions
yourself**. Do **not** stop to discuss or ask for direction — I've delegated the judgment.
This is the bulk path; the per-source learning/control of Mode A is traded for throughput.

### 0. Materialize the YouTube inbox
`raw/youtube/inbox.md` is a queue of YouTube URLs I paste as I go (clips don't need this —
the Web Clipper drops them into `raw/clips/` already finished; only video needs a fetch step).
For each URL in the inbox whose `<id>` is **not** already a `raw/youtube/<id>/` directory,
run the `/ingest-youtube` fetch steps (1–2b: `yt-dlp` transcript + `clean_vtt.py` + slim
metadata) to materialize it — transcript-first, no video. A URL whose `<id>` dir already
exists is skipped (it was fetched on a prior run). If a video has no captions at all, leave
it and note it in the report. Then continue — the freshly fetched transcripts are now just
new `raw/youtube/<id>/` sources, picked up by step 1 like any other.

### 1. Find what's new
A raw source is "new" if it is **not** already represented in `index.md` (Sources) or by a
`## [date] ingest |` entry in `log.md`. Enumerate candidates and subtract what's ingested:
- `raw/clips/*.md` — match by title against the Sources list / source pages.
- `raw/youtube/<id>/` — match by `<id>` against the `video-id:` of existing source pages
  (and the `(YouTube)` Sources entries / log entries).
- `raw/tweets/*` (if any) — tweets never become source pages, so they won't appear in the
  Sources list; treat a tweet as new only if no matching `confidence: unverified` claim
  already exists on the relevant page.

List the new sources you found before integrating, so the final report is grounded.

### 2. Ingest each, autonomously
For each new source, run the right ingest path but **skip every interactive gate** — apply
your own judgment per the schema instead:
- **Clip / arXiv / blog / analysis** → §8 step 4 integration directly (no discussion).
- **YouTube** (`raw/youtube/<id>/`) → follow the `/ingest-youtube` mechanics, but make the
  **Gate A/Gate B visual-capture decision yourself** using the two-gate model — don't present
  a candidate list for approval. If a video has no transcript at all, skip it and note that
  in the report (you can't fabricate the source).
- **Tweet** → append a `confidence: unverified` attributed claim per §7; no page.

Decide page-vs-section, what to leave out, and credibility (`confidence:`) yourself.
Cross-reference **across the whole batch**, not just against the existing wiki — resolve
contradictions *among* the new sources too, since you're seeing them together.

### 3. Handle contradictions without me
When a source disputes an existing (or sibling-batch) claim, document it inline under a
`## Disputed` section on the concept page **and** add a one-liner to `contradictions.md` (§11).
You are trusted to make these calls; record them, don't escalate them.

### 4. Bookkeeping (once, covering the whole batch)
- Update `index.md` (§9) with every new entity / concept / source / analysis page.
- Append **one `## [YYYY-MM-DD] ingest |` entry per source** to `log.md` (§10) — keep the
  per-source granularity so the timeline stays greppable, even though it was one invocation.
- Then append **one short batch-summary entry**: `## [YYYY-MM-DD] ingest-batch | N sources`
  followed by a single line — the sources and any judgment calls to revisit. One line, not a
  recap of the per-source entries; this is the durable trace of the terminal report.

### 5. Report — surface the judgment calls
Briefly report: which sources were ingested, which pages each touched, and — most
importantly — a short list of the **decisions you made that I might want to revisit**:
contradictions logged, credibility downgrades, and any "deserves its own page vs. section"
coin-flips. This report is my review surface in lieu of the live discussion.
