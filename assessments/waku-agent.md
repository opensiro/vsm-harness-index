---
harness_id: waku-agent
project_name: Waku Agent
repository: https://github.com/ShenSeanChen/waku-agent
review_ref: b8310c08029732475b68076df02a6cc44e3e41e7
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Waku Agent

## Review boundary

- System in focus: one first-party Waku personal-assistant deployment at pinned revision `b8310c08029732475b68076df02a6cc44e3e41e7`, including the shipped model/tool loop, working-memory assembly, local durable memory, procedural skills, gateways/dashboard, opt-in graph workflows, tracing/eval surfaces and owner-editable `SOUL.md` identity/policy surface.
- Purpose and identity: operate as one local-first personal assistant that reasons over user requests, uses tools, preserves relevant long-term memory and standing preferences, and returns results through local gateways while remaining inspectable by its owner.
- Relevant environment: user requests and standing instructions, local calendar/notes/messages/files, configured provider/model responses, optional web/MCP/integration results, local memory state, conversation history, tool failures and current clock/context.
- Standard-distribution boundary: shipped `waku/` runtime and ordinary local dashboard/gateway paths at the pinned revision. Repository-development CI/release work, examples/lab experiments, future hosted designs and external model/provider systems remain outside the deployed assistant boundary unless directly reached as dependencies.
- Credited operating / distribution surfaces: CLI/dashboard/voice/chat gateway turns; `waku/loop/agent.py`; `runtime/session.py`; registered tools; local semantic/episodic/procedural memory; retrieval/consolidation; supported graph wrapper; dashboard human memory/SOUL editing; agent `update_soul` only as a mechanism returning parent policy into later operation.
- Adjacent first-party surfaces excluded from ownership: repository contributor workflow; deterministic/judge eval suites and `release_gate.py` as developer release-control surfaces; examples/lab experiments; future hosted architecture; provider/model internals; external MCP/services.
- First-party operating / deployment modes considered: ordinary single-agent turn; dashboard/CLI/voice/social gateways; opt-in graph workflow; memory retrieval/consolidation; owner memory/SOUL edits; user-directed agent memory/self-management tools.
- Recursion level: one Waku assistant is the system-in-focus. Its model-driven loop is the substantive S1 operation. The reviewed first-party runtime explicitly remains a single-agent architecture even when graph workflows wrap the loop.
- Reviewed revision: `b8310c08029732475b68076df02a6cc44e3e41e7`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Waku exposes one compact observe → reason → act → repeat model/tool loop. `run_loop` sends current working memory and tools to the configured model, executes requested tools through the first-party registry, appends tool results to the conversation and returns them to the model for later action. A turn ends when the model stops requesting tools or the deterministic iteration ceiling is reached. Gateways and dashboard drive this same loop rather than introducing separate operational actors.

Working memory is rebuilt per turn from the owner-editable `SOUL.md`, current time/provider identity, gated durable memory, matching procedural skills and recent conversation history. Long-term chat history is periodically consolidated by a separate summarizer into semantic facts and one episodic summary. The agent can also create procedural skills or append a standing behaviour rule to `SOUL.md` when the user teaches or requests one. These are substantive memory/policy mechanisms, but they do not automatically establish S4 or autonomous S5 ownership.

The graph layer is intentionally not a multi-agent organization. First-party architecture documentation states that graph `agent_node` execution is the same Waku loop invoked as a step, with deterministic edge routing and no peer-to-peer agent messaging. Therefore graph parallelism/routing is not used to manufacture an S2 claim.

Waku's eval/release surfaces belong to the development/release process rather than the deployed assistant operating loop. `make gate` manually runs deterministic pytest and optional LLM-as-judge suites after prompt/model/retrieval changes and exits open/closed for a release decision. Those checks do not independently inspect each deployed S1 turn and feed findings back into that same assistant operation, so they are not credited as S3* at the assessed recursion.

The durable identity/policy surface is `SOUL.md`. `runtime/session.py` describes it as the editable persona file and places it first in every turn's system prompt; changing it changes who Waku is. The dashboard supports full human rewrite with changes live on the next agent turn. `update_soul` lets the model append a durable behaviour rule, but its contract is specifically to save a standing preference/instruction the user gave it and the default system prompt tells it to do so on the user's behalf. Ultimate policy authority therefore remains with the parent user, yielding S5=`P` rather than autonomous policy ownership.

