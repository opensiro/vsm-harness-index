---
harness_id: go-agent-harness
project_name: Go Agent Harness
repository: https://github.com/shalyhinpavel/go-agent-harness
review_ref: 362eef286581c67c8d384369d03873aad0807843
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Go Agent Harness

## Review boundary

- System in focus: one installed Go Agent Harness engine, embedded Go instance, or bundled `harness` CLI/HTTP server running a model-driven tool loop and sessions.
- Purpose and identity: provider-neutral tool-using conversational agent runtime with configurable tools, session history, optional memory, hooks, approval and trace ports.
- Relevant environment: user prompts, configured model provider, files/web/MCP tools, interrupted streams, token/context limits, human approval, and external integrations.
- Standard-distribution boundary: shipped Go `agent`, `llm`, `internal/bootstrap`, `cmd/harness`, `server`, `tools`, `memory`, `mcpclient`, and `trace` components. Embedded callers may supply their own code, but hypothetical applications are not credited as completed first-party organizational functions.
- Credited operating / distribution surfaces: `agent/engine.go`, `agent/loop.go`, `agent/session.go`, `agent/types.go`, `internal/bootstrap/engine.go`, `cmd/harness/chat.go`, `server/server.go` and first-party tool/provider adapters.
- Adjacent first-party surfaces excluded from ownership: provider-conformance `cmd/harness/check.go`, unit/integration tests, `examples/` applications, development/release practices, and downstream programs that may independently build multi-agent coordination or governance from extension hooks. Model-provider cognition is external but is used through the packaged operating path.
- First-party operating / deployment modes considered: interactive CLI, one-shot command, HTTP/SSE server, embeddable `AgentEngine`, optional local memory/compaction, configured MCP tools, and optional human tool approval.
- Recursion level: one agent session or several independent sessions served by a single engine; an individual tool call is not a second viable S1 by definition.
- Reviewed revision: `362eef286581c67c8d384369d03873aad0807843` (source-static), observation date 2026-11-11.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

`internal/bootstrap.BuildEngine` constructs one registry, provider, session manager, optional memory ports/MCP connections and trace sink, then starts `AgentEngine`. `StreamChat` obtains a user-owned session and serializes turns within that session; on each iteration an external model selects zero or more registered tools, receives results and can select further steps. The runtime enforces iteration/context/result-size limits, permits bounded concurrent tool invocations and persists conversation history; a configured approver may reject side-effecting tools. CLI and HTTP/SSE adapt the same engine. File-backed sessions and optional memory survive individual conversations, while JSONL trace records operational events without a separate audit judge. These are verifiable code mechanisms, not an assertion of multi-agent governance. [Bootstrap](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/internal/bootstrap/engine.go), [engine](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/agent/engine.go), [tool loop](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/agent/loop.go), [README](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/README.md).

## Operational model

The installed operational unit is a tool-using language-model agent at one session, operating within configured limits. Its model supplies discretionary next-tool/answer decisions from returned tool and user feedback. The Go runtime owns session isolation, bounded execution and transport; embedding developers configure ports and policy, and optional parent users decide individual tool approvals. Multiple sessions and parallel tool calls are concurrent execution, not demonstrated independently regulated S1 organizations. The tool-interface's sub-agent examples do not automatically add shipped autonomous supervisory units.

## S1 — Operations

