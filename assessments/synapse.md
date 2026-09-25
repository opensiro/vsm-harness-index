---
harness_id: synapse
project_name: Synapse
repository: https://github.com/nshkrdotcom/synapse
review_ref: bc43df9671b1e4974054e1ce0109f3e37733e9f4
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Synapse

## Review boundary

- System in focus: the first-party Synapse reusable runtime/framework at frozen revision `bc43df9671b1e4974054e1ce0109f3e37733e9f4`, including `Synapse.Runtime`, signal routing/registry, declarative orchestrator runtime, workflow engine, coordination/consensus helpers, first-party action modules and the packaged CodeReview domain.
- Purpose and identity: provide a headless declarative framework for signal-driven workflows, specialist/orchestrator process management, configurable action execution, persistence/telemetry and multi-agent coordination construction.
- Relevant environment: host-supplied orchestration configuration, Jido action modules and callbacks, external LLM providers, application inputs, database persistence, parent pipeline/FlowStone callers and human escalation recipients.
- Standard-distribution boundary: code and configuration actually present in the frozen repository distribution. External model endpoints, downstream application callbacks/agents and missing deployment configuration do not donate autonomous ownership.
- Credited operating / distribution surfaces: `lib/synapse.ex`; `lib/synapse/runtime.ex`; `lib/synapse/orchestrator/**`; `lib/synapse/workflow/**`; signal registry/router; consensus/coordination/escalation helpers; packaged actions including `Synapse.Actions.GenerateCritique`; packaged `Synapse.Domains.CodeReview` actions.
- Adjacent first-party surfaces excluded from ownership: tests, docs/roadmaps/continuation prompts, examples, contributor workflows and hypothetical/downstream FlowStone agents. Documentation claims about `priv/orchestrator_agents.exs` are not credited as a deployment owner because the frozen repository contains no `priv/` directory or that configured file.
- First-party operating / deployment modes considered: application-supervised core runtime; declarative orchestrator runtime with a caller-supplied reachable config source; direct `Synapse.coordinate/3`; direct workflow/action execution; packaged CodeReview signal/action registration.
- Recursion level: one Synapse runtime/framework instance. Downstream systems assembled with independently supplied autonomous agents are separate systems-in-focus.
- Reviewed revision: `bc43df9671b1e4974054e1ce0109f3e37733e9f4`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Synapse ships substantial orchestration machinery but does not, at the frozen standard-distribution boundary, package an autonomous operational decision/action feedback loop. `Synapse.Runtime` supervises the signal router, agent registry and specialist supervisor. `Synapse.Orchestrator.Runtime` loads declarative agent definitions, starts/stops/restarts processes and exposes health/list/add/remove APIs. `DynamicAgent` subscribes to configured signals and executes the configured Jido actions through `RunConfig`; specialist actions, result builders, custom handlers, orchestration classifiers, specialist selection and negotiation callbacks are supplied by configuration.

The repository also exposes `Synapse.coordinate/3` as a multi-agent consensus API. Its production `execute_agent/3` path is a first-party stub returning `%{position: :approve, score: 1.0}` rather than invoking the `agent_runner` shown in the public API example. Consensus/timeout/escalation machinery therefore operates over placeholder or externally supplied test/downstream agent results at this ref; it does not establish autonomous S1 units.

One packaged action, `Synapse.Actions.GenerateCritique`, invokes an external LLM and returns model-generated critique. This is a real model-backed capability, but it is a one-shot action primitive: the first-party runtime does not package it as an autonomous decision/action/observation feedback loop. The CodeReview domain auto-registers signal schemas and provides deterministic classification/security/performance/summary actions, but domain registration does not wire a runnable autonomous agent topology.

The default application configuration enables `Synapse.Orchestrator.Runtime` with `config_source: {:priv, "orchestrator_agents.exs"}`. At the frozen revision, the repository has no `priv/` directory and `priv/orchestrator_agents.exs` is absent. The orchestrator runtime handles configuration-load failure by retaining its prior/empty configuration and therefore has no first-party default autonomous operating units to reconcile. README/docs references to that absent file are not used to close the boundary.

Primary evidence:

- [`lib/synapse.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse.ex) — `coordinate/3`, iterative consensus and production `execute_agent/3` stub.
- [`lib/synapse/runtime.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/runtime.ex) — core router/registry/specialist-supervisor runtime.
- [`lib/synapse/orchestrator/runtime.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/orchestrator/runtime.ex) — declarative topology reconciliation and runtime health/lifecycle APIs.
- [`lib/synapse/orchestrator/dynamic_agent.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/orchestrator/dynamic_agent.ex) — signal-triggered execution of configured actions.
- [`lib/synapse/orchestrator/actions/run_config.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/orchestrator/actions/run_config.ex) — specialist workflows plus downstream classifier/specialist/negotiation callbacks.
- [`lib/synapse/orchestrator/agent_config.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/orchestrator/agent_config.ex) — developer-supplied actions, handlers and orchestration callables.
- [`lib/synapse/actions/generate_critique.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/actions/generate_critique.ex) — one-shot LLM critique action.
- [`lib/synapse/consensus.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/consensus.ex) and [`lib/synapse/coordination_state.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/coordination_state.ex) — deterministic consensus/state helpers.
- [`lib/synapse/domains/code_review.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/domains/code_review.ex) — packaged domain schemas/actions without an autonomous topology.
- [`lib/synapse/domains/code_review/actions/classify_change.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/domains/code_review/actions/classify_change.ex) and [`lib/synapse/domains/code_review/actions/security/check_sql_injection.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/domains/code_review/actions/security/check_sql_injection.ex) — deterministic packaged review decisions inspected for S1/S3*.
- [`config/config.exs`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/config/config.exs) and [`lib/synapse/application/orchestrator.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/application/orchestrator.ex) — enabled default orchestrator points to absent `priv/orchestrator_agents.exs`.

## S1 — Operations

- State: —
- Function: no autonomous operational unit is closed by the frozen standard distribution.
- Disturbance / variety regulated: the framework can transport application/task variety to downstream actions/agents, but no first-party autonomous operating loop is packaged to absorb that variety through repeated decision/action/feedback.
- Decisive decision or feedback right: not established.
- Decision owner: none established at the reviewed boundary; host-supplied actions/callbacks/agents own substantive operation in constructor use.
- Supporting / enforcement mechanisms: signal routing, workflow execution/persistence, declarative process lifecycle, Jido action execution, LLM request adapter, retries/compensation and consensus helpers.
- Closure path: no first-party autonomous decision → environment/action → observation → subsequent autonomous decision loop is reachable in the frozen standard setup.
- Why this is / is not agent-owned: `DynamicAgent` executes configured modules rather than deciding what operation to perform; `coordinate/3` production agent execution is a hard-coded success stub; `GenerateCritique` is a single LLM generation action without a first-party action/observation feedback loop; and the configured default topology file is absent.
- Evidence: [`lib/synapse.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse.ex); [`lib/synapse/orchestrator/dynamic_agent.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/orchestrator/dynamic_agent.ex); [`lib/synapse/actions/generate_critique.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/actions/generate_critique.ex); [`config/config.exs`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/config/config.exs).
- Basis: explicit + structural
- Confidence: high
- Caveats: Synapse intentionally exposes strong construction primitives and downstream applications can wire autonomous actors through them. Under Methodology 0.3.6, generic constructor expressiveness does not substitute for the included-harness requirement that ordinary S1 ownership be autonomously closed.

### Absence scope

- Surfaces inspected: public README/API, core runtime, declarative orchestrator/runtime/config schema, DynamicAgent/RunConfig, direct coordination API, LLM action, CodeReview actions/domain registration, application config and default orchestrator bootstrap.
- Plausible first-party paths checked: default orchestrator topology, `Synapse.coordinate/3`, packaged specialists, LLM-backed critique, custom/declarative agents and CodeReview domain.
- Why no material first-party path remains: every plausible path either terminates in deterministic logic, a placeholder production agent, a one-shot model call, or a developer-supplied action/callback/agent; the nominal default agent topology is not present in the frozen distribution.

## S2 — Coordination

