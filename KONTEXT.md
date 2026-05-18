# AI Workspace — Context Manifest

> Diese Datei wird beim Onboarding (`/playbooks/onboard-mitarbeiter`) pro Mitarbeiter generiert. Aktuell: Default-Template (kein User onboarded).

## Who I am

See: `personal/profil.md`

Always load this first.

## What I have access to

### Personal Workspace (always available)

| Path | Content |
|------|---------|
| `personal/profil.md` | My profile, role, voice, preferences |
| `personal/notizen/` | My personal notes |
| `personal/aufgaben/` | My task lists |
| `personal/tagebuch/` | Daily logs + journal |
| `personal/entscheidungen/` | Personal decisions |

### Company Workspace (role-based)

<!-- DEFAULT-TEMPLATE: Full Access. Bootstrap-Playbook erzeugt rolle-spezifische Version. -->

| Path | Content |
|------|---------|
| `firma/ueberblick.md` | Company overview |
| `firma/marke.md` | Brand voice |
| `firma/wunschkunde-icp.md` | Ideal Customer Profile |
| `firma/strategie.md` | OKRs, priorities |
| `firma/tools.md` | Tech stack |
| `firma/prozesse/` | SOPs |
| `firma/vertrieb/` | Sales |
| `firma/marketing/` | Marketing |
| `firma/fulfillment/` | Operations |
| `firma/finance-hr-admin/` | Finance + HR + Admin |
| `firma/kunden/` | External CRM |
| `firma/projekte/` | Active projects |
| `firma/meetings-intern/` | Internal meetings |
| `firma/mitarbeiter/` | People roster |
| `firma/ablage/` | Archive |

## What I do NOT have access to

<!-- DEFAULT-TEMPLATE: kein Deny. Bootstrap-Playbook setzt role-spezifische Deny-Liste. -->

Paths nicht aufgelistet oben sind nicht synced auf dieses Device und werden nicht referenziert.

## Agent Instructions

When the user asks for help, you operate within this workspace.

**Context loading order:**
1. Load `personal/profil.md` to understand who the user is
2. Load relevant `firma/` subfolder based on the question
3. Never load or reference paths not listed in "What I have access to" above
4. If a question requires data from a restricted path, say so clearly and stop

**Scope rules:**
- Read only what is listed above
- Don't infer or guess content from out-of-scope folders
- Don't mix context from different `firma/` subfolders unless explicitly asked
- `personal/` and `firma/` contexts are always separate unless explicitly combined

**For tasks and notes:**
- New tasks → `personal/aufgaben/offen/`
- New notes → `personal/notizen/`
- Never write to `firma/` folders unless explicitly instructed

---

For tool-agnostic agent intro see `AGENTS.md`. For Claude-specific behavior see `CLAUDE.md`. For universal rules see `_rules.md`.
