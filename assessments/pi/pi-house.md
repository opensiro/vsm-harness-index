---
harness_id: pi-house
project_name: pi-house
repository: https://github.com/Jero110/pi-house
review_ref: 5c456584931025f421eb45c7232683737a628371
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# pi-house

## Review boundary

- System in focus: The installed `pih`/pi extension runtime, agent-link orchestration and shipped planner/executor skills, together with opt-in workflow memory/learning; not the unmodified upstream pi model runtime or the external coding assistants' generic intelligence.
- Purpose and identity: Turn a human-approved software plan into independently executed, coordinated and verified agent tasks, with bounded optional learning from prior runs.
- Relevant environment: Project code, plan dependencies, concurrent workers and overlapping files, usage/provider availability, task results, tests, and retained workflow evidence.
- Standard-distribution boundary: `pih` launches a pinned pi CLI with extensions and installed skills; the planner hands an approved plan to an executor that drives agent-link workers. Self-learning is a documented manual command with human approval for concrete edits.
- Credited operating / distribution surfaces: [launcher.ts](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/packages/pihouse/src/launcher.ts), [workflow.ts](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/packages/pihouse/src/extensions/workflow.ts), [executor skill](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/skills/build/executor/SKILL.md), [planner skill](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/skills/pre-build/planner/SKILL.md), [hub.ts](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/packages/agent-link-core/src/hub/hub.ts), [learning-review.ts](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/packages/pihouse/src/workflow/learning-review.ts), [proposals.ts](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/packages/pihouse/src/workflow/proposals.ts).
- Adjacent first-party surfaces excluded from ownership: `books-rag` ingestion and external Pinecone/S3 knowledge services; separate developer/research fixtures and smoke results; upstream pi internals; the external Claude, Codex and OpenCode agents' general tool decisions outside the installed plan/agent-link protocol.
- First-party operating / deployment modes considered: Human-reviewed planner → autonomous executor → parallel worker tasks; deterministic hub/pane routing and fenced replacement; optional manual `/workflow self-learning` → proposals → human approval and allowlisted apply.
- Recursion level: A project-plan execution managed by one executor with multiple S1 workers. A separate session, pane or harness vendor does not by itself make another viable recursion.
- Reviewed revision: `5c456584931025f421eb45c7232683737a628371`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The launcher installs an extension-bearing pi, while agent-link keeps a per-home hub, session lineage, worker adapters and a message/result journal. A planner records the user's approved tasks, owners, models, skills, prerequisites and validations. An executor then allocates independent work to workers, supervising them through returned results and independently checking their work before integration. Workers may run different supported external harnesses; the distinctive first-party decision protocol is the shipped executor skill, not a replacement implementation of those vendors' models. [architecture.md](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/docs/architecture.md), [workflow.ts](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/packages/pihouse/src/extensions/workflow.ts), [executor skill](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/skills/build/executor/SKILL.md).

Separately, optional captured runs become digests, bounded review proposals and finally human-approved version-pinned changes to allowlisted memory/skill files. The hub does not own that memory. Quota-aware routing and `replace` fencing are operational supports, not discretionary S2/S3/S5 decision owners. [self-learning.md](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/docs/self-learning.md), [hub.ts](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/packages/agent-link-core/src/hub/hub.ts).

## Operational model

The human fixes the binding goal and approves the plan. The model-bearing executor reads the whole plan, selects ready independent work, assigns concrete agents/models under quota and file-ownership constraints, integrates verified results and reports gaps. Distinct model-bearing workers perform coding tasks and return artifacts. The executor can test worker claims from source rather than trusting summaries; an unsuccessful validation returns a correction to the same worker. Learning changes are an alternative parent-governed path: a model suggests retained improvements, but only the human's pinned approval changes future skills or memory. [executor skill](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/skills/build/executor/SKILL.md), [self-learning.md](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/docs/self-learning.md).

## S1 — Operations

