---
harness_id: orchestrix
project_name: Orchestrix
repository: https://github.com/aswin-kevin/orchestrix
review_ref: 34447e81f54a605cb780d534d8557573add273a3
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Orchestrix

## Review boundary

- System in focus: The Orchestrix Go agent runtime, its orx distribution, and the installed SDK coordinator mode.
- Purpose and identity: Run model-backed projects and delegate subtasks to bounded workers.
- Relevant environment: Operator or embedding program, local or configured workspaces, provider APIs, and optional tool services.
- Standard-distribution boundary: First-party runtime, CLI, and documented shipped SDK configurations. Independently authored providers, workers' domain instructions, extensions and callbacks are external as sources of organizational ownership.
- Credited operating / distribution surfaces: The installed orx CLI, built-in agent loop and SDK coordinator with typed worker descriptions and documented async middleware.
- Adjacent first-party surfaces excluded from ownership: Examples as standalone deployments, evals, live tests, repository CI and package maintenance.
- First-party operating / deployment modes considered: Single-agent CLI and SDK runtime, optional first-party coordinator with configured workers. Examples corroborate wiring.
- Recursion level: One request-scoped coordinator team, with its worker agents as S1 units.
- Reviewed revision: 34447e81f54a605cb780d534d8557573add273a3
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

A Go model/tool loop maintains agent transcript state and emits events. Middleware supplies optional coordination, checkpointing, approval, recovery and grading. Coordinator construction binds an agent prompt, an enabled worker set and the async middleware. [agent/loop.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/agent/loop.go), [coordinator/coordinator.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/coordinator/coordinator.go), [agent/checkpoint.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/agent/checkpoint.go), [cmd/orx/main.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/cmd/orx/main.go).

## Operational model

Model-backed worker runs execute subtasks. In the coordinator mode, the leading model assigns self-contained worker commitments, gets status and results, and can send new instructions or cancel a running commitment. Other top-level SDK calls may run in separate threads outside that team's control.

## S1 — Operations

- State: A
- Function: Deliver operator or host tasks through a model-driven tool loop.
- Disturbance / variety regulated: Uncertain work inputs and tool outcomes.
- Decisive decision or feedback right: Choose and revise tool actions and end the task.
- Decision owner: The run's model-backed agent, including coordinator workers executing operative subtasks.
- Supporting / enforcement mechanisms: Tool routing, permission enforcement, events and checkpointing.
- Closure path: Tool results return to the transcript and directly condition subsequent model decisions.
- Boundary reachability: Both the CLI and SDK run the first-party loop. The coordinator starts workers through the included subagent and async implementations.
- Why this is / is not agent-owned: The runtime supplies model and tools, while the model chooses how to carry out the task.
- Evidence: [agent/loop.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/agent/loop.go), [agent/schedule.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/agent/schedule.go), [middleware/subagents/launcher.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/middleware/subagents/launcher.go).
- Basis: Explicit
- Confidence: High
- Caveats: An external model serves as inference infrastructure for the supplied runtime.

## S2 — Coordination

