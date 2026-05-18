---
name: bootstrap
description: First playbook to run after cloning agentic-os repo. Sets up workspace location, sync layer, git remotes, and initial role. Idempotent — re-run safe.
type: playbook
---

# Bootstrap

Initial setup of ai-workspace. Run once after `git clone`.

## Pre-Flight

Check CWD: must be `~/ai-workspace/` (rename folder if needed).

```bash
pwd
# Expected: ends in /ai-workspace
```

## Phase 1: Setup-Mode

> [!question] HUMAN-CHECKPOINT
> "Welcher Setup-Modus?
> 1. **solo** — Solo-Operator. Lokal, kein Cloud-Drive, GitHub als Backup
> 2. **team-cloud** — 5-20 Mitarbeiter. Cloud-Drive primär, GitHub für Template-Updates
> 3. **team-enterprise** — 50+ Mitarbeiter. Cloud-Drive + MDM, Branch-Strategy"

Save choice to `.claude/settings.json` field `setupMode`.

## Phase 2: Workspace Location

Based on mode:

- **solo**: workspace stays at `~/ai-workspace/`. Done.
- **team-cloud**: ask which Cloud-Drive provider (Google Workspace / Microsoft 365 / Dropbox). Move workspace to provider's local mount-path. Update `~/.zshrc` / `~/.bashrc` with symlink: `ln -s "/Users/{user}/Library/CloudStorage/.../ai-workspace" ~/ai-workspace`
- **team-enterprise**: same as team-cloud, plus MDM-deployment instructions in INSTALL-m365.md.

## Phase 3: Git Remotes

> [!question] HUMAN-CHECKPOINT
> "Eigenes GitHub-Repo für Versionierung + Backup?"
> 1. Ja, ich habe ein Repo. → URL eingeben → setze `origin = USER_REPO`, `upstream = edgeglobal/agentic-os`
> 2. Ja, erstellen. → ask user to create on github.com, return with URL
> 3. Nein, nur Template-Updates. → `upstream = edgeglobal/agentic-os` only, kein push

```bash
# Option 1/2:
git remote remove origin
git remote add origin {USER_REPO}
git remote add upstream https://github.com/edgeglobal/agentic-os.git

# Option 3:
git remote rename origin upstream
```

## Phase 4: Sync-Check

Run `check-sync-status` skill. If stubs detected, walk user through "Make Available Offline" in their Cloud-Drive client (link to INSTALL-{provider}.md).

## Phase 5: First Role

> [!question] HUMAN-CHECKPOINT
> "Welche Rolle hast du in der Firma? (Bestimmt deine Access-Permissions.)"
> 1. ceo / Geschäftsführung
> 2. vertrieb / Sales
> 3. marketing
> 4. fulfillment / Operations
> 5. finance-hr

Copy `.claude/role-templates/{role}.json` to `.claude/settings.json` (preserving `setupMode` field).

## Phase 6: Next Steps

Tell user:

```
✅ Bootstrap complete. 

Workspace: ~/ai-workspace
Mode: {mode}
Role: {role}
Origin: {origin or 'none'}
Upstream: edgeglobal/agentic-os

Empfohlene nächste Schritte:
1. `/playbooks/onboard-firma` — Firmen-Kontext aufbauen (7 Sektionen)
2. `/playbooks/onboard-mitarbeiter` — eigenes profil.md + KONTEXT.md generieren  
3. `/skills/audit` — initialen 4-C-Score messen
```