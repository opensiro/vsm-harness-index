---
harness_id: grit
project_name: Grit
repository: https://github.com/rtk-ai/grit
review_ref: 0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe
reviewed_at: 2026-09-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-27
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Grit

## Review boundary

- System in focus: the first-party `rtk-ai/grit` standard distribution at pinned revision `0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe`: the Rust CLI, AST symbol/dependency index, lock stores, queues, worktree/session integration, merge serialization, event/status surfaces and supported local/cloud coordination backends.
- Purpose and identity: coordinate multiple externally operated AI coding agents sharing one Git repository so overlapping edits and integration activity do not destructively interfere.
- Relevant environment: external AI coding agents and their model runtimes; human/operator invocation; the target Git repository and filesystem; Git/GitHub tooling; SQLite, Azure Blob and S3-compatible storage; concurrent edits, stale bases, lock expiry and merge contention.
- Standard-distribution boundary: the shipped `grit` CLI and library code under `src/`, its packaged coordination backends and ordinary command workflow are inside. Claude/Gemini/other agent runtimes are external clients. Benchmark launchers, tests, examples, repository development workflows and contributor automation are adjacent first-party surfaces and do not become product-runtime owners merely because they live in the same repository.
- Credited operating / distribution surfaces: `README.md`; `Cargo.toml`; `src/cli/mod.rs`; `src/db/lock_store.rs`; the standard database/backend implementations under `src/db/`; the Git/worktree/session implementation under `src/git/`; parser/index and notification/status paths under `src/parser/` and `src/room/`.
- Adjacent first-party surfaces excluded from ownership: `scripts/ai-agents/` and the other benchmark suites; `tests/claude_agents_test.sh`, `tests/harness.sh` and other test fixtures; `examples/05-claude-code-integration.sh` and examples generally; repository CI/release workflows; `CLAUDE.md` development instructions; maintainer/contributor workflows. These surfaces may demonstrate how external agents compose with Grit but are not part of the ordinary installed Grit runtime.
- First-party operating / deployment modes considered: local SQLite coordination; Azure Blob coordination; S3-compatible coordination; symbol claim/release with read/write modes; queue/wait promotion; worktree lifecycle and `done` merge/release; `plan`; `assign`; session start/PR/end; status/watch/heartbeat/gc.
- Recursion level: one installed Grit coordination substrate over a target repository. The Claude/Gemini/other coding agents using Grit are environmental actors at this repository-relative boundary. A wider composed multi-agent coding organization that includes those runtimes would be a different system in focus.
- Reviewed revision: `0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe`.
- Observation date: 2026-09-27.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Grit describes itself as a coordination layer for parallel AI agents on top of Git. Its shipped executable is a Rust command-line coordination substrate rather than an AI-agent runtime. The core workflow is caller driven: an external actor invokes `grit claim` with an explicit agent identifier, intent and symbol list; Grit attempts read/write locks, creates an isolated worktree for granted work, exposes queue/status information, and later `grit done` merges the actor's already-produced changes and releases its locks. The lock store records `symbol_id`, `agent_id`, `intent`, time-to-live and lock mode and returns deterministic `Granted` or `Blocked` results.

The repository contains useful helper automation, but those helpers do not add a first-party model/action loop. `grit plan` tokenizes a caller-supplied intent and performs a database symbol search before printing a suggested claim command. `grit assign` finds available symbols and deterministically chooses the first one, then reserves it and creates a worktree. Session commands create and manage a shared feature branch around external agent work. Status, watch, heartbeat and garbage collection expose or maintain coordination state. None of these paths receives a substantive coding objective, reasons over repository/tool feedback, edits the codebase and autonomously chooses what operational action follows.

The first-party Claude/Gemini surfaces are explicitly composition and evaluation artifacts rather than the installed product loop. `examples/05-claude-code-integration.sh` presents Grit instructions to be added to an external agent system prompt and separately launches `claude -p`. `scripts/ai-agents/bench.sh` identifies itself as an AI-agent benchmark, constructs prompts and launches external `claude` or `gemini` processes that call the Grit CLI. Those surfaces strongly demonstrate Grit's intended use with autonomous agents, but Methodology 0.3.6 does not permit adjacent benchmark/example agents to be borrowed as owners inside the assessed standard distribution.

