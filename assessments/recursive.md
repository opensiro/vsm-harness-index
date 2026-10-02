---
harness_id: recursive
project_name: Recursive
repository: https://github.com/jeffkit/recursive
review_ref: d693ff98ae9d3f47896994c55b2d8f494b4cca3d
reviewed_at: 2026-10-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-02
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Recursive

## Review boundary

- System in focus: one first-party Recursive multi-agent coding organization at frozen revision `d693ff98ae9d3f47896994c55b2d8f494b4cca3d`, centered on a model-backed coordinator and the specialist `AgentRuntime` workers it creates through the shipped `agent` tool, plus shared task/message state, coordinator control tools and the built-in verification role where they participate in the same coding objective.
- Purpose and identity: complete software-engineering goals by decomposing work into specialist operational cells, regulating when those cells execute concurrently or sequentially, supervising current worker commitments, independently challenging implementation claims, and synthesizing the resulting work into one project-level outcome.
- Relevant environment: user coding goal; target workspace/repository and tests; model-provider responses; native coding/search/shell tools; optional MCP services; worker/task state; project `AGENTS.md`/`CLAUDE.md`; runtime budgets/cancellation; operator configuration.
- Standard-distribution boundary: the Rust kernel/runtime, default-enabled sub-agent capability, `AgentTool`, `AgentPool`, shared memory/message bus, worker/task registries, coordinator prompt and supported `coordinator-mode` build/runtime mode, built-in agent definitions, CLI/HTTP/TUI entry points and ordinary first-party tools are inside. External model providers, MCP servers, host/container internals, FlowX and consumer applications are dependencies rather than Recursive organizational owners.
- Credited operating / distribution surfaces: `README.md`; `src/run_core.rs`; `src/runtime.rs`; `src/multi.rs`; `src/coordinator.rs`; `src/tools/agent.rs`; `src/tools/send_message.rs`; `src/tools/task_list.rs`; `src/tools/task_output.rs`; `src/tools/task_stop.rs`; `src/tasks.rs`; `.recursive/agents/verification.md`; `docs/architecture/tools/multi-agent.md`; `docs/architecture/tools/task-tools.md`.
- Adjacent first-party surfaces excluded from ownership: repository tests/CI/release governance; `.dev/goals`, journals, observations and `.dev/flows` self-improvement tooling; `bench`/development validation material; cloud-runtime storage paths documented as not yet wired in HTTP mode; external FlowX orchestration; provider/MCP internals.
- First-party operating / deployment modes considered: normal CLI/HTTP/TUI coding sessions with sub-agents enabled by default; single/parallel/sequential/background worker modes; cross-turn worker continuation; supported `coordinator-mode` cargo feature plus `RECURSIVE_COORDINATOR_MODE=1`; fresh verification-worker use; single-agent operation; loop/self-scheduling mode.
- Recursion level: one project/task organization is the system in focus. Specialist model-backed worker runtimes are S1 operational cells. The model-backed coordinator is assessed at the metasystem level when it regulates those workers. Background shell jobs and individual tool calls remain actions/resources of an S1, not additional S1 units.
- Reviewed revision: `d693ff98ae9d3f47896994c55b2d8f494b4cca3d`.
- Observation date: 2026-10-02.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Recursive is a Rust coding-agent platform built around a ReAct kernel and a stateful `AgentRuntime`. A model receives project/task context and registered tool schemas, chooses coding/search/shell/tool actions, receives execution results and continues until completion or a bounded finish condition. The same runtime is used by spawned workers, so workers are substantive model/tool S1 cells rather than static workflow labels.

Sub-agents are enabled by default. The first-party `agent` tool accepts a manifest of specialist workers and can run them as a single worker, concurrently in `parallel`, in ordered `sequential` mode, or as retained background workers. Each worker gets its own runtime/transcript and session-isolated tool state. Shared memory, mailboxes, a task registry and continuation channels let the parent/coordinator observe or communicate with active workers.

The shipped coordinator guidance makes a function-specific coordination distinction: independent read-only work may run in parallel, while write-heavy work should run sequentially unless the coordinator is confident that workers touch different files. This directly addresses a concrete shared-workspace collision mode rather than treating parallelism or messaging alone as S2.

