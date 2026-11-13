# Podcast Publishing Agent

This directory is the public RSS publishing surface for MLSYS Feed.

The agent working here owns RSS publishing, GitHub Pages deployment checks, and Xiaoyuzhou RSS-subscription hygiene. Other agents may deliver finished audio and show notes into this directory, but this agent is responsible for turning those artifacts into a valid public podcast feed.

## Program Identity

- Podcast title: `MLSYS Feed`
- Host/author: `小白超 AI算`
- Public feed URL: `https://baihuajun24.github.io/podcast/feed.xml`
- Public landing page: `https://baihuajun24.github.io/podcast/`
- Cover image: `https://baihuajun24.github.io/podcast/logo.jpg`
- Local repo: `/Users/baihuajun/Documents/baihuajun24.github.io`
- Local podcast directory: `/Users/baihuajun/Documents/baihuajun24.github.io/podcast`

## Role

Publishing is automated from the mini-genrec repo (since 2026-11-13):
`tools/publish_to_pages.py` there runs on every podcast kickoff firing (Tue–Sat
10:30/11:30/12:30 BJT). For every episode that is **public on Xiaoyuzhou** — daily
episodes, specials and weeklies alike — it adds one `<item>` to `podcast/feed.xml`
(newest first), bumps `lastBuildDate`, regenerates `podcast/episodes.js`, copies the
notes to `podcast/MMDD_show_notes_meta_YYYYMMDD.md`, commits only those files from a
dedicated clone and pushes. Run it by hand from mini-genrec with `--dry-run` to preview.

**No MP3 is published to the website any more** (PI 2026-11-13). New items carry a
`<link>` to the Xiaoyuzhou episode instead of an `<enclosure>`; the podcast page shows
a 「在小宇宙收听」 button for them. Xiaoyuzhou hosts the show itself (`SELF_HOSTING`) and
does not read this feed, so the feed cannot create duplicates there.

Existing audio stays where it is, because live URLs depend on it:
- episodes up to 0911: assets on the `audio-archive` GitHub Release
  (never rename or delete one);
- `podcast/special/*.mp3`: in git, because their URLs were shared directly.

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
      <guid isPermaLink="false">mlsys-feed-2026-06-05</guid>   <!-- specials: -special, weeklies: -weekly -->
      <link>https://www.xiaoyuzhoufm.com/episode/&lt;eid&gt;</link>
      <itunes:duration>09:48</itunes:duration>
      <itunes:explicit>false</itunes:explicit>
    </item>
```

`itunes:duration` is the floored Xiaoyuzhou duration; `pubDate` is the actual public time in GMT.

## Validation

The script checks well-formedness before committing. By hand:

```bash
xmllint --noout podcast/feed.xml
curl -fsSL https://baihuajun24.github.io/podcast/feed.xml | grep -n "mlsys-feed-2026-06-05"
```

GitHub Pages may serve the previous version for a minute or two.

## Xiaoyuzhou Notes

The program on Xiaoyuzhou is self-hosted (`syncMode: SELF_HOSTING`): episodes are uploaded
there directly from mini-genrec, and Xiaoyuzhou does not read this RSS feed. The feed
only drives the website's podcast page and any RSS readers.

## Manual edits

Hand edits to the feed are still fine (the script dedups by Xiaoyuzhou `eid` in `<link>`).
Work from `/Users/baihuajun/Documents/baihuajun24.github.io`, stage only the publishing
files (`podcast/feed.xml`, `podcast/episodes.js`, the notes file), and regenerate
`episodes.js` with:

```bash
node -e "const fs=require('fs');fs.writeFileSync('podcast/episodes.js','// Auto-generated snapshot of feed.xml so the page renders without fetch (e.g. file://).\n// Regenerate after each publish — see podcast/AGENTS.md.\nwindow.MLSYS_FEED_XML='+JSON.stringify(fs.readFileSync('podcast/feed.xml','utf8'))+';\n')"
```

Do not revert unrelated user changes; the worktree often holds unrelated WIP.
