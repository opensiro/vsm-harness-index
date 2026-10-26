---
harness_id: agetor
project_name: Agetor
repository: https://github.com/alamops/agetor
review_ref: c5cf1a2d431f2891506a26010695289a1b6c46ae
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Agetor

## Review boundary

- System in focus: An installed local Agetor workspace managing software-task cards, one or more configured agent CLIs, and explicitly configured pipelines. It is not the Agetor upstream development team or the full project/company that a task serves.
- Purpose and identity: Provide a local, human-operated, multi-harness workbench that turns a task prompt into worktree-isolated agent execution, visible output, optional multi-stage handoffs, diff review and eventual human-controlled delivery.
- Relevant environment: Repository changes, agent model/CLI availability, prompt uncertainty, worktree and Git errors, interrupted/restarted sessions, failing agent runs, concurrent changes, worker handoff ambiguity, review findings and human approvals.
- Standard-distribution boundary: Native macOS/Electrobun application and CLI daemon; built-in task/run orchestrator, repository worktree provisioning, provider-specific Claude/Codex/Cursor/Gemini/fx/Antigravity drivers, persisted runs, pipeline builder and step executor. External agent CLI cognition, native model policy and parent subagents are dependencies, not independent Agetor-owned regulators.
- Credited operating / distribution surfaces: [task and harness launch user contract](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/README.md), [task orchestration and provider launch](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/bun/orchestrator.ts), [agent driver bridge](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/bun/agents.ts), [worktree manager](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/bun/worktree.ts), [shipped pipeline runner](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/bun/pipeline-runner.ts), [pipeline prompt/handoff contract](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/shared/pipeline.ts).
- Adjacent first-party surfaces excluded from ownership: Archived planning documents and development notes, maintainer `CLAUDE.md`, provider/model-native review or auto-permission mechanisms, app sign/notary/update tooling, synthetic tests/fixtures, and user-created arbitrary pipelines not backed by a first-party admissible construction. Diff viewer, Git host reviewer invitations and user click-to-approve are not independent model audit.
- First-party operating / deployment modes: Default interactive task card with selected real CLI; parallel task/worktree operation; user-built, version-frozen multi-step pipelines with optionally separate Review agent; recoverable tmux session drivers; headless CLI/daemon control. fx does not share tmux restart guarantees; non-Claude providers are marked experimental by upstream.
- Recursion level: One local software-task work organization or one launched pipeline/card. External vendor subagents and the entire portfolio/business are separate recursions.
- Reviewed revision: `alamops/agetor@c5cf1a2d431f2891506a26010695289a1b6c46ae` (`main`), package version 1.0.2.
- Observation date: 2026-10-26; frozen source and deterministic protocol inspection only, no real model runtime test.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

Agetor's first-party code creates a local task, assigns a per-task git worktree, selects a concrete externally installed CLI provider and drives the real model agent through a per-provider process/session bridge. The board mirrors task execution, questions, approvals, conversation streams and status. The process manager can reattach supported `tmux` sessions after restart and distinguishes fx process lifetime. Its optional pipeline service snapshots a user-authored graph and chosen agent profiles, creates hidden step tasks that **share the pipeline parent's worktree**, composes a goal plus previous handoff prompt for each role, and starts the provider-specific task. On agent completion, the runner parses the final `<handoff>` JSON, routes to the named allowed next step or parallel fan-out, retries one malformed handoff reminder, then blocks for user intervention if needed. It serializes parent state updates and enforces step caps, but its graph semantics, queue, and status transitions are mechanical. The README's constructed `Plan → Implement → Review → Implement` loop shows a way to commission a separate model audit stage with a feedback path, but no dedicated default review agent or whole-sprint PM is installed.

## Operational model

The operational choices inside assigned coding tasks belong to the configured third-party CLI model agent, reached by Agetor's actual launching/monitoring infrastructure; task goals, worktrees and result contracts are first-party. Multiple S1s can run in independent per-card branches. Pipeline roles are model-backed but source instructions explicitly restrict each role to **its own step**, while graph control is predefined and optionally influenced by the current step's handoff `next` field. A user configuring a separate reviewer agent and a review-to-implementation return edge can create S3* as a narrow supported constructor. Neither normal UI diff review nor externally owned fx Auto safety review is credited. A user manually controls task priority, acceptance and ultimate delivery policy.

## S1 — Operations

