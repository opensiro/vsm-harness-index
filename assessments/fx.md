---
harness_id: fx
project_name: FX
repository: https://github.com/vercel-labs/fx
review_ref: b8ca67ac4531e63be57520ccfb313626d9b17f2f
reviewed_at: 2026-10-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# FX

## Review boundary

- System in focus: the first-party native Zig coding-agent runtime `fx` at the immutable reviewed commit, including its installed interactive and one-shot CLI, model/tool agent loop, built-in coding tools, permission admission, session state, managed subagent feature, and standard first-party ACP/embedding entry points when they instantiate this agent core.
- Purpose and identity: answer and act on a human coding request against a host workspace by iterating model decisions and read/edit/shell/tool observations while preserving bounded runtime, sessions and permissions.
- Relevant environment: the developer's checkout, shell and file system, human-provided task and authorization, model API/provider, optional MCP/skills and embedding host.
- Standard-distribution boundary: shipped `fx` CLI and `fx ask`, reusable native agent core, ACP and experimental libfx host-mode facilities at this pinned tree. An embedder's independently developed organizational logic and third-party services are not part of the evaluated harness.
- Credited operating / distribution surfaces: [README.md](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/README.md); [main.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/main.zig); [orchestrator.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/orchestrator.zig); [gateway_step.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/gateway_step.zig); [tool_batch.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/tool_batch.zig); [tool_admission.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/tool_admission.zig); [worker_runtime.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/worker_runtime.zig); [read_file.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/tools/filesystem/read_file.zig); [shell.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/tools/shell/shell.zig); [subagent.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/tools/agent/subagent.zig); [managed_owner.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/managed_owner.zig); [authority.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/authority.zig); [child_state.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/child_state.zig); [permissions.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/permissions/permissions.zig); [session_store.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/session/session_store.zig); [README.md](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/sdk/README.md).
- Adjacent first-party surfaces excluded from ownership: development-only repository `AGENTS.md` instructions, unit/E2E tests, release and build CI, examples of external embedded products, `sdk` consumer-provided host behavior, marketing and online services, external model/provider cognition beyond the invoked actor, and user-installed MCP servers or plugins. None is silently imported as a first-party organizational decision right.
- First-party operating / deployment modes considered: interactive terminal and one-shot `fx ask`; `ask` / `auto` / full-access permission modes; opt-in managed child sessions; ACP and libfx agent-core embedding subject to host-supplied state/permissions.
- Recursion level: one executable coding session as the operating system-in-focus, with managed child coding executions as subordinate task cells where enabled; the user's development organization and a fleet of unrelated FX instances are outside this session boundary.
- Reviewed revision: `b8ca67ac4531e63be57520ccfb313626d9b17f2f`.
- Observation date: 2026-10-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README.md](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/README.md) presents a Zig CLI with interactive coding and one-shot `fx ask` execution, ACP integration, and an experimental embeddable libfx/WASM core. The first-party [orchestrator.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/orchestrator.zig) performs the bounded agent-step loop, obtains gateway/model responses, dispatches tool actions and returns their outputs to successive model steps. [tool_batch.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/tool_batch.zig) assembles tool results and error/retry feedback; [tool_admission.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/tool_admission.zig) guards risky actions. Concrete shipped read and shell tools are defined in [read_file.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/tools/filesystem/read_file.zig) and [shell.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/tools/shell/shell.zig). [worker_runtime.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/worker_runtime.zig) handles prompt admission, turn lifecycle, steering, interruptions and processing completion. The agent's tool selection and next-step judgment are distinct from deterministic dispatch, retry caps and permission enforcement.

Optional [subagent.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/tools/agent/subagent.zig) exposes `run` and persistent named-child `message` actions. [managed_owner.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/managed_owner.zig) manages child launch, wait, steering and cancellation, while [authority.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/authority.zig) captures inherited permissions and tool availability; [child_state.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/child_state.zig) persists child identities, work and phases. These are substantive subordinate S1 task-execution and lifecycle features; tool/child count, persistent state and management API names do not by themselves demonstrate cross-S1 S2, whole-current S3, or complementary S3*.

