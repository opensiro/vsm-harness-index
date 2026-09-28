---
harness_id: researchharness
project_name: ResearchHarness
repository: https://github.com/InternScience/ResearchHarness
review_ref: 72e8a44737aadabc8c3f9e5c7ea76883b9c7032f
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ResearchHarness

## Review boundary

- System in focus: the first-party ResearchHarness base runtime at frozen revision `72e8a44737aadabc8c3f9e5c7ea76883b9c7032f`, including its ReAct/model-tool loop, workspace and tool surface, trace/session persistence, context compaction, CLI, local UI and OpenAI-compatible API serving.
- Purpose and identity: a lightweight general-purpose execution substrate for one tool-using LLM agent at a time, usable as a benchmark baseline, meta-harness and personal assistant runtime.
- Relevant environment: external OpenAI-compatible model providers, users/clients, local/web resources reached through tools, upper-layer agent frameworks and benchmark/product layers.
- Standard-distribution boundary: first-party `agent_base`, tool implementations, trace/session/compaction machinery, CLI/frontend/API server and request-local runtime controls are inside. ResearchClawBench, MarkScientist, external model/provider internals and upper-layer orchestration remain separate.
- Credited operating / distribution surfaces: the native ReAct loop, model/tool dispatch, bounded workspace tools, context compaction and durable trace/session state across CLI/Python/API/UI entry surfaces.
- Adjacent first-party surfaces excluded from ownership: repository tests/CI, benchmark adapters as evaluation artifacts, release/maintainer activity and documentation-only examples. Tests corroborate runtime behavior but are not product-runtime organizational actors.
- First-party operating / deployment modes considered: direct CLI/Python runs, local UI sessions and isolated OpenAI-compatible API requests using the same first-party agent runtime.
- Recursion level: one ResearchHarness-managed tool-using agent run. Concurrent API requests are separate independent S1 executions; the frozen distribution does not define them as one higher-level multi-agent organization.
- Reviewed revision: `72e8a44737aadabc8c3f9e5c7ea76883b9c7032f`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

ResearchHarness deliberately keeps one main ReAct loop. `agent_base/react_agent.py` builds a request from system/context/session state, calls the configured model with native tool schemas, receives model-selected tool calls, executes them through first-party tool objects, appends tool results to the ongoing message/session state and continues the round loop until the model returns a terminal plaintext answer or a bounded stop condition fires. Read-only tool calls may run concurrently, while mutation boundaries remain serialized; this is execution optimization inside one S1 rather than a multi-agent coordination organ.

Durability is run-local. `AgentSessionState` persists prompt, messages, token state, compaction records and termination/error state beside flat JSONL traces. Context compaction invokes a separate summarization call only to compress older turns into explicit working memory for continuation of the same task; its prompt says the workspace remains authoritative and asks for current Goal, Constraints, Evidence, Open issues and Next useful actions. That preserves operational context but does not create an outside-and-then adaptation loop.

The README explicitly positions the repository as a foundational/base harness rather than a workflow platform: one main ReAct loop, one workspace root and one trace format. Upper layers may subclass `BaseAgent` and override completion hooks, but those generic extension points do not supply S2-S5 functions inside the reviewed distribution.

Primary evidence:

- [`README.md`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/README.md) — base-harness positioning, one-main-loop architecture, execution surfaces and explicit non-workflow-platform boundary.
- [`agent_base/react_agent.py`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/react_agent.py) — model/tool/result continuation loop, runtime bounds, tool execution, tracing and compaction integration.
- [`agent_base/base.py`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/base.py) — intentionally generic upper-layer extension/completion hooks.
- [`agent_base/context_compact.py`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/context_compact.py) — same-task working-memory compaction semantics.
- [`agent_base/session_state.py`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/session_state.py) — run/session persistence and compaction records.
- [`agent_base/prompts/system_base.md`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/prompts/system_base.md) — operational planning/evidence discipline, local `plan.md`/`memory.md` guidance and tool-use contract.

## Operational model

A caller starts one agent with a prompt and workspace. The model autonomously chooses whether to answer or call one or more available tools. ResearchHarness validates and executes those calls, records their outputs, returns the observations to the model on a later round and persists the evolving session/trace until completion, interruption, timeout or round limit. API concurrency creates several independent runs but does not introduce a fleet-level relation among them.

The base system prompt encourages evidence gathering, plan maintenance, local memory and verification, but these remain task-level S1 behaviors. They do not themselves establish whole-system control, complementary audit independence, prospective organizational adaptation or ultimate-policy authority.

## S1 — Operations

