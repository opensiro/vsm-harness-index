---
harness_id: k-brain
project_name: K-brain
repository: https://github.com/Stack-Cairn/K-brain
review_ref: 3d7224343894861dc52a98f250d62faa84a3df0f
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# K-brain

## Review boundary

- System in focus: Installed K-brain (`kn`) terminal/CLI/ACP coding-agent runtime, including first-party child-task control and enabled backend services.
- Purpose and identity: Complete user coding and workspace tasks through a configurable model/tool loop with optional independent child tasks.
- Relevant environment: Local workspace, configured LLM API provider, user terminal, backend scheduler and memory services, optional external MCP/plugins, permission policy.
- Standard-distribution boundary: First-party Go CLI/TUI/ACP, shared agent/backend runtime, shipped tool and subagent interfaces, and native scheduled and memory operations.
- Credited operating / distribution surfaces: Model/agent turn loop, tools, background child spawn/steer/followup/status/cancel, native scheduling, local memory organizer, provider and permission/runtime wiring.
- Adjacent first-party surfaces excluded from ownership: Maintainer/CI governance, design and compatibility proposals, optional user-written hooks, external plugins/MCP services, the separately configured LLM API provider as an organizational system, and tests/example prompts as independent decision owners.
- First-party operating / deployment modes considered: Interactive terminal, noninteractive `kn run`, ACP and first-party backend with configured agent/provider, optionally with child tasks and scheduled memory.
- Recursion level: Root user task/session and the set of child S1 tasks it can actively control.
- Reviewed revision: `3d7224343894861dc52a98f250d62faa84a3df0f`.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The installed Go executable exposes terminal, headless and ACP entrypoints backed by a common agent. On each turn it constructs model requests from the current transcript, available tools and configured context, runs selected tools, records results and continues the model feedback loop. The root can delegate to foreground/background subagents with separate contexts, optionally use a worktree for isolation, inspect child statuses, steer running work, follow up on a completed child or request cancellation. Local write and bash locks protect tool execution within an agent, and deterministic runtime/backend queues and scheduler manage capacities. The optional memory organizer scans and deduplicates retained notes with a gated apply path; the AI approval reviewer analyzes action risk for tool authorization. Neither subsystem, solely by virtue of its name or model involvement, establishes S2, S3* or S4. [`README.md`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/README.md#L1-L145), [`internal/agent/agent.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/agent.go#L646-L895), [`internal/agent/subagent.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/subagent.go#L145-L230), [`internal/agent/subagent_control.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/subagent_control.go#L20-L135), [`internal/memoryruntime/organizer.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/memoryruntime/organizer.go#L46-L155), [`internal/approval/reviewer.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/approval/reviewer.go#L1-L105).

## Operational model

The task model chooses and observes repository actions, including delegating scoped child work. The root model can decide over its own active child portfolio using packaged task-control tools; child execution and cancellation are effectful but bounded by the runtime. Local locks, background queue, user permission rules, optional AI pre-action review, tool hooks and session retention enforce or record decisions at their own scopes, not necessarily additional organizational systems. Parent/operator authority over an immediate tool approval is not, by itself, standing S5 governance.

## S1 — Operations

- State: A
- Function: Perform code and workspace tasks through model-selected tools.
- Disturbance / variety regulated: Varying user requests, repository structure, execution failures and tool feedback.
- Decisive decision or feedback right: Select successive file, shell, tool and optional child-task actions based on observed outcomes.
- Decision owner: Configured model within the root agent and, when deployed, its child models.
- Supporting / enforcement mechanisms: Agent turn loop, provider adapters, tool registry/execution, task context, transcript and permission/sandbox controls.
- Closure path: The model emits tool calls; execution results enter conversation history and inform the next model turn or completion response.
- Why this is / is not agent-owned: Runtime dispatch executes requests, but discretionary task choice and feedback-driven continuation belong to the model.
- Evidence: [`internal/agent/agent.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/agent.go#L646-L895), [`internal/agent/tool_execution.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/tool_execution.go#L55-L113), [`README.md`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/README.md#L159-L220).
- Basis: structural
- Confidence: High
- Caveats: No live provider run is claimed.
- Boundary reachability: `kn` terminal, headless and ACP entrypoints use the shipped agent/backend and its configured provider/tool registry, not merely an example fixture.

## S2 — Coordination

- State: —
- Function: Attenuate interference between distinct S1 child operations.
- Disturbance / variety regulated: Concurrent child agents may modify overlapping files, consume shared capacity or return conflicting work.
- Decisive decision or feedback right: No first-party conflict-specific S2 owner with observed inter-child attenuation and returned corrective coordination was established.
- Decision owner: Root model assigns subagent work; runtime protects local operations through simple locks, optional worktree isolation and queue/scheduling rules.
- Supporting / enforcement mechanisms: `subagent` worktree option, per-agent `fileLocks`, backend queue, child communication and task status.
- Closure path: Worktree or locks constrain specific writes, and queued or steered messages reach a child; neither path establishes a shipped conflict-aware coordination decision closing across distinct S1 commitments.
- Why this is / is not agent-owned: Generic serialization and routed messages are infrastructure; a per-agent mutex is not whole-agent coordination, and isolation selected by the caller is not a runtime S2 conflict-correction protocol.
- Evidence: [`internal/agent/filelocks.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/filelocks.go#L1-L85), [`internal/agent/agent.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/agent.go#L471-L489), [`internal/agent/tool_execution.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/tool_execution.go#L60-L90), [`internal/agent/subagent.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/subagent.go#L155-L230).
- Basis: structural
- Confidence: Medium
- Caveats: A user-authored multi-agent workflow may implement its own collision resolution, not credited as bundled function.

### Absence scope

- Surfaces inspected: Child launch and steering, per-agent tool locks, worktree isolation, task registry, backend job/queue and scheduler.
- Plausible first-party paths checked: Overlapping file writes, bash global lock, optional child git worktrees, generic task messages, per-task concurrency controls.
- Why no material first-party path remains: The source shows local operation guards and generic root-selected task controls, but no first-party S2-specific detection, attenuation choice and verification/feedback closing an interference between distinct child operating units.

## S3 — Inside-and-now control

- State: A
- Function: Oversee and change current commitments across a root session's child-task portfolio.
- Disturbance / variety regulated: A subordinate task can stall, become obsolete or require follow-up while siblings remain active.
- Decisive decision or feedback right: Inspect currently running/completed tasks, choose a particular child for cancellation, steer a running child and resume a completed child with new instructions.
- Decision owner: Root task model through the shipped model-visible child-control tools.
- Supporting / enforcement mechanisms: `subagent_status`, `subagent_cancel`, `subagent_steer`, `subagent_followup`, `BackgroundTask` registry and child completion reporting.
- Closure path: The selected control action calls task cancellation or sends follow-up to an owned child, changes its work/continuation and returns state or result to the root; cancellation is explicitly asynchronous and therefore not mistaken for immediate full cleanup.
- Why this is / is not agent-owned: The model chooses which live commitment to stop or redirect based on the current child-status view; deterministic cancellation plumbing enforces the selected intervention.
- Evidence: [`internal/agent/subagent_control.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/subagent_control.go#L21-L140), [`internal/agent/subagent.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/subagent.go#L239-L315), [`internal/agent/agent.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/agent.go#L471-L489).
- Basis: structural
- Confidence: High
- Caveats: Bounded to the root's own children, not independent user sessions or wider deployment; asynchronous cancellation must be distinguished from completed cleanup.
- Boundary reachability: `taskControlTools(a)` are included in the shipped root agent tool set and their calls resolve through the parent-owned task registry; no external framework composition is needed.
- Whole-system current view: `subagent_status` lists all current known owned child tasks, their state and whether follow-up is possible; a selected child can expose its full report.
- Current-control decision scope: Decide which of the root's child commitments continues, receives a new instruction, or is cancelled, while leaving unrelated children active.

## S3* — Complementary audit

- State: —
- Function: Independently inspect operational claims or produced artifacts using complementary direct evidence and return an adjudicated correction to current control.
- Disturbance / variety regulated: An operation or tool action may be unsafe; produced work may be incorrect.
- Decisive decision or feedback right: No packaged independent, direct-result audit decision with a return-to-S3 corrective disposition was established.
- Decision owner: Configured AI pre-action reviewer evaluates proposed tool risk; human reviews task plans; task model may run tests or request a child inspection.
- Supporting / enforcement mechanisms: Tool-less action-risk reviewer, plan approval, test tools, child reports and hooks.
- Closure path: Risk review can tighten a tool permission before execution; human plan review can request changes. Neither supplies an independent evidence-based audit of an operational claim with corrective return to current portfolio control.
- Why this is / is not agent-owned: The pre-tool reviewer examines action intent and untrusted output to decide permission risk, not a completed S1 outcome; a generic review role is not proof of first-party S3*.
- Evidence: [`internal/approval/reviewer.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/approval/reviewer.go#L1-L102), [`internal/backend/ai_approval.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/backend/ai_approval.go#L1-L85), [`internal/agent/plan_review.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/plan_review.go#L1-L80), [`internal/agent/subagent.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/subagent.go#L150-L190).
- Basis: structural
- Confidence: Medium
- Caveats: External/reconfigured independent evaluators may exist but are outside this credited boundary.

### Absence scope

- Surfaces inspected: AI approval reviewer, backend action-review wiring, plan review, subagent roles, tool execution and available testing/integration extensions.
- Plausible first-party paths checked: Security preapproval, independent review-child prompt, model-directed test execution, plan approval and user-supplied hooks.
- Why no material first-party path remains: Shipped review paths gate proposed actions or return generic reports, without a dedicated direct-evidence audit verdict and feedback to a separate current-control decision owner over observed S1 outcomes.

## S4 — Outside-and-then intelligence

- State: —
- Function: Interpret changes or prospects in the outside environment and alter later system-wide capability in response.
- Disturbance / variety regulated: Provider and tooling capabilities, future tasks and retained memory evolve over time.
- Decisive decision or feedback right: No first-party prospective external-environment interpretation and capability-selection loop with operational return was established.
- Decision owner: User/operator configures providers, skills and reminders; scheduled memory organizer may apply bounded deterministic note cleanups.
- Supporting / enforcement mechanisms: Persisted memory, `RunOrganizer` and its gated scan/cluster/plan/apply, agent scheduling, configurable prompts, provider selection and skills.
- Closure path: Memory dedup applies an internal storage change and can influence later loaded notes; no future outside-environment strategic alternative is selected or committed from this feedback.
- Why this is / is not agent-owned: Internal memory housekeeping, provider fallback and cron reminders do not supply requisite outside-and-then strategic judgment, even where model calls may be configured.
- Evidence: [`internal/memoryruntime/organizer.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/memoryruntime/organizer.go#L18-L160), [`internal/memoryruntime/organizer.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/memoryruntime/organizer.go#L355-L373), [`internal/agent/agent.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/agent.go#L694-L722), [`README.md`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/README.md#L53-L95).
- Basis: structural
- Confidence: Medium
- Caveats: A user-authored scheduled research workflow could create another S4-like deployment.

### Absence scope

- Surfaces inspected: Memory organizer, context injection, cron/schedule routes, provider selection, durable sessions, skill/hook and extensibility configuration.
- Plausible first-party paths checked: Memory maintenance scheduling, retrospective consolidation, provider failover, recurrent user reminders and custom external research.
- Why no material first-party path remains: These paths execute current/scheduled intentions or internally clean notes, but do not provide a first-party prospective environmental assessment that chooses future organization capability and returns to ongoing operations.

## S5 — Policy and identity

- State: —
- Function: Resolve a binding organizational purpose, constitutive identity or standing policy decision for future operation.
- Disturbance / variety regulated: Different execution permissions, project constraints and user safety requirements.
- Decisive decision or feedback right: No standing S5 issue is escalated to a legitimate parent, decided, and returned as binding future operating authority within the assessed runtime.
- Decision owner: User approves concrete plans/actions and configures permissions; runtime enforces the chosen restrictions.
- Supporting / enforcement mechanisms: Permission modes, AI pre-tool review, sandbox, hooks, tool-use rules and manual plan approval.
- Closure path: Tool authorization or plan approval affects the immediate task; saved settings can constrain future calls but are not shown as a returned identity-level policy adjudication.
- Why this is / is not agent-owned: Enforcement of caller-set authority and immediate consent are not equivalent to the function that legitimately determines overarching identity and policy.
- Evidence: [`internal/agent/plan_review.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/agent/plan_review.go#L1-L85), [`internal/backend/ai_approval.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/backend/ai_approval.go#L1-L75), [`internal/approval/reviewer.go`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/internal/approval/reviewer.go#L20-L100), [`README.md`](https://github.com/Stack-Cairn/K-brain/blob/3d7224343894861dc52a98f250d62faa84a3df0f/README.md#L93-L160).
- Basis: structural
- Confidence: High
- Caveats: Maintainer governance is a different recursion outside the runtime assessment.

### Absence scope

- Surfaces inspected: Runtime approval modes, plan review, safety reviewer, operator configuration, hook authority and sandbox controls.
- Plausible first-party paths checked: Persisted permissions, user decision to implement a plan, AI action risk review, cross-session constitutive policy change and parent-level escalation.
- Why no material first-party path remains: Observed paths implement task authorization and safeguards; they do not close a recognized identity/ultimate-policy issue via a legitimate policy owner and return it to future operational control.

## Recursion

An optional child is a distinct bounded S1 task with fresh context and its own model/tool execution. The parent model retains current control over the aggregate of owned child commitments. No higher-level recursive viability is inferred merely from this delegation.

## Variety and escalation

The root model absorbs tool and task variability. Local resource/permission bounds and optional worktree isolation constrain mutations. Child task control handles current delegated-work disturbances. Operator review is immediate task authority, not necessarily VSM S5 identity authority.

## Evidence gaps

Pinned first-party source review without executing live provider/model calls, user-composed plugins, or independent review. S2/S3* negative conclusions are bounded to the credited first-party paths. Child cancellation is an asynchronous request, so the positive S3 evidence rests on scope selection and returned task-control effects, not invented immediate cleanup verification.
