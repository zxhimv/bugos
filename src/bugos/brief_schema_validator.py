"""Validate a redacted Bugcrowd brief JSON file."""

from __future__ import annotations

from typing import Any

REQUIRED_FIELDS = [
    "program_name",
    "targets",
    "out_of_scope",
    "rules",
]

RECOMMENDED_FIELDS = [
    "known_issues",
    "rewards",
    "submission_limits",
    "test_accounts_allowed",
    "disclosure_rules",
    "engagement_status",
]


def validate_brief_dict(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    for field in REQUIRED_FIELDS:
        if field not in data or data[field] in (None, "", []):
            errors.append(f"missing_required_field:{field}")

    for field in RECOMMENDED_FIELDS:
        if field not in data or data[field] in (None, "", []):
            warnings.append(f"missing_recommended_field:{field}")

    targets = data.get("targets", [])
    if targets and not isinstance(targets, list):
        errors.append("targets_must_be_list")
    if isinstance(targets, list):
        for idx, target in enumerate(targets):
            if not isinstance(target, dict):
                errors.append(f"target_{idx}_must_be_object")
                continue
            if not target.get("identifier"):
                errors.append(f"target_{idx}_missing_identifier")
            if target.get("in_scope") is not True:
                warnings.append(f"target_{idx}_not_explicitly_in_scope")

    if data.get("test_accounts_allowed") is None:
        warnings.append("test_account_permission_unknown")

    return {
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "conservative_default": "BLOCK_UNTIL_FIXED" if errors else "NEEDS_HUMAN_REVIEW",
    }
