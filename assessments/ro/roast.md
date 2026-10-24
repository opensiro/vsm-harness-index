---
harness_id: roast
project_name: Roast
repository: https://github.com/Shopify/roast
review_ref: 0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Roast

## Review boundary

- System in focus: the first-party Roast Ruby workflow DSL/runtime at frozen revision `0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c`, including workflow definition/loading, `ExecutionManager`, cog lifecycle, deterministic control-flow primitives, `chat`, `agent`, `cmd`, `ruby`, `map`, `repeat`, `call`, async execution, provider adapters, workflow context and event/output plumbing.
- Purpose and identity: let developers declare structured AI workflows that sequence LLM requests, shell/Ruby work, collection/iteration control and externally implemented coding-agent invocations.
- Relevant environment: workflow author/operator, target files/repositories, shell/Ruby environment, cloud LLM providers, externally installed Pi/Claude Code agent CLIs, model/provider-hosted tools/MCP servers and any application services invoked by custom cogs.
- Standard-distribution boundary: first-party Roast DSL/runtime, cogs, execution/context managers, command runner, provider adapters and bundled runtime configuration. External Pi CLI and Claude Code CLI internals, cloud-provider model/tool loops, model endpoints, externally configured MCP servers and user-defined downstream cogs do not donate autonomous ownership to Roast merely because Roast invokes them.
- Credited operating / distribution surfaces: `lib/roast/workflow.rb`; `lib/roast/execution_manager.rb`; `lib/roast/cog.rb`; built-in `chat`, `agent`, `cmd`, `ruby`, `map`, `repeat` and `call` cogs; `CommandRunner`; agent-provider adapters/parsers; workflow/context/output/event/control-flow plumbing.
- Adjacent first-party surfaces excluded from ownership: tests, tutorial prose, examples used only as demonstrations, repository CI/release/contributor workflows and documentation-only descriptions. Autonomous behavior internal to Pi, Claude Code, provider-hosted tools or other external runtimes is adjacent evidence and is not credited as first-party Roast intelligence.
- First-party operating / deployment modes considered: ordinary declarative workflows; `chat` request/response steps; external `agent` cog calls to Pi or Claude; serial and async cog execution; serial/parallel `map`; `repeat`; reusable `call` scopes; Ruby/shell cogs; session reuse exposed by external agent providers.
- Recursion level: one Roast workflow runtime. External coding-agent CLI processes and provider-side agent/tool loops are separate lower-level systems-in-focus; their autonomy is not inherited by the enclosing Roast repository-relative boundary.
- Reviewed revision: `0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Roast is a substantial first-party workflow mechanism, but the frozen distribution does not close a first-party autonomous operational agent loop. `Workflow#start!` runs a developer-authored `execute` program through `ExecutionManager`. The manager walks the predeclared cog stack, starts each cog, waits according to configured async behavior and computes final output. `map`, `repeat`, `call`, skip/next/break/fail and configuration blocks are Ruby control mechanisms whose topology and decisions come from authored workflow code and deterministic runtime conditions.

The `agent` cog does not implement the coding agent's decision/action/observation loop. `Agent#execute` delegates directly to `provider.invoke(input)`. The shipped Pi and Claude provider adapters construct CLI commands, start external `pi` or `claude` processes through `CommandRunner`, stream/parse those processes' session, turn, tool-use/tool-result and final-response messages, and expose the external result back to Roast. The actual arbitrary-task interpretation, planning, tool choice, environment observation and subsequent action selection occur inside those separately implemented CLI runtimes. Roast can pass prompts/system-prompt options, select models, resume sessions and report tool events, but those integration rights do not transfer the external runtime's autonomous policy into first-party Roast ownership.

The `chat` cog also does not supply the missing agent loop. It creates a provider chat, submits the rendered prompt once with `chat.ask(...)`, verifies truncation and returns the response/session. Provider-hosted tools or MCP services may exist according to the cloud model/provider, but their action/observation loops remain provider-side dependencies. Roast does not itself implement an iterative model → first-party action/tool execution → observation → next-model-decision control loop around `chat`.

This makes the counterfactual owner test decisive. Remove Pi, Claude Code and provider-side agent/tool cognition while leaving Roast's workflow engine, Ruby/shell cogs, map/repeat/call, async barrier, context, configuration and event machinery intact: Roast can still execute authored deterministic programs and ordinary one-shot LLM requests, but no first-party actor remains that can absorb an arbitrary task, choose substantive actions from observations and revise its course autonomously. Remove Roast while leaving Pi/Claude Code installed: those CLIs retain their own autonomous coding-agent loops. The standard Roast distribution therefore fails the repository-relative S1 inclusion threshold.

