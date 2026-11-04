---
harness_id: gray
project_name: gray
repository: https://github.com/vstaln/gray
review_ref: 06aced40a388051a2b42ce23303adfe98ad7d14e
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# gray

## Review boundary

- System in focus: The pinned gray CLI/library runtime and its shipped plugin-host construction surface.
- Purpose and identity: Execute coding and automation tasks through model-selected shell/tool actions with resumable local sessions.
- Relevant environment: User workspace, provider APIs, shell processes, context limits, tool errors and operator input.
- Standard-distribution boundary: Rust gray/gray-core plus provider, tool, session and plugin-host machinery at this ref. Separately versioned sidecar repositories, the live plugin index and local-only plugins are not pinned members of this assessment.
- Credited operating / distribution surfaces: [README.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/README.md); [docs/plugins.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/docs/plugins.md); [crates/gray/src/main.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray/src/main.rs); [crates/gray-core/src/agent_loop.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_loop.rs); [crates/gray-core/src/parallel.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/parallel.rs); [crates/gray-core/src/agent_tools.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_tools.rs).
- Adjacent first-party surfaces excluded from ownership: CI/release and Windows-development records, fixture sidecars, external model services, gray-web/account/plugin repositories, and separately installed gateway/memory/subagent implementations. docs/plugins.md explicitly says plugins are not developed in this repository.
- First-party operating / deployment modes considered: Interactive REPL, print/headless structured input, resumed sessions, serial/eligible-parallel tools and installed generic sidecar callbacks. Advertised cron/gateway/memory functionality delegated to separate plugins is considered as a host integration boundary, not imported implementation.
- Recursion level: One task-executing harness; multiple calls, processes or sessions do not establish recursive viability.
- Reviewed revision: `06aced40a388051a2b42ce23303adfe98ad7d14e`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI selects interactive or print execution and constructs an Agent around streaming providers and a tool executor. The core accumulates model responses, dispatches tool calls, records observations and continues until a final reply, stop or failure. It repairs malformed tool arguments, retries bounded transport failures, handles context compaction and persists sessions. Parallel execution is permitted only for eligible tool batches; mutating shell forms are filtered. The plugin host transports lifecycle hooks, commands and tools; implementations such as memory, permissions and subagents live in separate repositories or local-only sources. Operator model/config selection and runtime enforcement remain distinct from model task discretion.

Primary implementation: [README.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/README.md); [docs/plugins.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/docs/plugins.md); [crates/gray/src/main.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray/src/main.rs); [crates/gray-core/src/agent_loop.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_loop.rs); [crates/gray-core/src/parallel.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/parallel.rs); [crates/gray-core/src/agent_tools.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_tools.rs).

## Operational model

A task-producing model session is S1: it chooses commands and subsequent actions from actual tool observations. Rust dispatch, sessions and retries enable that decision. A batch of shell calls is not a set of distinct autonomous S1 organizations. External sidecars may extend a deployment, but their unpinned internal organizations cannot donate ownership to the reviewed core.

## S1 — Operations

- State: A
- Function: Transform a requested task into shell actions and a final result.
- Disturbance / variety regulated: Repository contents, command results, model responses and tool failures.
- Decisive decision or feedback right: Choose the next tool/action or finish after observing prior results.
- Decision owner: The active model-backed Agent actor.
- Supporting / enforcement mechanisms: Streaming provider adapters, tool argument repair, tool executor, transcript/compaction and retry machinery.
- Closure path: Tool outcomes are appended to messages and enter the next model request; the model continues or produces the final reply.
- Boundary reachability: main.rs dispatches print/REPL modes to the same gray-core Agent loop; this is the installed runtime, not a fixture.
- Why this is / is not agent-owned: Without the model actor the executor can run supplied commands but cannot choose materially the same task solution.
- Evidence: [crates/gray/src/main.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray/src/main.rs); [crates/gray-core/src/agent_loop.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_loop.rs); [crates/gray-core/src/agent_tools.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_tools.rs).
- Basis: structural.
- Confidence: high.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

## S2 — Coordination

