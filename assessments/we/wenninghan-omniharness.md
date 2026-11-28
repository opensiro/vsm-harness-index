---
harness_id: wenninghan-omniharness
project_name: OmniHarness
repository: https://github.com/WenNinghan/OmniHarness
review_ref: 482c7e75582fa25700f71e339f55b4fd43bfba0f
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# OmniHarness

## Review boundary

- System in focus: One OmniHarness agent run with its staged workers and supervised workspace.
- Purpose and identity: Carry out a user task by planning, executing tool actions and returning observations and a reviewed result.
- Relevant environment: The operator, configured external model providers, a PostgreSQL checkpoint store and optional workspace broker and sandbox.
- Standard-distribution boundary: The supported self-hosted web/API/worker distribution with its documented agent and optional tool switches.
- Credited operating / distribution surfaces: The worker, staged/compact agent workflows, optional workspace tools, run controls and supported bounded revision mode.
- Adjacent first-party surfaces excluded from ownership: Developer evaluation and validation fixtures, model-provider internals, broker infrastructure decisions and experimental owner qualification paths.
- First-party operating / deployment modes considered: Default chat, explicitly enabled PostgreSQL agent mode, tool-enabled workspace mode and opt-in revision.
- Recursion level: One run above its separately assigned execution tasks.
- Reviewed revision: 482c7e75582fa25700f71e339f55b4fd43bfba0f
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The self-hosted API queues an immutable run snapshot. The worker builds the chosen execution graph from pinned model and workflow settings. Staged runs bind bounded tasks and evidence to durable checkpoints. A tool-enabled deployment adds workspace and sandbox adapters. The browser reflects run, tool and check results.

## Operational model

Execution agents decide tool actions for their assigned tasks and return results. Planning and dispatch can establish dependencies and write scopes. The host enforces access and budget. The operator can relieve pauses, stop a run, or change active constraints through the supplied command channel.

## S1 — Operations