Parallel map execution, iterative repeat workflows and multi-step LLM chains are still useful harness mechanisms. They cannot establish S2-S5 organizational ownership without first-party autonomous S1 units at the declared recursion. Likewise, a workflow author can deliberately compose reviewer, planner or self-improvement patterns out of cogs, but generic programmability and examples are not dedicated first-party organizational functions under Methodology 0.3.6.

Primary evidence:

- [`README.md`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/README.md) — Roast is a Ruby DSL for structured AI workflows; `agent` runs local Pi/Claude Code-style agent CLIs and `chat` sends prompts to cloud LLMs.
- [`lib/roast/workflow.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/workflow.rb) — developer-authored workflow/config/execute blocks are loaded and run through deterministic first-party managers.
- [`lib/roast/execution_manager.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/execution_manager.rb) — predeclared cog-stack execution, async waiting and control-flow enforcement.
- [`lib/roast/cogs/agent.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/cogs/agent.rb) — first-party `agent` cog delegates actual agent execution to a configured provider adapter.
- [`lib/roast/cogs/agent/providers/pi/pi_invocation.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/cogs/agent/providers/pi/pi_invocation.rb) — starts the external Pi process and parses its emitted turns/tool events/results.
- [`lib/roast/cogs/agent/providers/claude/claude_invocation.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/cogs/agent/providers/claude/claude_invocation.rb) — constructs/starts the external `claude` CLI and parses its session/tool/result stream.
- [`lib/roast/cogs/chat.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/cogs/chat.rb) — one provider chat request/response path plus truncation/session plumbing rather than a first-party agent action loop.
- [`lib/roast/system_cogs/map.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/system_cogs/map.rb) and [`lib/roast/system_cogs/repeat.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/system_cogs/repeat.rb) — deterministic authored parallelism/iteration around execution scopes.

## Operational model

A developer writes Ruby workflow code declaring cogs and control flow. Roast evaluates that definition, constructs configuration/execution managers and executes the declared stack. Built-in Ruby/cmd cogs perform deterministic programmed operations; `chat` forwards a prompt to a cloud LLM; `agent` launches or resumes an external autonomous coding-agent CLI and transports its output/telemetry back into workflow state. Subsequent Roast steps are selected by the authored Ruby workflow and ordinary deterministic control-flow conditions rather than by a first-party Roast decision maker.