## Operational model

The model actor owns S1 task choices inside one Waku assistant. Deterministic iteration limits, retrieval gates, graph routing and gateway serialization support that operation but do not create separate metasystemic owners. Long-term memory adapts what the same actor can recall, but no separate outside/future intelligence loop is established. The user remains the legitimate parent for ultimate persona/standing rules through `SOUL.md`, and first-party runtime assembly returns those rules into each later S1 turn.

## S1 — Operations

- State: A
- Function: autonomously perform personal-assistant work through iterative model reasoning, model-selected tool calls, observation of tool results and subsequent model action.
- Disturbance / variety regulated: heterogeneous user requests, changing local calendar/notes/message/file state, web/MCP/integration results, tool failures, memory relevance and ambiguous natural-language task requirements.
- Decisive decision or feedback right: choose substantive next actions/tool calls, interpret returned observations and decide when to stop tool use and return a result.
- Decision owner: the configured model actor executing inside Waku's first-party `run_loop`.
- Supporting / enforcement mechanisms: tool registry/execution, provider adapters, working-memory assembly, current-time context, gated retrieval, matching skills, conversation history and max-iteration guardrail.
- Closure path: user request + assembled working memory → model selects tool/action → first-party runtime executes tool → tool result is appended and returned to the model → later model action changes from observation → final reply returns through the gateway.
- Boundary reachability: CLI, dashboard, voice and other shipped gateways invoke the same first-party assistant runtime; no repository-development actor is required.
- Why this is / is not agent-owned: deterministic code executes tools and caps iterations, but the model chooses the task-specific semantic action sequence and synthesizes the final response rather than following a fixed workflow result.
- Evidence: [`waku/loop/agent.py`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/waku/loop/agent.py); [`waku/runtime/session.py`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/waku/runtime/session.py); [`docs/architecture.md`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/docs/architecture.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider-hosted inference remains a dependency. The autonomy state credits the model actor reached through Waku's shipped loop, not the external provider as a separate organizational owner.

## S2 — Coordination

- State: —
- Function: no material first-party S2 coordination function is established at the assessed single-assistant recursion.
- Disturbance / variety regulated: the review looked specifically for interference among multiple distinct S1 operational units, not merely graph branches, tool calls, gateway concurrency or deterministic routing.
- Decisive decision or feedback right: no qualifying inter-S1 coordination decision exists because the reviewed runtime does not establish multiple distinct S1 agents whose interference must be attenuated.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: graph edges, node scheduling, gateway/server locks and ordinary tool sequencing may order execution, but they do not operate among distinct first-party S1 agents.
- Closure path: no qualifying distinct-S1 disturbance → attenuation → changed later S1 behaviour loop is present.
- Why this is / is not agent-owned: first-party architecture explicitly states that graph workflows are still not multi-agent; an `agent_node` invokes the same loop as a workflow step, and deterministic edges/routing do not create peer organizational units.
- Evidence: [`docs/architecture.md`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/docs/architecture.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: parallel graph/tool execution can be useful concurrency without satisfying S2's requirement for coordination among multiple distinct S1 operations.

### Absence scope

- Surfaces inspected: core loop, graph engine/workflow description, gateways/dashboard, tool registry/execution and memory processes.
- Plausible first-party paths checked: graph parallel steps; routed `agent_node` execution; concurrent gateway requests; tool sequencing; procedural skills.
- Why no material first-party path remains: the repository explicitly defines the deployed architecture as single-agent; graph nodes reuse the same loop and no peer-to-peer or separately owned S1 units are established, so there is no eligible inter-S1 disturbance to coordinate.

## S3 — Inside-and-now control

- State: —
- Function: no material separate whole-system current-control function is established above Waku's single S1 loop.
- Disturbance / variety regulated: runtime mechanisms bound a turn, choose memory retrieval and route graph steps, but they regulate local execution mechanics rather than a portfolio of multiple current S1 commitments/resources on behalf of the whole assistant.
- Decisive decision or feedback right: no qualifying whole-system current-control judgment/feedback right is established.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: max-iteration stop, retrieval gate, graph router, dashboard agent lock, gateway/session lifecycle and tool enablement.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: model decisions inside the assistant are S1 task decisions. Deterministic runtime limits/routing do not become a separate whole-system S3 owner merely because they constrain the turn.
- Evidence: [`waku/loop/agent.py`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/waku/loop/agent.py); [`docs/architecture.md`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/docs/architecture.md); [`waku/ops/dashboard.py`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/waku/ops/dashboard.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: this result is recursion-specific. A deterministic guard can be important operational control without satisfying Profile S3 at the assistant-organizational boundary.

### Absence scope

- Surfaces inspected: loop guardrails; runtime/session assembly; graph routing; dashboard/gateway concurrency; tool registry; tracing/usage surfaces; memory retrieval/consolidation.
- Plausible first-party paths checked: max iterations as S3; graph router as manager; retrieval gate; dashboard lock; trace/usage dashboard; tool enablement/configuration.
- Why no material first-party path remains: each inspected path constrains or observes one assistant turn/workflow and lacks a distinct whole-system current view and regulatory decision scope over multiple operational units/resources/commitments at this recursion.

## S3* — Complementary audit

- State: —
- Function: no material complementary audit function closes inside the deployed Waku assistant boundary.
- Disturbance / variety regulated: repository evals can detect regressions in prompts/models/tool behaviour during development, but they are not an independent audit channel over each live S1 operation.
- Decisive decision or feedback right: no qualifying runtime audit owner independently inspects a live assistant claim/output through complementary access and returns findings into current correction.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: deterministic pytest evals, DeepEval judge suite, traces and `release_gate.py` support repository development/release decisions rather than live complementary audit.
- Closure path: the developer manually runs `make gate` after changing a prompt/model/config; test/judge results produce an exit-code release gate. That path does not close as live S1 output → independent operational audit → corrective return into the same assistant operation.
- Why this is / is not agent-owned: the judge suite may use an LLM, but an LLM reviewer is not S3* by name; the decisive missing property is a first-party complementary runtime access/feedback path at the assessed deployment boundary.
- Evidence: [`docs/evals.md`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/docs/evals.md); [`waku/ops/release_gate.py`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/waku/ops/release_gate.py).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: this is not a claim that Waku lacks useful evaluation. It distinguishes developer/release evaluation from complementary audit inside the deployed assistant organization.

### Absence scope

- Surfaces inspected: deterministic evals, judge evals, release gate, tracing, dashboard Ops view, graph/error paths and ordinary tool-result feedback.
- Plausible first-party paths checked: LLM-as-judge as S3*; deterministic tool-fire checks; release gate; trace inspection; dashboard error/status presentation.
- Why no material first-party path remains: reviewed evals are manually invoked development/release controls outside the live assistant loop, while runtime tracing/status is observational and does not establish an independent corrective audit owner over current S1 output.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material distinct external-and-prospective adaptation function is established at the assessed assistant recursion.
- Disturbance / variety regulated: Waku can remember internal conversation history, distill facts/episodes, retrieve relevant memory and save user-taught procedural skills, but those mechanisms learn primarily from its own past operations or explicit parent teaching.
- Decisive decision or feedback right: no qualifying S4 owner builds a distinct model of the outside/future environment and returns prospective adaptation options into current organizational control.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: retrieval gate, semantic/episodic stores, periodic consolidation, procedural `SKILL.md`, `create_skill`, optional web/tool access and graph routing.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: the consolidation summarizer autonomously extracts durable internal facts/episodes and the model can create a user-taught skill, but internal-history compression/procedural learning is not the Profile S4 outside-and-then function.
- Evidence: [`waku/memory/consolidation.py`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/waku/memory/consolidation.py); [`waku/tools/memory_admin.py`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/waku/tools/memory_admin.py); [`docs/architecture.md`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/docs/architecture.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: web search or external tools can inform a current S1 task; without a distinct prospective adaptation organization and current/future return loop, that does not establish S4.

### Absence scope

- Surfaces inspected: retrieval gate; semantic/episodic memory; consolidation; procedural skills/create_skill; web/MCP tools; graph workflows; eval/release history.
- Plausible first-party paths checked: consolidation as adaptation; procedural skill learning; external search as environmental intelligence; release-gate history; memory retrieval as future planning.
- Why no material first-party path remains: inspected learning paths summarize internal conversations or explicit user teaching, while external tools remain part of current task execution; no separate outside/future model and no S3↔S4 current/future organizational conversation is established.

## S5 — Policy and identity

- State: P
- Function: define the durable persona, standing behavioural rules and ultimate user-specific operating policy that governs later Waku turns.
- Disturbance / variety regulated: drift in assistant identity, standing preferences, behavioural expectations and owner-defined constraints across sessions.
- Decisive decision or feedback right: decide the authoritative content of `SOUL.md`, including persona and standing behaviour rules that later assistant turns must receive.
- Decision owner: the legitimate parent user/owner. The dashboard can rewrite `SOUL.md` directly; when the user gives a standing instruction through chat, the agent's `update_soul` tool persists that parent-provided policy rather than independently claiming ultimate policy authority.
- Supporting / enforcement mechanisms: `load_soul`, automatic first-position system-prompt inclusion, dashboard `save_soul`, append-only `update_soul`, local filesystem persistence and next-turn session rebuild.
- Closure path: owner identifies a persona/standing-policy issue → owner edits `SOUL.md` directly or instructs Waku to remember a standing behaviour rule → first-party runtime persists the changed policy → next turn `load_soul` reads it → session system prompt includes it → later S1 behaviour is governed by the owner's returned policy.
- Boundary reachability: `SOUL.md` is created/read in the ordinary shipped runtime and is displayed/editable through the local dashboard; no repository maintainer action is required.
- Why this is / is not agent-owned: the model may choose the exact phrasing/tool call used to persist an explicitly requested standing preference, but the ultimate policy decision comes from the user. The tool contract says to use `update_soul` for a standing preference the user gives and preserves the user's superior rewrite authority, so the decisive S5 owner is parent (`P`).
- Identity / ultimate-policy issue: who Waku is for this user and which durable standing behavioural rules/preferences govern future turns.
- Ultimate authority in each claimed mode: Parent (`P`) — the local user/owner who can directly rewrite `SOUL.md` and whose standing instructions the agent is permitted to persist.
- Return-to-operation path: `runtime/session.py::load_soul` reads the authoritative `SOUL.md` on each system-prompt build; the changed persona/rules therefore govern the next and later model/tool turns.
- Evidence: [`waku/runtime/session.py`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/waku/runtime/session.py); [`waku/tools/memory_admin.py`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/waku/tools/memory_admin.py); [`waku/ops/dashboard.py`](https://github.com/ShenSeanChen/waku-agent/blob/b8310c08029732475b68076df02a6cc44e3e41e7/waku/ops/dashboard.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic prompt editability is not the positive evidence. The mapping depends on `SOUL.md` being explicitly the persistent identity/standing-rule surface and on its automatic return into later runtime operation.

## Distributed OSS parent arrangement

The repository maintainer/contributor organization is outside the deployed personal-assistant boundary and does not donate S5. The mapped parent is the local assistant owner/user whose persistent `SOUL.md` policy governs that deployment.

## Self-hosted and non-human modes

Waku is local-first. A user may operate it through non-interactive gateways, but those gateways still execute the same single S1 loop and the same owner-defined `SOUL.md`. Scheduled/background invocation, where present, does not create an additional VSM owner by itself.

## Recursion

The assessed recursion contains one substantive model-driven assistant operation. Tool calls, graph nodes, memory summarizers and eval judges are not assumed to be separate recursive viable systems merely because they invoke code or models. This keeps single-agent task execution separate from metasystemic organizational claims.

## Variety and escalation

Waku attenuates variety with tool schemas, max-iteration stopping, retrieval gating, bounded history, provider adapters, graph routing and durable owner rules. It amplifies response variety through model reasoning, local/web/MCP tools, memory and procedural skills. Failures generally fail open/back to the plain loop or surface to the user; these mechanisms support the mapped S1/S5 paths without independently establishing S2–S4.

## Evidence gaps

- The architecture explicitly rejects a multi-agent interpretation, so graph routing/parallelism is not promoted to S2.
- No separate whole-system current-control actor/view is established above the single S1 loop, so deterministic runtime guards remain support rather than S3.
- Built-in eval and release-gate machinery is developer LLM-Ops, not a live complementary-audit loop, so S3* remains absent.
- Durable memory, consolidation and user-taught skills are real learning mechanisms but do not close the external/prospective S4 function.
- `SOUL.md` closes S5 as parent-owned identity/policy because the local user retains ultimate rewrite authority and agent-side persistence is constrained to user-provided standing preferences.
