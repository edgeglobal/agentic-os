# Team-Referenzen

Team-spezifisches Wissen das **nicht firmenweit relevant** ist. Firmenweite Standards leben in `01-Firma Home/` und `Team-Wissen/`.

## Was rein gehoert

- Wettbewerber-Analysen (Marketing-Vertrieb)
- Lieferanten-Vergleiche (Fulfillment)
- Branchen-Trends, Studien
- Prozess-Doku die nur das Team braucht
- Glossar-Detailliertes (kurze Begriffe stehen in `kontext.md`)
- Interne Anleitungen
- Konkurrenz-Battle-Cards

## Was nicht

- **Externe Firmen mit Beziehung** → in `03-Unternehmen/<firma>/`
- **Externe Personen** → in `04-Personen/<name>/`
- **Firmenweite Richtlinien** → in `Team-Wissen/Richtlinien/`
- **Firmenweite SOPs** → in `Team-Wissen/SOPs/`

## Aufbau

Flach oder leicht geschachtelt — je nach Team. Marketing-Vertrieb hat z.B.:

```
referenzen/
├── wettbewerber-analyse.md
├── branchen-trends-q2-2026.md
├── messe-kalender-2026.md
└── battle-cards/
    ├── vs-mitbewerber-a.md
    └── vs-mitbewerber-b.md
```

## Pflege

Halbjaehrlich pruefen: was ist veraltet, was wird nicht genutzt. Veraltetes in `99-Archiv/teams/<team>/referenzen/`.
