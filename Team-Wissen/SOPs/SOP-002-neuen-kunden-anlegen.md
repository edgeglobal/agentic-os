# SOP-002 — Neuen Kunden anlegen

**Wofür:** Wenn ein neuer Kunde gewonnen wurde (Vertrag unterschrieben).
**Auslöser:** User sagt "wir haben einen neuen Kunden gewonnen: [Firma]"
**Verantwortlich:** Die KI
**Dauer:** ~10-15 Minuten interaktiv

---

## Schritte

### 1. Stammdaten erfassen

Die KI fragt:
- Firmenname (offiziell)?
- Hauptkontakt: Name, Position, E-Mail?
- Branche?
- Größe (MA-Anzahl, Umsatz wenn bekannt)?
- Welche Leistung wurde verkauft? (Verweis auf [[organization]])
- Vertragsstart?
- Vertragsdauer?
- Vertragswert (€)?

### 2. Ordner anlegen

```
03-CRM/Unternehmen/
└── <firma-kebab-case>/
    ├── _hub.md
    ├── briefing.md
    ├── meetings/
    ├── lieferungen/
    └── notizen.md
```

Filename: kebab-case, ohne GmbH/AG suffix. Beispiel: `acme/`, nicht `acme-gmbh/`.

### 3. Hub-Datei `_hub.md` erstellen

```markdown
---
type: kunde
firma: Acme GmbH
status: active
branche: Maschinenbau
groesse: 50 MA
hauptkontakt: Max Mustermann
hauptkontakt-email: max@acme.de
vertragsstart: 2026-05-15
vertragsdauer: 12 Monate
vertragswert: 45000
account-lead: [[<dein-name>]]
---

# Acme GmbH

## Status
Active — Phase 1 (Onboarding)

## Vertrag
Siehe [[2026-05-15-angebot]] — 12 Monate, €45.000.

## Hauptkontakte
- Max Mustermann (Geschäftsführer) — max@acme.de
- Anna Beispiel (Marketing) — anna@acme.de

## Aktuelle Phase
Phase 1: Setup (bis [Datum])

## Nächste Termine
- 2026-05-20: Kickoff-Meeting
- 2026-06-15: Erstes Review

## Risiken & Offene Punkte
- [Risiko/Punkt 1]
- [Risiko/Punkt 2]

## Lieferungen
- [[2026-06-01-konzept-v1]] (in Arbeit)

## Cross-Links
- [[organization]] — Leistungs-Definition
- [[wunschkunde-icp]] — passende ICP-Persona
```

### 4. Briefing-Dokument

Die KI schreibt: "Erstelle ein Onboarding-Briefing für Acme nach [[kunden-onboarding]] Vorlage."

Die KI füllt die Vorlage aus den Stammdaten und fragt User nach Lücken (Wer auf Kunden-Seite welche Rolle? Erwartete Risiken? Spezielle Anforderungen?).

### 5. Erstes Meeting planen

Die KI fragt: "Soll ich gleich einen Kickoff-Meeting-Termin vorschlagen?"

Bei Ja:
- Es wird geschrieben einen Vorschlag für die Kickoff-Agenda
- Die KI entwirft eine E-Mail an den Hauptkontakt zur Terminfindung (in [[brand]])

### 6. Cross-Linking

Die KI prüft:
- Passt der Kunde in eine bestehende ICP-Persona aus [[wunschkunde-icp]]? Wenn ja: Verweis hinzufügen.
- Gibt es ähnliche Kunden bereits im Vault, von denen dieser Kunde lernen kann?

### 7. Confirmation

> "Kunde angelegt. Ordner in `03-CRM/Unternehmen/<firma>/`, Hub gefüllt, Briefing-Dokument in `briefing.md`. Kickoff-Mail Entwurf ist im Chat — bereit zum Verschicken."

---

## Output

Angelegt:
- `03-CRM/Unternehmen/<firma>/_hub.md`
- `03-CRM/Unternehmen/<firma>/briefing.md`
- `03-CRM/Unternehmen/<firma>/meetings/` (leerer Ordner)
- `03-CRM/Unternehmen/<firma>/lieferungen/` (leerer Ordner)
- `03-CRM/Unternehmen/<firma>/notizen.md` (Stub)

## Referenzen

- [[kunden-onboarding]] (Vorlage)
- [[organization]]
- [[wunschkunde-icp]]
- [[brand]]
- [[R-001-namenskonventionen]]
