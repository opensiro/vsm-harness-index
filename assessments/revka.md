---
harness_id: revka
project_name: Revka
repository: https://github.com/KumihoIO/Revka
review_ref: a1acd826502e12a6c2f3d147e488a7d2982c480b
reviewed_at: 2026-10-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Revka

## Review boundary

- System in focus: A supported, configured first-party Revka application combining its Rust agent loop / gateway / daemon, Python `operator-mcp` workflow executor and optional supervisor agent pattern, deployed under explicit user workflow definitions and tools. The assessed recursion is an individual agent/workflow application, **not** the external Kumiho Cloud or Community Edition graph-server organization, the Revka OSS contributor team, or a hypothetical cluster of separate adopters.
- Purpose and identity: Execute model-directed user work and declared multistep agent workflows, with deterministic DAG admission/execution, human approval, bounded task costs, retries, checkpoint-resume, agent delegation, typed provenance and event-triggered chained workflows.
- Relevant environment: Prompts, provider responses, actual tool results, agent subprocess status, workflow node results, deadlines, cost budgets, Kumiho revision/tag events, user approval responses, configured trust records and external graph service availability.
- Standard-distribution boundary: Pinned `src/agent/loop_.rs`, Rust security/approval/trust and CLI/gateway, shipped `operator-mcp/operator_mcp/workflow` executor/validation/event listener, shipped `patterns/supervisor.py`, policy hooks and optional Kumiho client integration. Graph-store server implementation is **outside this repository**, even when the integration with its external API is visible. External Claude/Codex providers and private R&D or business operator rights are excluded.
- Credited operating / distribution surfaces: [src/agent/loop_.rs](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/src/agent/loop_.rs#L3773), [src/agent/loop_.rs](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/src/agent/loop_.rs#L4880), [src/agent/tool_execution.rs](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/src/agent/tool_execution.rs#L1), [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L1392), [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L5770), [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L6000), [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L6423), [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L6539), [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L6756), [operator-mcp/operator_mcp/workflow/validator.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/validator.py#L1), [operator-mcp/operator_mcp/workflow/event_listener.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/event_listener.py#L172), [operator-mcp/operator_mcp/workflow/event_listener.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/event_listener.py#L234), [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L190), [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L238), [operator-mcp/operator_mcp/workflow/kumiho_mutation.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/kumiho_mutation.py#L185).
- Adjacent first-party surfaces excluded from ownership: Project-authored YAML samples, bundled marketing claims and UI illustrations, source-vs-runtime descriptions of Kumiho graph functions, simulated tests, external hosted API/node infrastructure, model providers' cognitive decisions and separately supplied user organizational policy. Merely appearing on a dashboard does not grant a new VSM S-function decision right.
- First-party operating / deployment modes considered: Rust `run` and `process_message` model-tool-action loop; Python workflow DAG with agent, shell, Python, parallel/for_each/conditional/goto/loop, supervisor/group_chat/handoff, human approval and input, retries/cost guard, Kumiho patch/bundle interactions, checkpoints, entity revision triggers and local trust-informed delegation.
- Recursion level: A configured operational task/workflow, potentially spawning agents that are local task-operating units. The supervisor tool and event listener are workflow execution auxiliaries; they do not automatically form an enduring parent-level viable organization across diverse independently viable S1 cells.
- Reviewed revision: `a1acd826502e12a6c2f3d147e488a7d2982c480b`, exactly frozen by candidate intake #202 and batch #1669.
- Observation date: 2026-10-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Rust agent entry points `run` and `process_message` assemble configured memory, security and approval, provider routing, and executable tools; normal task iteration uses model response, real tool call and result feedback to continue or return a final response. Python Operator adds a distinct public orchestration layer with declarative typed workflow steps. `execute_workflow` validates DAG dependencies and variable references before execution, resumes selected checkpoints, tracks pending/running/completed node states, enforces cost/time/cancellation limits, executes registered step handlers and persists workflow outcomes. Workflow agent steps call configured subprocess agents and can enforce declared structured outputs. These are supported first-party operational paths, with external model/process dependencies explicitly bounded. [src/agent/loop_.rs](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/src/agent/loop_.rs#L3773), [src/agent/loop_.rs](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/src/agent/loop_.rs#L4880), [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L1392), [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L5770), [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L5970), [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L6423), [operator-mcp/operator_mcp/workflow/validator.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/validator.py#L1).

The first-party `tool_supervisor_run` pattern is a real model-directed task decomposition loop: each iteration runs a supervisor agent, parses one decision of `DELEGATE`, `COMPLETE` or `REQUEST_INFO`, invokes a chosen specialist under policy preflight, collects its result in work history and may use a Kumiho trust score in candidate selection. A typed workflow `supervisor` step bridges this operator pattern to `execute_workflow`. This is a task-scoped manager/specialist interaction: it can decide the **next task operation**, but does not thereby administer independent ongoing S1 portfolios/resources at the whole-system recursion. [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L22), [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L100), [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L159), [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L180), [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L239), [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L4862).

The event listener can watch `revision.tagged` data and trigger matching declared downstream workflows; singleton file locking and seen-event bookkeeping avoid duplicate executors. The executor can update Kumiho bundle/patch state and preserve run provenance. Rust security and approval and Python `human_approval` pause risky actions for an **external** decision; cost caps and step schema verification are enforceable execution constraints. These are significant graph/evidence infrastructure but not automatically independent VSM complementary audit or future-viability decision authority. The graph server's own internal policy and durability are not reviewed as first-party Revka logic. [operator-mcp/operator_mcp/workflow/event_listener.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/event_listener.py#L1), [operator-mcp/operator_mcp/workflow/event_listener.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/event_listener.py#L90), [operator-mcp/operator_mcp/workflow/event_listener.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/event_listener.py#L234), [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L5304), [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L6756), [operator-mcp/operator_mcp/workflow/kumiho_mutation.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/kumiho_mutation.py#L185), [WORKFLOWS.md](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/WORKFLOWS.md#L1).

## Operational model

A task arrives at the model-backed runtime or at a validated workflow definition. Revka may choose tools and delegate current task subtasks under bounded policy, collect actual outcomes, and adapt its continuing operations. Other first-party components sequence workflows, enforce configured approvals, track evidence and trigger later workflows when externally maintained graph tags change. Assessment distinguishes *technical reliability of an individual workflow* from independent organizational S2 damping, S3 current management, S3* complementary reality checks, S4 prospective strategy and S5 legitimate purpose ownership.

## S1 — Operations

- State: A
- Function: Perform user-authorized current work with model-selected tool execution and adaptive, result-informed specialist delegation in supported runtime/Operator modes.
- Disturbance / variety regulated: Unstructured user requests, tool/output errors, differing provider responses, changing files/services, subtask findings and retry/recovery needs.
- Decisive decision or feedback right: The installed Rust agent can choose registered tool actions from model responses and inspect tool results; the optional Python supervisor model chooses DELEGATE/COMPLETE/REQUEST_INFO and specialist per current observed work history, bounded by process policy.
- Decision owner: Configured model-backed Revka task agent and optional supervisor/task pattern under first-party Rust/Python execution code. External provider supplies semantic inference; user policy, approvals, tool configuration and constraints bound execution.
- Supporting / enforcement mechanisms: Runtime tools/provider routing, SecurityPolicy, approval manager, operator agent pool, supervisor action parser, persisted execution results, workflow retries, structured output and checkpoint state.
- Closure path: Input → Rust/Operator agent prompt → model-chosen tool/subtask → first-party executable handler/subprocess/tool → actual result/error → recorded history/next supervisor or model request → next work decision or completed response.
- Boundary reachability: Shipped Rust `run`/`process_message` invoke production tool initialization and provider setup; `tool_supervisor_run` is exported through workflow `_exec_supervisor` and dispatches real specialist subprocesses. No test-only or hypothetical first-party path needed for the claimed supported mode.
- Why this is / is not agent-owned: Current task actions change based on model judgments and returned observations. DAG validator, deterministic route selection and audit logging are important enforcement, but do not themselves supply the discretionary S1 right.
- Evidence: [src/agent/loop_.rs](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/src/agent/loop_.rs#L3773); [src/agent/loop_.rs](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/src/agent/loop_.rs#L4880); [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L22); [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L190); [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L239); [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L4862); [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L1392).
- Basis: Explicit first-party code-reachable feedback and model-driven supervisor delegation; model/provider runtime itself not tested live.
- Confidence: High structural, medium for untested external tool/model behavior.
- Caveats: Some configured YAML-only workflows are deterministic and do not include discretionary model-backed actions. Positive S1=A is for supported installed agent/supervisor modes, not every workflow graph.

## S2 — Coordination

- State: —
- Function: No distinct conflict-sensitive regulation loop between independently viable S1 operating units was established by shipped orchestration at this recursion.
- Disturbance / variety regulated: Multiple delegated agents, parallel DAG branches, duplicated event triggers or conflicting Kumiho mutations can interfere, but the inspected controls are task dependency/order guards and technical duplicate prevention.
- Decisive decision or feedback right: Parallel joining, `depends_on`, singleton trigger lock, stage retries and delegation choose execution order/protect shared run state. No shipped evaluator observes a particular inter-S1 operating conflict and chooses reciprocal corrective regulation over multiple viable units.
- Decision owner: Per-workflow scheduler/validator, developer-specified dependencies, event-listener technical leader lock and task supervisor; no separately assigned S2 disturbance-control actor.
- Supporting / enforcement mechanisms: Topological workflow validation, node state, cost/timeout/cancel guards, parallel branches, retry limits, event seen-cache/lock, external graph revision/provenance.
- Closure path: Declared task graph → scheduled ready nodes → result/checkpoint/next node. Missing observed reciprocal inter-operating-unit interference → adaptive stabilization choice → binding changed operations on those separate units.
- Why this is / is not agent-owned: Preventing duplicate trigger listeners or enforcing a declared DAG is infrastructure concurrency control; these are not independent VSM S2 actions over ongoing viable S1 organizations.
- Evidence: [operator-mcp/operator_mcp/workflow/validator.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/validator.py#L1); [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L5770); [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L6000); [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L6539); [operator-mcp/operator_mcp/workflow/event_listener.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/event_listener.py#L90); [operator-mcp/operator_mcp/workflow/event_listener.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/event_listener.py#L234).
- Basis: Bounded negative after checking strongest cross-agent, parallel, and duplication candidates.
- Confidence: Medium-high within first-party pinned sources.
- Caveats: An adopter can implement domain-specific S2 policies as workflows; not evidenced as built-in governing relation.

### Absence scope

- Surfaces inspected: Operator DAG validator/scheduler, parallel/for_each, supervisor/group_chat/handoff, event listener lock/dedup, versioned graph write paths and runtime policy.
- Plausible first-party paths checked: Cross-agent task interference, parallel result conflicts, event duplicate regulation, graph mutation conflict resolution, shared worker/resource capacity.
- Why no material first-party path remains: Actual first-party rules are per-workflow dependency, dispatch, lock or fail/retry mechanics; no source-closed S2 actor owns a specific sensed disturbance and reciprocal corrective return between independent viable S1 units.

## S3 — Inside-and-now control

- State: —
- Function: No accountable whole-current organizational control owner resolves obligations/resources/priorities across independent operating divisions.
- Disturbance / variety regulated: Cross-workflow backlog, costs, priority, agent availability, conflicts among goals and external commitments; single-run limits are explicit but do not constitute an enduring whole-current organization.
- Decisive decision or feedback right: Task Supervisor chooses next specialist; workflow executor gates cost/timeout/cancel; human approval controls a single pending node. None has whole-current legitimate binding allocation rights across multiple distinct S1 missions.
- Decision owner: Workflow/task operator and external human/policy configurator, not a packaged parent S3 decision holder overseeing an independent multi-unit portfolio.
- Supporting / enforcement mechanisms: Task history, workflow run-state, checkpoints/resume, cost guards, trust scores, reactive triggers, node/agent pool status and dashboard.
- Closure path: Current workflow reads results and continues/cancels; missing global running-operations obligations → explicit cross-unit current judgment → enforced return changing independent S1 commitments/resource deployment.
- Why this is / is not agent-owned: A system called Operator with retries, multiple agent types and an LLM supervisor still owns the present **task workflow** unless system-wide obligation/control closure is shown.
- Evidence: [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L180); [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L239); [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L5304); [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L5770); [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L6000); [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L6756).
- Basis: Bounded negative after inspecting supervisor, scheduling, cost guard, approval and external control plane.
- Confidence: Medium-high for the declared application recursion.
- Caveats: The adopter's broader business could own S3 externally, without being an exercised right of Revka's open-source runtime.

### Absence scope

- Surfaces inspected: Rust process/daemon agent, Operator supervisor and workflow DAG, run/cost policy, event listener/reactive runs, approval, dashboard and Kumiho graph APIs.
- Plausible first-party paths checked: Trust-score-driven delegation as whole-current management, workflow cost guard as resource allocation, supervisor as parent operations manager, multi-run status/approval and policy configuration.
- Why no material first-party path remains: Decisions are constrained to individual current task/delegated worker or developer-authored run policy. There is no native system-wide current management choice returned to independently governed operating units.

## S3* — Complementary audit

- State: —
- Function: No independently sourced complementary audit challenges current S3 claims and returns an enforceable corrective management intervention.
- Disturbance / variety regulated: Incorrect agent work, unreliable outputs, integrity faults, untrusted tool outcomes and possible policy breaches; first-party validation and provenance mechanisms can detect/report some anomalies.
- Decisive decision or feedback right: Structured `output_fields` fails malformed tasks; evidence graph/RunLog/audit SHA chain supports trace integrity, trust records inform later delegation, and approvals gate a step. No separate reviewer with independent operational fact access and S3 corrective return is evidenced.
- Decision owner: Workflow validator, Rust logging/security, optional verifier/approval in step definition, externally authoring human and graph service; not an independent organizational S3* holder.
- Supporting / enforcement mechanisms: Output field validation, SHA-256 evidence log, provenance graph edges, approval gates, trust score, graph patch preconditions, RunLog and checksums.
- Closure path: Task execution → trace/structured validation or approval → fail, pause or resume this workflow. Missing independent direct observations of S3-reported operations → challenge → authorized S3 management correction returned across operating units.
- Why this is / is not agent-owned: Provenance and cryptographic integrity can certify an event log's consistency without verifying the real-world truth of an agent's operational claim. Trust-based task routing does not become a complementary independent management audit.
- Evidence: [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L1331); [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L1392); [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L6756); [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L159); [operator-mcp/operator_mcp/workflow/kumiho_mutation.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/kumiho_mutation.py#L488); [README.md](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/README.md#L24).
- Basis: Strongest evidence, guardrails, approval and trust-record candidates inspected, bounded negative.
- Confidence: Medium; no first-party S3 corrective audit closure demonstrated at this recursion.
- Caveats: Future/enterprise configurations could wire independent verifier evidence to actual governance, which would be a different assessment boundary.

### Absence scope

- Surfaces inspected: Operator output-field contract, Rust evidence/logger descriptions, trust records, workflow handoff and agent-run statuses, approval/human_input and Kumiho revision/patch path.
- Plausible first-party paths checked: Hash-chain tamper detection, independent audit source versus model output, trust downgrade causing deployment change, human/reviewer exception and controlled retry.
- Why no material first-party path remains: Reviewed mechanisms validate task schema/provenance, authorize individual work or condition next selection; none independently tests whole-current management reporting and sends a binding corrective control decision to S3/S1.

## S4 — Outside-and-then intelligence

- State: —
- Function: No integrated prospective outside-environment intelligence selects and admits changed organizational capabilities into future operating practice.
- Disturbance / variety regulated: New Kumiho revisions, updated knowledge and agent trust performance can affect later workflows and delegation, but these are reactive task/routing data rather than authorized future strategy.
- Decisive decision or feedback right: Event listener fires developer-configured workflows on tagged revisions; supervisor can consider task performance/trust and choose next specialist. Workflow definitions and durable graph/mutation policies are provided by humans, not an independently empowered S4 actor choosing long-horizon organizational adaptation.
- Decision owner: Externally configured trigger rules and policy, trust-informed current-task delegator, human writer of workflow topology or approval decision.
- Supporting / enforcement mechanisms: revision.tagged registry, event listener/pollers, graph version metadata, Kumiho bundle/patch APIs, optional trust score, skill references and workflow YAML versioning.
- Closure path: New revision tag → matching downstream predeclared workflow or changed knowledge/trust hint; missing prospective environmental alternatives → system-wide viable option selection/admission → lasting capability/topology change explicitly adopted into future work.
- Why this is / is not agent-owned: Reactive chaining and task-level selection can make a system adaptive to data events, but do not themselves demonstrate an owner who chooses future viability strategies and binds changed organizational capability.
- Evidence: [operator-mcp/operator_mcp/workflow/event_listener.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/event_listener.py#L1); [operator-mcp/operator_mcp/workflow/event_listener.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/event_listener.py#L90); [operator-mcp/operator_mcp/workflow/event_listener.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/event_listener.py#L172); [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L159); [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L2964); [operator-mcp/operator_mcp/workflow/kumiho_mutation.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/kumiho_mutation.py#L185).
- Basis: Tests product's strongest reactive-graph and trust/adaptation claims against S4 decision/return contract.
- Confidence: Medium-high for shipped app paths, limited for external Kumiho server internals.
- Caveats: Graph mutation and workflow authoring tools could support a separately mandated S4 workflow; this assessment does not invent such authority or borrow it from user-configured YAML.

### Absence scope

- Surfaces inspected: Tag-driven workflow triggers, graph revision/patch/bundle update, trust-score lookup, supervisor pattern, skills, workflow version/config and reactive polling.
- Plausible first-party paths checked: Continuous improvement after recorded outcomes, future strategy inference, trusted agent portfolio evolution, autonomous workflow redesign or skill promotion on new evidence.
- Why no material first-party path remains: Triggers run existing human-defined workflows; supervisor chooses next delegate for a task. No installed prospective options owner/decision mandate plus accepted durable capability redesign is returned.

## S5 — Policy and identity

- State: —
- Function: No final legitimate organization-wide purpose/identity arbitration body is installed in Revka's first-party runtime.
- Disturbance / variety regulated: Autonomy/security settings, allowed tools, risk approval, task identity and workflow validation; these constrain local operations rather than deciding ultimate mission legitimacy.
- Decisive decision or feedback right: `SecurityPolicy::from_config`, operator policy.preflight_spawn and human_approval gate individual execution. Legitimate policy goals/workflow identity are set by external developer/operator, with no built-in final value conflict adjudication and binding organization-wide return.
- Decision owner: Human operator and static policy configuration, first-party enforcement mechanism at step/tool boundary; no packaged S5 identity/purpose governor.
- Supporting / enforcement mechanisms: Rust SecurityPolicy, ApprovalManager, operator policy, YAML workflow identity/version, verifiable intent and credentials, audit logs.
- Closure path: Configured rule/approval → block/allow current action; missing ultimate purpose question and legitimate S5 adjudication → authoritative changed system objective/policy → binding return into all governed divisions.
- Why this is / is not agent-owned: Human authorization of one risky action and tool-deny conditions demonstrate scope/security, not final governing purpose or identity of an independently viable organization.
- Evidence: [src/agent/loop_.rs](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/src/agent/loop_.rs#L3773); [src/agent/loop_.rs](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/src/agent/loop_.rs#L4880); [operator-mcp/operator_mcp/patterns/supervisor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/patterns/supervisor.py#L239); [operator-mcp/operator_mcp/workflow/executor.py](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/operator-mcp/operator_mcp/workflow/executor.py#L6756); [src/approval/mod.rs](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/src/approval/mod.rs#L1); [src/security/mod.rs](https://github.com/KumihoIO/Revka/blob/a1acd826502e12a6c2f3d147e488a7d2982c480b/src/security/mod.rs#L1).
- Basis: First-party policy and approval decision rights inspected, bounded negative.
- Confidence: Medium-high at app scope.
- Caveats: A real organization or separate Kumiho control plane may supply S5 externally; that authority must not be imported without actual first-party governed return evidence.

### Absence scope

- Surfaces inspected: Runtime SecurityPolicy and approval configuration, Operator spawn preflight, workflow YAML validation, immutable graph revision descriptions, verifiable-intent and human gate APIs.
- Plausible first-party paths checked: Policy constraints as final authority, auth/trust identity scores, signed intent as legitimate mission arbitration, externally supplied human approval as S5.
- Why no material first-party path remains: Every source-closed action is current authorization/config enforcement or external human input; no first-party ultimate system purpose/policy revision owner closes the loop.


## Distributed OSS parent arrangement

Revka Rust runtime, Python Operator, the Kumiho client, Kumiho Cloud/CE external graph backend, external model providers, user's organization and actual human approver are distinct systems/owners. The repo uses dual **MIT OR Apache-2.0** source licenses (`LICENSE-MIT`, `LICENSE-APACHE`) but the public graph-server's code is not included here. External approval and developer-authored YAML are not automatically parent-governed S3/S4/S5 authority.

## Self-hosted and non-human modes

First-party Rust/Operator components can be hosted and executed with user-configured model providers and local configuration. Some persistent graph/evidence/trust features require a separately provided external Kumiho server (Cloud or prebuilt CE). The first-party event listener and graph-facing API are reviewed, not uninspected graph-server policy/durability logic. No remote inference, persistent server account, real approval event, fleet runtime or production evidence chain was executed in this assessment.

## Recursion

A supervised workflow can spawn specialists and route results; individual specialists may own real task S1 choices. Across multiple workflows, dependency scheduling, run-state tracking and event-triggered chaining do not constitute a demonstrated higher-recursion organization with independent S2–S5 decisions. A full business control plane beyond the packaged code would need separately evidenced mandate, owner, observation and return.

## Variety and escalation

Structured output contracts and DAG validation reject malformed plans; Rust tool policy, auth/approval, run cost/time and retry/cancel reduce harmful operational variety. Trust-informed supervisor choices and reactive version events can change which task work runs next; a hash-chain audit supports retrospective traceability. These are meaningful enforcement, guardrail and adaptation infrastructure but are not automatically a viable-system complementary audit, strategic future capability selection or final policy authority.

## Evidence gaps

- Positive S1 derives from first-party Rust agent loop and optional Python LLM supervisor with actual subprocess delegation; deterministic YAML-only workflows do not automatically meet model-directed S1 autonomy.
- Multiple real coordination guards, singleton trigger lock, trust scores and structured output failure handling were inspected. No sampled source supplied an S2 feedback loop about an observed **inter-viable-S1** disturbance, despite valid technical scheduling and contention prevention.
- No independent management-audit corrective loop is proven merely by tamper-evident provenance, task-schema verification and human approval. External Kumiho server behavior and organizational legitimacy are beyond source boundaries.
- Event listener can trigger predeclared downstream workflows from revision tags; without a first-party prospective future-viability judgment and accepted capability modification, source supports event-driven reactivity rather than S4.
- Dual MIT/Apache-2.0 applies to this repo's code; related Kumiho server code is not included. Source-first review only; no live model/provider, human approval, external Kumiho API or full Rust/Python integration/E2E suite was executed. Index validation cannot establish production performance or governance authority.
