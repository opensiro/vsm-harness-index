---
harness_id: cogitator
project_name: Cogitator
repository: https://github.com/cogitator-ai/Cogitator-AI
review_ref: 67b4fde644f648bc1df02a1ab38b211cf2171fbd
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Cogitator

## Review boundary

- System in focus: A single self-hosted Cogitator runtime instance performing a user-specified task through first-party model-tool calls, with optional first-party `swarms` team/consensus, `workflows`, `memory`, `self-modifying` and evaluation packages. Not a hypothetical customer business, its hosting organization or Cogitator's own upstream development governance.
- Purpose and identity: Let an application owner instantiate model-operated tools, multi-agent teams, structured workflows, durable run recovery and current-task improvements under owner-chosen goals and permissions.
- Relevant environment: User requests, tool/environment responses, workspace, teammate outputs, errors, model/provider variability, external content available to configured tools, and operator deployments.
- Standard-distribution boundary: Shipped `@cogitator-ai/core` Agent/Cogitator runtime and optional published monorepo `swarms`, `workflows`, `memory`, `self-modifying` packages. The actual LLM model, credentials, domain application, live deployed agents, organization mandates and custom tools are external.
- Credited operating / distribution surfaces: `packages/core/src/agent.ts`, `packages/core/src/cogitator.ts`, `packages/core/src/cogitator/tool-executor.ts`, `packages/swarms/src/strategies/team.ts`, `packages/swarms/src/team/board.ts`, `packages/swarms/src/tools/team.ts`, `packages/swarms/src/strategies/consensus.ts`, `packages/swarms/src/strategies/hierarchical.ts`, optional `packages/self-modifying/src`.
- Adjacent first-party surfaces excluded from ownership: `@cogitator-ai/evals` offline model/agent comparison and CI, studio debugging, documentation examples, operator-owned policies, arbitrary user-provided roles and tools, infrastructure queue durability, third-party hosted LLM decisions. Source examples demonstrate reachable composition but are not evidence that every deployment automatically runs those arrangements.
- First-party operating / deployment modes considered: SDK `Cogitator.run(agent,input)` one-agent model/tool loop, optional `swarm(...).strategy('team').lead(...).members(...)` with shared task board and mailbox, hierarchical and consensus swarms, persisted workflows, self-modifying optional package, Studio/approval human UI and provider routing.
- Recursion level: User task/agent team in one configured instance, not the Cogitator software company's governance.
- Reviewed revision: `67b4fde644f648bc1df02a1ab38b211cf2171fbd`; public GitHub repository ID 1124938076, nonfork, nonarchived, MIT, created 2025-12-29T22:04:18Z.
- Observation date: 2026-11-20.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Cogitator is library-first: an owner supplies a model, agent instructions and tool definitions to `Cogitator`, which runs model-directed steps through validated tool calls. `swarms` composes several such agents behind a coordinator, message bus, blackboard and selectable strategy. In the `team` strategy the lead starts a plan, creates and assigns dependencies, workers claim eligible tasks and return results, and the lead reacts to messages/blocked work and synthesizes the result. The `TeamTaskBoard` updates its blackboard synchronously and rejects duplicate simultaneous ownership, preserving one active task per member and dependency conditions. A consensus configuration alternatively gives several model agents vote and discussion rounds and a conflict-resolution result; routing/retries by themselves are not credited as discretionary coordination. Durable workflows, scheduled routines, sandboxing, memory retrieval and host approval are support surfaces, with no assumed independent organizational identity or prospective adaptation authority.

Sources: [architecture](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/docs/ARCHITECTURE.md), [agent runtime](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/core/src/cogitator.ts), [team strategy](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/swarms/src/strategies/team.ts), [shared board](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/swarms/src/team/board.ts), [swarm guide](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/docs/SWARMS.md).

## Operational model

A human configures the task, agent roles and permissions; the running models choose task-specific actions. For a composed team, the lead model issues `create_task`, `assign_task` and `list_tasks`; workers claim tasks, write results and message teammates, and the strategy schedules eligible turns. Events and revised board state return to model-visible tools; human/host policy still controls approval and execution boundaries. A separately declared checker may inspect a draft and return factual challenges to the lead before synthesis; this is a *constructor mode*, not an always-on auditor of arbitrary tasks. Self-modifying tool generation is triggered by current user intent and local failures, and parameter/strategy changes use local-run observations, not proven future external-entropy management.

## S1 — Operations

