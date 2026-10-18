# appealmydenial.app — site repo and article rules

Static site for the Appeal My Denial iPhone app. Owner: Virtual Marketing Consultants, Inc.
(Joe Sanchez). Netlify project `appealit` publishes the committed `site/` folder.

## Layout
- `src/articles.py` — every guide (slug, tags, title, h1, desc, minutes, short, body, sources) and the `SRC` source list.
- `src/build.py` — generates guides, hubs, the deadline calculator, 51 state pages, sitemap, robots, home page into `site/`.
- `src/build_legal.py` — privacy and terms pages. Joe approved the text; do not change it without his OK.
- `content/` — source data: plan deadlines, 50-state external-review table, reason codes, letter templates; `topic-backlog.md`.
- `site/` — generated output, committed. Never hand-edit generated HTML; change the source and rebuild.

Build: `python3 src/build.py && python3 src/build_legal.py` from the repo root.
Footer must read "© 2026 Virtual Marketing Consultants, Inc."

## Weekly article run (scheduled task)
1. Pick 2–3 topics from `content/topic-backlog.md` (Priority 1 first), or a Search Console opportunity Joe forwarded.
2. Research from primary/official sources only: CMS, Medicare.gov, HealthCare.gov, eCFR/Cornell LII,
   state insurance departments, DOL/EBSA, KFF. No blogs or law-firm pages as sources.
3. Write each guide in the same structure as existing ones: 1,200–2,000 words, plain language,
   a "Short answer" box, steps people can act on, a "Your next question" link set, and Sources.
   Add every source to `SRC` and list its key on the article.
4. Link it: 2–4 links to related guides, the deadline calculator (/deadline/), and the state pages (/states/) where relevant.
   Update related existing guides to link back to it.
5. Independent fact-check: a separate agent that did not write the article checks every claim
   against its cited source. Fix or cut anything it cannot verify.
6. Rebuild, confirm 0 broken internal links and that sitemap.xml lists the new page.
7. Commit on a branch `articles/YYYY-MM-DD`, open a pull request titled "Articles for review: <topics>",
   and write Joe a short summary: topics, one-line takeaway each, any claims that were cut.
   Do NOT merge. Joe merges, which publishes the site.
8. Draft 2–3 Facebook-group posts from the new articles (educational, the useful content in the post,
   link at the end) in the PR description for Joe to post himself.

## Hard rules
- Educational, not disguised promotion. The app may be mentioned once near the end, plainly.
- Never invent statistics, deadlines, laws or quotes. Every number needs a cited source on the page.
- Not legal or medical advice; never promise outcomes. Keep the existing disclaimer pattern.
- No competitor bashing, no fear tactics, no fake reviews or testimonials.
- No link schemes: never buy links, swap links, or post links on other sites. Outreach is drafts only, for Joe.
- Quality over volume: never more than 3 new articles in a week; skip a week rather than publish thin pages.
- Don't touch privacy/terms, analytics token, or robots/sitemap rules beyond adding new pages.
