---
harness_id: swarm-agent-kit
project_name: Swarm Agent Kit
repository: https://github.com/moseleydev/swarm-kit
review_ref: 56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Swarm Agent Kit

## Review boundary

- System in focus: The installed `swarm-agent-kit` Python API, execution engine and supporting first-party CLI and Studio.
- Purpose and identity: Run one or more tool-capable language-model agents on a user task using a shared run state.
- Relevant environment: Host applications, model providers via LiteLLM, developer-supplied tools and optional storage and approval handlers.
- Standard-distribution boundary: Model-backed single-agent tasks, one-active-agent peer transfer and planner-led execution. Includes supported sync/async, state, persistence hooks, event reporting and read-only Studio.
- Credited operating / distribution surfaces: The packaged Agent and Swarm code, supported execution entry points and shipped event/Studio surfaces.
- Adjacent first-party surfaces excluded from ownership: Contributor workflows, development tests and sample task actors. Tests and examples corroborate runtime paths.
- First-party operating / deployment modes considered: `execute` / `execute_async` and `execute_plan` / `execute_plan_async`, with and without caller-supplied approval and persistence. External hosted systems and application-supplied organizational roles remain outside scope.
- Recursion level: One configured runtime serving application tasks, with named task agents inside it.
- Reviewed revision: `56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The [installed package](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/pyproject.toml) includes a Python API and CLI. `Agent` produces provider messages and normalizes model tool requests. `Swarm` shares one engine for sync and async driving with per-run message history, state and usage. The unsupervised engine switches the single active agent after `transfer`; the supervised engine parses an initial model-authored list of tasks and runs them in order with transfers disabled. Model turns consume tool results and errors. The host can inject persistence and per-call approval callbacks. Studio presents the event log. Sources include the [mode guide](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/docs/guide/modes.md), [engine](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/core/swarm.py), [approval guide](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/docs/guide/tools.md) and [Studio endpoint](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/ui/server.py#L10-L36).

## Operational model

The deployed swarm produces answers and side effects through configured local tools. Distinct role agents can perform different operational tasks, but the runtime gives them turns inside one task session. The model selects target actions and the library executes them. The host supplies business tools, model credentials, limits and callback implementations. The one-shot planner owns task decomposition before agent work begins.

## S1 — Operations

- State: A
- Function: Run tool-backed tasks and return a result for the caller.
- Disturbance / variety regulated: User requests, model outputs, tool data, errors and handoff choices vary within a run.
- Decisive decision or feedback right: Select tools and their arguments, choose the next action after feedback, and return the final answer.
- Decision owner: The model-backed active agent owns ordinary action selection in both execution modes. The application author supplies tools and instructions and owns any separately composed approval decision.
- Supporting / enforcement mechanisms: The shared generator implements the sync/async loop, schema and message handling, result conversion, persistence and limits. The supervised planner assigns work before execution.
- Closure path: Tool outcomes and exceptions enter conversation history. The next model turn observes them and can change course. A text response completes the unsupervised run, with result and available state returned to the caller.
- Boundary reachability: [Package exports and CLI entry](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/pyproject.toml#L38-L58) and the first-party execute methods reach both loops using configured model access and registered Python tools.
- Why this is / is not agent-owned: Without the active model, dispatch and persistence cannot choose the next task action. Agent ownership is claimed for ordinary operational discretion, not authority to override an approval denial.
- Evidence: [Agent model response and provider calls](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/core/agent.py#L171-L212), [Tool feedback and unsupervised loop](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/core/swarm.py#L396-L461), [Supervised task loop](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/core/swarm.py#L514-L565), [Tool feedback tests](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/tests/test_swarm.py#L74-L138)
- Basis: explicit
- Confidence: High
- Caveats: Provider quality and caller-authored tools vary. This is a source and test-code assessment.

## S2 — Coordination

- State: —
- Function: Attenuate interference among distinct operational units.
- Disturbance / variety regulated: Potential competing handoffs and shared-state writes between named task agents, and state contamination among independent sessions.
- Decisive decision or feedback right: No shipped decision path for resolving a concrete conflict between peer work commitments.
- Decision owner: Models select transfer targets. The runtime executes dispatch and enforces the plan sequence. The caller owns external shared-state policy.
- Supporting / enforcement mechanisms: A single active peer per run, ordered execution and optional distinct session history/state.
- Closure path: A successful transfer replaces the active agent and feeds task history forward. The transfer mechanism does not arbitrate simultaneous peer commitments or competing writes.
- Why this is / is not agent-owned: Transfer is model-owned operational routing. Per-session state namespaces partition independent callers and the examples rely on caller-supplied load/save functions.
- Evidence: [Transfer and next-agent selection](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/core/swarm.py#L362-L459), [Supervised sequence](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/core/swarm.py#L514-L566), [Persistence modes](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/docs/guide/persistence.md), [Async isolation fixture](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/tests/test_swarm.py#L167-L189)
- Basis: structural
- Confidence: High
- Caveats: A host can define conflict rules over its application state.

### Absence scope

- Surfaces inspected: Peer and supervised engines, state/persistence hooks, mode guide, async isolation and concurrent-tool tests.
- Plausible first-party paths checked: A repeated transfer could oscillate. The run cap stops the whole run and a target check rejects invalid/self transfer. In planned mode fixed sequencing removes handoff. Session tests check independent histories rather than arbitration over shared work.
- Why no material first-party path remains: Neither loop supplies inter-unit monitoring, negotiated adjustment, ownership claims, or feedback from conflict resolution. Independent session partitioning and one active peer are execution constraints within the assessed modes.

## S3 — Inside-and-now control

- State: —
- Function: Regulate current shared resources and commitments on behalf of the swarm as a whole.
- Disturbance / variety regulated: A live run can overrun its limits, choose an approval-gated tool, or end a planned task without success.
- Decisive decision or feedback right: No first-party system-level decision about revising current work, shared resources or priorities from a current whole-system view.
- Decision owner: The planner makes an initial task sequence. Caller code sets limits and optionally supplies the person or policy deciding individual tool approval.
- Supporting / enforcement mechanisms: Turn caps, token metering, per-call approval callback, structured events and a log viewer.
- Closure path: A callback decision can execute or deny the current call and feeds a result to the active agent. The supervised engine walks the original plan and offers no first-party decision loop over its live commitments.
- Why this is / is not agent-owned: Initial assignment, logging, fixed limits and one-call vetoes leave whole-swarm live regulation unconstructed.
- Evidence: [Pre-run planner and executor](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/core/swarm.py#L464-L565), [Tool approval and feedback](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/core/swarm.py#L396-L426), [Approval contract](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/docs/guide/tools.md#L115-L167), [Studio log endpoint](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/ui/server.py#L10-L36)
- Basis: structural
- Confidence: High
- Caveats: A host could consume events and add its own supervisory decision path.

### Absence scope

- Surfaces inspected: Planner and execution engines, approval callback, event API, Studio log endpoint, and approval tests.
- Plausible first-party paths checked: Planner replanning after intermediate results, changing live limits or work through Studio, and whether approval rejection updates the shared plan.
- Why no material first-party path remains: The planner is invoked before agents run, Studio returns log data, and the approval contract governs a single requested tool call. These paths do not compose a shipped whole-swarm reallocation or intervention loop.

## S3* — Complementary audit

- State: —
- Function: Independently challenge claims about operational results and return findings into control.
- Disturbance / variety regulated: An agent's task summary or recorded tool response could miss an error in the external work.
- Decisive decision or feedback right: No first-party audit judgment with complementary access and a corrective return path.
- Decision owner: The running agents and runtime generate events. Studio reads those events. A developer could introduce a separate reviewer and its evidence access.
- Supporting / enforcement mechanisms: Event callback, JSONL log and dashboard; configured sequential reviewers run as ordinary task agents.
- Closure path: No shipped path from an independent check to corrective swarm action.
- Why this is / is not agent-owned: The log viewer reads routine reports. A possible reviewer configured as another task in the plan must obtain independent inputs and corrective authority from the application.
- Evidence: [Observability guide](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/docs/guide/observability.md), [Studio read-only log surface](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/ui/server.py#L10-L36), [Agent loop and supervised execution](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/core/swarm.py#L396-L565)
- Basis: structural
- Confidence: High
- Caveats: Repository tests probe the implementation outside the assessed distribution.

### Absence scope

- Surfaces inspected: Event production and Studio reader, callback API, supervised example and engine, and package tests.
- Plausible first-party paths checked: Whether Studio cross-checks external ground truth, an ordinary editor step has distinct evidence/independence, or run history triggers independent inspection.
- Why no material first-party path remains: Studio presents the same run log and the executor gives planned agents run history and configured tools. The shipped code supplies no independent evidence boundary or audit-to-correction function.

## S4 — Outside-and-then intelligence

- State: —
- Function: Develop options for future operating capability using external distinctions.
- Disturbance / variety regulated: Providers, external tasks and tool capabilities may change between runs.
- Decisive decision or feedback right: No first-party option selection or capability adaptation loop.
- Decision owner: Caller supplies or changes provider, agent and tool configuration. The agent owns current-task actions.
- Supporting / enforcement mechanisms: Provider settings/retries, planning entry points, state and persistence hooks.
- Closure path: Persistent context can affect later task execution. No shipped path turns evidence about future environment or capability into an adopted adaptation.
- Why this is / is not agent-owned: The pre-run planner decomposes a submitted task and executor feedback remains within the operational loop.
- Evidence: [Execution modes](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/docs/guide/modes.md), [Provider configuration](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/docs/guide/providers.md), [Persistence](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/docs/guide/persistence.md), [Planner/worker loop](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/core/swarm.py#L464-L565)
- Basis: structural
- Confidence: High
- Caveats: Custom tools could gather external research and custom clients could apply it.

### Absence scope

- Surfaces inspected: Planner, model-provider configuration, state/persistence and event surfaces, and repository documentation.
- Plausible first-party paths checked: Whether persistent state generates adaptation options, planner evaluates future scenarios, or provider retry selects a new operating capability.
- Why no material first-party path remains: The shipped plan and state mechanisms support task execution. No documented first-party actor links prospective external evidence to a decision changing what the installed swarm can do.

## S5 — Policy and identity

- State: —
- Function: Stabilize swarm identity and resolve ultimate-policy questions at the assessed recursion.
- Disturbance / variety regulated: Deployed task agents have configured roles and may request actions that exceed a configured operating permission.
- Decisive decision or feedback right: No operative path for escalating, choosing and returning an identity or ultimate-policy decision.
- Decision owner: The host author sets instructions, tool exposure and approval configuration. Callback owners decide individual calls.
- Supporting / enforcement mechanisms: Agent instructions, tool declarations and a caller-provided approval callback enforced by the runtime.
- Closure path: Instructions shape requests and approval decisions affect the requested action only. No shipped mechanism returns an authoritative policy ruling governing later runs.
- Why this is / is not agent-owned: A caller can edit prompts or approve a tool request. Neither path establishes a function-specific policy decision procedure in this runtime.
- Evidence: [Agent configuration](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/docs/guide/agents.md), [Approval scope](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/docs/guide/tools.md#L115-L167), [Approval dispatch](https://github.com/moseleydev/swarm-kit/blob/56cc87688feaaa4ac9ded2e5ee65b7e7ceeb34cb/src/swarm_kit/core/swarm.py#L396-L426)
- Basis: structural
- Confidence: High
- Caveats: Repository maintenance decisions belong to the adjacent project boundary.

### Absence scope

- Surfaces inspected: Agent and swarm configuration, approval hook, starter CLI, Studio and contributor-facing project surfaces.
- Plausible first-party paths checked: Whether a rejected call triggers a decision over the operating mandate, and whether configuration or Studio exposes a returned identity-policy decision.
- Why no material first-party path remains: The first-party hook takes one tool request, and Studio is observational. Host setup sets starting constraints. No designated actor or returned policy decision is shipped for the deployed swarm.

## Recursion

Agent roles can represent distinct operational work, such as triage and billing, inside the configured task swarm. The first-party handoff changes which agent acts. There is no evidence of separately viable nested organizational systems at this boundary.

## Variety and escalation

Models handle local task variation through tool use, handoffs and feedback. A host-configured gate can request a positive decision for an individual tool call. An error is returned to the model for bounded operational recovery. Turn caps and persistence support the task loop. The source supplies no separate whole-system exceptional channel.

## Evidence gaps

This review reads the pinned runtime, documentation and test code. Live model calls, external storage, and particular caller implementations were outside the reviewed evidence. The scope is the packaged operating modes, so hypothetical application composition does not supply a missing first-party function.

