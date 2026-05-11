---
name: onboard
description: Use on Day 1 of an AI OS install OR when adding a new Team, Unternehmen, or Person. Trigger phrases: "set me up", "onboard me", "let's get started", "lass uns einrichten", "richte dich ein", "fill in my AI OS", "neues Team anlegen", "neues Unternehmen anlegen", "neue Person anlegen", or has just cloned the kit. Has 4 modes (Firma / Team / Unternehmen / Person). Idempotent — re-run any time.
---

# Onboard-Skill

Interaktives Setup mit vier Modi. Beim Aufrufen ohne klaren Bezug: Modus erfragen.

## Modus-Auswahl

Bei Trigger ohne klaren Bezug, frage:

> **Welcher Modus?**
> 1. **Firma** — Erst-Setup. Befuellt `01-Firma Home/` mit Markenstimme, ICP, Leistungen, Strategie, Tools, Stakeholder.
> 2. **Team** — Neuer Team-Folder unter `02-Teams/<team-name>/`.
> 3. **Unternehmen** — Neuer externer Firmen-Folder unter `03-CRM/Unternehmen/<firma>/`.
> 4. **Person** — Neue externe Person unter `03-CRM/Personen/<name>/`.

Bei "lass uns einrichten" ohne Spezifikation → Default: Firma (Erst-Setup).

Bei "neues Team anlegen" / "neuer Kunde" / "neue Person" → klar abgeleitet.

---

## Modus 1: Firma (Erst-Setup)

**Vorbedingung:** wird vom Operator oder Geschaeftsfuehrung durchgefuehrt, nicht vom normalen Mitarbeiter.

### Phase 0: Lage-Check

Lies diese Files:
- `01-Firma Home/markenstimme.md`
- `01-Firma Home/unsere-kunden.md`
- `01-Firma Home/unsere-leistungen.md`
- `01-Firma Home/strategie.md`
- `01-Firma Home/unsere-tools.md`
- `01-Firma Home/stakeholder.md`
- `04-Mitarbeiter/team-mitglieder.md`

Pruefe was schon ausgefuellt ist vs. Platzhalter.

- **Alle gefuellt** → ueberspringe Interview, frage was geupdatet werden soll.
- **Teilweise gefuellt** → frage: "Ich sehe Sektionen A, C, E sind beantwortet. Den Rest jetzt fuellen oder mit dem was da ist scaffolden?"
- **Leer (frischer Klon)** → starte Phase 1.

### Phase 1: Optional Doks hochladen

Frage:

> Habt ihr existierende Dokumente die helfen koennten? Beispiele:
> - Brand-Brief / Marken-Guide
> - Pitch-Deck / Sales-Praesentation
> - ICP / Persona-Doku
> - Strategiepapier / Vision-Doc
> - Webseiten-Texte (About-us, Leistungen)
>
> Wenn ja: bitte einfuegen oder Pfad nennen. Wenn nein, geht's mit dem Interview weiter.

Wenn Doks geliefert werden: parsen und Inhalte in die spaeteren Sektionen einbauen. Bei Konflikten mit User-Antworten: Doks zitieren und nachfragen welche Version stimmt.

### Phase 2: 7 Sektionen Interview

Pro Sektion: kurz erklaeren wofuer es ist, dann Fragen einzeln stellen. Antworten in `00-Inbox/onboarding-intake.md` zwischenspeichern.

#### Sektion 1: Eure Firma (→ `unsere-leistungen.md` + Teil von `markenstimme.md`)

1. Was bietet eure Firma an? Erklaert es wie einem Freund der nichts von der Branche weiss.
2. In welcher Branche / Nische seid ihr?
3. Wer sind eure 3 wichtigsten Mitbewerber, und was unterscheidet euch?
4. Was ist in den letzten 3-5 Jahren in eurer Branche passiert, das wirklich zaehlt?
5. Was nervt in eurer Branche? Was ist kaputt?

#### Sektion 2: Eure Kunden (→ `unsere-kunden.md`)

1. Wer kauft bei euch? Beschreibt ihren idealen Kunden (Rolle, Firmengroesse, Branche, Situation).
2. Welche 1-3 Hauptprobleme loest ihr fuer sie?
3. Was ist das Ergebnis das ihr liefert? (Zahlen, Outcomes, Transformationen)
4. Warum kaufen Kunden bei euch und nicht beim Mitbewerber?
5. Wie lange braucht es typischerweise vom Erstkontakt bis zum Kauf?

#### Sektion 3: Eure Positionierung (→ ergaenzt `unsere-leistungen.md` + `unsere-kunden.md`)

