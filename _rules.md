# Business AOS Rules

Behavioral rules for any AI agent working in this Business AOS workspace.

## 1. Obsidian Syntax

- **Wikilinks** for every entity: `[[kunden/unternehmen/acme]]`, `[[mitarbeiter/anna]]`. Weave into sentences. Never as bullet lists or footnotes.
- **Embeds** for context: `![[ueberblick]]`.
- **Callouts** sparse (1-3 per doc): `> [!type] Title` (note, tip, warning, important, question, todo, success, failure, info).
- **Highlights** rare: `==text==`.
- **Comments** AI-only: `%%internal note%%`.
- **Tags** inline `#tag` or frontmatter `tags: [...]`.

**Frontmatter** mandatory on all notes:

```yaml
type: meeting | decision | project | note | sop | ...
status: ...
tags: [tag1, tag2]
created: YYYY-MM-DD
```

Common additional: `project:`, `team:`, `priority:`, `owner:`.

## 2. Voice

Documents sound like a teammate, never AI. Specific names, specific consequences. Never generic.

- BAD: "The project is progressing well."
- GOOD: "Onboarding 70% done. Next checkpoint: contract signature. Blocked on Acme legal team."

**NEVER use em dashes.** Use periods, commas, colons, or restructure.

## 3. Language

Default DE. Denglish OK. Never force translation. Match the user's language.

## 4. Project Status

Folder-as-status pattern. For projects with status tracking, status equals folder location (e.g. `projekte/aktiv/{name}/` vs `projekte/done/{name}/`). Move files; don't edit `status:` frontmatter.

`owner:` frontmatter mandatory. Allowed values:
- `gerald` (or other Mitarbeiter name)
- `agent:openclaw | agent:hermes | agent:claude | agent:{name}`

## 5. Session-Triggers

| Phrase | Action |
|---|---|
| "what's open?" | Walk `00-inbox/` + `projekte/` for active work |
| "what did I miss?" | Scan `00-inbox/` last 7d, recent `kunden/meetings/` |
| "let's realign" | Re-read `ueberblick.md` + `strategie.md` |
| "let's start fresh" | Discard current thread context |

## 6. Wiki Operations

Three-ops model:

- **Ingest**: capture new info into right folder (inbox, projects, meetings) with frontmatter and Wikilinks.
- **Query**: read existing notes. Use `grep` for keyword scan. Read full file only when scan identifies relevance.
- **Lint**: maintenance. Find orphan notes, broken Wikilinks, stale entries, missing frontmatter.

## 7. Folder Indexes

Each major folder has a `CLAUDE.md`:
- Top: "What's here" overview
- Bottom: "How to use this folder" routing, frontmatter standards, naming conventions

## 8. AI Output Routing

Route AI-generated content by semantic intent:

- Customer-related output: `kunden/`
- Decision record: `intelligence/decisions/{date}-{slug}.md`
- Meeting summary: `kunden/meetings/` or `meetings-intern/`
- Project work: `projekte/{name}/`
- Reference material: appropriate team folder

NEVER save to workspace root.

## 9. Sensitive Content

Credentials, PII, contracts: NEVER in workspace. Reference via env-var or external store (e.g. `secret_ref: ENV_VAR_NAME`).

## 10. Em Dashes

Forbidden. Use periods, commas, colons, or restructure. Non-negotiable.

## 11. Optional Personal AI Sibling

If `../Personal AI/` exists:
- READ access OK for operator context.
- WRITE access FORBIDDEN — never modify, never sync content from there into here.
- If user asks for cross-cutting analysis spanning both, do it read-only.

## 12. Context First

Before any work that touches business context (brand, ICP, offer, pricing, decisions, positioning, strategy), load relevant context files FIRST. Don't ask the user to explain what's already documented.
