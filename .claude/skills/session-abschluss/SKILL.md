---
name: session-abschluss
description: Use when the user says "schliess die session ab", "session abschluss", "wickle ab", "wir machen schluss", "save session", "close session", or signals end-of-day. Writes a session log, runs the librarian pass (SSOT, broken links, orphans, missing index entries), and prints a one-screen summary.
---

## What this skill does

Performs the two end-of-session duties:

1. **Bibliothekar-Pass** — scan vault for structural drift, fix what can be fixed, flag what can't.
2. **Session-Log Author** — write `Team-Wissen/Session-Logs/YYYY/MM/YYYY-MM-DD-<slug>.md` capturing decisions, realignments, deltas, and cross-links to prior logs.

Append-only memory layer. Replaces unreliable AI auto-memory.

## Execution

### Step 1: Bibliothekar-Pass

Scan the vault (read-only, except for safe fixes):

**A. SSOT-Verletzungen (Duplikate)**
Use Grep to find facts that appear in multiple files. Heuristics:
- Gleiche Zahl/Euro-Betrag in 2+ Dateien wo eine Datei das kanonische Zuhause ist
- Gleiche Personen-Kontakt-Info in 2+ Dateien
- Gleiche Produkt-/Leistungs-Beschreibung in 2+ Dateien

For each violation:
- Pick canonical home (autoritativste Datei: `01-Firma Home/*` for business facts, `03-Unternehmen/<x>/_hub.md` for customer facts, `05-Team/<x>/_hub.md` for team facts)
- Replace duplicate with `[[wikilink]]`
- Note the change in the upcoming session log

**B. Broken Wikilinks**
Use Grep to find `[[...]]` links and check each target file exists.

For each broken link:
- If intent clear: create stub at target path with frontmatter `status: stub` and a placeholder note
- If intent unclear: flag in session log for user to resolve

**C. Verwaiste Dateien**
Find files in `01-Firma Home/`, `Team-Wissen/`, `02-Vorlagen/` that have:
- No incoming `[[wikilink]]` from anywhere
- No entry in their section's `INDEX.md` (if applicable)

For each orphan:
- Add to relevant `INDEX.md` if section has one
- Flag in session log if cannot place

**D. Fehlende INDEX-Eintraege**
Compare files in each section to its `INDEX.md` listing.

For each missing entry:
- Add a one-line entry with `[[wikilink]]` to the file

### Step 2: Session-Log schreiben

Determine the slug:
- Read recent conversation context
- Identify the main theme (what dominated this session?)
- Slug: kebab-case, 2-4 words. Examples: `onboarding-und-setup`, `acme-kickoff-vorbereitung`, `q3-pricing-strategie`, `tagesabschluss`

Determine the path:
- `Team-Wissen/Session-Logs/YYYY/MM/YYYY-MM-DD-<slug>.md`
- If `YYYY/` or `YYYY/MM/` doesn't exist, create it

Read the most recent prior session log (one back) to enable cross-linking.

Write the log with these sections (Frontmatter, Aktive Tasks, Was wir gemacht haben, Was der User korrigiert/realigned hat, Entscheidungen, Deltas vs vorheriger Plan, Bibliothekar-Pass Strukturelle Fixes, Geflaggt fuer User-Klaerung, Cross-Links, Naechste Session sollte zuerst).

Beispiel-Schema:

- `type: session-log`, `date: YYYY-MM-DD`, `slug: <slug>`, `prior-log: [[<prior-slug>]]` oder `none`
- Aktive Tasks als Checkboxes (abgehakt = erledigt, leer = offen)
- 3-7 Bullets fuer "Was wir gemacht haben", hoechste Ebene, keine Details
- User-Realignments WOERTLICH erfassen wenn moeglich — das sind die wertvollsten Lerneffekte
- Entscheidungen mit Begruendung
- Bibliothekar-Pass-Fixes auflisten (X SSOT-Konflikte, X broken Links, X Orphans)
- Naechste-Session-Hinweise (1-3 Bullets)

### Step 3: Update Cross-Session-Lerneffekte

If the session produced an insight worth remembering across sessions (a User-Realignment that's a new rule, a recurring pattern):
- Append to `Team-Wissen/INDEX.md` Cross-Session-Lerneffekte section
- Format: `- YYYY-MM-DD: <Lerneffekt> ([[Session-Log]])`

### Step 4: Print Schluss-Notiz

One screen. Format:

```
✓ Session abgeschlossen.

Log: Team-Wissen/Session-Logs/YYYY/MM/YYYY-MM-DD-<slug>.md

Bibliothekar-Pass:
- X SSOT-Konflikte konsolidiert
- X broken Links gefixt
- X Orphans in INDEX eingetragen
- X Issues fuer dich geflaggt

Offene Tasks fuer naechste Session:
- <Task 1>
- <Task 2>

Bis naechste Session — sag einfach was du brauchst.
```

## Critical rules

1. **Append-only auf Session-Logs.** Niemals einen alten Log modifizieren — neue Sessions = neue Datei.
2. **Bibliothekar-Pass conservative.** Nur fixen wenn 100% sicher. Bei Zweifel — flaggen.
3. **Cross-Link minimum.** Mindestens prior-log und neu-erstellte-Dateien. Mehr ist besser.
4. **User-Realignments woertlich.** Diese sind der wertvollste Inhalt — formuliere nicht um.
5. **Auto-create der Datums-Ordner.** YYYY/MM erstellen wenn nicht da.
6. **Privacy.** Bei sensitiver Branche im Session: Session-Log kennzeichnen `privacy: sensitive` im Frontmatter.