- State: A
- Function: convert user tasks into model-selected tool actions and completed conversational results.
- Disturbance / variety regulated: user requests, tool errors/content, changed file/web observations, stream interruptions and context-window pressure.
- Decisive decision or feedback right: choose a registered tool and arguments after reading previous results, or end with an answer; subsequent iterations may revise the choice.
- Decision owner: the configured external model acting through a first-party executable `AgentEngine` loop; Go infrastructure bounds execution but does not select semantic task steps.
- Supporting / enforcement mechanisms: tool registry, provider adapters, parallel call executor, retry/compaction policy, session store, cancellation and opt-in approval.
- Closure path: prompt/session → model tool call → `executeToolsParallel` → tool-result message persisted → next model decision or terminal answer / `done` chunk.
- Boundary reachability: `internal/bootstrap.BuildEngine` wires the shipped CLI/server to `NewAgentEngine`, and `StreamChat` directly calls the configured provider and executes registered model-selected tools.
- Why this is / is not agent-owned: the model has task-level discretion and receives real tool feedback; provider autonomy is credited only within the packaged invocation, not as Go deterministic ownership of model judgment.
- Evidence: [engine turn and model loop](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/agent/engine.go#L370-L555), [tool result/continuation](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/agent/engine.go#L750-L835), [parallel tool executor](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/agent/loop.go#L35-L203), [CLI bootstrap](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/internal/bootstrap/engine.go#L33-L215).
- Basis: structural, first-party shipped code; confidence: high for the described model-driven single-agent loop.
- Confidence: high.
- Caveats: source-static examination; no live provider quality, autonomy performance or model-level identity is inferred.

## S2 — Coordination

- State: —
- Function: no first-party coordination relation regulating interference among distinct autonomous S1 work units is established in the standard runtime.
- Disturbance / variety regulated: simultaneous calls and overlapping turns could conflict, but the shipped guards regulate one session's request lifecycle rather than negotiated interference between distinct operational agents.
- Decisive decision or feedback right: `BeginTurn` rejects concurrent turns of one session; `executeToolsParallel` serializes result order and caps tool fan-out without an agent-level arbitration choice.
- Decision owner: deterministic runtime for per-session exclusion/parallel tool mechanics; no distinct S2 owner or specifically composable inter-agent conflict controller shown.
- Supporting / enforcement mechanisms: session `busy` map, semaphore and stable result slots.
- Closure path: conflicting same-session second request returns busy/error, while independent sessions execute separately; neither is a demonstrated S1-to-S1 coordination feedback loop.
- Why this is / is not agent-owned: neither model nor configurable first-party mediation is shown to select an interference-specific coordination response across independent agent work units.
- Evidence: [session turn guard](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/agent/session.go#L180-L197), [parallel tool result ordering](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/agent/loop.go#L35-L215), [bootstrap one-engine assembly](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/internal/bootstrap/engine.go).
- Basis: bounded structural absence; confidence: medium-high.
- Confidence: medium-high.
- Caveats: external applications can embed several engines and implement S2, but their coordination is not supplied by this distribution.

### Absence scope

- Surfaces inspected: agent/session/loop, engine registry, bootstrap, HTTP session guards, hooks, tool examples and README.
- Plausible first-party paths checked: concurrent tool execution, multiple sessions, same-session busy guard, sub-agent-as-tool example and generic before/after hooks.
- Why no material first-party path remains: no shipped path identifies two distinct autonomous S1 units plus an actual inter-unit disturbance and returns a coordination-specific choice to both later operational units.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control decision loop over a portfolio of operational commitments and common resources is shipped.
- Disturbance / variety regulated: session concurrency, context exhaustion, tool side effects and model iteration budget are controlled locally, but not through a whole-current organizational intervention.
- Decisive decision or feedback right: configured limits and a caller-supplied `Proceed` hook constrain individual turns; no first-party actor surveys current multi-S1 commitments and chooses reassignment, resource bargain or exception intervention.
- Decision owner: embedding developer/operator selects configuration, runtime enforces; optional human approves individual tools (ordinary execution risk, not whole-current S3).
- Supporting / enforcement mechanisms: `MaxIterations`, `MaxParallelTools`, context guard, session TTL, tool approval and SSE broker.
- Closure path: limit/approval refusal changes or ends an individual tool/turn, not a first-party system-wide current-control decision returned to multiple S1 operations.
- Why this is / is not agent-owned: neither hard guard nor generic hook carries discretionary S3 current-control ownership on its own.
- Evidence: [config and hooks](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/agent/types.go), [limits and guards](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/agent/engine.go), [bootstrap](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/internal/bootstrap/engine.go).
- Basis: structural boundary-specific negative; confidence: medium.
- Confidence: medium.
- Caveats: a host program may build current-control policy over many engines, but that is outside this default harness's accountable operating boundary.

### Absence scope

- Surfaces inspected: `AgentConfig`/`ChatRequest`, control hooks, session registry, CLI/server, configuration/approval docs.
- Plausible first-party paths checked: `Proceed`, per-turn approval, busy session guard, iteration/parallelism budgets and shared trace/session use.
- Why no material first-party path remains: these enforce preselected local constraints; no supplied whole-system view with authority to choose and return cross-S1 resource or commitment decisions.

## S3* — Complementary audit

- State: —
- Function: no shipped complementary independent audit judgment/return path beyond normal agent/tool reporting.
- Disturbance / variety regulated: false tool-success claims or hidden operational errors are possible, but event trace alone does not audit the claim.
- Decisive decision or feedback right: none shown: optional trace files record steps and errors; provider conformance `check` tests model adapters outside a production session.
- Decision owner: normal engine records traces and configured user can inspect them later; no separate first-party auditor controls independent evidence and corrective return.
- Supporting / enforcement mechanisms: JSONL `trace.Sink`, stream event chunks, unit tests and live provider conformance checker.
- Closure path: logs are written for inspection/replay; no included audit decision demonstrably changes subsequent session operating authority.
- Why this is / is not agent-owned: model's own turn report and trace sink do not provide independent complementary judgment, and the separate checker belongs to adjacent testing.
- Evidence: [trace semantics and `Record`](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/trace/trace.go), [provider conformance checker](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/cmd/harness/check.go), [bootstrap opt-in trace](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/internal/bootstrap/engine.go#L132-L200).
- Basis: bounded negative after tracing candidate audit surfaces; confidence: medium-high.
- Confidence: medium-high.
- Caveats: trace is useful primary material for an externally composed auditor, not evidence that one ships in this runtime.

### Absence scope

- Surfaces inspected: trace event types and sink, engine recording, provider checker, tests, hooks and README trace documentation.
- Plausible first-party paths checked: JSONL trajectory capture, error warnings, `harness check`, `AfterTool` hook and client human observation.
- Why no material first-party path remains: no complementary sufficiently independent real-artifact judge with audit decision and feedback into later control is wired into the packaged operating mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party outside-and-then prospective environmental option selection and capability-return loop identified.
- Disturbance / variety regulated: changing models, token limits and user memory affect current requests, not strategic future viability choices.
- Decisive decision or feedback right: users/developers select providers and tools; auto-compaction summarizes past history, and memory ports retrieve user data rather than develop future capability options.
- Decision owner: developer/operator configures providers, prompt and memory; the model owns current task steps, not a shipped forward-looking adaptation decision process.
- Supporting / enforcement mechanisms: `PromptAugmenter`, `ContextCompactor`, `AutoCompact`, memory store, MCP registration and model configuration.
- Closure path: summarized history and user dossier enter a later model request; no evidenced external trend → evaluated prospective option → changed durable harness capability → S3 return path.
- Why this is / is not agent-owned: operational context preservation is not strategic learning/adaptation; a possible future custom hook is not a current first-party S4 constructor.
- Evidence: [compaction and prompt ports](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/agent/engine.go), [memory bootstrap](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/internal/bootstrap/engine.go#L58-L95), [README memory design](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/README.md).
- Basis: bounded negative after prospective-path search; confidence: medium.
- Confidence: medium.
- Caveats: model can reason about tomorrow if a user asks it to; this is task behavior, not an included organizational adaptation loop.

### Absence scope

- Surfaces inspected: prompt/memory/compaction code, provider selection, tool/MCP registry, CLI/server modes, README and roadmap.
- Plausible first-party paths checked: summary compaction, user-memory search, provider switching, extension hooks and optional external web tools.
- Why no material first-party path remains: none supplies a prospective environmental options process with persistent capability change and return to current operating control.

## S5 — Policy and identity

- State: —
- Function: no packaged identity/ultimate-policy judgment and legitimate returned decision path.
- Disturbance / variety regulated: action safety, file access, tool-level approvals and user/session isolation are runtime risk policy, not ultimate organizational mission disputes.
- Decisive decision or feedback right: human may approve/deny a tool call and developer can change system prompt, but neither is a shipped process for escalating and resolving mission/identity-level questions.
- Decision owner: external human/developer owns application purpose; Go runtime holds enforcement boundaries, not ultimate policy authority.
- Supporting / enforcement mechanisms: `Approver`, `ApprovalPolicy`, `ReadOnly`, bootstrap file/bash opt-ins, per-user session identity.
- Closure path: tool approval returns a particular execution answer; no first-party route takes an identity/ultimate-policy matter to legitimate parent authority and returns a governing identity decision for future operation.
- Why this is / is not agent-owned: deterministic restrictions and ordinary one-off human consent are not S5, nor is a static prompt.
- Evidence: [tool approval API](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/agent/types.go#L150-L175), [approval execution](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/agent/loop.go#L100-L145), [server approval broker](https://github.com/shalyhinpavel/go-agent-harness/blob/362eef286581c67c8d384369d03873aad0807843/server/server.go).
- Basis: bounded negative; confidence: medium-high.
- Confidence: medium-high.
- Caveats: application authors may add higher-recursion governance, not credited without a shipped first-party mode.

### Absence scope

- Surfaces inspected: system prompt/config, approval, session/user isolation, CLI/server and extension hooks.
- Plausible first-party paths checked: human approval, config changes, model instructions, high-risk tool gates and host-provided callbacks.
- Why no material first-party path remains: observed decisions regulate tool execution, not system identity, ultimate purpose or S3/S4 policy tension with attributable parent decision/return.

## Distributed OSS parent arrangement

Repository contributor governance is outside this one-instance agent-engine distribution. No organization-level S3/S4/S5 parent path is inferred from source code's maintainers, generic embedder or optional HTTP user.

## Self-hosted and non-human modes

The engine can be embedded or served on loopback with operator-selected models and tools. Optional approval provides per-tool parent interaction but not a first-party parent S3/S4/S5 function; the model owns ordinary S1 action selection with or without approval. No self-governing identity-level non-human organization is demonstrated.

## Recursion

One model-driven conversation is the relevant S1 unit. Parallel tools and nested tools with external sub-agents can extend task execution, but neither supplies its own evidenced independent metasystem/recursion or a higher-level control organization as shipped.

## Variety and escalation

Context compaction, tool-result truncation, finite iterations, bounded parallelism, retries, session isolation and approval reduce operational variety/risk; denial/errors feed back to the model or caller. These are not classified as additional VSM functions without the relevant distinct organizational decision rights.

## Evidence gaps

- This is a source-static general assessment of the frozen revision; no paid provider calls, independent auditor or real-user production outcomes were re-executed.
- Optional embedders can compose multi-agent coordination, whole-portfolio resource management or future capability redesign, but those extensions are not standard first-party integrated modes reviewed here.
- Negative states are bounded to the shipped implementation and named plausible paths; no claim of conceptual impossibility is made.
