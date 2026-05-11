<!--
AI OS v0.2.0 — © 2026 Gerald Eder · UmsatzAI
Licensed under MIT — see LICENSE
-->

# Installation — 5-Minuten-Setup

Diese Anleitung führt Sie durch die Erstinstallation von AI OS für Ihr Team.

## Voraussetzungen

| Was | Wofür | Wo bekommen |
|---|---|---|
| Claude Team Plan ($25/Mitarbeiter/Monat) | Org-Skills, geteilte Konfiguration | [claude.com/pricing](https://claude.com/pricing) |
| Claude Cowork Desktop App | Für nicht-technische Mitarbeiter | [anthropic.com/product/claude-cowork](https://www.anthropic.com/product/claude-cowork) |
| Cloud-Sync (Dropbox/GDrive/OneDrive) | Ordner zwischen Mitarbeitern teilen | Was Ihre Firma schon nutzt |
| Optional: Claude Code in VS Code | Für Founder/Devs | [Claude Code](https://claude.com/code) |

---

## Schritt 1 — Repo herunterladen

### Option A: Als ZIP (für Nicht-Techniker)

1. Gehen Sie auf https://github.com/edgeglobal/agentic-os
2. Klicken Sie **Code** → **Download ZIP**
3. Entpacken Sie die ZIP-Datei
4. Benennen Sie den Ordner um nach Ihrem Firmennamen, z.B. `acme-os` oder `mein-business-os`

### Option B: Mit git (für Techniker)

```bash
git clone https://github.com/edgeglobal/agentic-os.git mein-business-os
cd mein-business-os
rm -rf .git  # Wenn Sie keinen eigenen git-Workflow wollen
```

---

## Schritt 2 — In Sync-Ordner verschieben

Verschieben Sie den Ordner in Ihren Cloud-Sync:

**Dropbox:**
```
~/Dropbox/mein-business-os/
```

**Google Drive (Shared Drive):**
```
~/Library/CloudStorage/GoogleDrive-<account>/Geteilte Ablagen/MeinBusiness/mein-business-os/
```

**OneDrive:**
```
~/OneDrive/MeinBusiness/mein-business-os/
```

**Wichtig:** Alle Mitarbeiter, die Zugriff haben sollen, müssen den Cloud-Ordner abonniert haben. In Dropbox: rechtsklicken → "Mit Personen teilen". In GDrive: Shared Drive einrichten und Mitarbeiter einladen.

---

## Schritt 3 — Claude Cowork installieren

1. Laden Sie Cowork herunter von [anthropic.com/product/claude-cowork](https://www.anthropic.com/product/claude-cowork)
2. Installieren Sie auf Mac oder Windows
3. Loggen Sie sich mit Ihrem Team-Plan-Account ein
4. Klicken Sie **Open Folder** → wählen Sie Ihren `mein-business-os` Ordner

Cowork zeigt jetzt auf den Ordner. Alle Inhalte sind sichtbar und durchsuchbar.

---

## Schritt 4 — AI initialisieren

In Cowork (oder Claude Code) geben Sie ein:

> **Initialisiere dich in diesem Ordner.**

Die AI liest `AGENTS.md` und meldet sich:

> "Ich bin die KI in deinem Agentic OS. Bereit für deine Anweisung."

---

## Schritt 5 — Onboarding-Wizard starten

Sagen Sie zur KI:

> **Lass uns Agentic OS einrichten.**

Die KI stellt 7 Fragen über Ihre Firma:

1. Wer seid ihr, was verkauft ihr, an wen?
2. Was sind eure 2-3 wichtigsten Prioritäten für die nächsten 90 Tage?
3. Wo läuft Umsatz tatsächlich rein?
4. Wo redet ihr mit Kunden/Team?
5. Wo leben Meetings, Notizen, Dokumente?
6. Was ist der eine Task, der eure Woche frisst?
7. Bitte fügt 1-2 Beispiele eurer Schreibweise ein (E-Mail, LinkedIn-Post)

Aus den Antworten füllt die KI automatisch:

- `01-Firma Home/brand.md` (eure Schreibweise)
- `01-Firma Home/wunschkunde-icp.md` (ICP)
- `01-Firma Home/organization.md` (Angebot)
- `01-Firma Home/strategy.md` (Ziele, Prioritäten)
- `01-Firma Home/stakeholder.md` (externe Partner, Schlüsselpersonen)
- `04-Mitarbeiter/team-mitglieder.md` (wer ihr seid)
- `Team-Wissen/Session-Logs/2026/MM/2026-MM-DD-onboarding.md`

---

## Schritt 6 — Org-Skills hochladen (für Owner)

Wenn Sie auf Claude Team Plan sind, können Sie Skills für alle Team-Mitglieder zentral verteilen:

1. Loggen Sie sich auf [claude.com](https://claude.com) ein
2. Gehen Sie zu **Settings** → **Skills**
3. Laden Sie die Skills aus `.claude/skills/` als ZIP hoch:
   - `audit` — 4 C's Audit
   - `onboard` — KMU-Onboarding-Wizard
   - `level-up` — Wöchentliches Verbesserungs-Ritual
   - `neuer-kunde` — Neuen Kunden anlegen
   - `session-abschluss` — Session-Log schreiben

Alle Team-Mitglieder sehen die Skills automatisch in Cowork und Code.

---

## Schritt 7 — Mitarbeiter onboarden

Für jeden neuen Mitarbeiter:

1. Mitarbeiter zum Claude Team Plan einladen (über Settings → Members)
2. Mitarbeiter installiert Cowork Desktop und loggt sich ein
3. Mitarbeiter öffnet den Sync-Ordner (`~/Dropbox/mein-business-os/`)
4. Mitarbeiter sagt zur KI: **"Ich bin neu im Team. Onboarde mich."**
5. Die KI fragt nach Namen, Rolle, Team
6. Die KI trägt den Eintrag in `04-Mitarbeiter/team-mitglieder.md` ein
7. Die KI ergänzt das Team-Mitglied in `02-Teams/<team>/kontext.md`
8. Die KI fragt optional: "Gibt es etwas wie Claude mit dir reden soll (Tonfall, Anrede)?" — landet als Notiz in der Präferenz-Spalte des Rosters

Kein separater Mitarbeiter-Folder. Persönliche Präferenzen leben im Roster, nicht in eigenen Files. Begründung: Brand-Voice ist firmenweit, persönliche Sub-Folder pro Person sind für KMU Overkill.

Voller SOP: [[SOP-001-neuen-mitarbeiter-onboarden]]

---

## Schritt 8 — Tägliche Nutzung

Beispiele was Mitarbeiter ab jetzt machen können:

| Aufgabe | An die KI sagen |
|---|---|
| Meeting-Protokoll schreiben | "Ich hatte gerade ein Meeting mit [Kunde]. Hier die Stichpunkte: ..." |
| Neuen Kunden anlegen | "Wir haben einen neuen Kunden gewonnen: Acme GmbH" |
| Angebot vorbereiten | "Erstelle ein Angebot für [Kunde] basierend auf unserem Standardangebot" |
| LinkedIn-Post entwerfen | "Schreib einen LinkedIn-Post zum Thema X in unserem Stil" |
| Wochen-Review | "Mach mir einen Review der letzten Woche" |

---

## Häufige Probleme

### "Cowork findet die Skills nicht"

→ Prüfen Sie: Sind Sie auf Claude Team Plan (nicht Pro)? Hat der Owner die Skills in der Admin-Konsole hochgeladen?

### "Sync-Konflikte in Dropbox"

→ Wenn zwei Mitarbeiter gleichzeitig dieselbe Datei editieren, kann es Konflikt-Files geben. Best Practice:
- Editieren Sie nicht parallel dieselbe Datei
- Nutzen Sie `git`-Workflow wenn das Team größer wird (≥10 MA)

### "Wo gehören persönliche Files vs. Firmen-Files hin?"

→ Drei einfache Regeln:
- **Persönliches** (eigene Tone of Voice, Memory, About-me) → `04-Mitarbeiter/<dein-name>/`
- **Team-Sachen** (Prozesse, Skills die alle im Team nutzen) → `02-Teams/<dein-team>/`
- **Firma-weit** (Markenstimme, Wunschkunden, Strategie) → `01-Firma Home/`

Permissions setzen Sie pro Sub-Folder im Cloud-Provider — nicht durch separate Folder-Wurzeln.

### "Die KI kennt unser Geschäft nicht"

→ Prüfen Sie: Wurde der Onboarding-Wizard durchlaufen? Sind `01-Firma Home/brand.md`, `wunschkunde-icp.md`, `organization.md` ausgefüllt?

### "Wir brauchen einen Spezialisten, den es nicht gibt"

→ Sagen Sie zur KI: "Wir brauchen einen [Rolle]. Hire ihn." Die KI fragt nach was genau gebraucht wird und schlaegt einen passenden Workflow vor.

---

## Hilfe & Support

- **Dokumentation:** Alle SOPs leben in `Team-Wissen/SOPs/`
- **Custom Setup für Ihr Team:** [umsatzai.com](https://umsatzai.com) — Setup, Training, Pflege
- **Issues melden:** [GitHub Issues](https://github.com/edgeglobal/agentic-os/issues)
- **Updates:** `git pull` (wenn mit git geklont) oder neues ZIP herunterladen

---

**Built with care by Gerald Eder · [UmsatzAI](https://umsatzai.com) · 2026**
