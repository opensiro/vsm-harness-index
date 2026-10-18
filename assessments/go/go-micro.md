---
harness_id: go-micro
project_name: Go Micro
repository: https://github.com/micro/go-micro
review_ref: 792b18c3010715e2f12621f0120bf058be225482
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: A(P)
autonomy_s5: —
---

# Go Micro

## Review boundary

- System in focus: the shipped Go Micro v6 agent/service/flow harness at pinned revision `792b18c3010715e2f12621f0120bf058be225482`, including first-party `agent` execution, service-backed tools and registry discovery, built-in plan/delegate/request-input capabilities, `micro chat`, flow execution/verification, and the AI service-design/generation path used by `micro run --prompt` / `micro chat`.
- Purpose and identity: provide a Go-native runtime in which autonomous agents operate services as tools, persist context, delegate work, execute durable flows, interoperate through MCP/A2A, and — in supported development/runtime modes — add missing service capability to the running system.
- Relevant environment: user requests and desired capabilities; registered services/agents; service endpoints and external APIs; model/provider responses; tool/RPC/A2A results; persistent stores; flow results and grader feedback; compile/runtime failures; operator generation/approval decisions.
- Standard-distribution boundary: the installable Go library/CLI and shipped runtime modes at the frozen revision. External model providers, A2A peers, MCP consumers, x402 facilitators, backing registries/stores/brokers and user-defined service code are environment/substrate. A developer-supplied `flow.Grader` may complete a constructor path but is not imported as a first-party actor.
- Credited operating / distribution surfaces: `agent/` model/tool loop and built-ins; `cmd/micro/chat` direct-service agent session; `cmd/micro/cli/generate` service design/generation/compile-fix path; `cmd/micro/run --prompt`; `flow/` runtime including `Verify`, `LLMGrader`, `Analyze` and prompt-optimization primitives; registry/tool discovery and supported MCP/A2A/service integration insofar as Go Micro itself owns the surrounding closure.
- Adjacent first-party surfaces excluded from ownership: `.github/loop`, `cmd/micro/loop`, repository `CONTINUOUS_IMPROVEMENT.md`, autonomous repository-maintenance workflows, CI/harness tests, release/security/coherence/planner workflows, contributor instructions, benchmarks/examples used only as tests or demonstrations, website/blog editorial workflows and maintainer governance. `micro loop` is shipped and is relevant corroboration of a construction pattern, but the generated repository-development organization has a different purpose/recursion from the product runtime assessed here and is not borrowed to close S3*/S4/S5.
- First-party operating / deployment modes considered: `NewAgent` service-backed agents; `micro chat` direct-service fallback and registered-agent routing; plan/delegate agent operation; flow steps including agent/LLM/verification paths; autonomous missing-capability generation inside `micro chat`; parent-approved initial system generation through `micro run --prompt` / CLI generation.
- Recursion level: one Go Micro agent/service application or interactive `micro chat` system as the system-in-focus. Autonomous agent runs that directly transform the service/tool environment are S1 units. Generated or registered services are operational resources/tools unless they themselves host distinct agent actors. Repository self-maintenance is a separate higher/different-purpose system and is excluded.
- Reviewed revision: `792b18c3010715e2f12621f0120bf058be225482`.
- Stable GitHub repository id: `29217054`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Go Micro combines a mature service framework with a first-party agent harness. `NewAgent` exposes a model-driven service whose endpoints and custom functions become tools. The agent has durable conversation memory and built-in `plan`, `delegate`, and `request_input` capabilities. The tool handler layers plan enforcement, step/loop limits, spend limits, approval, checkpointing, retries/timeouts and tracing around the actual service/delegation call. The model receives tool results and continues the decision loop until it settles an answer.

Multi-agent interaction is primarily delegation and service discovery. `delegate` sends a self-contained task to a registered agent that owns relevant services, an A2A endpoint, or a focused ephemeral sub-agent. The parent can maintain a store-backed ordered plan and mark steps pending/in-progress/done. These capabilities establish distributed execution but do not by themselves establish S2 or S3: the built-in path is task decomposition/handoff rather than a demonstrated inter-S1 conflict-regulation loop or whole-system current-control function.

