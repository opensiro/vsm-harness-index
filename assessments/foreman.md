---
harness_id: foreman
project_name: Foreman
repository: https://github.com/marcelsud/claude-foreman
review_ref: 1863451a47f914a909f2b3857a73e87645ccd1fe
reviewed_at: 2026-09-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-22
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A(P)
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Foreman

## Review boundary

- System in focus: one first-party Foreman control organization at pinned revision `1863451a47f914a909f2b3857a73e87645ccd1fe`, including its MCP control plane, detached scheduler/daemon, durable SQLite goal/task/run/approval/event state, worker runner, isolated worktrees, approval protocol, verification service, manager review/requeue/accept path and reviewed workflow compiler.
- Purpose and identity: let an interactive Claude Code or Codex managing session delegate bounded coding tasks to background Claude/Codex workers while preserving durable lifecycle, exact approvals, independent verification evidence and explicit review before acceptance.
- Relevant environment: human user; interactive Claude Code or Codex manager; spawned Claude/Codex worker/model runtimes; target Git repositories; local subscription-authenticated provider state; operating-system sandboxing; project-defined verification commands; and downstream repositories/workflows using Foreman.
- Standard-distribution boundary: Foreman's shipped plugin/skill/MCP/daemon/database/runner/worktree/verification surfaces plus the explicitly integrated manager and worker actor relations they invoke. External Claude/Codex reasoning remains separate: Foreman receives and constrains those actors but does not inherit their internal functions merely because they run through the integration.
- Credited operating / distribution surfaces: root `README.md`; `plugins/foreman/README.md`; `plugins/foreman/skills/manage-foreman-agents/SKILL.md`; `plugins/foreman/skills/manage-foreman-agents/references/approval-policy.md`; `plugins/foreman/skills/manage-foreman-agents/references/workflow-schema.md`; `plugins/foreman/src/foreman/mcp_server.py`; `plugins/foreman/src/foreman/database.py`; `plugins/foreman/src/foreman/runner.py`; `plugins/foreman/src/foreman/verification.py`.
- Adjacent first-party surfaces excluded from ownership: repository-development CI, maintainer/contributor review, release/versioning activity, test fixtures except as corroboration, and any internal Claude Code/Codex model/tool behavior not exposed through the declared Foreman relation.
- First-party operating / deployment modes considered: interactive manager plus background scheduler; queued/running worker tasks; exact approval decisions; verification gates; manager review with accept/requeue; human-only escalation for critical actions; reviewed workflow versions compiled into dependency-gated phases; monitoring/wake/event surfaces.
- Recursion level: one Foreman-managed goal/task organization is the system-in-focus. Background implementation workers are S1 units. The interactive managing assistant and human user sit in the metasystem relation exposed by the shipped skill/MCP surfaces. Independent Foreman installations or unrelated manager sessions are not silently aggregated.
- Reviewed revision: `1863451a47f914a909f2b3857a73e87645ccd1fe`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Foreman is a durable local control plane rather than the coding reasoner itself. The interactive Claude Code or Codex session remains the manager. Through the shipped skill and MCP tools it creates goals/tasks, chooses provider/model/effort/priority/dependencies/verification gates, watches actionable events, decides routine exact approvals, reviews completed work, requeues defects with concrete feedback or accepts the result. The detached scheduler claims ready tasks from SQLite and launches separate Claude or Codex implementation workers in isolated Git worktrees.

Worker completion is not accepted automatically. After the worker exits, Foreman changes the task to `verifying`, executes configured verification commands independently through the Codex App Server sandbox, fingerprints the tested worktree state, records structured results, snapshots the worktree and moves the task to `awaiting_review`. The manager then inspects the full diff plus verification evidence and decides whether to accept or requeue. Requeue feedback is persisted and injected into the next worker prompt, creating a bounded corrective return from review into operation.

Foreman also supports dependencies and reviewed workflow phases. The scheduler prevents a dependent task from running until its parent is accepted, and a linear workflow chain can share one worktree. These are meaningful sequencing/isolation controls, but the reviewed standard distribution does not establish the stronger S2 witness required by Methodology 0.3.6: a concrete interaction-generated sibling disturbance together with a distinct coordination decision/feedback loop that attenuates it. Parallel root chains remain separate worktrees; dependency topology is not promoted to S2 by naming alone.

## Operational model

