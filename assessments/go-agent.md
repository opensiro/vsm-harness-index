---
harness_id: go-agent
project_name: go-agent
repository: https://github.com/Protocol-Lattice/go-agent
review_ref: ddfec8630783306b4ecb5ffd37519595384f8d15
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# go-agent

## Review boundary

- System in focus: one instantiated first-party `go-agent` runtime at pinned revision `ddfec8630783306b4ecb5ffd37519595384f8d15`, centered on the root `Agent` model/tool/memory loop and including first-party ADK construction, sub-agent directories, shared-session/swarm primitives, deterministic graph workflows, skill loading/routing, guardrails and checkpoint/restore support.
- Purpose and identity: execute model-driven agent work in Go while allowing applications to compose providers, tools, memory, sub-agents, deterministic workflows and runtime policy mechanisms.
- Relevant environment: user/application requests, model-provider outputs, tool/API/file results, configured sub-agents, persistent/session memory, workspace source state and parent-supplied configuration.
- Standard-distribution boundary: the reusable first-party Go package/runtime and its shipped ADK/runtime mechanisms. External model endpoints, UTCP services/tools, vector/database stores and application-specific organizational roles remain environmental dependencies and do not donate VSM ownership.
- Credited operating / distribution surfaces: root `Agent.Generate`/tool-planning loop; first-party model/tool/sub-agent directories; ADK agent construction; reusable memory/shared-session and swarm support; deterministic graph/run-store workflow runtime; first-party skills loader/router and output/input guardrail machinery.
- Adjacent first-party surfaces excluded from ownership: `cmd/example/**` demonstration organizations as examples rather than standard instantiated owners; `arena/**` as an evaluation harness separate from ordinary operating control; repository CI/tests/website; downstream-created role prompts, team topologies, evaluators, skill-revision loops and business/application policy.
- First-party operating / deployment modes considered: direct `agent.New`; ADK-built coordinator agents; configured sub-agent-as-tool/delegation paths; shared-session/swarm composition; durable graph execution; skill-routed operation; guarded/checkpointed operation.
- Recursion level: one instantiated `go-agent` runtime/agent organization is the system-in-focus. Configured sub-agents count as separate operational actors only where an application actually instantiates them; framework support for multiple agents does not by itself establish higher-level VSM functions.
- Reviewed revision: `ddfec8630783306b4ecb5ffd37519595384f8d15`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

The root `Agent` is a substantive first-party operating runtime rather than a provider-only wrapper. It owns request preprocessing, memory retrieval, model planning, tool selection, tool execution, observation feedback and completion. In the normal UTCP tool path, the model decides whether another tool is needed, selects exact tool names and arguments, receives tool observations, and is called again until it declares completion or a deterministic step bound stops the loop. The runtime therefore closes a first-party autonomous S1 path even though external model/tool endpoints supply environmental capabilities.

The repository also ships substantial composition machinery: ADK providers for models, memory, tools and sub-agents; shared-session/swarm memory spaces; sub-agent directories; graph workflows with joins and durable run stores; skills; guardrails; model middleware and an evaluation arena. Those mechanisms do not automatically become higher VSM functions. The standard distribution does not define a concrete disturbance among distinct S1 units plus an attenuation relation for S2, a whole-system current-management actor/right for S3, an independent complementary operational audit with corrective return for S3*, a closed outside/future capability-adaptation loop for S4, or an identity/ultimate-policy authority loop for S5.

In particular, `src/swarm` is a participant/shared-session façade: it manages participant lookup plus join/leave/save/retrieve operations over shared memory spaces. Shared memory can support a downstream coordination design, but it does not specify what inter-S1 conflict is being regulated or how peer feedback must alter later S1 behavior. ADK sub-agent providers similarly aggregate available specialists without defining a cross-unit coordination function.

Graph workflows are explicitly deterministic control flow. They execute caller-defined nodes, edges, routes, joins, step ceilings and persisted queues. Durable run state/checkpoints establish execution continuity, not a discretionary whole-system S3 authority over present commitments/resources/priorities. Model middleware budgets and guardrails regulate a request/model path under configured limits; they likewise do not create an S3 actor.