- State: A
- Function: Attenuate interference among worker assignments and incompatible worker outputs.
- Disturbance / variety regulated: Parallel agents do not share the coordinator's context, and their outputs can overlap or contradict each other.
- Decisive decision or feedback right: Partition independent assignments and revise work against conflict found in returned outputs.
- Decision owner: The model-backed coordinator of the active team.
- Supporting / enforcement mechanisms: Default coordination prompt, bounded async slots, task/results registry and live task updates.
- Closure path: The coordinator checks gaps or contradictions, revises worker instructions or sends follow-up work, then consumes the revised result.
- Boundary reachability: The first-party coordinator constructor installs the default prompt and routes its model to the shipped task tools. Hosts supply the roster, not the coordination callback.
- Why this is / is not agent-owned: The stock model supervisor owns the content of the assignments and how to resolve contradictions. A concurrency cap by itself does neither.
- Evidence: [coordinator/prompt.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/coordinator/prompt.go), [coordinator/coordinator.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/coordinator/coordinator.go#L85-L128), [middleware/async/tools.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/middleware/async/tools.go#L224-L256), [middleware/async/notify.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/middleware/async/notify.go).
- Basis: Structural
- Confidence: Medium
- Caveats: This is prompt-mediated regulation in the documented multi-worker coordinator mode. It does not serialize worker edits to a shared backend.
- Distinct S1 units: Separately launched worker model runs with their own task context.
- Inter-S1 disturbance: Overlapping scopes or incompatible results can prevent the assigned workers from jointly delivering the requested output.
- Attenuating coordination relation: The coordinator assigns independent scopes before parallel execution and uses results and contradiction checks to revise bounded worker assignments.
- Feedback into subsequent S1 behaviour: Updated instructions enter a running worker before its next step or become a new worker task, with the revised result returned to the coordinator.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The packaged prompt binds assignment partition and returned contradictions to a corrective worker step. The generic task tools alone do not establish the relationship.

## S3 — Inside-and-now control

- State: A
- Function: Regulate current work commitments and worker capacity for the whole request-scoped team.
- Disturbance / variety regulated: New dependencies, unnecessary running work and incomplete worker commitments.
- Decisive decision or feedback right: Choose whether to revise, cancel or start worker commitments across the current team.
- Decision owner: The model-backed coordinator.
- Supporting / enforcement mechanisms: Thread-scoped task registry, list/check/update/cancel tools and before-stop progress reminder.
- Closure path: Status and completion update the lead's current view. Cancel stops a selected run and returns its disposition; updates change subsequent worker steps.
- Boundary reachability: The shipped coordinator composes the same async implementation that exposes the current task list and interventions to the model.
- Why this is / is not agent-owned: The lead exercises scope and continuation discretion with the runtime enforcing the selected action.
- Evidence: [coordinator/prompt.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/coordinator/prompt.go), [middleware/async/prompt.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/middleware/async/prompt.go), [middleware/async/tools.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/middleware/async/tools.go#L162-L256), [middleware/async/records.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/middleware/async/records.go).
- Basis: Structural
- Confidence: High
- Caveats: The current view is confined to the assigned coordinator thread. No claim is made for unrelated top-level runs or a distinct whole-team human supervisory mode.
- Whole-system current view: Within the assessed team, list_tasks refreshes the full thread-scoped background task set. The lead also holds its synchronous work and result history.
- Current-control decision scope: Change current commitments through start, update and cancel over the workers assigned to the request, with observed status and outcomes.

## S3* — Complementary audit

- State: —
- Function: Independently challenge operational claims through complementary evidence.
- Disturbance / variety regulated: A worker or lead may report an answer unsupported by actual work.
- Decisive decision or feedback right: No packaged audit-specific primary-evidence judgment path was established.
- Decision owner: None established.
- Supporting / enforcement mechanisms: The coordinator reads reported worker results. The rubric checks the final answer against criteria and can trigger revision.
- Closure path: Rubric feedback returns to the producing run as an answer revision.
- Why this is / is not agent-owned: The standard rubric sees task, criteria and answer. A custom grader or read-only reviewer can add access by supplying external policy and implementation.
- Evidence: [middleware/rubric/rubric.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/middleware/rubric/rubric.go), [middleware/rubric/grader.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/middleware/rubric/grader.go), [coordinator/prompt.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/coordinator/prompt.go), [README.md](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/README.md).
- Basis: Structural
- Confidence: Medium
- Caveats: A configured host can supply a separate source-audit workflow, outside the credited distribution.

### Absence scope

- Surfaces inspected: Coordinator worker return, self-grading middleware, read-only reviewer example, event hooks and evals.
- Plausible first-party paths checked: Rubric running with a separate model, optional subagent reviewer, and diagnostic hooks for audit closure.
- Why no material first-party path remains: The independently invoked evaluator receives the ordinary output, and the example reviewer is host-authored. The package does not bind an independent operational-evidence path with corrective return to this boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: Use external intelligence to choose a prospective capability adaptation for the team.
- Disturbance / variety regulated: Future changes in models, tools, or workload can render the present capability mix unsuitable.
- Decisive decision or feedback right: No shipped future-directed adaptation decision was established.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Provider fallback, model profiles, memory, and web tools support configured execution or task work.
- Closure path: Fallback and model-specific profiles adjust current model use; memory can inform future tasks.
- Why this is / is not agent-owned: Built-in profiles match configured models and fallback handles failures. Neither supplies a loop from external evidence and anticipated conditions to an adaptation choice.
- Evidence: [fallback.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/fallback.go), [middleware/profiles/profiles.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/middleware/profiles/profiles.go), [README.md](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/README.md).
- Basis: Structural
- Confidence: Medium
- Caveats: A host can implement planning around external observations using these components.

### Absence scope

- Surfaces inspected: Fallback providers, matching model profiles, persistent memory and web tools.
- Plausible first-party paths checked: External information fed into future team design, profile selection, or operator capability-planning mode.
- Why no material first-party path remains: The supplied paths support current recovery, static configuration and task-local research. No first-party return of a prospective adaptation judgment to the team's capability was established.

## S5 — Policy and identity

- State: P
- Function: Define the standing mandate and identity for the operator-launched agent or its configured SDK team.
- Disturbance / variety regulated: Possible mandates and role boundaries conflict with the operator's purpose.
- Decisive decision or feedback right: Select the system mandate under which the top-level model and coordinator are commissioned.
- Decision owner: The CLI operator or responsible parent application owner.
- Supporting / enforcement mechanisms: The CLI reads the operator's system prompt file and passes it to the agent constructor. The SDK coordinator accepts a host-owned prompt and worker roles.
- Closure path: At runtime the loaded mandate is assembled into model requests and governs subsequent turns and how the lead commissions workers.
- Boundary reachability: orx exposes the operator-owned mandate file directly. A host can also instantiate the first-party coordinator with its own governing prompt.
- Why this is / is not agent-owned: The agent receives the mandate and works under it. The operator or parent owner chooses the standing purpose before commissioning the run.
- Evidence: [cmd/orx/main.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/cmd/orx/main.go#L231-L272), [coordinator/coordinator.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/coordinator/coordinator.go#L85-L128), [options.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/options.go), [agent/loop.go](https://github.com/aswin-kevin/orchestrix/blob/34447e81f54a605cb780d534d8557573add273a3/agent/loop.go#L374-L405).
- Basis: Structural
- Confidence: Medium
- Caveats: Per-tool approval does not establish S5. The positive claim concerns the first-party channel for assigning the enduring agent or team role.
- Identity / ultimate-policy issue: Which standing role and purpose the commissioned agent or team serves across its user work.
- Ultimate authority in each claimed mode: The launching operator or accountable host sets the mandate. No distinct agent-owned ultimate policy mechanism was established.
- Return-to-operation path: The selected role is loaded into the constructed agent and presented to the model on each run. The model's decisions then execute under that mandate.

## Distributed OSS parent arrangement

The operator or parent application owner acts only at its deployment boundary. Contributor and release governance remain adjacent.

## Self-hosted and non-human modes

Local CLI and host SDK are supported. The configurable lead can control current commitments without the operator choosing every tool step.

## Recursion

The most capable credited operating mode is scoped to one coordinator thread and its supplied working team.

## Variety and escalation

Permissions and approval interrupts control specific tool requests. The coordinator can resolve current assignment trouble through worker instructions, cancel, and follow-up.

## Evidence gaps

Source-only assessment. No live model calls, external services, custom callback implementations or host deployments were exercised.
