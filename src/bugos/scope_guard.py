"""Conservative scope gate.

The guard does not authorize testing. It only classifies whether the local plan
appears compatible with the already reviewed brief. Human approval still gates
real target interaction.
"""

from __future__ import annotations

from urllib.parse import urlparse

from .models import ProgramProfile, ScopeDecision

BLOCK_KEYWORDS = [
    "dos", "denial of service", "bruteforce", "brute force", "credential stuffing",
    "phishing", "social engineering", "spam", "malware", "destructive", "delete data",
    "production data", "customer data", "payment fraud", "rate limit bypass",
]


def _same_host_or_prefix(target: str, identifier: str) -> bool:
    t = target.strip().lower().rstrip("/")
    i = identifier.strip().lower().rstrip("/")
    if not t or not i:
        return False
    if t == i or t.startswith(i + "/"):
        return True
    parsed_t = urlparse(t)
    parsed_i = urlparse(i)
    if parsed_t.netloc and parsed_i.netloc and parsed_t.netloc == parsed_i.netloc:
        return True
    return False


def check_scope(profile: ProgramProfile, target: str, action: str) -> ScopeDecision:
    reasons: list[str] = []
    matched: list[str] = []
    required_human_checks = [
        "current_brief_reviewed",
        "out_of_scope_reviewed",
        "known_issues_reviewed",
        "submission_limits_reviewed",
        "rate_limits_reviewed",
        "test_account_permission_reviewed",
        "disclosure_rules_reviewed",
    ]

    action_l = action.lower()
    target_l = target.lower()

    for forbidden in BLOCK_KEYWORDS:
        if forbidden in action_l:
            reasons.append(f"blocked_action_keyword:{forbidden}")

    for rule in profile.out_of_scope:
        if str(rule).lower() and str(rule).lower() in (action_l + " " + target_l):
            reasons.append(f"matches_out_of_scope:{rule}")

    for asset in profile.targets:
        if asset.in_scope and _same_host_or_prefix(target, asset.identifier):
            matched.append(asset.identifier)
            if asset.allowed_actions:
                if not any(a.lower() in action_l for a in asset.allowed_actions):
                    reasons.append("action_not_in_asset_allowed_actions")

    if reasons:
        return ScopeDecision("BLOCK", target, action, reasons, matched, required_human_checks)

    if not matched:
        return ScopeDecision(
            "BLOCK",
            target,
            action,
            ["target_not_explicitly_in_scope"],
            matched,
            required_human_checks,
        )

    if profile.test_accounts_allowed is not True:
        return ScopeDecision(
            "NEEDS_HUMAN_REVIEW",
            target,
            action,
            ["test_account_permission_not_explicitly_true"],
            matched,
            required_human_checks,
        )

    return ScopeDecision(
        "NEEDS_HUMAN_REVIEW",
        target,
        action,
        ["scope_appears_compatible_but_human_gate_required"],
        matched,
        required_human_checks,
    )
