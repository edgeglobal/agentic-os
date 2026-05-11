<!--
AI OS — Agentic Operating System für KMUs
© 2026 Gerald Eder · UmsatzAI · MIT License
-->

# 08-Meetings/

Zentrale Heimat fuer alle Meeting-Notes und -Transkripte. Aufgeteilt in **internal** (interne Meetings: Geschaeftsfuehrungsrunden, Team-Standups, Wochen-Reviews) und **external** (Meetings mit Kunden, Lieferanten, Partnern, Beirat, externen Beratern).

## Aufbau

```
08-Meetings/
├── README.md                                              ← diese Datei
├── internal/
│   ├── README.md
│   └── YYYY/MM/YYYY-MM-DD-<thema>.md
└── external/
    ├── README.md
    └── YYYY/MM/YYYY-MM-DD-<unternehmen>-<thema>.md
```

## Was wo hin

**`internal/`** — keine externen Teilnehmer:

- Geschaeftsfuehrungsrunde
- Team-Standups
- Strategie-Sitzung, Quartals-Planning
- 1:1 zwischen Mitarbeitern
- All-Hands

**`external/`** — mindestens ein externer Teilnehmer:

- Kunden-Meetings, Jahresgespraeche
- Lieferanten-Verhandlungen
- Beirats-Sitzungen
- Investoren-Calls
- 1:1 mit externen Beratern / Mentoren

## Naming

Datum-Prefix, kebab-case fuer den Slug:

- `internal/2026/05/2026-05-11-geschaeftsfuehrungsrunde.md`
- `external/2026/05/2026-05-11-acme-jahresgespraech.md`

Bei externen Meetings: **Unternehmen-Slug im Filename**, damit man auf einen Blick sieht mit wem.

## Wikilinks (Pflicht bei externen Meetings)

Jedes External-Meeting hat Wikilinks zu:

- Firma → `[[03-Unternehmen/<firma>]]`
- Personen → `[[04-Personen/<name>]]`
- Bezug auf Projekte → `[[05-Projekte/<projekt>]]`

Diese Wikilinks erzeugen Backlinks in den jeweiligen Files — so baut sich das Wissens-Geflecht ueber die Jahre auf.

## Vorlage nutzen

Alle Meeting-Notes folgen `02-Vorlagen/meeting-protokoll.md`. Sage zur KI:

> "Schreib ein Meeting-Protokoll: [Stichpunkte oder Granola-Transkript einfuegen]"

Die KI nutzt die Vorlage, legt das File im richtigen Sub-Folder + Jahres/Monats-Pfad ab und setzt die Wikilinks.

## Granola / Fireflies / Otter Sync

Wenn ihr ein Meeting-Tool mit Auto-Transcription nutzt:

- Roh-Transkript in das Meeting-File einfuegen oder dorthin verlinken
- KI macht daraus ein sauberes Protokoll
- Sage: "Hier ist das Granola-Transkript von heute, mach mir ein sauberes Protokoll"

## DSGVO

- Transkripte enthalten oft personenbezogene Daten — Lawful Basis pruefen
- Audio-Files getrennt vom Markdown-Protokoll lagern, separate Loesch-Routine
- Roh-Transkripte nach 30-90 Tagen loeschen sobald Protokoll steht
- Bei Loesch-Anfrage einer Person: das Protokoll bereinigen oder pseudonymisieren
