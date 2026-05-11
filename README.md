<!--
AI OS v0.5.0 — © 2026 Gerald Eder
Licensed under MIT License — see LICENSE
-->

# AI OS

**Agentic Operating System.** Eine Ordner-Struktur in Markdown, die deiner KI sofort den vollen Firmen-Kontext gibt.

Klone das Repo, öffne es in deinem AI-Tool, starte den `/onboard` Skill — und deine KI kennt deine Firma, dein Team, deine Kunden, deine Strategie.

---

## Was AI OS ist

Ein Folder mit klarer Struktur. Drinnen liegen Markdown-Files, die die KI bei jeder Session liest:

- **Wer ihr seid** als Firma (Brand, Wunschkunden, Leistungen, Strategie)
- **Wie ihr euch aufteilt** in Teams (Marketing, Fulfillment, etc.)
- **Wen ihr kennt** — externe Unternehmen, externe Personen
- **Was ihr besprochen habt** — Meeting-Notes mit Wikilinks zum Wissen

Die KI nutzt diesen Kontext, um in eurer Sprache zu schreiben, eure Kunden zu kennen, und Vorgaenge sauber zu pflegen.

---

## Was du bekommst

| Element | Beschreibung |
|---|---|
| **Klare Ordner-Struktur** | Inbox, Firma Home, Teams, CRM (Unternehmen + Personen + Meetings), Mitarbeiter, Archiv |
| **CRM-Light in Markdown** | Unternehmen + Personen + Meetings via Wikilinks vernetzt — kein externes CRM noetig |
| **Team-Folder als Mini-Firma** | Jedes Team hat eigene kontext, vorlagen, projekte, referenzen, meetings, ablage, skills |
| **Default-Teams** | Marketing & Vertrieb, Fulfillment, Finance/HR/Admin — anpassbar oder loeschbar |
| **Universelle Context-Files** | organization, brand, wunschkunde-icp, strategy, tools, stakeholder |
| **5 Skills** | audit, onboard, level-up, neuer-kunde, session-abschluss |
| **Tool-agnostisch** | `AGENTS.md` lesen Claude, Codex, Cursor, Gemini nativ |

---

## Fuer wen ist das

Fuer jedes Team das mit KI arbeiten will und Wert auf strukturiertes Wissen legt. Solo-Operatoren mit Assistenten, Teams in Beratungen, Agenturen, Handwerks-Betrieben, Coaches, Anwaelten, Steuerberatern, Aerzten.

Egal ob ihr im Cloud-Storage syncht oder lokal arbeitet — die Folder-Struktur funktioniert in beidem.

---

## Schnellstart

```bash
git clone https://github.com/edgeglobal/agentic-os.git mein-ai-os
cd mein-ai-os
```

Oeffne den Folder in deinem AI-Tool (Claude Code, Codex CLI, Cursor, Gemini CLI, oder ein anderes Tool das `AGENTS.md` versteht).

Sag zur KI:

> **Initialisiere dich in diesem Ordner.**

Die KI liest `AGENTS.md` und stellt sich vor. Dann:

> **Nutze den Onboarding-Skill im Modus Firma.**

Der Skill interviewt dich in 7 Sektionen und fuellt automatisch alle Context-Files in `01-Firma Home/`.

Fertig. Deine KI hat jetzt vollen Firmen-Kontext.

---

## Folder-Struktur

```
mein-ai-os/
├── 00-Inbox/                  rohe Inputs (Brain-Dumps, Forwarded Mails, Voice-Memos)
├── 01-Firma Home/             firmenweite Single-Source-of-Truth
│   ├── organization.md        was ihr macht, Branche, Operations
│   ├── brand.md               Voice, Tonalitaet, Beispiele
│   ├── wunschkunde-icp.md     Ideal Customer Profile
│   ├── strategy.md            Ziele, Prioritaeten, Metriken
│   ├── tools.md               Tech-Stack
│   ├── stakeholder.md         Schluesselpersonen intern + extern
│   └── projekte/              firmenweite oder Cross-Team-Projekte
├── 02-Teams/                  Mini-Firmen pro Funktion
│   ├── marketing-vertrieb/
│   ├── fulfillment/
│   ├── finance-hr-admin/
│   └── _neues-team/           Vorlage zum Duplizieren
├── 03-CRM/                    Customer Relationship Management
│   ├── Unternehmen/           externe Firmen (Kunden, Lieferanten, Partner)
│   ├── Personen/              externe Personen (Ansprechpartner, Beirat)
│   └── Meetings/              nur externe Meetings, mit Wikilinks zum CRM
├── 04-Mitarbeiter/            Roster aller Menschen
├── 99-Archiv/                 Erledigtes
├── Team-Wissen/               SOPs, Workflows, Richtlinien, Session-Logs
└── .claude/skills/            firmenweite Skills
```

---

## Wie das funktioniert

**Schichten in einer Folder-Hierarchie**, nicht in getrennten Wurzeln:

| Bereich | Wo | Wer schreibt |
|---|---|---|
| **Firma-weit** | `01-Firma Home/` | Operator + Geschaeftsfuehrung |
| **Team** (Mini-Firma) | `02-Teams/<team>/` | Team-Mitglieder |
| **Externe Unternehmen** | `03-CRM/Unternehmen/<firma>/` | Teams die den Kontakt pflegen |
| **Externe Personen** | `03-CRM/Personen/<name>/` | Teams die den Kontakt pflegen |
| **Mitarbeiter-Roster** | `04-Mitarbeiter/` | Operator |
| **Meetings** | `03-CRM/Meetings/` (extern) + `02-Teams/<team>/meetings/` (intern) | Teilnehmer |

Permissions kommen vom Folder, nicht von der Wurzel. Wenn ihr im Cloud-Storage arbeitet: pro Sub-Folder einstellen wer rein darf.

---

## CRM-Light durch Wikilinks

Externe Firmen und Personen leben als eigene Folder mit `kontext.md`. Meeting-Notes verlinken via Wikilinks zu Unternehmen + Personen:

```markdown
# Jahresgespraech mit [[03-CRM/Unternehmen/acme-gmbh]] — 2026-05-11

Teilnehmer extern: [[03-CRM/Personen/hans-mueller]]
Bezug: [[01-Firma Home/projekte/webrelaunch-acme]]

## Was besprochen wurde
- ...
```

Backlinks in den jeweiligen `kontext.md`-Files erscheinen automatisch. Ueber Jahre baut sich ein Wissens-Geflecht auf — ohne separates CRM-Tool.

---

## Die 5 Skills

- **`/audit`** — pruefen wo ihr steht (Score nach 4 C's: Context, Connections, Capabilities, Cadence)
- **`/onboard`** — 4 Modi: neue Firma einrichten, neues Team anlegen, neues Unternehmen anlegen, neue Person anlegen
- **`/level-up`** — woechentliches Verbesserungs-Ritual
- **`/neuer-kunde`** — schneller Workflow fuer neuen Kunden-Folder
- **`/session-abschluss`** — Session-Log am Tagesende schreiben

---

## Lizenz

MIT — frei nutzbar, auch kommerziell. Forks willkommen.
