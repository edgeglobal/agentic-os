# SOP-001 — Neuen Mitarbeiter onboarden

**Wofuer:** Wenn jemand neu im Team startet.
**Ausloeser:** User sagt "neuer Mitarbeiter: [Name] als [Rolle]" oder "Max faengt am ... an".
**Verantwortlich:** Die KI fuehrt durch, Operator/HR signt off.
**Dauer:** 10-15 Minuten interaktiv.

---

## Schritte

### 1. Stammdaten erfassen

Die KI fragt (max 3 Fragen pro Block):

- **Vollstaendiger Name + bevorzugter Vorname?**
- **Position / Rolle in einem Satz?**
- **Hauptteam?** (eines von `02-Teams/<team>/`)
- **Mail im Unternehmen?** (optional)
- **Startdatum?**
- **Direkter Vorgesetzter?** (Wikilink falls schon im Roster)

### 2. Eintrag im Roster

Schreibe neue Zeile in `04-Mitarbeiter/team-mitglieder.md`. Es gibt **keinen Sub-Folder pro Person** — Praeferenzen leben als Spalten im Roster.

Spalten (Standard): Name, Rolle, Team, Mail, Start, Manager, optional Anrede/Tonfall.

### 3. Tool- & Zugangs-Checkliste

Die KI gibt der User eine Action-Liste fuer technische Setups:

- [ ] AI-Tool-Zugang (Claude / Codex / Gemini, je nach Stack)
- [ ] Cloud-Storage-Zugang (Permission auf relevante Sub-Folder dieses Vaults)
- [ ] Mail-Account
- [ ] Chat (Slack / Teams)
- [ ] CRM / ERP / Tool-spezifisch — siehe `01-Firma Home/tools.md`
- [ ] Optional Team-spezifische Zugaenge — siehe `02-Teams/<team>/kontext.md` Sektion Tools

Diese Liste landet als TODO beim Operator, **nicht als Datei im Vault**.

### 4. Was lesen am Tag 1

Standard-Leseliste (von der KI an den neuen MA verschickbar):

1. `AGENTS.md` — wie der Vault aufgebaut ist
2. `01-Firma Home/organization.md` — was die Firma macht
3. `01-Firma Home/brand.md` — wie wir klingen
4. `01-Firma Home/wunschkunde-icp.md` — fuer wen wir das machen
5. `02-Teams/<team>/kontext.md` — Team-Regeln
6. `Team-Wissen/INDEX.md` — wo SOPs/Workflows/Richtlinien liegen

### 5. Welcome-Message

Die KI entwirft eine 5-10-Zeilen-Welcome-Message in [[brand]]-Stil. Inhalt:

- Begruessung
- Erste 3 Files zum Lesen (siehe Schritt 4)
- Wie man die KI nutzt (Beispiel-Prompt)
- Wer der Buddy / Manager ist

User schickt die Message manuell — die KI postet nichts ins Mail-System.

### 6. Confirmation

Drei-Zeilen-Output:

```
[OK] Mitarbeiter im Roster: 04-Mitarbeiter/team-mitglieder.md
[OK] Welcome-Message ist im Chat — bereit zum Verschicken
TODO Operator: Zugaenge anlegen laut Liste oben
```

---

## Output

- `04-Mitarbeiter/team-mitglieder.md` — neue Zeile

## Referenzen

- [[team-mitglieder]]
- [[brand]]
- [[organization]]
- [[R-001-namenskonventionen]]
