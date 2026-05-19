---
type: folder-readme
scope: firma/meetings-intern
---

## What's here

Internal meetings: Standup, Quarterly, Team-Sync, Retrospectives. All meetings with internal Mitarbeiter only.

## How to use

- Filename: `{YYYY-MM-DD}-{slug}.md`
- Frontmatter: `type: meeting`, `meeting_type: standup | quarterly | team-sync | retro | 1on1 | other`, `participants: [...]`, `created:`
- Body: agenda, decisions, action-items with Wikilinks to `[[../mitarbeiter/{slug}]]`
- External meetings (with Kunden, Vendors, Partners): go to `firma/kunden/meetings/`, not here.
