# 03-Kunden

**Pro Kunde ein Ordner.**

Hier lebt alles was zu einem konkreten Kunden gehört: Verträge, Briefings, Liefertöpfe, Meeting-Protokolle, Erfolgs-Metriken.

## Struktur pro Kunde

```
03-Kunden/
└── acme-gmbh/                          ← kebab-case, kein Umlaut
    ├── _hub.md                         ← Hub-Datei mit Übersicht
    ├── briefing.md                     ← Initial-Briefing nach Onboarding
    ├── meetings/                       ← Meeting-Protokolle
    │   ├── 2026-05-09-kickoff.md
    │   └── 2026-05-23-review.md
    ├── lieferungen/                    ← Was wir liefern
    │   ├── 2026-05-15-konzept-v1.md
    │   └── 2026-06-01-final-deck.md
    └── notizen.md                      ← Lose Notizen
```

## Hub-Datei `_hub.md`

Jeder Kunde hat eine Hub-Datei. Die KI liest sie zuerst wenn ihr nach dem Kunden fragt. Sie sollte enthalten:

- Status (aktiv / pausiert / abgeschlossen)
- Vertragsumfang (Verweis auf [[Angebot vom YYYY-MM-DD]])
- Hauptkontakte
- Aktuelle Phase
- Nächste Termine
- Risiken und offene Punkte

## Neuen Kunden anlegen

Sag zur KI:

> "Wir haben einen neuen Kunden gewonnen: [Acme GmbH]"

Die KI läuft [[SOP-002-neuen-kunden-anlegen]] und legt den ganzen Ordner an, inklusive Hub-Datei und Verlinkung mit [[unsere-kunden]].

## Privacy

Falls ein Kunde sensitiver Branche (Anwälte, Ärzte, Finanzen):
- Klar im Hub vermerken: "**SENSITIV — keine Details außerhalb dieses Ordners zitieren**"
- Die KI respektiert das und vermeidet Querverweise in anderen Dokumenten