- State: —
- Function: no S2 function is established because the reviewed boundary does not establish multiple autonomous S1 operational units whose concrete interference is regulated.
- Disturbance / variety regulated: no qualifying inter-S1 disturbance at the declared recursion.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: SignalRouter, consensus algorithms, task/result signal roles, specialist selection, optional `negotiate_fn`, dependencies and coordination state.
- Closure path: no established distinct-S1 disturbance → attenuation decision → changed subsequent S1 behavior loop.
- Why this is / is not agent-owned: signal transport and deterministic consensus can support coordination, and `negotiate_fn` is a downstream callback hook, but the required autonomous S1 units and concrete first-party disturbance witness are absent. Generic multi-agent machinery is not S2 by topology alone.
- Evidence: [`lib/synapse/consensus.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/consensus.ex); [`lib/synapse/coordination_state.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/coordination_state.ex); [`lib/synapse/orchestrator/actions/run_config.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/orchestrator/actions/run_config.ex).
- Basis: explicit + structural
- Confidence: high
- Caveats: a downstream system can supply real S1 units and function-specific negotiation; that specialized system requires its own assessment.

### Absence scope

- Surfaces inspected: consensus loop, CoordinationState, signal router, orchestrator request/result aggregation, specialist selection and negotiation callback surface.
- Plausible first-party paths checked: weighted/unanimous/majority consensus, multiple configured specialists, signal routing and `negotiate_fn`.
- Why no material first-party path remains: without packaged autonomous S1 units, the first Profile gate fails; the remaining mechanisms are deterministic or downstream-composed primitives rather than an established inter-S1 regulatory relation.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established over autonomous operations.
- Disturbance / variety regulated: not established at whole-system current-operation scope.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: orchestrator `list_agents`, `health_check`, add/remove/reconcile/restart, workflow state/persistence, timeouts, iteration limits and process supervision.
- Closure path: no whole-system current view → discretionary resource/commitment/priority decision → changed autonomous S1 operation loop is established.
- Why this is / is not agent-owned: `Orchestrator.Runtime` has a real view of configured/running processes and can deterministically reconcile them, but desired topology is supplied by configuration and process health logic merely enforces it. Add/remove APIs are generic host controls, not a first-party autonomous current-management decision path.
- Evidence: [`lib/synapse/orchestrator/runtime.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/orchestrator/runtime.ex); [`lib/synapse.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse.ex).
- Basis: explicit + structural
- Confidence: high
- Caveats: deterministic lifecycle reconciliation is operationally useful but does not own the organizational decision selecting current priorities/resources.

### Absence scope

- Surfaces inspected: runtime health/list APIs, topology reconciliation, process restart/removal, coordination state, timeout/max-iteration controls and workflow persistence.
- Plausible first-party paths checked: orchestrator naming, health view, runtime add/remove, restart-on-crash, current consensus state and escalation.
- Why no material first-party path remains: no first-party actor uses the whole-system view to choose or revise current commitments/resources/priorities on behalf of autonomous S1 operations.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit path is established.
- Disturbance / variety regulated: not established.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: workflow audit trails, telemetry, CodeReview security/performance actions, consensus result aggregation and escalation messages.
- Closure path: no ordinary operational claim → complementary independent access → audit judgment → corrective return into operation loop is packaged.
- Why this is / is not agent-owned: workflow audit trails/telemetry observe the ordinary execution path; deterministic code-review scanners are ordinary configured review work rather than a complementary audit of an S1/S3 claim; no independent auditor with a corrective return path is wired into the standard distribution.
- Evidence: [`lib/synapse/orchestrator/actions/run_config.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/orchestrator/actions/run_config.ex); [`lib/synapse/domains/code_review/actions/security/check_sql_injection.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/domains/code_review/actions/security/check_sql_injection.ex).
- Basis: explicit + structural
- Confidence: high
- Caveats: downstream workflows may use Synapse to construct independent review cells; repository co-location or a component named review does not establish S3* here.

### Absence scope

- Surfaces inspected: workflow audit trails/persistence, telemetry, CodeReview scanners/summary, consensus and signal result paths.
- Plausible first-party paths checked: audit trail, code review, security/performance specialists, telemetry and escalation.
- Why no material first-party path remains: none supplies complementary operational access plus an independent audit judgment that returns findings into corrective regulation of an established operating organization.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: not established as future-oriented organizational adaptation.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: external LLM calls, configurable skills/actions, signal ingestion, workflow persistence, telemetry and developer-reloadable orchestrator configuration.
- Closure path: no external/future distinction → adaptation option → decision → changed present capability/S3 loop is packaged.
- Why this is / is not agent-owned: `GenerateCritique` reacts to a supplied prompt; signal ingestion reacts to current events; configuration/skills are supplied by developers. None first-party senses future-relevant change and autonomously develops an adaptation option that changes the runtime's capability.
- Evidence: [`lib/synapse/actions/generate_critique.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/actions/generate_critique.ex); [`lib/synapse/orchestrator/runtime.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/orchestrator/runtime.ex).
- Basis: explicit + structural
- Confidence: high
- Caveats: hot-reloadable topology and configurable actions are constructor surfaces, not prospective adaptation decisions by themselves.

### Absence scope

- Surfaces inspected: LLM adapter/action, action/skill configuration, runtime reload/reconciliation, signals, workflow persistence and telemetry.
- Plausible first-party paths checked: LLM critique, configuration reload, skill/action changes, event ingestion, retry/compensation and historical workflow state.
- Why no material first-party path remains: adaptation content and decision authority remain external/developer-owned; the runtime supplies execution machinery rather than an outside-and-then intelligence loop.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy closure is established.
- Disturbance / variety regulated: not established at identity/ultimate-policy scope.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: declarative agent metadata/configuration, signal schemas, escalation policy strings, workflow limits, external model profiles and host application configuration.
- Closure path: no identity/ultimate-policy issue → legitimate ultimate authority → returned decision governing subsequent operation loop is packaged.
- Why this is / is not agent-owned: configuration and escalation policies define technical behavior but do not create an ultimate-policy decision process. Human escalation on failed consensus is an ordinary operational exception and has no first-party returned identity/policy closure.
- Evidence: [`lib/synapse/orchestrator/agent_config.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse/orchestrator/agent_config.ex); [`lib/synapse.ex`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/lib/synapse.ex); [`config/config.exs`](https://github.com/nshkrdotcom/synapse/blob/bc43df9671b1e4974054e1ce0109f3e37733e9f4/config/config.exs).
- Basis: explicit + structural
- Confidence: high
- Caveats: a parent application can define organizational identity/policy around Synapse, but that separate authority is not a first-party S5 closure of this framework.

### Absence scope

- Surfaces inspected: orchestration configuration, agent metadata, escalation policy, signal/domain registration, model profiles and application configuration.
- Plausible first-party paths checked: orchestrator role, human escalation, static config/policies, agent metadata and external provider selection.
- Why no material first-party path remains: these are technical configuration or operational escalation mechanisms; no reviewed path raises and closes an identity/ultimate-policy matter at the assessed recursion.

## Recursion

Synapse is explicitly a framework for constructing systems with coordinators and multiple agents, but the frozen distribution does not itself package the autonomous S1 organization needed to treat those configured processes as recursive viable units. Downstream compositions are separate systems-in-focus and may receive different mappings when their actual actors, disturbances and decision rights are evidenced.

## Variety and escalation

The framework provides strong technical variety handling: typed signals, workflow persistence, process supervision, consensus thresholds, retries/compensation, timeout budgets and escalation payloads. These mechanisms attenuate and transport execution variety but do not substitute for autonomous organizational ownership. The `coordinate/3` no-consensus path can emit a human escalation request, yet the returned parent decision is not first-party closed back into operation at this ref.

## Summary

At the frozen revision, Synapse is a substantive constructor/orchestration framework but not an included autonomous harness. Its declarative runtime, signals, workflows, consensus and LLM action are real first-party primitives; however the standard distribution does not close an autonomous S1 decision/action feedback loop. The direct coordination API's production agent invocation is a stub, the nominal default orchestrator configuration file is absent, and declarative agents leave substantive actions/callbacks to downstream composition. Because included assessments require `S1=A`, the canonical outcome should be `excluded-no-agentic-vsm` rather than forcing Constructor notation onto S1.
