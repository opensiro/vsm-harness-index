---
harness_id: rightcommit
project_name: rightcommit
repository: https://github.com/rightcommit/rightcommit
review_ref: d909627d71e010572202dfa4c3fe8019e296ae79
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: P
---

# rightcommit

## Review boundary

- System in focus: A rightcommit self-hosted workflow deployment executing a user's software or service work through configured first-party workflow nodes, external CLI coding models, verification stages and supported interactive/assisted/unattended supervision.
- Purpose and identity: Turn an approved specification and workflow into monitored edits, tests, agent review and optional authorized delivery, preserving per-run evidence and policy gates.
- Relevant environment: Software source trees, changing issue/specification input, externally hosted or local model runtime responses, test failures, concurrent branches, revision requests, human approvals and external service writes.
- Standard-distribution boundary: The published Rust HTTP server, `src/engine.rs` runner, `src/agents.rs` adapter, `src/manager.rs` Project Manager agent binding, `src/supervision.rs` AI supervisor, workspace state, review/test gates, first-party UI, settings and workflow data model.
- Credited operating / distribution surfaces: Runnable Task/Review/Connection/Merge/Fork/Join nodes with configured Claude Code/Codex/Pi runtime adapter; executor/supervisor decisions with persisted feedback; workflow design proposals and human save/activation; server-local tests, artifact versions and review rework.
- Adjacent first-party surfaces excluded from ownership: External Claude Code, Codex and Pi products as independent enterprises; separate hosted AI providers; developer-specific infrastructure, checked-in example workflows/tests, optional GitHub/Azure/ServiceNow services outside committed workflow, demo screenshot, maintainers and repo CI.
- First-party operating / deployment modes considered: User-controlled interactive workflow and parent approval, assisted AI recommendation with user decision, unattended AI supervisor making authorized bounded run decisions, parallel-agent workflow with explicit Review and test gates, workflow design chat.
- Recursion level: One rightcommit-configured run and its agent steps in a self-hosted workspace, with an owner administering that run/workflow; not an entire GitHub organization or provider's global operation.
- Reviewed revision: `rightcommit/rightcommit@d909627d71e010572202dfa4c3fe8019e296ae79`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The Rust engine validates a workflow graph and executes node-bound source operations, including model agent Task/Review turns, local tests and external-service Connection nodes. The model adapter invokes configured executable CLIs; first-party runner persists the run state, outputs and snapshots. Fork/Join lets distinct agent Tasks share an explicitly scoped workspace and later hand off results. Review nodes and server-local CI can route failures to iterative rework. The Project Manager conversation produces a proposed workflow from the user request, which the owner may apply. Run supervision is selectable in `ExecutionMode::{Interactive,Assisted,Unattended}`: in assisted mode a model makes a persisted approval recommendation but a human remains decisive, whereas unattended mode a bounded AI supervisor receives entire run policy/graph/context/outputs/artifact hashes and returns a decision through the ordinary run gate. External effects remain bound by `allow_external_writes`. Sources: [README control modes](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/README.md), [engine](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/engine.rs), [model](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/model.rs), [supervisor](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/supervision.rs), [Project Manager](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/manager.rs), [agent adapters](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/agents.rs), [artifact snapshots](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/artifacts.rs).

## Operational model

The actual S1 units are executable coding/workflow agent Tasks carrying out requested changes and producing saved code/artifacts, not deterministic orchestration wrappers. Different Task agents can be configured to run in parallel; the graph compiler, join handoff and permit scheduler are coordination substrate, but not on their own proof of a S2 inter-unit conflict regulator. At the declared single-run recursion, present control over outstanding gates, rework and authorization has two supported owners: human operator and the configured unattended AI supervisor. A distinct reviewer/checking path can be composed with a different agent and server-local test evidence. Long-lived workflow modifications and allowed external-write policies remain controlled by the user.

## S1 — Operations

