---
harness_id: legion
project_name: Legion
repository: https://github.com/software-mansion/legion
review_ref: 24322c80bf194fe392e3f282ac1a4434aecd5696
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Legion

## Review boundary

- System in focus: A normal installed Legion agent running a task with optionally configured tools, persistent conversation and owned subagents in a host Elixir application.
- Purpose and identity: Turn task requests into model-selected Lua scripts that invoke permitted host tool modules, consume results and produce answers.
- Relevant environment: Host application modules exposed as tools, task input, model service, runtime errors and a developer/application operator.
- Standard-distribution boundary: The Legion library's `Legion.Agent`, `AgentServer`, `Executor`, configured sandbox, tool bridge, rate-limit guard and optional first-party agent-tool/human-tool/LLM EvalGuard modes. External applications must compose their own higher-order governance and are not credited.
- Credited operating / distribution surfaces: Shipped model-driven `Executor` loop and `Legion.Eval` sandbox, supported runtime agent sessions and subagent APIs, optional runtime guards and persistence.
- Adjacent first-party surfaces excluded from ownership: Project CI/release/issue governance, examples and tests not wired into a normal installed agent, external host application's policy decisions, MCP client/host orchestration, developer-authored specialized tool implementations.
- First-party operating / deployment modes considered: One-off `Legion.execute`, persistent `Legion.start_link/call`, optional `AgentTool` subagents, Lua sandbox, configured `EvalGuard.LLM` and rate limits.
- Recursion level: One host-embedded Legion agent organization; owned child agents are subordinate task cells when present, not automatic independent higher recursion.
- Reviewed revision: `24322c80bf194fe392e3f282ac1a4434aecd5696`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Legion is a library/SDK rather than a centrally operated fleet. Its `Executor` requests structured actions from a model, executes an `eval_and_continue` or `eval_and_complete` action in the Lua sandbox and puts code results back into the next model turn. AgentServer manages persistent conversation, rate limits and recovery; AgentTool supports optional task-scoped child agents with ownership checks and parallel/pipeline helpers. `EvalGuard.LLM` is a configurable second-model pre-execution safety review, not a built-in independent post-hoc audit of operating reality. Developer/application code specifies tools and policy configuration. [`lib/legion/executor.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/executor.ex#L173-L232), [`lib/legion/executor.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/executor.ex#L233-L275), [`lib/legion/executor.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/executor.ex#L334-L374), [`lib/legion/tools/agent_tool.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/tools/agent_tool.ex#L102-L210), [`lib/legion/eval_guard/llm.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/eval_guard/llm.ex#L1-L36).

## Operational model

One Legion model agent responds to a task with an executable program, chooses tool invocations, interprets the returned data and may continue autonomously. A host may expose additional tools, write guard rules, bind conversations or create subagents. Decision ownership differs: the model owns the local tool/action choice; the developer owns which tools, models, evaluation gates and limits exist; deterministic sandbox and rate limiter enforce those decisions. Optional subagents are scoped to their owner and do not by themselves demonstrate an S2, S3 or higher function.

## S1 — Operations

- State: A
- Function: Produce task outcomes by choosing and running tool-using Lua code in a model-feedback loop.
- Disturbance / variety regulated: Task uncertainty, changing tool results and execution errors.
- Decisive decision or feedback right: The model chooses structured return/eval actions and code, then incorporates execution results into later actions.
- Decision owner: The model-backed Legion agent.
- Supporting / enforcement mechanisms: Structured-action schema, Lua sandbox, timeout/reduction/memory limits, exposed tool functions, Executor checkpoints and persistent session.
- Closure path: Model-generated code is guarded and executed; formatted tool/code results enter conversation history and trigger the next model iteration until the agent returns or completes.
- Why this is / is not agent-owned: Removing model action selection leaves a sandbox and user-selected tool surface without adaptive action decisions.
- Evidence: [`lib/legion/executor.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/executor.ex#L144-L232); [`lib/legion/executor.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/executor.ex#L233-L275); [`lib/legion/executor.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/executor.ex#L334-L374); [`lib/legion/eval.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/eval.ex#L33-L68); [`lib/legion/eval.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/eval.ex#L71-L90).
- Basis: structural
- Confidence: High for the shipped model-backed execution mode.
- Caveats: Live provider behavior was not exercised in this review; no inference about unspecified host tools or MCP clients.
- Boundary reachability: The public installed `Legion.execute` and persistent `Legion.call` modes invoke the first-party Executor/Eval directly.

## S2 — Coordination

- State: —
- Function: No evidenced first-party function attenuates interference/oscillation between distinct S1 work units at the assessed organization boundary.
- Disturbance / variety regulated: Optional parallel child agents could compete for work or generate incompatible outputs, but this possibility alone is not an established S2 conflict witness.
- Decisive decision or feedback right: No first-party arbitration/negotiation path for inter-S1 conflict found.
- Decision owner: None established for the S2-specific decision.
- Supporting / enforcement mechanisms: AgentTool `parallel`, `pipeline`, child ownership checks, max-subagent limits and result collection.
- Closure path: The helpers dispatch child tasks and relay responses or cancellations; no conflict detection and corrective return to competing child units is established.
- Why this is / is not agent-owned: Model may select child tasks, but delegation and fan-out alone do not constitute coordination of actual shared interference.
- Evidence: [`lib/legion/tools/agent_tool.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/tools/agent_tool.ex#L102-L210); [`lib/legion/tools/agent_tool.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/tools/agent_tool.ex#L331-L399); [`lib/legion.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion.ex#L462-L520).
- Basis: structural
- Confidence: Moderate, bounded to the examined shipped agent/subagent interfaces.
- Caveats: A host application could add S2; its independent implementation is outside the library's default assessed boundary.

### Absence scope

- Surfaces inspected: AgentTool child spawn/call/cast/stop, parallel/pipeline, ownership and concurrency checks, persisted agent messages and main Executor action loop.
- Plausible first-party paths checked: Concurrent child task results, child ownership isolation, width/capacity limits, pipeline response propagation.
- Why no material first-party path remains: These are task composition and local safety constraints; no concrete inter-S1 collision/oscillation is detected and resolved with returned behavior-changing feedback to the affected S1 units.

## S3 — Inside-and-now control

- State: —
- Function: No first-party whole-system current-control owner identified in the standalone host-embedded Legion library.
- Disturbance / variety regulated: Shared capacity, budgets, priorities and competing commitments would need current portfolio control if a larger agent organization were composed.
- Decisive decision or feedback right: No shipped decision right to revise whole-agent-system commitments/resources based on a current whole-system view is evidenced.
- Decision owner: No qualifying owner. Developer config selects limits; model agent chooses task-local subagents; rate limiter enforces limits deterministically.
- Supporting / enforcement mechanisms: AgentServer rates, agent index, subagent owner caps, task cancellation and usage telemetry.
- Closure path: Rate limits can refuse local operations and child caps stop excess starts; this enforces a preselected constraint without changing organization-level commitments.
- Why this is / is not agent-owned: Delegating or stopping a task-owned child does not show model access to a whole-portfolio view plus regulation of shared current objectives.
- Evidence: [`lib/legion/agent_server.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/agent_server.ex#L395-L439); [`lib/legion/tools/agent_tool.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/tools/agent_tool.ex#L102-L159); [`lib/legion/tools/agent_tool.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/tools/agent_tool.ex#L340-L384); [`lib/legion/agent.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/agent.ex#L155-L174).
- Basis: structural
- Confidence: Moderate within declared installed-library boundary.
- Caveats: The host application may implement S3 using these primitives; not credited as Legion-owned without the owner's actual closure.

### Absence scope

- Surfaces inspected: AgentServer rate limiting and process handling, AgentIndex, AgentTool lifecycle/owner caps, Executor and library-level parallel/pipeline.
- Plausible first-party paths checked: Per-agent rate-limit rules, child capacity enforcement, task-level model-selected delegation, persistent conversations.
- Why no material first-party path remains: No whole-system current view and discretionary authority over shared priorities/resources/commitments at this recursion are included in the shipped library; enforcement and task-local decisions do not fill the missing organizational function.

## S3* — Complementary audit

- State: —
- Function: No shipped complementary independent audit of **executed operational reality** is established.
- Disturbance / variety regulated: Agent-provided results or executed tool side effects could diverge from reality.
- Decisive decision or feedback right: Independent examination of actual side effects or source artifacts and return of corrective findings to current control.
- Decision owner: None. An optional separate EvalGuard.LLM judge can refuse proposed code, but it reviews intent before execution rather than independently observing completed operations.
- Supporting / enforcement mechanisms: Static sandbox check, optional LLM EvalGuard, deny-by-default on broken guard, evaluation telemetry and result formatting.
- Closure path: A pre-execution denial is returned to the model for rewriting; no independent post-execution audit finding and corrective-control loop is evidenced.
- Why this is / is not agent-owned: Separate model review owns an optional preflight risk verdict, not a complementary audit of operational truth; model independence alone is not an S3* function witness.
- Evidence: [`lib/legion/eval.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/eval.ex#L33-L68); [`lib/legion/eval_guard.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/eval_guard.ex#L67-L105); [`lib/legion/eval_guard/llm.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/eval_guard/llm.ex#L1-L36); [`lib/legion/eval_guard/llm.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/eval_guard/llm.ex#L94-L123).
- Basis: structural
- Confidence: Moderate for this bounded absent-audit judgment.
- Caveats: A host-level independent execution audit is not part of the credited first-party installed boundary.

### Absence scope

- Surfaces inspected: EvalGuard and its second-model reviewer, Lua sandbox execution, tool/result callbacks, telemetry and persist/restore functions.
- Plausible first-party paths checked: Proposed code LLM review, sandbox permission checks, post-execution result formatting and error feedback, conversation persistence.
- Why no material first-party path remains: These paths validate prospective code or echo normal task output, without independently sampling actual side effects/operational artifacts and returning a complementary finding to a supervisory control loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: No outside-and-then sensing/option-selection loop changing future system capabilities was established.
- Disturbance / variety regulated: Changes in host task environment or future tool availability might motivate capability adaptation.
- Decisive decision or feedback right: No internal prospective organizational adaptation authority or closed feedback to current capability.
- Decision owner: Not established. The host developer may change modules/configuration; that is external composition, not an installed future intelligence function.
- Supporting / enforcement mechanisms: Conversation persistence, tool schema configuration, recovery/checkpoints, modular sandbox and optional external tools.
- Closure path: Stored conversations can inform later S1 turns, but the reviewed library does not evaluate external future conditions and adopt a capability change on behalf of the organization.
- Why this is / is not agent-owned: Long-term state and code execution alone are not S4; a model writing a script for a current task is still S1.
- Evidence: [`lib/legion/agent.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/agent.ex#L129-L174); [`lib/legion/executor.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/executor.ex#L290-L307); [`lib/legion/agent_server.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/agent_server.ex#L395-L411); [`lib/legion.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion.ex#L319-L413).
- Basis: structural
- Confidence: Moderate.
- Caveats: Does not preclude an Orloj-like or host-built prospective organization on top of Legion.

### Absence scope

- Surfaces inspected: Agent config/known keys, persistence and recovery, dynamic model tool loop, tool module bridge, optional human tool and eval guard.
- Plausible first-party paths checked: Persistent memory, reusable Lua bindings, recovery, user-supplied changing config and task-derived scripts.
- Why no material first-party path remains: None of the shipped paths owns external/future intelligence and an adoption judgment returning a changed capability to current organizational control.

## S5 — Policy and identity

- State: —
- Function: No installed identity-level or ultimate-policy decision/return loop at the assessed organization recursion.
- Disturbance / variety regulated: A host could need to define or revise organizational identity and ultimate tool/policy authority, but Legion exposes only configuration of embedded agents.
- Decisive decision or feedback right: No first-party ultimate identity/policy authority with a complete return-to-operation loop in the standard distribution.
- Decision owner: Not established. The host developer selects tools and guard, while the optional second model only judges individual code snippets under host-supplied rules.
- Supporting / enforcement mechanisms: Agent module compile-time defaults, host/application config, allowed subagent list, EvalGuard rules, per-agent tool sandbox and rate-limit policy.
- Closure path: Runtime obeys host-set configuration; no first-party identity-level proposal, legitimate decision and operationally returned governance sequence is present beyond static configuration.
- Why this is / is not agent-owned: Model cannot redefine the organization's identity; static tool allowlist and code approval are not sufficient for S5.
- Evidence: [`lib/legion/agent.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/agent.ex#L129-L174); [`lib/legion/tools/agent_tool.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/tools/agent_tool.ex#L331-L344); [`lib/legion/eval_guard/llm.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/eval_guard/llm.ex#L1-L36); [`lib/legion/eval.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/eval.ex#L33-L68).
- Basis: structural
- Confidence: Moderate, limited to standalone installed SDK modes.
- Caveats: External host organization ownership could qualify under a different boundary but cannot be imported without implementation evidence.

### Absence scope

- Surfaces inspected: Agent module definition, host config resolution, guard and allowed-tool/subagent configuration, lifecycle and persistence.
- Plausible first-party paths checked: HumanTool question/approval, host-set policy, EvalGuard verdicts, agent spawn/stop, dynamic Lua tool calls.
- Why no material first-party path remains: The examined library owns enforcement and task-level choices, not a legitimate first-party runtime institution deciding identity/ultimate policy and returning that authoritative decision to govern future operation.

## Distributed OSS parent arrangement

Repository contributors and maintainers are outside the installed agent's operational recursion. No GitHub review or release change is borrowed to upgrade S3–S5 into P modes.

## Self-hosted and non-human modes

Legion can be self-hosted inside an Elixir app, but external application composition is the decisive difference. Parent modes are not assigned simply because the application developer sets config. Neither model-generated scripts nor optional EvalGuard review proves autonomous metasystem closure.

## Recursion

The assessed system is an installed root agent and its optionally owned task-local children. A child process, caller relationship, pipeline or tool invocation does not automatically establish an independently viable recursive organization.

## Variety and escalation

The model absorbs request variety via tool code and observations; runtime guards can deny unsafe code or rate-limited starts. HumanTool can ask a host actor for a task-level answer. These are task/permission interrupts, not independent S3/S4/S5 evidence. [`lib/legion/tools/human_tool.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/tools/human_tool.ex#L36-L70), [`lib/legion/agent_server.ex`](https://github.com/software-mansion/legion/blob/24322c80bf194fe392e3f282ac1a4434aecd5696/lib/legion/agent_server.ex#L418-L439).

## Evidence gaps

- No live model calls or host application-specific custom policies were included; classification is first-party source-bound.
- Reassess S2 or S3 only for a *concrete deployed* owner/feedback path that regulates cross-agent interference or whole-org current commitments, rather than generic parallel/subagent controls.
- An EvalGuard.LLM model might be separately invoked, but its reviewed inputs are proposed code and policy, not independent actual operation evidence required for S3*.
- No positive S4/S5 source route within the declared standalone SDK boundary was found; absence is bounded by the inspected surfaces, not a claim about all possible Legion applications.
