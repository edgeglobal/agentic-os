# SOP-004 — Inbox verarbeiten

**Wofuer:** `00-Inbox/` regelmaessig auf 0 bringen — keine Notizen, Voice-Memos, Anhaenge oder Schnipsel mehr im Drop-Folder.
**Ausloeser:** "Verarbeite die Inbox", "Raeum die Inbox auf", oder als wiederkehrender Termin (z.B. Freitag-Nachmittag).
**Verantwortlich:** Die KI sortiert, der User entscheidet bei Unsicherheit.
**Dauer:** 5-15 Minuten je nach Volumen.

---

## Schritte

### 1. Inbox scannen

Die KI listet alle Files in `00-Inbox/`:

- Filename
- Erste 1-3 Zeilen Inhalt
- Filetyp (Markdown, Bild, PDF, Audio-Transkript)
- Datum erstellt

Bei Voice-Memos oder Audio: KI fragt ob es schon transkribiert ist. Wenn nein: User soll transkribieren bevor weitergeht.

### 2. Pro File: 4-D-Klassifikation

Fuer jedes File eine der vier Entscheidungen:

**Delete** — keine Relevanz mehr (Dubletten, Schmierzettel, ueberholte Notizen).
Aktion: nach `99-Archiv/inbox-cleanup/YYYY-MM-DD/` verschieben (nicht direkt loeschen — Sicherheits-Netz).

**Defer** — relevant, aber Bearbeitung jetzt nicht moeglich (z.B. wartet auf Info).
Aktion: in `00-Inbox/_warten/` mit Datums-Praefix `YYYY-MM-DD-` lassen, Notiz im Chat ueber Wartegrund.

**Delegate** — gehoert in den Vault, aber an einen anderen Ort.
Aktion: Routing-Regeln unten anwenden.

**Do** — eine kurze Aktion (< 2 Min) erledigt es.
Aktion: sofort tun (z.B. Wikilink in `03-CRM/Unternehmen/<firma>/kontext.md` einfuegen) und File loeschen.

### 3. Routing-Regeln fuer "Delegate"

| Inhalt | Zielort |
|---|---|
| Info ueber einen Kunden | `03-CRM/Unternehmen/<firma>/kontext.md` (eingearbeitet) oder neuer Meeting-Eintrag |
| Info ueber eine Person | `03-CRM/Personen/<name>/kontext.md` |
| Idee / Insight / Inspiration | `Team-Wissen/INDEX.md` Sektion "Insights", oder thematischer Folder in `Team-Wissen/Richtlinien/` |
| Wiederkehrende Aufgabe entdeckt | Vorschlag eine **neue SOP** in `Team-Wissen/SOPs/` anzulegen |
| Branchen-Wissen / Artikel | `Team-Wissen/` oder team-spezifisch `02-Teams/<team>/referenzen/` |
| Persoenliche Aufgabe | bleibt bei User (TodoList / Kalender / Tag-Plan — **nicht im Vault**) |
| Sensitive Daten (Passwoerter, IDs) | Loeschen, User informieren wo es hingehoert (Passwort-Manager etc.) |

### 4. Pro "Delegate"-File: Confirmation

Die KI zeigt fuer jedes geroutete File:

```
[Filename] -> [Zielort]
   Was passiert: [Eingearbeitet / Verschoben / Ergaenzt um Backlink]
```

Bei Unsicherheit fragt sie 1x: "Routing X korrekt, oder anders?"

### 5. Abschluss-Report

```
Inbox-Cleanup Report:
- Bearbeitet: N Files
- Deleted: N
- Deferred: N (warten in 00-Inbox/_warten/)
- Delegated: N (verteilt im Vault)
- Done: N (Quick-Aktionen)

Inbox-Status: [X Files uebrig | leer]
Vorschlaege fuer neue SOPs: [Liste falls Patterns aufgetaucht]
```

---

## Output

- `00-Inbox/` auf 0 oder nur noch `_warten/`-Inhalte
- Backlinks und Eintraege in Ziel-Files
- Optional: 1-3 Vorschlaege fuer neue SOPs

## Referenzen

- [[R-001-namenskonventionen]]
- [[Team-Wissen/INDEX]]
