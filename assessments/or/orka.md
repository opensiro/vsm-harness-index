---
harness_id: orka
project_name: Orka
repository: https://github.com/orka-agents/orka
review_ref: 7cffe130efa74f505d66dce561ade6c18901ba6e
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Orka

## Review boundary

- System in focus: a deployed Orka Kubernetes agent-task installation with an enabled model-driven coordinator and, as a separate supported mode, a RepositoryMonitor with a configured reviewer Agent.
- Purpose and identity: execute configured AI, coding and container Tasks in isolated pods; accept current user/project work, coordinate specialist work, and return task/review/repair decisions and durable records.
- Relevant environment: user requests, model/tool/provider responses, Kubernetes pod health, code repositories, GitHub PR heads, validation/CI failures, changing child-task outcomes, namespace/credential limits.
- Standard-distribution boundary: Orka API/chat orchestrator, in-cluster AI workers, Agent/Task/Session CRDs, coordinator delegation and messaging tools, Task/RepositoryMonitor controllers, reviewer result store and documented optional repair/readiness flow.
- Credited operating / distribution surfaces: `internal/api/chat.go`, `chat_system_prompt.go`, `chat_tool_executor.go`; `internal/tools/delegate_task.go`, `wait_for_tasks.go`, `cancel_task.go`, `send_message.go`, `check_messages.go`; `internal/controller/repositorymonitor_*.go`, `workers/general/main.go`, and the packaged CRD/runtime gateway.
- Adjacent first-party surfaces excluded from ownership: demo blueprints, Helm rendering and Kubernetes resource reconciliation without semantic model decisions, provider proxy, test fixtures, contribution/release governance. External Codex/Claude Code/OpenCode/Copilot reasoning loops are not donated; Orka's configured orchestration and oversight contracts are in scope.
- Modes considered: direct AI Task, externally hosted coding runtime, self-bootstrapping model-driven coordinator, explicit sibling messaging/racing, read-only repository review with optional validation, bounded repair and optional automerge, scheduled and webhook review; not every mode is a default installation setting.
- Recursion level: one user/project agent-task organization inside a deployed Orka namespace, with subordinate specialist Tasks; cluster platform administration and independent repository governance remain adjacent.
- Reviewed revision: `orka-agents/orka@7cffe130efa74f505d66dce561ade6c18901ba6e`, GitHub repository ID 1150204028, frozen batch #2501 / controller #2502 row 2.
- Observation date: 2026-10-31; Profile 0.2.4 and released Methodology 0.3.7; source/static review, not live Kubernetes/provider E2E.

## Repository architecture

The pinned [README](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/README.md) documents `Task` execution in pods, provider/tool-backed in-cluster AI Tasks and external coding-agent runtimes. The [chat coordinator instructions](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/api/chat_system_prompt.go) select actual create/delegate/wait/repair tools, not just display prose; the [chat executor](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/api/chat_tool_executor.go) binds tool invocations to authorized Kubernetes tasks and a scoped session. Separate [RepositoryMonitor guidance](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/website/docs/guides/repository-monitors.md), [reconciler](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/controller/repositorymonitor_controller.go), [review ingestion](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/controller/repositorymonitor_review_ingest.go) and [repair path](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/controller/repositorymonitor_repair.go) show distinct exact-head read-only reviewer jobs and return of verdict/readiness/repair state to the PR workflow. Orka labels the platform experimental; there is no claim of production maturity or observed run success.

## Operational model

An Orka coordinator is a model-driven decision actor operating over first-party create, delegate, wait, cancel and messaging tools. Specialists execute model/tool turns as subordinate S1 cells. The Kubernetes controller owns deterministic constraints, not their semantic judgments. RepositoryMonitor is a separate packaged complementary oversight mode: it dispatches a distinct reviewer on pinned PR evidence, validates its structured verdict and can block readiness or arrange bounded repair/validation; human or explicitly configured automerge retains merge authority. Scoping one coordinated mission avoids attributing installation-wide governance to a chat prompt.

## S1 — Operations

