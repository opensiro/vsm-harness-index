---
harness_id: reachai-enterpriseagentframework
project_name: ReachAI / EnterpriseAgentFramework
repository: https://github.com/w8123/EnterpriseAgentFramework
review_ref: 44bc68d3670709b4b6ab490af8a699f8934aab38
reviewed_at: 2026-10-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: —
---

# ReachAI / EnterpriseAgentFramework

## Review boundary

- System in focus: First-party installed ReachAI enterprise agent-runtime application, comprising its Runtime AgentScope Supervisor, published Agent configurations, pinned Workflow-as-Tool GraphSpec execution, business capability access and policy/approval/trace feedback. Control-service candidate generation, packaged RunOps/EvalOps and runtime operator interfaces are inspected as optional first-party modes, not assumed active inside every conversation.
- Purpose and identity: Let enterprise users request work in existing Java business systems via selected authenticated capability/workflow/page operations; enable safe business actions with observable runtime decisions and controlled published agent/workflow configurations.
- Relevant environment: User/tenant/project business messages and policy, external LLM and AgentScope library, registered enterprise API capabilities, workflow results and errors, model changes, traces and candidate publication decisions.
- Standard-distribution boundary: Shipped runtime/control service source and standard documented deployment; model endpoints, third-party AI coding executors (Codex/Cursor/etc.), enterprise target application API and organizational approval decisions are separate dependencies. Operator-triggered candidate/evaluation modes are distinct from live execution; build-time repository CI and demos do not count as production owners.
- Credited operating / distribution surfaces: [enter](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/RuntimeAgentExecutionService.java#L515), [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L185), [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L243), [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L1841), [policy](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/SupervisorToolPolicyService.java#L83), [graph](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/execution/RuntimeGraphSpecExecutor.java#L113), [context](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/agent/RuntimeAgentExecutionContextResolver.java), together with bundled RunOps, EvalOps and trace-to-draft control workflows only where reachable.
- Adjacent first-party surfaces excluded from ownership: Test suites, product/docs claims without wiring, maintainer development CI, user-company governance external to ReachAI, AI Coding executor internal behavior, and independent third-party APIs/models. The RunOps trace-to-draft subsystem is first-party but intentionally segregated from automatic live Agent publication [provider](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-control-service/src/main/java/com/enterprise/ai/control/runops/TraceWorkflowCandidateTaskProvider.java#L34).
- First-party operating / deployment modes considered: Published normal AgentScope ReAct agent with configured model, workflow tool allowlist, managed/A2A delegation, read-only parallel option, business identity and one-time tool approval; immutable GraphSpec runtime; optional operator-triggered EvalOps and RunOps trace candidate authoring, AI Coding artifact acceptance and separate workflow/config publishing.
- Recursion level: One deployed ReachAI application containing subordinate specialist/Workflow-as-Tool operational cells; multiple clients/projects/remote A2A or nested supervisor tools are not silently promoted to another independent VSM recursion.
- Reviewed revision: `44bc68d3670709b4b6ab490af8a699f8934aab38` frozen by #202 and active batch #1669, not latest upstream head.
- Observation date: 2026-10-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

A request resolves an installed Agent's ACTIVE configuration snapshot and pinned Workflow-as-Tool bindings, then invokes the first-party Supervisor adapter. The adapter constructs AgentScope's model-backed ReActAgent and toolset, supports model-directed plan/next tool, calls first-party GraphSpec execution, returns policy/tool outcomes, and emits run/trace records. Human confirmation is required for specified risks; business and provider systems remain external. Sources: [enter](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/RuntimeAgentExecutionService.java#L552), [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L185), [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L243), [policy](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/SupervisorToolPolicyService.java#L83), [graph](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/execution/RuntimeGraphSpecExecutor.java#L113).

RunOps records traces/guard decisions and offers comparisons/diagnostics. EvalOps runs separately selected datasets against frozen baseline/candidate Agent versions and returns a deterministic gate result. A separate operator-triggered control-service pathway filters a successful, bounded **read-only** production trace; external AI Coding constructs a draft GraphSpec and first-party validation makes it a DRAFT with `publishRequired=true`, `published=false`. This provider explicitly does not perform publication or Agent attachment, which has a distinct privileged configuration version publisher. Sources: [ops](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/runops/RuntimeRunOpsQueryService.java#L54), [eval](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/eval/RuntimeEvalExperimentService.java#L271), [eval](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/eval/RuntimeEvalExperimentService.java#L406), [eligible](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-control-service/src/main/java/com/enterprise/ai/control/runops/TraceWorkflowCandidateEligibility.java#L46), [provider](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-control-service/src/main/java/com/enterprise/ai/control/runops/TraceWorkflowCandidateTaskProvider.java#L34), [provider](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-control-service/src/main/java/com/enterprise/ai/control/runops/TraceWorkflowCandidateTaskProvider.java#L280), [provider](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-control-service/src/main/java/com/enterprise/ai/control/runops/TraceWorkflowCandidateTaskProvider.java#L365), [attach](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/agent/RuntimeAgentConfigService.java#L247).

## Operational model

The principal S1 is a configured model-driven enterprise task agent invoking an approved set of workflow and other first-party tools. A workflow GraphSpec executes reproducible deterministic steps and preserves identity/interaction state; external business operations are called using narrowly scoped authority. Model chooses task-level next action, while first-party enforcement limits it. Trace comparison, candidate generation, manual publication, agent configuration and per-run approval are different rights and should not be collapsed into a single autonomous controlling agent.

## S1 — Operations

- State: A
- Function: Deliver enterprise-user outcomes through model-directed planning, selection of authorized Workflow-as-Tool and iterative response to actual tool/environment feedback.
- Disturbance / variety regulated: Variable user intent, external business-service results/errors, workflow outcomes, permission refusal and unanticipated needs for replan.
- Decisive decision or feedback right: The configured model-backed Supervisor chooses plan, eligible tool calls or revised path using returned ToolResultBlock / observation.
- Decision owner: Configured AgentScope ReAct model actor within the first-party assembled ReachAI Supervisor, not the external inference provider organization; deterministic GraphSpec executor and policy are supporting mechanisms.
- Supporting / enforcement mechanisms: Published immutable Agent/Workflow snapshots, tool allowlist, identity resolution, policy guard, human one-time approval, GraphSpec kernel, trace/state and workflow conversation memory.
- Closure path: User request → first-party Active Agent snapshot → ReAct plan/tool choice → first-party policy allow/confirm/deny → pinned GraphSpec workflow or approved external capability → tool result/error returned to ReAct → continuing plan/replan or final answer/trace.
- Boundary reachability: Ordinary RuntimeAgentExecutionService.executeResolvedContext invokes SupervisorRuntimeAdapter; the shipped AgentScopeSupervisorRuntimeAdapter builds ReActAgent/Toolkit and executes workflow tools through actual policy and GraphSpec. No example-only agent or unrelated provider internals are credited.
- Why this is / is not agent-owned: Model-selected plan and tool decisions respond to runtime observations; declarative steps and hard permission enforcement are not autonomous decisions.
- Evidence: [enter](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/RuntimeAgentExecutionService.java#L552); [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L185); [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L243); [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L276); [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L1841); [policy](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/SupervisorToolPolicyService.java#L83); [graph](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/execution/RuntimeGraphSpecExecutor.java#L113).
- Basis: Explicit first-party source control flow.
- Confidence: High for reachable supported source path, not an executed live business/LLM test.
- Caveats: Real effects require configured model, enterprise integrations and published tools; no claim about model quality or externally hosted applications.

## S2 — Coordination

- State: —
- Function: No shipped S2-specific inter-independent-S1 interference attenuation and returned mutual adjustment was established at this app recursion.
- Disturbance / variety regulated: Potential concurrent reads, duplicate side effects, tool collisions and different worker/workflow demands; reviewed gates regulate one execution plan and unsafe task operations rather than opposing independent S1 goals.
- Decisive decision or feedback right: The configured Supervisor decides which planned Workflow tool to invoke; deterministic reservations and read-only parallel flag enforce task safety but do not choose a dynamic response to inter-S1 oscillation.
- Decision owner: Task-local model actor, runtime admission/policy gates and user confirmation; no distinct verified S2-specific adjustment owner.
- Supporting / enforcement mechanisms: Toolkit parallel-read-only configuration, single-run planning reservations, duplicate workflow-call prevention, risk permissions and workflow state.
- Closure path: Per-run planned calls reserve/execute or fail; there is no demonstrated identification of a concrete clash of independent operating S1 units followed by attenuation and returned change of their behavior.
- Why this is / is not agent-owned: Parallel-read-only restrictions and routing are safety constraints/task scheduling, not evidenced inter-unit coordination decisions.
- Evidence: [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L207); [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L243); [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L1841); [policy](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/SupervisorToolPolicyService.java#L83).
- Basis: Explicit per-execution constraints and examined app-level boundary, bounded negative.
- Confidence: Medium-high in installed first-party standard paths.
- Caveats: A deployment can compose a multi-workstream coordinator externally; no such S2 loop may be borrowed.

### Absence scope

- Surfaces inspected: Supervisor toolset, per-run plan reservations, Workflow GraphSpec execution, Guard policy, Agent configuration, RunOps and automation entries.
- Plausible first-party paths checked: Read-only parallel flag, workflow-tool reservation/duplicate blocking, workflow plan handoff, fixed policy and remote-agent delegation.
- Why no material first-party path remains: Those paths sequence/protect individual execution and permissions, not identify a specified disturbance between autonomous operating cells and close conflict-sensitive mutual adjustments at system level.

## S3 — Inside-and-now control

- State: —
- Function: No established cross-operational current-control decision loop, despite administrative monitoring, workflow runtime and agent controls.
- Disturbance / variety regulated: Concurrent business projects, agent workloads and runtime failures could compete for shared commitments/capacity, but examined native surfaces operate per Agent/run or summarize them without a single governing cross-workload decision-return owner.
- Decisive decision or feedback right: Current Supervisor selects tools and replans one user task; administrator may publish/change Agent config; neither source path ties whole-current RunOps aggregate view to a direct resource/commitment/priority bargaining judgment affecting multiple S1 units.
- Decision owner: Task model, deterministic guard/execution services and external administrator; no demonstrated first-party whole-current S3 right or parent-governed returned decision at this recursion.
- Supporting / enforcement mechanisms: RunOps diagnostics and trace views, automation target execution, fixed published version/configuration, ACL and per-task planner.
- Closure path: RunOps provides operating records and administrators can separately modify configuration; missing witnessed loop is cross-S1 current situation → resource/commitment arbitration → binding returned interventions into S1.
- Why this is / is not agent-owned: The word Supervisor, dashboards and publish APIs do not establish whole-organization current-control judgment; static caps and monitoring are separate from ownership.
- Evidence: [ops](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/runops/RuntimeRunOpsQueryService.java#L88); [ops](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/runops/RuntimeRunOpsQueryService.java#L187); [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L185); [attach](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/agent/RuntimeAgentConfigService.java#L172); [enter](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/RuntimeAgentExecutionService.java#L552).
- Basis: Inspected active operating paths and distinct administrative APIs, bounded negative.
- Confidence: Medium; operator deployment can layer S3 but no app-owned integrated whole-current loop established.
- Caveats: Does not claim that humans running an enterprise deployment cannot provide actual S3 outside the packaged runtime.

### Absence scope

- Surfaces inspected: Runtime Supervisor, RunOps recent/diagnostic/comparison queries, Agent configuration/publish service, automation and execution policy.
- Plausible first-party paths checked: RunOps whole-project visibility → prioritized resource/current-commitment decision; Agent config changes; tool caps; multi-workflow dispatch; scheduled automation.
- Why no material first-party path remains: Present code has operating dashboards plus per-Agent config/execution decisions, but lacks an evidenced S3-specific whole-current allocative adjudication and returned intervention loop for distinct S1 units at declared application recursion.

## S3* — Complementary audit

- State: ?
- Function: Plausible but unresolved independent complementary challenge of operating claims via first-party RunOps and separately chosen EvalOps datasets.
- Disturbance / variety regulated: Unreliable agent/workflow success claims, regression and unexpected guard/side-effect conditions.
- Decisive decision or feedback right: EvalOps worker separately evaluates frozen Agent/version candidates against versioned datasets, scores and stores gate pass/fail; whether this independently audits ordinary operating evidence and returns an actionable finding into current-control/report correction is not established.
- Decision owner: External selected evaluation dataset/test designer and deterministic EvalOps evaluator/gate; no evidenced S3*-specific independent model/controller judgment with corrective operating return.
- Supporting / enforcement mechanisms: RunOps per-run trace/guard facts; experiment baseline/candidate snapshots, dataset items, deterministic judge, persisted results and gateStatus.
- Closure path: Selected eval experiment → isolated evaluation tasks → deterministic scoring/regression gate result; identified missing/unclear link is audit finding that amends or withholds ordinary S1–S3 operating claims and changes live control.
- Why this is / is not agent-owned: An independent comparison and a gate status are real, but the current evidence does not show ownership and corrective return required for S3*. Neither assert positive nor erase this material shipped candidate with a definitive absence grade.
- Evidence: [ops](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/runops/RuntimeRunOpsQueryService.java#L54); [ops](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/runops/RuntimeRunOpsQueryService.java#L175); [evalrun](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/eval/RuntimeEvalTaskWorker.java#L53); [eval](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/eval/RuntimeEvalExperimentService.java#L271); [eval](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/eval/RuntimeEvalExperimentService.java#L406); [policy](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/SupervisorToolPolicyService.java#L83).
- Basis: Explicit installed independent evaluation facility and separate gate output; missing function-specific corrective-return evidence.
- Confidence: Low for S3* classification; moderate for real evaluator path.
- Caveats: Unknown whether an additional product-owned publish/feedback consumer ties a FAILED gate to accountable corrective control. Do not confuse routine permission Guard with independent audit.

## S4 — Outside-and-then intelligence

- State: ?
- Function: A specific prospective capability-adaptation candidate exists, but its selection, parent authority and effective return into installed operation are not yet fully reconstructed.
- Disturbance / variety regulated: Changing enterprise work patterns, successful production routes not yet exposed as reusable Workflow capability, future provider/workflow quality.
- Decisive decision or feedback right: A selected successful RunOps trace can trigger AI Coding draft generation and source-checked read-only GraphSpec validation; legitimate developer/operator separately accepts, publishes and attaches; unclear whether this is one supported function-specific adaptation decision loop or merely independently operable artifacts.
- Decision owner: Operator initiates trace candidate; external AI Coding worker proposes; first-party services validate/store DRAFT; operator/administrator explicitly chooses publication, with publishedBy recorded. Neither an internally autonomous S4 nor integrated first-party parent-mode completion is yet proven.
- Supporting / enforcement mechanisms: RunOps Trace fields, strict trace candidate eligibility, source workflow pin, AI Coding task/artifact acceptance, Runtime DRAFT and validation, AgentConfig publish and tool version pin.
- Closure path: A particular successful production trace → eligibility filter → human-created AI Coding task → AI-generated validated DRAFT with published=false → [separate human review/replay/publication and Agent attachment] → new ACTIVE Agent config and subsequent selected Workflow; the bracketed bridge must be evidenced as one function-specific authority-return path before positive grading.
- Why this is / is not agent-owned: Only a proposed option is model-assisted; one path intentionally stops at DRAFT and never autonomously publishes. Presence of a separate publish API is not automatically evidence of completed S4 adaptation.
- Evidence: [eligible](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-control-service/src/main/java/com/enterprise/ai/control/runops/TraceWorkflowCandidateEligibility.java#L46); [candidate](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-control-service/src/main/java/com/enterprise/ai/control/runops/TraceWorkflowCandidateApplicationService.java#L40); [provider](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-control-service/src/main/java/com/enterprise/ai/control/runops/TraceWorkflowCandidateTaskProvider.java#L34); [provider](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-control-service/src/main/java/com/enterprise/ai/control/runops/TraceWorkflowCandidateTaskProvider.java#L280); [provider](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-control-service/src/main/java/com/enterprise/ai/control/runops/TraceWorkflowCandidateTaskProvider.java#L365); [draft](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/workflow/RuntimeTraceWorkflowCandidateDraftService.java#L29); [attach](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/agent/RuntimeAgentConfigService.java#L172); [attach](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/agent/RuntimeAgentConfigService.java#L247); [enter](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/RuntimeAgentExecutionService.java#L552).
- Basis: Explicit first-party source supports real prospective candidate construction; the decisive parent-return boundary is unresolved.
- Confidence: Moderate for draft option path, low for S4 closure.
- Caveats: Do not call this proven S4=A/C/P without checking whether the operator publication/attachment chain actually forms a coherent first-party future-capability feedback relationship.

## S5 — Policy and identity

- State: —
- Function: No function-specific legitimate ultimate-purpose/identity governance loop proven inside the packaged ReachAI runtime despite extensive access control.
- Disturbance / variety regulated: Business permissions, tool risk, project/tenant identity and approval boundaries; these are operational trust/risk decisions, not an evidenced ultimate organizational ethos dispute.
- Decisive decision or feedback right: Static policy profile, verified business identity and one-time per-tool approval constrain runtime acts; operator can publish Agent configuration. These do not identify or settle an ultimate system-identity purpose conflict via authoritative returned policy.
- Decision owner: Application administrator and trusted business principal for configuration/approval; deterministic risk Guard enforces inherited policy.
- Supporting / enforcement mechanisms: Tool ACL, project/tenant scope, READ/WRITE/IRREVERSIBLE risk modes, approval sessions, configuration publish and traces.
- Closure path: Trusted identity → Guard allow/deny/confirm → operation or paused task returns; no separate ultimate-identity issue → legitimate S5 adjudication → accepted policy → governing subsequent operation chain established.
- Why this is / is not agent-owned: Neither an autonomous ReAct planning choice nor a human confirming a WRITE tool owns ultimate organizational identity.
- Evidence: [policy](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/SupervisorToolPolicyService.java#L83); [policy](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/SupervisorToolPolicyService.java#L151); [attach](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/agent/RuntimeAgentConfigService.java#L247); [agent](https://github.com/w8123/EnterpriseAgentFramework/blob/44bc68d3670709b4b6ab490af8a699f8934aab38/reachai-runtime-service/src/main/java/com/enterprise/ai/runtime/supervisor/AgentScopeSupervisorRuntimeAdapter.java#L1841).
- Basis: Explicit operational policy and authority-partition review; bounded negative for first-party S5.
- Confidence: Medium-high for application-boundary conclusion.
- Caveats: Business institution/user may provide upstream human-owned S5 outside the first-party harness; OSS maintainers are another separate organization.

### Absence scope

- Surfaces inspected: Tool policy and confirmation, identity validation, published Agent/workflow configuration, operator interfaces and trace/guard reporting.
- Plausible first-party paths checked: Guard policy selection/approval, live administrator configuration, per-tool risk-mode escalation and model-selected tool availability.
- Why no material first-party path remains: These are bounded business execution governance and access authorization. No shipped function-specific mechanism establishes an ultimate-purpose/identity judgment and returned application-wide authoritative resolution.

## Distributed OSS parent arrangement

ReachAI product operators, users, separate third-party AI Coding tools and repository maintainers are not one jointly evidenced governance organization. The explicit draft-review/publish/attach interfaces warrant investigation of a possible bounded parent S4 mode, not an automatic `P` grade. Actual institutional parent decision rights and returned closure need to be reconstructed under the deployed product scope.

## Self-hosted and non-human modes

Normal self-hosted config can support model-directed S1 and explicitly supervised tool confirmation. External models, user authority over a single business write, and internal CI are not imported as autonomous metasystem. No production run/benchmark is attested; source inspection supports only the declared modes.

## Recursion

An AgentScope ReAct supervisor plus published GraphSpec tasks and remote A2A binding comprise one first-party application boundary. Agent/tool plurality and nested workflows do not automatically establish viable recursive organizational levels.

## Variety and escalation

Policy enforcement, approvals, replan on denied actions, per-run traces and fixed version pinning reduce operational risk. EvalOps and trace-to-draft expose possible prospective/audit input but are not yet shown to close all metasystem decision rights. For unresolved S3*/S4 retained `?` is preferable to classifying an unproven positive or claiming universal absence.

## Evidence gaps

- **S3*:** Confirm whether stored EvalOps FAILED gates ever stop an actual live Agent/Workflow publish, amend an operating report or trigger independently controlled corrective S3 action. The reviewed `gateStatus` producer shows stored gate results, but no exact consumer/return owner was proved.
- **S4:** Reconstruct the legitimate operator selection path from a source trace-generated DRAFT (explicitly not auto-published) through replay/evaluation, published Workflow, Agent attachment/ACTIVE config and subsequent task execution; distinguish mere independently callable administration APIs from function-specific closed parent adaptation.
- This is a source-based pinned-code review; no enterprise system, real external AI Coding executor, Java integration runtime, MySQL deployment or model inference was exercised. Absence statements are scoped to inspected standard first-party paths and must not be read as impossibility for custom adopters.
