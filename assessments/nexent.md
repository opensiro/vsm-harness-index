---
harness_id: nexent
project_name: Nexent
repository: https://github.com/ModelEngine-Group/nexent
review_ref: 9713e7823eb2b11410776acf40d2633eef425af7
reviewed_at: 2026-09-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-29
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Nexent

## Review boundary

- System in focus: the first-party Nexent agent runtime/platform at frozen revision `9713e7823eb2b11410776acf40d2633eef425af7`, including the SDK `CoreAgent`/`NexentAgent` loop, recursively configured managed agents, external-A2A proxy integration, run/concurrency lifecycle, context runtime, verification/guardrails, optional durable human-interaction runtime, scheduler, memory/Dreaming subsystem, agent-version service and platform RBAC where those surfaces are part of the shipped distribution.
- Purpose and identity: provide an enterprise agent platform in which configured agents reason, invoke tools or managed agents, retrieve context/memory and return user-facing outcomes, while platform services govern deployment, access, persistence and lifecycle.
- Relevant environment: users and operators, external model providers, MCP/tools and knowledge sources, remote A2A agents, tenant resources, scheduled jobs and application data.
- Standard-distribution boundary: Nexent SDK/backend orchestration and platform services are inside. External model cognition, remote A2A implementations, MCP servers, external data stores/providers and user/operator judgment remain external actors even when Nexent transports their decisions.
- Credited operating / distribution surfaces: ordinary `CoreAgent` execution; recursively constructed internal managed agents; configured external A2A wrappers as callable managed-agent tools; optional HITL root-agent mode; verification/guardrail mode; memory/Dreaming and version-management services.
- Adjacent first-party surfaces excluded from ownership: benchmark/evaluation directories, repository tests/CI, contributor/development workflows, frontend presentation by itself, and generic platform administration unless it closes a VSM function in the assessed operating boundary.
- First-party operating / deployment modes considered: ordinary single-agent runtime; nested internal managed-agent trees; external A2A delegation; root-agent HITL mode; platform scheduler/memory/version/RBAC services. These are capability modes and are not assumed to run simultaneously.
- Recursion level: the assessed whole is Nexent as an agent harness/platform. A managed child can itself be a full `CoreAgent`, but nesting/delegation is not treated as recursive viability without an independently evidenced metasystem at the child level.
- Reviewed revision: `9713e7823eb2b11410776acf40d2633eef425af7`.
- Observation date: 2026-09-29.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Nexent's operational center is `CoreAgent`, a first-party extension of the smolagents code-agent loop. A run prepares context, sends the active tool and managed-agent surface to the executor, obtains model-selected executable actions, dispatches them, records observations in agent memory and repeats until a final answer or runtime boundary terminates the run. Verification and guardrails can screen input, tool arguments, tool results and final answers; failed final verification can feed a repair instruction back into another agent attempt.

`NexentAgent.create_single_agent` recursively constructs configured managed agents. Internal children are full Nexent agents wrapped as callable tools; configured remote A2A agents are also wrapped into the parent's `managed_agents` surface. The wrapper records nesting boundaries but delegates execution to the child. Separate backend services reserve live runs and per-agent concurrency slots, while the reusable scheduler uses leases, renewal and stale-worker fencing for durable jobs.

The optional human-interaction runtime supports root-agent clarification, safe-boundary steering, durable checkpoints and exactly-once-style tool receipts. It explicitly rejects a root carrying managed/A2A subagents in that mode. Memory includes retrieval and a Dreaming pipeline that scores/promotes short-term evidence into bounded long-term summaries. Agent publication/versioning snapshots models/tools/relations/skills, pins child versions and exposes explicit user-driven publish/rollback. Platform RBAC maps roles to cached resource permissions.

Primary evidence:

- [`sdk/nexent/core/agents/core_agent.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/core_agent.py)
- [`sdk/nexent/core/agents/nexent_agent.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/nexent_agent.py)
- [`sdk/nexent/core/agents/subagent_wrapper.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/subagent_wrapper.py)
- [`sdk/nexent/core/agents/a2a_agent_proxy.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/a2a_agent_proxy.py)
- [`sdk/nexent/core/agents/verification.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/verification.py)
- [`backend/agents/agent_run_manager.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/backend/agents/agent_run_manager.py)
- [`sdk/nexent/core/human_interaction/runtime.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/human_interaction/runtime.py)
- [`sdk/nexent/scheduler/core.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/scheduler/core.py)
- [`sdk/nexent/memory/dreaming/service.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/memory/dreaming/service.py)
- [`sdk/nexent/memory/dreaming/version_builder.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/memory/dreaming/version_builder.py)
- [`backend/services/agent_version_service.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/backend/services/agent_version_service.py)
- [`backend/permissions/rbac.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/backend/permissions/rbac.py)

