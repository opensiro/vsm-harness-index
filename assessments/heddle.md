---
harness_id: heddle
project_name: Heddle
repository: https://github.com/roackb2/heddle
review_ref: 436eaac836512dac99520b91ae09b06212a658f4
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Heddle

## Review boundary

- System in focus: the first-party **Heddle TypeScript agent runtime**, conversation engine and shipped opt-in child delegation modes, including the packaged `@heddleagent/runtime` and first-party `@heddleagent/cli` coding host at frozen SHA `436eaac836512dac99520b91ae09b06212a658f4`.
- Purpose and identity: reusable model/tool conversation operation, stateful continuation and tool approvals, durable hosted runs and bounded delegation, without claiming customer product authority.
- Relevant environment: user goals, model completions and tool feedback, attached repo/workspace, host model/provider, custom skills, MCP tool endpoints, saved turns and approval decisions.
- Standard-distribution boundary: public runtime and coding-agent CLI with built-in model/tool loop; optional same-root `delegate_task` child agent loop in `createConversationEngine`. A *separate Execution Host* is an external deployment; a compatible host described as private research is not credited.
- Credited operating / distribution surfaces: `AgentRunService`, `AgentLoopRuntimeService`, `ConversationAgentService`, packaged CLI, live delegation scope/child runtime and approval/permission composition; hosted run lifecycle is operational support.
- Adjacent first-party surfaces excluded from ownership: CI, evals, demonstrations, docs-only roadmap, customer-host identity/authenticated database and retention systems, external hosted Execution Host product, separate model API organizational internals and custom agent code not activated in supported default.
- First-party operating / deployment modes considered: SDK runtime alone; standard CLI coding agent; ordinary multi-turn persisted conversation; opt-in delegation with builtin Ask/Review/Code children; approval-paused and hosted-run transport modes. The low-level delegation service is disabled by default, while conversation engine enables a scoped tool subject to explicit off controls.
- Recursion level: one bounded model/tool coding conversation as direct S1; a root conversation and several independently model-driven child loops at child-team recursion when delegation is allowed. Child actors do not recursively delegate; all action children share a workspace, and mutating ones execute serially.
- Reviewed revision: `436eaac836512dac99520b91ae09b06212a658f4`.
- Observation date: 2026-10-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [README.md](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/README.md) distinguishes the runtime package, embedded hosted-run facility, external Execution Host and CLI coding product. [src/core/agent/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/agent/service.ts) owns a first-party while-budget model/tool loop: request model response, dispatch tools and consume results, then request subsequent model response or finish. [src/core/runtime/loop/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/runtime/loop/service.ts) assembles the provider, tools and checkpoint/approval/event return; [src/sdk/conversation/headless/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/sdk/conversation/headless/service.ts) exposes persisted multi-turn requests, run ownership and cancellation. These are live packaged paths rather than source snippets for an external agent.

[src/core/delegation/README.md](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/delegation/README.md), [src/core/delegation/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/delegation/service.ts) and [src/core/delegation/child-runtime.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/delegation/child-runtime.ts) document and implement a model-visible `delegate_task` for independently looping Ask, Review and action-capable Code child profiles. `createConversationEngine` offers this by default subject to parent authority and turn disable; low-level SDK callers must opt in. Child registry has no further delegation. Distinct children have fresh context, per-child model adapter, status and bounded lifecycle records. They share one workspace; action children are serialized while read-only children can run concurrently, and root authority ceilings and approval policies apply.

[src/core/agent/tools/tool-turn-service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/agent/tools/tool-turn-service.ts) schedules and returns tool results for the single agent but concurrency of these tool calls is not evidence of multiple S1 units. [src/core/memory/maintainer.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/memory/maintainer.ts) and hosted run events are ordinary support/maintenance and should not be given autonomous S4 or independently governed S3* ownership merely by their names.

## Operational model

