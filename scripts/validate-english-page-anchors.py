#!/usr/bin/env python3
"""Validate English source-page anchoring against verified Tamil page records.

The validator deliberately does not compare paragraph counts.  It checks marker
coverage/order, non-empty translated content for source pages that contain story
text, printed-page agreement, and optional human-adjudicated start/end anchors.

Usage:
    python3 scripts/validate-english-page-anchors.py stories/<slug>
    python3 scripts/validate-english-page-anchors.py --self-test
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


MARKER_RE = re.compile(
    r"<!--\s*(?:(?:source|anthology)\s+scan(?:\s+page)?)\s*:?\s*(\d+)"
    r"\s*;\s*printed\s+page\s*:?\s*([0-9]+|—|-)\s*-->",
    re.IGNORECASE,
)
COMMENT_RE = re.compile(r"<!--.*?-->", re.DOTALL)
FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.DOTALL)
FIELD_RE = re.compile(r"^([A-Za-z_]+):\s*(.*?)\s*$")
APPARATUS_HEADING_RE = re.compile(
    r"(?mi)^\s*(?:#\s+அச்சு உரை|##\s+Source[- ]review note)\s*$"
)


@dataclass(frozen=True)
class PageInfo:
    scan: int
    printed_page: int | None
    has_story_text: bool
    path: str = ""


def parse_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'\"', "'"}:
        return value[1:-1]
    return value


def parse_page_record(path: Path) -> PageInfo:
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER_RE.match(text)
    if not match:
        raise ValueError(f"{path}: missing YAML front matter")

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        field_match = FIELD_RE.match(line)
        if field_match:
            fields[field_match.group(1)] = parse_scalar(field_match.group(2))

    if "scan_page" not in fields:
        raise ValueError(f"{path}: missing scan_page")
    scan = int(fields["scan_page"])

    printed_raw = fields.get("printed_page", "null")
    printed_page = None if printed_raw in {"null", "None", "—", "-"} else int(printed_raw)

    status = fields.get("status")
    if status != "verified":
        raise ValueError(f"{path}: expected status verified, found {status!r}")

    body = text[match.end() :]
    body = COMMENT_RE.sub("", body)
    body = APPARATUS_HEADING_RE.sub("", body)
    has_story_text = bool(body.strip())

    return PageInfo(scan=scan, printed_page=printed_page, has_story_text=has_story_text, path=str(path))


def parse_marker_printed(raw: str) -> int | None:
    return None if raw in {"—", "-"} else int(raw)


def clean_english_section(section: str) -> str:
    """Remove non-reading HTML comments but preserve headings and prose."""
    return COMMENT_RE.sub("", section).strip()


def validate_text(
    english_text: str,
    pages: Iterable[PageInfo],
    anchors: list[dict[str, object]] | None = None,
) -> list[str]:
    errors: list[str] = []
    expected_pages = sorted(pages, key=lambda page: page.scan)
    expected_scans = [page.scan for page in expected_pages]

    matches = list(MARKER_RE.finditer(english_text))
    actual_scans = [int(match.group(1)) for match in matches]

    if actual_scans != expected_scans:
        errors.append(
            "source marker scan sequence mismatch: "
            f"expected {expected_scans}, found {actual_scans}"
        )

    if len(set(actual_scans)) != len(actual_scans):
        errors.append("duplicate English source-page marker detected")

    sections: dict[int, str] = {}
    printed_by_scan: dict[int, int | None] = {}
    for index, match in enumerate(matches):
        scan = int(match.group(1))
        printed_by_scan[scan] = parse_marker_printed(match.group(2))
        section_end = matches[index + 1].start() if index + 1 < len(matches) else len(english_text)
        sections[scan] = english_text[match.end() : section_end]

    for page in expected_pages:
        if page.scan not in sections:
            continue
        marker_printed = printed_by_scan.get(page.scan)
        if marker_printed != page.printed_page:
            errors.append(
                f"scan {page.scan}: printed-page mismatch; "
                f"page record={page.printed_page}, English marker={marker_printed}"
            )

        clean = clean_english_section(sections[page.scan])
        if page.has_story_text and not clean:
            errors.append(
                f"scan {page.scan}: English marker section is empty even though "
                "the verified Tamil page record contains story text"
            )

    if anchors:
        anchor_scans = [int(anchor["scan"]) for anchor in anchors]
        if anchor_scans != expected_scans:
            errors.append(
                "anchor manifest scan sequence mismatch: "
                f"expected {expected_scans}, found {anchor_scans}"
            )

        for anchor in anchors:
            scan = int(anchor["scan"])
            if scan not in sections:
                continue
            clean = clean_english_section(sections[scan])
            expected_start = str(anchor.get("english_starts_with", ""))
            expected_end = str(anchor.get("english_ends_with", ""))
            expected_printed = anchor.get("printed_page")

            if expected_printed is not None and printed_by_scan.get(scan) != int(expected_printed):
                errors.append(
                    f"scan {scan}: anchor manifest printed page {expected_printed} "
                    f"does not match English marker {printed_by_scan.get(scan)}"
                )
            if expected_start and not clean.startswith(expected_start):
                actual_start = clean[:120].replace("\n", " ")
                errors.append(
                    f"scan {scan}: translated content does not begin at the "
                    f"human-reviewed source boundary; expected prefix {expected_start!r}, "
                    f"found {actual_start!r}"
                )
            if expected_end and not clean.endswith(expected_end):
                actual_end = clean[-120:].replace("\n", " ")
                errors.append(
                    f"scan {scan}: translated content does not end at the "
                    f"human-reviewed source boundary; expected suffix {expected_end!r}, "
                    f"found {actual_end!r}"
                )

    return errors


def load_story(story_dir: Path) -> tuple[str, list[PageInfo], list[dict[str, object]] | None]:
    slug = story_dir.name
    english_path = story_dir / "translations" / "en" / f"{slug}.md"
    if not english_path.exists():
        raise ValueError(f"missing English translation: {english_path}")

    page_paths = sorted((story_dir / "pages").glob("*.md"))
    if not page_paths:
        raise ValueError(f"no page records found under {story_dir / 'pages'}")
    pages = [parse_page_record(path) for path in page_paths]

    anchor_path = story_dir / "translations" / "en" / "page-anchors.json"
    anchors: list[dict[str, object]] | None = None
    if anchor_path.exists():
        data = json.loads(anchor_path.read_text(encoding="utf-8"))
        if data.get("story") != slug:
            raise ValueError(
                f"{anchor_path}: story={data.get('story')!r} does not match directory {slug!r}"
            )
        anchors = list(data.get("anchors", []))

    return english_path.read_text(encoding="utf-8"), pages, anchors


def run_self_test() -> int:
    pages = [
        PageInfo(scan=1, printed_page=10, has_story_text=True),
        PageInfo(scan=2, printed_page=11, has_story_text=True),
        PageInfo(scan=3, printed_page=12, has_story_text=True),
    ]
    anchors = [
        {"scan": 1, "printed_page": 10, "english_starts_with": "Alpha", "english_ends_with": "A-end"},
        {"scan": 2, "printed_page": 11, "english_starts_with": "Beta", "english_ends_with": "B-end"},
        {"scan": 3, "printed_page": 12, "english_starts_with": "Gamma", "english_ends_with": "C-end"},
    ]
    corrected = (
        "<!-- source scan 1; printed page 10 -->\nAlpha A-end\n\n"
        "<!-- source scan 2; printed page 11 -->\nBeta B-end\n\n"
        "<!-- source scan 3; printed page 12 -->\nGamma C-end\n"
    )
    shifted = (
        "<!-- source scan 1; printed page 10 -->\nAlpha A-end\n\nBeta B-end\n\n"
        "<!-- source scan 2; printed page 11 -->\nGamma C-end\n\n"
        "<!-- source scan 3; printed page 12 -->\n<!-- closing ornament -->\n"
    )

    first = validate_text(corrected, pages, anchors)
    negative = validate_text(shifted, pages, anchors)
    restored = validate_text(corrected, pages, anchors)

    if first:
        print("SELF-TEST corrected fixture: FAIL")
        print("\n".join(first))
        return 1
    print("SELF-TEST corrected fixture: PASS")

    if not negative:
        print("SELF-TEST shifted-marker fixture: UNEXPECTED PASS")
        return 1
    print("SELF-TEST shifted-marker fixture: EXPECTED FAIL")
    for error in negative:
        print(f"  - {error}")

    if restored:
        print("SELF-TEST restored fixture: FAIL")
        print("\n".join(restored))
        return 1
    print("SELF-TEST restored fixture: PASS")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("story_dir", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        return run_self_test()
    if args.story_dir is None:
        parser.error("story_dir is required unless --self-test is used")

    try:
        english_text, pages, anchors = load_story(args.story_dir)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    errors = validate_text(english_text, pages, anchors)
    if errors:
        print(f"FAIL {args.story_dir}")
        for error in errors:
            print(f"  - {error}")
        return 1

    scans = [page.scan for page in sorted(pages, key=lambda page: page.scan)]
    anchor_note = " with human-reviewed boundary anchors" if anchors else ""
    print(
        f"PASS {args.story_dir}: scans {scans[0]}–{scans[-1]} "
        f"are structurally anchored{anchor_note}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
