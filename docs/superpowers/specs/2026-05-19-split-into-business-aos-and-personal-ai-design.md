# Split agentic-os into Business AOS + Personal AI

**Date:** 2026-05-19
**Status:** Approved (pending spec review)
**Owner:** Gerald Eder

## Problem

The monolithic `gerald-eder/agentic-os` repo bundles two distinct AI Operating Systems behind a single template: a Personal layer (`personal/`) and a Business layer (`firma/`). Customers cannot adopt one without the other. The focus is on the Business layer, and the bundled Personal layer dilutes the customer-facing product.

The repo also carries a multi-business concept (`firma/_weitere-unternehmen/_template/`) that does not match the intended use case. One Business AOS clone should represent one business.

## Goal

Two separate GitHub template repos, both standalone, that compose cleanly when a solopreneur installs both.

- `gerald-eder/business-aos` — primary product. Full operating system for **one** business.
- `gerald-eder/personal-ai` — companion product. Lighter operating system for a person's private layer.

Each works alone. When both are installed as siblings under `~/ai-os/`, their CLAUDE.md instructions detect the sibling and load it as additional context.

## Non-Goals

- **No multi-business inside one Business AOS.** No holding structure, no sub-companies, no `_weitere-unternehmen/`. One folder = one business. Multiple businesses = multiple clones.
- **No meta-repo, no parent CLAUDE.md generator.** The two repos coordinate purely through prose instructions in their own CLAUDE.md files.
- **No cross-layer audit/level-up skill in v1.** Skills score only their own layer. Cross-cutting analysis is future work.

## Architecture

### Disk layout when both installed

```
~/ai-os/
  Business AOS/                       # gerald-eder/business-aos clone
    .git/
    .claude/                          # business-scoped skills, playbooks, role-templates
    CLAUDE.md
    AGENTS.md
    KONTEXT.md
    _rules.md
    README.md
    INSTALL.md
    LICENSE
    VERSION                           # 2.0.0
    CHANGELOG.md
    ueberblick.md                     # this business
    marke.md
    strategie.md
    tools.md
    wunschkunde-icp.md
    00-inbox/
    ablage/
    finance-hr-admin/
    fulfillment/
    kunden/
      meetings/
      personen/
      unternehmen/
    marketing/
    meetings-intern/
    mitarbeiter/
    projekte/
    prozesse/
      richtlinien/
      sops/
      workflows/
    vertrieb/
  Personal AI/                        # gerald-eder/personal-ai clone
    .git/
    .claude/                          # personal-scoped, minimal
    CLAUDE.md
    AGENTS.md
    _rules.md
    README.md
    INSTALL.md
    LICENSE
    VERSION                           # 1.0.0
    CHANGELOG.md
    profil.md
    aufgaben/
      offen/
      in-arbeit/
      erledigt/
      abgebrochen/
    entscheidungen/
    notizen/
    tagebuch/
```

Both can be installed in isolation. `~/ai-os/Business AOS/` alone or `~/ai-os/Personal AI/` alone is a complete OS.

### Cross-Detection

Each repo's CLAUDE.md contains a prose block telling the orchestrator to check for a sibling and load it as additional context if present.

In **Business AOS** `CLAUDE.md`:

> ## Optional: Personal AI Layer
> If a sibling folder `../Personal AI/` exists, read its `profil.md` for operator context. Treat that file as authoritative for the operator's identity, voice, working style, and decision style. Wikilinks like `[[../Personal AI/profil]]` resolve naturally.

In **Personal AI** `CLAUDE.md`:

> ## Optional: Business AOS Layer
> If a sibling folder `../Business AOS/` exists, read its `ueberblick.md` for company context. When the operator references "die Firma", "der Kunde XY", or any business-scoped concept, that sibling is the source of truth.

No @-imports across repos (file may not exist). Pure prose-driven, robust against missing siblings.

### Skills Strategy

**In Business AOS** `.claude/skills/`:

- `audit/` — 4-C-Score (Context, Connections, Capabilities, Cadence) scoped to business layer only. Strip all personal-references.
- `level-up/` — weekly improvement ritual scoped to business layer.
- `check-sync-status/` — xattr-based Cloud-Drive stub detection. Works on whatever folder it runs in, no layer-specific logic. Light edit.

**In Business AOS** `.claude/playbooks/`:

- `bootstrap/` — initial Business AOS setup wizard. Adapted from current, personal-layer steps removed. Auto-renames clone folder to `Business AOS` if customer cloned with different name.
- `onboard-firma/` — keep (the 7-section company interview). Update doc-refs only.
- `onboard-mitarbeiter/`, `onboard-unternehmen/`, `onboard-person/` — keep.
- `session-abschluss/`, `weekly-review/` — keep, scope to business only.
- `migrate-from-v0.5.0/` — keep for legacy users.
- **Drop** `promote-multi-biz/` — multi-biz concept removed.

