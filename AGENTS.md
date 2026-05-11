<!--
AI OS v0.3.3 — © 2026 Gerald Eder · UmsatzAI
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
├── 01-Firma Home/           ← Firmenweite SoT: markenstimme, unsere-kunden,
│                              unsere-leistungen, unsere-tools, strategie, stakeholder
├── 02-Teams/                ← Pro Team-Funktion eine Mini-Firma
│   ├── marketing-vertrieb/  ← Default-Team (mit website/ als team-spezifischer Sub-Container)
│   ├── fulfillment/         ← Default-Team
│   ├── finance-hr-admin/    ← Default-Team
│   └── _neues-team/         ← Vorlage (kontext, vorlagen, projekte, referenzen, meetings, ablage, skills)
├── 03-CRM/                  ← Customer Relationship: Unternehmen, Personen, Meetings
│   ├── Unternehmen/         ← externe Firmen (Kunden, Lieferanten, Partner, Berater)
│   │   ├── _neues-unternehmen/
│   │   └── acme-gmbh/       ← Beispiel: kontext, gespraeche, ablage
│   ├── Personen/            ← externe Personen (Ansprechpartner, Beirat, Investoren)
│   │   ├── _neue-person/
│   │   └── hans-mueller/    ← Beispiel: kontext mit Verlauf, Vorlieben
│   └── Meetings/            ← **externe** Meetings mit Unternehmen + Personen
│       └── _protokoll-vorlage.md ← Standard-Meeting-Format

(Interne Meetings — Standups, Team-Reviews — liegen in `02-Teams/<team>/meetings/`.)
├── 04-Projekte/             ← Aktive firmenweite oder Cross-Team-Projekte
├── 05-Mitarbeiter/          ← Roster aller Menschen in der Firma
│   └── team-mitglieder.md   ← Liste mit Name, Rolle, Team, optionale Praeferenzen
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

## Schichten (lebt im selben Folder, Permissions per Sub-Folder)

- **Firma-weit** (`01-Firma Home/`, `04-Projekte/`, `05-Mitarbeiter/`, `.claude/skills/`) — alle Mitarbeiter lesen, Operator + Geschaeftsfuehrung schreiben
- **Team** als Mini-Firma (`02-Teams/<team>/`) — eigene `kontext`, `vorlagen`, `projekte`, `referenzen`, `ablage`, `.claude/skills`. Team-Mitglieder schreiben, Rest liest.
- **Externe Unternehmen** (`03-CRM/Unternehmen/<firma>/`) — gezielte Freigaben pro Firma, auch fuer Externe (Steuerberater etc.) moeglich
- **Externe Personen** (`03-CRM/Personen/<name>/`) — Ansprechpartner, Beirat, Investoren, Berater. Pflege durch Teams die Kontakt haben.

Es gibt **keinen Sub-Folder pro Mitarbeiter**. Persoenliche Praeferenzen (Tonfall, Anrede) leben als Spalte im Roster. Brand-Voice ist firmenweit in `01-Firma Home/markenstimme.md`, nicht pro Person.

Permissions per Sub-Folder ueber Cloud-Provider (Google Drive / OneDrive / Dropbox), nicht ueber separate Folder-Wurzeln.

## Wikilink-basiertes CRM-Light

Externe Firmen und Personen werden als eigene Folder gepflegt. Meeting-Notes in `03-CRM/Meetings/external/` verlinken via Wikilinks zu `[[03-CRM/Unternehmen/...]]` und `[[03-CRM/Personen/...]]`. Backlinks in den jeweiligen kontext.md-Files bauen ueber Jahre ein Wissens-Geflecht auf — perfekt fuer KMU ohne CRM-Tool.

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
- User-Content in `01-Firma Home/`, `03-CRM/Unternehmen/` ohne explizite Aufgabe
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
