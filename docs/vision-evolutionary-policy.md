# Vision: Evolutionary Policy & Living Constitution

**ODD PLAYGROUND · Seonhye Gu · Seoul, Korea**

*Draft for investor-facing materials (e.g. YC, a16z Speedrun) — Vision section only. Includes capabilities not yet implemented.*

---

### One-line vision

A **living constitution** for AI agents — **Policy** that agents and humans **co-evolve**.

### The problem we are solving

Today’s agent stack optimizes two questions:

- **Capability:** Can the agent perform better?
- **Observability:** Can we see what the agent did?

The third question is often missing:

**Governability:** Who decides how the agent *should* behave — and how, and when?

Most teams encode this ad hoc in code, set it once at deploy, or skip it. The result is agents that are either powerful but uncontrollable, or safe but too constrained to be useful.

### Core insight

**Policy is not a rulebook. Policy is the agent’s worldview.**

Rulebooks are static. Worldviews are alive.

In a healthy organization, people do not get coached on every action. They internalize values and judgment, act autonomously inside them, and those values themselves evolve with experience.

Agents should work the same way.

### The vision: Evolutionary Policy

Three loops, one system:

```
┌─────────────────────────────────────────────────────────┐
│                  EVOLUTIONARY POLICY                      │
│                                                         │
│  Policy (worldview)                                     │
│       ↓ agents act inside Policy                        │
│  Execution + debate                                     │
│       ↓ outcomes and evidence accumulate                │
│  Learning                                               │
│       ↓ Policy improves                                 │
│  Policy (evolved worldview)                             │
└─────────────────────────────────────────────────────────┘
```

**How this differs from recursive self-improvement (RSI):**

- **RSI** improves **capability**.
- **Evolutionary Policy** improves **values and judgment**.

Improving capability alone can erode control. Improving values and judgment can stay aligned with humans.

### Five primitives

1. **Policy as worldview** — Give agents judgment criteria, not only hard rules. They decide inside that worldview.

2. **Agent debate with evidence** — Hard decisions are argued by agents; agree-to-disagree is allowed. Every session leaves **agreed points**, **open disagreements**, and **evidence** humans can use.

3. **Simulation before action** — Before side effects in the real world, run **simulation** to surface unintended impact.

4. **Living constitution** — Policy is not frozen. Outcomes, debate evidence, and failure patterns feed back into Policy. Some steps may look like regression; they can still be part of a larger evolutionary path.

5. **Transparent runtime** — Like live code in an editor, the agent **backend** is inspectable (“MRI”). Non-experts can operate inside templates. **Cost and resources** are first-class.

### Why now

- Regulators and enterprises increasingly require **auditability** for AI-driven decisions.
- As agents touch real workflows, **control** is a production problem, not a paper exercise.
- Constitutional AI showed the direction; **operational** tooling for companies is still thin.

### Built vs building

| AgentOS MVP (today) | Vision |
|---------------------|--------|
| Policy — hand-written YAML | Policy co-evolved by agents + humans |
| Oversight — human approval gates | Oversight via **debate + evidence** |
| Observability — replay + System MRI | Observability + **simulation** + transparent runtime |
| Learning — not yet | **Policy self-improvement** loop |

### One-liner for investors

“We’re building the **governance layer** that makes AI agents safe to deploy in the real world — not by crippling what they can do, but by giving them a **value system** they can evolve.”

### Honest assessment

Most of this vision is **not** shipped yet.

**Working today:** execution replay, policy engine (YAML), human gates, System MRI, reliability cards.

**Next to build:** agent debate + evidence as first-class artifacts, then a policy self-improvement loop.

The foundation we are laying matches where we believe the product must go.

---

*Document version: 2026-03-29 · ODD PLAYGROUND*