- State: —
- Function: No separate in-boundary inter-S1 stabilization function established.
- Disturbance / variety regulated: Potential interference among shell calls or separate sessions.
- Decisive decision or feedback right: No S2-specific discretionary coordination right found.
- Decision owner: Tool batching and session handling are deterministic runtime support; optional external subagent actors are outside the pin.
- Supporting / enforcement mechanisms: parallel.rs command eligibility, tool dispatch, session state and plugin callbacks.
- Closure path: Tool results return to one task actor, not an inter-unit stabilization loop.
- Why this is / is not agent-owned: Read-only batching and serial mutation selection regulate tool effects within a turn, not independently operating S1 units.
- Evidence: [README.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/README.md); [docs/plugins.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/docs/plugins.md); [crates/gray/src/main.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray/src/main.rs); [crates/gray-core/src/agent_loop.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_loop.rs); [crates/gray-core/src/parallel.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/parallel.rs); [crates/gray-core/src/agent_tools.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_tools.rs).
- Basis: structural.
- Confidence: high within the declared pinned host boundary.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/README.md); [docs/plugins.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/docs/plugins.md); [crates/gray/src/main.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray/src/main.rs); [crates/gray-core/src/agent_loop.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_loop.rs); [crates/gray-core/src/parallel.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/parallel.rs); [crates/gray-core/src/agent_tools.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_tools.rs).
- Plausible first-party paths checked: Tool concurrency, optional subagent host protocol, command hooks and session/task interfaces.
- Why no material first-party path remains: The pinned core supplies no distinct S1 collision-negotiation actor or S2-specific feedback constructor. Separate plugin implementations would need their own pinned boundary.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system current-control organization established.
- Disturbance / variety regulated: Quota failures, context limits and present task execution.
- Decisive decision or feedback right: No shared-resource/commitment bargaining or intervention judgment on behalf of a whole identified.
- Decision owner: Operator configuration and deterministic retry/dispatch choose or enforce fixed execution constraints.
- Supporting / enforcement mechanisms: Backoff limits, stop conditions, compaction, CLI configuration and plugin forwarding.
- Closure path: Local execution resumes or stops; no whole-system returned current-control judgment.
- Why this is / is not agent-owned: A task agent choosing tools and a runtime enforcing limits do not establish S3.
- Evidence: [README.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/README.md); [docs/plugins.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/docs/plugins.md); [crates/gray/src/main.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray/src/main.rs); [crates/gray-core/src/agent_loop.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_loop.rs); [crates/gray-core/src/parallel.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/parallel.rs); [crates/gray-core/src/agent_tools.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_tools.rs).
- Basis: structural.
- Confidence: high within the declared pinned host boundary.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/README.md); [docs/plugins.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/docs/plugins.md); [crates/gray/src/main.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray/src/main.rs); [crates/gray-core/src/agent_loop.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_loop.rs); [crates/gray-core/src/parallel.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/parallel.rs); [crates/gray-core/src/agent_tools.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_tools.rs).
- Plausible first-party paths checked: Quota/retry decisions, print/REPL steering, gateway/cron forwarding and generic hook authority.
- Why no material first-party path remains: No current whole-system view plus S3-specific autonomous or parent-decision return is shipped in the reviewed host.

## S3* — Complementary audit

- State: —
- Function: No complementary independent operational audit established.
- Disturbance / variety regulated: Possible false task completion or corrupted tool output.
- Decisive decision or feedback right: No independent audit judgment with corrective return found.
- Decision owner: The task actor owns its ordinary self-check; development test authors own adjacent tests.
- Supporting / enforcement mechanisms: Transcripts, error repair, provider tests and plugin event notifications.
- Closure path: Ordinary observations return to the producer; no separate challenge-to-control path.
- Why this is / is not agent-owned: Tracing, repair tests and generic event hooks do not supply an independently owned audit function.
- Evidence: [README.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/README.md); [docs/plugins.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/docs/plugins.md); [crates/gray/src/main.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray/src/main.rs); [crates/gray-core/src/agent_loop.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_loop.rs); [crates/gray-core/src/parallel.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/parallel.rs); [crates/gray-core/src/agent_tools.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_tools.rs).
- Basis: structural.
- Confidence: high within the declared pinned host boundary.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/README.md); [docs/plugins.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/docs/plugins.md); [crates/gray/src/main.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray/src/main.rs); [crates/gray-core/src/agent_loop.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_loop.rs); [crates/gray-core/src/parallel.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/parallel.rs); [crates/gray-core/src/agent_tools.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_tools.rs).
- Plausible first-party paths checked: Agent/test separation, transcript evidence, plugin hooks and fixture sidecars.
- Why no material first-party path remains: The host has no shipped audit-specific actor, alternate operational access and corrective authority; arbitrary future sidecars are not an S3* constructor.

## S4 — Outside-and-then intelligence

