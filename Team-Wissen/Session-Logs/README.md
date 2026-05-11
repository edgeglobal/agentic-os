# Session-Logs

**Append-only Sitzungs-Gedächtnis.**

Jede Arbeits-Session mit dem AI-Team produziert einen Session-Log. Die KI schreibt ihn am Session-Ende.

## Struktur

```
Session-Logs/
├── 2026/
│   ├── 05/
│   │   ├── 2026-05-09-onboarding-und-setup.md
│   │   ├── 2026-05-09-tagesabschluss.md
│   │   └── 2026-05-10-strategie-q3.md
│   └── 06/
│       └── ...
```

Format: `YYYY/MM/YYYY-MM-DD-<slug>.md`

## Inhalt eines Session-Logs

Jeder Log enthält:

- **Aktive Tasks** (Checkboxen oben — Single Source of Truth für die Session)
- **Was wir gemacht haben** (Highlights, nicht jedes Detail)
- **Was der User korrigiert hat** (Realignments — wertvollste Lerneffekte)
- **Entscheidungen** (mit Begründung)
- **Deltas vs vorheriger Plan** (was hat sich geändert seit letzter Session)
- **SSOT/Strukturelle Fixes** (Bibliothekar-Pass)
- **Cross-Links** zu früheren Logs

## Warum das wichtig ist

Auto-Memory von AI ist unzuverlässig. Session-Logs sind:
- ✅ Persistent (überstehen Updates, Session-Wechsel, Tool-Wechsel)
- ✅ Durchsuchbar (Markdown, von Claude lesbar, von Mensch lesbar)
- ✅ Auditable (jeder weiß, was wann entschieden wurde)
- ✅ Cross-linked (Logs verweisen aufeinander)

## Wer liest Session-Logs?

- **Die KI am Anfang jeder neuen Session** — schaut letzten Log ein bis drei zurück, baut sich Kontext auf
- **Du** wenn du nachvollziehen willst, "was hatten wir letztes Mal entschieden?"
- **Neue Mitarbeiter** beim Onboarding — sie lesen die letzten 4 Wochen, um zu verstehen wie das Team tickt

## Privacy

Session-Logs können sensitiv sein (Strategie, Personalfragen, Krisen). Wenn Logs für VAs/externe MA freigegeben werden:
- Vorab-Filter durch die KI: "Welche Logs darf [Person] sehen?"
- Sensitive Logs in `99-Archiv/team-internal/` umlagern, wenn nicht mehr aktiv

## Session-Log manuell auslösen

Sag zur KI:
> "Schließ die Session ab" / "Schreib einen Session-Log"

Die KI führt `/session-abschluss` Skill aus (Claude Code) oder läuft den Workflow manuell.
