---
harness_id: paddles
project_name: Paddles
repository: https://github.com/spoke-sh/paddles
review_ref: eb7a03bfe0ba33123debd8cd8c0c97d073f55e33
reviewed_at: 2026-11-07
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

# Paddles

## Review boundary

- System in focus: the shipped Paddles Rust coding-agent harness, not the project-development organization, its Keel board or a future distributed agent system.
- Purpose and identity: turn operator coding requests into source-grounded answers, verified-in-loop evidence, applied workspace edits or explicit blocked outcomes.
- Relevant environment: repository files and diffs, model HTTP endpoints, available local retrieval/semantic tools, command outcomes, context strain, user steering, runtime policy and resource budgets.
- Standard-distribution boundary: `src/main.rs`/CLI and embedded `AgentRuntime` → `src/application/turn.rs` → `agent_loop.rs`, the model-backed action selector, governed workspace tools, final rendering, session/thread traces and optional configured retrieval interfaces.
- Credited operating / distribution surfaces: live recursive action-selection and workspace-tool execution; typed instruction/turn contracts, read/inspect/edit/shell and external-capability gating; operator memory and guidance, model-directed sequential thread state and evidence/trace readback.
- Adjacent first-party surfaces excluded from ownership: `.keel/` project mission board, `CONSTITUTION.md`/`POLICY.md` as developer/maintainer design commitments, CI/tests and dev-governance, `src/application/worker_runtime.rs` test-only worker-spawn/integration path not called from the shipped turn loop, prospective real subagents/MCP transport/parallel sibling generation, and third-party retrieval/model systems.
- First-party operating / deployment modes considered: local-first HTTP model service such as Ollama or configured remote model; CLI/interactive/web/embedded library surfaces; one model-directed current-turn action loop; read-only review/planning/execution turn contracts; sequential session-thread continuation/branch/merge; operator steering and governed tool permissions.
- Recursion level: one user-request coding-agent operating cell; conversational branches are not separate concurrent operating agents, and no independently autonomous child S1 loop is wired in the frozen distribution.
- Reviewed revision: `spoke-sh/paddles@eb7a03bfe0ba33123debd8cd8c0c97d073f55e33`, stable GitHub repository ID `1182878595`.
- Observation date: 2026-11-07. Profile 0.2.4; Methodology 0.3.7, including immutable generation provenance.

## Repository architecture

The Rust executable and library expose an `AgentRuntime` that assembles `AGENTS.md` operator memory, model-derived guidance/procedures, active session context and evidence. `turn.rs` obtains a model-selected thread decision for a captured user prompt and then enters the common turn runtime; `agent_loop.rs` obtains bounded model-selected actions, validates them, dispatches actual retrieval/terminal/file/shell/semantic work and feeds resulting evidence into later decisions. The final-rendering model is a separate *answer-authoring* role, not a second operational or auditing agent. The trace recorder and TUI/web forensic projections provide durable observability and human inspection.

`PlannerAction::Branch` records bounded labeled branches in `pending_branches`, and the next planner context renders these as `pending branch: ...`; it does not spawn an independent child. Model-directed `ConversationThreadLayer` branch/merge decisions manage sequential interactive turns. `BoundedWorkerRuntime` and `WorkerEvidenceIntegrator` offer typed worker-spawn and conflicting-write-scope rejection, but the only invocations at this ref are module tests. The live action loop has no call to their `spawn` or `integrate` methods; `ARCHITECTURE.md` explicitly describes true subagents and simultaneous sibling generation as future work. Therefore neither an active multi-agent S2 nor current multi-unit S3 can borrow that scaffold.

Paddles' governor monitors stalls/timeouts and emits typed state; steering policies may trigger a *second action-selection request* to reconsider a premature edit, stale premise or exhausted budget. An instruction frame prevents advice-only completion when an edit obligation remains open. These are legitimate local execution and completion controls, but do not independently audit task correctness or direct an organizational portfolio. `POLICY.md` and `CONSTITUTION.md` describe development expectations and runtime constraints; operator approval is not a mission-level policy ratification mechanism.

Frozen first-party evidence:

- [Product and model-directed recursive loop](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/README.md)
- [Active/runtime architecture, explicit future subagent and concurrency limits](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/ARCHITECTURE.md)
- [Turn entry, model-directed session-thread decisions](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/turn.rs)
- [Real action loop, branch handling, tool execution and completion checks](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/agent_loop.rs)
- [Application runtime, pending-branch context and same-selector steering review](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/mod.rs)
- [Shared bounded action schema](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/planner_action_schema.rs), [worker constructor/integrator including unit tests](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/worker_runtime.rs)
- [Operational policies, including honesty about sequential threading](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/POLICY.md), [trace projection for operator inspection](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/conversation_read_model.rs)

