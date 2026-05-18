---
name: level-up
description: Use weekly. Triggers: "level up our setup", "weekly improvement", "what should we add next?", "where are the gaps", "next iteration". Identifies the single highest-leverage improvement based on current 4-C-scores + recent friction patterns.
---

# Level-Up-Skill

Weekly improvement ritual. Identifies ONE high-leverage upgrade per week.

## Execution

### Step 1: Quick audit

Invoke `audit` skill, capture 4-C-Scores.

### Step 2: Friction-scan

Read last 7 days of `personal/tagebuch/`. Identify recurring friction patterns:
- Tasks repeatedly carried-forward
- Inbox items not triaged
- Same question asked multiple times (knowledge-gap signal)
- Tool/Agent failures mentioned

### Step 3: Recommend ONE upgrade

Pick the highest-leverage of:

1. **Fill a context-gap** — e.g. `firma/marke.md` has placeholders, fill via `/playbooks/onboard-firma` Sektion 2
2. **Add a SOP** — recurring task without SOP → write one in `firma/prozesse/sops/`
3. **Add a Skill** — recurring AI-task → make it a Skill in `.claude/skills/`
4. **Add a Playbook** — recurring multi-step workflow → make it a Playbook
5. **Add a Connection** — recurring need for external data → install MCP / wire up integration
6. **Establish a cadence** — recurring forgotten ritual → add to `firma/prozesse/workflows/` with schedule

### Step 4: HUMAN-CHECKPOINT

> [!question] HUMAN-CHECKPOINT
> "Empfehlung: {upgrade}. Grund: {friction}. Hilft v.a. bei: {C}. Soll ich loslegen?"

Wait for user OK before executing. If yes, hand off to relevant playbook or perform directly.