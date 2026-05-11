# 01-Firma

**Was Die KI über euer Geschäft wissen müssen.**

Dies ist die **Single Source of Truth** für alles, was euer Unternehmen ausmacht. Die KI liest diese Dateien automatisch und nutzt sie als Kontext für jede Antwort.

## Pflicht-Dateien

| Datei | Inhalt |
|---|---|
| [[brand]] | Wie euer Unternehmen schreibt und spricht. Beispiel-Texte, Tabu-Wörter, Tonalität |
| [[wunschkunde-icp]] | Ideal Customer Profile (ICP). Wer kauft bei euch, warum, mit welchen Schmerzpunkten |
| [[organization]] | Was ihr verkauft, zu welchen Preisen, mit welchen USPs |

## Optionale Dateien

Je nach Geschäftsmodell könnt ihr ergänzen:

- `unsere-werte.md` — Firmenwerte und Mission
- `unsere-prozesse.md` — Wie Aufträge bei euch durchlaufen
- `unsere-konkurrenz.md` — Wer sind eure Mitbewerber
- `tools.md` — Welche Software/Tools ihr nutzt
- `unsere-marken.md` — Wenn ihr mehrere Marken/Produktlinien habt

## Regel

**SSOT (Single Source of Truth):** Jeder Fakt lebt in genau einer Datei. Wenn ihr "wir haben 3 Kundengruppen" in einer Datei schreibt, dann nicht woanders nochmal — sondern dort verlinken via `[[wunschkunde-icp]]`.

Die KI erzwingt diese Regel am Session-Ende.

## Wie befüllen

Beim ersten Setup nutzt der `/onboard` Skill (Claude Code) oder sag zur KI: "Lass uns Agentic OS einrichten." Der 7-Fragen-Wizard füllt diese Dateien automatisch aus euren Antworten.

Später ergänzt ihr direkt — Die KI erkennt Änderungen und passt seine Antworten an.
