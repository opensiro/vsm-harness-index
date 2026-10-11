---
harness_id: oblivion-ai
project_name: Oblivion AI
repository: https://github.com/Rohith-s-hub/Oblivion-agent
review_ref: 7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb
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

# Oblivion AI

## Review boundary

- System in focus: the first-party Oblivion/M.E.E.R.A. terminal coding-agent installation and its reachable CLI/TUI runtime; optional local workspace search, watcher, voice and MCP tool-serving modes are examined for possible organizational closure, rather than treated as separately autonomous agents.
- Purpose and identity: fulfill a user's software investigation, generation, editing, testing and repository operations through an iterative locally mediated model/tool cycle.
- Relevant environment: the operator's workspace and filesystem, subprocesses, local installed tests, source and Git state, selected external or local inference providers, web/package information, and user approval. These are interfaces and disturbances, not imported decision owners.
- Standard-distribution boundary: shipped `oblivion` application paths, core Agent, TUI AgentRuntime, registered first-party tools, plan/permission guard, persisted state, workspace watcher, knowledge/RAG support and self-hosted MCP tier modes at the exact frozen commit. External editors, provider model services, user-owned project governance, proposed features, and maintainer development/release systems do not become first-party organizational functions just because they are adjacent.
- Credited operating / distribution surfaces: [main.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/main.py); [agent/core.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/core.py); [agent/runtime.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/runtime.py); [agent/llm.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/llm.py); [agent/parser.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/parser.py); [agent/plan_guard.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/plan_guard.py); [agent/permissions.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/permissions.py); [tools/registry.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/tools/registry.py); [tools/test_runner.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/tools/test_runner.py); [ui/app.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/ui/app.py); [mcp_server/core.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/mcp_server/core.py); [agent/watcher.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/watcher.py); [agent/updater.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/updater.py).
- Adjacent first-party surfaces excluded from ownership: [.github/workflows/snake.yml](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/.github/workflows/snake.yml) is maintainer/development automation rather than installed harness governance; [test/test.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/test/test.py) and the `simulator/` example are not an independently governed production evaluator; `README.md` roadmap claims are not implemented operating paths. The external Claude Desktop/Cursor/Zed agent that may consume the [mcp_server/server.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/mcp_server/server.py) tool service and third-party model inference are outside the first-party decision boundary.
- First-party operating / deployment modes considered: interactive CLI `Agent.run`; TUI asynchronous `AgentRuntime.run_async` with user approval/auto/trust settings and disk-backed plan enforcement; model retry/fallback; ordinary code verification and test tools; background index watcher; local RAG/knowledge/voice; manual update; `oblivion mcp` safe, standard and full tool-serving tiers over stdio/SSE.
- Recursion level: one installed local coding-agent application controlling one user-directed coding session/workspace at a time; user/maintainer organizations and external MCP clients are outside this recursion.
- Reviewed revision: 7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Oblivion ships a Python coding agent. Its [main.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/main.py) CLI constructs [agent/core.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/core.py) `Agent`, which constructs model messages, receives generated action descriptions, parses tool calls and returns actual execution observations into subsequent model choices. The TUI in [ui/app.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/ui/app.py#L2440-L2458) instead invokes [agent/runtime.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/runtime.py#L137-L245) `AgentRuntime`; `run_async` parses model outputs, enforces execution limits and permissions, invokes `dispatch` and feeds observations back into the model's next iteration ([agent/runtime.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/runtime.py#L500-L742)). [tools/registry.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/tools/registry.py#L475-L600) dispatches local file/shell/search/test/Git/plan tools. [agent/llm.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/llm.py#L169-L295) is a provider-neutral inference caller with retry/cooldown/fallback, not an external agent harness whose organizational rights are borrowed.

User plans are stored and checked against real workspace files by [agent/plan_guard.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/plan_guard.py#L14-L91); the runtime can reject unsupported task-completion claims, block duplicate writes and prompt renewed local work. [agent/permissions.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/permissions.py#L100-L159) classifies read/mutate/destructive actions; the TUI can return operator approval/denial to the executing loop. [agent/brain.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/brain.py#L101-L192), [tools/test_runner.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/tools/test_runner.py#L202-L335) and [tools/auto.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/tools/auto.py) provide concrete syntax/test/build observations, but these are ordinary task-execution instruments, not an independently mandated audit organization.

[agent/watcher.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/watcher.py#L17-L173) triggers incremental RAG indexing after local file changes and returns UI status. [agent/rag.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/rag.py), [agent/symbol_index.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/symbol_index.py) and [knowledge/injector.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/knowledge/injector.py) provide code context. [agent/updater.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/updater.py#L21-L132) compares installed versions with PyPI and enables a user-commanded package upgrade; this is a maintenance function, not evidence of prospective strategic adaptation. [mcp_server/core.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/mcp_server/core.py#L25-L139) supplies first-party tools to *external* MCP consumers with configured static access tiers, without embedding their independent model decision processes inside Oblivion.

## Operational model

The operational S1 is a single first-party iterative model-guided coder, instantiated in CLI or TUI mode, acting upon the user's workspace. Tool results, file-plan status, syntax/test outcomes and denied permissions inform this coder's next local action. Runtime guards, model fallback, memory/RAG, indexing and UI callbacks support that one operation. No shipped peer/child agent workforce with distinct S1 claims and a conflict regulation return path was established; multiple inference providers and parallel embedding/search operations are support mechanisms, not distinct operational S1 organizations. The user owns requested purpose and tool consent, rather than a first-party automated whole-current controller or identity-policy authority.

## S1 — Operations

- State: A
- Function: perform user-directed coding/investigation through repeated model-selected first-party tools and feedback.
- Disturbance / variety regulated: under-specified user tasks, changing workspace/source context, tool successes/failures, syntax/test feedback, denied tool approvals, missing planned files and inference interruptions.
- Decisive decision or feedback right: choose next file/search/shell/test/edit action or final response after observing the previous execution result.
- Decision owner: the configured model operating through Oblivion's first-party `Agent` or TUI `AgentRuntime`; the operator supplies task and consent, and fixed guards enforce limits.
- Supporting / enforcement mechanisms: `LLMClient`, output parser, tool registry, disk plan guard, tiered permissions, persisted session/memory, hybrid search and fallback retries.
- Closure path: user request → compiled system/task context → inference → parsed `ToolCall` → first-party tool dispatch → real observation appended to the next model context → revised tool action or `FinalAnswer`.
- Boundary reachability: [main.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/main.py#L11-L65) constructs the installed `Agent` CLI path, while [ui/app.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/ui/app.py#L2440-L2458) constructs the TUI `AgentRuntime` and [ui/app.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/ui/app.py#L2660-L2695) awaits its run, each using the same first-party tool registry rather than calling an external coding-agent binary.
- Why this is / is not agent-owned: removing model discretion leaves deterministic parsing, tool execution and authorization but no autonomous selection of context-sensitive coding actions; removing the guards would not transfer those action choices to another orchestrator.
- Evidence: [agent/core.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/core.py#L355-L495); [agent/runtime.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/runtime.py#L137-L245); [agent/runtime.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/runtime.py#L500-L742); [tools/registry.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/tools/registry.py#L475-L600); [agent/llm.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/llm.py#L169-L295); [main.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/main.py); [ui/app.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/ui/app.py#L2440-L2458).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: agent autonomy concerns operational choice within one session, not user goals/permissions or the performance of a particular external inference provider.

## S2 — Coordination

- State: —
- Function: no implemented relation was established that attenuates interference or oscillation among *distinct active S1 operational units*.
- Disturbance / variety regulated: model retries, repeated actions, duplicate file writes and competing file state may disturb the one coding loop, but the inspected distribution does not demonstrate two separately accountable S1 units requiring inter-unit coordination.
- Decisive decision or feedback right: no identifiable inter-S1 collision arbitration, agreement, reservation or coordination response owner.
- Decision owner: none established for an S2 function; the model's ordinary local task sequencing remains S1, and deterministic loop/plan guards implement local constraints.
- Supporting / enforcement mechanisms: action-loop repetition detection, per-run file-write ledger, execution budgets, provider fallback, TUI callbacks, MCP request routing and indexing debounce.
- Closure path: a repeated or invalid single-agent tool call is rejected or corrected locally; no S2-specific information about distinct S1 interference is fed back to multiple regulated operational units.
- Why this is / is not agent-owned: an LLM's decision to choose its next action within one task is not conflict-specific attenuation between independent S1 units, even when the runtime schedules asynchronous support operations.
- Evidence: [agent/runtime.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/runtime.py#L500-L742); [agent/llm.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/llm.py#L245-L295); [agent/watcher.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/watcher.py#L17-L90); [mcp_server/core.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/mcp_server/core.py#L25-L139); [tools/registry.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/tools/registry.py#L475-L600).
- Basis: structural.
- Confidence: high for the bounded standard-distribution review.
- Caveats: separate external editors may call the MCP tool server concurrently, but their operational identities/coordination governance are not owned by the assessed first-party app.

### Absence scope

- Surfaces inspected: both CLI/TUI runtime loops, action registry, model fallback, filesystem and plan/write guards, asynchronous watcher/indexer, MCP tiers and external-client boundary.
- Plausible first-party paths checked: independent child/peer agents and inter-unit work commitments; shared-workspace collision arbitration; cross-agent write conflict detection with an attenuation response returned into later behaviour of *both* S1s; event/queue and client request coordination.
- Why no material first-party path remains: the shipped product contains one controlling coder and supporting operations, while repeats/duplicate writes are one loop's local safety rules. The MCP server exposes tools to independent external actors without becoming their inter-S1 coordinator.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current decision authority regulating the broader organization's simultaneous commitments, constraints, resource priorities or accountability was established.
- Disturbance / variety regulated: runaway loops, model outages, unfinished planned files, unsafe tool calls and overlong local tasks are addressed by individual session mechanisms, not by management of multiple organizational S1 commitments.
- Decisive decision or feedback right: fixed `max_iterations`, tool approval rules and plan-completion checks; a user can authorize a particular edit/bash call; none establishes a whole-current S3 decision with an organization-wide view.
- Decision owner: no separate whole-current management owner at this recursion; user owns specific task consents, model owns current coding actions, runtime enforces preconfigured guards.
- Supporting / enforcement mechanisms: plan persistence and disk inspection, runtime abort/retry conditions, tier permissions, fallback, TUI status and session logging.
- Closure path: plan/tool observation is returned to the current coder or user for another local action; no system-wide resource/commitment judgment returns to alter multiple S1 operations.
- Why this is / is not agent-owned: model-selected plans and provider fallback regulate one task, while fixed budgets and user approvals are operational boundaries, not agent-owned current-organization oversight.
- Evidence: [agent/plan_guard.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/plan_guard.py#L14-L91); [agent/runtime.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/runtime.py#L137-L245); [agent/runtime.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/runtime.py#L420-L505); [agent/permissions.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/permissions.py#L100-L159); [ui/app.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/ui/app.py#L2440-L2695).
- Basis: structural.
- Confidence: medium-high.
- Caveats: an individual user's ability to interrupt execution or approve tools remains external local control and not an evidenced S3 parent closure.

### Absence scope

- Surfaces inspected: CLI/TUI task/plan state, model fallback, execution ceilings, mode/trust/approval settings, session persistence and remote-tool-serving options.
- Plausible first-party paths checked: current whole-workspace portfolio/commitment view, competing S1 priority/resource negotiation, self-managed budget adaptation and supervisory operator mode with a returned cross-work decision.
- Why no material first-party path remains: guards constrain one task and tool permissions govern individual operations; no shipped S3-scoped resource/commitment choice over the whole at the declared recursion appears.

## S3* — Complementary audit

- State: —
- Function: no organizationally complementary and sufficiently independent source of operational truth with its own audit judgment returned to control was established.
- Disturbance / variety regulated: generated-code errors, fabricated file-creation claims, missing plan artifacts and failed tests can contradict coding claims, but are handled as routine operational validation in the same agent task loop.
- Decisive decision or feedback right: static plan/disk-existence checks and test-tool responses affect the same agent's next local action; no separately accountable audit selection, alternative evidentiary investigation or consequential complementary review path is demonstrated.
- Decision owner: the coder chooses ordinary verification tools and responds to observations; deterministic runtime gates enforce the disk plan, rather than independently owning an S3* audit decision.
- Supporting / enforcement mechanisms: actual disk-file checks, syntactic `verify_code`, project test runner and lint, status messages, activity log and watcher reindex notifications.
- Closure path: tool check/test result or missing-file rejection → ordinary model observation/redo within S1. This has factual access to the workspace but not a separable complementary audit judgment directed to metasystemic current control.
- Why this is / is not agent-owned: a verifier tool or automatic missing-file gate is not the owner of an alternative audit path simply because it reads real files; no materially independent audit mandate or subsequent control decision was found.
- Evidence: [agent/plan_guard.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/plan_guard.py#L64-L91); [agent/runtime.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/runtime.py#L420-L505); [agent/brain.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/brain.py#L101-L192); [tools/test_runner.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/tools/test_runner.py#L202-L335); [tools/auto.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/tools/auto.py#L210-L240); [agent/watcher.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/watcher.py#L17-L90).
- Basis: structural.
- Confidence: medium-high.
- Caveats: ordinary project tests can supply external-to-model facts, but neither that fact nor a test name alone establishes an independent complementary audit with returned organizational control.

### Absence scope

- Surfaces inspected: plan-validation/anti-hallucination hooks, test/build/syntax tool implementations, event/log and status paths, file watcher, Git tools, optional MCP server, CLI and TUI callback ownership.
- Plausible first-party paths checked: independent raw-artifact sampling/replay, separately operated adversarial reviewer, distinct audit source from normal production check, audit judgment provenance, findings routed to a system-wide control owner.
- Why no material first-party path remains: the inspected checks are in-band tools and fixed task-local guards; no independently selectable alternative audit/access path or S3* finding→whole-current control loop is wired into the shipped agent boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no external-and-prospective intelligence process developing adaptation options and returning them to the system's current operational capability was established.
- Disturbance / variety regulated: new user requests, changing project files, package information and model-provider rate limits are handled as current-task input/support; a remote PyPI version check can alert to an update, but not by itself choose or evaluate future adaptation options.
- Decisive decision or feedback right: current task/tool choice, fallback model selection, RAG knowledge pack selection and manual product update; no future-oriented system adaptation judgment owner.
- Decision owner: task model for current coding/search; deterministic runtime for fallback/knowledge detection; user for manual version installation, not a demonstrated S4 strategic parent mode.
- Supporting / enforcement mechanisms: web/search/package tools, external provider fallback, knowledge-pack injection, file-change indexing and optional version-update command.
- Closure path: new evidence is injected as task context or version update displayed to user; no ongoing external-forecast/options→present S3 capability adjustment loop was found.
- Why this is / is not agent-owned: transient external information used to finish a coding task is not organizational prospective intelligence, and a package upgrade triggered by user action is not an independently warranted S4 adaptation option.
- Evidence: [agent/updater.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/updater.py#L21-L132); [agent/llm.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/llm.py#L245-L295); [knowledge/detector.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/knowledge/detector.py); [knowledge/injector.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/knowledge/injector.py); [agent/rag.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/rag.py); [agent/watcher.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/watcher.py); [tools/web_search.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/tools/web_search.py); [ui/app.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/ui/app.py#L2180-L2205).
- Basis: structural.
- Confidence: medium-high.
- Caveats: fresh online search content can inform the operative coder; claims of wider autonomous strategy or prospective environmental modelling are not inferred from optional tools alone.

### Absence scope

- Surfaces inspected: web/package search, model/provider configuration and fallback, memory/knowledge packs, watcher/RAG, updater, TUI user control and developer roadmap.
- Plausible first-party paths checked: environmental change detection as future-relevant signal; comparative development of adaptation alternatives; discretionary prospective review of capabilities; feedback and effective implementation through current S3 or eligible legitimate parent.
- Why no material first-party path remains: every shipped external-information path either serves the current user task or a manually commanded maintenance action; a closed prospective adaptation conversation with current operations is absent at the product boundary.

## S5 — Policy and identity

- State: —
- Function: no ultimate identity/policy conflict decision with legitimate authority and returned binding rule was established at this local coding-agent recursion.
- Disturbance / variety regulated: user tool-permission risks, unsafe commands, chosen session trust and model settings are governed as execution safety conditions, not exceptional decisions about the system's durable mission/identity and competing current/future requirements.
- Decisive decision or feedback right: user can allow/deny particular tool execution and configure trust/auto/tier modes; runtime applies fixed safety classification. No ultimate-policy deliberation/choice is implemented as a first-party path.
- Decision owner: operator for local consent and configured limits, developer for fixed classifications, not an evidenced first-party S5 owner.
- Supporting / enforcement mechanisms: tool tier lists, destructive-action prompts, environment config, UI approval callback, static CLI/MCP tier selection.
- Closure path: an ordinary action request is allowed/denied and the same current task continues; no identity/ultimate-policy issue → legitimate parent decision → durable policy return governing subsequent organizational operation.
- Why this is / is not agent-owned: a model action and user permission decision are not a binding ultimate-policy settlement; the programmer's constraints do not automatically establish operating S5.
- Evidence: [agent/permissions.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/permissions.py#L100-L159); [mcp_server/core.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/mcp_server/core.py#L25-L58); [mcp_server/server.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/mcp_server/server.py#L16-L70); [agent/runtime.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/agent/runtime.py#L630-L664); [ui/app.py](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/ui/app.py#L2440-L2695); [README.md](https://github.com/Rohith-s-hub/Oblivion-agent/blob/7c57fd23ddd9abb5a2795788364f5dcdf3ec87cb/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: the broader human software team may have policies, but this separate parent organization is not first-party Oblivion's wired S5.

### Absence scope

- Surfaces inspected: command/tier permission modes, user authorization callbacks, session config, CLI/MCP deployment, plans/goals, user/maintainer boundary and persisted workspace.
- Plausible first-party paths checked: identity-level issue recognition/escalation, authorized parent policy adjudication, durable returned governance decision and compliance of later activity with that new rule.
- Why no material first-party path remains: only fixed tool safety and per-operation approvals are implemented; neither an identity/policy dispute nor a legitimate ultimate authority's returned policy decision is a supported executable pathway.

## Recursion

Oblivion is assessed as the local terminal coding product, not as the software team deploying it. A CLI/TUI session exercises S1 tool decisions. MCP tool-serving does not incorporate the external editor's decisions as a recursive native S1, and running multiple copies does not create first-party coordination. Neither model/provider choice nor voice input is a separate recursive organizational actor. Maintainer/development workflows, human project policy and editor orchestration remain external higher-level systems without proven function-specific parent-return wiring.

## Variety and escalation

User tasks and changing code create S1 operational variety. Search and model context amplify the coder's awareness; result truncation and memory compression can attenuate it. Retry/fallback, plan guards, test feedback and operator permissions regulate immediate operational disturbances. Destructive actions request explicit human approval rather than silently escalating an ultimate-policy issue. The source did not demonstrate a first-party S2 conflict channel, whole-current S3 negotiation, complementary S3* finding, prospective S4 option or binding S5 return. Local model fallback and test outcomes should not be mistaken for cross-functional or metasystemic closure.

## Evidence gaps

The classification is source- and frozen-revision-relative; no performance benchmark, actual provider deployment trace, external-editor organizational policy or live operator outcomes are inferred. The first-party CLI/TUI and supporting MCP/agent tools were inspected for plausible positive and parent-governed paths. No concrete in-boundary untraced shipped S2–S5 positive path was identified warranting `?` under Methodology 0.3.7; the documented `—` results are bounded to this reviewed distribution and are not claims that future versions or external compositions cannot add functions.
