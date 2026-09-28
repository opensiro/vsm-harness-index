---
harness_id: aesop
project_name: Aesop
repository: https://github.com/matt82198/aesop
review_ref: 2a661c12007c5484f964176da3d5532c6bdf070d
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: A(P)
---

# Aesop

## Review boundary

- System in focus: one Aesop-managed software-development project/wave organization at pinned revision `2a661c12007c5484f964176da3d5532c6bdf070d`, including the shipped `/power` and `/buildsystem` orchestration skills, worker-driver seam, wave scheduler/loop, ownership/worktree isolation, durable tracker/journal/checkpoint state, verification gates, watchdog/recovery surfaces and project `CLAUDE.md` rule layer.
- Purpose and identity: convert a ranked project backlog into verified software changes by dispatching bounded model-driven coding workers, keeping concurrent work coherent, regulating the current wave, independently challenging worker-green claims and preserving durable project operating rules across restarts.
- Relevant environment: project repository/git state, backlog and dependencies, worker/model availability, test/build results, CI/PR state, cost and liveness signals, failures/stalls, owner instructions and changing project code/contracts.
- Standard-distribution boundary: shipped source-available Aesop CLI/tools/skills/driver/daemon surfaces at the pinned revision and the ordinary target-project files they install/manage. Underlying Claude Code, Codex/OpenAI-compatible models, provider internals, GitHub itself and repository-contributor governance are dependencies or adjacent systems rather than first-party organizational owners.
- Credited operating / distribution surfaces: `/power`; `/buildsystem`; `driver/wave_scheduler.py`; `driver/wave_loop.py`; `driver/agent_driver.py`; worker dispatch; deterministic file-ownership selection; worktree isolation; exact-gate replay; tracker/journal/checkpoint state; watchdog/liveness handling; generated/loaded project `CLAUDE.md` layers.
- Adjacent first-party surfaces excluded from ownership: Aesop's own maintainer/release organization, CI and developer trap tests as development controls, benchmark/A-B datasets as repository R&D, archived cancelled architectures, examples/replay kits except as corroboration, and documentation claims not matched by a reachable frozen runtime/procedure.
- First-party operating / deployment modes considered: model-driven `/buildsystem` wave orchestration; Python `wave_scheduler`/`wave_loop` backend-portable execution; parallel worker dispatch with ownership/worktree isolation; crash/restart recovery; exact-gate spot-check replay; project init/prime and later owner-maintained project rules.
- Recursion level: one Aesop-managed software project/wave is the system-in-focus. Dispatched coding agents are bounded S1 operational units. The main model-driven orchestrator regulates the active project wave at S3. Project-root/domain `CLAUDE.md` rules are assessed as project-recursion identity/policy because later orchestration and workers operate under that durable layer.
- Reviewed revision: `2a661c12007c5484f964176da3d5532c6bdf070d`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Aesop is a crash-only multi-agent software-development harness. Its standard organization separates a model-driven orchestrator from multiple bounded model-driven coding workers. The shipped `/buildsystem` skill tells the orchestrator to read the current backlog/state, rank work, assign worker types, dispatch several workers, monitor liveness/build/test/cost signals, triage failures, route review and close the wave. `AgentDriver` supplies a backend-independent worker seam, while `wave_scheduler.py` and `wave_loop.py` supply deterministic intake, safety, verification, recovery and shipping machinery around those model decisions.

Concurrent workers are not credited as S2 merely because they are parallel. Aesop exposes a concrete interference mode and two first-party attenuation mechanisms: overlapping `ownsFiles` claims are rejected before dispatch, and concurrent agents operate in separate git worktrees/branches. The project documentation explicitly ties worktree isolation to preventing agents from interfering with one another. The later serial merge train is additional integration discipline rather than the sole S2 witness.

Current-control closes above individual coding workers in the ordinary `/buildsystem` mode. The orchestrator reads project state/backlog, ranks priorities/dependencies, assigns current work, monitors the fleet and decides retry/triage/integration actions. Deterministic `wave_scheduler` selection, HALT/cost gates, tracker transitions and `wave_loop` repair/ship machinery constrain and enforce this current-control process but do not replace the model actor's whole-wave semantic choices in the credited mode.

