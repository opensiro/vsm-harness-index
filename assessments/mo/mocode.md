---
harness_id: mocode
project_name: MoCode
repository: https://github.com/wanxunyang/mocode
review_ref: b6cb603a541e10862005c046fcdaea45a5e70f47
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# MoCode

## Review boundary

- System in focus: the distributed `mocode-ai` v1.6.7 terminal coding harness, including its model/tool loops, nested subagents, tool resource locking, background jobs and scheduled-agent operation.
- Purpose and identity: execute operator-initiated coding, investigation and automation tasks within an authorized local workspace, including delegated parallel work.
- Relevant environment: changing project files, concurrent subagent writes, tool failures, model-provider results, task cancellation, scheduled triggers and human intervention in background work.
- Standard-distribution boundary: executable TypeScript implementation under `src/agent`, `src/tools`, `src/jobs`, `src/schedule`, `src/repl`, `src/memory`, `src/bots` and `src/index.ts`; first-party CLI, TUI and documented background/daemon modes.
- Credited operating / distribution surfaces: interactive model/tool session; model-callable `task`/`sub-agent` and `arena` tools; shared read/write lock manager used by nested agent tool dispatch; shipped detached-job launcher and `/jobs` status/log/kill/approval commands; schedule daemon.
- Adjacent first-party surfaces excluded from ownership: development tests and fixture models, npm build/release automation, Pet app packaging, maintainers' own work, project GitHub review/CI, an external LLM provider's internal behavior, independently created consumer agents and user-authored skills.
- First-party modes checked: ordinary terminal loop, nested model-backed subagents, parallel `arena` candidate runs, detached `mocode run --bg` jobs, schedule-triggered jobs, parent `/jobs` control, memory reflection and bot messaging.
- Recursion level: one installed workspace-level MoCode operating organization; its nested model-backed workers and background jobs are subordinate operations, not the npm maintainer community.
- Reviewed revision: `b6cb603a541e10862005c046fcdaea45a5e70f47` (batch [#1006](https://github.com/opensiro/vsm-harness-index/issues/1006), row 10).
- License: MIT (`LICENSE`). Observation date: 2026-10-24. Profile 0.2.4; Methodology 0.3.7.

## Repository architecture

The first-party `runAgentCoreLegacy` model/tool loop runs tools through `ToolRuntime` and returns observations to the model. A model-callable `task` tool enters `spawnAgent`, which constructs a separately progressing model-backed child with its own result and conversation state. The child uses the parent runtime's tool policies and shares the workspace. Delegation can nest, with a configured depth gate and abort propagation. `ToolRuntime` wraps filesystem/process-affecting operations in a global `ResourceLockManager` that resolves canonical file identities, supports fair read/write requests, and falls back to a whole-workspace write lock for unclassifiable effects. `src/changeset/index.ts` shares the same locking subsystem. A lock is held for the tool operation, not for the entire subagent task or a different operating-system process.

In a separate operational mode, the CLI starts detached background jobs, persists job status and log records, and exposes a parent-accessible current-job list plus controls to inspect, kill and approve/deny paused jobs. The schedule daemon triggers new background jobs by cron/webhook. Model-callable `arena` runs several *candidate answers* as separate subagents and sends their returned textual summaries to one model judge for ranking. That judge does not independently inspect implementation diffs, files or test results. The memory reflector asynchronously summarizes completed sessions into cross-session facts and decisions, while messaging and bot tools exchange work messages. Neither memory persistence nor message transport alone implements prospective S4 adaptation or S5 ultimate policy.

Pinned source evidence: [loop coordinator](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/agent/run-coordinator.ts), [subagent runtime](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/agent/spawn.ts), [task tool](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/tools/builtins/task.ts), [tool execution](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/tools/tool-runtime.ts), [locks](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/tools/resource-lock.ts), [job console](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/repl/commands/jobs.ts), [job launcher](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/jobs/launch.ts), [scheduler](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/schedule/daemon.ts), [arena](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/tools/builtins/arena.ts), [memory reflection](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/memory/reflect.ts).

## Operational model

The parent and spawned child model sessions each choose task actions and revise them from tool outcomes (`S1=A`). Concurrent children may contend over the same workspace resources; the first-party lock manager attenuates a particular execution-time race (`S2=C`), but its fixed arbitration policy does not give an autonomous model the decisive coordination-policy right. Independent detached jobs can be surveyed and intervened upon from an operator job console (`S3=P`); the root coding agent's own delegation is not a separate autonomous *whole-current* S3 owner. Candidate-summary judging is not sufficiently complementary independent audit of operational claims (`S3*=—`). Historical memory and scheduled runs do not select prospectively adapted capability (`S4=—`). Task permissions and operator approval are not legitimate identity-policy deliberation (`S5=—`).

## S1 — Operations

- State: A
- Function: interpret coding/automation tasks, select tools, execute local changes and investigate errors via repeated observations.
- Disturbance / variety regulated: unfamiliar code, tool failures, incomplete work, changed files and user requests.
- Decisive decision or feedback right: the model selects tool calls, arguments, delegated subtasks, repair attempts and task completion.
- Decision owner: active parent or child LLM-backed agent for its own delegated task.
- Supporting / enforcement mechanisms: `runAgentCoreLegacy`, model runner, `ToolRuntime`, tool schemas, step/depth caps, AbortSignal and change tracking.
- Closure path: task message → model decision → built-in tool or child subagent operation → returned result/error/summary → next model-selected operation.
- Boundary reachability: `src/agent/core.ts` calls the shipped model/tool coordinator from the normal runtime; `task` invokes the same coordinator for child workers.
- Why this is / is not agent-owned: substantive operations and retries are model-selected, while dispatch and validation constrain execution without selecting a task-specific answer.
- Evidence: [agent core](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/agent/core.ts), [run coordinator](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/agent/run-coordinator.ts), [tool dispatcher](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/agent/stages/tool-dispatcher.ts), [task](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/tools/builtins/task.ts).
- Basis: structural first-party loop, corroborated by mocked Node tests.
- Confidence: high for construction, not live model task success.
- Caveats: a provider key and the human's granted tool boundary are external prerequisites.

## S2 — Coordination

- State: C
- Function: attenuate same-workspace write/read-write collisions between independently choosing nested S1 workers through a shared per-operation resource arbitration path.
- Disturbance / variety regulated: two parallel child agents issuing conflicting edits or process effects against the same canonical path/workspace at overlapping times.
- Decisive decision or feedback right: an explicit built-in arbitration relation classifies each tool's resource effect, queues conflicting lock claims and permits a blocked operation only after earlier claims release. The lock policy itself is deterministic; agents choose their local tool requests, not system-wide contention strategy.
- Decision owner: first-party lock machinery for fixed arbitration, with no separate autonomous agent currently choosing adaptive inter-agent policy. This is a specifically installed S2 coordination path awaiting autonomous ownership/composition, not `S2=A`.
- Supporting / enforcement mechanisms: canonical-path keys, `read`/`write` lock modes, fail-closed workspace lock, abort-aware fair queue and shared manager used in tool and changeset runtime.
- Closure path: two separate S1 tools request colliding resources → second execution waits → first finishes and releases → second executes on the post-first state → result/error returns to its own model's subsequent decision.
- Boundary reachability: `ToolRuntime.execute` calls `resolveResourceLockRequests` and `resourceLockManager.withLocks` around the first-party actual tool execution; nested `spawnAgent` instances inherit the same runtime context/process lock manager, rather than a test-only stand-in.
- Why this is / is not agent-owned: file/workspace collisions are a concrete inter-S1 disturbance and locks change when independent workers can act. Removing the model leaves the same lock ordering policy, so the model does not own the decisive *coordination* discretion; `C` credits the purpose-built path, not full agent-owned conflict planning.
- Distinct S1 units: parent coding agent and independently executing `task` child, or two parallel `arena`/task child agent sessions, each with a separate model history and selectable tool actions.
- Inter-S1 disturbance: parallel children share the same filesystem, and write-capable tools could overwrite or race on a path or a process-mutated workspace.
- Attenuating coordination relation: a process-global `ResourceLockManager` arbitrates conflicting declared file/workspace claims and delays incompatible requests before executing effects.
- Feedback into subsequent S1 behaviour: released claim unblocks the next tool; that worker receives its own tool result/error and can decide a follow-up action against the changed workspace.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the lock requests are derived from concrete conflicting *resource effects* and block one independent worker's action until the other completes; the mailbox and mere spawn facility are not the witness.
- Evidence: [shared lock](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/tools/resource-lock.ts), [runtime lock call](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/tools/tool-runtime.ts), [nested workers](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/agent/spawn.ts), [lock tests](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/tests/resource-lock.test.ts).
- Basis: structural first-party code and offline deterministic lock test suite.
- Confidence: medium-high for bounded within-process attenuation; no dynamic organizational negotiator evidenced.
- Caveats: locks do not persist across detached processes, hold across entire multi-step subagent workflows, prevent logical stale-read/write errors after the lock releases, or make parallel `arena` file edits safe. Those limits preclude a general S2=A claim.

## S3 — Inside-and-now control

- State: P
- Function: let the legitimate human operator supervise and intervene in the live portfolio of MoCode detached agent jobs.
- Disturbance / variety regulated: long-running or runaway jobs, work that is no longer relevant, paused decisions, stalled or unwanted background commitments.
- Decisive decision or feedback right: the operator inspects the current jobs and their outputs, kills selected jobs, and approves/denies paused execution to change the ongoing portfolio.
- Decision owner: human operator with first-party CLI/REPL current-supervision powers. The fixed scheduler and child model do not choose portfolio-wide priorities or interventions.
- Supporting / enforcement mechanisms: persistent `.mocode/jobs` records, `/jobs` and `/jobs log`, `/jobs kill`, `/jobs approve|deny`, detached-process launcher, kill-tree handler and scheduled-job daemon.
- Closure path: background jobs produce status/log/pending approval → `/jobs` displays portfolio/selected evidence → operator chooses intervention → launcher/approval bridge changes the running or paused job → its subsequent operation or termination changes.
- Boundary reachability: shipped interactive `/jobs` commands read the same first-party on-disk job records used by `mocode run --bg` and the scheduler; kill and approval handlers control those operating processes.
- Why this is / is not agent-owned: only the parent/operator exercises discretion across currently active detached jobs; the agent's own `task` delegation and static timeout gates lack an independent whole-current control view.
- Whole-system current view: `/jobs` lists the available MoCode background job portfolio and links each selected job to its status, pending approval and captured log, beyond a single model/tool turn.
- Current-control decision scope: the human decides which presently running or paused job to terminate, approve or deny; this is bounded operator portfolio intervention, not autonomous reprioritization of all available tasks.
- Evidence: [job UI and commands](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/repl/commands/jobs.ts), [job storage](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/jobs/store.ts), [background launcher](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/jobs/launch.ts), [job approval](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/jobs/approve-cli.ts), [schedule daemon](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/schedule/daemon.ts).
- Basis: structural shipped multi-job operator control mode.
- Confidence: medium-high for the bounded current-job portfolio.
- Caveats: parent management depends on the user invoking those commands and only governs accessible MoCode job records, not unrelated independent processes or an autonomous S3 agent.

## S3* — Complementary audit

- State: —
- Function: no installed independent operational-reality audit path returns adjudicated contradictory evidence to a separate current-control owner.
- Disturbance / variety regulated: inflated code/completion claims and mutually inconsistent candidate reasoning may occur; the `arena` judge ranks candidate *summaries*, not the raw operation or artifacts that could disconfirm those summaries.
- Decisive decision or feedback right: an `arena` model assigns comparative scores and a winner, but does not access the changed workspace/diff/tests independently or issue an auditable accept/reject finding to the job supervisor.
- Decision owner: `arena` judge for its one-off answer preference, parent S1 for whether to use that answer; no distinct S3* function owner.
- Supporting / enforcement mechanisms: independent text-generation histories, candidate-summary collection, one judging model call and forgiving JSON parser/fallback.
- Closure path: parallel candidate text → model ranking → winner returned as an ordinary tool outcome to original coding agent; no complementary evidence intake → finding → parent current-control correction loop.
- Why this is / is not agent-owned: a different judging prompt/LLM call is a potentially useful comparator but independence of *access to operational reality* is absent; repository unit tests are development validation, not an in-product auditor.
- Evidence: [arena candidate/judge implementation](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/tools/builtins/arena.ts), [subagent summaries](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/agent/spawn.ts), [tool registry](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/tools/index.ts).
- Basis: source-level distinction between comparative ranking and complementary audit.
- Confidence: medium-high at the pinned standard-distribution boundary.
- Caveats: a user can independently inspect or ask a new child to verify files, but such user-composed review is not a first-party accountable S3* route.

### Absence scope

- Surfaces inspected: `arena`, child agent execution and results, model-callable tool catalog, job reports and local offline test surface.
- Plausible first-party paths checked: separate `arena` judge as auditor, candidate diversity as independence, child task reviewing sibling work, tests/feedback as complementary reality access, `/jobs log` as S3*.
- Why no material first-party path remains: the shipped judge consumes the same candidate-written summaries, and no dedicated complementary artifact/evidence channel with review findings disposition into supervisory intervention is supplied.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective environment analysis → capability-option choice → adoption-and-feedback circuit is supplied.
- Disturbance / variety regulated: remembered prior failures, future scheduled work and new workspace requirements are possible, but current automation does not evaluate strategic capability alternatives against external change.
- Decisive decision or feedback right: memory reflection decides which historic facts/pitfalls to preserve; an operator chooses schedules, skills and package changes. Neither owns a prospective system-capability adaptation program.
- Decision owner: reflective model for information retention and human for explicit configuration, not an S4 strategic capability owner.
- Supporting / enforcement mechanisms: `runReflection` memory saves/updates/forgets, memory retrieval, user-authored skills, cron triggers and package update commands.
- Closure path: completed task → reflective memory → later prompt recall; or scheduled trigger → another current S1 run. Neither closes an assessed environmental forecast → new capability adoption → S3 operating change.
- Why this is / is not agent-owned: storing task knowledge improves context, but by itself does not decide future-facing organizational investment or capability change.
- Evidence: [reflection](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/memory/reflect.ts), [memory store](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/memory/store.ts), [scheduler](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/schedule/daemon.ts), [skills](https://github.com/wanxunyang/mocode/tree/b6cb603a541e10862005c046fcdaea45a5e70f47/src/skills).
- Basis: inspected plausible shipped future-oriented mechanisms.
- Confidence: medium-high within the bounded first-party product.
- Caveats: future operators or extension authors could deliberately construct an S4 process not bundled here.

### Absence scope

- Surfaces inspected: reflection prompt and retention pipeline, memory injection, package/skill controls, schedules, long-lived jobs and bot tools.
- Plausible first-party paths checked: learned pitfall as strategy, autonomous memory rewrite as adaptive capability, cron as future research, updating a package as innovation, skill loading as capability redesign.
- Why no material first-party path remains: the observed loops retain/execute existing knowledge and fixed tasks but do not choose, implement and assess prospective new operating capability in response to external variety.

## S5 — Policy and identity

- State: —
- Function: no separately identified ultimate-purpose/identity decision-and-return institution for the installed MoCode organization.
- Disturbance / variety regulated: task permission disputes, dangerous tools and operator approvals are operational risk decisions rather than charter/identity revisions.
- Decisive decision or feedback right: operator configures providers/tools, authorizes particular risky actions and can approve paused jobs; package developer supplies defaults. None resolves an ultimate-policy question with a binding constitutional return.
- Decision owner: operator for specific task permissions and maintainers for shipped source, outside an installed runtime S5 circuit.
- Supporting / enforcement mechanisms: tool policy, risk classification, `ask_human`, job approval bridge, static system prompts and runtime configuration.
- Closure path: risky operation → approval/refusal → current S1 tool continuation or stop; no organization-purpose dispute → legitimate identity decision → changed charter/policy → return to operations.
- Why this is / is not agent-owned: external user sovereignty and operational veto do not alone instantiate the Profile's S5 organizational decision right.
- Evidence: [tool policy](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/tools/policy.ts), [job approval](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/jobs/approve-cli.ts), [configuration](https://github.com/wanxunyang/mocode/blob/b6cb603a541e10862005c046fcdaea45a5e70f47/src/config/index.ts).
- Basis: runtime permission and identity path inspection.
- Confidence: medium-high for bounded absence.
- Caveats: a deployment's external company can impose legitimate policy, but its separate governance is not shipped by MoCode.

### Absence scope

- Surfaces inspected: prompt construction, user/tool permissions, job approval handling, local config, maintainer/runtime boundary and scheduler/bot setup.
- Plausible first-party paths checked: `ask_human` as parent constitution, an operator veto as S5, model instruction hierarchy as institutional legitimacy, source maintainers as runtime policy owner.
- Why no material first-party path remains: those paths regulate particular operations or supply static defaults, without a first-party ultimate identity/policy dispute and binding supervisory return.

## Distributed OSS parent arrangement

The repository/npm maintainers supply software releases, and local operators configure their own installs. No evidence ties these independent parent actors into one distributed current-control or ultimate-policy decision circuit for all MoCode users. The bounded `S3=P` observation concerns a legitimate *individual installation's* operator controlling first-party background jobs, not the upstream OSS developer organization.

## Self-hosted and non-human modes

Subagent work and scheduled/detached agent jobs may execute autonomously at S1 without constant user attention. The lock manager gives a narrow shared-process coordination construction path. Only the operator's interactive job console provides a reconstructed whole-current S3 authority; the schedule daemon's cron clock is not agentic management. Neither `arena` nor the memory reflector is silently promoted to an independent institutional S3*/S4 function.

## Recursion

Parent MoCode runtime and separately deciding children operate under one installed task/workspace boundary. A child has its own model loop but inherits root tool policy, shared workspace and parent abort; nested calls alone do not establish full VSM recursion. Detached jobs are separable operating processes monitored through the same job-record/command interface but not protected by the same in-process resource lock.

## Variety and escalation

Failures return to the requesting model for repair; contested tool effects are queued by the lock manager; exceptions/pauses can be inspected by the operator and approved, rejected or killed. Long-term memory records retrospective lessons. These paths mitigate current operational disturbance but do not supply a prospective S4 capability choice, audit S3* independence or charter-level S5 decision.

## Evidence gaps

- Frozen revision `b6cb603a541e10862005c046fcdaea45a5e70f47`; MIT and npm package v1.6.7 checked. Node workspace builds for `@mocode/protocol` and `@mocode/runtime` PASS. `npm test`: **554 tests, 553 PASS, 1 SKIP, 0 FAIL (21 suites)** after building internal workspace packages. `npm run typecheck` PASS.
- Tests use mocked/fake model providers or deterministic code fixtures. **No live model, agent benchmark or external task-success trial** was run; behavioral success, security and autonomy effectiveness are not inferred from source-only wiring.
- S2 only proves *within-process, per-tool* conflicting resource serialization, not stale-plan detection, distributed jobs' locking or model-owned policy negotiation. Its `C` classification may be revisited if a materially independent S2 coordination decision owner is found at the same SHA.
- S3 parent whole-current view is local job-status/log control; no claim that an AI manager reprioritizes a global fleet. The `arena` judge's access to answer summaries, not independent operational artifacts, is the key bounded S3* negative evidence.
