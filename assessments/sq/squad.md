---
harness_id: squad
project_name: Squad
repository: https://github.com/bradygaster/squad
review_ref: 2099faf51c08a912c359209447011b06decf0565
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Squad

## Review boundary

- System in focus: Squad's first-party persistent team runtime, Coordinator, member agents, shared `.squad/` state, reviewer protocol, Ralph watch loop and human-team/parent governance paths at pinned revision `2099faf51c08a912c359209447011b06decf0565`.
- Purpose and identity: provide a persistent human-led AI software team whose specialist agents execute work, coordinate through explicit team state, regulate current commitments, review each other's outputs and remain ultimately governed by the human operator.
- Relevant environment: target repository, GitHub/GitLab issues and PRs, GitHub Copilot/model hosts, human operator/reviewers, CI/test state and external project constraints.
- Standard-distribution boundary: Squad CLI/templates/prompts/state protocol, Coordinator/Scribe/Ralph/reviewer conventions and watch execution machinery. GitHub Copilot/model service and external human communication remain outside the implementation boundary but can be actors in first-party supported modes.
- First-party operating/deployment modes considered: interactive Coordinator-led team operation, parallel agent execution, reviewer gates, Ralph watch/execute mode, human roster members and human final-arbiter intervention.
- Recursion level: one repository/project Squad organization. Specialist agents are S1 operational units; human team members are parent/participant actors where the first-party protocol routes authority to them.
- Reviewed revision: `2099faf51c08a912c359209447011b06decf0565` from the repository's `dev` default branch.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.1`.

## Repository architecture

Squad persists a team roster, routing rules, decisions, per-agent charters/context/history and orchestration logs under `.squad/`. The Coordinator reads requests and routing state, decomposes work, launches specialist agents in parallel or sequentially according to dependencies, collects results and enforces reviewer gates. Scribe merges team decisions into shared memory. Ralph can continuously inspect issue/team context, delegate issue selection to an agent, dispatch execution and apply tiered recovery/escalation. Human members can occupy review/approval roles; the user can override decisions, change the roster and durable directives, and receives escalations when automated current-control paths cannot resolve the situation.

## Primary evidence