Flows provide deterministic/event-driven composition around agents and services. `flow.Verify` is a function-specific grade-and-retry constructor: it runs a body, passes the result to a `Grader`, and on rejection threads grader feedback into the next attempt. Go Micro includes `LLMGrader`, but it reuses the flow's configured model and sees the latest output; therefore the default path does not establish sufficiently independent complementary audit ownership. The `Grader` contract plus first-party feedback/retry closure does, however, intentionally expose the S3*-specific decision path so a deployment can compose an independent auditor, yielding constructor rather than autonomous credit.

The strongest metasystem feature in the product boundary is live capability generation. `micro chat` explicitly instructs its autonomous model to call `micro_generate_service` when no existing service can satisfy a user request. The first-party generator scans the existing service set, asks a model to design an extension, writes/updates service definitions and handlers, iteratively compile-fixes them, builds and starts newly created services, waits for registry registration, refreshes the tool set, and returns those endpoints to the same ongoing chat loop. Separately, `micro run --prompt` / CLI generation first presents the LLM-designed service architecture and asks the operator `Generate? [Y/n]`; approval drives the same generation path. These are distinct autonomous and parent-governed S4 modes over the same adaptation function.

Go Micro also ships `flow.Analyze` and `LLMOptimizer`: persisted runs and verification feedback can be ranked into improvement candidates and an LLM can propose a revised prompt, but applying the proposal remains caller-gated. This corroborates the framework's adaptation orientation; the published S4 state below does not depend on that incomplete apply seam because service generation already closes a stronger first-party adaptation loop.

## Operational model

In ordinary agent operation, the model receives the current conversation, plan/memory context and discovered service/custom tools. It chooses a tool or built-in capability, Go Micro executes/gates the call, and the resulting observation is returned to the model for another decision. Registered agents can receive delegated subtasks through RPC/A2A; otherwise a focused ephemeral agent may execute the delegated work and return only its result.

In `micro chat` direct-service mode, the agent continuously refreshes the set of available services/tools. When a request requires a missing capability, the model itself can choose `micro_generate_service`. The generator models the existing system plus the new requirement, creates/updates code, compile-fixes it, starts new services, observes registry availability and refreshes tools. The new capability is then available to the same agent for the still-active user objective.

In the parent-governed generation mode, a user supplies a desired system description, Go Micro asks the model to produce a service architecture, displays that proposal, and waits for `Generate? [Y/n]`. The user's decision controls whether the capability adaptation is materialized; an affirmative answer returns through code generation/compilation/startup into subsequent agent/service operation.

## S1 — Operations

- State: A
- Function: autonomously transform user/task state through a model → tool/service/delegation → observation loop until an operational result is produced.
- Disturbance / variety regulated: heterogeneous user goals, changing service/tool availability, tool/RPC/A2A results, persistent conversation state, provider responses, tool failures and intermediate observations requiring context-sensitive next actions.
- Decisive decision or feedback right: choose the next service/custom/built-in tool, decide whether to plan or delegate, consume returned observations, continue the loop or settle the answer.
- Decision owner: the active Go Micro LLM agent in `NewAgent` or `micro chat` direct-service mode.
- Supporting / enforcement mechanisms: model adapters, service registry/tool discovery, built-in plan/delegate/request-input tools, memory/store, tool wrappers, step/loop/spend limits, approvals, checkpointing, retry/timeout logic, RPC/A2A/MCP integration.
- Closure path: user/assigned task + current context → agent selects action/tool/delegation → Go Micro executes/gates it → tool/service/sub-agent result returns into model context → agent selects another action or final result.
- Boundary reachability: `NewAgent` and `micro chat` are shipped, documented first-party runtime modes; the positive S1 loop is implemented in `agent/` and CLI runtime code rather than inferred from examples or repository dogfood.
- Why this is / is not agent-owned: removing the model-driven agent while retaining registry, memory, tool execution and guardrails leaves no contextual actor choosing the next operational action. Deterministic wrappers constrain and transport the model's decisions rather than replacing them.
- Evidence: [`README.md`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/README.md), [`agent/builtin.go`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/agent/builtin.go), [`cmd/micro/chat/chat.go`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/cmd/micro/chat/chat.go).
- Basis: structural
- Confidence: high
- Caveats: external model inference and remote A2A peers are substrate/environment. The positive state is established independently by the first-party agent loop around those dependencies.

