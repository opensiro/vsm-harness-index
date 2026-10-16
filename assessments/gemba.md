---
harness_id: gemba
project_name: Gemba
repository: https://github.com/GembaCore/gemba-core
review_ref: 64c266f889c6d6a579904c5e336676fa1c49b216
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Gemba

## Review boundary

- System in focus: Gemba's pinned, first-party Go server with native orchestration, pool dispatch, work planning/board, persona consultations and in-process Onboarder planning agent. Not the internal autonomous cognition of Claude Code, Codex, Pi, other attached terminal agents or Beads.
- Purpose and identity: organize a single project's work into milestones/epics/beads, mediate current work priority, run controllable external worker sessions and offer model-authored new-project plans. Its model-assisted plan creation is a narrower first-party S1 operation than end-to-end coding.
- Relevant environment: project work graph / configured WorkPlane, human operator, optional OrchestrationPlane and pools, live external agent sessions, CLI/tmux backends, selected LLM API, task and workspace state, work completion and escalation signals.
- Standard-distribution boundary: the shipped `gemba serve` app, its real Onboarder skill and ratifier, native orchestration adaptor, configured autonomous worker pools, planner workspace-collision gate, consult/walk/board endpoints. WorkPlane data may be supplied by Beads or Dolt; terminal coding-agent implementations and provider cognition remain dependencies.
- Credited operating / distribution surfaces: `internal/cli/serve.go` production wiring of `AttachNewProject`; `internal/skills/newproject/skill.go`; `internal/personas/onboarder/`; `internal/server/newproject_ratify.go`; native session lifecycle; optional `internal/cli/pool_wiring.go` + `internal/planner/autodispatch/daemon.go` + selection/workspace collision functions; work-item dispatch/board operations.
- Adjacent first-party surfaces excluded from ownership: contributor instructions, development/design sketches, the test suite and E2E fixtures as independent actors; external coding-agent binaries, vendor models and external WorkPlane internals. Tests corroborate installed paths but do not stand in for live execution. Unwired extension examples are not an assessed mode.
- First-party operating / deployment modes considered: `gemba serve` with Onboarder enabled by a configured Anthropic-compatible LLM client; browser-mediated project ratification; manually dispatched native sessions; **optional configured** pool autodispatch; Beads-only mode and Beads-read-only mode as reduced-function counterfactuals.
- Recursion level: Gemba's single project/workspace operations with the first-party planning unit and optional externally executed worker sessions governed by first-party orchestration. Lower-recursion coding agency in vendor executables is explicitly not imported as Gemba-owned autonomy.
- Reviewed revision: `64c266f889c6d6a579904c5e336676fa1c49b216` (frozen intake #193).
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Gemba is a Go HTTP service with a browser workspace/board, pluggable WorkPlane and optional OrchestrationPlane; its own native adaptor launches and supervises terminal agent processes. The README explicitly distinguishes an external WorkPlane and vendor coding-agent cognition from Gemba's control surfaces. A Beads-only read-only deployment cannot dispatch agents, whereas the supported native mode can launch sessions and manage lifecycle. The platform should therefore not inherit S1 cognitive operations from an attached Codex/Claude Code instance ([README.md](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/README.md), [internal/adapter/native/start.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/adapter/native/start.go), [internal/cli/serve.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/cli/serve.go)).

There is a narrower **installed first-party model-driven operational unit**. Production `serve` wires a real Onboarder `SkillTurner`, a provider client resolver and a transactional ratifier. The `newproject.Run` skill sends structured prior project state and the operator's new input to its model client, receives a model-chosen updated plan and reply, validates the envelope, and returns the next state. Validation failures trigger a bounded model retry, while project persistence waits for a distinct human ratification step. Thus Gemba **owns the adaptive planning conversation**, not the provider's neural implementation nor the operator's authorization to commit work ([internal/cli/serve.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/cli/serve.go), [internal/personas/onboarder/onboarder.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/personas/onboarder/onboarder.go), [internal/skills/newproject/skill.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/skills/newproject/skill.go), [internal/server/newproject_ratify.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/server/newproject_ratify.go)).

Native worker pools are opt-in and wired from the first-party serve path. Each pool daemon observes idle and live sessions, the ready work set and worktree/repository overlap. It filters conflicting tasks, applies rate/concurrency and eligibility gates, and dispatches or cold-starts compatible external agent sessions. This **attenuates collision among managed workers** without claiming the dispatcher is the workers' reasoning agent. It is also not, alone, a model-owned S3 decision: deterministic affinity selection executes configured priorities ([internal/cli/pool_wiring.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/cli/pool_wiring.go), [internal/planner/autodispatch/daemon.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/planner/autodispatch/daemon.go), [internal/planner/workspace_collision.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/planner/workspace_collision.go), [internal/planner/selection/selection.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/planner/selection/selection.go)).

The operator can view project work and active session state, change work items, and explicitly dispatch eligible children from epic/milestone hierarchy through production endpoints. This is a distinct present-tense current-control path from automatic scoring. Parent-controlled Gemba behavior should be described as **human-owned**, not upgraded to S3=A by surrounding queues and automation ([internal/server/work_items_cascade.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/server/work_items_cascade.go), [internal/server/work_items_write.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/server/work_items_write.go), [internal/cli/serve.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/cli/serve.go)). Broader persona consultations, Gemba walks, QA facilities and retrospective/planning scaffolds are present, but this pinned review did not yet establish a sufficiently independent audit return path or an outside-and-then capability-adaptation owner for those functions; they are retained as explicit evidence gaps, not advertised autonomous grades ([internal/persona/dispatcher.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/persona/dispatcher.go), [internal/walk/agenda.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/walk/agenda.go), [internal/planner/retro/runner.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/planner/retro/runner.go)).

## Operational model

In the supported model-assisted start mode, a user proposes a project, the in-process Onboarder model produces/updates a structured work plan over conversational turns, and the parent ratifies before work items are persisted. Thereafter Gemba maintains project/work/session state. In configured native-pool mode its dispatcher schedules ready work onto external agents while enforcing first-party per-workspace collision and pool gates. Parent operators inspect the workspace and choose explicit work/commitment interventions. The agentic *coding* in launched worker binaries is outside the assessed Gemba-owned S1. No actual external LLM run, real multi-worker contention trial, or independently witnessed operator intervention is claimed here.

## S1 — Operations

- State: A
- Function: the in-process Onboarder adaptively transforms a user's project request and conversational feedback into a validated milestone/epic/bead work plan.
- Disturbance / variety regulated: incomplete or changing operator requirements, plan-schema errors, inconsistencies between prior draft state and a new message.
- Decisive decision or feedback right: propose revised project structure and conversational response from prior state/new request; choose a corrected plan after validation feedback. The consequential write/ratification right remains human-owned.
- Decision owner: the model-driven Onboarder constructed/wired by Gemba's first-party skill and LLM transport; a vendor API supplies the model inference, not a prebuilt external agent harness.
- Supporting / enforcement mechanisms: `newproject.Run`, model client, strict envelope/schema validation, retry-once, session Turn state, operator ratifier.
- Closure path: user message + prior state → model-composed plan/reply → first-party validation/retry → next draft state and further operator feedback; separately, explicit ratification creates project work.
- Boundary reachability: `gemba serve` installs the real Onboarder `SkillTurner` and `NewRatifier`; a configured client enables this first-party route. A Beads-only mode without an LLM has reduced scope and does not demonstrate it.
- Why this is / is not agent-owned: the installed model chooses the plan contents from conversational feedback rather than a fixed template or external coding CLI. The model does *not* own final project authorization, downstream coding or a generic autonomous tool-action loop.
- Evidence: [internal/cli/serve.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/cli/serve.go); [internal/skills/newproject/skill.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/skills/newproject/skill.go); [internal/personas/onboarder/onboarder.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/personas/onboarder/onboarder.go); [internal/server/newproject.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/server/newproject.go); [internal/server/newproject_ratify.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/server/newproject_ratify.go).
- Basis: explicit installed source path and structural closure; no provider-backed live run.
- Confidence: medium-high for the bounded planning S1; not a claim of first-party autonomous software engineering.
- Caveats: this S1 is specifically conversational project-plan production. Native worker processes remain independent autonomous systems.

## S2 — Coordination

- State: C
- Function: prevent two managed external worker sessions from consuming conflicting current repository/worktree work while the configured pool allocates ready jobs.
- Disturbance / variety regulated: concurrent task assignment to sessions targeting overlapping Git repository/branch/worktree resources; duplicate claims and unsafe reuse.
- Decisive decision or feedback right: reject a conflicting ready bead, choose a non-conflicting eligible bead, and dispatch or decline/cold-start a session under configured resource gates.
- Decision owner: first-party deterministic scheduler/collision constructor operating under user-provided pool configuration; not the attached worker models.
- Supporting / enforcement mechanisms: `WorkspaceCollisions`, daemon ready/live/idle view, `DispatchGate`, `SessionDispatcher`, first-party native `StartSession`, atomic claim semantics.
- Closure path: live worker assignments + ready-bead targets → workspace collision edges and pool eligibility → incompatible assignments withheld, eligible assignment claimed/dispatched → subsequent worker sessions operate on non-conflicting selected targets; later pool ticks refresh current occupancy.
- Boundary reachability: first-party `startPoolDaemons` runs after production `serve` config resolves pools, wiring the daemon to the installed native orchestration and WorkPlane adapters. It is **opt-in**, not inherent in bare Beads-only mode.
- Why this is / is not agent-owned: Gemba constructs the specific interference attenuator and enforces it automatically; the configured policy and scheduler, rather than an autonomous model negotiating conflicts, own the decision.
- Distinct S1 units: concurrently operating agent sessions launched/adopted under Gemba's native OrchestrationPlane; individual coding-agent model loops remain external dependencies.
- Inter-S1 disturbance: overlapping worker writes to the same repository/branch/worktree and duplicated task claim across concurrently active sessions.
- Attenuating coordination relation: worktree-target collision graph and atomic current-bead claim before `StartSession`/dispatch, plus configured max-concurrency and minimum dispatch intervals.
- Feedback into subsequent S1 behaviour: collision gate removes candidate assignments before launch, then updated active/idle session state and claims shape the following scheduling cycle.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: gate inspects contested writable resource targets of **multiple operational sessions** and withholds overlapping execution, directly attenuating inter-worker interference rather than merely displaying a queue.
- Evidence: [internal/cli/pool_wiring.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/cli/pool_wiring.go); [internal/planner/autodispatch/daemon.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/planner/autodispatch/daemon.go); [internal/planner/workspace_collision.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/planner/workspace_collision.go); [internal/planner/selection/selection.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/planner/selection/selection.go); [internal/adapter/native/start.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/adapter/native/start.go).
- Basis: wired, selectable native operating mode; structural interference suppression.
- Confidence: medium-high for the opt-in construction, not an observed live concurrency outcome.
- Caveats: Gemba prevents specific resource collisions; it cannot guarantee semantic noninterference or correctness of agent-produced code.

## S3 — Inside-and-now control

- State: P
- Function: parent operator's current workspace-wide choice of live commitments, work priority and explicit launch/redispatch across managed work items and active sessions.
- Disturbance / variety regulated: competing work commitments, blocked dependencies, operator attention and need to reallocate current agent execution.
- Decisive decision or feedback right: inspect aggregate project/work and session state, edit the active work graph and explicitly start eligible epic/milestone descendant jobs; the autonomous pool scorer does not independently choose organizational mission or portfolio strategy.
- Decision owner: human project owner/operator using Gemba's first-party board and task/dispatch API; automatic scheduler only enforces configured bounds.
- Supporting / enforcement mechanisms: WorkPlane state, board and work-item edit routes, dependency selection, native OrchestrationPlane `StartSession`, work-item cascade dispatcher, status/attention reporting.
- Closure path: project board and worker/task state → operator edits priorities/assignments or submits dispatch → Gemba applies current work mutation / starts permitted child sessions → updated WorkPlane and active session state feed back to subsequent operator and pool decisions.
- Boundary reachability: shipped HTTP/SPA and `POST /api/work-items/{id}/cascade-dispatch` with native adaptor (rather than merely a design document); Beads-only read-only mode cannot perform this closure.
- Why this is / is not agent-owned: the human parent retains judgment over current portfolio commitments, while Gemba executes constrained requests. Deterministic affinity and auto-launch do not warrant autonomous S3 ownership.
- Whole-system current view: per-project active work graph/board and available session statuses, including ready/blocker/assignment and action results; this is a project/workspace view, not arbitrary cross-tenant coordination.
- Current-control decision scope: manual work-item mutation, active epic/milestone dispatch and choice to launch new worker commitments; not only reading logs or approving isolated tools.
- Evidence: [README.md](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/README.md); [internal/server/work_items_cascade.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/server/work_items_cascade.go); [internal/server/work_items_write.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/server/work_items_write.go); [internal/adapter/native/start.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/adapter/native/start.go); [internal/cli/serve.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/cli/serve.go).
- Basis: explicit user-present control and first-party effects route.
- Confidence: medium for the supported parent-owned workflow; no specific operator intervention was run live.
- Caveats: scope is one workspace/project; operator decisions outside Gemba or a broader organization are not imported.

## S3* — Complementary audit

- State: —
- Function: no *reachable first-party* complementary audit owner with materially independent operational access and findings-to-current-control closure is established in the pinned supported modes.
- Disturbance / variety regulated: worker completion claims, QA correctness, declared-vs-actual modification drift and escalation findings are plausible audit subjects.
- Decisive decision or feedback right: independent challenge of ordinary S1/S3 operational claims based on separate observed evidence, with findings causing an actual later correction or control adjustment. Not furnished end-to-end.
- Decision owner: none identified for an independent audit function within the credited Gemba runtime; the operator reviews escalations, and optional persona suggestions depend on external Claude Code consultations rather than an installed complementary auditor.
- Supporting / enforcement mechanisms: walk agenda, persona consult audit log, `bootstrap_review` advisory batch review, regression suite *registry*, offline retrospective comparator and evidence adapters.
- Closure path: the shipped walk lists current work and escalations for an operator, and persona recommendations may be applied by operator action, but no separately sourced independent completion audit regularly or optionally reaches binding corrective operations in the evidenced first-party standard mode.
- Boundary reachability: `serve` wires `AttachWalk`, but Witness/Refinery sources are nil/no-op; the consult-inside-walk handler returns **501**, and `qa/regression` explicitly registers potential suites without executing them. `retro.Runner` has logic to compare actual Git diffs with declarations and update profiles but is not wired into `serve` by the reviewed production code; `gemba retro list` only reads existing/offline grades.
- Why this is / is not agent-owned: neither advisory user-led review nor an unwired retrospective or future witness adapter grants a Gemba first-party independent audit actor a decisive judgment-and-return right. External vendor agent reasoning is not credited.
- Evidence: [internal/cli/serve.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/cli/serve.go); [internal/server/walks.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/server/walks.go); [internal/walk/sources/witness.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/walk/sources/witness.go); [internal/walk/sources/refinery.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/walk/sources/refinery.go); [internal/qa/regression/suite.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/qa/regression/suite.go); [internal/planner/retro/runner.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/planner/retro/runner.go); [internal/cli/retro.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/cli/retro.go); [internal/skills/bootstrap_review/skill.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/skills/bootstrap_review/skill.go).
- Basis: explicit non-execution/no-op/501 production paths plus structural comparison of possible audit sources.
- Confidence: medium-high for bounded shipped-mode absence; does not rule out operator-attached independent review integrations outside the pinned standard distribution.
- Caveats: if an externally integrated worker/witness supplies its own independent audit, it belongs to that enlarged composed system, not to Gemba by inference.

### Absence scope

- Surfaces inspected: production `serve` persona and walk wiring, live witness/refinery default sources, walk consult handler, bootstrap-review advisor, QA regression registration, retro comparison/runner and the `gemba retro` CLI.
- Plausible first-party paths checked: independent witness findings, separate QA execution against raw code, declared-vs-actual Git change audit feeding follow-on regulation, independently consulted coach and walk decision/applier loop.
- Why no material first-party path remains: default witness/refinery sources contribute no independently gathered observations, consult-inside-walk is not implemented, regression suites are inspection-only, and retro corrective processing is not connected into the normal serving path. Operator acknowledgement and advisory persona output do not substitute for a first-party complementary audit closure.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supported Gemba-owned external-and-prospective intelligence/adaptation loop with a new capability option and returned installation into current operating capacity is established.
- Disturbance / variety regulated: incoming project demands, changing technological environment, worker effectiveness, evolving dependencies and future requirements.
- Decisive decision or feedback right: independently or parent-governedly recognize future/environment distinctions and choose/install an adaptation of organizational capability. No such function-specific path is evidenced.
- Decision owner: the operator may change task strategy and configuration; onboarder/PM personas may propose milestones and epic order. These are current/project planning and operator decisions, not demonstrated outside-and-then capability governance.
- Supporting / enforcement mechanisms: PM `epic_order`, project Onboarder, source scan scheduling, agent-profile scoring and retrospective comparison/calibration.
- Closure path: future milestone plans and current work rankings can enter WorkPlane and affect today’s task order, but no outside-world forecast/option development → capability adaptation decision → updated Gemba operational repertoire was found.
- Boundary reachability: shipped Onboarder and PM skill are wired, but their prompts are scoped to task plan/sprint-order; source scan scheduler is a deterministic trigger/coalescer, and retro runner is not wired into production `serve`.
- Why this is / is not agent-owned: bounded planning about later *tasks* and updated affinity scores are not an organizational future/environment intelligence process. External model or developer modification is not attributed to Gemba.
- Evidence: [internal/skills/newproject/skill.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/skills/newproject/skill.go); [internal/server/embedded_personas/project-manager.toml](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/server/embedded_personas/project-manager.toml); [internal/skills/epic_order/skill.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/skills/epic_order/skill.go); [internal/planner/scanscheduler/scheduler.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/planner/scanscheduler/scheduler.go); [internal/planner/retro/runner.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/planner/retro/runner.go); [internal/cli/serve.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/cli/serve.go).
- Basis: first-party role and production-wire scrutiny, explicit distinction of prospective capability vs current-task planning.
- Confidence: medium-high for bounded present distribution, not universal impossibility.
- Caveats: future extensions may provide environment intelligence or evolutionary selection; unshipped/injected components are outside the frozen scope.

### Absence scope

- Surfaces inspected: shipped new-project and PM persona prompts, production consult/applier setup, planner source-scans, session affinity/profile/retro machinery, project/workflow orchestration.
- Plausible first-party paths checked: evolving epic priorities, new milestones, completed-work learning, external source scans, revised worker policies and capability promotion.
- Why no material first-party path remains: found behavior orders *current and known* work, schedules source scans or recalibrates dispatch scoring; it does not construct and choose externally grounded future options that revise the organization's capability model and return that decision to operating S1/S3.

## S5 — Identity and ultimate policy

- State: —
- Function: no first-party ultimate-identity or ethos/policy *regulatory decision* with appropriate authority and return to whole-system operation is demonstrated beyond project setup.
- Disturbance / variety regulated: fundamental organizational mission, operating identity and tensions between current commitments and future adaptation.
- Decisive decision or feedback right: establish/revise identity or ultimate policy, resolve S3–S4-level tensions and govern subsequent operations. Not evidenced for the assessed deployed harness.
- Decision owner: a human project user selects and ratifies the *initial project plan*; repository developers/operators own app configuration. Neither is shown making a function-specific ultimate-policy decision through a shipped Gemba identity/governance loop.
- Supporting / enforcement mechanisms: Onboarder validation and separate project-ratification transaction, workspace configs, permission flags, credentials, tenant/auth layer, static persona role descriptions.
- Closure path: model-proposed project draft → user authorizes creation → directory/WorkPlane is initialized. This is operative *project creation* and does not exhibit identity/ultimate-policy choice after environmental adaptation tension or a later policy return that governs the organizational whole.
- Boundary reachability: the initial project ratifier is production-wired, but no S5-specific identity-policy channel and subsequent policy-effect loop is evidenced in the audited surface. This is not a negative claim about human ultimate authority outside Gemba.
- Why this is / is not agent-owned: LLM plan construction, human consent and static enforcement do not turn the model, ratifier or permission checks into an S5 organ. A parent-owned S5 `P` needs a real policy-level decision route, not only a normal project-creation confirmation.
- Evidence: [internal/server/newproject_ratify.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/server/newproject_ratify.go); [internal/cli/serve.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/cli/serve.go); [internal/personas/onboarder/onboarder.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/personas/onboarder/onboarder.go); [internal/server/newproject.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/server/newproject.go); [internal/auth/](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/auth/).
- Basis: source-confirmed setup/authorization boundary; no distinct S5 policy closure in shipped runtime.
- Confidence: medium-high for bounded reviewed first-party modes.
- Caveats: a separate institution or user can hold S5 for a wider organization that deploys Gemba; that wider owner is outside this repository-relative assessment.

### Absence scope

- Surfaces inspected: creation/ratification, project/workspace setup, auth and permissions, persona configuration, planner and operator work-control routes.
- Plausible first-party paths checked: project mission ratification, policy/identity revision, human decision return and permission enforcement, future/current adaptation arbitration.
- Why no material first-party path remains: the established ratifier creates the initial work context; controls are operational permissions or static configuration. No supported identity/ultimate-policy *regulatory* loop exists at the declared Gemba recursion rather than operator governance external to this artifact.

## Evidence gaps

- There was no provider-backed Onboarder dialogue, real multi-worker workspace collision trial or independently witnessed operator current-control decision. Source-wired capability and live effectiveness remain separate evidence types.
- The S1 claim is **bounded to the installed model-driven conversational plan unit**. Gemba does not own the tool-level coding S1 inside vendor CLIs or the mandatory external WorkPlane.
- S2 is **optional configured** auto-dispatch workspace collision attenuation, not generic scheduling or a default Beads-only capability.
- Three negative higher-function results are **bounded source-inspection findings**, not claims that integrated external agents/rigs or future plugin modes could never provide them.
- One legitimate follow-up would be a new frozen-revision assessment if upstream ships a real witness adaptor, serving-mode retrospective corrective loop or independent QA source; none can be credited ahead of the frozen commit.

## Conclusion

**Proposed general assessment, not yet canonical:** `S1=A / S2=C / S3=P / S3*=— / S4=— / S5=—` in the explicitly reviewed supported modes. Gemba's first-party model-mediated Onboarder produces plans via a validated feedback loop; opt-in native pool dispatch attenuates inter-session workspace collisions; human project operators exercise current whole-project priority and dispatch rights. The built-in consult/QA/walk/retro and project-creation mechanisms do **not** establish independent complementary audit, future-environment capability adaptation or ultimate identity governance under the frozen first-party evidence boundary. No external coding-agent reasoning is inherited. Source-first decision rests on shipped wiring and bounded counterfactuals, not on the structural checker or unobserved model performance.
