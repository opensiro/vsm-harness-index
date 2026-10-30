---
harness_id: dsh-flow
project_name: dsh-flow
repository: https://github.com/rootkiller6788/dsh-flow
review_ref: d11ad4f04400fda9c58cf2b9b5a11fa971818eed
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# dsh-flow

## Review boundary

- System in focus: one installed first-party `dsh-flow` plugin in a compatible DSH host, with one model-backed captain session and managed member sessions in the **selected `runner: subagents`** mode; optionally structured requirements/implementation/review/repair task types. The external DSH host supplies the underlying model and continuable subagent engine but the plugin mounts the team organization, task, feedback and quality circuits.
- Purpose and identity: turn a goal and named roster into a staged, reviewable task graph; dispatch member-agent work, preserve source-of-truth team state and ensure statuses, dependencies, mail, permissions and verification decisions stay consistent across host sessions and browser canvas.
- Relevant environment: operator/captain goal and plan, code/workspace files, running host model/tool sessions, teammate activity and messages, task dependencies, review findings, verification outputs and persistent team event/mailbox records.
- Standard-distribution boundary: `kernel.js` composition root; `src/runner/subagents.js` and `scheduler.js`; `src/runner/member-runtime.js` and host adapter; `src/tools/` captain/member tool surface; `src/rules/` gates, tasks, quality follow-up and completion; first-party store, mailbox, status/canvas. `manual` is considered as an explicit **non-executing** alternative, not credited as autonomous operation.
- Credited operating / distribution surfaces: default selected `subagents` runner with host continuable children; `/dsh-flow [--profile]` captain creation, model-selected staged plan and human approval; approved multi-member team dispatch; structured implementation/review/repair modes and their model-produced findings; task/mailbox/status and captain-driven interventions. The S3* claim is restricted to a configured **separate reviewer member** actually inspecting work, not every quality gate.
- Adjacent first-party surfaces excluded from ownership: web canvas is a view/control surface, not another autonomous agent; `scripts/diff-agent-teams.mjs` and rehearsal are development/comparison checks; read-only imported `.agent-teams` source is not a second owned execution engine. The comparison project `dsh-agent-teams`, host Cordis/DSH framework, model provider, filesystem, human and unrelated host agents remain externally owned.
- First-party operating / deployment modes considered: composition-time `subagents` vs `manual` runner; native and imported read-only team sources; seed vs captain task planning; staged review/approval; live member work and durable recovery; quality/coverage gates, separate review and bounded automatic repair follow-up. No claim that every profile selects all structured quality kinds.
- Recursion level: an approved team/goal as the system-in-focus; captain manages several operational member S1 cells and selected complementary reviewers. Individual member agents have their own task recursion, but their technical child status does not prove each has an independent S2–S5 metasystem.
- Reviewed revision: `rootkiller6788/dsh-flow@d11ad4f04400fda9c58cf2b9b5a11fa971818eed`; verified local `HEAD` exactly matches frozen commit, MIT license.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`installFlowKernel` chooses exactly **one** task runner at mount time. Default `subagents` creates a scheduler and host continuable child setup, binds the store and tools, and dispatches work when host status/explicit kicks arrive. `manual` preserves read/edit capability but does not execute autonomous members. This composition-time restriction prevents two schedulers from claiming the same team task; it is not a model deciding how to coordinate. [Kernel mount and runners](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/kernel.js#L1-L146), [subagent runner and quiescence](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/runner/subagents.js#L1-L149), [deployment mode](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/README.md#L287-L325).

The captain creates and shapes a staged team via `flow_create`/`flow_edit_plan`, then an allowed approval starts members and dispatch. The scheduler uses a unique member queue, team locks and deterministic rules: a member's unfinished attempt before fresh tasks, then its ready assigned tasks, then unowned tasks after dependencies complete. Assignment prompts include task IDs, source scopes, evidence contracts and predecessor outputs. Worker model decisions happen through **host-managed agent sessions**, but dsh-flow's first-party selected mode constructs their team relation, per-task identities and result/feedback paths. [Captain lifecycle tools](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/tools/lifecycle.js#L22-L174), [scheduler arbitration](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/runner/scheduler.js#L18-L175), [assignment and dependency results](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/rules/assignment.js#L20-L189).

`flow_send_message` persists a member/captain message and attempts live delivery; a captain sees incoming member progress in its next model step, while `flow_status` shows the full team graph, member state, task/attempt/outcome, mailboxes and quality coverage. The captain can direct new work, reassign/interrupt, halt/resume and address failures, subject to deterministic authorization/attempt gates. The model's semantic corrective choice is distinct from runtime event persistence and lock enforcement. [Message and live captain delivery](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/tools/comms.js#L1-L131), [captain status and evidence](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/tools/comms.js#L153-L261), [task reassign and handoff](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/tools/tasks.js).

For structured work, first-party rules reject simultaneous live **overlapping writer scopes**, block on unfinished dependencies, require per-attempt capability and acceptance/verify evidence, and prevent success declarations with unresolved high findings. A separate model-backed review member can inspect a completed implementation and issue a verdict and file/line-specific findings. On `needs_revision`, the rule engine creates repair and next-round review tasks, selecting a reviewer different from the repair implementer; round/attempt ceilings escalate to the parent. These are distinguishable S2 collision prevention, S3/quality enforcement support and selected S3* complementary model judgment rather than one undifferentiated `quality` feature. [Writer collision gate](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/rules/gates.js#L100-L153), [completion truth conditions](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/rules/completion.js#L1-L143), [review/repair follow-up](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/rules/followup.js#L48-L175).

## Operational model

The DSH host retains the underlying model/tool execution loop for each member and captain, while this installed plugin provides **first-party owned team wiring**: team-specific continuable children, model-facing tools, durable assignment and feedback, source-of-truth state and restricted task identities. The captain model can choose work decomposition and revise current team commitments; member models locally choose task steps. Pure-core overlap and quality rules enforce safe states but are not model judgments. In manual runner mode nothing runs autonomously, so all positive states refer to the supported active subagents mode (and S3* additionally requires separate structured review).

## S1 — Operations

- State: A
- Function: perform user-goal work in the actual project environment through multiple scoped member model-agent sessions; captain may also carry a bounded task, but its principal credited role here is team control.
- Disturbance / variety regulated: varying implementation/research/verifier tasks, changing file/tool outputs, failed commands, partial results and review findings.
- Decisive decision or feedback right: selected member model chooses tool/actions and reports task outcome within the assigned contract; the host supplies the model/tool engine, the plugin supplies live delegation, scoped task/attempt identity and return to team.
- Decision owner: the operating captain/member model sessions, instantiated as DSH host continuable agents for this plugin's selected team; deterministic scheduler, rules and adapter do not choose the semantic work solution.
- Supporting / enforcement mechanisms: `createSubagentsRunner`, host continuable child API, model route inheritance, task claims/attempt capability, assigned dependency results, inbox, state logs and completion evidence gate.
- Closure path: approved team → scheduler dispatches ready task to member session → model acts in workspace → `flow_update_task` and message return structured evidence → team state/captain observes → next work or review task. The host executes individual tools; first-party dsh-flow installs the closed team feedback relation.
- Boundary reachability: `runner: subagents` is the default mount and `/dsh-flow` plus `flow_approve` initiate actual member execution, with tests exercising scheduler/host adapters. Manual mode is expressly non-executing.
- Why this is / is not agent-owned: without the member's model decision there is no task-specific implementation/verification result; locks, dispatch and signatures alone would only manage empty work tickets.
- Evidence: [subagents runner mounting host agent](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/runner/subagents.js#L28-L112), [scheduler claim/dispatch](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/runner/scheduler.js#L103-L230), [assignment prompt/tool output](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/rules/assignment.js#L139-L189), [supported team command](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/README.md#L275-L283).
- Basis: structural, supported by fake-host scheduler/subagent tests.
- Confidence: high for first-party team wiring, medium-high for external host runtime reachability without a live DSH model session.
- Caveats: host/model provider remains separate; a pure `runner: manual` installation has no active S1, and an imported `.agent-teams` record is read-only visualization rather than new execution.

## S2 — Coordination

- State: C
- Function: attenuate destructive interference among multiple member S1 cells attempting incompatible writes or dependent work during a shared team goal.
- Disturbance / variety regulated: file write collision, duplicate task claiming, unfinished attempt interleaving and premature dependent dispatch between separately operating team members.
- Distinct S1 units: independently operating, named member model sessions with separate task/attempt identities and potentially competing paths in one workspace.
- Inter-S1 disturbance: two independently acting implementation/repair members may claim overlapping workspace paths and overwrite each other's output; two task claims can also invalidate one member's existing attempt.
- Specific interference / oscillation: concurrently open implementation/repair tasks can declare overlapping `inScope` paths and corrupt/overwrite each other's work; duplicate task claims or a member taking a second task before finishing its first can interleave commitments and lose the correct attempt.
- Attenuating coordination relation: the shared first-party task graph refuses overlapping live writer scopes, withholds dependent tasks, and serializes member claims with identity-bound attempts.
- Coordination response: `validateCreateTask` rejects overlapping scopes and explains `serialize these tasks or split the paths`; dependency readiness blocks downstream work until predecessor success; `createMemberQueues` and task locks ensure one active claim per member/attempt. Reassignment revalidates handoff after interruption.
- Decisive decision or feedback right: first-party **deterministic rules** decide that an incompatible graph/task claim is inadmissible; captain/member may then revise work scopes or dependencies after the error, but the enforced anti-collision verdict is constructor-owned, so the state is `C` rather than `A`.
- Decision owner: shipped rule constructors `gates.js`/`assignment.js` plus scheduler serialization for the S2 verdict; model captain remains owner of a revised *plan*, not of the invariant.
- Supporting / enforcement mechanisms: scope-overlap matcher, team lock, member serial queue, dependency graph, attempt ID/capability, delivery state and error response.
- Closure path: proposed overlapping tasks/competing claim → deterministic rejection or blocked readiness → visible tool error/status to captain and members → corrected serial/decomposed plan or later ready dispatch; later task work respects the new non-overlapping graph. This is a concrete interference/attenuation path, not generic messaging.
- Feedback into subsequent S1 behaviour: the captain receives the explicit scope-conflict error and must split/serialize the plan; after a dependency finishes, the scheduler makes only newly eligible nonconflicting work available to the next member turn.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: a concrete overlapping-writer interference is recognized and prevented at the team boundary, with refusal and corrected task eligibility affecting what distinct S1 cells can actually do next.
- Boundary reachability: gates and claim selection are invoked by normal `flow_create_task`/`flow_update_task` and default subagents scheduler, not only a test fixture.
- Why this is / is not agent-owned: removing the model from the overlap test leaves the same deterministic reject/serialized admission decision; model-generated alternatives support adaptation but the decisive S2 collision protection is constructed in code.
- Evidence: [live overlapping writers refused](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/rules/gates.js#L117-L151), [dependency/owned-task selection](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/rules/assignment.js#L20-L44), [per-member double-claim lock](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/runner/scheduler.js#L22-L58), [task reassignment locking](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/tools/tasks.js#L1-L18).
- Basis: explicit code-level invariant and structural execution path.
- Confidence: high for deterministic protection; not a measurement of all real-world file races.
- Caveats: scopes rely on accurate captain/model-declared paths; unmodeled side effects and external writers remain outside these protections. A blocked task requires legitimate correction; the gate alone does not invent the right new plan.

## S3 — Inside-and-now control

- State: A
- Function: let a team captain regulate the **whole currently operating group**—member commitments, task ownership, progression, failures and interventions—while members absorb local implementation variety.
- Whole-system current view: `flow_status` supplies all active team members, their live activity, all task assignments/dependencies/attempts/outputs, captain mail and quality/coverage state to the captain's model context.
- Current-control decision scope: captain model chooses new/reassigned current member commitments, can halt or resume this team, send corrective instructions and change the task graph based on the complete status/failure feedback.
- Disturbance / variety regulated: concurrent or stuck members, stale attempts, work failures, dependency bottlenecks, incomplete coverage, quality escalation and changing current priorities within an approved goal.
- Decisive decision or feedback right: captain model can see all members/task statuses/mailboxes and choose current task creation, assignment/reassignment, messages, halt/resume and follow-up based on returned work. Human approval of the initial staged plan is a bounded launch right, not automatically a distinct S3 parent mode.
- Decision owner: the model-backed **captain session** for semantic whole-team current interventions; deterministic scheduler selects ready tasks and enforces locks/attempt identity; operator chooses profile/approval policy and is the final deployment authority.
- Supporting / enforcement mechanisms: `flow_status` whole-team view, per-member `flow_send_message`, `flow_reassign_task` with interrupt, `flow_create_task`, `flow_halt`/`flow_resume`, membership controls, state/coverage diagnostics, event-driven scheduler and mailboxes.
- Closure path: member progress/failure → persisted task state and captain-directed message (live steer or mailbox) → captain sees all task commitments and evidence in `flow_status` → model chooses intervention/reassignment/repair/stop → gated tool writes state and scheduler dispatches changed work → subsequent member outcomes return again.
- Boundary reachability: selected default subagents mode creates an actual captain-owned team, dispatches members and registers captain-facing tools; live message steering and durable fallback make the feedback available in normal supported operation.
- Why this is / is not agent-owned: scheduler/quality gates can enforce the captain's selected commitments, but cannot decide whether to change a goal-constrained priority, replace an implementer or ask for revised evidence. That discretionary current-control choice resides in the captain model when operated as a team.
- Evidence: [captain-only lifecycle tools](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/tools/lifecycle.js#L1-L174), [whole-team status](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/tools/comms.js#L152-L262), [live member→captain steer](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/tools/comms.js#L25-L124), [task ownership/interrupt and reassignment](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/tools/tasks.js), [scheduler feedback](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/runner/scheduler.js#L70-L175).
- Basis: structural supported-mode control loop, with explicit tool rights and return path.
- Confidence: medium-high for model-visible group view/control; no live provider captain intervention was measured.
- Caveats: a pure manual runner is an operator editing a static plan, not autonomous S3. A single all-in-one worker task cannot be promoted to a whole-team S3 merely because a captain persona exists.

## S3* — Complementary audit

- State: A
- Function: obtain a separate reviewer model's judgment on implementation/repair claims using task files, acceptance evidence and changed paths, and route findings back to corrective control.
- Disturbance / variety regulated: divergence between an implementer's completion assertion and raw code/test artifacts, including unresolved severe findings and incorrect acceptance or changed-path claims.
- Claim being audited: an implementation or repair member's reported completion, scope compliance, tested behavior and asserted acceptance against the actual delivered artifacts.
- Ordinary reporting path: implementer `flow_update_task` status/output/changedPaths/acceptanceResults/commandsRun plus ordinary member message to the captain.
- Complementary access path: a **separately assigned review member** receives a structured `kind: review` task with `reviewedTaskId`, independent prompt/work and access to code/verification artifacts under host task tools, then returns its own verdict and structured findings with concrete required fixes.
- Independence boundary: in the selected structured quality mode, the reviewer is a different member model session from the implementer; automatic follow-up deliberately chooses a reviewer other than the repair implementer. This is task-relative independence, not an external security audit.
- Decisive decision or feedback right: reviewer model inspects evidence and makes `pass`, `needs_revision` or `reject` judgment; pure rules validate the result shape and plan bounded repairs, while captain/user can act on escalations.
- Decision owner: independent reviewer member model for the substantive audit judgment; constructor-owned `evaluateQualityCompletion` and `planQualityFollowUp` enforce nonfabrication of completion and deterministic follow-up limits; human/captain control task policies.
- Supporting / enforcement mechanisms: structured review task kind/objective/acceptance, required verdict/findings with `problem`/`requiredFix`/optional `file`/`line`, task-specific claim and role permissions, changed-path/verification gates, repair/review round counters and team status/canvas.
- Closure path: implementer output + actual code/evidence → separately executed reviewer task → model verdict with findings → `flow_update_task` rejects unsupported pass or accepts failure → `planQualityFollowUp` creates scoped repair and fresh independent review (or escalates) → member performs repair and reviewer rechecks → captain sees updated current quality state.
- Boundary reachability: standard `flow_create_task` accepts `review` tasks, default active subagents runner dispatches them as ordinary member work, `flow_update_task` carries verdict/findings and the first-party follow-up rule selects a distinct reviewer. This is selectable first-party functionality, not a standalone benchmark evaluator.
- Why this is / is not agent-owned: the evidence comparison and diagnosis is model-owned by a distinct reviewer, not produced solely by the implementer or a deterministic unit test. The shape validator and automatic repair planner do not confer audit judgment ownership.
- Who acts on findings: an implementation member performs planned repair; another reviewer performs the new review; captain receives status/escalation and can reallocate current work or ask the user when limits are reached.
- Evidence: [review-task schema and real dispatch](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/tools/tasks.js#L128-L156), [review evidence parsing](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/tools/tasks.js#L36-L111), [completion review verdict checks](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/rules/completion.js#L58-L110), [separate reviewer and repair round](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/rules/followup.js#L103-L173), [review assignment prompt](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/rules/assignment.js#L139-L189).
- Basis: structurally evidenced selected-mode audit with model-authored reviewer verdict; not inferred from generic QA label.
- Confidence: medium-high for path/role separation, medium for observed real-artifact review quality without live provider.
- Caveats: the captain/profile must actually create/assign a separate reviewer task; ordinary `work` has no mandatory review. The initial schema does not universally forbid a captain from assigning an ordinary review to the same implementer, so S3*=A refers to a **distinct reviewer** mode and explicit automatic follow-up separation, not every team or task.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped whole-team, externally and prospectively oriented agent loop constructs future adaptation options and closes them against current S3 capacity.
- Disturbance / variety regulated: current task progress, plan defects, implementation/test failures, member availability, required scope changes and review follow-ups; these are present goal/work controls.
- Decisive decision or feedback right: captain model revises the current staged or active task plan; human/deployment author configures roles/profiles and decides whether the team should pursue a new goal.
- Decision owner: captain for current work, operator/higher organization for long-horizon goals and profile evolution; no first-party future-environment intelligence owner found.
- Supporting / enforcement mechanisms: profile registry, plan requirements, goal coverage, task DAG, status/coverage matrix, review findings and imported team sources.
- Closure path: task failure/review updates current repair or work; no separate external trend/opportunity sensing → modeled alternatives → S3–S4 dialogue → changed long-term capability path is shipped.
- Why this is / is not agent-owned: current-task planning and immediate code repair are not S4 even when model-driven; roster/configurability is not strategic external adaptation.
- Evidence: [profile/task-planning modes](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/README.md#L317-L329), [bounded repair follow-up](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/rules/followup.js#L89-L174), [captain tool boundary](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/tools/lifecycle.js#L1-L174).
- Basis: structural negative.
- Confidence: medium-high across reviewed supported modes.
- Caveats: the plugin can host a research task about future technologies, but a one-off task is an S1 operation until a governed prospective capability-change loop is evidenced.

### Absence scope

- Surfaces inspected: captain planning and edit/approve, profiles, task dependency/coverage, quality repair loop, native/imported sources and configured runner modes.
- Plausible first-party paths checked: captain-authored new plans, requirements work, long-running tasks, manual profile edits, review-driven repair and cross-team source migration.
- Why no material first-party path remains: all evidenced decisions remain task/goal-local or host-operator configured; no autonomous external/future model closes a strategic S4 conversation into current S3 resource policy.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy deliberation and returned governance path is established for the deployed team as an ongoing viable organization.
- Disturbance / variety regulated: team membership, task ownership, profile review rules, host permissions, approval of staged plan and risk/quality limits are ordinary task controls.
- Decisive decision or feedback right: human operator/deployment author chooses goals/profiles and approves a staged plan; captain model edits a plan within those granted rights; host identity/permission checks protect sessions.
- Decision owner: human/external DSH host for ultimate organizational identity and policy; kernel enforces profiles, team session role and task capability. No explicit first-party S5 judgment at an ultimate identity tension is evidenced.
- Supporting / enforcement mechanisms: `flow_approve` staging gate, captain/member access restrictions, persisted identity/team IDs, member retirement guard, review policy, scope and acceptance constraints.
- Closure path: approved plan activates new member work and constraints, but that is normal task launch/current-control authorization, not a distinct identity-level issue routed to legitimate parent S5 and returned as ultimate policy.
- Why this is / is not agent-owned: human approval of an ordinary plan and profile YAML do not automatically become parent-governed S5; a captain role label is not ultimate authority.
- Evidence: [staged approval and tool rights](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/tools/lifecycle.js#L1-L177), [captain/member tool distinction](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/rules/tool-names.js), [retired member guard](https://github.com/rootkiller6788/dsh-flow/blob/d11ad4f04400fda9c58cf2b9b5a11fa971818eed/src/runner/retired-guard.js).
- Basis: structural negative.
- Confidence: medium-high.
- Caveats: a human organization using the plugin may provide real higher-recursion governance, but the plugin's task approval alone does not demonstrate the required S5 function.

### Absence scope

- Surfaces inspected: deployment profile/identity, captain/member role enforcement, plan approval, member retirement, task safety/quality policies and exceptional escalation.
- Plausible first-party paths checked: human staged approval, captain goal authority, role retirement and model-route settings, quality escalation to user, manual runner configuration.
- Why no material first-party path remains: none identifies and resolves an actual ultimate identity/policy tension with a corresponding governance decision returning into the autonomous team; normal safety/launch controls are lower-level.

## Recursion

The team as a whole contains operational member agents whose task discretion comes from host-managed model sessions. The plugin owns the **team relation** (captain rights, roster, task graph, collision gates, mailbox, quality and current-control feedback), not the model-provider or host's internal execution algorithms. Each member can be treated as an S1 at the team's recursion; the fact that some are children of a host session does not by itself make them viable nested systems. `runner: manual` and imported read-only teams do not instantiate these positive autonomous modes. Complementary reviewer mode is genuine only when a separate reviewer member executes.

## Variety and escalation

- Local absorption: member models solve scoped work, interpret tool/results, verify and submit structured completion; captain model decomposes a goal and decides current cross-team interventions.
- S2 attenuation: explicit writer-scope anti-collision, dependency gates, team/member locks, attempt IDs and task ownership; these are constructor-owned decisions with visible errors requiring corrections.
- S3 amplification/current control: whole-team status/coverage, live member→captain messages, captain tool rights, reassign/interrupt/halt and updated task graph.
- S3* complementary channel: separately assigned model reviewer inspecting delivered artifacts, required evidence/findings, bounded repair/review loop and escalation to captain/user.
- Algedonic/exceptional information: task `failed`/`escalated`, malformed-log diagnostics and review ceilings are visible signals; their existence does not separately prove S4/S5 or an identity-level algedonic response.
- Operational bounds: event-driven scheduler has no always-on polling/boot recovery scan; failure of a host member may be recovered on an idle edge/kick. This constrains deployment responsiveness and is not a VSM viability certification.

## Evidence gaps

- Frozen first-party SHA and MIT license verified. No live DSH host session, paid model/provider, real multi-member workspace task or third-party imported team state was executed; classification is source-first structural, not measured task performance.
- Native deterministic checks: `npm run build` passed (107 modules parse, 66 modules/7 layer boundaries valid, canvas allowlist). `npm test` passed **32/32** Node test files/suites; these use fake host/store interfaces and do not establish provider results.
- S1/S3 ownership depends on the selected `runner: subagents` mode and a compatible DSH host supplying continuable agent/model tool mechanics; static `manual` mode is not credited.
- S2's `C` covers declared path scopes and task/attempt ownership. Real unreported filesystem side effects or external writers may still conflict, and agents must provide correct `inScope` declarations.
- S3*'s `A` covers actual separate model review with access to task artifacts; the source does not guarantee every team/profile assigns a separate reviewer, nor universal reviewer independence. The selected mode's code path and bounded repair return are evidenced, but no live audit efficacy was measured.
- No material unresolved shipped S4/S5 loop was identified within the reviewed standard distribution, so bounded `—` is used instead of hypothetical `?`.
