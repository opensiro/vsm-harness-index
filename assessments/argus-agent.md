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
last_checked_ref: 746f76b7a74a1217507c9ee348eecd3b782f7c92
last_checked_at: 2026-09-29
assessment_changed_at: 2026-09-29
last_reassessment_round: R3
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: P
---

# Argus

## Review boundary

- System in focus: one persistent first-party Argus Project organization at pinned revision `746f76b7a74a1217507c9ee348eecd3b782f7c92`, including Manager, Planner, Engineer, Reviewer, the durable Project daemon/backlog/state, `SkillLoop`, shipped Agent Team runtime, project/profile learning paths and operator control surfaces.
- Purpose and identity: pursue one operator-defined research or engineering project across durable missions while separating current control, planning, implementation, independent review, retained learning and operator-reserved authority.
- Relevant environment: the operator, project workspace/repository, files/builds/tests/experiments, external data and domain conditions, Agent CLI/model responses, credentials/hardware, persisted project/profile state and other independently running Argus Projects.
- Standard-distribution boundary: first-party Argus runtime, built-in roles and Skills, daemon, state machines, Team runtime, learning/review machinery and documented source installation. External model/Agent CLI implementations remain environment/providers and do not donate organizational autonomy.
- Credited operating / distribution surfaces: Manager front door and stage authority; continuous Planner/backlog; Engineer mission and tool execution; independent read-only Reviewer; `SkillLoop`/`SupervisedEngineer`; Agent Team lead contract, durable team control CLI, task board, Curator and teammate entrypoint; durable Project daemon/operator control; post-mission TEAM/SELF Skill evolution; identity card and project-local vertical lifecycle.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/contributor workflows; technical-report prose where runtime/docs already establish behavior; external Agent CLI/model internals; separate Argus Projects as sibling systems rather than S1 units inside this Project; companion applications unless wired into the assessed Project mode; generic telemetry/logging when merely observational.
- First-party operating / deployment modes considered: bounded and standing Project campaigns; direct and staged TEAM work; Agent Team parallel missions; persistent SELF operation; independent-review paths; attended operator control; unattended progression inside operator-granted authority; source-installed runtime using a supported external Agent CLI backend.
- Recursion level: one Argus Project is the primary system-in-focus. Ordinary Engineer missions and Agent Team teammate missions are operational activity inside that Project. Separate Project daemons are separate systems at the same recursion and are not imported as S1 units of this Project.
- Reviewed revision: `746f76b7a74a1217507c9ee348eecd3b782f7c92`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Argus splits its driver function across Manager, Planner, Engineer and Reviewer. Manager routes operator intent and owns Project-stage changes; Planner chooses bounded missions from current Project state; Engineer performs implementation/research/experiments; Reviewer independently inspects results and controls whether work settles, continues, replans or blocks. The Project daemon persists campaign state.

Argus also ships an Agent Team runtime inside the same Project. An Engineer or explicitly assigned lead forms a durable backlog only when multiple tasks can progress concurrently, partitions writable paths and dependencies, chooses pool width and later synthesizes results. The daemon-resident Curator is the sole allocator/reaper: it atomically claims dependency-ready tasks and launches fresh teammate missions. Each teammate executes one substantive headless Argus Engineer mission with its own Reviewer, isolated life/event state and result shard. The lead is the single writer of the canonical synthesis, which still enters the ordinary mission Reviewer path.

The Manager remains sole Project-stage authority. Teammates explicitly run with `holds_stage_authority=False` because otherwise concurrent teammates sharing the Project root could each write `PIPELINE_STATE.json` from a task-local view. This is a concrete shipped coordination boundary rather than generic multi-agent vocabulary.

After operation, Argus closes a prospective adaptation path: an isolated model-driven learning review can turn settled evidence into reviewed reusable role Skills scoped project → vertical → global and make them available to later work. Ultimate identity/policy rights remain with the operator.

Primary evidence:

- [`README.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/README.md) — Project purpose, four-role authority split and human-reserved actions.
- [`docs/FEATURES.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/docs/FEATURES.md) — implemented role transitions, operator controls and learning.
- [`argus_skill/builtin_skills/agent-team-lead.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/builtin_skills/agent-team-lead.md) — agent-owned Team formation/partition/synthesis contract and explicit overlap constraints.
- [`argus_skill/tools/team.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/tools/team.py) — agent-facing Team control plane.
- [`argus_skill/team/task_board.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/team/task_board.py) — atomic claim/dependency coordination and durable ownership state.
- [`argus_skill/team/curator.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/team/curator.py) — bounded teammate allocation/reaping.
- [`argus_skill/team/teammate_entry.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/team/teammate_entry.py) — substantive teammate mission, isolated local state and explicit removal of sibling stage-write authority.
- [`argus_skill/manager/_stage_ops.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/manager/_stage_ops.py) — Manager model judgment and sole Project-stage write.
- [`argus_skill/life/supervisor/_evolution.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/life/supervisor/_evolution.py) and [`argus_skill/manager/skill_tidy.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/manager/skill_tidy.py) — prospective Skill adaptation.
- [`argus_skill/apps/_init_identity.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/apps/_init_identity.py) and [`argus_skill/life/memory.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/life/memory.py) — operator-owned identity and return path.

## Operational model

The ordinary S1 is a model-driven Engineer mission. In Agent Team mode, several fresh teammate Engineer→Reviewer missions become distinct bounded S1 units for one parallel work package: each has its own objective, acceptance evidence, execution feedback, isolated life state and result shard. The Team lead owns semantic coordination decisions—whether parallelism is justified, task/path partitioning, dependency structure, priority, pool width and final synthesis—while Curator, locks and compare-and-set machinery enforce those decisions. Manager owns whole-Project current control; Reviewer owns complementary audit; the post-mission learning reviewer owns future-facing procedural adaptation; the operator owns ultimate identity/policy.

## S1 — Operations

