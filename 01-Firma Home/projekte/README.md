# 01-Firma Home/projekte

**Aktive interne Projekte.**

Hier landen Projekte, die nicht direkt einem Kunden zuzuordnen sind:

- Eigenes Marketing (Webseiten-Relaunch, Content-Kampagne, Event-Vorbereitung)
- Eigene Produktentwicklung
- Hire-Prozesse für neue Mitarbeiter
- Größere Initiativen (z.B. "Q3 Pricing-Reform")

## Was hier NICHT rein soll

- Kunden-Projekte → `03-CRM/Unternehmen/<kunde>/`
- Tagesgeschäft → einzelne Aufgaben sind keine Projekte
- Wissens-Aufbau → `01-Firma Home/`

## Struktur pro Projekt

```
01-Firma Home/projekte/
└── q3-pricing-reform/
    ├── _hub.md
    ├── recherche/
    ├── entscheidungen/
    └── kommunikation/
```

## Hub-Datei

Jedes Projekt hat eine `_hub.md`:

- Ziel
- Verantwortlich
- Status (planning / doing / paused / done)
- Meilensteine
- Risiken
- Nächste Schritte

## Abschluss

Wenn ein Projekt fertig ist:

> "Schließ das Projekt q3-pricing-reform ab"

Die KI verschiebt den Ordner nach `99-Archiv/projekte/YYYY/MM/` und schreibt eine kurze Lessons-Learned in `Team-Wissen/`.
