---
name: neuer-kunde
description: Use when the user says "wir haben einen neuen Kunden gewonnen", "neuer Kunde", "Kunde X hat unterschrieben", "lege Kunde X an", "new client onboarded", or "wir haben Vertrag mit [Firma]". Runs SOP-002 conversationally — collects customer info, scaffolds the customer folder with hub, briefing, and meeting/delivery subfolders.
---

## What this skill does

Conducts the new-customer-onboarding flow defined in [[SOP-002-neuen-kunden-anlegen]]. Asks for stammdaten, creates the folder structure, fills the hub file, drafts a briefing, and (optionally) drafts a kickoff email in the user's brand voice.

## Inputs the skill reads

- `01-Wissen/markenstimme.md` — fuer den Stil der Kickoff-Mail
- `01-Wissen/unsere-leistungen.md` — fuer korrekte Leistungs-Bezeichnung
- `01-Wissen/unsere-kunden.md` — fuer Persona-Zuordnung
- `02-Vorlagen/kunden-onboarding.md` — Briefing-Template
- `Team-Wissen/Richtlinien/R-001-namenskonventionen.md` — fuer Filename-Regeln
- `03-Kunden/` — pruefen dass kein Duplikat existiert

## Execution

### Step 1: Stammdaten

Ask in Bloecken (nicht eine Frage nach der anderen — Block fragt 4-5 zusammen):

**Block A — Firma:**
- Firmenname (offiziell, ggf. mit Rechtsform)?
- Firmenname (fuer Kommunikation, kurz)?
- Webseite?
- Branche?
- Groesse (MA / Umsatz wenn bekannt)?
- Standort?

**Block B — Hauptkontakt:**
- Vor- und Nachname?
- Position?
- E-Mail?
- Telefon (optional)?

**Block C — Vertrag:**
- Welche Leistung wurde verkauft? (zeige Liste aus `unsere-leistungen.md` zur Auswahl)
- Vertragsstart-Datum?
- Vertragsdauer?
- Vertragswert (€)?
- Bereits ein Angebot/Vertrag-File im Vault? (verweisen wir darauf)

**Block D — Spezielles:**
- Erwartete Risiken aus dem Verkaufsgespraech?
- Spezielle Anforderungen (Compliance, NDA, sensitive Branche)?
- Account-Lead bei euch (Name)?

### Step 2: Folder anlegen

Filename-Regel: kebab-case, ohne Rechtsform-Suffix, keine Umlaute. Beispiele:
- "Acme GmbH" → `acme/`
- "Maier & Soehne KG" → `maier-und-soehne/`
- "Dr. Schmidt Klinik" → `schmidt-klinik/`

Create:
```
03-Kunden/<slug>/
├── _hub.md
├── briefing.md
├── meetings/
├── lieferungen/
└── notizen.md
```

### Step 3: Hub-Datei `_hub.md`

Frontmatter ausfuellen aus den Stammdaten:

```yaml
---
type: kunde
firma: <full name>
status: active
branche: <branche>
groesse: <groesse>
hauptkontakt: <name>
hauptkontakt-email: <email>
vertragsstart: YYYY-MM-DD
vertragsdauer: <dauer>
vertragswert: <€>
account-lead: [[<account-lead>]]
---
```

Body: kurzer Hub-Aufbau mit Sektionen Status, Vertrag, Hauptkontakte, Aktuelle Phase, Naechste Termine, Risiken, Lieferungen, Cross-Links.

Cross-Links setzen:
- Wenn Angebot existiert: `[[YYYY-MM-DD-angebot-<slug>]]`
- Auf passende ICP-Persona aus `unsere-kunden.md`
- Auf gekaufte Leistung in `unsere-leistungen.md`

### Step 4: Briefing-Datei

Fill `briefing.md` based on `02-Vorlagen/kunden-onboarding.md`. Aus Stammdaten ausfuellen, Luecken als `[?]` markieren mit Frage zum nachtragen.

Bei Luecken (z.B. fehlende Liefermeilensteine, fehlender Kommunikations-Rhythmus): User fragen, ob er die jetzt fuellen will, oder spaeter im Kickoff-Meeting klaeren.

### Step 5: Kickoff-E-Mail-Entwurf (optional)

Frage: "Soll ich gleich einen Kickoff-Mail-Entwurf machen?"

Bei Ja:
- Larry liest `01-Wissen/markenstimme.md`
- Schreibt eine kurze E-Mail (3-5 Saetze) an den Hauptkontakt mit:
  - Begruessung in Markenstimme
  - Bestaetigung des Vertragsabschlusses
  - Vorschlag fuer Kickoff-Termin (innerhalb 5 Werktagen)
  - Was vom Kunden zur Vorbereitung gebraucht wird (aus Briefing-Liste)
  - Schlussformel

E-Mail-Entwurf in den Chat printen (nicht in Datei schreiben — User schickt selbst).

### Step 6: Confirmation

```
✓ Kunde angelegt: <Firma>

Pfad: 03-Kunden/<slug>/
- _hub.md (gefuellt)
- briefing.md (Stub mit X offenen Punkten)
- meetings/ (leer, fuer Protokolle)
- lieferungen/ (leer)
- notizen.md (Stub)

Cross-Links:
- ICP-Persona: [[<persona-name>]]
- Leistung: [[unsere-leistungen]]
- Account-Lead: [[<name>]]

Kickoff-Mail-Entwurf: [oben im Chat / nicht erstellt]

Naechster Schritt: Mail verschicken / Briefing-Luecken fuellen / Kickoff-Termin setzen.
```

## Critical rules

1. **Kein Duplikat anlegen.** Wenn der Slug bereits existiert in `03-Kunden/`, fragen ob es derselbe Kunde ist (dann an existing anhaengen) oder ein anderer (dann Slug schaerfen).
2. **Sensitive-Branchen-Flag.** Wenn Branche Anwalt/Arzt/Finanz/Behoerde, im `_hub.md` "**SENSITIV — keine Details aussserhalb dieses Ordners zitieren**" einfuegen.
3. **Markenstimme strict.** Kickoff-Mail-Entwurf MUSS `markenstimme.md` befolgen — Tabu-Woerter checken.
4. **Read-only auf `01-Wissen/`.** Nur 03-Kunden/-Pfade neu anlegen.
5. **Frontmatter komplett.** Kein leeres Pflichtfeld.