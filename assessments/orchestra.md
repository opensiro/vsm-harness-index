---
harness_id: orchestra
project_name: Orchestra
repository: https://github.com/DrSeedon/orchestra
review_ref: 72d48a93210c3cf12da91f7e693a4a6aae0e40f2
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

# Orchestra

## Review boundary
- System in focus: frozen first-party Orchestra multi-agent application, orchestrator and worker session manager, worktree management, model-facing MCP worker/merge controls, optional independent review receipts, acceptance oracle, quota/run guards and dashboard/Telegram entry.
- Purpose and identity: execute human-requested software goals by agent-led decomposition/delegation, preserving independent workers' context, safely merging accepted changes and observing results across long-running sessions.
- Relevant environment: user goal and approvals, managed source repositories and branches, concurrent model-driven worker sessions, test/CI feedback, independent review findings, versioned acceptance oracle and tool/usage limits.
- Standard-distribution boundary: shipped Python app, orchestrator role tools, session/pipeline manager, native OpenRouter Harness plus configured supported external CLI agent processes, worktree and merger gates ([README.md](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/README.md); [app/manager.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/manager.py); [app/mcp_stdio.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/mcp_stdio.py); [app/merge_operations.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/merge_operations.py)). Vendor model reasoning and CLI runtime internals, GitHub/Telegram service internals and user-authored portfolio strategy remain external.
- Credited operating / distribution surfaces: [app/manager.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/manager.py); [app/mcp_stdio.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/mcp_stdio.py); [app/workspace.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/workspace.py); [app/merge_operations.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/merge_operations.py); [app/acceptance.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/acceptance.py); [app/merge_test_gate.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/merge_test_gate.py); [app/work_review.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/work_review.py); [app/work_review.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/work_review.py); [app/pipeline.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/pipeline.py); [app/session.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/session.py).
- Adjacent first-party surfaces excluded from ownership: providers' native subagent internals and model policy, user's external review/approval organization, product CI unrelated to the managed merge, future capabilities described as unsupported, benchmark/tests as standalone VSM actors.
- First-party modes considered: orchestrator-managed code goal with multiple independent workers in dedicated worktrees, optional built-in model/tool execution, optional distinct-vendor code review with durable receipt, independently pinned oracle/test gate before merge, session persistence/recovery and current portfolio watchdog.
- Recursion level: one Orchestra-managed working team around an orchestrator, its separately operating worker sessions and a pre-merge review/verification path; no automatic claim about higher company governance.
- Reviewed revision: `72d48a93210c3cf12da91f7e693a4a6aae0e40f2`.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture
A model-led orchestrator is given real `spawn_worker`, `send_message`, task and `merge_worker` controls. SessionManager constructs persistent worker sessions attached to independent Git worktrees, supporting distinct registered vendor runtimes and a first-party in-process model loop. Child worker sessions can independently modify sources, exchange messages and retain state across process restarts. The first-party manager and worktree/merge engine own actual session dispatch, file ownership checks, task tracking and target integration, rather than just displaying a DAG ([app/mcp_stdio.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/mcp_stdio.py); [app/manager.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/manager.py); [app/workspace.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/workspace.py); [app/harness/loop.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/harness/loop.py)).
Merge operations freeze worker source/head and target/acceptance identity, run a scoped test subset, reject failed or inconclusive required verification, and require authenticated worker-HEAD acceptance notes for assigned task runs. A different vendor's reviewer can inspect source code and return an attributable review artifact; however, this frozen revision permits an explicit acceptance note explaining why no review was needed. Review is advisory/optional, not a mandatory cross-model merge gate. The orchestrator remains responsible for acting on the findings; the test/oracle gate is independently enforced ([app/merge_operations.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/merge_operations.py); [app/merge_test_gate.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/merge_test_gate.py); [app/acceptance.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/acceptance.py); [app/work_review.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/work_review.py); [app/mcp_stdio.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/mcp_stdio.py)).
Current-session memory, quota controls and portfolio watchdog provide operational availability and progress observations. Although they support long-lived project execution, no complete first-party **outside-and-then** strategic adaptation or ultimate organization identity-policy return loop has been established, so S4/S5 remain evidence-bounded unknown.

