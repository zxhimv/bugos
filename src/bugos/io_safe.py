"""Safe local file I/O helpers.

All commands are offline and path-constrained. These helpers reject path
traversal and write parents automatically.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[^'\"\s]+"),
    re.compile(r"(?i)authorization:\s*bearer\s+[a-z0-9._\-]+"),
    re.compile(r"(?i)cookie:\s*[^\n]+"),
]


def resolve_safe(path: str | Path, base: str | Path | None = None) -> Path:
    base_path = Path(base or Path.cwd()).resolve()
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = base_path / candidate
    resolved = candidate.resolve()
    try:
        resolved.relative_to(base_path)
    except ValueError as exc:
        raise ValueError(f"Unsafe path outside workspace: {resolved}") from exc
    return resolved


def read_text(path: str | Path) -> str:
    return Path(path).read_text(encoding="utf-8")


def write_text(path: str | Path, data: str) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(data, encoding="utf-8")


def read_json(path: str | Path) -> Any:
    return json.loads(read_text(path))


def write_json(path: str | Path, data: Any) -> None:
    write_text(path, json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n")


def redact_secrets(text: str) -> tuple[str, list[str]]:
    findings: list[str] = []
    redacted = text
    for idx, pattern in enumerate(SECRET_PATTERNS, start=1):
        if pattern.search(redacted):
            findings.append(f"secret_pattern_{idx}")
            redacted = pattern.sub("[REDACTED_SECRET]", redacted)
    return redacted, findings


def sanitize_slug(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9_.-]+", "-", value.strip()).strip("-._")
    return slug[:80] or "untitled"
