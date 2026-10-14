---
harness_id: bareagent
project_name: BareAgent
repository: https://github.com/525300887039/BareAgent
review_ref: 1dfd1057d372e872f54c0a666f375dce2bc11a26
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# BareAgent

## Review boundary

- System in focus: installed BareAgent Python coding REPL/runtime, including the native model/tool loop, connected autonomous team subsystem, shared task manager, permission controls, and supported first-party team and workflow tools.
- Purpose and identity: respond to developer work requests, inspect/edit/test code autonomously within permissions, and optionally manage several persistent cooperating coding teammates executing messages or independently claiming shared ready tasks.
- Relevant environment: local repository/filesystem and shell, model-provider credentials, per-workspace task/teammate/mailbox files, human terminal, project instructions, skill directories, and optional tools/MCP/LSP.
- Standard-distribution boundary: `src/bareagent/main.py` composition through regular REPL, built-in `core/tools.py` team/task schemas and handlers, `core/loop.py`, `team/*`, `planning/tasks.py`, built-in workflow and permission/compaction. Not arbitrary user-launched agent fleets.
- Credited operating / distribution surfaces: [README](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/README.md); [REPL composition and handlers](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/main.py); [agent_loop](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/core/loop.py); [team/task tool schemas](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/core/tools.py); [AutonomousAgent](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/team/autonomous.py); [MessageBus](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/team/mailbox.py); [ProtocolFSM](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/team/protocols.py); [TeammateManager](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/team/manager.py); [TaskManager](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/planning/tasks.py); [subagent execution](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/planning/subagent.py); [workflow DAG](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/core/workflow.py); [skill generation](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/planning/skill_gen.py); [team mode documentation](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/docs/guide/ch10-team.md).
- Adjacent first-party surfaces excluded from ownership: `.trellis/` local contributor/development orchestration, archived implementation/research worklogs, GitHub CI/release workflows, static documentation examples, independently deployed external orchestrators, and user-authored policy/skills not shipped as deciding organizational actors.
- First-party operating / deployment modes considered: ordinary interactive solo coding agent; standard first-party `team_register`→`team_spawn`→autonomous background teammates and mailbox/task dispatch; root model using built-in team/task tools; parent human using `/team` and `/task` commands; optional static DAG workflow; reflected draft skills requiring human promotion.
- Recursion level: active root coding session plus first-party background teammate population in that session/workspace. The persistent teammates are distinct operational S1 units; a single tool call or static workflow node need not be a distinct autonomous organization. No other institutional recursion is assumed.
- Reviewed revision: `1dfd1057d372e872f54c0a666f375dce2bc11a26`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[main.py](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/main.py) composes a provider, local coding tools, `TaskManager`, `TeammateManager`, per-session `MessageBus`, background execution pool and a root interactive agent. Built-in [TEAM_TOOL_SCHEMAS](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/core/tools.py) expose `team_list`, `team_register`, `team_spawn`, `team_send`, `team_shutdown`, and `team_request_review` as model-callable tools; `task_create`, `task_list`, `task_get`, and `task_update` expose current task commitments. The user can also invoke first-party `/team` commands. [agent_loop](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/core/loop.py) collects model-selected tool calls, checks permissions/hooks, executes the corresponding native handlers, and returns observations into model history.

[_make_team_handlers](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/main.py) binds the tool names to real running-session actions. `team_spawn` constructs a fresh provider-backed `AutonomousAgent` via [TeammateManager](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/team/manager.py) and runs it through the background manager; `team_list` reports registrations plus actual running thread status; `team_send` and `team_request_review` send messages to teammates, await responses, and relay the result into the root model/console. [AutonomousAgent.run](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/team/autonomous.py) prioritizes mailbox requests, then queries the shared ready task queue and uses an atomic expected-`pending` claim before executing work. The shared [TaskManager.update](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/planning/tasks.py) holds a lock, compares the expected status and rejects a conflicting claim; a losing teammate tries other work rather than executing the same claimed task. [ProtocolFSM](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/team/protocols.py) transports plan-approval and shutdown requests; plan review is a specialized model prompt but does not automatically require independent operational-artifact sampling.

The optional [workflow DAG](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/core/workflow.py) schedules layers of independent subagent nodes with completion/failure propagation. [SkillGenerator](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/planning/skill_gen.py) may trigger a second model to draft or refine reusable skills after sufficient task activity; [/skill promotion path](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/main.py) requires the human to promote a pending draft. These are relevant but not, by themselves, independent future-environment modeling.

## Operational model

The root coding agent controls tool selection during a local developer task. In team mode it also obtains a live teammate roster and current task status, can register/start/stop a teammate or change work assignments, and receives subordinate work responses. Background teammates autonomously execute incoming messages and claim ready tasks without a root tool call for every step. The native lock/CAS path protects a specific shared task against competing S1 claimants; it is not itself an agent choosing organizational coordination policy. A separate human/operator command surface can exercise current-control judgments over the same first-party roster. This is an alternative supported parent mode rather than simultaneous joint ownership.

