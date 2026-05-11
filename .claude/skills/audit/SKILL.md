---
name: audit
description: Use when the user asks for an "audit", "AI OS audit", "wie steht unser Setup", "4 C's score", "find gaps in our AI OS", "audit unseren setup", or wants to score their Agentic OS installation. Produces a Four-Cs scoreboard with top-3 fixes ranked by leverage.
---

## What this skill does

Runs the **Four Cs Audit** on the current Agentic OS installation. Reads (never writes) the project's structure, files, skills, agents, and references. Scores each of the Four Cs out of 25. Surfaces strengths and the top 3 leverage-weighted gaps with concrete next-step commands.

**Scope is structural — "is the AI OS built right?"** It is NOT a capability planner. Capability gaps belong to `/level-up`. The audit answers: are the files, folders, registries, and connections in good shape?

First run is the baseline. Re-run weekly to watch the score climb.

## Today's context

- **Date:** !`date +%Y-%m-%d`
- **Project root:** the current working directory (sollte ein Agentic OS Vault sein)

## The Four Cs (scored 25 each = 100 total)

| Schicht | Test |
|---|---|
| **Context** | Knows the business — `01-Firma Home/`, `markenstimme.md`, `unsere-kunden.md`, `unsere-leistungen.md`, `team-mitglieder.md` |
| **Connections** | Reaches the user's stuff — Org-Skills installed, MCPs configured, external tool integrations |
| **Capabilities** | Knows how to do work — Spezialisten in `Team/`, SOPs in `Team-Wissen/SOPs/`, Workflows |
| **Cadence** | Runs without being asked — Session-Logs being written, scheduled triggers, recurring rituals |

## Execution

### Step 1: Discover the project shape

The audit looks for **patterns and intent**, not exact paths. Use Glob and Read to check:

**Operating manual:** `AGENTS.md` (root), `CLAUDE.md` if exists.
**Knowledge files:** `01-Firma Home/markenstimme.md`, `01-Firma Home/unsere-kunden.md`, `01-Firma Home/unsere-leistungen.md`, `05-Team/team-mitglieder.md`.
**Specialists:** `Team/<Name>/AGENTS.md` — count.
**SOPs:** `Team-Wissen/SOPs/SOP-*.md` — count.
**Workflows:** `Team-Wissen/Workflows/WF-*.md` — count.
**Richtlinien:** `Team-Wissen/Richtlinien/R-*.md` — count.
**Session-Logs:** `Team-Wissen/Session-Logs/YYYY/MM/*.md` — count + most recent date.
**Customer folders:** `03-Unternehmen/<name>/_hub.md` — count.
**Project folders:** `05-Projekte/<name>/_hub.md` — count.
**Skills:** `.claude/skills/*/SKILL.md` — count + names.
**Connection mechanisms:**
- MCPs: `.mcp.json`, `.claude/settings.json`
- Org-Skills (only detectable as a configured Team-Plan; user reports)

### Step 2: Score each C (25 points each)

#### Context (25 pts)

| Criterion | Points | How to detect |
|---|---|---|
| AGENTS.md exists with proper structure | 5 | Read AGENTS.md, check for proper section structure |
| markenstimme.md filled (>200 words, not just template) | 5 | Read file, count non-placeholder content |
| unsere-kunden.md filled (>200 words) | 5 | Same |
| unsere-leistungen.md filled (>200 words) | 5 | Same |
| team-mitglieder.md has ≥1 real entry | 5 | Read file, check non-placeholder rows |

#### Connections (25 pts)

