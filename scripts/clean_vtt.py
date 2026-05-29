#!/usr/bin/env python3
"""Clean a WebVTT subtitle file into readable Markdown.

Built for YouTube auto-generated captions, which are messy in two specific ways:
  1. Inline timing/styling tags inside cue text, e.g. ``hello<00:00:00.480><c> world</c>``.
  2. A rolling window where each cue repeats the previous line plus one newly revealed
     line, so naive concatenation duplicates almost everything.

This strips the tags, collapses the rolling duplicates (consecutive-line dedupe), and
re-flows the result into ~60-second paragraphs each prefixed with an ``[mm:ss]`` marker so
curated timestamps map back to the video.

Usage:
    python scripts/clean_vtt.py input.vtt [> output.md]

Pure standard library; no third-party dependencies.
"""

import html
import re
import sys

# Matches a cue timing line: "00:00:01.000 --> 00:00:03.000 align:start position:0%"
CUE_TIMING = re.compile(
    r"^(\d{2}):(\d{2}):(\d{2})\.\d{3}\s*-->\s*\d{2}:\d{2}:\d{2}\.\d{3}"
)
# Inline tags: <00:00:00.480>, <c>, </c>, <c.colorXXX>, etc.
INLINE_TAG = re.compile(r"<[^>]+>")
# Paragraph break cadence, in seconds.
PARAGRAPH_SECONDS = 60


def parse_cues(text):
    """Yield (start_seconds, [text_lines]) for each cue in the VTT body."""
    lines = text.splitlines()
    i = 0
    n = len(lines)
    while i < n:
        m = CUE_TIMING.match(lines[i].strip())
        if not m:
            i += 1
            continue
        hh, mm, ss = (int(g) for g in m.groups())
        start = hh * 3600 + mm * 60 + ss
        i += 1
        body = []
        while i < n and lines[i].strip() != "":
            body.append(lines[i])
            i += 1
        yield start, body


def clean_line(line):
    """Strip inline tags, unescape entities, collapse whitespace."""
    line = INLINE_TAG.sub("", line)
    line = html.unescape(line)
    return re.sub(r"\s+", " ", line).strip()


def dedupe(cues):
    """Flatten cues to (start_seconds, line), dropping consecutive duplicate lines.

    The rolling-window structure of auto-subs means each confirmed line appears twice in
    consecutive cues; collapsing consecutive duplicates removes the repetition while
    keeping genuine repeats that are separated by other text.
    """
    out = []
    last = None
    for start, body in cues:
        for raw in body:
            line = clean_line(raw)
            if not line or line == last:
                continue
            out.append((start, line))
            last = line
    return out


def format_timestamp(seconds):
    m, s = divmod(seconds, 60)
    if m >= 60:
        h, m = divmod(m, 60)
        return f"{h:d}:{m:02d}:{s:02d}"
    return f"{m:d}:{s:02d}"


def to_markdown(entries):
    """Group dedup'd lines into ~PARAGRAPH_SECONDS paragraphs with [mm:ss] markers."""
    if not entries:
        return ""
    paragraphs = []
    current = []
    para_start = entries[0][0]
    for start, line in entries:
        if current and start - para_start >= PARAGRAPH_SECONDS:
            paragraphs.append((para_start, " ".join(current)))
            current = []
            para_start = start
        current.append(line)
    if current:
        paragraphs.append((para_start, " ".join(current)))
    return "\n\n".join(
        f"[{format_timestamp(start)}] {body}" for start, body in paragraphs
    )


def main(argv):
    if len(argv) != 2:
        sys.stderr.write("usage: python clean_vtt.py input.vtt [> output.md]\n")
        return 2
    with open(argv[1], "r", encoding="utf-8") as fh:
        text = fh.read()
    markdown = to_markdown(dedupe(parse_cues(text)))
    sys.stdout.write(markdown + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
