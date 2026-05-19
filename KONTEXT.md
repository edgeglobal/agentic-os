# KONTEXT — Workspace Scope and Permissions

Scope-gating manifest for this Business AOS workspace. Edit per operator / per team to control what AI agents may read or write.

## Identity

- **Workspace owner:** {fill during bootstrap}
- **Primary user role:** {ceo | vertrieb | marketing | fulfillment | finance-hr}
- **Setup mode:** {solo | team-cloud | team-enterprise}

## Scope — What AI may READ

By default: all folders in this workspace EXCEPT folders listed in "Restricted" below.

## Scope — What AI may WRITE

By default: all folders in this workspace EXCEPT:
- `LICENSE`, `VERSION`, `CHANGELOG.md`, `README.md`, `INSTALL.md` (template files)
- Any folder in "Restricted" below

## Restricted (per operator decision)

Add folder paths here that the current AI role should NOT touch. Examples:
- `finance-hr-admin/` (only finance-hr role agent)
- `intelligence/decisions/` (read-only for non-CEO roles)

```text
# Add restricted paths, one per line, relative to workspace root
```

## Sibling Workspace Awareness

If a sibling folder `../Personal AI/` exists:
- READ access OK for operator identity context.
- WRITE access FORBIDDEN.

## Sync Layer

- **Provider:** {google-drive | onedrive | dropbox | none}
- **Local mount:** {auto-detected during bootstrap}
- **Cloud-Drive stub-detection:** run `.claude/skills/check-sync-status` periodically.
