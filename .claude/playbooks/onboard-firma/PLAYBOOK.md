---
name: onboard-firma
description: 7-section company interview. Fills firma/{ueberblick,marke,wunschkunde-icp,strategie,tools}.md and optionally creates stakeholder kontext-files. Run once after bootstrap, re-run safe (updates existing files).
type: playbook
---

# Onboard Firma

Strukturiertes Interview zur Befüllung des `firma/` Kontextes. 7 Sektionen, jede mit HUMAN-CHECKPOINT vor dem Schreiben.

## Pre-Flight

Sicherstellen dass die Ziel-Files existieren (von Task 9 angelegte Stubs mit `{{PLACEHOLDERS}}`):

```bash
for f in firma/ueberblick.md firma/marke.md firma/wunschkunde-icp.md firma/strategie.md firma/tools.md; do
  test -f "$f" || echo "MISSING: $f"
done
```

Falls Files fehlen: STOP und User informieren. `bootstrap` muss vorher gelaufen sein, ggf. Repo neu klonen.

CWD-Check: muss `~/ai-workspace/` sein (oder Symlink darauf).

## Phase 1: Identität

Ziel-File: `firma/ueberblick.md` (Sektion "Identität").

Fragen:
1. Firmenname (Marke + ggf. Legal-Name falls anders)?
2. Branche / Industry (1 Satz, was ihr macht)?
3. Standort (Stadt, Land, remote-first ja/nein)?
4. Legal-Entity (GmbH, GbR, Einzelunternehmen, Ltd, Inc, ...)?
5. Größe (Solo, 2-5, 6-20, 21-50, 50+ Mitarbeiter)?

> [!question] HUMAN-CHECKPOINT
> Zeige zusammenfassendes YAML/Prosa-Block, frage: "Soll ich das in `firma/ueberblick.md` Sektion Identität schreiben? (j/n/edit)"

Bei `j`: ersetze `{{IDENTITAET_*}}` Placeholders. Bei `edit`: erfasse Korrekturen, dann erneut HUMAN-CHECKPOINT.

## Phase 2: Mission

Ziel-File: `firma/ueberblick.md` (Sektion "Mission" + "North-Star").

Fragen:
1. Mission in 1 Satz: warum existiert die Firma?
2. North-Star Metric: die EINE Zahl, die wenn sie steigt, alles besser läuft (z.B. MRR, aktive Kunden, Leads/Monat)?
3. Aktueller Wert + Ziel-Wert dieser Metric (Zeitraum: 12 Monate)?

> [!question] HUMAN-CHECKPOINT
> Zeige Mission + North-Star Block. "Schreiben in `firma/ueberblick.md`? (j/n/edit)"

Bei `j`: ersetze `{{MISSION_*}}` und `{{NORTHSTAR_*}}` Placeholders.

## Phase 3: Marke

Ziel-File: `firma/marke.md`.

Fragen:
1. Brand-Story in 2-3 Sätzen (Origin + Was-anders)?
2. 3-5 Voice-Prinzipien (z.B. "direkt statt höflich", "konkret statt abstrakt")?
3. Tone-Spektrum (formal ↔ casual, ernst ↔ verspielt, jeweils 1-10 plus Begründung)?
4. NEVER-Patterns: 3-5 Dinge die wir NIE sagen oder tun (Phrasen, Themen, Stil)?
5. ALWAYS-Patterns: 3-5 wiederkehrende Markenzeichen (Wording, Format, Ritual)?

> [!question] HUMAN-CHECKPOINT
> Zeige Marke-Block (Story + Voice + Tone + Never/Always Listen). "Schreiben in `firma/marke.md`? (j/n/edit)"

Bei `j`: ersetze `{{MARKE_*}}` Placeholders.

## Phase 4: Wunschkunde

Ziel-File: `firma/wunschkunde-icp.md`.

Fragen:
1. Demographie (Branche, Firmen-Größe, Rolle, Region, Budget-Range)?
2. Psychographie (Werte, Frustrationen, Aspirationen, Vokabular)?
3. Buying-Journey (Awareness-Trigger, Evaluation-Kriterien, Entscheider, typische Sales-Cycle-Länge)?
4. Non-ICP: wen wollen wir explizit NICHT als Kunden (Branchen, Größen, Rote-Flaggen)?

