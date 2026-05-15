import json
import os
import subprocess
import sys
from pathlib import Path


def _run_bugos(args, cwd):
    repo = Path(__file__).resolve().parents[1]
    return subprocess.run(
        [sys.executable, "-m", "bugos.cli", *args],
        check=False,
        text=True,
        capture_output=True,
        cwd=cwd,
        env={**os.environ, "PYTHONPATH": str(repo / "src")},
    )


def test_cli_run_demo(tmp_path):
    result = _run_bugos(["run-demo", "--workspace", "demo"], tmp_path)
    assert result.returncode == 0, result.stderr
    final_path = tmp_path / "demo" / "final_submission_check.json"
    assert final_path.exists()
    data = json.loads(final_path.read_text(encoding="utf-8"))
    assert data["decision"] in {"NEEDS_HUMAN_REVIEW", "BLOCK"}
    assert data["automatic_submission_allowed"] is False
    assert data["ready_meaning"] == "ready_for_human_review_only_not_submission_approval"


def test_cli_invalid_json_writes_stable_error(tmp_path):
    (tmp_path / "bad.json").write_text("{not json", encoding="utf-8")
    result = _run_bugos(["validate-brief", "--brief", "bad.json", "--out", "error.json"], tmp_path)
    assert result.returncode == 2
    data = json.loads((tmp_path / "error.json").read_text(encoding="utf-8"))
    assert data["ok"] is False
    assert data["error"] == "invalid_json"
    assert data["errors"]
    assert "Traceback" not in result.stderr


def test_cli_missing_file_writes_stable_error(tmp_path):
    result = _run_bugos(["validate-brief", "--brief", "missing.json", "--out", "error.json"], tmp_path)
    assert result.returncode == 2
    data = json.loads((tmp_path / "error.json").read_text(encoding="utf-8"))
    assert data["ok"] is False
    assert data["error"] == "file_not_found"
    assert "Traceback" not in result.stderr


def test_cli_blocks_out_of_workspace_input_path(tmp_path):
    outside = tmp_path.parent / "outside_bugos_test.json"
    outside.write_text('{"program_name":"Outside"}', encoding="utf-8")
    try:
        result = _run_bugos(["validate-brief", "--brief", "../outside_bugos_test.json", "--out", "error.json"], tmp_path)
        assert result.returncode == 2
        data = json.loads((tmp_path / "error.json").read_text(encoding="utf-8"))
        assert data["ok"] is False
        assert data["error"] == "invalid_input"
        assert "path_outside_workspace" in data["errors"][0]
    finally:
        outside.unlink(missing_ok=True)


def test_cli_scope_check_rejects_broken_profile(tmp_path):
    (tmp_path / "profile.json").write_text(json.dumps({"program_name": "Demo", "targets": {"bad": True}}), encoding="utf-8")
    result = _run_bugos([
        "scope-check",
        "--profile",
        "profile.json",
        "--target",
        "https://app.demo.example",
        "--action",
        "manual read-only authorization check",
        "--out",
        "error.json",
    ], tmp_path)
    assert result.returncode == 2
    data = json.loads((tmp_path / "error.json").read_text(encoding="utf-8"))
    assert data["ok"] is False
    assert "profile.targets_must_be_json_array" in data["errors"]
