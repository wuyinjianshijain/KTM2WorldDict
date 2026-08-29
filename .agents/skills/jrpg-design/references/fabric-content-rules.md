# Fabric and KubeJS implementation rules

## Project-first verification

Inspect the target repository before writing code. Determine:

- Minecraft, Fabric Loader, Fabric API, KubeJS, and add-on versions;
- the project's recipe and trade registration patterns;
- available item and tag IDs;
- whether generated data or runtime scripts own the content;
- existing validation or reload commands.

Do not assume that an API remembered from another modpack exists here.

## Tags

Prefer Fabric common tags such as `#c:logs`, `#c:iron_ingots`, and `#c:stripped_logs` when the installed versions and project conventions support them. Do not substitute `#forge:` tags in a Fabric project unless compatibility code intentionally defines them.

## Crafting responsibility

Classify each item before designing its acquisition path:

- **Hand craft:** crude assembly, survival improvisation, and low-complexity processing.
- **Workstation craft:** repeatable skilled production with a tool, station, fuel, or time gate.
- **Merchant/service:** specialist labor, regulated goods, or economic progression.
- **Loot/reward:** exploration, combat, reputation, or narrative payoff.

Use the classification as a design decision, not a universal realism rule.

## Legacy project-specific patterns

The Gemini-era skill referenced `.maxTrades(8)`, `.multiOffer(TradeItem...)`, and `.keepIngredient('mod:tool_id')`. Treat these as clues about an earlier project API. Search the current repository or dependency documentation and confirm signatures before using them. If they are unavailable, implement the same design intent through the project's supported API rather than inventing a compatible-looking call.

## Implementation safety

- Keep edits minimal and scoped.
- Preserve file encoding and line endings.
- Avoid reformatting unrelated scripts or generated data.
- Validate recipe counts and returned ingredients.
- Test reload/startup behavior when the user requested implementation.
- Report any unverified API assumption explicitly.
