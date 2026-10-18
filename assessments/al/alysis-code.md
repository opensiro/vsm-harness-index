---
harness_id: alysis-code
project_name: Alysis Code
repository: https://github.com/AlysisAi/alysis-code
review_ref: ff6682acb4a339dbbf9ce687c46374ce536ad641
reviewed_at: 2026-10-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Alysis Code

## Review boundary

- System in focus: first-party Python Alysis Code coding-agent CLI, session/model/tool loop, nested model-driven subagents, retained isolated candidate worktrees, optional source-reading verifier, and optional current Forge/Swarm plan control.
- Purpose and identity: transform a user coding task into accepted workspace changes and inspected evidence under host-owned execution policy.
- Relevant environment: user instructions, local repository, remote model providers, source revisions, test runners, parallel child models, permitted extensions, and trusted approval policy.
- Standard-distribution boundary: `alysis-code` packaged CLI `chat`, `run`, `forge`, `swarm`; first-party `src/alysis_code/` runtime and deterministic candidate admission. No external model provider internals or user's independent compliance organization credited.
- Credited operating / distribution surfaces: [src/alysis_code/agent/turn/core.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/agent/turn/core.py); [src/alysis_code/agent/subagent_execution.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/agent/subagent_execution.py); [src/alysis_code/agent/subagent_workspace.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/agent/subagent_workspace.py); [src/alysis_code/swarm_scheduler.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/swarm_scheduler.py); [src/alysis_code/swarm_orchestrator.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/swarm_orchestrator.py); [src/alysis_code/agent/verification.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/agent/verification.py).
- Adjacent first-party surfaces excluded from ownership: developer CI, benchmark adapters, unapproved external plugin and MCP servers, arbitrary custom tool scripts, future roadmap proposals.
- First-party operating / deployment modes considered: chat/one-shot agent, isolated parallel child writers with optional direct-source verifier, Forge/Swarm accepted plan control, completion contract. Positive claims limited to the modes that actually instantiate each constructor or model role.
- Recursion level: current Alysis Code user-owned coding session, and its optional first-party multi-task Forge run at the next nested operating decomposition; not maintainer company.
- Reviewed revision: `ff6682acb4a339dbbf9ce687c46374ce536ad641`.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The published CLI binds local task context and invokes first-party model/tool turns. Session-owned child models can inspect or write task-specific code, synchronously or in background. Mutating children can use separate Git worktrees, while the first-party child scheduler serializes incompatible shared mutations, prevents early release of pinned verifier evidence and checks candidate merge conflicts. Forge additionally tracks a whole current plan and admits or rejects dependency-safe task batches after integration verification. [docs/architecture.md](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/docs/architecture.md); [docs/subagents.md](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/docs/subagents.md); [docs/forge.md](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/docs/forge.md).

For complementary auditing, a completed isolated writer's exact retained worktree can be mounted read-only as a verifier child; its evidence and recommendation return to the parent before an explicit `subagent_apply`. This independent model-led source observation is distinct from deterministic completion-certificate verification and the producing model's own adversarial self-prompt. [docs/subagents.md](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/docs/subagents.md); [src/alysis_code/agent/verification.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/agent/verification.py); [src/alysis_code/agent/subagent_workspace.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/agent/subagent_workspace.py).

## Operational model

In ordinary chat, the producer selects actions and can route a bounded subagent. In the optional multiunit modes the runtime coordinates overlapping workspaces and manages current Forge task commitments. A separate verifier can inspect raw candidate code and return negative findings to the parent. S3/S3* functions are conditional on their advertised modes and are not inferred from optional source code alone.

## S1 — Operations

- State: A
- Function: Autonomous local coding session accepts user task, calls model and host-approved file/shell/verification tools and iterates on returned observations; model-driven focused child sessions can execute scoped coding tasks.
- Disturbance / variety regulated: User requirements, evolving code and tests, tool errors, sandbox conditions, provider responses.
- Decisive decision or feedback right: Choose task-specific source edits, inspections and verification work after reading direct tool feedback.
- Decision owner: First-party provider-driven Alysis Code agent model and separately model-driven bounded child Session where explicitly delegated.
- Supporting / enforcement mechanisms: CLI `alysis chat`/`alysis run`, turn.core controller, first-party tool assembly, permission/sandbox enforcement, model turn history.
- Closure path: Request → model/tool choice → allowed action → observations and completion/repair evidence → next model step/final.
- Boundary reachability: Official `alysis-code` package CLI binds workspace and creates first-party runtime; code paths and documentation agree.
- Why this is / is not agent-owned: Coding choices are genuinely model-selected; deterministic sandbox and completion constraints do not replace these decisions.
- Evidence: [docs/architecture.md](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/docs/architecture.md); [src/alysis_code/__main__.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/__main__.py); [src/alysis_code/agent/turn/core.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/agent/turn/core.py); [src/alysis_code/agent/verification.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/agent/verification.py)
- Basis: structural
- Confidence: high
- Caveats: No live model execution or quality benchmark was run for this source-only assessment.