## S2 — Coordination

- State: —
- Function: no material first-party S2-specific loop was established that regulates a concrete interference/conflict/oscillation among distinct Go Micro S1 agent units at the declared product-runtime recursion.
- Disturbance / variety regulated: candidate paths inspected included multiple registered agents, RPC/A2A handoffs, service discovery/load balancing, durable flows, duplicate delegate/retry protection and shared registry/store infrastructure.
- Decisive decision or feedback right: no qualifying S2-specific decision right is supplied. Delegation selects another actor for a subtask; service discovery/load balancing routes calls; idempotency/retry controls duplicate side effects; flow edges order work.
- Decision owner: none established for S2 in the reviewed standard product-runtime boundary.
- Supporting / enforcement mechanisms: registry, client load balancing, broker/store, plan/delegate tools, A2A/MCP transport, flow sequencing, retry/idempotency guards and isolated ephemeral sub-agent context.
- Closure path: no first-party path was found that detects a specific interaction disturbance among two distinct S1 agents, selects an attenuation response for that disturbance, and feeds the coordination result back into subsequent local S1 behaviour.
- Why this is / is not agent-owned: multi-agent reachability, routing and delegation are present, but the Methodology explicitly requires more than communication/handoff. The reviewed product runtime does not supply an S2-specific autonomous or constructor path tied to a concrete inter-S1 oscillation/conflict witness.
- Evidence: [`README.md`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/README.md), [`agent/builtin.go`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/agent/builtin.go), [`gateway/a2a/a2a.go`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/gateway/a2a/a2a.go).
- Basis: structural
- Confidence: high
- Caveats: applications can construct richer cross-agent coordination using Go Micro primitives; generic framework expressiveness is not enough for `S2=C`.

### Absence scope

- Surfaces inspected: built-in plan/delegate paths, registered-agent routing, A2A gateway/client, service registry/load balancing, flow sequencing/durability, retry/idempotency and multi-agent documentation.
- Plausible first-party paths checked: delegated registered agents, ephemeral sub-agents, cross-agent RPC/A2A, service discovery, flow ordering, duplicate delegated side-effect protection and shared infrastructure.
- Why no material first-party path remains: every inspected path either transports/selects work, isolates a delegated subtask, sequences a workflow or prevents replay/duplicate side effects. None ties a specific distinct-S1 interaction disturbance to an S2-specific adjustment loop that returns to alter multiple agents' later local behaviour.

## S3 — Inside-and-now control

