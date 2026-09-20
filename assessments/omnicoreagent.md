---
harness_id: omnicoreagent
project_name: OmniCoreAgent
repository: https://github.com/omnirexflora-labs/omnicoreagent
review_ref: 60da57a6dacd3f7796fffd9d198c0a7420aa6aad
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-20
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OmniCoreAgent

## Review boundary

- System in focus: one OmniCoreAgent application-facing agent harness using the first-party model/reasoning loop, local/MCP tools, structured observations, memory/context/workspace, dynamic subagents, optional governed execution, background tasks, workflow composition, telemetry and OmniServe lifecycle.
- Purpose and identity: provide a production-oriented runtime boundary that turns a model into an application agent capable of tool use, persistent sessions, bounded delegation, durable background work and service deployment.
- Relevant environment: user/application requests, local and MCP tools, model providers, workspace data, background schedules/task stores, serving clients and application-authored policies.
- Standard-distribution boundary: first-party `omnicoreagent` runtime and shipped production/background/workflow/serving components. External model providers, MCP servers, application business logic and application-authored policies remain external unless a first-party OmniCoreAgent loop itself owns a claimed VSM decision right.
- Credited operating / distribution surfaces: `OmniCoreAgent.run`, runtime execution loop, observation/tool pipeline, dynamic `SubagentFactory`, background manager/supervisor/task store, workflow agents, governance enforcement, memory/context/workspace and OmniServe lifecycle/API.
- Adjacent first-party surfaces excluded from ownership: contributor/CI/release surfaces, engineering design/specification documents as development artifacts rather than running actors, tests, cookbook examples when used only as demonstrations, documentation publishing/search infrastructure and repository governance.
- First-party operating / deployment modes considered: ordinary single-agent runtime, dynamic subagent mode, background/scheduled execution, workflow composition, optional governance policy enforcement and OmniServe deployment.
- Recursion level: one configured OmniCoreAgent application harness. The lead agent is the principal S1 operational unit; dynamic subagents are bounded delegated workers inside that operational task unless a higher multi-S1 recursion is explicitly evidenced.
- Reviewed revision: `60da57a6dacd3f7796fffd9d198c0a7420aa6aad`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

OmniCoreAgent explicitly defines the harness boundary around the model: prompt contract, reasoning loop, tool resolution/execution, structured observations, memory, context control, workspace files, guardrails, events and optional subagents. `OmniCoreAgent.run` starts telemetry, applies input guardrails, builds the runtime prompt, invokes the first-party agent execution loop and returns the resulting response plus run/session correlation. Tool outputs are returned as structured observations for another model decision.

Dynamic subagents are created by a first-party factory. They inherit bounded configuration/tools, receive a focused task, execute an OmniCoreAgent loop, write output to workspace paths and return a result to the lead agent. Parallel subagents are gathered and summarized, but the reviewed standard path does not establish a separate S2-specific interference relation or project-wide S3 controller merely because delegation and parallelism exist.

The production harness also includes durable background execution. Task/run/attempt/lease/retry/cancellation state is stored separately from conversation memory; supervisors claim runs, renew/interpret leases, retry according to authored policy and recover stale work. Governance can allow/deny/ask for approvals, apply capability policy, enforce budgets and require sandbox routing. Those mechanisms are strong current-operation constraints, but their decisive choices are authored policy/deterministic evaluation or external approval rather than an autonomous whole-system S3 actor in the reviewed standard distribution.

Primary evidence:

- [`README.md`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/README.md) — explicit harness boundary, runtime features, observation pipeline, loop detection, subagents, background tasks, workflows and OmniServe.
- [`src/omnicoreagent/core/runtime/omnicore_agent.py`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/src/omnicoreagent/core/runtime/omnicore_agent.py) — first-party run/session/telemetry path and invocation of the model/tool agent loop.
- [`src/omnicoreagent/core/subagents.py`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/src/omnicoreagent/core/subagents.py) — focused worker construction, parallel subagent execution and return to the lead agent.
- [`engineering/architecture/background-agents.md`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/engineering/architecture/background-agents.md) — durable task/run/attempt/lease/retry/cancellation architecture.
- [`src/omnicoreagent/background/supervisor.py`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/src/omnicoreagent/background/supervisor.py) and [`recovery.py`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/src/omnicoreagent/background/recovery.py) — retry/lease/recovery enforcement.
- [`src/omnicoreagent/governance/enforcement.py`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/src/omnicoreagent/governance/enforcement.py) — fail-closed policy evaluation, budgets, ASK approvals and sandbox constraints.

