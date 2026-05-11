<!--
AI OS — Agentic Operating System für KMUs
© 2026 Gerald Eder · MIT License
-->

# 03-CRM/Meetings/

**Externe Meetings** mit Unternehmen + Personen. Interne Meetings (Standups, Team-Reviews, Retrospektiven) liegen im jeweiligen Team-Folder unter `02-Teams/<team>/meetings/`.

## Was hier rein gehoert

- Kunden-Gespraeche, Jahresgespraeche, Quartals-Reviews
- Lieferanten-Verhandlungen
- Beirats-Sitzungen
- Investoren-Calls
- 1:1 mit externen Beratern / Mentoren

## Naming

`YYYY/MM/YYYY-MM-DD-<unternehmen>-<thema>.md`

Unternehmen-Slug im Filename, damit man auf einen Blick sieht mit wem:

- `2026/05/2026-05-11-acme-jahresgespraech.md`
- `2026/05/2026-05-14-dhl-tarifverhandlung.md`
- `2026/05/2026-05-20-beirat-meyer-q2.md`

## Wikilinks (Pflicht)

Jedes Meeting-File hat Wikilinks zu:

- **Firma** → `[[03-CRM/Unternehmen/<firma>]]`
- **Personen** → `[[03-CRM/Personen/<name>]]`
- **Bezug auf Projekte** (falls relevant) → `[[01-Firma Home/projekte/<projekt>]]`
- **Verantwortliches Team** → z.B. `[[02-Teams/marketing-vertrieb]]`

Diese Wikilinks erzeugen Backlinks in den jeweiligen Files — so baut sich das Wissens-Geflecht ueber die Jahre auf.

## Vorlage nutzen

Alle Meeting-Notes folgen `_protokoll-vorlage.md`. Sage zur KI:

> "Schreib ein Meeting-Protokoll: [Stichpunkte oder Transkript einfuegen]"

Die KI nutzt die Vorlage, legt das File im richtigen Jahres/Monats-Pfad ab und setzt die Wikilinks.

## Granola / Fireflies / Otter Sync

Wenn ihr ein Meeting-Tool mit Auto-Transcription nutzt:

- Roh-Transkript in das Meeting-File einfuegen oder dorthin verlinken
- KI macht daraus ein sauberes Protokoll
- Sage: "Hier ist das Transkript von heute, mach mir ein sauberes Protokoll"

## DSGVO

- Transkripte enthalten oft personenbezogene Daten — Lawful Basis pruefen
- Audio-Files getrennt vom Markdown-Protokoll lagern, separate Loesch-Routine
- Roh-Transkripte nach 30-90 Tagen loeschen sobald Protokoll steht
- Bei Loesch-Anfrage einer Person: das Protokoll bereinigen oder pseudonymisieren
