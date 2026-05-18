# SOP-005 — Angebot erstellen

**Wofuer:** Wenn ein Interessent oder Bestandskunde ein Angebot braucht.
**Ausloeser:** "Erstelle ein Angebot fuer [Firma]", "Schreib einen Vorschlag fuer Acme zur Leistung X".
**Verantwortlich:** Die KI schreibt, Vertrieb / Geschaeftsfuehrung signt off vor Versand.
**Dauer:** 15-30 Minuten je nach Komplexitaet.

---

## Schritte

### 1. Kontext laden

Die KI liest **bevor** sie eine Zeile schreibt:

1. `03-CRM/Unternehmen/<firma>/kontext.md` — wer ist das, Beziehungs-Status, Tonalitaet (Du/Sie)
2. `01-Firma Home/organization.md` — welche Leistungen wir anbieten
3. `01-Firma Home/brand.md` — wie wir klingen (Tonalitaet, Signature-Phrases, was wir nie sagen)
4. `01-Firma Home/wunschkunde-icp.md` — bekannte Pain-Points der Persona
5. Frueheste Eintraege aus `03-CRM/Meetings/` mit diesem Kunden — was wurde diskutiert
6. Falls vorhanden: frueheste Angebote im selben Kunden-Folder als Stil-Referenz

Wenn der Kunden-Folder noch nicht existiert: erst SOP-002 (neuen Kunden anlegen) ausfuehren.

### 2. Bedarf klaeren

Die KI fragt max 3 Fragen pro Block:

- **Welche Leistung?** (Match mit organization.md — welcher Punkt?)
- **Umfang?** (Mengen, Module, Dauer)
- **Timeline?** (Wann Start? Wann Lieferung?)
- **Budget-Range?** (Hat der Kunde einen Rahmen genannt?)
- **Spezialwuensche / Ausnahmen?**
- **Entscheider auf Kunden-Seite?** Wer sagt am Ende Ja?

### 3. Lueckeneraehlung mit dem User

Wenn etwas unklar ist (z.B. Kunde hat noch keinen Pain-Point genannt), **nicht erfinden** — User fragen.

Bei Annahmen: in der Draft `[zu pruefen: ...]` markieren.

### 4. Angebot schreiben in [[brand]]-Stil

Standard-Struktur (anpassbar je nach Branche):

```markdown
# Angebot — [Leistung] fuer [Firma]

[Datum] | Angebot-Nr [Lfd.-Nr.]

## Verstaendnis

[2-4 Saetze: Was wir vom Kunden verstanden haben. Spiegelt zurueck — zeigt dass zugehoert wurde. Nutzt **Begriffe des Kunden**, nicht unsere internen Termini.]

## Loesung

[Was wir vorschlagen. Verbindet Pain-Point aus "Verstaendnis" mit unserer Leistung aus organization.md. **Nicht Feature-Listen** — Outcome-orientiert.]

## Was wir liefern

- [Konkretes Deliverable 1 mit Format/Umfang]
- [Konkretes Deliverable 2]
- [...]

## Wie wir arbeiten

[Kurz: Methode, Ablauf, Touchpoints mit dem Kunden. Hier passt Brand-Voice am direktesten — Tonalitaet aus brand.md.]

## Timeline

| Phase | Inhalt | Dauer |
|---|---|---|
| 1 | [Kickoff + Discovery] | [X Wochen] |
| 2 | [Bauphase] | [X Wochen] |
| 3 | [Review + Handover] | [X Wochen] |

Start: [Datum]. Ende: [Datum].

## Investment

[Betrag in EUR, netto. Zahlungsplan: z.B. 50/50, 30/40/30. **Ein Preis, eine Loesung.** Bei mehreren Optionen: max 3, mit klarem Empfehlungs-Tag.]

## Naechste Schritte

1. Rueckmeldung bis [Datum]
2. Bei Annahme: [konkreter erster Termin]
3. Vertrag / LOI

---

Mit besten Gruessen
[Name] | [Position]
```

### 5. Pruefen gegen Anti-Slop-Liste

Die KI checkt automatisch ob im Draft enthalten ist:

- Generische Marketing-Floskeln ("ganzheitlich", "innovativ", "auf Augenhoehe") — entfernen
- Versprechen die nicht in organization.md gedeckt sind — entfernen oder als `[zu pruefen]` markieren
- Tonalitaets-Bruch (Du wo Sie sein muss, oder umgekehrt) — Anrede aus kontext.md
- Phrasen die in brand.md unter "Was wir nie sagen" stehen — entfernen

### 6. Speichern

`03-CRM/Unternehmen/<firma>/angebote/YYYY-MM-DD-<leistung-slug>.md`

Folder `angebote/` wird beim ersten Mal angelegt — nicht praeventiv leer.

Frontmatter:

```yaml
---
type: angebot
firma: [[03-CRM/Unternehmen/<slug>]]
datum: YYYY-MM-DD
leistung: [Kurzname]
status: draft | gesendet | angenommen | abgelehnt
wert-eur: 0
gueltig-bis: YYYY-MM-DD
---
```

### 7. Backlink im Kunden-`kontext.md`

In `03-CRM/Unternehmen/<firma>/kontext.md` neue Zeile in einer Sektion "Angebote":

```markdown
- [[YYYY-MM-DD-<leistung-slug>]] — [Leistung] — [Wert] EUR — Status: draft
```

### 8. Confirmation

```
[OK] Draft: 03-CRM/Unternehmen/<firma>/angebote/<file>.md
[OK] Backlink in kontext.md gesetzt
[?]  Pre-flight gegen Anti-Slop-Liste: <N Issues gefunden | sauber>
NEXT Operator: lesen, anpassen, manuell verschicken
```

Die KI verschickt **nichts automatisch**.

---

## Output

- `03-CRM/Unternehmen/<firma>/angebote/YYYY-MM-DD-<slug>.md` — neu
- Backlink in `kontext.md`
- Optional: Pre-flight-Issue-Liste

## Referenzen

- [[organization]] — Leistungs-Katalog
- [[brand]] — Tonalitaet, was wir nie sagen
- [[wunschkunde-icp]] — Pain-Points der Persona
- [[03-CRM/Unternehmen/_neues-unternehmen/kontext]] — Kontext-Vorlage
- [[R-001-namenskonventionen]]