A model selects task-relevant actions from changing context; the first-party runtime dispatches tools, carries results into new model decisions and persists/checkpoints terminal outcomes. Optional delegated child loops can perform independent bounded tasks, reporting their outcome to the root. Deterministic authority/approval and serial-write constraints reduce interference but do not themselves choose a model-directed conflict resolution; the caller/parent chooses whether and how to delegate. Runtime does not own the customer application's ultimate identity or future strategic capability decisions.

## S1 — Operations

- State: A
- Function: perform model-directed coding/research/document operations through repeated observation/tool/action steps.
- Disturbance / variety regulated: user goals, files and tool responses, model/provider failures, approval pauses and contextual changes.
- Decisive decision or feedback right: choose new tool actions or completion using observations from prior executions.
- Decision owner: model-driven actor inside first-party `AgentRunService` and CLI/conversation runtime; hosted LLM computes tokens but does not own the harness execution loop.
- Supporting / enforcement mechanisms: model adapter, tools, budget, approval context, checkpoints, session persistence and hosted-run event transport.
- Closure path: objective → model turn → tool call → first-party tool result → next model turn or terminal result; child actor same model/tool loop in a supported delegated mode.
- Boundary reachability: shipped `@heddleagent/runtime` and `@heddleagent/cli` both invoke these paths without borrowing an outside coding harness.
- Why this is / is not agent-owned: model chooses task-specific next steps from real feedback; host policy only constrains which actions may execute.
- Evidence: [README.md](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/README.md); [src/core/agent/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/agent/service.ts); [src/core/runtime/loop/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/runtime/loop/service.ts); [src/sdk/conversation/headless/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/sdk/conversation/headless/service.ts).
- Basis: explicit executable model/tool loop and supported public package.
- Confidence: high.
- Caveats: read-only Ask and single-step static tool use do not individually imply all functions.

## S2 — Coordination

- State: ?
- Function: attenuation of actual interference among multiple independently running model-guided children in a shared workspace is plausible but its independent feedback/decision owner is unresolved.
- Disturbance / variety regulated: parallel delegated child S1s may read stale files or concurrently mutate the same workspace; the packaged runtime serializes action-capable children and allows read-only children in parallel.
- Decisive decision or feedback right: choose a specific response to observed inter-child conflicts and return a revised partition/order/task instruction into subsequent S1 behaviour.
- Decision owner: scope enforces serial action-child execution and child approval ceilings, while model parent chooses individual tasks/profiles; code tracing does not show a model-owned conflict diagnosis → revised worker coordination loop based on concrete conflict effects.
- Supporting / enforcement mechanisms: child reservation and concurrency semaphore, one action-child at a time, root scope life cycle, correlated child results and parent-facing model tool output.
- Closure path: parent delegates → action serialization prevents concurrent mutations → child outcomes return to parent. The further specific *inter-S1 conflict-based coordination* revision and its return are not demonstrated in supported ordinary code.
- Why this is / is not agent-owned: multiple genuinely model-driven child loops exist, and shared workspace serialization is concrete attenuation; what remains unresolved is whether the model parent has the required inter-S1 coordination feedback rather than independently picking bounded tasks and seeing summaries.
- Evidence: [src/core/delegation/README.md](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/delegation/README.md); [src/core/delegation/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/delegation/service.ts); [src/core/delegation/child-runtime.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/delegation/child-runtime.ts); [src/core/agent/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/agent/service.ts).
- Basis: concrete plausible in-boundary inter-child interference path with incomplete agent-owned corrective-return evidence.
- Confidence: unresolved.
- Caveats: serial lock alone is not S2=A; do not silently attribute customer host task orchestration.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-current operating-unit commitments controller with authoritative discretionary intervention established at declared root delegation scope.
- Disturbance / variety regulated: child concurrency/budget/deadline/authority, cancellation and lifecycle status.
- Decisive decision or feedback right: inspect whole team current commitments and revise allocation/priorities/resources in response to collected operating feedback.
- Decision owner: parent model can delegate individual tasks and await results; deterministic root scope tracks a graph and imposes ceilings, but no model-visible whole-team operating view plus adaptive current-control return is established.
- Supporting / enforcement mechanisms: `DelegationRootScope`, reservation counter, child snapshot/records, cancellation and bounded output summaries.
- Closure path: fixed ceiling and individual delegations → settled result; no whole-system portfolio feedback to a distinct S3 owner causing continuing reallocation across S1 units.
- Why this is / is not agent-owned: task delegation and state tracking are not by themselves whole-current supervisory discretion; the runtime controls limits but cannot determine the root team's business priorities.
- Evidence: [src/core/delegation/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/delegation/service.ts); [src/core/delegation/README.md](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/delegation/README.md); [src/core/runtime/loop/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/runtime/loop/service.ts).
- Basis: source-bounded negative.
- Confidence: medium-high.
- Caveats: an embedding product may provide an S3 parent using Heddle runs but it must be assessed at its own boundary.

