# 06-Meetings

**Meeting-Notizen.**

Für Meetings die NICHT direkt einem Kunden oder Projekt zuzuordnen sind. Kunden-Meetings gehören in `03-Kunden/<kunde>/meetings/`. Projekt-Meetings in `04-Projekte/<projekt>/`.

Was hier rein kommt:
- Strategie-Meetings (Quartals-Planung, Jahres-Review)
- Team-Meetings (Standup, All-Hands)
- 1:1s mit externen Beratern/Mentoren
- Spontane Sessions ohne klaren Bezug

## Struktur

```
06-Meetings/
├── 2026/
│   ├── 05/
│   │   ├── 2026-05-09-quartal-planung.md
│   │   └── 2026-05-15-team-standup.md
│   └── 06/
│       └── ...
```

Datum-basierte Ordner. Filename-Format: `YYYY-MM-DD-<thema-kebab-case>.md`

## Vorlage nutzen

Alle Meeting-Notizen folgen [[meeting-protokoll]] (in `02-Vorlagen/`). Sag zur KI:

> "Schreib ein Meeting-Protokoll: [Stichpunkte]"

Die KI nutzt automatisch die Vorlage und legt es im richtigen Datums-Ordner ab.

## Granola/Fireflies-Sync

Wenn ihr ein Meeting-Tool mit Auto-Transcription nutzt:
- Granola/Fireflies-Transkripte können hier rein
- Die KI kann Meeting-Aufnahmen verarbeiten und ein sauberes Protokoll daraus erstellen
- Dafür sagt: "Hier ist das Granola-Transkript von heute, mach mir ein sauberes Protokoll"
