---
harness_id: zero
project_name: Zero
repository: https://github.com/Gitlawb/zero
review_ref: 99721c762f37cd43ac511007a5f51d1846df959e
reviewed_at: 2026-10-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Zero

## Review boundary

- System in focus: the first-party installed Zero Go coding agent, including its CLI/TUI/exec agent loop, built-in specialist Task runtime, and optional on-demand in-process swarm/team orchestration.
- Purpose and identity: autonomously inspect/edit a local codebase, run tools and tests, optionally divide current coding work among built-in subordinate agent contexts, collect results and revise work.
- Relevant environment: local workspace and shell, configured provider/model endpoint, durable sessions, sandbox and human tool permissions, opt-in specialists and swarm members.
- Standard-distribution boundary: native shipped Zero CLI/TUI/exec with first-party built-in worker/explorer/code-review specialists and available swarm_* tools, not externally composed workflows or development CI.
- Credited operating / distribution surfaces: [README.md](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/README.md); [HOW_ZERO_WORKS.md](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/docs/HOW_ZERO_WORKS.md); [SPECIALISTS.md](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/docs/SPECIALISTS.md); [loop.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/agent/loop.go); [selfcorrect.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/agent/selfcorrect.go); [task_tool.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/task_tool.go); [output_tool.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/output_tool.go); [builtin.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/builtin.go); [exec.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/exec.go); [tools.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/tools.go); [team.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/team.go); [coordinator.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/coordinator.go); [lifecycle.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/lifecycle.go); [definition.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/definition.go); [scheduler.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/scheduler.go); [app.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/cli/app.go).
- Adjacent first-party surfaces excluded from ownership: repository CI and action templates, release tooling, benchmark/eval harnesses, sample workflows, external provider services/MCP/skills/plugins, developer-authored scripts and human GitHub PR approval. Their activity cannot supply decisive owners to the native agent.
- First-party operating / deployment modes considered: ordinary interactive/headless coding turn; shipped Task specialist delegation; opt-in concurrent swarm spawn/send/status/collect/handoff/schedule within a standard session. Optional code-review specialist is credited only when explicitly invoked and its returned findings affect subsequent task control; no default always-on audit is claimed.
- Recursion level: top-level coding agent over subordinate independently model-running specialist/swarm S1 work units when opted in; in a simple session only one coding S1. CLI process/queued job machinery is not automatically another S1.
- Reviewed revision: `99721c762f37cd43ac511007a5f51d1846df959e`.
- Observation date: 2026-10-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/README.md) documents executable Zero coding with edit, shell, terminal, browser and local durable sessions. [loop.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/agent/loop.go) implements model-tool turn execution and result feedback; [selfcorrect.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/agent/selfcorrect.go) optionally runs post-edit verification with correction feedback. [SPECIALISTS.md](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/docs/SPECIALISTS.md) and [builtin.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/builtin.go) document and implement shipped `worker` (read/edit/execute), `explorer` and independent read-only `code-review` specialists. The [task_tool.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/task_tool.go) launcher creates a separate specialist execution context; [output_tool.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/output_tool.go) returns background child results to the parent.

[app.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/cli/app.go) registers specialist tools and instantiates a first-party swarm with [tools.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/tools.go) in normal supported agent sessions, except excluded special execution modes. [lifecycle.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/lifecycle.go) admits running members or queues them, and [team.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/team.go) limits concurrently active child workers per team. [coordinator.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/coordinator.go) tracks current member/task lifecycle and results. The parent agent can inspect a whole team, send messages and hand active commitments to a successor, with [lifecycle.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/lifecycle.go) enforcing source-stop-before-successor-start to avoid simultaneous ownership of transferred work. These are executable standard-distribution mechanisms, not solely an example or a benchmark.

## Operational model

The root model selects engineering steps and invokes the tool loop. For delegated work, it can choose worker roles/briefings and launch simultaneous subordinate coding S1s, observe status and returned results, communicate follow-up, and reassign unfinished work via a protected handoff. Runtime policies and team capacity enforce constraints; the root's model decisions and returned results remain distinct from those deterministic mechanisms. A separate built-in reviewer can be invoked as a direct-source read-only audit subtask, returning findings for root/worker corrective work.

## S1 — Operations