## S2 — Coordination

- State: C
- Function: Prevent simultaneous independently executing child coding sessions from corrupting a shared worktree or merging incompatible work.
- Distinct S1 units: `subagent_run`/`subagent_spawn` create first-party nested sessions with model instructions and their own tools; Forge swarm workers also work in isolated tasks.
- Inter-S1 disturbance: Two write-capable children working in the same parent repository can race on the same files or overwrite the other's candidate; read-only helpers may inadvertently mutate the shared root.
- Attenuating coordination relation: Shared write-capable child runs are serialized; parallel writers use separate detached worktrees, guarded conflict-aware `subagent_apply`, and dependency/release pinning. Swarm batch scheduler requires disjoint precise claimed path scopes; overlap forces a separate batch.
- Feedback into subsequent S1 behaviour: A conflicting task is deferred/serialized, and candidate apply returns fail-closed conflict or a successfully integrated patch; parent receives bounded child outcomes before choosing further work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The system regulates concrete interference among concurrently acting child S1s through worktree isolation and overlap-based batch admission, not just assigning tasks or passing messages.
- Disturbance / variety regulated: Concurrent child edits, overlapping file claims, source-worktree release before checker completion.
- Decisive decision or feedback right: Select safe concurrent subset, delay incompatible child writes, enforce isolated candidate release/apply.
- Decision owner: Deterministic host `SubagentWorkspaceProvider`, batch scheduler and host admission constructor rather than an independent coordinating model.
- Supporting / enforcement mechanisms: Detached Git worktrees, overlap checker, release-pin lock, patch conflict detection, staged task dependencies and child registry.
- Closure path: Competing child requests → runtime scope/worktree admission → safe execution or deferral → conflict-aware integration → returned parent result.
- Boundary reachability: Documented CLI child modes and Forge swarm are implemented in first-party packages; positive claim bounded to concurrent child/isolation modes.
- Why this is / is not agent-owned: Agent may choose delegation, but inter-child safety policy is enforced by the runtime.
- Evidence: [docs/subagents.md](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/docs/subagents.md); [src/alysis_code/agent/subagent_workspace.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/agent/subagent_workspace.py); [src/alysis_code/swarm_scheduler.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/swarm_scheduler.py); [src/alysis_code/swarm_orchestrator.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/swarm_orchestrator.py)
- Basis: structural / explicit
- Confidence: high for constructor, medium for execution efficacy
- Caveats: Shared-worktree read-only parallelism is separately restricted and may require opt-in; no guarantee against all semantic integration conflicts.

## S3 — Inside-and-now control

