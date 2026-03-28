# AI Engineer World's Fair 2026 — CFP + Vision Document

**ODD PLAYGROUND | Seonhye Gu | Seoul, Korea**

---

## PART 1: CFP 제출 최종본

### 제출 #1 — Stage Talk (18–20 min)

**Session Topic / Name**

From Failure to Replay: Building Agent Observability That Actually Works in Production

**Session Description**

Most agent frameworks tell you what happened. Very few let you do anything about it.

This talk is about what comes after the log line. Drawing from building AgentOS — an agent runtime with execution replay, YAML-based policy gates, and automated failure diagnosis — I'll share the concrete decisions that went into making agent failures recoverable, not just observable.

Three primitives that changed everything:

- **Execution Replay:** every step writes an immutable snapshot. When something breaks, you replay from that exact point into a new run — original run untouched, context fully preserved.

- **Policy as a Gate:** YAML rules that evaluate before each step runs. Not logging after the fact — stopping before the damage. `deny`, `require_approval`, `pause_and_alert`, with hot reload and dry-run evaluation built in.

- **System MRI:** when a run fails, an automated diagnosis classifies the failure type, identifies affected steps, and suggests fixes — rule-based first, LLM-enhanced when available.

You'll walk away able to instrument your own agent system for replay, set policy-based gates that actually stop bad behavior, and get structured diagnosis when things go wrong.

**Session Format**

Stage Talk (18–20 min) + Lightning Talk (5–10 min)

**Tracks**

- evals & observability
- llm production infra
- sandboxes

**Special Flags**

없음 (체크 안 함)

**Speaker Pitch**

I built AgentOS solo, from Seoul — a runtime where when an agent fails, you don't just see what happened, you can replay from any step and get an automated diagnosis of why it broke. Everything in this talk exists as working code. I'm not describing what could be built; I'm sharing what I actually had to design when I needed agents to be recoverable, not just observable.

I'm a solo founder building this in production, not a researcher describing what could be done. I think that's the perspective this community actually needs right now.

---

### 제출 #2 — Stage Talk (18–20 min)

**Session Topic / Name**

YAML as a Safety Layer: Policy-Driven Human Oversight for Autonomous Agents

**Session Description**

The "human-in-the-loop" conversation in AI is mostly hand-wavy. Most implementations toggle between two extremes: fully automated, or human reviews everything.

This talk presents a third path built from production experience: a YAML-based policy engine that decides — before each step runs — whether an agent should proceed, pause for human approval, or be denied entirely.

What makes this different from access control or simple guards:

- Policies evaluate against rich step context: agent tags, risk level, tool call rate — not just identity.
- Three distinct actions: deny (hard stop), require_approval (human gate), pause_and_alert (async escalation).
- Hot reload without restart. Dry-run evaluation from a dashboard.
- Policy decisions become part of the immutable audit log — every deny, every approval, every escalation is evidence.

The result: agents that operate autonomously within defined boundaries, where humans set and adjust those boundaries at runtime — not at deploy time.

Concrete topics:

- Designing policy rules that don't become a maintenance nightmare
- Where to place human gates without killing throughput
- Using policy violations as a diagnostic signal, not just a blocker
- The audit trail as a compliance artifact

**Session Format**

Stage Talk (18–20 min) + Lightning Talk (5–10 min)

**Tracks**

- evals & observability
- llm production infra
- role: ai architects (ctos, vps of ai, leadership/management)

**Special Flags**

없음 (체크 안 함)

**Speaker Pitch**

I've had to design this tradeoff concretely — where exactly does a human step in, what context do they need, and how do you hand back control to the agent afterward? The policy engine in AgentOS is the answer I landed on after many iterations.

I built this solo, from Seoul. The code exists and runs. I want to share it because I think a lot of teams are reinventing this independently right now, and getting it wrong in the same ways.

---

### 공통 Personal Info

- **First Name:** Seonhye  
- **Last Name:** Gu  

**Bio (한 줄)**

Solo builder and AI/ML founder based in Seoul, Korea. Building AgentOS — an agent runtime with execution replay, policy-based human oversight, and automated failure diagnosis. Previously consulted on B2B AI strategy across enterprise clients in Korea.

**제출 링크:** https://www.accelevents.com/e/ai-engineer-worlds-fair-2026/speaker-registration

---

## PART 2: Vision Document — Evolutionary Policy & Living Constitution

*이 문서는 YC, a16z Speedrun 등 투자자 지원서의 Vision 섹션을 위한 초안이다. CFP 제출용이 아님. 아직 구현되지 않은 비전을 포함한다.*

### One-Line Vision

AI 에이전트를 위한 살아있는 헌법 — 에이전트와 인간이 함께 진화시키는 Policy.

### The Problem We're Actually Solving

