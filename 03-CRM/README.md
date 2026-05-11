<!--
AI OS — Agentic Operating System für KMUs
© 2026 Gerald Eder · UmsatzAI · MIT License
-->

# 03-CRM/

Customer Relationship Management — alles was mit externen Kontakten zu tun hat.

```
03-CRM/
├── Unternehmen/              externe Firmen (Kunden, Lieferanten, Partner, Berater)
├── Personen/                 externe Personen (Ansprechpartner, Beirat, Investoren)
└── Meetings/                 Meeting-Notes (internal + external) mit Wikilinks
```

## Warum diese drei zusammen

Sie sind das Wissens-Geflecht der Geschaeftsbeziehungen:

- **Unternehmen** = mit wem
- **Personen** = mit wem konkret
- **Meetings** = was wurde besprochen, wann

Wikilinks zwischen den dreien bauen ueber Jahre Kunden-/Kontakt-Wissen auf. Beispiel: ein Meeting-File verweist auf `[[Unternehmen/acme-gmbh]]` und `[[Personen/hans-mueller]]`. Backlinks erscheinen automatisch in den jeweiligen kontext.md-Files.

## CRM-Light statt CRM-Tool

Fuer KMU ohne CRM-Loesung (HubSpot, Pipedrive, lexoffice CRM) ist dieser Folder das CRM. Markdown-only, in jedem Cloud-Sync-Editor zugaenglich, ueber Jahre durchsuchbar.

Falls die Firma ein CRM-Tool hat: hier nur die Schluesselkunden/-personen mit hoher Beziehungs-Tiefe pflegen. Massen-Kontakte bleiben im CRM-Tool.

## Pflege

- **Wer pflegt:** Teams die mit dem Kontakt arbeiten
- **Wer schreibt was:** je nach Folder-Permission im Cloud-Sync
- **Verknuepfung:** via `[[Wikilinks]]` — die KI hilft beim Setzen
