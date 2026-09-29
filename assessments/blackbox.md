---
harness_id: blackbox
project_name: Blackbox
repository: https://github.com/tyxter-dev/blackbox
review_ref: d5be68e03ca7750920569578710a2ee25d25530c
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Blackbox

## Review boundary

- System in focus: first-party `tyxter-dev/blackbox` runtime at frozen revision `d5be68e03ca7750920569578710a2ee25d25530c`, including the shared `AgentLoop`, local agent/session machinery, runtime state/events, tools/MCP/skills, approvals, workspaces, workspace-agent contracts, output validation, and the environment-worker reference path.
- Purpose and identity: a provider-native multi-provider runtime that owns model/tool iteration and common lifecycle/contracts around local or provider-managed agent sessions and portable governed workspace-agent packages.
- Relevant environment: external model providers, provider-managed agents such as Claude Code/OpenAI Agents SDK, caller applications, external work/control planes, workspace backends, users/operators, and tool/MCP services.
- Standard-distribution boundary: the local first-party autonomous model/tool loop, local session facade, runtime policies/permissions, typed events/state/artifacts, package registry/scheduler contracts, and reference worker implementation are inside. Provider-managed agent cognition, external queue/control-plane lease ownership, application scheduling decisions, and caller-supplied evaluators/policies remain outside ownership claims.
- Credited operating / distribution surfaces: high-level `AgentRuntime.run(...)`, `LocalAgentProvider` through the shared `AgentLoop`, package execution through `run_workspace_agent`, and local tools/workspaces/policies that feed observations back into that loop.
- Adjacent first-party surfaces excluded from ownership: tests/CI, repository governance, development plans, examples as actors, offline evaluation utilities without corrective return, deterministic schedule execution, and lifecycle facades controlled only by caller/application decisions.
- Recursion level: one Blackbox local model/tool loop is the operational S1. Provider-managed sessions remain external agent systems supervised through an adapter boundary; plurality of sessions/packages/workers is not itself treated as a higher VSM recursion.
- Reviewed revision: `d5be68e03ca7750920569578710a2ee25d25530c`.
- Observation date: 2026-09-29.

## Repository architecture

Blackbox explicitly defines `AgentLoop` as the reusable autonomous execution layer between provider-native model turns and tool execution. It repeatedly streams model events, dispatches requested local/hosted tools under first-party policy/approval checks, feeds results back through provider-native continuation state, and continues until the model stops requesting tools or a terminal bound is reached. The high-level runtime and the first-party local agent provider both delegate to this loop.

The repository also provides session lifecycle APIs, workspace-agent packaging/permissions/schedules, environment-worker queue contracts, traces, and evaluator helpers. Those mechanisms do not by themselves move higher VSM functions inside the assessed organization: scheduled runs are deterministic/caller-driven; provider-managed sessions remain external cognition; the reference work source is explicitly single-process and real multi-node lease ownership belongs to a substituted control plane; `evaluate_trace` returns reports but has no first-party corrective control loop.

Primary evidence:

- [`README.md`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/README.md)
- [`src/blackbox/runtime/README.md`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/runtime/README.md)
- [`src/blackbox/runtime/agent_loop.py`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/runtime/agent_loop.py)
- [`docs/AGENT.md`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/docs/AGENT.md)
- [`src/blackbox/workspace_agents/README.md`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/workspace_agents/README.md)
- [`src/blackbox/workspace_agents/runtime.py`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/workspace_agents/runtime.py)
- [`src/blackbox/workspace_agents/executor.py`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/workspace_agents/executor.py)
- [`src/blackbox/workers/README.md`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/workers/README.md)
- [`src/blackbox/workers/source.py`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/workers/source.py)
- [`src/blackbox/workers/worker.py`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/workers/worker.py)
- [`src/blackbox/observability/evals.py`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/observability/evals.py)

## Operational model

A local Blackbox run asks the configured model for a turn, captures requested tools, applies Blackbox policy/approval/permission checks, executes allowed tools, and feeds their results back to the same model through provider-native continuation. This creates a first-party operational feedback loop even though the model provider itself is external. Other repository surfaces supervise or package execution, but no first-party autonomous whole-system manager, independent corrective auditor, prospective adaptation loop, or identity organ is established at this frozen boundary.

## S1 — Operations

