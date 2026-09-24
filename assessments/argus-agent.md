---
harness_id: argus-agent
project_name: Argus
repository: https://github.com/microsoft/ArgusAgent
review_ref: 746f76b7a74a1217507c9ee348eecd3b782f7c92
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: P
---

# Argus

## Review boundary

- System in focus: one persistent first-party Argus Project organization at pinned revision `746f76b7a74a1217507c9ee348eecd3b782f7c92`, including its Manager, Planner, Engineer, Reviewer, durable project daemon/backlog/state, SkillLoop, project/profile learning paths, operator control surfaces and Argus-owned long-command supervision.
- Purpose and identity: pursue one operator-defined research or engineering project across durable missions while separating current-control, planning, implementation, independent review, retained learning and operator-reserved authority.
- Relevant environment: the operator, project workspace/repository, files/builds/tests/experiments, external data and domain conditions, Agent CLI/model responses, credentials/hardware, persisted project/profile state and other independently running projects.
- Standard-distribution boundary: first-party Argus runtime, built-in roles, daemon, state machines, learning/review machinery and documented source installation. External model/Agent CLI implementations such as Copilot, Pi, Codex, Claude Code, Cursor, OpenCode, Grok, Qoder and DeepSeek Harness remain environment/providers and do not donate organizational autonomy.
- Credited operating / distribution surfaces: Manager front door and stage authority; continuous Planner/backlog; Engineer mission and tool execution; independent read-only Reviewer; `SkillLoop`/`SupervisedEngineer`; durable project daemon and operator control; post-mission TEAM/SELF Skill evolution; identity card; project-local vertical lifecycle; supervised long-command monitoring where it supports current operation.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/contributor workflows; technical-report prose as evidence where code/docs already establish behavior; external Agent CLI/model internals; separate Argus projects/daemons as sibling systems rather than S1 units inside this Project; framework self-maintenance before an operator-approved deployment; generic telemetry/logging when merely observational.
- First-party operating / deployment modes considered: bounded and standing Project campaigns; direct and staged TEAM work; persistent SELF operation; independent-review paths; attended operator control; unattended progression inside operator-granted authority; source-installed runtime using any supported external Agent CLI backend.
- Recursion level: one Argus Project is the primary system-in-focus because Argus documents Project as the persistent organizing boundary and gives each project its own daemon, workspace, backlog, transcript and outputs. Missions/Engineer work are operational activity within that project. Separate project daemons are separate systems at the same recursion, not automatically S1 units of one assessed Project.
- Reviewed revision: `746f76b7a74a1217507c9ee348eecd3b782f7c92`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Argus explicitly splits its driver function across Manager, Planner, Engineer and Reviewer. The Manager routes operator intent and owns project-stage changes; Planner reads current project state and chooses the next bounded mission; Engineer performs implementation/research/experiments and verification; Reviewer independently inspects the result and controls whether work settles, continues, replans or blocks. A Project daemon persists the campaign and serializes TEAM missions through a durable backlog.

The separation is operational rather than nominal. `SkillLoop` wires an Engineer runner to a first-party Reviewer and, by default, requires independent review. The Manager's stage implementation separately states that it is the sole writer of project stage and makes its own model judgment from current review/checklist evidence before applying advance/hold/rollback/complete. The operator remains a live parent: pause/abort/steering/authorization controls affect durable runtime state and replacement of a standing objective supersedes pending work.

Argus also closes a prospective adaptation path after operation. An isolated model-driven TEAM learning review examines the settled mission result and bounded project-local Skill candidates, decides whether a durable role procedure would improve later sessions, and can write reviewed procedures into profile-level Manager/Planner/Engineer/Reviewer Skill libraries. Those Skills are available to later tasks and sessions. This is distinct from ordinary in-task replanning and from framework source deployment.

Primary evidence:

