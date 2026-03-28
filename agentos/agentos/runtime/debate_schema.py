"""Debate + evidence event types (events.jsonl schema 1.1+)."""

from __future__ import annotations

from typing import Any, Literal

# Event types appended for multi-agent debate sessions (immutable audit trail).
DEBATE_EVENT_TYPES: frozenset[str] = frozenset(
    {
        "debate_session_started",
        "debate_round",
        "debate_evidence",
        "debate_resolved",
    },
)

DebateOutcome = Literal["consensus", "disputed", "escalated"]


def normalize_participant(raw: dict[str, Any]) -> dict[str, str]:
    return {
        "agent": str(raw.get("agent", "unknown")),
        "role": str(raw.get("role", "participant")),
    }


def group_debates_from_events(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Aggregate debate_* lines into session objects for API / UI.

    Each session is keyed by debate_id; order follows first appearance.
    """
    order: list[str] = []
    sessions: dict[str, dict[str, Any]] = {}

    for e in events:
        t = e.get("type")
        if t not in DEBATE_EVENT_TYPES:
            continue
        did = e.get("debate_id")
        if not isinstance(did, str):
            continue
        if did not in sessions:
            order.append(did)
            sessions[did] = {
                "debate_id": did,
                "step_id": e.get("step_id"),
                "topic": None,
                "rounds": [],
                "evidence": [],
                "resolution": None,
            }
        s = sessions[did]
        if t == "debate_session_started":
            s["topic"] = e.get("topic")
            s["step_id"] = e.get("step_id", s.get("step_id"))
            s["participants"] = e.get("participants")
        elif t == "debate_round":
            s["rounds"].append(
                {
                    "round": e.get("round"),
                    "agent": e.get("agent"),
                    "role": e.get("role"),
                    "summary": e.get("summary"),
                    "stance": e.get("stance"),
                },
            )
        elif t == "debate_evidence":
            s["evidence"].append(
                {
                    "claim_id": e.get("claim_id"),
                    "payload": e.get("payload"),
                    "refs": e.get("refs"),
                },
            )
        elif t == "debate_resolved":
            s["resolution"] = {
                "outcome": e.get("outcome"),
                "summary": e.get("summary"),
                "open_issues": e.get("open_issues"),
            }

    return [sessions[i] for i in order]