- State: A
- Function: Carry out a scoped software task or pipeline-step operation through an active model-backed coding harness and return changed artifacts, answers, test outputs or structured handoff.
- Disturbance / variety regulated: Uncertain codebase state, task-specific implementation choices, test failures, unexpected tool results, external dependencies and user follow-up requirements.
- Decisive decision or feedback right: A configured Claude/Codex/Cursor/Gemini/fx/Antigravity agent chooses concrete code reads/edits and tool actions within its own native permissions; Agetor allocates task worktree/session, sends prompt/turn, records result and relays further input.
- Decision owner: Task's configured model-backed agent running under an Agetor-authored task/step envelope; the Agetor transport/board alone does not semantically solve the coding task.
- Supporting / enforcement mechanisms: Worktree pinned-base isolation, selected harness/profile, native CLI/ACP/tmux driver, per-task run records, status events, user interaction cards and pipeline `<handoff>` capture.
- Closure path: User task/card or pipeline goal → Agetor creates task/worktree and launches selected CLI → model agent selects work/tool operations → resulting source/output/status/handoff is captured → task card or next step/human receives feedback.
- Boundary reachability: The normal Run action in README and `startTask`/`startTaskInner` connect local task data to real installed provider launch implementations; a pipeline `launchStep` creates a hidden task and invokes the same running path.
- Why this is / is not agent-owned: Without executing the selected model-backed CLI, board transitions and tmux/branch scripts cannot autonomously choose the requested source-level implementation, testing or explanation.
- Evidence: [shipped Run and supported harness contract](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/README.md#quick-start); [task start and agent launch dispatch](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/bun/orchestrator.ts#L1431-L1600); [provider agent bridge](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/bun/agents.ts); [pipeline hidden step task launch](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/bun/pipeline-runner.ts#L632-L835).
- Basis: Executable first-party task/harness orchestration with model action/feedback path in standard supported mode.
- Confidence: High for reachable task transport, medium for runtime behavior across experimental providers.
- Caveats: Actual model, account, macOS-compatible binary and chosen permissions must be present. Source/CI fixtures do not measure quality or safety; no agent execution was performed here.

## S2 — Coordination

- State: —
- Function: Would attenuate a specific actual inter-S1 collision and return a coordinated adjustment to the competing workers.
- Disturbance / variety regulated: Concurrent workers editing shared files, incompatible assumptions passed between different steps, and competing changes requiring arbitration rather than isolation alone.
- Decisive decision or feedback right: Each ordinary card has its own branch/worktree, and pipeline parent state has serialized updates; Agetor provides warnings and human-guided git conflict tools but no source-established autonomous collision-reading mediator between two S1s.
- Decision owner: Human project operator or external model agent separately assigned a repair task, not the built-in routing or worktree allocator as an independent S2 model regulator.
- Supporting / enforcement mechanisms: Per-task worktrees, per-parent pipeline locks, parallel step list in task prompt, explicit warning to avoid overlapping files, manual merge-conflict repair task, Git status and PR checks.
- Closure path: Isolation prevents many cross-card overwrites; within a pipeline, parallel agents share a worktree and receive a warning. An actual source collision is not diagnosed and negotiated by a first-party dedicated S2 arbiter before workers modify their behavior.
- Boundary reachability: All named mechanisms are available, but an inter-worker semantic conflict → discretionary settlement → instructions back to the distinct conflicting agents is not evidenced in a standard shipped construction.
- Why this is / is not agent-owned: Per-card worktree separation and serialized metadata updates are mechanical conflict avoidance, not an owner assessing the incompatibility between two workers and changing their commitments.
- Evidence: [parallel pipeline worktree collision warning](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/README.md#pipelines); [parent update lock and shared step worktree](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/bun/pipeline-runner.ts#L100-L160); [parallel worker warning in composed prompt](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/shared/pipeline.ts#L1091-L1160).
- Basis: Source-negative for distinct inter-S1 conflict attenuation at this recursion; mechanical safety surfaces are substantial but not S2.
- Confidence: Medium-high.
- Caveats: A bespoke user-built coordination agent could be added, but unbounded external prompt engineering is not credited as a first-party owned standard mode.

### Absence scope

- Surfaces inspected: Worktree creation, pipeline fan-out/fan-in, parallel sibling prompts, parent locks, task status, native Git/PR conflict operations and review-loop description.
- Plausible first-party paths checked: Shared-worktree write collisions, dependency/assumption arbitration, cross-branch merge clashes, repeated agent disagreement and concurrent resource contention.
- Why no material first-party path remains: Source explicitly warns that parallel pipeline agents can edit the same files without prevention; isolation and warnings do not settle semantic conflicts, and Git conflict-resolution is a separately commissioned task/human action.

## S3 — Inside-and-now control

- State: —
- Function: Would own a discretionary, whole-current task/pipeline view and redirect present commitments among operational units based on feedback.
- Disturbance / variety regulated: Current mission drift, multi-agent scheduling priorities, failures after review, task-level reallocation and overall acceptance/readiness conflicts.
- Decisive decision or feedback right: The user defines the task board and pipeline graph. The pipeline runner auto-follows single edges or fan-out, passes the current **step agent's** selected outgoing `next` to a predefined graph edge, and blocks/moves for explicit human retry/advance on failures. No shipped model PM with whole-current decision rights is evidenced.
- Decision owner: Human operator for mission-level choices and a deterministic pipeline engine for prescribed state transitions; individual agents own only their assigned step or local branch suggestion.
- Supporting / enforcement mechanisms: Pipeline snapshot, handoff schema, `resolveNextSteps`, sequential/parallel edges, step caps, once-only malformed-handoff reminder, task status and manual Advance/Retry/Stop actions.
- Closure path: User-authored graph → step worker sees overall goal and preceding handoff → worker chooses a permitted `next` only when multiple outgoing edges exist → deterministic runner launches allowed successor or blocks for user. This is step-local routing, not a dedicated whole-current discretionary control loop.
- Boundary reachability: The runner is fully connected, but its own emitted step prompts state that the worker is responsible for its **step only, not the whole pipeline**. An arbitrary user-authored supervisory prompt is not a shipped, bounded current-manager construction.
- Why this is / is not agent-owned: Model choice of an allowed outgoing edge is real but remains local operational branch selection; the broader task portfolio priorities, coordination, stop/replan and acceptance still reside with the operator or predefined code.
- Evidence: [step-scoped authority in composed prompt](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/shared/pipeline.ts#L1042-L1075); [single/all/agent-next routing](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/shared/pipeline.ts#L900-L945); [runner reacts to settled steps](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/bun/pipeline-runner.ts#L2023-L2250); [operator retry/advance modes](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/README.md#pipelines).
- Basis: Negative for a whole-current discretionary owner; positive local branching and execution scheduling deliberately not overcounted.
- Confidence: Medium-high for published normal pipeline contract.
- Caveats: A user could define an entire PM-agent workflow using generic agent profiles; mere capability to author arbitrary instructions does not establish a first-party S3 current-governor path.

### Absence scope

- Surfaces inspected: Orchestrator task lifecycle, pipeline graph model, `launchStep`, handoff prompt, next-edge resolution, live run reconciliation, UI board and manual pipeline controls.
- Plausible first-party paths checked: Whole-task PM role, model selection of rescheduling/rework outside prescribed edges, cross-worker allocation correction, current-global mission replanning and closure readiness.
- Why no material first-party path remains: Each model role is bounded to its step; pipeline engine only interprets graph and structured outputs, while the operator owns graph and exception decisions. No installed whole-current model control authority was found.

## S3* — Complementary audit

- State: C
- Function: Allow a user-built pipeline to insert a separate model-backed Review role to test a preceding implementer's changes and return a pass/fail route for correction.
- Disturbance / variety regulated: Implementation errors or missing requirements concealed by an implementer's self-reported success and undiscovered branch regressions.
- Decisive decision or feedback right: A separately configured `Review` agent/profile, when included in a pipeline, runs as its own hidden step task against the same original worktree and parent goal, then may place `next: Implement` or `next: Docs`/finish in the handoff according to its inspection verdict.
- Decision owner: Distinct user-selected model-backed reviewer step operating through Agetor's first-party snapshot/launch/return facility; user chooses role/instructions and native CLI permissions.
- Supporting / enforcement mechanisms: Separate agent-profile step, code worktree visibility, prior handoff with untrusted-data framing, prompt containing overall goal, structured `<handoff>` verdict/next target, graph transition restrictions and runner's follow-up execution.
- Closure path: Implementer produces source changes and `<handoff>` → configured separate Review agent receives goal, previous outcome and same worktree → reviewer examines original files/tests/diff if its profile instructions require this → reviewer selects a configured correction/approval edge → runner re-launches Implement or advances to next stage.
- Boundary reachability: README ships an explicit Plan → Implement → Review graph with `Review -- changes requested --> Implement` and `Review -- approved --> Docs`. `pipeline-runner.ts` constructs hidden model-backed Review tasks from selected profiles and passes original worktree; `pipeline.ts` renders untrusted handoff context and checks route; `resolveNextSteps` consumes reviewer-selected `next` when multiple edges exist. The construction is optional, not a built-in always-on independent reviewer.
- Why this is / is not agent-owned: The separate model step can make a semantic correctness assessment using the actual project artifacts and redirect work. Graph labels alone, diff UI or the original implementing agent's self-review would not meet this condition.
- Claim being audited: Implementer's assertion that current branch satisfies the requested software goal and is ready to advance.
- Ordinary reporting path: Implementer agent's final message/structured handoff, task status and ordinary saved transcript.
- Complementary access path: Different model-agent step receives original source worktree, goal and earlier handoff (explicitly fenced as untrusted), and can inspect files/tests independently rather than only trusting the implementation summary.
- Independence boundary: Distinct selected agent profile and separate hidden step task/turn; same worktree, same user machine and potentially same vendor/model, with no mandatory independent sandbox or read-only reviewer policy.
- Who acts on findings: The Agetor runner follows the reviewer's configured `next` edge back to the Implement agent when changes are requested; unresolved steps can block and require human choice.
- Evidence: [first-party graph review/correction example](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/README.md#pipelines); [per-step agent task and worktree](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/bun/pipeline-runner.ts#L632-L835); [original goal, untrusted prior output and step instructions](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/shared/pipeline.ts#L1042-L1175); [model-chosen rework edge](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/shared/pipeline.ts#L900-L945).
- Basis: Supported but user-assembled independent-review constructor with real source/handoff access and correction-edge return.
- Confidence: Medium; no built-in substantive reviewer prompt, required original-artifact checklist or mandatory model separation was established.
- Caveats: The user must configure a genuinely separate reviewer profile, original-artifact inspection instruction, and rework edge; arbitrary pipeline called “review” without actual inspection is not S3*. Native fx safety tool reviewer is fx-owned and excluded.

## S4 — Outside-and-then intelligence

- State: —
- Function: Would explore future external changes and choose enduring new capabilities for the local work organization, returning those to present work.
- Disturbance / variety regulated: Future coding agent/provider developments, new methods, product/market conditions or unseen environment changes beyond current task execution.
- Decisive decision or feedback right: Agetor discovers model names, available harnesses and account plans, and operators update agents/pipelines; no independent model-backed strategic external sensing and autonomous future adaptation owner was found.
- Decision owner: Human Agetor operator chooses agent profiles, models, next tasks, new workflow capabilities and app updates; discovery feeds current CLI compatibility.
- Supporting / enforcement mechanisms: CLI model discovery, version checks, presets, exported agent profiles, pipeline editor, update facility and usage meter.
- Closure path: Updated model catalog may enable an operator to choose another harness for a future task, but is not an agent-owned prospective intelligence → adaptation design → current-control return circuit.
- Boundary reachability: Model discovery is operationally wired yet only exposes currently available provider options and refusal/upgrade hints; it is not a future capability decision-making layer.
- Why this is / is not agent-owned: Enumerating available models and remembering configured profiles does not autonomously weigh a future environmental threat and redesign organizational capabilities.
- Evidence: [model/provider discovery and profile control](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/README.md#features); [harness discovery code](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/src/bun/harness-discovery.ts); [user-owned pipeline configuration](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/README.md#pipelines).
- Basis: Negative for prospective agent-owned capability strategy.
- Confidence: Medium-high.
- Caveats: An external agent could be directed to research a future platform change as an S1 task; task-level research alone is not a standing S4 regulator of Agetor.

### Absence scope

- Surfaces inspected: Harness/model discovery, profile and pipeline import/export, runtime status, usage tracking, software updates, README and task lifecycle.
- Plausible first-party paths checked: Trend monitoring, explicit prospective strategy, choosing durable new workflow competencies, agent self-redesign and returning a future-facing policy/capability into a current pipeline.
- Why no material first-party path remains: Discovered compatibility data inform human settings or launch refusal and all durable workflow design remains operator-authored; no agent-owned externally prospective adaptation loop is evidenced.

## S5 — Policy and identity

- State: —
- Function: Would decide ultimate legitimate purpose/identity disputes and install binding organizational policy.
- Disturbance / variety regulated: Contradictory ultimate goals, stakeholder values or legitimate final authority above task/CLI permissions and PR approvals.
- Decisive decision or feedback right: Agetor replays native provider approval questions, exposes per-agent safety modes and lets the user approve diff/PR delivery. It does not decide ultimate purpose or define a constitutional hierarchy.
- Decision owner: User/operator of the local workspace, and native external provider permissions for individual tools; application itself is a bounded workflow interface.
- Supporting / enforcement mechanisms: Session permission cards, native CLI modes, worktree restrictions, Git host authentication and human PR publication/merge choices.
- Closure path: A user resolves an external approval question or changes a harness mode, which changes allowed operations in the current task; no identity-conflict decision is made and returned as enduring purpose policy.
- Boundary reachability: Approval UI and provider-native mode controls exist and can be exercised, but no first-party ultimate-policy judgment owner is reached.
- Why this is / is not agent-owned: Existing user privileges and native CLI sandbox decisions are fixed conditions and operator choices, not autonomous adjudication of the organization's higher purpose.
- Evidence: [permission and approval interface](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/README.md#converse); [explicit native privilege warning](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/README.md#security); [user-controlled pipeline and PR actions](https://github.com/alamops/agetor/blob/c5cf1a2d431f2891506a26010695289a1b6c46ae/README.md#ship).
- Basis: Bounded source-negative for identity and ultimate policy.
- Confidence: High at the chosen task-workbench recursion.
- Caveats: Workspace human may be a parent S5 for its wider business, but the user providing permissions or reviewing a PR is not automatically a first-party Agetor `P` mode.

### Absence scope

- Surfaces inspected: Local permissions, harness safety modes, user confirmations, Git host actions, pipeline graph authoring, update and task lifecycle.
- Plausible first-party paths checked: Organizational identity disputes, policy-revision decisions, parent ultimate governance, durable mission change and binding return to operational units.
- Why no material first-party path remains: All reviewed mechanisms implement task/CLI authorization or software delivery already defined by the operator; no independent ultimate-purpose deliberation/decision path exists inside Agetor.

## Distributed OSS parent arrangement

Agetor's local operator, external CLI providers, Git host and source maintainers retain separate authority. Agetor controls local transport and records, but does not own Claude/Codex/fx native model security, external subagent policies or the user's company strategy. These parts must not be composed into an unevidenced overall S5.

## Self-hosted and non-human modes

Agetor requires its target macOS/Apple Silicon environment for published binary support. Its headless CLI/daemon can operate locally without visible app, while actual non-human task decisions still require a compatible installed provider CLI and authentication. Per-task worktree separation is present; multiple steps of one pipeline can share a worktree. Claude/Codex and other tmux-backed sessions may reattach after restart; fx processes are not restart-persistent.

## Recursion

One task card or configured pipeline is the operating unit. Individual model agents execute bounded code steps; the user's graph is the workflow and human owner remains current-goal allocator and ultimate authority. A configured separate reviewer step may audit implementation, but the general board/graph and its persisted state do not become an agent-owned S3 manager merely because they track multiple agents.

## Variety and escalation

User task uncertainty enters selected coding agent/tool operations, with outputs and errors returned to the local task board. The pipeline translates step-local handoff choices into permitted next edges, retries once on malformed handoff format, then blocks for an operator. Optional separate reviewer can use the same worktree to challenge implementation and return a correction edge. Concurrent worktree and provider liveness safeguards reduce interference but are not semantic inter-S1 arbitration; ultimate delivery and policy remain with the operator.

## Evidence gaps

- Frozen `c5cf1a2d...` source was inspected. The runtime test runner `bun` was not available in the assessment environment, so shipped Agetor tests were **not** executed; repeatable Index, version-pinned methodology, derived views and GitHub CI are the available verification gates. No LLM/provider/Browser agent-quality tests were performed.
- The included S1 claim depends on a selected installed model CLI; Agetor alone is a workbench and process manager, not a first-party inference service.
- No source-established whole-current model PM was found. `handoff.next` is an S1 worker's local selection among user-defined graph edges; the step prompt explicitly excludes responsibility for the entire pipeline.
- `S3*=C` is limited to the explicitly user-assembled Review profile/step with original source access and review-to-implementation edge. It does not assert that ordinary diff UI, fx provider-native tool review, or any arbitrary named “Review” stage is independent semantic audit.
- Pipeline parallel steps share a worktree and user warnings acknowledge edit collisions. No claim of semantic S2 conflict settlement is made.
