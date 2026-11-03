---
harness_id: jorgitobg-agent-harness
project_name: agent-harness
repository: https://github.com/jorgitobg/agent-harness
review_ref: cc06ca7d9684d7d720b0e40062538a033010c5b7
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# agent-harness (jorgitobg)

## Review boundary

- System in focus: the presently released pedagogical Python agent-loop library, policy and tool registry; not the distinct indexed repository `0xenzyme/agent-harness`.
- Purpose and identity: expose understandable building blocks for a model/tool coding harness, one feature at a time.
- Relevant environment: embedding developer, injected model client, injected tool handlers and approval adapters, Python callers and tool data.
- Standard-distribution boundary: `src/agent_harness` as supplied at the pinned commit; no external model runtime, application CLI or tool-backed agent installation is packaged.
- Credited operating / distribution surfaces: `application/agent_loop.py`, `registry.py`, `guardrails.py`, `domain` ports, policies and budgets.
- Adjacent first-party surfaces excluded from ownership: `tests/`, specification, ADR, CI and `adapters/scripted.py` (explicitly only a fake model for tests/offline demo); external model clients and hypothetical later US4–US8 adapters.
- First-party operating / deployment modes considered: library `AgentLoop.run` with caller-injected `ModelClient`, `ToolRegistry` and optional `GuardedRegistry`; scripted-model test simulation; no bundled real-model adapter, CLI, agent entrypoint or default agent workload.
- Recursion level: the published self-contained library distribution, not an application a downstream integrator might construct.
- Reviewed revision: `cc06ca7d9684d7d720b0e40062538a033010c5b7`.
- Observation date: 2026-11-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The source implements typed `ToolSpec`/`ToolCall`/`ToolResult`, registry validation/dispatch, a synchronous `AgentLoop` that invokes a **caller-supplied** `ModelClient.complete`, and a wrapper for preselected allow/deny/ask permission policies. All actual tool behavior comes from an embedding caller's handlers. The only bundled model client, `ScriptedModel`, explicitly replays predetermined turns in tests/offline simulation; it neither autonomously interprets a changing goal nor invokes a real provider. README marks a CLI confirmation adapter pending, context/memory, subagents, model router, tracing/replay and evaluations as planned. No supported first-party operating mode wires a goal-deciding model and executable tool set into an autonomous end-to-end agent. The core is a meaningful construction primitive, but a later third-party composition is not credited as the current shipped agentic system.

Primary evidence: [README](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/README.md), [model/loop port](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/src/agent_harness/application/agent_loop.py), [script-only client](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/src/agent_harness/adapters/scripted.py), [tool registry](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/src/agent_harness/application/registry.py), [guardrails](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/src/agent_harness/application/guardrails.py), [spec](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/docs/spec/0001-agent-harness.md).

## Operational model

The library can execute a scripted replay and allows an **external developer** to supply an actually deciding model plus tools; neither the provided scripts nor the abstract `Protocol` is an independent first-party operational agent. For the frozen standard distribution, no qualifying agentic S1 is demonstrated. This is a bounded **exclusion**, not a finding that the library cannot be integrated into a viable agent system. An integrated deployment would require a new system boundary and fresh review.

## S1 — Operations

