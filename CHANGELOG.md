# Changelog

Alle nennenswerten Änderungen an AI OS werden hier dokumentiert.

Format folgt [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Versionierung folgt [Semantic Versioning](https://semver.org/lang/de/).

## [0.4.0] — 2026-05-11

### Changed

- **Onboard-Skill auf 4 Modi aufgebohrt:**
  - **Firma** (Erst-Setup): 7-Sektionen-Interview befuellt alle 6 Files in `01-Firma Home/` plus Mitarbeiter-Roster. Akzeptiert hochgeladene Dokumente (Brand-Brief, Pitch-Deck, ICP-Doc) zur Anreicherung.
  - **Team** (neuer Team-Folder): 4 Sektionen — Wer-wir-sind, Tools, Regeln, Glossar. Schreibt `02-Teams/<team>/kontext.md` + Skill-Vorschlaege.
  - **Unternehmen** (neuer externer Firmen-Folder): 5 Sektionen — Stammdaten, Beziehung, Schluesselpersonen, Was-wir-machen, Tonalitaet. Schreibt `03-CRM/Unternehmen/<slug>/kontext.md`.
  - **Person** (neuer externer Personen-Folder): 4 Sektionen — Basis, Verlauf, Persoenliches, Strategische Relevanz. Schreibt `03-CRM/Personen/<slug>/kontext.md` plus Backlink im Unternehmen.

### Architecture Decision

- **Onboard ist das EINE Setup-Tool fuer alle vier Bereiche.** Statt vier separate Skills (`onboard`, `neuer-kunde`, `neue-person`, `neues-team`) ein zentraler Skill mit Modus-Auswahl. Rationale: konsistente UX, ein Trigger-Verb, eine Wartungsstelle. Voice-Sample-Paste-Rule bleibt erhalten (kein Wispr-Flow-Verweis — Tool-Empfehlungen gehoeren nicht in den Skill).

## [0.3.3] — 2026-05-11

### Changed

- **CRM-Container eingefuehrt.** Unternehmen, Personen und externe Meetings wandern unter `03-CRM/`:
  - `03-Unternehmen/` → `03-CRM/Unternehmen/`
  - `04-Personen/` → `03-CRM/Personen/`
  - `07-Meetings/external/*` → `03-CRM/Meetings/` (nur externe)
- **Interne Meetings wandern in den jeweiligen Team-Folder** unter `02-Teams/<team>/meetings/`. Standups, Wochen-Reviews, Retrospektiven gehoeren zum Team, nicht ins CRM.
- Renumerierung:
  - `05-Projekte/` → `04-Projekte/`
  - `06-Mitarbeiter/` → `05-Mitarbeiter/`
- README, AGENTS, INSTALL aktualisiert auf neue Struktur.

### Added

- `03-CRM/README.md` erklaert warum die drei Sub-Folder zusammen sind: Unternehmen (mit wem), Personen (mit wem konkret), Meetings (was wurde besprochen) — Wikilinks bauen das Wissens-Geflecht.
- `02-Teams/<team>/meetings/` als Standard-Sub-Folder fuer interne Team-Meetings.

### Architecture Decisions

- **CRM-Light als eigene Container-Schicht.** Statt Unternehmen, Personen und externe Meetings nebeneinander auf Top-Level: ein semantischer CRM-Container der die Zusammenhaenge sichtbar macht. Rationale: KMU ohne CRM-Tool nutzen diese drei Folder als Lightweight-CRM, deshalb gehoeren sie auch visuell zusammen.
- **Interne Meetings im Team-Folder.** Standups, Wochen-Reviews, Retros sind Team-Operations — sie gehoeren zum Team, nicht ins CRM. Konsistent mit "Team = Mini-Firma": jedes Team hat seine eigenen Meetings.

## [0.3.2] — 2026-05-11

### Added

- `02-Teams/marketing-vertrieb/website/` (team-spezifischer Sub-Container, leer ausser README)
- Hinweis in `_neues-team/README`: jedes Team kann eigene Sub-Container anlegen wenn sinnvoll (Beispiele: Marketing hat `website/`, Fulfillment koennte `lager/` haben, Finance koennte `buchhaltung/`)

## [0.3.1] — 2026-05-11

### Changed

- **Teams aus `07-` nach `02-` verschoben.** Direkt nach `01-Firma Home/` — Teams sind der Hauptarbeitsbereich, gehoeren nach Firma.
- **Meetings aus `08-` nach `07-` verschoben.** Konsekutive Nummerierung nachdem `02-Vorlagen/` weggefallen ist.

### Removed

- **`02-Vorlagen/` Folder entfernt.** Vorlagen sind in der Praxis team-spezifisch — kein Bedarf fuer firmenweiten Vorlagen-Container. Team-spezifische Vorlagen leben in `02-Teams/<team>/vorlagen/`.
- `meeting-protokoll.md` verschoben nach `03-CRM/Meetings/_protokoll-vorlage.md` (gehoert dorthin wo Meetings liegen).

### Architecture Decision

- **Keine zentralen Vorlagen.** Was firmenweit als Template gilt, ist entweder Brand-Voice-Regel (gehoert in `01-Firma Home/markenstimme.md`) oder team-spezifisch (gehoert in `02-Teams/<team>/vorlagen/`). Ein zentraler Vorlagen-Container war unklar und unbefuellt. Rationale: KISS, kein Folder ohne klaren Pflegeauftrag.

## [0.3.0] — 2026-05-11

### Changed

- **Folder-Renames + Renumerierung:**
  - `01-Firma/` → `01-Firma Home/` (mit Leerzeichen, SharePoint-Style)
  - `03-Kunden/` → `03-CRM/Unternehmen/` (alle externen Firmen, nicht nur Kunden)
  - `04-Projekte/` → `04-Projekte/` (Platz fuer Personen)
  - `05-Mitarbeiter/` → `05-Mitarbeiter/`
  - `06-Teams/` → `07-Teams/`
  - `03-CRM/Meetings/` → `08-Meetings/`
- `02-Vorlagen/` enthaelt nur noch firmenweite Templates (meeting-protokoll). Team-spezifische Vorlagen wandern in die Team-Folder.

### Added

- **`03-CRM/Personen/`** (NEU): pro externe Person ein Sub-Folder mit kontext.md. Ansprechpartner, Beirat, Investoren, Berater. Sub-Vorlage `_neue-person/`.
- **`03-CRM/Unternehmen/`** mit `_neues-unternehmen/`-Vorlage. Frontmatter mit `beziehung: [kunde, lieferant, partner, berater, beirat, mitbewerber]` — ein Unternehmen kann mehrere Beziehungs-Typen haben.
- **`08-Meetings/internal/` + `external/`** Sub-Struktur. External-Meetings haben Wikilinks zu `[[03-CRM/Unternehmen/...]]` und `[[03-CRM/Personen/...]]` — Backlinks bauen Wissens-Geflecht ueber Jahre auf.
- **Team-Folder als Mini-Firma**: jeder Team-Folder hat jetzt `kontext.md`, `vorlagen/`, `projekte/` (mit `_neues-projekt/`-Sub-Vorlage inkl. briefing, status, entscheidungen, outputs), `referenzen/`, `ablage/`, `.claude/skills/`.
- Team-spezifische Vorlagen verschoben: `angebot.md`, `linkedin-post.md`, `kunden-onboarding.md` aus `02-Vorlagen/` → `07-Teams/marketing-vertrieb/vorlagen/`.
- README erklaert "CRM-Light durch Wikilinks" — wie Unternehmen + Personen + Meetings sich gegenseitig referenzieren.

### Architecture Decisions

- **Externe Firmen + Personen als zentrale Wissens-Schicht.** Statt CRM-Tool zu fordern: AI OS modelliert Unternehmen und Personen als eigene Folder. Meetings verlinken via Wikilinks. Ueber Jahre baut sich Kunden-/Kontakt-Wissen auf, das in jedem Cloud-Sync-Editor zugaenglich ist. Rationale: viele KMU haben kein CRM, AI OS soll die Luecke fuellen.
- **Team = Mini-Firma.** Jedes Team hat strukturell dieselbe Tiefe wie die Firma (Identitaet, Vorlagen, Projekte, Referenzen, Skills). Vorlagen leben dort wo sie genutzt werden, nicht zentral. Rationale: team-spezifische Outputs sind die Mehrheit; zentrale Vorlagen sind nur das wirklich firmenweit Universelle.
- **Meetings zentral mit internal/external-Split.** Statt verstreuter Meeting-Notes in Kunden-/Projekt-Foldern: zentrale Heimat in `03-CRM/Meetings/`. Wikilinks erzeugen die Verteilung. Rationale: Cross-Team-Suche, Wissens-Aufbau, klare Heimat fuer Transkripte.

## [0.2.0] — 2026-05-11

### Changed

- Brand-Name: "Agentic OS" → "AI OS — Agentic Operating System für KMUs"
- GitHub-Repo-Description white-label-konform (keine Quellen-Attribution mehr)
- `05-Team/` umbenannt zu `05-Mitarbeiter/` (klarere Semantik: Menschen, nicht AI-Specialists)
- `06-Meetings/` umbenannt zu `03-CRM/Meetings/` (macht Platz für `06-Teams/`)
- README.md, INSTALL.md, AGENTS.md auf neue Struktur aktualisiert

### Added

- `06-Teams/` neuer Top-Level-Folder für Funktions-Teams
- 3 Default-Teams vorbefüllt: `marketing-vertrieb/`, `fulfillment/`, `finance-hr-admin/` (jeweils mit `kontext.md` + `.claude/skills/`)
- `06-Teams/_neues-team/` als Vorlage zum Duplizieren für weitere Teams
- `01-Firma Home/strategie.md` (Ziele, Prioritäten, Metriken)
- `01-Firma Home/stakeholder.md` (externe Partner, Schlüsselpersonen)
- README erklärt das Drei-Schichten-Modell (Firma / Team / Mitarbeiter) explizit
- INSTALL hat einen "Wo gehören Files hin?"-Abschnitt

### Architecture Decisions

- **Ein Cloud-Folder pro Firma, mehrere Schichten als Sub-Folder** statt physisch getrennter Folder-Wurzeln. Permissions kommen vom Cloud-Sync pro Sub-Folder. Rationale: weniger Setup-Friktion für Office-Worker, Pfade variieren nicht pro Mitarbeiter-Rechner.
- **Kein Sub-Folder pro Mitarbeiter.** `05-Mitarbeiter/` enthält nur einen Roster (`team-mitglieder.md`) mit optionaler Präferenz-Spalte pro Person. Rationale: Brand-Voice ist firmenweit (`01-Firma Home/markenstimme.md`), persönliche Files pro Person bringen für KMU mehr Pflegeaufwand als Wert.

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
