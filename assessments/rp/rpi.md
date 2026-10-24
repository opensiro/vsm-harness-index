---
harness_id: rpi
project_name: rpi
repository: https://github.com/bigfish1913/pi-rust
review_ref: db4eacd64e8c24939345fb6bd4efc2ef4328ee13
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# rpi

## Review boundary

- System in focus: first-party Rust-native rpi coding-agent system built as nine distributed crates at pinned `db4eacd64e8c24939345fb6bd4efc2ef4328ee13`, including `rpi-agent`, `rpi-harness`, `rpi-tools` and the `rpi-cli` frontend.
- Purpose and identity: embed or operate an autonomous model-directed file/shell coding agent with durable crash-resumable sessions and a plugin ABI.
- Relevant environment: user coding request, local repository and OS tools, provider model responses, terminal UI, session JSONL, config and installed optional packages/plugins.
- Standard-distribution boundary: first-party shipped `rpi` CLI and SDK's reusable tool loop, provider adapter, local code tools, JSONL persistence and compaction, plugins and event channels. No self-hosted external parent organization or user-authored plugin's agency is counted.
- Credited operating / distribution surfaces: CLI TUI/one-shot/JSON modes and `rpi-agent::AgentBuilder` model-to-tools loop, `rpi-tools` native workspace commands and `rpi-harness` session/resume/compaction logic.
- Adjacent first-party surfaces excluded from ownership: upstream model providers and hosted models, CI, benchmark/demo tape, user-installed third-party plugin code, separately written SDK applications and maintained repository governance.
- First-party operating / deployment modes considered: installed `rpi` binary, embedded library use with native tools and optional published plugin loading. No provider-backed live task was performed for this source inspection.
- Recursion level: one rpi-managed coding work session; additional user-embedded runtimes and plugin-provided agent teams are external constructions requiring separate evidence.
- Reviewed revision: `db4eacd64e8c24939345fb6bd4efc2ef4328ee13`, frozen Index candidate #379.
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The library-first Rust monorepo ships its own asynchronous model-to-tool agent loop, providers and file/shell operations. The `AgentBuilder` API constructs an actor that chooses tool calls based on provider responses, emits feedback events, and supports steer/follow-up/abort. `rpi-cli` supplies terminal, one-shot and JSON entry points, while `rpi-harness` persists sessions as append-only JSONL and restores work from a committed frame ([crates/pi-agent/src/agent.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-agent/src/agent.rs), [crates/pi-agent/src/agent_loop.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-agent/src/agent_loop.rs), [crates/pi-harness/src/agent_harness.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-harness/src/agent_harness.rs), [README.md](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/README.md)). The first-party `rpi-tools` package exposes read/write/edit/bash and search to the active model loop ([crates/pi-tools/src/lib.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-tools/src/lib.rs)).

Parallel tool execution choices, queues, cancellation, retries, model routing and session durability are useful within a single S1 actor. No separate standing agent population, collision diagnosis among competing S1 units, distinct whole-current supervisory authority, complementary independently assigned claim auditor, prospective environment-capability strategy or ultimate-policy/identity decision mechanism was found in the standard library+CLI implementation. Optional custom plugins can supply more, but their semantics are not shipped first-party obligations.

## Operational model

A user starts `rpi` and supplies a coding request. The agent stream receives provider output, dispatches selected first-party tools against local execution environment, returns tool results to the model's next choice and emits progress/finish events. Session frames persist and can resume after a crash. SDK embedding or a plugin may change the surrounding application, but those external choices are not evidence of built-in metasystem control.

## S1 — Operations

- State: A
- Function: model-guided coding work with observable tool feedback.
- Disturbance / variety regulated: changing source files, unknown repository topology, build/test outputs, tool errors and task uncertainty.
- Decisive decision or feedback right: choose next coding/file/shell tool invocation from observed model/tool context and adapt based on returned results.
- Decision owner: first-party `rpi-agent` model-directed coding actor, mediated by runtime; external model supplies inference, not an imported harness runtime.
- Supporting / enforcement mechanisms: `AgentBuilder`, `run_agent_loop`, stream function, tool registry, `ExecutionEnv`, transcript state and events.
- Closure path: user prompt→provider model response→tool calls executed in `rpi-tools`→tool outcomes appended→next model response or terminal answer.
- Boundary reachability: installed `rpi-cli` and embedded `rpi-agent` SDK use this shipped first-party actor.
- Why this is / is not agent-owned: unbounded task steps and tool choices are model-dependent, not simply a fixed developer script.
- Evidence: [crates/pi-agent/src/agent_loop.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-agent/src/agent_loop.rs), [crates/pi-agent/src/agent.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-agent/src/agent.rs), [crates/pi-tools/src/lib.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-tools/src/lib.rs), [crates/pi-cli/src/agent_session.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-cli/src/agent_session.rs).
- Basis: first-party source / installed CLI and SDK.
- Confidence: high for source path, no live provider output measured.
- Caveats: actual quality/latency and optional third-party tools vary by setup.