- [`README.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/README.md) — Project runtime purpose, four-role authority split, external backends and human-reserved actions.
- [`docs/FEATURES.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/docs/FEATURES.md) — implemented role transitions, one-mission-per-project behavior, operator controls, learning and cross-session reuse.
- [`argus_skill/loop.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/loop.py) — first-party Engineer/Reviewer mission loop and default independent-review configuration.
- [`argus_skill/builtin_skills/manager/argus-manager-role.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/builtin_skills/manager/argus-manager-role.md) — Manager current-control authority and operator relationship.
- [`argus_skill/builtin_skills/planner/argus-planner-role.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/builtin_skills/planner/argus-planner-role.md) — current-project planning authority and boundaries.
- [`argus_skill/builtin_skills/reviewer/argus-reviewer-role.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/builtin_skills/reviewer/argus-reviewer-role.md) — independent audit judgment, direct checks and verdict semantics.
- [`argus_skill/manager/_stage_ops.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/manager/_stage_ops.py) — Manager model call, current-context fingerprint, sole stage write and current-control closure.
- [`argus_skill/life/supervisor/_evolution.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/life/supervisor/_evolution.py) and [`argus_skill/manager/skill_tidy.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/manager/skill_tidy.py) — post-mission prospective Skill adaptation and propagation.
- [`argus_skill/apps/_init_identity.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/apps/_init_identity.py) and [`argus_skill/life/memory.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/life/memory.py) — operator-owned persistent identity card and future-prompt return path.
- [`argus_skill/daemon/_life_worker_boot.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/daemon/_life_worker_boot.py) — parent-controlled standing-objective resume/replacement and Manager handoff.
- [`argus_skill/tools/subagent/_resource_admission.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/tools/subagent/_resource_admission.py) and [`_supervised_run.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/tools/subagent/_supervised_run.py) — command-resource admission and semantic long-run supervision, treated as current-operation support rather than proof of sibling-S1 coordination.

## S1 — Operations

- State: A
- Function: perform substantive project work through model-driven engineering/research missions that inspect project state, choose implementation/experimental actions, execute tools and absorb resulting evidence.
- Disturbance / variety regulated: task ambiguity, repository/workspace state, build/test failures, experimental outcomes, external data, tool results, implementation defects and domain-specific constraints encountered while producing the requested deliverable.
- Decisive decision or feedback right: choose substantive operational actions inside the admitted mission — implementation changes, research/experiment steps, commands and evidence-producing verification — and adapt those actions from returned project/tool evidence.
- Decision owner: the model-driven Engineer role within the first-party Argus mission runtime.
- Supporting / enforcement mechanisms: Planner mission brief, `SkillLoop`, tool/sandbox policy, project Wiki/Skills, durable command handoff, acceptance constraints, budgets, checkpoints and Reviewer feedback.
- Closure path: Manager/Planner admits a mission → Engineer model inspects current project/evidence and chooses work/tool actions → Argus executes those actions and returns files/command/test/experiment observations → Engineer changes subsequent action or reaches its decision point → result enters independent review/settlement.
- Boundary reachability: the Engineer role, mission loop, tool execution and feedback transport are standard Argus runtime surfaces; an adopter supplies an external model backend but does not have to construct the organizational S1 loop or its decision right.
- Why this is / is not agent-owned: Argus explicitly assigns implementation, research, experiments and artifacts to Engineer model decisions. Deterministic host gates constrain execution and Reviewer owns acceptance, but neither removes Engineer ownership of the operational next-action loop.
- Evidence: [`README.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/README.md); [`docs/FEATURES.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/docs/FEATURES.md); [`argus_skill/loop.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/loop.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: external Agent CLI/model services supply inference, not organizational autonomy. Engineer cannot certify its own work; that is a deliberate S3* separation rather than evidence against S1 ownership.

## S2 — Coordination

- State: —
- Function: no material first-party S2 relation is established among multiple distinct autonomous S1 units inside one assessed Argus Project.
- Disturbance / variety regulated: Argus regulates queues, hardware/resource leases and background command execution, but the reviewed Project boundary does not establish sibling autonomous S1 operations whose mutual interference is being attenuated as S2.
- Decisive decision or feedback right: none established for inter-S1 coordination at this recursion.
- Decision owner: none established.
- Supporting / enforcement mechanisms: serial TEAM backlog, one-mission-per-project daemon, resource ledger for long-command workers, CPU/resource admission, semantic experiment supervision and durable subagent registries.
- Closure path: no qualifying sibling-S1 disturbance → attenuation → changed later S1 behavior loop was found at the Project recursion.
- Why this is / is not agent-owned: background `subagent` and supervised-command facilities can run durable work and arbitrate hardware, but naming and concurrency do not make those command workers independent S1 organizations. Argus explicitly serializes TEAM missions within a project, while separate project daemons are separate systems-in-focus.
- Evidence: [`docs/FEATURES.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/docs/FEATURES.md); [`argus_skill/tools/subagent/_resource_admission.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/tools/subagent/_resource_admission.py); [`argus_skill/tools/subagent/_supervised_run.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/tools/subagent/_supervised_run.py).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: another system boundary that deliberately groups several Argus Projects could expose a higher-recursion coordination problem, but that would be a separate system-in-focus and needs its own evidence.

### Absence scope