- State: A
- Function: Carry out plan-scoped code tasks and evaluate local acceptance results.
- Disturbance / variety regulated: Task-specific code state, unforeseen implementation obstacles, command results and integration errors.
- Decisive decision or feedback right: The dispatched model worker selects edits, tools, tests and repairs within its stated task contract.
- Decision owner: Individual model-bearing agent process working under the first-party executor/agent-link protocol.
- Supporting / enforcement mechanisms: Pinned plan, task brief, harness-native coding interface, isolated worktree, result routing and test commands.
- Closure path: Task brief → worker inspects source → edits and tests → reports result/commit → executor verification and possible repair → accepted code.
- Boundary reachability: The shipped planner/executor skills and agent-link `spawn` route instantiate this ordinary mode through installed `pih`, not through an unrelated downstream user application.
- Why this is / is not agent-owned: Workers adapt code/tool choices and failures; the hub and test executable alone do not choose fixes. Model cognition belongs to installed external runtimes but the task execution operating loop is explicitly first-party assembled.
- Evidence: [executor skill, Steps 1–3](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/skills/build/executor/SKILL.md), [architecture.md](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/docs/architecture.md).
- Basis: explicit + structural.
- Confidence: high for the shipped protocol; no provider-backed run executed for this review.
- Caveats: External agent/model availability and the user's task quality remain outside ownership.

## S2 — Coordination

- State: A
- Distinct S1 units: Concurrent model-bearing coding workers, each assigned a task, branch/worktree, and owned files.
- Inter-S1 disturbance: Two otherwise valid workers editing shared files, violating prerequisite order, clashing during integration or exhausting a shared quota pool.
- Attenuating coordination relation: The executor checks dependency and file independence before fanout, assigns disjoint ownership, defers shared wiring, revises dispatch after results and resolves isolated integration conflicts; the hub relays workers' status and feedback.
- Feedback into subsequent S1 behaviour: A conflicting or unverified result is not declared done; the executor revises task integration or asks the worker for a corrected result, and only independent ready tasks continue concurrently.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The executor skill names inter-worker file conflicts and dependent work as disturbances, requiring model-owned independence judgment and changed commitments, above deterministic message relay and FIFO routing.
- Function: Attenuate collisions among S1 workers contributing to one plan.
- Disturbance / variety regulated: Overlapping edits, premature dependent work, model-account budget contention, and inconsistent integration.
- Decisive decision or feedback right: Decide which tasks can safely run simultaneously, partition files and change worker/merge commitments when feedback exposes interference.
- Decision owner: Model-bearing executor; individual workers respond to revised briefs and correction requests.
- Supporting / enforcement mechanisms: Dependency graph, per-task worktrees, assigned owned files, global quota-backed worker cap, agent-link result delivery and merge verification.
- Closure path: Plan/worktree overlap identified → executor allocates or delays workers → detects conflict/result → adjusts task/merge order or issues correction → subsequent workers proceed under new ownership.
- Boundary reachability: `skills/build/executor/SKILL.md` is part of the installed standard planner-to-executor flow, and hub `spawn`/results are first-party tools.
- Why this is / is not agent-owned: Deterministic worktree isolation cannot decide semantic independence; the executor is instructed to inspect dependencies and ownership and act on real feedback.
- Evidence: [executor skill, Step 1 and Step 3](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/skills/build/executor/SKILL.md), [hub.ts](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/packages/agent-link-core/src/hub/hub.ts).
- Basis: explicit + structural.
- Confidence: medium-high for the documented deployed path, not measured conflict success.
- Caveats: No S2 attribution to the FIFO hub alone or the external harnesses' generic team features.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: The executor reads the complete validated plan, progress ledger, dependency state, quota observations and returned worker results.
- Current-control decision scope: Allocate current tasks to workers, choose authorized model routes, adjust concurrency/priority on failures, integrate branches and determine verified completion versus gaps.
- Function: Manage present project-plan commitments and recovery across S1 workers.
- Disturbance / variety regulated: Blocked prerequisites, failed results, exhausted accounts, unverified work and integration deviations.
- Decisive decision or feedback right: Dispatch independent ready tasks; pause blocked work; choose one bounded retry/correction; integrate accepted changes and decide the plan's completion report.
- Decision owner: Model-bearing executor under the user-approved plan; user holds plan/goal authority outside this S3 autonomous current-control path.
- Supporting / enforcement mechanisms: Plan ledger, usage observations, worker reports/transcripts, integration branch, validation commands, and limits enforced by router/hub.
- Closure path: Current plan and progress → executor observes availability/results → assigns/pauses/repairs commitments → integrates verified code → reports whole-plan status.
- Boundary reachability: The default planner handoff opens the executor pane and runs the installed executor protocol; no separate management application needs to implement the decision loop.
- Why this is / is not agent-owned: The executor makes substantive current resource/commitment choices; the router, worker cap and test exit codes only constrain/enforce those decisions.
- Evidence: [executor skill, Steps 0–4](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/skills/build/executor/SKILL.md), [workflow.ts](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/packages/pihouse/src/extensions/workflow.ts).
- Basis: explicit + structural.
- Confidence: high for procedural current-control rights, no measured end-to-end success in this review.
- Caveats: Parent-approved plan decisions and quotas are not silently reassigned to the executor as S5 governance.

