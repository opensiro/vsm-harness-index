---
harness_id: soduwork
project_name: SoduWork
repository: https://github.com/mdiri-ai/SoduWork
review_ref: 97b9c2118a966869a862ef3aa3181ccb77c3dd3b
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# SoduWork

## Review boundary

- System in focus: the shipped SoduWork Hub plus its registered Runner and supported external coding-agent execution, with the first-party workflow, resource routing, independent code review, evidence and human issue-board oversight. SoduWork does not itself implement the inner reasoning/tool loops of OpenCode, Pi, Codex or other external coding agents.
- Purpose and identity: let a team turn requests into assigned, executable, reviewed and accepted deliverables, recording the exact artifact and the authorized owner at each stage.
- Relevant environment: multiple team requests and running agents, runner capacity and connectivity, competing execution slots, mutable repositories, failed reviews, changed deliverable versions and human business acceptance.
- Standard-distribution boundary: MIT-licensed self-hosted Hub and Runner services, bundled starter delivery workflow, agent adapters, task/approval APIs, code delivery and review, repository checkout and project board; optional third-party agents are exercised through their declared integration contracts.
- Credited operating / distribution surfaces: first-party orchestration of model-owned work in registered external agents, per-attempt isolated worktrees, distinct AI reviewer on a pinned commit, bounded feedback rework, current team issue board and operator assignment, capacity-triggered alternative admission/retry.
- Adjacent first-party surfaces excluded from ownership: the vendor internals of OpenCode/Pi/Codex/Claude/etc.; embedded upstream Harness² algorithms are attributed to their upstream, with SoduWork-specific adapter and bounded text-only planning probe identified separately; optional custom plugins, enterprise/private systems, repository CI and external provider models are not silently owned by Hub.
- First-party operating / deployment modes considered: self-hosted multi-user Hub with local or remote Runners and configured agent kind; bundled AI-plan/implementation/review/human-acceptance/publish starter; human-managed task board; optional Harness² text-planning refinement prior to actual agent execution.
- Recursion level: one team workspace with multiple agent-executed issues and the Hub's workflow-level supervision; an individual Runner or one DAG node is an operational unit, not a separate viable enterprise by naming alone.
- Reviewed revision: `97b9c2118a966869a862ef3aa3181ccb77c3dd3b`.
- Observation date: 2026-11-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The Hub's task service stores owners, priorities, requirements, assignments and audit events. Approved plugin versions define a DAG of AI, AI-review, quality, human-review, publication and other nodes. `workflow_engine` advances persisted node/outbox states exactly once, resolves the configured agent via `ai_exec` and Runner routing, and collects immutable delivery receipts. The bundled starter plugin moves from an AI-authored plan to AI implementation, an isolated AI code reviewer, human acceptance, and publication. The first-party Hub is the controlling harness for this **assembled operating system**, while each external agent owns its own inner model/tool reasoning loop. The optional Harness² adapter performs a text-only model-directed planning probe and returns instruction changes to the downstream agent rather than independently executing the business task. [README](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/README.md), [starter workflow](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/plugin_starter.py), [workflow engine](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/workflow_engine.py), [Harness² adapter](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/harness2_engine.py).

## Operational model

An agent receives a task brief and workspace, performs model-directed work using its own agent loop, and returns a versioned result to Hub. Hub can dispatch a different review agent against the immutable commit and route evidence-backed change requests back to an implementation attempt. Runner capacity conflicts are intercepted and retried by the workflow controller. The Hub's board exposes multiple live commitments to human operators who can assign/reassign and change priority. These paths establish a composite autonomous S1, constructed S2 resource coordination, human-parent S3 current control and independent model-based S3* audit; they do not prove an autonomous organization-wide strategist or ultimate-policy decision.

## S1 — Operations

