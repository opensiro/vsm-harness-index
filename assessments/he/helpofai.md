---
harness_id: helpofai
project_name: HelpOfAi
repository: https://github.com/helpofai/HelpOfAi-Cli
review_ref: a102dfbd043b41688b155135fb9bd48ebb7a3113
reviewed_at: 2026-10-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-05
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# HelpOfAi

## Review boundary

- System in focus: the first-party HelpOfAi coding-agent runtime at frozen revision `a102dfbd043b41688b155135fb9bd48ebb7a3113`, including the Rust TUI/headless agent loop, goal loop, first-party tools, durable sessions, subagents/fleet workers, Agent Fleet scheduler/ledger/typed manager controls, model-backed review tool, memory/project-context/constitution loading, permissions/sandboxing, skills and runtime APIs.
- Purpose and identity: execute coding tasks interactively or headlessly, persist long-running goals, delegate durable worker tasks, manage multi-worker runs, review code and recover from worker/runtime failures.
- Relevant environment: user coding objectives, repository/workspace state, command/build/test outputs, model-provider responses, worker/fleet state, host capacity, verifier/scorer evidence, persisted sessions/memory, MCP/runtime integrations and operator authority.
- Standard-distribution boundary: the repository-owned Rust runtime and shipped system skills are inside. External LLM providers, MCP servers, SSH hosts, model endpoints and optional external programs remain dependencies. The large `aios/` specification/design corpus is not credited unless a concrete frozen Rust runtime path instantiates it.
- Credited operating / distribution surfaces: TUI and `helpofai exec`; Plan/Agent/YOLO modes; persistent `/goal`; subagent/fleet-backed worker execution; Fleet scheduler/ledger/status/inspect/restart/interrupt/stop surfaces; bundled `fleet-manager` system skill; first-party `review` and `run_verifiers` tools; durable sessions, memory, sandbox/approval and runtime APIs.
- Adjacent first-party surfaces excluded from ownership: repository CI, benchmarks/eval harnesses, maintainer/release governance, declarative AIOS specs not wired into runtime, and documentation-only future Swarm/HelpFlow behavior where the frozen code explicitly says it is not yet available.
- First-party operating / deployment modes considered: ordinary local coding, headless exec, persistent goal mode, nested subagents, durable Agent Fleet local/SSH worker mode, manager-agent operation through the bundled fleet-manager skill, read-only review, and configured sandbox/approval/memory modes.
- Recursion level: an ordinary coding run or fleet worker is an S1 operational unit. A fleet-manager agent operates one recursion level above a set of current workers for S3 analysis. Deterministic Fleet scheduling and admission can construct S2 coordination across those S1 units.
- Reviewed revision: `a102dfbd043b41688b155135fb9bd48ebb7a3113`.
- Observation date: 2026-10-05.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

HelpOfAi exposes one durable model/tool runtime through TUI, headless `exec`, nested subagent and Agent Fleet launchers. Persistent goals re-dispatch the same operational runtime until the model reports completion/blocking or a configured token/time bound is exhausted.

Fleet adds a durable control plane over those workers: a ledger, leases, heartbeats, retry/restart state, host/task-class/run concurrency ceilings, worker receipts/artifacts and typed status/control APIs. Its deterministic scheduler reconstructs current fleet state, recovers stale work, admits queued work under configured capacity ceilings, leases workers and updates run state.

The frozen distribution also ships a `fleet-manager` system skill. A manager agent is instructed to inspect whole-run/worker state, classify failures and choose typed interventions such as restart, interrupt/stop or escalation. Those choices are model-owned while the Fleet runtime enforces and records them.

For audit, the first-party `review` tool resolves a file/diff/PR source and sends that evidence to a separate LLM call under a dedicated senior-reviewer system prompt with no tools, returning structured findings to the parent coding actor. `run_verifiers` separately provides deterministic parallel build/test/lint gates; those gates support evidence but are not themselves the agent-owned S3* decision.

## Operational model

A coding goal enters the main model/tool loop, which selects actions from workspace evidence and can persist across Goal turns. The actor can delegate nested worker assignments. When those workers are run through Fleet, deterministic scheduler policy coordinates shared worker/host capacity and durable lifecycle. A manager agent can observe the current fleet as a whole and intervene through typed controls. A separate reviewer model can directly inspect code/diff/PR evidence and return findings for corrective action.

## S1 — Operations

