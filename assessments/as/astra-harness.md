---
harness_id: astra-harness
project_name: Astra Harness
repository: https://github.com/ytinyx/astra-harness
review_ref: 0c24783eaef9d3b00f7176eb86b75410f42231a2
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Astra Harness

## Review boundary

- System in focus: Astra Harness's installed Python model/tool task engine and local single-user application, persistent runs/sessions, permissions and web/CLI interfaces at pinned source.
- Purpose and identity: turn a user's open-ended goal into authorized, observable, resumable model-guided tool execution in a selected local workspace.
- Relevant environment: user workspace files and processes, local browser UI, optional model providers, local SQLite state, registered tools/MCP services and user approval decisions.
- Standard-distribution boundary: the `astra_harness` Python package and supported local application/engine modes; external providers/MCP services are dependencies, not credited decision owners.
- Credited operating / distribution surfaces: `astra_harness/engine.py`, `application.py`, `runtime.py`, `tools.py`, builtin file/command tools, workspace/permission bindings, model adapter, CLI/web server and SQLite store.
- Adjacent first-party surfaces excluded from ownership: `examples/`, `tests/`, `benchmark.py`, `evaluation.py`, development/CI/release machinery and website/product planning documents. These do not run as a separate auditor or manager in the installed agent mode.
- First-party operating / deployment modes considered: model-driven task loop, direct host tool operation, local web and CLI, tool approval/pause/resume, model/profile selection, workspace binding, durable recovery, optional installed extensions/MCP/knowledge.
- Recursion level: the installed local single-user task organization; individual runs are S1 activity, not an independently governed agent fleet.
- Reviewed revision: `0c24783eaef9d3b00f7176eb86b75410f42231a2`.
- Observation date: 2026-11-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

`Engine` registers a fixed tool snapshot, records model/tool phases, asks an injected model for `ModelResponse`, validates tool calls, executes permitted commands and appends resulting `ToolResult` messages before the next model step. It records explicit waiting-approval, paused, unknown-side-effect and terminal states. `Application` binds the engine to SQLite-backed sessions and runs, workspace/model profiles, single background worker, approval APIs and web/CLI control. Unknown side effects block new dispatch pending operator reconciliation; in-flight tool execution is not blindly retried. Direct host `submit_tool` is a distinct caller-selected operation without a model phase and is not counted as autonomous S1. Tests/benchmarks exercise the engine but are not deployed runtime audit agents. Model-provider endpoints and MCP servers remain outside the first-party evidence boundary.