### Absence scope

- Surfaces inspected: delegation root scope, child graph/records, runtime budgets/deadlines, hosted active runs, root agent model-visible delegate tool.
- Plausible first-party paths checked: root delegation as current task allocation, live child status as whole-current view, cancellation as control, customer host controller.
- Why no material first-party path remains: child scopes enforce fixed per-turn envelopes and report bounded results; no first-party model-owned whole-current resources/commitment view with returned intervention over active S1 organization is shown.

## S3* — Complementary audit

- State: —
- Function: no shipped sufficiently independent complementary organizational audit of S1/S3 reports and returned S3 correction established.
- Disturbance / variety regulated: errors in model results, unsafe commands, misleading child summaries or missing audit history.
- Decisive decision or feedback right: independently inspect direct operational reality, challenge ordinary reports and return findings to current regulation.
- Decision owner: ordinary tool approval and Review-profile child can check a delegated task, but neither proves a separately owned sporadic audit outside the routine result path.
- Supporting / enforcement mechanisms: event traces, artifacts, read-only Review child, task approval and logs, eval/tracing tools.
- Closure path: ordinary review/report reaches the parent as task evidence; no independent complementary direct-evidence judgment with corrective-return authority beyond normal task QA is established.
- Why this is / is not agent-owned: naming a child Review or publishing traces does not create an independently owned S3* function.
- Evidence: [src/core/delegation/README.md](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/delegation/README.md); [src/core/agent/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/agent/service.ts); [src/core/eval/trace-analyzer.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/eval/trace-analyzer.ts); [README.md](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/README.md).
- Basis: bounded source-negative.
- Confidence: medium-high.
- Caveats: a host application can attach external audit with independent direct evidence; it is not standard first-party Heddle.

### Absence scope

- Surfaces inspected: Review child tool envelope, correlated child reporting, approval chain, activity tracing and eval tooling.
- Plausible first-party paths checked: Review-profile agent as complementary auditor, trace replay, scored checks, separate hosted monitoring.
- Why no material first-party path remains: inspection is either another bounded task child or ordinary logs/QA; independent challenge of routine S1/S3 claims with authoritative returned correction is not shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: no automatic future/outside environmental sensing and strategic capability adaptation of the deployed Heddle organization.
- Disturbance / variety regulated: changing tools, threats, user needs, model providers and ecosystem.
- Decisive decision or feedback right: select future adaptations from outside-environment evidence and return changed current capability.
- Decision owner: users/hosts/maintainers select integrations, tools, memory and release priorities.
- Supporting / enforcement mechanisms: memory maintenance, model adapters, Agent Skills, heartbeat and browser automation opt-ins.
- Closure path: per-conversation memory updates or user-authored tool registration support future calls but do not autonomously choose future organizational strategy and promote it back to execution.
- Why this is / is not agent-owned: remembering old conversations and scheduling heartbeat jobs is not prospective external intelligence with owned adaptation return.
- Evidence: [src/core/memory/maintainer.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/memory/maintainer.ts); [README.md](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/README.md); [src/core/runtime/loop/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/runtime/loop/service.ts).
- Basis: bounded source-negative.
- Confidence: medium-high.
- Caveats: future host-specific product intelligence is outside the package's own boundary.