- State: A
- Function: autonomously perform coding work by selecting, executing and revising model/tool actions against a live workspace.
- Disturbance / variety regulated: unfamiliar code, changing files, shell/build/test failures, provider/tool errors, long-running goals, context limits, task uncertainty and user/sandbox constraints.
- Decisive decision or feedback right: choose the next coding/tool/delegation action from current evidence, revise strategy after failures, and decide when the current operational objective is complete or blocked.
- Decision owner: the active model-backed HelpOfAi coding agent or fleet worker.
- Supporting / enforcement mechanisms: core agent loop, tool catalog/execution, persistent goal loop, sessions, context management, file/shell/search/git tools, subagents, skills, sandbox/approval and provider routing.
- Closure path: objective/context → model selects action/tool → runtime executes → concrete workspace/tool evidence returns → model revises subsequent work until completion, blocking, cancellation or configured budget exhaustion.
- Boundary reachability: ordinary TUI and `helpofai exec` directly instantiate the model/tool runtime; persistent Goal and fleet worker paths reuse that same supported runtime.
- Why this is / is not agent-owned: without the model actor the runtime still exposes tools, persistence and enforcement, but open-ended coding decisions and strategy revision disappear.
- Evidence: README; `docs/AGENT_RUNTIME.md`; `crates/tui/src/goal_loop.rs`; `crates/tui/src/core/engine/tool_execution.rs`; `crates/tui/src/tools/subagent/mod.rs`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external providers supply inference but do not own the product's operational coding loop.

## S2 — Coordination

- State: C
- Function: attenuate interference among distinct current worker S1 units competing for bounded Fleet execution capacity.
- Disturbance / variety regulated: simultaneous worker demand can exceed configured per-run, per-host or per-task-class capacity; stale leases and interrupted workers can also retain execution claims that would otherwise interfere with later work.
- Decisive decision or feedback right: the shipped Fleet scheduler applies configured worker/host/task-class ceilings, lease validity, heartbeat/retry policy and queued-work eligibility to decide which worker slots may be launched or recovered.
- Decision owner: constructor/runtime policy. The scheduler deterministically executes configured coordination policy; it does not itself make autonomous semantic tradeoffs among workers.
- Supporting / enforcement mechanisms: Fleet ledger, leases, heartbeats, `max_workers_per_run`, `max_workers_per_host`, `max_workers_per_task_class`, stale-worker recovery, launch admission, retry/restart state and worker lifecycle events.
- Closure path: current worker occupancy/lease state + queued tasks → scheduler evaluates coordination policy → eligible work is launched/restarted while excess/conflicting work remains queued or stale claims are recovered → updated worker/ledger state is visible on the next scheduler tick.
- Boundary reachability: Agent Fleet is a shipped local-first runtime mode and `FleetScheduler` is directly used by the first-party fleet control plane; no custom coordinator implementation is required.
- Why this is / is not agent-owned: the coordination loop is real and closed, but its decisive capacity/lease rules are configured deterministic policy; therefore the state is constructor `C`, not `A`.
- Evidence: `docs/FLEET.md`; `docs/AGENT_RUNTIME.md`; `crates/tui/src/fleet/scheduler.rs`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the higher-level fleet-manager agent performs S3 intervention; S2 here is specifically the deterministic peer-capacity/lease coordination relation.

- Distinct S1 units: separate headless HelpOfAi fleet workers, each running its own model/tool coding loop and bounded task assignment.
- Inter-S1 disturbance: worker processes can contend for bounded per-run, per-host and per-task-class execution capacity, while stale leases can leave capacity falsely occupied.
- Attenuating coordination relation: the scheduler applies concurrency ceilings and leases, recovers stale work and controls which queued worker/task is admitted to execution.
- Feedback into subsequent S1 behaviour: admitted workers start/restart while deferred workers remain queued; lease/heartbeat/recovery events alter later worker availability and task execution.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the relation exists specifically to attenuate concurrent worker interference over scarce execution capacity and stale ownership, not merely to pass messages or order a workflow.

## S3 — Inside-and-now control

