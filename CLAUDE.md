# baihuajun24.github.io

Personal academic homepage + MLSYS Feed podcast host, published via GitHub Pages from the `main` branch (no build step — every file is served as-is).

- Live site: https://baihuajun24.github.io/
- Podcast page: https://baihuajun24.github.io/podcast/ (RSS: `podcast/feed.xml`, consumed by Xiaoyuzhou)
- Podcast publishing workflow (episodes, RSS, GUIDs): see `podcast/AGENTS.md`

## Structure

- `index.html` / `index_zh.html` — English and Chinese homepages. Keep them in sync when editing content: every content change applies to both.
- `style.css` — shared by the homepages AND `podcast/index.html`. Layout changes here affect all pages.
- `podcast/index.html` — renders the episode list client-side from `feed.xml`; needs no per-episode edits.
- `podcast/episodes.js` — auto-generated snapshot of `feed.xml` (fallback when `fetch` is unavailable, e.g. `file://`). Regenerate after every feed change (command in `podcast/AGENTS.md`).
- `podcast/audio/` — episode MP3s and show-notes markdown.

## Local preview

```bash
python3 -m http.server 8000   # from the repo root
# open http://localhost:8000/ and http://localhost:8000/podcast/
```

Do NOT judge the podcast page by opening files via `file://` — browsers block `fetch('feed.xml')` there (the page falls back to the `episodes.js` snapshot, which may be stale) and directory links resolve to folder listings instead of `index.html`.

Visual check with headless Chrome:

```bash
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --virtual-time-budget=5000 --window-size=1280,1400 \
  --screenshot=/tmp/page.png http://localhost:8000/podcast/
```

Caveat: headless Chrome renders fonts slightly narrower than the user's real browser — layouts that "just fit" in a screenshot may wrap on a real screen. Leave generous slack in flex rows.

## Publishing

Pushing to `main` is publishing. There is no staging environment.

```bash
xmllint --noout podcast/feed.xml   # if the feed changed
git add <specific files>           # never `git add -A`: worktree often holds unrelated WIP
git commit && git push origin main
```

Deployment is the automatic "pages build and deployment" workflow — typically live in 1–3 minutes, occasionally queued for several. Verify:

```bash
curl -fsSL "https://api.github.com/repos/baihuajun24/baihuajun24.github.io/actions/runs?per_page=1" \
  | python3 -c "import json,sys; r=json.load(sys.stdin)['workflow_runs'][0]; print(r['status'], r['conclusion'], r['head_sha'][:7])"
curl -fsSL https://baihuajun24.github.io/ | grep -n "<something from the new change>"
```

Note: `gh` CLI is NOT installed on this machine — use `curl` against the GitHub API.

## Hosting MP3s on GitHub Pages

Fine at current scale, with known ceilings:

- Per-file hard limit 100 MB (episodes are ~5–10 MB — no issue).
- Repo/site size: ~1 GB recommended, 5 GB hard. Audio is ~73 MB as of June 2026; daily ~9 MB episodes reach 1 GB in roughly 3–4 months of daily publishing.
- Bandwidth: 100 GB/month soft limit — plenty for a small audience.
- Git history never shrinks: deleting old MP3s does not reclaim repo size without history rewriting, which would break clones.

When approaching ~1 GB, move audio to external object storage (e.g. Cloudflare R2, free egress) and point `<enclosure>` URLs there — GUIDs stay stable, so podcast platforms won't duplicate episodes. New episodes can switch immediately; old enclosure URLs should keep working.