- State: C
- Function: Maintain a whole-current Forge run's task states, dependencies, acceptance, integration health and continuation under a first-party plan/control cycle.
- Whole-system current view: Forge canonical plan and task-status ledger cover all current tasks (runnable, blocked, executing, failed, and awaiting integration), explicit dependencies and changed-path/write scope, plus batch integration evidence. The swarm orchestrator assembles this whole-current picture before admitting subsequent units.
- Current-control decision scope: Host Forge/Swarm controller authoritatively chooses which child tasks are runnable together, blocks dependencies or overlapping write scopes, accepts/rejects integration verified batches, updates canonical task states, and optionally recomputes the schedule after validated current-run replanning. This authority crosses multiple S1 task workers rather than operating within one producer's tool turn.
- Disturbance / variety regulated: Individual child failure, unmet prerequisites, incompatible candidate branches, integration verification failures, scope drift and blocked tasks.
- Decisive decision or feedback right: Determine runnable task batches, disallow blocked/dependency-unsatisfied work, reject failed integration, record authoritative task state, and recompute tasks/plan when admissible replanning changes it.
- Decision owner: Deterministic Forge/Swarm orchestrator control constructor with optional model replanning constrained by validation and run mode; not an independently chartered model S3 manager.
- Supporting / enforcement mechanisms: Canonical plan/run ledger, TaskCandidate/Schedule, explicit task statuses and dependencies, integration-gate verification, replan bookkeeping and merge guards.
- Closure path: Whole-run task-status/dependency view → select runnable work → execute children → inspect integration results → approve/reject merge and update task/run states → recalculate plan/schedule for subsequent work.
- Boundary reachability: Shipped `alysis forge run`, `forge exec`, `forge swarm` bind this control plane to plan-driven user tasks; ordinary single chat need not run Forge.
- Why this is / is not agent-owned: Current plan-level authority is host-owned; it makes binding decisions across multiple child tasks and is therefore C rather than A. One-shot completion gate alone would not warrant organization-level S3.
- Evidence: [docs/forge.md](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/docs/forge.md); [src/alysis_code/swarm_scheduler.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/swarm_scheduler.py); [src/alysis_code/swarm_orchestrator.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/swarm_orchestrator.py); [src/alysis_code/forge.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/forge.py)
- Basis: structural
- Confidence: medium-high
- Caveats: This is a conditional Forge recursion with explicit plan and tasks; not attributed to every CLI one-shot turn or to parent operator governance.

## S3* — Complementary audit

- State: A
- Function: Independently inspect a produced coding candidate via separate first-party verifier/code-reviewer model session, with direct access to the frozen candidate worktree and consequential feedback for parent admission.
- Claim being audited: A completed write-capable child reports a valid modification satisfying the parent's task and required verification.
- Ordinary reporting path: Producing child returns its own bounded summary/tool events; parent could otherwise trust the child-provided report.
- Complementary access path: A separate read-only `verifier` or `code-reviewer` subagent is launched with `workspace_from_run=<writer_run_id>`, pointing to the completed unreleased Git worktree itself, rather than solely the writer's claim. Deterministic independent host acceptance/execution evidence is also collected by the completion certificate.
- Independence boundary: Separate subagent model invocation and direct candidate-source view provide a first-party complementary route, not independent OpenSiro external reviewer or verified cross-provider separation.
- Who acts on findings: Verifying child returns bounded outcome; parent can resume worker for correction or discard, and calls `subagent_apply` only after accepting the verifier result. Host worktree release locks prevent apply/discard while the reading verifier is running.
- Disturbance / variety regulated: Hallucinated completion, wrong patch semantics, scope violations, failing verification of produced candidate.
- Decisive decision or feedback right: Read the candidate in a separately bounded model session and make a task-specific verifier judgment; parent uses findings to withhold admission and request repair.
- Decision owner: Configured separate verifier/code-reviewer model session (`A`), assisted by deterministic host evidence gate (`C`); no automatic universal audit guarantee.
- Supporting / enforcement mechanisms: Pinned source-worktree reader, wait/join and dependency chain, read-only roles, candidate release lock, acceptance certificate, verification evidence.
- Closure path: Write child finishes → separate verifier reads exact candidate → model verdict returned to parent → parent applies only if accepted or routes back via `subagent_resume` → candidate admitted/discarded.
- Boundary reachability: Documented first-party `subagent_spawn`, `subagent_wait`, `workspace_from_run`, `subagent_apply` are available in supported top-level chat/one-shot modes; this mode must be specifically requested or chosen by the parent and is not Forge default.
- Why this is / is not agent-owned: The verifier, unlike the deterministic completion gate or same-model adversarial nudge, is a distinct model actor with raw-source access and own evidence-directed judgment.
- Evidence: [docs/subagents.md](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/docs/subagents.md); [src/alysis_code/agent/subagent_execution.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/agent/subagent_execution.py); [src/alysis_code/agent/subagent_workspace.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/agent/subagent_workspace.py); [src/alysis_code/agent/verification.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/agent/verification.py); [src/alysis_code/agent/turn/core.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/agent/turn/core.py)
- Basis: structural / explicitly documented
- Confidence: medium-high for audit opportunity, medium for realized efficacy
- Caveats: Verifier call is optional, user/parent-led and can report incomplete or fail; independent model execution does not imply independent outside organization. An `adversarial_finalize` self-model nudge alone would only be a weaker constructor.

## S4 — Outside-and-then intelligence

