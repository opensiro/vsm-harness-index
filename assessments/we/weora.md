---
harness_id: weora
project_name: Weora
repository: https://github.com/yuzhiyang1/weora
review_ref: b860b68d1aeff13d0b90394d3468bc9c60eff456
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: ?
autonomy_s5: P
---

# Weora

## Review boundary

- System in focus: One configured Weora self-hosted workspace with source-authorized project tasks, a model-backed main coordinator, task workers and human workspace/task approval.
- Purpose and identity: Turn console/Feishu requests into permission-scoped plans and agent work, returning saved run/test/diff/delivery evidence to authorized users.
- Relevant environment: External code repository, user messages, Feishu threads, installed Pi runtime and browser/sandbox, test outcomes, code host, model/tool responses and access revocations.
- Standard-distribution boundary: FastAPI backend, coordination engine/main-session/worker dispatch, native runtime adapters, task and delivery services, sandbox and code-host connectors, workspace/agent/permission/console APIs.
- Credited operating / distribution surfaces: Model coordinator choosing task route under frozen authorization, executable worker Pi sessions, project-local tool execution and tested task reports, authorized user visibility and approvals.
- Adjacent first-party surfaces excluded from ownership: Marketing console illustration, planned memory/RAG/scheduled jobs and future CLI, docs-only future ideas, end-user development CI, underlying Pi/Oh My Pi provider ecosystems, external Feishu/GitHub authorization as independent organizations.
- First-party operating / deployment modes considered: Configured self-hosted web/Feishu task worker, optional model-backed main coordinator, human-approved plan and access, sandbox test/diff/code review, explicit task continuation/stop, agent/version settings.
- Recursion level: One authorized workspace/project-route team of a main coordinator and one or more worker tasks, not all cloud services or a cross-company organization.
- Reviewed revision: yuzhiyang1/weora@b860b68d1aeff13d0b90394d3468bc9c60eff456.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

FastAPI stores workspace, tasks, run events and grants in PostgreSQL; Celery dispatches worker runs to configured Pi/optional OMP runtimes. The first-party main coordination session loads authorized state and a fixed agent/skill version, invokes an actual model runtime with approved tools, and applies model choices through engine.decide. This engine checks ticket ownership, author-specific source grants, current leases and valid mandates, then attaches inputs to existing tickets or creates new scoped worker assignments. Worker RunExecutor renews leases while invoking the provider/runtime and stops on lost authorization or expired limits. User console, Feishu reply and code-host review expose run steps, tests, code diffs and authorization choices. Long-term memory, scheduled jobs and RAG remain planned, not shipped. Sources: [README.md](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/README.md), [backend/src/weora/modules/coordination/main_session.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/coordination/main_session.py), [backend/src/weora/modules/coordination/engine.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/coordination/engine.py), [backend/src/weora/modules/runs/application/execution.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/runs/application/execution.py), [backend/src/weora/modules/delivery/application/service.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/delivery/application/service.py).

## Operational model

S1 belongs to substantive source/task worker agent decisions under first-party runtime orchestration, not the lease renewer. The main coordinator has a distinct model-disposition path deciding whether incoming messages create tasks, attach to existing work or stop it. This supports a constructed S2-specific anti-duplication/ownership regulation mode but does not prove a live conflict resolution trace. Main-session model controls present task routing and acceptance, while a user retains access, approvals and stop rights. Independent source/test review is constructible as S3*, not automatically a running independent audit. Durable future capability evolution lacks a closed external-then feedback proof, so S4 remains unknown.

## S1 — Operations