1. Wer oder was ist euer "Feind"? (Die alte Art Dinge zu tun, eine Mitbewerber-Kategorie, ein Mindset)
2. Wie wollt ihr von Markt wahrgenommen werden?
3. Was ist eure Kern-Value-Proposition in einem Absatz?
4. Was sind 2-3 Kern-Botschaften die jede Kommunikation transportieren soll?

#### Sektion 4: Eure Markenstimme (→ `markenstimme.md`)

1. Wenn eure Firma eine Persoenlichkeit waere — 5 Adjektive.
2. Welche Tonalitaet nutzt ihr in externer Kommunikation? (Formell, locker, mutig, technisch, direkt, verspielt)
3. Gibt es Phrasen / Begriffe die ihr oft nutzt? (Signature-Saetze, Themen, verbale Marker)
4. Was wuerde eure Firma niemals sagen? Welche Themen meidet ihr publik?
5. **Bitte 2-3 echte Beispiel-Texte einfuegen** (LinkedIn-Post, Mail, Webseiten-Text). **Wichtig: Original einfuegen, nicht im Chat tippen.** Falls getippt: ablehnen und auf Paste bestehen.

#### Sektion 5: Strategie & Ziele (→ `strategie.md`)

1. Was sind eure 1-3 Top-Prioritaeten fuers naechste Quartal?
2. Wo wollt ihr in 12 Monaten sein?
3. Was messt ihr aktuell um zu wissen ob es laeuft? (Umsatz, Kunden, Conversion, etc.)
4. Was, wenn ihr es nailen wuerdet, wuerde alles aendern?
5. Was habt ihr probiert was nicht funktioniert hat? Was wurde gelernt?

#### Sektion 6: Operations & Tools (→ `unsere-tools.md`)

7-Bucket-Walkthrough. Pro Bucket: welches Tool nutzt ihr?

1. **Buchhaltung / Finanzen** (z.B. lexoffice, Datev, Sevdesk)
2. **Kunden-CRM** (z.B. HubSpot, Pipedrive, oder kein CRM)
3. **Kalender** (z.B. Google Calendar, Outlook)
4. **Mail / Kommunikation intern** (z.B. M365, Google Workspace, Slack, Teams)
5. **Projekt-Tracking** (z.B. Notion, Asana, ClickUp, Linear, Trello)
6. **Meeting-Aufzeichnungen** (z.B. Granola, Otter, Fireflies, Teams-Aufnahme)
7. **Wissen / Files** (z.B. Drive, OneDrive, Notion, Confluence)

Pro Tool: kurz "verbunden / nicht verbunden" notieren.

#### Sektion 7: Stakeholder (→ `stakeholder.md`)

1. Wer sind interne Schluesselpersonen ueber das normale Team hinaus? (Mit-GF, Beirat)
2. Welche externen Partner habt ihr regelmaessig? (Steuerberater, IT-Dienstleister, Anwalt)
3. Schluessel-Lieferanten?
4. Schluessel-Kunden (nur die mit Sonder-Beziehung — Stammdaten bleiben in `03-CRM/`)?
5. Verbaende, Kammern, Behoerden mit regelmaessigem Kontakt?
6. Gibt es Investoren / Geldgeber?

### Phase 3: Mitarbeiter-Roster

Optional, falls noch nicht da. Frage:

> Wer ist im Team? Name, Rolle, Hauptteam, optional Kontakt. Lass dich nicht von "noch nicht ganz fertig" abhalten — wir koennen es spaeter ergaenzen.

Trag in `04-Mitarbeiter/team-mitglieder.md` ein.

### Phase 4: Scaffold

Schreibe in einem Rutsch (mit Backup nach `99-Archiv/intake-YYYY-MM-DD-HHMM/` falls Files schon existieren):

1. `01-Firma Home/unsere-leistungen.md` — aus Sektion 1 + 3
2. `01-Firma Home/unsere-kunden.md` — aus Sektion 2 + 3
3. `01-Firma Home/markenstimme.md` — aus Sektion 4 (Beispiel-Texte woertlich)
4. `01-Firma Home/strategie.md` — aus Sektion 5
5. `01-Firma Home/unsere-tools.md` — aus Sektion 6 (7-Bucket-Tabelle)
6. `01-Firma Home/stakeholder.md` — aus Sektion 7
7. `04-Mitarbeiter/team-mitglieder.md` — Roster
8. `Team-Wissen/Session-Logs/YYYY/MM/YYYY-MM-DD-onboarding-firma.md` — Session-Log mit allen Antworten

### Phase 5: Abschluss

Drei-Zeilen-Output:

```
✓ Erst-Setup erledigt. AI OS kennt euch jetzt.

Naechster Schritt: sag mir — "woran soll ich diese Woche arbeiten?"
Spaeter: lauf /audit fuer den 4 C's Score.
```

Wenn der User die "woran soll ich"-Frage stellt: 3-Bullet-Antwort in der eigenen Markenstimme, basierend auf Sektion 5 (Strategie).

---

## Modus 2: Team (neuer Team-Folder)

**Vorbedingung:** Team-Verantwortlicher oder Operator.

### Phase 1: Setup

Frage:

1. **Team-Name (kebab-case fuer Folder):** z.B. `produktion`, `it`, `kundenservice`
2. **Funktion in einem Satz:** Was macht das Team in der Firma?

Lege Folder an: `02-Teams/<team-name>/` als Kopie von `02-Teams/_neues-team/`.

### Phase 2: 4 Sektionen

#### Sektion 1: Wer wir sind (→ `kontext.md` Kopf)

1. Team-Verantwortlicher (Name)?
2. Mitglieder (Namen + Rolle, kurz)?

#### Sektion 2: Tools & Schnittstellen (→ `kontext.md`)

1. Welche externen Tools nutzt das Team die NICHT firmenweit sind? (CRM, ERP, Spezialsoftware)
2. Welche externen Dienstleister oder Schnittstellen sind relevant?
3. Mit welchen anderen Teams arbeitet ihr eng zusammen, und wofuer?

#### Sektion 3: Team-Regeln (→ `kontext.md`)

1. Welche 3-5 wichtigsten wiederkehrenden Vorgaenge habt ihr?
2. Welche Regeln gelten nur in diesem Team (zusaetzlich zu Firmen-Regeln)?
3. Welche Themen brauchen 4-Augen-Prinzip oder Eskalation?

#### Sektion 4: Glossar (→ `kontext.md`)

1. Welche Fachbegriffe nutzt ihr, die ein Aussenstehender nicht verstehen wuerde?
2. Welche Abkuerzungen?

### Phase 3: Skills-Hinweis

Frage:

> Welche wiederkehrenden Aufgaben koennten als Skills automatisiert werden? (3-5 Vorschlaege)

Notiere die Vorschlaege als Liste in `02-Teams/<team>/.claude/skills/README.md`. Bauen passieren spaeter, separat.

### Phase 4: Scaffold

1. `02-Teams/<team>/kontext.md` ausgefuellt
2. Eintrag in `04-Mitarbeiter/team-mitglieder.md` falls neue Personen
3. `Team-Wissen/Session-Logs/YYYY/MM/YYYY-MM-DD-onboarding-team-<name>.md`

---

## Modus 3: Unternehmen (neuer externer Firmen-Folder)

### Phase 1: Setup

Frage:

1. **Firmenname (voller Name inkl. Rechtsform):**
2. **Folder-Slug (kebab-case, ohne Rechtsform):** z.B. `acme-gmbh` → `acme`. Bei Unsicherheit: vorschlagen.
3. **Beziehungs-Typ** (kann mehrere): kunde / lieferant / partner / berater / beirat / mitbewerber / ehemalig

Lege Folder an: `03-CRM/Unternehmen/<slug>/` als Kopie von `_neues-unternehmen/`.

### Phase 2: 5 Sektionen

#### Sektion 1: Stammdaten (→ `kontext.md`)

1. Branche, Niche
2. Standort
3. Webseite
4. Wann kam der Kontakt zustande?
5. Wer hat den Kontakt bei euch aufgebaut?

#### Sektion 2: Beziehung (→ `kontext.md`)

1. Aktueller Beziehungs-Status (aktiv / schlafend / eskaliert)?
2. Bei Kunden: Vertrag / Vereinbarung / einmalig?
3. Bei Lieferanten: wie kritisch (ersetzbar / schwer ersetzbar / nicht ersetzbar)?
4. Hauptbetreuendes Team auf eurer Seite?

#### Sektion 3: Schluesselpersonen (→ `kontext.md` + ggf. neue Personen-Folder)

1. Liste Hauptansprechpartner (Name, Funktion) auf der Gegenseite
2. Pro Person: relevant genug fuer eigenen `03-CRM/Personen/<name>/` Folder? Bei JA: Wikilink setzen, evtl. spaeter Modus "Person" laufen.

#### Sektion 4: Was wir machen (→ `kontext.md`)

1. Bei Kunden: welche Leistungen / Produkte erhalten sie?
2. Bei Lieferanten: was liefern sie?
3. Bei Partnern: Art der Kooperation?
4. Bei Berater/Beirat: in welchem Format und Rhythmus?

#### Sektion 5: Beziehung & Tonalitaet (→ `kontext.md`)

