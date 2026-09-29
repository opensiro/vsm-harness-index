---
harness_id: embabel
project_name: Embabel
repository: https://github.com/embabel/embabel-agent
review_ref: 45c70d4051f758034b213f1c730c64ec190dc6fe
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Embabel

## Review boundary

- System in focus: the first-party `embabel/embabel-agent` JVM agent platform at frozen revision `45c70d4051f758034b213f1c730c64ec190dc6fe`, including the standard `AgentPlatform` / `AgentProcess` runtime, `Autonomy` goal/agent selection, LLM ranking, GOAP/utility/supervisor execution modes, blackboard/process state, first-party process control and the shipped interactive approval path where they bear on organizational function.
- Purpose and identity: execute developer-declared agent capabilities against user/application intent while dynamically selecting agents or goals, constructing goal-seeking agents, planning and replanning action paths from current world state, and supporting LLM-supervised orchestration of available actions.
- Relevant environment: user/application intent and bindings, developer-supplied actions/goals/conditions/domain objects, current blackboard/world state, tool and model responses, model/provider availability, process budgets and termination signals, and optional human shell responses.
- Standard-distribution boundary: shipped Embabel runtime modules that create/run `AgentProcess` instances and expose Focused, Closed, Open, Utility and Supervisor invocation modes are inside. External LLM providers, MCP servers/tools, application/domain implementations supplied by downstream developers, remote A2A peers, and generated downstream applications are environment/dependencies rather than Embabel organizational owners.
- Credited operating / distribution surfaces: `README.md`; `embabel-agent-api` runtime including `AgentPlatform`, `DefaultAgentPlatform`, `Autonomy`, `LlmRanker`, `SimpleAgentProcess`, `ConcurrentAgentProcess`, `SupervisorInvocation`, process-control/blackboard primitives, and the shipped goal-approval interface; the shell path only where it demonstrates the supported human goal-veto mode.
- Adjacent first-party surfaces excluded from ownership: repository tests and examples; documentation generation; CI/release/contributor workflows; the optional observability module's traces/metrics/exporters; A2A transport/server adapters as transport rather than decision owners; development-only test fixtures and future modes described but not shipped.
- First-party operating / deployment modes considered: Focused invocation of a chosen agent; Closed model-backed agent choice; Open model-backed goal choice followed by dynamic agent construction and GOAP/utility planning; Supervisor invocation using an LLM to orchestrate available actions; Simple and Concurrent process implementations; child-agent transformations; optional shell goal approval/HITL; process budgets/termination/guardrails and observability.
- Recursion level: one Embabel `AgentPlatform` application serving a task/intent. A running goal-seeking/supervisor `AgentProcess` is the operational S1 at this recursion. Individual actions/tool calls are operations inside that S1 rather than separate viable S1 units merely because they may execute concurrently; nested child processes are lower-recursion delegated operations unless evidence establishes independent same-recursion units.
- Reviewed revision: `45c70d4051f758034b213f1c730c64ec190dc6fe`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Embabel is a Spring/JVM agent framework centered on a stateful `AgentPlatform`. Developers supply typed actions, goals, conditions and domain objects; the platform turns them into runnable `AgentProcess` instances backed by a blackboard and a planning system. The README describes plans as dynamically formulated rather than programmed sequences and states that the process replans after actions as conditions/world state change.

The standard distribution includes an explicit `Autonomy` service. In Closed mode it sends the user's intent plus the set of deployed agents to the default `Ranker`, filters the returned confidence ranking and autonomously selects a credible agent. In Open mode the same service ranks available goals, selects a credible goal, creates a dynamic goal-seeking agent from the platform scope and then runs it. The default Spring configuration wires `Ranker` to `LlmRanker`; that implementation prompts an LLM to choose among named agents/goals and return confidence scores. Thus the decisive semantic choice is not merely an application callback or deterministic router.

After a process exists, `SimpleAgentProcess` repeatedly determines current world state, asks its planner for a best-value plan, executes the next selected action, observes the resulting state and replans until a goal is complete or the process reaches another terminal/waiting state. `ConcurrentAgentProcess` can launch currently achievable actions in parallel, but this remains one process-level operational loop. It contains deterministic handling for concurrent replan requests and status aggregation rather than an independent coordination actor among separately established S1 units.

