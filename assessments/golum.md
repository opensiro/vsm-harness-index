---
harness_id: golum
project_name: Golum
repository: https://github.com/Vignesh-Rajarajan/golum
review_ref: ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Golum

## Review boundary

- System in focus: the first-party Golum terminal coding-agent runtime at frozen revision `ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af`, centered on `pkg/harness` plus directly owned coding tools, execution confinement, durable session/recovery state, context compaction, steering/follow-up queues, memory, hooks, prompt/skill configuration and the supported TUI.
- Purpose and identity: perform software-engineering work in a selected workspace through a durable model/tool loop while preserving recoverable execution state and allowing an interactive operator to redirect or stop current work.
- Relevant environment: user goals and follow-ups, workspace/source/build/test state, shell/tool results, model/provider responses, configured MCP services, project/user instructions, persisted session/history/memory state and operator interventions.
- Standard-distribution boundary: Golum's `pkg/harness`, built-in tools and execution environment, TUI, session/reducer/recovery machinery, context manager, memory, hooks, skills/prompts and MCP client integration are inside. External model providers and MCP servers are dependencies and cannot donate organizational functions.
- Credited operating / distribution surfaces: `README.md`; `cmd/golum/main.go`; `internal/ui/model.go`; `internal/ui/commands.go`; `internal/ui/approval.go`; `pkg/harness/harness.go`; `pkg/harness/driver.go`; `pkg/harness/director.go`; `pkg/harness/queue.go`; `pkg/harness/session/`; `pkg/contextmgr/`; `pkg/tool/`; `pkg/memory/`; `pkg/hooks/`; `pkg/prompt/`.
- Adjacent first-party surfaces excluded from ownership: `pkg/evals/`, `scripts/run-evals.sh`, repository tests/fuzz/benchmarks, CI/nightly/release workflows and maintainer/contributor governance. These may corroborate implementation properties but are not wired as organizational owners in ordinary Golum runtime operation.
- First-party operating / deployment modes considered: the interactive terminal TUI; fresh, resumed and recovered sessions; operator tool approvals; mid-turn steering and queued-item cancellation; abort/resume of suspended runs; session branch/fork navigation; model/tool configuration; automatic/manual compaction; memory and configured hooks/MCP tools.
- Recursion level: one Golum coding session around one workspace/task is the assessed organization. The model-backed coding actor is its S1. Tool calls, MCP operations, shell processes, reducers, queues and storage records are components rather than separate S1 units. In interactive TUI mode the human operator is a legitimate parent actor for the distinct current-control S3 mode over the active run and pending steering commitments.
- Reviewed revision: `ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Golum is a Go terminal coding agent. `AgentHarness.Prompt` durably starts a run and `RunAgentLoop` / `Driver` repeatedly derives the next action from append-only session records, streams the model, executes requested tools, persists results and feeds them back into subsequent model context. Built-in tools cover repository reads/search, edits/writes, shell execution, todos, configured MCP invocation and optional memory. Workspace/path/security enforcement and approvals constrain mutating operations.

The reducer and append-only orchestration log make execution resumable after interruption. Sessions persist to SQLite, can be resumed or forked, and record operations, tool starts/results, queue events and compactions. Context management prunes/summarizes when necessary while preserving full history. Procedural, episodic and semantic memory provide project/user instructions, turn-change/failure digests and a derived Go repository map.

The interactive TUI adds a parent current-control path. While a run is active, new operator input is persisted as a steering queue item and consumed at a subsequent model-step boundary. Pending steers are visibly listed and individually cancelable; Esc aborts the current stream/run, while suspended operations can be resumed or durably aborted. These controls alter the coding actor's current commitments but do not create another autonomous coding S1.

Model-backed evaluations under `pkg/evals` and the nightly workflow instantiate the harness for development/evaluation purposes. They are adjacent first-party evidence rather than a runtime audit actor inside the assessed standard-distribution boundary.

## Operational model

The main model-backed actor receives a coding request plus repository/context state, chooses coding tools, observes concrete results and revises subsequent actions until it returns a final answer or a bounded runtime condition ends the run. A request-scoped status message supplies workspace, model, tool/model-call counts, consecutive errors and todos; deterministic limits, loop detection, ForceTool directors, approval checks and execution confinement support or constrain the actor without owning its open-ended coding decisions.

The operator can govern the live interactive session's current direction by injecting a steer into the running operation, canceling a pending steer, aborting the active run, or deciding whether a recovered suspended operation resumes or is discarded. That parent path is distinct from ordinary per-tool approval: the S3 witness is current commitment control over the active/pending session, not the mere existence of an approval prompt.

## S1 — Operations

- State: A
- Function: autonomously perform coding work through model-selected repository/tool actions and iterative feedback.
- Disturbance / variety regulated: unfamiliar repository structure, source state, build/test/shell results, tool errors, changing task evidence, context pressure and interrupted execution.
- Decisive decision or feedback right: choose the next inspection/edit/command/tool action, interpret returned evidence, revise the approach and decide when the requested coding work is complete.
- Decision owner: the active model-backed Golum coding agent.
- Supporting / enforcement mechanisms: `AgentHarness`, `Driver`, reducer-derived action state, coding tools, workspace confinement, approvals, session persistence, compaction, memory, todos, loop limits, hooks and configured MCP access.
- Closure path: user task/context → model chooses action/tool → runtime executes and persists concrete result → result returns to model context → model changes subsequent work → repeat until answer, abort or bounded failure.
- Boundary reachability: the ordinary Golum TUI directly instantiates `AgentHarness` with the built-in tool registry and drives the same first-party model/tool loop.
- Why this is / is not agent-owned: removing the model actor while leaving reducers, persistence, limits and tools intact removes the discretionary coding choices that select actions and interpret evidence; the remaining machinery only transports, constrains or replays previously selected work.
- Evidence: [README.md](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/README.md); [pkg/harness/harness.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/harness/harness.go); [pkg/harness/driver.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/harness/driver.go); [pkg/tool/default.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/tool/default.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model providers supply inference, while first-party deterministic machinery persists and enforces the loop; neither fact transfers the agent's open-ended operational decision right to those support mechanisms.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established at the selected recursion.
- Disturbance / variety regulated: not established because the standard runtime exposes one model-backed coding S1 rather than multiple interacting operational S1 units with a concrete conflict or oscillation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: steering/follow-up queues, todos, session branches, ordered reducer actions, MCP invocation and hook/event transport.
- Closure path: not applicable; no distinct-S1 disturbance → coordination response → changed subsequent S1 behaviour loop was found.
- Why this is / is not agent-owned: queued operator messages coordinate a parent with one S1, while tools, shell processes and external MCP operations are not first-party autonomous coding S1 units.
- Evidence: [pkg/harness/queue.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/harness/queue.go); [pkg/harness/driver.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/harness/driver.go); [pkg/tool/invoke.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/tool/invoke.go); [README.md](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the prompt renderer can describe externally registered `subagent_*` tools, but the frozen standard distribution does not supply a first-party subagent implementation or a concrete inter-S1 attenuation path.

### Absence scope

- Surfaces inspected: harness action/reducer loop; built-in tool registry; queues/todos; session tree; hooks; MCP catalog/invocation; prompt tool rendering; TUI runtime; repository tree for first-party worker/subagent implementations.
- Plausible first-party paths checked: parallel coding workers, session branches as simultaneous S1s, queued messages as S1s, MCP services as S1s, hooks as coordinators, tool ordering and shared-state conflict control.
- Why no material first-party path remains: the assessed distribution contains one operational coding actor. Other concurrent or queued entities are inputs, tools, transport/state mechanisms or external dependencies, so the prerequisite distinct interacting S1 units and disturbance-specific attenuation loop are absent.

## S3 — Inside-and-now control

- State: P
- Function: regulate the interactive session's current commitments by allowing a parent operator to redirect, cancel or terminate active/pending work on behalf of the whole session.
- Disturbance / variety regulated: the coding actor may continue on an obsolete direction while the user's intent changes; a pending steer may become unnecessary; an interrupted run may need to be resumed or discarded; current work may need immediate termination rather than ordinary completion.
- Decisive decision or feedback right: decide whether and how the active coding run should be redirected or stopped, whether a queued steer remains a live commitment, and whether a recovered suspended operation should continue or be abandoned.
- Decision owner: the human user/operator as legitimate parent authority in the supported interactive TUI mode.
- Supporting / enforcement mechanisms: visible working/approval status, persisted steering queue records, queued-steer display with stable IDs, `/cancel`, Esc cancellation, `AbortContext`, `/resume-run`, `/abort-run`, session records and reducer replay.
- Closure path: TUI exposes active-run state plus pending steers/recovery state → operator selects steer/cancel/abort/resume decision → runtime persists or applies that decision → the next model step or operation state follows the returned parent decision.
- Boundary reachability: mid-turn input, queued-steer display, `/cancel`, Esc abort and suspended-run resume/abort are shipped first-party TUI/runtime features at the assessed boundary.
- Why this is / is not agent-owned: the runtime records and enforces the intervention, but the discretionary decision to redirect, retain, cancel, resume or abort current session commitments belongs to the operator; without the parent decision the same current-control intervention is not selected.
- Evidence: [README.md](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/README.md); [internal/ui/model.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/internal/ui/model.go); [internal/ui/commands.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/internal/ui/commands.go); [pkg/harness/queue.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/harness/queue.go); [pkg/harness/harness.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/harness/harness.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary y/n tool approval and static loop limits are not credited as S3. The positive witness is the recurring parent path over active and pending whole-session commitments. No autonomous or S3-specific constructor base mode is claimed.
- Whole-system current view: the TUI distinguishes an active working/approval/run state, visibly renders pending steer items with stable cancellation IDs, maintains current todos/tool events and detects recovered suspended operations.
- Current-control decision scope: redirect the live coding actor at a model-step boundary, remove a pending steering commitment, terminate the active run, and decide whether a suspended current operation resumes or is durably aborted.
- Parent mode: in interactive TUI operation the human operator owns these current-control choices; queue/session/reducer machinery transports and enforces the returned decision so subsequent operation changes accordingly.

## S3* — Complementary audit

- State: —
- Function: no material complementary and sufficiently independent runtime audit path was established.
- Disturbance / variety regulated: not established at S3* level.
- Decisive decision or feedback right: not established. The main coding actor can inspect its own tool/test results and persistent records, while model-backed `pkg/evals` and nightly evaluation run in adjacent development/evaluation surfaces rather than as an auditor wired into ordinary Golum control.
- Decision owner: not established.
- Supporting / enforcement mechanisms: append-only session/orchestration records, reducer validation/replay, episodic failure digests, observability, repository tests and the separate eval harness/nightly workflow.
- Closure path: not applicable; no complementary independent access → audit judgment → corrective return into the live assessed runtime was found.
- Why this is / is not agent-owned: logs/replay preserve operational truth but make no independent audit judgment. The eval harness can judge test runs, but it is separately invoked development/evaluation infrastructure and its verdict is not a first-party ordinary-runtime control owner.
- Evidence: [pkg/harness/session/record.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/harness/session/record.go); [pkg/harness/episodic.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/harness/episodic.go); [pkg/evals/README.md](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/evals/README.md); [.github/workflows/nightly.yml](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/.github/workflows/nightly.yml).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: strong event sourcing, replay and behavioral evals improve reliability and reviewability, but Methodology 0.3.6 does not equate observability/evaluation infrastructure with an in-boundary complementary audit owner.

### Absence scope

- Surfaces inspected: session/orchestration logs; reducer/replay/validation; crash recovery; episodic memory; runtime tool/test feedback; observability; `pkg/evals`; CI/nightly workflows; hooks.
- Plausible first-party paths checked: reducer consistency checking as audit, append-only replay as audit, separate reviewer/verifier actor, model-backed eval judge, nightly evaluation and operator transcript inspection.
- Why no material first-party path remains: in-boundary records and checks are the ordinary execution/recovery path, while sufficiently independent eval/judge infrastructure is adjacent and not wired back as a corrective audit loop in supported runtime operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective organizational adaptation loop was established.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. Procedural/episodic/semantic memory, project indexing, skills, model/tool configuration and external MCP access improve current-task context but do not generate and adopt future-oriented harness adaptations from environmental change.
- Decision owner: not established.
- Supporting / enforcement mechanisms: `AGENTS.md`/procedural memory, per-turn episodic digests, semantic Go-repository index, `/reindex`, static skills/templates, compaction, configurable model/tools and MCP invocation.
- Closure path: not applicable; no external/future distinction → adaptation option → adopted change to present organizational capability/control loop was found.
- Why this is / is not agent-owned: memory and indexing preserve/retrieve past or current evidence, while skills/configuration are operator/developer supplied. None closes an agent-owned prospective adaptation program.
- Evidence: [pkg/memory/memory.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/memory/memory.go); [pkg/memory/procedural.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/memory/procedural.go); [pkg/memory/semantic.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/memory/semantic.go); [README.md](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: external information can be reached through configured MCP services, but those services are dependencies and present-task research does not itself establish outside-and-then adaptation.

### Absence scope

- Surfaces inspected: all three memory tiers; semantic reindex; context compaction; skills/templates; model/tool configuration; MCP integration; hooks; runtime prompt; repository eval/development surfaces.
- Plausible first-party paths checked: memory as learning/adaptation, semantic reindex as environmental model, autonomous skill acquisition, model/provider switching, external research through MCP, eval-driven self-improvement and hook-driven capability mutation.
- Why no material first-party path remains: the reviewed runtime retrieves or reconfigures present capability but does not autonomously sense prospective environmental distinctions, develop adaptation options and install a selected option back into durable current capability.

## S5 — Policy and identity

- State: —
- Function: no material identity- or ultimate-policy-level closure was established inside the supported runtime.
- Disturbance / variety regulated: not established at S5 level; located prompt, approval, sandbox, path/security and configuration mechanisms constrain ordinary coding actions.
- Decisive decision or feedback right: no identity/ultimate-policy issue is routed to a legitimate ultimate authority and returned as a durable governing decision for subsequent Golum operation.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: system prompt identity/security text, AGENTS/project instructions, y/n mutating-tool approvals, workspace confinement, sensitive-path denial, loop limits, model/tool selection, hooks and operator configuration.
- Closure path: not applicable; ordinary approvals/configuration can change an action or session setting but do not form identity/policy issue → ultimate authority → authoritative decision → returned durable operation.
- Why this is / is not agent-owned: deterministic constraints enforce already-selected rules and the operator approves individual mutations; neither is an autonomous or parent-governed S5 closure at the assessed recursion.
- Evidence: [pkg/prompt/system.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/prompt/system.go); [internal/ui/approval.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/internal/ui/approval.go); [pkg/harness/harness.go](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/pkg/harness/harness.go); [README.md](https://github.com/Vignesh-Rajarajan/golum/blob/ca9a01c67e16b8093ef1abc4ed93d2407b5ef7af/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: repository maintainers and operators can change product/configuration policy outside the run, but those development/deployment authority paths are adjacent to the assessed runtime and do not supply a first-party S5 closure.

### Absence scope

- Surfaces inspected: system prompt; procedural instructions; approvals; execution/path security; loop limits/directors; model/tool configuration; hooks; TUI operator controls; repository governance/CI.
- Plausible first-party paths checked: system prompt as constitution, approvals as ultimate authority, AGENTS instructions as policy, hooks as policy constructor, user/operator as S5, maintainer governance as runtime identity closure.
- Why no material first-party path remains: all in-boundary mechanisms govern ordinary task execution or enforce preselected constraints, while project governance is outside the runtime boundary. No identity/ultimate-policy dispute is closed and returned as durable harness policy.

## Distributed OSS parent arrangement

Golum's positive parent-mode claim is local to one interactive coding session: the operator governs that session's current commitments. No organization-level distributed parent arrangement is inferred from repository contributors or maintainer governance.

## Self-hosted and non-human modes

Golum is locally operated and its TUI exposes the parent current-control mode credited for S3. No separate autonomous S3 base mode is established. No positive S4/S5 parent mode is inferred from generic operator configurability.

## Recursion

The focal recursive unit is one coding session. Session branches and forks preserve alternate histories but are not simultaneously operating viable units, and no first-party subagent population is supplied at the frozen revision. Tools and shell/MCP processes remain components/dependencies rather than recursive S1 organizations.

## Variety and escalation

The S1 actor absorbs coding variety through iterative model/tool feedback, durable recovery, context compaction, memory, todos and loop-error feedback. The interactive operator can return exceptional or changed current intent through steering/cancellation/abort, which is credited as parent-governed S3 only because the decision feeds back into the active/pending whole-session commitments. Tool approvals and hard limits remain local constraints rather than additional VSM functions.

## Evidence gaps

No `?` state is required. The frozen repository exposes the complete agent loop, TUI steering/recovery controls, session/reducer machinery, tool/runtime boundary, memory/context paths and adjacent eval surfaces sufficiently to support S1=A, S3=P and the negative S2/S3*/S4/S5 conclusions.

## Assessment summary

Golum closes autonomous S1 through its durable model/tool coding loop and exposes a parent-governed S3 mode through first-party TUI steering, queued-commitment cancellation and run abort/resume controls that return operator decisions into current execution. It does not supply multiple interacting first-party S1 units for S2, an in-boundary complementary auditor for S3*, a prospective adaptation loop for S4 or an identity/ultimate-policy closure for S5.
