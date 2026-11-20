---
harness_id: timon
project_name: Timon
repository: https://github.com/ai-timon/timon
review_ref: 15794bf8db23cb620a40645f273c9b18d7a4b030
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: ?
---

# Timon

## Review boundary

- System in focus: the shipped locally operated Timon daemon and its configured agent team, project task lanes, mission process and web/desktop/CLI interaction modes. The organizational boundary includes Timon's first-party *composition* of configured CLI agent roles, not ownership of the external model or coding-engine implementation.
- Purpose and identity: accept user/project objectives; run delegated, persistent agent missions and code/review/merge work with status, coordination, operator intervention and review feedback.
- Relevant environment: the local host and filesystem, Git projects/worktrees, user/operator, installed CLI agent providers and their quota/permission surfaces, browser, optional remote clients, changing project work and opportunities outside the host.
- Standard-distribution boundary: root installer/README and `orchestrator/` service; default role seeding, Kanban dispatch, verification/wake loops, mission state, resource policy, memory and scheduled dreaming. Features that need an already-installed external CLI are credited as *integrated first-party operating modes*, not as Timon implementations of provider/model internals.
- Credited operating / distribution surfaces: `orchestrator/src/{agent,agent-seed,agent-orchestration,dispatcher,worktree,merge-gate,verification-loop,review-verdict,wake,series-plan,series-service,resources,memory-synthesize,dreaming,global-digest}.ts` and `orchestrator/src/plugins-bundled/dreams/routes.ts`.
- Adjacent first-party surfaces excluded from ownership: Timon repository's own CI, development/dogfood instances, bug anecdotes and benchmark claims, Electron/Next UI rendering alone, third-party CLI reasoning engines and their permission systems, plugin author's future extensions and OSS maintainer governance.
- First-party operating / deployment modes considered: default interactive main/project orchestrator plus coder/reviewer/merger team; unattended Kanban/series/wake-loop with configured providers; local operator's series-plan/model selection and approval mode; optional nightly memory-curation, scoring and external-web dreaming. Disabled/not-configured components are not claimed to run unconditionally.
- Recursion level: one user's local multi-project agent team, with project-specific mission and worker cells and a human operator as possible parent; not the open-source development organization.
- Reviewed revision: `15794bf8db23cb620a40645f273c9b18d7a4b030`.
- Observation date: 2026-11-20.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The host daemon launches configured external CLI agent engines through Timon's process/backend adapters; it collects normalized events and mission state, saves them in SQLite and exposes the same work through CLI, web and desktop clients. Its source distinguishes process/session continuity, bounded global admission, user permissions, direct agent messages and mission delegation. The project-specific orchestrator and the separate coder/reviewer/merger/researcher/ops roles are materialized with first-party prompts and per-role configuration. A project role is data, not the suffix of an arbitrary agent name. The project orchestrator is explicitly instructed to divide work, observe returns and escalate ambiguous decisions rather than write code itself.

The Kanban dispatcher routes typed tasks, creates distinct code worktrees and applies concurrency/resource caps, with dependency and branch-integration guards. A finished coding task normally creates a separate review task grounded in Git diff/commit evidence; the reviewer returns a structured verdict. A refusal spawns bounded corrective code work; pass enables a separate merge task. The wake loop delivers recaps and blocked-task signals into the original orchestrator mission or a new wake mission, with deduplication, admission/backoff and operator escalation. Operator choices from the series-plan form select provider/model per role/group before the agent applies the plan.

The daemon also performs optional internal memory synthesis and project scoring. Its nightly dream process builds improvement proposals from project context and external-opportunity proposals using explicit WebSearch/WebFetch, deduplicates them and presents a queue for human accept/reject/snooze. Accepted dream status is not itself automatic source-code change or work execution. Source inspection, not a live Timon/model run, is the evidentiary basis.

Primary paths: [daemon and backend mission execution](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/agent.ts), [role setup and prompts](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/agent-seed.ts), [dispatcher](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/dispatcher.ts), [worktree isolation](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/worktree.ts), [dependency gate](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/merge-gate.ts), [verification return](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/verification-loop.ts), [wake and escalation](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/wake.ts), [nightly external opportunity research](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/dreaming.ts).

