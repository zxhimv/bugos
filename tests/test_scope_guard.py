from bugos.models import ProgramProfile, ScopeAsset
from bugos.scope_guard import check_scope


def _profile():
    return ProgramProfile(
        program_name="Demo",
        targets=[ScopeAsset("https://app.demo.example", allowed_actions=["manual", "read-only", "authorization"])],
        out_of_scope=["denial of service"],
        test_accounts_allowed=True,
    )


def test_scope_guard_blocks_out_of_scope_target():
    d = check_scope(_profile(), "https://evil.example", "manual read-only authorization check")
    assert d.decision == "BLOCK"
    assert "target_not_explicitly_in_scope" in d.reasons


def test_scope_guard_blocks_dos_action():
    d = check_scope(_profile(), "https://app.demo.example/path", "denial of service test")
    assert d.decision == "BLOCK"


def test_scope_guard_requires_human_review_for_allowed_plan():
    d = check_scope(_profile(), "https://app.demo.example/path", "manual read-only authorization check")
    assert d.decision == "NEEDS_HUMAN_REVIEW"
    assert d.matched_assets


def test_scope_guard_blocks_credential_stuffing_phrase():
    d = check_scope(_profile(), "https://app.demo.example/path", "credential stuffing validation")
    assert d.decision == "BLOCK"
    assert "blocked_action_keyword:credential stuffing" in d.reasons


def test_scope_guard_blocks_customer_data_phrase():
    d = check_scope(_profile(), "https://app.demo.example/path", "manual customer data review")
    assert d.decision == "BLOCK"