The counterfactual owner test is decisive for S1. Remove the external Claude/Gemini/other coding agent while leaving the installed Grit CLI, AST index, lock stores, queues, worktrees, sessions and merge machinery in place. Grit can still index code, reserve symbols, report contention and manipulate Git structure when commanded, but there is no first-party actor that takes a coding objective, decides substantive edits from changing repository feedback and performs the work. The repository-relative autonomous S1 loop therefore does not close.

This result does not negate Grit's strong S2 evidence at a wider system boundary. OpenSiro's separate `functional-capability-depth` experiment already records public first-party Grit evidence for a direct non-canonical S2 coordination relation. That experimental observation concerns the composed product boundary where external coding workers are present; it is not imported into this standalone autonomy vector.

Primary evidence:

- [`README.md`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/README.md) — product identity, caller-driven claim/work/done workflow, symbol locking, queues, isolated worktrees, serialized merge and external-agent benchmark descriptions.
- [`Cargo.toml`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/Cargo.toml) — packaged Rust CLI/coordination dependency boundary; no model/provider runtime is part of the shipped crate dependencies.
- [`src/cli/mod.rs`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/src/cli/mod.rs) — caller supplies agent, intent and symbols; `plan`, `assign`, claim/queue, worktree, `done`, status/watch/session and maintenance paths remain deterministic coordination/control surfaces.
- [`src/db/lock_store.rs`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/src/db/lock_store.rs) — first-party lock abstraction and `Granted`/`Blocked` coordination outcomes.
- [`examples/05-claude-code-integration.sh`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/examples/05-claude-code-integration.sh) — external Claude process is separately launched and instructed to invoke Grit.
- [`scripts/ai-agents/bench.sh`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/scripts/ai-agents/bench.sh) — benchmark launcher explicitly starts external Claude/Gemini agents and tells them to coordinate through Grit.

## Operational model

An external coding agent or operator chooses the intended task, the concrete code changes and, in the ordinary claim workflow, the symbols to reserve. Grit then mediates shared-repository access. It indexes AST symbols/dependencies, records reservations, blocks incompatible accesses, optionally queues blocked actors, creates per-agent worktrees, serializes integration and releases/promotes coordination state after completion.

This is a material organizational capability when Grit is composed with autonomous workers: a worker can receive a block/grant/queue result and alter when or where it operates, directly attenuating edit/merge contention. But the workers that absorb coding-task variety and produce repository outcomes are not first-party operational units of the installed Grit substrate. The standard distribution supplies coordination infrastructure to those actors rather than the autonomous actors themselves.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational unit is established that receives a coding objective and closes a substantive decision/action/environment-feedback loop inside the installed Grit boundary.
- Disturbance / variety regulated: Grit itself handles code-symbol topology, lock state, queue state, worktree/session state, lock expiry and merge/integration conditions; substantive task ambiguity, implementation choices, tool use and repository-edit feedback are handled by the external coding agent.
- Decisive decision or feedback right: decide what code or other substantive repository action to perform next in pursuit of the task, using returned repository/tool/test feedback.
- Decision owner: the external AI coding agent or human/operator invoking Grit.
- Supporting / enforcement mechanisms: AST symbol/dependency index; read/write lock stores; TTL/heartbeat/gc; queue/backoff; isolated Git worktrees; session branches; merge serialization; status/watch notifications.
- Closure path: external actor selects task/action → invokes Grit to reserve work → Grit grants/blocks/queues and prepares the worktree → external actor performs the actual repository work → external actor invokes `done` → Grit integrates/reports/releases; the next substantive operational decision remains external.
- Why this is / is not agent-owned: removing the external agent leaves the complete Grit coordination substrate but removes the actor that interprets the coding objective, edits code and adapts its implementation actions from repository feedback.
- Evidence: [`README.md`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/README.md); [`src/cli/mod.rs`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/src/cli/mod.rs); [`Cargo.toml`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/Cargo.toml); [`examples/05-claude-code-integration.sh`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/examples/05-claude-code-integration.sh).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: benchmark and example scripts do launch autonomous external agents, but those adjacent evaluation/composition surfaces are not the shipped Grit runtime and cannot supply first-party S1 ownership for this assessment.

### Absence scope

