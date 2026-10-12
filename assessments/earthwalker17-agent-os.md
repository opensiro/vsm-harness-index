---
harness_id: earthwalker17-agent-os
project_name: Agent OS (earthwalker17)
repository: https://github.com/earthwalker17/agent-os
review_ref: 59833d3f436bd1fd842860af2aa1c081d4b20363
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: ?
---

# Agent OS (earthwalker17)

## Review boundary
- System in focus: frozen `earthwalker17/agent-os` local-first project cockpit, bundled main model orchestrator, independent CodingAgentRunner and its first-party multi-role team execution, patch integration and verification/feedback.
- Purpose and identity: assist one user with coding/project work across persistent projects through a model-directed chat/planning brain and sanctioned project-scoped coding/team runs.
- Relevant environment: user project repositories, model/provider outputs, project memory and skills, sandboxed code edits, delegated worker task plans, review findings, build/browser evidence and explicit user approvals.
- Standard-distribution boundary: first-party FastAPI application plus locally shipped Coding Agent runner, team mode, sandbox and user-facing execution/review surfaces in the pinned repository ([ARCHITECTURE.md](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/ARCHITECTURE.md); [README.md](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/README.md)). External model vendors, credentials, connected GitHub/Vercel/Supabase/Stripe services and user-custom project skills are not credited for organizational decisions.
- Credited operating / distribution surfaces: [backend/orchestrator.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/orchestrator.py); [backend/execution/runner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/runner.py); [backend/execution/integration.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/integration.py); [backend/execution/planner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/planner.py); [backend/execution/roles.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/roles.py); [backend/execution/verification.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/verification.py); [backend/execution/skill_patch.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/skill_patch.py); [backend/main.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/main.py).
- Adjacent first-party surfaces excluded from ownership: repo CI/dogfood tests, release/deployment governance, provider-internal models, external service workflows, static role registry labels not used in execution, synthetic demos.
- First-party modes considered: main chat/memory planning, user-approved CodingAgentRunner, opt-in team-parallel wave execution with isolated coders and separate reviewer role, global build/browser checks, post-run skills proposals and per-action user authority.
- Recursion level: one running Agent OS installation overseeing one bounded project coding team for S2/S3/S3*; not the vendor organization or external GitHub ecosystem. Previously included `andrewgolovanov/agent-os` at `assessments/agent-os.md` is a **different** implementation and is explicitly excluded.
- Reviewed revision: `59833d3f436bd1fd842860af2aa1c081d4b20363`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
The main Agent OS chat-orchestration unit handles user conversation, memory, research and delegation intent, but does not directly edit the project repo. With an explicitly authorized `@code` or confirmed task, `CodingAgentRunner` executes its own model-driven planning, tool use and bounded codework. Some plans become team-eligible, and specialized model-backed worker units are scheduled in waves. The product owns first-party scratch patch workspaces, deterministic integration, reviewer tasks and verification. [ARCHITECTURE.md](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/ARCHITECTURE.md); [backend/orchestrator.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/orchestrator.py); [backend/execution/runner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/runner.py).
A team wave executes independent patch writers against separate overlays, then the deterministic `integrate_wave` function de-duplicates compatible writes and produces concrete blockers/conflict evidence when task writes collide. The role registry also offers a model-backed read-only reviewer unit that may inspect actual shared project files, emit independent findings, and affect downstream progress when the plan includes it. [backend/execution/integration.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/integration.py); [backend/execution/roles.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/roles.py); [backend/execution/planner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/planner.py); [backend/execution/runner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/runner.py).
Verification commands/browser capture/visual judgment and memory/skill suggestions add other stages, but not every test or separately labeled `verifier` is independent S3*: the `verifier` system-stage label is deterministic and executes no model loop. User confirmation and skills edits do not alone close S4/S5. [backend/execution/verification.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/verification.py); [backend/execution/visual_judge.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/visual_judge.py); [backend/execution/roles.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/roles.py); [backend/execution/skill_patch.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/skill_patch.py).

## Operational model
The model chooses real task/code actions, and in eligible team mode devises a plan of multiple dependent/specialized workers, including read-only review. Independent coding tasks can create incompatible workspace changes, which the deterministic patch integrator safely arbitrates. Control findings are stored in the shared run status and returned for follow-up; long-term skill and ultimate policy decisions are not assumed from basic features.

## S1 — Operations

