---
type: knowledge
topic: tools
last-updated: 2026-05-11
status: template
---

# Unsere Tools

> **Anleitung:** Welche Software/SaaS nutzt die Firma fuer welchen Zweck. Die KI braucht das um zu wissen wo Daten liegen und wie sie auf Tools zugreifen kann (per MCP, API, oder gar nicht). Idealerweise fuellt der `/onboard` Skill das im Firma-Modus automatisch aus.

## Pro Bucket: was nutzen wir

> Sieben Buckets sind die typischen externen Systeme. Pro Bucket: Tool eintragen, Verbindungs-Status notieren.

| # | Bucket | Tool | Verbunden | Auth | Anmerkungen |
|---|---|---|---|---|---|
| 1 | **Buchhaltung / Finanzen** | [z.B. lexoffice / Datev / Sevdesk / Sage] | [nein / MCP / API / Export] | [API-Key / OAuth / -] | [Wer hat Zugriff] |
| 2 | **Kunden-Kommunikation / CRM** | [z.B. HubSpot / Pipedrive / lexoffice CRM] | [...] | [...] | [...] |
| 3 | **Kalender** | [z.B. Google Calendar / Outlook] | [...] | [...] | [...] |
| 4 | **Mail / Kommunikation** | [z.B. Microsoft 365 / Google Workspace / Slack / Teams] | [...] | [...] | [...] |
| 5 | **Projekt-Tracking** | [z.B. Notion / Asana / ClickUp / Linear] | [...] | [...] | [...] |
| 6 | **Meeting-Aufzeichnungen** | [z.B. Granola / Otter / Fireflies / Teams-Aufnahme] | [...] | [...] | [...] |
| 7 | **Wissen / Files** | [z.B. Google Drive / OneDrive / Notion / Confluence] | [...] | [...] | [...] |

## Verbindungs-Status

- **nein** — Tool wird genutzt, aber die KI hat keinen Zugriff (manuelle Eingabe noetig)
- **MCP** — Tool ueber Model Context Protocol angebunden, KI kann lesen/schreiben
- **API** — eigene API-Anbindung dokumentiert in [[references/<tool>-api]]
- **Export** — periodischer Export (CSV, PDF) ins AI-OS

## Was noch zu tun ist

> Liste der Tools die wir noch nicht haben angebunden, mit Prioritaet.

- [ ] [Tool 1] — Anbinden wuerde [Nutzen] bringen
- [ ] [Tool 2] — ...

## Tools die wir bewusst NICHT anbinden

> Datenschutz, Vertraulichkeit, oder andere Gruende.

- [Tool / Grund]

## Wie die KI mit Tool-Anbindungen umgeht

- Bei verbundenen Tools: kann sie selbststaendig nutzen
- Bei nicht-verbundenen Tools: fragt sie nach den Daten oder schlaegt einen Anbindungs-Skill vor
- Bei sensiblen Daten: immer Rueckfrage vor Verarbeitung
