<!--
AI OS — Agentic Operating System für KMUs
© 2026 Gerald Eder · UmsatzAI · MIT License
-->

# 02-Vorlagen/

**Firmenweite Templates** — Vorlagen die **jedes Team** nutzt.

Team-spezifische Vorlagen leben in den jeweiligen Team-Foldern unter `07-Teams/<team>/vorlagen/`. Beispiel: `angebot.md` ist Vertrieb, also unter `07-Teams/marketing-vertrieb/vorlagen/`.

## Standard-Vorlagen (firmenweit)

| Datei | Wofuer |
|---|---|
| [[meeting-protokoll]] | Standard-Meeting-Notiz fuer alle Meetings |

(Mehr firmenweite Vorlagen kommen bei Bedarf dazu — z.B. wenn ihr ein firmenweit identisches Mail-Format habt.)

## Eigene Vorlage anlegen

**Firmenweit nutzbar?** → hier in `02-Vorlagen/`
**Nur fuer ein Team?** → in `07-Teams/<team>/vorlagen/`

Sage zur KI:

> "Erstelle eine firmenweite Vorlage fuer [X]"
> oder
> "Erstelle eine Vorlage fuer [X] fuer das Vertriebs-Team"

Die KI fragt nach der Struktur und legt die Datei im richtigen Ordner an.

## Regel

Vorlagen sind **leere Hüllen mit Platzhaltern**, keine ausgefüllten Beispiele. Beispiele kommen woanders rein:

- Kunden-spezifische Beispiele → `03-Unternehmen/<firma>/`
- Allgemeine Best-Practice-Beispiele → `Team-Wissen/Richtlinien/`
- Fertige Team-Outputs → `07-Teams/<team>/ablage/`