## S1 — Operations

- Function: Autonomously perform uncertain developer coding tasks through file/shell/tool actions and observed feedback.
- Disturbance / variety regulated: Unknown repository state, errors, test failures, unavailable resources, and follow-up developer questions.
- Decisive decision or feedback right: Root model or each teammate model chooses which action to execute and how to respond to the returned result.
- State: A
- Decision owner: First-party model-driven root/teammate agent loops; the provider supplies inference while the built-in runtime carries out local actions.
- Supporting / enforcement mechanisms: Typed tool schemas/handlers, hooks/permissions, retry policy, message persistence/compaction, shell and file tools, background execution.
- Closure path: Work request → model-selected action → tool/handler result → model feedback in the same coding loop → next action or final result; background teammate handles a message or claimed task using the same loop.
- Boundary reachability: Default REPL invokes native agent_loop; the documented /team spawn path creates independent running AutonomousAgent workers that invoke agent_loop.
- Why this is / is not agent-owned: Tool execution and permissions do not pick a context-appropriate coding action without the operative model.
- Evidence: [core/loop.py](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/core/loop.py); [main.py](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/main.py); [autonomous.py](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/team/autonomous.py); [tools.py](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/core/tools.py).
- Basis: explicit and structural
- Confidence: high for source-level loop reachability; no paid-provider end-to-end evaluation executed
- Caveats: human permission gates and provider/network availability bound realized operations.

## S2 — Coordination

- Function: Attenuate duplicate execution of one shared pending task when several autonomous teammate S1 workers see the same ready item.
- Disturbance / variety regulated: Two independently running teammates can concurrently select the same pending task before either finishes; duplicate claims/work would waste work or conflict on the same task commitment.
- Decisive decision or feedback right: The shared task manager compares a task's expected status against current status and atomically commits the first claim; a rejected claimant re-evaluates the ready set rather than executing that task.
- State: C
- Decision owner: First-party deterministic claim-and-retry constraint; a developer/agent must still supply any discretionary policy for arbitration or rescheduling beyond first-winner conflict attenuation. No S2 coordinating agent owns adaptive arbitration as shipped.
- Supporting / enforcement mechanisms: TaskManager RLock, expected_status compare-and-update, persisted .tasks.json, dependency readiness, per-teammate run loops.
- Closure path: Concurrent ready-task observation → first atomic pending→in_progress update → competing update raises ValueError → second teammate skips the lost claim and searches other ready tasks instead.
- Boundary reachability: TaskManager instance is shared by the main REPL and spawned AutonomousAgent workers through _make_team_handlers; workers invoke _claim_task for ready work.
- Why this is / is not agent-owned: The collision-sensitive response is embedded in explicit first-party code but chosen by lock/CAS rules, not by a model's independent coordination judgment, so it supports C, not A.
- Distinct S1 units: Separately spawned AutonomousAgent background threads, each with its own provider, prompt, handler set, and task execution loop.
- Inter-S1 disturbance: Competing acquisition of the same ready persisted task by two running teammate agents.
- Attenuating coordination relation: Compare-and-set claim on shared task status and losing-claim rejection within the worker claim loop.
- Feedback into subsequent S1 behaviour: Losing worker does not execute a task it failed to claim; it resumes scan or waits, while winning worker marks done/failed on completion.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: This path rejects a concrete competing claim by two operating workers and changes which worker may proceed; the generic message bus, team routing and static workflow DAG are not used as independent S2 evidence.
- Evidence: [tasks.py update/get_ready_tasks](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/planning/tasks.py); [AutonomousAgent claim loop](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/team/autonomous.py); [shared TaskManager wiring](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/main.py).
- Basis: structural
- Confidence: medium-high for specific duplicate-task attenuation; no adaptive general conflict arbitration inferred
- Caveats: This narrow coordination is not a general edit collision protocol, resource negotiator, or proof of agent-directed S2.

## S3 — Inside-and-now control

