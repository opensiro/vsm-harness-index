---
harness_id: agentyou
project_name: AgentYou
repository: https://github.com/shreyasic77/agentyou
review_ref: a8289d95608aa974f2a51aba68af5374bfa71d01
reviewed_at: 2026-09-22
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-22
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: C
autonomy_s5: —
---

# AgentYou

## Review boundary

- System in focus: one locally run AgentYou personal second-brain application at frozen revision `a8289d95608aa974f2a51aba68af5374bfa71d01`, including its application-specific LangGraph graph, specialist agent implementations, Streamlit entry point, APScheduler background jobs, persistent user model, SQLite/Chroma-backed state and shipped MCP server.
- Purpose and identity: act as a proactive personal assistant that interprets the user's knowledge, habits and routine, produces context-aware advice and insights, and can surface time-sensitive nudges without waiting for a new user prompt.
- Relevant environment: user messages and preferences, habit/routine completion history, time and schedule state, the user's note corpus, uploaded documents, local persistence, external or local model providers and any external MCP client used with the standalone server.
- Standard-distribution boundary: the repository-shipped Streamlit app, `agents/` graph/specialists, `core/` scheduler/user model/database, `ingestion/` and `mcp_server/`. Generic LangGraph/LangChain behavior, model-provider internals and third-party MCP clients are dependencies rather than inherited VSM owners.
- Credited operating / distribution surfaces: `ui/app.py`; `agents/orchestrator.py`; `agents/memory_agent.py`; `agents/habit_agent.py`; `agents/routine_agent.py`; `agents/nudge_agent.py`; `core/scheduler.py`; `core/user_model.py`; `mcp_server/server.py`; `ingestion/ingest.py` where reached by the shipped app.
- Adjacent first-party surfaces excluded from ownership: recruiter/demo presentation text in `DEMO_GUIDE.md`; test-only fixtures and synthetic scenarios; `scripts/seed_demo.py`; repository-development/maintainer activity; README/DEMO claims where the frozen implementation does not wire the described path; generic LangGraph/LangChain framework internals.
- First-party operating / deployment modes considered: normal Streamlit chat; sidebar habit logging and document ingestion; scheduled background nudge/correlation/routine-report jobs started by the app; standalone first-party MCP server as an exposed construction/integration surface where relevant.
- Recursion level: one AgentYou personal-assistant organization serving one user. Specialist Memory/Habit/Routine/Nudge actors are assessed as application subunits; they are not assumed to be independently viable recursive organizations merely because they are separate classes/nodes.
- Reviewed revision: `a8289d95608aa974f2a51aba68af5374bfa71d01`.
- Observation date: 2026-09-22.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

AgentYou's shipped UI calls an application-specific LangGraph graph. An LLM router classifies each incoming message into memory, habit, routine/reminder, nudge, multi-domain or general-conversation intent. Single-domain routes invoke one specialist; the multi-domain route launches Memory, Habit and Routine agents concurrently, then a separate LLM call synthesizes their returned text. Each specialist reads first-party persistent state and uses an LLM to interpret that evidence into the response returned to the user.

The Streamlit application also starts an APScheduler background loop. Its jobs check reminders, habit risks, routine overload, habit correlations and weekly routine performance. The proactive scheduled path is materially deterministic around candidate construction, priority thresholds, deduplication, preferred hours and daily nudge budgets; a model is not credited with ownership merely because the component is named NudgeAgent. Interactive `NudgeAgent.run`, by contrast, does invoke an LLM to synthesize an operational response.

AgentYou keeps a structured JSON user model alongside SQLite/Chroma persistence. Habit correlation and timing analysis can update that model, and every specialist receives a compact user-context projection. The repository also ships an MCP server with typed knowledge/habit/routine/reminder/user-model mutation and query tools. However, the frozen application graph does not bind those MCP tools into the specialist LLM calls: specialist source reads the database/user model directly, and the Streamlit sidebar performs direct database writes for habit logging and ingestion. The MCP server is therefore credited only where it provides an explicit first-party construction path, not as if the standard graph were already tool-calling through MCP.

The strongest future-facing surface is the Routine adaptation engine. It turns repeated skip patterns, workload/energy mismatch and completion trends into concrete options such as removing/replacing a routine, rescheduling it or reducing deep-work load. A weekly scheduled job surfaces the top recommendation. The standard app does not apply that recommendation to current routines, and the MCP registry has creation/state-update primitives but no wired recommendation-to-activation path. This supports a constructor S4 path rather than autonomous or parent-closed S4.

