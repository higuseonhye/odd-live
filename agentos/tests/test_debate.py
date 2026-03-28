"""Debate schema, grouping, and workflow integration."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from agentos.config import settings
from agentos.runtime.debate_schema import group_debates_from_events
from agentos.runtime.workflow_runner import WorkflowRunner


def test_group_debates_from_events_orders_sessions() -> None:
    did = "d1-0000-0000-0000-000000000001"
    events = [
        {"type": "debate_session_started", "debate_id": did, "step_id": "s1", "topic": "T", "participants": []},
        {"type": "debate_round", "debate_id": did, "step_id": "s1", "round": 1, "agent": "a", "summary": "x"},
        {
            "type": "debate_resolved",
            "debate_id": did,
            "step_id": "s1",
            "outcome": "consensus",
            "summary": "done",
        },
    ]
    g = group_debates_from_events(events)
    assert len(g) == 1
    assert g[0]["debate_id"] == did
    assert g[0]["topic"] == "T"
    assert len(g[0]["rounds"]) == 1
    assert g[0]["resolution"]["outcome"] == "consensus"


def test_workflow_debate_step_writes_events(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(settings, "RUNS_DIR", tmp_path)
    wf = Path(__file__).resolve().parents[1] / "workflows" / "debate_sample.yaml"
    runner = WorkflowRunner()
    rid = runner.start_run(wf)
    rd = tmp_path / rid
    lines = (rd / "events.jsonl").read_text(encoding="utf-8").strip().splitlines()
    types = [json.loads(ln)["type"] for ln in lines]
    assert "debate_session_started" in types
    assert "debate_resolved" in types
    assert "run_completed" in types
    debate_files = list((rd / "debates").glob("*.jsonl"))
    assert len(debate_files) == 1

