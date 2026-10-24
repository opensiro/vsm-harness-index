---
harness_id: agent-runtime-mattbusel
project_name: agent-runtime
repository: https://github.com/Mattbusel/agent-runtime
review_ref: c398a209d0e503c4d47ce6e27888e13e83790ed1
reviewed_at: 2026-10-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-01
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# agent-runtime

## Review boundary

- System in focus: one first-party `llm-agent-runtime` deployment at pinned revision `c398a209d0e503c4d47ce6e27888e13e83790ed1`, including the shipped single-agent runtime, team orchestration, inter-agent coordination primitives, supervisor paths, shadow-traffic comparison, memory/world-model/planning support, policy enforcement, checkpoints, tools and public runtime modules.
- Purpose and identity: provide a batteries-included Rust runtime that turns user objectives into autonomous LLM-agent execution while exposing optional first-party multi-agent, supervision, coordination, observability and resilience constructors.
- Relevant environment: users/operators, caller-supplied LLM inference/providers, tools and external systems, host resources, peer agents, persisted/checkpointed state and configured runtime policies.
- Standard-distribution boundary: the public Rust crate and its documented first-party modules reachable through ordinary library use. External LLM/provider internals, externally supplied tool implementations, downstream application code and repository-development CI are separate systems.
- Credited operating / distribution surfaces: `AgentRuntime::run_agent`; `TeamOrchestrator`; public `negotiation`, `agent_supervisor`/`supervisor`, and `shadow_traffic` modules; supporting runtime/tool/memory/planning/policy modules intentionally exported by the crate.
- Adjacent first-party surfaces excluded from ownership: examples and tests as execution evidence in their own right, benchmark code, CI/release machinery, and any downstream application that could compose the exposed primitives into a stronger organization.
- First-party operating / deployment modes considered: single-agent ReAct execution, multi-agent team execution, resource-negotiation construction, supervised multi-agent/task operation, shadow comparison, reflection/world-state use, and RBAC/policy enforcement.
- Recursion level: one deployed runtime organization. Individual autonomous `run_agent`/team-member executions are S1 operational units when composed together; higher-system functions are credited only where the crate exposes a function-specific path over those units.
- Reviewed revision: `c398a209d0e503c4d47ce6e27888e13e83790ed1`.
- Observation date: 2026-10-01.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The crate centers on `AgentRuntime`, which wires an `AgentConfig` and a ReAct loop into `run_agent`; callers supply inference, while the first-party runtime owns the iterative thought/action/tool-observation organization, session state and deterministic execution envelope. The same distribution exposes `TeamOrchestrator` with Star/Mesh/Ring message topology plus Majority/Pipeline/Parallel result composition.

Several public modules go beyond generic orchestration. `negotiation` models explicit competing agent resource requests and resolves them with Greedy, FairShare, PriorityBased or Vickrey-style allocation. `agent_supervisor` tracks a group of agent lifecycle states and returns restart/escalation decisions, while the Erlang-style `supervisor` path can actually spawn, monitor and restart child tasks according to OneForOne/OneForAll/RestForOne strategy. `shadow_traffic` defines a distinct shadow-agent comparison path, paired production/shadow response records and divergence reports.

Other substantial modules do not by themselves close higher VSM functions. `reflection` scores and retries current reasoning; `world_model` stores present/historical beliefs and computes goal-state differences for planning; `policy` enforces preconfigured RBAC-style allow/deny rules. Those mechanisms were inspected for S4/S5 but do not establish prospective adaptation or runtime identity/ultimate-policy closure at the reviewed boundary.

Primary evidence:

