---
harness_id: openjarvis
project_name: OpenJarvis
repository: https://github.com/open-jarvis/OpenJarvis
review_ref: 61c2f89096006604774779b348176ee552afa01b
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenJarvis

## Review boundary
Pinned reusable OpenJarvis runtime/framework: first-party built-in agent modes, shared tool/memory/scheduling runtime and trace-driven learning machinery. Imported community skills, external cloud/model engines and deployment-specific presets are not credited as first-party organizational functions.

Reviewed revision: `61c2f89096006604774779b348176ee552afa01b`. Contract: Profile `0.2.1`, Methodology `0.3.1`. Upstream drift was checked: current `main` was one commit ahead at review time and the intervening change concerned SDK engine cleanup, so the candidate pin is preserved.

## Primary evidence
- [`README.md`](https://github.com/open-jarvis/OpenJarvis/blob/61c2f89096006604774779b348176ee552afa01b/README.md) — built-in agents, scheduled/continuous operation and trace-driven optimization surfaces.
- [`docs/user-guide/agents.md`](https://github.com/open-jarvis/OpenJarvis/blob/61c2f89096006604774779b348176ee552afa01b/docs/user-guide/agents.md) — built-in agent classes and the OrchestratorAgent tool-calling loop.
- [`docs/getting-started/configuration.md`](https://github.com/open-jarvis/OpenJarvis/blob/61c2f89096006604774779b348176ee552afa01b/docs/getting-started/configuration.md) — learning policies, user-authored agent/objective/persona configuration and defaults.
- [`src/openjarvis/learning/learning_orchestrator.py`](https://github.com/open-jarvis/OpenJarvis/blob/61c2f89096006604774779b348176ee552afa01b/src/openjarvis/learning/learning_orchestrator.py) — trace-to-learn-to-eval cycle, agent-config evolution and acceptance gate.

## S1 — Operations
`A`. Tool-using built-in agents such as Orchestrator/ReAct and persistent Operative modes execute model/tool trajectories autonomously within their configured task boundary. A selected built-in agent is the operational unit at the reusable-runtime boundary. Confidence: high.

## S2 — Coordination
`—`. The built-in agents are alternative execution modes rather than mutually interacting operational units. `OrchestratorAgent` is explicitly one multi-turn tool-calling loop; tool dispatch, schedules, recursive calls and persistent state do not establish a concrete inter-S1 interference-regulation relation. Confidence: high.

## S3 — Inside-and-now control
`—`. No distinct first-party actor was established that maintains a current view of multiple operational units and exercises authority over shared organizational resources, commitments, priorities or constraints. The `orchestrator` name describes one S1 tool loop rather than S3. Confidence: high.

## S3* — Complementary audit
`—`. Tracing, evaluation and guardrail-shaped runtime controls inspect or constrain normal execution, but the reviewed standard distribution does not establish a materially different first-party evidence-access channel with an independent audit judgment feeding corrective control. Confidence: medium-high.

## S4 — Outside-and-then intelligence
`—`. LearningOrchestrator mines the system's own traces, evolves routing/agent configuration, optionally trains, then evaluates the result. This is genuine self-improvement, but its source is accumulated internal operational evidence rather than an established outside-and-then environmental intelligence loop. Learning alone is not S4. Confidence: high.

## S5 — Policy and identity
`—`. `SOUL.md`, objectives, system prompts, model/cloud policy and user configuration can express identity or constraints, but they are parent-authored configuration surfaces. No first-party runtime process was established in which an identity/ultimate-policy tension reaches legitimate ultimate authority and returns as changed organizational policy. Confidence: high.

## Recursion, variety, and escalation
Multiple built-in agent types, models, tools and persistent modes amplify operational variety; configuration, turn limits, routing and evaluation attenuate it. Presets are deployments of the reusable runtime rather than automatically separate viable recursion levels.

## Admission conclusion
Canonical vector: `A — — — — —`.

The parked provisional result `A ? ? — A ?` is resolved at the pinned boundary: no first-party S2/S3/S5 closure was established, and the trace-driven learning loop is internal self-improvement rather than S4.