Because the autonomous action loop resides in adjacent providers/CLIs, the Index boundary does not treat external agent turns or tool calls as Roast-owned S1. That also prevents parallel invocations of those external systems from being counted as first-party S1 plurality for higher-system publication.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational unit that owns an arbitrary task-level decision/action/feedback loop is established in the frozen Roast distribution.
- Disturbance / variety regulated: Roast transports workflow inputs, LLM responses and external agent results, but arbitrary coding/task/environment variety is interpreted and acted on by external agent/provider runtimes or by developer-authored Ruby logic.
- Decisive decision or feedback right: choose a substantive action from current task/environment evidence, observe the result and decide the next substantive action autonomously.
- Decision owner: external Pi/Claude Code/provider-side agent runtime for the `agent` path; workflow author/deterministic Ruby program for first-party control flow. The one-shot `chat` response does not close an agentic action/observation loop inside Roast.
- Supporting / enforcement mechanisms: workflow/cog lifecycle, contexts, configuration, provider adapters, command runner, session identifiers, async barrier, control-flow exceptions, Ruby/cmd/map/repeat/call cogs and event/output plumbing.
- Closure path: authored workflow reaches `agent` → Roast starts external agent CLI → external CLI model/tool loop interprets, acts and observes → Roast parses/returns final result → authored workflow continues. The autonomous task loop closes in the adjacent CLI/provider runtime rather than in first-party Roast. For `chat`, prompt → provider response → workflow continuation is a single inference step without first-party action/observation feedback closure.
- Why this is / is not agent-owned: first-party code invokes, configures and observes external autonomous processes but does not implement their task policy. The provider adapters are process/protocol adapters; their parsed tool events originate in the external agent. Deterministic workflow composition and one-shot model calls do not substitute for a first-party autonomous S1 loop.
- Evidence: [`lib/roast/cogs/agent.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/cogs/agent.rb); [`lib/roast/cogs/agent/providers/pi/pi_invocation.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/cogs/agent/providers/pi/pi_invocation.rb); [`lib/roast/cogs/agent/providers/claude/claude_invocation.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/cogs/agent/providers/claude/claude_invocation.rb); [`lib/roast/cogs/chat.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/cogs/chat.rb); [`lib/roast/execution_manager.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/execution_manager.rb).
- Basis: explicit + structural
- Confidence: high
- Caveats: an assembled Roast workflow can clearly contain autonomous agents in ordinary use; the exclusion concerns first-party repository-relative ownership, not colloquial usefulness as an AI/agent workflow tool.

### Absence scope

- Surfaces inspected: workflow loader/executor, cog lifecycle, chat cog, agent cog, Pi/Claude provider adapters, command runner, session handling, Ruby/cmd cogs, map/repeat/call, async execution, context/configuration and examples/tutorials.
- Plausible first-party paths checked: external coding-agent wrapper as S1; one-shot `chat` as S1; repeated prompts/session reuse as a first-party loop; Ruby workflow conditions as agentic decision making; provider-emitted tool events as transferred tool ownership.
- Why no material first-party path remains: every general autonomous task/action loop is separately implemented by an external CLI/provider, while first-party Roast either executes authored deterministic logic, transports provider output or makes a single model request without owning the model-action-observation recurrence.

## S2 — Coordination

- State: —
- Function: no publishable first-party S2 organization is established because the reviewed boundary does not contain multiple first-party autonomous S1 units whose concrete interference is regulated.
- Disturbance / variety regulated: parallel `map` and async cogs regulate execution concurrency, but the autonomous units potentially invoked inside them are external runtimes rather than first-party Roast S1s.
- Decisive decision or feedback right: no first-party organizational coordination judgment among first-party autonomous S1 units is established.
- Decision owner: workflow author/configuration chooses serial/parallel topology and concurrency; Roast deterministically enforces it.
- Supporting / enforcement mechanisms: `map` parallel limit, `Async::Barrier`, optional semaphore, per-iteration `ExecutionManager`, cog async flags, skip/next/break/fail control flow and output collection.
- Closure path: authored workflow selects parallelism → Roast starts deterministic execution scopes/external calls → runtime waits/collects/stops according to authored control. No distinct first-party S1 plurality → concrete inter-S1 disturbance → attenuation decision → changed first-party S1 behavior loop is present.
- Why this is / is not agent-owned: parallelism and concurrency control are real execution mechanisms, but topology alone is not S2. The autonomous coding agents that could interfere are the external Pi/Claude runtimes, so their coordination cannot be published as first-party Roast S2 at this repository-relative recursion.
- Evidence: [`lib/roast/system_cogs/map.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/system_cogs/map.rb); [`lib/roast/execution_manager.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/execution_manager.rb); [`README.md`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/README.md).
- Basis: structural absence at declared ownership boundary
- Confidence: high
- Caveats: a wider deployed-system assessment that explicitly treats external agent CLIs as constituent S1 units could evaluate Roast's parallel/concurrency mechanisms as support for S2; that is a different system-in-focus.

### Absence scope

- Surfaces inspected: parallel/serial map, async cogs, barriers/semaphores, nested execution managers, repeat/call and external agent invocation.
- Plausible first-party paths checked: parallel map as S2; async cog scheduling as S2; per-iteration isolation as S2; multiple agent cogs as S1 plurality.
- Why no material first-party path remains: concurrency is developer-configured execution control around scopes/calls, while no first-party autonomous S1 plurality is established inside Roast to satisfy the S2 functional prerequisite.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system discretionary current-control function over autonomous S1 commitments/resources/priorities is established.
- Disturbance / variety regulated: current workflow failures, skip/next/break conditions and async task completion are handled, but as authored control flow/runtime lifecycle rather than organizational current management of autonomous operations.
- Decisive decision or feedback right: no first-party actor receives a whole autonomous-operation view and decides how current organizational commitments should change.
- Decision owner: workflow author supplies conditions/topology; deterministic runtime enforces them; substantive external agent decisions remain inside adjacent Pi/Claude/provider runtimes.
- Supporting / enforcement mechanisms: `ExecutionManager`, cog stack, barriers, fail/skip/next/break, repeat termination, output dependencies and exceptions.
- Closure path: no whole-system first-party S1 view → discretionary current commitment/resource/priority decision → returned change into autonomous S1 operation is established.
- Why this is / is not agent-owned: an execution manager that starts/waits/stops authored steps is not automatically VSM S3. It lacks a first-party decision owner that interprets current organizational evidence and revises commitments; external agent cognition cannot be imported to supply that owner.
- Evidence: [`lib/roast/execution_manager.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/execution_manager.rb); [`lib/roast/control_flow.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/control_flow.rb); [`lib/roast/system_cogs/repeat.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/system_cogs/repeat.rb).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: a developer can encode sophisticated current-control logic in Ruby or delegate it to an external model/agent, but generic programmable composition is not a packaged first-party S3 owner.

