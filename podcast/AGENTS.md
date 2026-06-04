# Podcast Publishing Agent

This directory is the public RSS publishing surface for MLSYS Feed.

The agent working here owns RSS publishing, GitHub Pages deployment checks, and Xiaoyuzhou RSS-subscription hygiene. Other agents may deliver finished audio and show notes into this directory, but this agent is responsible for turning those artifacts into a valid public podcast feed.

## Program Identity

- Podcast title: `MLSYS Feed`
- Host/author: `小白超 AI算`
- Public feed URL: `https://baihuajun24.github.io/podcast/feed.xml`
- Public landing page: `https://baihuajun24.github.io/podcast/`
- Cover image: `https://baihuajun24.github.io/podcast/logo.jpg`
- Local repo: `/Users/huajun/Documents/baihuajun24.github.io`
- Local podcast directory: `/Users/huajun/Documents/baihuajun24.github.io/podcast`

## Role

Act as the publishing and RSS operations agent.

When given new audio and notes:

1. Add the MP3 under `podcast/audio/`.
2. Add or preserve the source show-notes markdown under `podcast/audio/` or another clear podcast-local path.
3. Insert a new topmost `<item>` in `podcast/feed.xml`.
4. Update `lastBuildDate` and the landing page latest-episode pointer in `podcast/index.html`.
5. Validate the XML.
6. Commit and push the update to GitHub Pages.
7. Verify the public feed and MP3 URLs after Pages cache/deployment catches up.

## Episode Conventions

Use date-first filenames and stable RSS identifiers.

- Audio filename: `MMDD-daily-arxiv.mp3`, for example `0605-daily-arxiv.mp3`
- Notes filename: keep the delivered name if it is descriptive, for example `0605_show_notes_meta_20260604.md`
- Episode title should include the date and technical hooks, for example:
  `0605 MLSYS 论文简报：D²SD、Agent Safety 与 LLM Error Propagation`
- Episode GUID format:
  `mlsys-feed-YYYY-MM-DD`
- The GUID is the stable episode identity. Never change an existing episode GUID after publishing, or podcast platforms may duplicate the episode.
- The newest episode should appear before older `<item>` entries.

## Time And Scheduling

For a Xiaoyuzhou-style 08:30 China-time publication:

- Use `Asia/Shanghai` target time: `YYYY-MM-DD 08:30`
- RSS `pubDate` must be GMT/UTC.
- Example: `2026-06-05 08:30` China time is:
  `Fri, 05 Jun 2026 00:30:00 GMT`

If the user says "tomorrow 08:30", resolve it against the current date/time and state the exact calendar date before publishing.

## RSS Item Template

Use this shape for each episode:

```xml
    <item>
      <title>0605 MLSYS 论文简报：D²SD、Agent Safety 与 LLM Error Propagation</title>
      <description><![CDATA[...show notes markdown...]]></description>
      <content:encoded><![CDATA[...show notes markdown...]]></content:encoded>
      <pubDate>Fri, 05 Jun 2026 00:30:00 GMT</pubDate>
      <guid isPermaLink="false">mlsys-feed-2026-06-05</guid>
      <enclosure url="https://baihuajun24.github.io/podcast/audio/0605-daily-arxiv.mp3" length="9421868" type="audio/mpeg" />
      <itunes:duration>09:48</itunes:duration>
      <itunes:explicit>false</itunes:explicit>
    </item>
```

Set `length` from the actual MP3 byte size:

```bash
stat -f '%z' podcast/audio/0605-daily-arxiv.mp3
```

Keep `itunes:duration` aligned with the notes or audio metadata.

## Validation

Before committing:

```bash
xmllint --noout podcast/feed.xml
git diff --stat
git diff -- podcast/feed.xml podcast/index.html
```

After pushing:

```bash
curl -fsSL https://baihuajun24.github.io/podcast/feed.xml | rg -n "0605|mlsys-feed-2026-06-05|0605-daily-arxiv"
curl -I -L https://baihuajun24.github.io/podcast/audio/0605-daily-arxiv.mp3
```

GitHub Pages may serve the previous version for a minute or two. If the raw GitHub URL is updated but Pages is stale, wait and poll again.

## Xiaoyuzhou Notes

Xiaoyuzhou imports one program from the submitted RSS feed URL.

- The `<channel>` metadata identifies the program.
- Each `<item>` identifies an episode.
- The `<guid>` is the episode identity.
- The `<enclosure>` URL is the audio file Xiaoyuzhou fetches.

After Xiaoyuzhou approves the RSS verification request, publishing a new episode means updating this RSS feed and pushing GitHub Pages. If Xiaoyuzhou does not show the episode immediately, look for a manual sync button in the creator center or wait for its polling interval.

Do not rely on Xiaoyuzhou private upload APIs unless the user explicitly asks to experiment with browser automation. RSS publishing is the safer default workflow.

## Git Workflow

Work from:

```bash
cd /Users/huajun/Documents/baihuajun24.github.io
```

Commit focused publishing changes:

```bash
git add podcast/feed.xml podcast/index.html podcast/audio/...mp3 podcast/audio/...md
git commit -m "Add 0606 MLSYS feed episode"
git push origin main
```

Do not revert unrelated user changes. If the worktree is dirty, inspect the changed files and only stage files that belong to the podcast publish operation.