Operator permissions, credential/configuration choice, and selected extension behavior are constraints around coding operations. [session_store.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/session/session_store.zig) and the session modules persist/recover work; compaction, retry and user steering preserve present coding task capability. They are not automatically prospective organizational adaptation or identity-policy governance. [README.md](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/sdk/README.md) requires an embedding host to provide some surrounding I/O/state/policy facilities; a custom external embedder is excluded from function ownership.

## Operational model

The coding model decides what code or command to inspect or change based on task context and actual tool observations, and can choose a delegated work item. The native runtime executes or refuses those decisions under user-configured safety/permission boundaries, presents results, and persists session state. The human supplies the task, permission choices and ultimate external project policy. A managed child is a subordinate coding operation, not a distinct proof of whole-workforce regulation merely because it has a separate session, steering queue or lifecycle registry.

## S1 — Operations

- State: A
- Function: directly transform a developer-supplied coding/repository task through autonomous selection of observations and coding tool actions.
- Disturbance / variety regulated: unknown repository state, code/API differences, failed tools, tool-generated observations, code edits requiring further action, and task-local interruptions.
- Decisive decision or feedback right: the active model selects tool calls and continuation/final response after observing prior tool results; optional child invocation is also selected as work to undertake.
- Decision owner: the active coding agent/model, not the deterministic dispatcher or tool-permission checker.
- Supporting / enforcement mechanisms: CLI entry, orchestrator/tool-loop execution, tool schema and dispatch, mutation and shell admission, operator permission responses, session persistence, runtime stops.
- Closure path: model decision → admitted tool call → file/shell/read operation or bounded denial → returned tool output and next model turn → further task action or final response.
- Boundary reachability: the shipped interactive CLI and one-shot `fx ask` explicitly invoke the same first-party coding tool/model runtime; they do not require downstream developer wiring to create the agent loop.
- Why this is / is not agent-owned: removal of the model's discretionary choice leaves tool validation and invocation primitives but no corresponding task-aware choice of the next coding action; authorization remains a separate owner.
- Evidence: [README.md](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/README.md); [orchestrator.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/orchestrator.zig); [gateway_step.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/gateway_step.zig); [tool_batch.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/tool_batch.zig); [tool_admission.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/tool_admission.zig); [read_file.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/tools/filesystem/read_file.zig); [shell.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/tools/shell/shell.zig).
- Basis: explicit and structural.
- Confidence: high for source-wired model/tool feedback; this was a pinned-source inspection, not a credentialed live model run.
- Caveats: user deny/ask decisions are human-owned constraints; embedding in another application does not donate that application's VSM functions.

## S2 — Coordination

- State: —
- Function: no material first-party cross-S1 interference-specific coordination loop is established at the assessed coding-session recursion.
- Disturbance / variety regulated: possible contention or incompatible changes among concurrent subordinate coding workers, not a documented first-party attenuated oscillation.
- Decisive decision or feedback right: no agent-controlled decision over a documented inter-S1 interference and returned stabilizing relation is evidenced.
- Decision owner: none established for an S2-specific function; root-model delegation and host child-state persistence have narrower task/lifecycle roles.
- Supporting / enforcement mechanisms: child registry, child admission, inherited permissions, bounded child execution and steering.
- Closure path: child outputs/steering can return to a caller, but no conflict-specific attenuation/feedback channel into distinct S1s is established by that alone.
- Why this is / is not agent-owned: parent task delegation and child cancellation do not identify an independently regulated inter-S1 collision; registry serialization protects bookkeeping, not an S2 organizational relation.
- Evidence: [subagent.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/tools/agent/subagent.zig); [authority.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/authority.zig); [child_state.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/child_state.zig); [managed_owner.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/managed_owner.zig); [execution.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/execution.zig).
- Basis: structural, bounded shipped-source conclusion.
- Confidence: medium; specific extension/host arrangements are deliberately excluded.
- Caveats: a user or embedding host may add actual cross-worker coordination; that external construction is not present at the declared boundary.

### Absence scope

- Surfaces inspected: shipped child tool API, inherited authority, persisted child registry, managed run/wait/steer/cancel and task loop feedback, as well as CLI/embedding modes.
- Plausible first-party paths checked: concurrent child workspace collision prevention, conflicting output/commit adjudication, independent worker reservations, explicit interference-specific decisions and returned corrective instructions.
- Why no material first-party path remains: these mechanisms supply bounded lifecycle and ordinary delegation, but not a concrete evidenced disturbance between distinct S1 units plus its specific attenuation and corrective feedback.

