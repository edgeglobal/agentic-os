# Changelog

Alle nennenswerten Änderungen an AI OS werden hier dokumentiert.

Format folgt [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versionierung folgt [Semantic Versioning](https://semver.org/lang/de/).

## [0.3.0] — 2026-05-11

### Changed

- **Folder-Renames + Renumerierung:**
  - `01-Firma/` → `01-Firma Home/` (mit Leerzeichen, SharePoint-Style)
  - `03-Kunden/` → `03-Unternehmen/` (alle externen Firmen, nicht nur Kunden)
  - `04-Projekte/` → `05-Projekte/` (Platz fuer Personen)
  - `05-Mitarbeiter/` → `06-Mitarbeiter/`
  - `06-Teams/` → `07-Teams/`
  - `07-Meetings/` → `08-Meetings/`
- `02-Vorlagen/` enthaelt nur noch **firmenweite** Templates (meeting-protokoll). Team-spezifische Vorlagen wandern in die Team-Folder.

### Added

- **`04-Personen/`** (NEU): pro externe Person ein Sub-Folder mit kontext.md. Ansprechpartner, Beirat, Investoren, Berater. Sub-Vorlage `_neue-person/`.
- **`03-Unternehmen/`** mit `_neues-unternehmen/`-Vorlage. Frontmatter mit `beziehung: [kunde, lieferant, partner, berater, beirat, mitbewerber]` — ein Unternehmen kann mehrere Beziehungs-Typen haben.
- **`08-Meetings/internal/` + `external/`** Sub-Struktur. External-Meetings haben Wikilinks zu `[[03-Unternehmen/...]]` und `[[04-Personen/...]]` — Backlinks bauen Wissens-Geflecht ueber Jahre auf.
- **Team-Folder als Mini-Firma**: jeder Team-Folder hat jetzt `kontext.md`, `vorlagen/`, `projekte/` (mit `_neues-projekt/`-Sub-Vorlage inkl. briefing, status, entscheidungen, outputs), `referenzen/`, `ablage/`, `.claude/skills/`.
- Team-spezifische Vorlagen verschoben: `angebot.md`, `linkedin-post.md`, `kunden-onboarding.md` aus `02-Vorlagen/` → `07-Teams/marketing-vertrieb/vorlagen/`.
- README erklaert "CRM-Light durch Wikilinks" — wie Unternehmen + Personen + Meetings sich gegenseitig referenzieren.

### Architecture Decisions

- **Externe Firmen + Personen als zentrale Wissens-Schicht.** Statt CRM-Tool zu fordern: AI OS modelliert Unternehmen und Personen als eigene Folder. Meetings verlinken via Wikilinks. Ueber Jahre baut sich Kunden-/Kontakt-Wissen auf, das in jedem Cloud-Sync-Editor zugaenglich ist. Rationale: viele KMU haben kein CRM, AI OS soll die Luecke fuellen.
- **Team = Mini-Firma.** Jedes Team hat strukturell dieselbe Tiefe wie die Firma (Identitaet, Vorlagen, Projekte, Referenzen, Skills). Vorlagen leben dort wo sie genutzt werden, nicht zentral. Rationale: team-spezifische Outputs sind die Mehrheit; zentrale Vorlagen sind nur das wirklich firmenweit Universelle.
- **Meetings zentral mit internal/external-Split.** Statt verstreuter Meeting-Notes in Kunden-/Projekt-Foldern: zentrale Heimat in `08-Meetings/`. Wikilinks erzeugen die Verteilung. Rationale: Cross-Team-Suche, Wissens-Aufbau, klare Heimat fuer Transkripte.

## [0.2.0] — 2026-05-11

### Changed

- Brand-Name: "Agentic OS" → "AI OS — Agentic Operating System für KMUs"
- GitHub-Repo-Description white-label-konform (keine Quellen-Attribution mehr)
- `05-Team/` umbenannt zu `06-Mitarbeiter/` (klarere Semantik: Menschen, nicht AI-Specialists)
- `06-Meetings/` umbenannt zu `08-Meetings/` (macht Platz für `07-Teams/`)
- README.md, INSTALL.md, AGENTS.md auf neue Struktur aktualisiert

### Added

- `07-Teams/` neuer Top-Level-Folder für Funktions-Teams
- 3 Default-Teams vorbefüllt: `marketing-vertrieb/`, `fulfillment/`, `finance-hr-admin/` (jeweils mit `kontext.md` + `.claude/skills/`)
- `07-Teams/_neues-team/` als Vorlage zum Duplizieren für weitere Teams
- `01-Firma Home/strategie.md` (Ziele, Prioritäten, Metriken)
- `01-Firma Home/stakeholder.md` (externe Partner, Schlüsselpersonen)
- README erklärt das Drei-Schichten-Modell (Firma / Team / Mitarbeiter) explizit
- INSTALL hat einen "Wo gehören Files hin?"-Abschnitt

### Architecture Decisions

- **Ein Cloud-Folder pro Firma, mehrere Schichten als Sub-Folder** statt physisch getrennter Folder-Wurzeln. Permissions kommen vom Cloud-Sync pro Sub-Folder. Rationale: weniger Setup-Friktion für Office-Worker, Pfade variieren nicht pro Mitarbeiter-Rechner.
- **Kein Sub-Folder pro Mitarbeiter.** `06-Mitarbeiter/` enthält nur einen Roster (`team-mitglieder.md`) mit optionaler Präferenz-Spalte pro Person. Rationale: Brand-Voice ist firmenweit (`01-Firma Home/markenstimme.md`), persönliche Files pro Person bringen für KMU mehr Pflegeaufwand als Wert.

## [0.1.0] — 2026-05-09

### Initial release

- 9 Hauptordner-Struktur (Inbox, Wissen, Vorlagen, Kunden, Projekte, Team, Meetings, Archiv)
- 4 AI-Spezialisten (Larry, Penn, Pax, Nolan) mit Routing-Tabelle
- Team-Wissen-Layer mit SOPs, Workflows, Richtlinien, Session-Logs
- 5 Skills für Claude Code: audit, onboard, level-up, neuer-kunde, session-abschluss
- Vorlagen für Markenstimme, ICP, Angebot, Meeting-Protokoll, LinkedIn-Post
- 3 Standard-SOPs (Mitarbeiter onboarden, Kunde anlegen, Meeting vorbereiten)
- Tool-agnostisch: AGENTS.md als Standard für Claude, Codex, Cursor, Gemini
- ADAPTER-PROMPT.md für Tool-Initialisierung
- README, INSTALL Guide, MIT License