## Operational model
One model-led orchestrator chooses and revises worker tasks and current merge/control commitments, while separately running worker models perform the substantive operating work. The host protects source isolation and acceptance/test gates; separately requested review findings can inform, but do not automatically veto, merge. The current product isn't credited for uninstalled providers or future organizational planning functions.

## S1 — Operations

- State: A
- Function: Perform first-party hosted model-directed software-development operations in independently executing worker sessions, including file changes, investigation and bounded tool results.
- Disturbance / variety regulated: Unstructured software goals, varying repository states, tool/model failures, uncertain code correctness and active worker messages.
- Decisive decision or feedback right: Select task-specific coding and tool actions, observe results and revise work in the active model worker.
- Decision owner: Worker's configured agent model running within first-party Orchestra-managed session; provider runtime internals excluded.
- Supporting / enforcement mechanisms: Orchestra SessionManager, runtime backend adapters, built-in Harness loop, per-worker worktree/tool context, task/turn state and durable session history.
- Closure path: Orchestrator assigns work → running model worker changes/checks code → tool/file observations and results → model follow-up, output and merge proposal.
- Boundary reachability: First-party `spawn_worker` constructs an actual persistent worker and registered runtime and the session has a functional in-process model/tool loop as one supported mode.
- Why this is / is not agent-owned: Task-specific choices are made by a model actor with real files/results; session host and API framework enforce but do not replace those choices.
- Evidence: [app/mcp_stdio.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/mcp_stdio.py); [app/manager.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/manager.py); [app/harness/loop.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/harness/loop.py); [app/runtime_registry.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/runtime_registry.py); [app/session.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/session.py)
- Basis: structural
- Confidence: high
- Caveats: Static primary-source review at frozen revision, not proof of production reliability or all backends having equivalent controls.

## S2 — Coordination

- State: C
- Function: Reduce concrete inter-worker interference from concurrent code writing and unsafe integration of overlapping work.
- Distinct S1 units: Worker sessions run separate model/tool loops in isolated Git worktrees.
- Inter-S1 disturbance: Conflicting repository file edits, simultaneous ownership of the same directory, incompatible target branch changes.
- Attenuating coordination relation: Worktree isolation, controlled scope collision handling, snapshot-pinned merge workflow and conflict reporting.
- Feedback into subsequent S1 behaviour: Failed spawn/merge gates and conflict status are returned to orchestrator/worker for reassignment or revision.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: It detects and regulates actual code-edit/merge interference rather than merely carrying messages.
- Disturbance / variety regulated: Independently operating coding workers may claim the same path/scope and attempt incompatible branch integration.
- Decisive decision or feedback right: Reject conflicting ownership claims where enforced, isolate each worker in a worktree and refuse incomplete/conflicting merge under integration gates.
- Decision owner: First-party deterministic SessionManager ownership checks, worktree and merge policy; orchestrator handles subsequent changes.
- Supporting / enforcement mechanisms: Worktree-per-worker isolation, owned-directory overlap checks in manager path, git merge/conflict state, snapshot identity, merge receipts and tests.
- Closure path: Two worker scopes/branches → concrete overlap checks/isolation → reject or defer conflicting work and apply guarded merge → feed conflict/incomplete result back to orchestrator for further assignment.
- Boundary reachability: The session creation and merge paths call actual first-party scope and worktree logic, with live overlap/conflict and snapshot checks.
- Why this is / is not agent-owned: This attenuates collisions between multiple independent active coding S1s, but the interfering-work gate is deterministic, not itself an agentic coordinating decision.
- Evidence: [app/manager.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/manager.py); [app/workspace.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/workspace.py); [app/merge_operations.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/merge_operations.py); [app/mcp_stdio.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/mcp_stdio.py)
- Basis: structural
- Confidence: medium
- Caveats: Static primary-source review at frozen revision, not proof of production reliability or all backends having equivalent controls.

## S3 — Inside-and-now control

