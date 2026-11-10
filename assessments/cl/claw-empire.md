---
harness_id: claw-empire
project_name: Claw-Empire
repository: https://github.com/GreenSheep01201/claw-empire
review_ref: 66a24ea7df2435ef897c48c147deb7ec572c01c2
reviewed_at: 2026-11-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Claw-Empire

## Review boundary

- System in focus: the shipped local-first Claw-Empire task/department/agent office runtime, not the Claude Code, Codex, OpenCode, Gemini or other separate provider products it launches.
- Purpose and identity: organize multiple model-backed working agents into departmental task execution, cross-department delegation, review and consolidation to deliver user-directed projects.
- Relevant environment: user/CEO decisions, local project files, Git working copies, external CLI agents, HTTP/OAuth/model providers, machine permissions and incoming project requirements.
- Standard-distribution boundary: installed application server, database, task/agent routes, provider launcher, delegation and multi-agent meeting/review workflows, including its supported operator and YOLO modes. It does not absorb external vendor internals as first-party mechanisms.
- Credited operating / distribution surfaces: [task run endpoint](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/core/tasks/execution-run.ts), [CLI-agent spawn route](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/core/agents/spawn.ts), [department delegation](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/collab/subtask-delegation.ts), [cross-department task reconciliation](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/collab/coordination/cross-dept-subtasks.ts), [agent review meeting](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/orchestration/meetings/review-consensus.ts), [review decision return](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/ops/messages/decision-inbox/review-round-reply.ts).
- Adjacent first-party surfaces excluded from ownership: README marketing claims, visual office simulation/sprites, build/CI tooling, Playwright and QA fixtures, demo slides and example artifacts, release machinery and the OSS maintainer organization. External agent CLI/model runtimes and the user's wider projects do not inherit function ownership solely from Claw-Empire's UI.
- First-party operating / deployment modes considered: local UI/API with configured external CLI, HTTP or OAuth provider agents; role/department task execution and review; human CEO Decision Inbox; opt-in deterministic YOLO decision processing. Individual direct chat and unassigned agent routes were checked as narrower modes.
- Recursion level: one deployed office/project organization coordinating several departmental task-executing agent cells. Each task has a local environment; department labels and spawned subprocesses do not on their own prove nested viable organizations.
- Reviewed revision: `66a24ea7df2435ef897c48c147deb7ec572c01c2`, frozen by Index intake #3047 / controller #3048.
- Observation date: 2026-11-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The [project README](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/README.md) documents a local office with agent roles, teams and several CLI/API connectors. The first-party TypeScript server persists agents, projects, tasks, subtasks and meeting minutes in a local database, exposes task/agent APIs, selects eligible agents according to configured workflow packs and role/dept constraints, constructs working prompts, creates worktrees, launches configured external agent providers, streams logs/status and handles completion. [Task execution](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/core/tasks/execution-run.ts), [auto assignment](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/core/tasks/execution-run-auto-assign.ts), [runtime providers](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/agents/providers.ts).

For task collaboration, source-shipped foreign-department subtasks are delegated in department-specific batches; delegated task statuses reconcile into parent-subtask state. On completion, the workflow may hold a parent task until child work is review-ready, then launch first-party one-shot team-leader discussion, collect specific revisions, persist meeting minutes and request a CEO Decision Inbox selection. The selected remediation items become new subtasks and can be returned to execution. [Delegation](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/collab/subtask-delegation.ts), [review consensus outcome](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/orchestration/meetings/review-consensus-outcome.ts), [decision application](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/ops/messages/decision-inbox/review-round-reply.ts).

Crucial provider distinction: direct API-agent execution makes a single streamed text-completion request and records output; it is **not** itself an iterative model/tool coding loop. In the standard CLI-agent mode, the separate provider CLI owns the inner tool-use loop while Claw-Empire ships the enclosing task assignment, model-directed working prompt, launch, completion and next-work feedback. [API provider execution](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/agents/providers/api-provider-tools.ts), [CLI spawn](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/core/agents/spawn.ts).