- Surfaces inspected: Project daemon/backlog; Planner/Engineer mission flow; durable direct/supervised subagents; resource ledger and yield requests; separate-project behavior; Manager/Reviewer roles.
- Plausible first-party paths checked: concurrent background commands; supervised experiments; hardware lease arbitration; queued TEAM requests; multiple project daemons; role-to-role handoffs.
- Why no material first-party path remains: within one Project, TEAM missions are durably serialized and command workers are subordinate execution mechanisms of the active mission rather than proven autonomous sibling S1 units. Separate Projects are isolated peer systems, so their concurrency cannot be imported into this Project's S2 assessment.

## S3 — Inside-and-now control

- State: A(P)
- Function: maintain current control of the Project's active campaign by interpreting whole-project evidence and deciding stage progression, rollback, hold or completion while retaining an explicit operator parent mode for live intervention.
- Disturbance / variety regulated: project-stage mismatch, unresolved checklist/review obligations, failed or incomplete missions, current objective changes, planner/reviewer conflicts, pauses, authorization needs and conditions requiring rollback or a different current direction.
- Decisive decision or feedback right: autonomous mode — decide and write the Project's current stage and current-control transition from present evidence; parent mode — pause, abort, steer, authorize or replace the standing objective through first-party operator surfaces.
- Decision owner: autonomous mode — the model-driven Manager, explicitly the sole writer of project stage; parent mode — the operator for live intervention and replacement/authorization decisions reserved to the parent.
- Supporting / enforcement mechanisms: current pipeline/campaign/control-head fingerprint, current-stage checklist, Reviewer/Planner structured evidence, Manager read-only project inspection, strict decision parser, stage-machine gates, durable control state and continuous-config compare-and-swap.
- Closure path: current project/review/checklist/control state is assembled → Manager model independently chooses advance/hold/rollback/complete → first-party stage code commits the legal decision to durable Project state → Planner/Engineer subsequent work runs under the changed stage; alternatively an operator control/replacement updates durable runtime/campaign state and later work follows it.
- Boundary reachability: Manager stage authority and operator control are wired into standard Project execution and daemon lifecycle; neither requires a downstream user to invent a whole-system current-control relation.
- Why this is / is not agent-owned: in autonomous mode the Manager model, not a deterministic scheduler, owns the semantic current-control decision. Stage/checklist code validates and commits it. Parent controls coexist as a distinct legitimate mode and therefore do not erase autonomous S3 ownership.
- Evidence: [`argus_skill/manager/_stage_ops.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/manager/_stage_ops.py); [`argus_skill/builtin_skills/manager/argus-manager-role.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/builtin_skills/manager/argus-manager-role.md); [`docs/FEATURES.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/docs/FEATURES.md); [`argus_skill/daemon/_life_worker_boot.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/daemon/_life_worker_boot.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: deterministic completion gates and stale-context holds are enforcement, not the autonomous S3 owner. Parent credit is for explicit live control/replacement paths, not mere configuration editability.
- Whole-system current view: the Manager decision binds current pipeline state, campaign identity and control head, reads current-stage checklist plus Reviewer/Planner evidence and may inspect relevant project evidence before deciding overall direction.
- Current-control decision scope: Project stage advance/hold/rollback/complete, workflow/lifetime direction, replacement of standing intent, and live pause/abort/steering/authorization that govern what current or next mission may proceed.

### Ownership mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Manager model | current review/planner/checklist/project evidence requires a stage/current-control decision | Manager verdict → stage validation → durable advance/hold/rollback/complete → subsequent Planner/Engineer work follows current stage | `argus_skill/manager/_stage_ops.py`, Manager role contract |
| Parent (`P`) | Operator | explicit pause/abort/steering/authorization or replacement of standing objective | Manager/Host control path updates durable daemon/campaign state, supersedes or pauses work, and subsequent operation follows the operator decision | `docs/FEATURES.md`, `argus_skill/daemon/_life_worker_boot.py` |

## S3* — Complementary audit

- State: A
- Function: independently challenge Engineer claims/results against the objective, direct project artifacts, verification evidence and active vertical requirements before accepting, repairing or replanning work.
- Disturbance / variety regulated: self-reported success, implementation defects, regressions, weak evidence, incomplete scope, unsupported research claims, failed verification and work whose next useful move lies outside the current mission.
- Decisive decision or feedback right: issue the independent verdict `done`, `continue`, `replan_requested` or `blocked` from direct evidence and thereby decide whether the current work may settle or must return to Engineer/Planner/operator.
- Decision owner: the model-driven read-only Reviewer role.
- Supporting / enforcement mechanisms: Reviewer-specific prompt/Skill contract, read-only sandbox, project-file/result inspection, short deterministic checks, distinct role session/backend boundary, structured `next_action`, review-required flags and Host transition mapping.
- Closure path: Engineer reaches a decision point and reports its result → Reviewer independently inspects relevant files/results and may rerun short checks → Reviewer produces a verdict → `done` permits settlement, `continue` returns concrete work to Engineer, `replan_requested` returns to Planner, and `blocked` escalates to the operator → subsequent operation changes accordingly.
- Boundary reachability: independent review is a first-party role wired by `SkillLoop`/`SupervisedEngineer` and enabled by default for the standard reviewed path; callers may supply a distinct Reviewer runner, but they need not construct the audit organization.
- Why this is / is not agent-owned: the audit judgment is explicitly assigned to a separate model role that cannot edit the work it judges. Host code transports/enforces the verdict but does not decide whether the evidence is correct or sufficient.
- Evidence: [`argus_skill/builtin_skills/reviewer/argus-reviewer-role.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/builtin_skills/reviewer/argus-reviewer-role.md); [`argus_skill/loop.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/loop.py); [`docs/FEATURES.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/docs/FEATURES.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: bounded low-risk work may explicitly waive a separate Reviewer where the Host contract permits Engineer self-verification. The positive claim is for the standard first-party independent-review mode, which is materially supported and default-configured rather than inferred for every possible task.
- Claim being audited: that Engineer's current implementation/research result satisfies the admitted mission/objective with adequate correctness, evidence, limitations and vertical-specific completion conditions.
- Ordinary reporting path: Engineer's own result, verification output, project changes and mission status presented at its decision point.
- Complementary access path: Reviewer directly opens relevant project files/results, applies the current objective/vertical requirements and can run short deterministic checks; failed verification overrides Engineer self-report.
- Independence boundary: Reviewer is a distinct read-only model role/session, cannot edit the work under review, and can use a separately supplied runner; its judgment is therefore not confined to Engineer's narrative or repair path.
- Who acts on findings: Reviewer decides the verdict; Engineer performs requested repairs on `continue`, Planner changes direction on `replan_requested`, operator resolves parent-owned blockers, and Host settles only accepted work.

## S4 — Outside-and-then intelligence

- State: A
- Function: convert evidence learned from completed interaction/project work into reviewed reusable role procedures intended to improve future missions and sessions, then return those adaptations into the operating role libraries.
- Disturbance / variety regulated: project/domain patterns that current procedures do not yet capture, recurring effective techniques, verified failure mechanisms, role-review weaknesses and environment-specific lessons whose applicability may extend beyond the just-settled mission.
- Decisive decision or feedback right: judge whether observed mission evidence warrants a durable future-facing procedure and, when justified, create or update the appropriate shared Manager/Planner/Engineer/Reviewer Skill rather than merely preserving current-task state.
- Decision owner: an isolated first-party model-driven TEAM learning reviewer operating after mission settlement; SELF learning provides a parallel future-facing path for stable conversation/operator patterns.
- Supporting / enforcement mechanisms: post-mission trigger, bounded candidate evidence, profile role Skill roots, project→shared propagation, verifier-surface quarantine, reviewed-candidate receipts, Wiki/project evidence and cross-session Skill loading.
- Closure path: current mission settles and leaves project/environment evidence plus candidate learning → isolated learning model asks what durable procedure would materially improve later sessions → model creates/updates a reviewed role Skill when evidence warrants it → shared profile Skill becomes available to the next applicable mission/session → future operational behavior changes.
- Boundary reachability: TEAM and SELF evolution are documented first-party runtime mechanisms, enabled on the standard profile path and invoked from the life supervisor; no downstream adaptation service is required.
- Why this is / is not agent-owned: the harness supplies timing, bounded evidence and safety/quarantine constraints, but the semantic choice of what future procedure to retain and its content is made by a model turn. This is prospective organizational adaptation, not merely current-mission replanning or passive memory storage.
- Evidence: [`docs/FEATURES.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/docs/FEATURES.md); [`argus_skill/life/supervisor/_evolution.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/life/supervisor/_evolution.py); [`argus_skill/manager/skill_tidy.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/manager/skill_tidy.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: generic Wiki persistence or in-mission Planner replanning would not establish S4 alone. The `A` claim relies on the explicit post-settlement, later-session-oriented model review and its return into loaded role capability.
- External distinction: settled work exposes distinctions in the project/domain environment — successful techniques, verified failures, evidence limitations and operator interaction patterns — that are compared against the role procedures currently available.
- Future / prospective distinction: the TEAM learning prompt explicitly asks whether a durable procedure would materially improve later sessions; documentation specifies first use on the next mission and reuse across later tasks/sessions.
- Adaptation option generated: the learning model may author or update a profile-level semantic Skill for Manager, Planner, Engineer or Reviewer, with scope/evidence limits; unjustified adaptations are withheld or quarantined.
- Path back into current capability / S3: profile role Skills are part of later role prompt/tool context and can be read/applied by subsequent Manager/Planner/Engineer/Reviewer operation; cross-role visibility rules return the reviewed procedure to future current-control and operational decisions.

## S5 — Policy and identity

- State: P
- Function: preserve operator-defined identity, red lines, standing purpose and reserved ultimate-policy decisions, and return those authoritative choices into subsequent Argus operation.
- Disturbance / variety regulated: identity/persona changes, operator red lines, standing-objective replacement, credential/payment/irreversible/publication decisions, scope expansion and other questions that the autonomous roles are not legitimate to decide for themselves.
- Decisive decision or feedback right: define/edit the persistent operator identity card, replace or re-arm the standing objective, and make the actions explicitly reserved for human authority.
- Decision owner: the human operator as first-party parent authority.
- Supporting / enforcement mechanisms: persistent `identity.md`, identity wizard and `/identity` update surface, default-identity suppression, prompt injection only for operator-edited identity, continuous campaign config/generation, Manager front door, durable parent controls and role contracts that stop for reserved decisions.
- Closure path: an identity/ultimate-policy matter is presented to or changed by the operator → first-party identity/control state persists the authoritative choice → edited identity enters later role context or standing objective/control state is replaced/re-armed → Manager/Planner/Engineer/Reviewer resume future operation under that parent decision.
- Boundary reachability: the identity card, operator controls and standing-objective lifecycle ship with Argus and are directly reachable through its standard CLI/Web/daemon operation; the parent does not need to add a separate governance component.
- Why this is / is not agent-owned: Argus intentionally reserves these rights to the operator. Manager may interpret and route within the granted purpose, but it cannot legitimately rewrite operator-binding identity/red lines or self-authorize credentials, payment, irreversible actions or publication.
- Evidence: [`argus_skill/apps/_init_identity.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/apps/_init_identity.py); [`argus_skill/life/memory.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/life/memory.py); [`docs/FEATURES.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/docs/FEATURES.md); [`README.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/README.md); [`argus_skill/daemon/_life_worker_boot.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/daemon/_life_worker_boot.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary stage transitions and task approvals remain S3/current-operation concerns. S5 credit is limited to identity/ultimate-policy matters explicitly bound to the operator, not every human interaction.
- Identity / ultimate-policy issue: who Argus is for this operator, its operator-binding persona/red lines, which standing purpose governs the Project, and whether actions outside delegated authority such as credentials/payment/irreversible changes/publication may proceed.
- Ultimate authority in each claimed mode: parent mode only — the operator authors/edits identity and retains the reserved policy rights. No autonomous S5 mode is credited.
- Return-to-operation path: `identity.md` is persisted and, once operator-edited, its text is returned into subsequent model context; operator replacement/re-arm of standing intent updates durable campaign state, after which Manager produces a new handoff and later missions follow the authoritative purpose.

## Recursion

The assessed recursion is one persistent Argus Project. Its Engineer missions are the operational work coordinated by one Project's Manager/Planner/Reviewer metasystem; durable command workers remain subordinate execution mechanisms unless separate evidence establishes them as viable systems. Multiple Argus Projects each have isolated daemon/workspace/backlog state and therefore require their own system-in-focus treatment before any higher-recursion organization can be inferred.

## Variety, escalation and closure

Argus attenuates operational variety through Manager intent routing, Planner mission bounding, vertical/stage contracts, serial project backlog, resource admission, safe tool boundaries and deterministic completion gates. It amplifies regulatory capacity through model-driven Manager current control, independent read-only Reviewer challenge, supervised experiments, operator escalation and post-mission evolution of role Skills.

Exceptional paths have explicit closure: Reviewer `continue` returns defects to Engineer, `replan_requested` returns direction to Planner, `blocked` reaches the operator, Manager stage decisions update durable project state, operator replacement supersedes stale pending work, and reviewed learning returns into later role operation. These paths are classified by the organizational function they perform rather than by component names.

## Evidence gaps

No material evidence gap remains that requires `?` at this pinned boundary. The boundary-sensitive conclusion is S2: Argus has substantial multi-agent vocabulary, durable background workers and resource arbitration, but first-party Project semantics serialize TEAM missions and do not establish multiple distinct autonomous sibling S1 units inside one Project. Those mechanisms are therefore not promoted to S2 without the required inter-S1 evidence.