A supported `coordinator-mode` cargo feature, combined with `RECURSIVE_COORDINATOR_MODE=1`, turns the top-level model into a restricted coordinator: direct `Edit`, `Write` and `Bash` are removed, while worker dispatch, task listing/output, task cancellation/update, messaging and read-only inspection remain available. The coordinator can therefore obtain current worker/task state and alter current commitments without doing the underlying coding work itself.

Recursive also ships a first-party `verification` agent definition. The coordinator guidance explicitly says that verifying another worker's code should use a fresh worker rather than continue the implementer's context. The verification specialist is adversarial, receives the original task/files/approach, reads the workspace and executes existing build/test/lint commands under a read-only role, and returns an explicit PASS/FAIL/PARTIAL verdict. Its result returns to the coordinator, which can continue, replace or redirect implementation work.

The repository contains a substantial self-improvement workflow under `.dev/flows`, but `Cargo.toml` excludes `.dev/` from the published crate and the workflow documentation explicitly states that external FlowX orchestrates the loop while the Recursive binary is only an executor. Loop mode, scheduled wakeups, provider-catalog refresh, memory and web search extend present operation but do not by themselves close an externally and prospectively oriented S4 adaptation loop.

## Operational model

For a multi-agent coding objective, the top-level model analyses the task and chooses what specialist workers are needed. It writes self-contained worker briefs, decides whether work can run in parallel or must be sequential, may retain a worker for background continuation, observes returned results/task state, sends follow-up messages or stops work, and synthesizes the project-level answer. The decisive choices are model-backed; deterministic registries, cancellation tokens, deadlines and tool restrictions enforce those choices.

The same coordinator may create a fresh verification worker after implementation. That verifier has a new context and different role/access path from the implementer, directly probes repository/test reality, and returns findings to current control. This is treated separately from ordinary worker self-testing or the goal evaluator, which only judges the transcript and is not complementary S3* access.

## S1 — Operations