### Absence scope

- Surfaces inspected: execution manager, workflow context/output access, control-flow exceptions, repeat/map/call managers, async lifecycle and external-agent session handling.
- Plausible first-party paths checked: `ExecutionManager` naming as S3; repeat/break decisions as S3; failure handling as S3; output-driven Ruby conditions as S3; external agent session continuation as S3.
- Why no material first-party path remains: inspected mechanisms execute authored program control or adjacent-agent calls and do not close a whole-current-organization discretionary decision loop over first-party autonomous S1 units.

## S3* — Complementary audit

- State: —
- Function: no dedicated materially independent first-party audit function is established over claims/results from a first-party autonomous S1 reporting path.
- Disturbance / variety regulated: workflows can call a second chat/agent and authors can build code-review patterns, but such composition is ordinary generic workflow programming and the reviewed boundary lacks a first-party S1 claim/audit relation.
- Decisive decision or feedback right: no packaged first-party auditor owns an independent challenge verdict and corrective return into a qualifying operational organization.
- Decision owner: workflow author or externally invoked model/agent when a custom workflow creates such a pattern.
- Supporting / enforcement mechanisms: chained cogs, output access, repeat/call, examples such as code review, ordinary Ruby predicates and external provider calls.
- Closure path: no first-party ordinary S1 report → complementary evidence acquisition → sufficiently independent audit judgment → corrective return into first-party S1/S3 is packaged in the standard distribution.
- Why this is / is not agent-owned: calling another LLM/agent from developer-authored workflow code does not itself create a dedicated organizational audit constructor; the judgment remains deployment-authored and any agent cognition remains external.
- Evidence: [`README.md`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/README.md); [`lib/roast/execution_manager.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/execution_manager.rb); [`tutorial/02_chaining_cogs/code_review.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/tutorial/02_chaining_cogs/code_review.rb).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: Roast is expressive enough to host an application-specific review loop; such a composed workflow would need assessment on its own exact implementation and independence evidence.

### Absence scope

- Surfaces inspected: chained chat/agent cogs, code-review tutorial/example, repeat/call, output access, failure/control-flow paths and provider event parsing.
- Plausible first-party paths checked: second LLM as reviewer; code-review example; repeated review/fix workflow; provider tool/result telemetry as audit; deterministic validation/error handling.
- Why no material first-party path remains: no dedicated audit primitive with organizational independence and corrective closure is supplied, and the required underlying first-party S1 reporting organization is absent.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party environment-facing prospective adaptation function is established.
- Disturbance / variety regulated: workflows can iterate, consume new data and be rewritten by users/external agents, but first-party Roast does not itself monitor future/external distinctions and adopt persistent changes to its organizational capability or strategy.
- Decisive decision or feedback right: no first-party actor selects a future-facing adaptation option for Roast's later operating capability.
- Decision owner: not established inside the standard distribution.
- Supporting / enforcement mechanisms: repeat/map/call, session reuse, workflow parameters, custom cog loading and developer-authored Ruby code.
- Closure path: no external/future distinction → generated adaptation option → adoption decision → persistent capability/strategy change → later first-party operation loop is established.
- Why this is / is not agent-owned: iteration and parameterization concern current programmed workflow execution. External agents may edit workflow files or developers may add cogs, but those outside actors do not donate S4 ownership to Roast.
- Evidence: [`lib/roast/system_cogs/repeat.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/system_cogs/repeat.rb); [`lib/roast/workflow.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/workflow.rb); [`README.md`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/README.md).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: a developer can author an evolutionary/self-modifying Roast workflow; generic DSL expressivity is not by itself a first-party S4 constructor.

### Absence scope