## Operational model

One model-controlled recursive worker selects the next bounded workspace operation, receives concrete file/tool evidence and iterates until answer, edit, stop or exhausted budget. The deterministic controller validates and enforces constraints; optional final-rendering and specialist-continuity inference provide output or notes, not separate organizational owners. User steering, thread switching and approval remain human-initiated current-task controls. The only supported autonomous VSM closure found is S1.

## S1 — Operations

- State: A
- Function: investigate code, run bounded tools, apply edits and return a source-backed completion or an explicit inability to satisfy a request.
- Disturbance / variety regulated: unknown code structure, contradictory evidence, failing commands, model/provider limitations, unavailable tools, context truncation and incomplete edit obligations.
- Decisive decision or feedback right: the selected model decides the next typed action (`search`, `read`, `inspect`, `shell`, edit, `refine`, `branch`, `answer` or `stop`) and revises it after actual evidence returns.
- Decision owner: first-party model-directed recursive agent loop; separately chosen HTTP inference provider supplies the model, while controller enforcement is bounded machinery.
- Supporting / enforcement mechanisms: typed shared action schema, capability manifest, instruction frame, steering review, memory/guidance context, tool execution handlers, budgets, terminal governance, trace and final renderer.
- Closure path: request → interpretation → model action → validated first-party execution → observed result/evidence → model's next decision or terminal/blocked answer.
- Boundary reachability: CLI, web and library call the same shipped `AgentRuntime` turn path; `turn.rs` and `agent_loop.rs` invoke model action selection and concrete workspace effects without custom test assembly.
- Why this is / is not agent-owned: actual action choice and task-level response to external evidence are model-owned, while deterministic validation, budgets, and human permissions constrain rather than select the task-directed action.
- Evidence: [README turn cycle](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/README.md), [action loop](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/agent_loop.rs), [turn entry](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/turn.rs).
- Basis: explicit architecture and structural primary-source reachability.
- Confidence: high for source-wired local S1.
- Caveats: static frozen-source review, no Rust toolchain, provider-backed live inference, or upstream integration suite executed here.

## S2 — Coordination

- State: —
- Function: no operational anti-interference feedback relation among separate concurrently acting first-party S1 cells is established.
- Disturbance / variety regulated: simultaneous sibling workspace writes would be an S2 hazard, and the worker constructor tests contain explicit scope-conflict rejection; however that path is not mounted in the standard agent runtime.
- Distinct S1 units: only one model-directed active coding S1 is shipped; separate rendering, retrieval and sequential conversation-thread branches are not independent task-operating S1 cells.
- Inter-S1 disturbance: hypothetical overlapping writes in isolated worker tests; no reachable shipped overlapping S1 pair is evidenced.
- Attenuating coordination relation: `WorkerEvidenceIntegrator` can reject conflicting scopes in tests, but has no live integration caller/returned effect in the default runtime.
- Feedback into subsequent S1 behaviour: tested conflict verdict is not delivered to shipped concurrent S1 operations; branching labels merely re-enter the same action loop's prompt context.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: source explicitly defines future true subagents/concurrency, whereas current thread routing and pending branch labels schedule one agent's own work.
- Decisive decision or feedback right: no live shared-agent coordination decision regulates conflicting independent S1 commitments.
- Decision owner: model's individual branch/thread choice, deterministic thread state and test-only worker fixture, not a shipped S2 authority.
- Supporting / enforcement mechanisms: branch traces, sequential conversation merge records, reserved worker runtime types and test conflict guard.
- Closure path: current agent queues branch label → label re-enters current agent context; no inter-agent conflict → returned coordination decision path.
- Why this is / is not agent-owned: an agent can decompose its own task but there is no distinct inter-agent disturbance for it to settle.
- Evidence: [live branch handler](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/agent_loop.rs), [context recycling](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/mod.rs), [worker-only tests](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/worker_runtime.rs), [roadmap limits](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/ARCHITECTURE.md).
- Basis: structural negative with explicit documented distribution limit.
- Confidence: high.
- Caveats: the worker API may become S2 evidence after future production wiring, but does not establish a current constructor path within the assessed mode.

### Absence scope

- Surfaces inspected: agent runtime, action-schema/branch dispatch, thread selector and merge trace, worker runtime/integrator/call sites, policy and current/roadmap architecture.
- Plausible first-party paths checked: concurrent bounded S1 worker spawning, write-scope interference arbitration, active shared-work conflict feedback, true sibling execution and model-mediated thread merge-back.
- Why no material first-party path remains: the only conflict-specific worker path is invoked in tests; the shipped runtime explicitly executes a single model-directed action loop with checkpoint-bounded sequential threads.