- State: A
- Function: perform bounded software-engineering work on the target workspace through open-ended model/tool interaction.
- Disturbance / variety regulated: repository structure, incomplete requirements, implementation choices, code/test/tool failures, shell/search results and changing workspace state encountered while completing a delegated coding subtask.
- Decisive decision or feedback right: choose what code/evidence to inspect, which allowed tools/actions to invoke, what implementation changes to make, how to react to returned results and when the delegated outcome is ready.
- Decision owner: each model-backed Recursive worker `AgentRuntime` (and the top-level model in single-agent mode).
- Supporting / enforcement mechanisms: ReAct kernel, tool registry, workspace/path restrictions, permissions, transcripts, step/wall budgets, cancellation, context management, provider adapters and worker-specific runtime/tool state.
- Closure path: coordinator/user supplies a goal → worker runtime builds model context/tools → model chooses an action → Recursive executes or rejects it → environment/tool result returns to the same worker → worker revises its next action until a terminal result.
- Boundary reachability: normal Recursive CLI/HTTP/TUI sessions instantiate the first-party runtime directly, and sub-agent support is enabled by default; no application-supplied agent loop is required.
- Why this is / is not agent-owned: removing the model actor leaves execution and safety machinery but removes the task-specific coding judgment that selects and revises operations.
- Evidence: [`README.md`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/README.md); [`src/run_core.rs`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/src/run_core.rs); [`src/tools/agent.rs`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/src/tools/agent.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference is external; the assessment credits Recursive's first-party role/tool/runtime closure, not provider internals.

## S2 — Coordination

- State: A
- Function: attenuate destructive interference among multiple worker S1 cells that may otherwise act on the same project workspace concurrently.
- Disturbance / variety regulated: two or more write-capable workers can modify overlapping files or act on stale shared-workspace assumptions concurrently, creating edit conflicts or incoherent changes even when each local subtask is reasonable.
- Distinct S1 units: separately instantiated model-backed worker `AgentRuntime` instances created from the `agent` manifest.
- Inter-S1 disturbance: shared-workspace write-heavy tasks can collide when run concurrently; worker findings can also require ordering when one worker's output is an input to another.
- Attenuating coordination relation: the model-backed coordinator chooses `parallel` for independent read-only work and `sequential` for write-heavy/overlapping work, can chain dependent work, use shared memory/messages, and continue an existing worker only when context overlap justifies it.
- Feedback into subsequent S1 behaviour: the selected execution mode determines whether workers run concurrently or wait for prior worker completion; coordinator follow-up messages and synthesized briefs alter what a subsequent/continued worker does.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping is tied to the explicitly documented shared-file/write-interference mode and the coordinator's task-specific choice of parallel versus sequential execution to damp that disturbance, not to the existence of a message bus or task queue alone.
- Decisive decision or feedback right: decide whether identified worker work is safe to run concurrently, must be serialized, or should continue in an existing context versus a fresh worker.
- Decision owner: the model-backed coordinator agent.
- Supporting / enforcement mechanisms: `AgentMode::Parallel`/`Sequential`, manifest ordering, separate worker runtimes/tool state, shared memory, message bus, continuation channels, deadlines/cancellation.
- Closure path: coordinator identifies worker subtasks and interference/dependency → selects parallel/sequential/continue/fresh relation → runtime enforces that relation → affected workers execute under the changed ordering/context → their results return for the next coordination decision.
- Boundary reachability: the `agent` tool and its coordinator guidance are registered by the standard runtime when sub-agents are enabled, which is the default configuration; the coordination decision does not require downstream application code.
- Why this is / is not agent-owned: if the coordinator model is removed while the runtime modes remain, no component retains the task-specific discretion to decide which concrete work conflicts and which mode should regulate it.
- Evidence: [`src/multi.rs`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/src/multi.rs); [`src/tools/agent.rs`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/src/tools/agent.rs); [`docs/architecture/tools/multi-agent.md`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/docs/architecture/tools/multi-agent.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: shared memory/messages alone would not justify S2; the positive state depends on the explicit write-collision/dependency distinction and returned execution-mode decision.

## S3 — Inside-and-now control

- State: A
- Function: regulate current commitments and intervention across the active worker/task population on behalf of the project-level coding objective.
- Disturbance / variety regulated: which specialists should consume work now, whether work should run in parallel/sequential/background form, which retained worker should continue, current task failures/completions, stale or unnecessary work, and whether a running task should be redirected or cancelled.
- Whole-system current view: in supported coordinator mode the coordinator can list workers/tasks across the shared registry, inspect task status/output and read shared project state rather than relying only on one worker's local transcript.
- Current-control decision scope: design/dispatch the active specialist set, choose execution mode, inspect current tasks/results, send corrective/follow-up work, choose continue-versus-fresh worker, stop active tasks and synthesize or revise the present project commitment.
- Decisive decision or feedback right: choose and revise project-level worker commitments/interventions under current fleet state.
- Decision owner: the model-backed coordinator agent.
- Supporting / enforcement mechanisms: coordinator tool allow-list, shared `TaskRegistry`/`WorkerRegistry`, `task_list`, `task_output`, `task_stop`, `task_update`, `send_message`, `agent`, worker deadlines/cancellation and read-only coordinator restriction.
- Closure path: current worker/task state is exposed to coordinator → coordinator judges present allocation/intervention → dispatch/continue/stop/revise action mutates active worker commitments → later worker execution and project synthesis follow that returned decision.
- Boundary reachability: Recursive ships `coordinator-mode` as a first-party cargo feature and runtime gate; compiling that supported feature and setting `RECURSIVE_COORDINATOR_MODE=1` yields the restricted coordinator/tool path without application-specific orchestration code.
- Why this is / is not agent-owned: deterministic task registries and cancellation only record/enforce state; removing the coordinator model removes the semantic choice of which current work to create, continue, stop or replace.
- Evidence: [`README.md`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/README.md); [`src/coordinator.rs`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/src/coordinator.rs); [`src/multi.rs`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/src/multi.rs); [`docs/architecture/tools/task-tools.md`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/docs/architecture/tools/task-tools.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the strongest whole-fleet control path uses the opt-in `coordinator-mode` build feature rather than the default Cargo feature set; generic task decomposition outside that mode is not the evidence basis for S3.

## S3* — Complementary audit

- State: A
- Function: independently challenge an implementation worker's claim that a non-trivial change is complete/correct, using a fresh adversarial verifier with direct repository/test access, and return findings to current control.
- Disturbance / variety regulated: an implementation worker can report completion while code is incomplete, overfit to its own tests/assumptions, build-broken or wrong on edge/error paths.
- Claim being audited: the implementation satisfies the original task and works in the actual target repository, not merely that the implementer returned success.
- Ordinary reporting path: the implementation worker's own result, transcript and any tests it chose to run are returned through the normal worker result path.
- Complementary access path: a newly spawned `verification` worker receives the original task/files/approach with a fresh transcript, reads the current workspace independently, runs existing build/test/lint commands and adversarial probes, and emits a structured PASS/FAIL/PARTIAL verdict.
- Independence boundary: the verifier is a separate `AgentRuntime`/context with an explicit adversarial verification role and read-only mutation boundary; coordinator guidance explicitly recommends a fresh worker rather than continuing the implementer's context. It may use the same provider family, so independence is contextual/access-path rather than provider diversity.
- Who acts on findings: the coordinator receives verifier output as a worker result and can send follow-up instructions, continue/replace an implementation worker, stop work, or spawn corrective work before accepting/synthesizing the project result.
- Decisive decision or feedback right: make the semantic audit judgment from complementary repository/test evidence.
- Decision owner: the model-backed verification worker.
- Supporting / enforcement mechanisms: built-in `.recursive/agents/verification.md`, fresh worker construction, read-only role/tool restrictions, direct build/test execution, worker-result return and coordinator follow-up/dispatch tools.
- Closure path: implementation worker reports done → coordinator spawns fresh verifier → verifier probes actual workspace/tests and returns verdict/findings → coordinator uses findings to accept, redirect or repair current work → subsequent operation changes accordingly.
- Boundary reachability: the verification definition is shipped first-party and loaded by the standard `AgentDefinitions` path; the default-enabled `agent` tool can instantiate it without consumer-authored verifier code.
- Why this is / is not agent-owned: deterministic worker plumbing cannot decide whether arbitrary code satisfies the task; removing the verifier model removes the independent semantic audit judgment.
- Evidence: [`.recursive/agents/verification.md`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/.recursive/agents/verification.md); [`src/multi.rs`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/src/multi.rs); [`src/tools/agent.rs`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/src/tools/agent.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: verification is a supported coordinator-chosen path rather than a mandatory gate in every coding run; the positive state relies on the fresh role/context and direct workspace/test access, not merely on the word `verification`.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party runtime loop was established that models external/prospective change, develops adaptation options and returns a selected option into Recursive's current organizational capability.
- Disturbance / variety regulated: loop-mode events, provider catalogs, web/search results, memory and self-improvement development tooling expose change or history, but no qualifying S4 closure is supplied inside the assessed product boundary.
- Decisive decision or feedback right: none established for prospective organizational adaptation.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: `recursive loop`, `schedule_wakeup`, web/search tools, provider catalog refresh, vector/episodic memory, goal evaluator, `.dev/flows` self-improvement tooling.
- Closure path: no first-party external/future model → adaptation option → return into current capability/S3 loop was found inside the standard Recursive runtime.
- Why this is / is not agent-owned: self-scheduling and web access extend present S1 work; memory preserves information; provider refresh exposes operator-selectable capabilities. The documented self-improvement loop is orchestrated by external FlowX and is explicitly outside the published crate.
- Evidence: [`README.md`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/README.md); [`src/tools/schedule_wakeup.rs`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/src/tools/schedule_wakeup.rs); [`src/runtime_goal.rs`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/src/runtime_goal.rs); [`Cargo.toml`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/Cargo.toml); [`.dev/flows/SELF_IMPROVE.md`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/.dev/flows/SELF_IMPROVE.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: an external deployment can compose Recursive into an S4 process, but external FlowX or user-authored workflows do not donate S4 ownership to the frozen Recursive runtime.

### Absence scope

- Surfaces inspected: loop/self-scheduling runtime, wakeup/background tools, web/search, provider catalog management, vector/episodic memory, goal evaluator, project context/skills, `.dev/flows` self-improvement tooling and packaging boundary.
- Plausible first-party paths checked: loop mode as future intelligence; provider refresh as capability adaptation; memory as learning; goal evaluator as strategic feedback; self-improving development flow as S4; coordinator research workers as prospective intelligence.
- Why no material first-party path remains: runtime mechanisms either continue the present task or expose information/capabilities for current operation. The only explicit self-improvement loop is external FlowX-driven developer tooling under `.dev/`, which `Cargo.toml` excludes from the published crate and whose own documentation says Recursive is only the executor.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy decision loop was established at the selected project/task recursion.
- Disturbance / variety regulated: project instructions, system prompts, permission modes, tool allow-lists, plan approval and coordinator restrictions define operating constraints, but no identity-level issue is adjudicated and returned as ultimate policy.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established for an in-boundary S5 function.
- Supporting / enforcement mechanisms: `AGENTS.md`/`CLAUDE.md` context, base/custom system prompt, permission hooks/modes, plan mode, coordinator allow/deny lists, custom agent definitions and user configuration.
- Closure path: no identity/ultimate-policy issue → legitimate ultimate authority → authoritative decision → return-to-operation loop was found.
- Why this is / is not agent-owned: the coordinator and workers act under supplied purpose/policy; their ability to design worker roles or choose tools is operational authority, not authority to redefine Recursive's project identity or ultimate policy.
- Evidence: [`src/system_prompt.rs`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/src/system_prompt.rs); [`src/coordinator.rs`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/src/coordinator.rs); [`README.md`](https://github.com/jeffkit/recursive/blob/d693ff98ae9d3f47896994c55b2d8f494b4cca3d/README.md).
- Basis: explicit + structural absence.
- Confidence: high.
- Caveats: a self-hosted owner can externally edit project instructions/configuration, but generic configuration or task approval is not a qualifying parent S5 loop.

### Absence scope

- Surfaces inspected: project instruction loading, system-prompt customization, permissions and bypass controls, plan mode, coordinator/tool restrictions, agent definitions, task/team controls and repository governance as an adjacent surface.
- Plausible first-party paths checked: coordinator as executive S5; user plan approval as parent S5; editable project instructions as durable policy; permission/runtime-rule configuration as constitution; custom agent definitions as identity.
- Why no material first-party path remains: the inspected mechanisms either supply/enforce externally chosen constraints or regulate current work. None operationalizes an identity/ultimate-policy issue with legitimate ultimate authority and a returned decision at the assessed recursion.

## Distributed OSS parent arrangement

Recursive's GitHub maintainers and contributors govern the software project, but that repository governance is outside one running task organization. Independent self-hosted deployments do not share a first-party organization-level parent runtime merely because they use the same OSS code.

## Self-hosted and non-human modes

The positive S1/S2/S3/S3* findings do not require continuous human decision-making. S2 and S3 are model-owned in the supported coordinator mode, and S3* is model-owned by a fresh verification worker. Human/operator configuration remains an external boundary and does not add `(P)` without a function-specific parent closure.

## Recursion

At the selected recursion, specialist worker runtimes are S1 cells whose local coding variety remains model-owned. The coordinator sits above them and owns task-specific coordination/current-control decisions; the fresh verification worker supplies a complementary audit path over worker claims. Nested sub-agents below a worker are bounded delegation and are not separately credited as another complete viable organization without additional evidence.

## Variety and escalation

Worker-local coding variety stays with S1. Potential shared-workspace edit interference is attenuated by S2 execution-mode choices. Current worker/task variety is compressed into registry/status/output and returned results for S3 intervention, including continue/fresh/stop decisions. Completion uncertainty can escalate to the fresh verification path; failed findings return into corrective worker action. Runtime step/wall budgets and cancellation bound execution without taking ownership of those semantic decisions.

## Evidence gaps

The strongest S3 closure depends on the shipped but non-default Cargo feature `coordinator-mode`; pre-built/default-feature operation still exposes default-on sub-agents and the S2/S3* mechanisms, but not the full task-control tool family. S3* independence is role/context/access-path separation rather than guaranteed provider diversity. No positive S4/S5 path was found inside the runtime boundary.