- State: A
- Function: perform open-ended local/web agent work through a model-driven decision/action/observation loop.
- Disturbance / variety regulated: user goals, changing workspace/web state, tool outputs/errors, provider responses, missing evidence, context pressure and runtime limits encountered during a trajectory.
- Decisive decision or feedback right: choose the next substantive answer or native tool action in response to current context and returned observations.
- Decision owner: the autonomous model-driven ResearchHarness agent actor.
- Supporting / enforcement mechanisms: `react_agent.py`, native tool schemas/dispatcher, bounded workspace paths, read-tool concurrency partitioning, retries/timeouts, session state, traces, context compaction and max-round/runtime limits.
- Closure path: user/client prompt → model turn → model-selected tool call → first-party tool execution → result enters messages/session state → next model turn observes the result and revises/continues → terminal answer or bounded stop.
- Boundary reachability: the loop is the core first-party runtime used by CLI, Python embedding, UI and API serving; no development-only or external orchestration actor is required beyond the configured model provider and environment tools.
- Why this is / is not agent-owned: deterministic host code executes and bounds actions, but the model chooses the substantive next action. Removing that actor leaves tools/session machinery without the goal-directed operational decision loop.
- Evidence: [`agent_base/react_agent.py`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/react_agent.py); [`README.md`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external provider internals are not imported; S1 credit rests on ResearchHarness owning the first-party tool execution and observation-return loop around the model.

## S2 — Coordination

- State: —
- Function: no inter-S1 coordination function is established at the reviewed recursion.
- Disturbance / variety regulated: no first-party topology with interacting distinct S1 units and a concrete cross-unit conflict/oscillation was found.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established.
- Supporting / enforcement mechanisms: independent API-run thread-pool concurrency, adjacent read-only tool parallelism and serialization of mutation-sensitive tool calls within one agent turn.
- Closure path: these mechanisms schedule execution inside or between independent requests but do not reconstruct a distinct-S1 disturbance → coordination response → changed later S1 behavior loop.
- Why this is / is not agent-owned: multiple tool calls and concurrent API requests are not multiple coordinated operational units. The repository explicitly presents one main ReAct loop rather than a multi-agent orchestration layer.
- Evidence: [`README.md`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/README.md); [`agent_base/react_agent.py`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/react_agent.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: an upper-layer framework may instantiate several ResearchHarness agents, but that organization is outside this repository's standalone boundary.

### Absence scope

- Surfaces inspected: core ReAct loop, API request concurrency, parallel read-tool execution, base-agent extension hooks, workspace/session/trace state and CLI/UI/API serving surfaces.
- Plausible first-party paths checked: parallel read-tool batching as S2; API thread-pool concurrency as S1 plurality; upper-layer role subclassing as multi-agent coordination; shared workspace behavior as collision regulation.
- Why no material first-party path remains: all inspected concurrency is either inside one S1 turn or independent request serving. No packaged first-party multi-agent relation identifies and attenuates a concrete inter-S1 disturbance.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-system current-control function is established above the single agent run.
- Disturbance / variety regulated: one run has round/time/token/retry boundaries and optional interactive clarification, but no portfolio of current S1 commitments/resources is presented to a whole-system controller.
- Decisive decision or feedback right: not established for S3.
- Decision owner: not established.
- Supporting / enforcement mechanisms: runtime limits, tool restrictions, request-local model/tool options, interruption, workspace confinement, AskUser and API concurrency limits.
- Closure path: limits can stop or constrain an individual run, and a user can answer a clarification, but no whole-system current view → allocation/commitment/intervention judgment → changed organization-wide operation loop exists.
- Why this is / is not agent-owned: deterministic limits are enforcement, not S3 ownership; AskUser is local task clarification rather than current-control authority over multiple S1 units.
- Evidence: [`agent_base/react_agent.py`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/react_agent.py); [`agent_base/prompts/system_base.md`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/prompts/system_base.md); [`README.md`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: host-level orchestration/control can be layered around the base harness but is not inherited into this assessment.

### Absence scope

- Surfaces inspected: runtime budgets/limits, interruption, API pool controls, tool selection/restrictions, AskUser, session state and base-agent completion hooks.
- Plausible first-party paths checked: runtime caps as resource governance; API max concurrency as whole-system capacity control; user clarification as parent S3; completion hooks as supervisor construction.
- Why no material first-party path remains: the mechanisms constrain isolated runs or expose generic extension points; none supplies a function-specific whole-system current view and authority over multiple operational commitments.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path is established.
- Disturbance / variety regulated: the agent may make incorrect claims or incomplete work, but the standard distribution does not add a separate audit actor/path that challenges ordinary S1 reporting through materially different access to operational reality.
- Decisive decision or feedback right: not established for S3*.
- Decision owner: not established.
- Supporting / enforcement mechanisms: direct tool observations, workspace rereads, traces, session state, prompt instructions to verify claims, benchmark/end-to-end tests and customizable completion hooks.
- Closure path: tool results and verification reads feed directly back into the same producing S1 loop; traces record that loop. No distinct ordinary-report claim → complementary evidence → audit judgment → corrective-return path is packaged.
- Why this is / is not agent-owned: self-verification by the producing agent and ordinary tool feedback do not establish complementary audit independence. Repository tests/benchmarks are development/evaluation surfaces outside the product-runtime boundary.
- Evidence: [`agent_base/prompts/system_base.md`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/prompts/system_base.md); [`agent_base/react_agent.py`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/react_agent.py); [`agent_base/base.py`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/base.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: an upper layer may override completion hooks or add a reviewer, but generic extensibility is not a first-party S3*-specific constructor.

### Absence scope

- Surfaces inspected: system verification instructions, workspace/tool feedback, traces, persisted session state, benchmark/end-to-end evaluation artifacts and completion hooks.
- Plausible first-party paths checked: self-verification as S3*; trace replay as audit; benchmark tests as runtime auditor; `should_accept_plaintext_result` overrides as review seam.
- Why no material first-party path remains: evidence collection and claim checking stay inside the producing S1 path, while independent evaluation surfaces are test/benchmark or caller-composed rather than a shipped operational audit loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party outside-and-then adaptation loop is established.
- Disturbance / variety regulated: no path was found that senses external/future change, develops an adaptation option and returns that option to modify later organizational capability.
- Decisive decision or feedback right: not established for S4.
- Decision owner: not established.
- Supporting / enforcement mechanisms: context compaction, local `plan.md`/`memory.md`, web/research tools, provider/model request options and extensible prompts/tools.
- Closure path: compaction summarizes older turns for continuation of the current task; plan/memory files preserve current-task state. Neither constitutes a future-oriented adaptation decision returned into durable capability.
- Why this is / is not agent-owned: the compaction prompt is explicitly working memory for continued execution and says workspace files remain authoritative. Web search/research during a task is S1 environmental work unless it enters a prospective organizational adaptation loop.
- Evidence: [`agent_base/context_compact.py`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/context_compact.py); [`agent_base/prompts/system_base.md`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/prompts/system_base.md); [`agent_base/session_state.py`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/session_state.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the repository describes itself as a possible meta-harness for future optimization, but repository-development optimization is not a first-party product-runtime S4 organ.

### Absence scope

- Surfaces inspected: compaction and session memory, local plan/memory prompt guidance, web/scholar tools, model/provider configuration, custom tools and upper-layer extension points.
- Plausible first-party paths checked: compaction as learning; plan/memory as adaptation; web research as environmental intelligence; meta-harness positioning as self-improvement.
- Why no material first-party path remains: the reviewed surfaces retain or gather information for the current S1 task or expose generic customization. They do not produce and return a durable future capability/organizational adaptation decision.

## S5 — Policy and identity

- State: —
- Function: no first-party identity/ultimate-policy closure is established.
- Disturbance / variety regulated: the base system prompt, role addenda, tool restrictions, workspace safety rules and runtime configuration constrain operation but do not constitute an identity/constitutional issue resolved by legitimate ultimate authority.
- Decisive decision or feedback right: not established for S5.
- Decision owner: caller configuration supplies role prompts/tool sets and the shipped base prompt supplies static operating rules; no qualifying S5 authority path exists.
- Supporting / enforcement mechanisms: system prompt composition, role-prompt files, tool lists, workspace confinement, API/CLI configuration and AskUser.
- Closure path: configuration affects later run behavior, but no identity/ultimate-policy matter → authoritative decision → returned organization-wide policy loop is established.
- Why this is / is not agent-owned: static prompts and safety constraints are explicitly insufficient under the Profile; AskUser handles task-level missing information/approval rather than constitutional authority.
- Evidence: [`agent_base/prompts/system_base.md`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/prompts/system_base.md); [`agent_base/base.py`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/agent_base/base.py); [`README.md`](https://github.com/InternScience/ResearchHarness/blob/72e8a44737aadabc8c3f9e5c7ea76883b9c7032f/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: an upper-layer application can impose governance around ResearchHarness, but that authority belongs to the upper layer's recursion.

### Absence scope

- Surfaces inspected: base/role prompts, tool restrictions, workspace safety rules, configuration precedence, AskUser and extension hooks.
- Plausible first-party paths checked: system prompt as identity; role prompt as durable purpose; tool safety policy as S5; human clarification as ultimate authority.
- Why no material first-party path remains: these surfaces are static constraints, per-run configuration or task-level input paths; none closes an identity/ultimate-policy dispute at the reviewed recursion.

## Recursion

ResearchHarness is intentionally a base harness. Upper layers can subclass `BaseAgent` and alter role prompt/tool defaults or completion hooks, but the frozen repository does not itself instantiate a recursively viable multi-agent organization. Concurrent API requests and multiple tool calls are operational concurrency, not recursive S1 organizations.

## Variety and escalation

Operational variety is attenuated through workspace confinement, tool routing, retries/timeouts, max rounds/runtime, provider compatibility, interruption handling and context compaction. Evidence/tool results return directly to the same S1 model loop. AskUser provides bounded task clarification in interactive mode. None of those paths establishes a separate metasystem function at this recursion.

## Evidence gaps

- No bundled multi-agent coordination/control plane was found; the project's own positioning favors one main ReAct loop.
- No independent product-runtime audit actor/path was found beyond self-verification, traces and development/benchmark evaluation surfaces.
- No future-facing self-adaptation organ was found; context compaction and local memory remain current-task continuity.
- No identity/constitutional authority loop was found; role/system prompts and configuration remain static/operator-supplied constraints.
- ResearchClawBench and MarkScientist are explicitly separate and were not imported into this assessment.