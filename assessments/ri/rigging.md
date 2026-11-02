---
harness_id: rigging
project_name: rigging
repository: https://github.com/glaborie/rigging
review_ref: 7b04ad9064a655d74a2c0566ac25c9bd7444df12
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# rigging

## Review boundary

- System in focus: A first-party `rigging` Python manifest-instantiated agent and its optional first-party child runs.
- Purpose and identity: A composable model/tool harness with configurable skills, guardrails, retrieval, approvals, event logs and observability.
- Relevant environment: User task inputs, model gateways, tool/MCP results, policies and resource limits.
- Standard-distribution boundary: The packaged Python runtime/CLI, manifest-defined extensions and first-party subagent implementation at the frozen commit; third-party plugins and their internal control are excluded.
- Credited operating / distribution surfaces: `rigging/loop.py`, `manifest.py`, `subagents.py`, tools, guardrails, approvals, event log and CLI-supported execution.
- Adjacent first-party surfaces excluded from ownership: Development golden eval suites, offline model calibration, demo fixtures, architecture roadmap and public maintainer governance.
- First-party operating / deployment modes considered: Single-agent manifest/CLI, optional guarded human handoff, MCP/retrieval, manifest-declared child agents and parallel tool execution.
- Recursion level: A deployed task-facing agent and its optional child-run tree; parallel tools are not separate autonomous operating units.
- Reviewed revision: `7b04ad9064a655d74a2c0566ac25c9bd7444df12`.
- Observation date: 2026-11-02.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The registry assembles an `AgentSpec` into a model client, named tool capabilities, guardrail hooks, approval policy, skills and event exporters. The agent loop sends model requests, executes the selected tools (optionally in a bounded thread pool), records structured events and gives tool results back to the model. Manifest-declared subagents become `spawn_<name>` tools: a child has its own prompt, model and budget, and reports to its parent in the shared event log. The read-only event-log web view cannot authorize or steer a run. The README's v0.6 capability matrix is less current than `docs/milestones.md`, which explicitly records completion of the source-implemented child-run, auth and parallel-tool milestone at the reviewed revision; this review considers those present code paths, not presumed deployment uptake.

## Operational model

The model makes task-level choices and can delegate a bounded subtask. Approval hooks and deterministic guardrails constrain these choices; the human decides whether to approve consequential calls or receive escalation. Logged eval assertions and offline calibration inform developers but are not wired as an independent operational controller. No function-specific higher-recursion planning, coordination, complementary audit or ultimate-policy adjudication loop is evidenced.

## S1 — Operations

