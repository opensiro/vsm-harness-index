---
harness_id: onethread
project_name: onethread
repository: https://github.com/RogyMD/onethread
review_ref: 27779473556ec490a03f07aaccca9ca3c1834316
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# onethread

## Review boundary

- System in focus: one onethread local installation across its registered repositories, owner-facing Claude Code/Codex lobby, detached background coding-agent task sessions, per-task Git worktrees, SQLite state/engine, resource-lease broker and operator confirmation interface.
- Purpose and identity: let a human use one model-facing conversation to queue and supervise multiple concurrent coding tasks without task-context collision, resource overload, false completion or unreviewed destructive publishing.
- Relevant environment: source repositories and changing task priorities/dependencies, CLI usage limits, worker crashes, expensive shared build tools, stalled human decisions, merge conflicts, branches/worktrees and owner feedback.
- Standard-distribution boundary: the shipped MIT Python 3.9+ `ot` CLI, `onethread/ops.py`, `scheduler.py`, `attention.py`, `supervisor.py`, `leases.py`, `worktrees.py`, `engine.py`, `model.py`, `finish.py`, `review.py`, prompt/lobby integration and Claude/Codex adapters. No service account or remote manager is distributed.
- Credited operating / distribution surfaces: real configured Claude Code/Codex worker in an isolated task session, model-facing lobby that invokes first-party `ot` commands, deterministic asynchronous task scheduler and class-based resource lease broker, schema-checked task results, owner approval and guarded merge/PR path.
- Adjacent first-party surfaces excluded from ownership: Claude/Codex providers' internal reasoning/security control, the user's employer/repo governance, third-party `agent-deck` usage cache, external CraftApps app creation, onethread's development roadmap and `tests/` fake workers as a production S1 agent. Public limitations on real-tool verification are retained.
- First-party modes considered: macOS standard CLI+agent use (primary supported path), user-selected Claude or Codex, 10-worker default scheduler capacity, worktree and resource lease handling, interactive owner takeover, manual review/merge and pending-work notifications. Fake-agent demo is evidence of integration logic only.
- Recursion level: one user-controlled multi-repository work queue, with each independently running coding-agent task as an operational unit. The external providers and user organization are not automatically nested first-party systems.
- Frozen revision: `27779473556ec490a03f07aaccca9ca3c1834316`, observed 2026-11-03; Profile 0.2.4 and released Methodology 0.3.7.

## Repository architecture

An owner talks to a configured Claude/Codex model inside an onethread-generated lobby whose instructions expose validated `ot` operations. The lobby model can describe task work and propose queue changes, but the worker scheduler itself is deterministic, selecting runnable tasks only after dependencies and capacity allow. Each worker uses a distinct Git worktree/agent session and returns structured `done`, `needs_input` or `failed` evidence; `supervisor.py` does not convert mere process exit into completion. A shared resource broker serializes contested high-cost command classes (for example Xcode builds), returns who owns the lease/queue position to waiting workers, reclaims dead leases and escalates long holds. A separate attention scheduler selects which blocked/review/interrupted tasks to present at a conversational pause. Review is by the human owner, with confirmation before accept/merge/cancel/push; no shipped separate model-driven corrective audit role is required. The background engine retains and recovers state across restarts, while model internals are external tools.

Pinned first-party evidence:

- [README: owner-facing orchestration, worker and review paths](https://github.com/RogyMD/onethread/blob/27779473556ec490a03f07aaccca9ca3c1834316/README.md)
- [Architecture: current lifecycle, schedulers, leases, recovery and evidence boundaries](https://github.com/RogyMD/onethread/blob/27779473556ec490a03f07aaccca9ca3c1834316/docs/ARCHITECTURE.md)
- [Public verification status and real-agent limitations](https://github.com/RogyMD/onethread/blob/27779473556ec490a03f07aaccca9ca3c1834316/docs/STATUS.md)
- [Lobby: agent role restrictions and `ot` task commands](https://github.com/RogyMD/onethread/blob/27779473556ec490a03f07aaccca9ca3c1834316/onethread/lobby.py)
- [Worker role prompts and result obligations](https://github.com/RogyMD/onethread/blob/27779473556ec490a03f07aaccca9ca3c1834316/onethread/prompts.py)
- [Supervisor: detached worker launch, schema-valid completion, crash recovery](https://github.com/RogyMD/onethread/blob/27779473556ec490a03f07aaccca9ca3c1834316/onethread/supervisor.py)
- [Scheduler: dependency/capacity/priority dispatch and preemption offer](https://github.com/RogyMD/onethread/blob/27779473556ec490a03f07aaccca9ca3c1834316/onethread/scheduler.py)
- [Lease broker: contested build tools, priorities and return message](https://github.com/RogyMD/onethread/blob/27779473556ec490a03f07aaccca9ca3c1834316/onethread/leases.py)
- [Validated task operation and manual confirmation boundary](https://github.com/RogyMD/onethread/blob/27779473556ec490a03f07aaccca9ca3c1834316/onethread/ops.py)
- [Review state based on what the owner inspected](https://github.com/RogyMD/onethread/blob/27779473556ec490a03f07aaccca9ca3c1834316/onethread/review.py)
- [Finish/merge handling with explicit human standing order](https://github.com/RogyMD/onethread/blob/27779473556ec490a03f07aaccca9ca3c1834316/onethread/finish.py)

## Operational model

The model-facing lobby interprets an owner's natural-language requests and invokes `ot` operations, but the documented controlling rule is that the model proposes while first-party code decides. A deterministic scheduler uses stored priority, dependencies, capacity and lease state to decide which tasks run. A live coding-agent worker can autonomously edit code/test inside its worktree and return a structured result. When two tasks need the same expensive command resource, the lease broker explicitly arbitrates and returns a waiting/retry instruction; this is a narrow constructor-governed S2 path. Owner review, required y/N for destructive operations and strict schema/status transitions are real control boundaries, but not an independent S3* reviewer or S5 constitutional policy authority.

## S1 — Operations

- State: A
- Function: an authorized background coding agent implements, tests and commits a repository task through its own persistent CLI session and isolated worktree.
- Disturbance / variety regulated: codebase-specific bugs, ambiguous implementation decisions, test failures, changing files and runtime tool results within the agreed task.
- Decisive decision or feedback right: choose task-specific code edits, commands/tests, correction steps and final summary/evidence, or ask for missing user input.
- Decision owner: first-party-managed worker role invoking the already configured Claude Code/Codex model-driven CLI; the model's underlying provider/internal hierarchy is not independently attributed to onethread.
- Supporting / enforcement mechanisms: `work_prompt`, per-task Git worktree, structured JSON result schema, adapter/supervisor, task session persistence, retry note and restrictive command permissions.
- Closure path: queued/approved task → supervisor starts worker with task context → model chooses code and test actions → environment feedback and commits → schema-valid `done`/`needs_input`/`failed` → review or blocked/corrective work.
- Boundary reachability: documented `ot` standard path starts authenticated Claude/Codex CLI workers via `Supervisor.start_work`, `agents/claude.py` and `agents/codex.py`; simulated tests additionally cover lifecycle but are not the sole basis.
- Why this is / is not agent-owned: Python task scheduling, Git worktrees and status parsing do not autonomously decide substantive repository edits; model-driven worker action closes the operating loop.
- Evidence: pinned `onethread/prompts.py`, `supervisor.py`, `agents/claude.py`, `agents/codex.py`, README, `docs/STATUS.md`.
- Basis: explicit + structural.
- Confidence: medium-high for shipped execution roles; some real-provider worker/merge flows are explicitly unverified one-by-one.
- Caveats: `docs/STATUS.md` warns that many tests use synthetic workers; an end-to-end real-provider run was not performed during this review.

## S2 — Coordination

- State: C
- Function: attenuate cross-worker contention for costly shared machine command resources, returning which task currently holds a class and when another may retry.
- Disturbance / variety regulated: two independent coding tasks simultaneously running Xcode builds, simulator operations or other expensive commands, overloading or corrupting each other's use of bounded local capacity.
- Decisive decision or feedback right: atomically grant one lease while a command class is at capacity, queue others by priority/time, return a concrete wait position/holder and reject/retry on timeout; reclaim dead process leases.
- Decision owner: constructor-defined `Broker` transaction policy in `onethread/leases.py`, not a dedicated model-driven S2 actor.
- Supporting / enforcement mechanisms: PATH command shims in worker environment, per-class limits, SQLite `BEGIN IMMEDIATE` lease table, process pid/start liveness, `wait_message`, timeout exit code 75 and overdue attention items.
- Closure path: worker A obtains xcode/build lease → worker B requests same limited class → broker refuses immediate execution and names holder/position → worker B waits or receives retry feedback → released/reaped lease permits later worker to proceed.
- Boundary reachability: normal workers receive a shim-prefixed PATH (`worker_env`, `install_shims`) and work prompt explicitly describes lease waiting/retry; supported command classes include Xcode/build tools, with `ot-lease heavy` for opt-in additional expensive commands.
- Why this is / is not agent-owned: contention and corrective return are real, yet grant/priority/timeout rules are prewritten transaction logic; workers cannot waive resource limits by autonomous S2 policy choice.
- Distinct S1 units: separate repository/task coding-agent worker processes, each with its own worktree and tool commands.
- Inter-S1 disturbance: simultaneous heavy command invocation against the same finite Mac build/simulator resource.
- Attenuating coordination relation: atomic priority-ordered lease claim and worker-side shim mediation.
- Feedback into subsequent S1 behaviour: the waiting worker sees current holder/queue position and retries after release or receives a temporary failure, rather than executing the colliding command concurrently.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: this is tied to a named contested *cross-worker external resource*, with one actual worker blocked and given the causal holder/retry feedback, not merely a general task queue.
- Evidence: pinned `onethread/leases.py`, `onethread/prompts.py`, `onethread/scheduler.py`, `docs/ARCHITECTURE.md` resource lease section.
- Basis: explicit + structural.
- Confidence: medium-high for documented implementation; real shell/adapters across provider environments need their own qualification.
- Caveats: shims cover declared command patterns, not every subprocess or arbitrary heavy command; a worker bypassing PATH or invoking an unclassified tool need not be protected.

## S3 — Inside-and-now control

- State: C
- Function: control present multi-repository queue commitments, task status, owner attention, safe lifecycle transitions and limited worker execution slots.
- Disturbance / variety regulated: priority clashes, dependencies not yet completed, worker crashes, capacity exhaustion, unclear review readiness, user takeover, interrupted tasks and blocked merge paths.
- Decisive decision or feedback right: determine which queued tasks are runnable by priority/dependency/resource/capacity; compare-and-set task status, detect interrupted work, hold requests for owner confirmation, and select the highest-value waiting attention offer.
- Decision owner: the onethread constructor's deterministic `scheduler`, `supervisor`, `attention`, `model` and `ops` rules, with explicit human approval for destructive and publication decisions. The lobby LLM may propose non-destructive priorities/tasks but does not itself own the binding dispatch algorithm or override owner confirmation.
- Supporting / enforcement mechanisms: SQLite WAL state, `runnable/tick`, dependency transitions, pid+start recovery, status schema, engine poll, review/finish standing orders, prompt hook and conversation attention ranking.
- Closure path: full current queue/owner/worker/lease state → scheduler and validated transition select launch/pause/notice → supervisor enforces process and task status → worker result/review/owner response returns → next tick or explicit operator action continues.
- Boundary reachability: `onethread/engine.py` runs supervisor/scheduler/attention loops; `onethread/scheduler.py` defines scheduling policy; `onethread/ops.py` enforces authoritative transition/confirmation, and `lobby.py` restricts the model to calling these tools.
- Why this is / is not agent-owned: although the owner converses with an LLM called the orchestrator, first-party instructions explicitly state **the model proposes; code decides**, and scheduling never follows unvalidated raw model output. Authoritative present-control decisions are therefore constructor C, not agent-owned S3=A.
- Whole-system current view: running/queued/blocked/review/done tasks across repositories, dependencies, priority, available worker slots, open attention, lease status, worker-process lifetime and merge/approval state.
- Current-control decision scope: queue admission/dispatch, status and interruption recovery, resource scheduling and owner notification; ultimate user mission and remote repository policy remain outside.
- Evidence: pinned `docs/ARCHITECTURE.md`, `onethread/scheduler.py`, `onethread/supervisor.py`, `onethread/ops.py`, `onethread/lobby.py`, `onethread/attention.py`.
- Basis: explicit + structural.
- Confidence: high for constructor control boundary.
- Caveats: this positive S3=C should not be read as autonomous portfolio management by a model; local owner actions and external provider limits remain determinative.

## S3* — Complementary audit

- State: —
- Function: no first-party independent, autonomously performed challenge of a worker's self-report against separate source/evidence with an agent-owned correction verdict is shown.
- Disturbance / variety regulated: mistaken claims of completion are bounded by schema validation and **human** review before acceptance; no second model reviewer is mandated.
- Decisive decision or feedback right: the owner inspects summary/diff/files or talks directly to the worker and chooses accept, changes or merge. Code checks that the owner has looked; it does not adjudicate whether the implementation is substantively correct.
- Decision owner: human owner for substantive review; constructor code for result schema and reviewed-event bookkeeping.
- Supporting / enforcement mechanisms: `review.looked/items`, `ot look`, `ot show`, manual feedback via `ot changes`, strict `schemas.py` worker-result validation, confirm dialog and merge conflict return.
- Closure path: worker JSON result → `review` state → owner selects actual artifacts and inspects → owner accepts or returns changes → worker revises; this is human review rather than first-party independent autonomous S3*.
- Why this is / is not agent-owned: a schema-valid result and review UI are not a separately commissioned model-driven auditor; no source path autonomously challenges the implementation with independent evidence before owner acceptance.
- Claim being audited: completed coding work satisfies the owner's task and deserves acceptance/merge.
- Ordinary reporting path: the implementing worker's `summary`, `tests`, `commits` and branch diff.
- Complementary access path: the owner can open files/diff or the task's own agent session, but that access remains human controlled; no standard separate reviewer agent is assigned.
- Independence boundary: human external to the model is an actual reviewer, not a credited autonomous S3* organizational agent in this harness profile.
- Who acts on findings: the owner uses `ot changes`/`ot review` and may request worker corrections; no autonomous S3* verdict loop is evidenced.
- Evidence: pinned `onethread/review.py`, `onethread/lobby.py`, `onethread/ops.py`, `onethread/supervisor.py`, README.
- Basis: bounded absence.
- Confidence: high for documented mandatory human review path.
- Caveats: a user may separately ask another Claude/Codex agent to audit a task, but such externally arranged verification is not a shipped first-party audit authority.

### Absence scope

- Surfaces inspected: worker completion schemas, supervisor result finalization, `ot look/show/review/changes`, automatic merge/finish, lobby instructions and verification-status caveats.
- Plausible first-party paths checked: schema validation as independent challenge, the owner-facing review UI as S3*, merge-conflict repair as audit and optional external peer-model review.
- Why no material first-party path remains: each closes formatting, human consent or ordinary repair; no separately commissioned autonomous reviewer with independent artifact access and corrective feedback authority is present.

## S4 — Outside-and-then intelligence

- State: —
- Function: no proven prospective environment-intelligence and future organizational capability decision loop inside the assessed onethread installation.
- Disturbance / variety regulated: repetitive owner commands, usage-window changes and new issues are visible, but are addressed as current queue control or at most a suggestion for a future local preference/task.
- Decisive decision or feedback right: the lobby model may suggest a daily tip based on recent command repetition; the owner chooses whether to save a preference, create an implementation task or disable tips; no autonomous future capability mandate is issued.
- Decision owner: external human for adopting preference or new development task, deterministic guard for one tip/day; no separate first-party S4 strategic authority established.
- Supporting / enforcement mechanisms: 30-day command journal, `tips.py`, `ot tip offered/yes/no`, `preferences.md` passed into subsequent prompts, saved queue tasks, provider usage snapshots.
- Closure path: repeated current commands → context exposes candidate improvement to lobby → owner may accept suggestion → future prompts receive preference or a new coding task; this is incremental user-approved workflow convenience, not a demonstrated external horizon/capability planning loop.
- Why this is / is not agent-owned: proposing a preference or an app idea is not sufficient for S4 without a supported environmental forecast, considered capability options and an S4 decision feeding durable changes in the work system.
- Evidence: pinned `onethread/lobby.py`, `onethread/tips.py`, `docs/ARCHITECTURE.md` tips section and README.
- Basis: bounded absence.
- Confidence: medium-high.
- Caveats: onethread may serve an external organization's S4 team or its own maintainers may develop the tool further; neither is its runtime-owned adaptation authority.

### Absence scope

- Surfaces inspected: command journal/tips, preferences, proactive notification/attention ranking, agent usage limits, owner-created tasks and architecture/design docs.
- Plausible first-party paths checked: daily repetition tip as prospective S4, suggested CraftApps project as adaptive capability creation, model task queueing as future planning and release roadmap as a runtime intelligence function.
- Why no material first-party path remains: suggestions require human acceptance and do not constitute a first-party environment-facing capability decision and return path; other paths only govern the current work queue.

## S5 — Policy and identity

- State: —
- Function: no source-supported ultimate identity/policy adjudication loop for the local onethread organization.
- Disturbance / variety regulated: destructive commands, repository permissions, owner personas, access and confirmation rules are externally specified and statically enforced, without adjudication of a constitutional identity conflict.
- Decisive decision or feedback right: only the human owner can approve accept/merge/push/cancel/pause and task takeover, regardless of what the model proposes; the model's persona changes presentation, not legitimate ultimate policy.
- Decision owner: external owner and onethread constructor safeguards, not an S5 agent or parent inside the shipped distribution.
- Supporting / enforcement mechanisms: terminal/macOS y/N, `confirm.py`, `ops.py`, no sandbox bypass, a persistent owner-only `with_you` state, cast/persona data and fixed safe merge rules.
- Closure path: human chooses authorized action and constraints → constructor validates and enforces → present work continues; there is no source path from ultimate identity dispute through legitimate policy settlement into future operation.
- Why this is / is not agent-owned: owner confirmations and a roleplay cast are real boundaries, not internally closed polity/mission choices by an organizational S5 function.
- Evidence: pinned `AGENTS.md`, `onethread/ops.py`, `onethread/confirm.py`, `onethread/lobby.py`, README.
- Basis: bounded absence.
- Confidence: high.
- Caveats: the real user may govern their own software business or research organization outside onethread; no such parent authority is borrowed.

### Absence scope

- Surfaces inspected: owner confirmations, operation policy, task takeover, cast/persona, repo access/security, prompt hook and human review.
- Plausible first-party paths checked: the human being boss as a built-in S5 return, persona setting as organizational identity policy, destructive approval as constitutional mandate and GitHub branch authority as S5.
- Why no material first-party path remains: each is an external owner action or static operational authorization gate; no specific ultimate identity/policy deliberation and authoritative return path is implemented in the local work organization.

## Distributed OSS parent arrangement

Users operate their own `ot` installations against their own local repositories and Claude/Codex accounts. The maintainer's design choices and end users' personal authorization rules do not create one shared distribution-level S5 organization or promote the external model services to internal control owners.

## Recursion

One onethread installation and its owner-facing task queue is the assessed recursion. Each task worker is an independent operational S1 role; the constructor's lease broker mediates one concrete horizontal resource conflict, and current queue control is constructor S3. Provider CLI internal agents, external human review and GitHub governance are outside the counted first-party recursion.

## Variety and escalation

Task partition and worktrees attenuate repository/file interference; individual models respond to code/test variety. Class-based leases prevent costly worker tool collision and tell waiting workers when they may retry. The background engine keeps current queue and worker status coherent through capacity/dependency dispatch, schema checks and crash recovery. Review-ready or blocked tasks are raised to the human at a natural conversational pause; the owner is the final publication/irreversible-action authority. Repetitive-command tips remain human-approved convenience proposals rather than future organizational strategy.

## Evidence gaps

- Source and first-party operational docs were inspected at the frozen SHA; no live Claude/Codex worker was launched in this assessment. `docs/STATUS.md` explicitly distinguishes 405 automated fake-agent tests from partially verified real-tool flows.
- The S2 positive result is scoped to declared costly-tool classes and PATH shims; it is not proof of universal cross-worker file conflict prevention.
- The model-facing lobby is termed an orchestrator, but current scheduling is deliberately deterministic; this analysis credits actual constructor-owned S3 decision/feedback, not the model's title.
- Human owner inspection and approval are observed authority constraints; no standard autonomous S3* audit role or S5 parent return is inferred from them.
- Repeated-pattern tips were checked as a possible S4 path; a human-approved future preference/task is not by itself an externally grounded future capability policy loop.

## Assessment summary

Proposed included at the standard local multi-task boundary: **A · C · C · — · — · —**. Model-driven task workers own substantive S1. Constructor-authored class leases attenuate concrete peer interference (S2=C) and deterministic queue/supervision/attention rules regulate current delivery (S3=C). Human review, suggestions and owner confirmations are not independent autonomous audit, prospective strategy or ultimate organizational policy.
