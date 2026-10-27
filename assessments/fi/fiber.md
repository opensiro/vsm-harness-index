---
harness_id: fiber
project_name: Fiber
repository: https://github.com/aakshintala/fiber
review_ref: 61af2a84f70a2ece2b6cf8f73a8fa70116360da7
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Fiber

## Review boundary

- System in focus: a source-built Fiber coding session and the Fiber delegate jobs it starts.
- Purpose and identity: perform coding work using a provider-backed agent loop, durable events and model-selected tools.
- Relevant environment: workspace/Git state, providers and quota, user rules, session clients and delegated processes.
- Standard-distribution boundary: current Rust source-build runtime, hub/doors, loop, jobs, worktrees, built-in tools and supplied extensions. No published release is assumed and external cursor-delegate/supervisor is not included.
- Credited operating / distribution surfaces: [README.md](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/README.md), [docs/architecture.md](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/architecture.md), [docs/loop.md](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/loop.md), [docs/delegates.md](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/delegates.md), [crates/loop/src/step.rs](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/crates/loop/src/step.rs), [crates/main/src/delegates.rs](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/crates/main/src/delegates.rs), [crates/jobs/src/tool.rs](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/crates/jobs/src/tool.rs)
- Adjacent first-party surfaces excluded from ownership: research jigs/fakes, benchmarks, contributor workflow/CI/review agents and archived Zig code are outside deployed ownership. ADR 0005's external supervisor and third-party harness internals are not borrowed.
- First-party operating / deployment modes considered: terminal and fiber ask through shared headless session semantics; hub supervised sessions; Fiber delegates with none/worktree isolation; documented always-auto permission system and human standing rules.
- Recursion level: one parent session's current delegate-job portfolio; an external multi-harness supervisor and the maintainer organization are outside.
- Reviewed revision: 61af2a84f70a2ece2b6cf8f73a8fa70116360da7
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

Fiber separates contract vocabulary, event log, loop, providers/tools/hooks, jobs, worktrees, hub and client doors. The loop drains steering/job notices, builds a model request, authorizes model-selected calls, executes permitted calls and returns ordered results. Events are the durable state. The hub transports/listens and supplies no hidden session owner. Built-in delegate tools start separate Fiber sessions or configured external harnesses, choose model roles, carry usage/final results, steer/resume and stop jobs. Optional worktrees isolate each delegate's changes and report retained dirty branches to the parent. Auto permissions use a reviewer supplied only curated human instruction/action data; it does not inspect arbitrary tool outputs. Hooks/extensions, memory, model catalogs, quota/budget and handoffs support the current loop. No external supervisor is used to close the functions credited here.

## Operational model

The parent model and its Fiber delegate models are operational agents. The parent can inspect its job portfolio and current usage/quota, choose model/credential resources and stop/revise ongoing delegate commitments. The log, hub, budget and process-group signals enforce/transport decisions without owning them. Delegating to a third-party harness does not import that harness's internal regulatory functions.

## S1 — Operations