- State: A
- Function: Perform substantive authorized agent changes and incident work under a persisted task mandate.
- Disturbance / variety regulated: Changing user objectives, code/repository environment, model/tool results, tests and follow-up messages.
- Decisive decision or feedback right: Configured worker agent chooses plan and authorized code/task actions through a native Pi session, and produces changed workspace/test/delivery evidence.
- Decision owner: First-party configured Weora worker agent under shipped worker runtime; Pi model runtime is a separately installed adapter, not an independent credited organization.
- Supporting / enforcement mechanisms: RunService, agent version/context, credential-authorized project sources, execution leases, sandbox tools, task/worker run events, continuation and code delivery.
- Closure path: User task and approved scope to worker model turn, tool execution under grants to saved changes and reports, test/diff or delivery receipt to task and later follow-up.
- Boundary reachability: Shipped backend code and APIs support this configured self-hosted mode with authorized owner, model runtime and workers.
- Why this is / is not agent-owned: Without model-directed worker there is no substantive answer/edit decision; the deterministic scheduler merely reserves and invokes it.
- Evidence: [backend/src/weora/modules/runs/application/execution.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/runs/application/execution.py), [backend/src/weora/modules/coordination/worker_runtime.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/coordination/worker_runtime.py), [backend/src/weora/modules/delivery/application/service.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/delivery/application/service.py), [README.md](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/README.md)
- Basis: structural
- Confidence: moderate
- Caveats: Exact pinned-source/static code analysis, without external Pi/cloud credentials or live model execution.


## S2 — Coordination

- State: C
- Function: Attenuate interference from simultaneous worker/task claims on shared objectives and incoming team instructions.
- Disturbance / variety regulated: Independent workers or incoming threads may initiate duplicate effort, cross-owner task routing and overlapping work.
- Decisive decision or feedback right: First-party coordination can select whether a request belongs to an existing task, stop/attach it instead of launching a competing new worker; actual inter-worker conflict adjudication needs an installed team configuration.
- Decision owner: Composed main-session coordinator plus separately configured worker/task cells; source supports the decision, but concrete S1-vs-S1 interference scenario was not executed.
- Supporting / enforcement mechanisms: Owner matching, single-task assignment, ticket mandates, canonical decision atomicity, source/author isolation, effect leases and worker dispatch.
- Closure path: Overlapping work request → coordinator assesses existing ticket ownership and may attach/stop or accept one scoped task → decision persisted and worker gets the new input or no duplicate worker created.
- Boundary reachability: Shipped backend code and APIs support this configured self-hosted mode with authorized owner, model runtime and workers.
- Why this is / is not agent-owned: Not merely an at-least-once queue: main-session model has an explicit attach/accept/stop choice and an existing owner guard, although only constructor-grade conflict closure is evidenced.
- Evidence: [backend/src/weora/modules/coordination/engine.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/coordination/engine.py), [backend/src/weora/modules/coordination/main_session.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/coordination/main_session.py), [backend/src/weora/modules/coordination/worker_dispatch.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/coordination/worker_dispatch.py)
- Basis: structural
- Confidence: moderate
- Caveats: Exact pinned-source/static code analysis, without external Pi/cloud credentials or live model execution.
- Distinct S1 units: Separately assigned task/worker agents in one configured workspace.
- Inter-S1 disturbance: Duplicate or overlapping incoming objectives can send two workers after the same work, or route new instructions to the wrong current worker.
- Attenuating coordination relation: The model coordinator classifies accept/attach/stop and source identity; the state engine prevents fresh competing acceptance when an existing task owner holds it.
- Feedback into subsequent S1 behaviour: Atomic decision either attaches new input to the existing ticket/worker, stops a ticket, or dispatches one new authorized worker with frozen scope.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: A constructible inter-worker duplicate-work/ownership attenuator is present, but not proven fully autonomous under a live cross-worker disturbance.


## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate current workspace task commitments, pending worker attention, stop/retry/continuation and authorized work.
- Disturbance / variety regulated: Pending or failed workers, changing human instructions, duplicate claims, unresolved attention and revoked access.
- Decisive decision or feedback right: Main coordinator chooses accept/attach/stop/resume/requeue based on current workspace state, while authorized user/admin may pause scopes, stop work or decide approval boundaries.
- Decision owner: Model-driven main-session coordinator in configured base mode; human workspace/task authority in parent mode.
- Supporting / enforcement mechanisms: Main-session reads authorized state, current tickets/effects, assignment reports and notices; engine validates decisions and persists leases/status; UI/APIs expose task status and owner actions.
- Closure path: Current ticket and worker reports → coordinator model decision → engine applies verified current task control → next worker assignment/input/resume or user hold; parent overrides access/stop/pause and the next worker honors it.
- Boundary reachability: Shipped backend code and APIs support this configured self-hosted mode with authorized owner, model runtime and workers.
- Why this is / is not agent-owned: A model makes actual disposition choices over whole scoped workload in main-session, while deterministic code checks leases and mandate. Parent choices are binding through exposed config/permission and run APIs.
- Evidence: [backend/src/weora/modules/coordination/main_session.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/coordination/main_session.py), [backend/src/weora/modules/coordination/engine.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/coordination/engine.py), [backend/src/weora/modules/coordination/service.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/coordination/service.py), [backend/src/weora/modules/runs/application/service.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/runs/application/service.py)
- Basis: structural
- Confidence: moderate
- Caveats: Exact pinned-source/static code analysis, without external Pi/cloud credentials or live model execution.
- Whole-system current view: Scoped main coordinator reads authorized triggers, tickets, active worker assignments, unresolved human/peer inputs and effects within one project route.
- Current-control decision scope: Accept/attach/stop/resume current objectives, choose when a worker may receive work, persist attention/wait and route completed/partial reports; human can revoke authorization/stop/pause work.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-backed first-party main-session coordinator | Changed tickets, worker reports and incoming requests | Accept/attach/stop/resume decision passed through engine, persisted and returned to assignment/worker | [backend/src/weora/modules/coordination/main_session.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/coordination/main_session.py) |
| Parent (`P`) | Authorized workspace member/administrator | Approval, task cancellation, workspace pause/access change | Scoped API/control setting persisted and rechecked before worker execution/continuation | [backend/src/weora/modules/coordination/service.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/coordination/service.py) |


## S3* — Complementary audit

- State: C
- Function: Supplement worker claims with directly inspectable test outputs, code diffs and delivery receipts under a distinct human review.
- Disturbance / variety regulated: Worker may assert successful task completion without current source/tests or authorization.
- Decisive decision or feedback right: An authorized human can inspect recorded sandbox test output and branch diff independent of agent summary, then authorize or demand another run; full independent default audit actor is not bundled.
- Decision owner: Constructed independent human/source reviewer, not the worker that generated the report.
- Supporting / enforcement mechanisms: Sandbox test execution and code-host review artifacts, receipt APIs, run event stream and user follow-up/approval path.
- Closure path: Worker report → independent source/test evidence view → user review or new directed task → follow-up run alters next task operation; source-level proof is configurable.
- Boundary reachability: Shipped backend code and APIs support this configured self-hosted mode with authorized owner, model runtime and workers.
- Why this is / is not agent-owned: The evidence originates from executed tests/source changes that can be checked outside the worker's self-report, rather than an LLM summary; independent audit is not default runtime autonomy.
- Evidence: [backend/src/weora/modules/delivery/application/service.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/delivery/application/service.py), [backend/src/weora/modules/delivery/infrastructure/github.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/delivery/infrastructure/github.py), [backend/src/weora/modules/runs/application/service.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/runs/application/service.py), [README.md](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/README.md)
- Basis: structural
- Confidence: moderate
- Caveats: Exact pinned-source/static code analysis, without external Pi/cloud credentials or live model execution.
- Claim being audited: Worker claim of passing tests, completed change and valid delivery.
- Ordinary reporting path: Worker status/report and task event feed.
- Complementary access path: User can inspect actual saved test output and versioned code diffs/PR artifact through sandbox and code-hosting integration.
- Independence boundary: Human source reviewer can use direct delivery/test evidence, distinct from model-authored report; first-party tools enforce source grants.
- Who acts on findings: User approves, rejects or issues a specific follow-up requiring a new worker run.


## S4 — Outside-and-then intelligence

