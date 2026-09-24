---
harness_id: agentoven
project_name: AgentOven
repository: https://github.com/agentoven/agentoven
review_ref: 7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6
reviewed_at: 2026-09-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-24
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AgentOven

## Review boundary

- System in focus: one public OSS AgentOven control-plane installation at pinned revision `7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6`, including the built-in managed Go executor, model router, MCP gateway, session/context machinery, Recipe workflow engine, community guardrails, process manager and public control-plane/API surfaces.
- Purpose and identity: define and run managed agents and multi-agent Recipes through a first-party model/tool runtime, while also exposing separate proxy/process paths for framework-native or external agents.
- Relevant environment: external model-provider APIs; MCP servers/tools; operator/API callers; framework-native LangChain/LangGraph/CrewAI/custom processes; external-mode A2A agents; optional infrastructure such as Docker/Kubernetes; humans resolving configured workflow gates.
- Standard-distribution boundary: AgentOven's built-in Go executor and OSS control-plane services are inside. External/framework-native processes retain their own reasoning loops and are not allowed to donate autonomy. Pro-only implementations and interfaces whose community implementation is no-op/unavailable are excluded from positive ownership claims.
- Credited operating / distribution surfaces: `control-plane/internal/executor/executor.go`; `control-plane/internal/api/handlers/handlers.go`; `control-plane/internal/workflow/engine.go`; `control-plane/internal/guardrails/guardrails.go`; `control-plane/pkg/models/models.go`; `control-plane/pkg/server/server.go`; shipped managed-agent and Recipe paths.
- Adjacent first-party surfaces excluded from ownership: Pro-only test-suite/promotion/environment implementations, repository-development ADR/CI/release work except as corroboration, framework-native generated/user processes where their own runtime owns the loop, and generic extension interfaces without a community implementation.
- First-party operating / deployment modes considered: default `managed` Agent mode with `RuntimeAgentOven`; reactive and agentic behavior; built-in MCP tool execution; session persistence/sliding context; built-in managed-to-managed `agentoven_delegate`; Recipe DAG execution with agent, evaluator, router, fan-out/fan-in, condition, map, sub-recipe and human-gate steps; community guardrails.
- Recursion level: one AgentOven installation. Individual managed agents are S1 operational units. A Recipe can compose several such units at a lower workflow recursion, but workflow topology is not automatically a metasystem function for the installation.
- Reviewed revision: `7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6`.
- Observation date: 2026-09-24.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

AgentOven has an explicit first-party managed runtime rather than relying only on external framework workers. `executor.go` defines the managed path as `prompt → Model Router → tool_calls → MCP Gateway → results → repeat` and implements that loop directly. For agentic behavior it additionally loads/persists a session, constructs a sliding context, calls the model with first-party tool definitions, executes returned calls, appends tool results and continues until a text response or the bounded turn limit is reached.

The boundary between this first-party path and external autonomy is explicit in the repository. `AgentRuntime` documents `agentoven` as the built-in Go executor and LangChain/LangGraph/CrewAI/custom as user-process runtimes. `InvokeAgent` rejects non-managed mode on the managed endpoint, proxies to a running process when one exists, and otherwise falls back to `Executor.Execute` for AgentOven-native managed agents. The standalone S1 claim therefore relies only on the built-in managed path, not on a framework-native worker's internal reasoning.

Managed agents can delegate through the virtual `agentoven_delegate` tool. The target managed Agent is resolved and recursively executed through the same first-party `Executor`; its response becomes a tool result in the caller's loop. Recipes add another composition layer: the workflow engine executes dependency-ordered Agent steps, can fan out/fan in, route or branch, retry failures, loop, map items, call sub-recipes and wait at human gates. These are meaningful orchestration facilities, but the frozen standard distribution does not establish a concrete inter-S1 disturbance that those generic topology primitives attenuate, so they do not establish S2 merely from plurality or sequencing.

The same function-first distinction applies to S3. The Recipe engine tracks the current run and mechanically schedules dependency-ready steps, branches from configured expressions, retries failures and exposes cancellation/human gates. A model-backed `StepRouter` can call an Agent and then evaluate predeclared branch expressions against its output, causing non-selected downstream branches to be skipped. That is local workflow routing over one Recipe, not a whole-installation current-management right over resources, priorities, commitments or accountability among AgentOven operations. Human gates likewise decide whether one configured workflow transition continues; they are not whole-system parent S3 by themselves.