- State: A
- Function: manage a current fleet run as a whole by diagnosing worker state and choosing current interventions over active commitments.
- Disturbance / variety regulated: stale or failed workers, transient transport/provider failures, verifier disagreement, task failures, retry exhaustion, unsafe continuation and ambiguous current ownership/escalation needs.
- Decisive decision or feedback right: classify a current worker failure and choose among restart, interrupt/stop, preserve/no-retry, or escalation based on typed run/worker/artifact evidence and current authority boundaries.
- Decision owner: the model-backed manager agent using the shipped `fleet-manager` system skill; deterministic Fleet controls execute and ledger the chosen intervention.
- Supporting / enforcement mechanisms: bundled fleet-manager skill, `fleet status`, `inspect`, `logs`, `artifacts`, `restart`, `interrupt`, `stop`, Runtime API controls, retry budgets and Fleet ledger.
- Closure path: whole-run status + worker/artifact evidence → manager agent classifies current condition → manager selects typed intervention or escalation → Fleet runtime applies/records action → subsequent worker/run state changes and is observable through the same typed surfaces.
- Boundary reachability: `crates/tui/assets/skills/fleet-manager/SKILL.md` is a bundled first-party system skill and the referenced Fleet CLI/API controls are shipped runtime surfaces.
- Why this is / is not agent-owned: removing the manager model leaves deterministic scheduler/restart primitives but removes the semantic diagnosis of transient/task/verifier/needs-human state and the discretionary choice of safe current intervention.
- Evidence: `crates/tui/assets/skills/fleet-manager/SKILL.md`; `docs/FLEET.md`; Fleet status/control runtime surfaces.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: scheduler-only operation would support constructor-level current control; `A` relies on the supported manager-agent mode that closes the model-owned current-control loop.

- Whole-system current view: the manager starts from Fleet run status and can inspect workers, logs and bounded artifact refs across the active run, including retry/heartbeat/verifier state.
- Current-control decision scope: restart a transient failed worker, interrupt/stop unsafe work, decline inappropriate retry, preserve failed artifacts, or escalate unresolved authority/verifier conflicts.

## S3* — Complementary audit

- State: A
- Function: independently review code or change evidence through a model-backed reviewer path distinct from the producing coding actor's ordinary report.
- Disturbance / variety regulated: defects, missing tests, correctness/security/reliability issues and unsupported completion claims that the producing actor may overlook.
- Decisive decision or feedback right: inspect resolved file/diff/PR evidence under a dedicated reviewer prompt and decide which issues/suggestions/overall assessment are materially warranted.
- Decision owner: the separate model call instantiated by the first-party `review` tool.
- Supporting / enforcement mechanisms: read-only review source resolver, dedicated senior-reviewer system prompt, separate LLM request with no tools, structured JSON findings, plus optional deterministic `run_verifiers` evidence.
- Closure path: producer changes workspace/reports progress → review tool directly resolves file/diff/PR evidence → separate reviewer model returns structured findings → parent coding/manager actor receives findings and can revise work or create corrective action.
- Boundary reachability: `review` is a shipped first-party agent tool in `crates/tui/src/tools/review.rs`; it does not depend on repository CI or an external review service.
- Why this is / is not agent-owned: removing the reviewer model leaves source collection and schemas but removes the semantic judgment that identifies and prioritizes issues.
- Evidence: `crates/tui/src/tools/review.rs`; `crates/tui/src/tools/verifier.rs`; `docs/SUBAGENTS.md`; agent prompt verification guidance.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `run_verifiers` itself is deterministic and is not the source of the `A` state; the positive claim rests on the separate reviewer LLM path.

- Claim being audited: that a file/change/PR or produced implementation is correct and complete enough for the requested coding objective.
- Ordinary reporting path: the producer coding agent's own completion/status/tool output in its main conversation or worker receipt.
- Complementary access path: `review` independently resolves the target file/diff/PR and sends that evidence to a fresh dedicated reviewer-model request rather than trusting the producer summary.
- Independence boundary: the reviewer has a separate system prompt/context and no tool/mutation surface in that review request; it cannot silently modify the code it judges.
- Who acts on findings: the parent coding or manager agent receives the structured review output and can perform corrective edits, delegate follow-up or change current control decisions.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct externally and prospectively oriented adaptation loop is established.
- Disturbance / variety regulated: durable memory, project context, skills, provider switching and codebase-memory can improve current or later coding work, but they primarily retain/reuse information or configuration.
- Decisive decision or feedback right: no shipped first-party path was found that autonomously distinguishes future environmental change, develops adaptation options for the HelpOfAi harness itself and returns a selected adaptation into present capability.
- Decision owner: not established at S4 level.
- Supporting / enforcement mechanisms: global/project memory, `remember`, project context/cache, skills, MCP/provider configuration, codebase memory and software/project facts.
- Closure path: persisted memory/context/skills are loaded into later prompts, but there is no separate outside-and-then option-generation/adaptation cycle.
- Why this is / is not agent-owned: retention, retrieval and configurable skills do not satisfy S4 without a future/external distinction and adaptation-option closure.
- Evidence: `docs/MEMORY.md`; `crates/tui/src/memory.rs`; project context and skills surfaces; `HELPOfAi-CODEBASE-MEMORY*.md`.
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the `aios/enterprise/learning-engine` material is declarative/specification content and is not imported as runtime evidence.

