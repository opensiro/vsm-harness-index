---
harness_id: librecode
project_name: LibreCode
repository: https://github.com/omarluq/librecode
review_ref: 1e7ba321306bc5e01a58f4ee9c53f18178f2cb96
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# LibreCode

## Review boundary

- System in focus: Installed LibreCode terminal and runtime, including its shipped task and workflow services.
- Purpose and identity: Perform coding and inspection tasks with model-selected tools and durable delegation.
- Relevant environment: Local workspace, provider integration, project configuration, and the terminal operator.
- Standard-distribution boundary: Native chat loop, built-in roles, durable subagent and workflow services, and terminal control surfaces.
- Credited operating / distribution surfaces: The local provider/tool loop, bundled explore and general roles, subagent and workflow state and control, and terminal task views.
- Adjacent first-party surfaces excluded from ownership: Examples, release CI, and user-authored extensions or workflow programs as independent sources of organization.
- First-party operating / deployment modes considered: Direct user chat, model-directed asynchronous delegation, and terminal operation with configured workflow support.
- Recursion level: One owning chat session and its portfolio of child tasks or workflows.
- Reviewed revision: `1e7ba321306bc5e01a58f4ee9c53f18178f2cb96`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Provider adapters execute native model/tool loops. Model-visible tools can launch, inspect, wait for or cancel persistent child tasks. A SQLite-backed scheduler restores queued work and preserves transcripts. The MVM workflow host exposes a narrow API for script-authored temporal structure. The terminal operator can inspect and cancel workflow commitments. [`README.md`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/README.md#L297-L311), [`internal/provider/anthropic.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/provider/anthropic.go#L49-L104), [`internal/assistant/agent_tool.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/assistant/agent_tool.go#L179-L342), [`internal/workflow/service.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/workflow/service.go#L335-L415), [`internal/terminal/workflows.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/terminal/workflows.go#L113-L234).

## Operational model

The root and its selected child roles produce inspected or changed project artifacts. The root model chooses child commitments from status and results. The local operator owns active workflow oversight. Profiles assign capabilities to roles and the scheduler enforces runtime execution limits.

## S1 — Operations

- State: A
- Function: Carry out repository investigation or coding.
- Disturbance / variety regulated: Tasks differ in relevant files, allowed tools and observed results.
- Decisive decision or feedback right: Choose a tool, arguments and subsequent actions after results.
- Decision owner: The model behind the root or shipped child role.
- Supporting / enforcement mechanisms: Provider adapters, role settings, tool registry, and durable transcript.
- Closure path: Tool output is returned as conversation content, shaping the next model action and final response.
- Why this is / is not agent-owned: Removing the model leaves dispatch code without a discretionary coder or explorer.
- Evidence: [`internal/provider/anthropic.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/provider/anthropic.go#L49-L104), [`internal/provider/tool_loop.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/provider/tool_loop.go#L43-L76), [`internal/agenttask/runtime_runner.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/agenttask/runtime_runner.go#L47-L98), [`README.md`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/README.md#L297-L311).
- Basis: structural
- Confidence: High
- Caveats: A writable child depends on the configured profile.
- Boundary reachability: The installed client reaches native provider tool loops and built-in explore and general roles through supported session entry points.

## S2 — Coordination

- State: —
- Function: Dampen interference among distinct live operational units.
- Disturbance / variety regulated: Independent child agents could contend over one workspace or limited concurrency.
- Decisive decision or feedback right: No first-party mechanism selects a response to concrete overlapping task scopes.
- Decision owner: The caller or workflow author sets the assignments; the scheduler enforces configured limits.
- Supporting / enforcement mechanisms: Agent task session isolation, bounded workers, and sequencing primitives.
- Closure path: A generic scheduler defers work when a slot is full. It does not route a work-scope collision back to peers.
- Why this is / is not agent-owned: Independent scheduling and order composition do not supply conflict-specific coordination judgment.
- Evidence: [`internal/agenttask/service.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/agenttask/service.go#L707-L817), [`internal/workflow/workflow.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/workflow/workflow.go#L65-L116), [`internal/workflowkernel/combinator.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/workflowkernel/combinator.go), [`README.md`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/README.md#L297-L311).
- Basis: structural
- Confidence: High
- Caveats: An independently authored workflow can supply a conflict policy.

### Absence scope

- Surfaces inspected: Agent task service, isolation and per-session slots, workflow controller and combinators.
- Plausible first-party paths checked: Checked concurrent mutating child tasks, queue deferral and user-authored workflow plans.
- Why no material first-party path remains: First-party paths bound concurrency or execute caller-defined relationships. They do not detect or correct conflicting work commitments across agents.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate current child or workflow commitments across the owning session.
- Disturbance / variety regulated: Parallel or durable work can become unnecessary, stalled or in need of replacement.
- Decisive decision or feedback right: Inspect currently active commitments and select which work to start, continue waiting for, or cancel.
- Decision owner: The root model controls its child portfolio. The responsible terminal operator can decide which current workflow remains active.
- Supporting / enforcement mechanisms: Owner-scoped task list, durable status, panel, scheduler and descendant cancellation.
- Closure path: Model-triggered cancellation changes child state. Terminal workflow cancellation cascades through the workflow controller and returns its disposition.
- Why this is / is not agent-owned: The respective actor selects a commitment to stop or replace. Cancellation APIs enforce that choice.
- Evidence: [`internal/assistant/agent_tool.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/assistant/agent_tool.go#L179-L342), [`internal/agenttask/service.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/agenttask/service.go#L512-L603), [`internal/terminal/workflows.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/terminal/workflows.go#L96-L234), [`internal/workflow/service.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/workflow/service.go#L335-L413).
- Basis: structural
- Confidence: High
- Caveats: The two modes operate in supported subsets of the same ownership scope. This does not imply authority over other sessions.
- Boundary reachability: The root registers the model-visible agent controls, and the terminal's workflows panel is wired to the shipped service.
- Whole-system current view: The model can list status across its own children. The operator's session view lists active workflows and shows their child execution details.
- Current-control decision scope: Decide which existing child commitments or whole workflow groups to stop, and in the model mode initiate alternate tasks.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Root model | Current child-task state calls for a change | The cancellation or start tool changes the session's durable child commitments | [`internal/assistant/agent_tool.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/assistant/agent_tool.go#L179-L342) |
| Parent (`P`) | Terminal operator | Current workflow view exposes an unwanted or stalled commitment | The selected run cancellation stops its workflow and owned work | [`internal/terminal/workflows.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/terminal/workflows.go#L196-L234) |

## S3* — Complementary audit

- State: —
- Function: Independently challenge a work claim with complementary evidence and a return path.
- Disturbance / variety regulated: A child can complete with an incorrect change or misleading answer.
- Decisive decision or feedback right: No packaged independent verdict is routed into rework or acceptance.
- Decision owner: The worker controls its ordinary completion. The operator or extension author may compose review.
- Supporting / enforcement mechanisms: Read-only exploration, task transcripts, schema checking and workflow APIs.
- Closure path: Results return to the delegating context. Structural schema validation can retry formatting.
- Why this is / is not agent-owned: An explorer is an operational role. Result shape checks do not adjudicate underlying work.
- Evidence: [`README.md`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/README.md#L297-L311), [`internal/agenttask/runtime_runner.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/agenttask/runtime_runner.go#L99-L228), [`internal/workflow/workflow.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/workflow/workflow.go#L65-L116).
- Basis: structural
- Confidence: High
- Caveats: Custom workflows can add a separate evaluator.

### Absence scope

- Surfaces inspected: Built-in role catalog and tools, child output validation, workflow API and terminal task inspection.
- Plausible first-party paths checked: Checked read-only explorer results, schema retries and composition of an independent evaluator by a user.
- Why no material first-party path remains: The shipped roles and lifecycle checks do not close an evidence-based complementary decision over a produced artifact.

## S4 — Outside-and-then intelligence

- State: —
- Function: Anticipate environmental changes and alter future operating capability.
- Disturbance / variety regulated: Provider characteristics and workspace needs may vary across deployments.
- Decisive decision or feedback right: No shipped decision path selects a future capability alternative from external evidence.
- Decision owner: The operator chooses providers and profiles. Trusted extension authors supply their code.
- Supporting / enforcement mechanisms: Provider configuration, skills and extension manager.
- Closure path: An installation or configuration is consumed by later use. No shipped evidence-driven selection loop is established.
- Why this is / is not agent-owned: Task-local retries or selectable startup capabilities do not supply prospective environmental judgment.
- Evidence: [`README.md`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/README.md#L179-L249), [`README.md`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/README.md#L313-L361), [`docs/extension-manager.md`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/docs/extension-manager.md), [`internal/agenttask/runtime_runner.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/agenttask/runtime_runner.go#L327-L367).
- Basis: structural
- Confidence: High
- Caveats: Generic extensions can provide another deployment design.

### Absence scope

- Surfaces inspected: Provider/profile selectors, skills/extensions, durable workflow host and observed-output retry path.
- Plausible first-party paths checked: Checked configuration and extension updates, provider switching and knowledge carried in session history.
- Why no material first-party path remains: No built-in path compares emerging external demands or alternatives and returns a governed capability choice.

## S5 — Policy and identity

- State: —
- Function: Resolve a standing purpose or authority issue for subsequent LibreCode operation.
- Disturbance / variety regulated: Operator and project preferences can differ over tool authority and mutating child roles.
- Decisive decision or feedback right: No shipped governance path adjudicates an ultimate policy exception for future work.
- Decision owner: The operator or project configuration author sets profiles; extensions are separately trusted local code.
- Supporting / enforcement mechanisms: Profile loading, tool filtering and mutation policy checks.
- Closure path: Loaded permissions constrain subsequent task execution and can be externally edited.
- Why this is / is not agent-owned: Static authority settings and enforcement constrain operation without closing a governance escalation.
- Evidence: [`README.md`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/README.md#L297-L338), [`internal/agenttask/runtime_runner.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/agenttask/runtime_runner.go#L327-L367), [`internal/agent/catalog.go`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/internal/agent/catalog.go), [`docs/extension-runtime.md`](https://github.com/omarluq/librecode/blob/1e7ba321306bc5e01a58f4ee9c53f18178f2cb96/docs/extension-runtime.md).
- Basis: structural
- Confidence: High
- Caveats: Repo governance and operators' own policy processes are outside this operating boundary.

### Absence scope

- Surfaces inspected: Built-in and custom role profiles, configuration, extension trust model, and task execution controls.
- Plausible first-party paths checked: Checked per-role mutation settings, workflow guest boundaries and terminal control for durable policy escalation.
- Why no material first-party path remains: Shipped paths apply loaded authority and let the operator intervene in current work. They do not receive or resolve a binding standing-policy issue.

## Recursion

Each delegated child has its own context and task. Root and terminal controls operate across commitments scoped to the owning session.

## Variety and escalation

Models absorb task and tool-result variation. Profile limits, the durable scheduler, and cancellation control the scope and persistence of delegated work.

## Evidence gaps

Source reviewed at the frozen commit. No live provider run or user-composed extension was used as evidence.