## S2 — Coordination

- State: —
- Function: no supported interference-specific attenuation between multiple distinct S1 operations.
- Disturbance / variety regulated: parallel tool calls or different user-embedded agents might edit overlapping files, but no first-party multi-unit conflict feedback is evidenced.
- Decisive decision or feedback right: detect a resource collision between independent operational actors and return a corrected allocation or arbitration; absent.
- Decision owner: runtime tool scheduling and queue operators act inside one agent rather than coordinating an independent S1 group.
- Supporting / enforcement mechanisms: single-agent tool execution modes, queues, cancellation and standalone plugin ABI.
- Closure path: selected tools execute and report back to the same model; no distinct collision finding→inter-agent changed work path.
- Why this is / is not agent-owned: tool scheduling inside one actor and generic pub/sub do not prove the VSM S2 inter-S1 relation.
- Evidence: [crates/pi-agent/src/agent_loop.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-agent/src/agent_loop.rs), [crates/pi-agent/src/agent.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-agent/src/agent.rs), [crates/pi-harness/src/runtime.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-harness/src/runtime.rs).
- Basis: bounded negative native-source inspection.
- Confidence: medium for the reviewed standard distribution.
- Caveats: external embedding or user-installed plugins may change the boundary and require separate assessment.

### Absence scope

- Surfaces inspected: tool loop, tool concurrency configuration, queued steering, harness runtime, plugin ABI.
- Plausible first-party paths checked: sequential/parallel tool mode, task queues and extension-owned coordination.
- Why no material first-party path remains: no owned two-S1 conflict-specific monitor/negotiation and binding feedback across separate workers.

## S3 — Inside-and-now control

- State: —
- Function: no supported distinct whole-current regulation of a live multi-S1 work organization.
- Disturbance / variety regulated: session budget, crashes, user steer/abort and model/tool errors are handled as runtime mechanics.
- Decisive decision or feedback right: choose and enforce whole-system current operational commitments across separately executing S1 units; absent.
- Decision owner: single model and user operate session controls, no separate differentiated portfolio supervisor.
- Supporting / enforcement mechanisms: session recovery, user steering, run budget, CLI status and JSONL event log.
- Closure path: stop/resume/steer controls a coding session but no separate whole-current controller redistributes an S1 population.
- Why this is / is not agent-owned: resumability and user task control alone do not establish an independent S3 actor.
- Evidence: [crates/pi-harness/src/session/session.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-harness/src/session/session.rs), [crates/pi-harness/src/agent_harness.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-harness/src/agent_harness.rs), [crates/pi-agent/src/agent.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-agent/src/agent.rs).
- Basis: bounded negative native-source inspection.
- Confidence: medium for the reviewed standard distribution.
- Caveats: external embedding or user-installed plugins may change the boundary and require separate assessment.

### Absence scope

- Surfaces inspected: session state/resume, run budget, steering, CLI and default SDK options.
- Plausible first-party paths checked: automatic continuation, user steer, dependency composition and plugin lifecycle.
- Why no material first-party path remains: no separate model/constructor whole-active-unit view deciding changed commitments with authoritative return.

## S3* — Complementary audit

- State: —
- Function: no supported independently owned evidence-taking review of S1 output claims with binding finding disposition.
- Disturbance / variety regulated: coding errors or invalid final claims can persist if the model does not independently check them.
- Decisive decision or feedback right: separate auditor challenges the producer from privileged evidence and forces correction or explicit failed handoff; absent.
- Decision owner: ordinary main model may run tools/tests but no installed independent reviewer is assigned.
- Supporting / enforcement mechanisms: tool results, event stream and searchable session logs, without review-verdict contract.
- Closure path: ordinary errors/test results are observations in S1; no separate challenger→finding→mandatory return.
- Why this is / is not agent-owned: observability, logs and manual test calls do not equal an independent complementary claim audit.
- Evidence: [crates/pi-agent/src/agent_loop.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-agent/src/agent_loop.rs), [crates/pi-harness/src/session/search.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-harness/src/session/search.rs), [crates/pi-harness/src/events.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-harness/src/events.rs).
- Basis: bounded negative native-source inspection.
- Confidence: medium for the reviewed standard distribution.
- Caveats: external embedding or user-installed plugins may change the boundary and require separate assessment.

