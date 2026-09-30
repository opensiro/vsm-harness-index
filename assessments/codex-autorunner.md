---
harness_id: codex-autorunner
project_name: codex-autorunner (CAR)
repository: https://github.com/Git-on-my-level/codex-autorunner
review_ref: 065f435d6120f95135425d8cc2df52760872a2d3
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# codex-autorunner (CAR)

## Review boundary

- System in focus: CAR's shipped hub/meta-harness organization at frozen revision `065f435d6120f95135425d8cc2df52760872a2d3`, including the hub control plane, PMA coordination path, managed threads, ticket-flow engine, repository/worktree lifecycle, agent adapters, durable orchestration state, recovery supervisor, Web/CLI/chat surfaces and first-party automation wiring.
- Purpose and identity: coordinate long-running coding-agent work across repositories and worktrees, preserve durable control state, route work into configured agent runtimes, isolate implementation cells, recover/pause failed work and escalate blocked decisions to the operator.
- Relevant environment: operator goals and replies; managed repositories and Git/worktree state; ticket queues and contextspace; configured Codex/Hermes/OMP/OpenCode/ACP runtimes; agent outputs and failures; hub/repo durable state; chat/file ingress; automation events; SCM state and external provider/runtime availability.
- Standard-distribution boundary: CAR's engine, control plane, adapters and supported surfaces are inside. Configured coding-agent runtimes are reachable operational actors in CAR's supported assembled mode, but their internal reasoning/tool-loop semantics remain external and are not inherited as CAR implementation evidence. External model/provider services, SCM hosts and chat transports remain dependencies.
- Credited operating / distribution surfaces: `README.md`; `docs/AGENT_SETUP_GUIDE.md`; `docs/ARCHITECTURE_BOUNDARIES.md`; `docs/car_constitution/20_ARCHITECTURE_MAP.md`; `src/codex_autorunner/docs/overview.md`; `src/codex_autorunner/docs/managed-threads.md`; `src/codex_autorunner/core/pma_prompt_builder.py`; `src/codex_autorunner/tickets/runner.py`; `src/codex_autorunner/core/flows/supervisor.py`; shipped Hub/Web/CLI/chat composition that wires these components.
- Adjacent first-party surfaces excluded from ownership: repository-development `AGENTS.md`/`CLAUDE.md`, CI/release workflows, tests/benchmarks, contributor governance, documentation-only architectural claims not reachable in the product, and external worker-agent internals beyond the concrete CAR adapter/session boundary.
- First-party operating / deployment modes considered: recommended self-hosted hub mode; hub PMA mode; managed-thread mode including PR-mode worktrees; ticket-flow autorunner; direct Web/CLI operator control; Telegram/Discord interaction; recovery/restart and automation/subscription paths.
- Recursion level: one CAR hub organization supervising its managed repo/worktree execution cells. A managed thread or active ticket-flow agent session is treated as an S1 work cell because it performs repository-facing work through a configured autonomous coding-agent runtime. The internal organization of Codex/Hermes/OMP/OpenCode is outside this assessment; only the operational cell exposed through CAR is used.
- Reviewed revision: `065f435d6120f95135425d8cc2df52760872a2d3`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

CAR explicitly describes itself as a meta-harness rather than a coding agent. The hub is the control plane; repositories and worktrees are execution workspaces; PMA is the hub-level coordinator. The architecture separates Engine, Control Plane, Adapters and Surfaces. The engine owns lifecycle/state transitions, scheduling, locks, queues and deterministic semantics; the control plane owns durable plans, snapshots, outputs and run metadata; adapters translate external agent/chat/SCM activity; surfaces render state and collect operator input.

The ordinary operational path is concrete rather than documentation-only. `TicketRunner.step` selects the first active ticket, builds bounded context, resolves the configured agent/profile, executes one agent turn through the first-party agent pool, captures Git/runtime state, reconciles the result and either continues, completes, retries or pauses. Agent runtimes remain separate dependencies, but CAR's standard setup requires at least one supported autonomous agent and directly routes ticket or managed-thread work into it.