- State: ?
- Function: Turn external future changes and review feedback into durable change of Weora agent capability.
- Disturbance / variety regulated: Evolving model performance, new skills and external team requirements.
- Decisive decision or feedback right: Human may select new agent version, skills and model configuration; a supported complete function-specific future-intelligence/option/return loop is not demonstrated.
- Decision owner: Potential workspace owner through agent registry, not a verified autonomous S4 decision maker.
- Supporting / enforcement mechanisms: Agent/version registry, skill sharing, model catalog and user settings; roadmap lists planned long-term memory/schedules.
- Closure path: Capability/config changes can be saved and used on later runs, but external future signal → evaluated adaptation options → returned decision with tested future capability effect is unestablished.
- Boundary reachability: Shipped backend code and APIs support this configured self-hosted mode with authorized owner, model runtime and workers.
- Why this is / is not agent-owned: The repo ships configuration persistence but not a demonstrated prospective analysis loop; planned memory/RAG/schedules are explicitly excluded.
- Evidence: [backend/src/weora/modules/agents/application/service.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/agents/application/service.py), [backend/src/weora/modules/console_settings/service.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/console_settings/service.py), [README.md](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/README.md)
- Basis: structural
- Confidence: moderate
- Caveats: Exact pinned-source/static code analysis, without external Pi/cloud credentials or live model execution.


## S5 — Policy and identity

- State: P
- Function: Maintain legitimate workspace purpose and permitted agent identity, authorization and execution rights.
- Disturbance / variety regulated: Unauthorized repository or Feishu inputs, version changes, unapproved writes, model credential abuse and scope expansion.
- Decisive decision or feedback right: Human workspace owner sets agent versions, source grants, runtime/connection choices and approves scoped plans before worker tools can act.
- Decision owner: Legitimate member/administrator at workspace recursion; model coordinators cannot invent or expand grants.
- Supporting / enforcement mechanisms: Authorized context and access checks, agent registry versions, route grants, main coordination policy, worker mandate checks and tool gateway.
- Closure path: Human policy/authorization → persisted workspace grants and agent/runtime version → repeated lease-time authorization checks → permitted or refused worker operation.
- Boundary reachability: Shipped backend code and APIs support this configured self-hosted mode with authorized owner, model runtime and workers.
- Why this is / is not agent-owned: Models can propose and route within approved scope, but cannot become the ultimate owner of access or task mandate.
- Evidence: [backend/src/weora/modules/coordination/service.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/coordination/service.py), [backend/src/weora/modules/coordination/engine.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/coordination/engine.py), [backend/src/weora/modules/agents/application/service.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/agents/application/service.py), [backend/src/weora/modules/runs/application/execution.py](https://github.com/yuzhiyang1/weora/blob/b860b68d1aeff13d0b90394d3468bc9c60eff456/backend/src/weora/modules/runs/application/execution.py)
- Basis: structural
- Confidence: moderate
- Caveats: Exact pinned-source/static code analysis, without external Pi/cloud credentials or live model execution.
- Identity / ultimate-policy issue: Which agents, source permissions, repository actions, model resources and approved task scopes are legitimate for this workspace.
- Ultimate authority in each claimed mode: Authorized human workspace/project owner; the coordinator and worker run under frozen mandates.
- Return-to-operation path: Saved scope/config and version/grant settings are checked by the coordinator and each worker/continuation before tools execute.


## Distributed OSS parent arrangement

Individual Weora workspaces have independent legitimate owners and stored grants. OSS maintainers and other users are not a common organization-level parent. Parent authority in S3/S5 belongs to the configured workspace/project owner.

## Self-hosted and non-human modes

The installed model coordinator and task worker can make bounded, authorized agentic decisions in supported modes; models do not gain source or approval rights from hosting alone. Human owners authorize grants and task scope; S3 parent mode is separate. Optional runtime adapter and provider requirements are not counted as native first-party organizational policy.

## Recursion

One workspace's configured main coordinator and worker task group. Multiple different user workspaces and vendor cloud/runtime infrastructure are outside this recursion; worker scheduling/leases alone do not establish additional VSM functions.

## Variety and escalation

Scoped permissions and model limits prevent tool overreach; persistent tickets/mandates prevent author leakage and duplicated assignment; completion reports require validation rather than worker self-declaration; attention and partial continuation return to the original legitimate actor. These mechanisms support bounded current control but are not automatic independent S3* audit or prospective S4.

## Evidence gaps

No live Pi/OMP session, Feishu tenant, external model or independently controlled audit was run. S2 is only the source-backed constructor of anti-duplicate task-owner routing, not an observed multiple-worker conflict test. S4 is unknown because shipped agent-version persistence does not establish a full future environment adaptation loop; planned long-term memory, RAG and schedules are explicitly excluded. Positive scope is one configured self-hosted workspace.
