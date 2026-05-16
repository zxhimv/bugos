from bugos.final_submission_check import final_check
from bugos.models import FinalSubmissionCheck
from bugos.sentinel.policy import DecisionState


def _valid_profile():
    return {"test_accounts_allowed": True}


def _valid_scope_decision():
    return {"decision": "NEEDS_HUMAN_REVIEW"}


def _valid_report_lint():
    return {"passed": True, "score": 90}


def _valid_manifest():
    return {"items": [{"evidence_id": "E01", "redaction_status": "reviewed"}]}


def test_final_check_adds_review_metadata_for_ready_output():
    check = final_check(_valid_profile(), _valid_scope_decision(), _valid_report_lint(), _valid_manifest())

    data = check.to_dict()

    assert data["decision"] == "NEEDS_HUMAN_REVIEW"
    assert data["sentinel_policy_state"] == DecisionState.NEEDS_HUMAN_REVIEW.value
    assert data["sentinel_policy_state_meaning"].startswith("local_review_state_only")


def test_final_check_adds_block_metadata_when_blockers_exist():
    check = final_check(_valid_profile(), {"decision": "BLOCK"}, _valid_report_lint(), _valid_manifest())

    data = check.to_dict()

    assert data["decision"] == "BLOCK"
    assert data["sentinel_policy_state"] == DecisionState.BLOCK.value


def test_final_submission_check_default_review_metadata():
    check = FinalSubmissionCheck(
        ready=True,
        ready_for_human_review=True,
        decision="NEEDS_HUMAN_REVIEW",
    )

    data = check.to_dict()

    assert data["sentinel_policy_state"] == DecisionState.NEEDS_HUMAN_REVIEW.value
    assert data["sentinel_policy_state_meaning"].startswith("local_review_state_only")