Primary evidence: [README](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/README.md), [engine](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/engine.py), [application](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/application.py), [runtime](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/runtime.py), [tests](https://github.com/ytinyx/astra-harness/tree/0c24783eaef9d3b00f7176eb86b75410f42231a2/tests).

## Operational model

The model-facing task execution loop is the operative S1. The model chooses substantive next tool calls and interprets returned observations, while the host validates/executes those calls, persists checkpoints, and requires operator approval for sensitive effects. User profile/tool grants and one-worker dispatch are strong constraints but do not replace the model's task discretion. Separately queued runs/sessions do not by themselves establish an S2 or S3 organizational relation; the application intentionally serializes one executor and protects state rather than governing several distinct simultaneously viable S1 cells.

## S1 — Operations

- State: A
- Function: repository-owned model/tool iterative task actor transforms goals into tool-backed outcomes.
- Disturbance / variety regulated: changing task requirements, tool observations/errors, approval decisions, uncertain side effects and workspace state.
- Decisive decision or feedback right: select next task-relevant tool action or final response based on prior messages and tool results.
- Decision owner: model-guided task agent as wired by `Engine._model` and `_tool` within the first-party runtime; provider computes outputs but is not a foreign agent harness.
- Supporting / enforcement mechanisms: tool schema/permissions, time/step budgets, approval hash, run store, workspace/model bindings, cancel/pause/unknown-state guards.
- Closure path: submitted task → model response → validation and tool call or explicit approval → result/error appended to conversation → subsequent model decision/final result.
- Boundary reachability: `Application.submit` creates and persists an `Engine` state, `_worker` advances it, and the shipped CLI/web APIs expose the complete local mode; no example-only actor is needed.
- Why this is / is not agent-owned: model outputs choose task actions; host caps, queues and permissions enforce externally selected constraints instead of choosing the solution.
- Evidence: [engine](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/engine.py), [application](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/application.py).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: source-controlled and local test evidence; no claim of paid-provider real-world task success.

## S2 — Coordination

- State: —
- Function: no independently established inter-S1 adjustment/anti-oscillation between distinct operative agent units.
- Disturbance / variety regulated: active-session duplication, request-id collisions and uncertain side effects are controlled at the run-store/executor level.
- Decisive decision or feedback right: choose coordination to attenuate interference among multiple S1 units; no such agentic cross-unit choice is shipped.
- Decision owner: deterministic `Application` admission and its single `_worker`, not a separate S2 actor.
- Supporting / enforcement mechanisms: `request_id` idempotence/conflict checks, one-active-run-per-session check, single worker, blocking unknown states and tool-update reservations.
- Closure path: invalid/conflicting submissions are rejected or queued; a single run executes at a time, rather than negotiating/feedback-adjusting two simultaneous S1 agent behaviours.
- Why this is / is not agent-owned: meaningful safety isolation exists, but it is a serialized host execution policy, not evidenced S2-specific coordination between independently operating first-party S1 units.
- Evidence: [application](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/application.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a multi-agent composition could reuse these primitives, but is not the assessed standard mode.

### Absence scope

- Surfaces inspected: application submit/worker, workspace identities, stores, tool registration and engine loop.
- Plausible first-party paths checked: queued sessions as separate S1; unknown-effect global block as S2; workspace/model conflicts as anti-oscillation; MCP calls as inter-agent communication.
- Why no material first-party path remains: the first-party mode executes one task agent at a time; the observed protections prevent execution conflicts rather than closing an inter-S1 regulatory feedback relationship.

## S3 — Inside-and-now control

- State: —
- Function: no independent whole-system current-operational supervisory decision over an S1 organization is established.
- Disturbance / variety regulated: tool risk, runtime limits, queue state, model and workspace configuration drift.
- Decisive decision or feedback right: choose/revise shared operational commitments, priorities and resources for the whole.
- Decision owner: local operator for approvals/configuration, runtime for deterministic safety; model actor owns task-local actions.
- Supporting / enforcement mechanisms: statuses, limits, select-profile/workspace API, pause/cancel, `reserve_tool_update`, SQLite run views.
- Closure path: per-tool approval/denial or config reservation changes one run's feasibility; no function-specific parent supervisory whole-system decision returns to a distinct current S1 organization.
- Why this is / is not agent-owned: an operator dashboard and execution controls alone do not establish S3, S3=P or autonomous current-control ownership.
- Evidence: [application](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/application.py), [engine](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/engine.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a larger multi-user organization would require a new boundary review.

### Absence scope

- Surfaces inspected: run-state API, workspace/model configuration, approval/cancel, worker, tool updates and limits.
- Plausible first-party paths checked: dashboard as whole current view; approval as parent S3; worker scheduling as whole-resource choice.
- Why no material first-party path remains: controls enforce selected single-run constraints and local authorizations, with no S3-owned discretionary whole-system intervention/return path.

## S3* — Complementary audit

- State: —
- Function: no operational independent audit of routine execution claims plus corrective return is wired into the user task mode.
- Disturbance / variety regulated: invalid model responses, unsupported tools, uncertain effects and model/time budgets.
- Decisive decision or feedback right: independently inspect actual operation and challenge ordinary reporting to control.
- Decision owner: no separate audit actor; executor/host validators perform regular checks.
- Supporting / enforcement mechanisms: event tracing, snapshots, protocol validators, unknown-effect quarantine, tests and benchmark evaluator.
- Closure path: a failed check or uncertain side effect stops/blocks a run; benchmark and tests are external development evidence, not a deployed complementary auditor returning corrective management feedback.
- Why this is / is not agent-owned: source-level integrity checks are valuable but not a functionally separate independent S3* relationship.
- Evidence: [engine](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/engine.py), [evaluation](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/evaluation.py).
- Basis: structural.
- Confidence: high.
- Caveats: external operator audits could be added but are not first-party active paths.

### Absence scope

- Surfaces inspected: engine validation, telemetry, recovery/unknown safeguards, evaluation module and tests.
- Plausible first-party paths checked: independent verifier from evaluation, trace as S3*, approvals as an alternate access path.
- Why no material first-party path remains: no independent auditor receives ordinary claims, inspects different ground truth and returns corrective current-control findings in the supported runtime.

## S4 — Outside-and-then intelligence

- State: —
- Function: no future-oriented environmental options loop closes into current operational capability.
- Disturbance / variety regulated: user prompts, added knowledge materials, model profile choices and extension configuration.
- Decisive decision or feedback right: interpret external/future distinctions, generate adaptation options and return changes to present capabilities.
- Decision owner: local user/operator selects profiles, workspaces and knowledge; task model handles immediate goals.
- Supporting / enforcement mechanisms: model/skill/knowledge profiles, context assembly, extension tooling and workbench APIs.
- Closure path: selected content/configuration conditions later model requests, but no standing prospective alternative-evaluation/selection/implementation path is established.
- Why this is / is not agent-owned: contextual knowledge and configurable tools are not S4 without external-and-prospective adaptation feedback.
- Evidence: [application](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/application.py), [knowledge library](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/knowledge_library.py).
- Basis: structural.
- Confidence: high.
- Caveats: external product development and offline benchmarking are adjacent, not shipped S4.

### Absence scope

- Surfaces inspected: knowledge/profile/skills surfaces, task context, runtime options and offline evaluation.
- Plausible first-party paths checked: knowledge uploads as sensing; model switching as adaptation; tests/benchmarks as S4 options.
- Why no material first-party path remains: supported interactions are user-directed configuration and current-task context, without a future-environment options loop returning to current capability.

## S5 — Policy and identity

- State: —
- Function: no autonomous or operational parent-governed ultimate-policy/identity decision path exists at the assessed local task recursion.
- Disturbance / variety regulated: permissions, credential protection, workspace selection and tool-approval rules.
- Decisive decision or feedback right: settle identity/ultimate-policy matters and bind future operation.
- Decision owner: developer/operator configuration and ordinary action-specific human approval, not a demonstrated ultimate-policy authority/return loop.
- Supporting / enforcement mechanisms: immutable tool snapshots, explicit approvals, permission catalogs, system instruction and host security boundaries.
- Closure path: updated configuration or user grant constrains later tool calls; no identity-level matter-to-legitimate-parent decision and returned governance transition is evidenced.
- Why this is / is not agent-owned: security controls and per-tool approvals are not S5 or S5=P merely because a human can override a run.
- Evidence: [engine](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/engine.py), [application](https://github.com/ytinyx/astra-harness/blob/0c24783eaef9d3b00f7176eb86b75410f42231a2/astra_harness/application.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: wider institutional deployment governance is outside this local single-user boundary.

### Absence scope

- Surfaces inspected: permission/model/workspace configuration, system instruction, user approval and run-state transitions.
- Plausible first-party paths checked: tool policy as S5; operator approval as parent S5; profile change as identity decision.
- Why no material first-party path remains: these concern ordinary safety and task configuration, not returned identity/ultimate-policy closure at the declared recursion.

## Distributed OSS parent arrangement

Contributor repository governance is excluded from the distributed application runtime; no organization-level parent ownership of S3/S4/S5 is borrowed from it.

## Self-hosted and non-human modes

The supported local operator mode provides tool approval, pause/resume, profile and workspace control; no separate function-specific parent S3/S4/S5 loop is evidenced. The system is not represented as a non-human autonomous multi-level organization.

## Recursion

Sessions, tool plugins, MCP calls and workspaces do not demonstrate recursively viable agent organizations. The task engine is the one operative S1 at this boundary.

## Variety and escalation

Validation attenuates malformed model/tool variety; approvals route risk to the operator, and unknown side-effect states prevent unsafe replay until operator resolution. These are valuable S1 support and safety channels but not automatic S3/S3*/S5 states or algedonic proof.

## Evidence gaps

No paid model-provider E2E outcome is claimed. Local Python unittest discovery exercised 747 tests, but environment lacks optional `httpx`/`fastapi` dependencies and yielded 102 import/setup errors; these are not interpreted as first-party behavior failures. The source-level S1 loop and bounded higher-function non-claims remain independently inspectable.