Embabel also ships `SupervisorInvocation`, which creates a synthetic supervisor agent. Its first-party contract explicitly uses an LLM to orchestrate available actions toward a caller-specified result type. This is another supported autonomous S1 execution mode, not evidence by itself of VSM S3: the supervisor is solving the current task by selecting tools/actions, not regulating organization-wide resources, commitments or priorities across independently established operations.

Process limits and safety surfaces are deliberately separated from ownership. `ProcessOptions`/`ProcessControl` encode budgets, maximum actions/tokens/cost and early termination policies; guardrails validate prompts/responses against supplied policy; termination/kill paths enforce requested or configured constraints. The optional observability module supplies traces/metrics/export rather than a separate audit judgment loop. The shell can ask a user to approve a selected goal or answer HITL requests, but ordinary task-goal approval is not identity/ultimate-policy governance.

Primary evidence:

- [`README.md`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/README.md)
- [`AgentPlatform.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/AgentPlatform.kt)
- [`DefaultAgentPlatform.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/support/DefaultAgentPlatform.kt)
- [`Autonomy.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/api/common/autonomy/Autonomy.kt)
- [`LlmRanker.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/spi/support/LlmRanker.kt)
- [`SimpleAgentProcess.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/support/SimpleAgentProcess.kt)
- [`ConcurrentAgentProcess.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/support/ConcurrentAgentProcess.kt)
- [`SupervisorInvocation.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/api/invocation/SupervisorInvocation.kt)
- [`ProcessOptions.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/ProcessOptions.kt)
- [`GoalChoiceApprover.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/api/common/autonomy/GoalChoiceApprover.kt)
- [`GuardRail.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/api/validation/guardrails/GuardRail.kt)
- [`TerminalServices.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-shell/src/main/kotlin/com/embabel/agent/shell/TerminalServices.kt)
- [`embabel-agent-observability/README.md`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-observability/README.md)

## Operational model

In the strongest standard mode, a caller supplies an intent/bindings and an `AgentScope` containing developer-declared capabilities. `Autonomy` asks the shipped LLM ranker to judge which goal or agent best matches that intent. In Open mode it then constructs a goal-specific agent from all relevant platform resources; in Closed mode it runs the selected deployed agent. The resulting `AgentProcess` maintains blackboard/world state and repeatedly plans, executes and replans. In Supervisor mode a shipped LLM-supervisor action chooses which available action/tool to invoke toward a declared output goal.

The developer still defines the available domain capabilities and ultimate application boundary, but the standard runtime contains a live autonomous actor that makes consequential operational choices among those capabilities. Deterministic planning, thresholds, budgets, status aggregation, persistence and guardrail enforcement support that operation without being credited as higher VSM ownership merely because they can control execution.

## S1 — Operations

- State: A
- Function: turn a user/application intent and current process state into an achieved domain goal by autonomously selecting a suitable agent/goal and executing/replanning among the available declared capabilities.
- Disturbance / variety regulated: heterogeneous user intents, multiple candidate agents/goals, changing blackboard/world state after each action, model/tool outputs and alternative action paths toward the requested result.
- Decisive decision or feedback right: in Closed/Open modes, judge which agent or goal best matches the current intent; in Supervisor mode, decide which available action/tool to invoke next toward the specified result. The subsequent process loop selects/reselects an executable plan from current state until completion or termination.
- Decision owner: the model-backed autonomous actor invoked through Embabel's shipped `LlmRanker` / supervisor execution path for semantic agent/goal/action choice, with the first-party planner/runtime closing execution and feedback.
- Supporting / enforcement mechanisms: developer-declared actions/goals/conditions and domain model; `AgentPlatform`; confidence cutoffs; deterministic GOAP/utility planners; blackboard/world-state determination; process persistence; tool/model adapters; retries; budget and termination enforcement.
- Closure path: caller intent/bindings → first-party Autonomy or Supervisor path exposes available capabilities to a model-backed decision actor → selected agent/goal/action path is instantiated/executed → action/tool results update process state/blackboard → the process re-evaluates state and replans/continues → goal completion or another supported process outcome is returned.
- Boundary reachability: `Autonomy` is a shipped Spring service on `AgentPlatform`, the default Spring configuration wires `Ranker` to first-party `LlmRanker`, and `SupervisorInvocation` directly creates and runs a first-party supervisor agent. Applications provide capabilities and model credentials, but do not have to author the autonomous agent/goal ranking or supervisor orchestration loop itself.
- Why this is / is not agent-owned: removing the model-backed decision actor while retaining the planner, blackboard and scheduler removes the semantic choice of which agent/goal best fits open/closed user intent and removes the LLM supervisor's action-selection discretion. Deterministic machinery can still execute a preselected agent/plan, but materially the same autonomous operational decision does not occur.
- Evidence: [`README.md`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/README.md); [`Autonomy.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/api/common/autonomy/Autonomy.kt); [`LlmRanker.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/spi/support/LlmRanker.kt); [`SupervisorInvocation.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/api/invocation/SupervisorInvocation.kt); [`SimpleAgentProcess.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/support/SimpleAgentProcess.kt).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: application developers define the available actions/goals/conditions and may choose Focused execution that bypasses dynamic ranking. `A` is credited because first-party Open/Closed/Supervisor modes operationally close an autonomous S1 loop; it does not claim every Embabel invocation is autonomous in the same way. External LLM inference remains a provider dependency rather than a first-party organizational owner outside the shipped role/runtime path.

## S2 — Coordination

- State: —
- Function: no material first-party same-recursion inter-S1 conflict/oscillation attenuation loop was established.
- Disturbance / variety regulated: concurrent action execution, nested child processes and multiple deployed agents create topology/concurrency, but the reviewed standard modes do not establish a specific same-recursion conflict among distinct operational S1 units together with an S2-specific feedback relation that attenuates it.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `ConcurrentAgentProcess` launches achievable actions concurrently and deterministically aggregates their statuses; when multiple concurrent actions request replanning it keeps the first replan request and intentionally drops the others' blackboard updates. Child processes inherit/spawn blackboards and lifecycle relations. These mechanisms coordinate execution mechanics inside/delegated from one operational process but do not by themselves establish S2 at the assessed recursion.
- Closure path: not applicable at S2; no qualifying distinct-S1 disturbance → coordination judgment → changed subsequent S1 behaviour loop was found.
- Why this is / is not agent-owned: there is no established S2 function to own. The observed concurrency/replan handling is deterministic runtime arbitration among actions inside one process, not evidence that an autonomous coordinator regulates interference among independently established S1 units.
- Evidence: [`ConcurrentAgentProcess.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/support/ConcurrentAgentProcess.kt); [`AgentPlatform.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/AgentPlatform.kt); [`DefaultAgentPlatform.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/support/DefaultAgentPlatform.kt).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: an application can compose multiple Embabel agents/processes and custom coordination. Generic composition, shared state, delegation or parallelism does not satisfy the Methodology's S2 constructor threshold without an evidenced S2-specific conflict path.