**In Business AOS** `.claude/role-templates/`: keep all five (ceo, vertrieb, marketing, fulfillment, finance-hr).

**In Personal AI** `.claude/skills/`:

- `personal-audit/` — new, simple. Scores Personal AI layer: profil.md filled? aufgaben/ has open items? tagebuch/ entries recent? notizen/ count? Returns a brief score and gap-list. Lightweight v1.

**In Personal AI** `.claude/playbooks/`:

- `bootstrap/` — new, simpler. Workspace location, git remote, sync layer (lokal vs Cloud-Drive). Auto-renames clone folder to `Personal AI` if customer cloned with different name.

### File Move Map

| Current location in `gerald-eder/agentic-os` | New location |
|---|---|
| `firma/*` (all contents) | `gerald-eder/business-aos` repo root |
| `firma/_weitere-unternehmen/` | **DELETED** (no multi-biz concept) |
| `personal/*` (all contents) | `gerald-eder/personal-ai` repo root |
| `CLAUDE.md` | Split. Business AOS gets a business-scoped CLAUDE.md, Personal AI gets a personal-scoped CLAUDE.md. |
| `AGENTS.md` | Split into two scoped versions. |
| `KONTEXT.md` | Move to Business AOS (scope-gating is mainly a business concern). Personal AI does not need KONTEXT.md in v1. |
| `_rules.md` | Split. Business AOS keeps business rules (folder-as-status for tasks if Business has tasks, wikilinks, em-dash ban, sensitive content). Personal AI gets a minimal subset focused on personal-layer rules. |
| `README.md` | Split. Each repo gets its own customer-facing README. |
| `INSTALL.md` | Split. Each repo gets its own install guide. |
| `LICENSE` | Copy to both. |
| `VERSION` | Business AOS bumps to `2.0.0` (breaking restructure). Personal AI starts at `1.0.0`. |
| `CHANGELOG.md` | Business AOS continues the current changelog with a v2.0.0 entry. Personal AI starts a fresh changelog. |
| `.claude/skills/audit/`, `level-up/`, `check-sync-status/` | Move to Business AOS, strip personal-refs. |
| `.claude/skills/personal-audit/` | **NEW** in Personal AI. |
| `.claude/playbooks/bootstrap/` | Two copies: business-scoped in Business AOS, personal-scoped in Personal AI. |
| `.claude/role-templates/*.json` | Move to Business AOS only. |
| `.claude/settings.json` | Copy to both, scoped per repo. |
| `.github/` | Move to Business AOS. Personal AI gets a fresh `.github/` with minimal workflow scaffold. |
| `.gitignore` | Copy to both, scoped. |

### Bootstrap UX

**Business AOS Bootstrap** (run after `git clone`):