- State: A
- Function: perform open-ended task work through a repeated model→tool→observation loop.
- Disturbance / variety regulated: task changes, model responses, tool/environment results and failures, approval/policy outcomes, workspace state, and provider continuation state.
- Decisive decision or feedback right: choose the next substantive response/tool request after observing prior tool results and current task state.
- Decision owner: the model-driven local Blackbox agent actor operating through `AgentLoop`.
- Supporting / enforcement mechanisms: `AgentLoop`, model/provider streaming, `ToolRuntime`, hosted tool runner, approval/policy checks, tool-call budgets, provider state, output finalization, typed events, workspaces, and session state.
- Closure path: task/input → model turn → requested tool/action → first-party policy/dispatch/execution → tool result returned as continuation input → later model turn revises/continues → final output or bounded stop.
- Boundary reachability: both `AgentRuntime.run(...)` and the first-party `LocalAgentProvider` use the shared autonomous loop in normal shipped paths.
- Why this is / is not agent-owned: deterministic host code gates/executes tool choices, but the external model inference supplies the substantive next-action choice within the first-party closed execution loop; removing that model-driven actor leaves only dispatch machinery.
- Evidence: [`README.md`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/README.md); [`src/blackbox/runtime/agent_loop.py`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/runtime/agent_loop.py); [`src/blackbox/runtime/README.md`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/runtime/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider-managed coding agents are not needed for this credit and are not imported as Blackbox-owned actors; S1 rests on the first-party local loop.

## S2 — Coordination

- State: —
- Function: no qualifying first-party S2 coordination function is established at the assessed boundary.
- Disturbance / variety regulated: no concrete inter-S1 disturbance with a complete first-party attenuation-and-feedback relation is established.
- Decisive decision or feedback right: no qualifying coordination right is established.
- Decision owner: none identified for S2 inside the assessed organization.
- Supporting / enforcement mechanisms: tool concurrency limits, package permissions, schedules, queues, leases, routing, and session lifecycle are present, but these do not establish S2 on topology/infrastructure alone.
- Closure path: no complete first-party path from a disturbance among distinct autonomous Blackbox S1 units through attenuation back into subsequent S1 behaviour was found.
- Why this is / is not agent-owned: because the function itself is not established, autonomy is not graded.
- Evidence: [`src/blackbox/workspace_agents/README.md`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/workspace_agents/README.md); [`src/blackbox/workers/README.md`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/workers/README.md); [`src/blackbox/workers/source.py`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/workers/source.py).
- Basis: explicit absence after function-first review.
- Confidence: medium-high.
- Caveats: the queue contract has claim/lease/reclaim vocabulary, but the shipped reference source is explicitly single-process and real multi-node control-plane ownership cannot be borrowed from an external source implementation.

### Absence scope

- Surfaces inspected: local runtime/tool loop, workspace-agent permissions/scheduler, environment workers/work source, agent session lifecycle and workspace abstractions.
- Plausible first-party paths checked: tool concurrency, session plurality, schedule execution, package permission isolation, work-item claim/lease/reclaim, provider fallback and workspace separation.
- Why no material first-party path remains: these mechanisms gate, route, schedule, isolate, or supervise execution but do not close a qualifying first-party relation for a demonstrated disturbance among distinct autonomous Blackbox S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no qualifying first-party whole-system inside-and-now control function is established.
- Disturbance / variety regulated: no whole-organization current-control disturbance is closed by a first-party S3 owner.
- Decisive decision or feedback right: lifecycle APIs expose start/stream/follow-up/approve/cancel operations, but the substantive current-control choice remains with the caller/application or external provider-managed agent.
- Decision owner: none identified as a first-party autonomous S3 actor.
- Supporting / enforcement mechanisms: `AgentProvider` session lifecycle, status/events, cancellation, approval routing, scheduler and worker status exist as control infrastructure.
- Closure path: no first-party autonomous path was found from a whole-system current view through commitment/intervention choice back into multiple current S1 operations.
- Why this is / is not agent-owned: lifecycle mechanisms are caller-controlled interfaces rather than evidence of an autonomous manager making current portfolio decisions.
- Evidence: [`docs/AGENT.md`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/docs/AGENT.md); [`src/blackbox/workspace_agents/executor.py`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/workspace_agents/executor.py).
- Basis: explicit absence after ownership review.
- Confidence: high.
- Caveats: “supervises agent sessions” in the API sense is not treated as VSM S3 without an owning current-control actor and whole-system closure.

### Absence scope

- Surfaces inspected: AgentProvider lifecycle, durable session state, schedule executor, environment-worker status/control, runtime orchestration facade.
- Plausible first-party paths checked: cancel/follow-up/approval, session status/events, deterministic schedules, worker stop, provider fallback and persisted session resume.
- Why no material first-party path remains: these paths expose control to callers or deterministically execute configured policy; none establishes first-party autonomous whole-system current-control discretion.

## S3* — Audit / monitoring

- State: —
- Function: no qualifying independent corrective audit function is established.
- Disturbance / variety regulated: traces/evaluations can identify run quality issues, but no first-party audit-to-correction loop is closed.
- Decisive decision or feedback right: `evaluate_trace` invokes caller-supplied evaluators and returns reports/events; it does not decide corrective operational intervention.
- Decision owner: none identified for a first-party S3* function.
- Supporting / enforcement mechanisms: traces, replay, evaluator protocol, evaluation lifecycle events, output validation, approvals and typed artifacts.
- Closure path: trace → supplied evaluator → report exists, but the repository does not close report → independent corrective decision → changed current operation.
- Why this is / is not agent-owned: evaluation is an analysis utility at this boundary rather than an independent auditing organ with corrective return.
- Evidence: [`src/blackbox/observability/evals.py`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/observability/evals.py).
- Basis: explicit + structural absence of corrective closure.
- Confidence: high.
- Caveats: output schema validation and approval gates are not substituted for an independent audit function.

### Absence scope

- Surfaces inspected: trace/eval utilities, output validation, approvals/policy, events/artifacts and session result collection.
- Plausible first-party paths checked: evaluator reports, guardrail/eval event names, structured-output validation, policy denial and approval flows.
- Why no material first-party path remains: none provides both an independent evidence path and a first-party corrective feedback return into current operational control.

## S4 — Intelligence / adaptation

- State: —
- Function: no qualifying first-party prospective adaptation/intelligence function is established.
- Disturbance / variety regulated: no environment-facing future-capability disturbance is shown to drive a first-party adaptation decision.
- Decisive decision or feedback right: no first-party actor is shown selecting durable capability changes from evidence for later runs.
- Decision owner: none identified for S4.
- Supporting / enforcement mechanisms: persisted sessions/provider state, skills/packages, registries, dynamic tool selection and replay are available, but persistence/configuration reuse is not adaptation by itself.
- Closure path: no first-party path from external/future evidence through candidate capability change and evaluation back into adopted later operating capability was found.
- Why this is / is not agent-owned: state reuse and caller-managed package/spec changes do not demonstrate a self-owned prospective adaptation loop.
- Evidence: [`README.md`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/README.md); [`src/blackbox/workspace_agents/README.md`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/workspace_agents/README.md).
- Basis: explicit absence after adaptation review.
- Confidence: high.
- Caveats: dynamic tool discovery changes a current run's visible tool surface and does not by itself establish future-oriented S4 adaptation.

### Absence scope

- Surfaces inspected: dynamic tools, skills/packages, registries, session persistence/replay, evaluations and schedule/package execution.
- Plausible first-party paths checked: persisted provider state, package versioning, dynamic tool loading, skills, eval reports and reusable workspace-agent specs.
- Why no material first-party path remains: retained/configured state is application-authored or current-run state; no evidence-driven first-party future capability selection/adoption loop is closed.

## S5 — Identity / ultimate policy

- State: —
- Function: no qualifying identity / ultimate-policy function is established.
- Disturbance / variety regulated: no identity-level constitutional disturbance is established.
- Decisive decision or feedback right: policy/permission configuration and approvals constrain execution but do not establish ultimate organizational identity authority.
- Decision owner: none identified for S5.
- Supporting / enforcement mechanisms: policies, approvals, permission snapshots, package manifests, connectors and configuration constraints.
- Closure path: no path from an identity/constitutional issue through ultimate authority back into subsequent operating identity/policy was found.
- Why this is / is not agent-owned: because no S5 function is established, autonomy is not graded.
- Evidence: [`src/blackbox/workspace_agents/README.md`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/workspace_agents/README.md); [`src/blackbox/runtime/agent_loop.py`](https://github.com/tyxter-dev/blackbox/blob/d5be68e03ca7750920569578710a2ee25d25530c/src/blackbox/runtime/agent_loop.py).
- Basis: explicit absence after boundary review.
- Confidence: high.
- Caveats: generic policy and approval infrastructure is not promoted to S5 without an identity/ultimate-policy issue and legitimate ultimate authority.

### Absence scope

- Surfaces inspected: package permissions, runtime policy/approval paths, agent/package specs, scheduler, session lifecycle and repository governance boundary.
- Plausible first-party paths checked: permission modes, connector grants, approvals, package publication/versioning and agent instructions/configuration.
- Why no material first-party path remains: these are operational constraints/configuration surfaces and do not constitute an identity-level ultimate-policy loop.

## Recursion

Blackbox can run or supervise many sessions/packages, but the frozen first-party boundary does not establish a recursive autonomous organization above the local model/tool S1. Provider-managed agents retain their own external cognition; configured workspace-agent packages are execution descriptions, not automatically higher-level VSM organs.

## Variety and escalation

Policy checkpoints, approvals, permission snapshots, tool budgets, cancellation, provider fallback, schedules, session persistence and queue status constrain operational variety. They are treated as supporting mechanisms rather than independent VSM organs unless the function-specific ownership and closure requirements are met.

## Evidence gaps / terminal outcome

Proposed vector: `S1=A / S2=— / S3=— / S3*=— / S4=— / S5=—`.

The decisive positive path is the first-party local `AgentLoop`, which closes model-selected tool use back into later model decisions. Higher-function candidates remain infrastructure or externally owned composition boundaries at this frozen revision: provider-managed agent cognition is outside Blackbox, scheduler/lifecycle choices are caller-controlled or deterministic, real multi-node lease ownership lives in the substituted work source/control plane, evaluator reports lack corrective return, and no prospective adaptation or identity loop is established.
