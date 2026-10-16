# Economy and progression reference

## Authority

Three sources, three jobs. Know which one answers the question before you price anything.

| Question | Source |
| --- | --- |
| What does an ordinary person earn, what does bread cost, why did prices move, what does a bounty mean in someone's life | KTM2 WorldDict: [`Lore/Economy_and_Livelihood.md`](../../../../Lore/Economy_and_Livelihood.md) |
| What should an item cost, which tier band, what sell-back ratio, does this recipe pass the crafting check | **this file** (see "KTM2 economic contract" below) |
| What does the game currently charge | the game's own docs: <https://kentomahou.com/zh-cn/wiki/trading/> and the mod's `trade_overrides` data |

The direction of authority is deliberate and unusual: **the contract in this file is the design target, and merchant offers align to it**, not the other way round. That is the one place where the KTM2 WorldDict ecosystem does not defer to shipped data.

The contract moved here from the WorldDict's former `Systems/Economy_System.md`, which was retired on 2026-10-16 along with the rest of that directory: a setting library should not host balance tables that drift against implementation. The WorldDict keeps the in-world half (wages, living costs, price causes, the bounty economy as an institution) because story and settlement writing needs it. Read that document first for anchors; read this file for the numbers derived from them.

Treat the generic sections below as method for any project. Treat the KTM2 section as binding for KTM2.

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

Use these bands as a first-pass scale and retune them against actual income-per-hour. For KTM2 use the T1-T5 tier table in the contract section instead: tiers track adventurer rank rather than material name, and each step is roughly `3.2x`.

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

## KTM2 economic contract

Binding for KTM2. Every value here is a **design target**; merchant offers align to it. When a shipped price disagrees, the shipped price is what gets corrected. Balance posture is **40 per cent plausibility, 60 per cent playability**: prices must survive the question "how does this person stay alive", but where realism and playability collide, playability wins and the reason gets written down.

### Currency contract

| Unit | UI mark | In copper | **Internal base** |
| --- | --- | ---: | ---: |
| Copper | C | 1 | `1` |
| Silver | S | 100 C | `100` |
| Gold | G | 100 S / 10,000 C | `10000` |

**The internal-base column is an implementation contract.** Every number in a merchant offer is an integer count of copper matching this file's C value: `12 S` here means `1200` in data. There is no conversion layer between document and implementation, and no second set of "game prices" is permitted. Display converts to G / S / C automatically.

Magic stones are not legal tender. The guild's stable buy price makes them look like hard currency, but the price moves with purity, regional demand, and phasing state.

### Living anchors

The in-world anchor set lives in the WorldDict ([`Lore/Economy_and_Livelihood.md`](../../../../Lore/Economy_and_Livelihood.md)) and is the geology every other price is derived from: day wages from `55-80 C` for unskilled labour up to `2-4 S` for border garrison, black bread `8 C`, stew `30 C`, beer `12 C`, standard inn room `80 C` per night, stable bunk `15 C`, public bath `12 C`. Read it before deriving anything; do not restate those numbers in a second place.

One consequence worth keeping in view while pricing: **a day labourer needs roughly two hundred days of wages to hold one gold coin.** Anything priced in gold is, to an ordinary resident, another world's price list.

### Food price formula

Food is not hand-priced per item; it is derived from comfort so new food needs no adjudication:

```
unit price = 8 + comfort * 4        (comfort >= 0)
unit price = 120 + |comfort| * 16   (comfort < 0: harmful or status food)
```

Comfort 0 yields black bread's `8 C`; comfort 28 yields a whole roast chicken at `120 C`; comfort 5 yields `28 C` against the stew anchor of `30 C`. Liquor takes a `48 C` floor. Signature dishes take the top of their band. This formula is live in implementation and is the part of the contract that is fully aligned.

### Tier price bands

All goods price into five tiers. Tiers track **adventurer rank, not material name**.

