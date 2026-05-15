import json
import os
import subprocess
import sys
from pathlib import Path


def test_cli_run_demo(tmp_path):
    result = subprocess.run(
        [sys.executable, "-m", "bugos.cli", "run-demo", "--workspace", str(tmp_path)],
        check=False,
        text=True,
        capture_output=True,
        env={**os.environ, "PYTHONPATH": str(Path.cwd() / "src")},
    )
    assert result.returncode == 0, result.stderr
    final_path = tmp_path / "final_submission_check.json"
    assert final_path.exists()
    data = json.loads(final_path.read_text(encoding="utf-8"))
    assert data["decision"] in {"NEEDS_HUMAN_REVIEW", "BLOCK"}
