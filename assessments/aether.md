---
harness_id: aether
project_name: Aether
repository: https://github.com/Aetherdz/aether
review_ref: 7476a0336bd47fa01dc2feb03d9572155395da47
reviewed_at: 2026-10-11
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

# Aether

## Review boundary

- System in focus: first-party Rust Aether terminal coding agent, its plan/build/route model-guided operational loop and supported CLI/TUI, with native sandboxed tool calls, model/provider adapters, session persistence and sync, and MCP session-context serving. The assessment recursion is one installed terminal agent controlling user-directed workspace work.
- Purpose and identity: perform user-chosen coding actions and request-level plan/build/route cycles with selected local/cloud models, maintaining sessions and permitting explicit consent for risky file or shell operations.
- Relevant environment: workspace source files, shell command outputs, model-provider responses, human terminal approvals, persisted sessions and devices that share transcripts via local folder/GitHub gist.
- Standard-distribution boundary: the exact pinned open Rust workspace and shipped cargo binary/CLI/TUI crates. Planner, builder and router are separate model roles inside one first-party coding operation; the adjacent repository CI, user organization, upstream inspiration blueprints and external model providers are not imported as organizational owners. Cross-device transcript storage is session synchronization, not a team of autonomous operational agents.
- Credited operating / distribution surfaces: [Cargo.toml](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/Cargo.toml); [crates/aether-cli/src/main.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-cli/src/main.rs); [crates/aether-cli/src/cli.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-cli/src/cli.rs); [crates/aether-agent/src/agent.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/agent.rs); [crates/aether-agent/src/plan.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/plan.rs); [crates/aether-agent/src/route.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/route.rs); [crates/aether-agent/src/prompts.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/prompts.rs); [crates/aether-agent/src/tools.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/tools.rs); [crates/aether-agent/src/observer.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/observer.rs); [crates/aether-agent/src/undo.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/undo.rs); [crates/aether-core/src/sandbox.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-core/src/sandbox.rs); [crates/aether-provider/src/client.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-provider/src/client.rs); [crates/aether-sync/src/lib.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-sync/src/lib.rs); [crates/aether-session/src/lib.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-session/src/lib.rs); [crates/aether-mcp/src/lib.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-mcp/src/lib.rs); [crates/aether-tui/src/agent_screen.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-tui/src/agent_screen.rs).
- Adjacent first-party surfaces excluded from ownership: [.github/workflows/ci.yml](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/.github/workflows/ci.yml), [docs/security-audit.md](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/docs/security-audit.md), [benchmark/results.txt](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/benchmark/results.txt) and [docs/build-plan-v3.md](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/docs/build-plan-v3.md) are development, documentation or benchmarking evidence rather than runtime S3* auditing or policy; [docs/rust-migration-blueprint.md](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/docs/rust-migration-blueprint.md) describes design, not deployed ownership. The external model API and human local policies are external actors, not first-party S4/S5 authorities.
- First-party operating / deployment modes considered: `aether agent TASK` three-role loop with configurable model IDs, continuation from serialized checkpoint, native file/diff approval and command allow-list, CLI/TUI observer, session list/show/resume, sync via gist/folder merge, MCP session tools, static sandbox constraints and optional provider selection.
- Recursion level: one installed Aether instance's coding task, not its maintainers' engineering organization. Different role-model requests are consecutive parts of a single task; synchronization between historical device sessions does not make first-party concurrently operating autonomous peers.
- Reviewed revision: 7476a0336bd47fa01dc2feb03d9572155395da47.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [crates/aether-cli/src/cli.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-cli/src/cli.rs) command definitions and [crates/aether-cli/src/main.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-cli/src/main.rs) dispatch invoke [crates/aether-agent/src/agent.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/agent.rs) `Agent` for an explicit request or resume. The agent makes a planner model request to produce a structured plan, then runs builder-model tool rounds through [crates/aether-agent/src/tools.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/tools.rs) in a workspace-constrained sandbox. A separate router model request receives the user's task, current plan, **builder summary** and prior loop history, parses a `Done`, `Continue` or `Revise` verdict ([crates/aether-agent/src/route.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/route.rs)), and routes another build round or terminates. This gives a genuine model-directed operational closed feedback loop for the *one* user task.

[crates/aether-agent/src/agent.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/agent.rs) persists in-flight progress to `.aether-agent-state.json` and permits resume at the same plan/iteration and feedback history after interruption. Caps on iterations, tool calls, stagnation, command timeout and allow-listed path handling are operational bounds. [crates/aether-agent/src/observer.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/observer.rs) sends phase transitions to the TUI for presentation; by design, the observer is fire-and-forget and does not return a separate decision to the model loop. Risky file writes and shell commands require user approval under [crates/aether-agent/src/tools.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/tools.rs) and [crates/aether-core/src/sandbox.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-core/src/sandbox.rs); a fixed permission classifier is not identity-level VSM policy authority.

