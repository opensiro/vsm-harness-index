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
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
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

- State: ?
- Function: potential distinct source-backed assessment of delivery claims and project drift, beyond ordinary worker status reporting; binding complementary corrective closure not yet established here.
- Disturbance / variety regulated: incorrect or unsupported worker completion, stale milestones, delivery/QA drift.
- Decisive decision or feedback right: a sufficiently independent audit finding must reach a control path changing subsequent work; the reviewed persona/walk assembly and general QA packages have not yet shown this as an end-to-end, standard-mode requirement.
- Decision owner: unresolved; specialized persona consults may rely on separately launched external model CLIs while the operator remains a parent, and no first-party autonomous auditor has been proven.
- Supporting / enforcement mechanisms: persona dispatcher, audit log, walk agenda, candidate QA/review gates and corrections.
- Closure path: candidate operational records → walk/persona/QA evidence gathering → potential findings → *unproven* independent corrective return.
- Boundary reachability: walk agenda and persona consult APIs are shipped, but the distinct independent judgment and its mandatory or optional findings-to-operations path require targeted review.
- Why this is / is not agent-owned: a consult log or test result alone does not establish a distinct auditor's decision right, independence and corrective closure.
- Evidence: [internal/persona/dispatcher.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/persona/dispatcher.go); [internal/persona/applier.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/persona/applier.go); [internal/walk/agenda.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/walk/agenda.go); [internal/qa/regression/suite.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/qa/regression/suite.go); [internal/server/consults_post.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/server/consults_post.go).
- Basis: structural candidate; insufficient evidence for either positive grade or bounded absence.
- Confidence: high in uncertainty, not in an autonomous audit claim.
- Caveats: investigate whether user-applied persona corrections offer a genuinely complementary source rather than worker self-report.

## S4 — Outside-and-then intelligence

- State: ?
- Function: possible prospective adaptation through roadmap/planning, drift, retrospective and agent-profile calibration, but distinct external-environment sensing and effect on future capability not established.
- Disturbance / variety regulated: changing project environment, incoming external requirements, changing worker capability/availability.
- Decisive decision or feedback right: propose/choose a future capability change from external-facing evidence and return that change into working policy/tools; not yet traced end-to-end.
- Decision owner: unresolved; operator-owned planning, model persona suggestions and deterministic score/profile refresh are not necessarily S4.
- Supporting / enforcement mechanisms: planning personas and epic-order skill, retro comparison/calibration, workflow scheduling and project history.
- Closure path: possible observations → prospective recommendations → **unverified** choice/installation into subsequent current operational capability.
- Boundary reachability: planner/retrospective code ships; whether the credited S4-specific path is actually selected and closed in standard modes remains open.
- Why this is / is not agent-owned: memory, backlog reprioritization, planned epics or retrospective scores are not sufficient without a separately evidenced outside-and-then loop.
- Evidence: [internal/planner/retro/runner.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/planner/retro/runner.go); [internal/planner/scanscheduler/scheduler.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/planner/scanscheduler/scheduler.go); [internal/planner/profile.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/planner/profile.go); [internal/persona/dispatcher.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/persona/dispatcher.go).
- Basis: plausible first-party candidate, not enough to grade.
- Confidence: high in recorded coverage gap.
- Caveats: follow live wiring to discriminate present-work S3 from genuine prospective S4.

## S5 — Identity and ultimate policy

- State: ?
- Function: possible project-purpose identity and parent ratification of a new project's work plan; does not yet establish ongoing ultimate policy and identity regulation for the whole Gemba organization.
- Disturbance / variety regulated: what this project's ultimate purpose and binding operator policy are.
- Decisive decision or feedback right: final parent ratification of proposed project identity/plan and any later ultimate-policy changes; ordinary approval of plan data is not enough by itself.
- Decision owner: project operator for ratification; whether an actual higher-level S5 closure lives in the same first-party recursion is unresolved.
- Supporting / enforcement mechanisms: Onboarder state and ratifier, per-project configuration and host access policy.
- Closure path: model-generated proposal → explicit ratification → WorkPlane mutations; ongoing ultimate identity/policy review and binding return **not established**.
- Boundary reachability: production ratifier exists, but its project-creation transaction is not automatically the VSM S5 identity organ.
- Why this is / is not agent-owned: authorization remains human-owned; no distinct ultimate-policy decision by the Onboarder or scheduler is demonstrated.
- Evidence: [internal/server/newproject_ratify.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/server/newproject_ratify.go); [internal/cli/serve.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/cli/serve.go); [internal/personas/onboarder/onboarder.go](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/personas/onboarder/onboarder.go); [internal/auth/](https://github.com/GembaCore/gemba-core/blob/64c266f889c6d6a579904c5e336676fa1c49b216/internal/auth/).
- Basis: structural candidate and material policy-boundary uncertainty.
- Confidence: medium-high for absence of established autonomous ownership; unresolved parent-mode qualification.
- Caveats: test whether project initialization or tenant policy constitutes a first-party and complete S5 loop rather than local setup authorization.

## Evidence gaps

- Source-based structure and shipped wiring were inspected at frozen commit; there was no provider-backed Onboarder dialogue, real multi-worker collision trial or human operator observation. Those missing live witnesses do not erase source-confirmed paths, but limit outcome claims.
- S3* remains `?` pending independent-vs-producer access and a demonstrable correction return in one supported mode.
- S4 remains `?` pending first-party external-and-prospective sensing, option selection, capability change and operational effect trace.
- S5 remains `?` pending proof that parent-approved mission/policy selection is an ongoing identity-level function with returned implementation, not just a new-project form.
- The external coding-agent subprocesses and Beads/Dolt data-plane internals were not assessed as Gemba-owned autonomous cognitive actors.

## Conclusion

**Proposed, not canonical.** At the narrow shipped Gemba organization boundary, the first-party Onboarder provides bounded model-driven planning S1; optional first-party worker-pool collision gates provide S2 construction; the shipped project board/native dispatch exposes a parent-owned current-control path. No external coding-agent cognition is borrowed. S3*/S4/S5 are left unresolved where adjacent mechanisms do not yet show decisive organizational ownership and closure. This assessment should not be admitted until remaining evidence gaps and its operator-S3 interpretation receive a complete source-first disposition.