- State: —
- Function: no shipped agent interprets open-ended task evidence to choose subsequent substantive actions.
- Disturbance / variety regulated: typed calls/errors, step/time/cost/token budgets and developer-supplied commands.
- Decisive decision or feedback right: choose task-effective next model/tool action after inspecting live tool results.
- Decision owner: external `ModelClient` implementer if provided, or pre-authored script in the only shipped client; the library itself owns validation/execution plumbing.
- Supporting / enforcement mechanisms: `AgentLoop.run`, `ToolRegistry`, `GuardedRegistry`, typed stops and `Budget`.
- Closure path: caller prompt → injected `model.complete` → dispatcher output → injected model again; the necessary autonomous decision owner is not supplied by the standard distribution.
- Why this is / is not agent-owned: a real model adapter and task tools are missing; scripted turns are replay data, not model agency.
- Evidence: [agent loop](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/src/agent_harness/application/agent_loop.py), [scripted adapter](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/src/agent_harness/adapters/scripted.py), [README status](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is a distribution-boundary admission judgment; the agent loop constructor is implemented and could close in a separately integrated system.

### Absence scope

- Surfaces inspected: package file inventory, README US status, main `AgentLoop`/`ModelClient` port, scripted adapter, tool registry, guardrails and tests.
- Plausible first-party paths checked: bundled model client as operating S1, standalone command entrypoint, model callback as locally owned agent, scripted tests as an operational mode.
- Why no material first-party path remains: only shipped model behavior is predetermined replay; real task discretion and tool handlers must be supplied by another application, and no production agent entrypoint is present.

## S2 — Coordination

- State: —
- Function: no operational inter-S1 attenuation among distinct autonomous internal cells.
- Disturbance / variety regulated: malformed tool calls and permissions, not cross-agent conflict.
- Decisive decision or feedback right: resolve interference and return changed operating constraints to multiple S1 actors.
- Decision owner: none within this library mode.
- Supporting / enforcement mechanisms: tool registry, permission gate and ordered iteration through calls.
- Closure path: one injected loop dispatches calls sequentially, with no separately built cross-unit adjustment relation.
- Why this is / is not agent-owned: neither subagents nor S2-specific inter-agent coordination exist at this revision.
- Evidence: [README US6 planned](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/README.md), [loop](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/src/agent_harness/application/agent_loop.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: tool sequencing is not independent S2 coordination.

### Absence scope

- Surfaces inspected: registry, loop, policy, docs/spec US6 and complete runtime inventory.
- Plausible first-party paths checked: tool dispatch as S2; planned subagents; guardrails as conflict resolution.
- Why no material first-party path remains: one abstract model loop has no internal S1 relationships or specific interference feedback contract.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system present-operational management of multiple S1 units.
- Disturbance / variety regulated: per-run budgets and one-call permission decisions.
- Decisive decision or feedback right: choose current whole-system priorities, resources or interventions, and return them to operations.
- Decision owner: embedding developer/operator selects fixed budget and tool policy; runtime deterministically enforces.
- Supporting / enforcement mechanisms: max-step/token/cost/time checks, permission levels, confirmation port.
- Closure path: per-run limit breach yields typed stop; not a parent current-control decision returned to a qualifying agent organization.
- Why this is / is not agent-owned: enforcement of externally specified limits is not S3 ownership.
- Evidence: [loop budget](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/src/agent_harness/application/agent_loop.py), [permission guardrails](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/src/agent_harness/application/guardrails.py).
- Basis: structural.
- Confidence: high.
- Caveats: operator choice of per-tool permissions is not a parent S3 loop at this boundary.

### Absence scope

- Surfaces inspected: loop budget, policies, confirmation protocol, package inventory.
- Plausible first-party paths checked: budget as S3; permission policy as S3; human confirmation as parent S3.
- Why no material first-party path remains: all are local preconfigured constraints on a nonexistent packaged agent organization, without whole-system supervisory discretion.

## S3* — Complementary audit

- State: —
- Function: no independent complementary source-observing audit of operational results.
- Disturbance / variety regulated: bad tool arguments and disallowed tool calls are checked inline.
- Decisive decision or feedback right: independently challenge S1 reports using complementary evidence and return findings.
- Decision owner: none; validation and developer tests are ordinary correctness gates.
- Supporting / enforcement mechanisms: JSON-schema validator, error results, CI unit tests.
- Closure path: local validation rejects malformed calls, not an independent audit feedback channel.
- Why this is / is not agent-owned: schema validity and test fixtures do not examine live results independently.
- Evidence: [registry](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/src/agent_harness/application/registry.py), [README status](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: later planned tracing/evaluations cannot be borrowed as current audit ownership.

### Absence scope

- Surfaces inspected: registry guards, tests, planned US8, script fixture and package.
- Plausible first-party paths checked: JSON validation, CI tests and planned evals as S3*.
- Why no material first-party path remains: no shipped independent audit decision owner, complementary operational access or return path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective environmental sensing and capability adaptation loop.
- Disturbance / variety regulated: transient model errors and runtime budget breaches.
- Decisive decision or feedback right: formulate capability-change options from future/external conditions and feed accepted options into present operations.
- Decision owner: future developers or embedding application, not a first-party shipped strategic actor.
- Supporting / enforcement mechanisms: typed model-error stop and externally selected budget.
- Closure path: library returns a typed stop; no option generation or strategy-to-current-control feedback.
- Why this is / is not agent-owned: roadmap items and a planned router/compactor are not operational S4.
- Evidence: [README roadmap](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/README.md), [loop](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/src/agent_harness/application/agent_loop.py).
- Basis: structural.
- Confidence: high.
- Caveats: future versions may support adaptation and must be assessed at their own refs.

### Absence scope

- Surfaces inspected: spec/roadmap, runtime loop, package file inventory and model port.
- Plausible first-party paths checked: provider fallback (planned), context compaction (planned), external developer improvements as S4.
- Why no material first-party path remains: none is a current shipped future-oriented intelligence/feedback loop in the assessed mode.

## S5 — Policy and identity

- State: —
- Function: no identity or ultimate-policy governance loop at this library recursion.
- Disturbance / variety regulated: ordinary tool-access risk.
- Decisive decision or feedback right: decide and return identity-level policy governing future operations.
- Decision owner: embedding developer and human users select static call permission policy; no first-party identity authority.
- Supporting / enforcement mechanisms: `PermissionPolicy`, `GuardedRegistry`, confirmation port.
- Closure path: one tool is permitted/refused under predetermined rules; no identity-level matter reaches legitimate authority and returns as updated ultimate policy.
- Why this is / is not agent-owned: per-call approval and static access levels are not S5.
- Evidence: [policy](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/src/agent_harness/domain/policy.py), [guardrails](https://github.com/jorgitobg/agent-harness/blob/cc06ca7d9684d7d720b0e40062538a033010c5b7/src/agent_harness/application/guardrails.py).
- Basis: structural.
- Confidence: high.
- Caveats: first-party parent-governed mode requires an actual identity-level closure, not an abstract `ConfirmationPort`.

### Absence scope

- Surfaces inspected: policy, guardrails, README, specs and package.
- Plausible first-party paths checked: ask/deny as ultimate policy, confirmation caller as parent S5, accepted spec/ADR as governance S5.
- Why no material first-party path remains: static per-call enforcement and development documents lack a runtime identity-level authoritative return path.

## Distributed OSS parent arrangement

No S3/S4/S5 parent governance is inferred from maintainers or accepted specs: their decisions develop the library and are not part of an operating first-party agent organization at the pinned standard distribution boundary.

## Self-hosted and non-human modes

An embedding application could supply autonomous model clients, tool handlers and operator controls; that hypothetical downstream system is not a first-party self-hosted mode of this released package.

## Recursion, variety, escalation and evidence gaps

- Recursion: the library offers pieces for one downstream agent; multi-unit organizational recursion is not packaged.
- Variety: schema, budget and permission variety are handled deterministically; open-world task variety must be handled by an injected model not supplied in distribution.
- Escalation: `ConfirmationPort` and `MODEL_ERROR`/budget stops inform an embedding caller; no established S3/S5 parent return closure exists.
- Evidence gaps: no live provider E2E test was attempted. The source evidence is sufficient for the narrow current distribution exclusion; absence does not rule out a locally implemented `ModelClient` by a downstream integrator.

## Outcome

**Proposed exclusion — `excluded-no-agentic-vsm`.** Genuine tool and model-loop primitives are shipped, but the only included model implementation is an offline scripted fixture and there is no first-party autonomous model/tool runtime. Reassess on a new pinned version if a supported real-model adapter and executable agent mode are added.