## Operational model

The orchestrator and coding/research/review/merge roles are actual separate work cells: their external-model-backed missions make different task-specific decisions and return artifacts, findings or Git changes. The daemon provides the organizational composition—prompts, dispatch, isolation, feedback, escalation, persisted mission records, quotas and operator intervention. For autonomy, the decisive discretion of a running model-backed first-party configured role is distinguishable from the deterministic daemon that enforces a selected limit. For scope, a CLI model cannot supply an unshipped S3/S4/S5 mechanism by virtue of general intelligence alone.

## S1 — Operations

- State: A
- Function: project worker missions turn assigned programming, research, maintenance and review tasks into outputs in their working environments.
- Disturbance / variety regulated: changing repository/task contents, errors, uncertain steps, input from other workers and user corrections.
- Decisive decision or feedback right: choose task actions, edits, next tool calls or a completed/blocked response within the role's constraints.
- Decision owner: the configured model-backed coder/researcher/etc. actor launched by Timon's installed agent composition; external CLI engines supply model execution but do not independently define Timon's roles, task commitments or orchestration.
- Supporting / enforcement mechanisms: role templates, backend launch, process fence, tool preauthorization, mission persistence, per-task worktrees and task status API.
- Closure path: the role receives task context, executes through the CLI process, reports the outcome via `timon task done/block` and the dispatcher/wake loop returns that outcome to the orchestrator and subsequent work.
- Boundary reachability: standard onboarding/materialization creates complete project agents; ordinary dispatcher and daemon process adapters launch those configured roles without a user implementing a new agent harness.
- Why this is / is not agent-owned: removing the model-backed role leaves task routing and enforcement but not the context-sensitive choice of edits, research or substantive review judgment; removing Timon leaves provider CLIs but not this installed team workflow.
- Evidence: [agent role prompts and seeding](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/agent-seed.ts); [dispatcher routes to role missions](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/dispatcher.ts); [mission/backend process engine](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/agent.ts); [README installation and agent-team boundary](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/README.md).
- Basis: structural.
- Confidence: high for the configured team; limited to integrations where an external CLI has actually been installed and authenticated.
- Caveats: this does not imply model-provider control or verified real-task performance; external CLI/model execution is a mandatory dependency of agent-owned task discretion.

## S2 — Coordination