## Operational model

- Operational outcome: user-directed software/document/media/project deliverables created through model-backed working agents, with parent tasks and cross-department subtasks as durable units of work.
- S1 units: task-assigned model-backed workers operating on distinct local tasks/project worktrees; their agent-owned task decisions depend on configured external model/CLI executors, but are reachable from Claw-Empire's shipped task execution workflow. The office database/UI is not itself a cognition owner.
- Ownership split: working agents choose outcome-producing task actions; server code deterministically enforces assignment, ordering, status and review caps; separate model-backed team leads supply opinions. In a supported human-decision mode, a CEO/operator selects project-review readiness and which corrective actions run. YOLO delegates only a deterministic default option picker, not a newly autonomous S3/S5 agent.

## S1 — Operations

- State: A
- Function: configured model-backed worker agents perform assigned project tasks and generate artifacts in the project's local environment.
- Disturbance / variety regulated: changing user task requirements, code/file state, tool failures and feedback from subtask/QA results.
- Decisive decision or feedback right: choose detailed task-solving steps and generated deliverables after receiving the task/role/project prompt; the external CLI/provider executes model-selected actions rather than the server inventing their content.
- Decision owner: the model-backed assigned working agent in the supported CLI-agent deployment, not Claw-Empire's deterministic assignment selector. An API-text-only mode has a narrower repertoire and is not used as proof of file tool autonomy.
- Supporting / enforcement mechanisms: role/department prompt assembly, worktree creation, provider spawn, task state DB, streaming logs, timeout and session interrupt controls.
- Closure path: a task is assigned or auto-selected, server builds its project/role instructions and launches the configured agent; the agent's actions change the project; task completion updates stored state and subsequent review/delegation/next-task workflow. Subsequent agent actions depend on the task context and observations within the provider-run loop.
- Boundary reachability: [first-party task run route](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/core/tasks/execution-run.ts) wires first-party tasks to [supported CLI provider spawn](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/core/agents/spawn.ts); no demo-only fixture is needed to reach the actor/task/result path.
- Why this is / is not agent-owned: removing model-backed worker discretion leaves a launcher and fixed state machine unable to solve arbitrary assigned projects; CLI agent inner implementation is external, but the deployment ships its operative invocation/feedback path.
- Evidence: [task run](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/core/tasks/execution-run.ts), [spawn](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/core/agents/spawn.ts), [on-complete state](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/orchestration/run-complete-handler.ts).
- Basis: structural.
- Confidence: medium-high for supported CLI deployment wiring; source-static, not empirically executed.
- Caveats: requires installed/authorized external CLI/model provider; model capability, task success and real operational reliability are not verified. Single-prompt API mode does not independently prove an iterative tool loop.

## S2 — Coordination

