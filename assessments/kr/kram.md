---
harness_id: kram
project_name: Kram
repository: https://github.com/codexmark/kram
review_ref: 5f18406709f432dbdb2d6b09da6f140385516366
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Kram

## Review boundary

- System in focus: the released original Go `kram` local-first coding-agent loop/daemon/tools with independently executing delegated child sessions, gateway and policy controls, at frozen revision `5f18406709f432dbdb2d6b09da6f140385516366`.
- Purpose and identity: take developer tasks, inspect/edit/test workspace source with model-selected tool calls, use delegated self-contained subtasks, maintain bounded long-lived context and route model traffic across providers.
- Relevant environment: changing source repository and terminal, gateway/model outcomes, approval replies, durable session and memory, concurrent delegated task results.
- Standard-distribution boundary: shipped single Go binary invoking the first-party agent loop, gateway/daemon and tools; `delegate_task` calls separate model loops through first-party `RunTask`. External providers calculate tokens, not Kram organizational decisions.
- Credited operating / distribution surfaces: `internal/daemon/agent` run loop, `internal/daemon/tools` handlers/delegation, daemon persistent store, permission/approval, gateway model routing, verification/steering/compaction in ordinary operation.
- Adjacent first-party surfaces excluded from ownership: contributor `DECISIONS.md` retrospectives, CI/evals/tests and release installers, user configuration changes, future planned capability additions, other first-party apps and external coding agents not running in the same Kram process.
- First-party operating / deployment modes considered: interactive coding/TUI+daemon session; delegated concurrent independent subtasks with isolated *conversation context*; user permissions/approval, gateway routing and optional human questions.
- Recursion level: one root run with separately executed child coding sessions as S1s in a task fan-out. The child context is isolated, but a distinct filesystem/worktree per child is **not** evidenced by the delegate implementation.
- Reviewed revision: `5f18406709f432dbdb2d6b09da6f140385516366`.
- Observation date: 2026-10-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/README.md) describes an original first-party coding loop with gateway, daemon, TUI and `delegate_task` subtasks. [internal/daemon/agent/agent.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/agent/agent.go) implements `Service.Run`, `RunTask` and a bounded `runLoop` across model turn, tool execution and renewed context, including steering, budget, stop and verification nudges. [internal/daemon/tools/delegate.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/tools/delegate.go) registers model-visible delegation, explicitly requiring independent self-contained tasks, starts up to three child goroutines, asks each to execute `RunTask` in a fresh session and returns bounded results to the root model's next turn.

[internal/daemon/tools/tools.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/tools/tools.go) configures tool registry and concrete delegator; [internal/daemon/store/search.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/store/search.go) excludes internal child-session traces from ordinary user search by default. [internal/daemon/agent/systemprompt.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/agent/systemprompt.go) asks the parent to batch independent tasks rather than launch unrelated serial child calls. The child `RunTask` gets no parent conversation/clarification surface; these are genuine first-party model-run children rather than fictional role labels.

The gateway's model selection, circuit breaking, routing telemetry, permission system and user approval are bounded support/enforcement facilities. They are not separate organizational S2/S3/S4/S5 owners simply because their names refer to control, planning or governance.

## Operational model

The first-party loop sends the task and current state to an LLM, receives a tool invocation, validates/executes it, records the observation and sends the outcome into another model decision. If the model chooses a batch `delegate_task`, separate child agent loops run concurrently in isolated conversations and return task results. The parent model may interpret those results and decide more work; the shipped delegate logic assumes independence and has no proven shared-file conflict admission, ownership-claim/merge-resolution or post-conflict remediation path. Runtime limits and user approvals constrain activity but do not own team-wide current commitments or institutional purpose.

## S1 — Operations

- State: A
- Function: perform bounded autonomous repository coding/investigation with model-selected tools and subsequent evidence-based decisions.
- Disturbance / variety regulated: unknown source state, shell results, test failures, model responses, permission refusals and child observations.
- Decisive decision or feedback right: choose the next read/edit/command/delegation and revise from actual tool or child results.
- Decision owner: root and child model actors in first-party `agent.Service.runLoop`; the LLM provider supplies a completion, not an external agent implementation.
- Supporting / enforcement mechanisms: first-party tool registry, gateway client, persistent messages, run budget and segments, verify and approval gates.
- Closure path: model → tool → first-party dispatch/results/history → model next decision or task completion; `RunTask` runs the same loop for children.
- Boundary reachability: standard supported binary and `delegate_task` tool registration/agent service, not a CI-only fixture or outside CLI.
- Why this is / is not agent-owned: choices about source actions and fixes come from model calls reacting to observations rather than predetermined script nodes.
- Evidence: [README.md](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/README.md); [internal/daemon/agent/agent.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/agent/agent.go); [internal/daemon/tools/delegate.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/tools/delegate.go); [internal/daemon/tools/tools.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/tools/tools.go).
- Basis: directly implemented model/tool loop.
- Confidence: high.
- Caveats: actual success and latency have not been measured in live model inference here.

## S2 — Coordination

