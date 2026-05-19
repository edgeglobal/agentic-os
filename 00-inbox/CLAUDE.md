---
type: folder-readme
scope: firma/00-inbox
---

## What's here

Transient capture. Brain-dumps, forwarded emails, voice-memo transcripts, raw inputs that need triage.

## How to use

- Filename: `{YYYY-MM-DD}-{HH-MM}-{slug}.md` or `{slug}.md`
- Frontmatter minimal: `type: inbox`, `source: voice | email | manual | agent`, `created:`
- Triage via `/playbooks/session-abschluss` at session-close: routed to right folder, original deleted.
- Files older than 7 days flagged for review.
