<!--
Agentic OS v0.1 — © 2026 Gerald Eder · UmsatzAI
Licensed under MIT License — see LICENSE
-->

# Agentic OS

**Das AI Operating System für Teams.**

Eine sofort einsatzbereite Ordnerstruktur für KMU (2–15 Mitarbeiter), die mit Claude (Cowork Desktop oder Claude Code), Codex, Gemini oder Cursor zusammenarbeitet. Markdown-only. Tool-agnostisch. Keine Datenbank. Funktioniert in jedem Texteditor — und in jedem AI-Tool.

> Gebaut von [Gerald Eder](https://geraldeder.com) bei [UmsatzAI](https://umsatzai.com) — AI-Beratung für Mittelstand und Solopreneure im DACH-Raum.

---

## Was das ist

Stellen Sie sich vor, Ihr Unternehmen hätte einen Assistenten, der:

- die Markenstimme kennt
- jeden Kunden im Detail versteht
- alle SOPs befolgen kann
- Meeting-Protokolle schreibt
- den Posteingang sortiert
- nie etwas vergisst

Genau das ist Agentic OS. Ein gemeinsamer Wissensordner + ein Team aus AI-Spezialisten + klare Regeln, wie Mensch und KI zusammenarbeiten.

## Was Sie bekommen

| Element | Beschreibung |
|---|---|
| **9 Hauptordner** | Posteingang, Wissen, Vorlagen, Kunden, Projekte, Team, Meetings, Archiv |
| **AI-Team mit 4 Spezialisten** | Larry (Orchestrator), Penn (Schreiber), Pax (Recherche), Nolan (Personal) |
| **Vorlagen-Bibliothek** | Markenstimme, Kunden-Profil, Angebot, Meeting-Protokoll, LinkedIn-Post |
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

Die AI liest `AGENTS.md` und wird zu **Larry**, dem Team-Orchestrator. Larry stellt sich vor, fragt nach Ihrer Firma und füllt die Vorlagen aus.

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
│   ~/Dropbox/AcmeCo/  (oder GDrive, OneDrive)        │
│   ├── 01-Wissen/         ← was Claude wissen muss   │
│   ├── 02-Vorlagen/       ← Templates                │
│   ├── 03-Kunden/         ← pro Kunde ein Ordner     │
│   ├── Team/              ← AI-Spezialisten          │
│   ├── Team-Wissen/SOPs/  ← Standardabläufe          │
│   └── ...                                            │
└─────────────────────────────────────────────────────┘
```

**Der Trick:** Skills werden über Anthropic verteilt (Schicht 1). Daten werden über Dropbox/GDrive synchronisiert (Schicht 2). Die zwei Schichten sind getrennt — das macht das System einfach und robust.

---

## Die 4 C's

Agentic OS folgt den **4 C's eines AI Operating Systems**:

| Schicht | Was es bedeutet | Wo es im Repo lebt |
|---|---|---|
| **Context** | Die AI weiß, wer Sie sind, was Sie verkaufen, wie Sie sprechen | `01-Wissen/`, `AGENTS.md` |
| **Connections** | Die AI kann auf Ihre Tools zugreifen (Calendar, CRM, Mail) | Org-Skills via Claude Team Plan |
| **Capabilities** | Die AI weiß, wie Sie Dinge tun (SOPs, Workflows) | `Team-Wissen/SOPs/`, `.claude/skills/` |
| **Cadence** | Die AI macht Dinge automatisch (Morgenbrief, Wochenreview) | Workflows + Scheduled Triggers |

Mit dem `/audit` Skill können Sie jederzeit prüfen, wo Sie stehen.

---

## Die 4 Spezialisten

Sie sprechen immer mit **Larry**. Larry delegiert intern:

- **Larry** — Orchestrator. Nimmt jede Anfrage entgegen und routet sie. Schreibt Session-Logs am Ende.
- **Penn** — Schreiber. Journal-Einträge, Notizen, kurze Dokumentation.
- **Pax** — Researcher. Tiefe Recherche mit Quellenangaben.
- **Nolan** — Personal. Hireshhttps neue Spezialisten wenn Sie was Neues brauchen (z.B. einen Frontend-Developer für ein Projekt).

**Die wichtigste Regel:** Wenn Sie etwas brauchen wofür kein Spezialist da ist, sagt Larry **nicht** "kann ich nicht". Larry briefed Nolan, der den passenden neuen Spezialisten "anstellt". Das Team wächst mit Ihnen.

---

## Lizenz & Beitragen

MIT-Lizenz — frei nutzbar, auch kommerziell. Forks willkommen. Pull Requests werden geprüft.

Wenn Sie Hilfe bei der Einrichtung brauchen oder Custom Skills für Ihr Unternehmen wollen: [umsatzai.com](https://umsatzai.com) bietet Setup, Training und laufende Pflege als Service.

---

**Built with care by Gerald Eder · [UmsatzAI](https://umsatzai.com) · 2026**
