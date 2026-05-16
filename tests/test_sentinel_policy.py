import pytest

from bugos.models import FinalSubmissionCheck
from bugos.sentinel.policy import (
    DecisionState,
    decision_allows_auto_action,
    normalize_decision_state,
    requires_human_gate,
)


def test_normalize_decision_state_accepts_known_values():
    assert normalize_decision_state("allow_local_readonly") is DecisionState.ALLOW_LOCAL_READONLY
    assert normalize_decision_state(" NEEDS_HUMAN_REVIEW ") is DecisionState.NEEDS_HUMAN_REVIEW
    assert normalize_decision_state(DecisionState.BLOCK) is DecisionState.BLOCK


@pytest.mark.parametrize("value", ["", "allow", "APPROVE", "UNKNOWN", object(), None])
def test_normalize_decision_state_rejects_unknown_values(value):
    with pytest.raises(ValueError, match="unknown_decision_state"):
        normalize_decision_state(value)  # type: ignore[arg-type]


@pytest.mark.parametrize("state", list(DecisionState))
def test_no_sentinel_state_allows_unattended_action(state):
    assert decision_allows_auto_action(state) is False


@pytest.mark.parametrize("state", [DecisionState.NEEDS_HUMAN_REVIEW, DecisionState.AUDIT_REQUIRED])
def test_review_states_require_human_gate(state):
    assert requires_human_gate(state) is True


@pytest.mark.parametrize(
    "state",
    [DecisionState.ALLOW_LOCAL_READONLY, DecisionState.BLOCK, DecisionState.QUARANTINE],
)
def test_non_review_states_do_not_clear_blockers_by_themselves(state):
    assert requires_human_gate(state) is False
    assert decision_allows_auto_action(state) is False


def test_existing_final_submission_check_keeps_auto_submission_disabled():
    check = FinalSubmissionCheck(
        ready=True,
        ready_for_human_review=True,
        decision="NEEDS_HUMAN_REVIEW",
    )

    data = check.to_dict()

    assert data["automatic_submission_allowed"] is False
    assert data["decision"] == "NEEDS_HUMAN_REVIEW"
    assert data["ready_meaning"] == "ready_for_human_review_only_not_submission_approval"