[crates/aether-sync/src/lib.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-sync/src/lib.rs) merges session transcripts by line timestamps and deduplication and stores/pulls them via a gist or folder backend, without native inter-S1 workload assignment or conflict arbitration. [crates/aether-mcp/src/lib.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-mcp/src/lib.rs) shares those sessions with external editors/agents as context tools, not their model choices or organizational control. Provider routing is for current inference and not a future-facing capability management process.

## Operational model

One first-party coding operation uses model-guided planning, iterative tool execution, and another model-guided completion/continue/revise judgment. The router's verdict does affect later builder behavior, which strongly establishes **S1=A**, but both roles regulate the completion of the *same* user task. No distinct independently accountable first-party S1 workplace units, organization-wide current-control owner, sufficiently independent raw-artifact audit, externally prospective adaptation or identity-policy closure is observed.

## S1 — Operations

- State: A
- Function: execute user-directed coding/investigation through native tool calls, model-selected build actions and feedback/revision of the task plan.
- Disturbance / variety regulated: underspecified coding requests, new workspace file state, tool failures, stalled or incomplete implementation, provider output ambiguity, iteration limits and interrupted runs.
- Decisive decision or feedback right: builder model selects file/search/command actions; router model chooses whether the task should continue, revise or finish after observing builder summary/loop history. These are mutually supporting first-party decisions within one operation.
- Decision owner: first-party model-directed builder/router roles under Rust Agent's task loop, not the provider transport or the user permission gate.
- Supporting / enforcement mechanisms: planner schema/parser, sandboxed tools, persisted checkpoint, router verdict parser, file-diff review prompt, static risk classifier, timeout and iteration/stagnation guards.
- Closure path: request → planned task → builder-model selected real tool calls → tool results and summary → router-model decision to `Done/Continue/Revise` → revised builder plan/history in subsequent iteration or terminal answer.
- Boundary reachability: [crates/aether-cli/src/main.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-cli/src/main.rs) constructs and invokes the [crates/aether-agent/src/agent.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/agent.rs) loop from the documented `aether agent` CLI; `run_from`, `build_round` and `route` dispatch native functions, with model/tool responses wired back to the next role.
- Why this is / is not agent-owned: removing the model judgments leaves parsing/sandbox tools, but no context-dependent tool selection or discretionary decision whether to continue/modify the plan.
- Evidence: [crates/aether-agent/src/agent.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/agent.rs); [crates/aether-agent/src/route.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/route.rs); [crates/aether-agent/src/plan.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/plan.rs); [crates/aether-agent/src/tools.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/tools.rs); [crates/aether-cli/src/main.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-cli/src/main.rs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: plan/build/route can use three provider model IDs without becoming three separate concurrent operational S1 organizations.

## S2 — Coordination

- State: —
- Function: no first-party conflict attenuation among multiple distinct concurrently operating S1 units is evidenced at this recursion.
- Disturbance / variety regulated: different model roles may disagree over task completion, and session copies may conflict or overlap after cross-device sync; the former is one task's feedback, the latter concerns transcript replication rather than active S1 work interference.
- Decisive decision or feedback right: no native active peer-resource collision arbitration or regulator returning correction to competing S1 units is established. Router decision routes the *single* builder, and sync merges stored session lines.
- Decision owner: the task's router/model for its own operative next step and fixed session sync algorithm for stored text; neither owns an S2-specific inter-S1 coordination loop.
- Supporting / enforcement mechanisms: sequential role model calls, deterministic session merge, sandbox constraints and TUI status.
- Closure path: router returns continue/revise/done to the same coding operation; cross-device sync merges historical messages but does not coordinate independently operating active peers.
- Why this is / is not agent-owned: a plan-vs-build distinction and several models in sequence are not separate S1 peers with collisions; deterministic transcript reconciliation is not S2 work-interference feedback.
- Evidence: [crates/aether-agent/src/agent.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/agent.rs); [crates/aether-agent/src/route.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/route.rs); [crates/aether-sync/src/lib.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-sync/src/lib.rs); [crates/aether-mcp/src/lib.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-mcp/src/lib.rs); [crates/aether-session/src/lib.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-session/src/lib.rs).
- Basis: structural.
- Confidence: high within one-installation boundary.
- Caveats: a separate editor using MCP or several human devices may exercise external coordination not native to this coding-agent controller.

### Absence scope

- Surfaces inspected: plan/build/route orchestration and observer, CLI/TUI, session sync/merge, MCP, sandbox and tool access.
- Plausible first-party paths checked: active multiple independently tasked S1 workers, coordination of shared resources/conflicting writes, peer feedback/locking/assignment and an S2-specific response closing interference into later behavior of competing operational units.
- Why no material first-party path remains: shipped model roles serve one sequential task, observer is one-way UI status, sync operates on historical transcripts and MCP exports context; no first-party active-peer interference relation is wired.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current management across separately operating S1 commitments/resources is evidenced beyond one coding task.
- Disturbance / variety regulated: multiple build attempts, stalled progress or alternate plans affect the user's task, but no portfolio/organizational allocation involving other current operative units exists.
- Decisive decision or feedback right: the router chooses to continue/revise/finish *one* task, not to reprioritize an organization of independently operating S1 systems.
- Decision owner: one task's router/model operating within S1, no separate first-party whole-current management owner.
- Supporting / enforcement mechanisms: iteration state, plan update, router role, TUI phase observer, checkpoint and explicit user approval.
- Closure path: build summary → router verdict → subsequent build of same task; nothing applies a whole-current management judgment to multiple organizational operations.
- Why this is / is not agent-owned: an agent-owned operational control of one task is not automatically a whole-current S3 management system, even with specialized plan/route model roles.
- Evidence: [crates/aether-agent/src/agent.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/agent.rs); [crates/aether-agent/src/route.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/route.rs); [crates/aether-agent/src/observer.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/observer.rs); [crates/aether-tui/src/agent_screen.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-tui/src/agent_screen.rs).
- Basis: structural.
- Confidence: high.
- Caveats: user may run many independent Aether instances, but the user organization is outside the selected first-party boundary.

### Absence scope

- Surfaces inspected: single-task plan/build/route owner, TUI status and observer, session store, sync, model selection/CLI and tool approvals.
- Plausible first-party paths checked: multiple active organizational commitments, global resource/status view, current-control arbitration/priority choices and return of those decisions to multiple operational units.
- Why no material first-party path remains: there is a single request-centric plan/build/route loop with no separate current portfolio or first-party workforce oversight.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary operational reality access and substantive audit judgment returned to current control was established.
- Disturbance / variety regulated: the builder can make erroneous completion claims and miss code defects, but the router receives the builder's summary and prior conversation rather than an independently sampled workspace/test ground truth.
- Decisive decision or feedback right: router's task-completion verdict is ordinary progress routing using the producer's report; `AgentObserver` provides event/status output to the UI, not an independent artifact evaluator or feedback owner.
- Decision owner: task router model for ordinary plan/build continuation; no first-party alternative auditor with a distinct evidence access/return to S3.
- Supporting / enforcement mechanisms: model route prompt, output verdict schema, file diff approval preview, static tool/sandbox checks, TUI observer and maintainer security docs.
- Closure path: summary → route verdict → same operational loop; audit-specific independent observation → findings → separate control correction is absent.
- Why this is / is not agent-owned: a second model can criticize summary but it has no evidenced independent raw-artifact inspection/test/replay mandate and no distinct returned organizational control route; a completion router and ordinary source guards do not become S3* by role name.
- Evidence: [crates/aether-agent/src/agent.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/agent.rs); [crates/aether-agent/src/route.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/route.rs); [crates/aether-agent/src/prompts.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/prompts.rs); [crates/aether-agent/src/observer.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/observer.rs); [crates/aether-agent/src/tools.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/tools.rs); [docs/security-audit.md](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/docs/security-audit.md).
- Basis: explicit + structural.
- Confidence: high for the bounded open source.
- Caveats: an external user-run verifier or independent test suite may challenge Aether, but this source review does not import that outside audit authority.

### Absence scope

- Surfaces inspected: router's concrete inputs, observer's unidirectional phase callback, test/benchmark artifacts and release CI, tool safety gates, MCP session access.
- Plausible first-party paths checked: independently selected primary evidence, raw-artifact verification or replay, distinct auditor judgment, findings return to whole-current control and later operational correction.
- Why no material first-party path remains: router receives the builder's reported summary and loop history only, while observers broadcast UI telemetry and maintainer CI is development-time; no alternate in-boundary auditor access/decision/returned control loop is implemented.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally prospective sensing and future capability-adaptation options linked back to current operational control is evidenced.
- Disturbance / variety regulated: changing provider configuration, stored cross-device context and codebase changes provide current execution inputs, not a strategy process for future capability.
- Decisive decision or feedback right: user sets provider/models and requests current task; model route feedback adapts today's plan, not future organization capabilities.
- Decision owner: current task model and user settings, not a native S4 alternative-development owner.
- Supporting / enforcement mechanisms: model registry, provider selection, session sync, saved context, CLI/TUI, plan revision.
- Closure path: altered context or provider settings change the next coding request; no outside/future sensing → alternative capability option → conversation with current organizational management → implementation closure.
- Why this is / is not agent-owned: plan revisions, model choice, history sync and checkpoint resume are operational current-task mechanisms rather than forward intelligence.
- Evidence: [crates/aether-agent/src/agent.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/agent.rs); [crates/aether-provider/src/registry.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-provider/src/registry.rs); [crates/aether-sync/src/lib.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-sync/src/lib.rs); [crates/aether-session/src/lib.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-session/src/lib.rs); [README.md](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: independently governed teams deploying Aether can plan long-horizon changes, but their externally exercised strategic decisions are not a first-party S4 mode.

### Absence scope

- Surfaces inspected: provider registry/model selection, agent plan/route, sync, session/recall, MCP, TUI and public documentation.
- Plausible first-party paths checked: systematic prospective external change detection, future capability-option development, comparative evaluation and returned decision to change current system capacity.
- Why no material first-party path remains: source-backed model roles and supporting tools focus on the current coding task or session transport; no externally prospective capability loop is implemented.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy conflict adjudication and binding return path exists.
- Disturbance / variety regulated: dangerous tools, path escape risks, command approvals, provider settings and CLI safety are enforced at operation level; they do not resolve a mission/identity dispute.
- Decisive decision or feedback right: human operator grants/denies a risky command/file write or configures allow lists; static sandbox rejects invalid paths. No ultimate authority settles S3–S4 tensions in a parent mode.
- Decision owner: user for local consent and developer-defined tool safety rules for deterministic enforcement, not an evidenced S5 actor.
- Supporting / enforcement mechanisms: `ConfirmPolicy`, shell risk classification, path sandbox, allow-list file/environment, default refusal without interactive TTY, CLI config and provider setup.
- Closure path: attempted tool call → fixed risk rule/user confirmation → current task continues or aborts; no identity issue → ultimate-policy judgment → durable governance return to operational management.
- Why this is / is not agent-owned: sandbox/permission checks are important security mechanisms, not system-wide policy/identity decisions by legitimate organization authority.
- Evidence: [crates/aether-agent/src/tools.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-agent/src/tools.rs); [crates/aether-core/src/sandbox.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-core/src/sandbox.rs); [crates/aether-cli/src/main.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-cli/src/main.rs); [crates/aether-core/src/config.rs](https://github.com/Aetherdz/aether/blob/7476a0336bd47fa01dc2feb03d9572155395da47/crates/aether-core/src/config.rs).
- Basis: structural.
- Confidence: medium-high.
- Caveats: maintainer SECURITY.md and user policy may govern installations externally, but they do not supply an implemented first-party S5 parent return.

### Absence scope

- Surfaces inspected: native tool approvals, command-risk policy, file sandbox and user allowlist, config/provider selection, release/docs and plan/router.
- Plausible first-party paths checked: detection of an ultimate identity/mission conflict, legitimate policy decision, integration of present/future system tradeoffs and durable binding feedback into subsequent organizational control.
- Why no material first-party path remains: implemented policy is local execution safety/user consent with no higher-order identity authority or returned organization-wide decision.

## Recursion

Planner, builder and router are separate requested model roles participating in one operational task, not a persistent organization of three independently accountable S1 units with their own conflicting commitments. The router evaluates builder summaries to alter the next build turn; this is S1 operational regulation. MCP and sync expose session context to external users and editors without incorporating their managerial/policy decision ownership. The user's organization and the OSS maintainer/release ecosystem lie at different boundaries.

## Variety and escalation

A coding task may encounter tool errors or stalled iterations. Aether attenuates variety with sandbox/permission checks and capped/stagnation detection; amplifies awareness through real tool observations, plan and history; and adapts S1 behavior when the router issues revise/continue. Observer events present progress to humans but do not act on operational outcomes. Session sync handles message duplication/timestamp order, not multi-worker commitments. No S2, S3, complementary S3*, prospective S4 or ultimate S5 closed path was established.

## Evidence gaps

This source-first assessment is pinned to the exact public Rust revision; the tool workspace did not execute a full cargo/provider-backed integration run, so real-world reliability is not inferred. The positive S1 evidence is first-party control-flow wiring and source tests. The bounded negative classifications do not prove absence across hypothetical integrations, externally coupled management, or future Aether releases. The router's source-confirmed completion judgment uses builder summary and loop history, not independently acquired operational truth, explaining the negative S3* rather than an assumed audit credit.
