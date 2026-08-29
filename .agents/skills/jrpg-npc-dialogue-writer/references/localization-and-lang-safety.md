# Localization and language-file safety

## Localization standard

- Write idiomatic target-language dialogue rather than preserving source syntax.
- Preserve intent, relationship distance, humor, register, and subtext.
- Avoid repetitive anime shorthand such as constant `笨蛋` or `本小姐` unless the character profile establishes a controlled frequency.
- Keep system feedback actionable while phrasing it inside the fiction.

## Preflight

Before changing `zh_cn.json`, `en_us.json`, or another localization file, record:

1. UTF encoding and whether a BOM is present;
2. newline style (`CRLF` or `LF`);
3. indentation and comma style;
4. `lang_comment` section boundaries and spacing;
5. current key order and whether duplicate keys exist;
6. the exact key set authorized by the user.

Do not normalize the complete file as a side effect of a small migration.

## Isekai Expansion migration

When the user explicitly requests the legacy `lang migrate` behavior:

- insert localized values into `zh_cn.json`;
- mirror the exact new keys in `en_us.json` with `""` values unless the user requests English localization;
- group keys under the matching `lang_comment` sections such as `dialogues`, `npc_miscellaneous`, or `npc_parent_menu`;
- retain one empty line before an established section marker if that is the file's convention;
- preserve existing section headings, spacing, BOM, and unrelated values;
- create a missing menu or miscellaneous key only when it belongs to the requested NPC/key set and is required for completeness;
- never edit a similarly named but unrelated localization key.

## Verification

After editing:

1. inspect a minimal diff;
2. parse both JSON files with UTF-8 BOM awareness;
3. check duplicate keys;
4. confirm every migrated key exists in both files;
5. confirm mirrored `en_us` values are empty when required;
6. confirm the inserted `zh_cn` values and placeholders match the approved source;
7. confirm BOM and newline style are unchanged.

Suggested command:

```powershell
python scripts/validate_lang_json.py zh_cn.json --peer en_us.json --keys-file dialogue_keys_zh_cn.json --require-bom --require-empty-peer --require-values-match-source
```
