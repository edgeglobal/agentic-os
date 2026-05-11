---
name: onboard
description: Use on Day 1 of an Agentic OS install, when someone says "set me up", "onboard me", "let's get started", "lass uns einrichten", "richte dich ein", "fill in my Agentic OS", or has just cloned the kit. Combined wizard — runs the 7-question intake AND scaffolds the Day-1 file set at the end. Idempotent — re-run any time after editing the knowledge files.
---

## What this skill does

Single combined wizard for new Agentic OS installations. Conducts a 7-question interview about the user's business, then fills `01-Firma Home/markenstimme.md`, `01-Firma Home/unsere-kunden.md`, `01-Firma Home/unsere-leistungen.md`, and `05-Team/team-mitglieder.md` from the answers.

**The wow moment:** at the end, suggest the closing prompt *"Sag mir: woran soll ich diese Woche arbeiten?"* The user runs it once. The AI uses the new knowledge files to give a personalized answer.

## When NOT to run this

- If already onboarded and wants to refresh: run, but skip already-answered questions (idempotent).
- If user wants to add a connection: not onboarding — point at the relevant skill.

## Execution

### Step 1: Check state

Read these files:
- `01-Firma Home/markenstimme.md`
- `01-Firma Home/unsere-kunden.md`
- `01-Firma Home/unsere-leistungen.md`
- `05-Team/team-mitglieder.md`

Check which sections are filled vs. still placeholder.

- **All filled** → skip Step 2, ask user what they want to update.
- **Some filled** → ask: "Ich sehe Q1, Q3, Q4 sind beantwortet. Willst du den Rest jetzt ausfuellen, oder mit dem was da ist scaffolden?" Their call.
- **None filled (fresh clone)** → run Step 2 conversationally.

### Step 2: The interview (7 questions, hard cap)

Ask one at a time. Write each answer to a temporary `00-Inbox/onboarding-intake.md` as you go.

**Q1 — Wer seid ihr, was verkauft ihr, an wen?**
Identity, Angebot, Zielgruppe. Ein Absatz pro Teil.

**Q2 — Bitte fuegt 1-2 Beispiele eurer Schreibweise ein. Nicht editieren — Original einfuegen.**
*This is the only question with a hard rule.* Voice samples MUST be pasted, not typed mid-conversation. If the user types fresh prose, refuse:

> *"Stop — bitte einfuegen, nicht tippen. Wenn du es im Chat tippst, ist das Sample bereits durch unser Gespraech geformt. Oeffne deinen letzten LinkedIn-Post oder eine Kunden-E-Mail in einem anderen Tab und fuege unbearbeitet ein."*

Ask for two samples. Eine E-Mail, ein Post. Oder zwei vom selben Typ.

**Q3 — Was sind eure 2-3 wichtigsten Prioritaeten fuer die naechsten 90 Tage?**
Quartals-Prioritaeten. Push back wenn sie sagen "Wachstum". Lass sie konkret werden — Zahl, Deadline, oder Liefergegenstand.

**Q4 — Wo laeuft Umsatz tatsaechlich rein, und wo wird er getracked?**
Mehrere Antworten OK. Beispiele: Stripe, Lexoffice, DATEV, GHL, Notion-Tabelle, Excel.

**Q5 — Wo redet ihr mit Kunden, eurem Team, der Aussenwelt im Tagesgeschaeft?**
Email (Gmail/Outlook), Slack/Teams/Discord, DMs. Wo laeuft was?

**Q6 — Wo leben Meeting-Aufnahmen, Notizen, wichtige Dokumente?**
Granola, Otter, Fireflies, Zoom-Cloud, Notion, Drive, Dropbox, Confluence?

**Q7 — Was ist der eine Task, der eure Woche frisst, und wo trackt ihr Aufgaben?**
Top Pain (fuer `/level-up` spaeter) + Tool fuer Task-Tracking (ClickUp, Asana, Linear, Notion, Trello).

### Step 3: Frag nach dem Team

Optional 8. Frage: "Wer ist sonst noch im Team? Name + Rolle reicht."

Schreib alle in `05-Team/team-mitglieder.md` Tabelle.

### Step 4: Scaffold the Day-1 file set

Once intake complete, generate these files (or update if re-running). Back up originals to `99-Archiv/intake-{YYYY-MM-DD-HHMM}/` if they exist.

1. **`01-Firma Home/markenstimme.md`** — from Q1 (Identitaet) + Q2 (Beispiele). Beispiele woertlich einfuegen mit Header "Beispiel-Texte". Tonalitaets-Adjektive aus den Beispielen ableiten und im Tonalitaets-Block als Vorschlag stellen. Tabu-Woerter / Lieblings-Woerter erstmal leer lassen.

2. **`01-Firma Home/unsere-kunden.md`** — from Q1 (Zielgruppe). Eine Persona ausarbeiten basierend auf was der User gesagt hat. Pain Points / Wuensche / Anti-Persona als Stub mit "Bitte ergaenzen".

3. **`01-Firma Home/unsere-leistungen.md`** — from Q1 (Angebot) + Q4 (Umsatzkanaele). Leistungs-Liste mit Platzhalter-Preisen wenn nicht genannt.

4. **`05-Team/team-mitglieder.md`** — Tabelle mit allen genannten Personen.

5. **`Team-Wissen/Session-Logs/YYYY/MM/YYYY-MM-DD-onboarding.md`** — Initialer Session-Log mit den 7 Antworten und allen erstellten Dateien.

### Step 5: The closing screen

Print one screen. Three lines max:

```
✓ Tag 1 erledigt. Agentic OS kennt euch jetzt.

Heute: frag mich — "woran soll ich diese Woche arbeiten?"
Morgen: Org-Skills im Claude Team Admin-Konsole hochladen (.claude/skills/* als ZIP).
Tag 7: lauf /audit um euren 4 C's Score zu sehen.
```

When the user runs the closing prompt, respond using only the new knowledge files:
- 3-bullet Prioritaeten-Liste, in ihrer Markenstimme aus Q2
- Jeder Bullet bezieht sich auf eine 90-Tage-Prioritaet aus Q3
- Letzte Zeile: *"Wenn ich fuer Montag eine Sache waehlen muesste, waere es [X]. Soll ich den ersten Email-Entwurf machen?"*

## Critical implementation rules

1. **The 7-question cap is non-negotiable.** Don't add Q8 mid-conversation.
2. **Voice paste cannot be skipped.**
3. **One-shot scaffold.** After Step 2, write Step 3-4 files in a single batch.
4. **Idempotent.** Re-running with edited intake refreshes knowledge files; backs up originals.
5. **Closing screen is three lines.** Not a menu.
6. **No extra skills generated.** The kit ships 5 skills.
7. **No `.env` writes.** Don't ask for API keys on Day 1.