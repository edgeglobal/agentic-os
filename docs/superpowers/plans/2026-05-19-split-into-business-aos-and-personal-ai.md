# Split agentic-os into Business AOS + Personal AI — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Split the monolithic `gerald-eder/agentic-os` repo into two standalone template repos: `gerald-eder/business-aos` (primary, restructured from current repo) and `gerald-eder/personal-ai` (new). Each works alone; both compose as siblings under `~/ai-os/` when a solopreneur installs both.

**Architecture:** Phase 1 restructures the existing repo on branch `restructure/v2-split` (move `firma/*` to root, drop multi-biz, extract `personal/*` to a tmp seed, rewrite top-level docs as business-scoped, strip personal-refs from skills). Phase 2 creates the new `personal-ai` repo from the extracted seed with personal-scoped docs and a new `personal-audit` skill. Phase 3 verifies standalone and combined installs.

**Tech Stack:** Markdown content, Bash/Git/`gh` CLI, Python 3 (only for `check-sync-status` and new `personal-audit` skill), pytest for skill tests.

**Spec:** [docs/superpowers/specs/2026-05-19-split-into-business-aos-and-personal-ai-design.md](../specs/2026-05-19-split-into-business-aos-and-personal-ai-design.md)

**Repo working directory:** `~/developer/agentic-os/`

---

## Phase 1 — Restructure existing repo into Business AOS

### Task 1: Prepare branch and extract personal/ seed

**Files:**
- Branch: create `restructure/v2-split` from `v1.0-dev`
- Create: `/tmp/personal-ai-seed/` (outside repo, holds extracted personal content for Phase 2)
- Delete: `personal/` (after extraction)

- [ ] **Step 1: Create working branch**

```bash
cd ~/developer/agentic-os
git checkout v1.0-dev
git pull origin v1.0-dev
git checkout -b restructure/v2-split
```

Expected: `Switched to a new branch 'restructure/v2-split'`

- [ ] **Step 2: Extract `personal/` to tmp seed**

```bash
rm -rf /tmp/personal-ai-seed
mkdir -p /tmp/personal-ai-seed
cp -a personal/. /tmp/personal-ai-seed/
ls -la /tmp/personal-ai-seed/
```

Expected output includes: `profil.md`, `aufgaben/`, `entscheidungen/`, `notizen/`, `tagebuch/`.

- [ ] **Step 3: Delete `personal/` from repo**

```bash
git rm -r personal/
```

Expected: `rm 'personal/profil.md'`, `rm 'personal/aufgaben/...'`, etc.

- [ ] **Step 4: Commit**

```bash
git commit -m "refactor: extract personal/ layer for separate personal-ai repo"
```

---

### Task 2: Move firma/* to repo root, delete _weitere-unternehmen

**Files:**
- Move: `firma/*` → repo root
- Delete: `firma/` wrapper folder
- Delete: `firma/_weitere-unternehmen/` (no multi-biz)
- Conflict: `firma/CLAUDE.md` will collide with root `CLAUDE.md` — keep root, drop firma's (root gets rewritten in Task 3)

- [ ] **Step 1: Delete `firma/_weitere-unternehmen/` (no multi-biz)**

```bash
cd ~/developer/agentic-os
git rm -r firma/_weitere-unternehmen
```

Expected: 18+ deletions including `_template/` subfolders.

- [ ] **Step 2: Delete `firma/CLAUDE.md` (root CLAUDE.md will be rewritten to be business-scoped in Task 3)**

```bash
git rm firma/CLAUDE.md
```

- [ ] **Step 3: Move all remaining `firma/*` contents to repo root**

```bash
git mv firma/ueberblick.md ueberblick.md
git mv firma/marke.md marke.md
git mv firma/strategie.md strategie.md
git mv firma/tools.md tools.md
git mv firma/wunschkunde-icp.md wunschkunde-icp.md
git mv firma/00-inbox 00-inbox
git mv firma/ablage ablage
git mv firma/finance-hr-admin finance-hr-admin
git mv firma/fulfillment fulfillment
git mv firma/kunden kunden
git mv firma/marketing marketing
git mv firma/meetings-intern meetings-intern
git mv firma/mitarbeiter mitarbeiter
git mv firma/projekte projekte
git mv firma/prozesse prozesse
git mv firma/vertrieb vertrieb
```

- [ ] **Step 4: Verify `firma/` is empty and remove it**

```bash
ls firma/
rmdir firma/
```

Expected: `ls` returns nothing, `rmdir` succeeds.

- [ ] **Step 5: Verify resulting root structure**

```bash
ls -F | sort
```

Expected output (folders end with `/`):
```
00-inbox/
AGENTS.md
CHANGELOG.md
CLAUDE.md
INSTALL.md
KONTEXT.md
LICENSE
README.md
VERSION
_rules.md
ablage/
docs/
finance-hr-admin/
fulfillment/
kunden/
marke.md
marketing/
meetings-intern/
mitarbeiter/
projekte/
prozesse/
strategie.md
tools.md
ueberblick.md
vertrieb/
wunschkunde-icp.md
```

- [ ] **Step 6: Commit**

```bash
git commit -m "refactor: flatten firma/ to repo root, drop multi-biz folder"
```

---

### Task 3: Rewrite root CLAUDE.md (business-scoped, with sibling-detection)

**Files:**
- Modify: `CLAUDE.md` (full rewrite)

- [ ] **Step 1: Write new root CLAUDE.md**

Replace the entire content of `CLAUDE.md` with:

```markdown
@ueberblick.md
@marke.md
@_rules.md

# Orchestrator-Pattern

You are the Orchestrator for this Business AOS workspace. Every request lands here first. Clarify intent, pick the right Skill or Playbook, hand off a clean brief, synthesize the answer. You delegate specialist work to focused tools and sub-agents.

## Session Start

1. Check `00-inbox/` for unprocessed captures (only if today's haven't been triaged).
2. Walk `projekte/` for active projects.
3. Walk `kunden/meetings/` for upcoming or recent customer meetings.
4. Greet briefly with: "X inbox items, Y active projects. Wo legen wir los?"

## Optional: Personal AI Layer

If a sibling folder `../Personal AI/` exists, read its `profil.md` as authoritative operator context (identity, voice, working style, decision style). Wikilinks like `[[../Personal AI/profil]]` resolve naturally. If the sibling is absent, operate purely on business context.

## Knowledge Routing

| Type | Route to |
|------|----------|
| Company identity | `ueberblick.md` |
| Brand/Voice | `marke.md` |
| Ideal Customer | `wunschkunde-icp.md` |
| Strategy/OKRs | `strategie.md` |
| Tool stack | `tools.md` |
| SOPs/Processes | `prozesse/` |
| Company Decisions | `intelligence/decisions/` (if exists) |
| External Companies | `kunden/unternehmen/{slug}/` |
| External People | `kunden/personen/{slug}/` |
| External Meetings | `kunden/meetings/{date}-{slug}.md` |
| Internal Meetings | `meetings-intern/{date}-{slug}.md` |
| Inbox capture | `00-inbox/` |
| Projects | `projekte/{name}/` |
| Team — Marketing | `marketing/` |
| Team — Vertrieb | `vertrieb/` |
| Team — Fulfillment | `fulfillment/` |
| Team — Finance/HR/Admin | `finance-hr-admin/` |
| Mitarbeiter | `mitarbeiter/` |
| Ablage | `ablage/` |
| Skills | `.claude/skills/{name}/SKILL.md` |
| Playbooks | `.claude/playbooks/{name}/` |

## Session-Triggers

| Phrase | Action |
|---|---|
| "what's open?" | Walk `00-inbox/` + `projekte/` for active work |
| "what did I miss?" | Scan `00-inbox/` last 7d, recent `kunden/meetings/` |
| "let's realign" | Re-read `ueberblick.md` + `strategie.md` |
| "let's start fresh" | Discard current thread context |

## Available Skills + Playbooks

**Skills (atomic):**
- `audit` — 4-C-Score (Context, Connections, Capabilities, Cadence)
- `check-sync-status` — xattr-check for Cloud-Drive Mirror vs Stub
- `level-up` — weekly improvement ritual

**Playbooks (orchestrated):**
- `bootstrap` — initial setup wizard

## Rules Summary

Full rules in `_rules.md`. Highlights:

1. Folder-as-status for project work. Move files, don't edit status frontmatter.
2. Wikilinks for every entity (people, companies, meetings, projects).
3. NEVER use em dashes (use periods, commas, colons, restructure).
4. NEVER write to workspace root. Every file lives in a typed folder.
5. NEVER write to folders outside scope (see `KONTEXT.md`).
6. User corrections → save as permanent rule in `_rules.md`. Don't ask permission.
7. Sensitive content (credentials, PII): NEVER in workspace. Reference via env-var or external store.

## Anti-Patterns

Do NOT:
- Duplicate filename as `# Title` heading
- Create orphan notes (always link from existing note)
- Cram all info into root `README.md`
- Write project names, people, companies as plain text (always `[[wikilinks]]`)
- Use `[markdown](links)` for internal references (Wikilinks only)
- Synthesize across files into hidden "wiki" structure
```

- [ ] **Step 2: Verify no `personal/` refs remain in CLAUDE.md**

```bash
grep -n "personal" CLAUDE.md
```

Expected: only the "Optional: Personal AI Layer" section. No `personal/` paths.

- [ ] **Step 3: Commit**

```bash
git add CLAUDE.md
git commit -m "feat: rewrite CLAUDE.md as business-scoped orchestrator with sibling detection"
```

---

### Task 4: Rewrite root AGENTS.md

**Files:**
- Modify: `AGENTS.md` (full rewrite)

- [ ] **Step 1: Write new AGENTS.md**

Replace the entire content of `AGENTS.md` with:

```markdown
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
```

- [ ] **Step 2: Commit**

```bash
git add AGENTS.md
git commit -m "feat: rewrite AGENTS.md as business-scoped manual with sibling note"
```

---

### Task 5: Rewrite root _rules.md (business-scoped)

**Files:**
- Modify: `_rules.md` (full rewrite, drop personal-layer rules)

- [ ] **Step 1: Write new _rules.md**

Replace the entire content of `_rules.md` with:

```markdown
# Business AOS Rules