- State: —
- Function: No outside-and-then capability adaptation organization established.
- Disturbance / variety regulated: Changing providers, context pressure and recurring user tasks.
- Decisive decision or feedback right: No prospective external-distinction-to-capability adaptation judgment identified.
- Decision owner: User selects model/config/plugins; deterministic compaction and update machinery retain or replace artifacts.
- Supporting / enforcement mechanisms: Context summarization, model catalog/configuration, skill loading and separate memory/cron sidecars.
- Closure path: Task context is compressed or commands forwarded, without an S4 conversation returning adaptation into present capability.
- Why this is / is not agent-owned: Persistence, scheduling or installing a user-chosen plugin does not by itself own prospective adaptation.
- Evidence: [README.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/README.md); [docs/plugins.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/docs/plugins.md); [crates/gray/src/main.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray/src/main.rs); [crates/gray-core/src/agent_loop.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_loop.rs); [crates/gray-core/src/parallel.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/parallel.rs); [crates/gray-core/src/agent_tools.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_tools.rs).
- Basis: structural.
- Confidence: high within the declared pinned host boundary.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/README.md); [docs/plugins.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/docs/plugins.md); [crates/gray/src/main.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray/src/main.rs); [crates/gray-core/src/agent_loop.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_loop.rs); [crates/gray-core/src/parallel.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/parallel.rs); [crates/gray-core/src/agent_tools.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_tools.rs).
- Plausible first-party paths checked: Skills, model selection, compaction, plugin install/update and advertised memory/cron integration.
- Why no material first-party path remains: No pinned prospective adaptation actor or S4-specific constructor/parent-return closure remains; external plugin implementation is not inherited.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy closure established.
- Disturbance / variety regulated: Potential changes to task instructions, permissions and purpose.
- Decisive decision or feedback right: No identity-level referral and authoritative return procedure found.
- Decision owner: The operator/developer supplies initial instructions and local configuration.
- Supporting / enforcement mechanisms: AGENTS.md/skills, permissions hook protocol, user questions and stop/steering support.
- Closure path: Instruction or hook output can affect a turn, but no identity dispute reaches an S5 authority and returns as ultimate policy.
- Why this is / is not agent-owned: Static constraints and ordinary command approvals do not establish S5.
- Evidence: [README.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/README.md); [docs/plugins.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/docs/plugins.md); [crates/gray/src/main.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray/src/main.rs); [crates/gray-core/src/agent_loop.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_loop.rs); [crates/gray-core/src/parallel.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/parallel.rs); [crates/gray-core/src/agent_tools.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_tools.rs).
- Basis: structural.
- Confidence: high within the declared pinned host boundary.
- Caveats: Source inspection establishes the shipped path, not successful live provider execution or product effectiveness.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/README.md); [docs/plugins.md](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/docs/plugins.md); [crates/gray/src/main.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray/src/main.rs); [crates/gray-core/src/agent_loop.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_loop.rs); [crates/gray-core/src/parallel.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/parallel.rs); [crates/gray-core/src/agent_tools.rs](https://github.com/vstaln/gray/blob/06aced40a388051a2b42ce23303adfe98ad7d14e/crates/gray-core/src/agent_tools.rs).
- Plausible first-party paths checked: System instructions, plugin permission/question interfaces, configuration, operator steering and upstream governance.
- Why no material first-party path remains: The pinned distribution has no identity/ultimate-policy decision-and-return organization; maintainer development decisions remain adjacent.

## Distributed OSS parent arrangement

The upstream maintainer and contributors govern repository development. That adjacent organization is not a runtime parent mode of the assessed task harness. No function-specific returned organization-level S3/S4/S5 decision is credited merely from contributor activity.

## Self-hosted and non-human modes

The self-hosted CLI runs with operator-selected credentials, model, shell prefix and plugins. REPL steering, stop/resume and configuration are ordinary task control; no separate whole-system parent S3, prospective S4 or identity-return S5 loop is established in the pinned host.

## Recursion

No complete recursive viable unit is established. Local tool execution, process spawning and durable session state alone do not demonstrate a child identity, environment and metasystem.

## Variety and escalation

Streaming/provider errors, quota waits, malformed calls, context overflow and shell outcomes are transduced into retries, observations or an explicit failed/aborted turn. Hook denial and human steering may constrain work; these mechanisms alone are not algedonic channels or metasystem ownership.

## Evidence gaps

This is pinned-source analysis. No real model, paid provider, external worker or production workload was executed. Operational success, reliability and downstream effectiveness are unmeasured. The bounded negative judgments concern the declared distribution, not hypothetical future extensions.