- State: A
- Function: carry out user-directed AI tasks, generate code/reviews and use first-party registered tools to produce work artifacts.
- Disturbance / variety regulated: heterogeneous prompts, code/test state, model/tool results, errors and task-specific context.
- Decisive decision or feedback right: an instantiated AI worker or coordinator chooses content-bearing tool calls and task actions based on returned observations.
- Decision owner: Orka-instantiated model-driven AI Task/coordinator; external coding CLIs keep their own lower-level agent loops and are not the sole witness.
- Supporting / enforcement mechanisms: Kubernetes Task CRD, pod lifecycle, credentials, workspace, provider proxy, RBAC, task timeout and durable result store.
- Closure path: user/Task prompt → worker/model decision → tool or delegated action → pod/run result → subsequent model decision or returned artifact.
- Boundary reachability: README's in-cluster `type: ai`, chat request handling and registered create/execute tools are supported paths, not only demos.
- Why this is / is not agent-owned: model-driven selection resolves task content; fixed pod orchestration and auth do not substitute for S1 discretion.
- Evidence: [README](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/README.md); [chat.go](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/api/chat.go); [chat_tool_executor.go](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/api/chat_tool_executor.go); [general worker](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/workers/general/main.go).
- Basis: structural
- Confidence: medium
- Caveats: no live provider/cluster trace was executed.

## S2 — Coordination

- State: C
- Function: attenuate interference among sibling specialist Tasks for a configured coordinator mission, including redundant race candidates and result-dependent message handoffs.
- Distinct S1 units: separately instantiated coder, reviewer, tester or peer Tasks under one coordinator/transaction, each capable of independently performing work.
- Inter-S1 disturbance: redundant simultaneously running alternatives consuming capacity, stale handoffs and sibling actions on incompatible intermediate results.
- Attenuating coordination relation: the coordinator may select the first useful race result and cancel other running siblings; configured send/check message and explicit dependency handoff give sibling work a shared decision route instead of independent conflicting continuation.
- Feedback into subsequent S1 behaviour: `wait_for_tasks` returns terminal child status/retry metadata, `cancel_task` stops no-longer-useful work and `check_messages` changes a receiver's next step.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the witness is a selected collision/duplication-interference pattern with returned control into separately executing S1s, not generic parallelism or sequential tool calls.
- Disturbance / variety regulated: race/redundancy and incoherent sibling outcomes.
- Decisive decision or feedback right: decide which running child to retain or stop and when an intermediate handoff is safe.
- Decision owner: model-driven coordinator only when a coordination-enabled Agent and corresponding task patterns are configured; primitives supply the constructor but no global automatic S2 is assumed.
- Supporting / enforcement mechanisms: child identity, scoped task authorization, cancellation API, durable messaging and structured terminal waits.
- Closure path: concurrent child observations → coordinator judgment about winner/dependency → cancel/message/wait invocation → sibling next behavior/terminal status.
- Boundary reachability: coordinated execution and control are shipped as tools, not only example YAML; a configured coordinator can call them via the first-party session.
- Why this is / is not agent-owned: an agent can make the interference choice in the composed race mode; generic messenger/Task storage alone do not supply a mandatory organization-wide coordinator, hence `C` rather than `A`.
- Evidence: [coordination section](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/api/chat_system_prompt.go), registered [delegate](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/tools/delegate_task.go), [wait](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/tools/wait_for_tasks.go), [cancel](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/tools/cancel_task.go) and [messages](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/tools/send_message.go).
- Basis: structural
- Confidence: medium-low
- Caveats: race and dependency patterns are optional compositions, not a proved default arbitration loop for all peers.

## S3 — Inside-and-now control

- State: A
- Function: supervise the current delegated mission, its specialist task status and correction loop, rather than all independent Kubernetes namespaces.
- Whole-system current view: the configured coordinator observes the complete active mission's child-task status, rework, validation and review outcomes, not unaffiliated namespace workloads.
- Current-control decision scope: current mission task assignment, retry, rework, cancellation, blocked disposition and completion readiness under the original user's authority.
- Disturbance / variety regulated: failed specialist deliverables, validation/review failures, blocked Tasks and incomplete current mission steps.
- Decisive decision or feedback right: model-driven coordinator decides retry/rework/delegation/cancellation from returned child/evaluation feedback and decides when to finalize or report a blocked mission.
- Decision owner: configured coordinator agent; platform timeouts and allowlists remain subordinate enforcement.
- Supporting / enforcement mechanisms: `wait_for_tasks` terminal returns, validation and PR-CI tools, task/agent creation and update, task records, bounded retry budgets in product guidance.
- Closure path: mission plan → delegated work → wait/validate/review/CI feedback → coordinator correction/delegation → revised task outputs and terminal mission disposition.
- Boundary reachability: `create_agent` coordination and optional `initialPrompt` initiate a coordinator and subordinate task using the supported API, and the [shipped coding workflow guidance](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/api/chat_system_prompt.go) explicitly loops over failed validation/reviews before PR/CI closure.
- Why this is / is not agent-owned: the coordinator interprets heterogeneous current results and chooses corrections, not just fixed scheduling; no all-installation budget/policy S3 is claimed.
- Evidence: [chat_system_prompt.go](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/api/chat_system_prompt.go); [delegate_task.go](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/tools/delegate_task.go); [wait_for_tasks.go](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/tools/wait_for_tasks.go).
- Basis: structural
- Confidence: medium
- Caveats: enabled coordinator mission is the boundary; unrelated cluster workloads are outside its authority.

