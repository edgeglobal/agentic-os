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