Aesop also has a complementary deterministic audit path that is stronger evidence than the repository's broader "adversarial review" narrative. After a worker result is already marked verified, Phase 5.5 independently re-runs the exact `testCmd` on the orchestrator side for a deterministic sample. A failed replay flips `verified` back to false, marks `fake_green`, persists the event and therefore changes downstream ship eligibility. This is credited as constructor-owned S3*. The separate model adversarial-review path is not needed for the mapping because its frozen Python activation/configuration does not cleanly match every documentation claim.

The repository contains extensive internal incident learning, closing audits, benchmark comparisons, capability probes and durable history. Those surfaces can improve future Aesop versions or populate a next backlog, but at the assessed project recursion they do not establish a distinct outside-and-then intelligence organization that models the external/future environment and negotiates adaptations with S3. S4 therefore remains absent.

Project identity/policy is carried through the durable `CLAUDE.md` layer. `/power` treats project-root `CLAUDE.md` as authoritative on every already-primed run. On an unprimed project, the model-driven orchestration brain fans out read-only exploration, synthesizes project purpose/commands/gotchas/domain contracts into project/domain `CLAUDE.md` files, writes and pushes that layer, and later runs load it. A legitimate project owner can review, edit and iterate the same authoritative files. That supplies distinct autonomous and parent-governed project-policy modes, yielding S5=`A(P)`.

## Operational model

At this recursion, model-driven coding workers are S1 units. Deterministic ownership partitioning/worktree isolation closes S2. The model-driven `/buildsystem` orchestrator owns whole-wave current prioritization, assignment, monitoring and triage at S3, while deterministic scheduler/gate machinery supplies support and enforcement. Independent orchestrator-side exact-gate replay supplies constructor-owned S3*. Internal retrospective learning is not promoted to S4. Project `CLAUDE.md` identity/rules can be synthesized by the model-driven init-prime path or directly governed by the legitimate project owner, closing S5 in `A(P)` modes.

## S1 — Operations

