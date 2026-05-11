# R-001 — Namenskonventionen

> Wie wir Dateien und Ordner benennen.

## Grundregeln

1. **Englisch oder Deutsch — konsequent pro Bereich.** Standardordner sind deutsch (`01-Firma Home/`, `03-Unternehmen/`). System-Bereiche sind englisch (`Team/`, `.claude/`).
2. **Kebab-Case bei Filenames.** `neuer-kunde.md`, nicht `Neuer Kunde.md` oder `neuer_kunde.md`.
3. **Keine Umlaute in Filenames.** `markenstimme.md`, nicht `markenstimmë.md`. Inhalt darf Umlaute haben.
4. **Keine Sonderzeichen außer `-` und `_`.** Vermeide Slashes, Klammern, Doppelpunkte in Filenames.
5. **Datum-Prefix wenn chronologisch wichtig.** `2026-05-09-meeting-acme.md` für Meeting-Protokolle. ISO-Format: `YYYY-MM-DD`.

## Ordner

- **Hauptordner:** Nummer-Prefix für Reihenfolge. `00-Inbox`, `01-Firma`, etc.
- **Team-Ordner:** kebab-case Funktions-Name. Beispiel: `marketing-vertrieb/`, `fulfillment/`.
- **Kunden:** kebab-case ohne Rechtsform-Suffix. `acme/` statt `acme-gmbh/`. Status im Frontmatter, nicht im Foldername.
- **Mitarbeiter:** Eintrag im `06-Mitarbeiter/team-mitglieder.md`-Roster, kein eigener Sub-Folder.

## Dateien nach Typ

| Typ | Format | Beispiel |
|---|---|---|
| Hub-Datei | `_hub.md` | `03-Unternehmen/acme/_hub.md` |
| INDEX | `INDEX.md` | `Team-Wissen/SOPs/INDEX.md` |
| README | `README.md` | `00-Inbox/README.md` |
| AGENTS-Vertrag | `AGENTS.md` | `AGENTS.md` (Root) |
| SOP | `SOP-NNN-<titel>.md` | `SOP-001-neuen-mitarbeiter-onboarden.md` |
| Workflow | `WF-NNN-<titel>.md` | `WF-001-taegliches-journal.md` |
| Richtlinie | `R-NNN-<titel>.md` | `R-001-namenskonventionen.md` |
| Session-Log | `YYYY-MM-DD-<slug>.md` | `2026-05-09-onboarding.md` |
| Meeting | `YYYY-MM-DD-<thema>.md` | `2026-05-09-kickoff-acme.md` |
| Briefing | `briefing.md` (im Kunden-Ordner) | `03-Unternehmen/acme/briefing.md` |
| Notizen | `notizen.md` (im Kunden-Ordner) | `03-Unternehmen/acme/notizen.md` |

## Slugs

Wenn ein Dateiname einen Slug enthält (z.B. `2026-05-09-<slug>.md`):
- Kebab-case
- Max 5-6 Wörter
- Beschreibend, nicht generisch
- ✅ `2026-05-09-pricing-reform-strategie.md`
- ❌ `2026-05-09-meeting.md` (zu generisch)
- ❌ `2026-05-09-besprechung-mit-team-zur-pricing-reform-und-mehreren-anderen-themen.md` (zu lang)

## Frontmatter

YAML-Frontmatter gehört an den Anfang jeder Datei (außer reine README.md):

```yaml
---
type: kunde | mitarbeiter | template | knowledge | meeting | sop | workflow | richtlinie
last-updated: YYYY-MM-DD
status: active | archived | draft
---
```

Spezifischere Felder je nach Typ — siehe Standard-Vorlagen.

## Wikilinks

- `[[dateiname]]` wenn der Name im Vault eindeutig ist
- `[[ordner/dateiname]]` bei Kollisionsrisiko
- `[[dateiname|Anzeigetext]]` für custom Anzeigetext
- Bild-Embeds: `![[Bilder/2026/05/2026-05-09-screenshot.png]]`

## Was Die KI erzwingt

Am Session-Ende prüft die KI:
- ✅ Alle neuen Dateien folgen den Naming-Regeln
- ✅ Frontmatter ist gesetzt wo nötig
- ✅ Wikilinks zeigen auf existierende Dateien (oder Stubs werden angelegt)
- ❌ Dateien mit Umlaut/Leerzeichen → Die KI benennt um, wenn keine externen Links betroffen sind, sonst flagged