> [!question] HUMAN-CHECKPOINT
> Zeige ICP-Profil + Non-ICP. "Schreiben in `firma/wunschkunde-icp.md`? (j/n/edit)"

Bei `j`: ersetze `{{ICP_*}}` Placeholders.

## Phase 5: Strategie

Ziel-File: `firma/strategie.md`.

Fragen:
1. 12-Monats North-Star (Re-Statement aus Phase 2, jetzt mit Pfad-Hypothese)?
2. Annual-Targets (3-5 messbare Jahresziele)?
3. Q-OKRs aktuelles Quartal (1 Objective + 3 Key Results)?
4. Strategic Bets: 2-3 Wetten die wir dieses Jahr machen (Kanal, Produkt, Markt)?
5. Not-Doing-List: 3-5 Dinge die andere im Markt machen, wir bewusst NICHT?

> [!question] HUMAN-CHECKPOINT
> Zeige Strategie-Block (NorthStar + Targets + OKRs + Bets + Not-Doing). "Schreiben in `firma/strategie.md`? (j/n/edit)"

Bei `j`: ersetze `{{STRATEGIE_*}}` Placeholders.

## Phase 6: Tools

Ziel-File: `firma/tools.md`.

Fragen:
1. Operative Tools nach Funktion: CRM, Email, Buchhaltung, Comms, Project-Mgmt, Website, Analytics, Ads (Tool-Name pro Slot, "keins" ist valid)?
2. AI-Modelle: welche LLMs sind in Use (Claude, OpenAI, Gemini, OpenRouter, lokale Modelle)?
3. MCP-Server: welche MCPs aktiv (Airtable, Notion, GHL, Slack, GCal, Drive, ...)?
4. Credentials-Note: wo liegen die API-Keys (z.B. `~/.secrets`, 1Password Vault, AWS Secrets Manager)? KEINE Werte erfragen, nur Storage-Location.

> [!question] HUMAN-CHECKPOINT
> Zeige Tool-Stack-Tabelle. "Schreiben in `firma/tools.md`? (j/n/edit)"

Bei `j`: ersetze `{{TOOLS_*}}` Placeholders.

## Phase 7: Stakeholder (OPTIONAL)

Diese Phase kann übersprungen werden. Sinnvoll wenn 2+ Personen mit Stake (Co-Founder, Schlüsselrollen, externe Partner mit Kontext-Relevanz).

> [!question] HUMAN-CHECKPOINT
> "Phase 7 Stakeholder erfassen? (j/n) Erstellt pro Person `firma/mitarbeiter/{slug}/kontext.md`. Für eigenes Profil später `/playbooks/onboard-mitarbeiter` nutzen."

Bei `n`: skip zu Phase 8.

Bei `j`, pro Person:
1. Name + Slug (kebab-case, z.B. `anna-mueller`)?
2. Rolle in der Firma (Geschäftsführung, Sales-Lead, Tech-Lead, externe Buchhaltung, ...)?
3. Entscheidungs-Scope: was darf diese Person allein entscheiden, was braucht Abstimmung?
4. Arbeits-Kontext: wo arbeitet sie (Tools, Channels), wann verfügbar (Timezone, Tage)?
5. Kommunikations-Präferenzen (async ok, sync nur für X, Direct-Style ja/nein)?

```bash
mkdir -p firma/mitarbeiter/{slug}
# kontext.md schreiben mit obigen 5 Antworten als Sektionen
```

> [!question] HUMAN-CHECKPOINT
> Pro Person: "Schreiben nach `firma/mitarbeiter/{slug}/kontext.md`? (j/n/edit)"

Loop bis keine weiteren Personen.

## Phase 8: Next Steps

Tell user:

```
✅ Onboard-Firma complete.

Geschrieben:
- firma/ueberblick.md (Identität + Mission + North-Star)
- firma/marke.md (Story + Voice + Tone + Patterns)
- firma/wunschkunde-icp.md (ICP + Non-ICP)
- firma/strategie.md (NorthStar + Targets + OKRs + Bets + Not-Doing)
- firma/tools.md (Stack + AI + MCPs + Credentials-Note)
- firma/mitarbeiter/{slug}/kontext.md (falls Phase 7)

Empfohlene nächste Schritte:
1. `/playbooks/onboard-mitarbeiter`: eigenes profil.md + KONTEXT.md generieren
2. `/skills/audit`: initialen 4-C-Score messen (Context, Capability, Consistency, Compliance)
```