AgentOven exposes `StepEvaluator`, traces and community output guardrails, but none establishes S3*. In the engine, `StepEvaluator` is executed through the same generic `executeAgentStep` path as an ordinary Agent step; independence, complementary evidence and corrective closure are not supplied merely by the step kind. Community guardrails are deterministic keyword/regex/heuristic checks over input/output and can block an already-produced response. Pro-only custom LLM/webhook judges and test-suite backends are not part of the OSS standard boundary.

Persistent sessions, summarization, RAG retrieval, provider failover and Agent/Recipe versioning support current operation and deployment but do not form an outside-and-then adaptation loop. Public OSS contracts mention environments/promotions/test runners, while the current community implementation identifies test suites as disabled/no-op and Pro injects promotion/environment capabilities. No standard OSS actor senses an external/future distinction, develops an organizational adaptation option and returns a selected change into current capability as S4.

Finally, Agent definitions, workspace/community guardrails, API/RBAC/auth hooks, human gates and configuration/version controls constrain operation without establishing identity/ultimate-policy closure. No runtime path was found that recognizes an identity-level issue, sends it to legitimate ultimate authority and returns that decision as the governing identity/policy of the installation. S5 is therefore absent rather than inferred from policy-like vocabulary.

Primary evidence:

- [`control-plane/internal/executor/executor.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/executor/executor.go) — explicit built-in managed model/tool loop, session/context handling, MCP execution and managed-agent delegation.
- [`control-plane/internal/api/handlers/handlers.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/api/handlers/handlers.go) — managed endpoint boundary, framework/process proxy path, default managed registration and fallback into the Go executor.
- [`control-plane/pkg/models/models.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/pkg/models/models.go) — explicit `managed`/`external` and `agentoven`/framework-native ownership split, agentic behavior, Recipe step kinds and configuration contracts.
- [`control-plane/internal/workflow/engine.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/workflow/engine.go) — Recipe execution, retries, fan-out/fan-in, router/evaluator/human-gate behavior, branching and run lifecycle.
- [`control-plane/internal/guardrails/guardrails.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/guardrails/guardrails.go) — OSS deterministic input/output guardrails and explicit no-op boundary for custom Pro judging.
- [`control-plane/pkg/server/server.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/pkg/server/server.go) — standard OSS composition of model router, MCP gateway, notification service and workflow engine.
- [`control-plane/pkg/contracts/contracts.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/pkg/contracts/contracts.go) — community no-op test-runner boundary and extension contracts that must not be mistaken for shipped Pro implementations.

## Operational model

For a built-in managed Agent, first-party code resolves its model/tools, builds the prompt/context and repeatedly invokes the Model Router. A model response containing tool calls is translated into MCP or managed-agent delegation actions. Their results are inserted into the ongoing message context and returned to the model on the next turn. A text response closes the run; agentic mode also persists the conversation/session state and can summarize older context when the budget is exceeded.

Recipe workflows sit above those operational loops. They feed outputs from dependency steps into subsequent agents, run dependency-ready steps concurrently and apply predeclared branching/retry/gate rules. This supplies reusable orchestration but does not transfer ownership of distinct VSM metasystem functions merely because it has a global run object or because a step is named evaluator/router.

## S1 — Operations

- State: A
- Function: perform a goal-directed managed Agent run through repeated semantic model decisions, MCP/delegation actions and returned observations until completion.
- Disturbance / variety regulated: user objective, dynamic model output, available MCP tools, tool success/failure, delegated-agent output, provider errors/failover, session history and context-budget pressure.
- Decisive decision or feedback right: choose the next substantive answer/tool/delegation action from current context and use returned observations to choose what follows.
- Decision owner: the model-driven AgentOven-native managed Agent loop implemented by first-party `Executor`.
- Supporting / enforcement mechanisms: Model Router, MCP Gateway, resolver, session store, sliding context/summarization, max-turn bound, trace recording, backup provider and deterministic guardrails.
- Closure path: user/session context → Model Router → model answer or tool calls → first-party MCP/delegation execution → results appended to messages → next model turn → final answer/bounded termination; session state is persisted for agentic agents.
- Boundary reachability: standard OSS server construction wires Model Router/MCP Gateway and handlers create `Executor`; default Agent mode is managed and AgentOven-native managed invocations without an external process call `Executor.Execute` directly.
- Why this is / is not agent-owned: deterministic machinery transports/enforces the loop, while the substantive next action is selected by the model over first-party-maintained context. External framework-native processes are not used to establish this state.
- Evidence: [`executor.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/executor/executor.go); [`handlers.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/api/handlers/handlers.go); [`models.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/pkg/models/models.go); [`server.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/pkg/server/server.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: a running framework-native process may also contain an autonomous agent, but that is a separate ownership path and its internal loop is excluded from the positive first-party claim.

## S2 — Coordination

- State: —
- Function: no material first-party path establishes regulation of a concrete disturbance between distinct AgentOven S1 units with feedback into their subsequent behavior.
- Disturbance / variety regulated: AgentOven can run several managed Agents, delegate among them, sequence dependencies, fan out/fan in and aggregate results, but the reviewed standard distribution does not bind these primitives to a specific cross-S1 conflict, contention, oscillation or contradictory commitment requiring coordination.
- Decisive decision or feedback right: not established as an S2-specific right.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: `agentoven_delegate`, Recipe dependency edges, fan-out/fan-in, map/sub-recipe steps, A2A calls and result propagation.
- Closure path: delegation/Recipe topology moves work and results among Agents. No disturbance-specific detection/attenuation/feedback loop between viable units is established by the generic primitives themselves.
- Boundary reachability: all cited orchestration primitives are shipped, but their organizational function is task decomposition/routing rather than proven S2.
- Why this is / is not agent-owned: plurality, messaging, delegation, sequencing and fan-in are insufficient under the Profile without a reconstructed inter-S1 disturbance.
- Evidence: [`executor.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/executor/executor.go); [`engine.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/workflow/engine.go); [`models.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/pkg/models/models.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a downstream Recipe may instantiate a real coordination problem, but that downstream organization requires its own evidence rather than inheriting S2 from generic topology.
- Distinct S1 units checked: multiple managed Agents invoked through `agentoven_delegate` or Recipe Agent steps.
- Inter-S1 disturbance checked: no first-party standard contract ties delegation/dependency execution to a concrete mutual interference condition.
- Why generic communication/routing/delegation is insufficient: results flow between steps/agents because the workflow declares edges; the flow does not itself attenuate instability or conflict between those agents.

### Absence scope

- Surfaces inspected: managed delegation, Recipe Agent/fan-out/fan-in/map/sub-recipe/router steps, A2A result propagation and workflow scheduler.
- Plausible first-party paths checked: delegation as S2; DAG dependencies as coordination; fan-in/out as coordination; router steps as S2; shared Recipe state as S2.
- Why no material first-party path remains: all paths are generic composition/routing primitives without the required disturbance-specific witness.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system present-management function is established for the AgentOven installation.
- Disturbance / variety regulated: Recipe execution machinery tracks run/step state, schedules dependency-ready work, retries failures, branches, pauses at human gates and permits run cancellation; these are current workflow controls rather than a whole-system management right over the installation's operations.
- Decisive decision or feedback right: no standard first-party actor is shown receiving a whole-installation view and deciding resource allocation, priorities, commitments, accountability, synergy or intervention among current AgentOven operations.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: Recipe run state, dependency scheduler, `StepRouter`, conditions, retries/timeouts, run cancel and human gates.
- Closure path: configured workflow state mechanically determines eligible steps; model-backed routers can influence one local branch and human gates can approve one transition. No whole-system current-management judgment/return loop closes at the installation recursion.
- Boundary reachability: workflow and gate paths are shipped OSS runtime surfaces; their negative classification is functional, not due to unreachability.
- Why this is / is not agent-owned: the scheduler enforces predeclared topology. A router Agent sees the input/dependency outputs of its step and influences downstream branch selection, but it does not receive or regulate the whole current operational organization. A gate approval similarly governs one transition, not the whole.
- Evidence: [`engine.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/workflow/engine.go); [`models.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/pkg/models/models.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: one specially designed Recipe could place a manager Agent over a downstream work organization; that instantiated Recipe would be a separate system-in-focus and is not implied by the generic `router` step.
- Whole-system current view checked: RecipeRun/step results cover one configured workflow run, while traces/dashboard/process state are observational; no standard manager binds them into installation-wide current-control discretion.
- Current-control scope checked: branching/retries/gates/cancel act on local workflow execution rather than whole-system allocation/accountability.

### Absence scope

- Surfaces inspected: Recipe scheduler/run lifecycle, router/condition steps, run cancellation, human gates, process manager and agent invocation paths.
- Plausible first-party paths checked: workflow engine as S3; model router step as agent manager; human gate as parent S3; process manager as S3; run cancellation as S3.
- Why no material first-party path remains: each path is deterministic workflow/process enforcement or local transition control rather than whole-current organizational management.

## S3* — Complementary audit

- State: —
- Function: no material first-party independent complementary audit loop over S1 operation is established in the OSS standard distribution.
- Disturbance / variety regulated: AgentOven can record traces, apply deterministic output guardrails and include an `evaluator` step in Recipes, but these do not supply the required independent audit organization and corrective return by themselves.
- Decisive decision or feedback right: no first-party auditor is shown independently challenging ordinary operational evidence and owning a corrective finding that returns into S1 behavior.
- Decision owner: not established for S3*.
- Supporting / enforcement mechanisms: traces, `StepEvaluator`, community input/output guardrails, workflow branches and Pro extension contracts excluded from the OSS ownership boundary.
- Closure path: `StepEvaluator` executes through the same generic Agent-step implementation; any correction/retry topology must be explicitly authored by the adopter. Community guardrails deterministically block text based on configured rules but do not form complementary autonomous audit judgment.
- Boundary reachability: community guardrails and Recipe evaluators are shipped. Pro custom webhook/LLM judges/test-suite execution are not credited because the public community implementation does not provide those operational paths.
- Why this is / is not agent-owned: a label `evaluator` does not create audit independence, and a deterministic content filter is enforcement rather than an autonomous complementary auditor.
- Evidence: [`engine.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/workflow/engine.go); [`guardrails.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/guardrails/guardrails.go); [`contracts.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/pkg/contracts/contracts.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a downstream Recipe can deliberately wire a distinct reviewer Agent and corrective loop; that composition requires its own evidence and cannot be inferred from `StepEvaluator` alone.

### Absence scope

- Surfaces inspected: Recipe evaluator/router/branch/retry paths, traces, community guardrails, test-runner contracts and community/Pro implementation boundary.
- Plausible first-party paths checked: evaluator step as S3*; guardrail output check as S3*; traceability as audit; test suite as S3*; human gate as independent review.
- Why no material first-party path remains: OSS provides observations/enforcement and generic composition primitives but no standard independent audit owner plus corrective closure.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party prospective adaptation loop is established in the OSS runtime.
- Disturbance / variety regulated: sessions, context summarization, RAG, provider failover, Agent versioning and Recipe deployment configuration improve present operation or support manual release management, but do not close outside/future intelligence into autonomous or parent-governed adaptation of AgentOven's organization/capability.
- Decisive decision or feedback right: no runtime owner is shown sensing external/future distinctions, developing adaptation options and returning a selected option into present capability as an S4 loop.
- Decision owner: not established for S4 within the OSS standard distribution.
- Supporting / enforcement mechanisms: session memory, summarization, RAG retrieval, backup-provider failover, version fields, deployment/promotion contracts and Pro extension points.
- Closure path: not established. Current-session memory feeds current S1; provider failover reacts to present failure; promotion/test interfaces require non-community implementations or explicit operator/deployment activity rather than an evidenced S4 loop.
- Boundary reachability: public OSS server identifies several Pro extension points, and community test-runner behavior is no-op/unavailable; absent Pro implementation is not treated as a first-party standard runtime path.
- Why this is / is not agent-owned: persistence, retrieval, fallback, versioning and roadmap/deployment machinery do not become S4 without an outside/future adaptation judgment and return path.
- Evidence: [`executor.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/executor/executor.go); [`models.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/pkg/models/models.go); [`server.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/pkg/server/server.go); [`contracts.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/pkg/contracts/contracts.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: Pro or downstream deployment machinery may create an adaptation topology, but it is outside the public OSS standard boundary assessed here.

### Absence scope

- Surfaces inspected: agentic session/context memory, summarization, RAG, provider failover, Agent versioning, environment/promotion/test-runner contracts and OSS/Pro server boundaries.
- Plausible first-party paths checked: memory as S4; RAG as S4; provider failover as adaptation; version bump/promotion as S4; test-suite feedback as S4.
- Why no material first-party path remains: identified paths either serve current operation or depend on excluded Pro/manual composition; no prospective organizational adaptation loop closes in public OSS runtime.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established at the AgentOven installation recursion.
- Disturbance / variety regulated: Agent configuration, guardrails, authentication/RBAC extension points, human gates and workspace policy can constrain operation, but none is shown resolving identity/ultimate-policy disputes for the organization.
- Decisive decision or feedback right: no path establishes identity/policy matter → legitimate ultimate authority → authoritative decision → return governing subsequent organization-wide operation.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: Agent definitions, community/workspace guardrails, gate approver constraints, auth/tier interfaces, version/configuration APIs and operator administration.
- Closure path: configured constraints enter lower-level operation directly; human gates approve/reject a concrete workflow transition. No separate identity/ultimate-policy feedback loop is established.
- Boundary reachability: policy/configuration and gate mechanisms are shipped, but their organizational function is lower-level action/workflow constraint rather than S5.
- Why this is / is not agent-owned: policy vocabulary, mandatory guardrails and human final say over one gate are insufficient under the Profile's S5 threshold.
- Evidence: [`guardrails.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/guardrails/guardrails.go); [`engine.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/internal/workflow/engine.go); [`models.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/pkg/models/models.go); [`server.go`](https://github.com/agentoven/agentoven/blob/7575127d3a11788a31c1f7d029d0d3eb5c6f2fc6/control-plane/pkg/server/server.go).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: an operator or enterprise parent may own policy in a wider deployed organization; generic administration does not establish standalone AgentOven S5.

### Absence scope

- Surfaces inspected: Agent/Recipe configuration, workspace/community guardrails and exceptions, human-gate approver constraints, auth/RBAC/tier extension boundary, version/deployment configuration.
- Plausible first-party paths checked: workspace mandatory guardrails as S5; human gate as S5; Agent config as constitution; kitchen/workspace policy as identity; enterprise auth/RBAC as parent S5.
- Why no material first-party path remains: each mechanism constrains lower-level access/action/workflow or is an extension surface, without identity/ultimate-policy closure.

## Distributed OSS parent arrangement

Public repository maintainers are not treated as the parent of a running AgentOven installation merely because they publish code. Human-gate approvers and local administrators have real lower-level decision rights in configured workflows, but those rights are not promoted into S3/S5 without the required whole-system or identity-level function.

## Self-hosted and non-human modes

The autonomous S1 path is first-party and does not require a human gate. An operator may configure guardrails or Recipe human gates around specific actions/transitions, but those optional parent interventions do not remove the built-in autonomous managed-agent loop and do not create a metasystem function by themselves.

## Recursion

`agentoven_delegate` recursively runs another managed Agent through the same Executor, and Recipes can compose multiple Agents and sub-recipes. This demonstrates operational recursion/decomposition. It does not automatically establish S2/S3: the function at each recursion still requires its own disturbance/current-control evidence.

## Variety and escalation

AgentOven attenuates operational variety through bounded turns, provider routing/failover, tool resolution, session/context budgets, workflow dependencies/retries/timeouts, deterministic guardrails and human gates. It amplifies operational capacity through MCP tools, RAG, delegated managed Agents and Recipe composition. Escalation can pause one Recipe transition for an authorized human approval and then return the decision into that workflow. This remains a local operational gate unless the evidence separately establishes a whole-system or identity-level function.

## Evidence gaps

- No standard-distribution S2-specific disturbance/feedback relation was established beyond generic delegation and workflow topology.
- No whole-installation current-management owner was established; Recipe routing and gates operate within configured workflow runs.
- `StepEvaluator` is a generic Agent step implementation, and OSS guardrails are deterministic; no independent S3* audit loop is established.
- Public Pro contracts for tests/promotions/environments do not supply public OSS runtime ownership and are not credited toward S3*/S4.
- No identity/ultimate-policy closure was established for S5.