Hub PMA is a materially agentic control path. `pma_prompt_builder.py` supplies a hub snapshot and first-turn control routine: process blocked/paused runs first; inspect current managed threads; reuse a relevant active thread or spawn a new one; choose managed thread versus ticket-flow organization; create PR-mode worktrees; manage subscriptions/timers; route new files; and escalate ambiguous dirty-worktree or ownership cases instead of guessing. PMA therefore has both a hub-level current view and first-party commands that alter current commitments.

Managed-thread PR mode creates a fresh hub-owned worktree from the repository default branch and retains thread lifecycle/progress/subscription visibility. This is a first-party structural isolation primitive for concurrent implementation cells. It attenuates the concrete Git/filesystem interference that would arise if independent coding-agent cells edited the same checkout. PMA additionally sees active managed threads and is instructed to reuse an existing relevant thread rather than duplicate a cell.

Ticket-flow recovery is separately runtime-owned. The flow supervisor observes worker health, backend state, commit barriers and restart policy, then emits typed recovery effects such as lifecycle transitions, restart attempts, notifications and crash artifacts. These deterministic mechanisms support current control, but do not become agent-owned merely because they enforce PMA/operator decisions.

The direct operator mode is also first-party. The Web Hub is the primary management interface for adding repositories, creating/managing tickets, monitoring agent runs and chatting with PMA; CLI/surface commands expose start/resume/stop/thread/ticket operations. This gives the human operator a distinct supported parent-governed current-control mode in addition to autonomous PMA control.

Primary evidence:

- [`README.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/README.md)
- [`docs/AGENT_SETUP_GUIDE.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/docs/AGENT_SETUP_GUIDE.md)
- [`docs/ARCHITECTURE_BOUNDARIES.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/docs/ARCHITECTURE_BOUNDARIES.md)
- [`docs/car_constitution/20_ARCHITECTURE_MAP.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/docs/car_constitution/20_ARCHITECTURE_MAP.md)
- [`src/codex_autorunner/docs/overview.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/docs/overview.md)
- [`src/codex_autorunner/docs/managed-threads.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/docs/managed-threads.md)
- [`src/codex_autorunner/core/pma_prompt_builder.py`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/core/pma_prompt_builder.py)
- [`src/codex_autorunner/tickets/runner.py`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/tickets/runner.py)
- [`src/codex_autorunner/core/flows/supervisor.py`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/core/flows/supervisor.py)

## Operational model

CAR's S1 outcomes are produced by managed agent work cells: a configured autonomous coding-agent runtime receives a managed-thread prompt or ticket-flow prompt, acts on a repository/worktree and returns progress/result state through CAR. CAR does not claim the external agent's internal reasoning as first-party implementation, but the shipped CAR deployment concretely instantiates and supervises those agent actors.

At hub recursion, CAR supplies two metasystemic paths. First, deterministic worktree/lifecycle machinery isolates concurrent implementation cells and prevents shared-checkout interference. Second, PMA receives a cross-hub operational snapshot and exercises discretionary current control: triaging blocked work, reusing or spawning cells, choosing the execution form, creating PR-mode cells, resuming or retiring work and arranging future wake-ups. Direct Web/CLI operation supplies a separate parent-governed mode for the same current-control function.

## S1 — Operations

