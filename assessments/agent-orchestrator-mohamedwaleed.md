---
harness_id: agent-orchestrator-mohamedwaleed
project_name: Agent Orchestrator (waves)
repository: https://github.com/mohamedwaleed/agent-orchestrator
review_ref: 5445af144773374450d933f05851d2018724ae25
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent Orchestrator (waves)

## Review boundary

- System in focus: one local Agent Orchestrator run at project/task-fleet recursion, including first-party ticket intake/normalization, dependency graph and wave planner, run state, worktree/session lifecycle, parallel-wave executor, Codex/Devin adapter boundary, and orchestrator-owned squash/commit/push/PR/merge machinery.
- Purpose and identity: execute dependency-annotated software tickets through isolated coding-agent work cells, preserve dependency/integration order, and produce one reviewable PR per task while giving the local user explicit control over current execution and merge commitments.
- Relevant environment: target Git repository, GitHub issues/PRs, local ticket files, Git worktrees, Codex/Devin CLIs, user/operator, configured models/providers, git/gh subprocesses, and upstream dependency declarations.
- Standard-distribution boundary: the first-party TypeScript core, adapter packages, CLI, run-state persistence, ticket sources, planner/wave logic, worktree/git operations and implemented user-driven execution controls are inside. Devin/Codex internal reasoning/tool loops, provider infrastructure, GitHub's own review/merge semantics, host Git/gh internals and upstream ticket-grilling logic remain separate systems. The first-party adapter path may make a coding agent operationally reachable as an S1 actor without importing other organizational functions from that external agent.
- Credited operating / distribution surfaces: `README.md`; `CONTEXT.md`; `docs/adr/0009-user-driven-execution-model.md`; `packages/core/src/orchestrator.ts`; `packages/core/src/planner/planner.ts`; `packages/core/src/execution/wave-executor.ts`; `packages/core/src/execution/real-git-operations.ts`; `packages/core/src/state/run-state-manager.ts`; `packages/core/src/cli.ts`; `packages/adapter-codex/src/index.ts`; and `packages/adapter-devin/src/index.ts`.
- Adjacent first-party surfaces excluded from ownership: planned/not-current approval-dashboard behavior beyond implemented CLI controls; planned attach/intervention/resume semantics not closed at the frozen ref; repository-development tests/CI; maintainer/contributor governance; design/spec claims not backed by current runtime code; and external coding-agent internals.
- First-party operating / deployment modes considered: user-driven `plan → execute-wave → review → merge-wave → continue`; full-auto `run` tracer-bullet mode; Codex and Devin adapters; local/GitHub ticket sources; merge-gate enabled/disabled behavior; task selection and max-parallelism controls.
- Recursion level: one project-wide orchestration run containing multiple coding-task S1 cells. Each external model-backed coding session is a lower-recursion operational cell reached and bounded by the first-party adapter/worktree path; the orchestrator/user pair regulates the population above them.
- Reviewed revision: `5445af144773374450d933f05851d2018724ae25`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Agent Orchestrator is a local TypeScript control plane around external coding-agent CLIs. Ticket sources normalize GitHub issues or Markdown into tickets with predeclared dependencies. The Planner deterministically topologically sorts those declarations into sequential waves. Its advertised LLM prompt generation/size-assessment layer is not implemented at the frozen ref: the source returns a simple derived prompt and no size warning, so no organizational function is credited to a Planner LLM.

For execution, each task receives a dedicated Git worktree and branch. First-party Codex and Devin adapters spawn the corresponding CLI in automatic-accept mode, retain session/process identity, wait for completion and return structured exit/output/last-message evidence. On successful completion, the orchestrator—not the agent adapter—owns squash/commit, push and PR creation. Waves can run several task sessions concurrently under a user-supplied maximum. The merge path gathers completed PRs for a wave and, in the normal merge-gate mode, asks the local user whether to merge after review; declining leaves PRs open. Merge failures become durable `conflicted` state.

The frozen implementation deliberately supports a user-driven control model. Separate CLI commands expose the full run state, permit selecting which tasks in a wave to execute and how much concurrency to allocate, and require a later `merge-wave` action after PR review. A full-auto `run` command remains as a convenience/tracer-bullet mode, but its deterministic wave loop does not itself introduce a discretionary whole-system manager.

## Operational model

Coding-agent sessions are the operational S1 cells. Rail-like first-party scaffolding—task prompts, worktree cwd, automatic-accept invocation, session lifecycle and result capture—makes these actors operationally reachable without treating Codex/Devin internals as part of the orchestrator.

S2 is supplied by deterministic anti-interference mechanisms. Distinct task cells execute in separate worktrees, worktree creation is serialized because shared Git worktree metadata is not safe for concurrent mutation, dependencies separate waves, parallelism is bounded when requested, and completed PRs are integrated sequentially. These mechanisms directly regulate shared-repository ordering/collision variety but do not own semantic task work.