## S3* — Complementary audit

- State: A
- Function: independently challenge the working PR/task outcome against exact-head evidence, then make findings consequential for mission readiness and rework.
- Claim being audited: a coder's PR head satisfies acceptance, safety and correctness requirements and associated validation passed.
- Ordinary reporting path: coder/implementation Task produces changed files, a PR/commit and self-reported success.
- Complementary access path: separately configured read-only reviewer Agent receives exact PR head SHA plus bounded changed-file/patch context; the controller rejects stale or malformed verdicts and separately verifies required validation-task provenance.
- Independence boundary: dedicated reviewer Task/runtime and read-intent workspace are isolated from the implementation Task, forbidden from modifying the checkout or receiving write credentials. Reviewer model may be an external supported runtime, but Orka owns dispatch, evidence identity, ingestion and return.
- Who acts on findings: RepositoryMonitor records `needs_changes`/safety states as blocked readiness; coordinator or explicit `orka:fix`/`orka:fix-ci` repair tasks must produce a new exact-head receipt, reset stale review and re-review before readiness. Optional automerge enforces fresh review/CI and policy gates; merge never follows review text alone.
- Disturbance / variety regulated: optimistic self-report, untested diffs, stale review, hidden security/correctness defects, unsupported validation claims.
- Decisive decision or feedback right: reviewer provides an evidence-backed contrary verdict and the monitoring/workflow path can block advancement or require repair.
- Decision owner: distinct reviewer Agent for substantive critique; first-party controller for trustworthy exact-head admission and current readiness state.
- Supporting / enforcement mechanisms: read-only workspace, signed/scoped inventory, JSON verdict schema, versioned review records, CI and separate validation provenance, bounded repair jobs.
- Closure path: submitted PR → exact-head reviewer evidence → accepted verdict/blocked state → corrective agent task or human disposition → new head and re-review → readiness/merge policy.
- Boundary reachability: the packaged reviewer Agent and RepositoryMonitor CRD/controller are first-party runnable paths, not a bare example prompt.
- Why this is / is not agent-owned: the critique is a separate model-driven reviewer and its findings are returned through first-party readiness/repair feedback; deterministic SHA/CI checks enforce validity but do not generate the semantic review.
- Evidence: [RepositoryMonitor](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/website/docs/guides/repository-monitors.md), [controller](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/controller/repositorymonitor_controller.go), [review result ingestion](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/controller/repositorymonitor_review_ingest.go) and [repair](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/controller/repositorymonitor_repair.go).
- Basis: structural
- Confidence: medium
- Caveats: separately enabled RepositoryMonitor/reviewer mode, no live repository/API review run observed; configuration and human-controlled merge authority remain explicit.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct owner evidenced that interprets changing external prospects and selects longer-horizon adaptation of the Orka operating organization.
- Disturbance / variety regulated: model/provider changes, future project requirements and workflow evolution were checked as plausible paths.
- Decisive decision or feedback right: no source-backed right to convert trend/forecast/strategy intelligence into a revised ongoing mission capacity/plan, distinct from present PR repair.
- Decision owner: users/administrators preconfigure Agents, providers, schedules and policies; individual coding tasks may modify repositories but that is mission S1, not system-level S4.
- Supporting / enforcement mechanisms: scheduled monitors, task templates, runtime-policy config, CI and dashboards.
- Closure path: recurring current-state review and operational corrections are evidenced, but not future-looking intelligence → adaptation choice → changed S3 capability → later effectiveness feedback.
- Why this is / is not agent-owned: repeated runs, CI repair, model configuration and repository improvement do not alone prove a distinct prospective adaptation owner.
- Evidence: [README](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/README.md); [chat_system_prompt.go](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/api/chat_system_prompt.go); [RepositoryMonitor guidance](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/website/docs/guides/repository-monitors.md).
- Basis: structural
- Confidence: medium-low
- Caveats: bounded absence for inspected first-party standard modes, not an impossibility for customized workflows.