- State: A
- Function: Execute substantive user task steps, evaluate outputs and write source/workflow artifacts through configured agent sessions.
- Disturbance / variety regulated: Changes in issue specifications and repo files, failing tests, tool responses, review feedback, evolving task details.
- Decisive decision or feedback right: The bound coding agent selects substantive edits, tool actions and artifact content in a `Task` node and can revise work from returned review feedback.
- Decision owner: Configured Claude Code/Codex/Pi model agent in the first-party engine-controlled execution loop; not the deterministic Rust scheduler itself.
- Supporting / enforcement mechanisms: First-party `agents::turn` runtime adapters, workspace/source checkout, task prompts, run output snapshots and test/rework gates.
- Closure path: Run input and task context → model-directed code/artifact work → saved workspace and task output → server tests/review/feedback → subsequent agent action or terminal run.
- Boundary reachability: `src/engine.rs` dispatches Task nodes through released `agents::turn` and stores state; `src/agents.rs` supports configured CLIs, including resumed run sessions.
- Why this is / is not agent-owned: Removing the model agent while preserving graph/loop leaves no material coding decision; deterministic routing alone is not the S1 owner.
- Evidence: [run driver](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/engine.rs), [model turn and CLI bridge](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/agents.rs), [task rework test](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/tests.rs), [README](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/README.md).
- Basis: structural
- Confidence: high
- Caveats: No model/API execution was performed during this source review; external provider decisions are credited only when invoked by the shipped first-party runtime, not as an unrelated product's operations.


## S2 — Coordination

- State: —
- Function: Attenuate actual interference among the multiple S1 coding agents in one workflow.
- Disturbance / variety regulated: Potential shared-file contention and parallel branch clashes, but no evidenced first-party conflict-specific agent decision loop.
- Decisive decision or feedback right: The repo validates graph paths, schedules parallel branches and hands off results; an inter-agent conflict adjudication choice with returned S1 behaviour was not established.
- Decision owner: No verified independent S2 coordinator in the shipped standard workflow boundary.
- Supporting / enforcement mechanisms: `parallel_branches`, `execute_parallel`, `join_handoffs`, shared-workspace prompt instructions and `parallelism::Scheduler` permits.
- Closure path: Fork/join and resource admission arrange execution and deliver handoffs; they do not demonstrate a controller resolving a concrete S1-versus-S1 disturbance.
- Boundary reachability: All these paths ship in first-party `src/engine.rs` and `src/parallelism.rs`, so absence is not based on ignoring parallelism.
- Why this is / is not agent-owned: The code contains sequencing, a common workspace and handoff, not a source-backed choice to attenuate oscillation/conflict between distinct S1 units with closed-loop feedback.
- Evidence: [parallel task graph](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/engine.rs), [permit scheduler](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/parallelism.rs), [fork/join integration test](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/engine.rs).
- Basis: structural
- Confidence: moderate
- Caveats: An explicitly configured coordinating agent might eventually perform this organizational function; the generic Task extensibility itself is not a first-party S2-specific constructor witness.


### Absence scope

- Surfaces inspected: Parallel fork/join, shared workspace, agent handoff, manager graph proposal, scheduler and available source tests.
- Plausible first-party paths checked: Searched for a first-party explicit conflict-specific decision, arbitration or resource-commitment feedback among distinct model Task S1 units.
- Why no material first-party path remains: Branch scheduling, common context and join output convey results without proving an organizational S2 interference-feedback closure; no additional native conflict-regulating loop was established.


## S3 — Inside-and-now control

- State: A(P)
- Function: Control current run commitments, review gates, rework and authorized external effects against the overall run objective.
- Disturbance / variety regulated: Incomplete or stale tested code, pending reviews, blocked tasks, connection write attempts and changing present run state.
- Decisive decision or feedback right: In unattended mode AI supervisor independently chooses approve/reject/answer for pending requests based on whole run and artifacts, with changes returned through `engine::apply_decision`; in interactive/assisted modes human chooses those current run interventions.
- Decision owner: First-party configured AI supervisor (unattended base mode); legitimate human run owner (interactive and assisted parent mode).
- Supporting / enforcement mechanisms: Persisted `Run` with workflow/state/outputs and artifact hashes, bounded supervision policy, `apply_decision` gating, manual approval UI, run state and test invalidation.
- Closure path: Pending gate/review → whole-run current context and evidence → supervisor or user decision → approve, rework, answer or abort → persisted changes to current downstream execution.
- Boundary reachability: The packaged supervisor passes the whole workflow, objective, outputs, decisions and artifact evidence to a configured model, then applies its decision in unattended mode; other shipped modes allow the owner to approve the same gate.
- Why this is / is not agent-owned: A model chooses whether current obligations meet the task and what rework to require in unattended mode. Rust enforces bounded permissions and persists; in interactive/assisted modes the human owns the corresponding intervention right.
- Evidence: [AI supervisor and application](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/supervision.rs), [graph/gates and decision return](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/engine.rs), [execution modes](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/model.rs), [human/AI modes](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/README.md).
- Basis: structural
- Confidence: moderate-high
- Caveats: Single-workflow recursion only; the AI does not control organization-wide capacity or create new permissions. Supervision concerns actually pending current decisions, not ultimate identity.
- Whole-system current view: AI supervision prompt receives the run objective, full workflow graph, pending request, outputs, context, recent decisions and bounded current artifact evidence; the operator sees the same run progress and gates.
- Current-control decision scope: Approve/reject a blocked run obligation, demand rework, answer pending gate, stop an unauthorized external write, resume authorized downstream node processing.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Configured AI supervisor in `Unattended` | Current pending gate or review with run-wide context and explicit execution policy | Supervisor decision stored, applied via `engine::apply_decision`, changes following node/rework/effect handling | [supervision.rs](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/supervision.rs) |
| Parent (`P`) | Authorized human run owner in `Interactive`/`Assisted` | Same pending run-level gate, user inspection or AI recommendation | Human approve/reject/answer applied via first-party decision endpoint, returned to workflow | [engine.rs](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/engine.rs), [README](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/README.md) |


