---
harness_id: urbanbreach-harness
project_name: urbanbreach Harness
repository: https://github.com/urbanbreach/agent-harness
review_ref: 5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-16
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# urbanbreach Harness

## Review boundary

- System in focus: first-party Rust terminal coding-agent runtime, including the coordinator, model-provider adapter, local tool execution, permission path, subagents, session journal and CLI/TUI at upstream revision `5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4`.
- Purpose and identity: accept an open-ended engineering task and let a model-steered local agent inspect, modify and test a project while leaving replayable evidence.
- Relevant environment: working-directory files, host shell, tool results, user permissions, installed providers and external tools; a remote or local model endpoint supplies inference.
- Standard-distribution boundary: packaged `crates/harness`, `crates/harness-core`, `crates/harness-tools` and TUI, as documented for locally built Rust CLI. Shipped `harness doctor` and `harness tui --mock` are diagnostic/illustration modes, not evidence that a mock model solves tasks.
- Credited operating / distribution surfaces: coordinator run/turn/worker machinery, tool registry and execution, supported model-driven turn lifecycle, session/event state, permission checks, supported subagent execution and TUI/CLI invocation.
- Adjacent first-party surfaces excluded from ownership: examples, CI and test fixtures, benchmark/eval tools, release automation, project-maintainer changes, recorded demo and support bundles. External providers, user approvals and third-party MCP servers do not donate autonomous VSM functions.
- First-party operating / deployment modes considered: interactive TUI, direct prompt operation, supported subagent/task delegation, persistent/resumed local sessions, and bounded ask/allow/deny tool permissions. No provider-backed live run was performed for this assessment.
- Recursion level: one operator-launched first-party coding-agent session, with optional child agents contained inside this session, rather than the overall OSS project or all installations.
- Reviewed revision: `5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4` (default `dev` at pinning); do not interpret subsequent commits as evaluated.
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/README.md) describes a first-party Rust executable with model integrations, file/shell/search tools, append-only journaling, permission rules and optional subagents. Crucially, the code itself includes a model/tool continuation loop: [`crates/harness-core/src/coord/turn/worker.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/turn/worker.rs) `Worker::converse` repeatedly obtains provider responses, handles returned tool calls, runs tools, appends results to conversation messages and continues until a final answer. [`coord/turn.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/turn.rs) queues user requests into coordinator tasks and agent identities. [`coord/tools/execution.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/tools/execution.rs) runs first-party tool implementations and records completion/result events. [`coord/permissions.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/permissions.rs) applies permission policy, emits `PermissionRequested`, records a pending human gate and defaults a timeout to deny.

Subagent machinery spans [`coord/public_subagents.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/public_subagents.rs), [`coord/children.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/children.rs) and [`crates/harness-tools/src/subagents.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-tools/src/subagents.rs). Sessions and event materialization are in [`session.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/session.rs) and [`store.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/store.rs). These support child work, handoffs, resumption and observation but do not automatically constitute distinct S2/S3/S3*/S4 ownership. The GitHub repo's test/CI suite is a development surface, not a live runtime supervisor; documented reviewer/security-reviewer children require separate scrutiny of the independence and correction path.

## Operational model

A user prompt becomes a scheduled turn of a local session. The first-party worker assembles conversation context and sends a provider request. A model response chooses textual continuation or concrete tool calls; on tool calls, first-party registration, permission checks and execution run the tools, capture results and return them into model context. The model can then choose follow-up tool actions or finish. Permission prompts can pause/block a tool and return an operator choice; they do not make the human author of each coding step. Child-agent execution can be invoked for narrower work, with the parent/coordinator preserving the event and result path.

The owner counterfactual for S1: removing the model-selected actions leaves the executable with deterministic queues, tools, permissions, event replay and a mock, but not the ability to choose next engineering operations. Removing the Rust coordinator leaves the external model endpoint without this repository's first-party tool execution and return path. At the declared *combined installed coding-harness* boundary, the supported model-steered actor owns operational task discretion while the coordinator enforces and records it.

## S1 — Operations

- State: A
- Function: execute one coding/inspection task through model-selected tool actions and observation-dependent continuation.
- Disturbance / variety regulated: unknown file/project state, command results, errors and changing requirements within the operator's task.
- Decisive decision or feedback right: choose the next file/tool/shell action from the evolving prompt/observations or stop with an answer.
- Decision owner: model-driven coding-agent actor in the first-party turn worker; external API supplies model computation, not an external prebuilt coding-agent harness.
- Supporting / enforcement mechanisms: `Runtime::queue_turn`, provider request, registry, execution semaphore, permissions, tool result journal, session context and optional subagents.
- Closure path: user turn → provider response with calls → permission/dispatch → `run_tools` → `after_tools` → `update_prompt` → another `provider_response` or final answer.
- Boundary reachability: `crates/harness-core/src/coord/turn/worker.rs` executes this loop as the normal turn-worker path, not in examples, CI or an imported third-party coding agent. Standard CLI/TUI users enter the coordinator and can enable installed tool registry.
- Why this is / is not agent-owned: nontrivial next-action selection comes from a model rather than a fixed tool script. The coordinator's limits and human allow/deny permissions constrain execution but do not prescribe the full action sequence.
- Evidence: [`coord/turn/worker.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/turn/worker.rs), [`coord/turn.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/turn.rs), [`coord/tools/execution.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/tools/execution.rs).
- Basis: explicit.
- Confidence: high for code-path existence; runtime inference not independently executed.
- Caveats: tool access and final coding quality depend on permissions, environment and provider availability.

