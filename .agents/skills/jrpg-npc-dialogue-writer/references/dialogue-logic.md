# Isekai Expansion dialogue logic

## Relationship tiers

- `normal`: stranger, guarded contact, business relationship, or earned condescension.
- `friendly`: familiar acquaintance, reliable comrade, emerging interest, or guarded warmth.
- `trust`: confidant, tested loyalty, private vulnerability, or exclusive tenderness.
- `married`: established mutual commitment, deep familiarity, protection, and loyalty.

Treat these as behavioral ranges, not mandatory emotional stereotypes. A reserved character can remain reserved at every tier while changing what they permit, reveal, or prioritize.

## Context neutrality

Dialogue may trigger in town, wilderness, combat-adjacent space, or a dungeon. Do not mention a specific place, weather condition, nearby object, physical activity, or journey unless the trigger guarantees it.

Gift and trade contents may be dynamic. Do not name a specific item unless its ID or event contract guarantees that item. Use character-appropriate category language such as supplies, materials, relics, provisions, or fragments.

## Trade semantics

The trade menu consumes player currency or items.

- Never claim that a trade is free or that no payment is required.
- At low relationship tiers, emphasize price, value, scrutiny, or equivalent exchange as appropriate to the character.
- At high tiers, discounts, partner privileges, subsidized costs, teasing premiums, or private terms are allowed only when they remain compatible with the mechanical payment.

## Farewell semantics

`farewell` means the dialogue interface closed; it does not guarantee physical departure.

- Do not write a dramatic goodbye, safe-travel wish, return-home request, or promise to wait elsewhere.
- End the exchange while allowing the player to remain nearby: return attention to the task, continue exploring, or signal that the NPC remains present.

## Requirement and denial text

Avoid fourth-wall UI vocabulary such as relationship points, interaction range, menu state, or required tier. Express the cause through observable behavior or the character's worldview while keeping the remedy understandable.

Examples of useful transformation:

- distance failure -> voice, attention, magic, or perception cannot reach; invite the player closer;
- insufficient trust -> guarded posture, withheld access, or an unproven relationship;
- missing gift -> the player does not appear to be holding an appropriate offering.

## `is_married` multiplayer modifier

When a key contains `is_married`, the NPC is married to a different player. The current player is an outsider, acquaintance, or friend.

- Do not flirt, blush romantically, imply availability, or express partner-exclusive intimacy.
- Maintain a natural boundary appropriate to the character.
- Mention the spouse only when it improves clarity or voice; do not mechanically repeat the spouse in every line.

## Phase and proposal consistency

- `initial` at `trust` or `married` must not act like a first meeting.
- `engage_denied_already` means the NPC is already engaged or married. React as recognition, exasperation, humor, or boundary reinforcement—not confusion about the ring.
- `engage_denied_unready` means commitment is premature:
  - `normal`: reject presumption or unserious behavior;
  - `friendly`: acknowledge that the relationship is moving too quickly;
  - `trust`: communicate genuine attachment while asking for time or resolving an obstacle.

## Choice and placeholder rules

- Preserve `{player}`, `{name}`, and every other supplied placeholder exactly.
- Do not introduce a placeholder that the runtime does not define.
- Avoid `[action]` or `【action】` wrappers. For a pure-action choice, use the action naturally. For a spoken choice, prefer the spoken line without redundant stage direction.
- If the schema requires a response for a choice but none exists, use `{EMPTY}` only as defined by the user's generator contract.