## Operational model

The ordinary autonomous operational decision owner is the model actor reached through the AgentYou graph: the router interprets user intent and the selected specialist interprets first-party evidence into the substantive answer or advice returned to the user. Memory retrieval, habit/routine statistics and persistence code supply observations; they do not preselect the model's final interpretation. Scheduled notifications provide an additional deterministic proactive operating path but are not used to inflate agent ownership beyond what the interactive model loop establishes.

The graph does not implement a distinct current-control metasystem. Routing selects which specialist handles a request and multi-agent synthesis combines three results, but there is no evidenced actor with a whole-organization current view plus authority to rebalance resources, commitments, priorities or interventions across those operations. Likewise, the repository does not supply a runtime complementary-audit actor independent of the ordinary production path.

For future adaptation, first-party code does more than generic persistence: `suggest_adaptations()` explicitly constructs future routine-change options from longitudinal behavior and `job_weekly_routine_report()` surfaces them. What is missing is the binding that authoritatively selects and applies an option to subsequent operation. This is kept at `C`; the separate MCP mutation surface does not silently upgrade the standard app to autonomous closure.

## Primary evidence

- [`README.md`](https://github.com/shreyasic77/agentyou/blob/a8289d95608aa974f2a51aba68af5374bfa71d01/README.md) — declared product boundary, four-specialist architecture, persistent user model and scheduled proactive flow.
- [`agents/orchestrator.py`](https://github.com/shreyasic77/agentyou/blob/a8289d95608aa974f2a51aba68af5374bfa71d01/agents/orchestrator.py) — LLM intent routing, specialist invocation, parallel multi-domain execution and final synthesis.
- [`agents/memory_agent.py`](https://github.com/shreyasic77/agentyou/blob/a8289d95608aa974f2a51aba68af5374bfa71d01/agents/memory_agent.py) — note retrieval/connection evidence followed by model-owned synthesis.
- [`agents/habit_agent.py`](https://github.com/shreyasic77/agentyou/blob/a8289d95608aa974f2a51aba68af5374bfa71d01/agents/habit_agent.py) — streak/trend/risk/correlation analysis, user-model updates and model interpretation.
- [`agents/routine_agent.py`](https://github.com/shreyasic77/agentyou/blob/a8289d95608aa974f2a51aba68af5374bfa71d01/agents/routine_agent.py) — skip-pattern/overload analysis, explicit routine adaptation options and weekly report generation.
- [`agents/nudge_agent.py`](https://github.com/shreyasic77/agentyou/blob/a8289d95608aa974f2a51aba68af5374bfa71d01/agents/nudge_agent.py) — proactive candidate construction, priority/deduplication logic and interactive LLM synthesis.
- [`core/scheduler.py`](https://github.com/shreyasic77/agentyou/blob/a8289d95608aa974f2a51aba68af5374bfa71d01/core/scheduler.py) — scheduled proactive checks, weekly correlation analysis, weekly routine report and best-time recalculation.
- [`core/user_model.py`](https://github.com/shreyasic77/agentyou/blob/a8289d95608aa974f2a51aba68af5374bfa71d01/core/user_model.py) — durable user context, goals/preferences and learned habit/routine summaries consumed by agents.
- [`mcp_server/server.py`](https://github.com/shreyasic77/agentyou/blob/a8289d95608aa974f2a51aba68af5374bfa71d01/mcp_server/server.py) — first-party typed query/mutation primitives; inspected as a construction surface rather than assumed graph wiring.
- [`ui/app.py`](https://github.com/shreyasic77/agentyou/blob/a8289d95608aa974f2a51aba68af5374bfa71d01/ui/app.py) — actual app startup, scheduler wiring, graph invocation and direct UI persistence paths.
- [`DEMO_GUIDE.md`](https://github.com/shreyasic77/agentyou/blob/a8289d95608aa974f2a51aba68af5374bfa71d01/DEMO_GUIDE.md) — explicit statement that nudge timing is currently rule-based and that a response-feedback learning loop would be future work; used only to corroborate the S4 closure limit.

## S1 — Operations

- State: A
- Function: produce useful personal-assistant outcomes by interpreting the user's request and local personal evidence into answers, insights, routine/habit guidance and proactive advice.
- Disturbance / variety regulated: heterogeneous user intents, note content, habit/routine state, changing completion history, timing/overload conditions, model uncertainty and cross-domain requests that require several evidence sources.
- Decisive decision or feedback right: classify the incoming conversational need, choose the relevant specialist path and interpret retrieved/computed evidence into the substantive response or advice returned to the user.
- Decision owner: the model actors in the shipped AgentYou graph — the LLM router for intent selection and the selected specialist/synthesizer model for the substantive user-facing result.
- Supporting / enforcement mechanisms: LangGraph edges/state, direct SQLite/Chroma reads, user-model context projection, deterministic statistical/risk computations, Streamlit presentation and model-provider adapters.
- Closure path: user request → model intent classification → specialist evidence retrieval/computation → model interpretation/synthesis → response returned through the Streamlit chat; scheduled paths separately push deterministic first-party nudges into the UI queue.
- Boundary reachability: `ui/app.py` directly invokes `agents.orchestrator.chat`, and the compiled first-party graph invokes the router and specialist LLM calls in the standard run path without requiring an external orchestrator implementation.
- Why this is / is not agent-owned: deterministic retrieval/statistics constrain the evidence available, but they do not determine the model's final interpretation, cross-domain synthesis or user-facing advice. The scheduled deterministic nudge path is treated as support/parallel operation rather than the basis for agent ownership.
- Evidence: `agents/orchestrator.py`, `agents/memory_agent.py`, `agents/habit_agent.py`, `agents/routine_agent.py`, `agents/nudge_agent.py`, `ui/app.py`.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the app does not implement a general iterative tool-calling loop in its LangGraph specialists; `A` is credited for autonomous reasoning over first-party observations and response selection, not for MCP tool autonomy that the frozen graph does not wire.

## S2 — Coordination

- State: —
- Function: no material first-party S2-specific coordination path is established among distinct operational units at the reviewed recursion.
- Disturbance / variety regulated: the review looked for a concrete interference, conflict or oscillation among specialist operations, not merely routing, parallel execution or shared persistence.
- Decisive decision or feedback right: no first-party coordination judgment was established that detects an inter-S1 disturbance, selects an attenuating response and feeds that response back into later specialist behavior.
- Decision owner: none established for qualifying S2.
- Supporting / enforcement mechanisms: LangGraph conditional routing, `asyncio.gather` for multi-domain requests, shared `ARIAState`, shared user-model/SQLite state and deterministic scheduler timing.
- Closure path: no qualifying disturbance → coordination response → changed subsequent S1 behavior loop is implemented. Multi-domain execution gathers three results and synthesizes them, which is task composition rather than interference regulation.
- Why this is / is not agent-owned: the LLM router chooses a specialist from user intent and the multi node combines outputs, but neither path is evidenced as mutual adjustment against an inter-S1 conflict. Parallel specialist reads/writes do not become S2 merely because they share state.
- Evidence: `agents/orchestrator.py`, `core/user_model.py`, specialist implementations.
- Basis: structural.
- Confidence: high.
- Caveats: the parallel multi-domain path can cause specialists to touch shared persistent/user-model state in the same overall request; the frozen source does not pair that potential interference with an S2-specific collision-resolution mechanism.

### Absence scope

- Surfaces inspected: LangGraph router/edges/shared state, multi-agent parallel branch, all four specialist implementations, user-model persistence, scheduler jobs and MCP server tool registry.
- Plausible first-party paths checked: intent routing, parallel `asyncio.gather`, result synthesis, shared JSON/SQLite state, scheduler serialization and MCP request dispatch.
- Why no material first-party path remains: these mechanisms route, run, combine or persist work, but primary evidence does not tie any of them to regulation of a specific inter-S1 interference/oscillation with a closed feedback path into later S1 behavior.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system current-control function is established at the reviewed AgentYou organization boundary.
- Disturbance / variety regulated: the review looked for current cross-operation resource/commitment/prioritization/accountability decisions on behalf of the whole rather than interpreting the `orchestrator` name as S3.
- Decisive decision or feedback right: no actor is evidenced as holding a whole-organization current view plus authority to rebalance resources, commitments, priorities or interventions across specialist operations.
- Decision owner: none established for qualifying S3.
- Supporting / enforcement mechanisms: the intent router, static graph topology, multi-agent synthesizer, nudge priority scores, preferred-hour checks, daily nudge budget and APScheduler triggers.
- Closure path: these mechanisms choose a request path or enforce preconfigured timing/budget rules, but no whole-system current-control decision → operational intervention → changed current organization loop was established.
- Why this is / is not agent-owned: router and synthesizer models own operational interpretation, not metasystemic regulation; deterministic scheduler/nudge limits enforce configured bounds and do not own a current-control decision.
- Evidence: `agents/orchestrator.py`, `agents/nudge_agent.py`, `core/scheduler.py`, `ui/app.py`.
- Basis: structural.
- Confidence: high.
- Caveats: a future supervisor that can inspect all active specialist work and change shared commitments/resources would require reassessment; the frozen graph executes one routed branch or a fixed three-specialist fan-out.

### Absence scope

- Surfaces inspected: router and multi-agent graph, specialist state access, scheduler, nudge priority/budget logic, UI controls and MCP server.
- Plausible first-party paths checked: central orchestrator, multi-domain synthesis, proactive scheduler, cross-domain NudgeAgent and user-model context.
- Why no material first-party path remains: none combines a whole-system current operational view with authority over current resources/commitments/priorities/interventions; observed centralization is routing, presentation or fixed enforcement.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit relation is supplied in the standard runtime.
- Disturbance / variety regulated: incorrect model interpretations, stale/incorrect personal state and weak recommendations were considered, but no first-party runtime path obtains materially different operational evidence and independently challenges ordinary reporting.
- Decisive decision or feedback right: no qualifying audit owner is established that forms an independent judgment and returns findings into subsequent control.
- Decision owner: none established for qualifying S3*.
- Supporting / enforcement mechanisms: source citation in MemoryAgent responses, deterministic statistics, nudge deduplication and repository unit tests improve correctness but do not constitute runtime complementary audit.
- Closure path: no independent audit finding → current-control response → changed subsequent operation loop is implemented.
- Why this is / is not agent-owned: specialist self-interpretation and ordinary data checks stay inside the production path; tests are development-only and are excluded from runtime ownership.
- Evidence: `agents/memory_agent.py`, `agents/habit_agent.py`, `agents/routine_agent.py`, `tests/test_phase2.py`.
- Basis: explicit absence after boundary review.
- Confidence: high.
- Caveats: citing retrieved notes gives evidence-grounded S1 behavior, not the independent complementary access required for S3*.

### Absence scope

- Surfaces inspected: specialist response construction, retrieved-note citation behavior, statistics/risk checks, scheduler/nudge logging, tests and MCP query paths.
- Plausible first-party paths checked: self-checking via source retrieval, deterministic validation/statistics, duplicate suppression, test suite and any separate reviewer/verifier actor.
- Why no material first-party path remains: no runtime actor has a sufficiently independent complementary channel to operational reality plus findings-to-control closure; repository tests and ordinary retrieval are outside or inside the normal production path respectively.

## S4 — Outside-and-then intelligence

- State: C
- Function: expose a first-party future-facing adaptation path that turns longitudinal user behavior and workload/energy mismatch into concrete routine-change options for later operation.
- Disturbance / variety regulated: persistent routine skipping, changing completion patterns, overload relative to the user's observed capacity and behavioral patterns that make the current routine a poor fit for future use.
- Decisive decision or feedback right: decide which routine adaptation to adopt — remove/replace a repeatedly skipped item, reschedule it, reduce deep-work load or preserve a newly successful arrangement — and cause that choice to alter later routine behavior. AgentYou generates the options, but the shipped app does not own/apply that final activation decision.
- Decision owner: constructor path only. First-party adaptation analysis deterministically generates specific options; a downstream autonomous actor/application must still be composed to select and apply them to persistent routine capability.
- Supporting / enforcement mechanisms: `analyse_skip_patterns`, `detect_overload`, `suggest_adaptations`, weekly report generation/scheduling, persistent user-model statistics, and separate MCP routine/user-model mutation primitives.
- Closure path: historical user behavior + current capacity model → explicit future routine-change options → weekly/on-demand recommendation → **missing binding in the standard app** that selects/applies the option to persistent routine state → later operation. The exposed adaptation and mutation surfaces make the path constructible, but the activation edge is incomplete.
- Boundary reachability: the option-generation functions are shipped in `agents/routine_agent.py` and are invoked by the standard scheduled weekly report/on-demand RoutineAgent path; the first-party MCP server separately exposes persistent routine creation and user-model update primitives. No development-only actor is borrowed for the constructor claim.
- Why this is / is not agent-owned: an LLM may explain and prioritize already-generated recommendations to the user, but no model in the standard distribution is wired with authority to apply those changes. Deterministic heuristics create the options and the developer/downstream composition must supply autonomous selection/activation, so the state remains `C` rather than `A`.
- Evidence: `agents/routine_agent.py`, `core/scheduler.py`, `mcp_server/server.py`, `core/user_model.py`, `DEMO_GUIDE.md`.
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: habit correlations/best-time persistence alone are not credited as S4. The positive mapping is narrowly the explicit future routine-adaptation path; the demo documentation itself notes that a genuine response-feedback learning loop for nudge timing remains future work.
- External distinction: observed user completion/skip behavior and workload fit relative to the user's recorded energy/capacity pattern.
- Future / prospective distinction: whether the current routine arrangement is likely to remain viable on later days/weeks given repeated skips, overload or changing completion performance.
- Adaptation option generated: remove/replace, reschedule, reduce workload or reinforce an arrangement that recently improved.
- Path back into current capability / S3: the standard app surfaces the option to the user, while first-party MCP primitives can create routine state/update the user model; the frozen source does not bind recommendation selection to a routine mutation. A downstream actor/application must compose that final return edge.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy decision loop is established for the AgentYou organization.
- Disturbance / variety regulated: user name/goals/preferences, agent system prompts and model/provider configuration shape context and behavior, but the review found no identity/ultimate-policy issue with a legitimate decisive authority and returned organizational closure.
- Decisive decision or feedback right: no qualifying runtime right to decide AgentYou's ultimate identity, ethos or policy was established.
- Decision owner: none established for qualifying S5.
- Supporting / enforcement mechanisms: static specialist/system prompts, `user_model.identity`/goals, nudge preferences, model-provider settings and the MCP `user_model_update_goals` primitive.
- Closure path: configuration/profile values feed later prompts, but no identity/policy issue → ultimate-authority judgment → returned governance path is implemented at the assessed recursion.
- Why this is / is not agent-owned: the conversation agent can discuss profile setup and the MCP server can update user goals, but a profile/configuration edit is not S5 by itself and the standard chat graph does not wire an identity-level decision/escalation path.
- Evidence: `agents/orchestrator.py`, `core/user_model.py`, `mcp_server/server.py`, `core/config.py`.
- Basis: structural.
- Confidence: high.
- Caveats: the user's legitimate authority over their personal data/goals is not disputed; the negative finding is only that the repository does not turn that authority into a first-party closed S5 organizational conversation.

### Absence scope

- Surfaces inspected: specialist system prompts, conversation path, user-model identity/goals/preferences, configuration/provider settings, MCP user-model tools, Streamlit UI and scheduler.
- Plausible first-party paths checked: conversational profile setup, direct/MCP goal updates, nudge-policy preferences, model selection and static agent instructions.
- Why no material first-party path remains: inspected surfaces configure operational context or preferences but do not establish a genuine identity/ultimate-policy issue reaching ultimate authority and returning as an authoritative S5 decision governing the organization as a whole.

## Distributed OSS parent arrangement

Repository maintainers/contributors, portfolio/demo presentation and development tests are outside the local personal-assistant runtime boundary and are not used to infer parent governance. One user can edit local profile/configuration or use an external MCP client, but ordinary configuration is not promoted to S3/S4/S5 parent mode without a function-specific returned decision loop.

## Self-hosted and non-human modes

AgentYou is local/self-hosted and can use OpenAI or Ollama-style model backends. The local operator controls configuration and persisted personal data. No `(P)` state is inferred merely from that operator control. For S4, the standard app stops at recommendation and a separate construction surface; it does not expose a closed parent-return application step for routine adaptations.

## Recursion

The assessment is at the one-user AgentYou application recursion. Memory/Habit/Routine/Nudge specialists have differentiated purposes and evidence domains, but the frozen repository does not establish them as independently viable recursive systems. LangGraph nesting/parallel fan-out is therefore treated as task organization, not VSM recursion.

## Variety and escalation

AgentYou attenuates user-request variety through model intent routing and specialist evidence domains, while local persistence preserves user-specific distinctions across sessions. The proactive scheduler amplifies regulatory reach by revisiting habit/routine state without a new prompt, but its timing/budget rules are deterministic. Cross-domain requests fan out to multiple specialists and return through one synthesis call. Future routine misfit is surfaced as adaptation options, but activation remains outside the autonomous standard path. There is no distinct first-party escalation channel for whole-system current control, complementary audit or identity-level policy.

## Evidence gaps

The main classification boundary is S4. The frozen code clearly performs longitudinal/future-facing routine adaptation analysis and emits concrete change options, which is stronger than generic memory/learning. However, it does not wire those recommendations to persistent routine mutation or to a parent decision-return protocol; therefore `C` is used rather than `A`, `P` or a composite state. The README/DEMO description of MCP as the agents' data interface is not used to infer stronger autonomy because the actual frozen specialist implementations read the database/user model directly and the orchestrator does not bind MCP tools.