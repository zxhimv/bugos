from pathlib import Path
from bugos.report_linter import lint_report_markdown


def test_good_report_passes():
    text = Path("fixtures/sample_report_good.md").read_text(encoding="utf-8")
    result = lint_report_markdown(text)
    assert result["passed"] is True
    assert result["score"] >= 80
    assert "E01" in result["detected_evidence_ids"]


def test_bad_report_fails():
    text = Path("fixtures/sample_report_bad.md").read_text(encoding="utf-8")
    result = lint_report_markdown(text)
    assert result["passed"] is False
    assert result["missing_sections"]
