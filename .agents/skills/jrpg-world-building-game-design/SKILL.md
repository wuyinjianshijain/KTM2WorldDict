---
name: jrpg-world-building-game-design
description: Explicit-invocation-only workflow for designing production-ready JRPG worlds, characters, character voices and dialogue, factions, locations, lore, narrative systems, quests, and their WorldDict canon documentation. Use only when the user explicitly invokes `$jrpg-world-building-game-design`, names `jrpg-world-building-game-design`, or directly says to use the JRPG world-building game-design skill. Do not activate merely because a request concerns fantasy, JRPGs, worldbuilding, characters, lore, game design, or Markdown files.
---

# JRPG World-Building and Game Design

## Activation boundary

Apply this workflow only after explicit invocation. If this skill was loaded without the user naming or requesting it, do not apply its rules.

Do not silently invoke the economy or dialogue skills. When those specialties are useful, mention the relevant explicit skill name and continue within the user's current scope unless they invoke it.

## Locate and classify the WorldDict

Use the WorldDict root supplied by the user. Otherwise prefer the current workspace when it contains the category folders. The canonical repository is <https://github.com/Kzeroko/KTM2WorldDict>; related checkouts (`IsekaiExpansion`, `kzeroko.github.io`) sit beside it, so reach them with `../<repo>` rather than an absolute path. Never hard-code a machine-local path, and never create a parallel WorldDict root by assumption.

Before designing or editing:

1. Inventory the relevant category and filenames with `rg --files` or an equivalent fast search.
2. When the WorldDict root contains `AUTHORING_GUIDE.md`, read it before writing and treat it as the project-specific extension of this skill's general contract. Note its tone and register rules specifically: they govern all public-facing text and override this skill's defaults.
3. Search canonical names, aliases, IDs, factions, locations, systems, and linked concepts across current files.
4. Read only the files needed for the task, then expand when a dependency or conflict appears.
5. Treat `legacy/` as historical input, not authoritative canon, unless the user explicitly promotes it. If a completed `MIGRATION_REPORT.md` records that legacy material was absorbed and removed, do not recreate or cite those deleted files as active sources.
6. Resolve authority in this order: current user instruction, project-specific authoring guide, dedicated current document, current overview/index, then legacy material. Report unresolved conflicts instead of silently choosing.

## Content model

The folder taxonomy is stable; the internal Markdown schema is allowed to evolve.

- Preserve a document's existing structure during a scoped edit unless the user asks for migration.
- For a new document, use the minimal, type-adaptive contract in [worlddict-authoring-contract.md](references/worlddict-authoring-contract.md).
- Do not force one character template onto every character, and never convert existing documents merely to make formatting uniform.
- Use stable IDs and explicit relationships for developer-facing references when the project has adopted them.
- Keep canon, proposal, unknown, contradiction, and deprecated material distinguishable.

## Design workflow

1. Restate the production decision being made and identify constraints already fixed by canon.
2. Find the design's core tension, player-facing promise, and consequences for ordinary life.
3. Develop only the dimensions needed by the request: narrative, society, ecology, visual language, gameplay, progression, quests, encounters, dialogue implications, or production dependencies.
4. Connect the design to discovered party members and existing systems when the connection is meaningful; do not force cameos.
5. Separate public belief, institutional account, and hidden truth when contested history matters. Do not mechanically add all three layers to unrelated content.
6. Detect contradictions and missing decisions. Put the recommended option in the main design; list alternatives with tradeoffs only for consequential uncertainty.
7. If the user explicitly requests comprehensive design, four-part structure, or deep expansion, read [deep-design-framework.md](references/deep-design-framework.md).
8. If writing files was requested, route the document to the existing category, make minimal cross-reference updates, and inspect the final diff or changed excerpts.

## Character voice and quote gate

For any task that creates, rewrites, expands, or audits a character, opening quote, sample line, relationship dialogue, or voiced scene, read and apply [character-voice-and-dialogue.md](references/character-voice-and-dialogue.md) before drafting.

It is a completion gate, not polish. The reference carries the full method; these three failures recur, survive careful line-by-line drafting, and must be checked explicitly:

1. **Illegible quotes.** Every opening quote and public-facing line must be understandable by someone who has read nothing else. Retreating from an author-thesis quote into an opaque in-scene fragment fails the same gate from the other side; correct toward the middle, not the opposite extreme.
2. **One voice across the cast.** Lay all characters' lines for the same state side by side and compare skeletons, not vocabulary. Enforce a one-owner quota per rhetorical template, and apply the same pass to location and faction epigraphs.
3. **Lines that assert canon.** Verify every physical or biographical claim inside a line against the character's own entry before shipping it.

## Writing standard

- Default to Simplified Chinese unless the user requests another language or the target document establishes a different convention.
- **Match register to audience.** Internal design text is specific, restrained, concrete, and decision-oriented. Player- and reader-facing text — opening quotes, public character introductions, epigraphs, item and quest copy — must be enjoyable cold, by someone with no prior context, in the project's established tone. Applying the internal register to public text is a known failure of this skill: it yields pages that read like status reports.
- Replace vague scale or mystery adjectives with observable evidence, information asymmetry, cost, and consequence.
- Make every substantial section useful to narrative, systems, art, level design, audio, UI, localization, or implementation.
- When presenting multilingual names, use `Localized name (English / Japanese) -- internal short name` only for languages that are actually established.
- Do not invent certainty. Label assumptions and proposals.
- Do not add AI disclaimers or process chatter to production documents.

## Scope and writes

Answer in conversation when the user asks for ideation, explanation, or review. Create or edit WorldDict files only when the request asks for an artifact or repository change. Preserve unrelated user content, encoding, line endings, and naming conventions.

For high-impact canon changes, include a compact impact note covering affected characters, factions, systems, chronology, quests, and localization. Do not propagate speculative changes as canon without approval.