| Tier | Rank | Level | Weapon | Armour (full set) | Material / piece | Consumable |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| T1 | F-E | 1-12 | 300-600 | 600-1000 | 4-80 | 20-60 |
| T2 | E-D | 10-20 | 700-1800 | 1500-2800 | 80-400 | 60-250 |
| T3 | C | 15-30 | 1800-6000 | 4000-9000 | 400-1600 | 250-900 |
| T4 | B-A | 25-40 | 6500-20000 | 12000-30000 | 1600-7000 | 900-3000 |
| T5 | A-S | 30-50+ | 20000-60000 | 35000-90000 | 7000-30000 | 3000-12000 |

Values are in copper. **Each step is about 3.2x**, and the same ratio constrains equipment, materials, and bounty income, so "a few more jobs buys the next piece" holds at every stage. Do not reintroduce the uneven jumps an earlier revision used at T3 and T5 (6.7x and 11.3x), which decoupled late equipment from same-rank income.

- **Training and crude self-made gear sits below T1** and occupies no band: wood, stone, rope and practice equipment price at 50-60 per cent of T1. Its job is to give the player something before the first real purchase, not to form a tier.
- The consumable column covers **regular** consumables only: potions, antidotes, meal vouchers, things worth stocking. **Relic consumables** (one-shot reversals, experience and level elixirs, full-restore relics) form their own band at roughly 10x the same tier's regular consumable, and must be low-stock and low-weight. Conflating the two forces ordinary medicine to inflate, or turns relics into farmable staples.
- A few **special-source items** may exceed the T5 ceiling: safely reusable capital tools, enchant-slot extensions, full-restore relics, dimensional infrastructure. Their price comes from rarity and source character, not material tier, and they must be low-stock.

### Shop and salvage ratios

- Player sell price for equipment defaults to **40 per cent** of intact retail.
- General buy price for materials and loot is **20-35 per cent**; a specialist buyer pays **60-80 per cent** within their category.
- Worn equipment multiplies by **20-100 per cent** on remaining durability, enchant stability, and local demand.
- Goods of unknown provenance cannot move through ordinary shops. Black-market offers are low and raise the regional investigation value.
- Food, potions and single-use items are not bought back once they leave the shop, unless sealed and bearing a merchant-house seal.

The 40 per cent figure is a baseline for program and player expectation, not a law that every merchant in the world mysteriously obeys.

### Crafting incentive rule

The anti-farming rules need one checkable hard constraint, or "buying beats making" reappears quietly at high tiers:

> **retail price of output >= 4 x unit price of the main material.**

Iron validates it: iron ore `3 S`, iron sword `12 S`, exactly 4x, and self-crafting saves about half. An earlier revision violated it with mythril (ore `5 G` against a `9 G` sword: one ore was 55 per cent of the output, so crafting cost more than buying), corrected by repricing mythril ore to `1 G 30 S`. **Every new material and output must pass this check.**

### Bounty bands

The client posts a deposit; the guild takes a standard **10 per cent** for registration, investigation, rescue reserve, and liability. Rewards below are what the player sees after that cut. Danger rating measures the **worst outcome**, not the target's level.

| Rating | Stage | Money reward | Common extras |
| --- | --- | ---: | --- |
| F | Lv 1-5 | 50-150 C | small potion, meal voucher |
| E | Lv 5-12 | 3-8 S | iron gear, crude reinforcement stone |
| D | Lv 10-20 | 8-20 S | regional map, crafting permit |
| C | Lv 15-30 | 20-50 S | steel equipment, medium potion |
| B | Lv 25-40 | 50 S - 1 G 50 S | rare catalyst, faction introduction |
| A | Lv 30-50 | 1 G 50 S - 5 G | mythril, enchant permit |
| S | Lv 50+ | 10-30 G | causal relic, unpurchasable access |

Adjacent ratings are about **2.5-3x** apart (F-E and A-S are wider), in step with the tier bands, so **one piece of same-rank equipment is roughly one to four same-rank jobs**. Keep A's floor at `1 G 50 S` so it does not overlap B, and keep S at `10-30 G`; the older `30-100 G` was a twentyfold jump over A and broke the curve.

Failure is not automatically zero income. Completed escort legs, returned investigation evidence, and lawfully incurred rescue costs settle. Fraud, unauthorised escalation, and concealing a member's death are what trigger penalties and demotion.

### Reference prices