## S3 — Inside-and-now control

- State: —
- Function: no organizational whole-current supervision of multiple operating cells, commitments or resources is closed.
- Disturbance / variety regulated: runtime stalls, token/step/search budgets, scope violations, edit obligations and operator interrupts are enforced per turn, not balanced across a multi-unit operational whole.
- Decisive decision or feedback right: no separate decision owner reallocates current commitments or resources across distinct S1 units; model chooses local next work, and the governor implements predetermined limits.
- Decision owner: local agent for task steps; deterministic governor and turn contracts for resource/status enforcement; human for immediate stop/mode permissions.
- Supporting / enforcement mechanisms: typed phase/governor events, runtime budgets, instruction-frame completion gate, execution governance and session checkpoint controls.
- Closure path: active step → governor/contract emits pacing, stop or blocked result within same S1 turn; no whole-current S3 portfolio decision/feedback loop.
- Why this is / is not agent-owned: removing the model leaves governor enforcement but no discretionary current cross-unit resource/commitment bargain; moving a single task's next step is S1, not S3.
- Evidence: [governor phases](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/ARCHITECTURE.md), [current-loop termination](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/agent_loop.rs), [control and budgets](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/mod.rs).
- Basis: explicit runtime scope plus structural negative.
- Confidence: medium-high.
- Caveats: a strong single-loop governor is useful current control but not organizational S3 at this declared recursion.

### Absence scope

- Surfaces inspected: governor/harness-state events, agent-loop budgets, turn instructions, thread decisions, available operator controls and worker stub.
- Plausible first-party paths checked: whole-current view over multiple S1 outcomes, cross-cell resource priority, active responsibility/commitment redistribution, parent supervisor return and exception arbitration.
- Why no material first-party path remains: actual discretionary choices and intervention scope remain local to one agent turn or operator session; whole-system current-operating-cell regulation is not assembled.

## S3* — Complementary audit

- State: —
- Function: no distinct complementary, sufficiently independent inspection of production claims with findings returning as corrective organizational control is shipped.
- Disturbance / variety regulated: incorrect code/final responses, misleading traces and unsupported edit-complete claims are risks; instruction-frame checks block advice-only responses, but are routine same-loop completion checks.
- Decisive decision or feedback right: the same action selector reconsiders its own work under `premise-challenge`/action-bias notes; forensic read model replays original records for operator viewing. Neither independently adjudicates the coding outcome against an alternative source and sends findings to a distinct control owner.
- Decision owner: producing model/current turn for steering redecision; deterministic contract and human trace viewer for other checks.
- Supporting / enforcement mechanisms: instruction frame, model steering notes, trace recorder, `/forensics` operator readback, final renderer and human-requested inspection.
- Claim being audited: whether a reported repository edit or answer is materially correct in the real workspace, not merely whether an instruction-frame state was honored.
- Ordinary reporting path: same action loop emits tool events, evidence, block/answer and durable trace, passed to final rendering.
- Complementary access path: no independent task-artifact audit; inspector reconstructs records from the ordinary report itself, and same selector's steering review receives the already collected evidence.
- Independence boundary: trace replay is separate viewing but not independent verification of producing unit's task claim; completion enforcement reuses the production action/instruction path.
- Who acts on findings: agent acts on its own steering notes; a human may inspect web/TUI traces but no installed independent verdict-to-rework arrangement exists.
- Closure path: routine signal → same model redecision or deterministic blocked outcome; separate forensic replay → operator visualization. No independent audit result returns to S3.
- Why this is / is not agent-owned: an extra model call, an inspector UI and reliable traceability do not prove complementary ground-truth access or independent audit ownership.
- Evidence: [steering-review implementation](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/mod.rs), [forensic projection](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/conversation_read_model.rs), [completion enforcement](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/agent_loop.rs).
- Basis: structural negative with architecture review.
- Confidence: medium-high.
- Caveats: externally supplied independent reviewing agents are not part of this first-party operating mode.

### Absence scope