## S3* — Complementary audit

- State: A
- Claim being audited: A worker's reported task completion, validation evidence and claimed changes/commit.
- Ordinary reporting path: Worker sends `STATUS`, summary, validation output, commit and concerns to its parent executor.
- Complementary access path: The separate executor independently runs the task's validation in the worker checkout, checks missing evidence once, reads transcript/state if needed, and returns a bounded correction or records a gap.
- Independence boundary: Executor is a separate model-bearing agent from the S1 task owner and checks actual checkout state. It is also S3 current-control owner, not an external third-party auditor; its independent inspection is task-level, not certification of the whole system.
- Who acts on findings: The executor requests a correction from the same worker (one retry), otherwise records an unresolved gap, and refuses to integrate an unverified task.
- Function: Challenge worker success reports using independent current evidence.
- Disturbance / variety regulated: Incorrect `PASS` summaries, absent validation, untested code and integration claims that disagree with actual repository state.
- Decisive decision or feedback right: Accept, recheck, refuse or return worker work for correction based on direct checkout validation.
- Decision owner: The separate model-bearing executor inspecting the S1 worker's artifacts.
- Supporting / enforcement mechanisms: `run validation yourself`, worktree access, worker brief's acceptance criteria, one-retry policy, ledger and reporting gaps.
- Closure path: Worker claims PASS → executor runs validation against actual worktree → failure or missing evidence returns to worker → corrected artifact is retested or marked a gap before integration.
- Boundary reachability: Independent executor check is mandatory in the installed executor skill's `Step 2`; the worker and parent run as distinct agent-link sessions.
- Why this is / is not agent-owned: The command exit code is mechanical, but deciding which claims lack evidence, asking for additional evidence and directing corrections are assigned to the executor; no claim of third-party independence is made.
- Evidence: [executor skill, Step 2 and Step 3](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/skills/build/executor/SKILL.md), [architecture.md](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/docs/architecture.md).
- Basis: explicit + structural.
- Confidence: medium; independent internal check is mandated, external audit independence is not.
- Caveats: Test selection derives from the plan; this is complementary task-work audit, not a proved independent S3* organization.

## S4 — Outside-and-then intelligence

- State: P
- External distinction: Prior completed workflow runs, token/skill-use observations, recurring failure patterns and retained run digests are inputs distinct from current task execution.
- Future / prospective distinction: Bounded review generates proposed changes to skills or scoped memory intended to improve later runs, not to repair the current checkout immediately.
- Adaptation option generated: Separate scan/review worker suggests concrete before/after changes with supporting/opposing digest evidence, uncertainty and validation.
- Path back into current capability / S3: Human reviews an immutable proposal version, approves it explicitly, then the system applies an allowlisted version-checked skill/memory change with validation and receipt; future agent invocations can retrieve/use the approved content.
- Function: Parent-authorized development of future harness skills and reusable operational memory from retrospective environment evidence.
- Disturbance / variety regulated: Repeated skill misuse, avoidable failed runs and loss of operational experience across future tasks.
- Decisive decision or feedback right: Authorize or reject the proposed future change; no automatic model self-modification.
- Decision owner: Legitimate local human operator, acting as parent of this local harness instance; scan/review agents propose but do not own approval.
- Supporting / enforcement mechanisms: Manual `/workflow self-learning`, separate digest/review workers, scoped target allowlist, version-pinned approval, compare-and-swap apply, validation and receipt.
- Closure path: Captured run evidence → agent digest/review proposal → human version-pinned approve → code applies/validates → changed reusable skill or memory becomes available to subsequent S1/S3 tasks.
- Boundary reachability: `/workflow self-learning`, `/workflow proposals`, `/workflow approve` and the implementation of version-pinned `applyProposal` are public built-in commands; this is an operational local parent mode, not a hypothetical external governance overlay.
- Why this is / is not agent-owned: Agents make prospective recommendations, but the decisive durable capability choice is explicitly reserved for the human; parent mode is positive without inventing autonomous S4 approval.
- Evidence: [self-learning.md](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/docs/self-learning.md), [learning-review.ts](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/packages/pihouse/src/workflow/learning-review.ts), [proposals.ts](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/packages/pihouse/src/workflow/proposals.ts), [workflow.ts](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/packages/pihouse/src/extensions/workflow.ts).
- Basis: explicit + structural.
- Confidence: medium-high for the bounded parent-mode loop; no claim of automatic long-term adaptation quality.
- Caveats: Learning is manually invoked and bounded to allowlisted targets; general environmental forecasting and autonomous policy changes are not evidenced.