- State: C
- Function: attenuate concrete interference between simultaneously active code work cells and between a code/review/merge chain and tasks that depend on its integrated output.
- Disturbance / variety regulated: concurrent writers sharing a Git base could overwrite/conflict; a dependent coder could run on a branch missing a predecessor's unmerged changes; multiple review tasks could evaluate conflicting iterations.
- Distinct S1 units: separate dispatched coder tasks, review missions and merger missions, which work on distinct task identities and associated Git branches.
- Inter-S1 disturbance: overlapping base updates and dependency races between a completed `code` task and its outstanding review/merge; explicit source comments describe stale-base and duplicate-review failure modes.
- Attenuating coordination relation: task-specific worktree/branch creation; dependency gates wait for review pass and merge completion; review-chain single-flight and iteration linkage; worktree base refresh with explicit conflict outcomes.
- Feedback into subsequent S1 behaviour: a gated dependent remains waiting instead of executing on the wrong base; review change requests create a next coder iteration; base-refresh conflicts return an explicit path for the acting agent.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: worktree isolation, gated integration and conflicting-iteration control directly address identified concurrent-writing and stale-evidence disturbance, not just a message bus or queue.
- Decisive decision or feedback right: set/revise the inter-work-cell isolation and dependency/merge coordination response, distinct from choosing each worker's task.
- Decision owner: Timon's first-party developer-encoded coordination primitive in the shipped runtime. A model-backed agent does not demonstrably exercise autonomous discretion over revising the conflict-control policy across all concurrent cells.
- Supporting / enforcement mechanisms: worktree manager, commit/dependency metadata, merge gate, caps and event bus.
- Closure path: dispatch checks branch/dependency state and requeues or admits a task; workers then operate only when the relevant integration state can support their next actions.
- Boundary reachability: dispatcher imports `createWorktree`, `evaluateDeps` and `refreshWorktreeBase` in the shipped daemon; no third-party coordinator must be authored first.
- Why this is / is not agent-owned: the coordination relation is real and function-specific but fixed in source and enforced deterministically. Task/agent autonomy does not automatically transfer ownership of these S2 choices.
- Evidence: [worktree setup and refresh](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/worktree.ts); [merge/dependency integration gates](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/merge-gate.ts); [dispatcher and concurrency](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/dispatcher.ts); [code/review/merge chain deduplication](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/verification-loop.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: `C` is limited to this specifically evidenced source-native S2 path, not a claim that every cross-project team conflict has an autonomous negotiator.

## S3 — Inside-and-now control

- State: A(P)
- Function: control current whole-series/project commitments by breaking work into role-assigned tasks, observing blockers/returns, choosing next interventions and distributing execution across models/roles.
- Disturbance / variety regulated: blocked or failing tasks, exhausted backends, stalled review chains, quota pressure and competing commitments over a finite worker pool.
- Whole-system current view: project orchestrator obtains series/task state, completion recaps, blocked tasks and role/series plans; source explicitly seeds the orchestrator to follow rather than itself execute worker code.
- Current-control decision scope: the model-backed project/main orchestrator can replan the active work, send diagnostic/recovery missions, abandon or escalate blocked series; in an operator-plan mode the user selects model/provider resources for the whole task series.
- Decisive decision or feedback right: decide which current task/role needs attention and which commitment and resource allocation the project should pursue next.
- Decision owner: in the base mode, the model-backed orchestrator whose mission receives synthesized returns; in the parent mode, the human selects the series plan's per-role/provider allocations and the running orchestrator applies those choices.
- Supporting / enforcement mechanisms: task database, admission caps, role routing, resource watchdog and fixed day/night quotas, backoff, wake-trigger scheduling, model-selection validation.
- Closure path: worker completion/failure triggers recap, the orchestrator receives it and chooses a next task or escalation; the UI's human-selected series plan returns to the agent as commands, and the agent applies role/provider choices before the tasks are dispatched.
- Boundary reachability: orchestrator seeding and wake/dispatcher are standard first-party runtime; the series-plan UI question and per-role configuration are shipped, not a possible future plugin.
- Why this is / is not agent-owned: in the base mode, fixed resource caps do not select the substantive intervention; the agent does. In the distinct parent mode, the human's whole-series allocation judgment is the deciding authority, not merely a permission to execute a shell command.
- Evidence: [orchestrator role and its decisions](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/agent-seed.ts); [wake recaps and escalation](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/wake.ts); [series-plan user choices and applied commands](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/series-plan.ts); [series-wide role/provider enforcement](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/series-service.ts); [resource-only enforcement](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: the parent mode is limited to the explicitly supported user-controlled series-wide provider/task allocation; a generic allow/deny card, service restart or fixed hardware cap is not counted as S3 governance. No live mission traces were executed.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model-backed project/main orchestrator | Task completion, blocked worker or series progress | Recap delivered on wake, agent chooses next current intervention/task | `agent-seed.ts`, `wake.ts`, `dispatcher.ts` |
| Parent (`P`) | Operator selecting whole-series role/model plan | Agent opens series-plan form for multi-task execution | UI answer becomes validated series commands and role/backend choices for dispatch | `series-plan.ts`, `series-service.ts` |

## S3* — Complementary audit

- State: A
- Function: challenge the coder's ordinary completed-task claim by independent examination of the actual changed Git state before integration.
- Disturbance / variety regulated: an agent can report completion while its patch has defects, violates requirements or fails correctness/security review.
- Claim being audited: the coder's `code` task and underlying branch are fit to merge.
- Ordinary reporting path: coder's task closure and mission recap.
- Complementary access path: separately seeded reviewer role directly reads branch diff/commit evidence, returns `verdict: pass` or `verdict: changes_requested` with actionable findings.
- Independence boundary: reviewer has a different role prompt and task identity, is explicitly barred from editing, and uses underlying Git diff rather than only trusting coder's done comment. Separate model identity is configurable and need not imply independent model vendors.
- Who acts on findings: verification-loop parses the reviewer judgment; a failed review creates a bounded new code iteration with feedback, and pass creates a merge task; invalid verdict blocks/escalates rather than silently integrating.
- Decisive decision or feedback right: independent substantive judgment of whether the actual patch passes or needs changes.
- Decision owner: a separate model-backed reviewer actor in the ordinary configured code/review/merge pipeline; the parser and verification loop only enforce its verdict.
- Supporting / enforcement mechanisms: diff-stat preparation, review role tool restrictions, verdict parser, iteration cap, merge dependency and logs.
- Closure path: reviewer outcome `changes_requested` feeds into the next coder iteration; a pass unlocks the merger; unparseable review blocks and notifies the supervising orchestrator.
- Boundary reachability: `handleCodeDone` explicitly generates a review task and resolves/seeds a reviewer in the shipped full pipeline. It can be intentionally disabled in code-only mode, which is not credited as an S3* mode.
- Why this is / is not agent-owned: a bounded, read-only independent reviewer makes the quality judgment on complementary raw source evidence; deterministic parser/guard alone would not decide defect severity. The system's *own* patch audit is distinct from external security audit provided as a product task.
- Evidence: [reviewer identity, read-only rules and verdict contract](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/agent-seed.ts); [code-to-review-to-repair/merge closure](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/verification-loop.ts); [verdict parser](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/review-verdict.ts); [dependency closure gate](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/merge-gate.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: no empirical independence or recall measurement; a reviewer can share a provider family with the coder. Code-only and no-diff paths do not provide this audit.

## S4 — Outside-and-then intelligence

- State: C
- Function: produce prospective project-improvement and external-opportunity options relative to the owner's stated longer-term objectives.
- Disturbance / variety regulated: changing outside market/tool opportunities, future project requirements and mismatch between existing portfolio and objectives.
- External distinction: the bundled opportunity phase explicitly uses WebSearch/WebFetch for external trends, demand and tools; improvement phase combines current project scores, prior failures and accepted objectives.
- Future / prospective distinction: nightly dreaming generates options, cost/conviction rationales and first steps for potential later work, rather than just responding to an immediate operational task.
- Adaptation option generated: an OSS-shipped `dream_proposals` queue contains prospective suggestions, source links and human review actions.
- Path back into current capability / S3: an operator can accept/reject/snooze the specific proposed option in the bundled Dreams UI; acceptance is recorded, but the inspected code does **not** itself create an executing Kanban task, reconfigure the agent's current capability or automatically integrate source. That subsequent implementation/commitment loop requires a human/developer composition.
- Decisive decision or feedback right: assess future environment signals and select action-worthy options for the project portfolio.
- Decision owner: shipped dedicated agent prompt generates the options, but final prioritization/translation of accepted proposals into present controlled commitments is left to an operator. This establishes a function-specific S4 constructor path rather than an autonomously closed S4 adaptation loop.
- Supporting / enforcement mechanisms: nightly timer, raw project score, deduplication, proposal database, notification, web tools, human status route.
- Closure path: prospective proposals reach a structured review queue; the absence of automatic activation into present work limits the state to `C`, not `A` or `P`.
- Boundary reachability: `startDreamer` ships in the daemon and the Dreams route/UI includes accepting/rejecting proposals. A configured supported provider with WebSearch/WebFetch is needed for live external research.
- Why this is / is not agent-owned: the model chooses future options but source does not show it owning a complete adaptation decision that changes current capability; a generic browser or memory file alone would not be enough, whereas this future-oriented, external-evidence-to-proposal path is explicit.
- Evidence: [nightly prospective web research, proposal insert](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/dreaming.ts); [human accept/reject route](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/plugins-bundled/dreams/routes.ts); [Dreams UI decisions](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/app/src/plugins-client/dreams/dreams-page.tsx); [project priority signals](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/memory-score.ts).
- Basis: explicit and structural.
- Confidence: medium.
- Caveats: `C` does not grant automatic or closed autonomous adaptation; no evidence that accepting a dream automatically creates a resource-backed task. The separate internal memory-curation routine alone is not credited as external S4.

## S5 — Policy and identity

- State: ?
- Function: possible owner-level identity/ultimate-policy guidance for a local cross-project agent team; a policy-issue decision and authoritative returned resolution are not decisively reconstructed.
- Disturbance / variety regulated: competing project priorities and future directions can be reconciled against user-set objectives, but the boundary of an actual identity-policy *issue* versus normal task preference is unclear.
- Decisive decision or feedback right: decide the team's ultimate direction in the face of strategic conflicts, not simply authorize an individual tool or choose a model.
- Decision owner: the human user edits an objectives document and controls the acceptance of dream proposals; source establishes a possible parent direction, but not a bounded, issue-triggered S5 resolution transaction.
- Supporting / enforcement mechanisms: `objectives.md`, cross-project digest, project scorer, dream directives and approvals.
- Closure path: the objectives document feeds the `global_context` agent's mission digest and scorer; however, the connection from an explicit identity-level issue or S3–S4 conflict to a *resolved* ultimate-policy choice and its enforced return is not established by the inspected material.
- Why this is / is not agent-owned: neither routine tool approval nor editable objectives automatically establish S5; equally, the shipped objectives-to-cross-project-context path is concrete enough that this review does not assert a bounded absence without additional source/operating-mode evidence.
- Evidence: [objectives digest](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/global-digest.ts); [conditional digest injection](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/agent.ts); [objective-based scoring](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/memory-score.ts); [dream directives and proposals](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/dreaming.ts); [dream review route](https://github.com/ai-timon/timon/blob/15794bf8db23cb620a40645f273c9b18d7a4b030/orchestrator/src/plugins-bundled/dreams/routes.ts).
- Basis: structural and unknown.
- Confidence: low for a positive S5 claim; high for the described first-party signal paths.
- Caveats: `?` is specific to the potentially in-boundary objectives/policy loop and its unproven identity-level decision/closure, not a default negative state. OSS repo maintainer policy is an excluded higher recursion.

## Distributed OSS parent arrangement

Timon is a locally installed service; a user's configured team is the assessed recursion. External plugin authors, contributors and repository maintainers have no evidenced shared first-party parent-authority channel into independent local installations. Parent S3 is local operator series control, not a claim about the public OSS organization.

## Self-hosted and non-human modes

The local daemon supports unattended tasks and model-backed orchestration; it also exposes first-party interactive operator decisions over whole-series role/model allocation and mission permissions. Code-only pipeline mode deliberately omits automatic review and therefore does not independently support the S3* claim. The automatic external-opportunity dream path proposes for human curation but does not auto-execute accepted plans.

## Recursion

The local team is one recursion containing project-specific orchestrators and operational worker/reviewer/merger cells. These subordinate cells have task-specific authority and return channels; the repository's own contributor/CI recursion and provider internal organization are outside this assessment.

## Variety and escalation

Live task diversity is absorbed by CLI-backed workers; integration interference is damped by worktrees/dependency gates. A supervisor model receives current work, recoveries and blocked returns, with bounded loop/backpressure and operator escalations. Complementary raw Git inspection precedes merges in the full code pipeline. Dreaming extends the team's horizon with optional external evidence but leaves adoption decisions to a human. Hardware quotas, permission cards and static prompts are supporting constraints, not automatically S3/S5 agents.

## Evidence gaps

Source-only assessment: the pinned Timon daemon, real external model CLIs, UI and systemd scopes were not executed. Some first-party features are optional or require authenticated external CLIs, and marketing claims are not execution witnesses. S5 remains unresolved specifically because objectives are propagated into future agent context but a first-party ultimate-policy *issue → authority decision → return* closure is not demonstrated. Future evidence could inspect an explicit runtime identity/policy escalation that changes the team's governing objective or positively bound the absence. S4 constructor status could be upgraded only with a separately evidenced closed future-option-to-present-capability path; status `accepted` alone is not that proof.
