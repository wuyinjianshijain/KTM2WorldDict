#!/usr/bin/env python3
"""Validate localization JSON without rewriting it."""

from __future__ import annotations

import argparse
import codecs
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


class ValidationError(Exception):
    pass


@dataclass
class JsonFile:
    path: Path
    value: dict[str, Any]
    has_bom: bool
    newline: str


def reject_duplicate_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValidationError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def detect_newline(data: bytes) -> str:
    without_crlf = data.replace(b"\r\n", b"")
    kinds = []
    if b"\r\n" in data:
        kinds.append("CRLF")
    if b"\n" in without_crlf:
        kinds.append("LF")
    if b"\r" in without_crlf:
        kinds.append("CR")
    if len(kinds) > 1:
        raise ValidationError(f"mixed newline styles: {', '.join(kinds)}")
    return kinds[0] if kinds else "none"


def load_json_file(path: Path, require_bom: bool = False) -> JsonFile:
    try:
        data = path.read_bytes()
    except OSError as exc:
        raise ValidationError(f"cannot read {path}: {exc}") from exc

    has_bom = data.startswith(codecs.BOM_UTF8)
    if require_bom and not has_bom:
        raise ValidationError(f"{path} does not start with a UTF-8 BOM")

    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise ValidationError(f"{path} is not valid UTF-8: {exc}") from exc

    try:
        value = json.loads(text, object_pairs_hook=reject_duplicate_pairs)
    except (json.JSONDecodeError, ValidationError) as exc:
        raise ValidationError(f"invalid JSON in {path}: {exc}") from exc

    if not isinstance(value, dict):
        raise ValidationError(f"{path} must contain a top-level JSON object")

    return JsonFile(path=path, value=value, has_bom=has_bom, newline=detect_newline(data))


def load_key_source(path: Path) -> tuple[list[str], dict[str, Any]]:
    source = load_json_file(path)
    return list(source.value), source.value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("primary", type=Path, help="Localized JSON file to validate")
    parser.add_argument("--peer", type=Path, help="Mirrored locale JSON file")
    parser.add_argument("--keys-file", type=Path, help="JSON object defining the target key set")
    parser.add_argument("--require-bom", action="store_true", help="Require UTF-8 BOM on primary and peer")
    parser.add_argument("--require-empty-peer", action="store_true", help="Require target peer values to be empty strings")
    parser.add_argument(
        "--require-values-match-source",
        action="store_true",
        help="Require primary target values to equal values in --keys-file",
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    errors: list[str] = []

    try:
        if args.require_empty_peer and not args.peer:
            raise ValidationError("--require-empty-peer requires --peer")
        if args.require_values_match_source and not args.keys_file:
            raise ValidationError("--require-values-match-source requires --keys-file")

        primary = load_json_file(args.primary, args.require_bom)
        peer = load_json_file(args.peer, args.require_bom) if args.peer else None

        if args.keys_file:
            target_keys, source_values = load_key_source(args.keys_file)
        else:
            target_keys = list(primary.value)
            source_values = None

        for key in target_keys:
            if key not in primary.value:
                errors.append(f"primary is missing key: {key}")

        if args.require_values_match_source and source_values is not None:
            for key in target_keys:
                if key in primary.value and primary.value[key] != source_values[key]:
                    errors.append(f"primary value differs from source for key: {key}")

        if peer:
            for key in target_keys:
                if key not in peer.value:
                    errors.append(f"peer is missing key: {key}")
                elif args.require_empty_peer and peer.value[key] != "":
                    errors.append(f"peer value is not empty for key: {key}")

            if not args.keys_file:
                primary_only = sorted(set(primary.value) - set(peer.value))
                peer_only = sorted(set(peer.value) - set(primary.value))
                errors.extend(f"peer is missing key: {key}" for key in primary_only)
                errors.extend(f"primary is missing peer key: {key}" for key in peer_only)

        if errors:
            for error in errors:
                print(f"ERROR: {error}", file=sys.stderr)
            return 1

        peer_summary = ""
        if peer:
            peer_summary = f"; peer={peer.path} ({len(peer.value)} keys, {peer.newline}, BOM={peer.has_bom})"
        print(
            f"OK: {primary.path} ({len(primary.value)} keys, {primary.newline}, BOM={primary.has_bom}); "
            f"checked {len(target_keys)} target keys{peer_summary}"
        )
        return 0
    except ValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