- Function: Own whole-current commitments and interventions for a live team of independently executing coding S1s.
- Disturbance / variety regulated: Multiple running teammate commitments, pending/done/failed tasks and developer requests can require reassignment, roster adjustment, work reprioritization, shutdown, or additional work.
- Decisive decision or feedback right: In agent mode the root model may inspect task and team rosters, create/update tasks, register/spawn/shutdown workers, and send targeted work requests based on responses. In separate parent mode the human does equivalent current intervention via /team and task command surfaces.
- State: A(P)
- Decision owner: Autonomous root model in first-party agent-tool mode; human operator for the separately exposed command-controlled parent mode. Background manager and TaskManager transport/enforce these decisions but do not autonomously choose current priorities.
- Supporting / enforcement mechanisms: team_list, team_register, team_spawn, team_send, team_shutdown; task_list/task_create/task_update; per-session MessageBus and background worker state; running-thread probe; reply-to-request protocol.
- Closure path: Root agent sees whole-team roster/task status and teammate results → chooses new current allocation or intervention → concrete team/task tool action → updated task commitments, active teammate population, or returned worker instruction → subsequent worker execution/feedback.
- Boundary reachability: Team and task tool schemas are standard first-party tools registered through core/tools.py and connected by _build_handlers/_make_team_handlers in main.py. /team commands address the same handlers.
- Why this is / is not agent-owned: The root model can decide when to change team composition, who handles a request, or which commitments to create. A deterministic scheduler only enforces claims; a human alternative exists without removing autonomous tool-mode choice.
- Whole-system current view: team_list returns all registered workers with actual running status; task_list returns current work records and statuses; team_send and mailbox responses provide subordinate results.
- Current-control decision scope: Create/change a task commitment, launch/stop a worker, and send/revise an operational request across a whole current team; this is not solely selecting a single child function call.
- Evidence: [TEAM_TOOL_SCHEMAS and task tools](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/core/tools.py); [team handlers and /team commands](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/main.py); [worker task behavior](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/team/autonomous.py); [task ledger](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/planning/tasks.py).
- Basis: explicit and structural
- Confidence: medium: meaningful current-control reachability is clear; a live multi-worker strategy adaptation trace has not been independently reproduced
- Caveats: Default solo mode is only one S1 and does not exercise a team-level S3. Positive S3 is credited to the documented first-party team mode, not the bare presence of a queue or generic model planning.


### S3 ownership mode matrix

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Root model managing multiple running autonomous teammate S1 workers | team_list and task_list status, worker responses, current staffing/task needs | Model selects team_spawn/team_send/team_shutdown or changes tasks; handlers update team commitments and the following worker execution | [team/task tools](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/core/tools.py), [live handlers](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/main.py) |
| Parent (`P`) | Human REPL operator | /team list and task inspection plus explicit change of active team obligations | Operator chooses send/spawn/shutdown/task change; standard first-party handlers change subsequent background worker execution | [REPL /team operator mode](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/main.py) |

The alternative modes do not claim simultaneous dual ownership. This S3 mapping applies to the shipped multi-teammate operating mode rather than standalone solo operation.

## S3* — Complementary audit

- Function: No operationally guaranteed complementary independent audit of claims about teammate execution with a return to whole-current control was established.
- Disturbance / variety regulated: A teammate may produce faulty work or a weak plan; ordinary team_request_review solicits a model's opinion on the plan, not a verified independent observation of what the worker actually did.
- Decisive decision or feedback right: The root model or human requests a review; a nominated teammate writes an answer. The standard PLAN_APPROVAL path does not require sampled operational artifacts or separate protected evidence before an audit verdict is returned.
- State: —
- Decision owner: Requested reviewer model for plan opinion and the requester for next action; no distinct source-first operational audit authority guaranteed by shipped contract.
- Supporting / enforcement mechanisms: ProtocolFSM PLAN_APPROVAL request/response, separate provider-backed teammate, shared read-capable tools, per-request prompt wrapper, optional tests and traces.
- Closure path: Requester-supplied plan → teammate review prompt → textual verdict → requester. Missing guaranteed independent operational evidence → audit judgment → whole-current management correction circuit.
- Why this is / is not agent-owned: An independent worker identity alone is not sufficient for S3*; normal plan approval does not establish sufficiently complementary access to operational reality.
- Evidence: [_team_request_review](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/main.py); [_build_incoming_prompt](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/team/autonomous.py); [plan approval protocol](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/team/protocols.py); [team docs](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/docs/guide/ch10-team.md).
- Basis: structural
- Confidence: medium-high within standard deployment; custom reviewers may use additional tools but are not automatically independent audits
- Caveats: User-composed reviewer with explicit independent sampling might establish S3* in a new mode, but the task-specific contract and closure would need separate evidence.

### Absence scope

- Surfaces inspected: Team review tool and protocol, reviewer prompt, teammate isolation, ordinary tests/traces and background result path.
- Plausible first-party paths checked: Direct inspection of produced artifacts, independent evidence sampling rather than plan self-report, independent evaluator decision, mandatory return to current team controller.
- Why no material first-party path remains: Shipped approval path receives a proposer-supplied plan and permits a generic reply without a demanded independently sampled audit witness or audit-driven corrective decision.

## S4 — Outside-and-then intelligence