- State: A
- Function: perform substantive software-development work on bounded project backlog items through model-driven coding workers that inspect/edit repository state, run tools/tests and return implemented changes.
- Disturbance / variety regulated: heterogeneous implementation tasks, changing code and dependency state, ambiguous task requirements, test/build failures, tool/model uncertainty and task-specific acceptance criteria.
- Decisive decision or feedback right: choose task-specific implementation/tool actions, interpret repository/test observations and revise subsequent coding actions until a bounded work item is complete or fails.
- Decision owner: the dispatched model-driven worker reached through Aesop's first-party worker/harness path.
- Supporting / enforcement mechanisms: `AgentDriver`, work orders, owned-file boundaries, workdirs/worktrees, test commands, verification tiers, repair caps, durable journals and backend adapters.
- Closure path: selected backlog item + work order → model-driven worker chooses implementation/tool actions → repository/test observations return → later worker actions change from those observations → structured/filesystem result returns to the Aesop wave.
- Boundary reachability: `/buildsystem` directly dispatches model-driven coding workers, and the backend-portable `AgentDriver`/`wave_bridge` path is shipped first-party runtime at the frozen revision.
- Why this is / is not agent-owned: removing the model-driven worker while keeping scheduler, filesystem isolation, gates and persistence leaves coordination/control infrastructure but removes the semantic implementation decisions that produce the software outcome.
- Evidence: [`README.md`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/README.md); [`skills/buildsystem/SKILL.md`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/skills/buildsystem/SKILL.md); [`driver/agent_driver.py`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/driver/agent_driver.py); [`driver/wave_bridge.py`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/driver/wave_bridge.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider/model internals remain dependencies. `A` credits the model-driven worker actor reached through Aesop's shipped orchestration boundary, not autonomy of deterministic driver/scheduler code.

## S2 — Coordination

- State: C
- Function: attenuate destructive interference among concurrently active coding-worker S1 units by refusing overlapping file ownership before dispatch and isolating admitted workers in independent worktrees/branches.
- Disturbance / variety regulated: two workers modifying the same project files or mutable working tree concurrently can overwrite, race with or contaminate one another's changes and create unstable integration state.
- Decisive decision or feedback right: determine which current items may coexist without ownership overlap and enforce separated mutable workspaces for the workers that are allowed to run in parallel.
- Decision owner: deterministic first-party scheduler/preflight/worktree machinery.
- Supporting / enforcement mechanisms: normalized `ownsFiles`, disjoint-item selection, overlap abort/skip, git worktrees/feature branches and serial merge integration.
- Closure path: candidate concurrent items expose owned-file sets → deterministic preflight rejects/defers overlaps → admitted workers receive separate workspaces → each worker's later coding/tool actions proceed without sibling intermediate edits → completed branches/results return for controlled integration.
- Boundary reachability: the shipped `/buildsystem` contract requires disjoint ownership/worktree isolation, while `driver/wave_scheduler.py` mechanically selects file-disjoint items in the executable backend-portable wave path.
- Why this is / is not agent-owned: the inter-worker attenuation decision is encoded and enforced by deterministic first-party rules. Model workers remain autonomous inside their local tasks but do not decide whether ownership overlap is permissible.
- Distinct S1 units: two or more concurrently dispatched model-driven coding workers operating on separate backlog items.
- Inter-S1 disturbance: concurrent writes to overlapping project files or the same mutable working tree can collide or contaminate sibling work.
- Attenuating coordination relation: reject/defer overlapping `ownsFiles` before dispatch and isolate admitted worker writes in separate worktrees/branches.
- Feedback into subsequent S1 behaviour: conflicting workers are not jointly admitted; admitted workers continue later implementation/tool actions only inside their isolated ownership/worktree boundary, and their results are integrated after local work completes.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mapping rests on an explicit concurrent-write conflict and mechanisms specifically intended to prevent that cross-worker disturbance, not on the mere presence of a fleet, task queue or dispatcher.
- Evidence: [`skills/buildsystem/SKILL.md`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/skills/buildsystem/SKILL.md); [`driver/wave_scheduler.py`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/driver/wave_scheduler.py); [`docs/ARCHITECTURE.md`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/docs/ARCHITECTURE.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the MCP read-only status surface explicitly does not implement real-time coordination; it is not used for this S2 claim. The credited coordination path is ownership/workspace interference attenuation.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current project wave as a whole by prioritizing active backlog commitments, assigning bounded work to operational units, monitoring current fleet/test/liveness state and deciding retry, triage, review/integration and wave-closure actions.
- Disturbance / variety regulated: competing backlog priorities, dependencies, file ownership conflicts, stalled/failed workers, failing tests/PRs, budget/liveness constraints and the risk that locally successful worker changes are not suitable for the current project wave as a whole.
- Decisive decision or feedback right: choose current project priorities/assignments and exception responses across the active fleet, including which items to dispatch, how to triage/retry failures and which current results advance through review/integration.
- Decision owner: the model-driven main-thread orchestrator executing the shipped `/buildsystem` procedure in the credited mode.
- Whole-system current view: project-root `CLAUDE.md`, current backlog/STATE/BUILDLOG, dispatch assignments, worker heartbeats/status, build/test/PR results, cost and current wave progress are assembled for the orchestrator across the active project wave.
- Current-control decision scope: rank priorities/dependencies, assign workers, react to stalls/failures, choose redispatch/manual-triage paths, regulate review/integration and close/checkpoint the current wave.
- Supporting / enforcement mechanisms: deterministic `wave_scheduler` selection, HALT/cost gates, file-ownership guards, tracker/journal state, verification policy, repair caps, watchdog/liveness checks and merge/checkpoint machinery.
- Closure path: current project backlog/state + fleet signals/results → model orchestrator evaluates project-wide priorities/exceptions → dispatch/retry/triage/integration choice → first-party machinery enforces/records that choice → changed tracker/repository/wave state governs subsequent worker dispatch and wave actions.
- Boundary reachability: `/buildsystem` is a shipped Aesop skill intended for the ordinary installed Claude Code harness path; the README/setup exposes installation/use of these skills, and the frozen skill explicitly executes the rank → dispatch → monitor → review → checkpoint wave.
- Why this is / is not agent-owned: deterministic scheduler/gate code can still enforce overlap, cost, lifecycle and tracker constraints, but it does not make the same semantic project-wide priority/triage judgments with the orchestrator removed. In the credited `/buildsystem` mode those current-control choices are made by the model-driven orchestrator.
- Evidence: [`skills/buildsystem/SKILL.md`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/skills/buildsystem/SKILL.md); [`docs/ARCHITECTURE.md`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/docs/ARCHITECTURE.md); [`driver/wave_scheduler.py`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/driver/wave_scheduler.py); [`driver/orchestrator_driver.py`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/driver/orchestrator_driver.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the backend-portable Python scheduler also exposes substantial constructor-owned current control. Methodology `0.3.x` has no `A+C` composite; `A` records the ordinary supported model-orchestrated `/buildsystem` mode in which the decisive whole-wave semantic choices are agent-owned, while deterministic machinery is recorded separately as support/enforcement.

## S3* — Complementary audit

- State: C
- Function: independently challenge an already-green worker result by replaying its exact verification command on the orchestrator side and revoke green status when the independently observed result disagrees.
- Disturbance / variety regulated: worker execution or self-report can produce a fake-green condition in which an item appears verified even though the claimed test does not actually pass when independently repeated outside the worker's ordinary result path.
- Decisive decision or feedback right: re-run the exact `testCmd` against a deterministic sample of already-verified items and invalidate the item when the replay exits non-zero.
- Decision owner: deterministic first-party Phase 5.5 exact-gate runtime.
- Supporting / enforcement mechanisms: deterministic sampling by slug, `AgentDriver.run_command`, separate gate exit capture, `fake_green` marker, durable journal update and downstream `verified` gating.
- Closure path: worker result is already `verified=True` → orchestrator-side exact-gate independently re-runs `testCmd` → non-zero replay flips `verified=False` and records `fake_green` → later review/ship logic sees the revoked status and does not treat the item as green.
- Boundary reachability: `_verify_exact_gate` is invoked directly in the shipped `run_wave` phase sequence after repair and before adversarial/final-catch/ship handling; the active verification policy gives every supported tier a positive spot-check fraction.
- Why this is / is not agent-owned: the audit judgment here is the independently observed command exit and deterministic comparison, not a model's semantic reviewer discretion. Therefore ownership is constructor/runtime `C` even though model-driven workers produced the audited changes.
- Claim being audited: the operational worker/wave claim that the current item is genuinely verified/green according to its declared test command.
- Ordinary reporting path: the worker/driver build path and its initial test/verification result used to set `verified=True`.
- Complementary access path: a later orchestrator-side replay independently executes the exact verification command for a deterministic sample rather than trusting the prior worker/result status.
- Independence boundary: replay occurs after the ordinary build/repair path through separate orchestrator-side command execution; its verdict depends on the new process exit result, not on worker narrative or cached success.
- Who acts on findings: `wave_loop`; replay failure revokes `verified`, marks `fake_green`, persists the audit result and thereby changes downstream shipping/review eligibility.
- Evidence: [`driver/wave_loop.py`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/driver/wave_loop.py); [`driver/agent_driver.py`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/driver/agent_driver.py); [`driver/verification_policy.py`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/driver/verification_policy.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Aesop also contains model adversarial-review and orchestrator final-catch surfaces. They are not required for this mapping: at the frozen revision, Python adversarial-review activation/configuration is less cleanly aligned with narrative defaults, while final-catch itself notes limited evidence richness. The exact-gate replay supplies the narrower closed S3* witness.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material distinct external-and-prospective adaptation function is established inside the assessed project/wave organization.
- Disturbance / variety regulated: Aesop records incidents, audits completed waves, probes backend capability, compares architectures/models and can feed retrospective findings into a later backlog, but the reviewed standard project runtime does not maintain a separate model of the relevant outside/future environment and return prospective adaptation options through a distinct S3↔S4 conversation.
- Decisive decision or feedback right: no qualifying project-recursion external/future adaptation judgment/feedback right is established.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: closing audit, incident history, durable STATE/BUILDLOG/MEMORY, monitor signals, backend capability probes, verification-tier policy, benchmarks/A-B studies and next-backlog notes.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: retrospective audit and internal operational learning can change later work, and backend probes can adapt current verification strictness, but those are internal history/current execution regulation unless they form a distinct prospective environmental-intelligence function. The reviewed project runtime does not establish that separate S4 organization.
- Evidence: [`docs/ARCHITECTURE.md`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/docs/ARCHITECTURE.md); [`driver/agent_driver.py`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/driver/agent_driver.py); [`driver/verification_policy.py`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/driver/verification_policy.py); [`docs/INCIDENTS.md`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/docs/INCIDENTS.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the negative finding is recursion-specific. Aesop's repository-development organization may conduct substantial R&D/benchmarking, but adjacent maintainer/R&D activity does not become S4 of an ordinary deployed target-project wave merely by repository co-location.

### Absence scope

- Surfaces inspected: closing audit/next-backlog feedback; monitor/watchdog signals; durable STATE/BUILDLOG/MEMORY; backend capability probes and verification policy; incident history; benchmark/A-B architecture studies; `/power` project scanning; orchestrator decision schemas and current wave planning.
- Plausible first-party paths checked: closing audit as future intelligence; incident learning; backend/model capability probe; model/architecture A-B studies; monitor daemon; durable memory; project scanning; future backlog generation.
- Why no material first-party path remains: inspected live project paths primarily regulate current work or summarize internal historical operation. Benchmark/R&D surfaces belong to Aesop's adjacent repository-development organization. No separate deployed project function both models external/future distinctions and develops adaptation options that return into a distinct S3↔S4 organizational conversation.

## S5 — Policy and identity

- State: A(P)
- Function: maintain the durable project identity and ultimate operating rules that define project purpose, domain boundaries/contracts, build/run expectations, gotchas and standing orchestration constraints for later Aesop-managed work.
- Disturbance / variety regulated: missing or stale project identity, inconsistent worker assumptions, conflicting domain contracts, drift in standing development/orchestration rules and loss of durable project intent across sessions/restarts.
- Decisive decision or feedback right: decide the authoritative project/domain `CLAUDE.md` content that later `/power`, `/buildsystem` orchestration and workers must load/follow.
- Decision owner: Base (`A`) mode — the model-driven `/power` init-prime orchestrator synthesizes the exact project/domain rule layer from repository evidence and writes/pushes it. Parent (`P`) mode — the legitimate project owner/editor reviews, edits or iterates those same authoritative files directly.
- Supporting / enforcement mechanisms: read-only exploration fan-out, repository scans, git persistence/push, secret-scan gate, `/power` fast-path loading, `/buildsystem` prerequisite/rule loading, work-order constraints and scoped domain files.
- Closure path: project identity/policy gap or owner change → model init-prime synthesis or legitimate parent edit → authoritative project/domain `CLAUDE.md` is persisted → later `/power` loads/internalizes the changed rules → subsequent `/buildsystem` orchestration and worker work orders operate under that durable layer.
- Boundary reachability: `/power` is a shipped first-party skill; README/setup installs Aesop skills for ordinary use, and the frozen skill explicitly implements both autonomous init-prime writing and already-primed rule loading. Direct owner iteration of project/domain `CLAUDE.md` is part of the documented supported project workflow.
- Why this is / is not agent-owned: in base mode the user invokes `/power`, but the model actor inspects repository evidence and chooses the exact synthesized purpose/gotcha/domain-contract content rather than merely storing preselected text. Removing the model leaves file-writing machinery but not the semantic project-policy synthesis. In parent mode the legitimate owner directly chooses the authoritative rule edit.
- Identity / ultimate-policy issue: what the project is for and which durable contracts/rules govern later Aesop work at that project recursion, including purpose, domain boundaries, build/run commands, verified gotchas and standing orchestration expectations.
- Ultimate authority in each claimed mode: Base (`A`) — model-driven init-prime orchestrator for the synthesized project rule layer within higher-level Aesop cardinal constraints; Parent (`P`) — legitimate project owner/editor for direct authoritative project-rule changes.
- Return-to-operation path: project/domain `CLAUDE.md` files persist in the target repository; later `/power` explicitly loads them as authoritative semantic memory/rules and `/buildsystem` requires that loaded rule layer before dispatching/controlling subsequent workers.
- Evidence: [`skills/power/SKILL.md`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/skills/power/SKILL.md); [`skills/buildsystem/SKILL.md`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/skills/buildsystem/SKILL.md); [`tools/init_project.py`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/tools/init_project.py); [`README.md`](https://github.com/matt82198/aesop/blob/2a661c12007c5484f964176da3d5532c6bdf070d/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: autonomous project-policy synthesis remains bounded by higher-recursion Aesop/global cardinal rules and by the repository facts the init-prime path is instructed to preserve. `A(P)` does not claim that the model can rewrite those higher-level constraints; it records two supported ownership modes for project-recursion policy.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | model-driven `/power` init-prime orchestrator | authorized `/power` invocation on an unprimed Aesop-installed project | explore repository → synthesize exact project/domain rule layer → write/push `CLAUDE.md` files → later `/power` loads them → later orchestration/workers follow them | `skills/power/SKILL.md`, `skills/buildsystem/SKILL.md` |
| Parent (`P`) | legitimate project owner/editor | direct review/edit/iteration of project/domain `CLAUDE.md` | parent changes authoritative project rules → persistent repository files change → later `/power` reloads them → subsequent `/buildsystem` operation is governed by the returned rules | `skills/power/SKILL.md`, `tools/init_project.py` |

## Distributed OSS parent arrangement

Aesop's public repository maintainer/release organization is outside the deployed target-project boundary and does not donate S3/S4/S5 ownership. The S5 parent mode above is the legitimate owner of the target project editing its own durable project-rule layer, not Aesop's upstream maintainer deciding repository policy.

## Self-hosted and non-human modes

Aesop is designed for local/project-host execution and supports multiple model backends. Human visibility, manual triage and merge review do not automatically become parent-mode S3 or S5. The credited S5 parent mode is narrower: direct legitimate authority over the target project's durable identity/ultimate operating rules with an explicit return into later orchestration.

## Recursion

The target project/wave is the assessed viable organization. Individual coding workers are bounded S1 units rather than automatically recursive viable systems. The model orchestrator regulates their current project contribution at S3. Watchdog, scheduler, driver and verification processes are support/control machinery mapped by their actual functions. Project/domain `CLAUDE.md` is assessed at project recursion because it governs later waves and worker behavior across transient tasks.

## Variety and escalation

Aesop attenuates operational variety with backlog sizing, owned-file partitioning, isolated worktrees, verification tiers, cost/HALT gates, bounded repair and durable checkpointing. It amplifies regulatory capacity with a model orchestrator, multiple coding workers, backend portability, tests/replay and structured project state. Escalation appears through blocked tracker states, failed review/CI, retry ceilings, watchdog stall handling, manual triage and durable reports. These are classified by the receiving function rather than treated as an extra VSM system.

## Evidence gaps

- S2 credits concrete file/worktree interference attenuation, not fleet topology, shared state or dispatch by themselves.
- S3 credits the standard model-driven `/buildsystem` project-wave mode. Constructor-owned scheduler/gate control is supporting/alternate machinery, not evidence that the model loses the credited whole-wave decision right in that mode.
- S3* deliberately uses the narrower executable exact-gate replay rather than relying on broader adversarial-review claims whose frozen activation/configuration is less uniform.
- S4 remains absent despite rich incident logs, audits and R&D because the ordinary deployed project boundary lacks a distinct external-and-prospective S4 organization and S3↔S4 conversation.
- S5 `A(P)` is project-recursion policy only: autonomous init-prime synthesis and legitimate owner editing both return into later `CLAUDE.md`-governed operation; higher-recursion Aesop/global rules remain outside that ownership claim.