- State: C
- Function: mitigate contradictory or blocked cross-department task/review commitments through first-party conflict-feedback and structured remediation coordination.
- Disturbance / variety regulated: work from different department S1s can reach incompatible approval/hold judgments and parent consolidation can proceed before delegated children finish, creating revision/reconciliation interference.
- Distinct S1 units: independently task-executing agents in the origin department and other delegated departments; team leaders for those work cells provide differing review positions.
- Inter-S1 disturbance: review leaders can hold approval with concrete revisions while others approve; a parent has outstanding foreign-department subtasks or collaboration child tasks, so completion/merge would be premature.
- Attenuating coordination relation: first-party department-batched delegation and parent-child status reconciliation, followed by agent-supplied round-specific review feedback and deduplicated remediation items instead of silently merging conflicting work.
- Feedback into subsequent S1 behaviour: a selected review item is materialized by `seedReviewRevisionSubtasks`, delegated via `processSubtaskDelegations`, and can start `openSupplementRound`; the completed delegated task's state updates the parent subtask before another review round.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the combination responds to a concrete *cross-unit* incomplete/contradictory review condition, with hold/resolution and corrective work returned to the affected agents. Mere department sorting or message transport alone would not qualify.
- Decisive decision or feedback right: choose which competing review/remediation concerns are actually acted upon. The application supplies the inter-S1 state/evidence and decision-return path, but this final selection is normally human and in YOLO mode a fixed heuristic, not an autonomous coordinating agent's discretion.
- Decision owner: constructor-supplied review/decision workflow; team-lead model opinions contribute proposals, while final remediation option selection belongs to human CEO or deterministic YOLO picker.
- Supporting / enforcement mechanisms: delegated-task linkage, parent readiness gates, meeting state/round caps, saved transcripts, decision options and database updates.
- Closure path: distinct agents finish/defer work → conflicting/hold review signals are collected → options reach CEO Decision Inbox → chosen remediation seeds follow-up subtasks → affected S1 work resumes. The S2-specific path is packaged; ownership of final coordination discretion is not agent-owned in the supported checked modes.
- Boundary reachability: [cross-department delegation](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/collab/subtask-delegation.ts) and [review meeting](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/orchestration/meetings/review-consensus.ts) are wired from the shipped task completion and normal decision route; [decision reply](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/ops/messages/decision-inbox/review-round-reply.ts) returns selected issues to execution.
- Why this is / is not agent-owned: model-backed leaders can propose different correction choices, but the operative final selection is not the leaders' shared autonomous decision; deterministic queue/order logic alone would not own coordination discretion. This supports `C`, not an unqualified `A`.
- Evidence: [delegation](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/collab/subtask-delegation.ts), [review claims](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/orchestration/meetings/review-consensus-outcome.ts), [selected remediation return](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/ops/messages/decision-inbox/review-round-reply.ts).
- Basis: structural.
- Confidence: medium; the source shows a specific first-party coordination/revision loop, but no live test of actual cross-team conflicts.
- Caveats: approval/review quality can also be task-level S3-like supervisory control; only inter-department disagreement/readiness attenuation is credited here. The human decision itself is not separately published as `S2=P` under this Methodology.

## S3 — Inside-and-now control

- State: P
- Function: project-wide review readiness and active intervention on current task commitments in an operator-governed CEO mode.
- Disturbance / variety regulated: simultaneously active project tasks may be partially completed, inconsistent with review gates, or need additional remediation before project-wide closure.
- Whole-system current view: database queries aggregate active vs review-ready tasks by project and expose eligible individual task choices in the Decision Inbox; review completion also checks unfinished delegated children.
- Current-control decision scope: the operator selects representative tasks for approval meetings, starts or withholds project review, requests specific follow-up work and chooses remedial items; decisions change current task commitments rather than defining a future strategy.
- Decisive decision or feedback right: approve review-stage progression, hold it, select corrective work and change active commitments after seeing the project/review state.
- Decision owner: legitimate human CEO/operator using the first-party Decision Inbox; deterministic YOLO mode selects canned actions rather than exercising an agent-owned discretionary whole-current control judgment.
- Supporting / enforcement mechanisms: project readiness SQL aggregation, review stage transitions, meeting minutes, task status locks, review hold, retry/time caps and auto-resume.
- Closure path: active/review status is aggregated → project-review decision item reaches operator → explicit selected action is persisted and either starts review meetings or creates follow-up subtask → work is reentered and subsequent state/decisions change.
- Boundary reachability: [project review decision handler](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/ops/messages/decision-inbox/project-review-reply.ts) is in the shipped UI/API decision route and acts on [review readiness gates](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/orchestration/review-finalize-tools.ts); no contributor-only governance is borrowed.
- Why this is / is not agent-owned: a team lead can make recommendations, but whole-project commitment authority stays with a human in the supported selected mode. An opt-in rule-based autopicker does not create S3=A and a status dashboard alone would be insufficient without the decision/return path.
- Evidence: [project-wide ready query / decision action](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/ops/messages/decision-inbox/project-review-reply.ts), [review hold](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/orchestration/review-finalize-tools.ts), [YOLO default picker](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/ops/messages/decision-inbox/yolo-mode.ts).
- Basis: structural.
- Confidence: medium-high for supported operator mode; automatic-mode limits explicitly scoped.
- Caveats: the parent mode requires an actual human operator to act; this source-static assessment does not demonstrate attendance or SLA reliability. Routine worker assignment or static concurrency alone is not credited as S3.