- Function: No first-party external-and-prospective option-modeling function with feedback into whole-current capability is established.
- Disturbance / variety regulated: Changing project knowledge, user demands or reusable workflows may affect future work, but first-party skill reflection captures previous local actions and user-promoted drafts rather than prospectively modeling external change.
- Decisive decision or feedback right: Reflection model may propose a reusable skill; the human decides whether to promote; neither step demonstrates a distinct outside/future intelligence decision coupled to S3 current control.
- State: —
- Decision owner: Current coding model for task learning/drafts, operator for promotion; no attributable S4 owner.
- Supporting / enforcement mechanisms: SkillGenerator two-threshold trigger, isolated reflection model run, pending skill store, /skill keep promotion, model/provider configuration.
- Closure path: Accumulated local work → LLM reflects and drafts skill → human promotes into later skill catalog. Missing independent externally sensed change, prospective option appraisal, and return into current team strategy.
- Why this is / is not agent-owned: Generic experiential learning or reusable procedures do not satisfy the Profile's external-and-future condition by themselves.
- Evidence: [skill_gen.py](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/planning/skill_gen.py); [_run_skill_reflection and promotion](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/main.py); [skill catalog](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/planning/skills.py).
- Basis: structural
- Confidence: medium-high at pinned product revision
- Caveats: Skill self-evolution is genuine task learning, but must not be conflated with VSM S4.

### Absence scope

- Surfaces inspected: Skill draft/promotion, provider selection, workflow planning, memory, external web tools and config.
- Plausible first-party paths checked: Explicit scan of changing environment, future adaptation alternatives, prospective selection, S4→S3 implementation feedback.
- Why no material first-party path remains: No integrated external-prospective distinction and adaptation-decision return is shown in reviewed standard operation.

## S5 — Policy and identity

- Function: No first-party ultimate organizational identity/constitutional policy arbitration loop is evidenced at the live coding team recursion.
- Disturbance / variety regulated: Permission limits, developer config, workspace rules and team role descriptions constrain actions but do not resolve ultimate purpose/policy conflicts for the team organization.
- Decisive decision or feedback right: Human config sets security permissions/roles; root agent may define teammate work roles. Neither is a proven ultimate identity-policy authority with return to the operating whole.
- State: —
- Decision owner: Human for local permissions and safety preferences; deterministic enforcement for tool operations.
- Supporting / enforcement mechanisms: PermissionGuard, team role/system-prompt registry, sandbox, approval hooks, config and fail-closed child permissions.
- Closure path: User sets local constraint → permission or role handler applies it to a tool/worker. No S3–S4 identity conflict → legitimate ultimate authority → binding policy decision → whole-team return path.
- Why this is / is not agent-owned: Task permissions, system prompts and teammate role selection remain execution governance, not proof of constitutive identity decisions.
- Evidence: [permissions](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/permission/guard.py); [teammate roles](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/team/manager.py); [team composition](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/main.py); [hooks](https://github.com/525300887039/BareAgent/blob/1dfd1057d372e872f54c0a666f375dce2bc11a26/src/bareagent/hooks/engine.py).
- Basis: structural
- Confidence: medium-high
- Caveats: Maintainer policies and external institution/enterprise governance are outside the first-party running session.

### Absence scope

- Surfaces inspected: Tool authorization, role configuration, config hierarchy, user command controls, contributor governance outside runtime.
- Plausible first-party paths checked: Ultimate-policy disputes, legitimate S5 choice, and specific identity-level return into the operating team.
- Why no material first-party path remains: Available rights govern tools and teammate execution; no operational constitutional policy/identity adjudication path is supplied.
## Recursion

A root agent with concurrently running background teammates is a first-party team organization. Workers are autonomous S1s at the declared recursion; within a delegated worker, local tool execution is an operative loop at a lower task recursion. TaskManager collision regulation and root team controls are mapped at the multi-teammate organization boundary, not inflated from isolated tools. The repo's `.trellis` contributor planning infrastructure is a different development context and is not counted as runtime management.

## Variety and escalation

Ordinary tool feedback returns to the acting S1. A duplicate task claim fails atomically and causes the competing teammate to seek other work, demonstrating bounded S2 disturbance attenuation. Root team/task tools provide live operating feedback and changed commitments in S3 modes. A failed task is persisted as `failed` for later observation, but that alone does not establish a separate exceptional algedonic channel with guaranteed response. There is no separate first-party independent audit of active worker claims or future-facing adaptation loop established by the standard operating contract.

## Evidence gaps

- All claims are pinned static source/contract analysis. No live provider-invoked multi-teammate trace was reproduced.
- S2=C is **narrowly** supported by specific duplicate claim suppression; no general file-edit interference or adaptive arbitration claimed. Task arbitration is deterministic, not agent-owned S2=A.
- S3=A(P) relies on enabling first-party team mode and exposes separately model and human decision surfaces. No evidence of effective team-level performance improvement is asserted.
- Plan approval/review and automatic skill reflection are real features, but the Profile's independent reality access for S3* and external-prospective coupling for S4 are not established from these features alone.