- State: A
- Function: execute repository-facing implementation, review, debugging or other agent work inside a CAR-managed repo/worktree cell.
- Disturbance / variety regulated: repository state, code/test/tool feedback, task-specific implementation choices, runtime failures, changing evidence encountered by the configured coding agent and user replies during paused work.
- Decisive decision or feedback right: choose the next task-specific coding/tool action within the active managed thread or ticket-flow turn and revise later action from returned repository/tool evidence.
- Decision owner: the configured autonomous coding-agent actor (Codex, Hermes, OMP, OpenCode or another supported ACP agent) reached through CAR's shipped managed-thread/ticket-flow adapter path.
- Supporting / enforcement mechanisms: CAR ticket selection and prompt assembly; managed-thread lifecycle; agent adapters; contextspace; durable transcripts/run state; Git/worktree setup; ticket limits; pause/retry/recovery; permission/runtime configuration.
- Closure path: ticket/thread objective + CAR context → configured autonomous agent chooses repository/tool action → action executes in the bound workspace → result/progress returns through the agent session and CAR state → the same active agent cell continues, completes or dispatches a pause/escalation.
- Boundary reachability: hub setup explicitly requires a working supported agent, and shipped managed-thread/ticket-flow commands route work into those agents; no application-written integration is required to obtain the autonomous operational cell.
- Why this is / is not agent-owned: removing the configured autonomous agent while retaining CAR's ticket files, queues, worktrees and state machines leaves control infrastructure but no open-ended repository-facing operational discretion. The agent therefore owns the S1 task decision right even though its internal runtime is an external dependency.
- Evidence: [`README.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/README.md); [`docs/AGENT_SETUP_GUIDE.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/docs/AGENT_SETUP_GUIDE.md); [`src/codex_autorunner/tickets/runner.py`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/tickets/runner.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this claim credits the autonomous actor only where CAR concretely invokes it. It does not import the external agent runtime's internal delegation, planning, policy or audit functions into CAR.

## S2 — Coordination

- State: C
- Function: attenuate filesystem/Git interference among independently active coding-agent work cells by assigning implementation work to isolated hub-owned worktrees and maintaining explicit resource/thread bindings.
- Disturbance / variety regulated: two independent implementation cells against the same repository can otherwise contend over one checkout, branch, dirty working tree and transient repository state.
- Distinct S1 units: concurrently active managed threads or ticket-flow cells bound to separate repository/worktree resources, each executing a configured autonomous coding agent toward its own outcome.
- Inter-S1 disturbance: concurrent coding cells that share one mutable checkout can overwrite, observe or block one another's uncommitted state and branch operations; CAR's PR-mode path is structurally designed to avoid that shared-workspace collision.
- Attenuating coordination relation: PR-mode managed-thread creation provisions a fresh hub-owned worktree from `origin/<default-branch>` (or configured base) and binds the thread to that managed resource; PMA is instructed to reuse a relevant existing active thread rather than blindly duplicate work.
- Feedback into subsequent S1 behaviour: the managed-resource/thread binding determines the filesystem and branch state seen by the agent cell for all subsequent turns. Existing active-thread state is surfaced to PMA before it chooses reuse versus spawning another isolated cell.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive claim is not based on having queues or multiple agents. It is the concrete anti-interference relation `independent implementation cell → isolated worktree/resource binding → later actions constrained to that workspace`, plus current active-thread visibility used before another cell is created.
- Decisive decision or feedback right: establish and preserve the isolated managed-resource binding for a new PR-mode implementation cell rather than allowing independent cells to share the same mutable checkout.
- Decision owner: deterministic first-party CAR worktree/thread lifecycle. PMA/operator selects the work to run, while CAR supplies and enforces the S2-specific isolation primitive.
- Supporting / enforcement mechanisms: hub manifest/resource identity; managed-thread lifecycle records; PR-mode worktree creation; workspace setup; durable thread bindings; architecture rule that isolation is structural.
- Closure path: request for an independent PR-mode work cell → CAR creates/binds a fresh managed worktree → agent executes subsequent turns only in that resource → lifecycle/progress remain associated with that binding → later PMA/operator decisions observe the managed-cell state.
- Boundary reachability: PR mode is a documented shipped `car pma thread spawn ... --pr` path and the Web/CLI hub manages the resulting worktree directly; the coordination path is not a user-authored plugin.
- Why this is / is not agent-owned: the PMA may decide that a new PR work cell is appropriate, but the decisive anti-interference rule and worktree binding are runtime semantics. Removing PMA model judgment does not remove the first-party isolation path, so publication is `C`, not `A`.
- Evidence: [`src/codex_autorunner/docs/managed-threads.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/docs/managed-threads.md); [`src/codex_autorunner/core/pma_prompt_builder.py`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/core/pma_prompt_builder.py); [`docs/ARCHITECTURE_BOUNDARIES.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/docs/ARCHITECTURE_BOUNDARIES.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: the credited S2 witness is workspace/Git interference attenuation. No claim is made that CAR autonomously negotiates semantic disagreements or merge conflicts among independent agents.

## S3 — Inside-and-now control

- State: A(P)
- Function: maintain a hub-level view of current operational commitments and intervene over which work cell continues, is reused, is spawned, is restarted/resumed, is retired, or is escalated to the operator.
- Disturbance / variety regulated: blocked/paused/dead runs; duplicate or stale managed threads; changing workload across repos/worktrees; current delivery/file inboxes; dirty-worktree ambiguity; execution-form choice; active subscriptions/timers; resource and commitment continuity after failures.
- Whole-system current view: PMA receives `hub_snapshot` and explicit current surfaces for run dispatches, managed threads, inbox/file state, managed resources and automation. The hub itself owns the manifest, PMA state, managed-thread records and orchestration metadata across repositories/worktrees.
- Current-control decision scope: PMA is instructed to handle blocked runs first, choose inspect/reply/restart actions, reuse a relevant active thread or spawn a new one, choose managed thread versus ticket flow, create PR-mode cells, compact/retire threads, route files and configure automation/subscriptions for continuing work. These decisions change present commitments rather than merely report them.
- Decisive decision or feedback right: in PMA mode, choose the current intervention/delegation action over the hub's active work population; in direct operator mode, the human chooses equivalent current-control actions through the Hub/Web/CLI surfaces.
- Decision owner: base mode — PMA autonomous agent; parent mode — human hub operator.
- Supporting / enforcement mechanisms: hub snapshot/read models; durable orchestration/thread/ticket state; lifecycle reducer and supervisor; worktree creator; CLI/Web commands; restart policy; commit barriers; notification delivery.
- Closure path: current hub state → PMA or operator identifies a current-control need → spawn/send/reuse/resume/restart/retire/pause or related command → CAR mutates durable orchestration/workspace state → subsequent worker execution and later hub snapshots reflect the new commitment state.
- Boundary reachability: PMA is a shipped hub-level coordinator with first-party prompt, snapshot and CAR command surfaces; direct Web/CLI operation is the recommended self-hosted management surface. Both modes are reachable without custom application code.
- Why this is / is not agent-owned: in PMA mode, removing the PMA actor while leaving supervisors, queues and UI intact removes the discretionary choice among relevant current interventions; deterministic supervisors still enforce recovery policy but do not choose the broader work priority/delegation response. In direct operator mode the same class of decision is intentionally parent-owned.
- Evidence: [`src/codex_autorunner/docs/overview.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/docs/overview.md); [`src/codex_autorunner/core/pma_prompt_builder.py`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/core/pma_prompt_builder.py); [`docs/AGENT_SETUP_GUIDE.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/docs/AGENT_SETUP_GUIDE.md); [`src/codex_autorunner/core/flows/supervisor.py`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/core/flows/supervisor.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic ticket ordering, restart limits, commit barriers and state reducers are enforcement/support, not autonomous S3 ownership. The `A` claim is specifically the PMA whole-hub discretionary path; the parent mode is specifically the supported direct operator control path.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | PMA autonomous agent | hub snapshot exposes blocked/current work or the user requests new hub work | PMA chooses a current-control action and invokes CAR-native thread/ticket/worktree/automation commands; durable hub state and subsequent operation change | [`pma_prompt_builder.py`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/core/pma_prompt_builder.py), [`overview.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/docs/overview.md) |
| Parent (`P`) | human hub operator | operator observes current hub/repo/worktree/run state or receives a blocked-run escalation | operator creates/changes tickets, starts/stops/resumes work or replies through first-party Web/CLI/chat surfaces; CAR applies the decision to current execution | [`AGENT_SETUP_GUIDE.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/docs/AGENT_SETUP_GUIDE.md), [`README.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/README.md) |

## S3* — Complementary audit

- State: —
- Function: no boundary-reachable complementary audit path was established that is sufficiently independent of ordinary CAR/PMA/worker reporting and returns an audit judgment into current-control correction.
- Disturbance / variety regulated: not established as a distinct complementary-audit function. CAR has logs, run history, crash artifacts, tests, Git state and optional review work, but these are ordinary evidence/operations unless separately organized into an independent challenge loop.
- Decisive decision or feedback right: not established for an independent auditor.
- Decision owner: not established at S3*.
- Supporting / enforcement mechanisms: run history; durable orchestration records; crash artifacts; Git-state capture; commit barriers; CI/tests; operator review; PMA inspection; user-authored review tickets/managed threads.
- Closure path: no standard first-party path was found in which a materially independent auditor obtains complementary access, issues an audit judgment and automatically/operationally returns that judgment to change S3 commitments.
- Why this is / is not agent-owned: review can be assigned to agents or humans, but the shipped product does not make a sufficiently independent complementary auditor with corrective return part of the standard organization.
- Evidence: [`docs/car_constitution/20_ARCHITECTURE_MAP.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/docs/car_constitution/20_ARCHITECTURE_MAP.md); [`src/codex_autorunner/core/flows/supervisor.py`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/core/flows/supervisor.py); [`docs/car-ticket-skill.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/docs/car-ticket-skill.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: a user can compose an independent review workflow from managed threads/tickets; generic composability is not a positive S3* state.

### Absence scope

- Surfaces inspected: README; architecture/boundary docs; PMA overview/prompt; managed-thread and ticket-flow paths; lifecycle supervisor/recovery; run-history/state descriptions; ticket guidance; operator surfaces and adjacent tests/CI concepts.
- Plausible first-party paths checked: PMA inspection of worker state; final human-review tickets; separate review managed threads; run/crash artifacts; commit barriers; Git-state checks; CI/test verification; recovery supervisor decisions.
- Why no material first-party path remains: the reviewed paths either belong to routine operational/control reporting, deterministic recovery/enforcement, or user-composed review. None supplies a standard complementary independent audit judgment plus returned corrective-control closure at the declared hub recursion.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-then intelligence loop was established that senses external/future distinctions, develops adaptation options and returns a selected option into present CAR capability/S3.
- Disturbance / variety regulated: CAR reacts to current requests, run failures, files, SCM/chat events and scheduled wake-ups, but these are current operational/control events rather than a prospective environmental-intelligence function.
- Decisive decision or feedback right: not established for prospective adaptation.
- Decision owner: not established at S4.
- Supporting / enforcement mechanisms: PMA memory/context docs; automation/subscriptions/timers; SCM follow-up; agent/provider configuration; templates; contextspace; update/runtime state.
- Closure path: no first-party path was found from external/future sensing → adaptation-option generation → adaptation judgment → changed current organizational capability.
- Why this is / is not agent-owned: PMA can reason about a user's present request and schedule future wake-ups, but scheduling, memory and event reaction do not establish the Profile's external-and-prospective adaptation loop.
- Evidence: [`src/codex_autorunner/core/pma_prompt_builder.py`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/core/pma_prompt_builder.py); [`src/codex_autorunner/docs/overview.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/docs/overview.md); [`README.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/README.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: an external agent run may itself research future options, but that task-level behavior is not a standard CAR S4 closure unless CAR wires it into a prospective organizational adaptation loop.

### Absence scope

- Surfaces inspected: PMA prompt and durable docs; automation/timer/subscription paths; SCM/chat integration descriptions; ticket/contextspace semantics; hub/repo architecture; agent/runtime configuration and operator surfaces.
- Plausible first-party paths checked: scheduled automations; PMA context/memory; GitHub review/CI follow-up; file/chat event handling; contextspace updates; provider/agent selection; template use and generic agent research capability.
- Why no material first-party path remains: these mechanisms preserve continuity or react to present events. The pinned standard distribution does not establish an external-and-prospective intelligence conversation that generates adaptation options and closes them back into present organizational capability.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy closure was established at the CAR hub recursion.
- Disturbance / variety regulated: operator configuration, permissions, ticket rules, PMA guidance and codebase architecture constrain operation, but they do not constitute an identity-level decision process in the assessed runtime.
- Decisive decision or feedback right: not established for identity or ultimate policy.
- Decision owner: not established at S5.
- Supporting / enforcement mechanisms: hub/repo configuration; PMA `AGENTS.md`/active context; ticket frontmatter and acceptance criteria; architecture constitution; permissions/credentials; operator Web/CLI controls; static runtime limits and policy checks.
- Closure path: no standard first-party path was found by which an identity/ultimate-policy issue is detected or proposed, reaches a legitimate ultimate authority as such, receives an authoritative identity/policy decision and returns to govern later CAR operation.
- Why this is / is not agent-owned: PMA and the operator have substantial current-control discretion, but that is S3 scope. Editing configuration, instructions, permissions or tickets does not by itself establish S5.
- Evidence: [`docs/ARCHITECTURE_BOUNDARIES.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/docs/ARCHITECTURE_BOUNDARIES.md); [`src/codex_autorunner/core/pma_prompt_builder.py`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/src/codex_autorunner/core/pma_prompt_builder.py); [`docs/AGENT_SETUP_GUIDE.md`](https://github.com/Git-on-my-level/codex-autorunner/blob/065f435d6120f95135425d8cc2df52760872a2d3/docs/AGENT_SETUP_GUIDE.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: maintainers and operators obviously retain real-world authority over the OSS project and local deployment, but no function-specific first-party S5 closure is reconstructed from that fact alone.

### Absence scope

- Surfaces inspected: runtime architecture; PMA guidance/state; hub/repo configuration; ticket/control-plane semantics; operator surfaces; architecture constitution; permissions/credentials; contributor/CI/release surfaces as adjacent evidence.
- Plausible first-party paths checked: PMA changing operating instructions; operator configuration/approval; ticket policy; permissions and credentials; maintainer architecture rules; escalation from paused runs to humans.
- Why no material first-party path remains: all inspected runtime paths concern current task/control constraints, ordinary configuration or project-development governance. None establishes an identity/ultimate-policy issue-and-return loop at the assessed CAR hub recursion.

## Distributed OSS parent arrangement

The public repository has maintainer/contributor governance, but the positive parent-mode claim in this assessment does not rely on organization-level OSS governance. `S3=A(P)` uses the local self-hosted hub operator as the legitimate parent for a concrete CAR deployment. Contributor/release decisions remain adjacent to the runtime boundary and do not create S4/S5 parent modes here.

## Self-hosted and non-human modes

CAR is primarily self-hosted. In PMA mode, a configured autonomous agent owns the hub-level S3 intervention decision while deterministic CAR mechanisms enforce lifecycle/worktree/recovery effects. In direct Web/CLI operation, the human hub operator owns those current-control decisions and the same first-party state/action surfaces return them into execution. This supports the S3 parent modifier only; generic operator access does not create parent S4 or S5.

## Recursion

The assessed recursion is the hub-level CAR organization. Managed agent threads and ticket-flow sessions are subordinate operational cells coupled to repo/worktree environments. A configured external coding agent can itself contain richer internal orchestration, but that lower recursion is outside CAR's first-party boundary and is not imported into this vector.

## Variety and escalation

CAR attenuates operational variety through tickets, contextspace, managed-resource bindings, durable state, worktree isolation, bounded ticket turns, commit barriers and typed recovery. PMA amplifies regulatory variety by receiving a hub snapshot and choosing among CAR-native interventions. Failures or ambiguity that exceed safe automatic recovery become pauses/dispatches/notifications to the operator; the returned reply or direct operator action can resume current work. This is primarily S3 escalation, not S5 merely because a human is final for the intervention.

## Evidence gaps

- The assessment does not claim semantic-conflict negotiation or merge-conflict resolution as S2; only the structurally evidenced workspace/Git interference attenuation is credited.
- External worker-agent internals are intentionally excluded. Only autonomy reachable through CAR's concrete managed-thread/ticket-flow integration is used for S1.
- No standard complementary audit, prospective adaptation, or identity-level closure was found at the frozen revision; user-authored workflows could add such behavior without changing this repository-relative result until the first-party boundary itself supplies it.
