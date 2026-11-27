---
harness_id: hadal
project_name: Hadal
repository: https://github.com/T-Crypt/hadal
review_ref: b6eea00a3058491f185c0bcc76ac550caa54e098
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# Hadal

## Review boundary

- System in focus: A self-hosted Hadal installation with sessions, local workspaces, optional stage router and owner-facing Lantern.
- Purpose and identity: Carry out assigned workspace work and supervise multiple durable sessions.
- Relevant environment: Local or cloud model accounts, workspaces and optionally a shared llama-swap GPU.
- Standard-distribution boundary: The packaged Hadal server and UI, bundled tools, router, Lantern and approval-backed memory. Pi Durable provides the embedded runtime substrate.
- Credited operating / distribution surfaces: Workspace session execution, supported GPU mode, bundled router, Lantern and operator settings.
- Adjacent first-party surfaces excluded from ownership: Provider services, external repository governance, example sites and release/development workflows.
- First-party operating / deployment modes considered: Ordinary sessions, linked and subordinate sessions, standard stage router, owner supervision and approved lessons.
- Recursion level: One Hadal installation and its operational sessions. The complementary audit has a narrower router-run boundary.
- Reviewed revision: b6eea00a3058491f185c0bcc76ac550caa54e098
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Hadal constructs a durable agent runtime backed by SQLite and registers its environment and tools. Sessions can work independently in separate worktrees. The packaged router delegates configured stages to fresh agents. Lantern sees and acts across sessions in its authorized scope, and the operator can inspect spend and change constraints. A scoped memory flow carries approved lessons into later prompt assembly.

## Operational model

Each working session owns task actions and their responses to workspace evidence. A router can own current stage commitments. Lantern reads current sessions and chooses how to use them to carry out the operator's current authorized objective. The application enforces admission, spend, permissions and durable state.

## S1 — Operations