- State: —
- Function: no first-party closed attenuation of concrete interference between multiple independent child S1 coding operations is demonstrated.
- Disturbance / variety regulated: concurrent children can access the same workspace, return incompatible patches or depend on one another; the model is instructed to choose *independent* subtasks.
- Decisive decision or feedback right: detect actual competing work and choose revised scope/order/ownership with changes returned into continuing child S1 operation.
- Decision owner: parent model chooses initial independent goals, while `delegate_task` starts workers in parallel and returns their final answers; it has no specialized conflict sensor or coordination intervention owner.
- Supporting / enforcement mechanisms: per-call concurrency semaphore and max depth, isolated child sessions, task result collating and approval constraints.
- Closure path: parent-chosen independent tasks → parallel execution → ordered summaries to parent. No shipped specific cross-child conflict detection/claim registry, resolved merge decision or revised child scope return is demonstrated.
- Why this is / is not agent-owned: generic fan-out and shared summaries can support coordination externally, but mechanical concurrency limits and a statement that tasks should not interfere are not actual adaptive S2 attenuation.
- Evidence: [internal/daemon/tools/delegate.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/tools/delegate.go); [internal/daemon/agent/agent.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/agent/agent.go); [internal/daemon/agent/systemprompt.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/agent/systemprompt.go).
- Basis: bounded source-negative.
- Confidence: medium-high.
- Caveats: a user can ask a model to coordinate tasks, but no first-party guaranteed concrete interference path closes as an organizational function.

### Absence scope

- Surfaces inspected: child delegation and goroutines, session isolation, agent tool execution, prompt coordination policy and final results.
- Plausible first-party paths checked: overlap prevention via filesystem worktrees, explicit write-claim management, dependency scheduler, conflict resolution after results, re-tasking existing children.
- Why no material first-party path remains: child isolation concerns history, not proven workspace ownership. They are spawned to completion and joined; no distinct feedback/control path returns coordination actions to active conflicting children.

## S3 — Inside-and-now control

- State: —
- Function: no shipped model-owned whole-current population of child S1 operations with ongoing commitments/priority/reallocation authority is established.
- Disturbance / variety regulated: parent/child turn counts and independent delegated subtasks; costs, approvals and gateway fallbacks.
- Decisive decision or feedback right: observe whole current child organization and choose reallocations/cancellation/intervention from current outcomes, returning changed commitments into S1s.
- Decision owner: parent model can select initial batch tasks, but each `delegate_task` executes to completion with fixed per-call semaphore; daemon limits are predetermined.
- Supporting / enforcement mechanisms: delegated batch limits, depth, child session store and gateway telemetry, run context/approval.
- Closure path: one-shot task fan-out → child results → parent next task; not a live team-wide current resource/priority view controlling child agents during their operation.
- Why this is / is not agent-owned: a generic parent receiving results and a gateway managing model requests is not automatically S3 supervisory regulation.
- Evidence: [internal/daemon/tools/delegate.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/tools/delegate.go); [internal/daemon/agent/agent.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/agent/agent.go); [internal/daemon/store/search.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/store/search.go).
- Basis: bounded source-negative.
- Confidence: medium-high.
- Caveats: an externally assembled long-lived fleet control plane could add S3, outside this binary's root task mode.

### Absence scope

- Surfaces inspected: child statuses and per-call synchronization, parent agent run, gateway telemetry/fallback, daemon state and session search.
- Plausible first-party paths checked: live roster and status snapshot, parent worker stop/reassignment, budget reallocation, cross-episode current commitments.
- Why no material first-party path remains: child run completion is the principal return, while concurrent admission and depth are fixed limits without whole-current discretionary control/return.

## S3* — Complementary audit

- State: —
- Function: no independently owned complementary audit of root/child claims that returns an independently informed corrective judgment into a current S3 organization is shown.
- Disturbance / variety regulated: false verification claims, coding mistakes or misleading child results.
- Decisive decision or feedback right: inspect operational evidence through a complementary independent path and cause legitimate corrective action outside ordinary task verification.
- Decision owner: ordinary verify gate, trace and optional user check are part of the same normal run, not a separate first-party audit actor.
- Supporting / enforcement mechanisms: verification nudges, durable session transcripts, test commands, CI and reliability diagnostics.
- Closure path: failure/verify observations can cause another model turn in the operating S1, but not a complementary independent audit-to-S3 regulation loop.
- Why this is / is not agent-owned: model self-check and human approval are normal execution quality control, not distinct independent S3* governance.
- Evidence: [internal/daemon/agent/agent.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/agent/agent.go); [internal/daemon/agent/verifygate.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/agent/verifygate.go); [README.md](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/README.md).
- Basis: bounded source-negative.
- Confidence: medium-high.
- Caveats: configured specialized external audit could be created separately, but cannot be imported as first-party operational ownership.

### Absence scope

