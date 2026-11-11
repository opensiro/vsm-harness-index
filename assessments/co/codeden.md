---
harness_id: codeden
project_name: CodeDen
repository: https://github.com/leonvanzyl/codeden
review_ref: 8a05e5c2117b8ee5794f75538953a92e8f51b1ae
reviewed_at: 2026-11-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: P
---

# CodeDen

## Review boundary

- System in focus: installed local CodeDen server, runner, provider adapters, role-scoped orchestration and opt-in factory for coding projects.
- Purpose and identity: coordinate software-building agents, their isolated work, current commitments and optional unattended improvement/PR lifecycle.
- Relevant environment: local projects and repositories, GitHub issues/CI, user vision and constraints, code and tests, external Claude/Codex model processes, budgets and changing tasks.
- Standard-distribution boundary: [server/runner architecture](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/docs/architecture.md), [role orchestration](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/docs/orchestration.md), and opt-in experimental [autopilot/dark-factory modes](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/docs/autonomy-and-dark-factory.md); not every project uses factory mode.
- Credited operating / distribution surfaces: `apps/server/src/services/orchestration/`, `apps/server/src/services/sessions/`, `apps/server/src/services/factory/`, `apps/runner/src/`, `packages/providers/src/`, role/factory prompts, MCP/session tools, built-in UI and persisted state.
- Adjacent first-party surfaces excluded from ownership: tests/mocks, docs/design proposals, package publishing and CI for CodeDen itself, its desktop wrapper, external third-party model reasoning and GitHub as an independent institution; fake provider is deterministic test support, not autonomous evidence.
- First-party operating / deployment modes considered: manual/assisted PM and project sessions, opt-in Autopilot and experimental Dark factory with review/merge/follow-up, self-hosted server and runner, configured external provider/model sessions.
- Recursion level: one CodeDen-managed project with multiple concurrent coding sessions and project-manager role; global orchestrator is an enclosing level, not automatically a second S1 inside a single project.
- Reviewed revision: `8a05e5c2117b8ee5794f75538953a92e8f51b1ae`; 2026-11-11; source-static, no live paid-model execution.
- Generated Profile/Methodology: 0.2.4 / 0.3.8; current Profile/Methodology: 0.2.4 / 0.3.8.

## Repository architecture

