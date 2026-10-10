---
harness_id: monomind
project_name: Monomind
repository: https://github.com/monoes/monomind
review_ref: 4e875ea1b957a8715cef59be7b0bf1684208577a
reviewed_at: 2026-10-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: ?
---

# Monomind

## Review boundary

- System in focus: the shipped Monomind **Org Runtime v2** first-party persistent organization instantiated by `monomind org run`, comprising the org daemon, real per-role model-backed agent sessions, org-defined roles, task DAG, messages, policy gates, evidence/review and human-decision surfaces.
- Purpose and identity: execute an operator-declared organizational goal through a first-party managed roster of autonomous or semi-autonomous role agents, controlling shared task progress, worker lifecycles and decision access.
- Relevant environment: operator's project/workspace and goal, first-party org definition, local files/Git, role-specific tool outputs, external provider/model endpoints and host coding runtimes, human operator, other orgs via cross-process bridge.
- Standard-distribution boundary: packaged CLI/org daemon and wired `orgrt` source. Models, Claude Agent SDK, Codex/OpenCode/Kimi and other external runner implementations provide agent cognition/tool backends and do not donate additional governance functions; **their agent calls are instantiated and regulated by Monomind's own runtime**.
- Credited operating / distribution surfaces: `packages/@monomind/cli/src/orgrt/{daemon,session,agent-runner,task-dag,decisions,completion-gate,policy,approvals,questions,review-packet,session-ledger,org-memory,checkpoint-ops}.ts`, `packages/@monomind/cli/src/commands/org.ts`, and shipped `doc/concepts/org-runtime.md`.
- Adjacent first-party surfaces excluded from ownership: `/mastermind:autodev` and retired prompt-orchestrated `/mastermind:runorgv1`; MCP-only host injection/knowledge graph when not wired to Org Runtime v2; repository CI, benchmark/tests, scripts and maintainer organization; provider/SDK internal reasoning, external agent CLIs, external human organizations and other orgs as separate recursions.
- First-party operating / deployment modes considered: self-hosted `org run`, daemon role hierarchy with task DAG and on-demand role spawns, optional artifact-only reviewer, run-level memory/replay, policy/approval/decision gates, `org serve` scheduled operation and first-party operator CLI.
- Recursion level: **one named running organization**. The boss/coordinator and specialist model-backed role sessions are local operational units; distinct named organizations communicating across processes are outside this unit.
- Reviewed revision: `4e875ea1b957a8715cef59be7b0bf1684208577a`.
- Observation date: 2026-10-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

The README's supported `monomind org run` path starts an actual daemon whose `OrgDef` contains a goal, role topology and policy; this is explicitly distinct from legacy prompt choreography. `OrgDaemon.startOrgInner` selects a boss, instantiates a real runner-backed session for that role, exposes subordinate roles for lazy spawn, initializes a first-party `TaskDag`, and maintains per-role mailboxes, states and policies. A role's `runAgentSession` forwards a mailbox prompt stream plus first-party `org_*` tools to the configured runner, which by default calls the Claude Agent SDK. Each role's model selects operations while Monomind mediates their delivery, policy, persistence and lifecycle. External model backends do not themselves become first-party control owners.

The operator configures the initial roles, goal and constraints. During a run the boss model receives full-goal instructions and model-callable `org_task`, `org_plan_graph`, `org_tasks`, `org_send`, `org_task_split/merge/cancel`, and `org_complete` paths. `TaskDag` enforces dependencies/cycles and avoids dispatching follow-on work until predecessors have closed. The daemon manages resource-limited lazy spawns, crash recovery, checkpoint replay, metering and human approval/gate callbacks. An optional artifact-only reviewer receives a new evidence packet formed from a task's recorded commit/tests and a Git diff, rather than merely the worker's narrative.

- Runtime/session wiring: [daemon.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/daemon.ts), [session.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/session.ts), [agent-runner.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/agent-runner.ts).
- Dependencies/feedback: [task-dag.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/task-dag.ts), [decisions.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/decisions.ts), [mailbox.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/mailbox.ts).
- Review/closure, constraints and human intervention: [review-packet.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/review-packet.ts), [completion-gate.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/completion-gate.ts), [policy.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/policy.ts), [approvals.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/approvals.ts), [questions.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/questions.ts).
- Cross-run persistence: [org-memory.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/org-memory.ts), [session-ledger.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/session-ledger.ts), [checkpoint-ops.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/checkpoint-ops.ts).

## Operational model

