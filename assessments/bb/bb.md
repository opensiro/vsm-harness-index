---
harness_id: bb
project_name: bb
repository: https://github.com/get-bb/bb
review_ref: c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# bb

## Review boundary

- System in focus: the first-party self-hosted bb runtime at frozen revision `c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf`, including the server, host daemon, app/CLI/SDK, provider-backed coding threads, managed environments/worktrees, child-thread relationships and first-party bundled/official orchestration plugins in documented reachable modes.
- Purpose and identity: operate a programmable workspace/agentic IDE in which users and model-backed coding agents can execute software-engineering work, create and coordinate other threads, isolate parallel work, inspect live progress and steer or stop current work.
- Relevant environment: user objectives and steering, project repositories/workspaces, Git/worktree state, child-thread status/results, provider/model responses, shell/tool/test evidence, connected execution hosts and first-party plugin state.
- Standard-distribution boundary: shipped bb runtime and first-party bundled/official plugins only when their documented enabled modes are explicitly claimed. External model providers, host toolchains, external MCP/services, user-authored workflow scripts/prompts, marketplace/third-party plugins, get-bb repository maintenance/CI and personal maintainer configurations cannot donate organizational ownership.
- Credited operating / distribution surfaces: server/daemon thread lifecycle, `bb` CLI and SDK, managed environments/worktrees, parent/child threads, thread status/messaging/stop controls, and the bundled Tasks/Workflows/Automations surfaces only where the function is already instantiated by first-party runtime behavior.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/QA and development-only fixtures; getbb.app marketing/cloud-account services except where necessary to explain a shipped runtime interface; personal manager recipes as organizational owners; third-party marketplace plugins such as SlopCop.
- First-party operating / deployment modes considered: ordinary coding threads; parent/child cross-provider delegation; manager-thread coordination; separate managed worktrees; direct thread listing/steering/stopping; enabled first-party Tasks and Workflows plugins; scheduled wake-ups through the first-party Automations mechanism; operator steering/permission modes.
- Recursion level: one bb project/work organization inside one bb installation. Provider-backed coding threads are operational S1 units; a model-backed parent/manager thread can regulate the current set of child/project threads. The user remains the external parent/operator unless a parent-mode annotation is explicitly claimed.
- Reviewed revision: `c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf`.
- Observation date: 2026-10-06.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

bb separates a central stateful server from host daemons that provision workspaces and run provider processes. Threads are the unit of work, emit durable event streams and can own child threads. The system overview explicitly distinguishes standard threads that do work directly from manager threads that coordinate other threads. The app follows and steers work; the CLI is a first-class interface for users and agents.

The agent-facing CLI exposes thread creation, inspection, messaging and lifecycle operations. A parent can spawn children in the same or another project, select an execution machine/environment and create a separate Git worktree. Child threads report turns/blockers to their parent. Project-wide thread listing exposes status and parent relationships, while `bb thread tell` can steer an active turn and lifecycle commands can stop or archive work.

First-party orchestration plugins add stronger structured modes. Tasks connects tracked work to delegated worker threads and can notify/resume the last responding worker. Workflows fans work across ordinary worker threads, exposes durable phase/worker progress and supports cancellation, concurrency/call budgets, retries and result collection. These mechanisms strengthen observability/enforcement, but positive classifications below rest on model-owned decisions rather than deterministic limits alone.

## Operational model

An active coding thread is a model-backed operational actor. It receives the bb CLI and thread context as an agent-accessible orchestration surface, so a parent agent can create sibling/child work, inspect live thread state, send corrective input and stop work without requiring the human to make each substantive coordination decision.

Parallel coding can be separated into different Git worktrees. First-party product documentation describes that isolation specifically as the way to prevent parallel agents from overwriting one another's changes. This establishes a concrete inter-S1 disturbance and attenuation path rather than treating generic delegation as S2.

Complementary audit is reachable through a separate child thread. The first-party software-factory guide gives the explicit example of one coding agent spawning a different-provider worker to review its code; when the reviewer finishes, the parent is notified and can implement the feedback. That independent model context and return path are the basis of S3*, not ordinary self-review.

## S1 — Operations