- State: A
- Function: Model-guided first-party Coding Agent executes concrete software-development tasks using sandboxed read/write/shell tool actions and feeds results back into a bounded execution loop.
- Disturbance / variety regulated: Changing source files, test/build failures, user task constraints, subprocess/tool errors and runtime-generated observations.
- Decisive decision or feedback right: Choose task-specific project inspections, file changes and allowed tool calls; adapt actions after observed results.
- Decision owner: Configured coding-agent model through first-party CodingAgentRunner; `ToolRuntime` and `ProjectSandbox` enforce actions but do not choose them.
- Supporting / enforcement mechanisms: First-party CodingAgentRunner, task prompts, LLM protocol, ToolRuntime, ProjectSandbox, project run state and shell/test feedback.
- Closure path: Task request and workspace → LLM chooses tool/action → sandbox code/shell effect → observation/error → subsequent model step, repair or completion.
- Boundary reachability: The shipped background run dispatcher calls the first-party CodingAgentRunner using registered project workspaces. The runner executes model-supplied actions against the product's own ToolRuntime ([backend/execution/runner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/runner.py); [backend/execution/background.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/background.py)).
- Why this is / is not agent-owned: The operating right is discretionary model/tool action selection; a deterministic executor and cost/recovery gates are supporting control only.
- Evidence: [backend/execution/runner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/runner.py); [backend/execution/tool_runtime.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/tool_runtime.py); [backend/execution/sandbox.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/sandbox.py); [backend/main.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/main.py); [ARCHITECTURE.md](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/ARCHITECTURE.md)
- Basis: explicit + structural
- Confidence: high
- Caveats: Static first-party source inspection at frozen ref; not an executed provider-backed end-to-end evaluation. Mode-specific positives are not blanket claims about all installations.

## S2 — Coordination

- State: C
- Function: Protect concurrently operating coding S1 task units from mutually destructive file changes and surface content-specific integration conflicts.
- Distinct S1 units: Parallel coding task units, independently running model/tool role instances in one eligible team run.
- Inter-S1 disturbance: Different task units attempt to integrate incompatible overlapping changes.
- Attenuating coordination relation: Isolated overlays plus deterministic content/path collision detection and plan-order integration.
- Feedback into subsequent S1 behaviour: A rejected task's blocker and partial run status are returned to coordinating run outputs and future user/model action.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: It explicitly handles actual conflicting code edits, not only a queue, message bus, concurrency limit or worker count.
- Disturbance / variety regulated: Parallel specialist tasks can produce conflicting writes to the same repository-relative path or case-colliding path.
- Decisive decision or feedback right: Allow one compatible shared-file integration, reject conflicting later versions and mark the affected worker result as blocked/partial.
- Decision owner: Deterministic first-party wave integration policy (`integrate_wave`) and isolated patch workspace; not a separate model agent deciding merge priority.
- Supporting / enforcement mechanisms: Parallel wave executor, per-task patch overlay, first-writer-wins by plan order, normalized path collision checks, safe ToolRuntime writes and integration event/blocker store.
- Closure path: Independent worker artifacts → per-wave integration compares overlapping changes → retain first valid version / record incompatible later path → task blockers and partial status reach coordinator, verification and next run decisions.
- Boundary reachability: The shipped team runner launches multiple role-bound units using isolated overlays, invokes `integrate_wave` at each wave, writes conflict evidence to run artifacts and limits final status when conflicting ([backend/execution/runner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/runner.py); [backend/execution/integration.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/integration.py)).
- Why this is / is not agent-owned: Interference attenuation is real and file-content-specific, but the resolution policy is deterministic (C), while workers remain independent model-driven S1s.
- Evidence: [backend/execution/integration.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/integration.py); [backend/execution/runner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/runner.py); [backend/execution/planner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/planner.py); [ARCHITECTURE.md](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/ARCHITECTURE.md)
- Basis: explicit
- Confidence: high
- Caveats: Static first-party source inspection at frozen ref; not an executed provider-backed end-to-end evaluation. Mode-specific positives are not blanket claims about all installations.

## S3 — Inside-and-now control