### Absence scope

- Surfaces inspected: memory maintenance, heartbeat, MCP/skills and adapters, runtime config and package docs.
- Plausible first-party paths checked: memory synthesis as adaptation, automated external threat scanning, provider selection/release changes, cross-session prospective planning.
- Why no material first-party path remains: available loops are task/session maintenance or user-configured capabilities without a future external-option-to-current organizational change process.

## S5 — Policy and identity

- State: —
- Function: no ultimate identity/policy dispute adjudication for the first-party agent organization.
- Disturbance / variety regulated: risky tool operations, child authority and requested approvals.
- Decisive decision or feedback right: legitimately decide overarching identity/purpose conflicts and return binding changed policy.
- Decision owner: customer host/operator retains identity, authenticated database, approval and business policy; runtime enforces its supplied limits.
- Supporting / enforcement mechanisms: approval policies, tool catalog ceilings, child profiles, authenticated host hooks and hosted-run cancellation.
- Closure path: configured permissions → tool allow/deny/approval → local result, without identity-level authority decision/return.
- Why this is / is not agent-owned: customer ownership is explicitly reserved rather than implemented as first-party Heddle S5; approving a tool is not an ultimate governance decision.
- Evidence: [README.md](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/README.md); [src/core/delegation/README.md](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/delegation/README.md); [src/core/delegation/service.ts](https://github.com/roackb2/heddle/blob/436eaac836512dac99520b91ae09b06212a658f4/src/core/delegation/service.ts).
- Basis: bounded source-negative.
- Confidence: high.
- Caveats: host business can implement S5 separately; no borrowed parent mode.

### Absence scope

- Surfaces inspected: package and host deployment contract, policies/approvals, child authority, hosted run envelopes.
- Plausible first-party paths checked: host-provided identity as included S5, user approvals as ultimate policy, code-profile grants as policy resolution.
- Why no material first-party path remains: the first-party package intentionally delegates legitimate product-level policy and identity authority to its embedding host.

## Distributed OSS parent arrangement

Maintainers of the public runtime, host product developers and external LLM providers have distinct goals and decision rights. The package explicitly leaves customer identity and operational governance to the product. Their authority cannot be collapsed into one undocumented parent-governed VSM mode.

## Self-hosted and non-human modes

SDK and CLI can be operated locally or embedded in other products. Autonomous coding turns are first-party, but persistent run transport and separate Execution Host interfaces do not automatically establish company-level coordination, audit or policy. Child delegation is optional and one-level only, with serial action children and bounded model context.

## Recursion

One first-party `AgentRunService` conversation is S1. With delegation enabled, root and multiple child `AgentLoopRuntimeService` loops are separate operational agents; whether their shared workspace and serial execution have a complete S2 coordination owner is explicitly unresolved, rather than inferred from the word delegation.

## Variety and escalation

User tasks, tool results and changing files produce operational variety that model/tool feedback handles. Child model profiles, root ceiling, approval and cancellation reduce risk; exceptional denials return to the actor or host operator. These do not establish separately autonomous future strategy or ultimate identity governance.

## Evidence gaps

- Optional Code children are genuine first-party iterative S1 loops; action serialization dampens overlapping workspace write risk. The **specific agent-owned conflict-to-revised-child-behaviour feedback** required for S2 remains unproven by the default scope, supporting `?`.
- A child graph exists, but whole-current supervisory decisions and resource/commitment return over multiple S1s are not established in shipped operation.
- Review child and tracing are not an independently governed complementary audit path. No live provider benchmark was executed; this is structural source-first evidence at the pinned ref.

## Assessment summary

**Proposed disposition: `included`** with vector **`S1=A / S2=? / S3=— / S3*=— / S4=— / S5=—`** at the published runtime and bounded delegation interface. Heddle's first-party coding loop is clear. The optional one-level child agent mode is real, but organization-level S2 requires more than concurrency and serialized writes.
