---
type: folder-readme
scope: firma/kunden
---

## What's here

External CRM-Light. Companies, People, Meetings.

| Subfolder | Content |
|---|---|
| `unternehmen/` | External companies (clients, vendors, partners) |
| `personen/` | External people (contacts at companies) |
| `meetings/` | External meetings (with Wikilinks to unternehmen + personen) |

## How to use

### Companies
- Folder per company: `unternehmen/{slug}/`
- File: `unternehmen/{slug}/kontext.md` with frontmatter `type: company`, `status:`, `relationship: client | vendor | partner | lead`, `industry:`, `created:`
- Wikilinks to people at this company

### People
- Folder per person: `personen/{slug}/`
- File: `personen/{slug}/kontext.md` with frontmatter `type: person`, `status:`, `role:`, `company: [[../unternehmen/{slug}]]`, `created:`

### Meetings
- File: `meetings/{YYYY-MM-DD}-{slug}.md`
- Frontmatter: `type: meeting`, `participants: [...]`, `companies: [...]`, `created:`
- Body: Wikilinks to participants + companies, agenda, decisions, action-items

Internal meetings (Standup, Quarterly, Team-Sync): go to `firma/meetings-intern/`, not here.