### Absence scope

- Surfaces inspected: global/project memory, remember tool, codebase memory, project context/cache, skills, model/provider configuration, fleet receipts, AIOS learning-engine specs and runtime update/config surfaces.
- Plausible first-party paths checked: memory as S4; learned lessons in memory as adaptation; skills as future capability; AIOS learning engine as autonomous adaptation; provider switching as environmental intelligence.
- Why no material first-party path remains: executable paths retain/reuse operator/model-provided information or configuration, while the apparent learning-engine adaptation path is not instantiated by the reviewed Rust runtime.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure is established.
- Disturbance / variety regulated: HelpOfAi has global/project constitutions, protected invariants, authority ordering, branch/verification policy, escalation conditions, permissions, sandboxing and trust/capability policy.
- Decisive decision or feedback right: these mechanisms enforce or inject operator-authored policy, but no first-party runtime path was found that autonomously or parent-governedly resolves an identity/ultimate-policy issue and returns a durable authoritative identity decision into system operation.
- Decision owner: not established at S5 level.
- Supporting / enforcement mechanisms: global constitution, `.helpofai/constitution.json`, authority ordering, `escalate_when`, approval hooks, sandbox policy, fleet trust/capability grants and operator configuration.
- Closure path: configured policy constrains current action and can force user escalation, but the reviewed runtime does not itself close an identity-level policy deliberation/update loop.
- Why this is / is not agent-owned: a static or operator-authored constitution can be highly authoritative without itself being a VSM S5 decision process; permissions and escalation triggers are likewise insufficient alone.
- Evidence: README nested-constitution section; project-context constitution loader; sandbox/approval docs; Fleet trust-policy documentation.
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: `escalate_when` creates a path to human authority for selected operational conflicts, but the frozen evidence does not show a durable identity-policy issue → authority decision → changed governing identity closure rather than ordinary approval/escalation.

### Absence scope

- Surfaces inspected: global/repo constitution loading, authority ordering, protected invariants, branch and verification policy, `escalate_when`, Plan/Agent/YOLO modes, approval hooks, sandbox policy, Fleet trust/capability policy and maintainer governance.
- Plausible first-party paths checked: nested constitution as S5; user escalation as parent S5; permission mode as policy; Fleet trust policy as ultimate authority; repository governance as product identity.
- Why no material first-party path remains: these paths constrain ordinary operation or statically encode operator authority; no inspected path closes a genuine identity/ultimate-policy decision into a durable changed system identity/governing policy.

## Recursion

HelpOfAi explicitly converges subagents and Fleet workers on one durable headless agent runtime. Those workers can therefore be treated as distinct S1 units when executing bounded tasks. The fleet-manager role is assessed one recursion level above them for S3; this does not imply every nested worker contains its own complete viable-system metasystem.

## Variety and escalation

Operational variety is handled by model/tool iteration, persistent goals, subagents, fleet workers, retry/recovery, sandbox/approval and provider routing. Inter-worker execution-capacity variety is attenuated by deterministic Fleet scheduling. Current fleet failures can be escalated into the model-owned fleet-manager S3 loop, which either chooses a typed intervention or returns unresolved authority/product decisions to a human.

## Evidence gaps

No `?` state is required. The frozen Rust runtime and bundled system skill directly expose the S1, S2-constructor, S3-manager and S3* reviewer paths. S4/S5 negatives are based on executable runtime inspection rather than on the much broader declarative AIOS design corpus.

## Assessment summary

HelpOfAi closes autonomous S1 coding, supplies constructor S2 through deterministic Fleet capacity/lease coordination, closes autonomous S3 through the bundled fleet-manager agent and closes autonomous S3* through its separate model-backed review tool. Memory/skills do not establish prospective S4, and its nested constitution/security policies do not by themselves close identity-level S5.

**Vector:** A · C · A · A · — · —