- State: A
- Function: Complete an assigned task by selecting and interpreting available tools.
- Disturbance / variety regulated: Variable workspace state, model responses and tool results.
- Decisive decision or feedback right: Choose the working tool, revise the plan based on feedback and close the task.
- Decision owner: The configured execution model in the supplied agent runtime.
- Supporting / enforcement mechanisms: The worker constructs the graph, host supplies controls and authorized tools, and checkpoints store events.
- Closure path: Tool results are returned to the execution agent and the task result is collected and passed to review and final output.
- Why this is / is not agent-owned: The operator enables and configures tools. The installed agent owns tactical decisions during a supported run.
- Boundary reachability: The standard self-hosted worker dispatches the configured graph with the repository-owned execution agent.
- Evidence: [README.md](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/README.md#L92-L103), [src/omniharness/worker.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/worker.py#L341-L359), [src/omniharness/m3_worker.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m3_worker.py#L762-L812), [src/omniharness/m3_stages.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m3_stages.py#L777-L821), [src/omniharness/m4_runtime.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m4_runtime.py#L252-L280)
- Basis: Static inspection of pinned first-party source.
- Confidence: high
- Caveats: Deployment must explicitly enable the agent and configure any workspace-tool hosts.

## S2 — Coordination

- State: A
- Function: Prevent distinct execution tasks from conflicting over workspace writes and consuming premature dependencies.
- Disturbance / variety regulated: A pair of tasks can request overlapping path scopes or a consumer can start before its required producer.
- Decisive decision or feedback right: The planning model sets write scopes and dependency relationships within the supported collaborative mode.
- Decision owner: The plan/dispatch model that sees the global task and assigns work.
- Supporting / enforcement mechanisms: Validated plan schema, readiness selection, overlap detection and scoped dispatch.
- Closure path: Overlapping or unspecified writable scopes serialize when batching is available. A producer's completion and bound evidence enter the consumer context.
- Why this is / is not agent-owned: Model judgments establish which work and paths must be separated. Runtime selection applies the declared relationships.
- Boundary reachability: The supported collaboration graph uses the plan for actual dependency and overlap-aware dispatch.
- Distinct S1 units: Separate model-driven execution tasks with their own scoped workspace assignments.
- Inter-S1 disturbance: Overlapping write claims or early reads can corrupt or invalidate another task's output.
- Attenuating coordination relation: Declared dependencies and write scopes determine eligibility for joint scheduling.
- Feedback into subsequent S1 behaviour: A consumer gets completed predecessor evidence and the selected scope for its tool calls.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The scheduler tests shared path interference and uses actual producer completion for dependency handoff.
- Evidence: [src/omniharness/m3_stages.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m3_stages.py#L62-L104), [src/omniharness/m3_stages.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m3_stages.py#L619-L636), [src/omniharness/m3_stages.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m3_stages.py#L744-L821), [src/omniharness/m4_collaboration.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m4_collaboration.py#L52-L100)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: Interactive variants may schedule one ready task at a time. The overlap witness is the supplied collaborative batching strategy.

## S3 — Inside-and-now control

- State: P
- Function: Intervene in the active run across its planning and child execution commitments.
- Disturbance / variety regulated: A pending or active run can diverge from changed priorities or retain risky outstanding work.
- Decisive decision or feedback right: Inspect the current run and decide whether to suspend work or issue a revised binding requirement.
- Decision owner: The authenticated operator for the run.
- Supporting / enforcement mechanisms: Run and agent views, budgets, command log and fenced safe-boundary application.
- Closure path: The operator's command changes run state or adds requirements that the execution model receives before later calls.
- Why this is / is not agent-owned: The model selects task actions and plans. The attended operator owns the supplied current-run suspension and changed requirements path.
- Boundary reachability: The shipped run view and command endpoints expose a live first-party operator path to the worker.
- Whole-system current view: The operator sees the run status, child agent stages, live events, applied commands and run budgets.
- Current-control decision scope: Suspend or resume the current run and change requirements that constrain pending work across the run.
- Evidence: [docs/M3-controls.md](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/docs/M3-controls.md#L7-L19), [src/omniharness/api.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/api.py#L348-L377), [src/omniharness/services.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/services.py#L540-L597), [src/omniharness/m3_host.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m3_host.py#L154-L210), [src/omniharness/m3_stages.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m3_stages.py#L744-L750)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: Initial dispatch and automatic application of bounded revision rules do not establish autonomous whole-run reprioritization.

## S3* — Complementary audit

- State: A
- Function: Challenge executor claims by checking separate records and return actionable findings for correction.
- Disturbance / variety regulated: The executor's account can conflict with actual command evidence, stored artifacts or acceptance conditions.
- Decisive decision or feedback right: The review-stage model selects supported findings and corrective recommendations.
- Decision owner: A separately invoked review role with host-provided complementary evidence.
- Supporting / enforcement mechanisms: Protected review evidence binds host-stored tool events and artifacts to the run. Evidence reference validation and a bounded rework budget guard return.
- Closure path: In the supported bounded revision mode actionable findings become revision feedback and a revised result goes through review again.
- Why this is / is not agent-owned: The review actor judges the discrepancy and remedy. The controller deterministically enforces admission and revision limits.
- Boundary reachability: The deployed worker passes the supplied bounded-revision configuration to its staged graph.
- Claim being audited: An executor claim about command completion, artifact content or a required outcome.
- Ordinary reporting path: Task outputs and the aggregated execution answer.
- Complementary access path: The host collects provenance-bound tool operations and artifact evidence outside the executor summary.
- Independence boundary: A distinct review invocation compares the execution claim with host records and acceptance conditions.
- Who acts on findings: The host routes operationally eligible failures to bounded revision, and the execution agent receives the specific findings.
- Evidence: [README.md](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/README.md#L123-L128), [src/omniharness/m3_stages.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m3_stages.py#L394-L414), [src/omniharness/m3_stages.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m3_stages.py#L641-L670), [src/omniharness/review_evidence.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/review_evidence.py#L409-L427), [src/omniharness/review_evidence.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/review_evidence.py#L631-L670), [src/omniharness/m3_stages.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m3_stages.py#L1124-L1138), [src/omniharness/m3_stages.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m3_stages.py#L1198-L1249), [src/omniharness/m3_stages.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m3_stages.py#L1298-L1306)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: Bounded rework must be enabled. Evidence cannot guarantee facts beyond the verified reference scope, and model vendors may be shared.

## S4 — Outside-and-then intelligence

- State: —
- Function: Prospective change of the deployed capability in response to outside variation was sought.
- Disturbance / variety regulated: Provider model conditions and evaluation evidence can change over time.
- Decisive decision or feedback right: No supplied loop was found that takes those changes into a durable prospective adaptation decision.
- Decision owner: The operator configures provider models and accepts suggestions for a specific run.
- Supporting / enforcement mechanisms: On-demand model suggestions, registered provider capabilities, temporary routing cache and offline evaluation.
- Closure path: Routing selections freeze into the current run. Evaluation tools produce comparison evidence.
- Why this is / is not agent-owned: Current-run model allocation and development benchmarking do not supply a deployed adaptation return.
- Evidence: [docs/M3-on-demand-model-routing.md](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/docs/M3-on-demand-model-routing.md#L3-L8), [docs/M3-on-demand-model-routing.md](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/docs/M3-on-demand-model-routing.md#L18-L25), [src/omniharness/ai_routing.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/ai_routing.py#L160-L234), [docs/M4-evaluation.md](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/docs/M4-evaluation.md#L15-L32), [README.md](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/README.md#L125-L133)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: A later operator can independently edit model configuration.

### Absence scope

- Surfaces inspected: Routing UI and API, run snapshots, context controls, development evaluation and model settings.
- Plausible first-party paths checked: An external provider or capability signal that generates adaptation options and returns an accepted durable capability to future operations.
- Why no material first-party path remains: Suggestions affect a task snapshot and need explicit confirmation when reused. The evaluation output does not bind a runtime adaptation.

## S5 — Policy and identity

- State: —
- Function: Resolve identity or an ultimate-policy dispute for the runtime.
- Disturbance / variety regulated: A requested action may exceed authority or conflict with configured constraints.
- Decisive decision or feedback right: The shipped runtime does not route an identity issue to an adjudicator and return a governing policy decision.
- Decision owner: The authenticated operator owns run controls and deployment settings.
- Supporting / enforcement mechanisms: Credential and approval gates, action contract updates and workflow limits.
- Closure path: The service applies configured scope, or returns an accepted bounded decision to the current operation.
- Why this is / is not agent-owned: The identified paths regulate task scope and authorization. They do not resolve organizational identity.
- Evidence: [src/omniharness/api.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/api.py#L331-L362), [src/omniharness/services.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/services.py#L454-L488), [src/omniharness/m3_host.py](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/src/omniharness/m3_host.py#L154-L210), [docs/M4-tools-context.md](https://github.com/WenNinghan/OmniHarness/blob/482c7e75582fa25700f71e339f55b4fd43bfba0f/docs/M4-tools-context.md#L63-L65)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: Project development governance is adjacent to the deployed run.

### Absence scope

- Surfaces inspected: User commands, action-contract updates, workspace approvals, protected configuration and owner qualification.
- Plausible first-party paths checked: A policy escalation that settles a disagreement about the system's governing goals and binds later operation.
- Why no material first-party path remains: The current interfaces constrain or redirect a run within an existing policy. No first-party return path for an ultimate-policy adjudication was established.

## Recursion

The run hosts distinct execution tasks. The graph controller and the optional review stage serve the same run. Broker, database and model endpoints are dependencies.

## Variety and escalation

Task scopes, execution budgets and worker control commands constrain ordinary disturbance. Checkpointed questions can return a user answer. Unknown tool outcomes and blocked approvals surface in run evidence.

## Evidence gaps

Pinned source review. No provider calls, PostgreSQL instance, browser, broker, sandbox or revision round were run. Credit is confined to the reachable documented modes at this revision.
