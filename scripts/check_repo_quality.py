#!/usr/bin/env python3
"""Lightweight repository quality checks for docs, examples, and links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
REQUIRED_FILES = [
    REPO_ROOT / "LICENSE",
    REPO_ROOT / "README.md",
    REPO_ROOT / "CONTRIBUTING.md",
    REPO_ROOT / "SECURITY.md",
    REPO_ROOT / "SUPPORT.md",
    REPO_ROOT / "CITATION.cff",
    REPO_ROOT / ".github" / "CODEOWNERS",
    REPO_ROOT / ".github" / "pull_request_template.md",
    REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "bug_report.md",
    REPO_ROOT / ".github" / "ISSUE_TEMPLATE" / "docs_improvement.md",
]


def check_required_files() -> list[str]:
    failures: list[str] = []
    for path in REQUIRED_FILES:
        if not path.exists():
            failures.append(f"missing required file: {path.relative_to(REPO_ROOT)}")
    return failures


def check_json_files() -> list[str]:
    failures: list[str] = []
    for path in REPO_ROOT.rglob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"invalid JSON in {path.relative_to(REPO_ROOT)}: {exc}")
    return failures


def should_skip_link(target: str) -> bool:
    return (
        not target
        or target.startswith("#")
        or target.startswith("http://")
        or target.startswith("https://")
        or target.startswith("mailto:")
    )


def resolve_link(source: Path, target: str) -> Path:
    clean_target = target.split("#", 1)[0]
    candidate = (source.parent / clean_target).resolve()
    if candidate.is_dir():
        readme = candidate / "README.md"
        if readme.exists():
            return readme
    return candidate


def check_markdown_links() -> list[str]:
    failures: list[str] = []
    for path in REPO_ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for match in MARKDOWN_LINK_RE.finditer(text):
            target = match.group(1).strip()
            if should_skip_link(target):
                continue
            resolved = resolve_link(path, target)
            if not resolved.exists():
                failures.append(
                    f"broken relative link in {path.relative_to(REPO_ROOT)} -> {target}"
                )
    return failures


def check_trailing_whitespace() -> list[str]:
    failures: list[str] = []
    for path in REPO_ROOT.rglob("*.md"):
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
            if line.rstrip() != line:
                failures.append(f"trailing whitespace in {path.relative_to(REPO_ROOT)}:{lineno}")
    return failures


def main() -> int:
    checks = [
        ("required files", check_required_files),
        ("JSON files", check_json_files),
        ("Markdown links", check_markdown_links),
        ("Markdown whitespace", check_trailing_whitespace),
    ]

    failures: list[str] = []
    for label, fn in checks:
        result = fn()
        if result:
            failures.extend(result)
        else:
            print(f"PASS {label}")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1

    print("PASS repository quality checks completed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
