---
type: knowledge
topic: team
last-updated: 2026-05-09
status: template
---

# Team-Kontext: Marketing & Vertrieb

> **Anleitung:** Wir gewinnen Kunden und halten Kontakt. Lead-Generierung, Akquise, Angebote, Bestandskunden-Pflege, Marken-Auftritt. Diese Datei wird gelesen wenn die KI fuer dieses Team arbeitet.

## Wer wir sind

Wir gewinnen Kunden und halten Kontakt. Lead-Generierung, Akquise, Angebote, Bestandskunden-Pflege, Marken-Auftritt.

## Mitglieder

- [Name] - Vertriebsleitung
- [Name] - Marketing-Verantwortung
- [Name] - Innendienst / Angebotsabwicklung

Verantwortlich: [Name + Mail]

## Externe Tools die das Team nutzt

> Tools die NICHT firmenweit sind. Firmen-Tools-Stack in [[01-Firma/unsere-leistungen]] oder einer separaten tools.md.

- **CRM:** [z.B. HubSpot / Pipedrive / lexoffice CRM] - Leads, Kontakte, Pipeline
- **Newsletter-Tool:** [Mailchimp / Brevo / ActiveCampaign]
- **LinkedIn:** Firmenseite + persoenliche Profile der Vertriebler
- **Praesentations-Tools:** PowerPoint / Keynote / Pitch

## Team-spezifische Regeln

- **Tonalitaet bei Kunden-Kommunikation:** Standard aus [[01-Firma/markenstimme]]. Abweichungen pro Kunde stehen in `03-Kunden/<kunde>/kontext.md`.
- **Vor jedem Kundentermin:** Kunden-Kontext-Datei lesen plus letzte 2 Gespraechs-Protokolle.
- **Nach jedem Kundentermin:** Protokoll in `03-Kunden/<kunde>/gespraeche/` ablegen. Maximal 10 Bullet Points.
- **Angebote:** Draft in der persoenlichen Inbox starten, final-Version in `03-Kunden/<kunde>/ablage/`.
- **Preise:** nie ohne Ruecksprache mit Vertriebsleitung kommunizieren wenn ausserhalb der Standard-Listen.

## Skills die wir nutzen

> Skills die in `.claude/skills/` dieses Teams liegen. Die KI darf sie ohne Rueckfrage triggern.

- `angebot-entwurf` - Erst-Entwurf eines Angebots aus Kundenkontext und Anfrage
- `follow-up-mail` - Folgemail nach Kundengespraech, aus Protokoll
- `lead-qualifizierung` - eingehende Anfrage gegen ICP pruefen
- `newsletter-entwurf` - Erst-Entwurf eines Newsletters aus Themen-Liste

(Skills die noch nicht existieren werden bei Bedarf neu gebaut. Sag zur KI: "Lass einen Skill bauen fuer Angebots-Entwurf.")

## Glossar

- **Lead:** eingehende Anfrage, noch nicht qualifiziert
- **Qualifizierter Lead:** Lead passt ins ICP, ist als Opportunity erfasst
- **Angebot:** schriftliches Leistungs-Plus-Preis-Dokument
- **Pipeline:** Liste laufender Opportunities mit Status
- **Bestandskunde:** Kunde mit aktivem Vertrag oder Auftrag in den letzten 12 Monaten

## Wann andere Teams uns lesen duerfen

- Lese-Zugriff fuer: Geschaeftsfuehrung, Fulfillment (fuer Kundenkontext bei Lieferung)
- Schreib-Zugriff: nur Team-Mitglieder