A managing assistant creates a task or goal through Foreman's MCP surface. The scheduler atomically claims ready tasks subject to dependencies and goal state, prepares/reuses an isolated worktree and launches an external Claude/Codex worker. The worker owns task-local reasoning, while Foreman enforces sandbox/approval boundaries and records durable progress.

Routine in-scope approval requests may be decided by the manager against the exact request hash. Critical operations such as force-push, deployment, credential access, material deletion or sandbox bypass require explicit human confirmation. When the worker finishes, Foreman independently runs any declared verification gates and exposes their tested-state fingerprints/results together with the complete worktree diff. The manager then either accepts the reviewed result or requeues the task with feedback that is returned to the next worker attempt. Acceptance does not merge, push, deploy or delete the worktree.

## S1 — Operations

- State: A
- Function: perform bounded implementation work in a target repository through a background Claude Code or Codex worker operating in a Foreman-created worktree.
- Disturbance / variety regulated: task-specific repository state, implementation uncertainty, tests/build feedback, local tool outcomes, clarifying questions and review feedback from earlier attempts.
- Decisive decision or feedback right: choose the substantive task-local reasoning path, edits and tool actions required to satisfy the assigned implementation prompt within Foreman's worktree/sandbox/approval envelope.
- Decision owner: the autonomous external Claude/Codex worker actor launched through Foreman's first-party runner.
- Supporting / enforcement mechanisms: provider/model/effort assignment, worker policy, worktree lifecycle, sandboxing, turn budget, exact approval hooks, cancellation, durable events and retry/requeue lifecycle.
- Closure path: manager admits a task → detached scheduler claims it → Foreman prepares an isolated worktree and launches the selected external worker → worker makes task-local decisions and receives repository/tool feedback → worker reports completion/failure → Foreman runs verification and returns the result to metasystem review; requeue feedback can enter a later worker attempt.
- Boundary reachability: background task creation and execution are the primary shipped product path documented in the repository README and developer reference; `runner.py` directly launches Claude/Codex worker integrations under the normal daemon workflow.
- Why this is / is not agent-owned: the first-party control plane owns admission, lifecycle and constraints, but the model actor owns substantive implementation reasoning. Foreman's deterministic scheduler, sandbox and policy hooks do not choose the code-level solution.
- Evidence: [`README.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/README.md); [`plugins/foreman/README.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/README.md); [`plugins/foreman/src/foreman/runner.py`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/src/foreman/runner.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the internal organizational functions of Claude Code/Codex are not inherited. The positive state credits the reachable external operational actor only for the task-local decision right Foreman actually delegates to it.

## S2 — Coordination

- State: —
- Function: no installation-level S2 mutual-adjustment function is established from the reviewed standard distribution.
- Disturbance / variety regulated: Foreman can run multiple tasks, isolate them in worktrees, sequence dependency-gated phases and keep a shared-worktree workflow history linear, but the inspected standard paths do not establish a concrete sibling-generated oscillation/interference signal together with a coordination decision/feedback loop whose function is to damp that disturbance between active S1 units.
- Decisive decision or feedback right: not established at the declared recursion.
- Decision owner: not established.
- Supporting / enforcement mechanisms: per-task worktrees, dependency records, atomic ready-task claiming, reviewed workflow phase gates, priority and worker-concurrency limits provide isolation/sequencing/resource structure without independently satisfying S2.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: no qualifying S2 function was established, so there is no S2-specific decision right to classify.
- Evidence: [`plugins/foreman/README.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/README.md); [`plugins/foreman/skills/manage-foreman-agents/SKILL.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/skills/manage-foreman-agents/SKILL.md); [`plugins/foreman/skills/manage-foreman-agents/references/workflow-schema.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/skills/manage-foreman-agents/references/workflow-schema.md); [`plugins/foreman/src/foreman/database.py`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/src/foreman/database.py).
- Basis: explicit + structural negative search.
- Confidence: medium-high.
- Caveats: dependency scheduling can be part of S2 in another boundary if evidence ties it to a concrete inter-S1 disturbance. Here the documentation states dependency/prerequisite and linear-history semantics, not a distinct sensed sibling disturbance and corrective mutual-adjustment loop. Separate worktrees are preventive isolation rather than sufficient S2 evidence by themselves.

### Absence scope

- Surfaces inspected: task dependencies, scheduler claiming, worktree isolation/reuse, worker concurrency, workflow phase compilation, accepted-parent gating, event/wake supervision, review/requeue and verification paths.
- Plausible first-party paths checked: parallel tasks under one goal; separate root workflow chains; linear phases sharing a worktree; dependency release after acceptance; task priority and queue scheduling; review feedback between attempts.
- Why no material first-party path remains: the first-party mechanisms sequence prerequisites, isolate concurrent work, allocate scheduler capacity and return vertical review feedback. No reviewed path establishes an interaction-generated disturbance among sibling S1 units and then feeds a dedicated coordination adjustment into those siblings. Review/requeue belongs to S3/S3*, not S2.

## S3 — Inside-and-now control

- State: A(P)
- Function: regulate the current Foreman organization by deciding task admission/configuration, routine approvals, responses to actionable worker events, review/requeue/accept outcomes and cancellation/goal state while preserving human authority over critical actions.
- Disturbance / variety regulated: queued/running/blocked tasks, approval requests, worker errors, failed verification, incomplete diffs, model/provider choices, dependency readiness, cancellations and risky actions can require whole-goal current intervention.
- Decisive decision or feedback right: base mode — the autonomous managing Claude/Codex session chooses task definitions/configuration, routine exact approvals, monitoring responses, review feedback, requeue or acceptance; parent mode — the human user decides human-only critical approval requests and can direct/cancel/withhold acceptance through the manager interface.
- Decision owner: base mode — the autonomous external managing assistant explicitly assigned the manager role by the shipped Foreman skill and MCP interface. Parent mode — the human user for critical actions and direct supervisory decisions.
- Supporting / enforcement mechanisms: compact task/goal views, actionable `task_wait` wake events, durable event/approval state, exact hash-bound approval API, scheduler state, task configure/cancel, goal status, task diff, verification summary, requeue/accept transitions and daemon controls.
- Closure path: Foreman exposes current goal/task/approval/verification state → managing assistant or human identifies a present-control issue → decision is made through first-party MCP controls → scheduler/runner/database changes current task/approval/goal state → durable events/wake surfaces return the new current state to the manager.
- Boundary reachability: the root README instructs users to install the plugin into Claude Code/Codex and start a manager session; the shipped skill explicitly says the managing session is responsible for scope, approvals and final review, and `mcp_server.py` exposes the corresponding current-control tools.
- Why this is / is not agent-owned: the autonomous manager path is function-specific rather than inherited from generic model capability: the shipped skill instructs it to obtain an operational snapshot, wait on actionable events, decide scoped approvals, inspect diffs, requeue defects and accept complete work through Foreman's MCP tools. Deterministic scheduler/state transitions enforce decisions but do not own them. Human-only categories establish a distinct parent-governed mode.
- Evidence: [`README.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/README.md); [`plugins/foreman/skills/manage-foreman-agents/SKILL.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/skills/manage-foreman-agents/SKILL.md); [`plugins/foreman/skills/manage-foreman-agents/references/approval-policy.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/skills/manage-foreman-agents/references/approval-policy.md); [`plugins/foreman/src/foreman/mcp_server.py`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/src/foreman/mcp_server.py); [`plugins/foreman/src/foreman/database.py`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/src/foreman/database.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: queue claiming, dependency release, wake IPC, turn budgets and lifecycle state machines are supporting mechanisms and are not counted as autonomous S3 merely because they supervise execution. The autonomous state is grounded in the shipped manager role plus reachable current-control tools.
- Whole-system current view: `task_list`/`task_get`, goal state, actionable event cursors, approval lists, verification summaries, usage and the dashboard expose current task status, worker/model, progress, approvals, dependencies, verification and worktree details across the Foreman-managed goal.
- Current-control decision scope: create/configure/cancel tasks; set goal state; decide routine approvals; respond to worker questions; review full diffs/verification; requeue with feedback or accept; start/stop scheduler; escalate human-only risk.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | autonomous managing Claude Code/Codex session | actionable task/approval/verification/review state requires present intervention | manager reads first-party state, chooses an MCP current-control action and Foreman applies/persists it; subsequent events return the result | `README.md`; `plugins/foreman/skills/manage-foreman-agents/SKILL.md`; `plugins/foreman/src/foreman/mcp_server.py` |
| Parent (`P`) | human user | critical/human-only request or direct supervisory decision requires authority beyond routine manager scope | manager presents exact action; user explicitly confirms/rejects; `approval_decide` enforces `human_confirmed` for human-only risk and operation resumes/denies accordingly | `plugins/foreman/skills/manage-foreman-agents/references/approval-policy.md`; `plugins/foreman/src/foreman/mcp_server.py`; `plugins/foreman/src/foreman/runner.py` |

## S3* — Complementary audit

- State: C
- Function: independently test the worker-produced repository state through declared verification gates and return that complementary evidence into review/rework before acceptance.
- Disturbance / variety regulated: a worker can report completion while tests/lint/build/read-only Git checks fail, the verification environment errors, or the reviewed snapshot differs from what was actually tested.
- Decisive decision or feedback right: define the verification criteria/commands whose independently executed results will challenge the worker's ordinary completion report before current control accepts or requeues the result.
- Decision owner: Foreman does not package an autonomous auditor that chooses the audit criteria. The project/managing assistant supplies `verification_commands` (or composes an explicit reviewer phase); Foreman supplies the dedicated independent execution, fingerprinting, persistence and feedback path. Therefore the S3* path is constructor-owned.
- Supporting / enforcement mechanisms: separate verification App Server process, argv-only command execution, workspace-write sandbox, network disabled, bounded output/timeout, worktree fingerprint, durable gate/result records, `verifying` state, actionable verification-failure events, full diff view and review/requeue/accept transitions.
- Closure path: worker finishes and supplies its ordinary result summary → Foreman moves task to `verifying` → configured gates execute independently against the worker worktree and produce pass/fail/error plus tested-state fingerprint → task moves to `awaiting_review` with verification summary → manager inspects diff/evidence → failed/incomplete work can be `task_requeue`d with concrete feedback → Foreman persists `review.feedback` and injects it into the next worker prompt; accepted work closes the task.
- Boundary reachability: `verification_commands` are normal task/workflow inputs exposed by the shipped MCP surface and explicitly recommended by the manager skill; `runner.py` invokes `run_verification_gates` on every finished task that has gates before review.
- Why this is / is not agent-owned: the verification service is organizationally separate from the worker self-report and its evidence is tied to the tested worktree snapshot, but the meaningful audit judgment is configured by the manager/project rather than selected by an autonomous first-party reviewer. The manager's later accept/requeue decision is S3 response to audit evidence, not transfer of S3* audit ownership.
- Evidence: [`README.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/README.md); [`plugins/foreman/skills/manage-foreman-agents/SKILL.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/skills/manage-foreman-agents/SKILL.md); [`plugins/foreman/src/foreman/verification.py`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/src/foreman/verification.py); [`plugins/foreman/src/foreman/runner.py`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/src/foreman/runner.py); [`plugins/foreman/src/foreman/database.py`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/src/foreman/database.py); [`plugins/foreman/skills/manage-foreman-agents/references/workflow-schema.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/skills/manage-foreman-agents/references/workflow-schema.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a reviewed workflow may explicitly add a separate Claude/Codex reviewer phase, but that phase is downstream-composed rather than a mandatory autonomous auditor supplied by Foreman. Its existence reinforces constructor capability rather than changing the standalone state to `A`.
- Claim being audited: the implementation worker's claim that its finished worktree/result is ready to advance to acceptance.
- Ordinary reporting path: external worker completes its task and returns a textual result/summary to `runner.py`.
- Complementary access path: Foreman's separate verification service executes the configured repository commands directly against the finished worktree and computes a fingerprint of the tested tracked patch plus untracked files.
- Independence boundary: verification runs through a distinct Codex App Server command process after worker execution, under its own sandbox/network/output/timeout rules; gate results do not depend on the worker's self-reported test summary.
- Who acts on findings: the managing assistant receives actionable failed-verification/review state, inspects gate output/fingerprint and full diff, then accepts or requeues. Requeue feedback is persisted and returned to the subsequent worker attempt.

## S4 — Outside-and-then adaptation

- State: —
- Function: no installation-level S4 outside-and-then adaptation loop is established from the reviewed standard distribution.
- Disturbance / variety regulated: Foreman tracks durable event/usage history, provider/model availability, task outcomes and workflow versions, but the inspected paths do not establish environmental sensing with a prospective future distinction that generates an adaptation option and returns it into present capability/S3.
- Decisive decision or feedback right: not established for S4 at the declared recursion.
- Decision owner: not established.
- Supporting / enforcement mechanisms: durable SQLite history, usage summaries, live provider/model readiness checks, workflow versioning, task reconfiguration while queued and manager-authored workflow proposals.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: operational history and current provider availability can inform a manager, but persistence/monitoring/configuration are not a packaged S4 environmental adaptation conversation by themselves.
- Evidence: [`README.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/README.md); [`plugins/foreman/README.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/README.md); [`plugins/foreman/src/foreman/database.py`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/src/foreman/database.py); [`plugins/foreman/skills/manage-foreman-agents/SKILL.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/skills/manage-foreman-agents/SKILL.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a user can ask the external manager to research future options, but generic model capability or ad-hoc prompting is not a standard first-party S4 loop.

### Absence scope

- Surfaces inspected: durable event/run/usage history; provider/model selection and readiness; task reconfiguration; workflow propose/review/versioning; daemon/task monitoring; review/requeue feedback.
- Plausible first-party paths checked: reacting to model/provider availability, learning from past runs/usage, changing queued model/effort, evolving workflows and applying review feedback across attempts.
- Why no material first-party path remains: these mechanisms concern current execution, operator-authored configuration or retrospective task correction. No inspected standard path senses an external environmental change, forms a future-oriented model, generates an adaptation option from it and returns that option into Foreman's capability/current-control architecture.

## S5 — Identity / ultimate policy

- State: —
- Function: no installation-level identity/ultimate-policy closure is established from the reviewed standard distribution.
- Disturbance / variety regulated: Foreman contains strong safety policy, subscription-only authentication, exact approvals, human-only risk classes, immutable workflow review and explicit no-merge/no-deploy defaults, but these regulate operational authority and risk rather than organizational identity/ultimate policy.
- Decisive decision or feedback right: not established for an identity/ultimate-policy issue.
- Decision owner: not established.
- Supporting / enforcement mechanisms: approval policy, `human_confirmed` critical-action gate, worker policy, sandbox defaults, workflow activation review, model/provider selection and goal status.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: human authority over destructive/external actions is substantial parent governance, but generic final say over operational risk does not satisfy S5 without an identity/ultimate-policy issue and return-to-operation closure at that level.
- Evidence: [`README.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/README.md); [`plugins/foreman/skills/manage-foreman-agents/references/approval-policy.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/skills/manage-foreman-agents/references/approval-policy.md); [`plugins/foreman/skills/manage-foreman-agents/references/workflow-schema.md`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/skills/manage-foreman-agents/references/workflow-schema.md); [`plugins/foreman/src/foreman/mcp_server.py`](https://github.com/marcelsud/claude-foreman/blob/1863451a47f914a909f2b3857a73e87645ccd1fe/plugins/foreman/src/foreman/mcp_server.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: the negative result does not mean Foreman lacks policy. It keeps safety/approval/workflow policy mapped to the operational functions they actually regulate rather than promoting them to S5 from vocabulary or human authority alone.

### Absence scope

- Surfaces inspected: approval policy and human-only categories; worker policy; subscription-only identity/authentication; goal/task configuration; workflow proposal/review/activation; acceptance/merge/deploy boundaries; daemon and MCP controls.
- Plausible first-party paths checked: user confirmation of critical actions, workflow-version ratification, goal completion/cancellation, provider/model selection, no-merge/no-deploy policy and policy-edit prohibition during runs.
- Why no material first-party path remains: these decisions authorize current work, permissions, safety boundaries or reusable execution templates. No standard runtime path exposes an identity/ultimate-policy conflict, designates ultimate authority over that identity question and returns its resolution as S5 policy governing the operating organization.

## Summary

| Function | State | Assessment |
| --- | --- | --- |
| S1 | A | Foreman launches external autonomous Claude/Codex implementation workers that own task-local reasoning inside bounded worktrees. |
| S2 | — | Worktrees, dependencies and linear workflow phases provide isolation/sequencing but no complete sibling-disturbance → coordination → feedback witness is established. |
| S3 | A(P) | The shipped managing-agent skill/MCP loop owns autonomous current task/approval/review decisions, while critical actions close through explicit human parent authority. |
| S3* | C | Foreman provides independent sandboxed verification with tested-state fingerprints and corrective return through manager requeue, but the audit criteria/reviewer composition must be supplied downstream. |
| S4 | — | History, usage, provider readiness and workflow configuration do not establish external prospective adaptation closure. |
| S5 | — | Human-only risk policy and workflow review regulate operations, not identity/ultimate-policy closure. |

The resulting standalone signature is **`A — A(P) C — —`**.