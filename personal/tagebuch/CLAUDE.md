---
type: folder-readme
scope: personal/tagebuch
---

## What's here

Two file types:

- **Daily AI Logs**: `{YYYY-MM-DD}.md` — Orchestrator writes at session-close
- **Reflective Journal**: `journal-{YYYY-MM-DD}.md` — only user writes

## How to use

- AI-Log Frontmatter: `type: daily-log`, `date:`, `sessions: [time-ranges]`, `created:`
- Journal Frontmatter: `type: journal`, `date:`, `mood:`, `created:`
- AI never writes to `journal-*.md`. User never writes to `{date}.md` (AI-only).