### Absence scope

- Surfaces inspected: `AgentPlatform` deployment/process APIs; Simple and Concurrent process execution; child-process creation and agent-as-transformation delegation; Open/Closed/Supervisor composition; blackboard/process state; README claims about parallelization/federation.
- Plausible first-party paths checked: concurrent action execution; simultaneous replan requests; deployed-agent selection; child-process delegation; shared blackboard/state; dynamic agent construction; planned federation references.
- Why no material first-party path remains: the concrete collision-like behavior found is intra-process action/replan arbitration, while future federation is not a shipped current path. No same-recursion pair of distinct S1 units plus a first-party interference-specific attenuation loop and feedback into their subsequent behavior was established.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control loop over organization-wide resources, commitments, priorities, constraints, accountability or synergy was established beyond task execution and deterministic process enforcement.
- Disturbance / variety regulated: process/action progress, stuck states, changing world state, cost/token/action budgets, termination requests and tool/model failures are handled, but these are local task/runtime disturbances rather than evidenced whole-organization current-control variety.
- Decisive decision or feedback right: not established at S3. Goal/agent/action choice is operational task selection; planner replanning chooses a path for that task; configured budgets and termination policies enforce caller/developer constraints.
- Decision owner: not established as S3 owner.
- Supporting / enforcement mechanisms: `AgentProcess` status/lifecycle, `ProcessControl`, budget-based early termination, kill/terminate cascades, `StuckHandler`, deterministic planner/replan logic, Supervisor action orchestration, process repository and telemetry.
- Closure path: not applicable at S3; observed mechanisms either continue/stop/replan a specific process or execute preconfigured constraints and do not close a whole-system current-control decision loop.
- Why this is / is not agent-owned: the shipped model-backed supervisor sees available actions for one invocation goal and selects task actions, not organization-wide current operations/resources/commitments. Removing it leaves no separate S3 authority; deterministic process-control policies still enforce limits selected elsewhere.
- Evidence: [`SupervisorInvocation.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/api/invocation/SupervisorInvocation.kt); [`ProcessOptions.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/ProcessOptions.kt); [`SimpleAgentProcess.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/support/SimpleAgentProcess.kt); [`StuckHandler.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/api/common/StuckHandler.kt).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: Embabel uses names such as `Supervisor`, `AgentPlatform`, process control and workflow management. Those names and enforcement powers do not satisfy S3 without the required whole-system view and decisive organizational current-control right.