- State: A
- Function: Model-led orchestrator directs present worker commitments and merges, using active task/session status, collaboration messages and completion evidence.
- Whole-system current view: bounded orchestrator's current registered worker/task/portfolio status, not all provider/company operating state.
- Current-control decision scope: ongoing worker assignment, work routing, review/merge decisions and corrective session steering.
- Disturbance / variety regulated: Changing task priorities, parallel worker statuses, partial results, stalled sessions, new code dependencies and merge readiness.
- Decisive decision or feedback right: Select and update work assignments, choose models, launch/steer workers, solicit review, initiate merge or defer based on observed state.
- Decision owner: First-party orchestrator model role via shipped MCP tools, with deterministic service enforcing accepted limits.
- Supporting / enforcement mechanisms: Spawn/worker-list/send-message/merge MCP tools, session registry, task status, quota admission, watchdog and result/merge receipts.
- Closure path: Accepted user goal → orchestrator model creates/delegates current tasks → worker progress/messages and merge/verifier feedback → orchestrator reschedules/steers/reviews/merges tasks.
- Boundary reachability: `spawn_worker` and `merge_worker` are real role-facing tools, not placeholder planning stages; separate workers persist and message each other across turns.
- Why this is / is not agent-owned: The model chooses consequential team commitments based on workers and primary-source evidence; server enforces hard boundaries.
- Evidence: [app/mcp_stdio.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/mcp_stdio.py); [app/manager.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/manager.py); [app/task_runtime.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/task_runtime.py); [app/message_deliveries.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/message_deliveries.py); [app/quota_gate.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/quota_gate.py)
- Basis: explicit + structural
- Confidence: high
- Caveats: Static primary-source review at frozen revision, not proof of production reliability or all backends having equivalent controls.

## S3* — Complementary audit

- State: A
- Function: Complement production claims with independently sourced actual code/snapshot review and enforced artifact acceptance evidence before merge.
- Claim being audited: A particular worker's source diff correctly completes an accepted task.
- Ordinary reporting path: Worker's own chat/Task progress and reported code changes.
- Complementary access path: Cross-model reviewer accesses concrete source/changes and returns a distinct review artifact; separately, the pinned merge snapshot and first-party test/oracle capture actual execution outcomes.
- Independence boundary: Distinct reviewer model/vendor and version-pinned source artifacts, though organizational role is within same product.
- Who acts on findings: The orchestrator receives optional review findings and may request repair; the deterministic test/oracle gate may separately stop a merge.
- Disturbance / variety regulated: Worker claims task completion but output is defective, stale, inadequately reviewed or fails acceptance tests.
- Decisive decision or feedback right: When invoked, inspect actual code in a distinct model/vendor, record a durable reviewer receipt, and return findings for orchestrator acceptance or repair. Mandatory merge enforcement of a cross-model review is not established.
- Decision owner: Separate reviewer model for substantive code judgment, backed by first-party snapshot/receipt/test gates, not the producing worker alone.
- Supporting / enforcement mechanisms: Optional cross-vendor `codex_review` and durable review receipts, separately frozen merge worker snapshot, pinned acceptance oracle, mapped independent test execution, and explicit acceptor note.
- Closure path: Worker source → optionally invoked different-vendor reviewer → review artifact/receipt and findings returned to orchestrator; independently the required test/oracle can block merge, while the acceptor may document why no separate review was commissioned.
- Boundary reachability: First-party `merge_worker` checks accepted source identity, task assignment/acceptance note and test/oracle; separate supported `codex_review` invokes another vendor CLI on real sources. There is no source-backed unconditional cross-model review coverage gate at this frozen SHA.
- Why this is / is not agent-owned: When explicitly invoked, the reviewer observes actual source separately and issues review evidence to the orchestrator; corrective consequences depend on orchestrator/acceptor decisions rather than mandatory independent-review enforcement.
- Evidence: [app/mcp_stdio.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/mcp_stdio.py); [app/merge_operations.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/merge_operations.py); [app/work_review.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/work_review.py); [app/acceptance.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/acceptance.py); [app/merge_test_gate.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/merge_test_gate.py); [app/work_review.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/work_review.py)
- Basis: explicit + structural
- Confidence: high
- Caveats: Static primary-source review at frozen revision, not proof of production reliability or all backends having equivalent controls.

## S4 — Outside-and-then intelligence