- State: A
- Function: Perform workspace and coding tasks in an installed session.
- Disturbance / variety regulated: Changing project inputs, task requirements and tool outcomes.
- Decisive decision or feedback right: Choose work actions and revise them from observations.
- Decision owner: Model in the shipped model-backed Hadal session.
- Supporting / enforcement mechanisms: Embedded Pi Durable runtime, registered tools, workspace execution environment and persisted commits.
- Closure path: Session selects tools, observes results and continues until an answer or a runtime limit.
- Boundary reachability: Hadal opens the durable runtime with its registered tools and execution environment in its supported self-hosted distribution.
- Why this is / is not agent-owned: The runtime persists and executes work. Removing the model removes the decisions about which work to perform.
- Evidence: [README.md](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/README.md#L54-L64), [package.json](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/package.json#L28-L42), [src/server/app.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/app.ts#L1103-L1138)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: Model providers are configured dependencies. Package installation and live inference were not exercised.

## S2 — Coordination

- State: C
- Function: Attenuate contention between independent sessions using different models on one GPU.
- Disturbance / variety regulated: Alternating requests evict models and delay both independent agency loops.
- Decisive decision or feedback right: Choose a response to competing model use when the shared card cannot serve both models efficiently.
- Decision owner: The shared model lane supplies an interference-specific regulation path. Composition would be needed for an autonomous owner to change its policy.
- Supporting / enforcement mechanisms: GPU model acquisition and release, turn-completion feedback and grouped admission.
- Closure path: Pending model requests wait until a turn is available. A tool-use result can hold the current model for the continuation so queued work changes execution timing.
- Boundary reachability: The app installs a first-party request wrapper for the supported llama-swap model path.
- Why this is / is not agent-owned: The lane executes a fixed prescription. It does not give a model authority to set cross-session resource arbitration.
- Distinct S1 units: Independent work sessions and active subagents issuing requests for their own tasks.
- Inter-S1 disturbance: Contention for resident models on one local inference card causes frequent model swaps and interrupts ongoing loops.
- Attenuating coordination relation: A model-aware shared-card lane preserves a running model across tool turns and waits to admit conflicting requests.
- Feedback into subsequent S1 behaviour: Tool-use completion can retain the lane, while release allows waiting sessions to acquire it and resume inference.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The lane regulates concrete interference from incompatible model residency across the operating sessions.
- Evidence: [docs/features.md](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/docs/features.md#L74-L75), [src/server/app.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/app.ts#L5045-L5092)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: The witness is specific to supported shared-card deployments.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate active session commitments and resources on behalf of the local installation.
- Disturbance / variety regulated: Multiple live sessions can carry changing tasks, blocked approvals and spending demands.
- Decisive decision or feedback right: Choose where to assign or steer currently authorized work and how to act on blocked or resource-constrained commitments.
- Decision owner: Lantern model within standing or current delegated work. Owner remains the current budget and intervention authority in the supervised path.
- Supporting / enforcement mechanisms: Current session inventory, session reads, steering, return reports, spend view and enforcement.
- Closure path: Lantern reads the current sessions, changes a worker's current task or starts separate work and receives outcomes. The owner can receive the active status and change spend limits or intervene via the session control path.
- Boundary reachability: Lantern is a bundled extension with tool registry integration. Its tool decisions and the owner's live controls both reach the installed sessions.
- Why this is / is not agent-owned: The model chooses and issues an authorized steering response. A distinct parent path returns the owner's resource or intervention decision into ongoing work.
- Whole-system current view: Lantern can inspect visible sessions, their current state and results. The owner sees Running now and spend across sessions.
- Current-control decision scope: Select, redirect or hold current session commitments. The owner can apply live spend limits or act on blocked sessions.
- Evidence: [src/server/extensions/pip.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/extensions/pip.ts#L77-L89), [src/server/extensions/pip.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/extensions/pip.ts#L365-L399), [docs/features.md](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/docs/features.md#L47-L51)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: Lantern's authority is bounded by the owner's instructions. The app reserves some approvals, stops and model selection to people or explicit prior mandates.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Lantern model | Authorized work needs selection or redirection across current sessions. | Read live status, choose the session and steer it, then receive the result. | [src/server/extensions/pip.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/extensions/pip.ts#L77-L89), [src/server/extensions/pip.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/extensions/pip.ts#L365-L399) |
| Parent (`P`) | Installation owner | Live session/portfolio oversight with a resource or intervention decision. | Owner applies live limits or uses the current session control, which changes subsequent operation. | [docs/features.md](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/docs/features.md#L47-L51), [docs/features.md](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/docs/features.md#L16-L16) |

## S3* — Complementary audit

- State: A
- Function: Cross-check a router implementation's completion claims directly against code and tests.
- Disturbance / variety regulated: The implementation report can miss defects, failed edge cases or code paths affected by the change.
- Decisive decision or feedback right: Decide what underlying artifacts to inspect and which findings must be repaired before progression.
- Decision owner: Fresh reviewer stage agent in the shipped standard router.
- Supporting / enforcement mechanisms: Router dispatch, fresh stage contexts, workspace tools, independent findings file and ordered stage controls.
- Closure path: The reviewer inspects code and tests and records findings. The router sends the fix agent to those findings and re-runs review as needed.
- Boundary reachability: The distribution includes the standard router with review and fix templates and the stage-specific subagent path.
- Why this is / is not agent-owned: The reviewer independently selects the evidence and findings. The router uses them for current execution decisions.
- Claim being audited: The implementation meets the plan and work requirements.
- Ordinary reporting path: Implementation stage response and shared run artifacts.
- Complementary access path: The review stage reads the actual diff, exercises tests and inspects callers.
- Independence boundary: A fresh stage agent gets its own context. It may use the same model weights and reads the shared run folder.
- Who acts on findings: The router assigns a fix stage and may run review again before progression.
- Evidence: [src/server/routers.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/routers.ts#L90-L126), [src/server/routers.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/routers.ts#L130-L159), [src/server/routers.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/routers.ts#L192-L208)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: The witness is the configured standard router mode. A plain chat does not run this reviewer.

## S4 — Outside-and-then intelligence

- State: P
- Function: Keep future sessions aligned with durable changes in working environments and user practices.
- Disturbance / variety regulated: Repository conventions, work procedures or operator preferences can change between sessions.
- Decisive decision or feedback right: Decide whether a proposed cross-session lesson governs subsequent work.
- Decision owner: Installation owner who approves, rejects or changes a scoped lesson.
- Supporting / enforcement mechanisms: Memory tool, pending lessons, review and exact-content approval, and prompt assembly.
- Closure path: The session proposes durable changes from project or user evidence. The approval updates in-force memory reinserted into later sessions' prompts.
- Boundary reachability: The first-party memory extension and controls implement the proposal, owner decision and re-use in affected sessions.
- Why this is / is not agent-owned: The model detects and proposes prospective lessons. The owner has the decisive right to put a proposed change into force.
- External distinction: Project documentation/conventions and operator requests encountered by the session.
- Future / prospective distinction: A lesson is proposed for reuse beyond this task, at project or installation scope.
- Adaptation option generated: An add, change or forget proposal for a specific lesson.
- Path back into current capability / S3: Exact-content owner approval makes the changed lesson in force, and later prompts receive it.
- Evidence: [docs/features.md](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/docs/features.md#L22-L22), [src/server/extensions/memory.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/extensions/memory.ts#L154-L178), [src/server/memory.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/memory.ts#L172-L203), [src/server/memory.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/memory.ts#L425-L467)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: This finding is scoped to explicit prospective lessons. Transcript retention and operational notifications alone do not supply S4.

## S5 — Policy and identity

- State: —
- Function: Ultimate mission or policy governance was sought at installation level.
- Disturbance / variety regulated: Conflicting policy or identity demands across sessions or roles.
- Decisive decision or feedback right: No distinct ultimate-policy decision return identified in the reviewed release.
- Decision owner: The owner configures the installation and holds selected operational permissions.
- Supporting / enforcement mechanisms: Session roles, trust controls, owner tool bounds, prompt rules and scoped memory approval.
- Closure path: Ordinary permissions, settings and approved lesson changes affect subsequent decisions.
- Why this is / is not agent-owned: The inspected routes govern access, resources and future working procedures. They provide no distinct case of an identity-level dispute routed to ultimate authority and returned as a binding policy decision.
- Evidence: [docs/features.md](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/docs/features.md#L44-L46), [src/server/extensions/pip.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/extensions/pip.ts#L92-L114), [src/server/memory.ts](https://github.com/T-Crypt/hadal/blob/b6eea00a3058491f185c0bcc76ac550caa54e098/src/server/memory.ts#L425-L467)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: The owner can change settings and source.

### Absence scope

- Surfaces inspected: Installed trust, roles, permissions, router setup, Lantern constraints and memory decisions.
- Plausible first-party paths checked: Identity exception escalations, binding resolutions above ordinary operator configuration and return to subsequent behavior.
- Why no material first-party path remains: The supplied routes govern authorized access, current action and prospective working procedures. An identity-level governance loop was not established.

## Recursion

The installation contains independent project sessions with their own workspaces. Within the standard router, fresh stages act at a lower level. Lantern and owner controls span visible sessions from the installation level.

## Variety and escalation

Tool feedback, isolation, per-model admission and stage routing absorb local operating variation. Authorization and model failures can be returned to the operator through the application. Spend and permissions are enforced externally to the model.

## Evidence gaps

Static inspection of the pinned published source. No live model, GPU contention, restart or extension execution was run. Mode-specific ownership depends on supported configuration and the scope of delegated work.
