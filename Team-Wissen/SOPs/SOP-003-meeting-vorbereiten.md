# SOP-003 — Meeting vorbereiten und protokollieren

**Wofuer:** Vor (und nach) jedem wichtigen Meeting — Kunden-Meeting, Sales-Pitch, Strategie-Session, Lieferanten-Termin.
**Ausloeser:** "Ich habe morgen Meeting mit [...]", "Bereite mich auf das Meeting vor", "Hier sind meine Meeting-Notizen".
**Verantwortlich:** Die KI fuehrt, der User entscheidet inhaltlich.
**Dauer:** 5-10 Minuten Vorbereitung, 5 Minuten Nachbereitung.

---

## Phase A: Vor dem Meeting

### 1. Kontext klaeren

Die KI fragt:

- **Mit wem?** (Wikilink zu `03-CRM/Unternehmen/<firma>/` oder neue Person)
- **Worum geht's?** (Sales-Pitch, Status-Review, Kickoff, Eskalation)
- **Vorgeschichte?** (frueheres Meeting, Mail-Verlauf — User paste-t bei Bedarf)
- **Was ist das gewuenschte Ergebnis?**

### 2. Bestehenden Kontext laden

Die KI liest:

- Wenn Kunde existiert: `03-CRM/Unternehmen/<firma>/kontext.md` + frueheste Eintraege aus `03-CRM/Meetings/` mit diesem Kunden
- Wenn Person bekannt: `03-CRM/Personen/<name>/kontext.md` (Verlauf, Vorlieben)
- Wenn nur intern (Team-Meeting): `02-Teams/<team>/kontext.md` und letzte Eintraege aus `02-Teams/<team>/meetings/`

Zusammenfassung in 3 Saetzen: "Aus dem Vault: [Firma] ist [X], letzter Kontakt [Datum] mit [Inhalt]. Aktuelle Phase: [Y]."

### 3. Recherche bei Bedarf

Bei neuen Personen oder strategisch wichtigen Meetings: kurzes 5-Minuten-Briefing zu Person + Firma (LinkedIn, News, Branchenkontext, gemeinsame Verbindungen).

### 4. Strategie strukturieren

- **Bestes Ergebnis:** Was waere das Ideal-Outcome?
- **Worst Case:** Was vermeiden wir?
- **Position:** Wo stehen wir, wo der Gegenueber?
- **Argumente:** Was sind unsere staerksten 2-3 Argumente?
- **Einwaende:** Welche Einwaende erwarten wir, wie reagieren wir?

### 5. Agenda + Cheat-Sheet

Die KI entwirft Agenda und 1-Page-Cheat-Sheet:

```markdown
# Meeting — [Thema] — [Datum]

## Ziel (1 Satz)

## Agenda
1. [5 Min] Begruessung, Smalltalk
2. [10 Min] Status-Update
3. [15 Min] [Hauptthema]
4. [10 Min] [Zweites Thema]
5. [5 Min] Next Steps

## Cheat-Sheet
- Wer kommt + 3 Fakten zur Person/Firma
- Unsere Strategie (1 Satz)
- Top-3-Argumente
- Top-3-Einwaende + Reaktionen
- Gewuenschte Outcomes (Decision, Next Steps)
```

**Externes Meeting:** Datei nach `03-CRM/Meetings/YYYY-MM-DD-<thema>-vorbereitung.md`.
**Internes Meeting:** Datei nach `02-Teams/<team>/meetings/YYYY-MM-DD-<thema>-vorbereitung.md`.

---

## Phase B: Nach dem Meeting

### 6. Notizen einsammeln

User sagt: "Meeting fertig — hier meine Notizen: [...]"

Die KI extrahiert:

- **Was wurde besprochen** (3-7 Bullets)
- **Entscheidungen** mit Begruendung
- **Action Items** mit Owner und Deadline
- **Offene Punkte** fuer's naechste Meeting
- **Neue Wikilinks** (neue Personen, Firmen, Themen die genannt wurden)

### 7. Protokoll schreiben

Nutze [[03-CRM/Meetings/_protokoll-vorlage]] (extern) oder team-eigene Vorlage (intern).

Speicherort:

- **Extern:** `03-CRM/Meetings/YYYY-MM-DD-<thema>.md` — oder selbe Datei wie Vorbereitung, einfach ergaenzt
- **Intern:** `02-Teams/<team>/meetings/YYYY-MM-DD-<thema>.md`

### 8. Backlinks setzen

Die KI ergaenzt automatisch:

- In `03-CRM/Unternehmen/<firma>/kontext.md` Sektion "Letzte Meetings": Eintrag
- In `03-CRM/Personen/<name>/kontext.md` Sektion "Verlauf": Eintrag
- Action Items fuer einzelne MA: Wikilink zu `04-Mitarbeiter/team-mitglieder.md` setzen, Aufgabe im Chat nennen

### 9. Confirmation

```
[OK] Protokoll: <pfad>
[OK] Backlinks gesetzt: <liste>
[ ] Action Items (Owner zugewiesen): <liste mit Deadlines>
```

---

## Output

Mindestens:

- 1 Meeting-Datei (intern oder extern)
- Backlinks in Kunden- und/oder Personen-Files
- Action-Items-Liste im Chat

## Referenzen

- [[03-CRM/Meetings/_protokoll-vorlage]]
- [[brand]]
- [[organization]]
- [[R-001-namenskonventionen]]
