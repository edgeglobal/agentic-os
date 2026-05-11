# SOP-003 — Meeting vorbereiten

**Wofür:** Vor jedem wichtigen Meeting (Kunden-Meeting, Strategie-Session, Sales-Pitch).
**Auslöser:** User sagt "Ich habe morgen Meeting mit [...]" oder "Bereite mich auf das Meeting [...] vor"
**Verantwortlich:** Die KI
**Dauer:** ~5-10 Minuten

---

## Schritte

### 1. Meeting-Kontext klären

Die KI fragt:
- Mit wem? (Verweis auf [[03-CRM/Unternehmen/...]] oder neue Person)
- Worum geht's? (Verkauf? Review? Kick-off? Krisen-Gespräch?)
- Welche Vorgeschichte? (frühere Meetings, frühere E-Mails)
- Was ist das gewünschte Ergebnis?

### 2. Bestehenden Kontext laden

Die KI liest:
- Wenn Kunde existiert: `03-CRM/Unternehmen/<kunde>/_hub.md` + alle bisherigen Meeting-Notizen
- Wenn neue Person: existiert sie in `05-Team/` oder `03-CRM/Unternehmen/`?
- E-Mail-Verlauf (wenn User reinpaste)

Zusammenfassung: "Aus dem Vault: [Kunde] ist [X], letzter Kontakt [Datum] mit [Inhalt]. Aktuelle Phase: [Y]."

### 3. Recherche bei Bedarf

Wenn das Meeting mit jemand Neuem ist oder strategisch wichtig:

Die KI recherchiert: "Recherchier kurz zu [Person/Firma] — was sollten wir wissen?"

Die Recherche liefert ein 5-Minuten-Briefing:
- Aktuelle Situation des Gegenübers
- Letzter LinkedIn-Post / News
- Branchen-Kontext
- Gemeinsame Verbindungen

### 4. Ziel und Strategie

Die KI hilft strukturieren:
- **Bestes Ergebnis:** Was wäre das beste Outcome?
- **Worst Case:** Was vermeiden wir?
- **Position:** Wo stehen wir, wo der Gegenüber?
- **Argumente:** Was sind unsere stärksten 2-3 Argumente?
- **Einwände:** Welche Einwände erwarten wir, wie reagieren wir?

### 5. Agenda entwerfen

Es wird geschrieben einen Agenda-Vorschlag basierend auf User-Antworten:

```markdown
# Meeting — [Thema] — [Datum]

## Ziel
[1 Satz]

## Agenda
1. [5 Min] Begrüßung, Smalltalk
2. [10 Min] Status-Update
3. [15 Min] [Hauptthema]
4. [10 Min] [Zweites Thema]
5. [5 Min] Next Steps

## Vorbereitung mitbringen
- [Material 1]
- [Material 2]

## Cheat-Sheet
- Schlüsselzahlen: [...]
- Schlüsselargumente: [...]
- Frage-Liste: [...]
```

### 6. Cheat-Sheet ausgeben

Die KI gibt User ein 1-Page-Briefing mit:
- Wer kommt
- Wichtigste 3 Fakten zur Person/Firma
- Unsere Strategie (1 Satz)
- Top-3-Argumente
- Top-3-Risiken/Einwände + Reaktionen
- Erwünschte Outputs (Decision, Next Steps, etc.)

### 7. Nach dem Meeting

User sagt: "Meeting fertig — hier meine Notizen: [...]"

Die KI führt sich an, ein sauberes Protokoll nach [[03-CRM/Meetings/_protokoll-vorlage]] zu schreiben und im richtigen Ordner abzulegen (Kunde / Projekt / 06-Meetings).

---

## Output

Vor dem Meeting:
- `03-CRM/Unternehmen/<kunde>/meetings/YYYY-MM-DD-<thema>-vorbereitung.md` (oder `06-Meetings/...` wenn nicht kunden-bezogen)

Nach dem Meeting:
- Selbe Datei umbenannt (Vorbereitung + Protokoll im selben File ist ok), oder zusätzlich `YYYY-MM-DD-<thema>-protokoll.md`

## Referenzen

- [[03-CRM/Meetings/_protokoll-vorlage]] (Vorlage)
- [[markenstimme]]