### Absence scope

- Surfaces inspected: tool events, recovery, session search and CLI completion.
- Plausible first-party paths checked: manual test execution, SDK-constructed reviewer, instrumentation and off-box CI.
- Why no material first-party path remains: no first-party distinct audit role with source/readback rights and binding correction admission.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supported outside/future sensing, capability decision and return to improve later rpi operation.
- Disturbance / variety regulated: model availability, future project patterns or changed user needs are not tracked as separate strategic intelligence here.
- Decisive decision or feedback right: change future installed agent capabilities based on independent outside evidence; absent.
- Decision owner: user/install manager and external plugins can change capability manually, not a built-in adaptation owner.
- Supporting / enforcement mechanisms: compaction, skills, context files, provider adapters and package/plugin loader.
- Closure path: current session remembers context or reloads externally supplied tools; no observed future-facing sensing→option→adoption.
- Why this is / is not agent-owned: context persistence and an extensible ABI do not prove autonomous long-horizon adaptation.
- Evidence: [crates/pi-harness/src/compaction/compaction.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-harness/src/compaction/compaction.rs), [crates/pi-harness/src/skills.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-harness/src/skills.rs), [crates/pi-cli/src/packages.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-cli/src/packages.rs).
- Basis: bounded negative native-source inspection.
- Confidence: medium for the reviewed standard distribution.
- Caveats: external embedding or user-installed plugins may change the boundary and require separate assessment.

### Absence scope

- Surfaces inspected: context files, compaction, plugin reload, package installation and providers.
- Plausible first-party paths checked: plugin upgrade, SDK-constructed self-optimizer and session recall.
- Why no material first-party path remains: none of the inspected first-party paths owns a future option appraisal and operational capability update based on external intelligence.

## S5 — Identity and ultimate policy

- State: —
- Function: no supported ultimate system identity/purpose adjudication by a legitimate separate owner.
- Disturbance / variety regulated: provider credentials, settings and tool rights are standard execution boundaries rather than constitutional identity disputes.
- Decisive decision or feedback right: interpret overall purpose and policy authority, return binding identity resolution to S3/S4 and S1; absent.
- Decision owner: user config and caller define program instructions; no internal rightful ultimate-policy function.
- Supporting / enforcement mechanisms: system-prompt setting, provider selection, plugin trust and CLI options.
- Closure path: configured system prompt and tool permissions constrain S1 but do not adjudicate a contested higher-level identity.
- Why this is / is not agent-owned: a system prompt, user task and config are not an accountable S5 decision organ.
- Evidence: [crates/pi-harness/src/system_prompt.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-harness/src/system_prompt.rs), [crates/pi-cli/src/session.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-cli/src/session.rs), [crates/pi-agent/src/agent.rs](https://github.com/bigfish1913/pi-rust/blob/db4eacd64e8c24939345fb6bd4efc2ef4328ee13/crates/pi-agent/src/agent.rs).
- Basis: bounded negative native-source inspection.
- Confidence: medium for the reviewed standard distribution.
- Caveats: external embedding or user-installed plugins may change the boundary and require separate assessment.

### Absence scope

- Surfaces inspected: system prompt, settings, plugin trust and permission controls.
- Plausible first-party paths checked: top-level prompt configuration, tool policy, maintainer decisions and workspace-specific AGENTS guidance.
- Why no material first-party path remains: no first-party legitimate S5 remit and ultimate-identity judgment with return to current and prospective operations.

## Evidence gaps

- No live remote provider, actual repository coding trial or independently witnessed review was executed; source inspection supports ownership/path reachability rather than measured outcomes.
- SDK users may build complex agent organizations, and plugins can import arbitrary capabilities. Those external systems do not transfer their S2–S5 functions to the rpi standard distribution.
- Searchable session logs, crash recovery and tool concurrency may be crucial engineering mechanics, but no distinct same-recursion VSM metasystem feedback relation is inferred from their existence.

## Conclusion

The pinned rpi CLI and SDK expose a full first-party model-to-tool coding loop (S1=A). Multi-tool execution, durable sessions, plugins and extensibility are not sufficient evidence for separate S2 coordination, S3 whole-current control, S3* independent audit, S4 prospective adaptation or S5 ultimate identity authority. Proposed vector: **A / — / — / — / — / —**, frozen source-first.