## S3* — Complementary audit

- State: —
- Function: no evidenced sufficiently independent, complementary operational reality check beyond ordinary task execution/review reporting at this office recursion.
- Disturbance / variety regulated: code/artifact correctness and misleading task-success reports are addressed by regular team-lead review and artifact gates, not a separate sourced independent audit owner/path.
- Decisive decision or feedback right: no first-party autonomous or constructor-specific complementary audit judgment with distinct access/feedback into whole-system current control was established.
- Decision owner: ordinary execution agents, team-lead review participants and deterministic artifact gates; none is demonstrated as a separately independent operational audit owner.
- Supporting / enforcement mechanisms: review meetings and minutes, task logs, validator/quality gates, video-render file existence/size checks, QA fixtures.
- Closure path: routine approval/rework is ordinary stage-gated production feedback, not a separately sourced S3* audit returning an independent verdict.
- Why this is / is not agent-owned: review participants receive task text/history and produce opinions, but the source does not establish complementary reality access sufficiently independent of the reported ordinary work; a routine critic/reviewer label is insufficient.
- Evidence: [review consensus](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/orchestration/meetings/review-consensus.ts), [review finalization / video artifact checks](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/orchestration/review-finalize-tools.ts), [completion transition](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/orchestration/run-complete-handler.ts).
- Basis: structural.
- Confidence: medium within the checked review/QA distribution.
- Caveats: external, operator-appointed independent audits are possible, but are not established as shipped first-party mode by the checked paths.

### Absence scope

- Surfaces inspected: task completion/review, meeting prompts, hold consensus, decision inbox, logs and artifact/QA checks; first-party supported office modes.
- Plausible first-party paths checked: team-lead review, review consensus rounds, validator gates, project logs, artifact checks and separate build/test fixtures.
- Why no material first-party path remains: the evaluated checks sit in routine production review or verify artifact existence; no function-specific complementary independently controlled evidence channel with a separate judgment returned to organizational current control is established at this boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supported environment-facing prospective adaptation loop that changes the office's *future* operational capabilities was established.
- Disturbance / variety regulated: project requirements and execution errors are current-task disturbances; changing provider availability and future tool capabilities would require external operator/developer action.
- Decisive decision or feedback right: no evidenced first-party agent or parent converting future external distinctions into an adopted change of reusable office capability.
- Decision owner: user/developer configuration for provider/models/workflow packs; model-backed agents plan within assigned projects rather than changing the office's future repertoire.
- Supporting / enforcement mechanisms: project planning prompts, workflow packs, persistent task/memo state, provider settings and completion logs.
- Closure path: ordinary task plans feed into current S1 work; no distinct prospective external intelligence/adaptation return path to the office runtime.
- Why this is / is not agent-owned: a planning department or multi-round review is not S4 without an external/future distinction and capability change.
- Evidence: [planning/review prompt](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/orchestration/planned-approval.ts), [workflow orchestration](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/orchestration.ts), [provider config](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/workflow/agents/providers.ts).
- Basis: structural.
- Confidence: medium; broader uninspected optional plugin behavior could alter this conclusion.
- Caveats: external maintainer feature development and future model/provider upgrades are not themselves first-party office S4.

### Absence scope