- State: A
- Function: implement assigned code or document tasks and inspect resulting local artifacts using model-selected actions.
- Disturbance / variety regulated: novel requirements, repository contents, command results, implementation errors, changed code and review feedback.
- Decisive decision or feedback right: the configured agent model selects its next coding/research actions and subsequent corrections within the dispatched task; SoduWork's optional Harness² text adapter also uses models to propose task-method changes before actual work.
- Decision owner: configured external agent runtime for the substantive execution, not Hub's deterministic scheduler; SoduWork owns the packaged dispatch/receipt/rework integration, but does not claim the third-party agent's inner loop as original code.
- Supporting / enforcement mechanisms: `ai_exec.dispatch_sync`, Runner adapter, task-specific isolated worktree, persisted workflow/outbox, fixed artifact receipts, task context, retry caps and execution policy.
- Closure path: Hub task/approved plugin AI node → configured Runner invokes model-driven agent → agent observes repository/tools and performs work → versioned commit or file receipt returns to Hub → review feedback can dispatch a further agent work attempt.
- Boundary reachability: README's supported Runner/agent integrations and bundled starter `implement` node connect this operating path to the ordinary self-hosted distribution; it is not merely an unshipped extension point.
- Why this is / is not agent-owned: model judgment controls execution contents and rework; the Hub's graph, permissions and delivery checks constrain and record these decisions but do not author them. S1 ownership is at the composite supported deployment boundary, not a claim of first-party model-loop implementation.
- Evidence: [starter plan and implementation](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/plugin_starter.py), [AI dispatch and pinned workspace](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/workflow_engine.py), [external execution adapters](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/ai_exec.py), [text-only probe](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/harness2_bridge.py).
- Basis: explicit composition and code reachability.
- Confidence: high in dispatch and closure wiring; medium in generality across installed external agent kinds.
- Caveats: no live paid-provider or full deployment test; a Hub installation with zero configured agents has no executing S1, and the external runtime implements inner decisions.

## S2 — Coordination

- State: C
- Distinct S1 units: separate concurrently dispatched agent task executions, each owning its local model-directed implementation work on a registered Runner.
- Inter-S1 disturbance: two or more independent task executions compete for bounded Runner capacity; a new dispatch can receive `RUNNER_AT_CAPACITY` while another S1 holds execution slots.
- Attenuating coordination relation: Hub's Runner-capability and tag routing, explicit capacity-busy classification and persisted outbox retry defer the displaced task instead of falsely marking it executed or corrupting the incumbent.
- Feedback into subsequent S1 behaviour: after backoff and renewed admission the displaced S1 is actually started, processes the original task context and returns a real receipt; failure/busy is visible to the orchestration state meanwhile.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the source handles a named, observable interference among distinct operational task units over a finite common execution resource, and uses the returned capacity signal to alter when the next unit may act.
- Function: attenuate runner-execution interference between separate agent tasks competing for bounded Runner capacity, allowing later S1 work to proceed without pretending a rejected dispatch succeeded.
- Disturbance / variety regulated: simultaneous AI nodes requiring the same finite Runner slots, `RUNNER_AT_CAPACITY`, unavailable/incompatible machines and delayed remote acknowledgements.
- Decisive decision or feedback right: first-party constructor-defined capacity routing, busy classification and scheduled requeue; there is no demonstrated model-owned arbitration of shared capacity.
- Decision owner: SoduWork's deterministic Hub scheduler and agent-route selection, as constructed by the developer.
- Supporting / enforcement mechanisms: Runner `pick`/capability scope and capacity result, `_RunnerCapacityBusy`, `_requeue_capacity_wait`, persisted outbox claims and retry timing.
- Closure path: multiple active AI node dispatches → a Runner reports capacity busy → Hub classifies rather than fails task work → moves waiting dispatch back to eligible queue → later capacity permits agent operation and receipt collection.
- Boundary reachability: production `workflow_engine._execute_ai` handles `RUNNER_AT_CAPACITY`; the normal outbox `tick` path invokes capacity retry handling for registered Runner deployments.
- Why this is / is not agent-owned: this specific cross-task resource conflict and recovery path is packaged and operational, but its conflict handling is hard-coded rather than agent-decided, hence `C` rather than `A`.
- Evidence: [Runner busy classification and dispatch](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/workflow_engine.py), [Runner selection and execution](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/runner_hub.py), [outbox recovery](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/workflow_engine.py).
- Basis: structural constructive, with a concrete capacity-collision witness.
- Confidence: medium-high.
- Caveats: this is narrow execution-capacity coordination; authored DAG ordering or agent-to-reviewer handoff alone would not suffice for S2.

## S3 — Inside-and-now control

