---
description: Ask a question against the wiki
---

Answer the following question against the wiki using the **Query** workflow in `CLAUDE.md`
(§8): read `index.md` first to find relevant pages, drill into them, then synthesize an
answer with `[[links]]` and citations to the pages/sources you used.

## Grounding signal (§8 Query, step 3)

The answer should rest on the wiki. When a claim leans materially on your **training
knowledge** rather than a wiki page/source, flag it — don't suppress it and don't let it pass
as compiled knowledge:
- **Inline:** append a dagger `†` to the training-derived claim.
- **Footer note:** end the answer with one short note naming which parts are training-derived,
  then nudge — *the wiki is thin here; want me to research and ingest a source so this becomes
  compiled knowledge?*
- **Three states:** fully wiki-grounded → cite, no marker. Hybrid → cite grounded parts, dagger
  the rest + note. Wiki silent → lead with the note, then answer, then the research offer.
- Scope is this **answer** only — never write `†`-marked training content into a wiki page.

Render per tier: in-chat / markdown → dagger + a blockquote note; HTML → the `.ground-mark`
dagger + `.grounding` callout from the kit (see HTML conventions below).

## Output tier (§8 "Output formats")

Render format and persisting-as-knowledge are **two independent axes** — don't conflate them.

**Render** — pick the delivery tier:
- Default: answer **in-chat**.
- If the arguments contain `--md`, also write a markdown reading copy to
  `query-responses/<kebab-question>.md`.
- If the arguments contain `--html`, also write an HTML export to
  `query-responses/<kebab-question>.html`. Use HTML only when visuals earn the cost (diagrams,
  comparison tables, embedded `raw/youtube/<id>/frames/`). Follow the HTML conventions below.
- If no flag is given, answer in-chat and then **offer** the md/html exports.

Exports go in `query-responses/` (gitignored) — they are reading copies, **never** wiki pages.

**HTML conventions** (templates in `scripts/templates/`):
- Self-contained single file: **inline** the full `scripts/templates/query-kit.css` into a
  `<style>` block; use `query-skeleton.html` as the structural reference.
- Use the kit's 5 wiki-semantic components — citation, `confidence` badge, `## Disputed`
  callout, video-frame figure, training-derived grounding note (`.ground-mark` + `.grounding`).
  Design layout and any **diagrams bespoke per answer** (inline `<svg>` only — no CDN or JS
  libraries; it must render offline).
- Render `[[wikilinks]]` as `<span class="wikilink">name</span>` (styled plain text).
- QA before done: citations resolve to real pages/sources, every embedded image path exists,
  confidence badges sit on contested claims, `## Disputed` content is a callout, any training-
  derived claim has a `†` and a `.grounding` note, file renders offline (no network requests).

**Persist** — separately, if the answer is substantial or reusable, **offer to file it back**
as a `comparison`/`synthesis` page in `wiki/` so the exploration compounds (this
is the canonical wiki act; if filed, update `index.md` and `log.md`). This is independent of
which render tier was used.

Question: $ARGUMENTS
