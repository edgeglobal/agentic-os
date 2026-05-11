# 08-Meetings/internal/

Meetings ohne externe Teilnehmer: Geschaeftsfuehrungsrunden, Team-Standups, Team-Reviews, Strategie-Sitzungen, Quartals-Plannings.

## Typische Meetings

- **Team-Standups** (taeglich oder woechentlich) — pro Team
- **Wochen-Review** der Geschaeftsfuehrung
- **Quartals-Planning** firmenweit
- **Strategie-Sitzung**
- **Mitarbeiter-Jour-Fixe** (1:1)

## Naming

`YYYY/MM/YYYY-MM-DD-<thema>.md`

- `2026/05/2026-05-11-gf-runde.md`
- `2026/05/2026-05-12-marketing-standup.md`
- `2026/05/2026-05-15-quartals-planning-q3.md`

## Verknuepfung

Bei Team-Standups: Verknuepfung zum Team-Folder, z.B. `Team: [[07-Teams/marketing-vertrieb]]`.

Bei firmenweiten Meetings: Bezug zu Projekten und Personen via Wikilinks.

## Mindest-Struktur eines Meeting-Files

```markdown
# [Thema] — YYYY-MM-DD

**Teilnehmer:** [Namen]
**Typ:** [Standup / Review / Strategie / ...]
**Bezug:** [[Wikilinks zu Projekten / Teams]]

## Was besprochen wurde

- [Bullet]

## Entscheidungen

- [Was, wer]

## Action Items

- [ ] [Was, wer, bis wann]
```
