<!--
AI OS — Agentic Operating System für KMUs
© 2026 Gerald Eder · UmsatzAI · MIT License
-->

# 06-Mitarbeiter/

Roster aller Menschen in der Firma. Eine zentrale Liste, kein Sub-Folder pro Person.

> Dieser Ordner ist fuer die **Menschen** in der Firma — also Wer-arbeitet-hier. Nicht zu verwechseln mit `02-Teams/`, das die **Funktionen** abbildet (Marketing, Vertrieb, etc.).

## Aufbau

```
06-Mitarbeiter/
├── README.md                ← diese Datei
└── team-mitglieder.md       ← Liste aller Mitarbeiter mit Rolle, Team, Praeferenzen
```

**Bewusst nur ein File.** Frueher gab es hier Sub-Folder pro Person mit eigenem `ueber-mich.md`, `meine-stimme.md`, `memory.md`. Das hat sich als Overkill herausgestellt — fuer KMU mit 5-15 Mitarbeitern bringt das mehr Pflegeaufwand als Wert.

## Was hier liegt

**`team-mitglieder.md`** ist der Roster:

- Wer arbeitet hier
- Welche Rolle
- Welches Team
- Optional: persoenliche Praeferenzen fuer Claude (Tonfall, Anrede, Format)

Die KI liest den Roster bei jeder Session-Eroeffnung. Wenn ein Mitarbeiter sagt "Hallo, ich bin Max", weiss die KI wer Max ist und welches Team er hat.

## Brand-Voice gehoert der Firma, nicht dem Mitarbeiter

Die einheitliche Marken-Stimme der Firma liegt in [[01-Firma Home/markenstimme]]. Jeder Mitarbeiter nutzt diese Stimme fuer Firmen-Kommunikation (Angebote, Kunden-Mails, Newsletter).

Wenn ein einzelner Mitarbeiter im persoenlichen Bereich abweichen will (z.B. eigenes LinkedIn-Profil), kann er das in der Praeferenz-Spalte des Rosters vermerken. Aber: das ist die Ausnahme, nicht die Regel.

## Wenn ein neuer Mitarbeiter onboardet

Sage zur KI:

> "Wir haben einen neuen Mitarbeiter: Max Mustermann als Marketing Manager im Marketing-Vertriebs-Team."

Die KI laeuft [[SOP-001-neuen-mitarbeiter-onboarden]]:

1. Ergaenzt Eintrag in `team-mitglieder.md`
2. Ergaenzt Eintrag in `02-Teams/marketing-vertrieb/kontext.md` bei "Mitglieder"
3. Fragt nach optionalen Praeferenzen ("Wie soll Claude mit dir reden?")
4. Setzt einen Session-Log-Eintrag

Kein neuer Folder noetig.

## Wer schreibt

| Was | Schreib-Recht |
|---|---|
| `team-mitglieder.md` | Operator / Geschaeftsfuehrung (bei Mitarbeiter-Wechsel) |
| Praeferenz-Spalte pro Person | Mitarbeiter selbst, ueber die KI |

## Privacy

Persoenliche Daten (Gehalt, Krankschreibungen, Personalgespraechs-Notizen) **nicht** hier ablegen — gehoeren ins HR-System oder einen separat geschuetzten Folder mit eingeschraenktem Zugriff.

## Wenn jemand geht

> "Max Mustermann verlaesst das Team zum [Datum]"

Die KI:

1. Entfernt Max-Eintrag aus `team-mitglieder.md` und aus `02-Teams/<team>/kontext.md`
2. Sucht in `03-Unternehmen/` und `05-Projekte/` nach Verweisen auf Max und markiert sie als "Nachfolger benoetigt"
3. Schreibt Session-Log mit Datum
