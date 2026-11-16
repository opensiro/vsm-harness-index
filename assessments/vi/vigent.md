---
harness_id: vigent
project_name: vigent
repository: https://github.com/farming-labs/vigent
review_ref: 16a071f366c6507c7f275008e3af4009488884cc
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# vigent

**Canonical disposition:** `excluded-no-agentic-vsm`. Vigent ships substantial supervision, isolation and review of separately installed agent harnesses. The reviewed distribution does not close the agent-owned S1 loop required for inclusion in the general Index.

## Review boundary

- System in focus: One installed vigent TUI instance with its native worktree and CLI orchestration.
- Purpose and identity: Operator-controlled supervision of separate coding-agent harnesses and their proposed work.
- Relevant environment: Git repository, worktrees, operator, independently installed coding CLIs and available registry configuration.
- Standard-distribution boundary: The npm CLI implementation and the standalone Rust binary, including adapter/process supervision, worktrees, race, review, registry and trust.
- Credited operating / distribution surfaces: Shipped external CLI launch adapters, Pi RPC, worktree setup, session UX, landing hooks, registry and trusted project settings.
- Adjacent first-party surfaces excluded from ownership: Scripted demo, old design notes, test fixtures and external agent execution loops, plugins and provider credentials.
- First-party operating / deployment modes considered: npm package and standalone binary, independently installed native and Pi RPC engines, project and user settings.
- Recursion level: One launch/worktree supervisor instance. Instantiated engine processes are controlled external workers with their own agent loop.
- Reviewed revision: `16a071f366c6507c7f275008e3af4009488884cc`
- Observation date: 2026-11-16
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Vigent supplies a Vim-oriented terminal UI over sessions, process adapters and worktrees. Both npm and Rust paths start separately installed engines and consume their streamed events. The old design describes an intended in-process Pi integration. In the reviewed tree the bundled Pi adapters use an external process for RPC, and other adapters launch independent coding CLIs.

## Operational model

The user chooses a task, engine, worktree and follow-up. The independent agent executes its own model/tool loop. Vigent exposes process results and supports comparison, review, integration and host trust decisions. The checked boundary is the installed orchestrator.

## S1 — Operations