Operational outcomes are the project-specific deliverables each assigned role works toward. The boss is an agent that also performs coordination/current-management work for the org; specialist roles execute local assigned tasks in their respective SDK/model sessions. Roles are not counted as S1 just because `roles` lists them: the witnessed units are the distinct **executing** role-agent sessions, each with task goal, workspace and model/tool feedback. The runtime can enforce limits and sequence those units without owning the model's decisions. The operator's org definition sets the initial purpose/permissions and remains a parent constraint, not an automatic S5 claim.

## S1 — Operations

- State: A
- Function: execute assigned work in the project's environment through individual model-backed agent sessions with tools and returned feedback.
- Disturbance / variety regulated: evolving task requirements, workspace state, tool failures, peer requests and external output.
- Decisive decision or feedback right: each role model chooses task-specific tool calls, reasoning steps, replies and local completion behaviour.
- Decision owner: the configured model-backed role-agent session; Monomind owns the first-party composition/wiring, not cognition itself.
- Supporting / enforcement mechanisms: `ClaudeAgentRunner`/other runner adapters, `runAgentSession`, role mailbox, policy gates, project file permissions, host SDK/tool implementations, budget metering and crashes/restarts.
- Closure path: boss/peer/task mailbox message → autonomous role session → model-selected tools/communications → results → further local decisions and task reporting.
- Boundary reachability: `org run` starts boss and lazily instantiates real subordinate runner sessions; org tools are wired to daemon actions in the shipped runtime, not a standalone example.
- Why this is / is not agent-owned: without model-backed sessions, the remaining daemon can enforce and route requests but cannot produce materially the same task-specific discretionary work.
- Evidence: [daemon.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/daemon.ts), [session.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/session.ts), [agent-runner.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/agent-runner.ts), [Org Runtime documentation](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/doc/concepts/org-runtime.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: roles have differing permissions and runners; this state does not claim Monomind implements the underlying model.

## S2 — Coordination

- State: A
- Function: attenuate premature and conflicting progress across interdependent role-agent work units through agent-selected dependency edges and first-party gating/feedback.
- Disturbance / variety regulated: a downstream role executing or closing before an upstream role's required product exists; duplicated/early task dispatch and divergent assumptions about dependency completion.
- Decisive decision or feedback right: coordinator model chooses role assignments and dependency structure (`org_task`/`org_plan_graph`), receives result/status and may split/merge/rework the plan; the DAG enforces eligibility but does not choose what work depends on what.
- Decision owner: model-backed org coordinator for dependency/assignment discretion; deterministic `TaskDag` owns only admissibility/enforcement.
- Supporting / enforcement mechanisms: task DAG statuses and cycle checks, `dispatchReadyTasks`, role mailbox dispatch, evidence-based completion and requeue.
- Closure path: coordinator chooses dependent role tasks → DAG holds dependents → predecessor reports completion → DAG promotes and dispatches successor → recipient S1 acts on up-to-date prerequisite and sends result for further coordination.
- Boundary reachability: `runAgentSession` exposes task creation/planning/listing and the daemon registers those callbacks on running orgs with real subordinate roles.
- Why this is / is not agent-owned: the deterministic DAG could enforce a frozen plan without model cognition, but the coordinator supplies task/dependency judgment at runtime and revises it from operational feedback.
- Distinct S1 units: at least two instantiated agent roles, e.g., implementing role plus dependent validating/integration role, with separate sessions and task ownership.
- Inter-S1 disturbance: code explicitly guards a task being completed early from promoting its dependents **before required work exists**; a dependency creates a concrete upstream/downstream interference risk, not merely a message routing convenience.
- Attenuating coordination relation: `TaskDag.add` records dependency ownership, `TaskDag.complete` checks unsatisfied prerequisites, and `dispatchReadyTasks` sends newly ready work only to an available assigned role.
- Feedback into subsequent S1 behaviour: predecessor completion changes DAG state, unlocks dependent role's mailbox task and allows the next independent agent session to proceed.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the witness is prevention of premature dependent S1 operation with explicit dependency/commitment feedback, not bare `org_send`, a role label or a queue.
- Evidence: [task-dag.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/task-dag.ts), [decisions.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/decisions.ts), [session.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/session.ts), [daemon.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/daemon.ts).
- Basis: structural + explicit.
- Confidence: medium.
- Caveats: the witness concerns a structurally evidenced dependent-work disturbance, not general prevention of every concurrent filesystem conflict; the coordinator must actually instantiate at least two role S1 units. A narrower single-worker deployment would not independently provide this S2 witness.

## S3 — Inside-and-now control

- State: A
- Function: regulate current org-wide task portfolio, worker allocation and corrective intervention toward the declared whole goal.
- Disturbance / variety regulated: misallocated ongoing commitments, exhausted/crashed roles, prematurely declared completion and blocked/unfinished tasks.
- Decisive decision or feedback right: boss model views task portfolio, allocates/reallocates work, chooses next phase, can split/merge/cancel tasks, requests repair/review, and declares goal outcome subject to programmatic fact gates.
- Decision owner: boss/coordinator model for substantive present-work decisions; operator establishes initial goals/policy; daemon controls enforcement/spawn/restart.
- Supporting / enforcement mechanisms: task DAG, `org_tasks`, `org_respawn_role`, run-completion admissibility checks, role/budget status, mailbox, daemon crash and concurrency gates.
- Closure path: task/role outcomes enter the coordinator's tool and message stream → coordinator selects assignments, interventions or completion → tools change task/role state → further role sessions receive modified work.
- Boundary reachability: tools and daemon callbacks are present in `org run` sessions, with `org_complete` attached to the selected boss and task controls wired per running org.
- Why this is / is not agent-owned: static config/budgets constrain the coordinator but do not make discretionary current task/resource choices; counterfactually removing the boss leaves only fixed scheduling/enforcement.
- Whole-system current view: `org_tasks` returns the org-wide running task DAG; role outcomes and messages return to the boss, and `org_list_runtime_options`/`org_respawn_role` provide intervention on role capacity.
- Current-control decision scope: agent-chosen distribution, dependencies, cancellation/replacement, phase progression and termination for the named org.
- Evidence: [daemon.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/daemon.ts), [session.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/session.ts), [decisions.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/decisions.ts), [completion-gate.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/completion-gate.ts).
- Basis: structural + explicit.
- Confidence: high.
- Caveats: budget monitors and hard limits are enforcement, not autonomous S3 ownership; a human operator may constrain the model but no separate organization-wide parent-mode S3 loop is claimed here.

## S3* — Complementary audit

- State: A
- Function: optionally challenge an implementing role's reported deliverable using independent current Git artifacts and recorded acceptance evidence.
- Disturbance / variety regulated: accepted completion narratives that mask divergent code, failing checks, incorrect implementation or stale evidence.
- Decisive decision or feedback right: separately prompted, artifact-only reviewer agent interprets evidence and returns `VERDICT: APPROVE|REJECT` plus findings.
- Decision owner: reviewer role model for the audit judgment; requester/coordinator owns corrective operational response.
- Supporting / enforcement mechanisms: `org_review` admission (only for `review_input: artifact-only`), `buildReviewPacket`, `reviewDiff`, Git commit/test evidence, fresh task-scoped/cold reviewer session and mailbox delivery.
- Closure path: implementing role submits task evidence → requester invokes `org_review` → reviewer receives evidence plus direct diff → independent verdict returns via `org_send` → requester can require corrections and subsequent task work. This is an available feedback path, not a guarantee every configured org requests a review.
- Boundary reachability: standard Org Runtime v2 conditionally installs `org_review` when the org config includes an artifact-only reviewer, and `dagRequestReview` actually pushes the packet to its running session.
- Why this is / is not agent-owned: producing a distinct code-review judgment requires the reviewer's model; parsing and dispatch do not own its substantive findings.
- Claim being audited: task was completed correctly at claimed `headSha` with stated acceptance results.
- Ordinary reporting path: implementer's `org_task_done` summary, completion evidence and task-status channel.
- Complementary access path: `reviewDiff` resolves a Git diff between the selected base and claimed commit, and the evidence packet carries concrete check outputs rather than the implementer's narrative.
- Independence boundary: reviewer role requires an artifact-only intake and `cold` session scope, separated from implementer's prior model dialog; packet intentionally excludes implementer conversation and asks for file:line findings.
- Who acts on findings: requesting coordinator/role receives the structured verdict via org messaging and can allocate corrective work/review again.
- Evidence: [decisions.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/decisions.ts), [review-packet.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/review-packet.ts), [session-ledger.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/session-ledger.ts), [session.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/session.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: optional role; no proof of a mandatory automatic rejection gate for every code output. This credits a reachable complementary review path, not universal audit coverage.

## S4 — Outside-and-then intelligence

- State: ?
- Function: prospectively investigate environmental changes and generate adaptation options for the org's future operating capability; the complete mapping is not yet established.
- Disturbance / variety regulated: changing external requirements, project knowledge or future operating conditions; which adaptive decisions are closed is unresolved.
- Decisive decision or feedback right: uncertain. Models can `org_learn` from work and retrieve future knowledge, but the inspected path does not establish a separately reconstructable prospective environmental option-selection/return loop.
- Decision owner: unresolved; coordinator model supplies learning content, while the persisted knowledge graph supplies storage and recall.
- Supporting / enforcement mechanisms: `org_learn`, knowledge search/recall, run summary/memory and resumption briefings.
- Closure path: cross-run knowledge returns to a later model prompt; whether that information reflects a concrete outside-and-then adaptation choice that changes current S3 capability was not established.
- Boundary reachability: org knowledge/memory tools are wired into standard running role sessions; positive S4 mapping is intentionally withheld.
- Why this is / is not agent-owned: agent-generated lessons may influence choices; persistence plus retrospective insight alone is insufficient to attribute the S4 function.
- Evidence: [org-memory.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/org-memory.ts), [session.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/session.ts), [daemon.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/daemon.ts).
- Basis: structural + unknown.
- Confidence: medium (in the insufficiency finding).
- Caveats: this is `?` rather than `—` because prospective external adaptation might be instantiated in supported organization definitions not exhaustively inspected here.

## S5 — Policy and identity

- State: ?
- Function: legitimate whole-organization identity/ultimate-policy closure at the declared recursion remains unverified.
- Disturbance / variety regulated: conflicts concerning overall purpose/legitimacy/ultimate organizational policy, distinguishable from ordinary tool approvals.
- Decisive decision or feedback right: the operator writes an org goal and role policies and may reload them; no evidenced identity-level issue → legitimate authority → returned definitive decision loop was reconstructed in the inspected runtime.
- Decision owner: operator/configuration for declared goal and policy constraints; not automatically an S5 parent mode.
- Supporting / enforcement mechanisms: `OrgDef`, `PolicyEngine` role tools/budgets and hot reload, per-action `org_gate` and `ask_human`, operator CLI.
- Closure path: ordinary gate answers and policy/config changes return into execution; their status as **ultimate-policy** decisions rather than operational permissions is unresolved.
- Boundary reachability: operator policy reload and human action gates are supported but do not establish identity-level S5 closure on their own.
- Why this is / is not agent-owned: model roles can request operational exceptions, while operator-owned rules constrain them; nothing inspected shows the agent can autonomously settle ultimate identity matters.
- Evidence: [types.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/types.ts), [policy.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/policy.ts), [decisions.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/decisions.ts), [questions.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/questions.ts), [approvals.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/approvals.ts), [session.ts](https://github.com/monoes/monomind/blob/4e875ea1b957a8715cef59be7b0bf1684208577a/packages/%40monomind/cli/src/orgrt/session.ts).
- Basis: structural + unknown.
- Confidence: medium (in the insufficiency finding).
- Caveats: publication `P` requires an actual parent S5 issue and return path, not simply a human with edit permission; avoid inferring `—` without exhaustive negative-state source coverage.

## Distributed OSS parent arrangement

This assesses one locally instantiated Monomind org. A distributed community of Monomind contributors and its development/CI governance is a separate system. Multiple operators and published org templates are not proof of a common project-level S5 parent. The local operator is not credited as a function-specific parent mode absent a witnessed organizational closure.

## Self-hosted and non-human modes

The standard self-hosted daemon can execute without constant human intervention, while operator controls, `ask_human` and `org_gate` are first-party supported. Their concrete permission/approval scope is not promoted into S3/S4/S5 `(P)` without a qualifying whole-system parent decision right. A single boss and multiple model-backed roles are enough for locally owned S3 decisions in a configured multi-role organization; the role hierarchy by itself is not sufficient.

## Recursion

One named org is the focal recursion; role-agent sessions have bounded local tasks and discretionary tool choices, but their own complete metasystems are not assumed. Other named orgs connected through broker/cross-process messaging are peers or adjacent systems, not automatically subordinate S1 units of this org.

## Variety and escalation

Project/user/tool disturbances are absorbed by role agents where permitted. Dependencies, mailbox coordination and org-wide task tools mediate inter-role variety. Budget/tool/approval constraints can block action; `ask_human` and `org_gate` escalate named operational issues to the operator. Crash/restart and checkpoint recovery preserve work context but do not themselves demonstrate S4/S5 autonomy.

## Evidence gaps

- Independently test a representative deployed two-role dependent-work organization to confirm S2 closure and whether its agent decisions really establish nontrivial interference attenuation beyond DAG sequencing; preserve S2 medium confidence.
- Verify whether artifact-only verdicts demonstrably induce follow-up work and whether the intended cold-session independence is enforced across each runner, not merely available in the default route.
- Investigate concrete prospectively environment-facing `org_learn` workflows and any legitimate ultimate-policy issue/decision channel before replacing either `?`.
- Repository documents describe many runtime adapters; their host-owned behaviour and model reasoning remain outside first-party credit. No live provider invocation or end-to-end run was performed in this repository review.
