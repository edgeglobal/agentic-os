---
type: folder-readme
scope: personal/aufgaben
---

## What's here

Personal tasks. Folder-as-status pattern.

| Folder | Status |
|---|---|
| `offen/` | Not started |
| `in-arbeit/` | Actively working |
| `erledigt/` | Completed |
| `abgebrochen/` | Cancelled |

## How to use

- Filename: `{YYYY-MM-DD}-{slug}.md`
- Frontmatter mandatory: `type: task`, `owner: {user-slug}`, `priority: high | medium | low`, `created:`
- Move file to change status. Don't edit `status:` frontmatter.
- Wikilinks: link to people, companies, projects