## S3* — Complementary audit

- State: C
- Function: Check the implementer/run's claimed completion using distinct review and current-source test paths.
- Disturbance / variety regulated: Potential false 'done' assertions from agent work, stale test results, incorrect source edits or unverified external effects.
- Decisive decision or feedback right: A configured distinct reviewer agent can accept or reject an implementation based on the delivered artifact; server-local tests provide independently executed current workspace evidence and rejection routes edits to rework.
- Decision owner: Constructed separate review/checking agent and server-local test process; S3 operator uses the result. The ordinary implementer is not presumed to be its own auditor.
- Supporting / enforcement mechanisms: Workflow `Review` nodes, configurable agent assignment, artifact SHA-256 versions and diffs, local CI with freshness invalidation, feedback-to-author path.
- Closure path: Implementer output → separate reviewer/test evidence → verdict/rejection → saved gate and rework instruction → later implementation retested and re-reviewed.
- Boundary reachability: Native workflow graph can assign different models/agents to Review versus Task and ships local CI/review rework; the independent separation is *configurable*, not automatic in every workflow.
- Why this is / is not agent-owned: Independence is evidenced by an available separately configured reviewer and server-local test process, not by the ordinary Task agent's own completion message; without deliberate isolation the state would not be A.
- Evidence: [review/test design](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/README.md), [review gate and rework](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/engine.rs), [fresh-server-test assertions](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/tests.rs), [artifact snapshots](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/artifacts.rs).
- Basis: structural
- Confidence: moderate
- Caveats: C means first-party constructor supports an independent reviewer/checking arrangement. No claim that the default workflow automatically assigns a different reviewer, or that CI itself autonomously enforces strategic S3* decisions.
- Claim being audited: Implementer's asserted task completion and correctness of code/artifact output.
- Ordinary reporting path: Task `AgentResult`, run output, provider status and ordinary Activity Log.
- Complementary access path: Explicit Review agent node inspecting stored artifacts and server-local tests run against the workspace, including source diff/version comparisons.
- Independence boundary: Reviewer actor can be separately configured from author; local test runner is distinct from the implementing model, although both operate under the same self-hosted server.
- Who acts on findings: Review/test gate routes rejection or stale-test signals to the implementer for rework; run operator can intervene when required.


## S4 — Outside-and-then intelligence

- State: P
- Function: Adapt durable future workflow capability from changing requested work and accumulated evidence.
- Disturbance / variety regulated: New kinds of work, future project specifications, updated external service/provider requirements and deficiencies exposed by previous workflow runs.
- Decisive decision or feedback right: The human user decides whether to accept a model-generated new workflow or revised graph and saves it for later executions.
- Decision owner: Authorized workflow owner; Project Manager model proposes options but does not own their final adoption into ongoing capability.
- Supporting / enforcement mechanisms: Project Manager `manager::chat` generates structured workflow proposals; `engine::validate_draft`, revision and editor APIs, persisted workflow templates and subsequent run launch.
- Closure path: External future requirement → proposed workflow edit → user review/change/save → stored workflow graph → later run uses changed agent roles, review/test gates and connections.
- Boundary reachability: The Project Manager and workflow editor are first-party supported operating surfaces; reviewed workflow revisions are persisted for reuse, not just a maintainer backlog note.
- Why this is / is not agent-owned: The model offers prospective adaptation options; the lasting change to what the organization can execute later is owned by the user. Current task rework alone would be S1/S3, not S4.
- Evidence: [Project Manager proposals](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/manager.rs), [workflow graph validation](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/engine.rs), [drafts/commits and revisions](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/revision.rs), [README build/edit](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/README.md).
- Basis: structural
- Confidence: moderate
- Caveats: This is a bounded parent-governed adaptation of *workflow capability*, not proven autonomous environmental scanning, experimentation, model retraining or industry foresight.
- External distinction: User-supplied future project/work requirements, evolving software services and lessons from previous tasks enter the Project Manager workflow design conversation.
- Future / prospective distinction: Saving a new/revised workflow changes available future agent roles, gates and tools, not solely redoing one already-running step.
- Adaptation option generated: The model proposes a draft/new graph with tool and review stages, which the user can inspect, adjust and store.
- Path back into current capability / S3: Validated persisted workflow is chosen for subsequent runs; its gates then govern S3 supervision and S1 tasks.