- Surfaces inspected: README/product workflow; Cargo dependency boundary; CLI entrypoints; lock/database layer; parser/index; Git/worktree/session lifecycle; status/watch/heartbeat/gc; examples; real-agent benchmark/test launchers and repository automation boundary.
- Plausible first-party paths checked: `plan` as an autonomous planner; `assign` as autonomous task selection; session workflow as an agent runtime; worktrees as S1 units; queue promotion as autonomous operation; benchmark/test Claude/Gemini launchers as packaged product operation.
- Why no material first-party path remains: every shipped product path either transforms caller-supplied coordination state or manipulates Git/storage infrastructure. The only model-driven coding actors found are separately invoked external programs in examples/tests/benchmarks.

## S2 — Coordination

- State: —
- Function: Grit supplies a concrete anti-interference coordination relation for external coding workers, but no first-party inter-S1 coordination function exists among first-party operational units inside the declared repository-relative boundary because S1 admission itself does not close.
- Disturbance / variety regulated: competing external workers can attempt incompatible edits or integration against the same code symbols/repository state, causing overlapping writes, merge conflicts, stale work and lost output.
- Decisive decision or feedback right: decide whether a requested symbol access is compatible with active reservations and therefore may proceed now, must wait/queue or is blocked.
- Decision owner: constructor-defined Grit lock/queue rules at this boundary; the external agent chooses its task and whether/how to respond to the returned coordination result.
- Supporting / enforcement mechanisms: `LockStore::try_lock`; read/write modes; symbol/dependency indexing; queue/backoff and promotion; TTL/heartbeat/gc; isolated worktrees; serialized merge/release.
- Closure path: external worker requests a reservation → Grit returns grant/block/queue and changes repository/worktree access timing → after release the queue can promote a waiter → the external worker subsequently resumes/changes operation. The feedback loop is real but closes through environmental S1 actors rather than a first-party S1 population of Grit itself.
- Why this is / is not agent-owned: the coordination mechanism is first-party and materially changes external worker behavior, but the units being coordinated are not first-party Grit S1 units. A positive standalone S2 state would therefore import environmental operations across the declared boundary.
- Evidence: [`README.md`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/README.md); [`src/cli/mod.rs`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/src/cli/mod.rs); [`src/db/lock_store.rs`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/src/db/lock_store.rs); [`scripts/ai-agents/bench.sh`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/scripts/ai-agents/bench.sh).
- Basis: explicit + structural boundary analysis.
- Confidence: high.
- Caveats: this `—` is deliberately narrower than saying Grit lacks S2 capability. At the wider composed Grit-plus-agents boundary, its public locking/queue/worktree/merge path directly instantiates S2 and is already tracked separately by the capability-depth experiment.

### Absence scope