Behavioral rules for any AI agent working in this Business AOS workspace.

## 1. Obsidian Syntax

- **Wikilinks** for every entity: `[[kunden/unternehmen/acme]]`, `[[mitarbeiter/anna]]`. Weave into sentences. Never as bullet lists or footnotes.
- **Embeds** for context: `![[ueberblick]]`.
- **Callouts** sparse (1-3 per doc): `> [!type] Title` (note, tip, warning, important, question, todo, success, failure, info).
- **Highlights** rare: `==text==`.
- **Comments** AI-only: `%%internal note%%`.
- **Tags** inline `#tag` or frontmatter `tags: [...]`.

**Frontmatter** mandatory on all notes:

```yaml
type: meeting | decision | project | note | sop | ...
status: ...
tags: [tag1, tag2]
created: YYYY-MM-DD
```

Common additional: `project:`, `team:`, `priority:`, `owner:`.

## 2. Voice

Documents sound like a teammate, never AI. Specific names, specific consequences. Never generic.

- BAD: "The project is progressing well."
- GOOD: "Onboarding 70% done. Next checkpoint: contract signature. Blocked on Acme legal team."

**NEVER use em dashes.** Use periods, commas, colons, or restructure.

## 3. Language

Default DE. Denglish OK. Never force translation. Match the user's language.

## 4. Project Status

Folder-as-status pattern. For projects with status tracking, status equals folder location (e.g. `projekte/aktiv/{name}/` vs `projekte/done/{name}/`). Move files; don't edit `status:` frontmatter.

`owner:` frontmatter mandatory. Allowed values:
- `gerald` (or other Mitarbeiter name)
- `agent:openclaw | agent:hermes | agent:claude | agent:{name}`

## 5. Session-Triggers

| Phrase | Action |
|---|---|
| "what's open?" | Walk `00-inbox/` + `projekte/` for active work |
| "what did I miss?" | Scan `00-inbox/` last 7d, recent `kunden/meetings/` |
| "let's realign" | Re-read `ueberblick.md` + `strategie.md` |
| "let's start fresh" | Discard current thread context |

## 6. Wiki Operations

Three-ops model:

- **Ingest**: capture new info into right folder (inbox, projects, meetings) with frontmatter and Wikilinks.
- **Query**: read existing notes. Use `grep` for keyword scan. Read full file only when scan identifies relevance.
- **Lint**: maintenance. Find orphan notes, broken Wikilinks, stale entries, missing frontmatter.

## 7. Folder Indexes

Each major folder has a `CLAUDE.md`:
- Top: "What's here" overview
- Bottom: "How to use this folder" routing, frontmatter standards, naming conventions

## 8. AI Output Routing

Route AI-generated content by semantic intent:

- Customer-related output: `kunden/`
- Decision record: `intelligence/decisions/{date}-{slug}.md`
- Meeting summary: `kunden/meetings/` or `meetings-intern/`
- Project work: `projekte/{name}/`
- Reference material: appropriate team folder

NEVER save to workspace root.

## 9. Sensitive Content

Credentials, PII, contracts: NEVER in workspace. Reference via env-var or external store (e.g. `secret_ref: ENV_VAR_NAME`).

## 10. Em Dashes

Forbidden. Use periods, commas, colons, or restructure. Non-negotiable.

## 11. Optional Personal AI Sibling

If `../Personal AI/` exists:
- READ access OK for operator context.
- WRITE access FORBIDDEN — never modify, never sync content from there into here.
- If user asks for cross-cutting analysis spanning both, do it read-only.

## 12. Context First

Before any work that touches business context (brand, ICP, offer, pricing, decisions, positioning, strategy), load relevant context files FIRST. Don't ask the user to explain what's already documented.
```

- [ ] **Step 2: Verify no `personal/` (as path) references remain**

```bash
grep -nE "personal/[a-z]" _rules.md
```

Expected: zero matches.

- [ ] **Step 3: Commit**

```bash
git add _rules.md
git commit -m "feat: rewrite _rules.md as business-scoped behavioral rules"
```

---

### Task 6: Update KONTEXT.md (business-scoped scope-gating)

**Files:**
- Modify: `KONTEXT.md` (rewrite, remove personal-layer references)

- [ ] **Step 1: Read current KONTEXT.md to preserve any business-specific scope rules**

```bash
cat KONTEXT.md
```

- [ ] **Step 2: Write new KONTEXT.md**

Replace content with:

```markdown
# KONTEXT — Workspace Scope and Permissions

Scope-gating manifest for this Business AOS workspace. Edit per operator / per team to control what AI agents may read or write.

## Identity

- **Workspace owner:** {fill during bootstrap}
- **Primary user role:** {ceo | vertrieb | marketing | fulfillment | finance-hr}
- **Setup mode:** {solo | team-cloud | team-enterprise}

## Scope — What AI may READ

By default: all folders in this workspace EXCEPT folders listed in "Restricted" below.

## Scope — What AI may WRITE

By default: all folders in this workspace EXCEPT:
- `LICENSE`, `VERSION`, `CHANGELOG.md`, `README.md`, `INSTALL.md` (template files)
- Any folder in "Restricted" below

## Restricted (per operator decision)

Add folder paths here that the current AI role should NOT touch. Examples:
- `finance-hr-admin/` (only finance-hr role agent)
- `intelligence/decisions/` (read-only for non-CEO roles)

```text
# Add restricted paths, one per line, relative to workspace root
```

## Sibling Workspace Awareness

If a sibling folder `../Personal AI/` exists:
- READ access OK for operator identity context.
- WRITE access FORBIDDEN.

## Sync Layer

- **Provider:** {google-drive | onedrive | dropbox | none}
- **Local mount:** {auto-detected during bootstrap}
- **Cloud-Drive stub-detection:** run `.claude/skills/check-sync-status` periodically.
```

- [ ] **Step 3: Commit**

```bash
git add KONTEXT.md
git commit -m "feat: rewrite KONTEXT.md as business-scoped scope-gating"
```

---

### Task 7: Rewrite README.md (Business AOS customer-facing)

**Files:**
- Modify: `README.md` (full rewrite)

- [ ] **Step 1: Write new README.md**

Replace entire content of `README.md` with:

```markdown
<!--
Business AOS v2.0.0 — © 2026 Gerald Eder
Licensed under MIT License — see LICENSE
-->

# Business AOS

**Agent Operating System für ein Business.** Eine Ordner-Struktur in Markdown, die deiner KI sofort den vollen Firmen-Kontext gibt.

Klone das Repo, öffne es in deinem AI-Tool, starte das `bootstrap` Playbook — und deine KI kennt deine Firma, deine Kunden, deine Strategie, deine Prozesse.

---

## Was Business AOS ist

Ein Folder pro Business. Drinnen liegen Markdown-Files, die die KI bei jeder Session liest:

- **Wer ihr seid** als Firma (`ueberblick.md`, `marke.md`)
- **Wer eure Wunschkunden sind** (`wunschkunde-icp.md`)
- **Was eure Strategie ist** (`strategie.md`)
- **Welche Tools ihr nutzt** (`tools.md`)
- **Wen ihr kennt** (`kunden/unternehmen/`, `kunden/personen/`)
- **Was ihr besprochen habt** (`kunden/meetings/`, `meetings-intern/`)
- **Wie ihr arbeitet** (`prozesse/sops/`, `prozesse/richtlinien/`, `prozesse/workflows/`)

Die KI nutzt diesen Kontext, um in eurer Sprache zu schreiben, eure Kunden zu kennen, und Vorgänge sauber zu pflegen.

---

## Was du bekommst

| Element | Beschreibung |
|---|---|
| **Universelle Ordner-Struktur** | Ein Folder = ein Business. Keine Multi-Biz, keine Holding. Wer mehrere Businesses hat, klont mehrmals. |
| **CRM-Light in Markdown** | Unternehmen + Personen + Meetings via Wikilinks vernetzt. Kein externes CRM nötig. |
| **Default-Teams** | Marketing, Vertrieb, Fulfillment, Finance/HR/Admin. Anpassbar oder löschbar. |
| **Universelle Context-Files** | ueberblick, marke, wunschkunde-icp, strategie, tools |
| **3 Skills** | audit, check-sync-status, level-up |
| **5 Role-Templates** | ceo, vertrieb, marketing, fulfillment, finance-hr — als Mitarbeiter-Profile |
| **Tool-agnostisch** | `AGENTS.md` lesen Claude, Codex, Cursor, Gemini nativ |

---

## Quick Start

