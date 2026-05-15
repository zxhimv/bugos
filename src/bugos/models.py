"""Core data models for bugos.

The project intentionally uses only the Python standard library so that it can
run in restricted environments without dependency drift.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Literal

Decision = Literal["ALLOW", "BLOCK", "NEEDS_HUMAN_REVIEW"]
Severity = Literal["P1", "P2", "P3", "P4", "P5", "UNRATED"]
EvidenceGrade = Literal["A", "B", "C", "D"]


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


@dataclass(slots=True)
class ScopeAsset:
    identifier: str
    asset_type: str = "url"
    in_scope: bool = True
    allowed_actions: list[str] = field(default_factory=list)
    notes: str = ""


@dataclass(slots=True)
class ProgramProfile:
    program_name: str
    platform: str = "Bugcrowd"
    brief_version: str = "unknown"
    engagement_status: str = "unknown"
    collected_at: str = field(default_factory=utc_now_iso)
    targets: list[ScopeAsset] = field(default_factory=list)
    out_of_scope: list[str] = field(default_factory=list)
    known_issues: list[str] = field(default_factory=list)
    rules: list[str] = field(default_factory=list)
    rewards: dict[str, Any] = field(default_factory=dict)
    submission_limits: dict[str, Any] = field(default_factory=dict)
    test_accounts_allowed: bool | None = None
    disclosure_rules: list[str] = field(default_factory=list)
    human_gate_required: bool = True
    notes: str = ""

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ScopeDecision:
    decision: Decision
    target: str
    action: str
    reasons: list[str] = field(default_factory=list)
    matched_assets: list[str] = field(default_factory=list)
    required_human_checks: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=utc_now_iso)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ReportLintResult:
    passed: bool
    score: int
    missing_sections: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    required_improvements: list[str] = field(default_factory=list)
    detected_evidence_ids: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=utc_now_iso)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class EvidenceItem:
    evidence_id: str
    path: str
    sha256: str
    size_bytes: int
    mime_guess: str = "application/octet-stream"
    redaction_status: str = "unverified"
    notes: str = ""


@dataclass(slots=True)
class EvidenceManifest:
    manifest_version: str = "0.1.0"
    created_at: str = field(default_factory=utc_now_iso)
    items: list[EvidenceItem] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class FinalSubmissionCheck:
    ready: bool
    decision: Decision
    blockers: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    required_human_checks: list[str] = field(default_factory=list)
    created_at: str = field(default_factory=utc_now_iso)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)
