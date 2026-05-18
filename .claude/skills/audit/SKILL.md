---
name: audit
description: Use when user asks for an "audit", "4-C-Score", "find gaps in our AI workspace", "wie steht unser Setup", or wants to score the agentic-os installation. Produces 4-C-Scoreboard with top-3 fixes ranked by leverage.
---

# Audit-Skill

Runs the 4-C-Audit on the current workspace. Reads (never writes). Scores each C out of 25.

## Scope

Structural ("is the AI-OS built right?"), not capability-planning. Capability gaps belong to `level-up`.

## Today's Context

- **Date:** !`date +%Y-%m-%d`
- **Workspace root:** current working directory (sollte ein `~/ai-workspace/` sein)

## The Four Cs (scored 25 each = 100 total)

| Layer | Test |
|---|---|
| **Context** | Knows the business — `firma/ueberblick.md`, `marke.md`, `wunschkunde-icp.md`, `strategie.md`, `tools.md` filled? `personal/profil.md` filled? |
| **Connections** | Reaches the user's stuff — `firma/tools.md` documents MCPs, external integrations? GitHub-Remote set? Cloud-Drive sync configured? |
| **Capabilities** | Knows how to do work — skills installed? playbooks installed? SOPs in `firma/prozesse/sops/`? Workflows in `firma/prozesse/workflows/`? |
| **Cadence** | Runs without being asked — `personal/tagebuch/{date}.md` written recently? Scheduled playbooks active? Weekly-review run? |

## Execution

### Step 1: Discover

Use Glob + Read:

- Top-level: `KONTEXT.md`, `AGENTS.md`, `CLAUDE.md`, `_rules.md`
- Firma: `firma/ueberblick.md`, `firma/marke.md`, `firma/wunschkunde-icp.md`, `firma/strategie.md`, `firma/tools.md`
- Personal: `personal/profil.md`
- SOPs: glob `firma/prozesse/sops/SOP-*.md` (count)
- Workflows: glob `firma/prozesse/workflows/WF-*.md` (count)
- Richtlinien: glob `firma/prozesse/richtlinien/R-*.md` (count)
- Skills: glob `.claude/skills/*/SKILL.md` (count + names)
- Playbooks: glob `.claude/playbooks/*/PLAYBOOK.md` (count + names)
- Recent tagebuch: glob `personal/tagebuch/2026-*.md` (sort by date, last 7 days)
- Tasks: count `personal/aufgaben/{offen,in-arbeit}/*.md`
- Role: read `.claude/settings.json` for `_role`

### Step 2: Score (per C, out of 25)

**Context (max 25):**
- `firma/ueberblick.md` filled (no `{{TEMPLATE}}` placeholders): 5
- `firma/marke.md` filled: 5
- `firma/wunschkunde-icp.md` filled: 5
- `firma/strategie.md` filled with current quarter OKRs: 5
- `personal/profil.md` filled: 5

**Connections (max 25):**
- `firma/tools.md` filled: 5
- Cloud-Drive sync evidence (workspace under `~/Library/CloudStorage/` OR `~/OneDrive/`): 5
- GitHub remote set (`git remote -v` returns origin): 5
- `_role` set in `.claude/settings.json` (not default `ceo`): 5
- KONTEXT.md customized for user (not default template): 5

**Capabilities (max 25):**
- 3+ SOPs in `firma/prozesse/sops/`: 5
- 2+ Workflows in `firma/prozesse/workflows/`: 5
- 3 skills installed and complete (`audit`, `check-sync-status`, `level-up`): 5
- 5+ playbooks installed: 5
- 1+ team-specific subfolder content in `firma/vertrieb/` OR `firma/marketing/` OR `firma/fulfillment/`: 5

**Cadence (max 25):**
- `personal/tagebuch/{today-3d}.md` exists: 10
- `personal/aufgaben/in-arbeit/` non-empty: 5
- Weekly-review file from last 7 days in `personal/tagebuch/`: 5
- Recent commit activity (last 7 days): 5

### Step 3: Output

```
🎯 4-C-AUDIT — {DATE}

| Layer | Score |
|---|---|
| Context | XX/25 |
| Connections | XX/25 |
| Capabilities | XX/25 |
| Cadence | XX/25 |
| **TOTAL** | **XX/100** |

## Strengths

1. {top strength}
2. {second strength}

## Top 3 Leverage Fixes

1. **{fix}** — adds {N} points. Command: `{exact command}`
2. **{fix}** — adds {N} points. Command: `{exact command}`
3. **{fix}** — adds {N} points. Command: `{exact command}`
```

Always rank fixes by **leverage** (points-per-effort), not raw point-gain.