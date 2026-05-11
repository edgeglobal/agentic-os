# 08-Meetings/external/

Meetings mit externen Teilnehmern: Kunden, Lieferanten, Partner, Beirat, Investoren, Berater.

## Naming

`YYYY/MM/YYYY-MM-DD-<unternehmen>-<thema>.md`

Unternehmen-Slug im Namen, damit man auf einen Blick sieht mit wem:

- `2026/05/2026-05-11-acme-jahresgespraech.md`
- `2026/05/2026-05-14-dhl-tarifverhandlung.md`
- `2026/05/2026-05-20-beirat-quartal-q2.md`

## Verknuepfung (Pflicht)

Jedes External-Meeting hat Wikilinks zu:

- **Firma** → `[[03-Unternehmen/<firma>]]`
- **Personen** → `[[04-Personen/<name1>]]`, `[[04-Personen/<name2>]]`
- **Bezug auf Projekte** (falls relevant) → `[[05-Projekte/<projekt>]]`

Diese Wikilinks erzeugen Backlinks in den Firmen- und Personen-Files — so baut sich das Wissens-Geflecht ueber die Jahre auf.

## Struktur eines External-Meeting-Files

```markdown
# [Thema] mit [[03-Unternehmen/acme-gmbh]] — YYYY-MM-DD

**Teilnehmer extern:** [[04-Personen/hans-mueller]], [[04-Personen/elena-koenig]]
**Teilnehmer intern:** [Namen aus Roster]
**Hauptbetreuendes Team:** [[07-Teams/marketing-vertrieb]]
**Bezug:** [[05-Projekte/webrelaunch-acme]]

## Transkript

[Original-Transkript oder Verweis auf Audio-Datei]

## Wichtige Aussagen

- Hans: "..."
- Elena: "..."

## Entscheidungen

- [Was entschieden, von wem]

## Action Items

- [ ] [Was, wer, bis wann]

## Was Larry / die KI fuers naechste Mal merken soll

- [Tonalitaets-Hinweis, Praeferenz, Eigenheit]
```

## DSGVO

- Transkripte enthalten oft personenbezogene Daten — Lawful Basis pruefen
- Audio-Files getrennt vom Markdown-Protokoll lagern, separate Loesch-Routine
- Bei Loesch-Anfragen einer Person: das Protokoll bereinigen oder pseudonymisieren