1. **Folder-Name Auto-Rename.** Detect CWD folder name. If not `Business AOS`, ask: "Rename to `Business AOS`?" If yes, rename via `mv` + update symlinks. If user declines, proceed but warn that some scripts expect the standardized name.
2. **Setup Mode.** Solo / Team-Cloud / Team-Enterprise. Save to `.claude/settings.json` `setupMode`.
3. **Workspace Location.** Based on mode, move workspace to Cloud-Drive mount if team-cloud or team-enterprise.
4. **Git Remotes.** Configure `origin` (customer's repo) and `upstream` (`gerald-eder/business-aos`).
5. **Sync Check.** Run `check-sync-status` skill. If stubs detected, walk user through "Make Available Offline".
6. **First Role.** Pick a role-template (ceo, vertrieb, marketing, fulfillment, finance-hr). Install into appropriate folder's `.claude/`.
7. **Sibling Detection.** Check `../Personal AI/`. If present, log: "Personal AI sibling detected. Cross-context active."

**Personal AI Bootstrap** (run after `git clone`):

1. **Folder-Name Auto-Rename.** Detect CWD folder name. If not `Personal AI`, ask: "Rename to `Personal AI`?" Same pattern.
2. **Sync Mode.** Lokal-only vs Cloud-Drive (less common for Personal but possible).
3. **Git Remotes.** Configure `origin` and `upstream` (`gerald-eder/personal-ai`).
4. **Profile Seed.** Walk user through filling `profil.md` (name, role, values, working style).
5. **Sibling Detection.** Check `../Business AOS/`. If present, log: "Business AOS sibling detected."

## Migration Sequence

### Phase 1: Restructure existing `agentic-os` repo into Business AOS

1. In `~/developer/agentic-os/`, create branch `restructure/v2-split` from `main`.
2. Move all of `firma/*` to repo root. Delete the `firma/` wrapper folder.
3. Delete `firma/_weitere-unternehmen/` entirely (no multi-biz).
4. Extract `personal/*` to a temporary working folder outside the repo (e.g. `/tmp/personal-ai-seed/`). Remove `personal/` from the repo.
5. Rewrite `CLAUDE.md` to be business-scoped. Add Optional Personal AI Layer block.
6. Rewrite `AGENTS.md` to be business-scoped.
7. Rewrite `_rules.md`, business-scoped.
8. Keep `KONTEXT.md` in Business AOS, edit to remove personal-layer references.
9. Rewrite `README.md` to be Business AOS focused (drop personal layer mentions).
10. Update `INSTALL.md` accordingly.
11. Strip personal-refs from `.claude/skills/audit/`, `level-up/`, `check-sync-status/`.
12. Update `.claude/playbooks/bootstrap/PLAYBOOK.md` (drop personal-layer steps, add folder-rename step).
13. Delete `.claude/playbooks/promote-multi-biz/` if it exists.
14. Bump `VERSION` to `2.0.0`.
15. Add `CHANGELOG.md` entry for v2.0.0 documenting the breaking split.
16. Commit. Open PR (or fast-forward to main).
17. Push to GitHub.
18. Rename GitHub repo `gerald-eder/agentic-os` → `gerald-eder/business-aos`. GitHub auto-redirects old URLs.
19. Update local remote URL: `git remote set-url origin https://github.com/gerald-eder/business-aos.git`.
20. Verify template-flag still active. Re-set if needed via `gh repo edit gerald-eder/business-aos --template`.

### Phase 2: Create `personal-ai` repo

21. Create GitHub repo `gerald-eder/personal-ai` (public).
22. Initialize local: `mkdir ~/developer/personal-ai && cd ~/developer/personal-ai && git init && git branch -m main`.
23. Copy `/tmp/personal-ai-seed/*` to repo root.
24. Write `CLAUDE.md` (personal-scoped, with Optional Business AOS Layer block).
25. Write `AGENTS.md` (personal-scoped).
26. Write `_rules.md` (minimal personal-scoped).
27. Write `README.md` (Personal AI focused).
28. Write `INSTALL.md`.
29. Copy `LICENSE` from Business AOS.
30. `VERSION` = `1.0.0`.
31. Initialize `CHANGELOG.md` with v1.0.0 entry.
32. Build `.claude/skills/personal-audit/SKILL.md` (new, simple).
33. Build `.claude/playbooks/bootstrap/PLAYBOOK.md` (Personal AI version).
34. Build `.claude/settings.json` (personal-scoped).
35. Initial commit. Add remote. Push to `main`.
36. Set template-flag: `gh repo edit gerald-eder/personal-ai --template`.

### Phase 3: Verify

37. Test customer flow for Business AOS alone: clone, run bootstrap, verify standalone operation.
38. Test customer flow for Personal AI alone: clone, run bootstrap, verify standalone operation.
39. Test combined: clone both as siblings under `~/ai-os/`. Verify both CLAUDE.md detect the sibling. Verify wikilinks resolve.

## Open Risks

- **Existing customers of `agentic-os`.** Repo is 2 hours old, template-flag fresh. Risk minimal. GitHub auto-redirect handles old URLs.
- **`personal-audit` scope creep.** First version stays light: 4-5 checks, brief score, gap list. Resist adding complex weights or trend analysis.
- **Cross-detection prose drift.** If Business AOS's "Optional Personal AI Layer" block and Personal AI's "Optional Business AOS Layer" block diverge over time, integration breaks silently. Mitigation: identical structure, mirror updates as policy.

## Definition of Done

- [ ] `gerald-eder/business-aos` exists, template-flagged, v2.0.0, all `firma/*` content at root, no `personal/`, no `_weitere-unternehmen/`.
- [ ] `gerald-eder/personal-ai` exists, template-flagged, v1.0.0, all personal content at root.
- [ ] Both READMEs explain standalone use AND optional sibling pattern.
- [ ] Both bootstrap playbooks run cleanly in isolation.
- [ ] Combined install at `~/ai-os/{Business AOS,Personal AI}/` works end-to-end.
- [ ] Old `agentic-os` URL redirects to `business-aos`.

## Out of Scope (Future Work)

- Cross-layer audit skill (scores both layers, requires sibling-aware logic).
- Symlink-based shortcuts (e.g. Business AOS exposing `_personal -> ../Personal AI/`).
- Notion-sync layer for Personal AI.
- Multi-business support (deliberately not solved here; multiple clones is the answer).
