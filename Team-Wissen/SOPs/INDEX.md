# SOPs — Standardablaeufe

> Atomare Verfahren. Ein Job pro Datei. Filename: `SOP-NNN-<titel>.md`.

SOPs sind Rezepte fuer wiederkehrende Aufgaben. Sie sind LLM-agnostisch und re-usable — jede KI in jedem Tool kann sie lesen und ausfuehren. Eine SOP hat keinen "Owner", sie hat einen **Ausloeser**.

## Aktive SOPs

| Nummer | Titel | Wofuer |
| --- | --- | --- |
| [[SOP-001-neuen-mitarbeiter-onboarden]] | Neuer Mitarbeiter | Jemand startet neu im Team |
| [[SOP-002-neuen-kunden-anlegen]] | Neuer Kunde | Vertrag/LOI/erste Beauftragung |
| [[SOP-003-meeting-vorbereiten]] | Meeting fuehren | Vor + nach jedem wichtigen Meeting |
| [[SOP-004-inbox-verarbeiten]] | Inbox auf 0 | Wiederkehrend, z.B. Freitag-Nachmittag |
| [[SOP-005-angebot-erstellen]] | Angebot schreiben | Interessent oder Bestandskunde fragt an |

## SOP anlegen

Sag zur KI:

> "Erstelle eine SOP fuer [Aufgabe]"

Die KI fragt nach Ausloeser, Schritten und Output, dann legt sie eine neue SOP nach Schema an.

## Format pro SOP

Jede SOP folgt diesem Schema:

```markdown
# SOP-NNN — Titel

**Wofuer:** [Ein Satz: Wann fuehren wir diese SOP aus?]
**Ausloeser:** [Trigger-Phrase aus dem User]
**Verantwortlich:** [Rolle, oder "Die KI fuehrt, User signt off"]
**Dauer:** [Wie lange dauert das?]

## Schritte
1. [Schritt 1]
2. [Schritt 2]
...

## Output
[Welche Dateien wurden angelegt oder aktualisiert?]

## Referenzen
- [[Vorlage X]]
- [[Richtlinie Y]]
```

## Heuristik fuer neue SOPs

Frag dich vor dem Anlegen:

1. **Wiederkehrend?** 3+ mal pro Monat?
2. **Mehrere Schritte?** Wenn es 1 Schritt ist, ist es eine Notiz, keine SOP.
3. **Mehrere Personen?** Wenn nur eine Person es kann, ist es persoenliches Tacit-Wissen, keine SOP.

Zwei mal Ja: SOP anlegen. Sonst: ablegen im persoenlichen Workflow oder als Notiz in der Team-`kontext.md`.