Services and consumables: stable bunk `15 C` per night (no full astral-energy recovery), standard room `80 C`, luxury suite `5 S`, public bath `12 C`, small potion `50 C`, medium potion `2 S` (4x the small), antidote `40 C`, revival feather `8 S` (sells back `3 S` sealed), basic equipment service `20-80 C`, shattered-space phasing appraisal `1-20 S`.

Equipment: novice cloth `50 C`, leather set T1 `8 S`, iron sword T2 `12 S`, steel longsword T3 `42 S`, mythril sword T5 `5 G 20 S`, dragonbone greatsword special `20 G`. The leather set was raised from `4 S` to `8 S` because a four-piece set must not undercut a same-tier single weapon; the dragonbone greatsword was cut from `150 G`, which was seventeen times the mythril sword and exceeded any band step.

Loot and materials: wood or stone T1 `4 C` (player income `1 C`), slime gel T1 `20 C` (`5 C`), wolf pelt T1 `1 S 50 C` (`45 C`), magic stone fragment T2 player income `5-10 C`, iron ore T2 `3 S` (`80 C`), standard magic stone T3 player income `40-60 C`, high-purity magic stone T3 `12-30 S` (`3-10 S`), mythril ore T5 `1 G 30 S` (`32 S 50 C`, one quarter of the sword), ancient coin special `50 G` through collectors.

**Monsters do not drop generic currency.** Coin comes from humanoid enemies' carried goods, job settlement, and lawful loot auction; monsters supply materials the real economy can absorb.

Food, furniture, housing: black bread `8 C`, beer `12 C`, stew `30 C`, roast chicken `1 S 20 C`, basic stool `30 C`, four-seat table `1 S 50 C`, ornate bedding `1 G 50 S`, border single-storey cottage `14-28 G`, urban terrace `40-120 G`, workshop or shop residence `45-180 G`, manor or strategic plot `150-400 G`. Furniture was cut deliberately (stool `80 C` to `30 C`, table `4 S` to `1 S 50 C`): decorating is bought in bulk, and pricing it against inn rates stalls the building loop. This is an explicit playability-over-realism call. The manor was cut from `300-800 G` so it equals ten to twenty S-rank jobs rather than eighty. The old "ordinary house 500-800 G" is retired: that price is generations of ordinary income and applies only to manors, core commercial property, or land carrying political rights.

### Regional and dynamic modifiers

Border normal: imports `+5-12%`. Monster-tide alert: medicine and arrows `+15-35%`. Star-tower outage: magitech services `+20-60%`. Harvest festival: staple food `-10%`, liquor demand up. Player-invested workshop: matching crafting costs `-5-15%`. Bulk dumping: category buy price steps down per batch, floor at 50 per cent of baseline.

**Dynamic prices must be explained by NPC dialogue, shelf changes, or notices.** Never move a number silently in the UI.

### Failure, anti-farming and soft-lock protection

- A bankrupt player recovers through guild meal vouchers, low-risk day-settled jobs, and pawning non-critical items. Missing one meal must never permanently block the main line.
- Quest-critical items, unique keepsakes and relationship gifts cannot be mis-sold to ordinary shops; they need separate confirmation or a buy-back channel.
- Merchant stock and cash are finite, but basic medicine, food and repair keep a floor guarantee.
- Housing tax and upkeep do not accrue to confiscation while the player is offline; long non-payment suspends benefits and operation without deleting decoration.
- Revival items do not substitute for narrative death. Combat "down" means dying, not dead; real death is a narrative state.
- **Cross-merchant arbitrage must be negative.** Every merchant's buy price must sit below every merchant's sell price for the same item, including indirect paths through crafting, conversion, and conditional differences. Ore sell prices must exceed the combined sell price of their expected outputs, or buying raw ore and decomposing it becomes a shortcut around scarcity.

### Implementation notes

- Store copper integers internally; convert to G / S / C in the display layer only.
- Every price table supports five modifier classes (region, reputation, supply and demand, state, difficulty) and shows their source in the breakdown.
- Name buy and sell **from the player's point of view**, so material tables cannot invert the shop's buy-back direction.
- Split bounty settlement into base reward, evidence reward, optional objectives, loss deductions, and goods.
