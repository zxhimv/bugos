"""Sentinel policy states.

This module contains local review primitives for defensive workflow tooling.
It is intentionally small, deterministic, and conservative.
"""

from __future__ import annotations

from enum import StrEnum


class DecisionState(StrEnum):
    """Conservative Sentinel policy states with stable string values."""

    ALLOW_LOCAL_READONLY = "ALLOW_LOCAL_READONLY"
    NEEDS_HUMAN_REVIEW = "NEEDS_HUMAN_REVIEW"
    BLOCK = "BLOCK"
    QUARANTINE = "QUARANTINE"
    AUDIT_REQUIRED = "AUDIT_REQUIRED"


LOCAL_READONLY_STATES: frozenset[DecisionState] = frozenset({DecisionState.ALLOW_LOCAL_READONLY})

HUMAN_GATE_STATES: frozenset[DecisionState] = frozenset(
    {
        DecisionState.NEEDS_HUMAN_REVIEW,
        DecisionState.AUDIT_REQUIRED,
    }
)

TERMINAL_BLOCK_STATES: frozenset[DecisionState] = frozenset(
    {
        DecisionState.BLOCK,
        DecisionState.QUARANTINE,
    }
)


def normalize_decision_state(value: DecisionState | str) -> DecisionState:
    """Return a known DecisionState or raise ValueError."""

    if isinstance(value, DecisionState):
        return value
    if not isinstance(value, str) or not value.strip():
        raise ValueError("unknown_decision_state")
    try:
        return DecisionState(value.strip().upper())
    except ValueError as exc:
        raise ValueError("unknown_decision_state") from exc


def requires_human_gate(value: DecisionState | str) -> bool:
    """Return whether the state requires explicit human review."""

    state = normalize_decision_state(value)
    return state in HUMAN_GATE_STATES


def decision_allows_auto_action(value: DecisionState | str) -> bool:
    """Return whether a state permits unattended action.

    Sentinel review states never grant unattended action authority.
    """

    normalize_decision_state(value)
    return False
