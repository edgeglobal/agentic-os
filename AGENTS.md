# agentic-os — Agent Operating Manual

> Tool-agnostic intro. Read this first regardless of which AI tool you are (Claude, Cursor, Codex, Gemini, generic).

## What this workspace is

`~/ai-workspace/` is the operator's living folder structure. Two top-level layers:

- **`personal/`** — User-owned context (profile, notes, tasks, journal). NEVER synced to company drives.
- **`firma/`** — Company-owned context (brand, strategy, processes, customers). Cloud-synced, role-gated.

You operate as a colleague who knows the company context. Read the three manifests in order before doing anything:

1. **`KONTEXT.md`** — User-specific manifest with explicit scope (what you may read, what you must NOT read)
2. **`personal/profil.md`** — Operator profile (role, voice, working style, preferences)
3. **`firma/ueberblick.md`** — Company overview (mission, industry, operations)

Then load relevant `firma/` sections by topic. Read `_rules.md` for behavior rules.

## How to do work

- **Tasks**: folder-as-status pattern. `personal/aufgaben/offen/` → `in-arbeit/` → `erledigt/`. Move files; don't edit `status:` frontmatter.
- **Notes**: atomic, in `personal/notizen/`. Wikilinks for entities (`[[firma/kunden/unternehmen/acme]]`).
- **Decisions**: `personal/entscheidungen/` for personal, `firma/intelligence/decisions/` for company-level.
- **Meetings**: external in `firma/kunden/meetings/`, internal in `firma/meetings-intern/`.

Never write to `firma/` folders not in your scope (see `KONTEXT.md`). Never invent a "scratch" or "workspace" folder. Never write to workspace root.

## Skills + Playbooks

Two capability layers under `.claude/`:

- **`.claude/skills/`** — atomic capabilities (audit, check-sync-status, level-up)
- **`.claude/playbooks/`** — orchestrators (bootstrap, onboard-firma, weekly-review, etc.)

Invoke skills by name. Playbooks are multi-step processes with HUMAN-CHECKPOINTs at branch points.

## Setup Modes

This workspace was bootstrapped in one of three modes (check `.claude/settings.json` field `setupMode`):

- `solo` — local-only + GitHub backup
- `team-cloud` — cloud-drive primary + GitHub for template updates
- `team-enterprise` — cloud-drive + MDM + branch-strategy

Adapt behavior accordingly.

## Voice + Language

Default language: DE. Denglish OK. Never force translation. Never use em dashes (use periods, commas, colons). Specific names, specific consequences. No AI-mush.

## When in doubt

Ask the user. Don't synthesize across files into a new "wiki" structure — that breaks position-addressed memory.

For Claude-specific behavior + @-imports + Orchestrator-Pattern, see `CLAUDE.md`. For full behavior rules, see `_rules.md`.
