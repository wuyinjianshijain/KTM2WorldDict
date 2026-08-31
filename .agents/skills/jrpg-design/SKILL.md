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
2. Inspect only the relevant project files and WorldDict sources. Treat `legacy/` as historical evidence, not current canon, unless the user promotes it.
3. Establish economic anchors before assigning exceptional prices. Read [economy-and-progression.md](references/economy-and-progression.md) for the authority order, the inherited currency model, and balancing checks. When the WorldDict is present, its `Systems/Economy_System.md` outranks the legacy anchors.
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

## Output contract

Return only what the user requested. For a full balance proposal, include:

1. assumptions and anchors;
2. the proposed values or rules;
3. acquisition and sink analysis;
4. exploit and progression checks;
5. implementation notes or a patch when requested.

Use tables for comparable prices or recipes. Include formulas and units so future maintainers can retune the system.