- State: A
- Function: Select and carry out task-relevant actions through model/tool feedback, including optional child delegation.
- Disturbance / variety regulated: Changing prompts, tool/environment observations, denials, tool failures, budgets and incomplete subtasks.
- Decisive decision or feedback right: Choose next tool, child task or final response on the basis of returned results.
- Decision owner: The model in the first-party `run_agent` loop; an optional child model performs its own bounded S1 work.
- Supporting / enforcement mechanisms: Manifest/registry, model gateway, tool/MCP adapters, guardrails, approvals, token/step limits and persisted event log.
- Closure path: User/task context → model tool/delegation decision → constrained execution → tool/child result → next model request or answer.
- Boundary reachability: `harness run` instantiates the first-party loop; manifest `subagents` is resolved into an executable spawn tool by `run_agent` without external orchestration.
- Why this is / is not agent-owned: The model chooses substantive actions; the deterministic runtime enforces a safety envelope without owning action selection.
- Evidence: [agent loop](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/loop.py), [subagent implementation](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/subagents.py), [manifest](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/manifest.py), [CLI and shipped modes](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: Source-level review; no live provider invocation was reproduced by this assessment.

## S2 — Coordination

- State: —
- Function: No function-specific inter-S1 conflict attenuation mechanism identified.
- Disturbance / variety regulated: Potential conflict between simultaneously active agent children or tool results.
- Decisive decision or feedback right: No separate allocation/conflict-policy right beyond the parent's ordinary task choices.
- Decision owner: No qualifying S2 owner evidenced.
- Supporting / enforcement mechanisms: Child-run budgets/depth and parent approval, structured parent-child event identities, opt-in bounded parallel tool execution.
- Closure path: Child results return to parent S1; no observed cross-unit interference signal → coordinating correction → changed unit behavior loop.
- Why this is / is not agent-owned: Delegation topology, approval inheritance and thread-pool concurrency do not themselves constitute regulation of interference among viable S1 units.
- Evidence: [subagents](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/subagents.py), [parallel tool path](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/loop.py), [v0.6 milestone](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/docs/milestones.md).
- Basis: structural.
- Confidence: medium.
- Caveats: A specific third-party composition might impose work isolation, but no first-party distributed conflict closure is credited here.

### Absence scope

- Surfaces inspected: Child manifest/dispatch, shared event log, approval inheritance, thread-pool path and milestone contracts.
- Plausible first-party paths checked: Multiple child runs, budget/depth limits, sibling tasks, parallel tools and parent aggregation.
- Why no material first-party path remains: Implemented paths return individual tool/child results without a distinct cross-S1 interference witness and coordinating policy feedback.

## S3 — Inside-and-now control

- State: —
- Function: No distinct whole-system current supervisory loop established.
- Disturbance / variety regulated: Potential aggregate capacity, performance or policy breaches across task units.
- Decisive decision or feedback right: No supervisor with whole-system operating discretion; humans approve individual side-effecting calls.
- Decision owner: No qualifying S3 decision owner.
- Supporting / enforcement mechanisms: Deterministic guardrail hooks, approvals, per-agent budgets, events, tracing and read-only run viewer.
- Closure path: Guardrail denial/approval constrains a tool call, not an aggregate S3 observation → parent command → operating-unit adjustment cycle.
- Why this is / is not agent-owned: Per-tool gating, budget checks and logging are S1 support and safety enforcement rather than a separately owned current-management function.
- Evidence: [loop and controls](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/loop.py), [approvals](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/approvals.py), [read-only service](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: The human handoff is an operational exception path, not by itself evidence of a VSM S3 authority cycle.

### Absence scope

- Surfaces inspected: Loop budgets, guardrail and approval hooks, run logging, observability exporters, event viewer and CLI.
- Plausible first-party paths checked: `escalate_to_human`, approval policy, readonly dashboards, limits and emitted run metrics.
- Why no material first-party path remains: No first-party manager evaluates overall operating performance and returns prioritization or resource correction across units.

## S3* — Complementary audit

- State: —
- Function: No shipped operational independent audit-and-return loop identified.
- Disturbance / variety regulated: Potential divergence between an agent's output claims and execution reality.
- Decisive decision or feedback right: No separate runtime audit verdict with remediation authority.
- Decision owner: No qualifying independent auditor at the assessed boundary.
- Supporting / enforcement mechanisms: Event-log golden-case `harness eval`, deterministic guardrail checks, offline calibration and traces.
- Closure path: Eval reads recorded or newly produced test events for developer-facing pass/fail; no independent operational audit finding is returned for agent correction and re-review.
- Why this is / is not agent-owned: Event-log predicates are valuable external verification, but are a test runner with scripted expectations, not a complementary independent reviewer participating in runtime correction.
- Evidence: [eval runner](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/eval.py), [decision calibration](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/decide/calibrate.py), [milestones](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/docs/milestones.md).
- Basis: structural.
- Confidence: high.
- Caveats: Do not conflate deterministic safety enforcement or release qualification with a deployed S3* auditor.

### Absence scope

- Surfaces inspected: Event log, golden eval suite and CLI, calibrated decision adapters, guardrail implementations and observability.
- Plausible first-party paths checked: Log invariants, scripted test verdicts, prompt-injection flag, policy-commitment denial and model calibration.
- Why no material first-party path remains: Checks do not supply an independent operational reality-access/decision owner with findings-to-author corrective feedback.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective environment-to-capability adaptation cycle established.
- Disturbance / variety regulated: Long-term mismatch between external demand and future agent capabilities.
- Decisive decision or feedback right: No agent-owned adaptation program, option selection or return into deployed capability.
- Decision owner: No qualifying S4 owner; operators choose models, manifests and plugin installations.
- Supporting / enforcement mechanisms: Model gateway switching, retrieval, capability registry and offline decision-model calibration.
- Closure path: Configuration changes are made externally; the running agent does not select a prospective adaptation option and put it back into service.
- Why this is / is not agent-owned: Extensible protocols, calibration scores and memory/retrieval support current work or developer decisions, not separately owned future-oriented strategic adaptation.
- Evidence: [registry](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/registry.py), [manifest](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/manifest.py), [calibration](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/decide/calibrate.py).
- Basis: structural.
- Confidence: high.
- Caveats: A separately authored self-modification tool could change the boundary; this assessment does not assume one.

### Absence scope

- Surfaces inspected: Plugin registration, retrieval, model profiles, skills, offline calibration and docs.
- Plausible first-party paths checked: Dynamic tool discovery, swapping model endpoints, calibrating decision adapters and user-installed capabilities.
- Why no material first-party path remains: The available adaptation switches are configuration/developer choices without an external-prospective agent option and returned capability change loop.

## S5 — Policy and identity

- State: —
- Function: No operative ultimate-policy/identity arbitration path identified.
- Disturbance / variety regulated: Potential conflict over legitimacy of agent identity, authority and scope.
- Decisive decision or feedback right: No first-party authority for a governing identity dispute beyond operator-assigned manifest and runtime permission rules.
- Decision owner: Operator sets the manifest; there is no qualifying deployed S5 process.
- Supporting / enforcement mechanisms: System prompt, manifest validation, approval policy, budget and hard-coded guardrails.
- Closure path: Static policy/configuration constrains individual runs; no disputed ultimate-purpose question is escalated, decided and returned as governing policy.
- Why this is / is not agent-owned: Tool approval, human escalation and release maintainers are not S5 by themselves.
- Evidence: [manifest configuration](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/manifest.py), [approvals](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/approvals.py), [loop](https://github.com/glaborie/rigging/blob/7b04ad9064a655d74a2c0566ac25c9bd7444df12/rigging/loop.py).
- Basis: structural.
- Confidence: high.
- Caveats: External customer policy and the open-source governance are not imported as the deployed agent's ultimate-policy owner.

### Absence scope

- Surfaces inspected: Manifest, approval gates, handoff mechanism, safety checks and published governance docs.
- Plausible first-party paths checked: Human approval, policy prompts, deny/transform hooks, budget envelope and release decisions.
- Why no material first-party path remains: The reviewed distribution does not establish an identity/authority dispute, a legitimate final decider and a binding return to agent behavior.

## Distributed OSS parent arrangement

Repository maintainers govern the package's source and releases. They do not operate a deployed cross-installation S3/S4/S5 controller through the reviewed first-party code.

## Self-hosted and non-human modes

Local Ollama or remote model endpoints are ordinary provider transports. MCP tools and registry extensions can be third-party supplied; their internal decision loops are not credited. Scripted approvals in eval are not evidence of autonomous real-world permissions.

## Recursion

Optional child-run dispatch creates bounded subordinate operational units, but a separate S2–S5 organization governing their interactions is not shown. The shared session/log identity is a provenance mechanism rather than independently viable recursion.

## Variety and escalation

Budget exhaustion, denied tools and errors are surfaced to the active agent. A human escalation tool returns control outside the autonomous task loop; it does not establish S3 or S5 solely by existing.

## Evidence gaps

No live model execution or hosted service deployment was exercised here; evidence is frozen first-party source plus README/milestone contracts. The current v0.6 milestone source contradicts the older README capability matrix presentation, so implemented source reachability was inspected explicitly. No independent auditor or organizational parent is claimed from tests or tooling alone.