- State: A
- Function: take uncertain coding actions (repository inspection, file edits, command/test execution) in response to task goals and feedback.
- Disturbance / variety regulated: unknown codebase state, test failures, tool errors, partial patching and user-request changes.
- Decisive decision or feedback right: model chooses code actions, tool arguments, continuation/correction after observed results.
- Decision owner: Zero's coding agent model (and delegated specialist model in its own worker context).
- Supporting / enforcement mechanisms: Go turn engine, command and file tools, durable session context, sandbox/permission gate, optional post-edit verifier.
- Closure path: model tool call → first-party local read/edit/shell → tool/verification outcome re-enters turn history → model chooses repair, delegation or final response.
- Boundary reachability: normal `zero` / `zero exec` supported pathways, not only test fixtures.
- Why this is / is not agent-owned: without the current model's discretionary action selection, tool dispatch and verification only implement bounded mechanisms.
- Evidence: [README.md](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/README.md); [loop.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/agent/loop.go); [selfcorrect.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/agent/selfcorrect.go); [task_tool.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/task_tool.go); [exec.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/exec.go)
- Basis: explicit and structural
- Confidence: high for wired source path, no credentialed upstream provider run
- Caveats: shell subprocesses and deterministic verification are not additional autonomous S1s.

## S2 — Coordination

- State: C
- Distinct S1 units: simultaneously model-running `teammate`/`subagent` coding members launched via `swarm_spawn`, each executing its own delegated task; a predecessor/successor pair is distinct S1 execution ownership when `swarm_handoff` transfers work.
- Inter-S1 disturbance: concurrent members contend for a shared bounded set of team execution slots, and predecessor/successor actors can otherwise overlap execution of the same in-flight task during ownership transfer.
- Attenuating coordination relation: the team's maximum-concurrency cap queues excess S1s and the handoff source-stop execution barrier forbids the successor from executing until the incumbent exits; failed/timed-out handoffs fail closed.
- Feedback into subsequent S1 behaviour: pending tasks start only as slots free, and the successor receives the handoff briefing only after the source is stopped; coordinator status/results inform the manager's subsequent allocations.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: this is interference-specific control of competing independently model-running S1s for a shared capacity and exclusive ownership of a continuing task; mere mailbox messages or task launches are not the positive witness.
- Function: attenuate inter-S1 competition for a bounded team's concurrent execution slots and conflicting simultaneous ownership of work transferred between model-running workers.
- Disturbance / variety regulated: oversubscribed independent member launches, duplicate/conflicting execution by old and successor agent on one unfinished delegated task, late/invalid lifecycle transitions.
- Decisive decision or feedback right: team allocator admits at most bounded concurrent S1 member runs; handoff transition refuses successor execution until predecessor's side-effect execution barrier has closed.
- Decision owner: deterministic first-party swarm coordinator/team lifecycle (C), not an autonomous S2 model.
- Supporting / enforcement mechanisms: FIFO excess-member queue, per-member lifecycle status, reserved handoff successor, cancellation and fail-closed timeout, mutex/condition synchronization.
- Closure path: one S1 member requests spawn/handoff → team capacity or single-owner conflict is detected/enforced → member launch is deferred or incumbent stopped → queued/new agent executes only when legal → task status/results feed root and subsequent member assignments.
- Boundary reachability: [app.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/cli/app.go) ships [tools.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/tools.go) in regular supported agent sessions; [lifecycle.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/lifecycle.go) / [team.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/team.go) implement coordination in the invoked swarm mode.
- Why this is / is not agent-owned: model decides which team actions to request, but capacity and conflicting dual-ownership attenuation remain hard-coded if that model is removed.
- Evidence: [tools.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/tools.go); [team.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/team.go); [lifecycle.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/lifecycle.go); [coordinator.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/coordinator.go); [app.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/cli/app.go)
- Basis: structural
- Confidence: medium-high for resource/ownership coordination, not a general claim about detecting same-file edits across different tasks
- Caveats: no general git-write/file-overlap conflict detector is credited. S2 claim is limited to specific execution-capacity and task-handoff interference, not universal multi-agent coordination.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: `swarm_status` exposes per-task team, agent, current pending/running/failed/done/handoff state and aggregate counts, while `swarm_collect` returns all task results for the active swarm and mailbox messages provide targeted current feedback.
- Current-control decision scope: the root model can change the present multi-S1 work allocation and follow-up by choosing additional spawns, targeted member messages, handoff to another agent type, or new work after collecting live results; this is distinct from the scheduler's fixed capacity policy.
- Function: decide and revise current allocation of team coding commitments based on whole-active-task status and outcomes.
- Disturbance / variety regulated: worker failures, incomplete subtasks, uneven progress or current team capacity, requests requiring reassignment.
- Decisive decision or feedback right: root model chooses spawned tasks, specialist roles, message/follow-up and live handoff based on team-wide status and returned outputs.
- Decision owner: root model operating in optional first-party swarm mode, not the deterministic coordinator.
- Supporting / enforcement mechanisms: coordinator task registry and statuses, `swarm_status`, `swarm_collect`, `swarm_send`, `swarm_handoff`, policy inheritance and terminal status enforcement.
- Closure path: root launches complementary S1 tasks → [coordinator.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/coordinator.go) reports live roster/results → root selects current reassignment/message or correction → [tools.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/tools.go) and [lifecycle.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/lifecycle.go) apply it to active member work → changed execution/status feeds next decisions.
- Boundary reachability: real tool registration in [app.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/cli/app.go), available in shipped regular agent mode and not dependent on a custom third-party orchestrator.
- Why this is / is not agent-owned: hard-coded runtime records/executes tasks, but cannot decide the mission-relevant task split or discretionary correction after results without the root model.
- Evidence: [app.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/cli/app.go); [tools.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/tools.go); [coordinator.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/coordinator.go); [lifecycle.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/lifecycle.go); [definition.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/definition.go)
- Basis: structural
- Confidence: medium-high for optional shipped mode
- Caveats: organizational horizon is the active swarm/team of one Zero session, not a cross-repository fleet or global OpenSiro organization.

