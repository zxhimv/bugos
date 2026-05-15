"""Build evidence manifests for local files."""

from __future__ import annotations

import mimetypes
from pathlib import Path

from .hashing import sha256_file
from .io_safe import read_text, redact_secrets, resolve_safe
from .models import EvidenceItem, EvidenceManifest

TEXT_SUFFIXES = {".txt", ".md", ".json", ".har", ".log", ".yaml", ".yml", ".csv"}


def build_manifest(evidence_dir: str | Path) -> EvidenceManifest:
    root = resolve_safe(evidence_dir)
    manifest = EvidenceManifest()
    if not root.exists():
        manifest.warnings.append("evidence_dir_missing")
        return manifest
    if not root.is_dir():
        manifest.warnings.append("evidence_path_not_directory")
        return manifest
    if Path(evidence_dir).is_symlink():
        manifest.warnings.append("evidence_dir_symlink_blocked")
        return manifest

    files = sorted([p for p in root.rglob("*") if p.is_file() or p.is_symlink()])
    for idx, path in enumerate(files, start=1):
        relative_path = str(path.relative_to(root))
        if path.is_symlink():
            manifest.warnings.append(f"evidence_symlink_blocked:{relative_path}")
            continue

        redaction_status = "unverified"
        notes = ""
        if path.suffix.lower() in TEXT_SUFFIXES:
            try:
                _, findings = redact_secrets(read_text(path))
                redaction_status = "needs_review" if findings else "no_secret_pattern_detected"
                notes = ",".join(findings)
            except UnicodeDecodeError:
                redaction_status = "binary_or_unreadable"
        mime, _ = mimetypes.guess_type(str(path))
        manifest.items.append(
            EvidenceItem(
                evidence_id=f"E{len(manifest.items) + 1:02d}",
                path=relative_path,
                sha256=sha256_file(path),
                size_bytes=path.stat().st_size,
                mime_guess=mime or "application/octet-stream",
                redaction_status=redaction_status,
                notes=notes,
            )
        )
    if not manifest.items:
        manifest.warnings.append("no_evidence_files_found")
    return manifest
