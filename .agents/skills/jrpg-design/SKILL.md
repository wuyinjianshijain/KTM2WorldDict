---
name: jrpg-design
description: Explicit-invocation-only JRPG economy and game-content balancing workflow for currencies, prices, loot values, merchant catalogs, crafting progression, and KubeJS Fabric implementation. Use only when the user explicitly invokes `$jrpg-design`, names `jrpg-design`, or directly says to use the JRPG design skill. Do not activate from an ordinary discussion of JRPGs, economies, merchants, recipes, balancing, or modpacks.
---

# JRPG Economy and Content Design

## Activation boundary

Apply this workflow only after explicit invocation. If this skill was loaded without the user naming or requesting it, do not apply its rules.

Keep this skill focused on economic and implementable game-content design. Route setting and canon work to `$jrpg-world-building-game-design` only when the user explicitly invokes that skill. Route NPC prose and localization to `$jrpg-npc-dialogue-writer` only when explicitly invoked.

## Workflow

1. Identify the requested deliverable: balance analysis, price table, merchant pool, recipe policy, KubeJS patch, or review.
2. Inspect only the relevant project files and WorldDict sources. Treat `legacy/` as historical evidence, not current canon, unless the user promotes it. Read in-world anchors from the WorldDict and shipped prices from the game's own docs (<https://kentomahou.com/zh-cn/wiki/trading/>); do not take a number from the WorldDict, which by design carries none beyond the living anchors.
3. Establish economic anchors before assigning exceptional prices. Read [economy-and-progression.md](references/economy-and-progression.md) first: its Authority section states which of three sources answers which question, and its KTM2 economic contract section holds the binding currency contract, tier bands, food formula, crafting check, bounty bands and reference prices. That contract lives in this skill, not in the WorldDict - the WorldDict holds the in-world anchors (wages, living costs, price causes) that the contract is derived from, and **never** holds balance tables.
4. Derive processed-item values from inputs, labor, scarcity, risk, progression gate, and intended player behavior. Explain deliberate deviations.
5. Test acquisition loops, resale, crafting decomposition, renewable inputs, merchant refreshes, and multiplayer transfer for exploits.
6. Translate the design into the requested artifact. When editing Fabric/KubeJS content, read [fabric-content-rules.md](references/fabric-content-rules.md) first and verify project-local APIs before using legacy builder methods.
7. Verify arithmetic, units, identifiers, tags, key order when relevant, and the final diff. Do not rewrite unrelated files or rebalance content outside scope.

## Design rules

- Treat prices as player-behavior controls, not lore decoration.
- Keep ordinary life affordable enough to make the world legible; reserve extreme prices for real progression gates.
- Make gathering, crafting, questing, and trading occupy distinct economic roles.
- Prefer a small number of explicit anchors and formulas over hundreds of disconnected hand-tuned values.
- State assumptions and confidence when source data is incomplete.
- Separate design recommendation from confirmed project behavior.
- Do not invent mod IDs, recipe APIs, trade builders, item counts, or tags.
- Preserve existing formatting, encoding, and surrounding code when implementing changes.
- Do not write balance tables, tier bands or price contracts into a WorldDict entry. When a pricing decision needs recording, it belongs in this skill's economy reference; what the WorldDict may gain is the in-world consequence (who can now afford what, who got squeezed).

## Output contract

Return only what the user requested. For a full balance proposal, include:

1. assumptions and anchors;
2. the proposed values or rules;
3. acquisition and sink analysis;
4. exploit and progression checks;
5. implementation notes or a patch when requested.

Use tables for comparable prices or recipes. Include formulas and units so future maintainers can retune the system.
