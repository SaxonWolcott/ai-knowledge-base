---
description: Ingest a YouTube video into the wiki (interactive)
---

Ingest the YouTube video below into the wiki. This is the video-specific path of the
**Ingest** workflow in `CLAUDE.md` (§7/§8) — **interactive**: fetch the transcript, curate
which moments (if any) need their visuals captured, discuss takeaways, and only write pages
on my direction.

The default is **transcript-only** (free, fast, a true immutable `raw/` artifact). Visuals
are an **opt-in escalation** decided per-moment, not per-video. Never download the full
video unless we've agreed specific timestamps are worth a frame.

Video: $ARGUMENTS

## Procedure

### 1. Fetch metadata + transcript (NO video download)
```
yt-dlp --skip-download --write-info-json --write-auto-sub --write-sub \
  --sub-lang en --sub-format vtt \
  -o "raw/youtube/%(id)s/%(title)s.%(ext)s" <URL>
```
Prefer the human-authored subtitles (`.en.vtt`, not `.en.auto.vtt`) when both exist — they
have punctuation and speaker breaks. If **no captions exist at all**, stop and tell me: I can
clip a transcript with the Obsidian Web Clipper or paste one, mirroring the paywalled-page
fallback in §8.

### 2. Clean the transcript
```
python scripts/clean_vtt.py "raw/youtube/<id>/<title>.en.vtt" > "raw/youtube/<id>/transcript.md"
```
Keep the raw `.vtt` as the immutable source; the cleaned `transcript.md` sits alongside it.

### 2b. Slim the metadata, then delete the full dump
`--write-info-json` produces a ~10–15 MB file that's ~99% expiring format URLs + a replay
heatmap — worthless after ingest and ruinous to commit per-video. Extract the reusable fields
into a small `metadata.json` (≈5 KB), then delete the raw dump:
```
python -c "import json,glob,os; d=json.load(open(glob.glob('raw/youtube/<id>/*.info.json')[0],encoding='utf-8')); keep=['id','title','fulltitle','webpage_url','channel','channel_id','channel_url','uploader','uploader_id','uploader_url','upload_date','duration','duration_string','categories','tags','view_count','like_count','chapters','description','language']; json.dump({k:d[k] for k in keep if d.get(k) is not None}, open('raw/youtube/<id>/metadata.json','w',encoding='utf-8'), indent=2, ensure_ascii=False)"
```
Then remove the `*.info.json` (PowerShell `Remove-Item raw/youtube/<id>/*.info.json`). The
slim `metadata.json` keeps **chapters** (so frames can be re-grabbed later without re-fetching)
and the full description. `*.info.json` is gitignored as a backstop in case deletion is skipped.

### 3. Set the visual sensitivity — Gate A (the dial, from metadata)
Read `metadata.json` (title, description, **chapters**, categories, duration). This sets how
eager to be about grabbing frames — it does **not** decide on/off by itself:
- **Visual-rich formats** (slide talk, paper walkthrough, live-coding, whiteboard, demo,
  benchmark presentation) → **low bar**, grab on weaker signals.
- **Talking-head formats** (interview, podcast, panel, monologue) → **high bar**, grab only on
  strong or clustered signals.
- **Chapter titles override locally** — a "Results" / "Architecture" / "Demo" chapter lowers
  the bar just for that stretch, even inside a podcast.

### 4. Read the transcript fully and curate visual moments — Gate B (the trigger)
Read `transcript.md` end to end. A regex pre-pass (use Grep over the transcript) gives
high-recall candidates; **you** then curate with judgment. Caption signals, strongest first:
1. **Deictic / pointing:** "as you can see here", "this chart/figure/table", "the red line",
   "x-axis", "top-right", "highlighted", "shown here".
2. **Demo / code:** "let me show you", "if I click", "watch what happens", "line 40", "in the
   terminal".
3. **Structural:** "next slide", "moving on to", a slide title read aloud.
4. **Information absent from the words (most valuable):** the speaker references data/results
   the transcript never states — "look at *these* numbers", "the improvement is huge" — so the
   figure carries the payload. Only you can catch this; regex can't.

Governing principle (covers all four): **flag a moment when the transcript references
information that isn't recoverable from the words alone.** Resolve abstract "this" (an idea →
skip) vs. pointing "this" (something on screen → flag). Cluster nearby cues into one moment.

Present a **short** candidate list — `[mm:ss]` + the quoted line + one-line reason — and
**wait for my approval.** A talking-head video may legitimately yield zero; a slide talk
should yield the *informative* slides, not every slide.

### 5. On approval — capture the visuals (only now download a modest-res stream)
```
yt-dlp -f "bv*[height<=720]+ba/b[height<=720]" -o "raw/youtube/<id>/video.%(ext)s" <URL>
```
Find slide boundaries with scene detection, then snap each approved timestamp to the nearest
scene-change frame so we grab the settled slide, not a transition:
```
ffmpeg -i "raw/youtube/<id>/video.mp4" -vf "select='gt(scene,0.4)',showinfo" -vsync vfr -f null - 2>scenes.txt
ffmpeg -ss <ts> -i "raw/youtube/<id>/video.mp4" -frames:v 1 -q:v 2 "raw/youtube/<id>/frames/<ts>.jpg"
```
Read the extracted frames with the Read tool. Then **delete `video.*`** — `frames/`,
`transcript.md`, the raw `.vtt`, and the slim `metadata.json` are the retained artifacts.

### 6. Discuss combined takeaways
Following §8 step 3: surface what's new, what it connects to, what it contradicts, what
deserves a page — now informed by both transcript and any captured frames. **Wait for my
direction before writing pages.**

### 7. On approval, integrate (§8 step 4)
- Write the `sources/` page (see shape below); a video is a substantial source, so it gets a
  full page (unlike a tweet).
- Create/update relevant **entity** and **concept** pages; link liberally with `[[wikilinks]]`.
  Per §6: use `[[thing]]` only for things that are (or should become) their own page; for a
  concept you've decided lives as a *section* of another page, use a heading link
  `[[page#Heading|text]]` so it never auto-creates an empty page.
- Update `index.md` — Sources entry labeled `(YouTube)`.
- Append to `log.md`: `## [YYYY-MM-DD] ingest | <Video Title>`.
- If it contradicts an existing claim, document it under a `## Disputed` section on the
  concept page and add a one-liner to `contradictions.md`.
- Briefly report which pages you touched.

## Source-page shape
`wiki/sources/<kebab-title>.md`, matching the conventions in
`sources/attention-is-all-you-need.md` (frontmatter → one-sentence definition → sections →
`## Connections`). Frontmatter — standard source fields plus the YouTube ones:
```yaml
---
type: source
title: "<Video Title>"
date: YYYY-MM-DD
tags: [video, ...]
source-type: youtube-talk | youtube-lecture | youtube-paper-walkthrough | youtube-interview | youtube-podcast | youtube-demo
source-url: https://www.youtube.com/watch?v=<id>
author: [<Speaker(s)>]
channel: <Channel Name>
video-id: <id>
published: YYYY-MM-DD            # upload date
duration: <hh:mm:ss>
transcript: auto | manual        # auto-subs vs human-authored captions
visuals: captured | partial | none   # whether frames were grabbed for the visual moments
confidence: confirmed | contested | unverified
---
```
Set `confidence` per the §7 credibility nuance: a lab/conference talk is high-but-promotional;
a paper walkthrough inherits the paper's credibility; a speculative talking-head take is
tweet-tier — attribute its opinions to the speaker. When `visuals: none` or `partial` on a
visual-heavy talk, note in the page body what was not captured.
