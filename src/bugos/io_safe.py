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


class SafeIOError(ValueError):
    """Raised when local file access would leave the current workspace."""


def resolve_safe(path: str | Path, base: str | Path | None = None) -> Path:
    """Resolve *path* under *base* and reject traversal outside that tree.

    The default base is the process working directory, which keeps all CLI file
    access inside the local repository/workspace unless a narrower base is
    passed by a caller.
    """

    base_path = Path(base or Path.cwd()).resolve()
    candidate = Path(path)
    if not candidate.is_absolute():
        candidate = base_path / candidate
    resolved = candidate.resolve()
    try:
        resolved.relative_to(base_path)
    except ValueError as exc:
        raise SafeIOError(f"path_outside_workspace:{_display_path(resolved)}") from exc
    return resolved


def _display_path(path: Path) -> str:
    try:
        return str(path.relative_to(Path.cwd().resolve()))
    except ValueError:
        return str(path)


def read_text(path: str | Path, *, base: str | Path | None = None) -> str:
    return resolve_safe(path, base).read_text(encoding="utf-8")


def write_text(path: str | Path, data: str, *, base: str | Path | None = None) -> None:
    target = resolve_safe(path, base)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(data, encoding="utf-8")


def read_json(path: str | Path, *, base: str | Path | None = None) -> Any:
    return json.loads(read_text(path, base=base))


def write_json(path: str | Path, data: Any, *, base: str | Path | None = None) -> None:
    write_text(path, json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True) + "\n", base=base)


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