## S5 — Policy and identity

- State: —
- Function: No first-party owner is evidenced for resolving contested purpose, ultimate policy or identity and returning a legitimate binding organizational decision.
- Disturbance / variety regulated: Account/model authorization and plan ownership are boundaries fixed externally, not internal constitutional disputes.
- Decisive decision or feedback right: Redefine the system's binding purpose or policy by an accountable agent or local higher-recursion authority; not supplied.
- Decision owner: Human user establishes plan decisions, model/account authorization and local approval of bounded skills; no S5 purpose-adjudication actor within the assessed harness.
- Supporting / enforcement mechanisms: Planner user approval, routing allowlists, workflow proposal approvals and limits on remote worker actions.
- Closure path: Current plan governance and bounded S4 proposal authorization change operations/capabilities but do not provide an identity/policy question → constitutional authority → binding return loop.
- Why this is / is not agent-owned: A human approving a skill patch is not itself a legitimate organizational S5 policy court; the executor cannot override the goal or create new model spending authority.
- Evidence: [executor skill](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/skills/build/executor/SKILL.md), [self-learning.md](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/docs/self-learning.md), [architecture.md](https://github.com/Jero110/pi-house/blob/5c456584931025f421eb45c7232683737a628371/docs/architecture.md).
- Basis: structural.
- Confidence: medium-high within the reviewed operating modes.
- Caveats: A human/project maintainer may exercise external governance; this does not establish a first-party S5 return at the local operational recursion.

### Absence scope

- Surfaces inspected: Planner/executor authority, installed model routing, workflow approval/application commands, hub and published architecture.
- Plausible first-party paths checked: User-approved plan decisions, no-unauthorized-model fallback, skill/memory approvals and executor stop/report semantics.
- Why no material first-party path remains: These paths govern individual task scope, spending, or adaptive skill edits; none handles a contested identity/ultimate-policy issue and returns a binding purpose decision to the operational system.

## Distributed OSS parent arrangement

Each installed `pih` instance may have a legitimate local parent human who approves self-learning proposals; no shared project-wide parent mode is inferred from GitHub contributors. S4=P is local, not organizational OpenSiro or upstream maintainer governance.

## Self-hosted and non-human modes

Launcher, hub and memory are locally operated; external model subscriptions and supported third-party harness runtimes remain dependencies. An unattended executor can make current S2/S3 decisions after the user approves its plan. Learning requires an explicit human approval, and routing stops when no authorized account is available.

## Recursion

The executor's one plan and its workers are the assessed recursion. Cross-harness panes, model providers, local skills and the books-RAG service are subsystems, not automatically new viable units.

## Variety and escalation

Worktree separation, dependency/ownership decisions and result-driven replanning attenuate task interference. Quota limits stop unauthorized execution rather than create rights to spend. S1 audit failures escalate to executor retrial/gap reporting; optional learning escalates into a distinct human authorization before capability change.

## Evidence gaps

- No authenticated multi-provider execution or quantitative reliability/learning-outcome test was run against this frozen revision.
- Executor audit is internally separate from S1 workers but remains under the same plan's validation rules; no external independent S3* certification is implied.
- Actual effectiveness and regular use of optional self-learning are unmeasured; positive P asserts the bounded documented implementation and approval return only.
