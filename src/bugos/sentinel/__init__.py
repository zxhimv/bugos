"""Sentinel policy helpers for bugos."""

from bugos.sentinel.policy import (
    DecisionState,
    HUMAN_GATE_STATES,
    LOCAL_READONLY_STATES,
    TERMINAL_BLOCK_STATES,
    decision_allows_auto_action,
    normalize_decision_state,
    requires_human_gate,
)

__all__ = [
    "DecisionState",
    "HUMAN_GATE_STATES",
    "LOCAL_READONLY_STATES",
    "TERMINAL_BLOCK_STATES",
    "decision_allows_auto_action",
    "normalize_decision_state",
    "requires_human_gate",
]