- Surfaces inspected: action-selection signal reviewer, instruction-frame write evidence, final rendering, forensic trace projection/Web read routes, model role split, worker integration tests and operator-review mode.
- Plausible first-party paths checked: sampled artifact reinspection after production, independent verifier with separate evidence source, raw-file/diff replay and contradiction, audit verdict-to-controller correction.
- Why no material first-party path remains: actual checks are in the same operational path or operator-facing replay of producer trace; no separate assessment of task correctness and returned audit finding is wired.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective external-environment intelligence loop devises and implements strategic capability change for the harness.
- Disturbance / variety regulated: changing model capabilities, project instructions, tools, context and user goals affect execution but are handled through preselected configuration or current-turn evidence.
- Decisive decision or feedback right: human/developer chooses new model roles and software integration; task model chooses immediate action/search, not comparative future adaptation options for the system.
- Decision owner: operator and maintainer for future stack capabilities; same S1 model for present task reasoning.
- Supporting / enforcement mechanisms: dynamic capability manifest, model routing, `AGENTS.md`/guidance subgraph, specialist continuity notes, context compaction policy and roadmap ADRs.
- Closure path: configured capability disclosure → current model selects an action; future support requires developer implementation/configuration, not agent-selected S4 option returned to present operations.
- Why this is / is not agent-owned: guidance graph and recent-turn continuity are contextual memory; they neither model future external change nor close adaptation of the installed harness.
- Evidence: [model routing and backlog boundary](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/ARCHITECTURE.md), [routing principles](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/POLICY.md).
- Basis: explicit current-vs-future separation and structural negative.
- Confidence: high.
- Caveats: human-led software evolution is outside this evaluated runtime mode.

### Absence scope

- Surfaces inspected: capability manifest, guidance and memory integration, specialist continuity, HTTP model routing, project ADR/roadmap and retrieval/action selectors.
- Plausible first-party paths checked: external future signal detection, adaptive alternatives, comparison with present system constraints, authorized choice and deployment of new strategy/capability.
- Why no material first-party path remains: the same loop uses external evidence to fulfill the current task, while future system changes are configured or built by humans.

## S5 — Policy and identity

- State: —
- Function: no runtime ultimate identity/legitimacy decision loop returns a new authoritative charter to subsequent harness operation.
- Disturbance / variety regulated: unsafe commands, review/planning mutation rules, simulated board status and governance envelopes are constrained, but ordinary task safety/approval is not system identity adjudication.
- Decisive decision or feedback right: operator/developer supplies a static constitution and execution policies and approves particular effects; no first-party S5 decision settles present/future identity tensions at this runtime recursion.
- Decision owner: human operator for runtime permission, maintainers for source policy; deterministic controller for enforcing predefined constraints, not autonomous or first-party parent-closed S5.
- Supporting / enforcement mechanisms: `CONSTITUTION.md`, `POLICY.md`, turn contracts, execution governance/profile, fail-closed action tools and approval/mutation posture.
- Closure path: configured static constraint → tool validation/allow/block → current loop; no identity-level proposal → legitimate parent ratification → changed ultimate operating policy path.
- Why this is / is not agent-owned: removing the agent leaves fixed policy enforcement and developer documentation, not legitimate mission-level discretionary adjudication.
- Evidence: [policy](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/POLICY.md), [constitution](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/CONSTITUTION.md), [turn contract/application](https://github.com/spoke-sh/paddles/blob/eb7a03bfe0ba33123debd8cd8c0c97d073f55e33/src/application/mod.rs).
- Basis: structural negative after checking supported operator and policy surfaces.
- Confidence: high.
- Caveats: contributor governance of the Paddles source project is a separate organization, not the installed coding harness's own parent-closure mode.

### Absence scope

- Surfaces inspected: foundational governance docs, human operator roles, turn contract/mutation gates, execution governance and project mission/Keel conventions.
- Plausible first-party paths checked: runtime identity conflict escalation, parent policy decision and authoritative return to execution, autonomous ultimate-policy ratification and separated S3–S4 balance.
- Why no material first-party path remains: the inspected paths specify and enforce preexisting safety/workflow rules, not a legitimized runtime identity-level decision/return process.

## Recursion

One directly agent-operated coding cell is evidenced. Nested branch identifiers, sequential interactive thread lineage, typed worker lifecycles in tests and specialist runtime notes do not prove independently viable child units with their own metasystem and organizational closure.

## Variety and escalation

Paddles attenuates model/tool variety through a typed schema, explicit capability manifest, safe workspace execution, bounded resource budgets, memory compaction and blocked-on-unsatisfied edit outcomes. Premise-challenge and error-result feedback return into the same S1. Human steering/interrupts permit exceptional input, but no separate current-portfolio, prospective-adaptation or ultimate-policy function is established by their existence.

## Evidence gaps

- No upstream `cargo` toolchain or live model-provider run was available in the review environment. Functional claims are bounded to pinned first-party code/documentation and shipped-path structural reachability, not measured reliability or production deployment.
- The typed `worker_runtime` API could support future distinct workers; its test-only uses and the explicit roadmap exclusion resolve the *current* boundary to a bounded negative rather than an unexamined active multiagent mode.
- No independent human audit, task-correctness ground-truth replay, or closed organizational policy-return experiment was conducted.
