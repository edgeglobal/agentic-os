<!--
AI OS — Agentic Operating System für KMUs
© 2026 Gerald Eder · UmsatzAI · MIT License
-->

# 03-CRM/Personen/

Alle **externen** Personen mit denen ihr regelmaessig zu tun habt: Ansprechpartner bei Kunden, Lieferanten-Kontakte, Beirat, Investoren, Steuerberater, Anwalt, ehemalige Mitarbeiter die jetzt bei Kunden sind.

> Nicht zu verwechseln mit `04-Mitarbeiter/` — das sind eure **eigenen** Mitarbeiter.

## Wann jemand hier rein gehoert

- Person taucht in **3+ Meetings oder Mail-Threads** auf
- Person ist **Entscheider** bei einem Kunden oder Lieferanten
- Person ist **strukturell relevant** (Beirat, Investor, Steuerberater)
- Person hat **Kontext-Wissen** das ueber Jahre wert ist (Beziehungen, Vorlieben, Vorgeschichte)

## Wann nicht

- Einmal-Kontakte (z.B. Person aus Recherche-Anruf)
- Massenkontakte ohne persoenliche Beziehung (z.B. Newsletter-Abonnenten)
- Bewerber (gehoert ins HR-System)
- Privat-Kontakte (gehoeren nicht ins Firmen-OS)

## Aufbau

```
03-CRM/Personen/
├── README.md                 ← diese Datei
├── _neue-person/             ← Vorlage zum Duplizieren
│   └── kontext.md
├── hans-mueller/
│   └── kontext.md
├── andreas-weber/
│   └── kontext.md
└── ...
```

## Naming

Kebab-case, Vorname-Nachname:
- `hans-mueller/`
- `elena-koenig/`
- `andreas-weber/`

Bei Namensgleichheit: Anhang Firma oder Initial — `hans-mueller-acme/`, `hans-mueller-b/`.

## Verknuepfung

Im `kontext.md` einer Person:

- Wikilink zur aktuellen Firma: `Aktuelle Firma: [[03-CRM/Unternehmen/acme-gmbh]]`
- Verlauf bei vorherigen Firmen
- Backlinks zu Meeting-Notes (KI pflegt das automatisch)

In `03-CRM/Unternehmen/<firma>/kontext.md` gibt's eine Sektion "Schluesselpersonen" mit Wikilinks zu den entsprechenden Personen-Files.

## Wer darf was schreiben

| Was | Wer |
|---|---|
| Neue Person anlegen | Operator oder Teams die mit der Person arbeiten |
| Person-Kontext aktualisieren | Person der die Beziehung pflegt |
| Verlauf-Eintraege | KI automatisch nach Meeting + Vorgesetzter / Team-Lead |

## Privacy

Personenbezogene Daten unterliegen der DSGVO. Pruefen:

- **Lawful Basis** (Vertragserfuellung, berechtigtes Interesse, Einwilligung)
- **Sensitive Kategorien** (Gesundheit, politische Meinung, Religion) — NICHT erfassen
- **Loesch-Anfrage** durch Person — alle Files inkl. Backlinks loeschen