- Surfaces inspected: repeat/map/call, workflow parameters, provider sessions, custom cog loading, examples/tutorials and workflow-file execution.
- Plausible first-party paths checked: iterative workflows as S4; session persistence as learning; dynamic Ruby conditions; custom-cog loading; an external coding agent modifying Roast workflows.
- Why no material first-party path remains: none of the first-party paths observes future/external change and autonomously returns an adopted persistent adaptation into later first-party organizational capability.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy governance function is established.
- Disturbance / variety regulated: workflow/provider/model/system-prompt/configuration choices constrain operation but remain developer/operator configuration rather than a governed identity/ultimate-policy issue for an autonomous Roast organization.
- Decisive decision or feedback right: no first-party ultimate authority is established that resolves organizational identity/purpose/policy and returns the decision into autonomous operation.
- Decision owner: workflow author/operator supplies configuration and prompts; external agent providers own their internal policy/identity mechanisms.
- Supporting / enforcement mechanisms: config blocks, provider/model selection, append/replace system prompts for external agent CLIs, workflow parameters and custom cog loading.
- Closure path: no identity/ultimate-policy issue → legitimate authority → authoritative decision → return into first-party autonomous operation loop is established.
- Why this is / is not agent-owned: static configuration and prompt injection can strongly constrain external agents, but Methodology does not treat a prompt/config file alone as S5, and there is no qualifying first-party autonomous organization whose ultimate policy is being governed.
- Evidence: [`README.md`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/README.md); [`lib/roast/cogs/agent/providers/claude/claude_invocation.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/cogs/agent/providers/claude/claude_invocation.rb); [`lib/roast/cogs/agent/providers/pi/pi_invocation.rb`](https://github.com/Shopify/roast/blob/0cd5406ea02ac8f64b8b7a697270fd4d84a57b2c/lib/roast/cogs/agent/providers/pi/pi_invocation.rb).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: a parent application may impose meaningful policy through Roast's configuration surface; that authority belongs to the parent/composed system unless a dedicated first-party S5 closure is demonstrated.

### Absence scope

- Surfaces inspected: workflow/config blocks, provider/model settings, external-agent system-prompt options, parameters, custom cogs, control flow and product documentation.
- Plausible first-party paths checked: system-prompt replacement as S5; workflow source as policy; provider/model selection; developer configuration; external agent identity controls.
- Why no material first-party path remains: these are static construction/configuration inputs around external or deterministic execution, not a live first-party identity/ultimate-policy issue with segregated authority and return-to-operation closure.

## Recursion

The assessment fixes recursion at the first-party Roast workflow runtime. Pi and Claude Code may be viable autonomous S1 systems at their own recursion, but they are separately implemented external CLIs. Cloud-provider model/tool runtimes are likewise environmental dependencies. Widening the boundary to an application that composes Roast plus those agents can produce a genuinely agentic organization; that composed application is not the repository-relative system assessed here.

## Variety and escalation

Roast provides significant variety-handling mechanisms: arbitrary Ruby workflow code, reusable scopes, iteration, parallel map, async cogs, error/control-flow handling, shell/Ruby execution and adapters for powerful external agents. The decisive distinction is ownership. Those mechanisms either execute author-specified control or transport decisions made by adjacent autonomous runtimes. No first-party autonomous S1 loop survives the counterfactual removal of external agent/provider cognition, so higher VSM publication is not available at this boundary.

## Evidence gaps

- Provider-hosted cloud tools/MCP behavior is intentionally not imported into Roast; the `chat` cog documentation itself describes those capabilities as provider-supplied.
- External Pi/Claude sessions can span turns and expose rich tool telemetry, but the autonomous recurrence is executed by those CLI processes, not by Roast's provider adapter.
- Generic Ruby DSL extensibility means a downstream user could implement almost any organizational pattern. Methodology 0.3.6 requires a dedicated first-party construction/operating path rather than capability-by-arbitrary-code alone.
- No evidence found at the frozen revision overturns the repository-relative counterfactual: with external agentic runtimes removed, Roast remains a deterministic workflow/LLM composition engine rather than an autonomous agent organization.

## Assessment summary

Roast is a useful structured AI workflow DSL and a capable adapter around cloud LLMs and local coding-agent CLIs, but its standard frozen distribution does not own the autonomous operational decision/action/observation loop required for first-party S1. Agentic execution belongs to external Pi/Claude Code/provider runtimes, while Roast supplies authored sequencing, iteration, concurrency, context and transport. Under Profile 0.2.4 / Methodology 0.3.6, the proposed canonical outcome is `excluded-no-agentic-vsm` with `S1=— / S2=— / S3=— / S3*=— / S4=— / S5=—`.