- State: A
- Function: model-led coding transformation
- Disturbance / variety regulated: unknown repository, shell/file outcomes and changing task observations
- Decisive decision or feedback right: choose tool call/arguments and interpret results to select the next step
- Decision owner: the current session model and Fiber delegate models
- Supporting / enforcement mechanisms: event log, step loop, provider/tool seams, permissions, retries and result delivery
- Closure path: model request → selected permitted actions → ordered results → next model step; delegate completion wakes parent
- Why this is / is not agent-owned: With model choice removed the runtime keeps transport/enforcement but no coding strategy.
- Evidence: [docs/loop.md#L31-L58](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/loop.md#L31-L58), [crates/loop/src/step.rs#L31-L61](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/crates/loop/src/step.rs#L31-L61), [crates/loop/src/turn.rs#L20-L38](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/crates/loop/src/turn.rs#L20-L38), [crates/main/src/delegates.rs#L1-L7](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/crates/main/src/delegates.rs#L1-L7)
- Basis: structural
- Confidence: medium-high
- Caveats: Pinned source establishes a supported path, not observed effectiveness or universal deployment.
- Boundary reachability: Both front doors run the same first-party loop; main builds delegates for the installed session without custom agent code.

## S2 — Coordination

- State: C
- Function: isolate concurrent delegate writers and preserve their change sets
- Disturbance / variety regulated: parent/delegates share a default workspace, so concurrent writers can interfere
- Decisive decision or feedback right: construct an isolated branch/worktree for a selected delegate and report its retained path/dirty state
- Decision owner: first-party worktree/job implementation; caller must compose the conflict-aware allocation/integration policy
- Supporting / enforcement mechanisms: isolation parameter, git worktree creation, lifetime locks, clean removal/dirty retention and completion event
- Closure path: delegate assigned own worktree → writes isolated from peers → path/branch/dirty state returned → caller can select subsequent integration or resume in retained workspace
- Why this is / is not agent-owned: C credits the supplied interference-specific isolation/feedback path. The default is none, and no autonomous coordinator is claimed merely from delegation or a lock.
- Evidence: [docs/delegates.md#L44-L68](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/delegates.md#L44-L68), [docs/delegates.md#L247-L270](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/delegates.md#L247-L270), [crates/jobs/src/delegate.rs#L226-L283](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/crates/jobs/src/delegate.rs#L226-L283), [crates/jobs/src/delegate/run.rs#L97-L129](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/crates/jobs/src/delegate/run.rs#L97-L129), [crates/worktree/src/lib.rs](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/crates/worktree/src/lib.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: No automatic merge/arbitration or mandatory isolation. External shared services and changes outside the worktree are not isolated.
- Boundary reachability: isolation:worktree is a built-in delegate argument wired by main, with real worktree lifecycle and completion reporting.
- Distinct S1 units: parent coding session and concurrent Fiber delegate sessions.
- Inter-S1 disturbance: independent workspace writers can overwrite/interleave changes when sharing the default cwd.
- Attenuating coordination relation: per-delegate worktree/branch separates write sets and preserves nonempty work at completion.
- Feedback into subsequent S1 behaviour: delegate_finished returns path/branch/dirty; resumed delegate uses its kept workspace and caller can act on the returned change boundary.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism specifically separates concurrent file-write environments and returns change-set state, rather than only moving tasks/messages.

## S3 — Inside-and-now control

- State: A
- Function: current-control of the parent session's delegate commitments/resources
- Disturbance / variety regulated: outstanding/failed/completed jobs, model/quota alternatives and continued cost commitments
- Decisive decision or feedback right: inspect portfolio, choose model roles and isolation/time commitments, steer/resume ongoing work and stop selected delegate jobs
- Decision owner: parent model within its current job tree
- Supporting / enforcement mechanisms: jobs list/wait/stop, delegate_models quota, result wake, delegate_message and process-group stop; configured budget is enforcement
- Closure path: current job/result/quota observation → parent revises commitment/resource choice or stops work → delegate runtime changes → outcome returns into parent step
- Why this is / is not agent-owned: The parent can intervene after initial decomposition; runtime's hard budget/depth/concurrency rules do not independently own its discretionary choice.
- Evidence: [crates/jobs/src/tool.rs#L17-L85](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/crates/jobs/src/tool.rs#L17-L85), [crates/main/src/delegates.rs#L37-L69](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/crates/main/src/delegates.rs#L37-L69), [docs/delegates.md#L44-L68](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/delegates.md#L44-L68), [docs/delegates.md#L123-L132](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/delegates.md#L123-L132), [crates/loop/src/step.rs#L48-L57](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/crates/loop/src/step.rs#L48-L57)
- Basis: structural
- Confidence: medium-high
- Caveats: Does not establish global fleet control or an additional parent-governed S3 mode merely because the hub exposes driver commands.
- Boundary reachability: The model receives built-in delegate/job tools; the parent drains job notices in its own step loop. No external delegation supervisor is credited.
- Whole-system current view: parent's own job list, delegate result notices and available model/quota information.
- Current-control decision scope: continued task commitments, child model/time resources and targeted stop/steer/resume within that tree.

## S3* — Complementary audit

- State: —
- Function: complementary audit
- Disturbance / variety regulated: A separately named permission reviewer is a prospective action gate, not independent verification of operational claims.
- Decisive decision or feedback right: No function-specific decisive path established.
- Decision owner: None established for this function in the assessed mode.
- Supporting / enforcement mechanisms: auto reviewer prompt selection, standing rules, hooks, event diagnostics, delegate result channels and installed extension inventory
- Closure path: No qualifying function-specific return into operations.
- Why this is / is not agent-owned: Reviewer input deliberately strips tool/file outputs and judges proposed calls against human instructions; ordinary action authorization and diagnostics do not audit completed claims. Verification gates are assigned to an external supervisor. Supplied delegate tools permit custom review but provide no additional audit-specific judgment/return constructor at this boundary.
- Evidence: [docs/permissions.md#L222-L264](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/permissions.md#L222-L264), [docs/adr/0005-the-delegation-supervisor-is-external.md#L48-L59](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/adr/0005-the-delegation-supervisor-is-external.md#L48-L59), [docs/delegates.md](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/delegates.md), [docs/architecture.md](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/architecture.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded absence at the frozen first-party distribution; arbitrary surrounding organizations and user extensions are not assessed.

### Absence scope

- Surfaces inspected: auto reviewer prompt selection, standing rules, hooks, event diagnostics, delegate result channels and installed extension inventory
- Plausible first-party paths checked: whether reviewer sees alternate operational evidence, whether an audit-specific delegate mode is shipped, and whether external supervisor verification is in-boundary
- Why no material first-party path remains: Reviewer input deliberately strips tool/file outputs and judges proposed calls against human instructions; ordinary action authorization and diagnostics do not audit completed claims. Verification gates are assigned to an external supervisor. Supplied delegate tools permit custom review but provide no additional audit-specific judgment/return constructor at this boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: outside-and-then adaptation
- Disturbance / variety regulated: model catalogs/quota, updates, memory and hooks may change present execution but do not alone generate future-facing adaptation options.
- Decisive decision or feedback right: No function-specific decisive path established.
- Decision owner: None established for this function in the assessed mode.
- Supporting / enforcement mechanisms: model-routing/configuration, supplied memory/init/hooks extensions, provider discovery, update and handoff mechanisms
- Closure path: No qualifying function-specific return into operations.
- Why this is / is not agent-owned: Catalog/quota chooses currently available resources; memory/handoff preserves information; updates/installations apply selected code. No shipped external/future option-generation and return-to-current-capability loop was established.
- Evidence: [docs/model-routing.md](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/model-routing.md), [docs/loop.md](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/loop.md), [docs/extensions.md](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/extensions.md), [docs/architecture.md](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/architecture.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded absence at the frozen first-party distribution; arbitrary surrounding organizations and user extensions are not assessed.

### Absence scope

- Surfaces inspected: model-routing/configuration, supplied memory/init/hooks extensions, provider discovery, update and handoff mechanisms
- Plausible first-party paths checked: whether external changes become prospective options that negotiate with current capability, including a supported parent mode
- Why no material first-party path remains: Catalog/quota chooses currently available resources; memory/handoff preserves information; updates/installations apply selected code. No shipped external/future option-generation and return-to-current-capability loop was established.

## S5 — Policy and identity

- State: —
- Function: identity / ultimate-policy closure
- Disturbance / variety regulated: standing rules and human escalations concern tool authority; mutable system instructions are not sufficient for S5.
- Decisive decision or feedback right: No function-specific decisive path established.
- Decision owner: None established for this function in the assessed mode.
- Supporting / enforcement mechanisms: permission reviewer, reviewer notes, standing allow/ask/deny, repository-code approval and session driver replies
- Closure path: No qualifying function-specific return into operations.
- Why this is / is not agent-owned: Rules and approvals can govern actions without providing a function-specific identity-policy dispute/decision/return path. External supervisors and maintainer governance remain outside; no autonomous or parent-governed S5 loop is credited.
- Evidence: [docs/permissions.md](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/permissions.md), [docs/invocation.md](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/invocation.md), [docs/architecture.md](https://github.com/aakshintala/fiber/blob/61af2a84f70a2ece2b6cf8f73a8fa70116360da7/docs/architecture.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded absence at the frozen first-party distribution; arbitrary surrounding organizations and user extensions are not assessed.

### Absence scope

- Surfaces inspected: permission reviewer, reviewer notes, standing allow/ask/deny, repository-code approval and session driver replies
- Plausible first-party paths checked: whether an identity/ultimate-policy matter reaches legitimate authority and returns as governing runtime policy
- Why no material first-party path remains: Rules and approvals can govern actions without providing a function-specific identity-policy dispute/decision/return path. External supervisors and maintainer governance remain outside; no autonomous or parent-governed S5 loop is credited.

## Distributed OSS parent arrangement

The repository explicitly separates process/development documents from the product. Maintainer and external supervisor decisions are not credited as deployed parent governance; user standing rules and answers retain their ordinary permission role.

## Self-hosted and non-human modes

Source-built terminal/ask/hub modes share session logic. Supervised driving is supported transport, not proof that a particular external supervisor or human closes a VSM function. Other harness delegates keep their own internals outside the credited Fiber mode.

## Recursion

Each delegate has a session and log, but that alone is not recursive viability. Image child, hub and background shell jobs are not automatically S1 viable systems.

## Variety and escalation

Event streams preserve action/usage identity; bounded final notices attenuate larger results with full artifacts available. Worktree feedback preserves writer boundaries. Budget exhaustion stops delegate commitments under a configured rule; stop enforcement is separate from who chose the commitment.

## Evidence gaps

Static source review of current source-build distribution. Cargo absent; no build/native Rust tests or provider-backed task was run. Generic extensions/user skills and external supervisors may add functions but are not silently incorporated; no performance or independent audit claim.

## Index execution provenance

Frozen intake #2176, serial controller #2177, row 4. Source assessment is the executing Index S1 actor's work; GitHub, deterministic checks and CI are supporting machinery. No independent semantic review or autonomy grade is claimed. Proposed publication precedes a separate canonical transaction.