## S3 — Inside-and-now control

- State: —
- Function: no live whole-system current-control function over shared S1 commitments/resources is established within the assessed single coding session.
- Disturbance / variety regulated: current subtask delays, failures, approvals and resource limits, as opposed to a documented whole-organization trade-off among S1 commitments.
- Decisive decision or feedback right: no current whole-system resource/priority/constraint decision beyond the coding task's delegation and execution limits is established.
- Decision owner: coding model for individual delegation/steering; human/configuration for task limits and permission policy; neither is shown to close the distinct S3 function here.
- Supporting / enforcement mechanisms: child state, work status/cancel/wait, permission gating, step and retry budgets, user steering.
- Closure path: task and child status can affect their caller's next coding action; no separate whole-current organizational decision with an attributable owner and returned constraint/commitment change is evidenced.
- Why this is / is not agent-owned: naming a managed owner or choosing/cancelling a child task does not establish the whole-system current view and substantive managerial choice required for S3.
- Evidence: [managed_owner.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/managed_owner.zig); [child_state.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/child_state.zig); [worker_runtime.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/worker_runtime.zig); [orchestrator.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/orchestrator.zig); [tool_admission.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/tool_admission.zig).
- Basis: structural, bounded source inspection.
- Confidence: medium; no live multi-operator configuration has been credited.
- Caveats: another surrounding application could supply current-control decisions, but its agency is not bundled into this assessment.

### Absence scope

- Surfaces inspected: agent orchestration, subagent state and management, tool/admission/retry limits, sessions and operator configuration.
- Plausible first-party paths checked: a whole-current roster with actionable shared resource constraints, autonomously revised priorities or commitments, independent parent current-control mode with authoritative return, and feedback into multiple S1 operations.
- Why no material first-party path remains: first-party lifecycle functions govern one coding task or child and enforce previously chosen limits without shipping an evidenced whole-system manager of multiple operations.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit-to-current-control route is shipped at the stated system recursion.
- Disturbance / variety regulated: untrustworthy ordinary worker self-report or missed code defects that could require a distinct audit of operational reality.
- Decisive decision or feedback right: no first-party complementary audit judgment with independent raw-evidence challenge and an S3 corrective return is established.
- Decision owner: ordinary coding agent for optional task review, user for accepting outputs; neither is shown to own an independent S3* audit loop.
- Supporting / enforcement mechanisms: same-agent review continuation prompt, tool results and logs, optional generic child review task and normal test/shell actions.
- Closure path: review can affect the continuing task, but no separately owned complementary audit finding to whole-current control and corrective S1 return is evidenced.
- Why this is / is not agent-owned: a review prompt in [tool_batch.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/tool_batch.zig) requests another normal pass by the same production agent; a configurable child is delegated task execution, not by default a commissioned independent audit.
- Evidence: [tool_batch.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/tool_batch.zig); [subagent.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/tools/agent/subagent.zig); [managed_owner.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/managed_owner.zig); [orchestrator.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/orchestrator.zig).
- Basis: structural.
- Confidence: medium-high in the bounded shipped coding CLI.
- Caveats: external CI, E2E and maintainer code-review mechanisms do not become first-party S3* merely through repository co-location.

### Absence scope

