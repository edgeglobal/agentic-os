<!--
AI OS v0.2.0 — © 2026 Gerald Eder · UmsatzAI
Licensed under MIT — see LICENSE
-->

# AI OS — Root Orchestration Contract

This is the entry point for any LLM working inside this folder. Read this file first. It defines where things live and the rules that hold the system together.

> Diese Datei ist auf Englisch, weil sie ein Standard-Vertrag für AI-Tools ist (Claude Code, Codex, Cursor und Gemini lesen `AGENTS.md` nativ). Die User-Inhalte (Vorlagen, SOPs, Wissen) sind auf Deutsch.

## What this folder is

A **markdown-only AI Operating System** for small businesses (KMU, 2–15 employees). Plain text files connected by Obsidian-style `[[wikilinks]]` and per-section `INDEX.md` hubs. No databases. The vault is human-readable, syncable via Dropbox/Google Drive/OneDrive, and works in any text editor or AI tool.

You can open this folder in Claude Cowork (Desktop), Claude Code, Codex CLI, Gemini CLI, Cursor, Obsidian, or VS Code. The structure works the same way in all of them.

## Folder map

```
agentic-os/
├── 00-Inbox/                ← Wo Mitarbeiter rohe Inputs reinwerfen
├── 01-Firma/                ← Firmenweite SoT: markenstimme, unsere-kunden,
│                              unsere-leistungen, unsere-tools, strategie, stakeholder
├── 02-Vorlagen/             ← Templates: Angebot, Meeting-Protokoll, LinkedIn-Post, etc.
├── 03-Kunden/               ← Pro Kunde ein Ordner mit kontext, gespraeche, ablage
├── 04-Projekte/             ← Aktive Projekte (firmenweite oder Cross-Team)
├── 05-Mitarbeiter/          ← Roster aller Menschen in der Firma
│   └── team-mitglieder.md   ← Liste mit Name, Rolle, Team, optionale Praeferenzen
├── 06-Teams/                ← Pro Team-Funktion ein Sub-Folder (kontext, .claude/skills)
│   ├── marketing-vertrieb/  ← Default-Team
│   ├── fulfillment/         ← Default-Team
│   ├── finance-hr-admin/    ← Default-Team
│   └── _neues-team/         ← Vorlage zum Duplizieren
├── 07-Meetings/             ← Meeting-Notizen
├── 99-Archiv/               ← Erledigtes
│
├── Team-Wissen/             ← Operating know-how
│   ├── SOPs/                ← Standardabläufe (atomar, ein Job pro File)
│   ├── Workflows/           ← Wiederkehrende Orchestrierungen
│   ├── Richtlinien/         ← Statische Regeln (Naming, Ton)
│   └── Session-Logs/        ← Append-only Sitzungs-Gedächtnis
│
└── .claude/skills/          ← Firmenweite Skills (audit, onboard, level-up,
                               neuer-kunde, session-abschluss)
```

## Drei Schichten (lebt im selben Folder, Permissions per Sub-Folder)

- **Firma-weit** (`01-Firma/`, `02-Vorlagen/`, `04-Projekte/`, `.claude/skills/`, `05-Mitarbeiter/team-mitglieder.md`) — alle Mitarbeiter lesen, Operator + Geschaeftsfuehrung schreiben
- **Team** (`06-Teams/<team>/`) — Team-Mitglieder schreiben, Rest liest
- Zusaetzlich Sonderbereich **Kunden** (`03-Kunden/<kunde>/`) — gezielte Freigaben pro Kunde, auch fuer Externe (Steuerberater etc.) moeglich

Es gibt **keinen Sub-Folder pro Mitarbeiter**. Persoenliche Praeferenzen (Tonfall, Anrede) leben als Spalte im Roster. Brand-Voice ist firmenweit in `01-Firma/markenstimme.md`, nicht pro Person.

Permissions per Sub-Folder ueber Cloud-Provider (Google Drive / OneDrive / Dropbox), nicht ueber separate Folder-Wurzeln.

## Hard rules

### 1. SSOT (Single Source of Truth)

Jeder Fakt lebt in genau einer Datei. Überall sonst wird via `[[wikilink]]` darauf verwiesen. Keine Kopie. Keine Duplikate.

Wenn du beim Schreiben den gleichen Fakt zweimal triffst — stop. Wähle ein Zuhause für ihn, und verlinke vom anderen Ort dorthin.

### 2. Memory-Vorrang

Lokale Datei schlägt globalen Memory. Wenn `AGENTS.md` in diesem Ordner X sagt und dein globaler Memory Y, folge X.

### 3. Wikilink-Konvention

Jeder Querverweis nutzt `[[wikilinks]]`.

- `[[dateiname]]` wenn der Name im Vault eindeutig ist
- `[[ordner/dateiname]]` bei Kollisionsrisiko
- Bild-Embeds: `![[Bilder/2026/05/2026-05-09-screenshot.png]]`

Siehe [[Team-Wissen/Richtlinien/R-001-namenskonventionen]].

### 4. Datums-Ordner-Schachtelung

`Team-Wissen/Session-Logs/` schachtelt nach Jahr und Monat: `<root>/YYYY/MM/YYYY-MM-DD-<slug>.md`. Wenn der Ordner nicht existiert, lege ihn an.

Konzept-Ordner (Wissen, Vorlagen) bleiben flach. Eine Datei pro Konzept. Das Wiki verbindet sie.

### 5. Markdown-only

Keine SQLite. Keine Datenbank. Session-Logs sind Markdown. Cross-Session-Lerneffekte werden in `Team-Wissen/INDEX.md` angehängt.

### 6. Team-Wissen Taxonomie

- **SOPs** — atomare Verfahren. Ein Job, eine Datei. Dateiname: `SOP-NNN-<titel>.md`
- **Workflows** — wiederkehrende Multi-Step-Orchestrierungen. Dateiname: `WF-NNN-<titel>.md`. Sie referenzieren SOPs und Richtlinien, duplizieren sie aber nie.
- **Richtlinien** — statische Referenz-Info. Dateiname: `R-NNN-<titel>.md`. SOPs und Workflows verlinken via `[[wikilink]]` darauf.

### 7. Nicht-Bemächtigung

Du änderst niemals:
- User-Content in `01-Firma/`, `03-Kunden/` ohne explizite Aufgabe
- Diese Root-`AGENTS.md`

## Where to start

- **Erstmals hier?** Lies `Team-Wissen/INDEX.md` und starte das Onboarding via `/onboard` Skill (Claude Code) oder sage: "Lass uns AI OS einrichten."
- **Neuen Mitarbeiter onboarden?** Folge [[SOP-001-neuen-mitarbeiter-onboarden]].
- **Neuen Kunden anlegen?** Folge [[SOP-002-neuen-kunden-anlegen]].
- **Brauchst Naming-Regeln?** Siehe [[R-001-namenskonventionen]].
- **Sehen wo dein Setup steht?** Lass `/audit` laufen.

## Session-Ende

Am Ende jeder Session: schreibe ein Session-Log nach `Team-Wissen/Session-Logs/YYYY/MM/YYYY-MM-DD-<slug>.md`. Das Log enthält Entscheidungen, User-Realignments und Deltas zum vorherigen Plan. Cross-links zu früheren Logs via `[[wikilink]]`.

Sag "Session abschließen" oder nutze `/session-abschluss` (Claude Code).

---

Built with care by [Gerald Eder](https://geraldeder.com) · [UmsatzAI](https://umsatzai.com) · MIT License
