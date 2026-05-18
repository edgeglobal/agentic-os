---
name: check-sync-status
description: Use when user asks "are my files synced offline?", "check sync", "files showing as stub", "google drive cache check", or before running heavy reads on the workspace. Detects Cloud-Drive placeholder/stub files via macOS xattr inspection.
---

# Check-Sync-Status

Inspects critical workspace files for Cloud-Drive Stub-Status. Stubs = files that appear locally but content lives in cloud (Google Drive Stream, OneDrive Files-On-Demand, iCloud).

## Why

`Read`/`Grep` on stub files trigger background downloads (latency, bandwidth, sometimes offline-fail). Critical files (manifests, profile, brand) should always be Mirror (fully local).

## Critical paths (must be local, not stub)

- `KONTEXT.md`, `AGENTS.md`, `CLAUDE.md`, `_rules.md`
- `personal/profil.md`
- `firma/ueberblick.md`, `firma/marke.md`, `firma/wunschkunde-icp.md`, `firma/strategie.md`, `firma/tools.md`
- `.claude/settings.json`
- All files in `.claude/skills/`, `.claude/playbooks/`, `.claude/role-templates/`

## Execution

### Step 1: Run check

```bash
cd ~/ai-workspace
python3 .claude/skills/check-sync-status/check_sync.py
```

(Script reads the critical-paths list above and reports.)

### Step 2: If stubs found

Show user:

```
⚠️  N critical files are Cloud-Drive stubs (not fully downloaded):
  - KONTEXT.md
  - firma/marke.md
  
Risk: heavy reads will trigger downloads (latency, potential offline failure).

Fix: in Google Drive / OneDrive desktop client, right-click ~/ai-workspace/ folder → "Make available offline" / "Always keep on this device".
```

### Step 3: If clean

```
✅ All critical files are local (Mirror mode active).
```