- State: A
- Function: autonomously perform open-ended software-engineering work in a project through provider-backed coding threads with repository, shell/tool and environment access.
- Disturbance / variety regulated: unfamiliar code, implementation choices, test/build/tool failures, repository state, provider/model variability, user feedback and execution-environment constraints.
- Decisive decision or feedback right: choose substantive engineering actions, interpret tool/repository evidence, revise implementation and decide when the assigned objective is complete.
- Decision owner: the active model-backed coding thread.
- Supporting / enforcement mechanisms: server/daemon runtime, provider adapters, environments, workspace tools, permission modes, event persistence, app/CLI/SDK and thread lifecycle.
- Closure path: user/parent objective → coding agent chooses and executes repository/tool actions → runtime returns evidence → agent repairs/revises/verifies → result returns to parent/user or closes the thread.
- Boundary reachability: ordinary packaged bb operation instantiates provider-backed threads through the app, CLI, HTTP API and SDK; no optional multi-agent plugin is required for the base S1 path.
- Why this is / is not agent-owned: deterministic runtime code hosts and constrains execution, but removing the provider-backed model removes the open-ended engineering decisions.
- Evidence: [packages/bb-app/README.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/packages/bb-app/README.md); [docs/system-overview.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/docs/system-overview.md); [docs/repository-overview.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/docs/repository-overview.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external provider cognition is a dependency, but the assessed harness first-party runtime creates the operating thread, exposes the work environment/tools and closes the execution loop around that model.

## S2 — Coordination

- State: A
- Function: attenuate destructive interference among concurrently active coding threads by placing peer work into separate managed Git worktrees/environments and by choosing dependency/communication boundaries between child tasks.
- Disturbance / variety regulated: parallel agents overwriting each other's repository changes, conflicting workspace mutation and coordination failures between parent/child work.
- Decisive decision or feedback right: decide whether delegated work should run as a separate child and select a new worktree/environment for that work instead of sharing the current checkout.
- Decision owner: the model-backed parent/manager thread when it uses the agent-facing `bb thread` orchestration path.
- Supporting / enforcement mechanisms: managed environment/worktree provisioning, parent/child thread links, environment ownership, Git/workspace inspection and child completion/blocker notifications.
- Closure path: parent agent decomposes work → spawns peer/child work in an isolated worktree when concurrent mutation could collide → bb provisions the separate environment → child operates on its own checkout → child status/result returns to the parent → parent integrates or redirects subsequent work.
- Boundary reachability: the first-party CLI given to agents supports `bb thread spawn` with `--new-environment worktree`; the product's parallel-agent documentation explicitly recommends one Git worktree per thread to prevent agents overwriting one another.
- Why this is / is not agent-owned: worktree provisioning is deterministic enforcement, but the model parent owns the discretionary decomposition and environment/isolation choice that defines the coordination relation.
- Distinct S1 units: two or more provider-backed coding threads performing independent software-engineering work.
- Inter-S1 disturbance: concurrent threads can overwrite or invalidate one another's changes when they mutate the same checkout.
- Attenuating coordination relation: per-thread Git worktree/environment isolation plus parent/child task boundaries.
- Feedback into subsequent S1 behaviour: the chosen environment changes where the child may read/write; child completion/blocker reports return to the parent and determine integration, follow-up or redirection.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the first-party documentation ties separate worktrees to the concrete peer-S1 mutation hazard of agents overwriting each other's changes, and the parent-agent spawn decision changes the operational execution boundary.
- Evidence: [apps/web/src/compare/compare-content.tsx](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/apps/web/src/compare/compare-content.tsx); [plugins/bb-guide/skills/bb-cli/references/thread-creation.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/plugins/bb-guide/skills/bb-cli/references/thread-creation.md); [docs/system-overview.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/docs/system-overview.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: sharing one environment remains possible; the positive claim is for the documented isolated multi-thread mode, not for every parallel bb deployment.

## S3 — Inside-and-now control

- State: A
- Function: maintain a live view of current project/thread commitments and regulate them through selective delegation, status inspection, steering, waiting and lifecycle control.
- Disturbance / variety regulated: blocked, idle, active, failed or misdirected workers; changing current priorities; child blockers; work that must be stopped, redirected or continued.
- Decisive decision or feedback right: inspect the current project/child thread set, choose new delegated work, send immediate corrective input to a selected active thread, wait for work, or stop/archive selected work.
- Decision owner: the model-backed parent/manager thread using the first-party agent CLI.
- Supporting / enforcement mechanisms: project/parent-filtered `bb thread list` and counts, thread status/activity, child reporting, `bb thread tell` steering/queueing, spawn/wait/stop/archive operations, durable events and first-party Tasks/Workflows progress surfaces.
- Closure path: manager/parent inspects current thread state → chooses a current control response (spawn/wait/steer/stop/redirect) → bb executes the lifecycle/message operation → updated thread state/result returns through list/status/events/parent notification → manager makes the next current decision.
- Boundary reachability: the CLI is explicitly first-class for agents; bb's system overview defines manager threads as coordinating other threads, and the agent guide exposes list/status/message/lifecycle operations in ordinary supported runtime.
- Why this is / is not agent-owned: server/daemon state and lifecycle APIs provide observability/enforcement, but the parent model chooses the substantive response to the current worker situation.
- Whole-system current view: project-filtered thread listing/counts expose the current thread set with statuses, parent relationships and activity; manager/parent context also exposes its children and notifications.
- Current-control decision scope: create/delegate work, select environment/provider, steer an active turn, queue follow-up input, wait, stop or archive a selected thread and react to child completion/blockers.
- Evidence: [docs/system-overview.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/docs/system-overview.md); [plugins/bb-guide/skills/bb-cli/references/thread-operation.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/plugins/bb-guide/skills/bb-cli/references/thread-operation.md); [plugins/bb-guide/skills/bb-cli/references/thread-creation.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/plugins/bb-guide/skills/bb-cli/references/thread-creation.md); [packages/templates/src/templates/bb-guide-json.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/packages/templates/src/templates/bb-guide-json.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: deterministic Workflow concurrency limits and UI dashboards are supporting mechanisms, not the S3 owner; the A state rests on the model-accessible current-control path.

## S3* — Complementary audit

- State: A
- Function: independently challenge implementation claims through a separate fresh coding-agent thread that reviews the parent's work and returns findings before the parent proceeds.
- Disturbance / variety regulated: incorrect implementation claims, defects or omissions that the authoring thread may miss through self-review.
- Decisive decision or feedback right: independently inspect the code/repository in a separate model context and return review findings that can change the parent agent's subsequent implementation.
- Decision owner: the separately spawned reviewer model/thread.
- Supporting / enforcement mechanisms: cross-provider child-thread creation, separate thread/provider context, repository/environment access, parent notification on child completion and parent-to-child messaging.
- Closure path: authoring/manager thread produces work → spawns a separate reviewer child (including a different provider) → reviewer directly inspects the code and produces findings → bb reports child completion/output to the parent → parent implements feedback or otherwise resolves the findings.
- Boundary reachability: first-party bb product documentation gives this exact cross-provider reviewer pattern as a normal child-thread use case; it uses the shipped child-thread/notification path rather than a third-party plugin.
- Why this is / is not agent-owned: the substantive review judgment is made by a separate model instance with direct repository access; bb's notification/routing only carries the independent finding back.
- Claim being audited: correctness/readiness of code produced by the ordinary authoring thread.
- Ordinary reporting path: the authoring thread's own implementation, test evidence and completion account.
- Complementary access path: a separate child coding thread directly inspects the repository/change, optionally using a different provider/model.
- Independence boundary: separate provider-backed thread/context with its own model execution; the documented example explicitly uses a different-provider reviewer.
- Who acts on findings: the parent authoring/manager thread receives completion and can implement the review feedback before proceeding.
- Evidence: [apps/web/src/blog/posts/building-a-restrained-software-factory.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/apps/web/src/blog/posts/building-a-restrained-software-factory.md); [plugins/bb-guide/skills/bb-cli/references/thread-creation.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/plugins/bb-guide/skills/bb-cli/references/thread-creation.md); [apps/server/src/services/threads/child-thread-notifications.ts](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/apps/server/src/services/threads/child-thread-notifications.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: bb does not require every coding task to pass this reviewer path. The positive claim is for the documented first-party child-review operating mode, not a universal completion gate.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party outside-and-prospective intelligence function is established at the declared project recursion.
- Disturbance / variety regulated: long-lived manager examples can be configured to inspect changing external issues/submissions, but no shipped function-specific actor is established that autonomously converts those external/future distinctions into adaptation options and closes them into current S3.
- Decisive decision or feedback right: none established for S4 inside the standard-distribution boundary.
- Decision owner: none established.
- Supporting / enforcement mechanisms: durable thread history, scheduled wake-ups/Automations, manager context, Tasks, provider tools and Workflows can support a user-composed intelligence loop but do not themselves own one.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: first-party product writing demonstrates that users can configure long-lived managers to inspect marketplace submissions or issues, but those task-specific manager instructions/configurations are personal compositions rather than a shipped S4-specific decision function.
- Evidence: [apps/web/src/blog/posts/building-a-restrained-software-factory.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/apps/web/src/blog/posts/building-a-restrained-software-factory.md); [plugins/workflows/README.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/plugins/workflows/README.md); [docs/VISION.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/docs/VISION.md).
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: bb is unusually capable of hosting an S4 arrangement; the negative state is specifically because generic manager/prompt/scheduling composability is not promoted to a first-party S4 owner.

### Absence scope

- Surfaces inspected: manager/child-thread model, first-party software-factory manager examples, Automations/scheduled wake-up behavior, Tasks, Workflows, thread persistence, provider/tool access and project control surfaces.
- Plausible first-party paths checked: recurring external issue/market scanning, future-oriented option generation, autonomous capability/workflow adaptation and return of selected adaptations into current project control.
- Why no material first-party path remains: the external/prospective objective and adaptation policy come from user-authored manager instructions or external integrations; shipped primitives supply execution/scheduling/orchestration rather than the S4-specific substantive intelligence function.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established at the declared project recursion.
- Disturbance / variety regulated: permissions, machine ceilings, provider settings and user steering constrain current operation, but no identity-level or ultimate-policy issue is routed to an authoritative S5 owner and returned as governing organizational policy.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: permission modes, machine `maxPermissionMode`, user approvals, provider/config settings, plugin settings and runtime policy enforcement.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: model agents operate under these externally authored constraints; neither ordinary manager control nor permission administration establishes authority to redefine the bb project's identity or ultimate governing principles.
- Evidence: [plugins/bb-guide/skills/bb-cli/references/thread-creation.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/plugins/bb-guide/skills/bb-cli/references/thread-creation.md); [docs/VISION.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/docs/VISION.md); [packages/bb-app/README.md](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/packages/bb-app/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: the installation owner has legitimate authority over permissions and configuration, but operational permission policy is not automatically VSM S5 identity/ultimate-policy closure.

### Absence scope

- Surfaces inspected: permission modes/approval behavior, machine permission ceilings, provider/configuration settings, manager/task/workflow controls, product vision and operator control surfaces.
- Plausible first-party paths checked: constitutional/identity revision, authoritative resolution of competing system purposes, runtime policy-authoring actor and identity-policy feedback into S3.
- Why no material first-party path remains: all identified first-party policy surfaces are operational constraints/settings or externally supplied objectives rather than a substantive identity/ultimate-policy decision loop.

## Distributed OSS parent arrangement

The assessed organization is the running bb project/work organization, not the get-bb GitHub maintainer organization. Repository contribution practices, CI, release management and the maintainers' own use of bb are not imported as runtime S3/S4/S5 ownership.

## Self-hosted and non-human modes

bb is explicitly self-hostable and provider-agnostic across supported coding-agent providers. Positive S1–S3* claims do not depend on a specific vendor model. Human app/CLI steering is available, but no parent-mode annotation is needed for the claimed vector because the positive decision paths identified here can be exercised by model-backed bb threads through first-party agent-accessible controls.

## Recursion

At the selected recursion, provider-backed coding threads are operational S1 units. A parent/manager thread can create and regulate the current worker set, while separate reviewer children can provide complementary assurance. Server, daemon, database, UI, worktrees, Tasks and Workflows are supporting/control mechanisms unless a model-owned function-specific decision path is identified.

## Variety and escalation

S1 absorbs ordinary coding variety. S2 attenuates a concrete parallel-mutation hazard through isolated worktrees. S3 handles live worker/current-commitment variety through model-accessible inspection and targeted lifecycle/messaging controls. S3* can challenge author claims through an independent child reviewer. Higher prospective-intelligence and identity-governance functions are not credited from generic scheduling, persistence, plugins, prompts or permissions.

## Evidence gaps

No `?` state is required. The main residual uncertainty is classification strength for S3*: the reviewer mode is explicitly documented and fully reachable through first-party child-thread mechanisms, but it is an optional operating mode rather than a mandatory gate. Under Methodology 0.3.6 that affects universality, not the existence of the autonomous first-party mode, so the proposed state remains `A`.
