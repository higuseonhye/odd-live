# odd-live

ODD PLAYGROUND — product docs and AgentOS with the debate + evidence extension. Upstream without this layer lives in [`odd-agentos`](https://github.com/higuseonhye/odd-agentos).

## Layout

| Path | Role |
|------|------|
| `docs/` | Vision and product notes (e.g. `vision-evolutionary-policy.md`) |
| `agentos/` | Runnable AgentOS (`kind: debate`, `debate_*` events, Debates tab in the dashboard) |

## Run

```powershell
cd agentos
pip install -e ".[dev]"
pip install -e "./agentos-sdk[dev]"
python -m pytest tests agentos-sdk/tests -q
python -m agentos run workflows/debate_sample.yaml
# shorthand (same workflow):
python -m agentos run workflows/debate
```

API and dashboard setup: `agentos/README.md`.

To align the canonical [`odd-agentos`](https://github.com/higuseonhye/odd-agentos) repo with changes made here, cherry-pick or open a PR from this tree.