`arena` deliberately separates task execution from evaluation and can emit score/feedback, but its evaluators inspect the ordinary task/output contract supplied to the benchmark. The package does not establish materially different access to operational reality nor route findings back into an ordinary running organization's corrective control. Output guardrails, including the optional LLM safety evaluator, are routine production validation rather than complementary S3* audit.

Skill System 2.0 exposes typed skills, optional `SkillEvaluator`, `SaveSkill`, loading/routing and human-editable `SKILL.md` persistence. These are capability-development primitives, but the repository does not ship the missing organizational bridge from external/future evidence or evaluator feedback to a decision that generates/selects a revised skill and returns it into operation. A downstream application must construct that adaptation organization. Workspace Intelligence similarly maintains current repository context for coding work; updating an index when files change is environment tracking for current operation, not prospective adaptation of the harness organization.

Finally, the runtime has parent-configured system prompts, safety policies, permissions and skill instructions, but no identity-specific ultimate-policy issue/authority/return loop. A generic coordinator prompt or configured guardrail is not S5.

Primary evidence:

- [`agent.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/agent.go) — first-party Agent runtime, request/memory/model/tool/sub-agent/guardrail surfaces.
- [`agent_tool_orchestration.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/agent_tool_orchestration.go) — model-owned multi-step tool planning, observation feedback and bounded completion loop.
- [`src/adk/kit.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/adk/kit.go) — constructor/DI surface for models, memory, tools and sub-agents.
- [`src/swarm/swarm.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/swarm/swarm.go), [`src/swarm/participant.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/swarm/participant.go) and [`src/memory/session/shared_session.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/memory/session/shared_session.go) — multi-agent/shared-memory support inspected for S2.
- [`src/adk/workflow/graph.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/adk/workflow/graph.go) — caller-defined deterministic graph, joins, durable run state and checkpointing inspected for S2/S3.
- [`arena/arena.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/arena/arena.go) and [`arena/evaluators.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/arena/evaluators.go) — separate evaluation surface inspected for S3*.
- [`skills_v2.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/skills_v2.go), [`skill_runtime.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/skill_runtime.go) and [`docs/skill-system-2.md`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/docs/skill-system-2.md) — skill evaluation/persistence/loading primitives inspected for S4.
- [`docs/workspace-intelligence.md`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/docs/workspace-intelligence.md) — live workspace indexing/context surface inspected for S4.
- [`safety_policies.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/safety_policies.go) — deterministic/LLM output-safety validation inspected for S3*/S5.
- [`README.md`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/README.md) — public package boundary, local skills, ADK, graph workflows and durable execution semantics.

## S1 — Operations

- State: A
- Function: execute requests through a model-driven loop that can select and invoke first-party-registered tools/sub-agents, observe results and continue until substantive completion.
- Disturbance / variety regulated: ambiguous user objectives, changing tool observations, external API/file results, failed/invalid plans, memory/context variation and tasks that require multiple environment interactions before completion.
- Decisive decision or feedback right: decide whether to call another tool, which exact tool and arguments to use, and when the request is complete; configured direct sub-agent paths provide additional first-party operating choices.
- Decision owner: the model-driven `Agent` planner within the first-party runtime.
- Supporting / enforcement mechanisms: memory retrieval, tool catalog, UTCP execution, sub-agent directory, CodeMode restrictions, input/output guardrails, duplicate-call handling, mutation-completion checks and configured step limits.
- Closure path: request/context enter `Agent` → model planner selects a tool/action or completion → first-party runtime executes the selected registered tool → observation returns into the planner context → model selects the next action or final answer → result is stored/returned.
- Boundary reachability: `Agent.Generate` and its normal tool-orchestration path are shipped core package behavior; ADK builds the same first-party Agent runtime rather than delegating the loop to an external harness.
- Why this is / is not agent-owned: deterministic runtime checks constrain the allowed action space and termination envelope, but they do not determine which substantive tool/arguments or follow-up action satisfy the request. Removing the model planner removes those decisions.
- Evidence: [`agent.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/agent.go); [`agent_tool_orchestration.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/agent_tool_orchestration.go); [`src/adk/kit.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/adk/kit.go).
- Basis: explicit + structural
- Confidence: high
- Caveats: direct deterministic tool commands and caller-defined graph nodes also exist. `A` rests on the standard reachable model-owned operating path, not on every execution mode being autonomous.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 disturbance attenuation loop is established for the declared standard runtime boundary.
- Disturbance / variety regulated: not established.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: sub-agent directories, agent-as-tool composition, shared-session spaces, swarm participant join/leave, graph fan-out/join and ordinary delegation were inspected as supporting mechanisms only.
- Closure path: no first-party disturbance-specific S2 closure established.
- Why this is / is not agent-owned: the framework can instantiate and connect multiple autonomous agents, but the caller defines their roles/topology. Shared memory transports information; graph joins collect outputs; sub-agent calls delegate work. None of these standard mechanisms specifies a concrete cross-S1 oscillation/conflict/resource-interference problem and a coordination relation whose feedback changes later S1 behavior.
- Evidence: [`src/swarm/swarm.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/swarm/swarm.go); [`src/swarm/participant.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/swarm/participant.go); [`src/memory/session/shared_session.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/memory/session/shared_session.go); [`src/adk/kit.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/adk/kit.go); [`src/adk/workflow/graph.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/adk/workflow/graph.go).
- Basis: explicit + structural
- Confidence: high
- Caveats: a downstream organization built with go-agent may establish strong S2. That separately instantiated organization requires its own evidence and does not donate S2 to the reusable framework assessment.