### Absence scope — S4

- Surfaces inspected: chat/coordinator decision prompts and tools, in-cluster task workers, scheduled monitors, exact-head review/repair, model/provider configuration and task histories.
- Plausible first-party paths checked: scheduled/security/dependency reviews, PR improvement, model/provider switching, workflow retry/CI repair and cluster policy updates.
- Why no material first-party path remains: these are configured repetition, bounded operational correction or user-authored setup; no autonomous prospective organizational strategy and feedback owner is established.

## S5 — Policy and identity

- State: —
- Function: no in-boundary unresolved ultimate-identity/policy adjudication and return process is evidenced.
- Disturbance / variety regulated: conflicting goals, namespace trust and provider/tool allowances were considered but are preselected operational constraints.
- Decisive decision or feedback right: none evidenced for an independent identity-policy authority beyond fixed platform administration and task-scoped approvals.
- Decision owner: cluster administrators and user/tenant policy configuration; automated admission/RBAC only enforce already chosen constraints.
- Supporting / enforcement mechanisms: Kubernetes RBAC/admission, namespace authorization, scoped context tokens and provider/model allowlists.
- Closure path: operator settings constrain later pods; no open organization identity-policy conflict → legitimate identity decision → authoritative return loop is shown.
- Why this is / is not agent-owned: project governance, role prompts, admission policy and security rules do not create a semantic S5 organ.
- Evidence: [README](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/README.md); [security documentation](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/website/docs/concepts/security.md); [ToolExecutor authorization](https://github.com/orka-agents/orka/blob/7cffe130efa74f505d66dce561ade6c18901ba6e/internal/api/chat_tool_executor.go).
- Basis: structural
- Confidence: medium-low
- Caveats: bounded absence at namespace/task organization boundary, not a judgment about the Microsoft-controlled upstream repository governance.

### Absence scope — S5

- Surfaces inspected: README/security guidance, Kubernetes and gateway authorization, controller policy boundaries, user-facing agent role prompting and repository contribution policy.
- Plausible first-party paths checked: role/system prompt, namespace policies, credentials, task approval, model/provider and automerge constraints, upstream foundation-donation plan.
- Why no material first-party path remains: in-cluster rules constrain delegated authority; project/foundation governance is external to the running installation; no dynamic ultimate-identity decision-and-return contract appears.

## Distributed OSS parent arrangement

Upstream maintainers and Microsoft/future foundation governance are not the running system's S5. The repository review mode may delegate merge to authorized humans; that is a consequential operational/PR gate, not automatic S5 or a standing S4 parent-adaptation mode.

## Self-hosted and non-human modes

Orka runs in a user's Kubernetes cluster with scoped namespace credentials. Configured coordinator/reviewer agents may decide autonomously within those scopes while provider proxy and Kubernetes enforcement remain deterministic. `RepositoryMonitor` mode and coordinator-enabled model behavior are not assumed on every deployment.

## Recursion

The parent is one coordinated mission/monitored repository task organization; child specialist Tasks are operational units. The cluster controller is infrastructure beneath/around them, not automatically an autonomous organizational S3/S5.

## Variety and escalation

Task timeouts, retries, terminal waits, read-only reviews, exact-head locks and readiness gates reduce operational variety. `needs_human`, validation blocked and security-sensitive results surface explicit escalation. A notification or GitHub gate alone is not an independent metasystem organ.

## Evidence gaps

Static code/design review only: no live Kubernetes/LLM, GitHub credential, model or external CLI E2E was run. The strongest S2 feedback is an optional composed coordinator race/dependency pattern; no claim of global automatic conflict arbitration. S3 is at mission scope, not the whole cluster. S3* is a supported distinct exact-head PR review path with configured reviewer, not an automatically enabled audit for every Task. Future S4 and identity S5 remain absent within the inspected standard boundary.
