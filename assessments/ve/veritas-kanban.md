---
harness_id: veritas-kanban
project_name: Veritas Kanban
repository: https://github.com/BradGroux/veritas-kanban
review_ref: 1d2d45e770690046f934ec0cb038bf117a37d233
reviewed_at: 2026-10-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Veritas Kanban

## Review boundary

- System in focus: One Veritas Kanban workspace coordinating a bounded software-work sprint with optional managed agent runs and an explicitly commissioned model-backed PM. A board-only installation, the developer's company and upstream maintainers are outside the positive agent-owned claims.
- Purpose and identity: Hold task/worktree identity, launch controlled software agents, collect their work and review evidence, and allow current sprint coordination with human oversight.
- Relevant environment: Changing source and branch diffs, task priorities/dependencies, provider failures, tool and credential policy, agent work results, resource capacity, human approvals, disputed review findings and future product changes.
- Standard-distribution boundary: Published local server/CLI/MCP software, managed agent-provider adapters, task/workflow/review services, shipped PM and worker-handoff prompt contracts, and documented optional PM invocation. Third-party Codex/Claude/OpenClaw inference and their unconstrained native orchestration are external engines, not a Veritas-owned organizational layer.
- Credited operating / distribution surfaces: [agent runtime architecture](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/docs/architecture/V6-AGENT-RUNTIME-CONTROL-PLANE.md), [first-party adapter registry](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/agent-provider-adapter-registry.ts), [workflow step executor](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/workflow-step-executor.ts), [PM/worker SOP](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/docs/SOP-multi-agent-orchestration.md), [shipped PM prompt](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/prompt-registry/pm-orchestration.md), [Codex diff reviewer](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/codex-review-service.ts), [review route](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/routes/diff.ts).
- Adjacent first-party surfaces excluded from ownership: Board-only Kanban, dashboards, PM example transcripts, fixed YAML sequencing, routing/admission heuristics, deterministic progress watchdog, native Git conflict UI, optional feature advertisements, unverified external provider behavior, maintainer conformance fixtures and human-defined access policies. Prompt registry storage by itself is not PM runtime activation.
- First-party operating / deployment modes: Default local board; separately configured agent-ready workspace with supervised Codex/Claude/ACP/OpenClaw task launch; explicit human-requested PM-agent sprint mode using the shipped SOP and prompt; optional on-demand Codex read-only task-diff review. No all-modes-always-on PM or review gate is assumed.
- Recursion level: One project/sprint with distinct task-executing agents and an optionally commissioned PM. The agent vendors, upstream Veritas maintainers and a user's enduring company strategy are outside the current organization.
- Reviewed revision: `BradGroux/veritas-kanban@1d2d45e770690046f934ec0cb038bf117a37d233` (`main`), repository-advertised v6.3.0 candidate.
- Observation date: 2026-10-26; frozen first-party source, API wiring and deterministic checks; no hosted LLM trials.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The local task board is usable without AI. In agent-ready mode, Veritas itself owns task identity, immutable launch envelopes, worktrees, sandbox and credentials policy, causal event records, supervision, completion and workflow state. An adapter registry maps supported configured providers to task-envelope rendering, runtime probes and bounded launch/stop operations; the external model executes the actual requested work. Workflow steps can execute provider-backed tasks, while admission, resource queues, routing and telemetry constrain the run mechanically. The separate PM SOP and `pm-orchestration.md` supply a **manually commissioned** model-backed sprint-manager role above workers; no evidence shows this PM automatically starts for an ordinary board or every workflow. A separate authenticated task diff route can commission Codex SDK in read-only mode against the original worktree diff and persist a distinct review verdict. Neither automatic repair from that verdict nor a mandatory review gate is evidenced.

## Operational model

This assessment credits the supported, configured agent-ready mode only. Provider-specific cognition is borrowed, but Veritas's first-party current task envelope and launch path create a reachable agent-executed operational unit. The model PM is a supported **constructor** requiring operator invocation, first-party role instructions and available worker endpoints; standard workflow sequencing is not independently discretionary S3. The read-only Codex reviewer is also an opt-in audit **constructor**. Its saved decision can inform PM/human corrections, but no automatic verdict-to-rework gate is claimed. Tool approvals and policy definitions remain human permissions, not agent-owned S5.

## S1 — Operations

