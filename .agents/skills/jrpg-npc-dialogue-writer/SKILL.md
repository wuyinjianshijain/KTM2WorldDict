---
name: jrpg-npc-dialogue-writer
description: Explicit-invocation-only workflow for writing, polishing, validating, or migrating lore-consistent JRPG NPC dialogue and Isekai Expansion localization JSON. Use only when the user explicitly invokes `$jrpg-npc-dialogue-writer`, names `jrpg-npc-dialogue-writer`, or directly says to use the JRPG NPC dialogue writer skill. Do not activate merely because a request mentions NPCs, dialogue, localization, JSON, relationships, or the Isekai Expansion mod.
---

# JRPG NPC Dialogue Writer

## Activation boundary

Apply this workflow only after explicit invocation. If this skill was loaded without the user naming or requesting it, do not apply its rules.

Keep the scope to NPC dialogue, choice text, requirement text, localization, and explicitly requested language-file migration. Do not create or restructure WorldDict character files unless the user asks.

## Required source pass

Before drafting:

1. Inspect the supplied keys and identify route, phase, relationship tier, modifiers, placeholders, and target language.
2. Locate the relevant character profile from the user-provided path or current WorldDict. Search by canonical name and aliases; do not assume one fixed filename.
3. Extract a compact voice lock: identity, present goal, temperament, social posture, faction vocabulary, forbidden behaviors, and how the relationship tier changes expression.
4. Mark missing facts as unknown. Ask only when a missing fact would materially change the requested dialogue; otherwise make a conservative, reversible choice.
5. Take character facts, voice and relationships from the WorldDict; take mechanical facts (stats, spells, tiers, prices, what is implemented) from the game's own docs (for KTM2: <https://kentomahou.com/>). A WorldDict carries no values by design, and a character card's combat and personal-arc sections are explicitly marked WIP and non-canon - never let a line assert a mechanic or a quest outcome sourced from them.
6. For Isekai Expansion interaction keys, read [dialogue-logic.md](references/dialogue-logic.md) before writing.

## Drafting workflow

1. Apply mechanical semantics before characterization. A beautiful line that contradicts the game event is invalid.
2. Localize rather than translate literally. Use natural cadence, subtext, and character-specific vocabulary without stock anime verbal tics.
3. Keep trigger context neutral unless the key or user provides a guaranteed scene or item.
4. Preserve input key order, hierarchy, placeholders, escaping, and requested empty values.
5. Perform separate passes for event logic, relationship boundaries, voice, repetition, placeholders, and JSON validity.
6. Return only the requested fragment or edit. Do not fill unrelated empty keys.

## File-editing workflow

When the user explicitly asks to edit or migrate language files, read [localization-and-lang-safety.md](references/localization-and-lang-safety.md) first.

- Inspect encoding, BOM, newline style, indentation, section layout, and key ordering before editing.
- Preserve UTF-8 BOM when present or required by the project.
- Make a surgical edit; do not parse and reserialize the complete file if that would alter formatting.
- Preserve `lang_comment` section markers and unrelated entries byte-for-byte where practical.
- Store temporary artifacts outside the project workspace when the environment permits it.
- Inspect the diff and run `scripts/validate_lang_json.py` after editing.

## Output quality bar

- Dialogue must sound spoken, not like a lore encyclopedia or riddle generator. A line that only makes sense to someone who has read the lore entry has failed, however accurate it is.
- When writing many NPCs or many keys in one pass, compare the finished lines side by side and check skeletons rather than vocabulary. Distinct word choice does not prevent a whole cast from sharing one rhetorical shape. Full method: [character-voice-and-dialogue.md](../jrpg-world-building-game-design/references/character-voice-and-dialogue.md).
- A line should reveal personality through choice of words, rhythm, evasion, humor, or restraint.
- Intimacy must match the actual relationship state and multiplayer spouse semantics.
- Requirement and rejection text should remain immersive without obscuring the player's actionable meaning.
- Avoid bracketed stage directions in choice text unless the established localization schema requires them.
- Use `{EMPTY}` only when the supplied dialogue contract requires an absent choice response.
