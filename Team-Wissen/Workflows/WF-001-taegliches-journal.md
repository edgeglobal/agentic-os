# WF-001 — Tägliches Journal

**Wofür:** Tagesabschluss / Reflektion. User sagt am Ende des Tages was er gemacht hat, Penn schreibt einen strukturierten Eintrag.
**Auslöser:**
- User sagt "wie war heute?", "was hab ich gemacht?", "tagesabschluss", "journal heute"
- User wirft Stichpunkte rein: "Heute mit Acme telefoniert, dann Pricing-Doc fertig, dann Recruiting-Call mit Anna"

**Verantwortlich:** Larry (Orchestrator) → Penn (Schreiber)
**Dauer:** ~2 Minuten

---

## Schritte

### 1. Larry fragt klärend

Wenn der Input dünn ist:
- "Mit wem hattest du heute Meetings?"
- "Welche Entscheidungen hast du heute getroffen?"
- "Was war die wichtigste Erkenntnis heute?"

### 2. Larry brief Penn

> "Penn, schreib einen Tagesabschluss-Eintrag für heute. Hier die Stichpunkte: [...]. Bezug auf [[Kunde]] und [[Projekt]] wenn passend."

### 3. Penn extrahiert und strukturiert

Penn identifiziert:
- **Erwähnte Personen** → Cross-Links zu `03-Kunden/`, `05-Team/`
- **Erwähnte Projekte** → Cross-Links zu `04-Projekte/`
- **Entscheidungen** → in `Team-Wissen/INDEX.md` Cross-Session-Lerneffekte ergänzen wenn wichtig
- **Action Items** → klar herausstellen mit Verantwortlich + Deadline
- **Insights** → in eigene Sektion

### 4. Penn schreibt den Eintrag

**WICHTIG:** Tagesabschlüsse leben NICHT in einem `Journal/`-Ordner (Agentic OS ist Business-Vault, kein Personal-PKM). Stattdessen:

- **Wenn fast alles um einen Kunden ging:** anhängen an `03-Kunden/<kunde>/notizen.md` mit Datums-Header
- **Wenn fast alles um ein Projekt ging:** anhängen an `04-Projekte/<projekt>/_hub.md` Aktivitäts-Sektion
- **Wenn quergeschnitten:** als Session-Log `Team-Wissen/Session-Logs/YYYY/MM/YYYY-MM-DD-tagesabschluss.md`

Penn entscheidet je nach Inhalt. Bei Unsicherheit → fragt Larry, Larry fragt User.

### 5. Penn liefert zurück

Penn übergibt an Larry: "Eintrag geschrieben in [Pfad]. Kernpunkte: [3-Bullet-Zusammenfassung]. Cross-Links: [Liste]. Action Items für morgen: [Liste]."

### 6. Larry synthesiert für User

> "Erledigt. Heute war hauptsächlich [X], die wichtigste Entscheidung war [Y]. Action Items für morgen: [Liste]. Eintrag liegt in [Pfad]."

### 7. Optional: Action Items in Notion (wenn integriert)

Wenn User ein Notion/ClickUp/Asana hat: Larry kann die Action Items dort als Tasks anlegen (über entsprechende MCP-Connection).

---

## Output

- Mind. 1 Datei aktualisiert/angelegt (je nach Routing)
- Action Items im Klartext für den User
- Cross-Links gesetzt

## Referenzen

- [[meeting-protokoll]]
- [[Team/Penn - Schreiber/AGENTS]]