1. Anrede (Du / Sie / situativ)?
2. Kommunikations-Vorlieben (Mail / Telefon / Vor-Ort)?
3. Tabu-Themen oder heisse Eisen?
4. Bisherige Wins / Losses kurz?

### Phase 3: Scaffold

1. `03-CRM/Unternehmen/<slug>/kontext.md` ausgefuellt
2. `Team-Wissen/Session-Logs/YYYY/MM/YYYY-MM-DD-onboarding-unternehmen-<slug>.md`
3. Falls neue Personen genannt: Frage "Soll ich Modus 'Person' fuer [Name] starten?"

---

## Modus 4: Person (neuer externer Personen-Folder)

### Phase 1: Setup

Frage:

1. **Vor- und Nachname:**
2. **Folder-Slug (kebab-case):** z.B. `hans-mueller`. Bei Doppel-Namen: Anhang Firma (`hans-mueller-acme`).
3. **Aktuelle Firma:** Wikilink falls in `03-CRM/Unternehmen/` vorhanden, sonst nennen.

Lege Folder an: `03-CRM/Personen/<slug>/` als Kopie von `_neue-person/`.

### Phase 2: 4 Sektionen

#### Sektion 1: Basis (→ `kontext.md`)

1. Funktion / Rolle?
2. Aktuelle Firma + Wikilink
3. Mail / Telefon / LinkedIn (was vorhanden ist)?
4. Erste Begegnung (Datum + Anlass — Messe, Empfehlung, Cold-Call)?

#### Sektion 2: Verlauf (→ `kontext.md`)

1. Welche Karriere-Stationen waren beruflich relevant fuer die Beziehung?
2. Gibt es vorherige Firmen wo ihr auch Kontakt hattet?
3. Gibt es einen Trigger der die Beziehung gepraegt hat? (Empfehlung, gemeinsames Projekt, etc.)

#### Sektion 3: Persoenliches (→ `kontext.md`, nur beruflich-relevant)

1. Kommunikations-Stil (direkt / detailorientiert / strategisch)?
2. Vorlieben (z.B. mag Direktheit, hasst Powerpoint, bevorzugt Telefon)?
3. Smalltalk-Themen / Interessen die er gerne aufgreift?
4. Familie / Hintergrund (nur wenn er es selbst offen anspricht)?

#### Sektion 4: Strategische Relevanz (→ `kontext.md`)

1. Welche Entscheidungs-Schwellen hat er? (Z.B. Investitionen > 50k EUR braucht Vorstand-Approval)
2. Welche Pain Points hat er aktuell?
3. Wo koennt ihr ihm helfen?
4. Wo muesst ihr vorsichtig sein?

### Phase 3: Scaffold

1. `03-CRM/Personen/<slug>/kontext.md` ausgefuellt
2. Backlink-Eintrag in `03-CRM/Unternehmen/<firma>/kontext.md` (Schluesselpersonen-Liste) falls noch nicht da
3. `Team-Wissen/Session-Logs/YYYY/MM/YYYY-MM-DD-onboarding-person-<slug>.md`

---

## Regeln (alle Modi)

1. **Stell maximal 3 Fragen auf einmal.** Warte auf Antworten bevor du weitermachst.
2. **Wenn der User kurz antwortet, frag NICHT nach mehr.** Nimm was er gibt.
3. **Beim Schreiben: extrahier was wirklich gesagt wurde.** Erfinde nichts dazu.
4. **Schreib auf Deutsch.** Es sei denn der User antwortet konsequent englisch.
5. **Markiere Stellen wo du unsicher bist mit `[zu pruefen: ...]`** damit der User nachschaerfen kann.
6. **Schreibe NIE in einen Folder fuer den der User keine Schreib-Berechtigung hat.** Im Zweifel fragen.
7. **Idempotent.** Re-run aktualisiert, ueberschreibt nicht ohne Backup. Backup nach `99-Archiv/intake-{YYYY-MM-DD-HHMM}/`.
8. **Voice-Samples (Sektion 4 Firma-Modus): Paste-only.** Wenn der User im Chat tippt, ablehnen:

   > *"Stop — bitte einfuegen, nicht tippen. Original aus LinkedIn / Mail / Webseite reinkopieren, sonst ist das Sample bereits durch unser Gespraech geformt."*

## Was nicht

- Frag nicht alles auf einmal — das ueberfordert
- Erfinde keine Details die der User nicht gesagt hat
- Schreib keine generischen Marketing-Floskeln rein ("wir sind innovativ", "wir lieben Qualitaet")
- Frag nicht nach API-Keys oder Passwoertern am Tag 1