- Surfaces inspected: ordinary tool-result/review continuation, child execution API, application session feedback and separate developer test/CI surface.
- Plausible first-party paths checked: independent raw-artifact sampler/replayer, autonomous separate audit judgment, challenge of ordinary status/results, explicit finding disposition and returned control correction.
- Why no material first-party path remains: ordinary in-loop verification and discretionary subagent delegation provide no evidenced complementary audit ownership and corrective S3 return, even though users could program an audit with them.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped first-party outside-and-then intelligence loop owns future capability adaptation at the assessed recursion.
- Disturbance / variety regulated: possible changing models, tools and external developer environment, distinct from immediate task context.
- Decisive decision or feedback right: no first-party agent selects/ratifies prospective adaptation alternatives on the basis of an external model and returns them to ongoing system capability.
- Decision owner: user/configuration for models, skills and providers; active coding model for task-level web/search and immediate plan decisions.
- Supporting / enforcement mechanisms: providers, optional external web tools and MCP, skill loading, persistent session history, compaction.
- Closure path: observations may update a task's context, but no autonomous or parent-governed future capability adaptation and return path into present control is established.
- Why this is / is not agent-owned: task research, persistent summaries and capability configuration do not alone establish S4.
- Evidence: [README.md](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/README.md); [orchestrator.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/orchestrator.zig); [session_store.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/session/session_store.zig); [context_compaction.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/context_compaction.zig); [skill_runtime.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/skills/skill_runtime.zig).
- Basis: structural and documentation.
- Confidence: medium-high for stated first-party supported modes.
- Caveats: a future external agent or embedding product might implement adaptation without changing this pinned source.

### Absence scope

- Surfaces inspected: model/provider configuration, optional skills/MCP, task context, web/tool use, persistence/recovery and embedding boundary.
- Plausible first-party paths checked: sensing a future-relevant environmental distinction, generating alternative capabilities, authorized internal or parent adaptation decision, and returned modification to subsequent organization-wide operational capability.
- Why no material first-party path remains: available paths supply immediate coding information or externally selected configuration, not the prospective S4 decision/return loop.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy arbitration and authoritative return loop exists at the assessed coding-session boundary.
- Disturbance / variety regulated: competing ultimate-purpose or constitutional identity choices, as distinct from individual risky tool calls.
- Decisive decision or feedback right: no runtime S5 constitutional decision or first-party closed parent escalation of an identity-level matter is demonstrated.
- Decision owner: the user chooses tasks, permission modes and environment policy outside the assessed coding-session organization; tool approval is ordinary action authority, not identity judgment.
- Supporting / enforcement mechanisms: permission/request/deny policy, configuration precedence and child permission inheritance.
- Closure path: human approval/denial constrains one tool execution; there is no evidence of a higher-level identity matter → legitimate parent policy decision → returned governing identity change.
- Why this is / is not agent-owned: static guardrails and human authority over ordinary tool admission are not the ultimate organizational policy function.
- Evidence: [permissions.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/permissions/permissions.zig); [authority.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/subagent/authority.zig); [tool_admission.zig](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/src/core/agent/runtime/tool_admission.zig); [AGENTS.md](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/AGENTS.md); [README.md](https://github.com/vercel-labs/fx/blob/b8ca67ac4531e63be57520ccfb313626d9b17f2f/README.md).
- Basis: structural and explicit boundary separation.
- Confidence: medium-high.
- Caveats: developer repository contribution governance and a human user's wider enterprise identity belong to another recursion, not the installed FX runtime.

### Absence scope

- Surfaces inspected: settings/permission modes, child authority, request admission, prompts, CLI startup and adjacent public contributor governance.
- Plausible first-party paths checked: an internal identity-purpose adjudicator, agent-owned ultimate policy discretion, a first-party parent identity matter/decision/return loop, and durable changed governing policy.
- Why no material first-party path remains: installed controls regulate authorized tools and task execution only; they do not establish identity-level decisions and returning constitutional control.

## Recursion

The root session and managed child sessions can each run model/tool work. Subordinate sessions have local task context and controlled authority, but session nesting itself is not evidence of a self-viable recursive management organization. The assessment does not count external users/hosting providers or repository-maintainer governance as a higher in-boundary VSM recursion.

## Variety and escalation

Tool admission narrows executable actions; model/tool feedback enables an agent to respond to unexpected repository observations; retries and bounds prevent endless invalid tool execution; permissions can escalate a specific action to a human and return allow/deny to that task. These operational safety and intervention paths do not automatically become S2, S3, S3*, S4 or S5.

## Evidence gaps

Source-first static review only. No API-credentialed live agent run, full Zig build or cross-host embedding experiment was undertaken for this assessment. Specific optional user-authored tools, model prompts and host-constructed organizations cannot be asserted as bundled FX functions. Negative states are scoped to the pinned first-party distributed modes, not statements that future extensions are impossible. A genuinely additional shipped independent audit or cross-worker interference-control path found at the same frozen ref would warrant a targeted same-ref correction under Index rules.
