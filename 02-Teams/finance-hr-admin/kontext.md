---
type: knowledge
topic: team
last-updated: 2026-05-09
status: template
---

# Team-Kontext: Finance, HR & Admin

> **Anleitung:** Buchhaltung, Lohn, HR, Vertraege, Office, Compliance. Drei Funktionen unter einem Dach, weil sie in den meisten KMU dieselben Personen teilen. Diese Datei wird gelesen wenn die KI fuer dieses Team arbeitet.

## Wer wir sind

Wir halten den Laden zusammen. Buchhaltung, Lohnabrechnung, Personal, Vertraege, Office, Compliance. Was die anderen Teams "einfach laeuft" als selbstverstaendlich erleben.

## Mitglieder

- [Name] - Buchhaltung / Controlling
- [Name] - Personal / HR
- [Name] - Office / Admin
- [Name] - Geschaeftsfuehrung (oft Schnittstelle)

Verantwortlich: [Name + Mail]

## Externe Tools die das Team nutzt

- **Buchhaltung:** [Datev / lexoffice / Sevdesk / Sage] - Belege, Rechnungen, USt-VA
- **HR-System:** [Personio / HRWorks / lokale Excel] - Mitarbeiter-Stammdaten, Urlaub, Krankmeldungen
- **Vertraege:** [DocuSign / Adobe Sign / per Mail-PDF]
- **Banking:** [Online-Banking der Hausbank]
- **Office-Suite:** Microsoft 365 / Google Workspace

## Team-spezifische Regeln

- **Vertrauliches NIE im Markdown-AI-OS:** Gehaelter, Krankmeldungen, Bewerber-Daten, Personalgespraechs-Notizen gehoeren ins HR-System, nicht hier.
- **Buchhaltungs-Originale gehoeren ins Buchhaltungs-System.** Hier nur Markdown-Auswertungen / Memos / Prozess-Beschreibungen.
- **Vertraege im Klartext gehoeren ins DMS / Vertragssystem.** Hier nur Memos und Vertrags-Inhalts-Beschreibungen.
- **DSGVO:** vor jeder Verarbeitung personenbezogener Daten durch KI pruefen ob Lawful-Basis vorliegt.
- **Steuerberater-Kommunikation:** sachliche Sprache, keine kreative Brand-Voice.

## Skills die wir nutzen

- `beleg-klassifizierung` - Foto/Mail eines Belegs aufnehmen, klassifizieren, in Buchhaltungs-System einsortieren
- `rechnungs-vorlage` - Rechnung aus Auftrags-Daten generieren
- `bewerber-screening` - eingehende Bewerbung gegen Anforderungs-Profil pruefen (DSGVO-konform, kein Auto-Reject)
- `vertrags-zusammenfassung` - aus Vertragstext eine 1-Seiten-Zusammenfassung
- `monats-abschluss-checkliste` - Schritte fuer Monatsabschluss generieren und tracken
- `mitarbeiter-onboarding-checkliste` - alle Schritte fuer einen neuen Mitarbeiter

(Skills die noch nicht existieren werden bei Bedarf neu gebaut.)

## Glossar

- **Beleg:** Quittung, Rechnung, Bewirtungsbeleg - alles was buchhalterisch erfasst werden muss
- **OP (Offene Posten):** noch nicht bezahlte Rechnungen
- **USt-VA:** Umsatzsteuer-Voranmeldung (monatlich oder quartalsweise)
- **BWA:** Betriebswirtschaftliche Auswertung (vom Steuerberater)
- **DSGVO:** Datenschutz-Grundverordnung
- **Lawful-Basis:** Rechtsgrundlage fuer DSGVO-Verarbeitung (Einwilligung, Vertrag, berechtigtes Interesse, etc.)

## Wann andere Teams uns lesen duerfen

**Standard: kein Lese-Zugriff fuer Rest der Firma.** Dieser Team-Folder ist staerker abgeschottet. Nur Operator und Geschaeftsfuehrung haben Lese-Zugriff.

In Cloud-Storage: Folder-Berechtigung restriktiv setzen.