## S3* — Complementary audit

- State: A
- Claim being audited: an implementer S1's claim that its current code changes are correct, safe, and free of regressions/missing tests.
- Ordinary reporting path: worker sends completion status and its own run/test output to root through a Task result or swarm coordinator; the implementing worker's self-report is not the complementary witness.
- Complementary access path: the separately prompted built-in read-only `code-review` specialist has `read_file`/`grep`/`glob`/`list_directory` access to actual workspace code/diffs and forms its own defect review independent of the implementer's summary.
- Independence boundary: dedicated model-run specialist with different reviewer system prompt and read-only tool category, invoked as an independent task context rather than reusing the implementer's own self-correction result.
- Who acts on findings: the top-level S3 model can consume the returned reviewer findings and direct a worker to repair and optionally review again; no mandatory automatic blocking gate or independent human GitHub approval is claimed.
- Function: independently inspect a coding worker's artifact for correctness defects, regressions, unsafe behavior or missing tests and return a separate diagnostic judgment to current-control decision making.
- Disturbance / variety regulated: false or incomplete completion claims and regressions that may not be detected by the implementing S1.
- Decisive decision or feedback right: first-party read-only `code-review` specialist model independently chooses which direct code/diff evidence to inspect and what actionable problems to report; root then chooses whether to correct/reassign.
- Decision owner: separate specialist model in explicit review mode; corrective S3 follow-up remains under root's discretionary control.
- Supporting / enforcement mechanisms: built-in review system prompt/read-only tool limit, Task subprocess/session, TaskOutput for asynchronous result, original source and diff read tools.
- Closure path: root requests code review → separate model accesses current code/diff from the workspace → reports independent findings → Task/TaskOutput returns to root → root can ask an implementer to repair and re-review.
- Boundary reachability: [builtin.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/builtin.go) ships `code-review`; [task_tool.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/task_tool.go) dispatches it in supported main session; [output_tool.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/output_tool.go) provides a result-return path, without external CI or human reviewer.
- Why this is / is not agent-owned: deterministic checks do not produce the separate semantic defect judgment; it is made by a model in a distinct read-only review context.
- Evidence: [builtin.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/builtin.go); [task_tool.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/task_tool.go); [output_tool.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/output_tool.go); [SPECIALISTS.md](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/docs/SPECIALISTS.md); [system_prompt.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/agent/system_prompt.go); [app.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/cli/app.go)
- Basis: explicit and structural
- Confidence: medium; optional invoked path, without measured production reviewer effectiveness
- Caveats: not a mandatory final merge gate; parent can ignore findings and routine `zero verify`/self-correct is not credited as S3*. This is assessment of reachable independent audit ownership, not benchmark-proven quality.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party future-oriented organizational capacity adaptation cycle is established.
- Disturbance / variety regulated: prospective changes in provider availability, future workflows and evolving capability requirements.
- Decisive decision or feedback right: no active owner shown deciding future organizational change and returning an applied capability revision.
- Decision owner: user/developer config chooses external providers, plugins and specialist manifests; current agent handles current coding task.
- Supporting / enforcement mechanisms: model/provider selection, durable sessions, plan/context compaction, optional specialist generation, schedules and tools.
- Closure path: current task tools/config are selected or generated, but no independently closed outside-and-then sensing → strategic adaptation → incorporated future capability loop at this recursion.
- Why this is / is not agent-owned: task-local plans, stored prompts and project-defined specialists do not by themselves establish S4.
- Evidence: [README.md](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/README.md); [SPECIALISTS.md](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/docs/SPECIALISTS.md); [system_prompt.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/agent/system_prompt.go); [app.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/cli/app.go); [scheduler.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/scheduler.go); [loop.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/agent/loop.go)
- Basis: explicit and structural
- Confidence: medium
- Caveats: the packaged `GenerateSpecialist` can write a task-specific manifest; review found no separate long-horizon environment-to-capacity adaptation closure.

