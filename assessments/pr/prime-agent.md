---
harness_id: prime-agent
project_name: Prime Agent
repository: https://github.com/PrimeIntellect-ai/prime-agent
review_ref: 66abc2a604fc42a220292a1ca4cf33ee60cb5733
reviewed_at: 2026-09-17
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Prime Agent

## Review boundary
Pinned first-party Prime Agent coding/research runtime at `66abc2a604fc42a220292a1ca4cf33ee60cb5733`, including its persistent Python control environment, recursive child agents, background/session control and Continual Harness refinement. External providers and downstream task organizations are outside the boundary.

Contract: Profile `0.2.2`, Methodology `0.3.1`. Generation provenance is not backfilled because the pre-admission proposal did not record it.

## Primary evidence
- [`README.md`](https://github.com/PrimeIntellect-ai/prime-agent/blob/66abc2a604fc42a220292a1ca4cf33ee60cb5733/README.md) — coding/research agent, persistent environment, autonomous/background operation and Continual Harness surface.
- [`packages/coding-agent/docs/rlm.md`](https://github.com/PrimeIntellect-ai/prime-agent/blob/66abc2a604fc42a220292a1ca4cf33ee60cb5733/packages/coding-agent/docs/rlm.md) — recursive child-agent spawning, child registry/status, follow-up and lifecycle control from the parent environment.
- [`packages/coding-agent/src/core/refinement/refinement.ts`](https://github.com/PrimeIntellect-ai/prime-agent/blob/66abc2a604fc42a220292a1ca4cf33ee60cb5733/packages/coding-agent/src/core/refinement/refinement.ts) — evidence-backed durable refinement, candidate state, snapshots and rollback.

## Repository architecture
Prime Agent supplies a model-driven coding/research loop with a persistent Python control environment. The parent can spawn recursive children, inspect their state, follow up and terminate/delete child work while the host maintains lifecycle and execution machinery. Continual Harness persists prompts, memories, skills and subagent specifications and can refine them from collected trajectory evidence with snapshots/rollback.

## Operational model
Agent actors perform coding/research operations. At the reviewed recursion, the parent agent also has a current view of its child work and discretionary intervention rights over that live operational portfolio. Host limits and runtime lifecycle machinery support those decisions but do not inherit S3 ownership.

## S1 — Operations
`A`. First-party model-driven agents autonomously execute coding/research work through tools and the persistent control environment. Confidence: high.

## S2 — Coordination
`—`. Recursive spawning, direct messaging and parent/child communication establish delegation and communication, but the reviewed evidence does not identify a specific peer-S1 interference/conflict/oscillation together with an S2-specific attenuation and feedback loop. The earlier proposal's `C` treated generic composability as coordination evidence. Confidence: high.

## S3 — Inside-and-now control
`A`. The parent agent can inspect the current child registry/status and make discretionary whole-subtree intervention decisions such as spawning additional work, issuing follow-ups and terminating/deleting child work. Those decisions change subsequent current operation; host budgets/lifecycle controls are supporting enforcement. Confidence: medium-high.

## S3* — Complementary audit
`—`. Quality gates and refinement evidence are normal validation/optimization mechanisms. No sufficiently independent first-party audit actor with complementary access and a distinct audit judgment feeding corrective current control was established at the pin. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. Continual Harness performs real durable refinement from operational trajectories, but learning/self-improvement alone is not S4. The reviewed path does not establish an outside-and-then environmental intelligence distinction that generates prospective adaptation options and returns them into present capability. Confidence: high.

## S5 — Policy and identity
`—`. Base goals, task objectives and parent-supplied configuration constrain the agent but do not form an operationally closed identity/ultimate-policy loop. Parent ownership of a goal by itself is not `P`. Confidence: high.

## Recursion, variety, and escalation
Recursive children amplify problem-solving variety. Parent-agent child lifecycle decisions and host limits attenuate current variety; Continual Harness snapshots/rollback attenuate durable-change risk. A spawned child may be analyzed at its own recursion level, but spawning alone is not VSM recursion.

## Admission conclusion
Canonical vector: `A — A — — —`.

Pre-admission correction of the stale proposal `A C A C A P`: delegation/messaging are not sufficient S2, deterministic gates are not independent S3*, refinement alone is not S4, and parent-authored goals do not establish S5.