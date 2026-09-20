---
harness_id: agent-orchestrator
project_name: Agent Orchestrator
repository: https://github.com/Untrivial-ai/agent-orchestrator
review_ref: 1e4a394b20c470d281b2a7f6f63fd47c30af5019
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-20
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Agent Orchestrator

## Review boundary

- System in focus: one first-party Agent Orchestrator project organization at pinned revision `1e4a394b20c470d281b2a7f6f63fd47c30af5019`, including AO's daemon/session manager, project orchestrator session, AO-managed coding-worker sessions and isolated worktrees, project/session/PR/CI/review state, messaging/delegation surfaces, first-party reviewer runtime and optional auto-review delivery path, plus the supported desktop/CLI control surfaces that expose the same organization.
- Purpose and identity: organize concurrent software-engineering work across a repository by giving coding tasks isolated autonomous workers, maintaining project-wide ownership/current state, allocating or redirecting work, routing CI/review feedback, and independently reviewing worker pull requests before returning actionable findings.
- Relevant environment: user goals and project priorities, repository state, provider-backed issues, worker outputs, pull requests, CI checks, review comments, external coding-agent/model providers and SCM providers.
- Standard-distribution boundary: AO owns project/session orchestration, worker/worktree lifecycle, state persistence, role prompts, worker messaging/control, PR/CI/review observation, reviewer orchestration and desktop/CLI surfaces. Claude Code, Codex, Aider, OpenCode and other supported agent harnesses, model providers, GitHub/GitLab and external tools remain execution/environment dependencies; their internal organizational functions are not inherited.
- Credited operating / distribution surfaces: project orchestrator sessions created by AO; AO worker sessions and per-worker git worktrees; `ao status`, `ao spawn`, `ao send`, session/PR control APIs; desktop project/Kanban/session views; first-party review engine/launcher/reviewer prompts; auto-review coordinator and lifecycle review delivery.
- Adjacent first-party surfaces excluded from ownership: repository CI/release workflows, test/e2e fixtures, landing-page demos, contributor/maintainer governance, generated API clients/specification code except where it documents a runtime route, and cloud/mobile presentation surfaces that merely render the same underlying AO state. External SCM review/CI judgments are environment evidence rather than AO-owned S3* unless produced by AO's own reviewer subsystem.
- First-party operating / deployment modes considered: local daemon + desktop/CLI project mode; persistent project orchestrator plus multiple AO workers; direct human supervision through project/Kanban/session surfaces; opt-in AO auto-review using the first-party reviewer subsystem.
- Recursion level: one AO-managed software project. Individual AO worker sessions are operational S1 units; the persistent project orchestrator regulates them at the next recursion. Reviewer sessions are complementary audit actors, not extra production S1 units for this mapping.
- Reviewed revision: `1e4a394b20c470d281b2a7f6f63fd47c30af5019`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

Agent Orchestrator is a local multi-agent software-engineering workspace/control plane. AO creates coding-worker sessions backed by supported coding-agent harnesses and gives Git-backed workers isolated branches/worktrees. The worker owns implementation, tests, commits and PR follow-up for its assigned task. AO owns the worker/session lifecycle, project association, durable current state, messaging, PR/CI/review observations and the role contract injected into its project orchestrator and workers.

The project orchestrator is a first-party persistent model session with an explicit coordination-only role. Its shipped system prompt requires it to inspect current project state, identify which worker owns each task or PR, avoid duplicate active work, choose whether to spawn or redirect workers, message or terminate sessions, route CI/review feedback to the responsible worker and summarize blockers for the human. The README describes the same role at product level: project-wide planning and coordination grounded in active workers, ownership, PRs, CI and reviews.

AO also contains a distinct code-review organization. Its review engine launches a separate reviewer runtime against a worker's worktree/PR head. The reviewer receives a read-only role: inspect diffs and evidence, do not edit files, run project code, commit or push, and return an `approved` or `changes_requested` verdict. In the supported auto-review mode, a daemon coordinator detects eligible idle workers/current PR heads, starts that reviewer, and the lifecycle reducer automatically injects current-head `changes_requested` findings back into the responsible worker. That is materially different from merely displaying external GitHub review state.

Primary evidence:

- [`README.md`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/README.md) — worker/worktree model, persistent project orchestrator, live project state, Kanban/operator view and project-level planning/coordination.
- [`backend/internal/session_manager/prompt.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/session_manager/prompt.go) — first-party orchestrator and worker standing roles, ownership checks, spawn/redirect/message/kill control and CI/review routing.
- [`backend/internal/service/session/delegation.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/service/session/delegation.go) — standard worker-spawn path and project-orchestrator integration.
- [`backend/internal/review/review.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/review/review.go) — review-run planning/persistence and separate reviewer orchestration.
- [`backend/internal/review/launcher.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/review/launcher.go) — separate reviewer runtime over the worker worktree and stable reviewer identity.
- [`backend/internal/review/prompt.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/review/prompt.go) — read-only reviewer role, evidence surface and machine-readable verdict submission.
- [`backend/internal/autoreview/coordinator.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/autoreview/coordinator.go) — periodic first-party auto-review trigger from current session/PR/review facts.
- [`backend/internal/service/review/review.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/service/review/review.go) and [`backend/internal/lifecycle/reactions.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/lifecycle/reactions.go) — current-head changes-requested filtering and automatic return of AO reviewer findings into worker operation.

## Operational model

A user or project workflow creates an AO worker for a bounded coding task. AO allocates an isolated workspace/worktree and launches a selected external coding-agent harness under AO's worker role. The worker independently interprets its assigned task, edits and tests the codebase, manages its branch/PR work and reacts to later messages, CI failures and review findings. That model-driven implementation loop is the operational S1.

Across workers, the persistent project orchestrator consumes live project and ownership state. It is instructed to detect existing ownership before spawning new work, redirect or message existing workers where appropriate, and keep implementation out of the orchestrator session itself. At the same time, AO structurally isolates workers in distinct worktrees. The model-owned ownership/duplication decisions establish agent-owned S2; worktree isolation is supporting enforcement for a second concrete cross-worker collision risk.

At the project recursion the same orchestrator has a broader current-control function: observe all active workers and PR/CI/review state, decide priorities/sequence/ownership and intervene through spawn, redirect, send and kill operations. The desktop/Kanban/operator mode supplies an alternative parent-governed closure: a human sees project-wide current state and can return task, feedback and intervention decisions through the same AO control surfaces.

When AO auto-review is enabled, an idle worker with a reviewable current PR head can trigger a separate reviewer runtime. The reviewer inspects the diff under a read-only role and records its own judgment. A `changes_requested` result for the current head is automatically delivered to the worker through the lifecycle reducer, creating a closed complementary-audit loop without borrowing an external human reviewer.

## S1 — Operations

