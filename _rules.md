# Operating Rules — agentic-os v1.0

Universal behavior rules for any agent operating in this workspace. Cited from `AGENTS.md`, `CLAUDE.md`, and per-folder `CLAUDE.md` files.

## 1. obsidian-syntax

Always Obsidian-native syntax, never plain markdown:

- **Wikilinks**: `[[Note Name]]`, `[[Note|Display Text]]`. Weave into sentences naturally.
- **Embeds**: `![[Note Name]]`, `![[image.png|300]]`
- **Callouts**: `> [!type] Title` (types: note, tip, warning, important, question, todo, success, failure, info). 1-3 per doc max.
- **Highlights**: `==text==` sparingly.
- **Tags**: `#tag` inline or `tags: [tag1, tag2]` in frontmatter.

**Frontmatter** mandatory on all notes:

```yaml
type: note | task | meeting | decision | ...
status: ...
tags: [tag1, tag2]
created: YYYY-MM-DD
```

## 2. voice

Documents sound like a teammate, never AI. Specific names, specific consequences. Never generic.

- BAD: "The project is progressing well. Key milestones are being tracked."
- GOOD: "Eval framework 70% done. Next checkpoint: judge integration. Blocked on API access."

**NEVER use em dashes.** Use periods, commas, colons, or restructure.

## 3. language

Default DE. Denglish OK (mix DE/EN naturally where it fits, e.g. "Tasks" or "Playbook"). Never force translation.

## 4. tasks

Folder-as-status pattern. Status equals folder location:
- `personal/aufgaben/offen/`: not started
- `personal/aufgaben/in-arbeit/`: actively working
- `personal/aufgaben/erledigt/`: completed
- `personal/aufgaben/abgebrochen/`: dropped

`owner:` frontmatter mandatory. Allowed values: `{user-slug}`, `agent:{name}`, `human:{name}`. Move file across folders to change status. Don't edit `status:` frontmatter.

## 5. session-triggers

| Phrase | Action |
|---|---|
| "close session" | Append `personal/tagebuch/{date}.md`, move open tasks forward |
| "keep this in mind" | Save to right context file. Ambiguous, ask. |
| "what's open?" | Walk `personal/aufgaben/{offen,in-arbeit}` |
| "let's realign" | Re-read `personal/profil.md` + `firma/strategie.md` |

## 6. wiki-operations

Three operations for vault knowledge:

- **Ingest**: capture new info into right folder with proper frontmatter and wikilinks.
- **Query**: read existing notes. Use `grep`/`find` for scanning multiple files.
- **Lint**: maintenance. Find orphan notes, broken wikilinks, stale fleeting notes, missing frontmatter.

## 7. folder-indexes

Per-folder `CLAUDE.md` mandatory for major folders:
- Top: "What's here" overview
- Bottom: "How to use this folder" routing, frontmatter standards

## 8. ai-output-routing

When AI generates a file, route by semantic intent not by current CWD:

- Research output: `personal/notizen/{slug}.md`
- Decision record: `personal/entscheidungen/` or `firma/intelligence/decisions/` (Business)
- Meeting summary: `firma/kunden/meetings/` (extern) or `firma/meetings-intern/`
- Task: active scope's `aufgaben/`, `offen/`
- Daily log: `personal/tagebuch/{date}.md`
- Ambiguous: ask user before saving.

NEVER save to workspace root. NEVER invent a "scratch" folder.

## 9. memory-layer

Memory hierarchy from most-to-least authoritative:
1. **Active scope context** (`personal/profil.md` or `firma/*.md`)
2. **`_rules.md`** (this file)
3. **Recent `personal/tagebuch/`** (last 7 days)
4. **`personal/entscheidungen/`** + `firma/intelligence/decisions/`
5. **`personal/notizen/`** (atomic notes)
6. **`firma/ablage/`** (archive, low priority)

Cite source folder when stating a memory fact. Surface contradictions explicitly.

## 10. human-in-the-loop

Every Playbook has at least one explicit checkpoint:
- **PRE**: before destructive/expensive operations
- **MID**: at branch points where user's judgment changes outcome
- **POST**: review-before-commit/publish

Mark in playbook README with `> [!question] HUMAN-CHECKPOINT` callout.

## 11. tags-discipline

Every note has minimum 2 tags. Hierarchical via slash: `#ai/claude`, `#business/sales`.

## 12. entity-storage

CRM-Light single-source-of-truth: Companies, People, Meetings all live in `firma/kunden/`.

Storage locations:
- Companies → `firma/kunden/unternehmen/{slug}/`
- People → `firma/kunden/personen/{slug}/`
- Meetings → `firma/kunden/meetings/{YYYY-MM-DD}-{slug}.md` (extern) or `firma/meetings-intern/`

Business-context via frontmatter, not folder location.

## 13. skills-vs-playbooks

**Skills** = atomic capabilities. Single concern, callable in many contexts. Lives in `.claude/skills/{name}/SKILL.md`.

**Playbooks** = orchestrators. Multi-step processes that may invoke skills + tools. Lives in `.claude/playbooks/{name}/`.

Rule: when a capability is reused in 2+ playbooks, extract it into its own skill.

## 14. context-first

Before any work that touches business context (brand, ICP, offer, pricing, decisions, strategy), load context from `firma/*.md` FIRST. Don't ask user to explain what's already documented.

The 6 hard rules:
1. Check before asking
2. Trust the @-imports
3. Navigate position-first (folder path = semantic context)
4. Read context files before deciding
5. Never assume current state
6. Workspace is single source of truth

## 15. security-deny-list

Permissions enforced via `.claude/settings.json` Deny-List. CLAUDE.md instructions are probabilistic compliance, settings.json is technical enforcement. Both must be set.

Role-specific templates in `.claude/role-templates/` get copied to `.claude/settings.json` during onboarding.

---

For Claude-specific behavior, see `CLAUDE.md`. For tool-agnostic agent intro, see `AGENTS.md`. For user-specific scope, see `KONTEXT.md`.