### Absence scope

- Surfaces inspected: standard provider/agent configuration, specialist creation, team scheduler, context/session persistence and main turn loop
- Plausible first-party paths checked: prospective environmental intelligence, discretionary future reconfiguration/adaptation decision and incorporated change to ongoing organization
- Why no material first-party path remains: supported controls are present-run/workspace choices or task execution machinery without integrated prospective adaptation and returned organizational capability change.

## S5 — Policy and identity

- State: —
- Function: no in-boundary ultimate-purpose/identity policy authority is established for the coding-agent organization.
- Disturbance / variety regulated: conflicts over constitutional purpose or organizational identity beyond per-command permission.
- Decisive decision or feedback right: no first-party owner able to set and bind the organization's ultimate mission/identity.
- Decision owner: human/operator config sets task purpose and permission rules; main agent selects operations within those boundaries.
- Supporting / enforcement mechanisms: tool permission modes, sandbox, specialist capability restrictions, team policy inheritance and external user approvals.
- Closure path: action is approved/denied by configured permissions, but no organizational identity conflict is escalated to an S5 owner and returned as a binding mission/policy change.
- Why this is / is not agent-owned: inherited permission/role policies constrain tool execution and cannot decide ultimate organizational purpose.
- Evidence: [README.md](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/README.md); [SPECIALISTS.md](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/docs/SPECIALISTS.md); [task_tool.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/specialist/task_tool.go); [team.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/swarm/team.go); [app.go](https://github.com/Gitlawb/zero/blob/99721c762f37cd43ac511007a5f51d1846df959e/internal/cli/app.go)
- Basis: structural
- Confidence: medium-high in declared distribution
- Caveats: maintainers' policies and GitHub governance are outside the runtime under review.

### Absence scope

- Surfaces inspected: permission and sandbox boundaries, agent/team role configuration, specialist manifests and developer governance/CI
- Plausible first-party paths checked: constitutional/purpose dispute → legitimate parent policy authority → binding enacted change in operating identity
- Why no material first-party path remains: inspected first-party mechanisms enforce local tool safety and task assignments only; authority over mission/identity remains external to the shipped Zero organization.

## Recursion

At simple mode the main Zero coding agent is an S1. In opt-in Task/swarm mode, each independent model-running specialist/member is an operating S1 subordinate to a root manager at the next local recursion level. Coordinator, queue and policy inheritance form technical support/control for that level; they do not by themselves become agents. The assessed boundary excludes the operator's broader engineering organization.

## Variety and escalation

Local code/test results enter the agent loop and may drive repair. Concurrent worker resource contention is held by a capacity queue and task handoff single-owner barrier; team results/status return to the root for live reprioritization, and optional code-review findings can inform another correction cycle. Permission-denied effects return to the task controller or human; this is not ultimate S5 policy escalation. No evidence establishes a longer-term adaptation portfolio.

## Evidence gaps

This is a source-first review of the exact frozen revision, not a credentialed production-model task or empirical test of reviewer fidelity. Optional swarm and explicit reviewer paths are evaluated as *reachable modes* rather than mandatory default workflows. The claimed S2 witness is strictly team-capacity interference and serial ownership during a transferred task, not detection of same-file edits among arbitrary concurrent workers. No positive S4/S5 is inferred from general extensibility, schedules or permission metadata.
