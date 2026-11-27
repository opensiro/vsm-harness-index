---
harness_id: forgeline
project_name: Forgeline
repository: https://github.com/Nabwinsaud/forgeline
review_ref: 2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad
reviewed_at: 2026-11-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Forgeline

## Review boundary

- System in focus: The installed Forgeline software factory, its supplied engine and role agents, for one opted-in repository and its job portfolio.
- Purpose and identity: Convert scoped issues into reviewed software changes through configured development and staging gates.
- Relevant environment: Project repository, issue tracker, operating organization, test environments and host coding-agent runtime.
- Standard-distribution boundary: Forgeline CLI and job state, default pipeline, first-party roles, launcher and policy. External model inference, Git hosting and deployments are dependencies.
- Credited operating / distribution surfaces: Installed Claude Code orchestration and headless Claude runner, worktrees, roles, review gates, deterministic state transitions and human paused-job resolution.
- Adjacent first-party surfaces excluded from ownership: Maintainer roadmap, CI and manual setup scripts are adjacent. External trackers and provider runtimes do not supply the factory's organizational owners.
- First-party operating / deployment modes considered: Installed Claude Code plugin and first-party headless Claude configuration. Alternate runner and static setup were checked for boundary purposes.
- Recursion level: Configured factory for one repository, with a factory job and its constituent operational roles as the managed work scope.
- Reviewed revision: [2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad](https://github.com/Nabwinsaud/forgeline/tree/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad)
- Observation date: 2026-11-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Work is persisted per job. The engine issues typed role briefs and exact-attempt result paths, backed by configured worktrees and native runner modes. Verdicts and side effects are translated to the next stage by the supplied graph. A dedicated operator entry resolves paused jobs. [installed factory modes](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/README.md#L45-L93), [Claude Code stage loop](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/skills/run/SKILL.md#L14-L51), [stage and attempt claims](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/engine.py#L74-L156), [stage result aggregation and return](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/engine.py#L196-L233), [human intervention and re-entry](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/engine.py#L279-L303).

## Operational model

Builder, test and assessment roles own judgments and actions in their own stages. The compilation/gate, branch and tracker scripts enforce lifecycle. The separate approver makes a decision about the present release commitment and the parent operator can resolve paused jobs.

## S1 — Operations

- State: A
- Function: Implement and validate project changes in the installed factory.
- Disturbance / variety regulated: Incomplete specifications, source and test failures around a ticket.
- Decisive decision or feedback right: Choose the edits, tests and scoped changes needed for the assigned work.
- Decision owner: Supplied model-backed builders and other operational roles.
- Supporting / enforcement mechanisms: Role briefs, host model tools, job worktree and persisted result contract.
- Closure path: Selected actions modify or inspect project state, verify outcomes, and return status/data consumed by the engine.
- Boundary reachability: The first-party headless default runs a per-task Claude session, and the plugin skill invokes supplied subagents through the host without user assembly of a control loop.
- Why this is / is not agent-owned: Agents own productive actions within the worktree. The host runs tools and the engine applies protected effects.
- Evidence: [Claude Code stage loop](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/skills/run/SKILL.md#L14-L51), [Claude worker invocation](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/runner.py#L45-L63), [role results and group execution](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/runner.py#L83-L118), [stage result aggregation and return](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/engine.py#L196-L233), [builder role](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/agents/backend-builder.md#L11-L29)
- Basis: Pinned executable wiring and supplied role definition.
- Confidence: High.
- Caveats: Model providers and target repositories were not used at runtime.

## S2 — Coordination

- State: C
- Function: Attenuate contention among independent ticket jobs and between roles that would write the same job worktree.
- Disturbance / variety regulated: Concurrent jobs can contend for workers and overlapping project files. Builder roles within a job share a writable tree.
- Decisive decision or feedback right: Supply stage claims, isolation, writer ordering and bounded worker admission.
- Decision owner: The first-party factory constructor supplies the coordination rules.
- Supporting / enforcement mechanisms: Job-specific worktrees, serialized build/test role groups, distinct stage-attempt result files and bounded thread pool.
- Closure path: The launcher executes write groups in order, consumes results, then advances another stage or job. Independent worktrees keep unmerged effects separate.
- Boundary reachability: The normal runner honors the pipeline group's parallel flag and processes exact result files.
- Why this is / is not agent-owned: Coordination is first-party and function-specific. The deployed runner follows configured relationships.
- Evidence: [job worktree setup](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/scripts.py#L30-L51), [stage and attempt claims](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/engine.py#L74-L156), [role results and group execution](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/runner.py#L83-L118), [headless dispatch and job capacity](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/runner.py#L127-L154), [sequential write stages](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/defaults/pipeline.json#L24-L49)
- Basis: Pinned interference mechanism and return.
- Confidence: High for one launcher.
- Caveats: Persisted stage lock records were not treated as proof of atomic multi-launcher arbitration.
- Distinct S1 units: Independent ticket job agents and backend/frontend writers sharing an individual job's output branch.
- Inter-S1 disturbance: Parallel jobs can overwrite shared local files or overload workers. In-job writers can touch the same worktree.
- Attenuating coordination relation: Per-job worktrees and bounded worker groups, with serialized write-capable stages inside a job.
- Feedback into subsequent S1 behaviour: Completed role outputs unlock the next stage. Conflicted or failed outcomes shape subsequent attempts.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The separation and ordering respond to concrete shared-file and execution-resource interference.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate a current job commitment across implementation, verification, review and release.
- Disturbance / variety regulated: Different operating roles may report incompatible evidence, a prior risk judgment can become invalid, or a job may be unable to advance.
- Decisive decision or feedback right: Choose to proceed, return work for repair or suspend the commitment pending higher-level judgment.
- Decision owner: The installed approver model in the ordinary release path. The human operator in the separate paused-job mode.
- Supporting / enforcement mechanisms: Stage status aggregator, risk and gate-on-head enforcement, paused state and recorded operator action.
- Closure path: Approver verdicts go to merge, rebuild or operator hold. The parent can reject, resume or select the retry stage, after which execution uses the saved decision.
- Boundary reachability: The default job graph installs the same approver as a callable role and the CLI has a first-party paused-job control entry.
- Why this is / is not agent-owned: Agent judgment affects the job across roles. Code applies the transition. The human operator owns the different exception-mode judgment.
- Evidence: [approver's current release judgment](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/agents/approver.md#L9-L34), [review and release transition rules](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/defaults/pipeline.json#L57-L96), [stage result aggregation and return](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/engine.py#L196-L233), [human intervention and re-entry](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/engine.py#L279-L303), [current factory status](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/cli.py#L91-L113), [merge policy and scoped override](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/policy.py#L10-L45)
- Basis: Pinned evidence-to-current decision and distinct parent return.
- Confidence: High within one coordinated job.
- Caveats: This grade does not imply autonomous reallocation or reprioritization across all independent factory jobs.
- Whole-system current view: The approver receives the whole current job's spec, current diff, gate results, risk and prior independent findings. The operator can inspect live job status and history.
- Current-control decision scope: Send the job to correction, keep it on hold for a human, allow its current integration step, or in the parent mode abandon or retry an identified stage.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Shipped approver role | Current job reaches final approval | Its assessment redirects the job to rebuild, escalates it or enables guarded merge | [approver's current release judgment](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/agents/approver.md#L9-L34), [review and release transition rules](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/defaults/pipeline.json#L57-L96) |
| Parent (`P`) | Legitimate factory operator | An explicit paused or blocked job | Record approve, reject or retry, then change the current commitment or re-enter the runner | [human intervention and re-entry](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/engine.py#L279-L303), [merge policy and scoped override](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/policy.py#L10-L45) |

## S3* — Complementary audit

- State: A
- Function: Independently examine the actual candidate change against its accepted specification and feed material discrepancies into current control.
- Disturbance / variety regulated: Builder assertions or ordinary tests can miss requirements and harmful side effects.
- Decisive decision or feedback right: Judge whether a blocking discrepancy exists in the actual changes.
- Decision owner: Factory's separate code-review and specialized reviewer roles.
- Supporting / enforcement mechanisms: Role-scoped context, direct Git diff and source reads, typed findings and stage precedence.
- Closure path: Blocking findings redirect the current job to build and are included in the next brief. Findings and gate results also reach the final approver.
- Boundary reachability: The default pipeline automatically launches separate review roles on the proposed branch, with supported role-specific evidence access and structured feedback.
- Why this is / is not agent-owned: Reviewers make their own artifact-grounded judgment. No model-vendor distinction is needed.
- Evidence: [independent diff review role](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/agents/code-reviewer.md#L10-L35), [Claude worker invocation](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/runner.py#L45-L63), [review and release transition rules](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/defaults/pipeline.json#L57-L96), [stage result aggregation and return](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/engine.py#L196-L233), [rebuild feedback](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/compose.py#L44-L60), [approver's current release judgment](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/agents/approver.md#L9-L34)
- Basis: Pinned review material, independent context and corrective return.
- Confidence: High.
- Caveats: Role prescriptions and the headless tool selections are source evidence. They are not a claim that every host mode enforces complete read-only isolation.
- Claim being audited: The current proposed branch implements the accepted criteria and is suitably tested.
- Ordinary reporting path: Builder/test result JSON and the deterministic gate.
- Complementary access path: A different dispatched role reads the full diff against base and surrounding source, and can examine tests independently.
- Independence boundary: Separate review assignment and model invocation with no authorship of the candidate change, using direct repository evidence.
- Who acts on findings: The engine routes blocking findings to builders; the final approver checks that earlier findings are resolved.

## S4 — Outside-and-then intelligence

- State: —
- Function: No established model-to-future-capability adaptation loop for the factory itself.
- Disturbance / variety regulated: New tickets and project environments can change the work demanded of the factory.
- Decisive decision or feedback right: No supplied judgment over future factory capabilities with a returned adoption decision.
- Decision owner: No qualifying runtime S4 owner.
- Supporting / enforcement mechanisms: Initial domain setup and tracker intake sense different aspects of the environment.
- Closure path: The live loop allocates work to existing roles. Setup configures a new factory without a recurring prospective decision path.
- Why this is / is not agent-owned: Product change work and bootstrap stack detection are supplied as S1 and construction surfaces.
- Evidence: [domain setup](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/skills/init/SKILL.md#L10-L29), [Claude Code stage loop](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/skills/run/SKILL.md#L14-L51), [headless dispatch and job capacity](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/runner.py#L127-L154), [stack detection and checks generation](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/init.py#L24-L65)
- Basis: Bounded absence over setup, runtime transitions and role boundaries.
- Confidence: Moderate.
- Caveats: The operator can later edit domain setup using external judgment.

### Absence scope

- Surfaces inspected: Factory init, project stack detection, issue intake, pipeline feedback and operator configuration.
- Plausible first-party paths checked: Environment-driven changes to roles, gates or durable factory capabilities after activation.
- Why no material first-party path remains: Setup prepares components and checks, and runtime feedback corrects the current job. The reviewed pipeline does not investigate alternative future factory capabilities and return an adoption decision.

## S5 — Policy and identity

- State: —
- Function: No supplied closure over ultimate identity or policy for the installed factory.
- Disturbance / variety regulated: Operating roles may encounter business-risk, safety and protected-path choices.
- Decisive decision or feedback right: No escalated identity-level issue is decided and returned as a persisting policy decision for later jobs.
- Decision owner: The external domain owner defines settings. The installed operator decides current job exceptions.
- Supporting / enforcement mechanisms: Protected domain files, predefined rights, task-specific merge approval and deterministic guard.
- Closure path: A job override is stored for that job and cannot resolve a persistent identity-policy conflict by itself.
- Why this is / is not agent-owned: The organization starts from human-authored domain and merge policy. Its live human command resolves a current case.
- Evidence: [domain setup](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/skills/init/SKILL.md#L10-L29), [protected configuration](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/hooks/guard.py#L116-L131), [human intervention and re-entry](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/engine.py#L279-L303), [merge policy and scoped override](https://github.com/Nabwinsaud/forgeline/blob/2a2d2b7d9ffcb7183f7b77261eb1f54a1fd729ad/forgeline/policy.py#L10-L45)
- Basis: Bounded absence across authored policy and live operator surfaces.
- Confidence: Moderate.
- Caveats: Maintainer policy and project governance lie outside the factory's live loop.

### Absence scope

- Surfaces inspected: Domain onboarding, policy and guard sources, current job types and human resolution.
- Plausible first-party paths checked: Escalation of an ultimate policy question, role changes and authoritative return that governs subsequent jobs.
- Why no material first-party path remains: Allowed human actions operate on one current job. Domain files remain configured by a human outside an observed runtime decision-to-policy loop.

## Recursion

The job groups distinct role operations under a persistent state machine. A role or worktree is not treated as a fully viable nested organization. Factory-level portfolio policy is separate from job-scoped S3.

## Variety and escalation

Worktree isolation, attempts, first-party findings and current status handle scoped interference and faults. The human pause path absorbs unresolved present decisions.

## Evidence gaps

Static source reconstruction at the fixed revision. No model was called, no issues or PRs were opened upstream, and no target repository, release or deployment was changed. The primary runner witness is the supplied Claude mode.