## Operational model

A user task enters a stateful ReAct/code-tool loop. The model chooses executable actions over the active tool surface; first-party runtime code executes them and appends observations for the next model decision. A parent can invoke an internal child or remote A2A wrapper exactly as another callable managed tool. Platform services can constrain concurrency, suspend for clarification, verify outputs, persist memory or expose published versions, but Methodology 0.3.6 requires those mechanisms to be tied to the relevant organizational function before receiving S2–S5 credit.

## S1 — Operations

- State: A
- Function: execute user-directed agent work through a closed model/tool feedback loop.
- Disturbance / variety regulated: changing user tasks, tool/data results, execution errors, retrieved context, model outputs, context pressure and intermediate action state.
- Decisive decision or feedback right: choose the next substantive action/tool/managed-agent invocation or finish after observing current task state and prior execution results.
- Decision owner: the configured model acting through Nexent's `CoreAgent` loop.
- Supporting / enforcement mechanisms: context runtime, code executor/sandbox, tool registry, managed-agent wrappers, run cancellation, verification/guardrails, planning state and conversation memory.
- Closure path: task → model-selected action → first-party execution/tool or child call → observation appended to memory → later model decision → final outcome.
- Boundary reachability: this is the ordinary shipped SDK runtime instantiated by `NexentAgent`; no benchmark/development harness is borrowed.
- Why this is / is not agent-owned: if model discretion is removed while the execution machinery remains, the runtime no longer selects materially equivalent substantive next actions; the deterministic machinery executes and constrains rather than chooses the work.
- Evidence: [`core_agent.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/core_agent.py); [`nexent_agent.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/nexent_agent.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external model internals are outside the repository boundary; the credited autonomy is the closed first-party model/action/observation path.

## S2 — Coordination

- State: —
- Function: no material function-specific inter-S1 coordination relation was established at the reviewed boundary.
- Distinct S1 units: Nexent can instantiate multiple full managed agents and can call external A2A agents, but their coexistence alone is not an S2 witness.
- Inter-S1 disturbance: no specific actual or structurally evidenced oscillation/conflict among distinct Nexent S1 units was found with a corresponding first-party attenuation relation.
- Attenuating coordination relation: not established. Run reservations, per-agent capacity limits, scheduler leases/fencing and nested invocation serialize/admit infrastructure work but are not tied to a demonstrated inter-S1 operational disturbance.
- Feedback into subsequent S1 behaviour: no function-specific S2 closure path established.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: managed-agent calls and A2A are handoff/delegation transports; scheduler leases prevent duplicate durable-job execution; neither supplies the required specific inter-S1 mutual-adjustment witness.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: `SubAgentToolWrapper`, external A2A proxy, agent-run reservation/capacity counters, scheduler leases and cancellation/fencing.
- Closure path: not established for S2.
- Why this is / is not agent-owned: a parent model may choose a child agent, but delegation/task decomposition does not by itself regulate oscillation or destructive interference between autonomous operational units.
- Evidence: [`subagent_wrapper.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/subagent_wrapper.py); [`a2a_agent_proxy.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/a2a_agent_proxy.py); [`agent_run_manager.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/backend/agents/agent_run_manager.py); [`scheduler/core.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/scheduler/core.py).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: applications built on Nexent can define their own coordination semantics; constructor expressiveness alone does not publish `C` for S2.

### Absence scope

- Surfaces inspected: recursive internal managed agents, external A2A proxy, parent/child invocation wrapper, backend active-run/concurrency manager, scheduler lease/fencing core, planning/context runtime and platform lifecycle controls.
- Plausible first-party paths checked: parallel/nested agent execution, A2A collaboration, per-agent capacity, durable scheduler leases, shared runtime state and parent selection of child agents.
- Why no material first-party path remains: every reviewed path is delegation, transport, lifecycle admission, duplicate-execution prevention or generic shared state; none is tied to a specific interference/oscillation among distinct S1 operational units with a returned coordination result changing their later behavior.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-control function was established over multiple operational units' resources, commitments, priorities or accountability.
- Disturbance / variety regulated: current-run lifecycle and capacity are bounded, but no S3-level shared organizational commitment/resource variety is shown being discretionarily regulated on behalf of the whole.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: parent managed-agent calls, run/capacity reservation, stop/cancel controls, scheduler concurrency, plan state, published agent versions and HITL steering are useful control mechanisms but do not establish the S3 function.
- Closure path: no whole-system S3 closure established.
- Why this is / is not agent-owned: the parent model delegates a task to configured children and consumes their reports, which is below the Methodology's S3 threshold; host services enforce preselected capacity/lifecycle rules rather than bargaining/revising shared commitments from a whole-system view.
- Evidence: [`nexent_agent.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/nexent_agent.py); [`agent_run_manager.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/backend/agents/agent_run_manager.py); [`scheduler/core.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/scheduler/core.py); [`human_interaction/runtime.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/human_interaction/runtime.py); [`agent_version_service.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/backend/services/agent_version_service.py).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: an operator can alter agent versions/configuration and stop runs, but generic administration/current intervention is not a reconstructed S3 parent loop.

### Absence scope

- Surfaces inspected: nested-agent construction/invocation, run manager, scheduler, plan/context runtime, agent version publish/rollback, HITL clarification/steering, cancellation and platform RBAC.
- Plausible first-party paths checked: parent-as-manager, backend run supervisor, concurrency controller, scheduled work controller, operator version rollback, user steering and role permissions.
- Why no material first-party path remains: these surfaces delegate one parent task, enforce static limits, control individual run lifecycle or expose administrative edits. None combines a whole-system present-tense view with authority to discretionarily regulate shared operational commitments/resources as S3.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit path was established beyond the ordinary production/verification path.
- Claim being audited: Nexent can check tool results and final-answer candidates for syntax/errors/evidence/format and related criteria.
- Ordinary reporting path: `CoreAgent` records its own action/tool observations and candidate answer in the same run memory used by verification.
- Complementary access path: not established. The optional LLM final verifier reads a summary of that same run and calls the same configured model object; deterministic pre/post checks and guardrails are routine in-path gates.
- Independence boundary: the verifier is deliberately embedded in the normal production loop and shares the host model/evidence surface; it does not provide materially different access to operational reality.
- Who acts on findings: ordinary `CoreAgent` execution receives verification feedback and may retry/repair; this demonstrates corrective closure but not complementary-audit independence.
- Decisive decision or feedback right: no independent S3* audit judgment established.
- Decision owner: not applicable for S3* publication.
- Supporting / enforcement mechanisms: deterministic verification checks, LLM verifier, guardrail engine, observer/monitoring traces and repair-round counters.
- Closure path: verifier failure → repair instruction → same agent loop can retry, but this remains ordinary production QA rather than S3*.
- Boundary reachability: verification is shipped and reachable, but fails the S3* independence/function threshold rather than the deployment-boundary test.
- Why this is / is not agent-owned: an LLM may make a verification judgment, yet autonomy of a routine checker does not transform it into complementary audit.
- Evidence: [`verification.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/verification.py); [`core_agent.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/core_agent.py).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: external benchmarks/evaluation could supply independent evidence, but adjacent benchmark tooling is excluded unless wired into the assessed operating distribution.

### Absence scope

- Surfaces inspected: deterministic action/tool/final checks, optional LLM final verifier, guardrails, observer/monitoring events, repair loop and repository benchmark surface as an adjacent system.
- Plausible first-party paths checked: final-answer verification, tool-result checking, citation/evidence validation, monitoring/tracing, guardrails and benchmark/evaluation code.
- Why no material first-party path remains: shipped runtime checking is routine and uses the ordinary run's evidence/model path; adjacent benchmark code is not a reached complementary-audit controller for the supported runtime. No independent audit path with returned metasystemic control was found.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop was established for the Nexent organization/harness itself.
- Disturbance / variety regulated: memory relevance, prior interactions, tool/data changes and agent configuration can affect work, but no evidenced future-oriented environmental distinction is converted into an adaptation option for the harness and returned to current capability.
- External distinction: not established at S4 level. External retrieval/A2A/tool data are inputs to operational tasks rather than an evidenced environment-modeling function for organizational adaptation.
- Future / prospective distinction: not established.
- Adaptation option generated: not established. Dreaming creates bounded long-term memory versions from prior memory evidence; agent publish/rollback snapshots operator-authored configurations.
- Path back into current capability / S3: memory can influence later answers and an operator can publish/rollback agent versions, but no external/prospective option-generation conversation with current capability is evidenced.
- Decisive decision or feedback right: not established.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: memory retrieval, Dreaming candidate scoring/summarization, context management, agent version snapshots/publish/rollback and external tools/A2A.
- Closure path: no S4-specific closure established.
- Boundary reachability: all cited mechanisms are reachable first-party surfaces; the negative finding is functional, not merely boundary-based.
- Why this is / is not agent-owned: autonomous summarization/retrieval is internal memory consolidation; user-driven configuration publication is administration. Neither meets the external-and-prospective S4 test.
- Evidence: [`memory/dreaming/service.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/memory/dreaming/service.py); [`memory/dreaming/version_builder.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/memory/dreaming/version_builder.py); [`agent_version_service.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/backend/services/agent_version_service.py); [`a2a_agent_proxy.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/a2a_agent_proxy.py).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: applications can assign future-oriented research tasks to Nexent agents, but operational task research is not automatically an S4 function of the harness.

### Absence scope

- Surfaces inspected: memory service/Dreaming, context runtime, A2A/tool integration, agent versioning/rollback, scheduler and agent-generation/configuration surfaces identified in the distribution.
- Plausible first-party paths checked: memory consolidation, learned user facts, external retrieval, remote-agent calls, agent version evolution, scheduled work and generated agent/skill configuration.
- Why no material first-party path remains: reviewed mechanisms either support present operational tasks, summarize internal history or enact operator-selected configuration. No first-party path was found that senses future-relevant external distinctions, develops adaptation options and returns them into present organizational capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy closure was established at the assessed recursion.
- Disturbance / variety regulated: platform security/access and human steering constrain operation, but no identity-level or ultimate-policy issue/decision loop is shown.
- Decisive decision or feedback right: not established for S5.
- Decision owner: not applicable.
- Supporting / enforcement mechanisms: RBAC role→permission enforcement, guardrail rules, tenant isolation, HITL clarification/steering, agent configuration/version publication and runtime cancellation.
- Closure path: no identity/ultimate-policy issue → legitimate authority → authoritative decision → returned governing-policy path established.
- Why this is / is not agent-owned: RBAC and guardrails enforce preconfigured rules; HITL handles current-run clarification/steering and explicitly states that human approval does not replace resource permissions; version/config edits are generic administration rather than an S5 policy-resolution loop.
- Evidence: [`backend/permissions/rbac.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/backend/permissions/rbac.py); [`human_interaction/runtime.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/human_interaction/runtime.py); [`verification.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/sdk/nexent/core/agents/verification.py); [`agent_version_service.py`](https://github.com/ModelEngine-Group/nexent/blob/9713e7823eb2b11410776acf40d2633eef425af7/backend/services/agent_version_service.py).
- Basis: explicit + structural negative finding.
- Confidence: high.
- Caveats: platform administrators are legitimate authorities over deployment/configuration in practice, but Methodology 0.3.6 does not publish S5 from generic operator control without the function-specific policy/identity closure path.

### Absence scope

- Surfaces inspected: RBAC, tenant/resource permissions, guardrails, HITL clarification/steering/checkpointing, agent publish/rollback, runtime cancellation and configuration surfaces.
- Plausible first-party paths checked: admin permissions, safety policy rules, human approvals/steering, agent version governance and operator intervention.
- Why no material first-party path remains: every reviewed path is access enforcement, action-level steering, safety filtering or generic configuration administration. No runtime mechanism reconstructs an identity/ultimate-policy exception reaching legitimate authority and returning an authoritative policy decision that governs subsequent operation.

## Recursion

Managed Nexent children can be full agent loops and external A2A agents can be invoked through the same managed-agent interface. This establishes nested operational execution, not recursive VSM viability by itself. No S2–S5 state is inferred merely because an agent tree exists.

## Variety and escalation

Nexent attenuates runtime variety with context management, sandboxing, concurrency limits, scheduler leases, cancellation, verification/guardrails, RBAC and optional durable human steering. The HITL mode can ask clarifying questions and accept same-run steering at safe boundaries; it currently refuses managed/A2A children, reinforcing that this is a root-run interaction mode rather than an evidenced parent metasystem over a multi-agent organization. These mechanisms constrain or transport decisions and are not promoted to VSM ownership without function-specific closure.

## Evidence gaps / terminal outcome

Proposed vector: `S1=A / S2=— / S3=— / S3*=— / S4=— / S5=—`.

The classification intentionally resists name-based promotion. Managed agents/A2A establish delegation, not S2. Capacity/scheduler/version controls enforce lifecycle and administration, not S3. Verification has a real repair loop but remains routine same-path QA rather than complementary S3*. Dreaming is durable memory consolidation, not external/prospective S4. RBAC, guardrails and HITL constrain or steer ordinary operation without an S5 identity/ultimate-policy closure path.