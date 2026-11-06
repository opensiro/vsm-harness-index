---
harness_id: suncode
project_name: SunCode
repository: https://github.com/costanzo/suncode
review_ref: 623eb4c2d8b98546148e5b7294d1a0423ffea7b5
reviewed_at: 2026-11-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# SunCode

## Review boundary

- System in focus: the frozen SunCode Phase 1 embedded Rust coding-agent runtime, exposed to an operator through the .NET 10 Avalonia desktop client and native Rust one-shot CLI, including first-party model/tool loops, six optional specialist child agents, operation policy, approval continuation, tool execution, persistence and recovery.
- Purpose and identity: assist a developer with inspection, modification, testing and review of their local software project while keeping machine access bounded, observable and reversible where feasible.
- Relevant environment: user requests, local project and dependency roots, changing file/test results, LLM provider responses, approval decisions, OS process/browser/computer state, context pressure and interrupted sessions.
- Standard-distribution boundary: the desktop embeds `sdks/csharp` → `sdks/c` → `sdks/rust` → the Rust `agent/` core in-process; the native Rust CLI directly embeds the typed Rust SDK for one-shot turns. The main model and optional child models choose operations, while first-party Rust validates and dispatches effects. Third-party inference providers, project contents, native OS and human operator are external. The bundled Node/Playwright Browser Use worker is a first-party device driver, not a second agent or independent auditor.
- Credited operating / distribution surfaces: `agent/crates/core/src/agent/{run,tools,submission,continuations,builtin_agents,lifecycle}.rs`, `policy.rs`, `context.rs`, the `llm`, `tools`, `data`, `database`, browser and computer crates; the implemented SDK bindings and desktop/CLI entry points.
- Adjacent first-party surfaces excluded from ownership: `design-system/` React specification tooling, GitHub development/release workflows, repository-maintainer tests and feature roadmaps; they support research but do not run inside the user's production coding session as a governance/audit authority. Deferred Web/TUI/IDE/mobile clients and future executable extensions are not credited.
- Operating modes: interactive local desktop with policy-mediated tool calls and persistent sessions; non-interactive CLI one-shot `run` / session resume with fail-closed approvals; optional `delegate_agent` to six compiled specialist definitions (Architect, UI/UX, Product, SWE, QA, SRE) with linked child sessions and bounded tool sets. Children cannot delegate recursively and require the same policy for machine operations.
- Recursion level: one project/session's coding operations and delegated specialists, not the multi-project desktop product-maintenance organization.
- Reviewed revision: `623eb4c2d8b98546148e5b7294d1a0423ffea7b5`.
- Observation date: 2026-11-06.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The production desktop hosts a native Rust agent through in-process C ABI bindings. `Agent::run` builds the system prompt, advertises built-in and configured tools under the current permission ceiling, requests a model completion, validates tool calls, executes permitted operations, records their results and continues the decision loop. Rust `policy` decides allowed/approval-required/denied risk classes, while the operator can grant or deny individual higher-risk actions. Filesystem mutations receive pre/post-image checkpoints and restore is conflict-checked; provider/tool/session outcomes are stored in SQLite. An interrupted turn may be resumed only through durable recovery/approval rules, not blind replay.

The optional `delegate_agent` tool instantiates a real linked child session. The primary agent selects an immutable specialist and task; that child receives its own model context and tool allowlist, inherits model/reasoning policy, runs through the same first-party dispatcher and returns a structured result into the parent tool stream. Architect, UI/UX and Product are read-oriented; SWE, QA and SRE can edit and run approved commands. Child delegation and external MCP/tool connection are not equivalent to independent VSM control functions.

The unusually important evidence boundary is the explicit QA specialist: it can inspect raw files and run its own tests in a separate child context, potentially challenging the SWE/primary production narrative. However the inspected shipped runner does not enforce a producer-independent QA invocation, choose audit samples or route a distinct audit decision into supervisory correction. Because the named, reachable QA path is materially closer to S3* than ordinary inline `test` tools, its actual independence and corrective closure are left **unresolved (`?`)**, not automatically rejected or credited.

Primary source:

- [Phase 1 product boundary](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/README.md)
- [Implemented specialist catalog](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/builtin_agents.rs)
- [Primary model/tool run loop](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/run.rs)
- [Child delegation result path](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/tools.rs)
- [Runtime architecture](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/.agents/ARCHITECTURE.md)
- [Focused child invocation tests](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/tests.rs)

## Operational model

One model-backed primary loop performs the user-directed coding task, sometimes delegating bounded research, implementation, QA or SRE operations to another model-backed loop. The typed dispatcher and approval policy guard effects and record observations. A child works in a separately persisted session, reports its result or approval-suspension state, and the parent may choose a next coding action. Human settings, authorizations and recovery operations constrain the loop; they are not autonomous mission/policy decisions. Multiple UI windows and separate projects do not automatically form one coordinating viable organization.

## S1 — Operations

- State: A
- Function: transform user requests into working repository/project inspection, code edits, test execution and answers using feedback from the actual project environment.
- Disturbance / variety regulated: unknown file structures, user requests, compiler/test failures, tool/provider errors, approval outcomes, context pressure and interrupted operations.
- Decisive decision or feedback right: select task-specific tools, arguments, recovery or child delegation, incorporate observed results and decide the next implementation/testing step.
- Decision owner: the primary model-backed Rust agent loop and, when invoked, model-backed compiled specialist child loops within their respective tool ceilings.
- Supporting / enforcement mechanisms: provider adapters, tool schema validation, Rust policy and approvals, audited dispatcher, SQLite session persistence, checkpoint/undo, context compaction and cancellation.
- Closure path: user task + environment observation → model-selected tool/delegation → policy-mediated execution → actual result/error/child envelope → next model decision or final answer.
- Boundary reachability: both supported desktop and Rust CLI call the same implemented agent SDK; `run.rs` and `tools.rs` wire first-party model decisions to real tool effects and child submissions.
- Why this is / is not agent-owned: removing the model-backed actor retains deterministic guards and storage, but leaves no task-sensitive chooser of code changes, tests, exploration or iterative correction. Agent discretion remains despite human permission constraints.
- Evidence: [`run.rs`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/run.rs); [`tools.rs`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/tools.rs); [`submission.rs`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/submission.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: operator approval may be required; provider access/model configuration is external. Specialist roles are optional, not independently scheduled background workers.

## S2 — Coordination

- State: —
- Function: no demonstrated specific conflict/oscillation among distinct cooperating S1 units plus closed mitigating coordination relation at this chosen recursion.
- Disturbance / variety regulated: children and primary work in a project, but no implemented cross-child shared-file reservation, write collision arbitration or negotiated mutual adjustment is evidenced.
- Decisive decision or feedback right: no separate cross-unit disturbance-specific response right identified.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: linked child records, model-selected delegation, per-session execution locks, read-only batch-call parallelism, tool policy and checkpoint conflict handling at undo time.
- Closure path: child results flow to the parent; per-session locks avoid repeated turns in one session; checkpoint restore refuses an unsafe undo. Neither path is shown regulating interference among two active S1 agents in a common coordinated task.
- Why this is / is not agent-owned: selecting a specialist, serial tool actions and isolating one session are work decomposition/operational safety, not evidence of a concrete inter-S1 coordination disturbance and corrective feedback.
- Evidence: [`submission.rs`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/submission.rs); [`tools.rs`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/tools.rs); [`checkpoint.rs`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/tools/src/checkpoint.rs).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: the actual operational subsidiaries exist, but a separately designed cross-child interference controller might alter this conclusion.

### Absence scope

- Surfaces inspected: per-session submission/locks, child session links, bounded tool execution, file checkpoints and parent result processing.
- Plausible first-party paths checked: collision detection across SWE/QA/SRE edits, shared task claims, reservations, negotiated schedules and coordination feedback into multiple S1 cells.
- Why no material first-party path remains: inspected locks/restore checks protect individual sessions/actions; no demonstrably inter-S1 conflict-specific closed mitigation channel is wired.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current resource, priority, commitment and accountability regulation beyond one main coding task's decomposition.
- Disturbance / variety regulated: current task failures, child limits and approvals are bounded; no competing organizational operating commitments with a whole-system deciding authority are established.
- Decisive decision or feedback right: the parent can choose a child role/task, but no evidenced resource bargaining or current-performance intervention across a portfolio of independent S1 obligations.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: primary-agent task selection, child tool ceilings (32/64), project limit, session budget/timeouts, child status records, attention events and human permission gates.
- Closure path: a specialist's report changes the parent's next task action; the mechanism does not show metasystem-wide regulation of current capacities, risks or commitments.
- Why this is / is not agent-owned: the primary model exercises useful local task direction, but supervisor labels and bounded subtask assignment are insufficient to prove S3 ownership.
- Evidence: [`builtin_agents.rs`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/builtin_agents.rs); [`tools.rs`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/tools.rs); [`attention_hub.rs`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/attention_hub.rs).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: a primary agent may coordinate task stages, but a closed whole-system current-control function is not demonstrated.

### Absence scope

- Surfaces inspected: primary/child submission, active-turn and tool budgets, session scope, child invocation state and operator-visible notifications.
- Plausible first-party paths checked: shared-resource allocation across active autonomous S1 commitments, executive prioritization, portfolio metrics, explicit intervention and accountability feedback.
- Why no material first-party path remains: the shipped controls bound individual tasks or route child status and approvals; no organization-wide resource/commitment decision path distinct from task orchestration is evidenced.

## S3* — Complementary audit

- State: ?
- Function: potentially independent QA-agent inspection of project reality beyond the ordinary producing agent's report, but organizational independence and corrective control closure are not fully established.
- Disturbance / variety regulated: coding-agent claims about correctness may be challenged by project files/tests; there is a first-party QA child with direct `read/glob/grep/bash` capability and its own context.
- Decisive decision or feedback right: QA's agent-directed test selection/findings could challenge an SWE or primary claim, but no actual producer-independent audit sampling/adjudication right or obligatory return for corrective supervisory action is demonstrated.
- Decision owner: possible QA model actor for independent evidence gathering; control of audit invocation, scope and correction remains primary model discretion. Whether that is sufficient S3* independence is unresolved.
- Supporting / enforcement mechanisms: compiled QA specialist definition, linked child session, direct raw project/testing tool access, child result envelope, persisted trace and parent tool-result continuation.
- Closure path: the primary may invoke QA → QA can inspect raw code/run checks → QA report returns as a tool result → primary could revise. This is a **reachable potential path**, but code does not establish when QA must be independent of the producer's framing, nor a challenge/decision/returned correction contract that distinguishes audit from ordinary delegated QA.
- Why this is / is not agent-owned: a separately running QA model has discretion over inspection, unlike static logging; nevertheless its role name and generic delegated testing do not prove the complementary auditor's autonomous corrective authority.
- Evidence: [`builtin_agents.rs` QA policy](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/builtin_agents.rs); [`tools.rs` child-result path](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/tools.rs); [`submission.rs` child context](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/submission.rs); [`tests.rs` child invocation tests](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/tests.rs).
- Basis: explicit + structural, unresolved audit boundary.
- Confidence: medium for the open question; high for QA execution reachability.
- Caveats: project unit tests, Git diff UI, checkpoints and ordinary approval logs are not themselves S3*. The named QA child is the specific unresolved shipped path—not a hypothetical plugin or deferred design.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective intelligence loop developing future capability options and returning them to current S3-controlled structure.
- Disturbance / variety regulated: current model/provider availability, local projects, external fetched content and session context serve present task operation, not adaptive organization planning.
- Decisive decision or feedback right: no first-party agent-owned strategic capability adjustment across future conditions.
- Decision owner: not established.
- Supporting / enforcement mechanisms: provider/model catalog, WebFetch, MCP/LSP connectivity, context summarization, durable configuration and user choice of providers/credentials.
- Closure path: external information may inform the next coding step or operator configuration; no distinct external-sensing → prospective option → committed capability-change → current-control conversation is observed.
- Why this is / is not agent-owned: the model may plan a code change or consult web content, but generic research for a present task and operator-configured runtime options are not S4 prospective adaptation.
- Evidence: [`context.rs`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/context.rs); [`run.rs`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/run.rs); [`ARCHITECTURE.md`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/.agents/ARCHITECTURE.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: developer maintenance and proposed future native clients belong to adjacent product evolution, not an operating agent S4 at this boundary.

### Absence scope

- Surfaces inspected: model routing, context management, WebFetch and MCP/LSP tools, persistent configuration, agent/child prompts and repository plans.
- Plausible first-party paths checked: external threat/opportunity horizon scanning, future options, experimental capability upgrade proposals and S3-ratified adaptation returning to operations.
- Why no material first-party path remains: the shipped paths choose tools/provider settings for immediate coding tasks and do not close an organizational future-environment adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/mission-level policy adjudication or parent-governed ultimate-policy decision with durable return is established.
- Disturbance / variety regulated: dangerous filesystem/process/browser/computer operations and credential/external path risk are bounded by static risk labels, host capabilities, human approvals, project scope and deterministic denials.
- Decisive decision or feedback right: local allow-once/deny/full-control decisions apply to side effects; no identity-defining purpose/policy discretion or return path at S5 level.
- Decision owner: not established; the operator approves actions and configures the application, while code enforces authored policies.
- Supporting / enforcement mechanisms: `policy::evaluate`, session configuration, bounded tool definitions, approval continuation, checkpoints, Browser/Computer enablement and shutdown.
- Closure path: requested high-risk action → policy classification → human approval or denial → execution or stop of that action. No identity/constitution question becomes a durable decision governing the organization's future permissible mission.
- Why this is / is not agent-owned: removing the coding model leaves the same static risk rules and operator permission authority. Local approval and safety enforcement do not make the agent an ultimate-policy authority.
- Evidence: [`policy.rs`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/policy.rs); [`continuations.rs`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/agent/crates/core/src/agent/continuations.rs); [`ARCHITECTURE.md`](https://github.com/costanzo/suncode/blob/623eb4c2d8b98546148e5b7294d1a0423ffea7b5/.agents/ARCHITECTURE.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: proper human authority over a local tool is present; a general user approval is not by itself S5 organizational governance.

### Absence scope

- Surfaces inspected: policy modes and permission continuations, risk categories, embedded SDK/host capability boundary, prompts, credentials/configuration, child restrictions and project scope.
- Plausible first-party paths checked: constitutional/identity policy revision, legitimate parent escalation and decision, permanent identity-level policy return governing later operation.
- Why no material first-party path remains: documented decisions are per-tool risk/host settings, not decisions about SunCode's ultimate identity or mission with parent-ratified closure.

## Recursion

The main model and optional fixed specialists each form real operational loops. However a collection of subordinate work loops and their session link does not by itself supply the S2/S3/S4/S5 relations for a further viable recursion. Separate desktop projects, CLI sessions and the development organization are not merged into a common higher-order actor on repository co-location alone. The possible complementary QA path is recorded explicitly as unresolved within the selected project/task boundary.

## Variety and escalation

Provider choice, project tools, specialist operational roles, MCP/LSP/browser/computer access and web retrieval amplify the environment variety the coding agent can address. Rust policy, tool allowlists, host ceilings, project boundaries, user approvals, context budget, cancellation, checkpoint-based undo and durable continuation attenuate it. Side-effect risks reach the human; child status reaches the primary task model. This makes a substantial safe operating harness, but safety mechanisms do not automatically imply autonomous metasystem ownership.

## Evidence gaps

Static source-first inspection at the exact frozen revision, with focused Rust child-invocation tests read as implementation evidence. We did not run the desktop app with live model inference or independently reproduce model-selected QA reviewing SWE claims. **S3* remains `?`** because a real, separately-contextualized QA agent with direct file/test access is shipped, but the inspected delegation path does not establish a producer-independent QA sampling/return decision distinct from routine assigned testing. Resolving it would require a concrete supported producer→QA→corrective-supervisory trace or stronger source wiring/contract. This is a bounded live-path uncertainty, not an assumption about future development.

## Assessment summary

SunCode runs a first-party Rust model/tool loop with six implemented optional specialist child agents (**S1=A**). Separate child sessions, capability ceilings, host approval, checkpoints and event/attention streams do not establish S2/S3 current metasystem, S4 prospective adaptation or S5 ultimate identity policy. The explicit QA child presents a reachable but unresolved question about complementary independent audit (**S3*=?**).

Proposed vector: **`A · — · — · ? · — · —`**.
