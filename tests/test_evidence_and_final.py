from pathlib import Path
from bugos.evidence_manifest import build_manifest
from bugos.final_submission_check import final_check
from bugos.models import ProgramProfile, ScopeAsset
from bugos.scope_guard import check_scope
from bugos.report_linter import lint_report_markdown


def test_evidence_manifest_builds_hashes():
    manifest = build_manifest("fixtures/evidence")
    assert manifest.items
    assert len(manifest.items[0].sha256) == 64


def test_final_check_ready_with_good_local_artifacts():
    profile = ProgramProfile(
        program_name="Demo",
        targets=[ScopeAsset("https://app.demo.example", allowed_actions=["manual", "read-only", "authorization"])],
        out_of_scope=["denial of service"],
        test_accounts_allowed=True,
    )
    scope = check_scope(profile, "https://app.demo.example/account/123", "manual read-only authorization check")
    report = Path("fixtures/sample_report_good.md").read_text(encoding="utf-8")
    lint = lint_report_markdown(report)
    manifest = build_manifest("fixtures/evidence")
    result = final_check(profile.to_dict(), scope.to_dict(), lint, manifest.to_dict())
    assert result.ready is True
    assert result.decision == "NEEDS_HUMAN_REVIEW"