- State: —
- Function: no distinct first-party whole-system current-control function was established beyond local agent planning/delegation and deterministic runtime enforcement.
- Disturbance / variety regulated: candidate current-control paths inspected included store-backed plans, delegation, flow execution state, registry discovery, tool approvals, spend/step/loop limits and runtime stop/resume mechanisms.
- Decisive decision or feedback right: the ordinary agent may revise its own task plan and delegate subtasks, but no separate product-runtime path was found with a whole-system current view plus authority to bargain/regulate shared resources, commitments or priorities on behalf of multiple operational units.
- Decision owner: none established for S3 at the declared recursion.
- Supporting / enforcement mechanisms: `plan` memory, delegate routing, flow state/checkpoints, registry/client machinery, tool/step/loop/spend limits, approvals and cancellation/timeouts.
- Closure path: no S3-specific whole-system feedback/intervention loop was established. Local plan updates return to the same agent's task execution; deterministic limits enforce preselected constraints.
- Why this is / is not agent-owned: a parent agent that decomposes one user request and delegates one subtask is not automatically S3. The reviewed evidence does not show a standard mode where an agent receives a whole-system operational view and owns ongoing resource/commitment intervention across independent S1s.
- Evidence: [`agent/builtin.go`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/agent/builtin.go), [`README.md`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/README.md), [`flow/`](https://github.com/micro/go-micro/tree/792b18c3010715e2f12621f0120bf058be225482/flow).
- Basis: structural
- Confidence: high
- Caveats: `.github/loop` has project-level planning/current-work behavior, but it belongs to the excluded repository-development organization and is not borrowed into the product-runtime S3 mapping.

### Absence scope

- Surfaces inspected: agent plan/delegate implementation, flow execution/state, registry/service routing, tool approval/guardrails, checkpoint/recovery and the adjacent autonomous repository loop.
- Plausible first-party paths checked: agent plan updates, parent-to-child delegation, flow scheduler/state, service load balancing, runtime budget/limit enforcement and repository planner/builder dogfood.
- Why no material first-party path remains: product-runtime paths remain local task planning, routing or deterministic enforcement rather than whole-system discretionary current control. The only stronger project-level management path is outside the declared product system-in-focus.

## S3* — Complementary audit

- State: C
- Function: challenge a flow-step result through a distinct verification judgment and return rejection feedback into another operational attempt before the flow proceeds with the bounded result.
- Disturbance / variety regulated: plausible but deficient step outputs that ordinary body execution would otherwise return without a separate grade-and-correction pass.
- Decisive decision or feedback right: the `Grader` decides pass/fail and supplies corrective feedback; `Verify` threads rejection feedback into the next body attempt and records the final verification outcome.
- Decision owner: Go Micro does not ship a sufficiently independent default autonomous auditor for the general case. `LLMGrader` reuses the flow model and only sees the latest result. The application must compose a grader with independence appropriate to the audited claim; Go Micro supplies the S3*-specific verification/feedback closure.
- Supporting / enforcement mechanisms: bounded `Verify` attempt loop, feedback-field injection, optional backoff, verification metadata, flow checkpoint/result state and optional `LLMGrader` helper.
- Closure path: body produces candidate result → composed grader audits it → rejection/feedback enters the next body input → body retries → accepted or bounded-failure result becomes the flow state.
- Claim being audited: whether the current flow-step output satisfies the deployment-defined rubric/ground truth before it is accepted as the step's result.
- Ordinary reporting path: the body step returns its `State` as normal flow output.
- Complementary access path: the first-party `Grader` seam invokes a separately composed grading actor after body completion; the deployment can give that actor external ground truth, raw artifacts or a distinct model/service, and Go Micro closes its verdict back into retry.
- Independence boundary: independence is not guaranteed by the built-in `LLMGrader`; it is intentionally left to the developer-supplied `Grader`. This is why the state is `C`, not `A`.
- Who acts on findings: `flow.Verify` deterministically reinjects grader feedback into the next body attempt; the operational body/agent then produces the corrected candidate.
- Boundary reachability: `flow.Verify`, the `Grader` contract and feedback/retry closure are shipped public first-party flow primitives at the reviewed revision, not CI-only tests. A deployment only needs to supply the independent grading actor/ground-truth access.
- Why this is / is not agent-owned: the function-specific audit path and return loop are first-party, but the decisive sufficiently independent audit actor is not supplied in a standard autonomous mode. General custom-code extensibility is not the basis; the credit is for the dedicated `Verify`/`Grader` primitive whose semantics are verification judgment plus corrective return.
- Evidence: [`flow/verify.go`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/flow/verify.go), [`flow/verify_test.go`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/flow/verify_test.go).
- Basis: explicit
- Confidence: medium-high
- Caveats: same-model `LLMGrader` alone is not treated as sufficient complementary independence. A deployment that wires only that helper may not operationally realize S3* even though the first-party constructor exists.

## S4 — Outside-and-then intelligence

- State: A(P)
- Function: detect that current operational capability cannot satisfy an external requirement, develop a service-level adaptation, materialize it, and return the new capability into subsequent agent operation.
- Disturbance / variety regulated: new user needs not covered by existing registered services/tools; requests to extend or modify an existing system; design/code/compile failures encountered while materializing the capability.
- Decisive decision or feedback right: Base mode — the `micro chat` agent decides that no existing service can handle the request and chooses `micro_generate_service`; the generation models choose the service architecture/handler changes. Parent mode — the user reviews the LLM-designed system proposal and decides at `Generate? [Y/n]` whether the adaptation should be materialized.
- Decision owner: Base mode — the autonomous chat/generation model path. Parent mode — the human operator owns the decisive accept/reject adaptation judgment, while the generator autonomously develops and implements the approved option.
- Supporting / enforcement mechanisms: registry/tool discovery, `generate.Design`, existing-service scan, deterministic service-structure generation, LLM handler generation, bounded compile-fix loop, process startup, registry wait and tool refresh.
- Closure path: external capability request + current service inventory → missing-capability distinction → model designs service adaptation → autonomous choice or parent approval triggers generation → code is written/compile-fixed/built/started → registry/tool set refreshes → subsequent agent turns can use the new service.
- External distinction: the user asks for a capability absent from the current registered service/tool environment, or asks to extend/modify the existing system.
- Future / prospective distinction: Go Micro models a desired future system/service capability relative to the current inventory rather than only selecting among existing tools; `Design` explicitly receives existing services and constructs the complete extended target design.
- Adaptation option generated: one or more new/modified Go Micro services with schema/endpoints, generated handler/business logic and an updated managing agent/tool surface.
- Path back into current capability / S3: generated services are compiled and started, allowed to register, `micro chat` refreshes discovered tools, and the new endpoints become immediately usable by the same operational agent; in initial generation mode the approved system becomes the subsequent running service/agent environment.
- Boundary reachability: both `micro chat` autonomous missing-capability generation and `micro run --prompt` / CLI user-approved generation are shipped documented CLI modes. The positive mapping does not depend on repository CI or `.github/loop` dogfood.
- Why this is / is not agent-owned: in base mode removing the model's missing-capability judgment/service-design choices leaves only a generator with no contextual adaptation decision. In parent mode the human decides whether the proposed adaptation is admitted, and that decision is returned through the same generator into executable capability.
- Evidence: [`cmd/micro/chat/chat.go`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/cmd/micro/chat/chat.go), [`cmd/micro/cli/generate/generate.go`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/cmd/micro/cli/generate/generate.go), [`cmd/micro/run/run.go`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/cmd/micro/run/run.go), [`README.md`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/README.md), [`flow/analyze.go`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/flow/analyze.go).
- Basis: explicit
- Confidence: high
- Caveats: the adaptation path is developer/runtime oriented rather than production hot-patching of an arbitrary deployed service; the credited mode is nevertheless first-party and explicitly returns generated service capability into the supported running `micro chat` environment. `flow.Analyze`/`LLMOptimizer` alone would be only a partial adaptation constructor because applying its prompt proposal is caller-owned.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | `micro chat` autonomous model/generation path | User requests a capability no existing service can handle | Agent selects `micro_generate_service` → design/generate/compile/start → registry/tool refresh → same agent can use the new capability | `cmd/micro/chat/chat.go`, `cmd/micro/cli/generate/generate.go` |
| Parent (`P`) | Human operator | User starts prompt-driven system generation/extension and receives the LLM-designed proposal | Operator answers `Generate? [Y/n]`; affirmative decision drives generation/startup and changes the subsequent service/agent capability set | `cmd/micro/run/run.go`, `cmd/micro/cli/new/new.go`, `README.md` |

## S5 — Policy and identity

- State: —
- Function: no product-runtime identity/ultimate-policy decision loop was established at the declared recursion.
- Disturbance / variety regulated: candidate paths inspected included agent system prompts, auth/rules, tool approvals, spend/step/loop limits, `request_input`, generated-service confirmation and repository North Star/maintainer restrictions.
- Decisive decision or feedback right: none of the product-runtime mechanisms escalates a genuine identity/ultimate-policy issue to a legitimate ultimate authority and returns that decision to govern subsequent operation at this recursion.
- Decision owner: none established for S5 in the assessed product runtime.
- Supporting / enforcement mechanisms: auth rules/JWT wrappers, guardrails, tool approvals, static prompts/configuration, human input pauses, spend budgets and generation confirmation.
- Closure path: ordinary task/action approvals and configuration changes can alter execution, but no identity/ultimate-policy issue → legitimate authority → authoritative decision → returned policy loop was found.
- Why this is / is not agent-owned: policy text, permission checks and human approvals bound ordinary operations; they do not by themselves own system identity or ultimate policy. Repository `NORTH_STAR` and off-limits maintainer decisions belong to the excluded repository-development organization.
- Evidence: [`agent/builtin.go`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/agent/builtin.go), [`auth/`](https://github.com/micro/go-micro/tree/792b18c3010715e2f12621f0120bf058be225482/auth), [`internal/docs/CONTINUOUS_IMPROVEMENT.md`](https://github.com/micro/go-micro/blob/792b18c3010715e2f12621f0120bf058be225482/internal/docs/CONTINUOUS_IMPROVEMENT.md).
- Basis: structural
- Confidence: high
- Caveats: the shipped `micro loop` can scaffold repository governance/policy surfaces and Go Micro dogfoods them, but that is a separate repository-development recursion and is not imported into product-runtime S5.

### Absence scope

- Surfaces inspected: agent prompts/built-ins/guardrails, auth/rules, tool approvals and request-input, generation approval, flow/runtime controls, `micro loop`/North Star and maintainer guardrails as adjacent evidence.
- Plausible first-party paths checked: human tool approval, prompt/config policy, auth decisions, generation confirmation, repository North Star, off-limits change classes and human stop/revert authority.
- Why no material first-party path remains: product-runtime controls are ordinary permissions/current-operation/adaptation decisions rather than identity/ultimate-policy closure. The only explicit project-identity governance belongs to the separately scoped repository-development system.

## Recursion

Go Micro contains several possible recursions. An individual `NewAgent` can be treated as an S1 unit inside a wider application, while registered agents can delegate to one another. The assessment does not infer higher-level viability merely because one agent spawns/delegates another. The repository's autonomous maintenance loop is also a genuine organizational system, but it has the distinct purpose of developing Go Micro itself; mixing it with a deployed Go Micro application would collapse two recursions/purposes and violate the boundary-provenance rule.

## Variety and escalation

Operational variety includes provider/model responses, discovered service/tool sets, tool failures, persistent memory, delegation targets and external API state. Go Micro attenuates this through scoped tools, retries/timeouts, step/loop/spend limits, checkpoints and deterministic flows. Missing-capability variety is unusually amplified rather than merely rejected: the S4 path can add a service and therefore expand the tool repertoire during an active chat. Human input/approval can be requested for ordinary operations or generation, but those paths are classified by the function they actually close rather than promoted to S5.

## Evidence gaps

- No positive S2 witness was found that meets the current concrete-interference requirement among distinct S1 agents; future versions could add such a path without changing the meaning of current routing/delegation evidence.
- No product-runtime S3 whole-system controller was found. If a future team/fleet mode gives an agent live whole-application commitments/resources and intervention rights, that would require reassessment.
- `flow.Verify` is published as `C` because the built-in default does not prove complementary independence; deployments can supply stronger independent graders through the dedicated contract.
- `.github/loop` / `micro loop` is intentionally excluded from the product-runtime vector despite being shipped/dogfooded; a separate assessment of the repository-development organization could legitimately produce different S3*/S4/S5 mappings.