- State: —
- Function: Operate on a coding task by repeatedly choosing and applying actions against feedback.
- Disturbance / variety regulated: Task variety, edits, subprocess responses and failed coding operations.
- Decisive decision or feedback right: Choose the next code/tool action and revise it using task or tool feedback.
- Decision owner: Each independently installed coding CLI on the chosen run; the local operator originates and steers prompts.
- Supporting / enforcement mechanisms: Engine adapters, prompt/session transport, tool event display, isolated worktrees and input queues.
- Closure path: The external CLI owns the model request, tool dispatch and subsequent inferences. Vigent sends prompts and receives process output.
- Why this is / is not agent-owned: Process supervision and event parsing do not choose a task action. Removing the independent CLI leaves a terminal controller and no task agent.
- Evidence: [crates/vigent/src/engines/run.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/engines/run.rs#L17-L71), [crates/vigent/src/engines/pi.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/engines/pi.rs#L1-L31), [src/pi-session.ts](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/src/pi-session.ts#L74-L126), [src/cli-engines.ts](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/src/cli-engines.ts#L1-L87), [README.md](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/README.md#L1-L13).
- Basis: Shipped Rust and npm launch paths at the pinned commit.
- Confidence: High.
- Caveats: Scripted demo output cannot establish the normal execution boundary.

### Absence scope

- Surfaces inspected: Rust spawned CLI and Pi RPC adapters, npm engine and Pi bootstrap, documented regular and demo modes.
- Plausible first-party paths checked: Cross-engine adapter, the standalone binary, old in-process Pi design and the scripted demo.
- Why no material first-party path remains: Both current package paths drive separately supplied agent processes. The historical design's embedded Pi assumption does not match either launch path.

## S2 — Coordination

- State: —
- Function: Coordinate agent operations inside the scope of an autonomous project harness.
- Disturbance / variety regulated: Concurrent tool effects and multiple attempts at the same work.
- Decisive decision or feedback right: Own a first-party peer interference decision and returned behavioural change between in-boundary agent operations.
- Decision owner: No first-party S1 actor pair at the assessed boundary. The operator chooses race contestants and retention, and the worktree runtime enforces separation.
- Supporting / enforcement mechanisms: Reserved branch/file names, distinct worktree paths, race grouping, operator comparison and cleanup.
- Closure path: External agents write only to their supplied working directories. The race UI presents outcomes and the operator selects an attempt to keep.
- Why this is / is not agent-owned: Worktree isolation and cleanup supply genuine coordination support for external workers. They do not supply a first-party peer decision or in-boundary autonomous operational units.
- Evidence: [crates/vigent/src/worktree.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/worktree.rs#L97-L124), [crates/vigent/src/race.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/race.rs#L272-L329), [crates/vigent/src/race.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/race.rs#L502-L559), [README.md](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/README.md#L34-L45).
- Basis: Worktree planning and race launch/retention code.
- Confidence: High.
- Caveats: The exclusion does not deny filesystem isolation or coordinated human supervision.

### Absence scope

- Surfaces inspected: Per-agent worktree allocation, race supervision, worktree reservation and per-session follow-ups.
- Plausible first-party paths checked: Worktree conflict avoidance, race arbitration and cross-engine handoff.
- Why no material first-party path remains: The operation owner lies in the external CLI. Vigent has fixed worktree separation and operator-selected retention; its shipped peer paths do not instantiate an agent organization within this boundary.

## S3 — Inside-and-now control

- State: —
- Function: Make current portfolio decisions for an agent-owned coding organization.
- Disturbance / variety regulated: Uneven progress, failed jobs and resource or integration conflicts.
- Decisive decision or feedback right: Decide how to change live obligations or allocation across operating units.
- Decision owner: The local operator decides which session to start, steer or stop, and which work to retain or land.
- Supporting / enforcement mechanisms: Session sidebar, project dashboard, race comparison, merge commands and code-path status.
- Closure path: Operator commands are returned to the selected child process or branch; terminal events update the control surface.
- Why this is / is not agent-owned: This is a substantial current-control surface for a human operating external workers. The installed supervisor does not itself own a model-backed portfolio decision.
- Evidence: [crates/vigent/src/actions/sessions.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/actions/sessions.rs#L7-L62), [crates/vigent/src/race.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/race.rs#L502-L559), [crates/vigent/src/engines/handoff.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/engines/handoff.rs#L1-L38), [README.md](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/README.md#L66-L85).
- Basis: First-party operator command/control and process event sources.
- Confidence: High.
- Caveats: Human live controls remain part of the product even though the record is excluded from the autonomous harness corpus.

### Absence scope

- Surfaces inspected: Current sessions, user model switching, race selection and landing.
- Plausible first-party paths checked: An aggregate model controller, automatic race selection and automatic takeover on failure.
- Why no material first-party path remains: The reviewed paths route the operator's decisions and expose external status. They do not install an autonomous current-control actor for the product's own operational units.

## S3* — Complementary audit

- State: —
- Function: Independently audit claims from an in-boundary agent organization.
- Disturbance / variety regulated: External agents' summaries may diverge from their actual output or test results.
- Decisive decision or feedback right: Bind a complementary observer to a claim and return a corrective judgment to control.
- Decision owner: No shipped agentic audit decision in the assessed boundary. The operator inspects diffs and may configure a landing gate.
- Supporting / enforcement mechanisms: Raw diff/hunk views and optional before_merge commands run in the worktree.
- Closure path: The gate permits landing on success and returns failure to the current acceptance flow.
- Why this is / is not agent-owned: Patch inspection and the configured acceptance gate provide meaningful evidence. Neither creates a distinct first-party audit role for the external engine's claims.
- Evidence: [crates/vigent/src/review/hooks.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/review/hooks.rs#L33-L70), [README.md](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/README.md#L38-L48), [README.md](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/README.md#L88-L101).
- Basis: Review UI, landing gates and documented acceptance flow.
- Confidence: Medium-high.
- Caveats: A custom hook may implement additional checks under another deployment boundary.

### Absence scope

- Surfaces inspected: Diff and hunk review, pre-landing checks, external tool events and race comparisons.
- Plausible first-party paths checked: A side-channel reviewer of actual work, a pre-landing native verifier and a peer race as a check.
- Why no material first-party path remains: The available output evidence supports ordinary acceptance and user inspection. No standard mode binds a distinct audit actor and corrective return on operational claims.

## S4 — Outside-and-then intelligence

- State: —
- Function: Assess prospective changes and adopt capability for a first-party autonomous agent organization.
- Disturbance / variety regulated: New engine/setup requirements and future team workflows.
- Decisive decision or feedback right: Choose and return a prospective change in the harness capability envelope.
- Decision owner: The local user selects registry items or settings; the registry loader transports and installs that choice.
- Supporting / enforcement mechanisms: Registry descriptions and preview, config merge, engine/template entries and confirmed writes.
- Closure path: The requested registry item writes the selected configuration for subsequent use.
- Why this is / is not agent-owned: The registry is a first-party human-operated extension and adoption path. The reviewed package does not operate a strategy loop for in-boundary agents.
- Evidence: [crates/vigent/src/registry.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/registry.rs#L347-L405), [README.md](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/README.md#L88-L117), [crates/vigent/src/engines/handoff.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/engines/handoff.rs#L1-L38).
- Basis: Installed registry plan and user confirmation source.
- Confidence: High.
- Caveats: Future configuration can materially change the operator's options.

### Absence scope

- Surfaces inspected: Registry, setup and config changes, model handoff and external engine adapters.
- Plausible first-party paths checked: User adoption of external engine/setup items and switching live engines as prospective adaptation.
- Why no material first-party path remains: Registry selection remains operator-directed and external engines retain the resulting agent decisions. Model handoff carries an existing session to a user-selected engine, rather than choosing future organizational strategy.

## S5 — Policy and identity

- State: —
- Function: Govern the ultimate operating identity for an in-boundary agent organization.
- Disturbance / variety regulated: A project configuration can introduce executable hooks, engines or commands.
- Decisive decision or feedback right: Authorize the standing project execution policy and return the decision into operations.
- Decision owner: The human operator of vigent owns configuration trust; the externally installed engines own their own task and permission decisions.
- Supporting / enforcement mechanisms: Project file hash, gated config entries, trust state and refresh of active settings.
- Closure path: Trust binds the selected file content and enables its admitted configuration. Changed content requires a new trust decision.
- Why this is / is not agent-owned: The standing trust mechanism is implemented in vigent as a human host policy. It does not establish first-party agent identity or autonomous operating ownership for this Index boundary.
- Evidence: [crates/vigent/src/trust.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/trust.rs#L1-L10), [crates/vigent/src/trust.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/trust.rs#L84-L109), [crates/vigent/src/trust.rs](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/crates/vigent/src/trust.rs#L119-L154), [README.md](https://github.com/farming-labs/vigent/blob/16a071f366c6507c7f275008e3af4009488884cc/README.md#L88-L101).
- Basis: First-party trust storage and live reload path.
- Confidence: High.
- Caveats: The protection concerns project configuration and its associated adapter commands and hooks.

### Absence scope

- Surfaces inspected: Project trust and configuration reload, engine permission options and per-session actions.
- Plausible first-party paths checked: Durable host trust change, executable config gating and imported engine permissions.
- Why no material first-party path remains: These paths implement durable human policy for an orchestrator of external workers. The qualifying autonomous agent organization whose identity could be governed is absent from the assessed distribution.

## Distributed OSS parent arrangement

Vigent's project operator owns standing trust and output-admission decisions. External coding-agent maintainers and session actors are outside the assessed product boundary.

## Recursion

Each supervised engine runs in its own process/worktree and owns a separate tool loop. Vigent exercises process and worktree envelope control over that runtime.

## Variety and escalation

The TUI shows status and failures, the operator can choose an engine switch or restart, and worktree and hook gates bound operational effects.

## Evidence gaps

The finding is source-relative to the frozen revision. No live model, external engine or pre-landing hook was executed. Operator-facing functionality was inspected as source without a separate assessment of any launched engine.
