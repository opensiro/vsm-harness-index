---
harness_id: opensquilla
project_name: OpenSquilla
repository: https://github.com/TokenRhythm/opensquilla
review_ref: 71888b1fab67010770684ced0beffc4e91677cde
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenSquilla

## Review boundary

- System in focus: the installed OpenSquilla conversational agent and its first-party turn execution, tool-call, memory, model-routing and optional subagent runtime, not the ecosystem of provider models, remote tools or separately operated agents.
- Purpose and identity: execute user-directed tasks through a model-led conversational tool loop across documented CLI, Web and channel front ends.
- Relevant environment: user tasks, tool observations, filesystem/service state, model responses and failures, context budgets and active policy/permissions.
- Standard-distribution boundary: shipped Python `opensquilla.engine.Agent` / `TurnRunner` turn execution and registered built-in tools, optionally enabled subagents, routing and goal controls.
- Credited operating / distribution surfaces: [`engine/agent.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/engine/agent.py), [`engine/runtime.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/engine/runtime.py), [`engine/subagent.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/engine/subagent.py), [`tools/builtin/agents.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/tools/builtin/agents.py), [`tools/builtin/goal_control.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/tools/builtin/goal_control.py), and router/sandbox policy modules.
- Adjacent first-party surfaces excluded from ownership: GitHub CI, release and fault-injection workflows, tests, example skills, contributors and maintainers, benchmark/live evaluation jobs and operational telemetry infrastructure; external LLM providers, sandbox hosts and downstream agents are not independent first-party VSM authorities.
- First-party operating / deployment modes considered: local/server turn execution, tool-enabled mode, model-routing mode and explicitly enabled parent/child subagent mode; permissions and self-hosted configuration affect which capabilities can be invoked.
- Recursion level: one user/session-scoped harness; optional children are task-execution cells, without a demonstrated independent metasystem for each child.
- Reviewed revision: `71888b1fab67010770684ced0beffc4e91677cde`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The `Agent` and shared turn runner consume task/context and model responses, offer registered tools, dispatch model-selected calls, append results/history and continue until a terminal answer or execution stop. Session and history/compaction machinery provides context continuity. `SubagentManager` creates independent child agent instances, streams child events, enforces configured depth/concurrency/timeouts and records terminal outcomes. An optional built-in `subagents` tool exposes a session-scoped child list and `steer`/`kill` actions, but defaults to denied access. `goal_control` persists user-authorized objectives/progress and status; its policy explicitly reserves task/objective changes and pauses to user authority. `squilla_router` classifies requests and adjusts model tiers under operator-configured rollout, while `router_control` can set session-bound model holds. Sandbox, permission, telemetry and policy engines gate requests or retain observations. None is by itself a demonstrated independent VSM audit or ultimate-policy authority.

## Operational model

The model-backed agent selects content, tool calls and delegated task objectives; Python executes/enforces tool constraints and returns observations for the next model decision. Child execution is real and concurrent, but a task pool or scheduler alone does not demonstrate inter-S1 oscillation attenuation. Router tiers and context budgets are adaptive operational routing under preselected policies, not automatically prospective strategic intelligence. A parent agent may supervise its own children if relevant tools are enabled, but the evidence reviewed does not yet settle the required whole-system S3 current-control witness across a supported session mode.

## S1 — Operations

- State: A
- Function: transform varied user tasks into observable tool-mediated actions and conversational results.
- Disturbance / variety regulated: different task demands, changing tool outputs, model errors, filesystem/web state and context pressure.
- Decisive decision or feedback right: model chooses next response and tool invocation after seeing returned tool observations; the engine continues the turn loop.
- Decision owner: first-party configured model-backed `Agent` in a standard supported execution mode; external provider supplies computation but does not own the harness's task boundary.
- Supporting / enforcement mechanisms: `TurnRunner`, tool dispatcher, history/compaction, provider selection, tool policy, model and subagent budgets.
- Closure path: task and context → model action/tool decision → authorized dispatch → observation recorded → next model decision or final response.
- Boundary reachability: shipped `Agent.run_turn`/shared runtime executes the loop and registers built-in tools; no dev-only evaluator is needed for the ordinary task cycle.
- Why this is / is not agent-owned: agent model chooses semantic task/action content; deterministic runtime admits, executes and bounds its choices.
- Evidence: [`engine/agent.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/engine/agent.py), [`engine/runtime.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/engine/runtime.py), [`tools/dispatch.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/tools/dispatch.py).
- Basis: structural.
- Confidence: high for shipped architecture, not task-quality measurements.
- Caveats: exact tool reachability depends on configured permission and provider availability.

## S2 — Coordination