- State: A
- Function: perform substantive Project work through model-driven engineering/research missions that inspect project state, choose implementation or experimental actions, execute tools and absorb returned evidence.
- Disturbance / variety regulated: task ambiguity, repository/workspace state, build/test failures, experimental outcomes, external data, tool results, implementation defects and domain-specific constraints.
- Decisive decision or feedback right: choose substantive operational actions inside an admitted mission and adapt subsequent actions from returned project/tool evidence.
- Decision owner: the model-driven Engineer role; in Team mode each fresh teammate Engineer owns its bounded task-local operation.
- Supporting / enforcement mechanisms: Planner mission brief, `SkillLoop`, tool/sandbox policy, vertical context, budgets, checkpoints and Reviewer feedback.
- Closure path: mission admitted → Engineer inspects evidence and chooses work/tool actions → Argus executes and returns observations → Engineer adapts or reaches its decision point → result enters independent review/settlement.
- Boundary reachability: Engineer and teammate Engineer missions are first-party standard runtime surfaces; external model backends supply inference but do not require downstream construction of the organizational loop.
- Why this is / is not agent-owned: semantic operational choices are model-driven; host gates constrain execution and Reviewer controls acceptance without replacing Engineer task-local discretion.
- Evidence: [`argus_skill/loop.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/loop.py); [`argus_skill/team/teammate_entry.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/team/teammate_entry.py); [`README.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: teammate missions deliberately do not inherit Project-stage authority; that preserves recursion/coordination and does not reduce their task-local S1 autonomy.

## S2 — Coordination

- State: A
- Function: stabilize parallel teammate S1 work inside one Agent Team by partitioning mutable work, respecting dependencies, preventing duplicate ownership/stage writes and returning independently settled shards to one synthesis path.
- Disturbance / variety regulated: duplicate task claims; double-spawn into the same workdir after a live re-form; overlapping writable paths/shared mutable outputs; dependency-order violations; excessive concurrent width; and competing writes by multiple task-local teammates to shared Project stage state.
- Decisive decision or feedback right: decide whether Team mode is warranted and choose the coordination arrangement—task decomposition, non-overlapping `owns_paths`, dependencies, priorities, pool width, and final synthesis—then revise/stop that arrangement when Team status or blocked work requires it.
- Decision owner: the model-driven Engineer or explicitly assigned Team lead for semantic coordination choices. Curator owns deterministic process-lifecycle execution of the lead's admitted coordination plan but not the semantic partition/priority decision.
- Supporting / enforcement mechanisms: durable task board; exclusive locks and atomic writes; compare-and-set claims; dependency-ready eligibility; bounded Curator pool; isolated teammate life roots/result shards; nested-team admission guard; `holds_stage_authority=False`; single-writer Curator lifecycle/leaderboard and lead synthesis.
- Closure path: lead observes a parallelizable work package → chooses file-disjoint tasks/dependencies/width and forms the Team → Curator claims only eligible tasks and launches distinct teammate missions → runtime constraints prevent duplicate ownership and competing stage writes → teammate Reviewer-settled shards return to the shared board → lead inspects results, drains/dissolves the pool and writes one canonical synthesis → subsequent Project operation/review proceeds from that coordinated result.
- Boundary reachability: Agent Team is a built-in Skill plus first-party `argus_skill.tools.team`, daemon Curator, task board and teammate entrypoint reachable from a normal running Project; no downstream coordination subsystem must be invented.
- Why this is / is not agent-owned: removing the lead's semantic partition/dependency/width/synthesis judgment while retaining locks/Curator would not make materially the same coordination decisions. Deterministic machinery enforces a chosen arrangement; it does not choose which tasks are safe to parallelize or how their outputs should be synthesized.
- Evidence: [`argus_skill/builtin_skills/agent-team-lead.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/builtin_skills/agent-team-lead.md); [`argus_skill/tools/team.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/tools/team.py); [`argus_skill/team/task_board.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/team/task_board.py); [`argus_skill/team/teammate_entry.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/team/teammate_entry.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: `owns_paths` is a lead coordination contract rather than a filesystem sandbox, so Team formation is explicitly withheld when prompt-level ownership is insufficient. That limitation is itself part of the S2 attenuation policy.
- Distinct S1 units: two or more concurrently running fresh teammate Engineer→Reviewer missions, each with its own objective, acceptance evidence, local life state and result shard.
- Inter-S1 disturbance: concurrent teammates can otherwise claim the same task, touch the same mutable paths/output, violate dependency order, overrun admitted capacity, or independently write shared Project stage state from incompatible task-local views.
- Attenuating coordination relation: lead-chosen disjoint task/path/dependency/priority/width plan, enforced by atomic task claims, dependency gating, one Curator process-lifecycle owner, isolated teammate state and suppression of teammate stage authority.
- Feedback into subsequent S1 behaviour: the durable board determines which teammate may run what next; failed/blocked/finished states change later claim eligibility and pool refill; result shards/leaderboard inform later teammate objectives and the lead's synthesis; draining/dissolution stops further teammate launches.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the path is explicitly tied to concrete sibling interference in concurrent substantive operations and changes whether/how those S1 units may execute, own work and touch shared authority/state.

## S3 — Inside-and-now control

- State: A(P)
- Function: maintain current control of the Project campaign by interpreting whole-Project evidence and deciding stage progression, rollback, hold or completion, with a distinct operator parent mode for live intervention.
- Disturbance / variety regulated: stage mismatch, unresolved checklist/review obligations, failed or incomplete missions, objective changes, planner/reviewer conflicts, pauses and authorization needs.
- Decisive decision or feedback right: autonomous mode—decide/write current Project stage from present evidence; parent mode—pause, abort, steer, authorize or replace the standing objective.
- Decision owner: autonomous mode—the model-driven Manager; parent mode—the operator.
- Supporting / enforcement mechanisms: campaign/control-head fingerprint, stage checklist, Reviewer/Planner evidence, strict decision parser, stage-machine gates and durable control state.
- Closure path: current Project evidence assembled → Manager chooses advance/hold/rollback/complete → legal decision persists → later Planner/Engineer work follows it; alternatively operator control updates durable campaign state and later operation follows that decision.
- Boundary reachability: Manager stage authority and operator control are wired into standard Project execution/daemon lifecycle.
- Why this is / is not agent-owned: Manager owns the semantic current-control choice; deterministic stage code validates/commits it. Parent controls are a separate supported mode.
- Evidence: [`argus_skill/manager/_stage_ops.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/manager/_stage_ops.py); [`docs/FEATURES.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/docs/FEATURES.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: deterministic completion gates and stale-context holds enforce but do not own the semantic S3 decision.
- Whole-system current view: Manager binds current pipeline/campaign/control-head state, checklist and Reviewer/Planner evidence and may inspect Project evidence before deciding overall direction.
- Current-control decision scope: Project stage advance/hold/rollback/complete, current workflow direction, standing-intent replacement and live pause/abort/authorization.

### Ownership mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Manager model | current review/planner/checklist/project evidence requires a Project-level current-control decision | Manager verdict → stage validation → durable state → subsequent work follows the result | `argus_skill/manager/_stage_ops.py` |
| Parent (`P`) | Operator | explicit pause/abort/steering/authorization or standing-objective replacement | operator control updates durable campaign state → subsequent work follows it | `docs/FEATURES.md`, daemon control paths |

## S3* — Complementary audit

- State: A
- Function: independently challenge Engineer claims/results against objective, direct artifacts, verification evidence and active vertical requirements.
- Disturbance / variety regulated: self-reported success, implementation defects, regressions, weak evidence, incomplete scope and unsupported claims.
- Decisive decision or feedback right: issue `done`, `continue`, `replan_requested` or `blocked` from direct evidence and determine whether work settles or returns to Engineer/Planner/operator.
- Decision owner: model-driven read-only Reviewer.
- Supporting / enforcement mechanisms: Reviewer-specific role contract, read-only sandbox, artifact inspection, short checks, distinct role session/backend and host transition mapping.
- Closure path: Engineer reports result → Reviewer directly inspects evidence → verdict → settlement, repair, replanning or operator escalation changes subsequent work.
- Boundary reachability: independent review is first-party and wired into `SkillLoop`; teammate missions also retain their own Reviewer before returning shards.
- Why this is / is not agent-owned: a distinct model role makes the audit judgment and cannot edit the work it judges; host code transports/enforces the verdict.
- Evidence: [`argus_skill/loop.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/loop.py); [`argus_skill/roles/prompts/reviewer.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/roles/prompts/reviewer.py); [`argus_skill/team/teammate_entry.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/team/teammate_entry.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: bounded low-risk paths may explicitly waive a separate Reviewer; the positive claim is for the standard independent-review mode.
- Claim being audited: that the current Engineer or teammate result satisfies its admitted objective with adequate correctness/evidence.
- Ordinary reporting path: Engineer result, verification output, project changes and mission status.
- Complementary access path: Reviewer directly opens project artifacts/results and may run short checks rather than trusting Engineer narrative.
- Independence boundary: distinct read-only model role/session, unable to repair the artifact it judges.
- Who acts on findings: Engineer repairs on `continue`, Planner changes direction on `replan_requested`, operator resolves parent-owned blockers, and Host settles accepted work.

## S4 — Outside-and-then intelligence

- State: A
- Function: convert evidence learned from completed Project/environment interaction into reviewed reusable procedures intended to improve later missions/sessions.
- Disturbance / variety regulated: recurring effective techniques, verified failure mechanisms, domain changes/patterns and role-review weaknesses not captured by current procedures.
- Decisive decision or feedback right: judge whether settled evidence warrants a durable future-facing procedure and choose its content/scope.
- Decision owner: isolated first-party model-driven TEAM learning reviewer; SELF learning supplies a parallel future-facing path for stable operator/conversation patterns.
- Supporting / enforcement mechanisms: post-mission trigger, bounded candidate evidence, project→vertical→global scope rules, role Skill roots, reviewed receipts and quarantine constraints.
- Closure path: mission settles with environment/project evidence → learning model judges durable lesson → reviewed Skill is created/updated when warranted → later role context loads it → later operation changes.
- Boundary reachability: TEAM/SELF evolution is first-party runtime behavior invoked from the life supervisor; no downstream adaptation service is required.
- Why this is / is not agent-owned: runtime bounds evidence and timing, while a model makes the semantic adaptation choice and authors the retained procedure.
- Evidence: [`argus_skill/life/supervisor/_evolution.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/life/supervisor/_evolution.py); [`argus_skill/manager/skill_tidy.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/manager/skill_tidy.py); [`README.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: generic memory/in-mission replanning is not credited; the `A` claim relies on explicit post-settlement later-session-oriented model review.
- External distinction: settled work supplies distinctions about domain/project environment, effective techniques, failures and evidence limitations.
- Future / prospective distinction: the learning path asks what reusable procedure should improve later work rather than only repair the current mission.
- Adaptation option generated: create/update a scoped Manager/Planner/Engineer/Reviewer Skill or withhold an unsupported candidate.
- Path back into current capability / S3: admitted role Skills are loaded into later role context and therefore affect subsequent operational/current-control decisions.

## S5 — Policy and identity

- State: P
- Function: preserve operator-defined identity, red lines, standing purpose and reserved ultimate-policy decisions and return those choices into later Argus operation.
- Disturbance / variety regulated: identity/persona changes, standing-objective replacement, credentials/payment, irreversible actions, publication/external transmission and other questions autonomous roles are not legitimate to decide themselves.
- Decisive decision or feedback right: define/edit persistent operator identity and purpose and decide actions explicitly reserved for human authority.
- Decision owner: human operator as first-party parent authority.
- Supporting / enforcement mechanisms: persistent identity card, identity update surfaces, standing-objective lifecycle, Manager front door, durable parent controls and role contracts that stop at the authority boundary.
- Closure path: identity/ultimate-policy matter reaches the operator → authoritative choice persists in first-party identity/control state → later role context or standing objective is updated → subsequent Manager/Planner/Engineer/Reviewer operation follows it.
- Boundary reachability: identity, parent controls and standing-objective lifecycle ship with normal Argus operation.
- Why this is / is not agent-owned: Argus intentionally denies autonomous roles the legitimate right to rewrite operator-binding identity/red lines or self-authorize credentials, payment, irreversible actions or publication.
- Evidence: [`README.md`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/README.md); [`argus_skill/apps/_init_identity.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/apps/_init_identity.py); [`argus_skill/life/memory.py`](https://github.com/microsoft/ArgusAgent/blob/746f76b7a74a1217507c9ee348eecd3b782f7c92/argus_skill/life/memory.py).
- Basis: explicit + structural
- Confidence: high
- Caveats: ordinary task approvals/stage transitions are not S5. No autonomous S5 mode is credited or implied.
- Identity / ultimate-policy issue: who Argus is for this operator, its red lines/standing purpose and whether actions outside delegated authority may proceed.
- Ultimate authority in each claimed mode: parent mode only—the operator owns these rights.
- Return-to-operation path: operator edits persist and are returned into later model context/campaign state; later operation runs under the authoritative decision.

## Recursion

The assessed recursion is one persistent Argus Project. Ordinary Engineer missions and parallel Agent Team teammate missions are bounded operations inside that Project; teammate stage authority is deliberately suppressed so Project-level S3 remains with Manager. Multiple separate Argus Projects remain peer systems at the next potential recursion and are not needed for the S2 claim.

## Variety, escalation and closure

Argus attenuates operational variety through Manager intent routing, Planner mission bounding, Team path/dependency/ownership partitioning, Curator admission/claims, resource limits, safe tool boundaries and deterministic completion gates. It amplifies regulatory capacity through model-driven Manager current control, independent Reviewer challenge, parallel teammate operations, operator escalation and post-mission Skill evolution.

Exceptional paths close explicitly: Team blocked tasks retain the operator question and resume only after an answer; Reviewer `continue` returns defects to Engineer; `replan_requested` returns direction to Planner; `blocked` reaches the operator; Manager stage decisions update durable Project state; reviewed learning enters later role operation. The Team lead's coordination decisions feed directly into which S1 unit may execute which work next.

## Evidence gaps

No material unresolved evidence gap requires `?` at this pinned boundary. The same-ref correction changes only S2: the original assessment treated concurrent subagents as subordinate command workers and missed the separate shipped Agent Team surface, whose teammates are substantive Engineer→Reviewer missions with an explicit first-party coordination relation. S5 remains parent-owned by design and is not an assessment gap.