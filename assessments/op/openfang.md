---
harness_id: openfang
project_name: OpenFang
repository: https://github.com/RightNow-AI/openfang
review_ref: acf2587e46be174c10200489c9a2d23a39a98aeb
reviewed_at: 2026-09-20
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-20
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenFang

## Review boundary

- System in focus: the first-party OpenFang Agent OS at pinned revision `acf2587e46be174c10200489c9a2d23a39a98aeb`, including the Rust kernel/runtime, built-in LLM agent loop, shipped autonomous Hands, bundled agent manifests, inter-agent tools, workflow/trigger engines, memory, scheduler, channels, capabilities/security and API/CLI/desktop operating surfaces.
- Purpose and identity: run autonomous agents and persistent Hands under one local Agent OS, with first-party lifecycle, tools, memory, delegation, workflows, scheduling, security and control surfaces.
- Relevant environment: user and channel requests, web/tool observations, model responses, specialist-agent outputs, current fleet state, system/health/quota events, persistent memory, configured schedules, external services and model providers.
- Standard-distribution boundary: OpenFang-owned kernel/runtime, bundled agents/Hands, first-party agent loop and standard workflow/trigger/control surfaces are credited. External LLM providers, external MCP/services, user-authored custom manifests/workflows, and repository development/CI governance remain adjacent unless a first-party shipped mode closes the function.
- Credited operating / distribution surfaces: `openfang-runtime` agent loop and collaboration tools; kernel lifecycle; bundled `orchestrator` and specialist agents; autonomous Hands; workflow and trigger engines; memory/knowledge graph; scheduler; security/capability enforcement; API/CLI/desktop/channel surfaces.
- Adjacent first-party surfaces excluded from ownership: CI/release workflows, repository maintainer governance, tests/examples when they only illustrate composition, external provider decisions and downstream custom agents/workflows not shipped as an OpenFang operating mode.
- First-party operating / deployment modes considered: ordinary built-in chat agents; autonomous scheduled Hands; shipped Orchestrator + specialist-agent fleet; workflow engine pipelines; trigger-driven agents; daemon/API/CLI/desktop operation.
- Recursion level: one OpenFang Agent OS organization containing multiple agent/Hand operational units. Individual agents/Hands can themselves contain tool/subagent loops, but nesting/spawn alone is not credited as a separate VSM recursion.
- Reviewed revision: `acf2587e46be174c10200489c9a2d23a39a98aeb`.
- Observation date: 2026-09-20.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

OpenFang ships its own model/tool agent loop in `openfang-runtime`. `run_agent_loop` loads session context and memories, invokes the LLM, executes selected tools, returns tool results to later model iterations and persists the resulting conversation. The same runtime supports inter-agent calls with longer tool timeouts because `agent_send`/`agent_spawn` may trigger a complete child agent loop. Bundled Hands package autonomous operating programs such as lead generation, intelligence collection, browser work, predictions and social-media management, often with persistent or scheduled execution.

The standard distribution also ships an `orchestrator` agent whose system prompt calls it the command center of the Agent OS. It can inspect all running agents and capabilities through `agent_list`, delegate current work with `agent_send`, create capacity with `agent_spawn`, terminate agents with `agent_kill`, and use shared memory. The underlying `agent_list` tool exposes agent id/name/state/description/tags/tools/model, giving the orchestrator a current fleet view rather than only a static roster. Its first-party instructions require decomposition, inspection of available agents, allocation of subtasks, delegation and synthesis. This closes an autonomous whole-system current-control path and supports S3=A.

OpenFang has substantial multi-agent communication and workflow machinery, but no reviewed first-party path establishes the stricter S2 witness: a concrete inter-S1 interference/conflict/oscillation plus a coordination relation specifically attenuating that disturbance and feeding the result back into later S1 behaviour. Delegation, fan-out/collect, message passing, sequential workflows and capability restrictions therefore remain mechanisms rather than S2 evidence.

