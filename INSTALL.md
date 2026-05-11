<!--
AI OS v0.5.0 — © 2026 Gerald Eder
Licensed under MIT — see LICENSE
-->

# Installation

In 5 Minuten startklar.

## Schritt 1 — Repo herunterladen

```bash
git clone https://github.com/edgeglobal/agentic-os.git mein-ai-os
cd mein-ai-os
```

Oder als ZIP: gehe auf `https://github.com/edgeglobal/agentic-os`, klicke **Code** → **Download ZIP**, entpacke und benenne den Folder um.

Wenn du keinen eigenen git-Workflow brauchst:

```bash
rm -rf .git
```

## Schritt 2 — Folder dorthin legen wo er gebraucht wird

Drei typische Optionen:

- **Lokal** auf deinem Rechner (nur du arbeitest damit)
- **Im Cloud-Storage** (du teilst mit dem Team — Permissions per Sub-Folder)
- **In einem Git-Repo** (fuer technische Teams)

AI OS funktioniert in allen drei Varianten. Die Folder-Struktur ist die gleiche.

## Schritt 3 — In deinem AI-Tool oeffnen

Oeffne den Folder in einem Tool das `AGENTS.md` versteht — Claude Code, Codex CLI, Cursor, Gemini CLI, oder ein anderes.

Sag zur KI:

> **Initialisiere dich in diesem Ordner.**

Die KI liest `AGENTS.md` und stellt sich kurz vor.

## Schritt 4 — Onboarding-Wizard starten

Sag zur KI:

> **Nutze den Onboarding-Skill im Modus Firma.**

Du bekommst ein Interview in 7 Sektionen:

1. **Eure Firma** — was ihr macht, Branche, Mitbewerber
2. **Eure Kunden** — wer kauft bei euch, welche Probleme loest ihr
3. **Eure Positionierung** — wie ihr euch unterscheidet
4. **Eure Markenstimme** — Tonalitaet, Beispiel-Texte (Originale einfuegen!)
5. **Eure Strategie** — Quartals-Prioritaeten, 12-Monate-Ziel, Metriken
6. **Operations & Tools** — welche Software ihr nutzt
7. **Stakeholder** — interne + externe Schluesselpersonen

Aus den Antworten fuellt die KI alle Files in `01-Firma Home/` automatisch. Plus den Mitarbeiter-Roster in `04-Mitarbeiter/`.

Dauer: 20-30 Minuten.

## Schritt 5 — Neue Mitarbeiter, Teams, Kunden, Kontakte

Der gleiche `/onboard` Skill hat drei weitere Modi:

- **Team** — neuen Team-Folder anlegen mit Kontext-Interview
- **Unternehmen** — neuer Kunden- oder Lieferanten-Folder
- **Person** — neuer externer Ansprechpartner

Sag einfach:

> **Wir haben einen neuen Kunden: Acme GmbH**
> **Wir haben einen neuen Mitarbeiter: Max Mustermann**
> **Leg ein neues Team an: Produktion**

Die KI erkennt was du willst und startet den richtigen Modus.

## Schritt 6 — Taegliche Nutzung

Beispiele was du mit der KI machen kannst:

| Aufgabe | Sag zur KI |
|---|---|
| Meeting-Protokoll schreiben | "Ich hatte gerade ein Meeting mit Acme. Hier die Stichpunkte: ..." |
| Angebot vorbereiten | "Erstelle ein Angebot fuer Acme basierend auf unserem Standardangebot" |
| LinkedIn-Post entwerfen | "Schreib einen LinkedIn-Post zum Thema X in unserem Stil" |
| Inbox verarbeiten | "Verarbeite die Inbox" |
| Audit | "Lauf /audit und zeig mir wo wir stehen" |
| Tag abschliessen | "Schliess die Session ab" |

Die KI nutzt jeden Kontext aus deinen Files — Markenstimme, Wunschkunden, Kunden-Historie, laufende Projekte.

## Schritt 7 — Updates

Wenn du eine neue Version von AI OS holen willst:

```bash
git pull
```

Oder neue ZIP herunterladen. Deine Inhalte in `01-Firma Home/`, `02-Teams/`, `03-CRM/`, `04-Mitarbeiter/` bleiben — nur die Struktur-Files (`AGENTS.md`, `README.md`, Skills) werden aktualisiert.

## Hilfe

- **Alle Konzepte:** lies `AGENTS.md` und die `README.md` in jedem Folder
- **SOPs fuer wiederkehrende Workflows:** `Team-Wissen/SOPs/`
- **Naming-Regeln:** `Team-Wissen/Richtlinien/R-001-namenskonventionen.md`
- **Issues:** [GitHub Issues](https://github.com/edgeglobal/agentic-os/issues)
