"""Multi-agent debate execution: append-only events + optional debate artifact file."""

from __future__ import annotations

import json
import uuid
from pathlib import Path
from typing import Any

from agentos.runtime.debate_schema import DebateOutcome, normalize_participant
from agentos.runtime.run_events import append_run_event, runs_base_dir


def _debate_artifact_path(run_id: str, debate_id: str) -> Path:
    base = runs_base_dir(run_id) / "debates"
    base.mkdir(parents=True, exist_ok=True)
    return base / f"{debate_id}.jsonl"


def _append_artifact(path: Path, event: dict[str, Any]) -> None:
    from agentos.runtime.run_events import SCHEMA_VERSION

    line = json.dumps({**event, "schema_version": SCHEMA_VERSION}, ensure_ascii=False)
    with path.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


class DebateRunner:
    """
    Runs a deterministic stub debate (no extra LLM calls beyond existing stack).

    Emits debate_* events to events.jsonl and mirrors them to runs/<id>/debates/<debate_id>.jsonl.
    """

    def run(
        self,
        run_id: str,
        step_id: str,
        workflow_name: str | None,
        topic: str,
        participants_raw: list[dict[str, Any]],
        *,
        max_rounds: int = 2,
    ) -> dict[str, Any]:
        debate_id = str(uuid.uuid4())
        participants = [normalize_participant(p) for p in participants_raw]
        if not participants:
            participants = [
                {"agent": "agent-a", "role": "advocate"},
                {"agent": "agent-b", "role": "skeptic"},
            ]

        art = _debate_artifact_path(run_id, debate_id)

        started = {
            "type": "debate_session_started",
            "debate_id": debate_id,
            "step_id": step_id,
            "topic": topic,
            "participants": participants,
            "workflow": workflow_name,
        }
        append_run_event(run_id, started)
        _append_artifact(art, started)

        # Stub content: alternating voices per round (production: LLM calls per agent).
        for r in range(1, max_rounds + 1):
            for p in participants:
                summary = (
                    f"Round {r} — [{p['role']}] {p['agent']}: "
                    f"position on «{topic[:80]}» (stub; connect LLM in production)."
                )
                rnd = {
                    "type": "debate_round",
                    "debate_id": debate_id,
                    "step_id": step_id,
                    "round": r,
                    "agent": p["agent"],
                    "role": p["role"],
                    "stance": "for" if r % 2 == 1 else "against",
                    "summary": summary,
                }
                append_run_event(run_id, rnd)
                _append_artifact(art, rnd)

            ev = {
                "type": "debate_evidence",
                "debate_id": debate_id,
                "step_id": step_id,
                "claim_id": f"r{r}-synthesis",
                "payload": {
                    "round": r,
                    "notes": "Cross-check against policy and snapshots before merge.",
                },
                "refs": [f"snapshot:{step_id}"],
            }
            append_run_event(run_id, ev)
            _append_artifact(art, ev)

        outcome: DebateOutcome = "disputed" if len(participants) > 1 else "consensus"
        open_issues = (
            ["Cost ceiling", "Rollback plan"] if outcome == "disputed" else []
        )
        resolved = {
            "type": "debate_resolved",
            "debate_id": debate_id,
            "step_id": step_id,
            "outcome": outcome,
            "summary": (
                f"Debate on «{topic[:120]}» closed with outcome={outcome}. "
                "Review evidence lines and policy before execution."
            ),
            "open_issues": open_issues,
        }
        append_run_event(run_id, resolved)
        _append_artifact(art, resolved)

        return {
            "debate_id": debate_id,
            "outcome": outcome,
            "rounds": max_rounds * len(participants),
            "artifact": str(art.relative_to(runs_base_dir(run_id))),
            "summary": resolved["summary"],
        }
