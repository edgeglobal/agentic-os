# Business AOS — Agent Operating Manual

> Tool-agnostic intro. Read this first regardless of which AI tool you are (Claude, Cursor, Codex, Gemini, generic).

## What this workspace is

This is **Business AOS**, the operating system for ONE business. The folder you are reading right now represents the company: its brand, customers, processes, projects, and teams. Cloud-synced, role-gated.

You operate as a colleague who knows the company context. Read the three manifests in order before doing anything:

1. **`KONTEXT.md`** — User-specific manifest with explicit scope (what you may read, what you must NOT read)
2. **`ueberblick.md`** — Company overview (mission, industry, operations)
3. **`marke.md`** — Brand and voice

Then load relevant sections by topic. Read `_rules.md` for behavior rules.

## Optional sibling: Personal AI

If a folder `../Personal AI/` exists next to this one, that is the operator's private layer (profile, personal tasks, journal). Read `../Personal AI/profil.md` for operator identity. NEVER write to `../Personal AI/`. NEVER sync any of its contents into this workspace.

## How to do work

- **Projects**: each project gets a folder under `projekte/{name}/`. Use Wikilinks for entities (`[[kunden/unternehmen/acme]]`).
- **Decisions**: company-level decisions in `intelligence/decisions/` (create folder when first decision lands).
- **Meetings**: external in `kunden/meetings/`, internal in `meetings-intern/`.
- **Customers**: company entries in `kunden/unternehmen/{slug}/`, individuals in `kunden/personen/{slug}/`.

Never invent a "scratch" or "workspace" folder. Never write to workspace root.

## Skills + Playbooks

Two capability layers under `.claude/`:

- **`.claude/skills/`** — atomic capabilities (`audit`, `check-sync-status`, `level-up`)
- **`.claude/playbooks/`** — orchestrators (`bootstrap`)

Invoke skills by name. Playbooks are multi-step processes with HUMAN-CHECKPOINTs at branch points.

## Setup Modes

This workspace was bootstrapped in one of three modes (check `.claude/settings.json` field `setupMode`):

- **solo** — single operator, local-only, GitHub as backup
- **team-cloud** — 5-20 people, Cloud-Drive primary
- **team-enterprise** — 50+ people, Cloud-Drive plus MDM
