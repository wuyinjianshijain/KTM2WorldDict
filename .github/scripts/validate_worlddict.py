#!/usr/bin/env python3
"""WorldDict 词条结构校验。

检查《KTM2》WorldDict 的设定文件是否满足 AUTHORING_GUIDE.md 第 5 节的验收要求：
UTF-8 编码、frontmatter 完整、id 唯一、状态与类型取值合法、相对链接有效。

用法：
    python .github/scripts/validate_worlddict.py           # 校验全库
    python .github/scripts/validate_worlddict.py Characters/Foo.md   # 只校验指定文件

不依赖第三方库，Python 3.9 以上即可运行。校验失败时以退出码 1 结束。
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote

# Windows 控制台默认编码可能无法输出中文，这里统一按 UTF-8 打印，避免脚本直接崩掉。
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

REPO = Path(__file__).resolve().parents[2]

# 需要校验的词条目录；其余目录（.agents、.github、.claude）是工具与流程文件，不套用词条规范。
CONTENT_DIRS = ["Characters", "Factions", "Locations", "Lore", "Races", "Systems"]
ROOT_DOCS = [
    "README.md",
    "AUTHORING_GUIDE.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "MIGRATION_REPORT.md",
]

REQUIRED_KEYS = ["id", "type", "title", "status", "updated"]
VALID_STATUS = {"canon", "draft", "unknown", "conflict", "deprecated"}
VALID_TYPE = {
    "character", "location", "faction", "race", "lore", "system",
    "index", "guide", "report",
}

ID_PATTERN = re.compile(r"^[a-z][a-z0-9]*\.[a-z0-9-]+$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(\s*([^)\s]+)")
FENCE_PATTERN = re.compile(r"^\s*(```|~~~)")


class Problem:
    def __init__(self, path: Path, line: int, message: str) -> None:
        self.path = path
        self.line = line
        self.message = message

    def __str__(self) -> str:
        rel = self.path.relative_to(REPO).as_posix()
        where = f"{rel}:{self.line}" if self.line else rel
        return f"  {where}\n      {self.message}"


def parse_frontmatter(text: str) -> tuple[dict[str, object], int]:
    """解析 frontmatter 的最小实现：支持 `键: 值` 与 `键:` + `  - 列表项`。

    返回 (字段字典, frontmatter 结束行号)。没有 frontmatter 时返回 ({}, 0)。
    """
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return {}, 0

    data: dict[str, object] = {}
    current_list_key: str | None = None
    for index in range(1, len(lines)):
        raw = lines[index]
        if raw.strip() == "---":
            return data, index + 1
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        if raw.startswith((" ", "\t")) and raw.lstrip().startswith("- "):
            if current_list_key:
                data.setdefault(current_list_key, [])
                value = data[current_list_key]
                if isinstance(value, list):
                    value.append(raw.lstrip()[2:].strip())
            continue
        if ":" in raw:
            key, _, value = raw.partition(":")
            key, value = key.strip(), value.strip()
            if value:
                data[key] = value.strip("'\"")
                current_list_key = None
            else:
                data[key] = []
                current_list_key = key
    return data, 0


def strip_code_blocks(text: str) -> list[tuple[int, str]]:
    """返回 (行号, 行内容)，跳过围栏代码块与行内代码，避免把示例当成真实链接。"""
    result: list[tuple[int, str]] = []
    in_fence = False
    for number, line in enumerate(text.split("\n"), start=1):
        if FENCE_PATTERN.match(line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        result.append((number, re.sub(r"`[^`]*`", "``", line)))
    return result


def collect_targets(paths: list[str] | None) -> list[Path]:
    if paths:
        return [Path(p).resolve() for p in paths]
    files = [REPO / name for name in ROOT_DOCS if (REPO / name).exists()]
    for directory in CONTENT_DIRS:
        files.extend(sorted((REPO / directory).glob("*.md")))
    return files


def check_file(path: Path, seen_ids: dict[str, Path]) -> list[Problem]:
    problems: list[Problem] = []
    raw = path.read_bytes()

    if raw.startswith(b"\xef\xbb\xbf"):
        problems.append(Problem(path, 1, "文件带有 UTF-8 BOM，请另存为不带 BOM 的 UTF-8。"))
        raw = raw[3:]
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as error:
        problems.append(Problem(path, 0, f"文件不是有效的 UTF-8：{error}"))
        return problems

    data, _ = parse_frontmatter(text)
    if not data:
        problems.append(Problem(
            path, 1,
            "缺少 frontmatter。词条开头需要 --- 包裹的 id / type / title / status / tags / updated。",
        ))
    else:
        for key in REQUIRED_KEYS:
            if not data.get(key):
                problems.append(Problem(path, 1, f"frontmatter 缺少必填字段：{key}"))

        entry_id = data.get("id")
        if isinstance(entry_id, str) and entry_id:
            if not ID_PATTERN.match(entry_id):
                problems.append(Problem(
                    path, 1,
                    f"id「{entry_id}」格式不合规。应为 `分类.短横线名`，例如 `location.world-forge`。",
                ))
            if entry_id in seen_ids:
                other = seen_ids[entry_id].relative_to(REPO).as_posix()
                problems.append(Problem(path, 1, f"id「{entry_id}」与 {other} 重复。id 必须全库唯一。"))
            else:
                seen_ids[entry_id] = path

        status = data.get("status")
        if isinstance(status, str) and status and status not in VALID_STATUS:
            problems.append(Problem(
                path, 1,
                f"status「{status}」不在允许取值内：{' / '.join(sorted(VALID_STATUS))}。",
            ))

        entry_type = data.get("type")
        if isinstance(entry_type, str) and entry_type and entry_type not in VALID_TYPE:
            problems.append(Problem(
                path, 1,
                f"type「{entry_type}」不在允许取值内：{' / '.join(sorted(VALID_TYPE))}。",
            ))

        updated = data.get("updated")
        if isinstance(updated, str) and updated and not DATE_PATTERN.match(updated):
            problems.append(Problem(path, 1, f"updated「{updated}」应为 YYYY-MM-DD 格式。"))

        tags = data.get("tags")
        if isinstance(tags, list) and not tags:
            problems.append(Problem(path, 1, "tags 为空。至少写一个标签，方便检索与归类。"))

    for number, line in strip_code_blocks(text):
        for target in LINK_PATTERN.findall(line):
            if target.startswith(("http://", "https://", "mailto:", "#", "<")):
                continue
            local = unquote(target.split("#", 1)[0]).strip()
            if not local:
                continue
            if not (path.parent / local).exists():
                problems.append(Problem(path, number, f"链接失效：{target}"))

    return problems


def main(argv: list[str]) -> int:
    targets = collect_targets(argv[1:])
    seen_ids: dict[str, Path] = {}
    problems: list[Problem] = []

    for path in targets:
        if not path.exists():
            print(f"跳过不存在的文件：{path}")
            continue
        problems.extend(check_file(path, seen_ids))

    print(f"已检查 {len(targets)} 个文件。")
    if not problems:
        print("校验通过：frontmatter、id、状态与链接都没有问题。")
        return 0

    print(f"\n发现 {len(problems)} 处问题：\n")
    for problem in problems:
        print(problem)
    print("\n修改方法见 AUTHORING_GUIDE.md 与 CONTRIBUTING.md。")
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
