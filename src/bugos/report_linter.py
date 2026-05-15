"""Report quality linter for Bugcrowd-style submissions."""

from __future__ import annotations

import re

REQUIRED_SECTIONS = {
    "summary": ["summary", "beschreibung", "kurzbeschreibung"],
    "location": ["location", "fundort", "url", "where"],
    "affected_parties": ["affected", "betroffene", "who it affects"],
    "impact": ["impact", "risiko", "auswirkung"],
    "steps_to_reproduce": ["steps to reproduce", "reproduction", "reproduktion", "schritte"],
    "parameters": ["parameter", "endpoint", "request"],
    "proof_of_concept": ["proof of concept", "poc", "evidence", "nachweis"],
    "remediation": ["remediation", "fix", "empfehlung", "behebung"],
}

WEAK_PHRASES = [
    "might be vulnerable",
    "probably vulnerable",
    "i think",
    "scanner found",
    "please check",
    "100% sicher",
]

EVIDENCE_RE = re.compile(r"\bE\d{2,}\b")


def lint_report_markdown(markdown: str) -> dict:
    text_l = markdown.lower()
    missing: list[str] = []
    warnings: list[str] = []
    improvements: list[str] = []

    for section, aliases in REQUIRED_SECTIONS.items():
        if not any(alias in text_l for alias in aliases):
            missing.append(section)

    for phrase in WEAK_PHRASES:
        if phrase in text_l:
            warnings.append(f"weak_or_overclaiming_phrase:{phrase}")

    evidence_ids = sorted(set(EVIDENCE_RE.findall(markdown)))
    if not evidence_ids:
        improvements.append("add_evidence_ids_E01_style")

    if len(markdown.split()) < 120:
        warnings.append("report_too_short_for_reliable_triage")

    if "http" not in text_l and "endpoint" not in text_l:
        improvements.append("add_specific_url_or_endpoint")

    score = 100
    score -= len(missing) * 12
    score -= len(warnings) * 5
    score -= len(improvements) * 7
    score = max(score, 0)

    passed = not missing and score >= 80
    return {
        "passed": passed,
        "score": score,
        "missing_sections": missing,
        "warnings": warnings,
        "required_improvements": improvements,
        "detected_evidence_ids": evidence_ids,
    }
