<!--
AI OS — Agentic Operating System für KMUs
© 2026 Gerald Eder · UmsatzAI · MIT License
-->

# 02-Teams/

Pro Funktions-Team ein Sub-Folder mit team-spezifischem Kontext, Prozessen und Skills. So weiss die KI was in welchem Team passiert und kann Team-spezifische Workflows nutzen.

## Default-Teams (mitgeliefert)

```
02-Teams/
├── README.md                        ← diese Datei
├── _neues-team/                     ← Vorlage zum Duplizieren
├── marketing-vertrieb/              ← Kunden gewinnen & halten
├── fulfillment/                     ← Auftraege abwickeln & liefern
└── finance-hr-admin/                ← Buchhaltung, Personal, Office
```

Die drei Default-Teams decken die typischen Funktionen im KMU ab. Wenn ihr eines nicht braucht (z.B. kein Fulfillment in einer Beratung): einfach loeschen. Wenn ihr mehr braucht: aus `_neues-team/` duplizieren.

## Pro Team

Jeder Team-Folder enthaelt:

```
<team-name>/
├── kontext.md                       ← was macht das Team, mit welchen Tools, welche Regeln
├── README.md                        ← kurze Beschreibung
└── .claude/skills/                  ← Team-spezifische Skills
    └── (z.B. /angebot-entwurf, /lead-qualifizierung)
```

## Wenn ihr ein neues Team anlegt

1. `_neues-team/` duplizieren, mit Team-Name umbenennen (z.B. `produktion/`, `it/`, `kundenservice/`)
2. Im neuen Folder: `kontext.md` ausfuellen oder `/onboard` Skill im Modus 'Team' nutzen
3. Permissions im Cloud-Sync setzen: Team-Mitglieder schreiben, Rest liest

## Wer schreibt was

| Was | Wer darf editieren |
|---|---|
| `<team>/kontext.md` | Team-Verantwortlicher |
| `<team>/.claude/skills/` | Team-Verantwortlicher nach Review |
| `<team>/README.md` | Team-Verantwortlicher |

In Google Drive / OneDrive / Dropbox einstellen ueber Datei-Freigabe pro Sub-Folder.

## Verhaeltnis zu 04-Mitarbeiter/

- **04-Mitarbeiter/** = WER. Pro Person ein Folder.
- **02-Teams/** = WAS macht eine Funktion. Pro Funktion ein Folder.
- Verknuepfung ueber `team-mitglieder.md` und Eintraegen in `kontext.md` der Teams (Liste der Mitglieder).