- State: A
- Function: Produce user/task deliverables by selecting model-driven tool calls and revising the response to task/environment evidence.
- Disturbance / variety regulated: New user inputs, tool results, retrieval, execution errors and unforeseen partial subtask outputs.
- Decisive decision or feedback right: Select tool/arguments, incorporate result, and decide the next task action or final output.
- Decision owner: Active `Agent` model in a configured `Cogitator` run, or respective model worker inside a swarm.
- Supporting / enforcement mechanisms: Model/provider adapter, typed Zod tools, execution loop, history and context builder, permission engine and budget checks.
- Closure path: Owner-supplied goal -> runtime invokes model -> model-selected guarded tool executes -> tool result re-enters model history -> model revises action or final answer.
- Boundary reachability: Public `new Agent`, `new Cogitator`, `cog.run` in shipped core; examples instantiate genuine models and tool functions in the supported API.
- Why this is / is not agent-owned: Runtime enforces typed/permission rules but does not decide the substantive answer. The configured model does, without implying first-party model hosting.
- Evidence: [README quick start](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/README.md), [agent class](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/core/src/agent.ts), [runtime](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/core/src/cogitator.ts), [tool execution](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/core/src/cogitator/tool-executor.ts).
- Basis: explicit and structural
- Confidence: high
- Caveats: Model API credentials and real task execution were not exercised during the assessment.

## S2 — Coordination

- State: A
- Function: Attenuate inter-agent competition over shared tasks and incompatible decisions, coordinating distinct autonomous worker loops.
- Disturbance / variety regulated: Two agents claiming one task, taking blocked work, incompatible proposal choices, duplicate work and dependency conflicts.
- Decisive decision or feedback right: Lead model assigns cross-agent roles/work, updates assignments from board state, and in consensus mode model voters can revise proposals during subsequent rounds; deterministic board guard only prevents invalid claims.
- Decision owner: Model lead for discretionary team coordination and participating model voters for inter-agent consensus; board atomically enforces claim rights under configured team owner.
- Supporting / enforcement mechanisms: `TeamTaskBoard.claimTask` checks synchronous state, dependency/owner constraints and one active task per member; blackboard events, mailboxes, assignment tools, consensus ballot/round policy.
- Closure path: Lead creates/assigns tasks -> workers see and claim eligible tasks -> board prevents competing claims and emits completion/message events -> lead/other agents see updated board or votes -> follow-up assignments, conflict resolution and work choices change.
- Boundary reachability: First-party `@cogitator-ai/swarms` `team`, `hierarchical` and `consensus` strategies in published package; app owner composes the agents.
- Why this is / is not agent-owned: The board itself is an enforcing data structure; agent-owned part is the cross-worker discretionary assignment and decision/feedback inside `team` or vote reasoning.
- Distinct S1 units: At least two workers, each with a separate `Agent` model conversation and tools.
- Inter-S1 disturbance: Contention for one task and changed dependencies on the shared board; disagreement among independent model voters.
- Attenuating coordination relation: Atomic board claims plus team lead and consensus voting/discussion bounds.
- Feedback into subsequent S1 behaviour: `list_tasks`, `read_inbox`, completion/message events and next-round vote context alter subsequent worker/lead action selection.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Built-in concurrency-safe claim arbitration and explicit conflict-convergence rounds regulate mutually interfering independent workers, not only pass messages.
- Evidence: [board](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/swarms/src/team/board.ts), [team tools](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/swarms/src/tools/team.ts), [team strategy](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/swarms/src/strategies/team.ts), [consensus](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/swarms/src/strategies/consensus.ts), [swarm specification](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/docs/SWARMS.md).
- Basis: explicit and structural
- Confidence: high
- Caveats: Single-agent mode alone does not instantiate S2; the `team` or consensus configuration is an optional supported operating mode.

## S3 — Inside-and-now control

- State: A
- Function: Manage whole current-task commitments across team members, dependencies, failed/pending work and integration decisions.
- Disturbance / variety regulated: Incomplete dependencies, worker stalls/failures, unclaimed tasks, competing priorities and partial output.
- Decisive decision or feedback right: Model lead creates work items, sets dependencies, assigns/reassigns work, requests revisions and synthesizes accepted outputs in response to current whole-team status.
- Decision owner: Model leader in supported `team` or hierarchical supervisor mode; runtime scheduler and owner-configured max turns/budgets are enforcing supports.
- Supporting / enforcement mechanisms: Model-visible `create_task`, `assign_task`, `list_tasks`, `request_revision`, blackboard, per-member turn status and result visibility.
- Closure path: Read full current board/results -> lead model chooses reallocation/revision or new task -> board and worker calls change in-flight current work -> completion/event/result returns -> lead revises or concludes.
- Boundary reachability: `TeamStrategy.execute` ensures a lead agent takes the initial and return turns; `HierarchicalStrategy` supplies `request_revision` and `check_progress` and returns final supervisor output.
- Why this is / is not agent-owned: The lead model makes current system-level priority/acceptance judgments; worker-queue scheduling and fixed budget ceilings alone would not establish S3.
- Whole-system current view: Live task board with owner, dependencies, status, results and failures for a single user-task team.
- Current-control decision scope: Replan, reassign, request revisions, integrate or escalate within the owner-declared goal; not resource governance across company deployments.
- Evidence: [team](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/swarms/src/strategies/team.ts), [board](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/swarms/src/team/board.ts), [tools](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/swarms/src/tools/team.ts), [hierarchical](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/swarms/src/strategies/hierarchical.ts), [sample first-party run](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/examples/swarms/05-agent-team.ts).
- Basis: explicit and structural
- Confidence: high
- Caveats: The task-team mode is optional; no hosted org-wide executive or independent S5 is supplied.