지금 AI 에이전트 생태계는 두 가지 질문에 집중되어 있다.

- **Capability:** 에이전트가 더 잘 할 수 있는가?
- **Observability:** 에이전트가 뭘 했는지 볼 수 있는가?

하지만 세 번째 질문이 빠져 있다.

**Governability:** 에이전트가 어떻게 행동해야 하는지를, 누가, 어떻게, 언제 결정하는가?

현재 대부분의 팀은 이 문제를 코드로 하드코딩하거나, 배포 시점에 한 번 설정하거나, 아예 포기한다. 그 결과 에이전트는 강력하지만 통제 불가능하거나, 통제 가능하지만 쓸모없거나 둘 중 하나다.

### The Core Insight

우리가 수십 개의 에이전트 시스템 실험을 거쳐 도달한 핵심 통찰:

**Policy는 규칙집이 아니다. Policy는 에이전트의 세계관이다.**

규칙집은 정적이다. 세계관은 살아있다.

좋은 조직에서 구성원은 매 행동마다 코칭받지 않는다. 조직의 가치관과 판단 기준을 내면화하고, 그 안에서 자율적으로 행동한다. 그리고 그 가치관 자체도 조직의 경험을 통해 계속 진화한다.

에이전트도 마찬가지여야 한다.

### The Vision: Evolutionary Policy

세 개의 루프가 유기적으로 연결된 시스템:

```
┌─────────────────────────────────────────────────────────┐
│                    EVOLUTIONARY POLICY                   │
│                                                         │
│  Policy (세계관)                                         │
│       ↓ 에이전트가 Policy 안에서 자율 행동               │
│  Execution + Debate (행동 + 토론)                        │
│       ↓ 결과와 evidence가 쌓임                           │
│  Learning (학습)                                         │
│       ↓ Policy가 스스로 개선됨                           │
│  Policy (진화된 세계관)                                  │
└─────────────────────────────────────────────────────────┘
```

**이것이 Recursive Self Improvement와 다른 점:**

- **RSI**는 **능력 (capability)**의 자기 개선이다.
- **Evolutionary Policy**는 **가치관과 판단 기준 (values & judgment)**의 자기 개선이다.

능력의 개선은 통제를 잃을 위험이 있다. 가치관의 개선은 인간과 함께 방향을 잡을 수 있다.

### Five Primitives of the Vision

1. **Policy as World-View (세계관으로서의 Policy)** — 에이전트에게 행동 규칙을 주는 것이 아니라, 판단 기준을 준다. 에이전트는 그 세계관 안에서 스스로 판단하고 행동한다.

2. **Agent Debate with Evidence (증거 기반 에이전트 토론)** — 복잡한 의사결정을 에이전트들이 토론으로 처리. Agree to disagree 허용. 합의/비합의/근거를 evidence로 남겨 인간이 의사결정에 활용.

3. **Simulation Before Action (행동 전 시뮬레이션)** — 실제 세계에 영향을 미치기 전 시뮬레이션으로 결과 예측.

4. **Living Constitution (살아있는 헌법)** — Policy는 고정 문서가 아님. 행동 결과, debate evidence, 실패 패턴이 Policy를 개선. 때로 퇴화한 듯 보이는 변화도 더 큰 진화의 일부.

5. **Transparent Runtime (투명한 런타임)** — VSCode live처럼 backend를 MRI처럼 투명하게. 비전문가도 템플릿 안에서 설계·운영. 비용/자원 관리는 first-class primitive.

### Why Now

- EU AI Act 등으로 **감사 가능성 (auditability)** 요구 증가.
- 에이전트가 실무에 투입되며 통제는 이론이 아닌 현실 문제.
- Constitutional AI는 방향을 보였으나 기업 현장 구현은 아직 부족.

### What We've Built vs What We're Building

| 현재 (AgentOS MVP) | 비전 |
|-------------------|------|
| Policy — YAML 수동 작성 | 에이전트+인간이 함께 진화 |
| Oversight — Human gate | Debate + Evidence 기반 |
| Observability — Replay + MRI | Simulation + Transparent Runtime |
| Learning — 없음 | Policy self-improvement loop |

### For Investors: The One-Liner

"We're building the governance layer that makes AI agents safe to deploy in the real world — not by restricting what they can do, but by giving them a value system they can evolve."

### The Honest Assessment

이 비전의 대부분은 아직 구현되지 않았다.

**현재 작동하는 것:** Execution Replay, Policy Engine (YAML), Human Gate, System MRI, Reliability Card.

**다음에 빌딩할 것:** Agent Debate + Evidence 시스템. 그 다음: Policy self-improvement loop.

우리는 기반을 올바르게 쌓고 있다. 그리고 그 방향이 맞다고 확신한다.

---

*Document version: 2026-03-29 | ODD PLAYGROUND*
