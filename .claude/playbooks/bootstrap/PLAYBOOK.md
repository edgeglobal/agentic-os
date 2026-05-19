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