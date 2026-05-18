---
type: folder-readme
scope: firma
---

## What's here

Company-owned context. Cloud-synced, role-gated.

| Subfolder | Content |
|---|---|
| `00-inbox/` | Brain-Dumps, Forwarded Mails, Voice-Memos |
| `prozesse/` | SOPs, Workflows, Richtlinien |
| `vertrieb/` | Sales playbooks, scripts, targets |
| `marketing/` | Brand-Assets, Kampagnen, Content |
| `fulfillment/` | Operations, Delivery, Quality |
| `finance-hr-admin/` | Buchhaltung, HR, interne Admin |
| `kunden/` | External CRM (unternehmen, personen, meetings) |
| `projekte/` | Cross-functional projects |
| `meetings-intern/` | Internal meetings (Standup, Quarterly) |
| `mitarbeiter/` | People roster (Menschen + AI-Agents) |
| `ablage/` | Archive |
| `_weitere-unternehmen/` | OPTIONAL: Multi-Biz |

Top-level files: `ueberblick.md`, `marke.md`, `wunschkunde-icp.md`, `strategie.md`, `tools.md`.

## How to use

- All `firma/` content is cloud-synced. Mitarbeiter ohne Access auf einen Subfolder sehen den Folder gar nicht (Sync-Layer-Permissions) oder werden via `.claude/settings.json` Deny-List blockiert (Agent-Layer).
- Multi-Biz: zusätzliche Firmen in `_weitere-unternehmen/<biz-slug>/` mit gleicher Sub-Struktur.
- See `_rules.md` for global rules.