### Absence scope

- Surfaces inspected: platform/process lifecycle; Supervisor invocation; GOAP/utility planning and replanning; process budgets/termination; stuck handling; concurrent status aggregation; persistence/context state; observability and shell/HITL paths.
- Plausible first-party paths checked: supervisor orchestration; open-mode cross-provider capability composition; task/goal selection; budget/token/action limits; kill/termination cascades; stuck recovery; current process repository; human confirmation and process resumption.
- Why no material first-party path remains: all located interventions are task-level action/goal choices, local process recovery, deterministic enforcement or operator responses. No actor receives a whole-system current view and a materially discretionary right over shared organization-wide resources/commitments/priorities/constraints with returned closure into multiple current operations.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary and sufficiently independent audit loop over ordinary operational claims/outcomes was established.
- Disturbance / variety regulated: guardrails validate AI-interaction content and observability records traces/metrics, but neither establishes a separate complementary audit judgment with sufficiently independent access to operational reality and a returned finding that changes control.
- Decisive decision or feedback right: not established for S3*.
- Decision owner: not established.
- Supporting / enforcement mechanisms: input/output guardrail interfaces and violation handling; event listeners; traces, metrics and LLM/tool span export; testing utilities; process status/events.
- Closure path: not applicable at S3*; located validation/telemetry paths do not reconstruct ordinary operational claim → independent complementary evidence path → audit judgment → finding returned to control.
- Why this is / is not agent-owned: a guardrail may be developer-supplied and may block content, while telemetry may expose what occurred, but neither is a shipped autonomous independent auditor of the operational result. No first-party model/actor was found owning such an audit verdict and closure.
- Evidence: [`GuardRail.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/api/validation/guardrails/GuardRail.kt); [`embabel-agent-observability/README.md`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-observability/README.md); [`ProcessOptions.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/ProcessOptions.kt).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: downstream applications can implement reviewers/evaluators or analyze exported telemetry; those composed/external systems are outside the standard-distribution ownership boundary unless wired as a first-party audit loop.

### Absence scope

- Surfaces inspected: guardrail APIs and enforcement role; observability module; process events/status/history; testing/evaluation documentation surfaces; supervisor/autonomy loops; shell approval/HITL; persistence and tool/model call records.
- Plausible first-party paths checked: pre/post model validation; policy guardrails; traces/metrics; testing support; supervisor review-like naming; process history; human confirmation; model ranking confidence.
- Why no material first-party path remains: reviewed validation is inline policy/content checking and reviewed observability is telemetry. Neither supplies a distinct audit role with complementary access and a materially independent operational verdict that returns to change subsequent organizational control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective intelligence/adaptation loop was established in the shipped assessed boundary.
- Disturbance / variety regulated: the process continuously reacts to current blackboard/world-state changes and may replan, rank a current intent or recover from current failure, but those are present-task adaptations rather than prospective sensing of future/external developments.
- Decisive decision or feedback right: not established at S4. The planner chooses a current action path; `Autonomy` chooses a current goal/agent; developers add capabilities/configuration outside the runtime loop.
- Decision owner: not established at S4.
- Supporting / enforcement mechanisms: dynamic planning/replanning, current intent ranking, blackboard/context persistence, model/provider abstraction, extensible action/goal registration.
- Closure path: not applicable at S4; no shipped prospective environmental distinction → adaptation-options generation/judgment → return into present capability loop was found.
- Why this is / is not agent-owned: model-backed ranking and supervisor orchestration are autonomous but operate on the current task/capability set. The README explicitly presents an `Evolving` mode that could add goals/agents during a running process as a possible future mode rather than the current shipped capability.
- Evidence: [`README.md`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/README.md); [`Autonomy.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/api/common/autonomy/Autonomy.kt); [`SimpleAgentProcess.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/support/SimpleAgentProcess.kt).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: dynamic replanning is substantial autonomy but is inside-and-now operational adaptation to current state, not sufficient evidence for VSM S4.