- Surfaces inspected: claim/release/done flow; lock-store abstraction and backends; queue and promotion; worktrees/merge serialization; session/status/watch paths; README examples; benchmark/test multi-agent launchers.
- Plausible first-party paths checked: treating external named `agent_id` records as internal S1 units; treating worktrees as S1 units; treating `assign` as creation of S1; treating benchmark-launched Claude/Gemini processes as standard-distribution S1 units.
- Why no material first-party path remains: the interference and attenuation relation is well evidenced, but the independently acting operational units on both sides of that relation are external clients. Grit records their identities and constrains access without packaging their operational decision loops.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system current-control actor is established over a first-party operational whole.
- Disturbance / variety regulated: current lock occupancy, waiting queues, expired leases, worktree/session state and merge safety are regulated deterministically, but these are coordination/infrastructure conditions around external workers rather than discretionary whole-S1 resource/commitment regulation owned inside Grit.
- Decisive decision or feedback right: choose or revise current commitments, priorities, resources or interventions for the operational organization as a whole.
- Decision owner: not established inside the Grit standard distribution; callers choose tasks/intents/priorities, while Grit enforces fixed lock/session/merge rules.
- Supporting / enforcement mechanisms: status views; lock conflict checks; queue ordering; TTL/heartbeat/gc; session state; merge file lock; worktree lifecycle; command errors and fail-closed storage behavior.
- Closure path: current coordination state is inspected/enforced and results are returned to external actors, but no first-party S3 owner reviews the whole operational situation and makes discretionary current-control decisions that return into first-party S1 operation.
- Why this is / is not agent-owned: deterministic enforcement of reservation, queue and merge rules does not become S3 ownership, and no agentic manager is packaged in the assessed runtime.
- Evidence: [`src/cli/mod.rs`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/src/cli/mod.rs); [`README.md`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a parent orchestrator can use Grit state as an S3 input in a wider organization; that parent is outside this repository-relative boundary.

### Absence scope

- Surfaces inspected: status/watch; lock/queue/session state; `plan`; `assign`; heartbeat/gc; worktree/merge lifecycle; backend configuration and failure handling.
- Plausible first-party paths checked: `status` as whole-system S3 view; `assign` as priority/resource allocation; queue promotion as S3 authority; session commands as whole-system control; merge serialization as current-control ownership.
- Why no material first-party path remains: these paths expose or deterministically enforce coordination/infrastructure state and do not supply an internal discretionary owner over current operational commitments of first-party S1 units.

## S3* — Complementary audit

- State: —
- Function: no first-party complementary audit path independently challenges claims from a first-party operational unit and returns findings into its subsequent control.
- Disturbance / variety regulated: tests and benchmarks can detect coordination failures, merge conflicts and leftover locks during repository development/evaluation; runtime status can report current coordination state.
- Decisive decision or feedback right: independently judge an operational claim using materially different access to operational reality and feed that finding back into the assessed organization's current regulation.
- Decision owner: no such runtime auditor is established. Development tests/benchmarks and maintainer audit work are adjacent surfaces; status/watch are ordinary observability over the same coordination store.
- Supporting / enforcement mechanisms: tests, benchmark result checks, Git status, lock/status queries and repository CI.
- Closure path: adjacent development/evaluation findings may lead maintainers to change Grit in later revisions, but no standard-distribution complementary-audit finding closes back into current first-party S1 operation at runtime.
- Why this is / is not agent-owned: neither ordinary status visibility nor repository tests constitute an independent runtime audit organization, and the underlying first-party S1 operation is absent.
- Evidence: [`README.md`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/README.md); [`scripts/ai-agents/bench.sh`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/scripts/ai-agents/bench.sh); [`src/cli/mod.rs`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/src/cli/mod.rs).
- Basis: structural negative search.
- Confidence: high.
- Caveats: benchmark evidence is useful evidence about Grit's coordination capability but belongs to an evaluation system rather than a shipped complementary-audit loop.

### Absence scope

- Surfaces inspected: status/watch and lock state; benchmark/test verification paths; README benchmark claims; repository CI/release boundary; merge error/recovery reporting.
- Plausible first-party paths checked: benchmark harness as S3*; tests as independent evaluator; `status`/`watch` as complementary access; merge conflict/error detection as audit; repository maintenance audits as product-runtime S3*.
- Why no material first-party path remains: all candidate audit surfaces are either ordinary access to the coordination state or adjacent development/evaluation machinery, with no independent runtime judgment returning into first-party S1 behavior.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party external-and-prospective adaptation loop develops future-facing options and returns them into the installed Grit capability.
- Disturbance / variety regulated: Grit can rescan code structure on initialization, observe current lock changes, search symbols from caller intent and operate across configured storage backends; these are current coordination/runtime functions rather than prospective adaptation.
- Decisive decision or feedback right: interpret relevant environmental/future change, generate an adaptation option and adopt/change current capability accordingly.
- Decision owner: not established inside the installed runtime. Maintainers and users externally choose new releases, configuration, backends and operational conventions.
- Supporting / enforcement mechanisms: symbol re-indexing; dependency graph; backend configuration; status/watch; repository development/release automation.
- Closure path: no shipped path senses an external/future distinction, develops a capability change and autonomously returns it into the running system. Upstream maintainers can publish later code changes, which is an adjacent development organization.
- Why this is / is not agent-owned: current code search/index refresh and event observation do not constitute a prospective adaptation loop, and no agent actor owns installed capability evolution.
- Evidence: [`src/cli/mod.rs`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/src/cli/mod.rs); [`README.md`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/README.md); [`Cargo.toml`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/Cargo.toml).
- Basis: structural negative search.
- Confidence: high.
- Caveats: normal open-source development can adapt Grit over time, but contributor/release evolution is outside the assessed runtime boundary unless explicitly wired as an operational adaptation loop.

### Absence scope

- Surfaces inspected: parser/index refresh; `plan`; configuration; watch/status events; backend selection; session workflow; repository release/development surfaces.
- Plausible first-party paths checked: re-indexing as learning; dependency discovery as environmental modeling; `plan` as S4 planning; cloud backend selection as adaptation; maintainer release flow as installed-runtime S4.
- Why no material first-party path remains: candidate paths either recompute current deterministic state or depend on an external user/maintainer to change installed capability; no prospective first-party adaptation closure is supplied.

## S5 — Policy and identity

- State: —
- Function: no runtime identity- or ultimate-policy-level decision path is established inside Grit.
- Disturbance / variety regulated: users configure storage backend, sessions, lock modes, TTLs, intents and command choices, while the code embeds fixed coordination rules; neither supplies a first-party runtime ultimate-authority loop for an autonomous organization.
- Decisive decision or feedback right: settle identity/ultimate-policy questions for the organization and return the authoritative decision into subsequent operation.
- Decision owner: external user/operator or project maintainers for the relevant configuration/code choices; no first-party runtime S5 authority is packaged.
- Supporting / enforcement mechanisms: command/configuration options; session branch naming; lock compatibility rules; repository documentation and release governance.
- Closure path: external actors select configuration or install changed code and Grit enforces those choices; there is no runtime identity/policy issue → legitimate internal/parent authority → authoritative decision → returned governance loop at the assessed recursion.
- Why this is / is not agent-owned: prompts/instructions given to external agents and fixed coordination policy do not constitute Grit-owned ultimate policy; the installed substrate has no agent actor or explicit parent-governed S5 closure.
- Evidence: [`README.md`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/README.md); [`src/cli/mod.rs`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/src/cli/mod.rs); [`examples/05-claude-code-integration.sh`](https://github.com/rtk-ai/grit/blob/0f3c9d04abe9525b1884f3a0ade890e54a6d9ffe/examples/05-claude-code-integration.sh).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: an external multi-agent organization can place Grit under its own S5 authority; that authority belongs to the wider system and is not imported here.

### Absence scope

- Surfaces inspected: CLI/configuration; session lifecycle; lock/queue policy; README and agent-integration instructions; repository release/governance boundary.
- Plausible first-party paths checked: `CLAUDE.md`/agent prompt instructions as S5; backend/config selection as S5; session policy as organizational identity; fixed lock rules as ultimate policy; maintainer/release governance as runtime parent mode.
- Why no material first-party path remains: all identified policy-like constraints are static implementation/configuration or externally selected operating conventions, without a closed runtime identity/ultimate-policy authority path.

## Recursion

Grit names multiple agents and creates multiple worktrees, but neither naming nor worktree creation establishes VSM recursion. The worktrees are isolated Git working directories owned by external actors. Grit itself does not package those actors as viable first-party organizations with their own operational and metasystemic functions. A composed coding organization in which autonomous agent runtimes use Grit can be analyzed separately at a wider boundary.

## Variety and escalation

Grit is a strong variety attenuator for one concrete class of multi-agent disturbance: concurrent repository contention. AST-level symbols reduce unnecessary file-level exclusion; read/write locks distinguish compatible from incompatible access; dependency-aware reads, queues, TTLs, backoff, worktree isolation and serialized merge reduce the variety presented to each external coding worker and to Git integration. Blocked, expired and failed-merge conditions remain visible to the caller, and failed merges preserve the worktree/branch for recovery.

At the standalone Grit boundary, escalation is therefore chiefly transport and enforcement toward external operators/agents: Grit reports `Blocked`, queue positions, status, stale/expired locks and merge errors, while the external actor decides the substantive response. These channels are important to the wider organization but do not independently establish S3, S4 or S5 ownership inside Grit.

## Evidence gaps

No material evidence gap blocks the terminal repository-relative classification at the pinned revision. The source tree clearly separates the shipped coordination CLI from examples/tests/benchmarks that launch external Claude/Gemini processes. A future first-party Grit distribution that packages and wires autonomous worker execution into the ordinary runtime would create a materially different assessment boundary and should be reassessed rather than inferred from the current benchmark surfaces.