- State: A
- Function: autonomously implement and verify one bounded software-engineering task in an AO-managed worker workspace and produce task/branch/PR outcomes.
- Disturbance / variety regulated: repository structure, implementation ambiguity, tool/test observations, task-specific failures, CI/review follow-up and direct messages relevant to the assigned task.
- Decisive decision or feedback right: choose implementation/tool actions and iterate on the assigned task within AO's project/workspace/publishing constraints.
- Decision owner: the model-driven coding-agent worker session launched and managed by AO.
- Supporting / enforcement mechanisms: AO session manager, selected harness adapter, isolated worker worktree/branch, task prompt/project rules, session persistence, messaging, PR association and lifecycle APIs.
- Closure path: assigned task/issue → AO worker session → model-driven code/tool/test actions → repository/tool/CI/review observations → further worker action → commits/PR/task result.
- Boundary reachability: AO's standard spawn/delegation surfaces directly create `KindWorker` sessions under the first-party worker role and project/worktree lifecycle; downstream code does not have to construct a new organizational loop. External coding-agent/model software supplies inference/execution substrate but does not supply the AO project organization credited above it.
- Why this is / is not agent-owned: implementation and local task choices are made by the running worker agent from current evidence rather than by the deterministic AO daemon or a human preauthoring each action.
- Evidence: [`README.md`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/README.md), [`backend/internal/session_manager/prompt.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/session_manager/prompt.go), [`backend/internal/service/session/delegation.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/service/session/delegation.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external coding-agent harnesses retain their own internal loop semantics; this assessment credits only the supported AO-managed operational path and does not import those harnesses' metasystem functions.

## S2 — Coordination

- State: A
- Function: attenuate overlapping worker ownership and concurrent repository-write interference among distinct coding-worker S1 units.
- Disturbance / variety regulated: duplicate workers acting on the same current task/PR and concurrent workers colliding through shared mutable repository state.
- Decisive decision or feedback right: decide whether new work needs a new worker versus an existing worker redirect/message, maintain visible ownership, and keep concurrent worker writes isolated.
- Decision owner: the persistent project orchestrator for ownership/duplicate-work attenuation; AO's deterministic worktree/session machinery enforces workspace isolation.
- Supporting / enforcement mechanisms: live worker/ownership state, `ao status`, worker/session lookup, `ao spawn`, `ao send`, worker redirect/kill surfaces, per-worker branches/worktrees and project-scoped session state.
- Closure path: current worker ownership + requested/new work → orchestrator inspects current state → spawn existing/new or redirect/message decision → AO session/worktree control → subsequent worker assignment and writes reflect that coordination decision.
- Boundary reachability: the first-party orchestrator system prompt mandates ownership inspection and duplicate avoidance and exposes the required AO commands in the standard project-orchestrator session; isolated worktrees are also standard AO worker behavior. No downstream coordinator policy has to be authored to obtain these relations.
- Why this is / is not agent-owned: worktree allocation alone would be deterministic support, but the positive `A` claim rests on the model orchestrator's explicit current ownership check and discretionary new-worker-versus-redirect decision over distinct live workers.
- Evidence: [`README.md`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/README.md), [`backend/internal/session_manager/prompt.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/session_manager/prompt.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic worker messaging and task delegation are not the basis. The credited S2 witness is specifically duplicate/overlap attenuation plus workspace collision isolation among concurrently viable workers.
- Distinct S1 units: concurrently active AO coding-worker sessions, each responsible for a bounded task or PR.
- Inter-S1 disturbance: two workers can duplicate ownership of the same task/PR or interfere through concurrent writes against one shared checkout/branch state.
- Attenuating coordination relation: the orchestrator must inspect ownership/current sessions before spawn and reuse/redirect/message a suitable active worker instead of duplicating work; AO additionally gives Git-backed workers isolated worktrees/branches.
- Feedback into subsequent S1 behaviour: the orchestrator's spawn/redirect/message choice changes which worker owns the work and what that worker does next, while AO's chosen workspace constrains subsequent writes.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the evidence names concrete cross-worker disturbances—duplicate active ownership and mutable-workspace collision—and first-party relations that suppress those disturbances before subsequent worker action.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate the project-wide current portfolio of worker commitments, priorities, ownership, blockers and PR/CI/review interventions.
- Disturbance / variety regulated: changing project priorities, concurrent worker capacity, duplicate/obsolete commitments, stuck workers, CI failures, requested review changes, task/PR ownership and sequencing across the whole current project.
- Decisive decision or feedback right: choose or revise which current work should exist, which worker owns it, whether to spawn/redirect/message/kill a worker and what current issue/CI/review feedback should be routed into that work.
- Decision owner: base `A` mode — the persistent model-driven project orchestrator; parent `P` mode — the human operator using AO's project-wide current view and task/session feedback/control surfaces.
- Supporting / enforcement mechanisms: project/orchestrator state, `ao status`, project Kanban/current worker view, session list/get, spawn/send/kill APIs, PR/CI/review state and persistent project conversation/history.
- Closure path: whole-project live state → orchestrator or parent current-control judgment → spawn/redirect/send/kill/task-feedback action → AO updates/contacts the relevant worker → subsequent project commitments/current operation change.
- Boundary reachability: AO creates the persistent project orchestrator as a supported first-party session with the current-control role and commands already injected. The desktop/project/Kanban surfaces expose the same current project state and worker controls to the human parent without requiring a downstream control plane.
- Why this is / is not agent-owned: the base mode is more than deterministic scheduling: the model orchestrator is explicitly told to reason over ownership, priorities, blockers, CI/reviews and select interventions. The parent mode is separately closed because the human sees the same whole-project state and can return actionable current decisions through AO.
- Evidence: [`README.md`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/README.md), [`backend/internal/session_manager/prompt.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/session_manager/prompt.go), [`backend/internal/httpd/controllers/sessions.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/httpd/controllers/sessions.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: daemon/session lifecycle mechanics, concurrency enforcement and status persistence support S3 but are not independently treated as autonomous current-control owners.
- Whole-system current view: project orchestrator/desktop state combines active workers, ownership, tasks/PRs, CI, reviews and blockers across the project rather than one worker only.
- Current-control decision scope: assign or revise worker commitments and priorities, avoid duplicate active work, redirect/message stuck or existing workers, spawn additional workers and terminate sessions where appropriate.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | persistent project orchestrator agent | user/project request or changed live worker/PR/CI/review state | whole-project state → model current-control judgment → AO spawn/redirect/send/kill → changed worker commitments | `README.md`; `backend/internal/session_manager/prompt.go` |
| Parent (`P`) | human operator at the project recursion | Kanban/project view, worker blocker/needs-you state, direct project conversation or inspection of worker/PR/CI/review state | whole-project view → human task/feedback/intervention decision → AO orchestrator/session control surface → changed current worker operation | `README.md`; AO project/session APIs |

## S3* — Complementary audit

- State: A
- Function: independently challenge the correctness/readiness of worker PR output through a separate read-only reviewer and return adverse findings into the responsible worker.
- Disturbance / variety regulated: worker implementation defects, missing error handling/security/test coverage/convention violations and other discrepancies that ordinary worker self-report or CI may not reveal.
- Decisive decision or feedback right: inspect the worker's PR diff/base evidence under the reviewer role and decide `approved` versus `changes_requested` with concrete findings.
- Decision owner: a separately launched model-driven AO reviewer session under the configured reviewer harness.
- Supporting / enforcement mechanisms: review engine/run store, stable reviewer handle, reviewer-specific system/task prompts, PR/head selection, auto-review coordinator, review result persistence, current-head delivery filter and lifecycle `sendOnce` nudge.
- Closure path: eligible idle worker + current PR head → separate AO reviewer reads diff/evidence → reviewer submits verdict/findings → service keeps current-head `changes_requested` results → lifecycle `ApplyReviewBatch` sends findings to worker → worker receives corrective work order and subsequent implementation changes can follow.
- Boundary reachability: AO ships the reviewer engine, reviewer adapters/runtime launcher, auto-review coordinator, reviewer role and lifecycle delivery. Enabling the first-party auto-review mode on a session/project is sufficient to close the path; no external reviewer agent organization or custom corrective bridge is required.
- Why this is / is not agent-owned: the audit judgment is made by the independent reviewer model session, not by deterministic CI parsing or the worker being audited; AO then closes the returned finding into the worker automatically.
- Evidence: [`backend/internal/review/review.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/review/review.go), [`backend/internal/review/launcher.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/review/launcher.go), [`backend/internal/review/prompt.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/review/prompt.go), [`backend/internal/autoreview/coordinator.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/autoreview/coordinator.go), [`backend/internal/service/review/review.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/service/review/review.go), [`backend/internal/lifecycle/reactions.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/lifecycle/reactions.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary external GitHub review and CI observations are not credited as AO-owned S3*. The positive result rests on AO's own separate reviewer subsystem and the supported auto-review/delivery closure.
- Claim being audited: the worker's current PR/implementation is correct and ready enough to proceed without reviewer-requested changes.
- Ordinary reporting path: worker implementation, tests/commits/PR output, session status and normal PR/CI state observed by AO.
- Complementary access path: a separate reviewer process reads the worker worktree and PR diff against its base under reviewer-only instructions and submits an independent review verdict/body.
- Independence boundary: reviewer has a distinct runtime identity and prompt role and is explicitly forbidden to edit, stage, commit, push, switch branches or run project programs/tests/builds/installers/generators; it challenges evidence rather than producing the implementation.
- Who acts on findings: AO lifecycle delivery routes current-head `changes_requested` findings back to the responsible worker, which performs the corrective implementation; the project orchestrator/human can additionally observe the review state.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party prospective environment-sensing and capability-adaptation loop established at this project recursion.
- Disturbance / variety regulated: not established.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persistent project conversation/history, repository context, issue/PR/CI/review inputs and planning prompts provide current work context but do not by themselves own future capability adaptation.
- Closure path: no qualifying sensing → adaptation-option selection → return into reusable future capability path established.
- Boundary reachability: not applicable — no positive S4 ownership path is credited.
- Why this is / is not agent-owned: the project orchestrator can plan future project work, but planning current/future deliverables is not evidence that AO adapts the organization's reusable capability from prospective environmental intelligence.
- Evidence: [`README.md`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/README.md), [`backend/internal/session_manager/prompt.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/session_manager/prompt.go).
- Basis: explicit absence after boundary review.
- Confidence: medium-high.
- Caveats: model agents may use web/tools in individual tasks, but that is operational task work unless a separate prospective adaptation closure is shown.

### Absence scope

- Surfaces inspected: README project-orchestrator description; project/orchestrator and worker standing prompts; persistent project state/history; issue/PR/CI/review integration; review/auto-review subsystem; session/delegation runtime.
- Plausible first-party paths checked: project strategy/planning, persisted orchestrator reasoning/history, external tracker/review/CI inputs, reviewer history and session/runtime configuration.
- Why no material first-party path remains: all inspected paths either regulate current software-delivery work, preserve context, or audit current outputs; none establishes an AO-owned prospective environmental sensing judgment that selects and returns a reusable capability/organizational adaptation.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity / ultimate-policy closure established at the declared project recursion.
- Disturbance / variety regulated: not established as S5.
- Decisive decision or feedback right: not established.
- Decision owner: none established for a qualifying S5 loop.
- Supporting / enforcement mechanisms: project rules, worker/orchestrator standing prompts, publishing scope, harness/model selection, permission modes and explicit user restrictions constrain action but are authored/configured operating policy rather than a demonstrated identity/ultimate-policy decision loop.
- Closure path: no qualifying identity/policy issue → ultimate authority decision → returned governance of subsequent operation loop established.
- Boundary reachability: not applicable — no positive S5 ownership path is credited.
- Why this is / is not agent-owned: the orchestrator follows project/user policy and may reason about product direction, but evidence does not show it owns ultimate organizational identity or policy authority; human configuration/requests likewise do not by themselves establish a complete parent S5 loop.
- Evidence: [`backend/internal/session_manager/prompt.go`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/backend/internal/session_manager/prompt.go), [`README.md`](https://github.com/Untrivial-ai/agent-orchestrator/blob/1e4a394b20c470d281b2a7f6f63fd47c30af5019/README.md).
- Basis: explicit absence after boundary review.
- Confidence: high.
- Caveats: parent-governed S3 does not imply parent-governed S5; current-control authority and ultimate identity/policy authority are separate functions.

### Absence scope

- Surfaces inspected: project/worker/orchestrator prompts and rules, publishing restrictions, permission/model/harness configuration, project settings, human-facing project control and planning surfaces.
- Plausible first-party paths checked: product-direction discussion, user restrictions, project rules, publishing authority, model/harness selection and permission/approval configuration.
- Why no material first-party path remains: these surfaces supply goals and constraints or authorize particular actions; no inspected path reconstructs an ultimate identity/policy issue, legitimate S5 decision owner and authoritative return that governs the organization as a whole.

## Distributed OSS parent arrangement

The assessment is of a runnable AO project organization, not the upstream repository-development organization. Maintainers/contributors governing Agent Orchestrator source are outside the assessed operating boundary and are not used to justify parent-mode notation. The `P` mode on S3 is local to the supported project/operator recursion: a human sees current project state and returns current-control decisions into AO-managed workers.

## Self-hosted and non-human modes

The local/self-hosted project mode is the primary reviewed mode. It supports both a model-owned project orchestrator and direct human project supervision. Optional auto-review is credited because the first-party mode closes reviewer trigger, independent judgment and corrective delivery after enablement; the fact that a user can choose whether to enable that mode does not transfer the reviewer judgment to the user.

## Recursion

At the worker recursion, a coding-agent session regulates one implementation task. At the project recursion, the persistent AO orchestrator coordinates and regulates multiple workers and their current PR/CI/review commitments. The reviewer is a complementary audit role against worker output at the project recursion. External model/harness providers and SCM systems are environment/substrate rather than parent organizational owners for this mapping.

## Variety and escalation

AO absorbs operational variety by giving workers isolated contexts/worktrees, maintaining explicit ownership and letting the project orchestrator allocate or redirect work from live project state. CI and review findings are returned to the responsible worker rather than requiring the human to continuously poll every session. Human escalation remains available through the project conversation, Kanban/session inspection and intervention surfaces, establishing the S3 parent mode without converting ordinary approvals or configuration into S5.

## Evidence gaps

The pinned revision provides strong direct evidence for S1/S2/S3/S3* ownership and closure. No runtime trace was available in this review beyond repository source/docs/tests, so the assessment does not claim S4 from strategic planning/history or S5 from project rules/user authority. A later revision adding a first-party adaptation/evolution loop or explicit identity/ultimate-policy process would require new-ref reassessment rather than inference here.
