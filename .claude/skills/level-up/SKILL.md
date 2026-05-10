---
name: level-up
description: Use weekly to find and ship one new automation or capability. Trigger on "let's level up", "was sollten wir als naechstes automatisieren", "find me leverage this week", "naechster automatisierungs-schritt", or as a Friday ritual. One run = one shipped artifact (skill, workflow, SOP, or hire).
---

## What this skill does

Walks the user through a 3-phase interview each week to surface and ship one new capability:

1. **Mindset** — finde den Kandidaten (was schmerzt diese Woche?)
2. **Method** — scope einen davon (was ist die kleinste sinnvolle Aufgabe?)
3. **Machine** — bau ihn (welche Form: Skill, Workflow, SOP oder Hire?)

**Eine Sitzung = ein Liefergegenstand.** Keine Multi-Kandidat-Planung.

## When `/level-up` runs

- **Erste Sitzung: Tag 14 nach Onboarding.** Frueher liefert triviale Outputs.
- **Cadence: woechentlich, Freitag-Nachmittag.** Wochen-Review, eine Automation, Liefer-Montag.
- **On-demand jederzeit.** Wenn ein manueller Task waehrend der Woche schmerzt.

## Inputs the skill reads

- `01-Wissen/markenstimme.md`, `unsere-kunden.md`, `unsere-leistungen.md`
- `05-Team/team-mitglieder.md`
- `Team/agent-index.md` — wer kann was
- `Team-Wissen/Session-Logs/YYYY/MM/*.md` (letzte 7 Tage)
- `.claude/skills/*/SKILL.md` Frontmatter — was es schon gibt
- `Team-Wissen/SOPs/*.md` Frontmatter — was schon dokumentiert ist

## Execution — drei Phasen

### Phase 1 — Mindset Interview (find the candidate)

Surface 1-3 candidates ranked by leverage. Ask conversationally:

1. *"Erzaehl mir von der Woche. Was hast du 3+ Mal gemacht?"* (Frequenz)
2. *"Etwas was sich manuell, langweilig oder Copy-Paste angefuehlt hat?"* (Toil)
3. *"Etwas wo du dachtest 'das koennte ein guter Praktikant'?"* (Delegation)
4. *"Wenn morgen 500 neue Kunden kaemen, was wuerde zuerst brechen?"* (Bottleneck)
5. *"Was wuerde dir 500 mehr Kunden bringen?"* (Wachstumshebel)

**Output Phase 1:** nummerierte Liste 1-3 Kandidaten, ein-Zeilen-"warum-Hebel" pro Kandidat. Frage: *"Welcher davon? Pick einen."*

### Phase 2 — Method Interview (scope one)

User waehlt einen Kandidaten. Walk the 5-step Method:

**Step 1 — Constraint finden.** Welcher Bottleneck wird geloest, oder welcher Wachstumshebel geoeffnet?

**Step 2 — EAD: Eliminate / Automate / Delegate.**
- **Eliminieren zuerst:** *"Was passiert wenn wir's einfach lassen?"* Wenn "nichts bricht" → Skill exits cheerfully. Win, log to Session-Log, stop.
- **Automatisieren zweitens:** 60/30/10 Framing — ~60% deterministisch, ~30% AI-assistiert, ~10% manuell.
- **Delegieren drittens:** zu komplex/variabel → schlag Hire vor (an Nolan).

**Step 3 — Prozess mappen.** Fuenf Elemente:
- Trigger (was startet es)
- Datenquellen (woher kommt Info)
- Datentransformationen (wie aendert sich Info)
- Entscheidungspunkte (wo verzweigt es)
- Ziel (wo geht der Output hin)

Wenn der User ≥3 dieser fuenf nicht artikulieren kann: *"Wenn du's nicht einer Person erklaeren kannst, kannst du's auch keiner AI erklaeren. Skizzier's auf Papier, dann komm zurueck."* Skill stoppt.

**Step 4 — Autonomie-Level.**

| Level | Name | Was passiert |
|---|---|---|
| L0 | Manuell | Keine AI |
| L1 | Vorgeschlagen | AI schlaegt vor, Mensch entscheidet jeden Schritt |
| L2 | Entworfen | AI entwirft, Mensch reviewed und editiert |
| L3 | Beaufsichtigt | AI laeuft, Mensch validiert periodisch |
| L4 | Autonom | AI macht End-zu-End |

**Default = niedrigstes Level das das Problem loest.** Push back auf L4 wenn der User nicht erst niedrigere Level gefahren hat.

**Step 5 — KPI binden.** Welche der drei Buckets bewegt das?
- Mehr Kunden
- Mehr Wert pro Kunde
- Weniger Kosten

Plus eine konkrete Metrik (Antwortzeit, Fehlerrate, Conversion, Time-to-Completion). **Wenn der User keinen Bucket + keine Metrik nennen kann, Skill stoppt.** *"Wenn deine Automation keine Zahl bewegt, wozu bauen?"*

**Output Phase 2:** scoped Spec geschrieben in den Session-Log mit allen 5 Antworten + Autonomie-Level + KPI.

### Phase 3 — Machine Handoff (build it)

Frage: *"Wie willst du das ausliefern?"* Optionen, geordnet nach Boring-is-Beautiful:

1. **Prompt-only** — saved prompt template that der User per Hand laeuft. Null Infrastruktur.
2. **SOP** — neue Datei in `Team-Wissen/SOPs/SOP-NNN-...md`. Ein Mensch oder Larry kann's befolgen.
3. **Workflow** — neue Datei in `Team-Wissen/Workflows/WF-NNN-...md`. Multi-Spezialist-Orchestrierung.
4. **Skill** — `.claude/skills/<name>/SKILL.md` mit Frontmatter. Fuer Code-User.
5. **Hire** — Nolan briefed, neuer Spezialist. Letzter Ausweg, wenn dauerhafte Verantwortung.

**Default selected = niedrigste Komplexitaet die das Problem loest.** User muss explizit hoehere Komplexitaet waehlen.

Once chosen, write the artifact inline:
- Template schreiben mit Frontmatter, Struktur, ggf. Verweise auf existierende SOPs/Skills
- Speichern am richtigen Ort
- In passendem `INDEX.md` eintragen

## Output contract

Jede `/level-up` Sitzung produziert:

1. **Einen Session-Log-Eintrag** in `Team-Wissen/Session-Logs/YYYY/MM/YYYY-MM-DD-level-up-<thema>.md` mit Method-Spec
2. **Einen Liefergegenstand** — Prompt, SOP, Workflow, Skill, oder Nolan-Hire-Briefing
3. **Eine ein-Bildschirm-Schluss-Notiz** — was gescoped, was gebaut, naechster Schritt

## Critical implementation rules

1. **Eine Sitzung = ein Liefergegenstand.** Keine multi-Kandidat-Planung.
2. **Mindset zuerst, immer.** Auch wenn User mit fertiger Idee kommt — kurz validieren.
3. **EAD enforced "eliminate first".** Wenn die Antwort Eliminate ist, exit cheerfully — das ist ein Win.
4. **Default zum niedrigsten Autonomie-Level.** Push back auf L4.
5. **KPI ist Pflicht.** Wenn User Bucket+Metrik nicht nennt, Skill stoppt.
6. **Read-only auf User-Files except Session-Log und neuer Artifact.**