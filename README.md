# odd-live

**GitHub:** [github.com/higuseonhye/odd-live](https://github.com/higuseonhye/odd-live)

Product and integration work for **ODD PLAYGROUND** — kept separate from the upstream [`odd-agentos`](https://github.com/higuseonhye/odd-agentos) repo.

## Layout

| Path | Role |
|------|------|
| `docs/` | Vision, CFP notes, product docs |
| `agentos/` | Full AgentOS tree **including** the debate + evidence extension (`kind: debate` workflows, `debate_*` events, dashboard **Debates** tab). This is the working copy you run and change day to day. |

Upstream **`C:\projects\odd-agentos`** is restored to match `origin/main` (no debate patch in that folder).

## Run the extended AgentOS (from this repo)

```powershell
cd C:\projects\odd-live\agentos
pip install -e ".[dev]"
pip install -e "./agentos-sdk[dev]"
python -m pytest tests agentos-sdk/tests -q
python -m agentos run workflows/debate_sample.yaml
```

API + dashboard: see `agentos/README.md`.

## Syncing changes back to GitHub

- Develop in **`odd-live/agentos`** here.
- When you want the canonical repo to match, push from a clone that tracks `odd-agentos`, or copy changed paths into `higuseonhye/odd-agentos` and open a PR.

If you prefer **`odd-live` as the only git root**, run `git init` here and add `agentos/` (optionally as a subtree or submodule later).
