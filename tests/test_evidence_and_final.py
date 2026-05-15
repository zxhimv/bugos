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


def test_evidence_manifest_empty_dir_blocks(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    Path("evidence").mkdir()
    manifest = build_manifest("evidence")
    assert not manifest.items
    assert "no_evidence_files_found" in manifest.warnings


def test_evidence_manifest_marks_secret_patterns(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    evidence = tmp_path / "evidence"
    evidence.mkdir()
    (evidence / "secret.txt").write_text("api_key=example-secret-value", encoding="utf-8")
    manifest = build_manifest("evidence")
    assert manifest.items[0].redaction_status == "needs_review"
    assert manifest.items[0].notes == "secret_pattern_1"


def test_evidence_manifest_blocks_symlink(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    evidence = tmp_path / "evidence"
    evidence.mkdir()
    target = tmp_path / "target.txt"
    target.write_text("local", encoding="utf-8")
    (evidence / "linked.txt").symlink_to(target)
    manifest = build_manifest("evidence")
    assert not manifest.items
    assert "evidence_symlink_blocked:linked.txt" in manifest.warnings
    assert "no_evidence_files_found" in manifest.warnings


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
    assert result.ready_for_human_review is True
    assert result.automatic_submission_allowed is False
    assert result.decision == "NEEDS_HUMAN_REVIEW"
    assert "human_gate_required_before_any_submission" in result.warnings


def test_final_check_blocks_broken_manifest_items():
    result = final_check(
        {"test_accounts_allowed": True},
        {"decision": "NEEDS_HUMAN_REVIEW"},
        {"passed": True, "score": 100},
        {"items": "not-a-list"},
    )
    assert result.ready is False
    assert result.decision == "BLOCK"
    assert "manifest_items_must_be_json_array" in result.blockers
