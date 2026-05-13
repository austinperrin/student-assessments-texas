from __future__ import annotations

import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
FORBIDDEN_PATTERNS = [
    re.compile(r"/C:/Users/", re.IGNORECASE),
    re.compile(r"C:/Users/", re.IGNORECASE),
    re.compile(r"C:\\Users\\", re.IGNORECASE),
    re.compile(r"/Users/"),
    re.compile(r"/home/"),
    re.compile(r"file://", re.IGNORECASE),
]
SKIP_PARTS = {".git", ".venv", ".tmp", "focus_file_parsers", "node_modules"}


def iter_markdown_files() -> list[Path]:
    files: list[Path] = []
    for path in REPO_ROOT.rglob("*.md"):
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        files.append(path)
    return sorted(files)


def normalize_link_target(raw_target: str) -> str:
    target = raw_target.strip()
    if target.startswith("<") and target.endswith(">"):
        target = target[1:-1].strip()
    return target


def is_external_or_anchor_link(target: str) -> bool:
    lowered = target.lower()
    return (
        not target
        or target.startswith("#")
        or lowered.startswith("http://")
        or lowered.startswith("https://")
        or lowered.startswith("mailto:")
    )


def validate_relative_links(path: Path, text: str, errors: list[str]) -> None:
    for match in MARKDOWN_LINK_RE.finditer(text):
        target = normalize_link_target(match.group(1))
        if is_external_or_anchor_link(target):
            continue

        clean_target = target.split("#", 1)[0].split("?", 1)[0]
        resolved_path = (path.parent / clean_target).resolve()

        try:
            resolved_path.relative_to(REPO_ROOT)
        except ValueError:
            errors.append(f"{path}: link target '{target}' resolves outside the repository")
            continue

        if not resolved_path.exists():
            errors.append(f"{path}: relative link target '{target}' does not exist")


def main() -> int:
    errors: list[str] = []
    files = iter_markdown_files()

    for path in files:
        text = path.read_text(encoding="utf-8")
        for pattern in FORBIDDEN_PATTERNS:
            if pattern.search(text):
                errors.append(f"{path}: contains forbidden machine-specific or file URI path matching '{pattern.pattern}'")
        validate_relative_links(path, text, errors)

    if errors:
        print("Documentation validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validated {len(files)} markdown files successfully.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
