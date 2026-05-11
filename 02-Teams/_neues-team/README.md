<!--
AI OS — Agentic Operating System für KMUs
© 2026 Gerald Eder · MIT License
-->

# Team-Folder Vorlage

Ein Team-Folder ist eine **Mini-Firma** mit eigener Identitaet, eigenen Prozessen und eigenen Outputs. Die Struktur ist immer gleich, der Inhalt team-spezifisch.

## Aufbau

```
02-Teams/<team-name>/
├── README.md                  ← diese Datei (oder team-spezifisch angepasst)
├── kontext.md                 ← Pflicht: Wer wir sind, Tools, Regeln, Glossar
├── vorlagen/                  ← Standard: team-spezifische Output-Templates
│   └── (z.B. angebot.md, follow-up-mail.md)
├── projekte/                  ← Standard: laufende Team-Projekte
│   ├── _neues-projekt/        ← Projekt-Sub-Vorlage
│   └── (z.B. webrelaunch-acme/, lieferanten-audit-q2/)
├── referenzen/                ← Standard: team-spezifisches Wissen
│   └── (z.B. wettbewerber-analyse.md, prozess-doku.md)
├── meetings/                  ← Standard: team-interne Meetings (Standups, Reviews)
│   └── YYYY/MM/YYYY-MM-DD-<thema>.md
├── ablage/                    ← Standard: fertige Team-Outputs
│   └── (z.B. quartalsberichte/, praesentationen/)
└── .claude/skills/            ← Pflicht: team-spezifische Skills
    └── (z.B. /angebot-entwurf, /reklamations-erstantwort)
```

## Pflicht / Standard / Optional

- **Pflicht:** `kontext.md` + `.claude/skills/` — jedes Team braucht das
- **Standard:** `vorlagen/`, `projekte/`, `referenzen/`, `meetings/`, `ablage/` — vorbefuellt, kann angepasst oder bei Nichtbedarf geloescht werden
- **Team-spezifische Sub-Container:** jedes Team kann eigene Sub-Folder anlegen wenn sinnvoll. Beispiele: Marketing hat `website/`, Fulfillment koennte `lager/` haben, Finance koennte `buchhaltung/` haben. Frei waehlbar.

## Was wo lebt

**`kontext.md`:** Wer ist im Team, welche Tools, welche Regeln, Glossar. Die KI liest das bei jeder Team-bezogenen Anfrage.

**`vorlagen/`:** Output-Templates die nur dieses Team nutzt. Z.B. `angebot.md` fuer Vertrieb, `rechnung.md` fuer Finance.

**`projekte/`:** Team-Initiativen die ueber Wochen laufen. Pro Projekt ein Sub-Folder aus `_neues-projekt/` dupliziert.

**`referenzen/`:** Team-spezifisches Wissen — Wettbewerber-Analysen, Prozess-Doku, Studien, interne Anleitungen. Nicht firmenweit relevant.

**`ablage/`:** Fertige Team-Outputs die andere Teams oder die Geschaeftsfuehrung einsehen. Quartalsberichte, Strategiepapiere.

**`.claude/skills/`:** Team-spezifische Workflows als Skills. Marketing hat `/linkedin-post`, Vertrieb hat `/angebot-entwurf`, Finance hat `/beleg-klassifizierung`.

## Was nicht ins Team-Folder gehoert

- **Externe Firmen** → `03-CRM/Unternehmen/`, Team verweist per Wikilink
- **Externe Personen** → `03-CRM/Personen/`
- **Mitarbeiter-Roster** → `04-Mitarbeiter/team-mitglieder.md` (firmenweit)
- **Firmenweite Vorlagen** (z.B. Meeting-Protokoll) → `03-CRM/Meetings/_protokoll-vorlage.md`
- **Firmenweite Projekte mit mehreren Teams** → `01-Firma Home/projekte/`
- **Externe Meetings** (mit Unternehmen oder Personen) → `03-CRM/Meetings/`
- **Interne Meetings** des Teams (Standups, Reviews) → `meetings/` hier im Team-Folder

## Neues Team anlegen

1. `_neues-team/` duplizieren, mit Funktionsname umbenennen (z.B. `produktion/`, `it/`, `kundenservice/`)
2. `kontext.md` ausfuellen oder `/onboard` Skill im Modus "Team" nutzen
3. Permissions im Cloud-Sync setzen (Team-Mitglieder schreiben, Rest liest)
4. Nicht benoetigte Sub-Folder (z.B. `referenzen/`) loeschen oder leer lassen
