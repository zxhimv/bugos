"""Final conservative readiness gate."""

from __future__ import annotations

from typing import Any

from .models import FinalSubmissionCheck


def final_check(profile: dict[str, Any], scope_decision: dict[str, Any], report_lint: dict[str, Any], manifest: dict[str, Any]) -> FinalSubmissionCheck:
    blockers: list[str] = []
    warnings: list[str] = []
    required_human_checks = [
        "confirm_current_program_brief",
        "confirm_scope_and_out_of_scope",
        "confirm_known_issues_and_duplicate_risk",
        "confirm_submission_limit_slot_available",
        "confirm_no_sensitive_data_in_evidence",
        "confirm_test_account_permission",
        "confirm_disclosure_rules",
        "human_read_report_before_submission",
    ]

    if scope_decision.get("decision") == "BLOCK":
        blockers.append("scope_decision_block")
    if scope_decision.get("decision") != "NEEDS_HUMAN_REVIEW":
        warnings.append("scope_decision_not_in_expected_human_review_state")

    if not report_lint.get("passed"):
        blockers.append("report_lint_failed")
    if report_lint.get("score", 0) < 85:
        warnings.append("report_quality_below_preferred_threshold_85")

    items = manifest.get("items", []) or []
    if not items:
        blockers.append("no_evidence_items")
    for item in items:
        if item.get("redaction_status") in {"needs_review", "unverified"}:
            warnings.append(f"evidence_redaction_review_required:{item.get('evidence_id')}")

    if profile.get("test_accounts_allowed") is not True:
        warnings.append("test_account_permission_not_explicitly_true")

    decision = "NEEDS_HUMAN_REVIEW"
    ready = not blockers
    if blockers:
        decision = "BLOCK"

    return FinalSubmissionCheck(
        ready=ready,
        decision=decision,
        blockers=blockers,
        warnings=warnings,
        required_human_checks=required_human_checks,
    )