- State: A
- Function: Model-led run planner/director sets and revises current coding-team commitments, assigns multiple task units, dependency order and execution roles based on project task and returned work.
- Whole-system current view: The executing bounded team has an execution plan, dependency graph and task statuses/integration evidence stored for coordination; does not claim a global external company-level view.
- Current-control decision scope: Assignment, dependency ordering and further work in one authorized run, with user reauthorization where required.
- Disturbance / variety regulated: Several concurrent units, dependency requirements, task failure, blocker/recovery and incomplete current work.
- Decisive decision or feedback right: Choose a plan and role/task allocation, change current subtask sequence through model planning or bounded recovery/follow-up proposals; abort or continue work based on outcomes.
- Decision owner: First-party model-driven team planner within CodingAgentRunner; deterministic wave scheduler, worker pool and user approval enforce selected plan and execution boundaries.
- Supporting / enforcement mechanisms: LLM `_plan_loop`, ExecutionPlan task graph, role contracts, compute_waves, run-status summaries, bounded recovery, interruption/cancel and task report store.
- Closure path: User project goal → model-derived plan with multiple specialized tasks → worker outcomes/integration findings → coordinator tracks commitments and reports blockers, chooses/requests follow-up or recovery → next current operations.
- Boundary reachability: For team-eligible code tasks, the packaged CodingAgentRunner follows model `plan` actions, admits a dependency/role plan and actually dispatches multiple units in waves, integrating outcomes into run/plan state ([backend/execution/runner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/runner.py); [backend/execution/planner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/planner.py)).
- Why this is / is not agent-owned: The model chooses the consequential current task commitments; scheduler and recovery budget code only executes/adapts within those decisions.
- Evidence: [backend/execution/runner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/runner.py); [backend/execution/planner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/planner.py); [backend/execution/roles.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/roles.py); [backend/execution/background.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/background.py); [ARCHITECTURE.md](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/ARCHITECTURE.md)
- Basis: structural
- Confidence: medium
- Caveats: Static first-party source inspection at frozen ref; not an executed provider-backed end-to-end evaluation. Mode-specific positives are not blanket claims about all installations.

## S3* — Complementary audit

- State: A
- Function: A distinct first-party, model-based read-only Reviewer task can inspect primary repository artifacts and issue independent defect/blocker findings into the team run.
- Claim being audited: That coder-produced repository files satisfy requested task constraints.
- Ordinary reporting path: Coder task returns its own final action/summary and files_changed.
- Complementary access path: Read-only reviewer unit can independently open shared repository files and inspect for defects.
- Independence boundary: Separate planned task unit with a dedicated review prompt, enforced non-mutating source tools and its own model reasoning, not the producer's own stdout/test output.
- Who acts on findings: Coordinator stores reviewer blockers; subsequent worker task/user can repair or stop further integration.
- Disturbance / variety regulated: Errors in produced code or integration that are not reliably revealed by the coder's own completion report.
- Decisive decision or feedback right: Read actual workspace files and report concrete defects as blockers, without the authority to alter source files directly.
- Decision owner: First-party model-driven reviewer role in a separately executing runner task unit, under model-planned team workflow.
- Supporting / enforcement mechanisms: Reviewer role with enforced read-only tool allowlist, specialized review prompt, `final` action with blockers; dependency graph and task integration/run status.
- Closure path: Prior coding artifacts become visible in shared repository → separate reviewer model independently reads source → emits findings/blockers → coordinator records them and downstream/parent work is blocked or revised.
- Boundary reachability: The bundled `reviewer` role is planner-assignable and runs through the same real per-task model/tool engine with enforced read-only tools; it reads integrated shared repo in a later dependency wave and returns blockers to the team coordinator ([backend/execution/roles.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/roles.py); [backend/execution/runner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/runner.py); [ARCHITECTURE.md](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/ARCHITECTURE.md)).
- Why this is / is not agent-owned: Auditing judgment is performed by a distinct model role with primary-source access, not by a deterministic parser of the producer's report or UI approval.
- Evidence: [backend/execution/roles.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/roles.py); [backend/execution/runner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/runner.py); [backend/execution/planner.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/planner.py); [ARCHITECTURE.md](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/ARCHITECTURE.md)
- Basis: structural
- Confidence: medium
- Caveats: Static first-party source inspection at frozen ref; not an executed provider-backed end-to-end evaluation. Mode-specific positives are not blanket claims about all installations.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Project memory/research and a green-run skill-patch suggestion offer plausible future capability improvement, but the prospective external adaptation function/owner is not conclusively closed.
- External distinction: Search and project evidence can be gathered, but the reviewed adaptation suggestion is primarily triggered by past/current task outcomes.
- Future / prospective distinction: Reusable skills affect later executions, without proof of strategic external horizon assessment.
- Adaptation option generated: A bounded append-style skill patch suggestion exists but promotion is user action, not a proven independent future-design authority.
- Path back into current capability / S3: Approved skills can enter the standard skills store and later prompts; the missing externally prospective source/decision prevents a positive S4 state.
- Disturbance / variety regulated: New external technology/project needs and repeating task failures that might demand changing future system capability.
- Decisive decision or feedback right: The main model may research and propose reusable skill edits, but adaptation decisions and forward-looking options are user-gated or task-local.
- Decision owner: Unresolved division between chat model, post-run skill-patch judge and user Save action.
- Supporting / enforcement mechanisms: Research channel, structured project memory, memory reconciliation, `skill_patch` suggestion and user-facing skills store.
- Closure path: Successful execution / historical evidence → suggested skill refinement → explicit user Save may change later prompts; whether external prospective scanning drives capability adaptation remains unproven.
- Why this is / is not agent-owned: Memory, research, self-improvement and future skill suggestions alone are not a demonstrated outside-and-then foresight/adaptation loop.
- Evidence: [backend/execution/skill_patch.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/skill_patch.py); [backend/skills_store.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/skills_store.py); [backend/execution/memory_reconciliation.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/memory_reconciliation.py); [backend/orchestrator.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/orchestrator.py); [ARCHITECTURE.md](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/ARCHITECTURE.md)
- Basis: unknown
- Confidence: low
- Caveats: Static first-party source inspection at frozen ref; not an executed provider-backed end-to-end evaluation. Mode-specific positives are not blanket claims about all installations.

