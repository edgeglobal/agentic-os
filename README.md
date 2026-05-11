<!--
AI OS v0.3.0 — © 2026 Gerald Eder · UmsatzAI
Licensed under MIT License — see LICENSE
-->

# AI OS

**Agentic Operating System für KMUs.**

Eine sofort einsatzbereite Ordnerstruktur für KMU (2–15 Mitarbeiter), die mit Claude (Cowork Desktop oder Claude Code), Codex, Gemini oder Cursor zusammenarbeitet. Markdown-only. Tool-agnostisch. Keine Datenbank. Funktioniert in jedem Texteditor — und in jedem AI-Tool.

> Gebaut von [Gerald Eder](https://geraldeder.com) bei [UmsatzAI](https://umsatzai.com) — AI-Beratung für Mittelstand und Solopreneure im DACH-Raum.

---

## Was das ist

Stellen Sie sich vor, Ihr Unternehmen hätte einen Assistenten, der:

- die Markenstimme kennt
- jeden Kunden im Detail versteht
- alle SOPs befolgen kann
- Meeting-Protokolle schreibt
- die Inbox sortiert
- nie etwas vergisst

Genau das ist AI OS. Ein gemeinsamer Wissensordner + klare Regeln, wie Mensch und KI zusammenarbeiten.

## Was Sie bekommen

| Element | Beschreibung |
|---|---|
| **Klare Ordner-Struktur** | Inbox, Firma Home, Vorlagen, Unternehmen, Personen, Projekte, Mitarbeiter, Teams, Meetings, Archiv |
| **CRM-Light auf Markdown** | `03-Unternehmen/` und `04-Personen/` als zentrale Wissens-Schicht — perfekt für KMU ohne CRM |
| **Team-Folder als Mini-Firma** | Jedes Team hat eigene kontext, vorlagen, projekte, referenzen, ablage, skills |
| **Vorbefuellte Default-Teams** | Marketing & Vertrieb, Fulfillment, Finance/HR/Admin — anpassbar oder löschbar |
| **Universelle Firma-Context-Files** | Markenstimme, Wunschkunden, Leistungen, unsere-tools, Strategie, Stakeholder |
| **Meetings zentral mit Backlinks** | `08-Meetings/internal/` und `external/` — Wikilinks zu Unternehmen + Personen bauen Wissen über Jahre auf |
| **SOPs & Workflows** | Wie Sie neue Mitarbeiter onboarden, Kunden anlegen, Meetings vorbereiten |
| **5 Skills für Claude Code** | audit, onboard, level-up, neuer-kunde, session-abschluss |
| **Tool-agnostisch** | `AGENTS.md` ist der Standard, den Claude Code, Codex, Cursor und Gemini nativ lesen |

## Für wen ist das

- Solopreneure, die mit ein paar VAs arbeiten
- KMU mit 2–15 Mitarbeitern
- Beratungen, Agenturen, Coaches, Steuerberater, Anwälte, Handwerker
- Alle, die strukturiertes Wissen mit AI verbinden wollen

## Was Sie NICHT brauchen

- ❌ Programmierkenntnisse
- ❌ Server, Hosting, Datenbanken
- ❌ Einen DevOps-Mitarbeiter
- ❌ GitHub für die tägliche Nutzung (nur einmal zum Download)

## Was Sie brauchen

- ✅ **Claude Team Plan** ($25/Mitarbeiter/Monat) — für Org-Skills
- ✅ **Claude Cowork Desktop App** — für nicht-technische Mitarbeiter
- ✅ **Ein Sync-Tool** — Dropbox, Google Drive oder OneDrive (was Sie schon haben)
- ✅ **30 Minuten Zeit** für die Erstinstallation

---

## Schnellstart in 5 Minuten

Lesen Sie die [INSTALL.md](INSTALL.md) für die ausführliche Anleitung. Hier die Kurzfassung:

```bash
# 1. Repo klonen oder als ZIP herunterladen
git clone https://github.com/edgeglobal/agentic-os.git mein-business-os

# 2. In Sync-Ordner verschieben (Dropbox/GDrive/OneDrive)
mv mein-business-os ~/Dropbox/

# 3. In Claude Cowork oder Claude Code öffnen
# Cowork: "Open Folder" → ~/Dropbox/mein-business-os
# Code:   cd ~/Dropbox/mein-business-os && claude

# 4. Initialisieren
# Sagen Sie zur AI: "Initialisiere dich in diesem Ordner"
```

Die KI liest `AGENTS.md`, stellt sich vor, fragt nach Ihrer Firma und füllt die Vorlagen aus.

---

## Wie es funktioniert

```
┌─────────────────────────────────────────────────────┐
│  Anthropic Cloud — Claude Team Plan                 │
│  ├── Skills (vom Owner verwaltet, automatisch       │
│  │   verteilt an alle Team-Mitglieder)              │
│  └── 200k Context, jährliche Allocation             │
└─────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────┐
│  Claude Cowork (Desktop) oder Code (VS Code)        │
│  zeigt auf den Sync-Ordner:                         │
│                                                      │
│   ~/Dropbox/Muster GmbH/  (oder GDrive, OneDrive)   │
│   ├── 01-Firma Home/     ← firmenweite SoT          │
│   ├── 02-Vorlagen/       ← firmenweite Templates    │
│   ├── 03-Unternehmen/    ← externe Firmen           │
│   ├── 04-Personen/       ← externe Personen         │
│   ├── 05-Projekte/       ← Cross-Team-Projekte      │
│   ├── 06-Mitarbeiter/    ← Roster                   │
│   ├── 07-Teams/          ← pro Funktion eine Mini-Firma │
│   ├── 08-Meetings/       ← internal/ + external/    │
│   ├── Team-Wissen/SOPs/  ← Standardabläufe          │
│   ├── .claude/skills/    ← Firmenweite Skills       │
│   └── ...                                            │
└─────────────────────────────────────────────────────┘
```

**Der Trick:** Skills werden über Anthropic verteilt (Schicht 1). Daten werden über Dropbox/GDrive synchronisiert (Schicht 2). Die zwei Schichten sind getrennt — das macht das System einfach und robust.

## Schichten in einer einzigen Folder-Hierarchie

AI OS modelliert mehrere Schichten in **einem** Cloud-Folder, nicht in physisch getrennten Wurzeln. Permissions kommen vom Cloud-Sync pro Sub-Folder:

| Bereich | Wo | Wer schreibt | Wer liest |
|---|---|---|---|
| **Firma-weit** | `01-Firma Home/`, `02-Vorlagen/`, `05-Projekte/`, `.claude/skills/` | Operator + Geschäftsführung | alle Mitarbeiter |
| **Team** (Mini-Firma) | `07-Teams/<team>/` (kontext, vorlagen, projekte, referenzen, ablage, skills) | Team-Mitglieder | Rest liest meist mit |
| **Externe Unternehmen** | `03-Unternehmen/<firma>/` | Teams die den Kontakt pflegen | je nach Sensitivität |
| **Externe Personen** | `04-Personen/<name>/` | Teams die den Kontakt pflegen | alle Mitarbeiter intern |
| **Mitarbeiter-Roster** | `06-Mitarbeiter/team-mitglieder.md` | Operator | alle |
| **Meetings** | `08-Meetings/internal/` und `external/` | Teilnehmer | je nach Vertraulichkeit |

Das spart die Setup-Friktion von mehreren physisch getrennten Folder-Wurzeln. Permissions sind das was sie sein sollten: eine Eigenschaft des Ordners, nicht der Wurzel.

## CRM-Light durch Wikilinks

Ohne separates CRM-Tool entsteht das Kunden-/Kontakt-Wissen über Jahre durch konsequente Wikilink-Verknüpfung:

- Meeting-Note `2026-05-11-acme-jahresgespraech.md` enthält `[[03-Unternehmen/acme-gmbh]]` und `[[04-Personen/hans-mueller]]`
- In `03-Unternehmen/acme-gmbh/kontext.md` erscheint eine "Verknüpfte Meetings"-Sektion automatisch via Backlinks
- In `04-Personen/hans-mueller/kontext.md` analog: alle Meetings + Verlauf bei welchen Firmen er war

Das ist Obsidian-Style Knowledge-Vernetzung — funktioniert in Cowork, Code, Obsidian, Cursor.

---

## Die 4 C's

Agentic OS folgt den **4 C's eines AI Operating Systems**:

| Schicht | Was es bedeutet | Wo es im Repo lebt |
|---|---|---|
| **Context** | Die AI weiß, wer Sie sind, was Sie verkaufen, wie Sie sprechen | `01-Firma Home/`, `AGENTS.md` |
| **Connections** | Die AI kann auf Ihre Tools zugreifen (Calendar, CRM, Mail) | Org-Skills via Claude Team Plan |
| **Capabilities** | Die AI weiß, wie Sie Dinge tun (SOPs, Workflows) | `Team-Wissen/SOPs/`, `.claude/skills/` |
| **Cadence** | Die AI macht Dinge automatisch (Morgenbrief, Wochenreview) | Workflows + Scheduled Triggers |

Mit dem `/audit` Skill können Sie jederzeit prüfen, wo Sie stehen.

---

## Wie Sie mit der KI arbeiten

Sie sprechen direkt mit der KI. Sie liest beim Session-Start `AGENTS.md`, kennt die Folder-Struktur, die Regeln, und die fünf firmenweiten Skills (`audit`, `onboard`, `level-up`, `neuer-kunde`, `session-abschluss`).

**Was die KI kann (Default):**

- Posteingang-Items klassifizieren und routen
- Meeting-Protokolle, LinkedIn-Posts, Angebote in Ihrer Markenstimme entwerfen
- Kunden-Briefings aus Stammdaten + Gesprächs-Protokollen zusammenstellen
- Session-Logs schreiben am Ende jedes Arbeitstags
- Audit Ihres Setups (was fehlt im Wissen, in den Tools, in den Workflows)

**Wenn etwas fehlt:** sagen Sie was Sie brauchen. Die KI schlägt einen passenden Workflow oder einen neuen Skill vor — den Sie als Markdown-File in `.claude/skills/` ablegen können.

---

## Lizenz & Beitragen

MIT-Lizenz — frei nutzbar, auch kommerziell. Forks willkommen. Pull Requests werden geprüft.

Wenn Sie Hilfe bei der Einrichtung brauchen oder Custom Skills für Ihr Unternehmen wollen: [umsatzai.com](https://umsatzai.com) bietet Setup, Training und laufende Pflege als Service.

---

**Built with care by Gerald Eder · [UmsatzAI](https://umsatzai.com) · 2026**
