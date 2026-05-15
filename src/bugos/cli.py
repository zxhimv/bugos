"""bugos CLI entry point."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

from .brief_normalizer import normalize_brief_dict
from .brief_schema_validator import validate_brief_dict
from .evidence_manifest import build_manifest
from .final_submission_check import final_check
from .io_safe import read_json, read_text, write_json, write_text
from .models import ProgramProfile, ScopeAsset
from .report_linter import lint_report_markdown
from .scope_guard import check_scope


def _profile_from_dict(data: dict[str, Any]) -> ProgramProfile:
    return ProgramProfile(
        program_name=data.get("program_name", "unknown"),
        platform=data.get("platform", "Bugcrowd"),
        brief_version=data.get("brief_version", "unknown"),
        engagement_status=data.get("engagement_status", "unknown"),
        collected_at=data.get("collected_at") or data.get("created_at") or "unknown",
        targets=[
            ScopeAsset(
                identifier=t.get("identifier", ""),
                asset_type=t.get("asset_type", "url"),
                in_scope=bool(t.get("in_scope", False)),
                allowed_actions=list(t.get("allowed_actions", []) or []),
                notes=t.get("notes", ""),
            )
            for t in data.get("targets", [])
        ],
        out_of_scope=list(data.get("out_of_scope", []) or []),
        known_issues=list(data.get("known_issues", []) or []),
        rules=list(data.get("rules", []) or []),
        rewards=dict(data.get("rewards", {}) or {}),
        submission_limits=dict(data.get("submission_limits", {}) or {}),
        test_accounts_allowed=data.get("test_accounts_allowed"),
        disclosure_rules=list(data.get("disclosure_rules", []) or []),
        human_gate_required=bool(data.get("human_gate_required", True)),
        notes=data.get("notes", ""),
    )


def _cmd_validate_brief(args: argparse.Namespace) -> int:
    result = validate_brief_dict(read_json(args.brief))
    write_json(args.out, result)
    return 0 if result["valid"] else 2


def _cmd_normalize_brief(args: argparse.Namespace) -> int:
    data = read_json(args.brief)
    validation = validate_brief_dict(data)
    profile = normalize_brief_dict(data).to_dict()
    profile["validation"] = validation
    write_json(args.out, profile)
    return 0 if validation["valid"] else 2


def _cmd_scope_check(args: argparse.Namespace) -> int:
    profile = _profile_from_dict(read_json(args.profile))
    decision = check_scope(profile, args.target, args.action)
    write_json(args.out, decision.to_dict())
    return 0 if decision.decision != "BLOCK" else 2


def _cmd_lint_report(args: argparse.Namespace) -> int:
    result = lint_report_markdown(read_text(args.report))
    write_json(args.out, result)
    return 0 if result["passed"] else 2


def _cmd_build_evidence(args: argparse.Namespace) -> int:
    manifest = build_manifest(args.evidence_dir)
    write_json(args.out, manifest.to_dict())
    return 0 if manifest.items else 2


def _cmd_final_check(args: argparse.Namespace) -> int:
    check = final_check(
        profile=read_json(args.profile),
        scope_decision=read_json(args.scope_decision),
        report_lint=read_json(args.report_lint),
        manifest=read_json(args.manifest),
    )
    write_json(args.out, check.to_dict())
    return 0 if check.ready else 2


def _cmd_run_demo(args: argparse.Namespace) -> int:
    workspace = Path(args.workspace)
    workspace.mkdir(parents=True, exist_ok=True)
    evidence_dir = workspace / "evidence"
    evidence_dir.mkdir(exist_ok=True)

    brief = {
        "program_name": "Synthetic Demo Program",
        "platform": "Bugcrowd",
        "brief_version": "synthetic-v0",
        "engagement_status": "demo_only",
        "targets": [{
            "identifier": "https://app.demo.example",
            "asset_type": "url",
            "in_scope": True,
            "allowed_actions": ["manual", "read-only", "authorization"],
            "notes": "Synthetic local demo only. Not a real target.",
        }],
        "out_of_scope": ["denial of service", "bruteforce", "social engineering", "customer data"],
        "known_issues": ["generic reflected XSS on marketing pages"],
        "rules": ["Human approval required before any real target interaction."],
        "rewards": {"P1": "program-specific", "P2": "program-specific"},
        "submission_limits": {"pending_limit": 5},
        "test_accounts_allowed": True,
        "disclosure_rules": ["No public disclosure without approval."],
    }
    report = """# Summary
Manual read-only authorization check indicates that Demo User B can access Demo User A account metadata through an object identifier.

# Location
https://app.demo.example/account/123 and endpoint GET /api/accounts/123

# Affected parties
Any demo tenant account whose numeric object identifier can be guessed by another authenticated demo account.

# Impact
Unauthorized read access to account metadata could expose business profile information. No destructive action, credential access, or customer data access was attempted.

# Steps to reproduce
1. Sign in as owned demo account A and note object id 123.
2. Sign in as owned demo account B in a separate browser profile.
3. Send GET /api/accounts/123 as account B.
4. Observe account A metadata in the response. Evidence E01 shows the response with synthetic values only.

# Parameters
Path parameter: account id in /api/accounts/{id}.

# Proof of Concept / Evidence
E01: synthetic_request_response.txt with redacted request and response.

# Remediation
Enforce object-level authorization server-side for every account lookup and verify requester-to-resource ownership before returning data.
"""
    write_json(workspace / "synthetic_brief.json", brief)
    write_json(workspace / "validation.json", validate_brief_dict(brief))
    profile = normalize_brief_dict(brief)
    write_json(workspace / "program_profile.json", profile.to_dict())
    decision = check_scope(profile, "https://app.demo.example/account/123", "manual read-only authorization check with two owned demo test accounts")
    write_json(workspace / "scope_decision.json", decision.to_dict())
    write_text(workspace / "report_draft.md", report)
    write_text(evidence_dir / "synthetic_request_response.txt", "GET /api/accounts/123\nHTTP 200\n{\"owner\":\"DEMO_A\"}\n")
    manifest = build_manifest(evidence_dir)
    write_json(workspace / "evidence_manifest.json", manifest.to_dict())
    lint = lint_report_markdown(report)
    write_json(workspace / "report_lint.json", lint)
    write_json(workspace / "final_submission_check.json", final_check(profile.to_dict(), decision.to_dict(), lint, manifest.to_dict()).to_dict())
    write_text(workspace / "README_DEMO.md", "Synthetic bugos demo completed. No network or real target interaction occurred.\n")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="bugos", description="Offline bug bounty operations helper.")
    sub = parser.add_subparsers(dest="command", required=True)
    specs = [
        ("validate-brief", _cmd_validate_brief, [("--brief", True), ("--out", True)]),
        ("normalize-brief", _cmd_normalize_brief, [("--brief", True), ("--out", True)]),
        ("scope-check", _cmd_scope_check, [("--profile", True), ("--target", True), ("--action", True), ("--out", True)]),
        ("lint-report", _cmd_lint_report, [("--report", True), ("--out", True)]),
        ("build-evidence", _cmd_build_evidence, [("--evidence-dir", True), ("--out", True)]),
        ("final-check", _cmd_final_check, [("--profile", True), ("--scope-decision", True), ("--report-lint", True), ("--manifest", True), ("--out", True)]),
        ("run-demo", _cmd_run_demo, [("--workspace", True)]),
    ]
    for name, func, arguments in specs:
        p = sub.add_parser(name)
        for arg, required in arguments:
            p.add_argument(arg, required=required)
        p.set_defaults(func=func)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