- Surfaces inspected: verifygate, tool results/history, optional users, child sessions and repo test/CI workflows.
- Plausible first-party paths checked: second independent verifier model, direct raw artifact audit, corrective adjudication and return to an S3 decision owner.
- Why no material first-party path remains: verification is ordinary same-session nudge/retry; logs and external human tests are evidence sources, not a separately acting complementary authority.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective outside-environment sensing with autonomous adaptation of Kram's future organizational capabilities is established.
- Disturbance / variety regulated: changing providers, coding practices and tools across sessions.
- Decisive decision or feedback right: choose future capabilities from external intelligence and reintroduce the selected change to currently functioning runtime.
- Decision owner: user/maintainers choose installed skills/provider config/releases; memory observations support tasks but do not own future strategy.
- Supporting / enforcement mechanisms: memory/session search, skillpack, provider health/fallback and architecture decisions.
- Closure path: current observations become future prompt context, or provider fallback is selected for availability; no prospective strategy selection and capability promotion is shown.
- Why this is / is not agent-owned: provider redundancy and memory compaction optimize current work, not forward-looking outside organizational intelligence.
- Evidence: [internal/daemon/agent/agent.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/agent/agent.go); [internal/daemon/store/search.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/store/search.go); [README.md](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/README.md).
- Basis: bounded source-negative.
- Confidence: medium-high.
- Caveats: changes from manual project maintenance are beyond deployed S4 scope.

### Absence scope

- Surfaces inspected: durable memory, session reuse, provider routing and skills, architecture decision records and release workflow.
- Plausible first-party paths checked: model-independent trend sensing, learned future tool composition, autonomous skill evolution/promotion and returned adoption.
- Why no material first-party path remains: only ongoing task context and user-driven configuration/maintenance evidenced, no prospective option/decision/return owner.

## S5 — Policy and identity

- State: —
- Function: no ultimate shared identity/policy dispute resolution function within the first-party Kram runtime is established.
- Disturbance / variety regulated: tool permissions, approval prompts, provider access and operator-defined project boundaries.
- Decisive decision or feedback right: decide legitimate ultimate identity/mission tradeoffs and return binding policy updates into operation.
- Decision owner: operator controls permissions and model credentials; Kram enforces those instructions, not organizational ultimate values.
- Supporting / enforcement mechanisms: tool allow/deny/ask, permission presets, controlled shell, depth and provider settings.
- Closure path: operator-configured rights → tool execution veto or approval → continuation/stop, without ultimate organizational policy adjudication and returned changed identity rights.
- Why this is / is not agent-owned: one permission grant or user approval is operational authorization, not the VSM S5 function.
- Evidence: [internal/daemon/tools/tools.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/tools/tools.go); [internal/daemon/agent/agent.go](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/internal/daemon/agent/agent.go); [README.md](https://github.com/codexmark/kram/blob/5f18406709f432dbdb2d6b09da6f140385516366/README.md).
- Basis: bounded source-negative.
- Confidence: high.
- Caveats: Kram can be used in an organization that has an independent S5 parent; its human governance is not credited to the binary.

### Absence scope

- Surfaces inspected: permissions and approval, run controls, child grants, gateway/account configuration and maintainer process.
- Plausible first-party paths checked: escalated policy exception as identity decision, admin reconfiguration, issue/PR maintainer authority and child delegated grants.
- Why no material first-party path remains: authorization applies externally selected user task constraints without a first-party ultimate policy dispute/legitimate choice/returned organization mode.

## Distributed OSS parent arrangement

Local Kram users and public contributors have distinct authorities; the package contains no single organizational parent tying independent installations to legitimate current, future and ultimate-policy decisions. External model services and release servers also do not donate metasystem ownership.

## Self-hosted and non-human modes

Local gateway and daemon can be standalone or combined. The agent chooses coding actions and independent subtask goals; the user approves permissions. Subtasks get fresh conversation sessions with a bounded nesting limit and concurrency ceiling, but no proven independent workspace isolation, live whole-team management or autonomous future adaptation mode.

## Recursion

A root agent is one S1; independent child tasks each run the model/tool agent loop with fresh sessions, and their final answers re-enter parent conversation. The existence of multiple S1s supports the S2/S3 investigation but not automatic positive grades for those functions.

## Variety and escalation

Model-proposed tools, shell observations and child results expose operating variety. A deterministic gateway and permission constraints attenuate faults; child failures reach the parent model in bounded results, while unsupported approvals fail closed in child context. These are operational feedback and exceptional reports, not evidence for independent complementary audit or ultimate policy governance.

## Evidence gaps

- Local-first project claims and shipped source show first-party S1. The internal parallel `delegate_task` mechanism intentionally assumes tasks are independent; no specialized inter-S1 conflict management or whole-current organizational owner is established from those mechanisms.
- No live model-provider benchmark was executed. Positive S1 source evidence does not imply a particular score on task success, and negative grades are limited to pinned standard distribution.
- Third-party host code, maintainer project decisions and externally implemented governance are excluded.

## Assessment summary

**Proposed included**: `S1=A / S2=— / S3=— / S3*=— / S4=— / S5=—`. A first-party Go model/tool coding agent exists, including bounded child loops. Remaining system functions are not raised from mere fan-out, provider routing, memory, verification or operator permissions.
