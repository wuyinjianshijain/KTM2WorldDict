# WorldDict authoring contract

## Purpose

Keep the current category folders while allowing Markdown content to evolve toward a clean, linkable, writer-friendly knowledge base. This contract is adaptive: preserve existing documents during ordinary edits and apply the new-document baseline only where useful.

## What a WorldDict is for

Two audiences, one job: **developers writing stories, doujin work and quests**, and **players who want to understand the world**. Everything in an entry should serve one of them.

A WorldDict is therefore **not** an in-game wiki. It describes phenomena, names, institutions and consequences; the game's own documentation describes values and implementation. Authority is asymmetric and the split is not negotiable:

| Fact | Authority | For KTM2 |
| --- | --- | --- |
| Stats, talents, spells, tiers, nodes, status effects, prices, implementation status | the game's docs | <https://kentomahou.com/> and `../kzeroko.github.io/src/content/{wiki,dev}/` |
| History, institutions, people, motives, culture, causality, meaning | the WorldDict | this repository |

Game-internal facts that disagree are resolved in favour of the game's docs, and the WorldDict prose is corrected.

### Never in an entry

| Excluded | Why | Where it goes |
| --- | --- | --- |
| Numbers, multipliers, formulas, tier price bands | drift against implementation, unverifiable here | game docs |
| Registry IDs, placeholders, data paths | implementation detail, not setting | game docs, code |
| Node tables, spell catalogs, status registries | same, and the lists change | game docs |
| Implementation status, gaps, backlogs, schedules | a setting library cannot declare what shipped | game docs, issues |
| Art, audio, level-design directives | mostly never confirmed by production | nowhere |
| Quest lists and world-state tables for quests that do not exist | presents imagination as settled canon | rewrite as story hooks |

Test every sentence with: **would a balance patch make this wrong?** If yes, it is not WorldDict material. Qualitative world rules are welcome; their values are not.

Read the relevant game-doc page **before** writing any entry that touches a game-internal subject. If the game docs are unreachable, say so and keep the entry qualitative.

## Authority model

Use these states consistently:

- `canon`: approved current truth;
- `draft`: working proposal not yet authoritative;
- `deprecated`: retained for history but no longer current;
- `conflict`: incompatible claims requiring a decision;
- `unknown`: deliberately unanswered or not yet designed.

Files under `legacy/` remain historical unless explicitly promoted.

Unimplemented design is labelled, never asserted. Use `status: draft`, or mark the section heading with a WIP / non-canon marker plus a non-canon note on its first line when only part of an entry is speculative. KTM2 uses the heading suffix `(WIP design, non-canon)` rendered in the document's own language. Labelled material must not be cited as established fact by other entries, and must not reach public-facing text.

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
- **Canon facts:** confirmed rules and observable facts, stated qualitatively.
- **Effect on ordinary life:** what this leaves in daily routine, prices, habits, institutions.
- **Story hooks:** tensions a writer can act on today. Draw them from what the entry already establishes. No quest titles, no promise that any of it is scheduled, no state machines. This block replaces the old production-hooks block, which invited art, audio and level directives into entries that had no business carrying them.
- **Relationships and dependencies:** links to affected entries.
- **Open decisions:** proposals, conflicts, and unknowns with owners or next decisions when known.
- **Authority boundary:** the game-doc page this entry defers to, plus an explicit statement that the entry does not copy its values and that the game docs win on conflict. Every world entry ends with this block.

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

Use player experience and pacing, geography and access, population and livelihood, districts and points of interest, services and cost of living, authority and risk, then story hooks and relationships.

Do **not** add a visual/audio language block, a traversal or level-mechanics block, a quest list, or a world-state table keyed to player effects. A place's world conditions are legitimate when they are genuinely part of the setting (a facility that runs, strains, or stops): write them as world appearance and consequence for residents, not as player effects.

### Faction-focused blocks

Use public purpose, actual incentives, structure, resources, methods, internal divisions, external relationships, player reputation, and content hooks as needed.

### Lore-focused blocks

Use in-world mechanism and naming, institutions and social consequence, contested claims (folk consensus, institutional account, what remains unexplained), story hooks, then relationships and the authority boundary.

Where history is contested, the layers are evidence and source, public belief, institutional account, hidden truth, information holders, cost of discovery, and present-day consequence. Do not mechanically apply all layers to uncontested knowledge.

**There is no system-focused block.** A would-be system entry is either in-world meaning, which is a lore entry written qualitatively, or it is rules and values, which belong in the game's docs. If you cannot say who benefits, who pays, and how an ordinary person notices it, you are writing the wrong document.

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
7. keep rollback possible and do not delete legacy material without explicit approval;
8. run the repository's validator and fix everything it reports before handing work back. For KTM2: `python .github/scripts/validate_worlddict.py`, which enforces frontmatter, unique IDs, relative links, and the scope boundary in this contract.