Audit-like surfaces are also present but do not close S3*. The bundled `security-auditor` is a genuinely separate specialist with file/shell access and an audit-oriented prompt, and workflow examples route analysis through it. However those examples terminate its findings in a `security_review` variable and a report/summary; the fact-check example likewise reports findings without a first-party corrective return into the producing S1. Merkle/audit logs, health events and diagnostics are ordinary evidence/reporting mechanisms. A downstream workflow could wire findings into remediation, but that closure is not supplied as the standard repository mode reviewed here.

OpenFang's Hands, predictor/collector agents, memory consolidation, knowledge graphs, triggers and agent spawning can sense/change current work and retain information. They do not establish S4 for the Agent OS itself: no standard path takes prospective external distinctions, generates organizational/capability adaptation options, decides among them and changes later OpenFang capability. Likewise capability manifests, signed permissions, security rules and operator settings are strong policy/enforcement surfaces but no runtime identity/ultimate-policy S5 closure is established.

Primary evidence:

- [`crates/openfang-runtime/src/agent_loop.rs`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/crates/openfang-runtime/src/agent_loop.rs) — first-party model/tool operational loop and inter-agent tool execution context.
- [`agents/orchestrator/agent.toml`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/agents/orchestrator/agent.toml) — shipped autonomous current-control agent and its fleet/delegation/spawn/kill decision rights.
- [`crates/openfang-runtime/src/tool_runner.rs`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/crates/openfang-runtime/src/tool_runner.rs) — collaboration tools; `agent_list` exposes current agent state/capabilities and task/message machinery.
- [`crates/openfang-hands/bundled/`](https://github.com/RightNow-AI/openfang/tree/acf2587e46be174c10200489c9a2d23a39a98aeb/crates/openfang-hands/bundled) — shipped autonomous Hand definitions.
- [`agents/security-auditor/agent.toml`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/agents/security-auditor/agent.toml) — separate security specialist and proactive schedule.
- [`docs/workflows.md`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/docs/workflows.md) — workflow/trigger semantics and review/fact-check examples showing the limits of standard audit feedback closure.
- [`README.md`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/README.md) — product/runtime boundary, Hands, memory, scheduler, security, channels and deployment surfaces.

## Operational model

A normal OpenFang agent receives a task/message into the first-party agent loop. The model sees session/memory context and available tools, chooses actions/tool calls, OpenFang executes them and feeds observations back into subsequent model iterations until completion or a runtime bound. Hands package the same autonomous operating capability into longer-lived domain programs.

At the fleet recursion, the bundled Orchestrator is a separate autonomous agent with current access to agent states/capabilities and authority to send work, spawn additional agents and kill no-longer-needed agents. Its model therefore owns current choices about decomposition, specialist allocation and active fleet composition while deterministic kernel capability checks enforce what those choices are permitted to do.

The workflow engine adds deterministic authored pipelines: sequential, fan-out/collect, conditional and loop modes. Trigger rules convert lifecycle/system/memory/content events into prompts to configured agents. These are useful support/enforcement paths, but authored workflow topology and trigger matching do not automatically own S2/S3/S3*/S4/S5 decisions.

## S1 — Operations

- State: A
- Function: autonomously perform assigned work through a first-party model/tool decision-action loop and persistent Hands.
- Disturbance / variety regulated: task ambiguity, tool/environment observations, changing external information, tool failures/results and uncertainty over the next operational action.
- Decisive decision or feedback right: choose the next substantive tool/action from current context and observations and decide whether to continue or conclude.
- Decision owner: the running OpenFang agent/Hand model.
- Supporting / enforcement mechanisms: kernel lifecycle, tool runner, memory/session substrate, context guards, loop guard, provider retry/fallback, scheduler, capability checks, channels and sandboxing.
- Closure path: task/message → model decision → OpenFang executes selected tool/action → observation returned into conversation → next model decision → repeated operation or terminal outcome.
- Boundary reachability: `run_agent_loop` is the standard first-party runtime path and bundled agents/Hands directly use that runtime in the shipped distribution.
- Why this is / is not agent-owned: the kernel transports, bounds and enforces decisions, but the model selects substantive actions from current evidence; removing the model leaves only deterministic runtime machinery rather than materially the same operational choice.
- Evidence: [`crates/openfang-runtime/src/agent_loop.rs`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/crates/openfang-runtime/src/agent_loop.rs), [`crates/openfang-hands/bundled/`](https://github.com/RightNow-AI/openfang/tree/acf2587e46be174c10200489c9a2d23a39a98aeb/crates/openfang-hands/bundled), [`README.md`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external LLM providers supply inference but do not own OpenFang's first-party operating loop/closure.

## S2 — Coordination

- State: —
- Function: no sufficiently evidenced S2-specific attenuation of concrete interference/conflict/oscillation among distinct OpenFang S1 units is established in the reviewed standard distribution.
- Disturbance / variety regulated: no specific qualifying inter-S1 disturbance is established.
- Decisive decision or feedback right: none established for an S2-specific attenuation relation.
- Decision owner: none established for S2.
- Supporting / enforcement mechanisms: message bus, `agent_send`, delegation, shared memory, workflow sequencing, fan-out/collect, capability restrictions and task queues.
- Closure path: no qualifying inter-S1 disturbance → attenuation relation/decision → changed subsequent S1 behaviour loop is established.
- Why this is / is not agent-owned: OpenFang supplies substantial communication and orchestration, but delegation/routing/sequencing/shared state alone do not meet the Methodology's S2 function threshold.
- Evidence: [`agents/orchestrator/agent.toml`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/agents/orchestrator/agent.toml), [`crates/openfang-runtime/src/tool_runner.rs`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/crates/openfang-runtime/src/tool_runner.rs), [`docs/workflows.md`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/docs/workflows.md).
- Basis: explicit absence after function-first review.
- Confidence: high.
- Caveats: a downstream workflow can define an actual organizational collision and use OpenFang primitives to regulate it; that separate system would require its own assessment.

### Absence scope

- Surfaces inspected: inter-agent tools, Orchestrator delegation, workflow sequential/fan-out/collect/conditional/loop modes, task/message/shared-memory machinery and capability restrictions.
- Plausible first-party paths checked: delegation, specialist selection, messaging, shared memory, task queueing, parallel fan-out and deterministic sequencing.
- Why no material first-party path remains: the inspected paths transport/allocate work or constrain access but do not identify a concrete inter-S1 conflict/oscillation and a dedicated attenuation relation with feedback into subsequent S1 behaviour.

## S3 — Inside-and-now control

- State: A
- Function: autonomously regulate current fleet composition and allocation of work across the OpenFang agent organization.
- Disturbance / variety regulated: changing current task decomposition, available/running specialist agents, their capabilities/states and the need to allocate, add or remove operating capacity while work proceeds.
- Decisive decision or feedback right: inspect the current fleet, choose specialist allocations via `agent_send`, create agents with `agent_spawn`, terminate agents with `agent_kill`, and synthesize current delegated work.
- Decision owner: the shipped `orchestrator` model in the autonomous Orchestrator mode.
- Supporting / enforcement mechanisms: `agent_list` state/capability data, kernel lifecycle/capability enforcement, inter-agent messaging, shared memory, tool timeouts and deterministic spawn/kill execution.
- Closure path: current user/task demand + `agent_list` fleet view → Orchestrator model decides decomposition/allocation/fleet changes → kernel executes send/spawn/kill → affected specialists operate → their returned results/current state inform synthesis and later control decisions.
- Boundary reachability: the Orchestrator is a bundled first-party agent manifest in the standard distribution; its required collaboration tools are first-party kernel/runtime tools.
- Why this is / is not agent-owned: the model owns the discretionary choice of how to decompose and allocate current work and whether capacity should be spawned/killed. Kernel checks enforce permissions but do not choose the organizational allocation.
- Evidence: [`agents/orchestrator/agent.toml`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/agents/orchestrator/agent.toml), [`crates/openfang-runtime/src/tool_runner.rs`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/crates/openfang-runtime/src/tool_runner.rs), [`docs/agent-templates.md`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/docs/agent-templates.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic workflow engine scheduling is not the S3 owner. No `(P)` modifier is published because operator CLI/TUI controls were not sufficient on the reviewed evidence to reconstruct a distinct parent-governed whole-system S3 loop rather than administrative intervention controls.
- Whole-system current view: `agent_list` exposes all running agents with state, capabilities/tools, description/tags and model, and the Orchestrator is instructed to inspect available agents before allocating work.
- Current-control decision scope: current task decomposition/allocation, specialist selection, creation/removal of active agent capacity and inter-agent commitment routing.

## S3* — Complementary audit

- State: —
- Function: no standard first-party independent audit path is established whose findings are obligatorily returned into corrective production operation.
- Disturbance / variety regulated: hidden divergence between ordinary operational outputs and reality/security/quality can be inspected, but corrective audit closure is not established.
- Decisive decision or feedback right: none established for a complete complementary audit→correction loop.
- Decision owner: none established for S3* publication.
- Supporting / enforcement mechanisms: bundled `security-auditor`, security-review/fact-check workflow examples, Merkle audit trail, logs, health events, triggers and diagnostics.
- Closure path: reviewed examples produce audit/fact-check findings or reports, but no standard path requires those findings to modify the producing S1/current operation before completion.
- Why this is / is not agent-owned: the security auditor is a separate model actor with complementary tools/evidence, but independence plus judgment alone is insufficient; the first-party examples terminate findings in variables/reports/summaries instead of closing corrective feedback into operations.
- Evidence: [`agents/security-auditor/agent.toml`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/agents/security-auditor/agent.toml), [`docs/workflows.md`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/docs/workflows.md), [`README.md`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/README.md).
- Basis: explicit absence after closure review.
- Confidence: high.
- Caveats: users can author a remediation workflow using the supplied audit specialist and workflow engine, but that downstream composition is not the standard closed S3* mode assessed here.

### Absence scope

- Surfaces inspected: security-auditor manifest, workflow security-review/fact-check examples, iterative review loop, Merkle audit trail/security docs, health/system triggers and logs/diagnostics.
- Plausible first-party paths checked: independent security specialist, fact-check agent, code-review workflows, audit log verification and event-triggered monitoring.
- Why no material first-party path remains: audit-like evidence/judgments are available, but inspected standard paths end in reports/summaries or generic event prompts; no first-party closed path compels findings to alter the audited production S1/current operation.

## S4 — Intelligence/adaptation

- State: —
- Function: no prospective environment-facing adaptation loop is established that changes OpenFang's future organizational capability.
- Disturbance / variety regulated: external signals, predictions, collected intelligence and changing system events are handled as operational inputs, not as a first-party capability-adaptation program.
- Decisive decision or feedback right: none established for selecting and incorporating future capability/organizational adaptations.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: Collector/Predictor Hands, web/research agents, persistent memory/consolidation, knowledge graph, triggers, agent spawning, skill registry and user/developer custom manifests.
- Closure path: no standard external/prospective distinction → adaptation options → selected option → changed present capability/S3 loop is established.
- Why this is / is not agent-owned: Hands may continuously monitor the environment and agents may retain knowledge or spawn current specialists, but those behaviours serve current domain outcomes. They do not autonomously redesign or extend OpenFang's later capability from prospective intelligence.
- Evidence: [`crates/openfang-hands/bundled/collector/HAND.toml`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/crates/openfang-hands/bundled/collector/HAND.toml), [`crates/openfang-hands/bundled/predictor/HAND.toml`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/crates/openfang-hands/bundled/predictor/HAND.toml), [`docs/workflows.md`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/docs/workflows.md), [`README.md`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/README.md).
- Basis: explicit absence after function-first review.
- Confidence: high.
- Caveats: agent spawning changes current fleet capacity and therefore supports S3; it is not by itself prospective S4 adaptation. Developer-created agents/skills are external construction.

### Absence scope

- Surfaces inspected: autonomous Hands, predictor/collector behavior, memory/consolidation/knowledge graph, trigger engine, agent spawn/custom manifest paths, skill registry and workflow engine.
- Plausible first-party paths checked: persistent learning, external monitoring/prediction, event-driven reactions, dynamic agent creation and extension by skills/custom agents.
- Why no material first-party path remains: reviewed mechanisms either improve current information/operation or expose developer extensibility; none closes a prospective outside→options→future-capability adaptation loop owned by the running organization.

## S5 — Policy/identity

- State: —
- Function: no runtime identity or ultimate-policy authority loop is established at the OpenFang organization boundary.
- Disturbance / variety regulated: permissions, manifests, security controls, provider settings and operator configuration govern ordinary operation rather than an identity/ultimate-policy dispute.
- Decisive decision or feedback right: ultimate organizational identity/policy remains authored in manifests/configuration/operator choices; no autonomous or operationally closed parent S5 loop is established.
- Decision owner: none established for S5 publication.
- Supporting / enforcement mechanisms: capability system, signed manifests, sandboxing, security policies, credential handling, schedules, quotas, tool policy and operator/API configuration.
- Closure path: no qualifying identity/ultimate-policy matter → ultimate authority decision → returned governance of subsequent operation loop is established.
- Why this is / is not agent-owned: deterministic security and manifest policy strongly constrain agents but do not themselves make identity/ultimate-policy decisions. Operator configuration is not automatically a parent S5 mode.
- Evidence: [`README.md`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/README.md), [`docs/security.md`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/docs/security.md), [`docs/architecture.md`](https://github.com/RightNow-AI/openfang/blob/acf2587e46be174c10200489c9a2d23a39a98aeb/docs/architecture.md).
- Basis: explicit absence after function-first review.
- Confidence: high.
- Caveats: human operators/maintainers can change manifests, capabilities and configuration, but the reviewed standard distribution does not reconstruct an identity-level matter, legitimate ultimate authority and return-to-operation loop required for S5/P.

### Absence scope

- Surfaces inspected: capability permissions, signed manifests, sandbox/security controls, quotas, schedules, tool policy, operator configuration, API/CLI management and bundled agent prompts.
- Plausible first-party paths checked: manifest authority, capability grants, operator admin controls, security policies and agent system prompts.
- Why no material first-party path remains: all inspected paths pre-author or enforce operating constraints; none establishes a runtime identity/ultimate-policy decision function with authoritative closure.

## Recursion, variety, escalation and evidence gaps

- Recursion: individual agents/Hands are operational units inside an OpenFang fleet. The bundled Orchestrator provides a higher current-control layer over those units. Spawned subagents alone are not treated as proof of additional VSM recursion.
- Variety: model/tool choices, many specialist agents/Hands, workflows, channels and external integrations create operational variety; kernel capabilities, quotas, loop guards, sandboxes, workflow bounds and orchestration attenuate it.
- Escalation: system/health/quota events can trigger agents, humans can intervene through API/CLI/UI, and security/capability checks can block actions. These are escalation/control mechanisms and do not independently establish S3*, S4 or S5.
- Evidence gaps: no material gap blocks the vector. S3 parent-mode and S3* were reviewed conservatively: operator fleet controls do not by themselves establish `(P)`, and separate auditor/reporting surfaces lack a demonstrated standard corrective return path.

## Standalone vector

`A — A — — —`
