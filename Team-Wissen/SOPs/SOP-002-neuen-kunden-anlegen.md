# SOP-002 — Neuen Kunden anlegen

**Wofuer:** Wenn ein neuer Kunde gewonnen wurde (Vertrag, LOI, oder erste Beauftragung).
**Ausloeser:** User sagt "neuer Kunde: [Firma]" oder "wir haben Acme gewonnen".
**Verantwortlich:** Die KI fuehrt durch, Vertrieb / Account-Lead signt off.
**Dauer:** 10-15 Minuten interaktiv.

---

## Schritte

### 1. Schnellster Weg: `/onboard` Modus 3

In den meisten Faellen reicht der `onboard`-Skill im Modus **Unternehmen**:

> "Onboarde uns einen neuen Kunden: Acme GmbH."

Der Skill stellt 5 Sektionen Fragen, legt `03-CRM/Unternehmen/<slug>/` aus der `_neues-unternehmen/`-Vorlage an und fuellt `kontext.md`. Diese SOP beschreibt den manuellen Pfad falls der Skill nicht verfuegbar ist oder spezielle Felder gebraucht werden.

### 2. Slug bestimmen

Filename-Format: kebab-case, **ohne Rechtsform**.

- `Acme GmbH` -> `acme`
- `Mueller & Sohn KG` -> `mueller-und-sohn`
- Bei Namens-Kollision: kurzer Branchen-Zusatz (`acme-baeckerei`, `acme-software`).

Konvention siehe [[R-001-namenskonventionen]].

### 3. Folder anlegen

```
03-CRM/Unternehmen/<slug>/
└── kontext.md
```

Kopiere `03-CRM/Unternehmen/_neues-unternehmen/kontext.md` als Startpunkt.

Weitere Files werden bei Bedarf dazu angelegt — **nicht praeventiv leere Folder erzeugen** (`meetings/`, `angebote/` etc. entstehen erst wenn der erste Eintrag kommt).

### 4. `kontext.md` fuellen

Die KI fragt fuer die 5 Bloecke (analog onboard-Skill):

1. **Stammdaten** — Branche, Standort, Webseite, Erstkontakt-Datum, Aufbauender Kollege
2. **Beziehung** — Beziehungs-Status (aktiv/schlafend/eskaliert), Vertragsart, Hauptbetreuendes Team
3. **Schluesselpersonen** — Hauptansprechpartner mit Rolle. Bei JA-Frage "wichtig genug fuer eigenen Personen-Folder?": Wikilink setzen, spaeter `/onboard` Modus 4 starten.
4. **Was wir machen** — Verweis auf passende Leistung aus [[organization]]
5. **Beziehung & Tonalitaet** — Anrede (Du/Sie), Kommunikationsvorlieben, Tabu-Themen

Frontmatter mindestens: `type: unternehmen`, `beziehung`, `status`, `seit`, `last-updated`.

### 5. Cross-Links pruefen

Die KI prueft und ergaenzt:

- **ICP-Match:** passt der Kunde in eine Persona aus [[wunschkunde-icp]]? Wenn ja: Verweis in `kontext.md` ergaenzen.
- **Aehnliche Kunden:** gibt es vergleichbare Cases in `03-CRM/Unternehmen/`? Hinweis in `kontext.md` Sektion "Querverbindungen".
- **Roster-Cross-Ref:** der Account-Lead ist als Wikilink zu `04-Mitarbeiter/team-mitglieder.md` gesetzt.

### 6. Kickoff-Setup (optional)

Die KI fragt: "Soll ich einen Kickoff-Termin vorschlagen?"

Bei Ja:

- Erstelle ersten Meeting-Eintrag unter `03-CRM/Meetings/YYYY-MM-DD-acme-kickoff.md` (Vorlage [[03-CRM/Meetings/_protokoll-vorlage]])
- Entwirf eine Terminfindungs-Mail in [[brand]]-Stil
- Mail bleibt im Chat — User schickt manuell

### 7. Confirmation

```
[OK] 03-CRM/Unternehmen/<slug>/kontext.md angelegt + gefuellt
[OK] Cross-Links zu ICP / organization / Account-Lead gesetzt
[?]  Soll ich gleich Modus "Person" fuer den Hauptkontakt starten?
```

---

## Output

- `03-CRM/Unternehmen/<slug>/kontext.md` — neu
- optional: `03-CRM/Meetings/YYYY-MM-DD-<slug>-kickoff.md` — neu
- optional: Kickoff-Mail im Chat

## Referenzen

- [[organization]]
- [[wunschkunde-icp]]
- [[brand]]
- [[03-CRM/Meetings/_protokoll-vorlage]]
- [[R-001-namenskonventionen]]