| Criterion | Points | How to detect |
|---|---|---|
| Sync-layer is set up (folder is in Dropbox/GDrive/OneDrive) | 5 | Check working directory path |
| Org-Skills installed (Team Plan active) | 5 | Ask user — not detectable from filesystem |
| MCP-Server configured (≥1) | 5 | Check `.mcp.json` or settings |
| External service integrations (Notion, Calendar, Gmail) referenced | 5 | Grep AGENTS.md and CLAUDE.md for service mentions |
| Documented connections (any file describing what's connected) | 5 | Look for `verbindungen.md` or similar |

#### Capabilities (25 pts)

| Criterion | Points | How to detect |
|---|---|---|
| 3 Standard-Teams existieren (marketing-vertrieb, fulfillment, finance-hr-admin) | 10 | Count `07-Teams/*/kontext.md` ≥ 3 |
| ≥1 zusätzlicher Spezialist gehired | 5 | Count `Team/*/AGENTS.md` > 4 |
| ≥3 SOPs definiert | 5 | Count `Team-Wissen/SOPs/SOP-*.md` ≥ 3 |
| ≥1 Workflow definiert | 5 | Count `Team-Wissen/Workflows/WF-*.md` ≥ 1 |

#### Cadence (25 pts)

| Criterion | Points | How to detect |
|---|---|---|
| Session-Logs werden geschrieben (≥1 in letzten 7 Tagen) | 10 | Check `Team-Wissen/Session-Logs/YYYY/MM/` for recent files |
| Session-Logs gehen ≥4 Wochen zurück | 5 | Count distinct months in Session-Logs |
| ≥1 Kunde ist angelegt mit Hub | 5 | Count `03-Unternehmen/*/_hub.md` ≥ 1 |
| ≥1 aktives Projekt mit Hub | 5 | Count `05-Projekte/*/_hub.md` ≥ 1 |

### Step 3: Identify top 3 gaps by leverage

For each criterion that lost points: leverage = (points lost) × (impact multiplier).

**Impact multipliers:**
- 0 Wissens-Files gefüllt: **4x** (Die KI kann nichts personalisieren)
- 0 Sync-Layer: **3x** (Team kann nicht zusammenarbeiten)
- 0 Spezialisten gehired: **2x** (kein Wachstum, keine Differenzierung)
- 0 SOPs: **2x** (Team-Mitglieder bekommen keine Anleitung)
- 0 Session-Logs in 7 Tagen: **2x** (Memory-Layer tot)
- 0 Kunden/Projekte angelegt: **1.5x** (Vault wird nicht produktiv genutzt)
- All others: **1x**

Sort gaps by leverage descending. Take top 3. For each, write a one-line concrete next step.

### Step 4: Output the report

Print directly in chat (Markdown, German). Format:

```
# Agentic OS Audit — {date}
**Score: {total}/100** ({stage})

Stage thresholds:
- 0-39 → Stage 0: Fundament
- 40-69 → Stage 1: Aufgebaut
- 70-89 → Stage 2: Wachsend
- 90-100 → Stage 3: Autonom

## Scoreboard

Context        {bar}  {n}/25  {label}
Connections    {bar}  {n}/25  {label}
Capabilities   {bar}  {n}/25  {label}
Cadence        {bar}  {n}/25  {label}

(bar = ## per 5pts; label = "Stark" ≥20, "Solide" 15-19, "Dünn" 8-14, "Fehlt" <8)

## Stärken
- {1-3 short bullets from highest-scoring criteria}

## Top 3 Lücken (nach Hebelwirkung)
1. **{gap name}** (-{points} × {multiplier})
   → {concrete next-step}
2. **{gap name}** (-{points} × {multiplier})
   → {concrete next-step}
3. **{gap name}** (-{points} × {multiplier})
   → {concrete next-step}

## Empfohlener nächster Schritt: {single most leveraged action}

---
Strukturelle Lücken nur. Für CAPABILITY-Lücken (was euer AI OS könnte aber nicht tut), läuft /level-up nach diesem Audit.
```

### Step 5: Offer to save the report

After printing, ask: "Soll ich den Audit unter `99-Archiv/audits/audit-{date}.md` ablegen, damit ihr Score über Zeit tracken könnt?" If yes, write it.

## Notes

- **Read-only by default.** Modify keine User-Files. Einziger optionaler Write ist der Audit-Report.
- **Be flexible about file names.** Don't penalize for non-canonical names if intent is captured.
- **Honest, not generous.** A 95/100 ist ein Flex. Most setups land 40-70.
- **Don't suggest skills that don't exist.** Point to what's actually available.
- **Speed matters.** Report in under 60 seconds wall-clock.