# Team-Projekte

Initiativen die das Team treibt und die ueber **mehr als 2 Wochen** laufen.

Firmenweite Cross-Team-Projekte liegen in `04-Projekte/` auf Repo-Ebene.

## Wann ein Projekt hierhin gehoert

- Laeuft ueber 2+ Wochen
- Mehrere Team-Mitglieder beteiligt
- Erzeugt 5+ Outputs (Mails, Doks, Auswertungen)
- Hat ein klares Ende

## Wenn keiner dieser Punkte zutrifft

Dann ist es eher ein Tagesgeschaeft-Vorgang — in `ablage/` oder direkt in `03-CRM/Unternehmen/<firma>/` ablegen.

## Aufbau pro Projekt

```
projekte/
├── _neues-projekt/                  ← Vorlage zum Duplizieren
│   ├── briefing.md
│   ├── status.md
│   ├── entscheidungen.md
│   └── outputs/
└── webrelaunch-acme/
    ├── briefing.md
    ├── status.md
    ├── entscheidungen.md
    └── outputs/
```

## Naming

Kebab-case, kurz, beschreibend:

- `webrelaunch-acme/`
- `lieferanten-audit-q2/`
- `prozess-optimierung-fulfillment/`

## Neues Projekt anlegen

1. `_neues-projekt/` duplizieren
2. Mit Projektname umbenennen
3. `briefing.md` ausfuellen (Ziele, Beteiligte, Zeitrahmen)
4. Wenn Kunden-bezogen: Wikilink zu `[[03-CRM/Unternehmen/<firma>]]` im briefing