- State: —
- Function: no established dedicated regulation of interference among distinct S1 units at this assessed recursion.
- Disturbance / variety regulated: concurrent child execution and shared-resource hazards exist, but no concrete inter-S1 oscillation or conflicting operational commitments are shown to be corrected by a specific first-party coordination feedback relation.
- Decisive decision or feedback right: `SubagentManager` imposes maximum concurrent children and depth and records completion; `subagents` can list/steer/kill children. These are scheduling and intervention tools rather than an evidenced S2-specific reconciliation judgment.
- Decision owner: external operator sets limits; model can choose child tasks, subject to runtime enforcement.
- Supporting / enforcement mechanisms: `SubagentRegistry`, asyncio tasks, status records, timeout/cancel, per-session origin checks and permission gating.
- Closure path: child results return to its caller, but an independently identifiable interference → coordination → changed subsequent S1 operation path was not located.
- Why this is / is not agent-owned: parallel agency and a supervising tool are not themselves the Profile S2 function.
- Evidence: [`engine/subagent.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/engine/subagent.py), [`tools/builtin/agents.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/tools/builtin/agents.py), [`telemetry/coordination.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/telemetry/coordination.py).
- Basis: structural.
- Confidence: medium for bounded shipped modes.
- Caveats: applications built on the tools may add S2, but that cannot be borrowed by the standard harness.

### Absence scope

- Surfaces inspected: parent/child runtime manager, child listing/steering/kill tool, task timeout and concurrency checks, telemetry consent coordination, session/routing machinery.
- Plausible first-party paths checked: shared concurrency cap, cancel/steer, child completion reporting and telemetry `ScopeConsentCoordinator` locking.
- Why no material first-party path remains: each path is generic task/lifecycle control or serialized consent bookkeeping, without a shipped function-specific feedback that attenuates demonstrated interference among distinct operational S1 cells.

## S3 — Inside-and-now control

- State: ?
- Function: potential present control over a parent agent's active children and persistent goals, but the exact whole-system view and accountability boundary remain unresolved.
- Disturbance / variety regulated: child progress/failure, concurrent task pressure, goal status and session limits.
- Decisive decision or feedback right: optional agent-accessible `subagents.list`, `.kill` and `.steer` can redirect active child work; `goal_control` can update progress, but status transitions are constrained by user authority.
- Decision owner: potentially the parent agent when permissions expose tools; user owns objective and several status rights, runtime enforces the policies.
- Supporting / enforcement mechanisms: session list, task runtime `send`/`cancel`, `GoalService`, status records and stored configured budgets.
- Closure path: steering commands can reach child sessions and affect their next input; it is not yet established that a whole-of-system current view drives a shared resource/commitment decision in a supported standard mode.
- Why this is / is not agent-owned: agent can choose an intervention once allowed, but tool affordances alone do not prove a metasystem-wide S3 function; ordinary goal tracking and termination are insufficient.
- Evidence: [`tools/builtin/agents.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/tools/builtin/agents.py), [`tools/builtin/goal_control.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/tools/builtin/goal_control.py), [`engine/subagent.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/engine/subagent.py).
- Basis: structural for tools, unknown for whole-system S3 control.
- Confidence: low for S3 ownership.
- Caveats: resolve whether the permitted operating mode provides a real whole-of-parent work view and integrated current-control decisions, not merely optional agent intervention endpoints.

## S3* — Complementary audit

- State: —
- Function: no independent complementary direct-access audit of operating claims identified in the shipped agent run.
- Disturbance / variety regulated: tool failures and unsafe operations are handled by ordinary policy checks and logs; they do not automatically constitute complementary audit.
- Decisive decision or feedback right: middleware, tool guards, runtime events, telemetry and tests validate/enforce or observe the same operating stream rather than an independently owned corrective inspection channel.
- Decision owner: runtime guardrails, developer/operator config and CI testers; no independent audited judgment/return owner at the assessed boundary.
- Supporting / enforcement mechanisms: sandbox approval, tool policy, runtime event logging, diagnostics, fault-injection tests.
- Closure path: guard denials feed the ordinary task loop; no separate audit-to-S3 corrective feedback is evidenced.
- Why this is / is not agent-owned: a model checking its own tool result is ordinary operation, not necessarily independent S3* inspection.
- Evidence: [`sandbox/approval_runtime.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/sandbox/approval_runtime.py), [`tools/policy_runtime.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/tools/policy_runtime.py), [`engine/runtime_events.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/engine/runtime_events.py).
- Basis: structural.
- Confidence: medium.
- Caveats: an operator might provide external auditing; it is not part of the credited first-party assessment boundary.

### Absence scope

- Surfaces inspected: tool/sandbox policy, event logging, diagnostics, telemetry, repository CI/testing and parent-child status paths.
- Plausible first-party paths checked: approvals, logs, test/fault injection, tool guard evaluation and child observation.
- Why no material first-party path remains: no independently provisioned inspection of actual task reality with audit judgment returned to whole-system control is wired into the supported run; test/CI is adjacent rather than runtime S3*.

## S4 — Outside-and-then intelligence

- State: —
- Function: no evidenced prospectively oriented environment-sensing, alternative-strategy choice and feedback into current organizational capability.
- Disturbance / variety regulated: variation in per-request complexity, provider health and context pressure drives present-turn routing, not a prospective outside-and-then strategy cycle.
- Decisive decision or feedback right: Squilla router chooses tier/response-mode under operator rollout and capability policy; optional model hold changes later turns within a session.
- Decision owner: configured router model/policy for task-level routing and user/operator for available tiers; no identified separate S4 adaptation authority.
- Supporting / enforcement mechanisms: `RoutingPolicyEngine`, calibration store, model capability catalog, `RouterControlHoldStore`, snapshots and budget gates.
- Closure path: routing decisions affect next request/turn, but there is no evidenced future environmental distinction → strategic option → capability change through S3 return.
- Why this is / is not agent-owned: model-driven tier selection and dynamic tool/skill use are operational optimization; neither alone satisfies prospective S4.
- Evidence: [`engine/steps/squilla_router.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/engine/steps/squilla_router.py), [`router_control.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/router_control.py), [`tools/builtin/router_control.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/tools/builtin/router_control.py).
- Basis: structural.
- Confidence: medium.
- Caveats: source has substantial model-routing feedback; a strategic adaptation extension could alter this judgment if supplied in the first-party supported mode.