- State: —
- Function: No sufficiently evidenced prospective external environment intelligence that produces and deploys organization-wide future strategic capability changes at this recursion.
- Disturbance / variety regulated: Provider/model changes, future task needs and learned recurring issues are possible external signals but not shown as an owned prospective intelligence cycle.
- Decisive decision or feedback right: Current Forge replanner can amend immediate plan on integration failure, not conduct future environment sensing with capability options.
- Decision owner: User/operator policy and current task model/plan repair; no independent S4 owner.
- Supporting / enforcement mechanisms: Replanning, memory, plugins, skill loading, extension docs and historical feedback bundles.
- Closure path: Immediate failure → revised current task schedule, not outside-and-then option → accepted future capability change.
- Why this is / is not agent-owned: Current-run replanning is S3; memory and optional extensibility are supporting surfaces rather than prospective strategic intelligence.
- Evidence: [src/alysis_code/swarm_orchestrator.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/swarm_orchestrator.py); [src/alysis_code/replanning.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/replanning.py); [docs/architecture.md](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/docs/architecture.md)
- Basis: structural
- Confidence: medium
- Caveats: A differently scoped managed service using Alysis may provide S4 externally.

### Absence scope

- Surfaces inspected: Runtime/Forge replanning, persisted memory/feedback, plugin/skill surfaces and optional model/provider interfaces.
- Plausible first-party paths checked: Forward task replanning, external tool data, extension changes and history memory.
- Why no material first-party path remains: No observed first-party future environmental option selection with durable strategic adoption is closed.

## S5 — Policy and identity

- State: —
- Function: No distinct agent-owned or organization-legitimate ultimate policy and identity deliberation loop with binding returned changes.
- Disturbance / variety regulated: Approval, sandbox escapes, tool scopes and user trust preferences.
- Decisive decision or feedback right: Human/operator sets security policy, execution mode and approvals; host enforces them.
- Decision owner: Operator and host policy machinery, not an S5 authority that deliberates organizational identity.
- Supporting / enforcement mechanisms: Sandbox permission modes, trusted configuration restrictions, approval scopes and execution hooks.
- Closure path: Tool action → deterministic allow/deny or human approval; no ultimate-policy/identity issue → legitimate deciding organ → binding policy feedback.
- Why this is / is not agent-owned: Host-owned safety rails and reviewer veto do not create a sovereign identity/policy organ.
- Evidence: [docs/architecture.md](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/docs/architecture.md); [docs/security_model.md](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/docs/security_model.md); [src/alysis_code/approval_scope.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/approval_scope.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Maintainer governance and user organization outside the agent runtime not credited.

### Absence scope

- Surfaces inspected: Approval gates, sandbox modes, hook trust, role controls and Forge task admission.
- Plausible first-party paths checked: Permission rejection, runtime authority conflicts, external human approval, plan acceptance.
- Why no material first-party path remains: No ultimate identity/policy arbitration channel exists inside the assessed first-party recursion.

## Recursion

First-party child agent model loops are bounded by parent authority and tool/profile settings, not automatically viable whole-system S3/S4/S5 organizations. The optional Forge current plan can constitute an operational supervisory constructor for its multiple task workers but remains under user project governance. [docs/architecture.md](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/docs/architecture.md); [docs/subagents.md](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/docs/subagents.md); [src/alysis_code/swarm_orchestrator.py](https://github.com/AlysisAi/alysis-code/blob/ff6682acb4a339dbbf9ce687c46374ce536ad641/src/alysis_code/swarm_orchestrator.py).

## Variety and escalation

Concrete concurrent writer interference → isolated worktree and overlap admissibility → actual conflict-aware apply. Current multi-task failure → Forge task/gate rejection and optional replan. A separately prompted read-only verifier can return direct-source findings to the producing parent and delay candidate acceptance; ordinary completion gate additionally applies host-executed evidence policy.

## Evidence gaps

- Source-only analysis; no independent executed benchmarks, recorded live verifier outputs, or completeness claims across all install configurations.
- S2=C bounded to concurrent child modes, S3=C bounded to Forge task-control recursion, and S3*=A bounded to separately executed exact-worktree verifier modes. The one-shot adversarial finalize prompt alone does **not** support the S3*=A claim.
- The user or parent must invoke/accept verifier and candidate-apply flow; this is not an automatic Organization independent reviewer or mandatory gate on every run.