## S3* — Complementary audit

- State: C
- Function: Construct a second model-operated reviewer path that challenges draft/worker factual claims before whole-task integration.
- Disturbance / variety regulated: A writer's unverified factual claims might be accepted as final merely because its own report says complete.
- Decisive decision or feedback right: Separate configured reviewer `Agent` inspects a worker draft and returns wrong/unsupported/correct findings; team lead consumes review task result and can require revisions.
- Decision owner: Separately instantiated reviewer model for substantive content verdict, lead model for integration and rework.
- Supporting / enforcement mechanisms: First-party `team` task/dependency board, distinct worker message histories, `update_task` return, optional reviewer assignment and source-check tools.
- Closure path: Parent creates draft/review tasks with dependency -> author completes draft -> reviewer gets draft and available sources -> reviewer records independent assessment -> leader sees reviewer task result -> revision request or changed output.
- Boundary reachability: Published first-party team constructor has a `checker` model role in `examples/swarms/05-agent-team.ts`, which explicitly checks factual support and returns a separate verdict; `@cogitator-ai/swarms` can compose such a role at runtime.
- Why this is / is not agent-owned: When composed, the reviewer itself decides factual support separately from the author; ordinary eval/unit tests and dashboard traces do not count.
- Claim being audited: A separate writer's factual claims in a draft.
- Ordinary reporting path: Worker `writer` composes output and marks its task completed.
- Complementary access path: Reviewer receives the draft and separately supplied source/search tools, not only the author's self-grading; source access and role isolation must be configured for the instance.
- Independence boundary: Distinct model agent and separate task role but no guarantee of different model/vendor, blinded evidence, or independent upstream auditor. Specific first-party construction seam exists; actual audits remain contingent on composition.
- Who acts on findings: Team lead accepts/reworks the draft using the returned checker task verdict.
- Evidence: [checker role + task team](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/examples/swarms/05-agent-team.ts), [team board and task results](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/swarms/src/team/board.ts), [team tools](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/swarms/src/tools/team.ts), [hierarchical revision path](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/swarms/src/strategies/hierarchical.ts).
- Basis: explicit
- Confidence: medium
- Caveats: `C` rather than `A` because the source packages primitives and a working example but not a guaranteed always-on reviewer for arbitrary deployments. Reviewer's raw evidence access is app-configured; source inspection does not prove real model-independent execution.

## S4 — Outside-and-then intelligence

- State: —
- Function: No demonstrable standard first-party loop independently scans external future uncertainty, selects prospective capability options and returns implemented adaptation to current organizational operations.
- Disturbance / variety regulated: New external opportunities/threats and long-run changes to demand, models, technology and operating context could affect future capability.
- Decisive decision or feedback right: Self-modifying `GapAnalyzer` uses the current user's intent and failed attempts to propose task-local tools; `ObservationCollector` measures current-run progress/stagnation and meta-reasoning switches current-run strategy. External future-directed intelligence and authority are not established.
- Decision owner: User/application integrator for persistent architecture/identity choices; none for a separately qualified S4 process in the assessed standard system.
- Supporting / enforcement mechanisms: Self-modifying tool generation, local observation and architecture optimizer, memory upkeep, dynamic model selection, web retrieval and experimental scheduling.
- Closure path: Current task-gap -> generated tool or strategy setting -> current task can improve. This is a current-operation adjustment and does **not** establish external-and-then environmental intelligence returned as sustained new capability.
- Why this is / is not agent-owned: Internal parameter optimization and tactical tool generation are not automatically S4; memory of a previous chat and external web lookup for a present question are still operational.
- Evidence: [self modifying](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/self-modifying/src/self-modifying-agent.ts), [gap analyzer](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/self-modifying/src/tool-generation/gap-analyzer.ts), [run observations](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/self-modifying/src/meta-reasoning/observation-collector.ts), [architecture selection](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/packages/self-modifying/src/architecture-evolution/evolution-strategy.ts), [core memory](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/docs/MEMORY.md).
- Basis: structural
- Confidence: medium
- Caveats: An application can supply external future-sensing and accepted adaptation, but such user-composed components are not evidenced as a bundled S4 path.

### Absence scope

