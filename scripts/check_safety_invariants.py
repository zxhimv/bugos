#!/usr/bin/env python3
"""Local safety-invariant checker for bugos.

This script is intentionally conservative. It scans repository text files for
high-risk regressions that would weaken the offline-first and human-review
safety model.

It performs no network access and does not import project runtime modules.
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_RELATIVE_PATH = Path("scripts/check_safety_invariants.py")

TEXT_SUFFIXES = {
    ".md",
    ".py",
    ".json",
    ".toml",
    ".yaml",
    ".yml",
    ".txt",
}

SKIP_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    "build",
    "dist",
    "demo_out",
}

# Build forbidden strings from fragments so this checker does not match its own
# source code while scanning the repository.
FORBIDDEN_TEXT_PATTERNS = [
    "automatic_submission_allowed" + "\": " + "true",
    "automatic_submission_allowed" + ": " + "true",
    "decision" + "\": \"" + "ALLOW" + "\"",
    "decision" + ": " + "ALLOW",
    "final decision" + ": " + "ALLOW",
]

HIGH_RISK_TERMS = {
    "scanner": "Scanner language requires human review unless it is an explicit prohibition.",
    "exploit": "Exploit language requires human review unless it is an explicit prohibition.",
    "payload": "Payload language requires human review unless it is an explicit prohibition.",
    "credential": "Credential language requires human review unless it is an explicit prohibition.",
    "password reset": "Password-reset language requires human review unless it is an explicit prohibition.",
    "automatic submission": "Automatic-submission language requires human review unless it is an explicit prohibition.",
}

ALLOWED_NEGATING_CONTEXT = [
    "no ",
    "not ",
    "never ",
    "must not",
    "do not",
    "without ",
    "prohibited",
    "blocked",
    "disabled",
    "disallowed",
    "false",
    "remain disabled",
    "must remain disabled",
]


def iter_files() -> list[Path]:
    files: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
    return sorted(files)


def relative(path: Path) -> str:
    return str(path.relative_to(ROOT))


def validate_json(path: Path, errors: list[str]) -> None:
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"Invalid JSON: {relative(path)}:{exc.lineno}:{exc.colno}: {exc.msg}")


def has_negating_context(line: str, term: str) -> bool:
    lower = line.lower()
    index = lower.find(term)
    if index == -1:
        return True
    window = lower[max(0, index - 80): index + len(term) + 80]
    return any(marker in window for marker in ALLOWED_NEGATING_CONTEXT)


def scan_text(path: Path, errors: list[str], warnings: list[str]) -> None:
    text = path.read_text(encoding="utf-8", errors="replace")
    lower_text = text.lower()

    for pattern in FORBIDDEN_TEXT_PATTERNS:
        if pattern.lower() in lower_text:
            errors.append(f"Forbidden safety regression found in {relative(path)}: {pattern}")

    # The checker itself necessarily contains the review vocabulary. Do not turn
    # its own dictionary into warning noise.
    if Path(relative(path)) == SCRIPT_RELATIVE_PATH:
        return

    for line_number, line in enumerate(text.splitlines(), start=1):
        lower_line = line.lower()
        for term, message in HIGH_RISK_TERMS.items():
            if term in lower_line and not has_negating_context(lower_line, term):
                warnings.append(f"Review term in {relative(path)}:{line_number}: {term} — {message}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    files = iter_files()
    for path in files:
        if path.suffix.lower() == ".json":
            validate_json(path, errors)
        scan_text(path, errors, warnings)

    if warnings:
        print("Safety invariant warnings:")
        for warning in warnings:
            print(f"- {warning}")
        print()

    if errors:
        print("Safety invariant errors:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("Safety invariant check passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