At S3, the strongest implemented owner is the local user in user-driven mode. `status` exposes task/wave/PR/conflict state for the whole run; `execute-wave` lets the user select current tasks and parallelism; and `merge-wave` turns the user's post-review decision into actual base-branch commitments. The deterministic executor enforces those decisions and fixed plan rules but does not independently judge how current whole-system resources or commitments should be revised. Therefore the positive S3 mode is parent-owned `P`, not `C(P)`.

## S1 — Operations

- State: A
- Function: perform open-ended implementation work for one software ticket inside its assigned repository worktree and produce task output suitable for a PR.
- Disturbance / variety regulated: repository-specific implementation choices, code structure, debugging, tool/test feedback and local task ambiguity that deterministic wave/git logic cannot resolve.
- Decisive decision or feedback right: choose and revise semantic coding actions within the task prompt/worktree in response to repository/tool feedback.
- Decision owner: the model-backed Codex or Devin coding-agent session launched through the first-party adapter.
- Supporting / enforcement mechanisms: task prompt, per-task worktree/branch, adapter subprocess lifecycle, automatic-accept flags, session/result capture, orchestrator-owned commit/PR production.
- Closure path: runnable task → first-party adapter starts coding-agent CLI in isolated worktree → agent chooses implementation actions and reacts to local feedback → adapter returns completion/result → orchestrator commits/pushes/creates the task PR or records failure.
- Boundary reachability: built-in Codex and Devin adapters directly spawn the configured coding-agent CLI as the standard execution path; users need not implement a separate orchestration layer to create the operational cell.
- Why this is / is not agent-owned: removing the external coding-agent actor while retaining worktree, wave, state and git machinery leaves no component that can choose the open-ended implementation. The decisive operational discretion is therefore agent-owned, while its internal reasoning/tool loop remains external evidence boundary.
- Evidence: [`README.md`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/README.md); [`packages/adapter-codex/src/index.ts`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/packages/adapter-codex/src/index.ts); [`packages/adapter-devin/src/index.ts`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/packages/adapter-devin/src/index.ts); [`packages/core/src/execution/wave-executor.ts`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/packages/core/src/execution/wave-executor.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this credits the first-party assembled session path, not Codex/Devin's internal organizational functions.

## S2 — Coordination

- State: C
- Function: attenuate repository, dependency, Git-metadata and integration interference among distinct coding-task S1 cells while preserving their local implementation autonomy.
- Disturbance / variety regulated: parallel tasks can mutate the same working tree/Git metadata, run before prerequisite changes exist, exceed chosen concurrent capacity, or produce branches whose integration conflicts on the shared base.
- Distinct S1 units: separate Codex/Devin coding sessions mapped 1:1 from tickets and executed as distinct tasks/worktrees.
- Inter-S1 disturbance: concurrent filesystem/Git-worktree mutation and overlapping branch outputs can interfere; dependent tasks can operate against stale prerequisite state if run in the same stage; multiple sessions compete for configured local/provider capacity.
- Attenuating coordination relation: one worktree/branch per task; sequential worktree creation specifically because Git worktree metadata is unsafe under concurrent adds; deterministic dependency waves; optional max-parallelism; sequential PR merging; conflict state when integration fails.
- Feedback into subsequent S1 behaviour: task/wave readiness determines which S1 cells run; parallelism queues cells until a worker slot frees; later waves are created after earlier integration; failed/conflicted tasks remain non-runnable/held and are reflected in later status/continuation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited path is tied to concrete cross-cell collision modes—shared Git metadata, repository isolation, prerequisite state and integration conflicts—and its result changes later S1 admission/integration. Predeclared dependencies or wave labels alone are not the basis.
- Decisive decision or feedback right: enforce isolation/order/capacity relations that prevent one task cell from destructively interfering with another's execution or integration.
- Decision owner: deterministic first-party planner/executor/git machinery; no autonomous coordination actor is established.
- Supporting / enforcement mechanisms: topological sorting, worktree/branch creation, task statuses, concurrency worker pool, PR boundaries, merge order and conflict recording.
- Closure path: multiple task cells are derived → graph/worktree/capacity relation determines safe concurrent set → cells execute independently → PR/merge result updates task/run state and shared base → subsequent wave/cell execution uses the resulting state.
- Boundary reachability: all credited mechanisms are built into the normal `plan`, `execute-wave`, `run` and `merge-wave` paths.
- Why this is / is not agent-owned: removing coding agents leaves materially the same wave/worktree/concurrency/integration coordination decisions. They are constructor-owned, so `C`.
- Evidence: [`packages/core/src/planner/planner.ts`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/packages/core/src/planner/planner.ts); [`packages/core/src/execution/wave-executor.ts`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/packages/core/src/execution/wave-executor.ts); [`docs/adr/0009-user-driven-execution-model.md`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/docs/adr/0009-user-driven-execution-model.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: no S2 credit is inferred merely from parallelism, a dependency graph or generic sequencing.

## S3 — Inside-and-now control

- State: P
- Function: regulate the current project-wide run by deciding which ready commitments execute now, how much concurrent capacity they receive, and whether completed task outputs become shared base-branch commitments.
- Disturbance / variety regulated: current task/PR/failure/conflict distribution, finite concurrent agent capacity, selective task commitment within a wave, and uncertainty over whether completed PRs should be admitted to the shared base before later work proceeds.
- Whole-system current view: first-party `status`/run state exposes the complete run phase, current wave, all task statuses, PR URLs, conflict reasons and wave summaries; `mergeWave` obtains the completed PR set for the selected wave.
- Current-control decision scope: the local user chooses when to execute a wave, which task IDs to commit to now, the maximum current parallelism, whether reviewed completed PRs may be merged, and when to continue to later pending waves.
- Decisive decision or feedback right: select/approve current resource and commitment changes across the active task population.
- Decision owner: the legitimate local self-hosted human operator in the implemented user-driven mode.
- Supporting / enforcement mechanisms: persistent run/task state, `status`, `execute-wave --tasks`, `--max-parallelism`, merge-gate prompt, `merge-wave`, `continue`, conflict recording and deterministic wave executor.
- Closure path: whole-run state/PR set is surfaced → user chooses current task/concurrency/merge action → CLI passes that decision to the executor/merge path → work is admitted/queued or PRs are merged/left open → subsequent run state and later wave execution reflect the returned decision.
- Boundary reachability: these are shipped CLI/runtime surfaces and the ADR explicitly adopts the user-driven state machine as the operational model; the user does not need an external control application.
- Why this is / is not agent-owned: no first-party autonomous manager is shown making the whole-run resource/commitment judgment. The deterministic `run` convenience loop follows the predeclared plan and merge rules; task filtering, worker-pool limits and conflict recording enforce choices/state but do not establish separate S3 discretion.
- Evidence: [`docs/adr/0009-user-driven-execution-model.md`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/docs/adr/0009-user-driven-execution-model.md); [`packages/core/src/cli.ts`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/packages/core/src/cli.ts); [`packages/core/src/execution/wave-executor.ts`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/packages/core/src/execution/wave-executor.ts); [`packages/core/src/orchestrator.ts`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/packages/core/src/orchestrator.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: full-auto `run` is a supported convenience mode, but deterministic auto-execution is not independently promoted to `C` because the frozen implementation does not show a function-specific current-control judgment beyond applying the fixed plan/rules.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary audit path is established that independently challenges ordinary task success/current-control reporting and returns findings through a distinct audit loop.
- Disturbance / variety regulated: coding-agent success claims and PR quality can be manually reviewed, and merge conflicts are independently observable, but the frozen first-party runtime does not define a separate audit actor/evidence path with finding-to-control closure.
- Decisive decision or feedback right: none established for S3*.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: agent exit/result output, one PR per task, GitHub PR visibility, user review before `merge-wave`, conflict errors and task status.
- Closure path: no distinct complementary-audit finding path separate from ordinary parent merge control is supplied.
- Why this is / is not agent-owned: the user may inspect raw PR diffs on GitHub, but RailWarden-like review is not implemented here as a first-party independent verifier/auditor. The orchestrator merely asks the same parent controller whether to merge; it does not capture a separate audit claim/finding or route that finding back into S3.
- Evidence: [`README.md`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/README.md); [`docs/adr/0009-user-driven-execution-model.md`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/docs/adr/0009-user-driven-execution-model.md); [`packages/core/src/execution/wave-executor.ts`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/packages/core/src/execution/wave-executor.ts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: human PR review can be high-quality assurance in practice; the negative finding is about the Profile's distinct complementary-access/feedback requirement, and #177 explicitly cautions that human PR review is not automatically S3*.

### Absence scope

- Surfaces inspected: adapter result handling, PR generation, merge gate, GitHub review guidance, conflict handling, TUI/approval code, tests and planned intervention surfaces.
- Plausible first-party paths checked: human PR review as S3*; agent last-message versus raw diff; merge conflict detection; planned approval TUI; attach/intervention; tests/CI.
- Why no material first-party path remains: implemented review is the same parent merge-decision path, planned intervention/attach surfaces are excluded at the frozen ref, and development tests/CI are adjacent rather than live complementary audit owners.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective intelligence loop develops adaptation options and returns them into current orchestration capability.
- Disturbance / variety regulated: tickets, repository state and provider/session results supply current task context; these were examined separately from future/environmental adaptation.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: ticket intake, planned Planner LLM concepts, configuration, run JSON state and future-oriented spec/TUI/intervention design.
- Closure path: no external/future sensing → adaptation option → current-capability return loop is implemented.
- Why this is / is not agent-owned: ticket planning is internal task planning, and the advertised Planner LLM prompt/size functions are placeholders at this ref. JSON persistence records current work rather than adapting capability to prospective environmental change.
- Evidence: [`packages/core/src/planner/planner.ts`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/packages/core/src/planner/planner.ts); [`README.md`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/README.md); [`CONTEXT.md`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/CONTEXT.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: future provider/LLM planning or adaptation features could change this result; design vocabulary is not current operational evidence.

### Absence scope

- Surfaces inspected: Planner, ticket sources, config, run state, README/spec/CONTEXT roadmap claims, adapter lifecycle and user-driven controls.
- Plausible first-party paths checked: Planner LLM as S4; ticket intake as external sensing; future TUI/intervention/resume; adapter extensibility; configuration changes.
- Why no material first-party path remains: current implementation is task execution and persistence; planner semantic LLM functionality is placeholder, and no prospective environmental model generates capability adaptations that return to current control.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy loop is established for the orchestration organization.
- Disturbance / variety regulated: base branch, adapter/model, merge-gate configuration, ticket scope and user approvals constrain execution but are ordinary operational/configuration choices.
- Decisive decision or feedback right: no identity/ultimate-policy issue is raised, adjudicated by a legitimate ultimate authority and returned as governing organizational policy.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: layered config, CLI options, merge gate, ticket contracts, prompt templates and repository/user review.
- Closure path: no complete S5 issue → authority → decision → return-to-operation loop found.
- Why this is / is not agent-owned: merge approval and user task selection are credited to S3 parent current control; they do not become S5 merely because a human is authoritative over ordinary work. Static configuration likewise does not establish identity closure.
- Evidence: [`README.md`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/README.md); [`docs/adr/0009-user-driven-execution-model.md`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/docs/adr/0009-user-driven-execution-model.md); [`packages/core/src/cli.ts`](https://github.com/mohamedwaleed/agent-orchestrator/blob/5445af144773374450d933f05851d2018724ae25/packages/core/src/cli.ts).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: an external organization/user may hold broader policy authority, but this frozen distribution does not operationalize it as first-party S5 closure.

### Absence scope

- Surfaces inspected: configuration loader/CLI flags, ticket/dependency contracts, plan/merge approval, prompt templates, base-branch/adapter/model controls, contributor governance as adjacent surface.
- Plausible first-party paths checked: merge gate as S5; approval gate; config as policy; upstream dependency contracts; operator authority; repository governance.
- Why no material first-party path remains: these are task/current-control or static configuration surfaces, and #177 explicitly cautions against treating upstream contracts, merge-gate config or operator review as S5 without identity/ultimate-policy closure.

## Distributed OSS parent arrangement

Independent users can run local orchestrator instances and exercise the supported user-driven S3 parent loop. That local parent mode does not imply one organization-level parent across all OSS deployments. Repository maintainers/contributors are a development-governance surface and are not imported into runtime S3/S5 ownership.

## Self-hosted and non-human modes

The local self-hosted user-driven mode establishes S3=P because the operator sees the whole current run and returns task/concurrency/merge decisions through shipped controls. The full-auto mode remains deterministic execution of the frozen plan rather than an autonomous metasystemic owner. Coding-agent sessions retain local S1 autonomy while S2 remains deterministic.

## Recursion

At the selected recursion the project run is the system in focus and coding-agent task sessions are its operational cells. Their internal reasoning remains separate, but they have a distinct local environment (task worktree), durable contribution (task PR) and meaningful implementation autonomy. The orchestrator sits above them as deterministic S2 infrastructure, while the self-hosted user supplies the qualifying S3 parent decisions. Planned TUI/attach/intervention features are not used to inflate recursion or control.

## Variety and escalation

Task-local code variety is absorbed by coding agents. Cross-task filesystem, dependency, capacity and integration variety is attenuated by S2 worktrees/waves/concurrency/merge handling. Current whole-run commitment/resource variety is exposed to the user through persistent run status and explicit execution/merge commands. Failures remain failed, merge failures become conflicted and leave PRs for user intervention instead of silently advancing. No evidence supports separate prospective S4 or identity-level S5 escalation.

## Evidence gaps

The most important evidence boundary is intentional: Codex and Devin are external agents and their internal reasoning/tool loops are not inherited by Agent Orchestrator. S1 is credited only to the standard first-party adapter-managed operating cell. The planned Dashboard/Approval Gate, attach/intervention and richer resume behavior are not current evidence. A future independent verifier or implemented current-control agent could materially change S3/S3*, but they are not present at this frozen revision.