```bash
git clone https://github.com/gerald-eder/business-aos.git "Business AOS"
cd "Business AOS"
# Open in your AI tool (Claude Code, Cursor, etc.)
# Run the bootstrap playbook
```

Details in [`INSTALL.md`](INSTALL.md).

---

## Optional: Personal AI Companion

Wer als Solopreneur einen privaten Layer für sich selbst will (Profil, Aufgaben, Tagebuch, Notizen), kann zusätzlich [Personal AI](https://github.com/gerald-eder/personal-ai) als Sibling klonen:

```
~/ai-os/
  Business AOS/      # this repo
  Personal AI/       # github.com/gerald-eder/personal-ai
```

Beide Repos erkennen den jeweiligen Sibling automatisch. Beide funktionieren auch alleine.

---

## License

MIT. See [`LICENSE`](LICENSE).
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "feat: rewrite README.md as Business AOS customer-facing intro"
```

---

### Task 8: Update INSTALL.md

**Files:**
- Modify: `INSTALL.md` (rewrite)

- [ ] **Step 1: Write new INSTALL.md**

Replace content with:

```markdown
# Business AOS Install Guide

## Prerequisites

- Git
- An AI coding tool (Claude Code, Cursor, Codex, Gemini CLI)
- `gh` CLI (optional, for repo creation)
- macOS or Linux (Windows via WSL)

## Install

```bash
cd ~
mkdir -p ai-os
cd ai-os
git clone https://github.com/gerald-eder/business-aos.git "Business AOS"
cd "Business AOS"
```

## Bootstrap

Open the workspace in your AI tool, then invoke the `bootstrap` playbook. It will:

1. Verify the folder name is `Business AOS` (auto-rename if needed).
2. Ask for setup mode: `solo`, `team-cloud`, or `team-enterprise`.
3. Configure workspace location (move to Cloud-Drive mount if team mode).
4. Configure git remotes (`origin` = your repo, `upstream` = `gerald-eder/business-aos`).
5. Run a sync-status check.
6. Pick a first role-template.
7. Detect optional `../Personal AI/` sibling.

## Combined Install (with Personal AI)

If you also want the Personal AI companion:

```bash
cd ~/ai-os
git clone https://github.com/gerald-eder/personal-ai.git "Personal AI"
cd "Personal AI"
# Run Personal AI's bootstrap playbook
```

Both repos will auto-detect each other.

## Setup Modes

- **solo** — single operator, local-only, GitHub as backup.
- **team-cloud** — 5-20 people, Cloud-Drive primary (Google Drive, OneDrive, Dropbox).
- **team-enterprise** — 50+ people, Cloud-Drive plus MDM.

Cloud-Drive provider docs live in [`docs/INSTALL-google.md`](docs/INSTALL-google.md), [`docs/INSTALL-onedrive.md`](docs/INSTALL-onedrive.md), etc. (create per provider during onboarding).
```

- [ ] **Step 2: Commit**

```bash
git add INSTALL.md
git commit -m "docs: rewrite INSTALL.md for Business AOS with combined-install section"
```

---

### Task 9: Strip personal-refs from audit skill

**Files:**
- Modify: `.claude/skills/audit/SKILL.md`

- [ ] **Step 1: Identify personal references**

```bash
grep -n "personal" .claude/skills/audit/SKILL.md
```

Note every line number for context.

- [ ] **Step 2: Read full file to understand scoring structure**

```bash
cat .claude/skills/audit/SKILL.md
```

- [ ] **Step 3: Rewrite skill to score only business layer**

Edit `.claude/skills/audit/SKILL.md`. For every section that scores both layers:

- Remove personal-layer checks (profil.md, tagebuch/, aufgaben/, entscheidungen/, notizen/).
- Keep business-layer checks (ueberblick.md, marke.md, strategie.md, kunden/, projekte/, prozesse/, etc.).
- Adjust scoring rubric so total score reflects business-only (e.g. if old scoring was 50% personal + 50% business, new is 100% business with adjusted weights).
- Replace any "scope: workspace" framing with "scope: business workspace".

If the audit skill currently has a frontmatter `description:` mentioning personal layer, edit that too.

- [ ] **Step 4: Verify no personal-layer references remain**

```bash
grep -nE "personal/|profil\.md|tagebuch/|aufgaben/|entscheidungen/|notizen/" .claude/skills/audit/SKILL.md
```

Expected: zero matches.

- [ ] **Step 5: Commit**

```bash
git add .claude/skills/audit/SKILL.md
git commit -m "refactor(audit): scope to business layer only, drop personal-layer checks"
```

---

### Task 10: Strip personal-refs from level-up skill

**Files:**
- Modify: `.claude/skills/level-up/SKILL.md`

- [ ] **Step 1: Identify personal references**

```bash
grep -n "personal" .claude/skills/level-up/SKILL.md
```

- [ ] **Step 2: Edit skill — remove personal-layer improvement steps**

Open `.claude/skills/level-up/SKILL.md`. Remove every step or checkpoint that improves the personal layer (review tagebuch, audit aufgaben backlog, refresh profil, etc.). Keep only business-layer improvements (refresh ueberblick, audit kunden coverage, review prozesse, check team-folder hygiene, etc.).

Adjust the skill's frontmatter `description:` to reflect business-only scope.

- [ ] **Step 3: Verify**

```bash
grep -nE "personal/|profil\.md|tagebuch/|aufgaben/|entscheidungen/|notizen/" .claude/skills/level-up/SKILL.md
```

Expected: zero matches.

- [ ] **Step 4: Commit**

```bash
git add .claude/skills/level-up/SKILL.md
git commit -m "refactor(level-up): scope to business layer only"
```

---

### Task 11: Strip personal-refs from check-sync-status skill

**Files:**
- Modify: `.claude/skills/check-sync-status/SKILL.md`
- Modify: `.claude/skills/check-sync-status/check_sync.py` (if it hardcodes personal/firma paths)
- Modify: `.claude/skills/check-sync-status/test_check_sync.py` (if tests reference personal/firma paths)

- [ ] **Step 1: Identify personal references**

```bash
grep -n "personal" .claude/skills/check-sync-status/SKILL.md .claude/skills/check-sync-status/check_sync.py .claude/skills/check-sync-status/test_check_sync.py
```

- [ ] **Step 2: Edit SKILL.md to describe single-layer scope**

Open `.claude/skills/check-sync-status/SKILL.md`. Remove any references to scanning both layers. The skill scans whatever folder it runs in. Update description and examples to reflect "this Business AOS workspace" scope.

- [ ] **Step 3: Check if check_sync.py hardcodes any layer paths**

```bash
grep -nE "personal|firma" .claude/skills/check-sync-status/check_sync.py
```

If matches found: edit to remove hardcoded layer references. The script should accept a target path as argument (it likely already does; verify).

- [ ] **Step 4: Update test_check_sync.py if it hardcodes layer paths**

```bash
grep -nE "personal|firma" .claude/skills/check-sync-status/test_check_sync.py
```

If matches found: replace with generic test paths (e.g. `tmp_path / "ueberblick.md"` fixtures).

- [ ] **Step 5: Run the existing test to confirm nothing broke**

```bash
cd ~/developer/agentic-os/.claude/skills/check-sync-status
python -m pytest test_check_sync.py -v
cd ~/developer/agentic-os
```

Expected: all existing tests PASS.

- [ ] **Step 6: Commit**

```bash
git add .claude/skills/check-sync-status/
git commit -m "refactor(check-sync-status): scope to single workspace layer"
```

---

### Task 12: Update bootstrap playbook (drop personal steps, add folder-auto-rename)

**Files:**
- Modify: `.claude/playbooks/bootstrap/PLAYBOOK.md`

- [ ] **Step 1: Read current playbook to preserve all business-relevant phases**

```bash
cat .claude/playbooks/bootstrap/PLAYBOOK.md
```

- [ ] **Step 2: Rewrite playbook**

Replace entire content with:

```markdown
---
name: bootstrap
description: First playbook to run after cloning business-aos repo. Sets up workspace name, location, sync layer, git remotes, first role. Idempotent — re-run safe.
type: playbook
---

# Bootstrap

Initial setup of a Business AOS workspace. Run once after `git clone`.

## Phase 0: Folder-Name Auto-Rename

> [!question] HUMAN-CHECKPOINT
> Detect CWD folder name. Expected: `Business AOS`.

```bash
CURRENT_NAME=$(basename "$PWD")
echo "Current folder: $CURRENT_NAME"
```

If `$CURRENT_NAME` is not exactly `Business AOS`:

> [!question] HUMAN-CHECKPOINT
> "Folder heißt '$CURRENT_NAME'. Auf 'Business AOS' umbenennen?
> 1. Ja — Bootstrap renamt und passt Pfade an
> 2. Nein — Bootstrap fährt fort, warnt aber"

If yes:
```bash
cd ..
mv "$CURRENT_NAME" "Business AOS"
cd "Business AOS"
```

## Phase 1: Setup-Mode

> [!question] HUMAN-CHECKPOINT
> "Welcher Setup-Modus?
> 1. **solo** — Solo-Operator. Lokal, kein Cloud-Drive, GitHub als Backup
> 2. **team-cloud** — 5-20 Mitarbeiter. Cloud-Drive primär, GitHub für Template-Updates
> 3. **team-enterprise** — 50+ Mitarbeiter. Cloud-Drive plus MDM, Branch-Strategy"

Save choice to `.claude/settings.json` field `setupMode`.

## Phase 2: Workspace Location

Based on mode:

- **solo**: workspace stays at `~/ai-os/Business AOS/`. Done.
- **team-cloud**: ask which Cloud-Drive provider (Google Workspace, Microsoft 365, Dropbox). Move workspace to provider's local mount-path. Update `~/.zshrc` or `~/.bashrc` with symlink: `ln -s "/Users/{user}/Library/CloudStorage/.../Business AOS" ~/ai-os/"Business AOS"`.
- **team-enterprise**: same as team-cloud, plus MDM-deployment instructions per provider doc.

## Phase 3: Git Remotes

> [!question] HUMAN-CHECKPOINT
> "Eigenes GitHub-Repo für Versionierung und Backup?
> 1. Ja, ich habe ein Repo → URL eingeben → setze `origin = USER_REPO`, `upstream = gerald-eder/business-aos`
> 2. Ja, erstellen → Anweisung github.com zu öffnen, return mit URL
> 3. Nein, nur Template-Updates → `upstream = gerald-eder/business-aos` only, kein push"

```bash
# Option 1 or 2:
git remote remove origin
git remote add origin {USER_REPO}
git remote add upstream https://github.com/gerald-eder/business-aos.git

# Option 3:
git remote rename origin upstream
```

## Phase 4: Sync-Check

Run `check-sync-status` skill. If stubs detected, walk user through "Make Available Offline" in their Cloud-Drive client.

## Phase 5: First Role

> [!question] HUMAN-CHECKPOINT
> "Welche Rolle willst du als erstes setzen? Wähle ein Role-Template:
> 1. ceo
> 2. vertrieb
> 3. marketing
> 4. fulfillment
> 5. finance-hr"

Copy `.claude/role-templates/{choice}.json` to `mitarbeiter/{user-name}/role.json`.

## Phase 6: Sibling Detection

```bash
if [ -d "../Personal AI" ]; then
  echo "Personal AI sibling detected at ../Personal AI/. Cross-context active."
else
  echo "No Personal AI sibling. Business AOS standalone mode."
fi
```

## Done

```bash
echo "Business AOS bootstrap complete. Workspace ready."
```
```

- [ ] **Step 3: Commit**

```bash
git add .claude/playbooks/bootstrap/PLAYBOOK.md
git commit -m "feat(bootstrap): add folder-auto-rename phase, drop personal-layer steps, add sibling detection"
```

---

### Task 13: Remove any remaining personal-layer references in moved subfolder CLAUDE.md files

**Files:**
- Audit: all `*/CLAUDE.md` files under repo root

- [ ] **Step 1: List all CLAUDE.md files**

```bash
find . -name "CLAUDE.md" -not -path "./.git/*"
```

Expected: root `CLAUDE.md` plus per-folder ones from former `firma/*` (e.g. `00-inbox/CLAUDE.md`, `prozesse/CLAUDE.md`, `kunden/CLAUDE.md`).

- [ ] **Step 2: Grep all for personal-layer references**

```bash
grep -rn "personal/" --include="CLAUDE.md" .
grep -rn "tagebuch\|profil.md\|entscheidungen/" --include="CLAUDE.md" .
```

- [ ] **Step 3: For each match, edit to remove the reference**

For each file with matches: open and remove the personal-layer mention. Typical patterns:
- "See also `personal/profil.md` for operator context" → remove or replace with "See `../Personal AI/profil.md` if sibling exists"
- Routing tables that list both layers → drop personal rows
- Wikilinks like `[[personal/...]]` → drop or rewrite as `[[../Personal AI/...]]`

- [ ] **Step 4: Re-verify**

```bash
grep -rn "personal/" --include="CLAUDE.md" .
```

Expected: zero matches (or only the explicit `../Personal AI/` sibling references).

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "refactor: remove personal-layer refs from subfolder CLAUDE.md files"
```

---

### Task 14: Bump VERSION to 2.0.0 and update CHANGELOG.md

**Files:**
- Modify: `VERSION`
- Modify: `CHANGELOG.md`

- [ ] **Step 1: Bump VERSION**

```bash
echo "2.0.0" > VERSION
cat VERSION
```

Expected output: `2.0.0`.

- [ ] **Step 2: Read existing CHANGELOG.md head to match format**

```bash
head -20 CHANGELOG.md
```

- [ ] **Step 3: Prepend v2.0.0 entry**

Edit `CHANGELOG.md`. Insert at the top (after any existing header banner, before the previous version entry):

```markdown
## [2.0.0] — 2026-05-19

### BREAKING

- **Repo split.** `gerald-eder/agentic-os` renamed to `gerald-eder/business-aos`. The personal layer has moved to the new repo `gerald-eder/personal-ai`. Old clones with the personal layer still work, but updates will only land in the business layer.
- **Single-business scope.** Multi-biz folder `_weitere-unternehmen/` removed. One repo clone = one business. For multiple businesses, clone the repo multiple times.
- **Flattened structure.** All content from former `firma/*` is now at repo root.

### Added

- Optional sibling-detection: if `../Personal AI/` exists, business CLAUDE.md loads it as operator context.
- `bootstrap` playbook now includes folder-auto-rename to standardize the workspace folder name to `Business AOS`.

### Changed

- `CLAUDE.md`, `AGENTS.md`, `_rules.md`, `KONTEXT.md`, `README.md`, `INSTALL.md` all rewritten as business-scoped.
- Skills `audit`, `level-up`, `check-sync-status` rescoped to business layer only.

### Removed

- `personal/` folder (extracted to `gerald-eder/personal-ai`).
- `firma/_weitere-unternehmen/` (multi-biz concept dropped).
- `promote-multi-biz` playbook (if it existed).

### Migration

For users on v0.5.x or v1.0-dev:

1. Pull the v2.0.0 main branch.
2. If you had content in `firma/`, it now lives at repo root.
3. If you had content in `personal/`, clone `gerald-eder/personal-ai` as a sibling.
4. If you used `_weitere-unternehmen/`, that data is preserved in your local v1.0-dev branch; create separate Business AOS clones per business and move content manually.
```

- [ ] **Step 4: Commit**

```bash
git add VERSION CHANGELOG.md
git commit -m "chore: bump VERSION to 2.0.0 and document breaking changes in CHANGELOG"
```

---

### Task 15: Drop promote-multi-biz playbook if it exists

**Files:**
- Possibly delete: `.claude/playbooks/promote-multi-biz/`

- [ ] **Step 1: Check if playbook exists**

```bash
ls .claude/playbooks/
```

- [ ] **Step 2: If `promote-multi-biz/` exists, delete it**

```bash
if [ -d .claude/playbooks/promote-multi-biz ]; then
  git rm -r .claude/playbooks/promote-multi-biz
  git commit -m "refactor: drop promote-multi-biz playbook (multi-biz concept removed)"
else
  echo "promote-multi-biz playbook absent — nothing to drop"
fi
```

---

### Task 16: Final verification, push, rename GitHub repo

**Files:**
- Branch: `restructure/v2-split` on `~/developer/agentic-os`
- GitHub repo: `gerald-eder/agentic-os` → `gerald-eder/business-aos`

- [ ] **Step 1: Confirm no leftover personal-layer references repo-wide**

```bash
grep -rln "personal/" --exclude-dir=.git --exclude-dir=docs --exclude="CHANGELOG.md" .
```

Expected: zero matches except `CHANGELOG.md` (which documents the removal) and `docs/` (spec mentions it).

- [ ] **Step 2: Confirm structure**

```bash
ls -F | sort
test -f ueberblick.md && echo "ueberblick.md at root: OK"
test ! -d firma && echo "firma/ removed: OK"
test ! -d personal && echo "personal/ removed: OK"
test ! -d _weitere-unternehmen && echo "_weitere-unternehmen/ removed: OK"
```

Expected: all four "OK" lines.

- [ ] **Step 3: Run check-sync-status tests if applicable**

```bash
cd ~/developer/agentic-os/.claude/skills/check-sync-status
python -m pytest -v
cd ~/developer/agentic-os
```

Expected: all PASS.

- [ ] **Step 4: Push branch**

```bash
git push -u origin restructure/v2-split
```

- [ ] **Step 5: Fast-forward main to restructure/v2-split**

```bash
git checkout main
git pull origin main
git merge --ff-only restructure/v2-split
git push origin main
```

- [ ] **Step 6: Also update v1.0-dev to track main (clean up)**

```bash
git checkout v1.0-dev
git merge --ff-only main
git push origin v1.0-dev
```

- [ ] **Step 7: Rename GitHub repo via `gh`**

```bash
gh repo rename business-aos --repo gerald-eder/agentic-os
```

Expected: confirmation message that repo is renamed. GitHub auto-redirects old URLs.

- [ ] **Step 8: Update local remote URL**

```bash
git remote set-url origin https://github.com/gerald-eder/business-aos.git
git remote -v
```

Expected: remote URL shows `business-aos.git`.

- [ ] **Step 9: Verify template flag**

```bash
gh repo view gerald-eder/business-aos --json isTemplate,visibility,defaultBranchRef
```

Expected: `"isTemplate":true, "visibility":"PUBLIC", "defaultBranchRef":{"name":"main"}`.

If `isTemplate` is `false`, re-set:

```bash
gh repo edit gerald-eder/business-aos --template
```

- [ ] **Step 10: Tag v2.0.0**

```bash
git tag -a v2.0.0 -m "Business AOS v2.0.0 — split from agentic-os, single-business scope"
git push origin v2.0.0
```

---

## Phase 2 — Create new personal-ai repo

### Task 17: Initialize personal-ai repo locally

**Files:**
- Create: `~/developer/personal-ai/` (new repo)

- [ ] **Step 1: Create local repo folder**

```bash
mkdir -p ~/developer/personal-ai
cd ~/developer/personal-ai
git init
git branch -m main
```

- [ ] **Step 2: Copy extracted personal content from tmp seed**

```bash
cp -a /tmp/personal-ai-seed/. .
ls -la
```

Expected: `profil.md`, `aufgaben/`, `entscheidungen/`, `notizen/`, `tagebuch/` plus subfolder `CLAUDE.md` files and `.gitkeep` files.

- [ ] **Step 3: Verify subfolder CLAUDE.md files have no business-layer references**

```bash
grep -rn "firma/" --include="CLAUDE.md" .
grep -rn "ueberblick\|marke\.md\|wunschkunde-icp\|strategie\.md" --include="CLAUDE.md" .
```

If matches: edit each to remove. The Personal AI repo must not reference business-layer paths (except optional sibling block).

- [ ] **Step 4: Initial commit of raw content**

```bash
git add -A
git commit -m "chore: initial import of personal content from agentic-os split"
```

---

### Task 18: Write Personal AI CLAUDE.md

**Files:**
- Create: `~/developer/personal-ai/CLAUDE.md`

- [ ] **Step 1: Create CLAUDE.md**

Write file at `~/developer/personal-ai/CLAUDE.md`:

```markdown
@profil.md
@_rules.md

# Personal AI Orchestrator

You are the Orchestrator for this Personal AI workspace. Every request lands here first. Clarify intent, pick the right Skill or Playbook, hand off a clean brief.

## Session Start

1. Silently read latest `tagebuch/{date}.md` if it exists for recent context.
2. Walk `aufgaben/offen/` and `aufgaben/in-arbeit/` for open work.
3. Greet briefly: "X open tasks. Wo legen wir los?"

## Optional: Business AOS Layer

If a sibling folder `../Business AOS/` exists, that is the operator's business workspace. Read `../Business AOS/ueberblick.md` for company context. When the user references "die Firma", "der Kunde XY", or any business-scoped concept, that sibling is the source of truth. NEVER write to `../Business AOS/`.

If absent, operate purely on personal context.

## Knowledge Routing

| Type | Route to |
|------|----------|
| Operator profile | `profil.md` |
| Personal Tasks | `aufgaben/{offen,in-arbeit,erledigt,abgebrochen}/` |
| Personal Notes | `notizen/` (flat, `note_type:` frontmatter) |
| Daily AI log | `tagebuch/{date}.md` (you write) |
| Personal Journal | `tagebuch/journal-{date}.md` (only user writes) |
| Personal Decisions | `entscheidungen/` |
| Skills | `.claude/skills/{name}/SKILL.md` |
| Playbooks | `.claude/playbooks/{name}/` |

## Session-Triggers

| Phrase | Action |
|---|---|
| "close session" | Write `tagebuch/{date}.md`, move open tasks forward |
| "what's open?" | Walk `aufgaben/{offen,in-arbeit}/` |
| "let's realign" | Re-read `profil.md` |
| "let's start fresh" | Discard current thread context |

## Available Skills + Playbooks

**Skills:**
- `personal-audit` — quick health check of personal layer (profil filled, tasks tracked, journal cadence)

**Playbooks:**
- `bootstrap` — initial setup wizard

## Rules

See `_rules.md`.

Highlights:
- Folder-as-status for tasks. Move files, don't edit status frontmatter.
- Wikilinks for entities.
- NEVER use em dashes.
- NEVER write to workspace root (except this orchestrator file and the manifests).
```

- [ ] **Step 2: Commit**

```bash
git add CLAUDE.md
git commit -m "feat: add Personal AI orchestrator CLAUDE.md with sibling detection"
```

---

### Task 19: Write Personal AI AGENTS.md

**Files:**
- Create: `~/developer/personal-ai/AGENTS.md`

- [ ] **Step 1: Create AGENTS.md**

Write file:

```markdown
# Personal AI — Agent Operating Manual

> Tool-agnostic intro. Read this first regardless of which AI tool you are.

## What this workspace is

This is **Personal AI**, the operator's private layer. Tasks, journal, notes, decisions. ONE person owns this. Not shared with a team.

You operate as a personal assistant. Read in order:

1. **`profil.md`** — Operator identity (role, voice, values, working style)
2. **`_rules.md`** — Behavior rules

Then load relevant sections by topic.

## Optional sibling: Business AOS

If `../Business AOS/` exists, that is the operator's business workspace. Read `../Business AOS/ueberblick.md` for company context. NEVER write into `../Business AOS/`. NEVER copy business content into this personal layer.

## How to do work

- **Tasks**: folder-as-status. `aufgaben/offen/` → `in-arbeit/` → `erledigt/`. Move files.
- **Notes**: atomic, in `notizen/`. Wikilinks for entities.
- **Decisions**: `entscheidungen/{date}-{slug}.md`.
- **Journal**: user writes `tagebuch/journal-{date}.md`. AI writes `tagebuch/{date}.md` for daily AI-side log.

Never invent scratch folders. Never write to workspace root.

## Skills + Playbooks

- **`.claude/skills/`** — atomic (`personal-audit`)
- **`.claude/playbooks/`** — orchestrators (`bootstrap`)
```

- [ ] **Step 2: Commit**

```bash
git add AGENTS.md
git commit -m "feat: add Personal AI AGENTS.md"
```

---

### Task 20: Write Personal AI _rules.md

**Files:**
- Create: `~/developer/personal-ai/_rules.md`

- [ ] **Step 1: Create _rules.md**

Write file:

```markdown
# Personal AI Rules

Behavioral rules for any AI agent working in this Personal AI workspace.

## 1. Obsidian Syntax

- Wikilinks for entities: `[[notizen/some-thought]]`, `[[entscheidungen/2026-05-19-laptop-kauf]]`.
- Callouts sparse.
- Frontmatter mandatory:

```yaml
type: task | note | decision | journal | ...
status: ...
tags: [tag1, tag2]
created: YYYY-MM-DD
```

## 2. Voice

Specific names, specific consequences. Match the operator's voice (see `profil.md`).

**NEVER use em dashes.** Use periods, commas, colons, or restructure.

## 3. Language

Default DE. Denglish OK. Match user's language.

## 4. Tasks

Folder-as-status: `aufgaben/offen/` → `in-arbeit/` → `erledigt/` → `abgebrochen/`. Move files; don't edit `status:` frontmatter.

## 5. Session-Triggers

| Phrase | Action |
|---|---|
| "close session" | Write `tagebuch/{date}.md`, move open tasks forward |
| "what's open?" | Walk `aufgaben/{offen,in-arbeit}/` |
| "let's realign" | Re-read `profil.md` |

## 6. AI Output Routing

- Task from conversation: `aufgaben/offen/{slug}.md`
- Decision: `entscheidungen/{date}-{slug}.md`
- Note: `notizen/{slug}.md`
- Daily AI log: `tagebuch/{date}.md` (append, don't overwrite)

NEVER write to workspace root.

## 7. Sensitive Content

Credentials, financial details, contracts: NEVER in workspace. Reference via env-var or external store.

## 8. Em Dashes

Forbidden. Non-negotiable.

## 9. Optional Business AOS Sibling

If `../Business AOS/` exists:
- READ access OK for company context.
- WRITE access FORBIDDEN.
- Never copy business content into this personal layer.

## 10. Context First

Read `profil.md` before any work that touches identity, voice, or decision style.
```

- [ ] **Step 2: Commit**

```bash
git add _rules.md
git commit -m "feat: add Personal AI _rules.md"
```

---

### Task 21: Write Personal AI README.md and INSTALL.md

**Files:**
- Create: `~/developer/personal-ai/README.md`
- Create: `~/developer/personal-ai/INSTALL.md`

- [ ] **Step 1: Create README.md**

```markdown
<!--
Personal AI v1.0.0 — © 2026 Gerald Eder
Licensed under MIT License — see LICENSE
-->

# Personal AI

**Dein privater AI-Layer.** Eine Ordner-Struktur in Markdown, die deiner KI dich kennt: Profil, Aufgaben, Tagebuch, Notizen, Entscheidungen.

Klone das Repo, öffne es in deinem AI-Tool, starte das `bootstrap` Playbook. Deine KI weiß dann, wer du bist und wie du arbeitest.

---

## Was Personal AI ist

Ein Folder. Drinnen liegen Markdown-Files für deinen persönlichen Layer:

- **Wer du bist** (`profil.md`) — Identität, Werte, Arbeitsstil
- **Was du tun musst** (`aufgaben/{offen,in-arbeit,erledigt,abgebrochen}/`)
- **Was du denkst** (`notizen/`)
- **Was du entscheidest** (`entscheidungen/`)
- **Was du erlebst** (`tagebuch/`)

Die KI nutzt diesen Kontext, um in deiner Sprache zu schreiben und deinen Stil zu treffen.

---

## Was du bekommst

| Element | Beschreibung |
|---|---|
| **Klare Ordner-Struktur** | profil, aufgaben, notizen, entscheidungen, tagebuch |
| **Folder-as-Status für Tasks** | Move-Files-Pattern statt status-Frontmatter |
| **1 Skill** | personal-audit (Health-Check des Personal Layers) |
| **Tool-agnostisch** | `AGENTS.md` lesen Claude, Codex, Cursor, Gemini nativ |

---

## Quick Start

```bash
mkdir -p ~/ai-os
cd ~/ai-os
git clone https://github.com/gerald-eder/personal-ai.git "Personal AI"
cd "Personal AI"
# Open in your AI tool, run bootstrap playbook
```

Details in [`INSTALL.md`](INSTALL.md).

---

## Optional: Business AOS Companion

Wenn du auch eine Firma führst, kannst du [Business AOS](https://github.com/gerald-eder/business-aos) als Sibling klonen:

```
~/ai-os/
  Personal AI/       # this repo
  Business AOS/      # github.com/gerald-eder/business-aos
```

Beide Repos erkennen einander automatisch. Personal AI lädt dann auch deinen Firmen-Kontext als zusätzliche Quelle. Beide funktionieren auch alleine.

---

## License

MIT. See [`LICENSE`](LICENSE).
```

- [ ] **Step 2: Create INSTALL.md**

```markdown
# Personal AI Install Guide

## Prerequisites

- Git
- An AI coding tool (Claude Code, Cursor, Codex, Gemini CLI)
- macOS or Linux (Windows via WSL)

## Install

```bash
mkdir -p ~/ai-os
cd ~/ai-os
git clone https://github.com/gerald-eder/personal-ai.git "Personal AI"
cd "Personal AI"
```

## Bootstrap

Open the workspace in your AI tool, then invoke the `bootstrap` playbook. It will:

1. Verify the folder name is `Personal AI` (auto-rename if needed).
2. Ask for sync mode: `lokal` (default) or `cloud-drive` (optional).
3. Configure git remotes.
4. Walk you through filling `profil.md`.
5. Detect optional `../Business AOS/` sibling.

## Combined Install (with Business AOS)

If you also want the Business AOS companion:

```bash
cd ~/ai-os
git clone https://github.com/gerald-eder/business-aos.git "Business AOS"
cd "Business AOS"
# Run Business AOS's bootstrap playbook
```

Both repos auto-detect each other.
```

- [ ] **Step 3: Commit**

```bash
git add README.md INSTALL.md
git commit -m "docs: add Personal AI README and INSTALL guides"
```

---

### Task 22: Add LICENSE, VERSION, CHANGELOG.md, .gitignore

**Files:**
- Create: `LICENSE`, `VERSION`, `CHANGELOG.md`, `.gitignore`

- [ ] **Step 1: Copy LICENSE from Business AOS**

```bash
cp ~/developer/agentic-os/LICENSE ~/developer/personal-ai/LICENSE
```

- [ ] **Step 2: Create VERSION**

```bash
echo "1.0.0" > ~/developer/personal-ai/VERSION
```

- [ ] **Step 3: Create CHANGELOG.md**

```markdown
# Changelog

## [1.0.0] — 2026-05-19

### Added

- Initial release. Personal layer extracted from `gerald-eder/agentic-os` v2.0.0 split.
- Folders: `profil.md`, `aufgaben/`, `notizen/`, `entscheidungen/`, `tagebuch/`.
- `personal-audit` skill for layer health-check.
- `bootstrap` playbook with folder-auto-rename.
- Optional sibling detection for `../Business AOS/`.
```

- [ ] **Step 4: Create .gitignore**

```text
# OS
.DS_Store
Thumbs.db

# Editor
.idea/
.vscode/
*.swp
*~

# Python
__pycache__/
*.py[cod]
.pytest_cache/

# Sensitive
*.env
*.secret
secrets/
```

- [ ] **Step 5: Commit**

```bash
cd ~/developer/personal-ai
git add LICENSE VERSION CHANGELOG.md .gitignore
git commit -m "chore: add LICENSE, VERSION 1.0.0, CHANGELOG, .gitignore"
```

---

### Task 23: Build personal-audit skill (with test)

**Files:**
- Create: `.claude/skills/personal-audit/SKILL.md`
- Create: `.claude/skills/personal-audit/audit.py`
- Create: `.claude/skills/personal-audit/test_audit.py`

- [ ] **Step 1: Create skill folder and SKILL.md**

```bash
mkdir -p ~/developer/personal-ai/.claude/skills/personal-audit
```

Write `~/developer/personal-ai/.claude/skills/personal-audit/SKILL.md`:

```markdown
---
name: personal-audit
description: Quick health-check of the Personal AI workspace. Scores 4 dimensions (profile completeness, task discipline, journaling cadence, note volume) and returns a brief report with gap-list. Use when the operator asks for status, sanity-check, or wants to know what is missing.
type: skill
---

# personal-audit

Lightweight health-check of the Personal AI layer.

## Scoring Dimensions

1. **Profile** — is `profil.md` filled? (>= 100 words, sections present)
2. **Tasks** — are tasks being tracked? (any files in `aufgaben/offen/` or `aufgaben/in-arbeit/`; ratio of done vs open)
3. **Journal** — is the journal current? (at least one `tagebuch/` entry in last 7 days)
4. **Notes** — is the operator capturing notes? (>= 1 file in `notizen/`)

Each dimension scores 0-2 (0 missing, 1 weak, 2 healthy). Max score: 8.

## Usage

```bash
python .claude/skills/personal-audit/audit.py
```

Output: JSON with per-dimension score, total score, gap-list.

## Example Output

```json
{
  "profile": 2,
  "tasks": 1,
  "journal": 0,
  "notes": 2,
  "total": 5,
  "max": 8,
  "gaps": [
    "Journal: kein Eintrag in den letzten 7 Tagen. Empfehlung: heute Abend tagebuch/{today}.md schreiben."
  ]
}
```
```

- [ ] **Step 2: Write the failing test first**

Create `~/developer/personal-ai/.claude/skills/personal-audit/test_audit.py`:

```python
"""Tests for personal-audit skill."""
import json
from pathlib import Path
import pytest

from audit import audit_workspace


def test_empty_workspace_scores_zero(tmp_path):
    """A workspace with no profile, tasks, journal, or notes scores 0."""
    (tmp_path / "aufgaben" / "offen").mkdir(parents=True)
    (tmp_path / "aufgaben" / "in-arbeit").mkdir(parents=True)
    (tmp_path / "aufgaben" / "erledigt").mkdir(parents=True)
    (tmp_path / "notizen").mkdir()
    (tmp_path / "tagebuch").mkdir()
    (tmp_path / "profil.md").write_text("")

    result = audit_workspace(tmp_path)

    assert result["profile"] == 0
    assert result["tasks"] == 0
    assert result["journal"] == 0
    assert result["notes"] == 0
    assert result["total"] == 0
    assert result["max"] == 8
    assert len(result["gaps"]) == 4


def test_healthy_workspace_scores_max(tmp_path):
    """A workspace with filled profile, active tasks, recent journal, and notes scores 8."""
    from datetime import date

    (tmp_path / "aufgaben" / "offen").mkdir(parents=True)
    (tmp_path / "aufgaben" / "in-arbeit").mkdir(parents=True)
    (tmp_path / "aufgaben" / "erledigt").mkdir(parents=True)
    (tmp_path / "notizen").mkdir()
    (tmp_path / "tagebuch").mkdir()

    # Profile: 100+ words
    (tmp_path / "profil.md").write_text(" ".join(["wort"] * 120))

    # Tasks: one open, one done
    (tmp_path / "aufgaben" / "offen" / "task-a.md").write_text("task")
    (tmp_path / "aufgaben" / "erledigt" / "task-b.md").write_text("task")

    # Journal: entry today
    today = date.today().isoformat()
    (tmp_path / "tagebuch" / f"{today}.md").write_text("journal")

    # Notes: one note
    (tmp_path / "notizen" / "thought.md").write_text("note")

    result = audit_workspace(tmp_path)

    assert result["profile"] == 2
    assert result["tasks"] == 2
    assert result["journal"] == 2
    assert result["notes"] == 2
    assert result["total"] == 8
    assert result["gaps"] == []


def test_weak_signals_score_one(tmp_path):
    """A workspace with weak signals (short profile, only-done tasks, old journal, no notes) scores intermediate."""
    from datetime import date, timedelta

    (tmp_path / "aufgaben" / "offen").mkdir(parents=True)
    (tmp_path / "aufgaben" / "in-arbeit").mkdir(parents=True)
    (tmp_path / "aufgaben" / "erledigt").mkdir(parents=True)
    (tmp_path / "notizen").mkdir()
    (tmp_path / "tagebuch").mkdir()

    # Profile: short (10 words)
    (tmp_path / "profil.md").write_text(" ".join(["wort"] * 10))

    # Tasks: only done, no open
    (tmp_path / "aufgaben" / "erledigt" / "task-b.md").write_text("task")

    # Journal: older than 7 days
    old = (date.today() - timedelta(days=10)).isoformat()
    (tmp_path / "tagebuch" / f"{old}.md").write_text("journal")

    result = audit_workspace(tmp_path)

    assert result["profile"] == 1
    assert result["tasks"] == 1
    assert result["journal"] == 1
    assert result["notes"] == 0
    assert result["total"] == 3
```

- [ ] **Step 3: Run tests to verify they fail**

```bash
cd ~/developer/personal-ai/.claude/skills/personal-audit
python -m pytest test_audit.py -v 2>&1 | head -20
```

Expected: ImportError or FAIL because `audit.py` does not exist yet.

- [ ] **Step 4: Implement audit.py to pass the tests**

Create `~/developer/personal-ai/.claude/skills/personal-audit/audit.py`:

```python
"""Personal AI workspace audit. Scores 4 dimensions, returns brief health report."""
import json
import sys
from datetime import date, datetime, timedelta
from pathlib import Path


PROFILE_HEALTHY_MIN_WORDS = 100
JOURNAL_RECENCY_DAYS = 7


def _score_profile(workspace: Path) -> tuple[int, str | None]:
    profil = workspace / "profil.md"
    if not profil.exists() or profil.stat().st_size == 0:
        return 0, "Profile: profil.md fehlt oder ist leer. Empfehlung: profil.md ausfüllen (Identität, Werte, Arbeitsstil)."
    words = len(profil.read_text().split())
    if words < PROFILE_HEALTHY_MIN_WORDS:
        return 1, f"Profile: profil.md ist sehr kurz ({words} Wörter). Empfehlung: auf 100+ Wörter erweitern."
    return 2, None


def _score_tasks(workspace: Path) -> tuple[int, str | None]:
    offen = workspace / "aufgaben" / "offen"
    in_arbeit = workspace / "aufgaben" / "in-arbeit"
    erledigt = workspace / "aufgaben" / "erledigt"

    open_count = len([f for f in offen.glob("*.md")]) if offen.exists() else 0
    wip_count = len([f for f in in_arbeit.glob("*.md")]) if in_arbeit.exists() else 0
    done_count = len([f for f in erledigt.glob("*.md")]) if erledigt.exists() else 0

    total = open_count + wip_count + done_count
    if total == 0:
        return 0, "Tasks: keine Aufgaben getrackt. Empfehlung: erste Aufgabe in aufgaben/offen/ anlegen."

    active = open_count + wip_count
    if active == 0:
        return 1, f"Tasks: nur erledigte Aufgaben ({done_count}), keine aktiven. Empfehlung: aktuelle Vorhaben in aufgaben/offen/ erfassen."

    return 2, None


def _score_journal(workspace: Path) -> tuple[int, str | None]:
    tagebuch = workspace / "tagebuch"
    if not tagebuch.exists():
        return 0, "Journal: tagebuch/ existiert nicht."

    entries = list(tagebuch.glob("*.md"))
    if not entries:
        return 0, "Journal: kein Eintrag in tagebuch/. Empfehlung: heute Abend tagebuch/{today}.md schreiben."

    cutoff = date.today() - timedelta(days=JOURNAL_RECENCY_DAYS)
    recent = False
    for entry in entries:
        # Extract YYYY-MM-DD from filename like "2026-05-19.md" or "journal-2026-05-19.md"
        name = entry.stem
        for candidate in (name, name.replace("journal-", "")):
            try:
                entry_date = datetime.strptime(candidate, "%Y-%m-%d").date()
                if entry_date >= cutoff:
                    recent = True
                    break
            except ValueError:
                continue
        if recent:
            break

    if recent:
        return 2, None
    return 1, f"Journal: kein Eintrag in den letzten {JOURNAL_RECENCY_DAYS} Tagen. Empfehlung: heute Abend tagebuch/{date.today().isoformat()}.md schreiben."


def _score_notes(workspace: Path) -> tuple[int, str | None]:
    notizen = workspace / "notizen"
    if not notizen.exists():
        return 0, "Notes: notizen/ existiert nicht."
    count = len([f for f in notizen.glob("*.md")])
    if count == 0:
        return 0, "Notes: keine Notiz in notizen/. Empfehlung: nächsten Gedanken festhalten."
    return 2, None


def audit_workspace(workspace: Path) -> dict:
    """Audit a Personal AI workspace at the given path. Return scores and gap-list."""
    profile_score, profile_gap = _score_profile(workspace)
    tasks_score, tasks_gap = _score_tasks(workspace)
    journal_score, journal_gap = _score_journal(workspace)
    notes_score, notes_gap = _score_notes(workspace)

    gaps = [g for g in (profile_gap, tasks_gap, journal_gap, notes_gap) if g]

    return {
        "profile": profile_score,
        "tasks": tasks_score,
        "journal": journal_score,
        "notes": notes_score,
        "total": profile_score + tasks_score + journal_score + notes_score,
        "max": 8,
        "gaps": gaps,
    }


if __name__ == "__main__":
    target = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()
    result = audit_workspace(target)
    print(json.dumps(result, indent=2, ensure_ascii=False))
```

- [ ] **Step 5: Run tests to verify they pass**

```bash
cd ~/developer/personal-ai/.claude/skills/personal-audit
python -m pytest test_audit.py -v
```

Expected: 3 PASS.

- [ ] **Step 6: Commit**

```bash
cd ~/developer/personal-ai
git add .claude/skills/personal-audit
git commit -m "feat: add personal-audit skill with profile, tasks, journal, notes scoring"
```

---

### Task 24: Build Personal AI bootstrap playbook

**Files:**
- Create: `.claude/playbooks/bootstrap/PLAYBOOK.md`

- [ ] **Step 1: Create folder**

```bash
mkdir -p ~/developer/personal-ai/.claude/playbooks/bootstrap
```

- [ ] **Step 2: Write PLAYBOOK.md**

```markdown
---
name: bootstrap
description: First playbook to run after cloning personal-ai repo. Sets up workspace name, location, git remotes, profile seed. Idempotent — re-run safe.
type: playbook
---

# Bootstrap

Initial setup of a Personal AI workspace. Run once after `git clone`.

## Phase 0: Folder-Name Auto-Rename

```bash
CURRENT_NAME=$(basename "$PWD")
echo "Current folder: $CURRENT_NAME"
```

If `$CURRENT_NAME` is not exactly `Personal AI`:

> [!question] HUMAN-CHECKPOINT
> "Folder heißt '$CURRENT_NAME'. Auf 'Personal AI' umbenennen?
> 1. Ja
> 2. Nein, beibehalten"

If yes:
```bash
cd ..
mv "$CURRENT_NAME" "Personal AI"
cd "Personal AI"
```

## Phase 1: Sync Mode

> [!question] HUMAN-CHECKPOINT
> "Wo soll das Workspace liegen?
> 1. **lokal** — bleibt unter `~/ai-os/Personal AI/`
> 2. **cloud-drive** — Cloud-Drive Provider wählen (Google Workspace, OneDrive, Dropbox), Workspace dorthin verschieben"

Save choice to `.claude/settings.json` field `syncMode`.

If cloud-drive: move workspace to provider's mount path and create symlink at `~/ai-os/Personal AI/`.

## Phase 2: Git Remotes

> [!question] HUMAN-CHECKPOINT
> "Eigenes GitHub-Repo für Versionierung?
> 1. Ja, habe ein Repo → URL eingeben
> 2. Ja, erstellen → öffne github.com, return mit URL
> 3. Nein, nur Template-Updates"

```bash
# Option 1 or 2:
git remote remove origin
git remote add origin {USER_REPO}
git remote add upstream https://github.com/gerald-eder/personal-ai.git

# Option 3:
git remote rename origin upstream
```

## Phase 3: Profile Seed

> [!question] HUMAN-CHECKPOINT
> "profil.md ist leer oder Stub. Jetzt ausfüllen?
> 1. Ja, geführter Fragebogen (5 Minuten)
> 2. Später, ich mache das manuell"

If yes: walk through questions (Identität, Vision, Werte, Arbeitsstil, Sprache). Write answers to `profil.md`.

## Phase 4: Sibling Detection

```bash
if [ -d "../Business AOS" ]; then
  echo "Business AOS sibling detected at ../Business AOS/. Cross-context active."
else
  echo "No Business AOS sibling. Personal AI standalone mode."
fi
```

## Done

```bash
echo "Personal AI bootstrap complete."
```
```

- [ ] **Step 3: Create initial settings.json**

```bash
cat > ~/developer/personal-ai/.claude/settings.json <<'EOF'
{
  "$schema": "https://json.schemastore.org/claude-settings.json",
  "setupMode": null,
  "syncMode": null,
  "version": "1.0.0"
}
EOF
```

- [ ] **Step 4: Commit**

```bash
cd ~/developer/personal-ai
git add .claude/playbooks .claude/settings.json
git commit -m "feat: add Personal AI bootstrap playbook and settings.json"
```

---

### Task 25: Create GitHub repo and push

**Files:**
- GitHub: `gerald-eder/personal-ai` (new public template repo)

- [ ] **Step 1: Create GitHub repo via `gh`**

```bash
gh repo create gerald-eder/personal-ai --public --description "Personal AI Operating System for one individual. Markdown-only, tool-agnostic. Sibling to Business AOS. Built by Gerald Eder." --source=$HOME/developer/personal-ai --remote=origin --push
```

Expected: repo created and pushed.

If push fails because the initial commits weren't on `main` yet, run manually:

```bash
cd ~/developer/personal-ai
git push -u origin main
```

- [ ] **Step 2: Set template flag**

```bash
gh repo edit gerald-eder/personal-ai --template
```

- [ ] **Step 3: Verify visibility, template, default branch**

```bash
gh repo view gerald-eder/personal-ai --json isTemplate,visibility,defaultBranchRef,url
```

Expected: `"isTemplate":true, "visibility":"PUBLIC", "defaultBranchRef":{"name":"main"}, "url":"https://github.com/gerald-eder/personal-ai"`.

- [ ] **Step 4: Tag v1.0.0**

```bash
git tag -a v1.0.0 -m "Personal AI v1.0.0 — initial release, split from agentic-os"
git push origin v1.0.0
```

---

## Phase 3 — Verification

### Task 26: Test Business AOS standalone install

**Files:**
- Test environment: `/tmp/test-business-aos-standalone/`

- [ ] **Step 1: Fresh clone**

```bash
rm -rf /tmp/test-business-aos-standalone
mkdir /tmp/test-business-aos-standalone
cd /tmp/test-business-aos-standalone
git clone https://github.com/gerald-eder/business-aos.git "Business AOS"
cd "Business AOS"
```

Expected: clone succeeds, folder name is `Business AOS`.

- [ ] **Step 2: Verify structure**

```bash
ls -F | sort
test -f ueberblick.md && echo "OK: ueberblick.md at root"
test -f marke.md && echo "OK: marke.md at root"
test -f CLAUDE.md && echo "OK: CLAUDE.md at root"
test -d 00-inbox && echo "OK: 00-inbox/"
test -d kunden && echo "OK: kunden/"
test -d prozesse && echo "OK: prozesse/"
test ! -d firma && echo "OK: no firma/ wrapper"
test ! -d personal && echo "OK: no personal/ layer"
test ! -d _weitere-unternehmen && echo "OK: no multi-biz folder"
```

Expected: all "OK" lines.

- [ ] **Step 3: Verify CLAUDE.md sibling-detection block**

```bash
grep -A 3 "Optional: Personal AI Layer" CLAUDE.md
```

Expected: block exists and mentions `../Personal AI/profil.md`.

- [ ] **Step 4: Verify no broken personal-refs**

```bash
grep -rn "personal/" --include="*.md" --exclude-dir=docs --exclude="CHANGELOG.md" .
```

Expected: zero matches except the sibling-detection block in CLAUDE.md, AGENTS.md, _rules.md, KONTEXT.md (which reference `../Personal AI/`).

- [ ] **Step 5: Verify Python skills still importable**

```bash
cd .claude/skills/check-sync-status
python -m pytest -v
cd /tmp/test-business-aos-standalone/"Business AOS"
```

Expected: all tests PASS.

- [ ] **Step 6: Cleanup**

```bash
cd ~
rm -rf /tmp/test-business-aos-standalone
```

---

### Task 27: Test Personal AI standalone install

**Files:**
- Test environment: `/tmp/test-personal-ai-standalone/`

- [ ] **Step 1: Fresh clone**

```bash
rm -rf /tmp/test-personal-ai-standalone
mkdir /tmp/test-personal-ai-standalone
cd /tmp/test-personal-ai-standalone
git clone https://github.com/gerald-eder/personal-ai.git "Personal AI"
cd "Personal AI"
```

- [ ] **Step 2: Verify structure**

```bash
test -f profil.md && echo "OK: profil.md"
test -d aufgaben/offen && echo "OK: aufgaben/offen/"
test -d aufgaben/in-arbeit && echo "OK: aufgaben/in-arbeit/"
test -d aufgaben/erledigt && echo "OK: aufgaben/erledigt/"
test -d aufgaben/abgebrochen && echo "OK: aufgaben/abgebrochen/"
test -d notizen && echo "OK: notizen/"
test -d entscheidungen && echo "OK: entscheidungen/"
test -d tagebuch && echo "OK: tagebuch/"
test -f CLAUDE.md && echo "OK: CLAUDE.md"
test -f AGENTS.md && echo "OK: AGENTS.md"
test -f _rules.md && echo "OK: _rules.md"
test -f README.md && echo "OK: README.md"
test -f INSTALL.md && echo "OK: INSTALL.md"
test -f LICENSE && echo "OK: LICENSE"
test -f VERSION && echo "OK: VERSION"
test "$(cat VERSION)" = "1.0.0" && echo "OK: VERSION = 1.0.0"
```

Expected: all "OK" lines.

- [ ] **Step 3: Verify CLAUDE.md sibling-detection block**

```bash
grep -A 3 "Optional: Business AOS Layer" CLAUDE.md
```

Expected: block mentions `../Business AOS/ueberblick.md`.

- [ ] **Step 4: Run personal-audit skill against empty workspace**

```bash
cd .claude/skills/personal-audit
python audit.py /tmp/test-personal-ai-standalone/"Personal AI"
```

Expected: JSON output with profile=0 or 1, tasks=0, journal=0, notes=0, gaps list non-empty.

- [ ] **Step 5: Run personal-audit tests**

```bash
python -m pytest test_audit.py -v
```

Expected: 3 PASS.

- [ ] **Step 6: Verify no business-layer references**

```bash
cd /tmp/test-personal-ai-standalone/"Personal AI"
grep -rn "ueberblick\|marke\.md\|wunschkunde-icp\|strategie\.md\|kunden/" --include="*.md" --exclude="CHANGELOG.md" .
```

Expected: only references inside the explicit `../Business AOS/` sibling block.

- [ ] **Step 7: Cleanup**

```bash
cd ~
rm -rf /tmp/test-personal-ai-standalone
```

---

### Task 28: Test combined sibling install

**Files:**
- Test environment: `/tmp/test-ai-os-combined/`

- [ ] **Step 1: Fresh combined clone**

```bash
rm -rf /tmp/test-ai-os-combined
mkdir -p /tmp/test-ai-os-combined/ai-os
cd /tmp/test-ai-os-combined/ai-os
git clone https://github.com/gerald-eder/business-aos.git "Business AOS"
git clone https://github.com/gerald-eder/personal-ai.git "Personal AI"
ls -F
```

Expected output:
```
Business AOS/
Personal AI/
```

- [ ] **Step 2: From Business AOS, verify sibling is detectable**

```bash
cd "Business AOS"
test -d ../"Personal AI" && echo "OK: Personal AI sibling visible from Business AOS"
test -f ../"Personal AI"/profil.md && echo "OK: profil.md reachable"
```

- [ ] **Step 3: From Personal AI, verify sibling is detectable**

```bash
cd ../"Personal AI"
test -d ../"Business AOS" && echo "OK: Business AOS sibling visible from Personal AI"
test -f ../"Business AOS"/ueberblick.md && echo "OK: ueberblick.md reachable"
```

- [ ] **Step 4: Verify cross-references in routing tables**

Open `../Business AOS/CLAUDE.md` and confirm the "Optional: Personal AI Layer" section instructs reading `../Personal AI/profil.md`.

Open `../Personal AI/CLAUDE.md` and confirm the "Optional: Business AOS Layer" section instructs reading `../Business AOS/ueberblick.md`.

- [ ] **Step 5: Cleanup**

```bash
cd ~
rm -rf /tmp/test-ai-os-combined
```

---

### Task 29: Final cross-cutting verification

- [ ] **Step 1: Both repos public + template-flagged**

```bash
gh repo view gerald-eder/business-aos --json isTemplate,visibility,defaultBranchRef,url
gh repo view gerald-eder/personal-ai --json isTemplate,visibility,defaultBranchRef,url
```

Expected both: `"isTemplate":true, "visibility":"PUBLIC"`.

- [ ] **Step 2: Old `agentic-os` URL redirects**

```bash
gh repo view gerald-eder/agentic-os --json url 2>&1
```

Expected: returns `gerald-eder/business-aos` URL (GitHub auto-redirect).

- [ ] **Step 3: Both repos visible on profile**

```bash
gh repo list gerald-eder --limit 20 --json name,isTemplate | grep -E "business-aos|personal-ai"
```

Expected: both repos listed.

- [ ] **Step 4: Tag both at expected versions**

```bash
gh release list --repo gerald-eder/business-aos | head -3
gh release list --repo gerald-eder/personal-ai | head -3
```

Expected: `v2.0.0` for business-aos, `v1.0.0` for personal-ai.

- [ ] **Step 5: Cleanup tmp seed**

```bash
rm -rf /tmp/personal-ai-seed
```

- [ ] **Step 6: Final commit if any doc updates needed in Business AOS**

If verification surfaced doc issues in Business AOS:

```bash
cd ~/developer/agentic-os
# fix the issue
git add -A
git commit -m "docs: post-split verification fixes"
git push origin main
```

---

## Self-Review Notes

This plan covers all 5 sections of the spec:

- **Architecture** → Tasks 2, 3, 4, 17, 18 (disk layout, cross-detection prose)
- **Skills Strategy** → Tasks 9, 10, 11 (Business AOS skill rescope), 23 (new personal-audit)
- **File Move Map** → Tasks 1, 2 (extract personal, flatten firma, delete multi-biz)
- **Bootstrap UX** → Tasks 12 (Business AOS), 24 (Personal AI)
- **Migration Sequence** → Tasks 1-16 (Phase 1), 17-25 (Phase 2), 26-29 (Phase 3)

Three open risks from the spec are mitigated:

- **Existing customers** — Task 16 step 7 renames the GitHub repo so auto-redirects handle old URLs.
- **personal-audit scope creep** — Task 23 explicitly caps the skill at 4 dimensions, score 0-8.
- **Cross-detection prose drift** — Tasks 3 and 18 use mirrored block structure; a future maintenance rule should keep them aligned.
