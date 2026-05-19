---
name: audit
description: Use when user asks for an "audit", "4-C-Score", "find gaps in our AI workspace", "wie steht unser Setup", or wants to score the agentic-os installation. Produces 4-C-Scoreboard with top-3 fixes ranked by leverage. Scoped to the business workspace layer only.
---

# Audit-Skill

Runs the 4-C-Audit on the current business workspace. Reads (never writes). Scores each C out of 25.

## Scope

Structural ("is the Business AOS built right?"), not capability-planning. Capability gaps belong to `level-up`.

## Today's Context

- **Date:** !`date +%Y-%m-%d`
- **Workspace root:** current working directory (sollte ein `~/ai-workspace/` sein)

## The Four Cs (scored 25 each = 100 total)

| Layer | Test |
|---|---|
| **Context** | Knows the business — `ueberblick.md`, `marke.md`, `wunschkunde-icp.md`, `strategie.md`, `tools.md` filled? |
| **Connections** | Reaches the business's tools — `tools.md` documents MCPs, external integrations? GitHub-Remote set? Cloud-Drive sync configured? |
| **Capabilities** | Knows how to do work — skills installed? playbooks installed? SOPs in `prozesse/sops/`? Workflows in `prozesse/workflows/`? |
| **Cadence** | Runs without being asked — scheduled playbooks active? Weekly-review run? Recent commit activity? |

## Execution

### Step 1: Discover

Use Glob + Read:

- Top-level: `KONTEXT.md`, `AGENTS.md`, `CLAUDE.md`, `_rules.md`
- Business context: `ueberblick.md`, `marke.md`, `wunschkunde-icp.md`, `strategie.md`, `tools.md`
- SOPs: glob `prozesse/sops/SOP-*.md` (count)
- Workflows: glob `prozesse/workflows/WF-*.md` (count)
- Richtlinien: glob `prozesse/richtlinien/R-*.md` (count)
- Skills: glob `.claude/skills/*/SKILL.md` (count + names)
- Playbooks: glob `.claude/playbooks/*/PLAYBOOK.md` (count + names)
- Role: read `.claude/settings.json` for `_role`

### Step 2: Score (per C, out of 25)

**Context (max 25):**
- `ueberblick.md` filled (no `{{TEMPLATE}}` placeholders): 6
- `marke.md` filled: 6
- `wunschkunde-icp.md` filled: 6
- `strategie.md` filled with current quarter OKRs: 7

**Connections (max 25):**
- `tools.md` filled: 5
- Cloud-Drive sync evidence (workspace under `~/Library/CloudStorage/` OR `~/OneDrive/`): 5
- GitHub remote set (`git remote -v` returns origin): 5
- `_role` set in `.claude/settings.json` (not default `ceo`): 5
- KONTEXT.md customized for user (not default template): 5

**Capabilities (max 25):**
- 3+ SOPs in `prozesse/sops/`: 5
- 2+ Workflows in `prozesse/workflows/`: 5
- 3 skills installed and complete (`audit`, `check-sync-status`, `level-up`): 5
- 5+ playbooks installed: 5
- 1+ team-specific subfolder content in `vertrieb/` OR `marketing/` OR `fulfillment/`: 5

**Cadence (max 25):**
- Scheduled playbook configured (evidence in `prozesse/workflows/` or `.claude/settings.json`): 10
- Recent commit activity (last 7 days): 10
- Weekly-review playbook installed: 5

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