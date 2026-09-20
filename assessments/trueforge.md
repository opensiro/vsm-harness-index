---
harness_id: trueforge
project_name: TrueForge
repository: https://github.com/truefoundry/trueforge
review_ref: 651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# TrueForge

## Review boundary

- System in focus: one configured TrueForge agent session using the first-party agent execution harness, model/tool feedback loop, MCP/local tools, sandbox/filesystem, dynamic subagents, context compaction, session persistence, skills/plugins, approvals and supported gateway/CLI surfaces.
- Purpose and identity: execute open-ended multi-step user/application work autonomously with tools while the root agent may decompose selected subtasks into isolated parallel subagents and synthesize their returned results.
- Relevant environment: user/application requests, tool/MCP responses, sandbox/filesystem state, external information sources, configured model providers, approval decisions and persistent session context.
- Standard-distribution boundary: first-party `trueforge-core` runtime, built-in capabilities, TrueForge server/gateway/CLI wiring, dynamic subagent orchestration, approvals and persistence. Model providers, remote MCP servers, user-authored skills/plugins and application-specific business logic remain external unless TrueForge itself closes the claimed organizational function.
- Credited operating / distribution surfaces: public `AgentThread`/`AgentThreadOrchestrator` runtime, first-party model/tool loop, `DynamicSubAgents`, local/MCP tool execution, sandbox/filesystem, context/session machinery and supported CLI/gateway invocation.
- Adjacent first-party surfaces excluded from ownership: contributor/CI/release machinery, UI presentation logic except where it transports an approval decision, repository tests/evals, documentation publishing and TrueFoundry organizational governance outside a running agent session.
- First-party operating / deployment modes considered: ordinary headless/CLI/gateway agent execution with default dynamic subagents enabled, tool approvals as configured, sandbox/tools, persistent sessions and context compaction.
- Recursion level: one root TrueForge agent session. Dynamically spawned subagents are bounded delegated workers inside that root task unless evidence establishes a higher organizational recursion with separate current-control organs.
- Reviewed revision: `651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

TrueForge ships a headless agent execution harness. The documented execution cycle is user prompt → model → tool call → tool execution/result → model until a final answer. The public core exports `AgentThread` and `AgentThreadOrchestrator`, tool/MCP contracts, context compaction, web search, sandbox/skills and dynamic subagents.

Dynamic subagents are enabled by default. The root agent decides at runtime whether to delegate, generates a self-contained instruction and calls the first-party `create_sub_agent` tool. Multiple subagents may run concurrently, share the parent's tools/sandbox, and return only their final result. The root waits until the subagents finish and then continues its own model loop. The runtime orchestrator tracks active threads, executes leaf threads in bounded parallel batches and transports each completed child result back to its parent thread.

This is strong autonomous task decomposition, but the reviewed boundary does not establish a separate S2 or S3 organ. No specific inter-S1 conflict/oscillation is identified for S2. For S3, the thread map and execution scheduler are deterministic runtime machinery; the root chooses whether and what to delegate, but while children run it waits for their results rather than receiving a whole-system current view and exercising a distinct portfolio intervention right over their ongoing commitments.

Primary evidence:

- [`README.md`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/README.md) — product boundary, autonomous agent loop, tools, sandbox, persistence, context compaction, subagents, approvals and gateway/CLI surfaces.
- [`docs/key-features/subagents.mdx`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/docs/key-features/subagents.mdx) — root-owned delegation decision, generated child instructions, parallel isolated execution, wait/collect/synthesize behavior and one-level delegation boundary.
- [`packages/trueforge-core/src/core/capabilities/builtins/DynamicSubAgents.ts`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/packages/trueforge-core/src/core/capabilities/builtins/DynamicSubAgents.ts) — first-party `create_sub_agent` tool, child identity, shared tools/sandbox and delegated-task contract.
- [`packages/trueforge-core/src/core/runtime/AgentThreadOrchestrator.ts`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/packages/trueforge-core/src/core/runtime/AgentThreadOrchestrator.ts) — active-thread tracking, bounded parallel child execution, approval/auth stop conditions and child-result return to parent.

## S1 — Operations

- State: A
- Function: autonomously execute an open-ended user/application task by choosing substantive tool, sandbox, delegation and final-response actions from observed results.
- Disturbance / variety regulated: task ambiguity, external/tool results, filesystem state, errors, large unstructured responses, context pressure and intermediate findings discovered during execution.
- Decisive decision or feedback right: choose the next substantive model/tool action, decide whether a focused subtask should be delegated, generate the delegated instruction and synthesize returned results into later task decisions or the final answer.
- Decision owner: the model-driven root TrueForge agent; a spawned child agent owns its bounded delegated task decisions while active.
- Supporting / enforcement mechanisms: `AgentThread`, model adapter, local/MCP tools, sandbox, session state, context compaction, approval transport and `AgentThreadOrchestrator`.
- Closure path: request/context → model decision → tool execution or child delegation → observation/child result → updated root context → subsequent model action or final answer.
- Boundary reachability: the autonomous root loop and dynamic-subagent capability are exported/shipped first-party runtime paths and are documented as normal TrueForge operation; they do not require downstream code to build the operational feedback loop from generic primitives.
- Why this is / is not agent-owned: deterministic runtime machinery transports calls/results and enforces configured constraints, while the model chooses the substantive actions and delegation decisions from current task evidence.
- Evidence: [`README.md`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/README.md), [`subagents.mdx`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/docs/key-features/subagents.mdx), [`DynamicSubAgents.ts`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/packages/trueforge-core/src/core/capabilities/builtins/DynamicSubAgents.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: child agents are credited only as bounded operational workers inside the root session. Their existence is not used as a shortcut to S2/S3.

## S2 — Coordination

- State: —
- Function: no material first-party S2-specific regulation of a demonstrated interference/conflict/oscillation among distinct S1 units is established at this recursion.
- Disturbance / variety regulated: not established as an S2 disturbance.
- Decisive decision or feedback right: not established as S2.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: root-generated child instructions, parallel child execution, shared tools/sandbox and result merging provide task decomposition/isolation/aggregation.
- Closure path: child results return to the root for task synthesis, but no distinct coordination result is shown attenuating a specific inter-S1 disturbance and changing affected S1 behavior.
- Why this is / is not agent-owned: parallelism, shared state and delegation are generic orchestration mechanisms; Methodology 0.3.5 requires the S2 interference witness before ownership classification.
- Evidence: [`subagents.mdx`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/docs/key-features/subagents.mdx), [`AgentThreadOrchestrator.ts`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/packages/trueforge-core/src/core/runtime/AgentThreadOrchestrator.ts).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: a downstream TrueForge application could define interacting specialist units and an S2 policy, but that separate composition is not imported into this assessment.

### Absence scope

- Surfaces inspected: dynamic subagents, parallel thread execution, shared sandbox/tools, child instruction generation, result return/merge and runtime thread tracking.
- Plausible first-party paths checked: parallel subagent fan-out, shared workspace/tool access, parent-child hierarchy, thread scheduling and child result synthesis.
- Why no material first-party path remains: none identifies a specific inter-S1 interference/oscillation plus a first-party attenuation relation that feeds a coordination result back into affected operational units.

## S3 — Inside-and-now control

- State: —
- Function: no distinct autonomous whole-system inside-and-now control function is established at the declared root-session recursion.
- Disturbance / variety regulated: thread lifecycle, child parallelism, pending approvals/auth and execution termination are regulated by runtime machinery, but not by an evidenced autonomous S3 owner.
- Decisive decision or feedback right: no separate autonomous actor is shown holding a whole-session current operational view and choosing interventions over ongoing commitments/resources/priorities.
- Decision owner: the root model owns local task/delegation decisions; `AgentThreadOrchestrator` deterministically schedules/tracks threads and stops for required external actions.
- Supporting / enforcement mechanisms: active-thread map, leaf-thread selection, bounded parallel batches, thread completion/removal, approval/auth stop conditions and cancellation signal handling.
- Closure path: the runtime starts children, executes active leaves and returns child completion to the root; while multiple children run the root waits for completion rather than observing their current state and exercising a distinct whole-system intervention loop.
- Why this is / is not agent-owned: choosing to delegate is part of S1 task decomposition. The actor that sees/manages the live thread set is deterministic orchestration code, and the root lacks the evidenced project/portfolio-style current-control right required for S3.
- Evidence: [`subagents.mdx`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/docs/key-features/subagents.mdx), [`AgentThreadOrchestrator.ts`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/packages/trueforge-core/src/core/runtime/AgentThreadOrchestrator.ts).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: the runtime has strong execution authority over threads. Enforcement/scheduling authority alone is not autonomous organizational S3 ownership.

### Absence scope

- Surfaces inspected: root/child thread hierarchy, active-thread tracking, parallel execution batches, cancellation, approvals/auth requirements, persistent session/runtime state and gateway/CLI operation.
- Plausible first-party paths checked: root delegation, thread scheduler, live-thread map, approval stops, cancellation and session continuation.
- Why no material first-party path remains: root-agent discretion remains task-local, while whole-thread scheduling/control is deterministic runtime enforcement; no autonomous whole-system current-view → intervention → changed ongoing-operation feedback loop is established.

## S3* — Complementary audit

- State: —
- Function: no materially independent audit/challenge path with complementary evidence and corrective return is established in the standard runtime.
- Disturbance / variety regulated: approvals and ordinary tool/runtime errors constrain execution, but they are not independent audit of S1 claims.
- Decisive decision or feedback right: not established as S3*.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: tool approvals, runtime traces/events, child isolation and ordinary model/tool responses provide control/observability but not a distinct reviewer judgment.
- Closure path: approval-required tools pause for a user decision and traces/events report activity; no separate auditor reviews completed/claimed S1 work from complementary access and returns findings through corrective control.
- Why this is / is not agent-owned: no first-party reviewer/verifier/critic actor or equivalent independent challenge loop was found at the pinned standard boundary; names such as approval or tracing are not reclassified as audit.
- Evidence: [`AgentThreadOrchestrator.ts`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/packages/trueforge-core/src/core/runtime/AgentThreadOrchestrator.ts), [`README.md`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/README.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: a user may manually inspect work or a downstream skill may implement verification, but those are not a shipped independent S3* organ of TrueForge itself.

### Absence scope

- Surfaces inspected: runtime events/tracing, approvals, dynamic subagents, tool responses, sandbox/filesystem and documented built-in capabilities.
- Plausible first-party paths checked: human tool approval, traces/events, isolated child agents and any documented reviewer/verifier/audit/evaluator path.
- Why no material first-party path remains: inspected paths provide execution permission, observability or ordinary delegated work; none closes independent complementary audit judgment into corrective subsequent operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separate prospective environment-facing adaptation loop that changes future harness capability/program is established.
- Disturbance / variety regulated: external search/tool data and persisted context can inform current/future task reasoning, but not through an evidenced S4 organ.
- Decisive decision or feedback right: not established as an adaptation judgment.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: web/MCP tools, session persistence, context compaction, memory-like history, skills/plugins and dynamic subagents expand information/capability access.
- Closure path: retrieved information and persisted/summarized context return to the current/root agent loop; no first-party path autonomously forms adaptation options and promotes a selected change into later TrueForge capability or organizational program.
- Why this is / is not agent-owned: research, memory, context compaction and loading skills are mechanisms. They do not establish S4 without prospective sensing, adaptation selection and return into future capability.
- Evidence: [`README.md`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/README.md), [`core/index.ts`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/packages/trueforge-core/src/core/index.ts).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: user-installed skills/plugins can change capabilities, but configuration/installation by a parent is not itself a first-party autonomous S4 loop.

### Absence scope

- Surfaces inspected: web search/fetch, MCP tools, skills/plugins, context compaction, session persistence, dynamic subagents and documented memory/runtime settings.
- Plausible first-party paths checked: external research, persistent sessions, context summarization/compaction, skill mounting/marketplace and plugin/tool configuration.
- Why no material first-party path remains: these surfaces supply information, persistence and configurable capabilities; they do not close environment sensing → adaptation-option generation/selection → promoted future-capability change.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy closure is established at the root-agent-session recursion.
- Disturbance / variety regulated: system instructions, configured models/tools, approval requirements and runtime settings constrain execution but are not evidenced as identity-level policy disputes.
- Decisive decision or feedback right: not established as S5.
- Decision owner: user/deployer configuration for the inspected policy surfaces.
- Supporting / enforcement mechanisms: agent instructions/spec, MCP/tool selection, `require_approval_for_tools`, permission prompts, `--no-approval`, model/runtime settings and skill/plugin configuration.
- Closure path: configuration and approvals alter allowed operational actions, but no identity/ultimate-policy issue reaches an authoritative S5 actor and returns as governing system identity/policy.
- Why this is / is not agent-owned: prompt, permissions and approval gates are execution constraints, not S5 merely because they constrain the agent or leave final permission with a human.
- Evidence: [`README.md`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/README.md), [`docs/create-agent/overview.mdx`](https://github.com/truefoundry/trueforge/blob/651c574e6ebf8bc2f4c39a00c7f749b4c22d9f88/docs/create-agent/overview.mdx).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: parent users retain substantial configuration and approval authority, but no qualifying S5 function exists to publish `P`.

### Absence scope

- Surfaces inspected: agent instructions/specification, models, MCP/tool selection, approvals, sandbox/runtime settings, plugins/skills and CLI/gateway controls.
- Plausible first-party paths checked: human approval, destructive-tool gates, system instructions, model selection and runtime configuration.
- Why no material first-party path remains: all identified authority is operational/configurational; no identity/ultimate-policy matter → legitimate authority → returned governing-policy closure is evidenced.

## Distributed OSS parent arrangement

TrueForge maintainers and contributors govern development of the repository, but that is an adjacent OSS development recursion and is excluded from a running agent-session assessment. User tool approvals are execution authorization, not automatically parent S3/S4/S5 governance.

## Self-hosted and non-human modes

The harness supports headless and gateway operation and can run with approvals bypassed/configured. This establishes that S1 need not depend on continuous human steering. Conversely, configurable approval modes do not create `(P)` notation where the corresponding S3/S4/S5 function has not first been established.

## Recursion

The root session is the assessed system. Dynamic subagents are one-level-deep, focused workers created by the root and return only results before the root continues. A downstream application that maintains long-lived specialist agents, portfolio supervision or independent reviewers would be a different system-in-focus requiring its own evidence.

## Variety and escalation

TrueForge absorbs task variety through model/tool iteration, sandbox execution, dynamic decomposition, context compaction and user approval/auth pauses. The runtime can stop and wait when approval, client tool response or MCP authentication is required. These escalation/control paths support safe execution but do not independently establish S3, S3* or S5.

## Evidence gaps

No positive S2/S3/S3*/S4/S5 path was found at the frozen revision. Reassessment would be warranted if the standard distribution adds an autonomous supervisor with a live whole-agent portfolio, a separate reviewer/challenger whose findings close into rework, or an environment-facing self-adaptation loop that changes future agent capability.