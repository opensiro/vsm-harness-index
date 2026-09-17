---
harness_id: agency-swarm
project_name: Agency Swarm
repository: https://github.com/VRSEN/agency-swarm
review_ref: 853d37b9b243edc5dfe2ff2d2d4658aa8ec9a750
reviewed_at: 2026-09-17
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agency Swarm

## Review boundary

- System in focus: the first-party Agency Swarm framework/runtime at the pinned revision, including `Agent`, `Agency`, communication flows, `SendMessage`/handoffs, shared agency context, tool-concurrency support, and input/output guardrails.
- Purpose and identity: construct and run teams of autonomous agents that perform user-directed work through model/tool loops and explicitly configured inter-agent communication paths.
- Relevant environment: user requests, tools/APIs, files, MCP services, model responses, and other agents participating in a configured agency.
- Standard-distribution boundary: first-party runtime, documentation, examples, and tests. Application-specific domain agents, developer-authored organizational policy, and external services are not promoted into harness functions merely because Agency Swarm can host them.
- First-party operating / deployment modes considered: standalone agents and multi-agent agencies using `SendMessage` or handoff flows, shared context, and optional guardrails.
- Recursion level: one configured Agency is the system-in-focus; participating agents are candidate operational units. Agent spawning, delegation, or nested calls do not by themselves establish lower-recursion viability.
- Reviewed revision: `853d37b9b243edc5dfe2ff2d2d4658aa8ec9a750`.
- Observation date: 2026-09-17.
- Current Index contract: VSM Harness Profile `0.2.1`; VSM Harness Methodology `0.3.1`.
- Compatibility check: Profile `0.2.2` is current on Profile `main`; its release contract marks the transition as a terminology-only compatible patch with no assessment impact, so the Index's frozen `0.2.1` assessment provenance is retained.

The candidate pin is preserved. Upstream `main` was also checked on 2026-09-17 and had advanced beyond the pin; the observed changes did not require silently replacing the candidate review boundary.

## Repository architecture

Agency Swarm's `Agent` is an autonomous model/tool loop: the agent can choose actions toward its goal, observe results, and self-correct within configured bounds. An `Agency` groups agents and exposes directional `communication_flows`. `SendMessage` implements orchestrator-worker delegation in which a caller invokes a specialist and receives its result; `Handoff` transfers conversation control to another agent.

The framework also exposes shared `Agency Context`, input/output guardrails, and a `ToolConcurrencyManager`. These are important support mechanisms but their scope matters for VSM mapping. `ToolConcurrencyManager` is explicitly scoped to a single agent instance and serializes tools that require one-call-at-a-time execution. Agency Context is a generic shared state surface. Guardrails are developer-supplied validation functions that inspect ordinary input/output paths and either return guidance, trigger retries, or abort processing.

Primary evidence:

- [`docs/core-framework/agents/overview.mdx`](https://github.com/VRSEN/agency-swarm/blob/853d37b9b243edc5dfe2ff2d2d4658aa8ec9a750/docs/core-framework/agents/overview.mdx) — agents autonomously choose next actions, perceive feedback, and use tools.
- [`docs/core-framework/agencies/communication-flows.mdx`](https://github.com/VRSEN/agency-swarm/blob/853d37b9b243edc5dfe2ff2d2d4658aa8ec9a750/docs/core-framework/agencies/communication-flows.mdx) — handoff and orchestrator-worker semantics; `SendMessage` is the first-party inter-agent communication mechanism.
- [`src/agency_swarm/tools/concurrency.py`](https://github.com/VRSEN/agency-swarm/blob/853d37b9b243edc5dfe2ff2d2d4658aa8ec9a750/src/agency_swarm/tools/concurrency.py) — tool concurrency is managed for a single agent instance.
- [`docs/additional-features/agency-context.mdx`](https://github.com/VRSEN/agency-swarm/blob/853d37b9b243edc5dfe2ff2d2d4658aa8ec9a750/docs/additional-features/agency-context.mdx) — shared context is a general data/state surface used by developer-authored workflows.
- [`docs/additional-features/guardrails/input-guardrails.mdx`](https://github.com/VRSEN/agency-swarm/blob/853d37b9b243edc5dfe2ff2d2d4658aa8ec9a750/docs/additional-features/guardrails/input-guardrails.mdx) and [`output-guardrails.mdx`](https://github.com/VRSEN/agency-swarm/blob/853d37b9b243edc5dfe2ff2d2d4658aa8ec9a750/docs/additional-features/guardrails/output-guardrails.mdx) — ordinary message/output validation, guidance, retry, and abort paths.
- [`tests/integration/guardrails/test_guardrails_integration.py`](https://github.com/VRSEN/agency-swarm/blob/853d37b9b243edc5dfe2ff2d2d4658aa8ec9a750/tests/integration/guardrails/test_guardrails_integration.py) — guardrail feedback/persistence and subagent-suppression behavior in the ordinary execution path.

## Operational model

The operational units are autonomous agent loops that transform user/application goals into model/tool actions and results. A configured orchestrator agent may delegate bounded work to specialist agents and combine their returned outputs. Developers configure which agents exist, the allowed communication graph, shared instructions/context, and any guardrail rules. Deterministic runtime machinery transports messages, persists state, validates ordinary inputs/outputs, and constrains per-agent tool execution.

The assessment therefore separates autonomous operational work from framework expressiveness. A developer can use Agency Swarm to build stronger organizational functions, but generic topology, shared state, validation hooks, and delegation are not classified as `C` unless the corresponding VSM function itself is already established at the reviewed boundary.

## S1 — Operations

- State: `A`.
- Function: participating agents directly perform bounded operational work toward the agency's purpose using model reasoning and tools.
- Disturbance / variety regulated: task-specific user input, tool/environment observations, model feedback, and local execution outcomes.
- Decisive decision or feedback right: select the next action/tool and adapt the local trajectory from returned observations.
- Decision owner: the agent actor in the standard autonomous run.
- Supporting / enforcement mechanisms: tool registries, model/runtime adapters, guardrails, persistence, context, and per-agent tool-concurrency machinery.
- Closure path: observation/tool result returns to the agent loop and changes subsequent model/tool action.
- Why agent-owned: first-party documentation explicitly describes agents as autonomous goal-driven actors that choose their next action and self-correct from feedback.
- Evidence: agent overview at the pinned revision.
- Basis: `explicit` and `structural`.
- Confidence: high.
- Caveats: developer-authored instructions and available tools bound the local action space but do not remove the agent's operational discretion inside that boundary.

## S2 — Coordination

- State: `—`.
- Function finding: multiple agents can coexist, communicate, delegate, and share state, but the reviewed standard distribution does not supply a material first-party S2-specific path that regulates a concrete inter-S1 interference/conflict/oscillation.
- Distinct S1 units: multiple autonomous agents may be configured in one Agency.
- Inter-S1 disturbance: no built-in disturbance/regulation pair was established. The documentation shows delegation, handoff, shared state, and developer-defined message contracts rather than a first-party anti-oscillation or conflict-resolution responsibility.
- Coordination relation: none established beyond generic authored communication/validation primitives.
- Decisive decision or feedback right: not established for an S2 function.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: directional `communication_flows`, `SendMessage`, handoffs, Agency Context, and optional input/output guardrails.
- Closure path: these mechanisms do close ordinary delegation and validation loops, but no S2-specific closure was established.
- Why this is not `C`: `SendMessage` and handoffs route/delegate work; shared context is generic state; guardrail functions are developer-authored validation hooks. The developer must supply both the organizational disturbance and the coordination policy. `ToolConcurrencyManager` cannot supply the missing inter-S1 witness because its implementation explicitly manages concurrency for one agent instance.
- Evidence: communication-flows docs; `concurrency.py`; Agency Context docs; guardrail docs/tests.
- Basis: `structural`.
- Confidence: high.
- Caveats: a particular application can build S2 on these primitives; that composed application would require its own system-in-focus assessment.

## S3 — Inside-and-now control

- State: `—`.
- Function finding: no first-party whole-system current-control authority was established.
- Disturbance / variety regulated: not applicable as an S3 mapping; current task delegation and validation remain operational execution support.
- Decisive decision or feedback right: no built-in actor is shown maintaining a whole-Agency current view and exercising authority over shared resources, commitments, priorities, constraints, accountability, synergy, or intervention on behalf of the whole.
- Decision owner: not established.
- Supporting / enforcement mechanisms: orchestrator-worker delegation, shared context, guardrails, per-agent tool serialization, run limits, and runtime state.
- Closure path: delegation returns specialist results to the caller and guardrails can alter/retry an individual trajectory, but neither path closes S3 current regulation for the Agency as a whole.
- Why not agent-owned / constructor-owned: an orchestrator compiles delegated work, but task allocation and result integration are not S3 without whole-system current authority. Runtime constraints enforce developer-selected limits rather than owning the organizational decision.
- Evidence: communication-flows docs; concurrency implementation; guardrail docs.
- Basis: `structural`.
- Confidence: high.
- Caveats: application code can implement a manager with S3 rights, but framework expressiveness alone does not justify `C`.

## S3* — Complementary audit

- State: `—`.
- Claim being audited: ordinary messages and final outputs may be validated by configured guardrail functions.
- Ordinary reporting path: the same agent input/output and inter-agent message path used for normal production work.
- Complementary access path: none established. Guardrails inspect the ordinary candidate input/output supplied to the runtime; the framework does not provide a separate path with materially different access to operational reality.
- Independence boundary: not established by the framework. A developer may call another evaluator agent from a guardrail, but that is application composition and is not a supplied independent audit channel.
- Decisive audit judgment / owner: developer-supplied guardrail code or whatever application-defined evaluator it invokes; no first-party S3* organizational owner/path is established.
- Supporting / enforcement mechanisms: tripwires, persisted guardrail feedback, retry, strict abort, and suppression of in-flight subordinate output.
- Closure path: guardrail findings can block or feed ordinary retry guidance back into the same operational trajectory; this is routine validation closure, not complementary audit closure.
- Evidence: input/output guardrail docs and integration tests.
- Basis: `structural`.
- Confidence: high.
- Caveats: a separately designed independent evaluator using these hooks could become S3* in a different composed system.

## S4 — Outside-and-then intelligence

- State: `—`.
- Function finding: no first-party external-and-prospective organizational adaptation loop was established.
- External distinction: agents can perceive current tools/APIs/user context, but this is ordinary operational sensing.
- Future/prospective distinction: no separate future-oriented environmental model owned by the harness was established.
- Adaptation option generated: none at organizational capability level.
- Path back into current capability / S3: none established.
- Decision owner: not applicable.
- Supporting mechanisms: model planning, context, memory/persistence, external tools, and developer configuration.
- Closure path: not applicable for a positive S4 mapping.
- Evidence: agent and agency documentation reviewed at the pinned revision.
- Basis: `structural`.
- Confidence: high.
- Caveats: current-task planning or self-correction is not S4 by itself.

## S5 — Policy and identity

- State: `—`.
- Identity / ultimate-policy issue: no runtime identity/ultimate-policy decision path is supplied for the Agency as system-in-focus.
- Ultimate authority: developers/operators author instructions, communication topology, tools, guardrails, and other configuration before or around runs; that authorship is not itself a first-party S5 closure loop.
- Decisive decision or feedback right: no first-party runtime path was established by which an identity/ultimate-policy issue reaches legitimate ultimate authority and an authoritative decision returns to govern subsequent Agency operation.
- Supporting / enforcement mechanisms: shared instructions, agent instructions, topology configuration, guardrails, and runtime enforcement.
- Return-to-operation path: no S5-specific return path established.
- Why not `C` or `P`: static/configurable policy surfaces can constrain operations but do not themselves instantiate S5. Generic human ability to configure, approve, interrupt, or operate the framework does not establish a function-specific parent-governed S5 mode.
- Evidence: Agency and agent configuration docs plus guardrail behavior.
- Basis: `structural`.
- Confidence: high.
- Caveats: a composed organization may retain S5 at a human parent recursion, but that requires evidence for that organization rather than inference from framework configurability.

## Recursion

Agency Swarm supports nested and delegated agent structures, but the reviewed evidence does not establish that each child agent/team carries the metasystemic functions needed to count as a recursively viable subsystem. Spawning, handoff, or subagent calls therefore remain task decomposition unless a separately declared system boundary is assessed.

## Variety and escalation

Agency Swarm supplies useful variety-management mechanisms without thereby closing higher VSM functions. Communication topology attenuates which agents can contact which peers; guardrails constrain acceptable messages/outputs and can feed corrective guidance into retries; shared context transports state; per-agent concurrency serializes selected tool execution. These mechanisms improve operational reliability while the decisive organizational semantics remain application-defined.

Escalation is likewise application-dependent. Agents may return errors, guidance, or delegated results, but no separate first-party organizational escalation ladder establishes S3-S5 ownership at this boundary.

## Evidence gaps

No unresolved evidence gap requires `?` for S2-S5. The review covered the first-party surfaces most likely to support the historical positive claims: communication topology, `SendMessage`/handoffs, shared context, concurrency control, guardrails, and their integration tests. None establishes the missing function-specific organizational witnesses under the current contract.

## Admission conclusion

Canonical vector at the pinned revision: `A — — — — —`.

This is a same-ref correction of the historical proposed vector `A C C C — C`, not a new-ref reassessment. The old proposal promoted generic communication/concurrency/validation/configuration mechanisms into S2, S3, S3*, and S5 without the function-specific witnesses now required by the frozen Profile `0.2.1` / Methodology `0.3.1` contract. The candidate review ref remains unchanged.