## Operational model

The principal operational loop is autonomous: a model receives the prompt/history, chooses substantive tool or response actions, observes structured tool results and continues until it produces the task outcome or a runtime stop condition fires. Memory/context/workspace/guardrail systems shape the loop but do not replace that model-owned operational discretion.

The repository exposes many production-control mechanisms. Loop signatures can terminate repeated behavior; background supervisors implement leases, retries and cancellation; governance evaluates pre-authored capability/budget policy; OmniServe manages requests and lifecycle. These mechanisms can stop, route or retry execution, but Methodology 0.3.5 separates enforcement authority from organizational decision ownership. No first-party autonomous actor was established that has the required whole-system current view and discretionary S3 control across the assessed harness.

## S1 — Operations

- State: A
- Function: autonomously reason over an application request, choose tool/delegation/final-response actions, consume observations and produce the requested operational result.
- Disturbance / variety regulated: open-ended user/application tasks, tool/API outcomes, errors, large/noisy outputs, context pressure, discovered information and changing intermediate task state.
- Decisive decision or feedback right: choose the next substantive model/tool/delegation action and when to return the final task response within the configured harness contract.
- Decision owner: the model-driven OmniCoreAgent execution loop.
- Supporting / enforcement mechanisms: prompt builder, model transport, local/MCP tool registry, parallel tool runner, structured observation formatting, memory, context management, workspace/offloading, guardrails, loop signatures, telemetry and optional subagent factory.
- Closure path: request/history → model decision → tool call(s) or delegated worker → structured observation/result → updated model context → subsequent model decision/final response.
- Boundary reachability: `OmniCoreAgent.run` is the package's primary public entry point and directly builds/invokes the first-party runtime loop; it does not depend on a separate application implementing the operational feedback loop.
- Why this is / is not agent-owned: deterministic runtime code executes and constrains actions, but the running model chooses the substantive next action based on observations and owns the task-level decision loop.
- Evidence: [`README.md`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/README.md), [`OmniCoreAgent.run`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/src/omnicoreagent/core/runtime/omnicore_agent.py), [`subagents.py`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/src/omnicoreagent/core/subagents.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: dynamic subagents are credited as a mechanism available to S1; their mere existence does not imply S2 or S3 at a higher recursion.

## S2 — Coordination

- State: —
- Function: no material S2-specific inter-S1 conflict/oscillation attenuation path is established at the declared recursion.
- Disturbance / variety regulated: not established as an S2 disturbance.
- Decisive decision or feedback right: not established as S2.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: parallel tool batches, dynamic subagents, shared workspace output, sequential/parallel/router workflows and gathered results provide decomposition, routing and aggregation.
- Closure path: subagent results return to the lead agent or workflow output, but this is delegation/composition rather than a demonstrated attenuation loop for interference between distinct S1 units.
- Why this is / is not agent-owned: generic parallelism, routing and shared storage do not satisfy the S2 constructor threshold without a specific inter-S1 disturbance and coordination relation directed at it.
- Evidence: [`README.md`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/README.md), [`subagents.py`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/src/omnicoreagent/core/subagents.py), [`cookbook/workflows/README.mdx`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/cookbook/workflows/README.mdx).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: applications can compose multiple agents and workflow routers, but generic composition is intentionally insufficient for `S2=C` under Methodology 0.3.5.

### Absence scope

- Surfaces inspected: dynamic subagents, parallel execution, shared workspace output, workflow composition, background execution, telemetry/events and serving state.
- Plausible first-party paths checked: subagent result gathering, parallel agents, sequential/router workflows, workspace sharing and background task scheduling.
- Why no material first-party path remains: the inspected paths provide delegation/routing/aggregation/sequence but do not evidence a concrete interference or oscillation among distinct S1 units plus a first-party relation specifically attenuating it and feeding the result back into those units.

## S3 — Inside-and-now control

- State: —
- Function: no autonomous whole-system inside-and-now control function is established at the declared harness recursion.
- Disturbance / variety regulated: runtime failures, repeated loops, expired leases, retry conditions, cancellation requests, budget/policy violations and service lifecycle conditions are handled, but not through an evidenced autonomous S3 owner.
- Decisive decision or feedback right: no first-party autonomous actor is established as owning project/application-wide current allocation, priority, commitment or intervention decisions.
- Decision owner: authored runtime/policy configuration and deterministic machinery for the inspected control surfaces; external callers/approval resolvers may own some configured choices.
- Supporting / enforcement mechanisms: signature loop detection, max steps, background task state, leases/retries/recovery/cancellation, governance allow/deny/ask evaluation, budget accounting, sandbox requirements, request lifecycle and rate limits.
- Closure path: these mechanisms can terminate/retry/block/serve configured operation, but they enforce previously selected rules or external commands rather than closing an autonomous whole-system S3 discretion loop.
- Why this is / is not agent-owned: the lead model owns task-level S1 choices; the production control mechanisms around it are deterministic or externally authored and do not make the lead agent a whole-system regulator merely because it can delegate.
- Evidence: [`README.md`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/README.md), [`background-agents architecture`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/engineering/architecture/background-agents.md), [`GovernanceEngine`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/src/omnicoreagent/governance/enforcement.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: a developer can build a supervisory organization from the available primitives. General framework expressiveness is not a positive `C` state without an S3-specific autonomous decision path.

### Absence scope

- Surfaces inspected: lead runtime, subagent factory, workflow components, loop detection, background manager/supervisor/recovery/task store, governance/budget/approval enforcement, OmniServe lifecycle and telemetry.
- Plausible first-party paths checked: dynamic delegation, router workflows, background retry/recovery, cancellation, lease stealing, governance ASK/deny, budgets, serving timeouts/readiness and telemetry APIs.
- Why no material first-party path remains: all identified current-control surfaces either remain local S1 choices, deterministic enforcement of authored rules, or externally initiated controls; none establishes an autonomous actor with whole-system current view and discretionary S3 feedback closure.

## S3* — Complementary audit

- State: —
- Function: no materially independent complementary audit function with corrective return is established in the standard harness boundary.
- Disturbance / variety regulated: prompt injection, runtime errors and policy violations are screened/observed, but those checks are ordinary production safety/control mechanisms rather than an independent S3* challenge of S1 reporting.
- Decisive decision or feedback right: not established as an independent audit judgment.
- Decision owner: guardrail/policy/runtime machinery or application-authored policy, not a separate audit actor.
- Supporting / enforcement mechanisms: guardrails, telemetry/traces, structured events, governance evaluation, loop detection, logs and background run history.
- Closure path: safety checks can block ordinary execution and telemetry can expose evidence, but no distinct reviewer/challenger obtains complementary evidence, independently judges an S1 claim and returns findings into whole-system corrective control.
- Why this is / is not agent-owned: observability and guardrails can be valuable verification mechanisms while remaining inside the ordinary production/control path; Methodology 0.3.5 requires complementary access, independence and findings-to-control closure for S3*.
- Evidence: [`README.md`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/README.md), [`governance/enforcement.py`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/src/omnicoreagent/governance/enforcement.py), [`engineering/architecture/telemetry.md`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/engineering/architecture/telemetry.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: an application can consume traces and create an external reviewer, but that downstream composition is not credited to OmniCoreAgent itself.

### Absence scope

- Surfaces inspected: input/output guardrails, observation guardrails, telemetry/traces, governance decisions, background history/events, tests and workflow/subagent paths.
- Plausible first-party paths checked: policy evaluator, guardrail violations, telemetry exporters/trace retrieval, run history, loop signatures and subagent result validation.
- Why no material first-party path remains: none supplies the required independent complementary audit actor/path plus a returned corrective judgment into subsequent whole-system operation; they are enforcement, observability or ordinary result handling.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct prospective environment-facing adaptation loop is established at the assessed harness recursion.
- Disturbance / variety regulated: not established at S4 scope.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: memory, context summarization, workspace persistence, skills, retrieval/MCP tools and background schedules can retain or retrieve information but do not by themselves select future capability adaptation.
- Closure path: stored/retrieved information can affect later task reasoning, but no first-party loop senses future/environment distinctions, generates adaptation options and returns a selected capability/program change into current operation.
- Why this is / is not agent-owned: remembering earlier messages, summarizing context, retrieving external information or loading a skill is not equivalent to S4 adaptation ownership.
- Evidence: [`README.md`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/README.md), [`OmniCoreAgent runtime`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/src/omnicoreagent/core/runtime/omnicore_agent.py).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: application-specific agents can research the environment during S1 work; that task behavior does not establish a separate harness-level S4 function.

### Absence scope

- Surfaces inspected: memory/router, context summarization/truncation, workspace, skills/tools, external MCP access, background scheduling, workflow/subagent composition and telemetry.
- Plausible first-party paths checked: persistent memory, summarization, skill loading, workspace artifacts, web/MCP-style tool access and scheduled tasks.
- Why no material first-party path remains: these surfaces provide persistence and current-task information access, not a first-party prospective adaptation-option selection loop returned into future harness capability or organizational program.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy function is established at the assessed harness recursion.
- Disturbance / variety regulated: application-authored capability, budget, approval and sandbox constraints regulate execution but are not evidenced as identity-level policy disputes.
- Decisive decision or feedback right: not established as S5.
- Decision owner: application/deployer-authored policy and optional approval resolver for the inspected governance path.
- Supporting / enforcement mechanisms: `PolicyEnvelope`, allow/deny/ASK decisions, approval resolution, policy hashes, budget constraints, sandbox requirements, prompt contract and serving configuration.
- Closure path: governance decisions can permit/block/ask for individual execution capabilities, but no identity/ultimate-policy issue is routed to an S5 authority and returned as governing identity policy for the system.
- Why this is / is not agent-owned: a prompt contract, permission/capability policy, budget or human approval is not automatically S5; the policy objects regulate execution rights rather than the organization's identity/ultimate purpose at this recursion.
- Evidence: [`governance/enforcement.py`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/src/omnicoreagent/governance/enforcement.py), [`README.md`](https://github.com/omnirexflora-labs/omnicoreagent/blob/60da57a6dacd3f7796fffd9d198c0a7420aa6aad/README.md).
- Basis: structural negative finding.
- Confidence: high.
- Caveats: the governance subsystem deliberately exposes application control; this assessment does not reinterpret operational authorization as S5 without identity-level evidence.

### Absence scope

- Surfaces inspected: system instruction/prompt contract, governance policy, capability decisions, approval resolver, budgets, sandbox requirements, serving configuration and application integration boundary.
- Plausible first-party paths checked: policy allow/deny/ASK, human approval, policy provenance/hash, budget authority, sandbox requirements and system prompts.
- Why no material first-party path remains: these are execution-policy and authorization mechanisms; no first-party identity/ultimate-policy issue, legitimate S5 authority and return-to-operation closure is established.

## Distributed OSS parent arrangement

Repository maintainers and contributors govern development of OmniCoreAgent, but that is an adjacent OSS development recursion. It is not imported into a running application harness. The optional approval resolver can put a parent human/application into an execution authorization loop, but no qualifying S3/S4/S5 function was established for that approval path, so no `P` modifier is published.

## Self-hosted and non-human modes

OmniCoreAgent is designed for application/self-hosted use. Operators can configure prompts, tools, policies, budgets, serving boundaries and background execution. These controls remain authored configuration or external operational control unless a function-specific parent mode is reconstructed; generic operator authority does not change the published states.

## Recursion

At the chosen recursion, the lead OmniCoreAgent loop is one operational agent. Spawned subagents are temporary focused workers whose results return to that lead loop. A developer may construct a larger multi-agent organization from the workflow/background primitives, but each such composition is a separate system-in-focus and cannot be imported into this standalone assessment.

## Variety and escalation

Operational variety is absorbed through tool batches, structured observations, context management, loop detection, subagent delegation, durable background retry/recovery and fail-closed governance. These mechanisms make the harness production-oriented without implying that every control mechanism is a separate VSM function or autonomous organizational owner.

## Evidence gaps

The pinned repository gives strong evidence for S1 and broad evidence for negative findings around S2/S3/S3*/S4/S5. The closest future reassessment triggers would be a shipped autonomous portfolio supervisor over background/workflow units, a distinct independent audit actor with corrective closure, or a first-party prospective self-adaptation loop.