- State: P
- Whole-system current view: the Hub's multi-task issue/assignment/status board and live workflow state expose ongoing team commitments, failed work and available owner routes across issues rather than just one agent turn.
- Current-control decision scope: a legitimate human team operator can reassign current work, change priority and decide which stopped/ready issue to resume within the workspace's common operational capacity; the updates return through task state and assignment notifications.
- Function: maintain team-wide current issue commitments, ownership and priority, and return human portfolio intervention to the working operational cells.
- Disturbance / variety regulated: multiple simultaneous team requests, unassigned work, failed or blocked workflows, changing priorities and responsibilities.
- Decisive decision or feedback right: a human team operator edits issue priority/assignment or chooses the next start/rework; Hub enforces authorization and pushes the changed assignment into the relevant task/agent dispatch path.
- Decision owner: legitimate workspace operator/user in the shipped first-party parent-managed mode, not an autonomous S3 model. Automated scheduling and status transitions implement but do not own the portfolio judgment.
- Supporting / enforcement mechanisms: multi-task issue views, `tasks` update API with `priority` and `assigneeUserId`, task arrival notifications, workflow failure state, board status and user approval gates.
- Closure path: Hub issue list/current workflow state exposes portfolio → operator revises priority, ownership or authorization across team issues → `tasks` persists change and emits assignment events → later task dispatch/owner view follows revised commitments.
- Boundary reachability: the Hub/board and task mutation APIs ship with the standard multi-user application; the operator can close this parent loop without editing source or installing an extra plugin.
- Why this is / is not agent-owned: S3 is parent-owned human current control (`P`), while executor models remain bounded S1 agents. A human approval on *one* artifact alone is not the asserted S3 witness; the cross-issue state/commitment path is.
- Evidence: [task fields and reassignment](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/tasks.py), [task and workflow state](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/workflow_engine.py), [team workspace UX](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/README.md).
- Basis: parent-governed operating mode, structurally traced.
- Confidence: medium; project/workspace permissions and actual operator behavior vary by deployment.
- Caveats: no autonomous whole-current controller is established, and task-list visibility alone without reassignment/priority return would not qualify.

## S3* — Complementary audit

- State: A
- Claim being audited: an implementation agent's delivered commit is correct, secure, maintainable and satisfies the task's acceptance criteria.
- Ordinary reporting path: the implementer returns a git revision/receipt and its own status through the Runner to the workflow engine; that result is not treated as sufficient audit evidence.
- Complementary access path: the independent `ai_review` node is dispatched with the immutable commit and a separate isolated worktree, and instructed to read that repository reality directly and produce a fresh `code-review.json` rather than reuse an upstream completion summary.
- Independence boundary: a distinct review-node attempt with its own workspace, code read rights, pinned target, read-only/no-merge instruction and fresh structured findings; runtime configuration may still use the same vendor/model, so the claim is operational independence of evidence and action, not guaranteed model diversity.
- Who acts on findings: `workflow_engine` validates the review report, records attestation on approval or fails the node and returns change requests to implementation rework, subject to bounded retry/acceptance gates.
- Function: independently examine an implementation's fixed code artifact against task acceptance and code quality requirements, and issue corrective findings to current execution control.
- Disturbance / variety regulated: incorrect, insecure or unmaintainable implementations and false completion claims from the original executing agent.
- Decisive decision or feedback right: a separately dispatched reviewer agent reads the pinned code revision, forms an AI-authored structured verdict and findings; the Hub validates evidence shape and deterministically initiates rework on `changes_requested`.
- Decision owner: independent review-node model for the substantive audit judgment; Hub owns immutable target enforcement, report validation, attestation and rework routing.
- Supporting / enforcement mechanisms: bundled `ai_review` node separate from `implement`, per-node isolated worktree, fixed `codeReviewTarget` commit, no-write reviewer instruction, fresh `code-review.json`, `workflow_inputs.code_review_report`, and rejection/rework machinery.
- Closure path: implementation commit receipt → reviewer dispatched to inspect fixed commit directly → `code-review.json` with verdict/findings → Hub refuses success on changes requested and returns findings to new implementation attempt → revised commit can be independently checked again.
- Boundary reachability: the default starter plugin includes mandatory independent AI review before human acceptance; `workflow_engine` supplies pinned-version review and processes its structured result in the normal live node polling path.
- Why this is / is not agent-owned: a distinct model makes the fact-finding and correctness judgment with complementary access to the artifact itself, rather than trusting the implementation agent's status summary. Deterministic JSON checks and retry routing are enforcement, not the audit decision.
- Evidence: [shipped independent review stage](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/plugin_starter.py), [review isolation and locked target](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/workflow_engine.py), [review verdict/attestation processing](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/workflow_engine.py).
- Basis: explicit agent audit and corrective closure.
- Confidence: medium-high for isolated audit path; medium for strong reviewer-model/provider independence in every installation.
- Caveats: different node identity and isolated checkout do not guarantee different underlying foundation model; a review plugin that skips direct artifact examination would not satisfy this state in a particular run.

## S4 — Outside-and-then intelligence