### Absence scope

- Surfaces inspected: routing/controller code, calibration/hold storage, goal update, memory/history compaction, scheduler and agent run entry points.
- Plausible first-party paths checked: dynamic provider tiers, router calibration, learned conversation memory, skill availability, long-lived goal progress.
- Why no material first-party path remains: shipped paths adapt execution within predefined goals and provider choices, not external future opportunities/threats and prospective organizational capability.

## S5 — Policy and identity

- State: —
- Function: no installed internal or parent-governed ultimate-policy/identity decision-and-return cycle at the declared agent/session recursion.
- Disturbance / variety regulated: tool permissions, budget, routing overrides and user tasks are bounded by settings; they are not a system identity conflict.
- Decisive decision or feedback right: users/operators set runtime constraints and grant approvals; `goal_control` expressly reserves objective/status changes to the user in critical cases.
- Decision owner: human user/operator for configuration and objectives, without a first-party legitimate identity-level issue/ratification loop.
- Supporting / enforcement mechanisms: config/policy files, permission validators, sandbox and goal service state.
- Closure path: ordinary tool approval/denial changes execution; no policy-level issue reaches ultimate authority and returns as a governing identity decision.
- Why this is / is not agent-owned: tool safety and prompt-level instructions enforce existing policy; neither grants the model an ultimate-policy constitutional right nor builds a parent S5 closure.
- Evidence: [`tools/builtin/goal_control.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/tools/builtin/goal_control.py), [`sandbox/policy_store.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/sandbox/policy_store.py), [`tools/policy_runtime.py`](https://github.com/TokenRhythm/opensquilla/blob/71888b1fab67010770684ced0beffc4e91677cde/src/opensquilla/tools/policy_runtime.py).
- Basis: structural.
- Confidence: medium.
- Caveats: project maintainer governance and end-user choice remain outside this app's run-level identity-governing circuit.

### Absence scope

- Surfaces inspected: user-goal constraints, policy/permissions, sandbox, router control, runtime modes, repository maintainer and CI surfaces.
- Plausible first-party paths checked: human approval, permission override, goal amendments, operator routing holds and repository governance.
- Why no material first-party path remains: all paths change task scope or enforce predefined permissions; no shipped system identity question, legitimate ultimate adjudication and authoritative return governing later operation are connected.

## Distributed OSS parent arrangement

OpenSquilla is publicly developed, but no per-session running agent is shown to send an identity-level question through the maintainer governance system and receive binding first-party policy closure. Separate contributor-local agents are not a shared VSM parent organization.

## Self-hosted and non-human modes

Self-hosted users select model providers, consent and sandbox/tool policies. The standard model-backed loop may operate without a contemporaneous human decision for each turn. Optional parent/child tools and permissions change reachable control surfaces; this review does not silently promote user approvals to S3/S4/S5 parent ownership.

## Recursion

Spawn depth, session lineage and child task count encode execution topology, not evidenced independent nested VSM viability. A parent can steer children when explicitly permitted, but the child does not have an independently proved S3–S5 metasystem.

## Variety and escalation

Provider routing, tool failure feedback, run budgets, stop checks, memory compaction and optional child steering attenuate operational variety. Permission rejections and terminal child-status notices return into task operation; their presence alone does not prove an organizational algedonic channel or higher-recursion governance.

## Evidence gaps

- Structural pinned-source review only: no paid provider execution, model quality benchmark or network tool action was performed.
- S3 is explicitly unresolved because the optional child-management and goal tools could support more than a local task if a documented whole-system current view/decision loop is traced; no positive ownership claim is made on tool naming alone.
- Other negative results are bounded to shipped first-party distribution paths inspected at this immutable revision, not claims about external plugins or later versions.
