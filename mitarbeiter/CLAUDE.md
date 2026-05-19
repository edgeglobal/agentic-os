---
type: folder-readme
scope: firma/mitarbeiter
---

## What's here

People roster: human Mitarbeiter and AI Agents working in this company context.

## How to use

- Folder per person or agent: `mitarbeiter/{slug}/`
- Profile file: `mitarbeiter/{slug}/profil.md` with frontmatter `type: person | ai-agent`, `status: active | onboarding | offboarded`, `role:`, `owner:`, `created:`
- AI Agents: additional `AGENTS.md` in their folder with system-prompt, capabilities, and invocation patterns
- Wikilinks from Meetings, Tasks, and Projects to `[[../mitarbeiter/{slug}/profil]]`
- Offboarded Mitarbeiter: move to `firma/ablage/mitarbeiter/{slug}/`