- [`README.md`](https://github.com/bradygaster/squad/blob/2099faf51c08a912c359209447011b06decf0565/README.md) — human-led team boundary, persistent state, Ralph watch/execute loop and tiered recovery/escalation.
- [`docs/src/content/docs/concepts/architecture.md`](https://github.com/bradygaster/squad/blob/2099faf51c08a912c359209447011b06decf0565/docs/src/content/docs/concepts/architecture.md) — Coordinator, agent, Scribe and Ralph topology and team-wide state flow.
- [`docs/src/content/docs/concepts/parallel-work.md`](https://github.com/bradygaster/squad/blob/2099faf51c08a912c359209447011b06decf0565/docs/src/content/docs/concepts/parallel-work.md) — dependency analysis, parallel/sync execution, deadlock handling and concurrency control.
- [`docs/src/content/docs/concepts/your-team.md`](https://github.com/bradygaster/squad/blob/2099faf51c08a912c359209447011b06decf0565/docs/src/content/docs/concepts/your-team.md) — team formation, human members, reviewer protocol, lockout/reassignment/escalation, final human arbiter and auto-triggered design review/retrospective.
- [`docs/src/content/docs/features/routing.md`](https://github.com/bradygaster/squad/blob/2099faf51c08a912c359209447011b06decf0565/docs/src/content/docs/features/routing.md) — first-party routing and multi-agent shared-state protocol.
- [`docs/src/content/docs/features/memory.md`](https://github.com/bradygaster/squad/blob/2099faf51c08a912c359209447011b06decf0565/docs/src/content/docs/features/memory.md) — durable user directives/team decisions and return into later agent behaviour.

## Operational model

Specialist AI members are real S1 work units: each has its own context/role/history and independently produces repository/project outcomes. The Coordinator supplies more than task routing: it analyzes dependencies, decides parallel versus synchronous execution, mediates multi-agent shared-system work and performs team-wide current regulation. Review is a separate path: a Lead/Tester can reject another agent's work, after which the original author is locked out and work is reassigned or escalated. Humans are not incidental HITL; first-party modes explicitly route review/current-control matters to human members and reserve final organizational authority to the user.

## S1 — Operations

- State: `A`.
- Function: specialist agents autonomously implement, test, document, review or otherwise produce project outcomes in their bounded domains.
- Disturbance / variety regulated: repository/task uncertainty, tool results, implementation choices and domain-specific work state.
- Decisive decision or feedback right: each spawned specialist chooses local work actions within its charter/task boundary.
- Decision owner: model-driven specialist agent.
- Supporting / enforcement mechanisms: per-agent contexts, charters, histories, tools and isolated/background execution modes.
- Closure path: agent work changes repository/task state and returns labeled results into the team workflow.
- Basis / confidence: explicit + structural; high.

## S2 — Coordination

- State: `A`.
- Distinct S1 units: multiple specialist agents executing work in parallel or in dependency chains.
- Specific interference / oscillation: parallel agents can have data dependencies, circular dependencies or modify shared systems in ways that create conflicting implementations; the documentation explicitly warns and supplies design-review/dependency handling for these conditions.
- Coordination relation: the Coordinator performs dependency analysis, chooses fan-out versus synchronous sequencing, detects circular dependencies and mediates resolution; multi-agent shared-system work can auto-trigger a Design Review so agents surface interfaces/risks/contracts before continuing.
- Decisive right / owner: the model-driven Coordinator/Lead chooses the coordination response within the first-party team protocol rather than merely relaying messages.
- Supporting mechanisms: routing tables, shared `.squad/` state, background/sync execution and concurrency limits.
- Closure path: coordination decisions alter later S1 ordering, participation, shared decisions and execution constraints before work proceeds.
- Why not generic routing: the positive mapping rests on explicit dependency/cycle/shared-system conflict regulation, not named/domain dispatch alone.
- Basis / confidence: explicit + structural; high.

## S3 — Inside-and-now control

- State: `A(P)`.
- Autonomous mode function: regulate live whole-team commitments, assignment, concurrency, intervention and exception handling.
- Whole-system current view: Coordinator/Ralph consume team state, available issues, recent decisions, work status and agent capabilities.
- Autonomous decisive right / owner: Coordinator/Ralph-backed agent logic selects work, chooses which members execute it, decides parallel/sync structure, monitors execution and applies/recommends intervention; reviewer rejection can force reassignment rather than letting an S1 self-repair indefinitely.
- Supporting mechanisms: routing manifests, orchestration logs, watch polling, status/health surfaces and tiered recovery enforcement.
- Autonomous closure: decisions change assignment/execution/recovery state and subsequent team operation.
- Parent mode: when current control exceeds autonomous authority, the first-party protocol pauses/routes to a human member or escalates to the user. If all capable agents are reviewer-locked, the Coordinator offers parent choices such as manual fix, unlock with guidance or close; the returned human decision changes subsequent current operation.
- Parent owner: legitimate human team member/user at the project recursion.
- Why `A(P)`: autonomous current-control closure and a distinct operationally closed human-parent mode are both first-party supported; they are alternative ownership modes, not simultaneous dual control.
- Basis / confidence: explicit + structural; high.

## S3* — Complementary audit

- State: `A`.
- Claim being audited: that an S1 agent's submitted implementation/work is acceptable for correctness, quality, architecture/security or test criteria.
- Ordinary reporting path: the producing agent returns its result/history through the Coordinator.
- Complementary access path: a separate Lead/Tester reviewer inspects the work under reviewer authority rather than relying on the author's own success claim.
- Independence boundary: on rejection, the original author is locked out from self-revision for that task; the Coordinator must reassign work to another agent or escalate, preventing the audited S1 from owning both judgment and corrective disposition.
- Decisive feedback right / owner: the reviewer agent approves or rejects within its stated scope.
- Closure path: approval permits progression; rejection records the finding, locks the author and routes correction to a different actor or parent authority.
- Basis / confidence: explicit + structural; high.

## S4 — Outside-and-then intelligence

- State: `—`.
- Retrospectives, personal histories, shared decisions and reusable skills improve organizational memory and can change later behaviour, but the reviewed evidence is primarily internal/project-experience learning. It does not establish a distinct externally and prospectively oriented environmental-intelligence function that models changing future conditions, develops adaptation options and closes them into present capability through S3.
- Confidence: high.

## S5 — Policy and identity

- State: `P`.
- Identity / ultimate-policy issue: composition and role identity of the team, durable project directives/conventions and final resolution of decisions that the organization may not override autonomously.
- First-party parent path: during initialization Squad proposes a roster, but the human confirms/customizes it before materialization; later the user may add/remove/redefine members and establish durable “always/never” directives.
- Ultimate authority: the documentation names the user as the final arbiter who can override any decision.
- Return-to-operation path: parent roster/charter changes are materialized into `.squad/team.md`/agent charters/routing, while durable directives enter `decisions.md`; subsequent agents read the current team/decision state before working, so the returned parent decision governs later operation.
- Why not autonomous S5: Coordinator/Scribe may propose or propagate policy-like material, but the reviewed first-party boundary does not give them legitimate ultimate authority over team identity or final policy against the user.
- Why `P` rather than generic HITL: the evidence concerns organization identity/durable policy and includes a reconstructable parent decision → persisted rule/team definition → subsequent-operation closure.
- Basis / confidence: explicit + structural; medium-high.

## Distributed OSS parent arrangement

This assessment concerns one deployed Squad project organization, not the public repository's contributor governance. The parent-mode claims are local to the supported project/team recursion and do not infer a single organization-level parent across unrelated OSS contributors.

## Self-hosted and non-human modes

The standard distribution supports autonomous agent operation plus explicit human-led modes. Absence of autonomous S5 is not treated as a deficiency; ultimate authority intentionally remains with the user in the evidenced parent-governed mode.

## Recursion

Specialist members have durable roles and local contexts but are not automatically complete viable systems. Spawning or parallel execution is not itself counted as VSM recursion.

## Variety and escalation

Parallel specialists amplify operational variety. Dependency analysis, routing, shared decisions, design review and reviewer lockout attenuate destructive interference. Ralph's recovery ladder escalates unresolved current-control disturbances toward human intervention, while user directives and roster decisions return through persistent team state.

## Evidence gaps

No S4 state is inferred from memory/retrospectives without evidence of an external-and-prospective adaptation conversation. Parent modes are credited only where a first-party route and returned closure are documented.

## Admission conclusion

Canonical vector: `A A A(P) A — P`.