- State: —
- Function: no product-owned loop is established that prospectively scans environmental futures, selects adaptation options and returns changes to the team's future operating capability.
- Disturbance / variety regulated: new plugin versions, agent providers, requested future work and changing task methods can arise, but these are administered or triggered per task.
- Decisive decision or feedback right: operators install or approve plugins, choose agents and methods; the optional Harness² adapter refines one immediate task plan, not future system adaptation policy.
- Decision owner: human plugin/operator configuration and task-level model planning; no separate S4 authority is evidenced.
- Supporting / enforcement mechanisms: plugin catalog, version review, Harness² planning probe, task briefs and model-agent routing.
- Closure path: changed task prompts or manually installed capability can reach next execution; no environmental forecast → option portfolio → prospective capability decision → operating return is shown.
- Why this is / is not agent-owned: task-method improvement (including text-only Harness² probes) does not by itself change the team's future-facing viable capability.
- Evidence: [Harness² text refinement](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/harness2_engine.py), [plugin governance](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/plugin_governance.py).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: a custom future-intelligence plugin could instantiate S4 beyond the reviewed packaged boundary.

### Absence scope

- Surfaces inspected: bundled starter plugin, plugin catalog/governance, Harness² vendor bridge and text probe, model routing and workflow retries.
- Plausible first-party paths checked: plugin upgrades, agent selection, bounded self-improvement, scheduled tasks and optional user-authored prospective workflows.
- Why no material first-party path remains: reviewed features handle present work or human-controlled configuration, not an established first-party externally prospective adaptation and return loop.

## S5 — Policy and identity

- State: —
- Function: no completed identity or ultimate-policy decision concerning the team as a viable whole is shown within the shipped operational boundary.
- Disturbance / variety regulated: unsafe plugin capabilities, delivery permissions, worker access, approval rights and artifact release are constrained by policy.
- Decisive decision or feedback right: humans grant access, approve individual deliveries and authorize plugin versions; static rule checks reject prohibited operations but do not adjudicate an identity/ultimate-policy conflict.
- Decision owner: users and configured enforcement for ordinary authorization; no evidenced S5 matter is escalated to a legitimate ultimate-policy holder and returned as governing identity policy.
- Supporting / enforcement mechanisms: plugin governance queues, release-control approvals, role/permission checks, audit trail and runner admission.
- Closure path: approval allows or blocks a plugin/task/release; there is no demonstrated organization-identity conflict → S5 judgment → changed governing mandate propagated to S3/S1.
- Why this is / is not agent-owned: source-backed approval gates and access controls are real but not sufficient proof of S5 decision ownership.
- Evidence: [plugin governance](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/plugin_governance.py), [approval-driven task acceptance](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/task_acceptance_review.py), [workflow approval gates](https://github.com/mdiri-ai/SoduWork/blob/97b9c2118a966869a862ef3aa3181ccb77c3dd3b/hub-backend/app/services/workflow_engine.py).
- Basis: bounded negative.
- Confidence: medium-high.
- Caveats: an organization may use these controls to implement external S5 governance, but that parent arrangement is not established by this source alone.

### Absence scope

- Surfaces inspected: task authorization, human acceptance, plugin admission and review, role-based runner policy and workflow approvals.
- Plausible first-party paths checked: acceptance gates, plugin permission review, team role changes and version revocation.
- Why no material first-party path remains: observed checks regulate specific capabilities/deliveries; no ultimate identity issue and policy-to-operation return is reconstructed.

## Distributed OSS parent arrangement

GitHub contributors and upstream project maintainers govern the source distribution, not the live self-hosted team workspace in this assessment. A self-hosted human workspace operator is a first-party parent for current-control S3 because the product's live board and assignments return portfolio intervention to running work. That does not import S4 or S5 from the OSS project organization.

## Self-hosted and non-human modes

Hub and Runner can be self-hosted, with multiple humans and configured external agent models. Normal AI work and independent AI review are non-human, while the evaluated whole-current-control S3 loop remains human governed. A headless configuration without actual operator portfolio feedback would not instantiate that `P` mode merely by running the server.

## Recursion

An `ai` node, independent review node and Runner operate as task-level differentiated units under one Hub workspace. Separate tool processes and worktrees are not proof of fully viable recursive sub-organizations. Assessment does not infer subsidiary S3–S5 from nested workflow nodes.

## Variety and escalation

Capacity-busy outbox retry attenuates resource interference; isolated task contexts separate agent attempts; fixed revisions and audit reports prevent unreviewed artifact changes from silently passing. A failed review returns bounded feedback for implementation rework, while human acceptance settles the final business deliverable. Critical workflow failure notification is an operational escalation, not automatically an independent S5 channel.

## Evidence gaps

This was source- and repository-doc-backed review of a pinned revision, not an instrumented multi-Runner deployment or paid-model end-to-end test. The external agent loop and reviewer are installed dependencies, and configured provider identity may collapse independence in some deployments. The `P` whole-current path is a product capability with an actual human decision, not a claimed autonomous managerial agent. Capability and audit contracts should be rechecked if the repository changes how its default plugin, Runner routing or issue-board authority works.
