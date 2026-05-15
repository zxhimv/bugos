#!/usr/bin/env python3
"""Local revenue-autopilot stop check for bugos.

This script is intentionally conservative. It does not contact networks, import
runtime product modules, collect payments, send outreach, or interact with
security targets. It checks whether the safe revenue backlog has reached a point
where the correct autonomous outcome is to stop rather than create arbitrary
housekeeping PRs.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SAFE_REVENUE_FILES = [
    "docs/offers/core_offer.md",
    "docs/offers/service_menu.md",
    "docs/offers/landing_page_copy.md",
    "docs/offers/buyer_handoff.md",
    "docs/demo/README.md",
    "docs/demo/synthetic_program_brief.md",
    "docs/demo/synthetic_output_pack.md",
    "docs/delivery/README.md",
    "docs/delivery/sample_buyer_handoff.md",
    "docs/trust/data_handling_notice.md",
    "docs/trust/terms_of_use_notes.md",
    "docs/sales/manual_outreach_drafts.md",
    "docs/sales/pricing_hypothesis.md",
]

STOP_REQUIRED_MARKERS = [
    "No automated outreach",
    "No automatic submission",
    "automatic_submission_allowed",
    "No revenue or bounty outcome is guaranteed",
    "draft for human review",
]

EXTERNAL_ACTION_TERMS = [
    "payment collection",
    "external publication",
    "target interaction",
    "automated outreach",
    "automatic submission",
]


def read_text(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def main() -> int:
    missing = [path for path in REQUIRED_SAFE_REVENUE_FILES if not (ROOT / path).is_file()]
    if missing:
        print("Revenue autopilot check failed: required safe revenue files are missing.")
        for path in missing:
            print(f"- missing: {path}")
        print("Next safest action: complete the missing safe documentation before creating new revenue tasks.")
        return 1

    combined = "\n".join(read_text(path) for path in REQUIRED_SAFE_REVENUE_FILES)
    missing_markers = [marker for marker in STOP_REQUIRED_MARKERS if marker not in combined]
    if missing_markers:
        print("Revenue autopilot check failed: required stop/safety markers are missing.")
        for marker in missing_markers:
            print(f"- missing marker: {marker}")
        print("Next safest action: restore explicit stop and safety wording before further revenue work.")
        return 1

    print("Revenue autopilot status: safe revenue preparation baseline is present.")
    print("Backlog status: REV-001 through REV-009 have corresponding draft artifacts.")
    print("Next safest task: no change recommended unless a concrete reviewed business/legal/privacy gap is identified.")
    print("Stop condition report:")
    for term in EXTERNAL_ACTION_TERMS:
        print(f"- stop before {term}")
    print("- stop before creating arbitrary housekeeping or architecture PRs")
    print("- stop before adding runtime functionality")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
