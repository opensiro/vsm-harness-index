---
harness_id: voltagent
project_name: VoltAgent
repository: https://github.com/VoltAgent/voltagent
review_ref: 44b4c8e4998ce56095b2f0e4eaf1a988f5e6d0de
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# VoltAgent

## Review boundary

- System in focus: one first-party VoltAgent application runtime at pinned revision `44b4c8e4998ce56095b2f0e4eaf1a988f5e6d0de`, including the `@voltagent/core` Agent loop, optional supervisor/sub-agent path, workflow engine, memory/retrieval support, runtime guardrails, evaluation hooks and first-party server/runtime surfaces.
- Purpose and identity: provide an application framework in which model-driven agents execute tool-mediated tasks and application authors can compose specialist teams, durable workflows, memory, validation and evaluation around those agents.
- Relevant environment: user/application requests, tool and MCP results, retrievers/knowledge sources, model-provider responses, workflow resume events, persisted conversation state, and application-authored constraints.
- Standard-distribution boundary: first-party code and documentation in `VoltAgent/voltagent` at the pinned revision. External model providers, MCP servers, application business logic, user-defined policies and separately operated VoltOps services are external unless a first-party OSS runtime path itself closes the claimed organizational function.
- Credited operating / distribution surfaces: the first-party `Agent` model/tool loop; `SubAgentManager` and its automatically supplied `delegate_task` supervisor path; workflow execution including persistence/suspend/resume; working/conversation memory; first-party input/output guardrail execution; and OSS evaluation/scorer integration only to the extent that these surfaces participate in the running agent organization.
- Adjacent first-party surfaces excluded from ownership: contributor/CI/release machinery for developing VoltAgent itself; examples and docs where no corresponding first-party runtime exists; telemetry, eval dashboards and trace scoring when they only observe or measure operation; application-authored prompts, approval semantics and guardrail policies that do not transfer the relevant organizational decision right into VoltAgent.
- First-party operating / deployment modes considered: standalone tool-using `Agent`; an application-configured supervisor with two or more `subAgents`; nested supervisor/sub-agent teams where the same first-party path recurs; authored workflows with suspend/resume; agents using configured memory, retrieval, guardrails and evals.
- Recursion level: one VoltAgent application-level agent team. Individual sub-agents are candidate S1 units; a sub-agent that is itself configured as a supervisor can form a lower recursion, but functions are credited at the reviewed team boundary only when their decision/feedback path closes there.
- Reviewed revision: `44b4c8e4998ce56095b2f0e4eaf1a988f5e6d0de`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

VoltAgent is a TypeScript agent framework whose core `Agent` runs a model/tool loop and can be composed with tools, MCP, retrieval, memory, guardrails and workflows. The same Agent type can be configured with `subAgents`. In that mode `SubAgentManager` adds a `delegate_task` capability and generates a supervisor contract listing available specialists.

The supervisor path is stronger than generic delegation alone. The supervisor LLM decides which specialist or specialists are needed, may contact several in parallel, receives their results, forwards missing context or questions, and is explicitly instructed to act as the sole intermediary because sub-agents are unaware of one another. This supplies a real coordination path among multiple operational units, but it is an optional application-composed capability rather than a default team organization.

Other rich framework features remain mechanisms unless they establish a distinct organizational function. Suspend/resume persists workflow state and can carry human approval data, but the application defines what approval means and who invokes resume. Guardrails intercept the ordinary input/output path and can allow, modify or block content, while live evals primarily attach scores to traces. Working memory stores facts/preferences/goals across interactions. None of those paths, at this revision, independently establishes whole-team current control, complementary organizational audit, prospective adaptation, or ultimate policy authority.

Primary evidence:

- [`packages/core/src/agent/agent.ts`](https://github.com/VoltAgent/voltagent/blob/44b4c8e4998ce56095b2f0e4eaf1a988f5e6d0de/packages/core/src/agent/agent.ts) — first-party Agent execution loop, tool use, step limits and integration with memory/guardrails.
- [`packages/core/src/agent/subagent/index.ts`](https://github.com/VoltAgent/voltagent/blob/44b4c8e4998ce56095b2f0e4eaf1a988f5e6d0de/packages/core/src/agent/subagent/index.ts) — `SubAgentManager`, parent-child registration, supervisor system message, delegation/handoff execution and sole-intermediary coordination contract.
- [`website/docs/agents/subagents.md`](https://github.com/VoltAgent/voltagent/blob/44b4c8e4998ce56095b2f0e4eaf1a988f5e6d0de/website/docs/agents/subagents.md) — runtime flow in which the supervisor analyzes the request, chooses which sub-agent(s) to use, can target several simultaneously, receives their results and synthesizes the outcome.
- [`website/docs/workflows/suspend-resume.md`](https://github.com/VoltAgent/voltagent/blob/44b4c8e4998ce56095b2f0e4eaf1a988f5e6d0de/website/docs/workflows/suspend-resume.md) — persisted suspend/resume, typed resume data, approval examples, restart and replay semantics.
- [`website/docs/guardrails/overview.md`](https://github.com/VoltAgent/voltagent/blob/44b4c8e4998ce56095b2f0e4eaf1a988f5e6d0de/website/docs/guardrails/overview.md) — inline input/output interception with allow/modify/block actions.
- [`website/evaluation-docs/live-evaluations.md`](https://github.com/VoltAgent/voltagent/blob/44b4c8e4998ce56095b2f0e4eaf1a988f5e6d0de/website/evaluation-docs/live-evaluations.md) — production scorer results recorded as trace spans/telemetry rather than an automatically corrective organizational loop.
- [`website/docs/agents/memory/working-memory.md`](https://github.com/VoltAgent/voltagent/blob/44b4c8e4998ce56095b2f0e4eaf1a988f5e6d0de/website/docs/agents/memory/working-memory.md) — persistent compact context for facts, preferences and goals across turns.

## Operational model

A normal VoltAgent `Agent` is the primary S1: the model chooses substantive tool/reasoning actions inside application-authored bounds and iterates toward the requested result. Configuring `subAgents` adds separate autonomous specialist S1 units plus a model-driven supervisor. Those specialists execute independently and do not directly know one another; the supervisor becomes the intermediary through which relevant context and results move.

The supervisor therefore qualifies as composable S2, not because it is named “supervisor,” but because the first-party path closes a concrete coordination relation among otherwise separate S1 units. The same evidence does not establish S3: the supervisor is request-scoped delegation/synthesis and lacks a first-party persistent whole-team commitment/resource view with authority to reallocate current organizational capacity, reprioritize a standing portfolio, or intervene on behalf of the whole.

## S1 — Operations

- State: A
- Function: autonomously execute a bounded user/application task through iterative model reasoning, tool use and returned environment observations.
- Disturbance / variety regulated: task ambiguity, tool results, retrieved context, changing application/environment state and intermediate model observations encountered while completing the request.
- Decisive decision or feedback right: choose the next substantive model/tool action, use returned observations to continue or stop, and produce the operational result within configured limits.
- Decision owner: the running model-driven VoltAgent `Agent`.
- Supporting / enforcement mechanisms: tool/MCP adapters, provider calls, `maxSteps`/stop conditions, memory, retrieval, operation context, hooks and guardrails.
- Closure path: request enters `Agent` → model chooses an action/tool or response → tool/environment result returns into subsequent model steps → the agent continues until a final result, stop condition, error or configured boundary is reached.
- Boundary reachability: the Agent loop and its tool/context machinery are shipped first-party `@voltagent/core` runtime surfaces at the pinned revision; external model inference supplies decisions but does not replace the first-party execution contract.
- Why this is / is not agent-owned: application configuration bounds the action space, but the substantive sequence of reasoning/tool decisions is model-driven at runtime rather than predetermined by the framework author.
- Evidence: `packages/core/src/agent/agent.ts`, `website/docs/agents/overview.md`, and first-party examples/tests of tool-using agents.
- Basis: explicit and structural.
- Confidence: high.
- Caveats: autonomous ownership is credited to the running Agent organization, not to external model-provider infrastructure or application business logic.

## S2 — Coordination

- State: C
- Function: mediate information and work interaction among multiple autonomous specialist sub-agents that otherwise lack direct mutual awareness or shared conversation context.
- Disturbance / variety regulated: independently operating specialists can require one another's outputs or missing context, duplicate unnecessary work, or fail to combine complementary results because each sub-agent is intentionally unaware of the others.
- Decisive decision or feedback right: decide which specialist or specialists are necessary, contact several in parallel when appropriate, provide the context each needs, forward questions/confirmations and reintegrate their returned results into the parent interaction.
- Decision owner: the model-driven supervisor `Agent` once an application has composed the team through `subAgents`.
- Supporting / enforcement mechanisms: `SubAgentManager`, parent-child registry relationships, generated `<specialized_agents>` supervisor context, automatically supplied `delegate_task`, per-handoff conversation/context propagation, persisted sub-agent metadata and event forwarding.
- Closure path: application composes a supervisor plus sub-agents → user request reaches supervisor → supervisor selects one or more necessary specialists → `delegate_task` executes those S1 units and returns their outputs/questions → supervisor forwards needed context and synthesizes/continues until the team result is produced.
- Boundary reachability: `SubAgentManager`, `delegate_task`, handoff execution and the supervisor coordination contract are shipped first-party runtime paths at the pinned revision; the constructor only has to instantiate/configure the team.
- Why this is / is not agent-owned: once composed, the supervisor LLM owns the concrete contact/context-forwarding choices, but VoltAgent does not instantiate a standard team or S2 actor by default. The framework therefore exposes a constructor path rather than autonomous out-of-box S2.
- Evidence: `packages/core/src/agent/subagent/index.ts` and `website/docs/agents/subagents.md`.
- Basis: explicit and structural.
- Confidence: high.
- Caveats: ordinary one-way delegation would not be enough. The positive mapping rests on the explicit sole-intermediary relation and supervisor-owned selective/parallel information exchange among multiple independent S1 units.
- Distinct S1 units: two or more configured VoltAgent sub-agents, each executing its delegated task through its own Agent loop and tools/context.
- Inter-S1 disturbance: specialists are unaware of one another and may need outputs, answers or context held elsewhere in the team to produce a coherent combined result.
- Attenuating coordination relation: the supervisor is the sole intermediary, selectively contacts necessary agents, can contact several simultaneously, and forwards the context/questions/results required for coherent joint work.
- Feedback into subsequent S1 behaviour: returned specialist questions/results enter the supervisor's next decision; the supervisor can answer a specialist from retained history, forward user confirmation, contact another specialist or issue further delegated work with updated context.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the first-party contract is explicitly responsible for maintaining information relations among otherwise mutually unaware operational units, not merely transferring control to one worker or executing an authored sequence.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-team inside-and-now control function is established at the reviewed application/team boundary.
- Disturbance / variety regulated: the framework can encounter current task failures, workflow interruptions and sub-agent errors, but the reviewed paths do not regulate a standing organization's aggregate commitments, capacity, priorities or resource allocation on behalf of the whole.
- Decisive decision or feedback right: none established for a qualifying S3 current-control function.
- Decision owner: none established.
- Supporting / enforcement mechanisms: request-scoped supervisor delegation, workflow sequencing, retries/step limits, error propagation, suspend/resume, cancellation, restart/replay and application hooks.
- Closure path: not applicable; these mechanisms can control execution of a task/workflow, but no first-party path closes a persistent whole-system current view into commitment/resource reallocation or organization-wide intervention.
- Why this is / is not agent-owned: the supervisor decides which specialist helps answer the current request, but delegation/synthesis is operational orchestration rather than authority over a standing whole-system current-control domain.
- Evidence: `website/docs/agents/subagents.md`, `website/docs/workflows/suspend-resume.md`, and `packages/core/src/agent/agent.ts`.
- Basis: explicit plus absence review.
- Confidence: high.
- Caveats: an application can build an S3-like controller with VoltAgent primitives; that downstream organization is a separate system-in-focus and is not credited to the framework itself.

### Absence scope

- Surfaces inspected: supervisor/sub-agent runtime, Agent loop/state, workflow engine, suspend/resume/restart/cancellation, hooks, server/runtime APIs and current-control-adjacent configuration.
- Plausible first-party paths checked: supervisor delegation/error handling, workflow status/state, approval waits, restart/time-travel, step limits and lifecycle hooks.
- Why no material first-party path remains: every inspected candidate either regulates one execution trajectory or exposes an application composition primitive; none supplies a persistent whole-team current view plus a substantive decision right over shared commitments, capacity or organization-wide intervention.

## S3* — Complementary audit

- State: —
- Function: no materially independent first-party complementary audit/challenge function is established for operational claims at the reviewed boundary.
- Disturbance / variety regulated: malformed, unsafe or low-quality inputs/outputs can be detected by guardrails and scorers, but those mechanisms do not by themselves create an organizationally independent audit channel with protected access and corrective authority.
- Decisive decision or feedback right: none established for a qualifying S3* function.
- Decision owner: none established.
- Supporting / enforcement mechanisms: input/output guardrails, validators, middleware/hooks, live/offline eval scorers, telemetry traces and ordinary application-authored review workflows.
- Closure path: guardrails run inline with the producing operation and can allow/modify/block according to configured policy; live evals record scores in telemetry. No separate first-party auditor independently challenges the producer claim and returns findings through a protected corrective path.
- Why this is / is not agent-owned: a guardrail handler may block output and an evaluator may score it, but independence and complementary organizational access are not established; application-defined validators are ordinary execution controls unless composed into a separate audit organization.
- Evidence: `website/docs/guardrails/overview.md`, `packages/core/src/workflow/internal/guardrails.ts`, `website/evaluation-docs/live-evaluations.md`, and `website/docs/evals.md`.
- Basis: explicit plus absence review.
- Confidence: high.
- Caveats: downstream applications can compose independent reviewer agents or corrective evaluator loops, but generic support for doing so does not establish first-party S3* ownership.

### Absence scope

- Surfaces inspected: agent and workflow guardrails, validators, middleware/hooks, eval/scorer packages, live evaluation documentation, observability/feedback surfaces and sub-agent hooks.
- Plausible first-party paths checked: input/output block/modify handlers, stream aborts, workflow guardrails, live production scorers, offline experiments and handoff-completion hooks.
- Why no material first-party path remains: guardrails are in the normal execution pipeline and evals primarily measure/record results; no reviewed path establishes a sufficiently separate audit actor, complementary access boundary and coupled corrective-return authority.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct prospective environment-facing intelligence/adaptation function is established at the reviewed organizational boundary.
- Disturbance / variety regulated: conversation history, remembered facts, retrieved documents and user feedback can change current agent context, but the reviewed framework does not itself transform external/future distinctions into organization-level adaptation choices coupled back to current control.
- Decisive decision or feedback right: none established for a qualifying S4 function.
- Decision owner: none established.
- Supporting / enforcement mechanisms: conversation memory, working memory, semantic/vector retrieval, knowledge bases, feedback capture, eval datasets/experiments and application-authored scheduled/workflow activity.
- Closure path: these mechanisms persist or retrieve context and measure behavior; no first-party path was established from prospective environmental sensing through adaptation-option formation into changed current organizational capability or S3 decisions.
- Why this is / is not agent-owned: a model can read/update working memory and applications can evaluate agents, but memory/learning-like storage and measurement are not S4 without a future/external adaptation responsibility and return path.
- Evidence: `website/docs/agents/memory/working-memory.md`, `packages/core/src/memory/manager/memory-manager.ts`, `website/docs/evals.md`, and `website/observability/feedback.md`.
- Basis: explicit plus absence review.
- Confidence: high.
- Caveats: an application can use retrieved environmental information or eval results to implement strategic adaptation; that application-specific loop is not present as a first-party VoltAgent organizational function at this pin.

### Absence scope

- Surfaces inspected: working/conversation memory, retrieval/knowledge-base integration, feedback capture, offline/live evaluations, workflows and scheduling-adjacent runtime support.
- Plausible first-party paths checked: persistent facts/preferences/goals, semantic retrieval, user ratings/comments, dataset experiments, live production scoring and context updates.
- Why no material first-party path remains: the inspected paths store, retrieve or score information for current operation/engineering; none owns a prospective outside-and-then distinction and closes it into an organizational adaptation decision.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate policy/identity function is established for the VoltAgent application organization.
- Disturbance / variety regulated: applications need prompts, permissions, guardrail policies, approval rules, model/tool choices and team topology, but those identity/policy choices remain authored outside the running framework organization.
- Decisive decision or feedback right: none established for a qualifying S5 identity/ultimate-policy function.
- Decision owner: the application developer/operator or other external parent, not a first-party VoltAgent S5 organ.
- Supporting / enforcement mechanisms: Agent instructions, `supervisorConfig`, custom system messages, guardrail definitions, workflow resume schemas/approval steps, provider/tool configuration and application permissions.
- Closure path: external application configuration establishes these constraints before or around operation; VoltAgent enforces/executes them but does not itself decide the organization's ultimate identity or reconcile policy at the highest recursion.
- Why this is / is not agent-owned: prompts and policy checks constrain behavior, and HITL can return an external decision, but neither mechanism transfers ultimate policy authority into a first-party S5 process.
- Evidence: `website/docs/agents/subagents.md`, `website/docs/workflows/suspend-resume.md`, `website/docs/guardrails/overview.md`, and Agent configuration surfaces in `packages/core/src/agent/agent.ts`.
- Basis: explicit plus absence review.
- Confidence: high.
- Caveats: suspend/resume can be used for human approvals, but generic human interaction is not automatically parent-governed S5; the application must supply the identity/policy issue and authority relationship.

### Absence scope

- Surfaces inspected: Agent/supervisor instructions and configuration, guardrail policy, workflow HITL/suspend-resume, provider/tool permissions, application/server configuration and human-interaction examples.
- Plausible first-party paths checked: supervisor system-message customization, manual approval examples, validation/block rules, runtime permissions and operator-provided configuration.
- Why no material first-party path remains: all plausible policy/identity candidates are authored or decided by the embedding application/operator and then enforced by VoltAgent; no first-party mechanism owns ultimate organizational identity, highest-order policy reconciliation or a parent-governed S5 protocol.

## Recursion, variety, escalation

VoltAgent permits recursive supervisor/sub-agent composition because a sub-agent is itself an Agent and may own further sub-agents. That structural recursion does not automatically import higher-level VSM functions. At the assessed team boundary the first-party positive metasystemic finding is the optional S2 intermediary; errors, approvals, guardrails, memory and evals remain execution/composition support unless a downstream system assigns them stronger organizational decision rights.