- State: ?
- Function: Persistent knowledge, portfolio health monitoring and model tool flexibility may improve future work, but a distinct external future-scanning/capability adaptation controller is not demonstrated.
- External distinction: Current repo/project diagnostics and user instructions do not show independent foresight scanning.
- Future / prospective distinction: Session continuation and long-term notes mostly affect current/future task context, not capability redesign.
- Adaptation option generated: No traced first-party approved future organizational-capability alternative.
- Path back into current capability / S3: Model routing can change a current worker; systemic future-option adoption remains unresolved.
- Disturbance / variety regulated: Long-term product opportunity/risk and potential adaptations in tools, organizational topology or capability beyond current task work.
- Decisive decision or feedback right: Unknown future-adaptation choice; orchestrator can change near-term tactics and worker models but no horizon-driven capability adoption loop traced.
- Decision owner: Unresolved between human owner, ordinary orchestrator and operational watchdog.
- Supporting / enforcement mechanisms: Knowledge-base topic files, portfolio watchdog, usage analytics, model routing, task persistence and system instructions.
- Closure path: Current operating information persists and may influence later tasks, but an external opportunity → future capability option → adopted change returning into operations is not established.
- Boundary reachability: undefined
- Why this is / is not agent-owned: Long session duration, memory and choosing a worker model for a current task alone are not outside-and-then intelligence.
- Evidence: [app/portfolio_watchdog.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/portfolio_watchdog.py); [app/native_memory.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/native_memory.py); [app/prompting.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/prompting.py); [README.md](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/README.md)
- Basis: unknown
- Confidence: low
- Caveats: Static primary-source review at frozen revision, not proof of production reliability or all backends having equivalent controls.

## S5 — Policy and identity

- State: ?
- Function: Human goal/task approval, agent roles and safety constraints exist, but a full ultimate organizational purpose/identity policy decision and feedback loop is not established.
- Identity / ultimate-policy issue: Authority to define and revise the purpose of the whole Orchestra-managed organization.
- Ultimate authority in each claimed mode: Human goal/approval and static app policy; no source-grounded autonomous or parent-governed full S5 cycle.
- Return-to-operation path: Approved tasks reach workers, but identity-level policy feedback is not demonstrated.
- Disturbance / variety regulated: Changes of fundamental purpose, trust/authority and acceptable autonomous agent behavior.
- Decisive decision or feedback right: Human approves goals and sets permissions; exact policy boundaries govern spawning/merging but no overall ultimate-purpose revision right with return is reconstructed.
- Decision owner: Human/operator for stated mission and risk gates; no qualifying ultimate first-party S5 loop established.
- Supporting / enforcement mechanisms: Orchestrator role instructions, user approval in chat, model/role access, quota and merge policy, project KB.
- Closure path: User direction constrains task execution → hard gates/approval; overall purpose/policy reform and return into all operations unproven.
- Boundary reachability: undefined
- Why this is / is not agent-owned: Human authorization of individual tasks and a role prompt do not alone constitute complete ultimate identity/policy governance.
- Evidence: [AGENTS.md](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/AGENTS.md); [app/mcp_stdio.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/mcp_stdio.py); [app/quota_gate.py](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/app/quota_gate.py); [README.md](https://github.com/DrSeedon/orchestra/blob/72d48a93210c3cf12da91f7e693a4a6aae0e40f2/README.md)
- Basis: unknown
- Confidence: low
- Caveats: Static primary-source review at frozen revision, not proof of production reliability or all backends having equivalent controls.

## Recursion

Orchestra hosts multiple separately operating model-led worker S1 units. First-party source isolation/merge control attenuates current interference (S2=C); model-led orchestrator directs current worker and merge commitments (S3=A). Independently sourced cross-model review and snapshot/acceptance gates return actual correction/stop signals (S3*=A). Neither long-lived agent memory nor human task approval automatically upgrades S4/S5 beyond unknown.

## Variety and escalation

Worker/tool uncertainty feeds agent execution and the team manager. Conflicting ownership and incompatible diffs are blocked at spawn/merge, while quota/readiness gates and snapshot-pinned independent audit protect acceptance; review findings and verification failures can provoke a new operation or human handoff.

## Evidence gaps

No primary-source loop was established for prospective environmental scanning, future organizational capability redesign and adopted returns (S4). Likewise no ultimate system mission/policy change-and-return loop is established (S5). The README itself documents non-enforced role restrictions and other gaps; no unshipped capability is credited. Test and release claims are not independently executed against provider services.