### Absence scope

- Surfaces inspected: Open/Closed Autonomy; goal/agent ranking; GOAP/utility planning and per-action replanning; context/blackboard persistence; model/provider role resolution; README roadmap/future execution modes; supervisor orchestration and extension APIs.
- Plausible first-party paths checked: replanning after new information; utility optimization; model/provider abstraction; persisted history/context; dynamic agent construction; proposed Evolving mode; proposed federation; developer extension of actions/goals.
- Why no material first-party path remains: current runtime loops consume present intent/state and a fixed currently registered capability set. The repository describes stronger self-evolving/federating behavior prospectively, not as a shipped operational S4 loop at the frozen revision.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy closure was established.
- Disturbance / variety regulated: applications may configure available agents/goals, model roles, budgets, guardrails, identities and goal approvals, but these are supplied operating constraints/task approvals rather than a runtime constitutional choice over what the organization ultimately is or should remain.
- Decisive decision or feedback right: not established at S5. Application developers/operators define the capability/policy boundary; an optional human `GoalChoiceApprover` may veto a selected task goal but does not decide organization-level identity or ultimate policy.
- Decision owner: not established as a qualifying first-party S5 owner.
- Supporting / enforcement mechanisms: `GoalChoiceApprover`; shell confirmation/HITL; configured guardrails; process identities; model/provider role configuration; developer-defined actions/goals; budgets/termination policy.
- Closure path: not applicable at S5; no identity/ultimate-policy issue → legitimate S5 authority → authoritative decision → returned governance of subsequent operation loop was found.
- Why this is / is not agent-owned: autonomous actors choose operational goals/actions inside a developer/operator-authored capability envelope. They are not shown possessing authority to redefine that envelope or the platform's ultimate mandate. Human shell approval is a per-goal/task veto, not parent S5 governance under the Methodology.
- Evidence: [`GoalChoiceApprover.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/api/common/autonomy/GoalChoiceApprover.kt); [`TerminalServices.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-shell/src/main/kotlin/com/embabel/agent/shell/TerminalServices.kt); [`ProcessOptions.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/core/ProcessOptions.kt); [`GuardRail.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/api/validation/guardrails/GuardRail.kt).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: a downstream organization can place Embabel under institutional governance or implement policy-changing agents. Such external/composed governance is not borrowed into this repository-relative standard-distribution assessment.

### Absence scope

- Surfaces inspected: goal approval and shell confirmation/HITL; agent/goal registration; model/provider role configuration; process identities; guardrails; budgets/termination; Autonomy/Supervisor operational decision paths; repository governance adjacent to runtime.
- Plausible first-party paths checked: human veto of selected goals; application configuration; policy/content guardrails; runtime identity metadata; supervisor authority; open-mode dynamic goal choice; developer/maintainer governance.
- Why no material first-party path remains: located decisions either select/approve an operational task, enforce externally supplied constraints or occur outside the runtime organizational boundary. No shipped S5 actor or qualifying parent loop owns and closes identity/ultimate-policy authority for the assessed Embabel organization.

## Recursion

The assessment treats one Embabel `AgentPlatform` application as the focal organization and a currently running autonomous goal-seeking/supervisor process as its operational S1. Individual actions and concurrent tool calls are lower-level operations within that process. Child-agent transformations are nested/delegated lower-recursion work unless separately composed as independent same-recursion operations; their existence alone is not evidence of S2 or higher VSM recursion.

## Variety and escalation

Embabel absorbs operational variety through model-backed selection among agents/goals, dynamic agent construction, planning/replanning, typed state, tools and optional supervisor orchestration. The planner and process-control machinery attenuate path/execution variety deterministically, while model actors supply semantic operational judgment. Exceptional conditions can stop, wait, replan or request human input, but the reviewed distribution does not elevate those mechanisms into separate S2/S3/S3*/S4/S5 closures.

## Evidence gaps

No evidence gap requires `?` at the frozen revision. The repository exposes unusually rich planning, supervisor, guardrail, observability and HITL surfaces; each was checked against the stricter function-first thresholds. The negative states reflect boundary-relative absence of those VSM functions/closure paths, not lack of sophisticated orchestration features.
