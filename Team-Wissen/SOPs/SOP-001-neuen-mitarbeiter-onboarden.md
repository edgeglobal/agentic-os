# SOP-001 — Neuen Mitarbeiter onboarden

**Wofür:** Wenn ein neuer Mitarbeiter ins Team kommt.
**Auslöser:** User sagt "wir haben einen neuen Mitarbeiter: [Name] als [Rolle]"
**Verantwortlich:** Die KI
**Dauer:** ~10 Minuten interaktiv mit dem User

---

## Schritte

### 1. Stammdaten erfassen

Die KI fragt:
- Vollständiger Name?
- Position/Rolle?
- E-Mail im Unternehmen?
- Start-Datum?
- Anwesenheit (Vollzeit/Teilzeit, Tage)?
- Direkter Vorgesetzter?

### 2. Zugang zu Tools

Die KI checkt mit User welche Zugänge nötig sind:

- [ ] Claude Team Plan (Einladung über Settings → Members)
- [ ] Cowork Desktop installiert
- [ ] Cloud-Sync Zugang (Dropbox/GDrive/OneDrive)
- [ ] E-Mail-Account
- [ ] Slack/Teams Account
- [ ] CRM-Zugang
- [ ] Andere tool-spezifische Zugänge

Die KI erstellt eine Checklist als Action Items im Hub-File des MA.

### 3. Ordner anlegen

```
05-Team/
└── <vorname-nachname>/
    ├── _hub.md         ← Profil, Rolle, Verantwortung
    ├── ziele.md        ← Persönliche Ziele
    └── 1-1s/           ← Wird mit Zeit gefüllt
```

Filename-Format: kebab-case, ohne Umlaut. Beispiel: `max-mustermann/`.

### 4. Hub-Datei `_hub.md` erstellen

Inhalt:

```markdown
---
type: team-member
name: Max Mustermann
role: Marketing Manager
email: max@firma.de
start-date: 2026-05-15
status: active
manager: [[<vorgesetzter>]]
---

# Max Mustermann

## Rolle
Marketing Manager — verantwortlich für [Bereich]

## Anwesenheit
Mo–Do, 8 Std/Tag

## Verantwortlichkeiten
- [Bereich 1]
- [Bereich 2]

## Aktuelle Projekte
- [[Projekt A]]
- [[Projekt B]]

## 1:1 Rhythmus
Wöchentlich, [Wochentag] um [Uhrzeit]
```

### 5. Eintragen in [[team-mitglieder]]

Neue Zeile in der Tabelle in `05-Team/team-mitglieder.md`.

### 6. Onboarding-Plan für die ersten 30 Tage

Die KI fragt User:
- Welche Tasks soll der MA in Woche 1 erledigen?
- Mit welchen Personen sollte er Kennenlern-Gespräche haben?
- Welche Wissens-Dateien sollte er zuerst lesen?

Die KI legt einen 30-Tage-Plan in `05-Team/<vorname-nachname>/onboarding-plan.md` an.

### 7. Welcome-Message für den MA

Die KI entwirft eine kurze Willkommens-Nachricht in [[markenstimme]]-Stil, die der User dem neuen MA schicken kann. Mit:
- Begrüßung
- Erste Aufgaben für Tag 1
- Wichtigste Wissens-Datei zum Start: [[01-Firma/markenstimme]]
- Wie er die KI nutzen kann

### 8. Confirmation an User

> "Mitarbeiter angelegt. Hub-Datei in `05-Team/<name>/_hub.md`, Plan in `onboarding-plan.md`, Eintrag in `team-mitglieder.md`. Welcome-Message ist im Chat — bereit zum Verschicken."

---

## Output

Folgende Dateien wurden angelegt/aktualisiert:
- `05-Team/<name>/_hub.md` — neu
- `05-Team/<name>/onboarding-plan.md` — neu
- `05-Team/<name>/ziele.md` — leerer Stub
- `05-Team/team-mitglieder.md` — Zeile hinzugefügt

## Referenzen

- [[team-mitglieder]]
- [[markenstimme]]
- [[R-001-namenskonventionen]]
