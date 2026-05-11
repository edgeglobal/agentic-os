# 00-Inbox

**Wo Mitarbeiter rohe Inputs reinwerfen.**

Jeder im Team kann hier Dateien, Notizen, Screenshots, Voice-Memos oder Brain-Dumps ablegen. Die KI nimmt sie auf und routet sie an den richtigen Spezialisten.

## Was hier rein darf

- Geschäftskarten (Foto)
- Screenshots von wichtigen Nachrichten
- Voice-Memos (als Audio oder Transkript)
- Brain-Dumps ("hatte gerade Idee zu X")
- Forwarded E-Mails
- Meeting-Notizen die noch nicht aufbereitet sind
- Links zu interessanten Artikeln

## Was hier NICHT rein soll

- Fertige Dokumente (gehören in `01-Firma/` oder `02-Vorlagen/`)
- Kunden-spezifisches Material (gehört in `03-Kunden/<kunde>/`)
- Personalbezogene Daten (gehört in `05-Mitarbeiter/`)

## Wie die KI verarbeitet

Sage zur KI:

> "Verarbeite die Inbox"

Die KI geht jede Datei durch und schlägt vor, wohin sie soll. Bei Geschäftskarten erstellt er einen CRM-Eintrag, bei Brain-Dumps wird ein Journal-Eintrag geschrieben, bei Recherche-Anfragen startet die KI eine Recherche.

Verarbeitete Dateien werden gelöscht (nicht ins Archiv) — das Original-Wissen ist dann in der Zielstruktur.