### Absence scope

- Surfaces inspected: ADK sub-agent providers/directories; root sub-agent support; `src/swarm`; SharedSession spaces; graph fan-out/join/routing; documented agent-as-tool/hierarchical composition mechanisms.
- Plausible first-party paths checked: delegation, shared memory, participant spaces, graph joins/barriers, deterministic routes and multi-agent composition.
- Why no material first-party path remains: all inspected paths provide plurality, communication, sequencing, aggregation or delegation but leave the actual inter-S1 disturbance and attenuation relation to the adopter/application.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-management function is established at the declared runtime boundary.
- Disturbance / variety regulated: not established at whole-system scope.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: deterministic graph queues/checkpoints, model middleware rate/token/timeout policies, per-request tool-loop limits, guardrails and caller-configured coordinator/sub-agent relationships were inspected.
- Closure path: no whole-system current-view → discretionary current-control decision → changed commitments/resources/priorities loop is packaged.
- Why this is / is not agent-owned: graph execution follows caller-defined edges/routes and persists one run's queue/state; model middleware enforces configured limits around calls/workflows; a default prompt calling an agent a “primary coordinator” does not supply a current whole-system view or management authority.
- Evidence: [`src/adk/workflow/graph.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/adk/workflow/graph.go); [`README.md`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/README.md); [`src/adk/kit.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/adk/kit.go).
- Basis: explicit + structural
- Confidence: high
- Caveats: applications can construct a manager agent or current-control service from these primitives. Such downstream construction is a different organizational boundary.

### Absence scope

