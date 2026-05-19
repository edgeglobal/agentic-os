---
type: tools
status: active
tags: [tools, tech-stack]
created: 2026-05-18
---

# Tech-Stack + Tools

> Befüllt via `/playbooks/onboard-firma` Sektion 5.

## Operative Tools (per Funktion)

| Layer | Tool | Use-Case |
|---|---|---|
| CRM | {{CRM_TOOL}} | {{CRM_USE}} |
| Email | {{EMAIL_TOOL}} | {{EMAIL_USE}} |
| Calendar | {{CALENDAR_TOOL}} | {{CAL_USE}} |
| Project-Mgmt | {{PM_TOOL}} | {{PM_USE}} |
| Communication | {{COMMS_TOOL}} | {{COMMS_USE}} |
| File-Storage | {{STORAGE_TOOL}} | {{STORAGE_USE}} |
| Accounting | {{ACCOUNTING_TOOL}} | {{ACC_USE}} |
| Website | {{WEBSITE_TOOL}} | {{WEB_USE}} |

## AI Models + Compute

- {{AI_MODEL_PRIMARY}}: {{USE_CASE}}
- {{AI_MODEL_SECONDARY}}: {{USE_CASE}}

## MCP Servers (Claude-spezifisch)

| MCP | Purpose |
|---|---|
| {{MCP_1}} | {{PURPOSE}} |
| {{MCP_2}} | {{PURPOSE}} |

## Credentials

NEVER in workspace. Reference via env-var or external secret-store (`~/.secrets`, Vault, 1Password, etc.).

## Sync-Layer

- **Cloud-Drive:** {{GOOGLE_WS | M365 | OTHER}}
- **Mirror-Modus aktiviert für:** `~/ai-workspace/` komplett (außer `firma/ablage/`, inaktive `_weitere-unternehmen/`)
- **GitHub-Repo:** {{REPO_URL}} (origin), {{UPSTREAM}} (upstream für Template-Updates)

## Linked

- [[ueberblick]]
- [[../../INSTALL|Sync-Setup-Anleitung]]