- [`README.md`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/README.md) — documented runtime architecture, single-agent loop, multi-agent teams and public feature surface.
- [`src/runtime.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/runtime.rs) — `AgentRuntime` and first-party ReAct execution/session organization.
- [`src/team.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/team.rs) — multi-agent team topology and consensus execution.
- [`src/negotiation.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/negotiation.rs) — function-specific inter-agent resource-conflict attenuation constructor.
- [`src/agent_supervisor.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/agent_supervisor.rs) and [`src/supervisor.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/supervisor.rs) — current multi-agent/task supervision, restart and escalation paths.
- [`src/shadow_traffic.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/shadow_traffic.rs) — complementary shadow-response comparison and divergence reporting constructor.
- [`src/reflection.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/reflection.rs), [`src/world_model.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/world_model.rs), and [`src/policy.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/policy.rs) — inspected for possible S4/S5 evidence.

## Operational model

A standard single-agent run is an autonomous semantic loop hosted by deterministic Rust machinery: a caller supplies the inference actor, the runtime repeatedly obtains reasoning/action output, executes or routes supported actions, records observations/state and continues until a final answer or bounded termination. Multi-agent operation is separately available through team composition. Higher-system constructor modules can regulate resource contention, supervise current agent/task state, and compare production behavior with a shadow path, but their decisive autonomous authority or final return closure is not wired into one mandatory default control plane; those functions therefore classify as `C` rather than `A`.

## S1 — Operations

- State: A
- Function: transform a task objective into an answer or tool-mediated result through repeated model reasoning/action and returned observation feedback.
- Disturbance / variety regulated: task ambiguity, changing conversational/session state, tool availability/results/failures, memory/graph context and bounded runtime failures.
- Decisive decision or feedback right: choose the substantive next reasoning/action or final answer from current task state and returned observations.
- Decision owner: the autonomous inference actor supplied to the first-party `AgentRuntime` loop.
- Supporting / enforcement mechanisms: `AgentRuntime`, `ReActLoop`, tool registry/execution, session records, checkpoints, memory/graph context, time/iteration limits and error handling.
- Closure path: task + current context → inference actor selects next action → first-party runtime applies/records action and observation → observation enters subsequent step context → actor revises behavior or terminates with a final answer.
- Boundary reachability: `run_agent` is the documented standard crate path; a configured inference/provider is an external dependency, not a downstream replacement for the first-party loop organization.
- Why this is / is not agent-owned: removing the inference actor leaves deterministic runtime machinery but removes the semantic next-action choice; the same organizational decision does not continue autonomously.
- Evidence: [`src/runtime.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/runtime.rs); [`README.md`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: LLM inference itself is caller-supplied, but the reviewed crate supplies the executable ReAct control/feedback organization and applies the actor's choices.

## S2 — Coordination

- State: C
- Function: attenuate resource-allocation conflict among distinct agent operational units through an explicit first-party negotiation path.
- Disturbance / variety regulated: multiple agents submit competing token/compute/memory requests and priorities/deadlines/bids that cannot all be treated as unconstrained independent claims.
- Decisive decision or feedback right: select or scale an allocation outcome under Greedy, FairShare, PriorityBased or AuctionBased strategy and expose the result to subsequent agent execution.
- Decision owner: no autonomous owner is closed by the crate; the allocation rule is deterministic and the downstream developer composes the authority/actor and consumption path.
- Supporting / enforcement mechanisms: `NegotiationProposal`, `ResourceRequest`, `NegotiationRound`, `NegotiationStrategy`, `NegotiationResult` and fairness/allocation calculations.
- Closure path: distinct agent proposals → explicit shared-resource conflict → negotiation strategy attenuates contention → `NegotiationResult` identifies winner/allocation → caller can alter subsequent S1 resource availability/behavior. The final application/authority step requires composition.
- Boundary reachability: `negotiation` is an intentionally public first-party module in the standard crate distribution.
- Distinct S1 units: proposal identities are explicitly agent IDs and the same distribution exposes executable single-agent/team runtime units.
- Inter-S1 disturbance: competing resource claims over tokens, compute units and memory.
- Attenuating coordination relation: deterministic allocation/selection under one of four dedicated negotiation strategies.
- Feedback into subsequent S1 behaviour: the function-specific `NegotiationResult` is returned for enforcement/consumption by the composing runtime; that last closure is not automatically wired.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited primitive is not the generic bus/team topology; it explicitly models competing agent claims and resolves the identified contention.
- Why this is / is not agent-owned: no autonomous agent selects the coordination judgment in the standard constructor; composing such an actor/authority is left to the developer, so this is `C`, not `A`.
- Evidence: [`src/negotiation.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/negotiation.rs); [`src/lib.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/lib.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: `TeamOrchestrator` consensus/routing alone would not satisfy the S2 constructor threshold; the positive classification depends on the dedicated negotiation resource-conflict path.

## S3 — Inside-and-now control

- State: C
- Function: supervise the current operating set of agents/tasks and intervene through restart, group restart, stopping or escalation when failures exceed configured tolerances.
- Disturbance / variety regulated: current agent failures, crash loops, group dependency effects and loss of a currently running operational unit.
- Decisive decision or feedback right: determine which current agents/tasks restart under OneForOne/OneForAll/RestForOne and when repeated failure escalates instead of restarting.
- Decision owner: deterministic first-party supervisor policy; an autonomous organizational decision owner is not supplied by the standard constructor.
- Supporting / enforcement mechanisms: `AgentSupervisor` lifecycle map/restart windows, `Supervisor` child-task monitor, restart strategies, rate limits, lifecycle states and statistics.
- Closure path: current agent/task state → failure observed → supervisor evaluates configured strategy/rate window → restart/stop/escalate decision → first-party supervisor state and, in the executable supervisor path, child execution are changed. Autonomous discretion/authority remains to be composed.
- Boundary reachability: both supervisor surfaces are shipped public first-party modules rather than examples-only code.
- Whole-system current view: `AgentSupervisor` holds the supervised agent set and exposes running/failed state; `Supervisor` maintains the current child set and aggregate restart statistics.
- Current-control decision scope: current intervention over which operational units continue/restart together and when a failure is escalated.
- Why this is / is not agent-owned: the decisive strategy is preconfigured and deterministically enforced; removing any autonomous actor leaves materially the same restart judgment, so `A` is not supported. The first-party S3-specific construction path supports `C`.
- Evidence: [`src/agent_supervisor.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/agent_supervisor.rs); [`src/supervisor.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/supervisor.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: generic resource budgets and local retry logic were not used as S3 evidence; the positive classification rests on the group supervisory current-control path.

## S3* — Complementary audit

- State: C
- Function: compare ordinary production-agent output against a separate shadow-agent response path and derive divergence evidence without affecting the production response.
- Disturbance / variety regulated: undetected production-response divergence or behavioral regression that ordinary production output alone would not reveal.
- Decisive decision or feedback right: decide which requests enter the shadow path, pair ordinary/shadow responses, compute divergence and aggregate a shadow report that can trigger later control action.
- Decision owner: the first-party manager deterministically computes sampling/comparison; the autonomous auditor, strength of independence and action-on-finding authority require composition.
- Supporting / enforcement mechanisms: `ShadowConfig`, deterministic request sampling, distinct `shadow_agent_id`, paired `ShadowRecord`, normalized divergence scoring and `ShadowReport` aggregation.
- Closure path: ordinary production response + separately obtained shadow response → paired comparison → divergence/audit report → downstream controller can act on the finding. Supplying/running the independent shadow actor and closing findings back into control are composition responsibilities.
- Boundary reachability: `shadow_traffic` is an intentionally public first-party constructor in the shipped crate.
- Claim being audited: behavioral adequacy/consistency of the production agent response for the same request.
- Ordinary reporting path: production agent response.
- Complementary access path: separately identified shadow agent receives/replays sampled requests and its response is compared with production.
- Independence boundary: the constructor explicitly separates production and `shadow_agent_id`, but actual model/runtime/credential independence is selected by the composing deployment rather than guaranteed internally.
- Who acts on findings: not fixed by the crate; a downstream controller/operator/agent must consume `ShadowReport`, so ownership/closure remains constructor-level.
- Why this is / is not agent-owned: the crate provides an S3*-specific audit path but no standard autonomous actor owns the audit judgment-and-return loop; classification is `C`.
- Evidence: [`src/shadow_traffic.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/shadow_traffic.rs); [`src/lib.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/lib.rs).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: merely enabling shadow collection is not a closed autonomous S3* loop; concrete complementary independence and corrective return must be composed by the deployment.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established at the reviewed deployment boundary.
- Disturbance / variety regulated: current observations, historical beliefs, self-reflection scores and memory can change immediate or later task context, but no distinct future-facing adaptation-option loop is closed.
- Decisive decision or feedback right: no first-party path develops prospective environmental adaptation options and returns an adaptation judgment into present capability/S3.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: `WorldState`, temporal belief history, planning helpers, memory/consolidation, reflection/retry and shadow reports.
- Closure path: not applicable; reviewed mechanisms update current/historical context or task-local quality, not external distinction → future/prospective model → adaptation option → present-capability change.
- Boundary reachability: the inspected modules are public/reachable, but the S4 organizational function is not established.
- External distinction: tool/observation-derived world facts and shadow comparisons can represent external evidence.
- Future / prospective distinction: no separate future-oriented environmental distinction, forecast or prospective opportunity/threat model was found.
- Adaptation option generated: no qualifying first-party capability-adaptation option path was found.
- Path back into current capability / S3: current world facts can feed planning and reflection can cause a retry, but neither is a prospective capability-adaptation return loop.
- Why this is / is not agent-owned: function absent; task reflection and memory/world-state updates do not become S4 merely because an LLM may participate.
- Evidence: [`src/reflection.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/reflection.rs); [`src/world_model.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/world_model.rs); [`src/shadow_traffic.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/shadow_traffic.rs).
- Basis: structural absence review
- Confidence: high
- Caveats: downstream applications could use world history/shadow reports to construct S4, but that capability is not supplied as a first-party S4 loop here.

### Absence scope

- Surfaces inspected: reflection, world model/temporal beliefs, memory/consolidation surfaces, planner integration, shadow reports, runtime loop and public module exports.
- Plausible first-party paths checked: self-reflection-driven retry, observation/history-driven planning, persistent memory reuse and shadow-divergence analysis.
- Why no material first-party path remains: each reviewed mechanism regulates present-task execution, stores/reuses evidence or reports retrospective/current divergence; none establishes the required external-and-prospective distinction plus generated adaptation option and return into current capability.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy closure is established.
- Disturbance / variety regulated: RBAC allow/deny rules, principals, roles, rate limits and configuration constrain actions, but they do not adjudicate identity-level or ultimate-policy questions.
- Decisive decision or feedback right: no runtime path receives an identity/ultimate-policy issue, reaches a legitimate ultimate authority, and returns a newly authoritative policy decision into operation.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: `PolicyStore`, roles/permissions, allow/deny rules, conditions, rate limits and other static runtime configuration.
- Closure path: not applicable; loading/evaluating preconfigured authorization rules is enforcement of prior policy rather than an identity/ultimate-policy decision-and-return loop.
- Boundary reachability: policy enforcement is reachable, but the S5 organizational function is absent.
- Identity / ultimate-policy issue: none shown as an operating decision object.
- Ultimate authority in each claimed mode: no positive mode claimed.
- Return-to-operation path: static rules affect authorization, but no qualifying new ultimate-policy decision is produced through an authority path.
- Why this is / is not agent-owned: the deterministic policy engine enforces supplied rules; it does not own or regenerate the system's identity/ultimate policy.
- Evidence: [`src/policy.rs`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/src/policy.rs); [`README.md`](https://github.com/Mattbusel/agent-runtime/blob/c398a209d0e503c4d47ce6e27888e13e83790ed1/README.md).
- Basis: structural absence review
- Confidence: high
- Caveats: operators can configure policies externally, but generic configuration authority is not a parent S5 mode without a reconstructable identity/ultimate-policy closure.

### Absence scope

- Surfaces inspected: RBAC/policy engine, principal/role definitions, runtime configuration, supervisor escalation, team leadership and documented public feature surface.
- Plausible first-party paths checked: policy-rule changes, leader/supervisor authority, escalation and configuration selection.
- Why no material first-party path remains: reviewed mechanisms enforce operational constraints or current-control decisions; none establishes an identity/ultimate-policy issue, legitimate ultimate authority decision and authoritative return loop.

## Distributed OSS parent arrangement

Repository maintainers govern development of the library, but that development organization is outside the shipped runtime boundary and is not used to infer parent-governed S3/S4/S5 modes.

## Self-hosted and non-human modes

The crate is self-hostable and intentionally constructor-heavy. This is reflected by `C` where a VSM-specific first-party path exists but an autonomous actor, independence boundary, authority or final closure must still be assembled by the deployment. Ordinary operator configuration is not promoted to parent-mode notation.

## Recursion

One `run_agent` execution is a viable S1 operational unit. Team members or separately registered supervised agents become multiple S1 units when composed within one runtime organization. The positive S2/S3/S3* classifications rely on dedicated constructors that explicitly operate across or alongside those units, not on plurality alone.

## Variety and escalation

The agent loop absorbs semantic task variety through model reasoning and tool feedback. Negotiation attenuates explicit inter-agent resource contention. Supervision attenuates current failure/crash-loop variety through restart strategies and escalation. Shadow comparison adds a complementary evidence channel for behavioral divergence. None of those constructors establishes prospective S4 adaptation or ultimate-policy S5 closure by itself.

## Evidence gaps

No unresolved evidence gap requires `?` for the published vector. The main reassessment triggers would be a standard first-party autonomous controller that owns the S2/S3/S3* constructor decisions, a prospective environment-to-capability adaptation loop, or a runtime identity/ultimate-policy authority loop.