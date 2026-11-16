---
harness_id: gocode
project_name: gocode
repository: https://github.com/AlleyBo55/gocode
review_ref: d941b2af44f4c71fcf279e815fcfb785eab51c2a
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# gocode

## Review boundary

- System in focus: An installed gocode coding session with optional swarm agents and the shipped GitHub review action considered as an optional deployment surface.
- Purpose and identity: Inspect and change software through a model-backed Go CLI or perform a requested repository review through the action.
- Relevant environment: User objectives, local project and tool outputs, model providers, peer work and externally configured PR workspaces.
- Standard-distribution boundary: The gocode binary and the repository's gocode-action composite action at the frozen revision.
- Credited operating / distribution surfaces: Interactive REPL, one-shot run, shipped orchestrator and swarm, operator goal control, and the review-specific PR-comment action entry.
- Adjacent first-party surfaces excluded from ownership: Repository CI, evals and fixtures, unmounted helper packages, separately installed integrations and caller-owned deployment scaffolding.
- First-party operating / deployment modes considered: Interactive and one-shot local coding, optional subordinate model runs, REPL with persistent goal, and caller-composed PR review action.
- Recursion level: One deployed coding cell or its separately configured review mode. No authority over a multi-project organization is assessed.
- Reviewed revision: `d941b2af44f4c71fcf279e815fcfb785eab51c2a`
- Observation date: 2026-11-16
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The binary wires provider routing, a conversation runtime and workspace tools into interactive and one-shot entry points. Both install model-invocable specialist delegation and named swarm inboxes. In the REPL the user can supervise a persistent goal. A separate composite action provides a PR-comment review route whose environment is supplied by the caller. [`cmd/gocode/main.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/cmd/gocode/main.go#L776-L817), [`cmd/gocode/main.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/cmd/gocode/main.go#L878-L938), [`cmd/gocode/main.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/cmd/gocode/main.go#L1234-L1247), [`gocode-action/action.yml`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/gocode-action/action.yml#L1-L46).

## Operational model

One model-backed conversation owns local task and tool choice. Specialist runs can return their own results and exchange messages. The operator can inspect, pause or resume the currently persisted driving objective in ordinary REPL mode. The optional review action can act as a separate model reviewer when the caller binds it to the artifacts and control process being audited.

## S1 — Operations

- State: A
- Function: Use a model-led tool loop to complete workspace and coding requests.
- Disturbance / variety regulated: Uncertain task state, tool results and failed operations.
- Decisive decision or feedback right: Choose the concrete tool action and change subsequent steps based on its result.
- Decision owner: The model within the gocode conversation runtime.
- Supporting / enforcement mechanisms: Go runtime, provider routing, permissions, registry and usage or iteration limits.
- Closure path: The runtime executes provider-selected tool calls, appends tool results to the conversation and requests another model response.
- Why this is / is not agent-owned: Disabling the model leaves permission enforcement and tool transport but removes task action selection.
- Evidence: [`cmd/gocode/main.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/cmd/gocode/main.go#L878-L918), [`cmd/gocode/main.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/cmd/gocode/main.go#L1277-L1306), [`internal/agent/runtime.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/agent/runtime.go#L133-L170), [`internal/agent/runtime.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/agent/runtime.go#L384-L419)
- Basis: structural
- Confidence: High for the source path.
- Caveats: A configured model and suitable workspace are required.
- Boundary reachability: The installed interactive and one-shot commands construct the inspected conversation runtime.

## S2 — Coordination

- State: —
- Function: No returned inter-S1 work-conflict regulation path was evidenced.
- Disturbance / variety regulated: Multiple independently running specialists might compete for work or modify related workspace state.
- Decisive decision or feedback right: The shipped swarm offers explicit addressing and communication, with no supplied decision over a specific work conflict.
- Decision owner: Model agents own message content and task choices. Runtime owns mailbox identity and capacity.
- Supporting / enforcement mechanisms: Thread-safe swarm registry, distinct mailbox identities, capacity checks, return messages and worktree helpers.
- Closure path: Tool messages can reach the next model turn but no shipped rule detects or resolves duplicated work or shared-file interference.
- Why this is / is not agent-owned: Task decomposition and forwarding do not on their own instantiate a function-specific peer adjustment.
- Evidence: [`internal/orchestrator/orchestrator.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/orchestrator/orchestrator.go#L116-L170), [`internal/orchestrator/orchestrator.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/orchestrator/orchestrator.go#L173-L205), [`internal/swarm/swarm.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/swarm/swarm.go#L88-L150), [`internal/swarm/inbox.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/swarm/inbox.go#L39-L103), [`internal/worktree/tools.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/worktree/tools.go#L18-L51)
- Basis: structural
- Confidence: Moderate for wired CLI and swarm paths.
- Caveats: The model can be prompted to negotiate using the mailbox. No such caller composition is credited.

### Absence scope

- Surfaces inspected: Orchestrator tool registry, spawned runtime and swarm tools, task store, worktree helpers and CLI wiring.
- Plausible first-party paths checked: Competing task ownership, shared worktree contention, duplicate agent identities and cross-worker messages.
- Why no material first-party path remains: Unique names solve transport addressing. The mounted tools supply no conflict-sensitive operational claim or worktree reconciliation rule. Worktree helpers do not form a wired per-agent feedback path.

## S3 — Inside-and-now control

- State: P
- Function: Regulate continuation of the single persisted objective in the REPL operating cell.
- Disturbance / variety regulated: A running objective can become inappropriate, blocked, complete or over its token commitment.
- Decisive decision or feedback right: Inspect objective status and accumulated usage, then choose whether to keep the objective active, pause, block, resume or retire it.
- Decision owner: The local session operator in the REPL goal mode.
- Supporting / enforcement mechanisms: Goal tracker, status display, persisted state, usage accounting and prompt injection.
- Closure path: Pausing or retiring the objective removes the active driving instruction from subsequent turns. Resuming a paused goal restores the current directive under the tracker rules.
- Why this is / is not agent-owned: The operator selects the outcome based on current state. Token-limit auto-pause enforces configured bounds and does not make the discretionary operator decision.
- Evidence: [`cmd/gocode/main.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/cmd/gocode/main.go#L921-L938), [`internal/repl/repl.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/repl/repl.go#L467-L481), [`internal/repl/repl.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/repl/repl.go#L562-L572), [`internal/repl/repl.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/repl/repl.go#L828-L876), [`internal/goal/goal.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/goal/goal.go#L105-L141), [`internal/goal/goal.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/goal/goal.go#L179-L218)
- Basis: structural
- Confidence: Moderate for one REPL cell with the persistent goal active.
- Caveats: The goal state governs later lead turns. It does not cancel background specialists or manage organization-wide capacity.
- Boundary reachability: The installed REPL constructs the persistent tracker and exposes status and operator controls without a custom host.
- Whole-system current view: Status and use of the one active operating objective in the assessed single-REPL-cell goal mode.
- Current-control decision scope: Pause, block, retire or reactivate that current commitment and thereby change subsequent operating turns.

## S3* — Complementary audit

- State: C
- Function: Compose a complementary PR review in a separate gocode model invocation.
- Disturbance / variety regulated: A producer's PR description or self-review can diverge from the pinned change under review.
- Decisive decision or feedback right: Assess reviewed changes from a separately supplied artifact checkout and return findings to the PR operator.
- Decision owner: The constructed separate gocode reviewer model. The workflow author supplies artifact binding and review configuration.
- Supporting / enforcement mechanisms: Shipped PR-comment review trigger, reviewer prompt, fresh gocode invocation and return to the originating discussion.
- Closure path: The action can post the review result back to the originating PR. The caller must bind artifact identity and configure who uses the findings in review or correction.
- Why this is / is not agent-owned: The product supplies an event-specific review constructor rather than asserting that every installation has a separate reviewer or an exact-ref audit.
- Evidence: [`README.md`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/README.md#L282-L291), [`gocode-action/action.yml`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/gocode-action/action.yml#L1-L46), [`gocode-action/entrypoint.sh`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/gocode-action/entrypoint.sh#L64-L114), [`internal/repl/repl.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/repl/repl.go#L385-L392)
- Basis: structural
- Confidence: Moderate for the shipped constructor, conditional on caller wiring.
- Caveats: The PR-comment wrapper identifies the discussion but does not itself fetch or verify the PR head. The in-session /review runs in the coder context and is excluded from this claim.
- Boundary reachability: The first-party composite action ships a PR-comment path that starts a separate CLI run and can return its result to the triggering PR. An enclosing workflow must add checkout identity, suitable read access and a correction path.
- Claim being audited: Whether a proposed code change satisfies the assigned task or review criteria.
- Ordinary reporting path: The producer's PR summary, comments and normal coding result.
- Complementary access path: Caller config must give the dedicated reviewer a checkout or independently reachable diff for the exact PR under review.
- Independence boundary: Review runs in a new CLI invocation in the composed workflow rather than the original producer conversation.
- Who acts on findings: The workflow posts findings to the originating PR. A caller-supplied maintainer or integration process acts on the result.

## S4 — Outside-and-then intelligence

- State: —
- Function: No source-reachable future capability adaptation loop was established.
- Disturbance / variety regulated: Project changes and accumulated experience could justify changing future tool or operating choices.
- Decisive decision or feedback right: The visible runtime stores user-selected notes and returns heuristic profile choices, with no closed adaptation selection.
- Decision owner: Operator supplies memory entries and configuration, with no qualifying S4 decision owner established.
- Supporting / enforcement mechanisms: REPL memory, prompt loading, heuristic profile recommendation and a separately defined dream implementation.
- Closure path: The REPL can render persisted notes in a prompt. The inspected CLI assembly does not mount the dream constructor or feed profile recommendations into an assessed adaptation cycle.
- Why this is / is not agent-owned: A dream model is defined internally, but no production constructor call wires it into the pinned executable.
- Evidence: [`internal/repl/repl.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/repl/repl.go#L698-L732), [`internal/repl/repl.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/repl/repl.go#L1285-L1293), [`internal/profiles/profiles.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/profiles/profiles.go#L93-L109), [`internal/dream/dream.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/dream/dream.go#L192-L221), [`internal/repl/repl.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/repl/repl.go#L597-L600), [`cmd/gocode/main.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/cmd/gocode/main.go#L921-L940)
- Basis: structural
- Confidence: Moderate to high for the assessed CLI entry paths.
- Caveats: The reference dream implementation and generic skill loading do not demonstrate actual deployed capability closure.

### Absence scope

- Surfaces inspected: Chat and one-shot construction, REPL memory/goal and skill-loading paths, profile recommendation, Dreamer constructor and idle hooks.
- Plausible first-party paths checked: Dream model invocation, persistent project memory and profile choices as potential cross-session adaptation.
- Why no material first-party path remains: Dream hooks need an installed Dreamer and no production caller mounts one at this ref. The memory and profile paths capture context or advise choices without an evidenced prospective adaptation decision returned to current capability.

## S5 — Policy and identity

- State: —
- Function: No shipped ultimate-purpose or policy adjudication loop was established.
- Disturbance / variety regulated: Tool access and project instructions set scope and constraints.
- Decisive decision or feedback right: User grants scoped permissions or changes configured modes; no ultimate-policy issue is routed and resolved in the runtime.
- Decision owner: Local user owns operations permissions. No qualifying S5 adjudicator is established.
- Supporting / enforcement mechanisms: Permission policy, trusted tool store and project instructions.
- Closure path: Decisions allow or deny specific actions and affect ordinary task execution.
- Why this is / is not agent-owned: The shipped controls support local governance of tasks and access. They do not evidence an identity-level decision path.
- Evidence: [`internal/agent/permissions.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/agent/permissions.go#L18-L29), [`internal/agent/permissions.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/agent/permissions.go#L55-L77), [`internal/agent/trusted.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/agent/trusted.go#L30-L87), [`internal/repl/repl.go`](https://github.com/AlleyBo55/gocode/blob/d941b2af44f4c71fcf279e815fcfb785eab51c2a/internal/repl/repl.go#L828-L876)
- Basis: structural
- Confidence: Moderate for the declared cell.
- Caveats: Maintainer/project policy outside the deployed cell is outside scope.

### Absence scope

- Surfaces inspected: Permission guard, trust settings, REPL goal and mode controls and runtime prompt assembly.
- Plausible first-party paths checked: User grants or persistence of access rules as policy return, operator goal changes, source repository governance.
- Why no material first-party path remains: The first two are task and resource controls. No unresolved ultimate-policy or identity matter is sent to a legitimate parent and then applied as the returned policy of the assessed runtime.

## Distributed OSS parent arrangement

The local operator supervises the assessed REPL objective. Project maintainers and outside GitHub operators remain outside the CLI ownership boundary unless separately configured for a review deployment.

## Self-hosted and non-human modes

The CLI can run against configured hosted or local providers. The PR-review constructor requires an external workflow and a separate artifact boundary.

## Recursion

One coding cell, with task-scoped subordinate model units. The optional PR-review deployment can be composed to inspect a separate producer.

## Variety and escalation

Bounded cost and iteration, permission prompts, context compaction, peer messages and operator goal controls manage scoped disturbances. No additional algedonic claim is made.

## Evidence gaps

This fixed-ref review is source-based. The report does not assume that hosted review reads the exact PR head or that optional, unmounted Go packages execute in the ordinary binary.
