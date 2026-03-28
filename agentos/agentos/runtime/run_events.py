"""Append-only run event log (shared by workflow_runner and debate_runner)."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from agentos.config import settings

# Bump when new event families are added (e.g. debate_* in 1.1).
SCHEMA_VERSION = "1.1"


def runs_base_dir(run_id: str) -> Path:
    return settings.RUNS_DIR / run_id


def append_run_event(run_id: str, event: dict[str, Any]) -> None:
    rd = runs_base_dir(run_id)
    rd.mkdir(parents=True, exist_ok=True)
    path = rd / "events.jsonl"
    payload = {**event, "schema_version": SCHEMA_VERSION, "tenant_id": settings.AGENTOS_TENANT_ID}
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(payload, ensure_ascii=False) + "\n")
