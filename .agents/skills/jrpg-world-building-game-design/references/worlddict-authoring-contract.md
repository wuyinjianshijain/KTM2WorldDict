# WorldDict authoring contract

## Purpose

Keep the current category folders while allowing Markdown content to evolve toward a clean, linkable, developer-friendly knowledge base. This contract is adaptive: preserve existing documents during ordinary edits and apply the new-document baseline only where useful.

## Authority model

Use these states consistently:

- `canon`: approved current truth;
- `draft`: working proposal not yet authoritative;
- `deprecated`: retained for history but no longer current;
- `conflict`: incompatible claims requiring a decision;
- `unknown`: deliberately unanswered or not yet designed.

Files under `legacy/` remain historical unless explicitly promoted.

## Optional frontmatter for new or migrated files

Use frontmatter when stable machine-readable identity helps the project. Do not add it to every old file without an explicit migration request.

```yaml
---
id: character.evelina-astraea-logos
type: character
title: 伊维莉娜・阿斯特莱雅・罗格斯
status: canon
aliases:
  - Evelina Astraea Logos
tags:
  - clock-tower
updated: 2026-07-17
---
```

Rules:

- Keep `id` stable when a display name changes.
- Use lowercase dotted or hyphenated identifiers without spaces.
- Keep `type` aligned with the folder taxonomy.
- Use ISO dates.
- Store only indexing metadata in frontmatter; keep prose and design reasoning in the body.
- Add relationship metadata only after the project chooses a single representation. Until then, use explicit relative Markdown links in the body.

## Adaptive body blocks

Choose blocks by content type. Do not create empty sections.

### Shared blocks

- **Summary:** the smallest complete statement of the entry.
- **Canon facts:** confirmed rules and observable facts.
- **Production hooks:** consequences for narrative, gameplay, art, levels, audio, UI, or localization.
- **Relationships and dependencies:** links to affected entries.
- **Open decisions:** proposals, conflicts, and unknowns with owners or next decisions when known.

### Character-focused blocks

Use identity and dramatic function, visual silhouette, psychology and contradiction, relationships, voice, gameplay role, arc state, and interaction boundaries as needed. Avoid encyclopedic biography when the production need is only dialogue or combat design.

When a document contains character quotes or sample dialogue, the voice block must establish:

- who the character is addressing and what they need in that moment;
- a voice fingerprint that changes recognizably under ordinary, pressured, trusting, and vulnerable states;
- an opening quote grounded in a real moment that a reader with no prior context still understands, rather than either a theme summary or an opaque in-scene fragment;
- cross-character comparison showing that the line cannot be reassigned unchanged.

Dialogue coverage is a quality requirement, not a reason to force empty dialogue sections into characters who will never speak on screen.

### Public and internal layers

When a project publishes character material to a wiki, in-game encyclopedia, or marketing surface, split the card into a public layer and an internal layer inside the same file, separated by an explicit divider. Do not interleave them.

- **Public layer:** identity, silhouette, a readable introduction, notable traits, career summary, timeline, relationships, and quotable lines. No spoilers, and written in the project's public register rather than its design register.
- **Internal layer:** contradiction, hidden truth, information tiers, gameplay role, arc beats, voice direction, balance notes, and interaction boundaries.
- End the internal layer with an explicit list of what the public layer must never contain **for this character**. A general "no spoilers" rule is not enforceable; a per-character list is.
- Scale public timelines to available canon. Give major characters a full one and thinly documented characters three to five nodes; do not invent filler to make pages look uniform.

### Location-focused blocks

Use player experience, geography and access, population and livelihood, authority and conflict, visual/audio language, traversal or level mechanics, encounters, and quest state as needed.

### Faction-focused blocks

Use public purpose, actual incentives, structure, resources, methods, internal divisions, external relationships, player reputation, and content hooks as needed.

### System-focused blocks

Use player promise, rules, state transitions, inputs and outputs, progression, balance assumptions, failure cases, content dependencies, and implementation notes as needed.

### Lore-focused blocks

Use evidence and source, public belief, institutional account, hidden truth, information holders, cost of discovery, and present-day consequence as needed.

## Cross-reference rules

- Prefer relative Markdown links to bare filenames when the target exists.
- Link the first meaningful mention; avoid linking every repetition.
- Do not create a link to a planned file unless it is clearly marked as pending.
- When renaming or moving a file, update inbound references in the same requested migration.
- Search aliases before creating a new entry to prevent duplicates.

## Migration discipline

When the user asks to migrate existing content:

1. inventory files and current schemas;
2. propose the target contract and a representative conversion;
3. preserve information before reorganizing it;
4. separate cleanup from canon changes;
5. migrate in bounded batches;
6. verify links, IDs, encoding, and diffs after each batch;
7. keep rollback possible and do not delete legacy material without explicit approval.
