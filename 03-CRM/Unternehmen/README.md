<!--
AI OS — Agentic Operating System für KMUs
© 2026 Gerald Eder · UmsatzAI · MIT License
-->

# 03-CRM/Unternehmen/

**Pro externes Unternehmen ein Ordner.** Kunden, Lieferanten, Partner, Berater, Beirat — alle externen Firmen mit denen ihr regelmaessig zu tun habt.

Die Beziehungs-Art (Kunde / Lieferant / Partner / etc.) steht im Frontmatter — ein Unternehmen kann gleichzeitig Kunde UND Lieferant sein.

## Struktur pro Unternehmen

```
03-CRM/Unternehmen/
├── README.md                              ← diese Datei
├── _neues-unternehmen/                    ← Vorlage zum Duplizieren
│   └── kontext.md
└── acme-gmbh/                             ← kebab-case, kein Umlaut, ohne Rechtsform
    ├── kontext.md                         ← Stammdaten, Beziehung, Schluesselpersonen
    ├── gespraeche/                        ← Verweise auf Meeting-Files
    └── ablage/                            ← Angebote, Vereinbarungen, Memos
```

## Beziehungs-Typen

Im `kontext.md`-Frontmatter:

```yaml
---
type: unternehmen
beziehung: [kunde, lieferant, partner, berater, beirat, mitbewerber, ehemalig]
status: [aktiv, schlafend, eskaliert, abgelaufen]
seit: 2024-03-15
---
```

Ein Unternehmen kann mehrere Beziehungs-Typen haben.

## Naming

Kebab-case, ohne Rechtsform-Suffix, kein Umlaut:

- `acme-gmbh/` (Kunde)
- `dhl/` (Lieferant)
- `schulze-partner/` (Steuerberater)
- `beirat-meyer/` (Beirat)

## Wann ein Unternehmen hierhin gehoert

- Ihr habt regelmaessigen Geschaeftskontakt (3+ Touchpoints pro Jahr)
- Es gibt persoenliche Beziehung (Hauptansprechpartner)
- Es gibt operative Verflechtung (Vertrag, Lieferungen)

## Wann nicht

- Einmal-Kontakte ohne Vertrag
- Massen-Kunden (gehoeren ins ERP/CRM-System)
- Lead-Stage Kontakte vor Vertrag (gehoeren ins CRM oder als Eintrag in `03-CRM/Meetings/external/`)

## Verknuepfung mit Personen und Meetings

- **Personen** beim Unternehmen: Sektion "Schluesselpersonen" in `kontext.md` mit Wikilinks zu `[[03-CRM/Personen/<name>]]`
- **Meetings** mit dem Unternehmen: zentral in `03-CRM/Meetings/external/YYYY/MM/`. Backlinks erscheinen in `kontext.md` (KI pflegt automatisch).

## Wer darf was schreiben

| Was | Wer |
|---|---|
| Neues Unternehmen anlegen | Operator oder Team das den Kontakt aufbaut |
| `kontext.md` aktualisieren | Hauptbetreuendes Team |
| `gespraeche/` Eintraege | Wer am Meeting war |
| `ablage/` | Wer am Output gearbeitet hat |

## Neues Unternehmen anlegen

Sage zur KI:

> "Wir haben einen neuen Kunden gewonnen: Acme GmbH"

Die KI laeuft [[SOP-002-neuen-kunden-anlegen]] (oder analog fuer Lieferant/Partner) und legt den Folder an aus `_neues-unternehmen/`.

## Privacy

- Personenbezogene Daten in `kontext.md` minimal halten — Details gehoeren in `03-CRM/Personen/<name>/`
- Vertraege im Klartext gehoeren ins DMS, nicht hier
- Sensitive Branche (Anwaelte, Aerzte, Finanzen): im `kontext.md` vermerken "SENSITIV — keine Details ausserhalb dieses Ordners zitieren"
