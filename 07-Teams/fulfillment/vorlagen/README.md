# Team-Vorlagen

Output-Templates die **nur dieses Team** nutzt. Firmenweite Vorlagen (z.B. Meeting-Protokoll) liegen in `02-Vorlagen/`.

## Was sich als Team-Vorlage eignet

- Wiederkehrende Output-Formate des Teams
- Standardisierte Mail-Texte fuer Kunden-Kommunikation
- Formate fuer regelmaessige Berichte an Geschaeftsfuehrung

## Aufbau einer Vorlage

```markdown
# [Vorlagen-Name]

> **Wann nutzen:** [Use Case]
> **Wer nutzt:** [Rolle im Team]

## Inhalt

[Platzhalter wie {{kunde}}, {{datum}}, etc.]
```

## Skill nutzt Vorlage

Wenn ein Skill in `.claude/skills/` eine Vorlage nutzt, referenziert er sie per Pfad:

```yaml
file-access: [vorlagen/angebot.md, ...]
```

## Pflege

Halbjaehrlich vom Team-Verantwortlichen pruefen: was wird genutzt, was veraltet. Veraltetes in `99-Archiv/teams/<team>/vorlagen/` verschieben.
