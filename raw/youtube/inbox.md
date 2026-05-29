# YouTube inbox

Paste YouTube URLs here (one per line) as you find videos worth ingesting. They sit as plain
links — no transcript is fetched yet. When you run `/ingest` with no argument (Mode B), it
materializes each link it hasn't fetched before (`yt-dlp` transcript → `raw/youtube/<id>/`)
and then ingests it autonomously.

This is the only source type that needs a queue: clips (arXiv, blogs, etc.) land in
`raw/clips/` already finished via the Web Clipper, but a video has to be fetched first.

Lines starting with `#` are ignored. Processed links are safe to leave — re-running won't
re-fetch a video already in `raw/youtube/<id>/`.

## Queue