## S5 — Policy and identity

- State: P
- Function: Set the binding ultimate rule of the run/workflow including allowed effects, agents, review obligations and execution mode.
- Disturbance / variety regulated: Risk from external writes, unrestricted unattended model decisions, improperly approved work and unclear workflow scope.
- Decisive decision or feedback right: Choose stored workflow definition and execution policy: interactive/assisted/unattended mode, maximum model gate decisions, approval rules and `allow_external_writes`, authorizing or refusing the organization's binding operating mandate.
- Decision owner: Authenticated human workflow owner sets and owns these boundaries; an unattended supervisor cannot supersede the policy.
- Supporting / enforcement mechanisms: Persisted workflow graph, execution policy, user scoping/authorization, revision validation, model supervisor checks and external-write digest approvals.
- Closure path: User-defined policy/identity → stored workflow and execution setting → each run's gate checks and model supervisor limits → allowed or refused effects and persisted decision audit.
- Boundary reachability: First-party UI/API and stored settings provide authoritative parent choice and real runtime propagation. Even unattended supervision is strictly subordinate to those settings.
- Why this is / is not agent-owned: Model approval of a single pending effect is S3 and cannot redefine ultimate authorization; only the legitimate owner can change what the workflow identity and allowed external effects are.
- Evidence: [execution mode and permission model](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/model.rs), [supervisor policy enforcement](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/supervision.rs), [run authorization and effect gates](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/src/engine.rs), [README approvals](https://github.com/rightcommit/rightcommit/blob/d909627d71e010572202dfa4c3fe8019e296ae79/README.md).
- Basis: structural
- Confidence: high
- Caveats: P is at the single-workflow ownership recursion; GitHub organization strategy, model provider rules and maintainers are not inferred as a first-party autonomous S5.
- Identity / ultimate-policy issue: What actions this run is authorized to perform, on whose resources and under whose approved spec/review standard.
- Ultimate authority in each claimed mode: Human workflow owner retains policy authority in interactive, assisted and unattended modes; the autonomous supervisor merely operates within the selected limits.
- Return-to-operation path: Saved user policy/graph is loaded into `Run`, checked by `engine::drive` and `supervision::resolve`, and governs all later agent execution and effects.


## Distributed OSS parent arrangement

The public repository may have independent contributors, but its self-hosted runtime owners do not form a shared upstream organizational S5. Parent notation is confined to the authenticated user operating one rightcommit workflow. A model supervisor does not inherit rights from maintainers, repository CI or third-party service owners.

## Self-hosted and non-human modes

Both user-governed and model-supervised execution are shipped: `Interactive` and `Assisted` leave current run gate decisions to the legitimate owner; `Unattended` applies the supervised model decision within explicit quotas and effect-write policy. Hence S3=`A(P)` records distinct supported owners at the same run recursion. S4 and S5 remain human-governed in these modes because adoption of durable workflow capability and permission policy are owner actions.

## Recursion

One self-hosted configured workflow/run; its agent Task nodes are S1 operations, and the run supervisor monitors that recursion. Cross-workflow enterprise portfolio, vendor provisioning and contribution governance are not silently pulled inside the boundary.

## Variety and escalation

The graph sequences and fans out agent decisions, tests and review attenuate incorrect deliverables, and per-run agent supervision provides bounded current decisions. Pending human approval, failed external effect policy, stale tests and supervisor decision limits stop or trigger rework. Parallel graph joins carry handoffs but are not, without explicit conflict closure, enough to label S2. Independent Review is constructible only when the owner configures an actually distinct review actor.

## Evidence gaps

This is pinned code/document/test review only. No Claude Code/Codex/Pi provider session or live run executed; no independent semantic reviewer was operated during assessment. Full autonomous S4/S5 and automatically independent default S3* are not claimed. The evidenced S3 supervisor has a run-wide context, but does not constitute cross-workflow organizational executive authority.