- Surfaces inspected: Published package inventory, model/tool loop, self-modification gap/observation/architecture code, stored memory, workflows, scheduled triggers, model routing, examples and owner-permission interfaces.
- Plausible first-party paths checked: `self-modifying` architecture evolution, tools that fill immediate capability gaps, memory extraction/upkeep, model discovery/routing, scheduled routines and research/tool API.
- Why no material first-party path remains: Each inspected first-party decision either responds to a present task, internal telemetry, or an operator-defined schedule, or needs a separate external customer-defined decision/implementation. No pinned bundled mechanism showed future external signal -> chosen sustained capacity investment -> authoritative present-capability change loop.

## S5 — Policy and identity

- State: —
- Function: No first-party agent-owned or closed parent-governed *ultimate identity/organizational purpose* decision-and-return loop is established at the generic deployed task-team recursion.
- Disturbance / variety regulated: Contradictory operating goals, changes to legitimate organizational mission, and high-priority identity commitments require an ultimate-policy owner.
- Decisive decision or feedback right: Host/application developer configures agent instructions, approvers, execution permissions, providers and team roles; approvals on tools/workflow nodes are tactical safety/control decisions, not proven mission identity governance.
- Decision owner: External application's human owner. Inside the library runtime no sourced S5-specific parent-return mechanism was established.
- Supporting / enforcement mechanisms: Permission modes and approval UI, config files, human workflow nodes, scoped role instructions, optional memory.
- Closure path: Config changes can affect later runs, but no first-party structured identity/policy issue -> legitimate ultimate decision -> accepted revision -> operational feedback loop was shown for this recursion.
- Why this is / is not agent-owned: A model may set tasks and choose tools, but model autonomy within supplied instructions does not authorize redefining the enterprise/personal identity policy. Generic pause/approve is not S5.
- Identity / ultimate-policy issue: User-defined foundational goal and enduring authority hierarchy, not the correctness of one tool execution.
- Ultimate authority in each claimed mode: No positive S5 mode claimed; developer/operator holds the external application policy.
- Return-to-operation path: Host-supplied prompt/config affects future calls, but without a demonstrated first-party governance loop for legitimate identity changes.
- Evidence: [workflow approvals](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/docs/WORKFLOWS.md), [runtime security](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/docs/SECURITY.md), [architecture](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/docs/ARCHITECTURE.md), [memory](https://github.com/cogitator-ai/Cogitator-AI/blob/67b4fde644f648bc1df02a1ab38b211cf2171fbd/docs/MEMORY.md).
- Basis: structural
- Confidence: medium
- Caveats: A real adopting organization can impose S5 policy; this would require separately evidenced system-of-interest boundary and return path, not inferred from API configurability.

### Absence scope

- Surfaces inspected: Task/team operating API, approval and permission, prompts/config, workflow human nodes, memory and dashboard controls, self-modifying package and developer governance artifacts.
- Plausible first-party paths checked: Human-in-the-loop workflow approvals, model rules and instructions, host configuration, system skill/memory entries, policy settings.
- Why no material first-party path remains: All examined policy writes are external initial configuration or per-operation safety/approval; none establishes first-party specific authority to decide or legitimate identity conflicts with an evidenced returned governing decision.

## Distributed OSS parent arrangement

The public Cogitator monorepo is maintained by independent developers, but its OSS contribution/CI review rules are not inherited by a downstream customer's instantiated agent team. No organization-level parent (P) state is inferred from developers, GitHub approvals or shared model-access infrastructure.

## Self-hosted and non-human modes

The self-hosted runtime supports owner-driven provider/permission configuration and human approvals, plus fully model-directed task execution inside configured bounds. Neither generic permission prompts nor scheduled runs warrant S3/S4/S5 `(P)` notation absent a complete function-specific parent-governed mode at the declared operational recursion.

## Recursion

The team lead and members are distinct model-operated task cells with an internal current-task governance relation. Their finite budgets and dependency records do not make each a viable autonomous organizational recursion. An app author may embed several such teams but no unobserved higher recursion is credited.

## Variety and escalation

Dynamic user requirements and worker failures reach agents through tool outputs and task-board events. S2's claim arbitration attenuates worker contention, S3's model lead reallocates/revises current work, and optional constructed reviewer challenges content certainty. Budget exhaustion, absent models, unresolved vote rounds and sensitive approvals can escalate to the host; escalation is not a separate S5 function by itself.

## Evidence gaps

- Static source review, no live external LLM/provider/scheduled deployment or actual completed source-independent audit, and no runtime security test in this assessment.
- S3* C requires user-composed reviewer with independent raw source access and returned task dependency; the example alone does not prove runtime review independence or production prevalence.
- S4 negative finding is bounded to bundled first-party future/environment adaptation, not universal impossibility for user-built workflows.
- S5 boundary excludes legitimate downstream operator governance unless a distinct first-party mandate/return mechanism is shown.
