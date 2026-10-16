# Game-doc sync

How a WorldDict stays true to a game that keeps changing, without turning back into a wiki.

## Why this file exists

The KTM2 WorldDict once carried a `Systems/` directory that documented stats, skill-tree nodes, spell lists, astral-energy costs and implementation progress, reconciled by hand against the mod's data. It failed in the predictable way. By the time it was retired on 2026-10-16 its magic document registered 24 spells against 49 shipped, and it framed "which schools still lack spells" as the open question while the game had meanwhile built an entire new layer — spell formulas, with chaining, infusion, harmony, reaction, load and tiers — that the document did not mention at all.

The lesson is not "reconcile harder". It is that **a setting library must not restate implementation.** Prose about meaning survives a patch; a table of values does not.

## When to run a sync

- **Before writing** any entry that touches a game-internal subject: magic, progression, aptitude, economy, status effects, travel, crafting.
- **After a release** that the user says changed systems.
- **When the user reports** that an entry contradicts the game.
- **Never on a schedule of your own.** This is a reconciliation pass, not a crawl; do not invent recurring maintenance work.

## Where the game docs live

For KTM2, published at <https://kentomahou.com/>, source checked out beside this repository:

| Path | Holds |
| --- | --- |
| `../kzeroko.github.io/src/content/wiki/{en,zh-cn}/` | player-facing systems: spells, formulas, talents, elements, status effects, trading, progression |
| `../kzeroko.github.io/src/content/dev/{en,zh-cn}/` | runtime and API documentation |
| `../kzeroko.github.io/src/content/codex/{en,zh-cn}/` | the site's own lore pages — compare these against WorldDict entries for terminology drift |
| `../IsekaiExpansion/` | the implementation itself, when a doc is ambiguous |

Read the `zh-cn` variant when the WorldDict is written in Chinese: it carries the established Chinese terminology, which is what the entry must match. Never hard-code a machine-local absolute path.

## The pass

1. **Identify the subject**, then find every game-doc page covering it. A subject usually spans several (`spell-formulas`, `spell-catalog`, `status-effects`, `talents` all describe one magic system).
2. **Extract terminology first.** Build the list of in-world names the game actually uses, in the document's own language. Terminology drift is the most common and most damaging form of rot: an entry that calls a thing by a retired name is wrong in a way readers cannot detect.
3. **Extract qualitative rules** — what is possible, what is forbidden, what the system refuses to do, what trades against what. These are what a WorldDict may carry.
4. **Leave every value behind.** Ratios, caps, costs, node counts, tier numbers, lists. If a sentence needs one to make sense, rewrite the sentence.
5. **Reconcile the entry.** Correct names, correct rules, add the world-internal meaning of anything newly shipped. Where the game added a system the entry never knew about, that is new lore to write, not a table to copy.
6. **Update the authority-boundary block** with the pages you read.
7. **Update the glossary** with every term whose preferred form, definition, or retired alternative changed.
8. **Record it** where the project records impact — for KTM2, `MIGRATION_REPORT.md` — naming what changed and why.
9. **Run the validator** and fix what it reports.

## What a synced entry looks like

Good, because a patch cannot falsify it:

> A weave that asks the world to rewrite more than it will tolerate in one breath is refused. The gesture completes, the incantation completes, and the manuscript does not answer.

Bad, because the next balance pass makes it a lie:

> Stability is capped at 100. Four sweep circles at a 48-degree arc reach 96.

Also bad, and the harder failure to notice, because it reads like setting:

> The twelve schools should each offer six core spells, for 72 in total; water and light currently have none.

That is project management wearing a lore costume. It declares a target the setting library has no authority to set, and it will be wrong within one release.

## Do not

- Copy a table, a formula, or a list from the game docs into an entry.
- State whether something is implemented, how complete it is, or what is missing.
- Set content targets, densities or roadmaps.
- Resolve a game-internal contradiction in the WorldDict's favour. The game docs win; the entry gets corrected.
- Write about a system from imagination because the game docs were not reachable. Say they were not reachable and keep the entry qualitative.
