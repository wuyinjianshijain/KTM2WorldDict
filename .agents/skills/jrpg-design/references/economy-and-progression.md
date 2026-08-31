# Economy and progression reference

## Authority

When the KTM2 WorldDict is available (this repository, or checked out beside the target project), [`Systems/Economy_System.md`](../../../../Systems/Economy_System.md) is the economic authority. Its currency contract, tier price bands, food formula, and crafting-incentive rule are design targets that merchant offers align to, not the other way round. Read it first; treat this file as fallback for projects that have no such document, and as balancing method regardless.

## Inherited anchors

Use these as legacy defaults, not immutable canon. Prefer current project data or explicit user direction when they conflict. Two entries below are already superseded for KTM2 and must not be reused there: iron is `3 S` per ore and `12 S` per sword rather than `12 C` per ingot, and the progression bands are replaced by the T1-T5 tier table.

- `1 copper (C) = 1 value point`
- `1 silver (S) = 100 C`
- `1 gold (G) = 100 S = 10,000 C`
- subsistence food: approximately `5-8 C`
- ordinary prepared meal: approximately `30-50 C`
- iron ingot: approximately `12 C`
- wood log retail value: approximately `4 C`
- ordinary merchant sell-back: approximately `40%` of buy price

The old design used a `3-5x` merchant premium for gatherable monster drops and raw materials. Retain it only when the intended behavior is to reward field acquisition and when it cannot create a profitable conversion loop.

## Progression bands

Use these bands as a first-pass scale and retune them against actual income-per-hour. Where the WorldDict economy doc exists, use its T1-T5 tier table instead: tiers track adventurer rank rather than material name, and each step is roughly `3.2x`.

| Band | Legacy range | Intended role |
|---|---:|---|
| Early | `10-200 C` | basic tools, bait, food, common utility |
| Mid | `500-3,000 C` | standard adventurer equipment and workstations |
| Late | `4,000-25,000 C` | elite equipment and major utility purchases |
| Mythic | `50,000 C+` | scarce artifacts and deliberate long-term goals |

Do not price solely from tier labels. Compare the price with expected income, replacement frequency, combat impact, convenience, and whether the item is mandatory.

## Derived-price model

Start with:

`base value = material cost + labor margin + scarcity premium + risk premium`

Then apply progression and behavior modifiers only when justified:

`final value = base value × progression gate × convenience factor × supply modifier`

For a recipe output quantity `q`, the no-arbitrage floor is:

`unit floor = sum(merchant sell value of consumed inputs) / q`

Account for returned containers, persistent tools, by-products, durability loss, fuel, and reversible recipes.

## Balance checks

1. **Income clock:** Estimate how many minutes of appropriate play buy the item.
2. **Required-vs-optional:** Required progression items need a predictable path; luxuries may be volatile.
3. **Crafting arbitrage:** Compare input buy prices, output sell prices, by-products, and reverse recipes.
4. **Renewability:** Renewable automation must not dominate intended exploration or combat income.
5. **Merchant cycling:** Random pools and refresh timing must not make mandatory items inaccessible.
6. **Multiplayer:** Check gifting, alternate accounts, shared storage, and profession specialization.
7. **Currency sinks:** Repairs, services, travel, housing, rerolls, and cosmetics should not all punish the same player segment.
8. **Inflation resilience:** Prefer percentage or tier-aware sinks when player wealth can grow without bound.

## Merchant design

- Keep frequently used necessities stable and discoverable.
- Randomize optional breadth rather than mandatory progression.
- Consolidate cosmetic variants when the project API supports a safe multi-offer mechanism.
- Give specialist merchants a clear economic identity instead of overlapping universal catalogs.
- Move advanced equipment from hand crafting to merchants or loot only when that strengthens the desired loop; do not enforce the divide universally.