## S2 — Coordination

- State: —
- Function: no S2-specific inter-S1 conflict attenuation loop is established at the local session recursion.
- Disturbance / variety regulated: concurrent tool use, waiting tasks, subagent scheduling and potential workspace conflicts; these do not alone show specific interference between separate operational S1 units.
- Decisive decision or feedback right: adjudicate inter-S1 interference and return a coordination judgment altering subsequent S1 work.
- Decision owner: none evidenced for an S2-specific relation; session coordinator applies scheduling and tool-level constraints while the parent chooses subagent work.
- Supporting / enforcement mechanisms: children lifecycle, tools semaphore, task queue, journal and subagent outputs.
- Closure path: tools and children complete and return observations, but that general work routing is not independently established as conflict-specific S2 attenuation.
- Why this is / is not agent-owned: delegating to workers and limiting capacity are not an evidenced oscillation/collision regulation relation across distinct S1s.
- Evidence: [`coord/children.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/children.rs), [`coord/tools/execution.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/tools/execution.rs), [`crates/harness-tools/src/subagents.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-tools/src/subagents.rs).
- Basis: structural, bounded negative.
- Confidence: medium.
- Caveats: an externally configured multi-agent workflow may supply interference mediation beyond the evidence of this frozen standard operation.

### Absence scope

- Surfaces inspected: advertised subagent modes, child lifecycle, general turn scheduler, execution semaphore and tool results.
- Plausible first-party paths checked: parent/child task handoff, queued and background tool calls, concurrent child work, session memory/journal and explicit per-tool permissions.
- Why no material first-party path remains: observed coordination facilities manage work distribution and resource availability; no distinct disturbance-specific feedback regulation among multiple autonomous S1 operations was established at this recursion.

## S3 — Inside-and-now control

- State: —
- Function: no global current-control function governing a whole operational S1 portfolio at this session boundary is established.
- Disturbance / variety regulated: active-turn cancellation, permission violations, tool capacity, context-length pressure and prompt steering.
- Decisive decision or feedback right: reallocate shared S1 priorities/resources/commitments on a whole-system current view, with returned intervention.
- Decision owner: first-party fixed constraints and operator inputs control local session execution; no independent S3 discretionary owner is evidenced.
- Supporting / enforcement mechanisms: coordinator task queue, steering, lifecycle management, max iterations, cancellation, permission grant and session status.
- Closure path: local operations can be paused, denied, steered or ended; no separately evidenced whole-system current view → current-control decision → returned cross-S1 change.
- Why this is / is not agent-owned: scheduling, quotas and permission interrupts do not establish S3 simply because a coordinator owns them.
- Evidence: [`coord/turn.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/turn.rs), [`coord/lifecycle.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/lifecycle.rs), [`coord/permissions.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/permissions.rs).
- Basis: structural, bounded negative.
- Confidence: medium.
- Caveats: human management across multiple sessions or repositories is outside this included single-session recursion.

### Absence scope

- Surfaces inspected: central coordinator, session turn queue, child states, permission/gating and user steering.
- Plausible first-party paths checked: agent-wide active-state dashboard, limits, task interventions, user-selected child spawning and parent/operator oversight.
- Why no material first-party path remains: controls target local turns and optional child execution, without a proven global S1-portfolio current-control decision and return path.

## S3* — Complementary audit