The server persists an event log and projections, receives session and GitHub notices, wakes read-only PM/orchestrator model sessions, schedules automations and the factory. A separate runner operates code-adjacent provider sessions, worktrees, tools, browser, journals and resumable event delivery. [Provider adapters](https://github.com/leonvanzyl/codeden/tree/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/packages/providers/src) wire Claude Agent SDK and Codex app-server into first-party agent roles; the third-party models do the reasoning, but the shipped CodeDen mode supplies agent/tool/feedback and role rights. The [conflict gate](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/sessions/conflicts.ts) detects duplicate/overlapping work; PM prompts choose wait/skip/join/force and can return work to agents. Factory mode adds discovery, PM triage, builder, separate reviewer and exact PR checks; it is not the default.

## Operational model

- Coding sessions own local task plans, tool choices, edits, tests and PR proposals. Worktrees/constraints are enforcement, not the coding decision owner.
- Project PM receives a whole-current status digest and typed conflict/PR/session notices and can choose current task allocation and intervention. Distinct coding sessions are project-level S1 cells.
- Optional factory improvement finder and PM generate/triage prospective changes against the user-supplied project vision, followed by build, complementary review, merge and CI-watch feedback.
- Local human operator owns project goals/vision, protected subject matter and ultimate autonomy boundaries. This does not make every ordinary approval S5.

## S1 — Operations

- State: A
- Function: model-directed coding and verification for user/project work with tool feedback.
- Disturbance / variety regulated: changing requirements, code/test observations, tool failures, merge feedback and provider questions.
- Decisive decision or feedback right: choose implementation, tool calls, edits and iterative correction inside the task brief.
- Decision owner: first-party launched agent session using installed Claude/Codex model/tool adapter; model reasoning is external inference, while CodeDen's shipped role/session is the agentic execution organization.
- Supporting / enforcement mechanisms: runner, worktree, MCP proxy, approvals, session event stream, adapter capability flags and CI.
- Closure path: project PM/request → worktree coding session → model-driven code/tools → test/progress/PR result → follow-up/retry or finished task.
- Boundary reachability: installed [server/runner](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/docs/architecture.md) launches real provider sessions; manual and PM-started sessions are supported without a custom developer extension.
- Why this is / is not agent-owned: coding decisions are not predefined by the queue or UI; model-backed sessions choose their course within constraints.
- Evidence: [architecture](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/docs/architecture.md), [orchestration tools/flow](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/docs/orchestration.md), [factory builder instructions](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/prompts.ts).
- Basis: structural and explicit shipped mode.
- Confidence: high for implemented model-mediated agent loop, not for task quality.
- Caveats: requires an installed/configured provider; no paid model execution was attempted.

## S2 — Coordination

- State: A
- Function: attenuate conflicting work claims across distinct coding sessions within the same managed project.
- Disturbance / variety regulated: duplicate issue execution and overlapping paths/areas by concurrent S1 agents.
- Decisive decision or feedback right: choose among waiting, skipping, joining or forcing when a conflict is detected and adjust subsequent work.
- Decision owner: project PM model session in PM-started mode; a human instead owns decisions for conflicts from manually started work.
- Supporting / enforcement mechanisms: deterministic work-key/scope collision detection, persisted conflict records and inbox/UI choice delivery.
- Distinct S1 units: separate coding-agent sessions operating on different worktrees/tasks of the same project.
- Inter-S1 disturbance: simultaneous work keyed to one issue or intersecting code scope risks duplicated/conflicting changes.
- Attenuating coordination relation: [findConflicts](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/sessions/conflicts.ts) prevents automatic simultaneous admission and emits a conflict decision for PM resolution.
- Feedback into subsequent S1 behaviour: PM selects join/wait/skip/force; the pending start is redirected, queued, discarded or allowed, changing how agent sessions proceed.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: a concrete competing-work collision is detected and attenuated; the PM's resolution is discretionary, beyond mere message transport.
- Closure path: conflicting active sessions → collision notice → PM resolution → altered later session admission or follow-up.
- Boundary reachability: [PM prompt](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/orchestration/prompts.ts) explicitly instructs the model to select a remedy; [ConflictService](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/orchestration/conflicts.ts) implements the resolution path.
- Why this is / is not agent-owned: hard collision detection does not itself own the choice; PM chooses the response in a shipped agent role.
- Evidence: [conflict detector](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/sessions/conflicts.ts), [PM prompt](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/orchestration/prompts.ts), [orchestration documentation](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/docs/orchestration.md).
- Basis: structural.
- Confidence: high for collision and response wiring; lower for the practical quality of model selections.
- Caveats: the same collision can be human-owned for a manually started session; S2=A is supported by the PM mode, not every run.

## S3 — Inside-and-now control

- State: A
- Function: project-wide regulation of concurrent work commitments, priorities and resource limits.
- Disturbance / variety regulated: competing projects/issue priorities, sessions failing or awaiting input, spend/capacity constraints and current delivery bottlenecks.
- Decisive decision or feedback right: choose which issue to triage/accept, sequence/split work and intervene in active agents based on portfolio status.
- Decision owner: model-backed project manager in ordinary PM and factory modes; fixed factory limits enforce, but do not originate, its prioritization.
- Supporting / enforcement mechanisms: [status digest and notices](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/docs/orchestration.md), budgets, merge caps, session status, GitHub sync, factory scheduler.
- Whole-system current view: PM digest includes running/queued project sessions, inbox, CI/PR notices, scheduled work, failures and progress, rather than one coding task alone.
- Current-control decision scope: [PM triage](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/prompts.ts) scores and accepts/rejects candidates or splits large changes; session tools allow start/steer/stop and conflict resolution.
- Closure path: portfolio event/digest → PM model choice → start/steer/stop/triage tool → updated sessions and factory backlog → next status digest.
- Boundary reachability: PM role is shipped and invoked by notices; factory triage additionally calls [triage](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/decisions.ts) to persist a decision and create/label issues.
- Why this is / is not agent-owned: unlike a fixed budget alarm, the PM can choose and revise commitments from a current whole-project view.
- Evidence: [PM prompts](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/orchestration/prompts.ts), [factory triage](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/decisions.ts), [factory flow](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/loop.ts).
- Basis: structural and explicit.
- Confidence: medium-high.
- Caveats: cross-project orchestrator is a higher scope; deterministic factory admission caps are not agent-owned S3 by themselves.

## S3* — Complementary audit

- State: A
- Function: independently challenge code/PR quality claims made by production agents and feed findings into corrective control before integration.
- Disturbance / variety regulated: builder self-report blind spots, untested behavior, security/quality flaws.
- Decisive decision or feedback right: separate reviewer agent inspects diff/code/test evidence against criteria and issues approve/request-changes/reject judgment.
- Decision owner: distinct model-backed reviewer session, selected by the factory; deterministic checks and merge gate only enforce its verdict.
- Supporting / enforcement mechanisms: CI, test-file detection, protected-areas check, size and security command checks, reviewer-session state.
- Claim being audited: builder's PR fulfills accepted issue criteria and project vision without unsafe/untested effects.
- Ordinary reporting path: builder's own finish message, tests and PR summary, plus ordinary CI/status events.
- Complementary access path: [reviewer prompt](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/prompts.ts) directs a separate session to inspect local diff, code and tests and make a judgment, not restate builder output.
- Independence boundary: [startReviewer](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/sessions.ts) constructs a separate reviewer session with read-only brief; distinct provider preferred when available, not guaranteed; shared worktree/code evidence does not imply provider-independent audit.
- Who acts on findings: [verify](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/verify.ts) returns failed findings to builder for a fix/re-review or prevents merge; accepted verdict joins other merge gates.
- Closure path: builder PR → separate reviewer diff/code inspection → structured verdict → factory check → fix/re-review or authorized automatic merge.
- Boundary reachability: shipped opt-in [Autopilot/Dark factory](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/docs/autonomy-and-dark-factory.md) invokes reviewer before automatic merge; manual/assisted mode does not claim the same path.
- Why this is / is not agent-owned: reviewer has discretionary model verdict and complementary source access; deterministic CI alone would not qualify.
- Evidence: [review sessions](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/sessions.ts), [review prompt](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/prompts.ts), [verify loop](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/verify.ts).
- Basis: structural.
- Confidence: medium-high for separate audit path; not an effectiveness certificate.
- Caveats: alternative-provider selection is opportunistic; quality and independence of a real run not tested.

## S4 — Outside-and-then intelligence

- State: A
- Function: generate and select prospective improvements aligned to target users/project vision and return them to current project capability.
- Disturbance / variety regulated: new GitHub requirements, changing code quality/security/performance needs and future product fit against operator-defined goals.
- Decisive decision or feedback right: model-backed improvement finder proposes future capabilities/repairs, PM judges their priority and creates accepted backlog items.
- Decision owner: first-party launched finder and PM agent sessions in experimental Dark factory; the operator remains ultimate vision owner.
- Supporting / enforcement mechanisms: time/budget/slot-limited discovery scheduler, area rotation, candidate deduplication, issue and factory state machine.
- External distinction: incoming GitHub issues and project vision's target-user needs inform candidate triage; the finder also reads actual code for potential user-facing or security changes.
- Future / prospective distinction: proposed small future features, UX/security/performance and technical-debt options are evaluated against goals and expected subsequent capability, not only current task continuation.
- Adaptation option generated: structured candidate with title, rationale, affected paths and acceptance criteria.
- Path back into current capability / S3: [reportCandidates](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/decisions.ts) → PM triage → accepted issue/factory backlog → builder/verification/merge → changed code capability.
- Closure path: project environment/vision/code gap → finder/PM analysis → proposed option → triage and build/CI or rejection → subsequent project version.
- Boundary reachability: optional [Dark factory discover](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/loop.ts) launches [discoveryPrompt](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/prompts.ts) and accepts candidate reports through first-party tools.
- Why this is / is not agent-owned: model sessions choose future options and triage them; deterministic scheduler and status watches only carry and constrain the path.
- Evidence: [factory discovery](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/loop.ts), [prompts](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/prompts.ts), [candidate/triage tools](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/decisions.ts).
- Basis: structural, optional mode.
- Confidence: medium; strategic depth and actual environmental surveillance are narrow.
- Caveats: discovery is code/vision-centric, not general market forecasting; new issues and failed checks alone would be S1/S3 unless connected to prospective model-generated changes.

## S5 — Policy and identity

- State: P
- Function: establish the product's durable mission, target users, prohibited areas and autonomy boundaries that govern strategic/current decisions.
- Disturbance / variety regulated: pressure to maximize work throughput against protected identity, risk and user-selected purpose.
- Decisive decision or feedback right: determine and revise the authoritative project vision, forbidden scope/protected areas and allowed autonomy mode.
- Decision owner: legitimate local human operator; factory PM may triage within policy but cannot unilaterally redefine its final authority.
- Supporting / enforcement mechanisms: `.codeden/VISION.md`, [vision parser](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/vision.ts), [protectedHits](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/policy.ts), factory hold/escalation and operator controls.
- Identity / ultimate-policy issue: what the project is for, which target users and areas it excludes, and whether autonomous merging may exercise code-change authority.
- Ultimate authority in each claimed mode: the operator sets/updates the vision and autonomy mode; agent factory judgments operate below these rights.
- Return-to-operation path: operator-updated vision/mode → server reads/persists configuration → PM/finder/builder/reviewer prompts and protected-path checks → candidate rejection or permitted build/merge.
- Closure path: identity/policy revision → operator authoritative selection → project vision/protection updates → factory triage/merge constraints on subsequent work.
- Boundary reachability: supported [vision editor/API](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/docs/autonomy-and-dark-factory.md) is wired into factory execution; not generic policy-file presence alone.
- Why this is / is not agent-owned: model roles can make ordinary judgments but do not own the ultimate project identity/policy line.
- Evidence: [vision](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/vision.ts), [factory policy](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/policy.ts), [prompts](https://github.com/leonvanzyl/codeden/blob/8a05e5c2117b8ee5794f75538953a92e8f51b1ae/apps/server/src/services/factory/prompts.ts).
- Basis: explicit and structural parent mode.
- Confidence: medium-high for local operator policy return; no shared multi-maintainer S5 conclusion.
- Caveats: task approvals and ordinary protected-path escalation alone do not establish S5; parent claim rests on mission/ultimate-policy vision governance.

## Distributed OSS parent arrangement

Assessment is of a local CodeDen project, not CodeDen's upstream maintainer/contributor organization. No claims about organization-level distributed parent authority are made from the GitHub repository or its community.

## Self-hosted and non-human modes

The local operator retains policy authority even when experimental Dark factory executes ordinary backlog and merge decisions without asking. S3*/S4 claims require their opt-in mode and are not generalized to default Assisted. External provider accounts and GitHub permissions remain real operational prerequisites.

## Recursion

Each concurrent coding session is an operational S1 cell only when carrying a distinct deliverable and environment. A PM coordinates/manages the project level. The global orchestrator routes across projects at a higher recursion; child agent spawning alone is not a new viable-system claim.

## Variety and escalation

Work keys, scope collision gates, role-scoped tools, budgets, protected paths, re-review rounds, provider capability declarations and exact CI checks attenuate operational variety. Budget exhaustion/failing checks pause factory operation; status or pause alone does not prove an algedonic path. Parent escalation is retained for protected/irreversible policy decisions. Recovery after a merged CI regression prepares a revert PR and pauses the loop.

## Evidence gaps

- Source-static review only: no external Claude/Codex run, cross-provider review quality test, real GitHub merge or Dark factory smoke here.
- The S2 agent decision and S3/S4 agent triage roles are prompt- and tool-wired; their realized judgment quality is not validated by code presence.
- S4 is a narrow product-improvement future loop grounded in code/vision and incoming requirements; not a proven general external-foresight program.
- Model/provider, CI, GitHub and operating-system permissions are external dependencies; external maintainer authority is excluded.
