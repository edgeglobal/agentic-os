# Changelog

Alle nennenswerten Änderungen an AI OS werden hier dokumentiert.

Format folgt [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versionierung folgt [Semantic Versioning](https://semver.org/lang/de/).

## [0.2.0] — 2026-05-11

### Changed

- Brand-Name: "Agentic OS" → "AI OS — Agentic Operating System für KMUs"
- GitHub-Repo-Description white-label-konform (keine Quellen-Attribution mehr)
- `05-Team/` umbenannt zu `05-Mitarbeiter/` (klarere Semantik: Menschen, nicht AI-Specialists)
- `06-Meetings/` umbenannt zu `07-Meetings/` (macht Platz für `06-Teams/`)
- README.md, INSTALL.md, AGENTS.md auf neue Struktur aktualisiert

### Added

- `06-Teams/` neuer Top-Level-Folder für Funktions-Teams
- 3 Default-Teams vorbefüllt: `marketing-vertrieb/`, `fulfillment/`, `finance-hr-admin/` (jeweils mit `kontext.md` + `.claude/skills/`)
- `06-Teams/_neues-team/` als Vorlage zum Duplizieren für weitere Teams
- `01-Firma/strategie.md` (Ziele, Prioritäten, Metriken)
- `01-Firma/stakeholder.md` (externe Partner, Schlüsselpersonen)
- README erklärt das Drei-Schichten-Modell (Firma / Team / Mitarbeiter) explizit
- INSTALL hat einen "Wo gehören Files hin?"-Abschnitt

### Architecture Decisions

- **Ein Cloud-Folder pro Firma, mehrere Schichten als Sub-Folder** statt physisch getrennter Folder-Wurzeln. Permissions kommen vom Cloud-Sync pro Sub-Folder. Rationale: weniger Setup-Friktion für Office-Worker, Pfade variieren nicht pro Mitarbeiter-Rechner.
- **Kein Sub-Folder pro Mitarbeiter.** `05-Mitarbeiter/` enthält nur einen Roster (`team-mitglieder.md`) mit optionaler Präferenz-Spalte pro Person. Rationale: Brand-Voice ist firmenweit (`01-Firma/markenstimme.md`), persönliche Files pro Person bringen für KMU mehr Pflegeaufwand als Wert.

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
