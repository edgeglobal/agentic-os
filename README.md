<!--
Business AOS v2.0.0 — © 2026 Gerald Eder
Licensed under MIT License — see LICENSE
-->

# Business AOS

**Agent Operating System für ein Business.** Eine Ordner-Struktur in Markdown, die deiner KI sofort den vollen Firmen-Kontext gibt.

Klone das Repo, öffne es in deinem AI-Tool, starte das `bootstrap` Playbook — und deine KI kennt deine Firma, deine Kunden, deine Strategie, deine Prozesse.

---

## Was Business AOS ist

Ein Folder pro Business. Drinnen liegen Markdown-Files, die die KI bei jeder Session liest:

- **Wer ihr seid** als Firma (`ueberblick.md`, `marke.md`)
- **Wer eure Wunschkunden sind** (`wunschkunde-icp.md`)
- **Was eure Strategie ist** (`strategie.md`)
- **Welche Tools ihr nutzt** (`tools.md`)
- **Wen ihr kennt** (`kunden/unternehmen/`, `kunden/personen/`)
- **Was ihr besprochen habt** (`kunden/meetings/`, `meetings-intern/`)
- **Wie ihr arbeitet** (`prozesse/sops/`, `prozesse/richtlinien/`, `prozesse/workflows/`)

Die KI nutzt diesen Kontext, um in eurer Sprache zu schreiben, eure Kunden zu kennen, und Vorgänge sauber zu pflegen.

---

## Was du bekommst

| Element | Beschreibung |
|---|---|
| **Universelle Ordner-Struktur** | Ein Folder = ein Business. Keine Multi-Biz, keine Holding. Wer mehrere Businesses hat, klont mehrmals. |
| **CRM-Light in Markdown** | Unternehmen + Personen + Meetings via Wikilinks vernetzt. Kein externes CRM nötig. |
| **Default-Teams** | Marketing, Vertrieb, Fulfillment, Finance/HR/Admin. Anpassbar oder löschbar. |
| **Universelle Context-Files** | ueberblick, marke, wunschkunde-icp, strategie, tools |
| **3 Skills** | audit, check-sync-status, level-up |
| **5 Role-Templates** | ceo, vertrieb, marketing, fulfillment, finance-hr — als Mitarbeiter-Profile |
| **Tool-agnostisch** | `AGENTS.md` lesen Claude, Codex, Cursor, Gemini nativ |

---

## Quick Start

```bash
git clone https://github.com/gerald-eder/business-aos.git "Business AOS"
cd "Business AOS"
# Open in your AI tool (Claude Code, Cursor, etc.)
# Run the bootstrap playbook
```

Details in [`INSTALL.md`](INSTALL.md).

---

## Optional: Personal AI Companion

Wer als Solopreneur einen privaten Layer für sich selbst will (Profil, Aufgaben, Tagebuch, Notizen), kann zusätzlich [Personal AI](https://github.com/gerald-eder/personal-ai) als Sibling klonen:

```
~/ai-os/
  Business AOS/      # this repo
  Personal AI/       # github.com/gerald-eder/personal-ai
```

Beide Repos erkennen den jeweiligen Sibling automatisch. Beide funktionieren auch alleine.

---

## License

MIT. See [`LICENSE`](LICENSE).