- Surfaces inspected: ADK coordinator construction; graph workflow/run-store state; joins/routes; model rate/token/timeout middleware; root step limits; checkpoint/restore; sub-agent composition.
- Plausible first-party paths checked: named coordinator role, durable workflow state, graph scheduling, aggregate-looking token budgets, retries/timeouts and hierarchical examples.
- Why no material first-party path remains: none combines a standard whole-organization current view with a function-specific right to revise present commitments/resource allocation/priorities across S1 units; existing controls are local/configured execution mechanisms.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary operational audit path is established for ordinary go-agent operation.
- Disturbance / variety regulated: not established.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: Arena evaluators, output guardrails, LLM safety evaluator, tests and tracing/tool events were inspected.
- Closure path: no independent complementary-access findings → corrective current-operation return path is packaged.
- Why this is / is not agent-owned: Arena deliberately separates benchmark execution from evaluation but evaluates the supplied task/output contract and records score/feedback; it is not wired into ordinary runtime control and does not obtain an independent view of operational reality. Output guardrails inspect the ordinary proposed response in-path before return, which is routine QA rather than complementary audit.
- Evidence: [`arena/arena.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/arena/arena.go); [`arena/evaluators.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/arena/evaluators.go); [`safety_policies.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/safety_policies.go).
- Basis: explicit + structural
- Confidence: high
- Caveats: a downstream deployment can wire Arena or another evaluator to independent evidence and corrective action, but that additional organization is not present in the standard runtime.

### Absence scope

- Surfaces inspected: Arena runner/evaluator split and feedback records; exact/contains/score evaluators; LLM output safety policy; output guardrails; test suites; tool-event/observability mechanisms.
- Plausible first-party paths checked: separate evaluation harness, secondary-model safety judge, routine output validation and runtime event evidence.
- Why no material first-party path remains: evaluated material follows the ordinary task/output path or is benchmark data, and no standard path combines complementary access/independence with findings returned into corrective operational control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party prospective organizational/capability adaptation loop is established at the declared boundary.
- Disturbance / variety regulated: not established as an outside/future adaptation function.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persistent memory, local skills, Skill System 2.0 evaluator hooks/persistence, workspace indexing/watching, provider/tool discovery and checkpointing were inspected.
- Closure path: no first-party external/future distinction → generated/selected adaptation option → approved revision → returned future capability loop is packaged.
- Why this is / is not agent-owned: Skill System 2.0 can evaluate a skill, persist a caller-supplied `SkillDefinition` with `SaveSkill`, load skills and route them into future prompts, but the framework does not connect evaluation/external evidence to an actor that generates or selects a revised skill. The adopter must build that missing adaptation decision/feedback organization. Workspace Intelligence tracks current repository changes to keep context fresh; it does not adapt the harness's own future repertoire.
- Evidence: [`skills_v2.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/skills_v2.go); [`skill_runtime.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/skill_runtime.go); [`docs/skill-system-2.md`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/docs/skill-system-2.md); [`docs/workspace-intelligence.md`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/docs/workspace-intelligence.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: local skill persistence is closer to an S4 construction surface than generic memory, but disconnected capability storage/evaluation APIs are not enough for `C` under the function-specific closure requirement.

### Absence scope

- Surfaces inspected: skill loading/reloading; Skill System 2.0 registry/evaluator/SaveSkill; skill routing; workspace index/watcher/context builder; persistent memory; examples that demonstrate autonomous operation; Arena evaluation.
- Plausible first-party paths checked: evaluator-driven skill improvement, skill persistence, live skill reload, repository change detection, memory accumulation and workspace semantic indexing.
- Why no material first-party path remains: the repository supplies parts on both sides of a possible adaptation loop but not the first-party organizational bridge that turns external/future evidence into a selected capability revision and closes it back into future operation.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure is established for the declared runtime boundary.
- Disturbance / variety regulated: not established at identity/ultimate-policy scope.
- Decisive decision or feedback right: not established.
- Decision owner: none established.
- Supporting / enforcement mechanisms: configurable system prompt/default coordinator prompt, safety policies, input/output guardrails, tool permissions, skills and caller configuration were inspected.
- Closure path: no identity/ultimate-policy issue → legitimate ultimate authority → returned identity/policy decision loop is packaged.
- Why this is / is not agent-owned: prompts, guardrails and permissions constrain ordinary operation, but the framework does not distinguish a durable organizational identity/ultimate-policy source or an authority process that resolves such issues and returns the result into operation.
- Evidence: [`agent.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/agent.go); [`src/adk/kit.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/src/adk/kit.go); [`safety_policies.go`](https://github.com/Protocol-Lattice/go-agent/blob/ddfec8630783306b4ecb5ffd37519595384f8d15/safety_policies.go).
- Basis: explicit + structural
- Confidence: high
- Caveats: an application may use `SystemPrompt` as one input to a separately designed identity/governance regime; generic prompt configuration is not itself S5.

### Absence scope

- Surfaces inspected: default/custom system prompt; ADK prompt configuration; safety policies and LLM safety evaluator; input/output guardrails; tool safety/permissions; local skills.
- Plausible first-party paths checked: configured coordinator identity language, policy enforcement, safety approval and persistent instructions.
- Why no material first-party path remains: these paths define lower-level instructions/constraints but do not establish an identity-level issue, legitimate ultimate authority and explicit return-to-operation closure.

## Summary

go-agent closes autonomous S1 through its first-party model/tool observation loop. Its sub-agent/swarm/shared-memory and deterministic workflow facilities are reusable composition mechanisms rather than a closed S2 or S3 organization; Arena/guardrails do not provide complementary S3* audit; skills/workspace primitives do not close prospective S4 adaptation; and prompts/policies do not establish S5 identity authority. The standalone vector is therefore `A / — / — / — / — / —`.
