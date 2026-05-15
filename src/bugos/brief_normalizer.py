"""Normalize a redacted brief JSON into a ProgramProfile."""

from __future__ import annotations

from typing import Any

from .models import ProgramProfile, ScopeAsset


def normalize_brief_dict(data: dict[str, Any]) -> ProgramProfile:
    targets: list[ScopeAsset] = []
    for target in data.get("targets", []) or []:
        if not isinstance(target, dict):
            continue
        targets.append(
            ScopeAsset(
                identifier=str(target.get("identifier", "")).strip(),
                asset_type=str(target.get("asset_type", "url")),
                in_scope=bool(target.get("in_scope", False)),
                allowed_actions=list(target.get("allowed_actions", []) or []),
                notes=str(target.get("notes", "")),
            )
        )

    return ProgramProfile(
        program_name=str(data.get("program_name", "unknown")),
        platform=str(data.get("platform", "Bugcrowd")),
        brief_version=str(data.get("brief_version", "unknown")),
        engagement_status=str(data.get("engagement_status", "unknown")),
        targets=targets,
        out_of_scope=list(data.get("out_of_scope", []) or []),
        known_issues=list(data.get("known_issues", []) or []),
        rules=list(data.get("rules", []) or []),
        rewards=dict(data.get("rewards", {}) or {}),
        submission_limits=dict(data.get("submission_limits", {}) or {}),
        test_accounts_allowed=data.get("test_accounts_allowed"),
        disclosure_rules=list(data.get("disclosure_rules", []) or []),
        human_gate_required=bool(data.get("human_gate_required", True)),
        notes=str(data.get("notes", "")),
    )