## S5 — Policy and identity

- State: ?
- Function: SOUL identity anchor, manual approvals, sandbox policies and provider credential boundaries constrain behavior, but a higher ultimate policy/governance decision cycle is not demonstrated.
- Identity / ultimate-policy issue: Authority to revise the overall multi-project agent-system purpose and permissible conduct.
- Ultimate authority in each claimed mode: Human authorizes material execution and configured boundary, but full parent governance feedback is not traced.
- Return-to-operation path: Authorized requests alter individual allowed work, not verified organization-level ultimate policy evolution.
- Disturbance / variety regulated: Policy boundaries, unsafe shell actions, credential handling and user-desired identity of project work.
- Decisive decision or feedback right: User can manually authorize runs, change skill content and provide configuration; adaptive ultimate identity/policy authority and governing return remain unresolved.
- Decision owner: Human user and deterministic security/approval services; a qualifying first-party overall parent S5 loop not established.
- Supporting / enforcement mechanisms: SOUL.md identity, user confirmation, ProjectSandbox, secrets redactor, pending execution, skills registry and run budgets.
- Closure path: Human grant/deny or static policy → run/tool permission; no observed ultimate organizational identity revision prompted by feedback and returned to ongoing operations.
- Why this is / is not agent-owned: Static identity anchor or per-run approval is insufficient without legitimate ultimate policy judgment and return path.
- Evidence: [backend/execution/pending_execution.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/pending_execution.py); [backend/execution/sandbox.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/execution/sandbox.py); [backend/orchestrator.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/orchestrator.py); [ARCHITECTURE.md](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/ARCHITECTURE.md); [backend/main.py](https://github.com/earthwalker17/agent-os/blob/59833d3f436bd1fd842860af2aa1c081d4b20363/backend/main.py)
- Basis: unknown
- Confidence: low
- Caveats: Static first-party source inspection at frozen ref; not an executed provider-backed end-to-end evaluation. Mode-specific positives are not blanket claims about all installations.

## Recursion

First-party model-driven coding workers supply S1. Their parallel, independent edits create an actual cross-S1 merge-conflict disturbance; a deterministic coordinator supplies S2=C under parallel team mode. The model-led run planner and current task-status/role system provide team S3=A. A separately executing model reviewer with read-only primary source access and independent blockers can supply scoped S3*=A when selected and sequenced in a team plan. External SaaS services, CI and model-vendor internal agents remain out of scope.

## Variety and escalation

Changing task environment and model/tool failures are absorbed through the coding tool loop. Patch integration blocks incompatible edits and returns precise task-level conflicts. Reviewer findings and verification results may halt or prompt corrective work. User approval limits sensitive execution. Research, memory and skill change proposals provide plausible—but not yet positively closed—future adaptive capacity.

## Evidence gaps

Need stronger evidence for externally prospective capability option generation and adoption before S4 promotion, and for legitimate ultimate policy/identity decision-and-return before S5 promotion. S3* credit is limited to independently model-run reviewer tasks that directly inspect shared repo files; deterministic global verifier, visual diagnostics and ordinary coder self-tests are not credited as independent audit.
