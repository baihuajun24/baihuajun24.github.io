# baihuajun24.github.io

Personal academic homepage + MLSYS Feed podcast host, published via GitHub Pages from the `main` branch (no build step — every file is served as-is).

- Live site: https://baihuajun24.github.io/
- Podcast page: https://baihuajun24.github.io/podcast/ (RSS: `podcast/feed.xml`, consumed by Xiaoyuzhou)
- Podcast publishing workflow (episodes, RSS, GUIDs): see `podcast/AGENTS.md`

## Structure

- `index.html` / `index_zh.html` — English and Chinese homepages. Keep them in sync when editing content: every content change applies to both.
- `academic.css` — the homepages' stylesheet (linked with a `?v=YYYYMMDD` cache-buster; bump it in both homepages when the CSS changes).
- `style.css` — used only by `podcast/index.html` and `card.html`.
- `podcast/index.html` — renders the episode list client-side from `feed.xml`; needs no per-episode edits.
- `podcast/episodes.js` — auto-generated snapshot of `feed.xml` (fallback when `fetch` is unavailable, e.g. `file://`). Regenerate after every feed change (command in `podcast/AGENTS.md`).
- `podcast/audio/` — episode MP3s and show-notes markdown.

## Local preview

```bash
python3 -m http.server 8000   # from the repo root
# open http://localhost:8000/ and http://localhost:8000/podcast/
```

Do NOT judge the podcast page by opening files via `file://` — browsers block `fetch('feed.xml')` there (the page falls back to the `episodes.js` snapshot, which may be stale) and directory links resolve to folder listings instead of `index.html`.

Visual check with headless Edge (Google Chrome is NOT installed on this machine; Edge takes the same flags):

```bash
"/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" --headless --disable-gpu \
  --virtual-time-budget=5000 --window-size=1280,1400 \
  --screenshot=/tmp/page.png http://localhost:8000/podcast/
```

Caveats:
- Headless rendering shows fonts slightly narrower than the user's real browser — layouts that "just fit" in a screenshot may wrap on a real screen. Leave generous slack in flex rows.
- Narrow window sizes (e.g. `--window-size=390,...`) lay out ~20% wider than the window and clip the right edge — a headless quirk, not a real mobile-layout bug (the live site shows the same artifact). Don't chase it; test mobile layouts in a real browser's device mode.

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

## Where podcast audio lives

- Daily/regular episodes: assets on the `audio-archive` GitHub Release (not in git). A 265 MB checkout timed out the 10-minute Pages build (2026-08-06), so `podcast/audio/*.mp3` is gitignored. Release assets do not count toward the Pages build or repo size; per-file limit 2 GB; range requests work. Upload steps: `podcast/AGENTS.md`.
- `podcast/special/*.mp3` (~75 MB) stay in git only because their URLs were shared directly.
- Git history never shrinks: committing MP3s again would re-bloat every clone and the Pages build.
- If traffic ever outgrows GitHub, move enclosures to object storage (e.g. Cloudflare R2, free egress). GUIDs stay stable, so podcast apps won't duplicate episodes.
