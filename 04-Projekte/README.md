# 04-Projekte

**Aktive interne Projekte.**

Hier landen Projekte, die nicht direkt einem Kunden zuzuordnen sind:

- Eigenes Marketing (Webseiten-Relaunch, Content-Kampagne, Event-Vorbereitung)
- Eigene Produktentwicklung
- Hire-Prozesse für neue Mitarbeiter
- Größere Initiativen (z.B. "Q3 Pricing-Reform")

## Was hier NICHT rein soll

- Kunden-Projekte → `03-Kunden/<kunde>/`
- Tagesgeschäft → einzelne Aufgaben sind keine Projekte
- Wissens-Aufbau → `01-Wissen/`

## Struktur pro Projekt

```
04-Projekte/
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

> "Larry, schließ das Projekt q3-pricing-reform ab"

Larry verschiebt den Ordner nach `99-Archiv/projekte/YYYY/MM/` und schreibt eine kurze Lessons-Learned in `Team-Wissen/`.