- State: ?
- Function: distinct source-inspecting review children are supported in the standard interface, but their independence and corrective return at the declared runtime boundary have not been established with sufficient source coverage for S3*.
- Disturbance / variety regulated: incorrect code changes, unsafe tool use or inadequate subagent deliverables.
- Decisive decision or feedback right: independently assess operational evidence through a complementary path, return a finding that drives correction.
- Decision owner: possible model-driven reviewer child, dispatched by the parent; not verified as an independent corrective authority in the shipped first-party wiring.
- Supporting / enforcement mechanisms: named reviewer/security-reviewer subagents, optional child execution, shared event journal and parent-facing child outputs.
- Closure path: a reviewer may return messages, but the necessary complementary access/independence and correction-to-operation path remain unresolved. General model self-checks and CI are not a substitute.
- Why this is / is not agent-owned: a distinct child role could make an independent judgment, but a label and delegation alone do not prove an operationally complementary auditor or corrective closure.
- Evidence: [README](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/README.md), [`coord/public_subagents.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/public_subagents.rs), [`crates/harness-tools/src/subagents.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-tools/src/subagents.rs).
- Basis: explicit availability of child roles, unknown function-specific closure.
- Confidence: low.
- Caveats: no distinct operational auditor trace or configured enforcement of independent reviewer ownership was tested.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective environmental intelligence/adaptation loop is established.
- Disturbance / variety regulated: changing model abilities, project conventions, tool ecosystem and prospective workflows.
- Decisive decision or feedback right: judge future adaptation options based on external sensing, then return a changed capability/commitment into present operations.
- Decision owner: operator selects models/skills/configuration and project maintainers evolve releases; no first-party S4 owner/closure evidenced.
- Supporting / enforcement mechanisms: provider catalog, plug-in tools, user skills, configurable profiles, compaction, session fork/replay and hooks.
- Closure path: static configuration/skills can affect a subsequent turn, but no demonstrated external future-oriented detection → organizational adaptation choice → returned capability change.
- Why this is / is not agent-owned: tooling extensibility and response to current tool feedback belong to S1/local control, not necessarily S4.
- Evidence: [README](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/README.md), [`config.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/config.rs), [`provider_catalog.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/provider_catalog.rs).
- Basis: structural, bounded negative.
- Confidence: medium.
- Caveats: user-authored adaptation workflows are not first-party closed S4.

### Absence scope

- Surfaces inspected: provider selection, skills/hooks, config and repository docs, session state/replay and development/eval surfaces.
- Plausible first-party paths checked: agent-config modifications, model fallback, persistent memory, runtime skills, learned policy and automatic external-trend sensing.
- Why no material first-party path remains: no shipped procedure at this boundary establishes an autonomous or closed parent adaptation judgment over future environment coupled to operational capability change.

## S5 — Policy and identity

- State: —
- Function: no ultimate-policy/organizational identity adjudication loop is established for a local coding session.
- Disturbance / variety regulated: prohibited shell commands, out-of-workspace paths, user-approved permission exceptions and selected safety modes.
- Decisive decision or feedback right: resolve conflicting fundamental purposes/authority and return a binding ultimate-policy decision affecting the current organization.
- Decision owner: user/operator supplies permission rules and approvals; fixed engine enforces these rules. No supported identity-level governance decision loop with returned authorization is established.
- Supporting / enforcement mechanisms: permission policy allow/ask/deny and timeout, local config, prompt instructions, user steering and human CLI gate.
- Closure path: tool request → local policy evaluation → optional operator allow/deny → tool execution/denial. This is local permission enforcement, not a returned ultimate-policy decision over system identity.
- Why this is / is not agent-owned: prompt rules and operator gate ownership do not create first-party S5 decisional authority or the specific parent-mode closure required for `P`.
- Evidence: [`coord/permissions.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/coord/permissions.rs), [`config/permissions.rs`](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/crates/harness-core/src/config/permissions.rs), [README](https://github.com/urbanbreach/agent-harness/blob/5d2a15952ee86ea6cc3dfa8bc265b13f78c7d0a4/README.md).
- Basis: structural, bounded negative.
- Confidence: medium-high.
- Caveats: legitimate host organization can formulate broader policy externally, but is not included in this session.

### Absence scope

- Surfaces inspected: permission config, user asks, runtime limits, agent profiles, sessions and project contributor/release surfaces.
- Plausible first-party paths checked: human permission requests as a parent mode, system prompt edits, hard risk policies, agent/tool role restrictions and operator-driven scope changes.
- Why no material first-party path remains: the evidenced path authorizes specific actions under existing policy rather than admitting identity disputes, deciding ultimate policy and returning a binding policy-level change.

## Recursion

One human-launched terminal coding-agent process with a first-party model-steered S1 and optional subagents. Child agents may be independently model-driven S1 at a lower recursion, but their presence alone does not prove their mutual S2 or a current-control metasystem at the assessed local-session boundary. The global project/community is not included.

## Variety and escalation

Prompts and tool outputs drive the S1 reasoning and execution loop; failure, permission denial, interruption and external provider conditions are handled through retry, steering and turn completion where supported. A permission question reaches the human for a *local tool* decision. Session records support replay and inspection, not an algedonic channel or a free-standing S3/S5 decision.

## Evidence gaps

- No provider-backed run, sample trace or external testing was conducted; source evidence establishes execution paths but not reliability or task success.
- The conditional reviewer/security-reviewer child arrangement requires a narrower source/trace investigation of independently sourced artifacts and returned corrective feedback before resolving S3* from `?`.
- No claim is made that the demonstration video, CI or offline replay establishes runtime S3/S4 functions.