- Surfaces inspected: office task/department workflows, planned-approval meetings, provider/config surfaces, first-party persisted tasks and reviews, README-supported product boundary.
- Plausible first-party paths checked: task planning, workflow-pack customization, agent configuration, review revision memos, project knowledge persistence and provider upgrades.
- Why no material first-party path remains: all checked paths either solve/review current work or apply external configuration; none supplies prospective environmental sensing, adaptation-option selection and returned durable capability change as a supported office decision loop.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy decision closure for the office recursion is established by CEO branding or permissions alone.
- Disturbance / variety regulated: policies for tools, workflow packs, model credentials and task approvals constrain ongoing tasks but do not source an ultimate-identity dispute or return decision.
- Decisive decision or feedback right: no evidenced identity/ultimate-policy issue routed to a legitimate parent authority and returned as a governing office policy decision.
- Decision owner: human installer/operator and code/configuration authors set static role and permission constraints; ordinary CEO task approval is S3 current control, not S5.
- Supporting / enforcement mechanisms: configured role prompts, provider credentials, CSRF/interrupt control tokens, policy labels, project workflows and operator settings.
- Closure path: task-level decisions return to work, but no distinct ultimate-policy matter → legitimate authority → office-wide authoritative identity return path is demonstrated.
- Why this is / is not agent-owned: virtual CEO/leader roles, fixed constraints and human project approvals are insufficient to establish S5=A, S5=C or S5=P without an identity-level matter and return loop.
- Evidence: [operator decision handler](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/ops/messages/decision-inbox/project-review-reply.ts), [task interrupt and security](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/modules/routes/core/tasks/execution-control.ts), [runtime configuration](https://github.com/GreenSheep01201/claw-empire/blob/66a24ea7df2435ef897c48c147deb7ec572c01c2/server/config/runtime.ts).
- Basis: structural.
- Confidence: medium-high at the shipped task/office recursion.
- Caveats: maintainer governance and a user's wider organization may have separate S5, but they are outside the assessed runtime boundary.

### Absence scope

- Surfaces inspected: runtime configuration/security, task/agent state/authority, CEO Decision Inbox, planned/review meetings, code/README governance boundary.
- Plausible first-party paths checked: CEO task approvals, manual workflow/model selection, YOLO automatic decision choices, interrupt/stop authority, department policies and OSS maintainer configuration.
- Why no material first-party path remains: these are current operational choices or static enforcement mechanisms, not a shipped identity/ultimate-policy issue routed through legitimate authority with a return governing subsequent organizational identity.

## Recursion

An agent-task cell has a local project/worktree and model-backed operational discretion, but it relies on Claw-Empire for assignment, coordination and review and on an external CLI for the inner tool loop. Department names, hierarchy and spawned CLI processes are not sufficient to demonstrate recursively complete viable organizations. The office/project level is the declared system-in-focus, with human current-project supervision recognized only where a returned S3 path is source-wired.

## Variety and escalation

Task-specific variety reaches working agents through user prompt, project context, tool feedback and revision subtasks. Department queues/review holds attenuate potential inter-unit interference, while meeting transcripts and human-selected remediation can amplify the available correction repertoire. Fixed retry caps, workflow rules and YOLO default choice reduce presented options but are not automatically agent-owned choices. Missing providers, command failure or unfinished foreign subtask may cause a status/hold; status alone is not an algedonic governance channel or S5 claim. Genuine decisions beyond the local office's programmed/human operating envelope must be escalated outside the assessed runtime.

## Evidence gaps

- Source-static assessment only: no local installation, external CLI/provider authorization, live agent task, genuine human review, or artifact-production success was executed.
- The inner cognitive/tool loop of Claude/Codex/OpenCode is external, so the positive S1 claim is scoped to the *supported first-party orchestration/deployment* of such task-executing actors; the API text-only route does not independently provide coding-tool autonomy.
- S2=C and S3=P rely on identified first-party review/decision/feedback paths, not evidence that every user enables multi-department mode or performs the human decision on time. Multi-department/YOLO deployments outside shipped wiring are not assumed.
- Full security, every workflow pack, every provider adapter and all possible contributor-developed extensions were not exhaustively executed; the negative states are bounded to the inspected standard office distribution.