- State: A
- Function: Execute a bounded task against an assigned software worktree and return code, tests, artifacts or a failure explanation.
- Disturbance / variety regulated: Project-specific code uncertainty, implementation bugs, failing commands/tests and unforeseen task details.
- Decisive decision or feedback right: A configured model agent interprets the Veritas-authored task envelope, selects permitted source/tool operations and returns an attempt result; Veritas supervises the launch and terminal evidence.
- Decision owner: The task-executing configured provider agent operating inside Veritas's controlled attempt; Veritas does not own raw model inference, but owns the scoped task/distribution and result boundary.
- Supporting / enforcement mechanisms: Adapter registry, source worktrees, task envelopes, provider manifests, launch checks, supervised runs, tool policy, budget and recorded attempt events.
- Closure path: User/PM task → Veritas managed attempt envelope and executable provider adapter → model-selected current code/tool work → worktree effects and attempt status → task board/PM feedback.
- Boundary reachability: Server runtime has concrete Codex SDK/CLI, Claude Code, ACP and OpenClaw adapters, workflow-step execution and explicit configured launch semantics; unlike board-only display, these are supported execution paths.
- Why this is / is not agent-owned: Dynamic coding/research/tool selection depends on the model-backed worker; immutable launch policy, queues and a successful deterministic conformance fixture would not themselves perform the task.
- Evidence: [runtime owned/provider boundary](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/docs/architecture/V6-AGENT-RUNTIME-CONTROL-PLANE.md#authority-model); [adapter executable registry](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/agent-provider-adapter-registry.ts); [agent workflow step execution](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/workflow-step-executor.ts).
- Basis: Shipped model-provider execution adapter with an owned task envelope and feedback, limited to agent-ready mode.
- Confidence: High for reachable execution architecture; model quality and environment compatibility not measured.
- Caveats: Default board-only mode has no S1 agent. Required provider tools, credentials and permissions may be unavailable; unsupported provider configurations fail closed.

## S2 — Coordination

- State: —
- Function: Would attenuate a specific disturbance created between two independently acting S1 workers, beyond simple shared state or sequential scheduling.
- Disturbance / variety regulated: Conflicting edits/claims between concurrent workers, incompatible inter-worker interfaces or resource contention needing a differentiated arbitration decision.
- Decisive decision or feedback right: Veritas schedules capacity, applies resource reservations and permits Squad Chat and Git merge-conflict handling; no first-party model-backed current inter-S1 conflict arbiter with an evidenced return to both workers was located in the inspected normal paths.
- Decision owner: Operators, the explicitly commissioned PM when it handles a concrete task conflict, or the external agents; generic queue/routing services do not themselves exercise S2 discretion.
- Supporting / enforcement mechanisms: Admission control, host routing, workflow sequencing, dependency graph, task comments, Squad Chat and conflict-service Git operations.
- Closure path: A resource limit can queue a run and a Git conflict can be manually resolved, but these are mechanical/single-artifact responses, not a demonstrated distinct coordination relation that modifies two S1 behaviors after inter-S1 disturbance.
- Boundary reachability: Coordination mechanisms are shipped; the missing evidence is their connection to a dedicated, S2-specific corrective decision owner in the configured operating mode.
- Why this is / is not agent-owned: Deterministic capacity allocation, chat message transport or git merge tooling do not inspect and settle a semantic disagreement between task agents.
- Evidence: [admission control](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/admission-control-service.ts); [routing service](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/agent-routing-service.ts); [workflow executor](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/workflow-step-executor.ts); [Git conflict service](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/conflict-service.ts).
- Basis: Source-negative for differentiated S2, while recognizing nontrivial mechanical coordination.
- Confidence: Medium; a separately configured PM might settle collisions as S3 work, but this is not a proven S2 path.
- Caveats: S2 absence must not be read as absence of resource controls, multi-agent communication or conflict UI.

### Absence scope

- Surfaces inspected: Agent admission, host and roster routing, task dependencies, workflow sequencing/parallel steps, Squad Chat documentation, merge-conflict service and PM SOP.
- Plausible first-party paths checked: Inter-worker task collisions, shared file ownership, resource conflicts, contradictory review findings and corrective messages to affected workers.
- Why no material first-party path remains: Present mechanisms handle execution order, capacity, display or operator-mediated git conflict; the human-commissioned PM is the current sprint governor, without an independent evidenced S2-specific settlement channel.

## S3 — Inside-and-now control

- State: C
- Function: Hold the whole current sprint's task allocation, progress, blockers and corrections in one discretionary model-backed PM role.
- Disturbance / variety regulated: Worker failures, missing task dependencies, incomplete acceptance criteria, scope/timeline drift, blocked review findings and the need to reassign current commitments.
- Decisive decision or feedback right: When a human specifically starts the shipped PM-agent mode, its instructions call for inspecting the sprint task list, deciding task splits and worker assignments, following task statuses, requesting corrections and reporting/escalating unresolved blockers.
- Decision owner: The expressly commissioned PM model agent using Veritas task/API/CLI surfaces and provider-owned worker launch; it is not the rule-based WorkflowRunService or automatic Veritas board state.
- Supporting / enforcement mechanisms: PM orchestration prompt, multi-agent SOP, task comments, CLI/API, managed worker attempt timing, status/dashboard and human escalation triggers.
- Closure path: Human commissions a PM for one sprint → PM reads overall backlog/current task status → assigns/spawns S1 agents and requests repairs on failures → worker status and review reports return through Veritas → PM changes subsequent work or escalates to human.
- Boundary reachability: First-party `docs/SOP-multi-agent-orchestration.md` explicitly describes “Hey Veritas, can you be the PM” and a `sessions_spawn` PM example, while `prompt-registry/pm-orchestration.md` ships the corresponding first-party Plan/Assign/Track/Review/Report contract. This is a selectable human-assisted composition, **not** an automatically active built-in manager or proved unattended control loop.
- Why this is / is not agent-owned: The commissioned PM must make discretionary scope/allocation/rework choices using current feedback. Without PM execution, Veritas's ordinary workflow engine is deterministic launch order, not a semantic current-governor agent.
- Whole-system current view: Sprint goal, current tasks and dependencies, assigned worker state, blocker comments, time budget and acceptance evidence; view is bounded to the commissioned sprint, not every organizational project.
- Current-control decision scope: Break down and reprioritize present tasks, assign/reassign worker runs, request fixes or escalate; identity/policy authority and final production approvals stay with the human lead.
- Evidence: [first-party PM + worker SOP and activation example](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/docs/SOP-multi-agent-orchestration.md); [PM decision and escalation contract](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/prompt-registry/pm-orchestration.md); [CLI prompt management](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/cli/src/commands/prompts.ts).
- Basis: Explicit operator-commissioned first-party model-PM constructor; no evidence of universal autonomous activation.
- Confidence: Medium-low: the prompt/SOP can create the role, but the runtime does not appear to bind it automatically into each workflow or make its corrections mandatory.
- Caveats: Requires a human to commission the PM, compatible model agent capable of task API/tool use, and available workers; illustrative `sessions_spawn` itself belongs to the selected external host.

## S3* — Complementary audit

- State: C
- Function: Run an optional independent source/diff inspection that can challenge an implementing agent's completion claims before a human or PM chooses next action.
- Disturbance / variety regulated: Unseen regressions, source/requirement mismatches, insecure changes, omitted tests and inflated worker completion reports.
- Decisive decision or feedback right: On explicit `POST /api/diff/:taskId/codex-review`, a **separate** read-only Codex SDK thread reviews the actual task worktree diff against its base, returns a review decision and file/line findings and usually saves them as task review/comments.
- Decision owner: On-demand Codex reviewer for the semantic audit; the invoking operator or separately commissioned PM controls repair/acceptance. This distinct audit agent is hosted by the external Codex SDK but spawned and instructed by first-party Veritas code.
- Supporting / enforcement mechanisms: Worktree publication-authority resolution, immutable base diff, reviewer read-only sandbox, structured finding schema, persisted review comments, task view/packet and human review/approval UI.
- Closure path: Implementing agent changes task worktree → authorized operator invokes diff review → separate Codex thread reads source diff (not merely worker status) → saves `changes-requested`/`rejected` findings into the task → PM or human reads them and may reopen/reassign correction. The **last return is conditional**, not a mandatory automatic failure gate.
- Boundary reachability: `server/src/routes/diff.ts` wires the POST route to `CodexReviewService.reviewTask`; service imports `@openai/codex-sdk`, starts a distinct read-only thread, parses verdict and stores it via `TaskService.updateTask`. The source does not tie `task.review.decision` to its ordinary four-score `reviewGate` transition check.
- Why this is / is not agent-owned: Model reviewer chooses semantic findings after direct original-artifact inspection; a deterministic diff viewer or fixed score gate does not substitute for that independent challenge. Human-triggered return limits this to C.
- Claim being audited: Implementing worker's implicit assertion that its current task branch changes are correct, safe and complete.
- Ordinary reporting path: Worker result, task attempt status, comments, proposed PR and any routine test logs.
- Complementary access path: Reviewer resolves the authoritative worktree/base commit itself, runs the original git diff and sends that artifact directly to a separate Codex read-only thread.
- Independence boundary: Separate Codex SDK review thread with read-only sandbox and no implementation-author edit right inside that thread; not guaranteed different model vendor or adversarial provider independence.
- Who acts on findings: A human or an explicitly commissioned PM reading saved task review/comments may return them to a worker for repair; no automatic mandatory rework/closure block was established.
- Evidence: [source-diff review thread, response and task record](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/codex-review-service.ts); [reachable API endpoint](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/routes/diff.ts); [ordinary independent 4x10 completion gate](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/task-service.ts); [review in task risk packet](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/work-product-service.ts).
- Basis: First-party reachable optional read-only separate semantic auditor; correction feedback path is operator/PM mediated.
- Confidence: Medium for audit formation and persistence, low for downstream rework actually being selected.
- Caveats: No live Codex run tested; API invocation, SDK credentials and configured review model are required. This is not an always-on automatic quality gate and its verdict is not the four-score `reviewGate` condition.

## S4 — Outside-and-then intelligence

- State: —
- Function: Would monitor prospective external variations and choose enduring capability adaptations for future operations.
- Disturbance / variety regulated: Future platform, model, market, product and external capability changes beyond today's sprint.
- Decisive decision or feedback right: Veritas collects provider health and retrospective reflections and lets humans promote lessons into templates/agent profiles, but no supported first-party future-environment analyst with a discretionary adaptation/return mandate is established.
- Decision owner: Human operator controls future agent policy/profile and promotion; runtime monitors current health and task behavior within preselected policies.
- Supporting / enforcement mechanisms: Reflections, promotion adapters, agent roster/profile updates, provider compatibility and runtime checks, analytics, documentation freshness and optional research tasks.
- Closure path: A completed sprint can produce a human-reviewed reflection and a later template/profile change; this is retrospective operator approval, not a proved external-prospective S4 decision back into current capacity.
- Boundary reachability: The reflection and promotion code paths exist, but do not establish a standing model-owned external future analysis/option/operational adaptation circuit.
- Why this is / is not agent-owned: Retrospective data retention, drift thresholds and an operator approving a changed template do not themselves select a strategy for future environmental variation.
- Evidence: [reflection service](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/reflection-service.ts); [human-reviewed promotion adapters](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/server/src/services/reflection-promotion-adapters.ts); [runtime compatibility scope](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/docs/architecture/V6-AGENT-RUNTIME-CONTROL-PLANE.md).
- Basis: Negative for external-prospective autonomy at one sprint recursion; adjacent adaptation storage acknowledged.
- Confidence: Medium.
- Caveats: Distinct user-installed research agents might add S4 under a new boundary but are not part of the evidenced default composition.

### Absence scope

- Surfaces inspected: Provider health/capability registry, telemetry, task and decision reflections, promotion adapters, prompt/template registry, workflow and sprint roadmap descriptions.
- Plausible first-party paths checked: Future model discovery, independent technology scanning, self-redesign of agent roster, retained learned policy and returning prospective adaptations into PM actions.
- Why no material first-party path remains: Health/probe logic constrains immediate launch, while reflections summarize previous runs and require human promotion; none shows a differentiated self-owned, future-directed environmental scan and current-capability return.

## S5 — Policy and identity

- State: —
- Function: Would resolve the organization's ultimate purpose, identity, legitimate authority or policy conflicts and return binding new identity rules.
- Disturbance / variety regulated: Conflict over purpose and legitimate final authority, including conflicting stakeholder values beyond tool/task permission checks.
- Decisive decision or feedback right: First-party policies compile sandbox/approval decisions from human configuration; ChatGPT identity sign-in, roles and workspace membership authenticate access. No first-party ultimate-policy decision owner is demonstrated.
- Decision owner: User organization and administrator retain authorization, strategic policy and task/production approval; Veritas implements those choices.
- Supporting / enforcement mechanisms: Phase authority compiler, tool and credential policy, runtime approval broker, membership and role checks, human release boundaries.
- Closure path: Authorized principal/policy config constrains a launch and reviewer can grant/deny an exact action; this does not deliberate contested identity and return a changed ultimate policy to the organization.
- Boundary reachability: Real permission and policy enforcement is reachable; the missing path is higher-order identity/ultimate-purpose arbitration by an S5 actor within the defined sprint organization.
- Why this is / is not agent-owned: A least-privilege tool decision, login identity record or human approval is a bound placed on agent action, not a model-owned constitutional/policy judgment.
- Evidence: [phase capability contract](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/docs/architecture/PHASE-CAPABILITY-PROFILES.md); [tool control boundary](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/docs/architecture/TOOL-CONTROL-PLANE-V1.md); [runtime authority and approval model](https://github.com/BradGroux/veritas-kanban/blob/1d2d45e770690046f934ec0cb038bf117a37d233/docs/architecture/V6-AGENT-RUNTIME-CONTROL-PLANE.md).
- Basis: Source-negative for identity/ultimate-policy governance; genuine permission enforcement explicitly acknowledged.
- Confidence: Medium-high.
- Caveats: User/administrator may serve as external parent S5, but ordinary sign-in or approval is insufficient to assign `P` to a Veritas-hosted actor.

### Absence scope

- Surfaces inspected: Setup modes, governance controls, sandbox/tool permissions, profile parent authority, membership, approval broker, PM SOP and work-product review.
- Plausible first-party paths checked: Identity disputes, final legitimate authority, mission change, policy conflicts and binding organization-wide decision return.
- Why no material first-party path remains: The observed surfaces authorize concrete launches and govern current task safety from already specified human rules; no distinct deliberation/decision owner for ultimate identity disputes exists at this scope.

## Distributed OSS parent arrangement

Veritas maintains execution identity and policy enforcement but depends on external Codex, Claude, ACP/OpenClaw and operators for cognition, optional PM invocation, credentials and purpose. Those parties are not collapsed into a fictional single autonomous S3/S4/S5. An operator commissioning a PM or approving a review does not establish standalone parent `P`.

## Self-hosted and non-human modes

Local board-only mode can operate without model-backed agents and has no credited S1. The agent-ready mode can execute configured non-human workers under first-party attempt supervision. Commissioned PM and on-demand Codex review are separate explicit modes and may be absent; model, network and auth conditions were not live-validated.

## Recursion

The analyzed whole is one coordinated sprint/project workload, not all of Veritas's install base. Worktree/attempt agents serve as operational cells; commissioned PM holds a bounded current sprint view, and on-demand code audit can challenge one completed branch. Board-only users and user-company governance are different boundaries.

## Variety and escalation

Incoming task variability reaches task execution through the managed provider adapter. Deterministic admission/routing constrains resource/permission variety without qualifying as S2. When specifically commissioned, a PM can react to worker progress and direct new commitments. Separately requested Codex diff review can return findings to a task record, after which the operator/PM chooses correction or escalation. Provider faults, missing rights and unresolved quality disputes can halt work; no assured autonomous adaptation or ultimate-policy settlement is inferred.

## Evidence gaps

- No live provider model, Codex review quality, browser interaction, generated-code quality or agent prompt adherence test was run. Assessment is frozen-source decision-right analysis and repeatable Index structural validation only.
- First-party documentation and source explicitly separate board-only from agent-ready. Credit S1 only in configured managed-run mode.
- PM `S3=C` is a user-commissioned SOP/prompt constructor; the `sessions_spawn` example is external and not proof of Veritas automatically activating PM for each workflow.
- Codex `S3*=C` directly reads original diff in a separate thread and persists findings, but mandatory verdict-driven correction is **not wired** into the regular four-score task completion gate; an operator/PM must act on the result.
- Mechanical resource admission, routing, phases, chat and native git conflict resolution were not elevated to differentiated S2; retrospective reflections were not elevated to prospective S4; tool/identity enforcement was not elevated to S5.
