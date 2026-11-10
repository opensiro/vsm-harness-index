---
harness_id: homerail
project_name: HomeRail
repository: https://github.com/xiaotianfotos/homerail
review_ref: 7b734a06c712b454aad17b36ae385f120cfeb7bb
reviewed_at: 2026-11-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: C
autonomy_s5: —
---

# HomeRail

## Review boundary

- System in focus: Self-hosted HomeRail Manager, model-driven Manager Agent, persistent DAG execution with Node/Worker agents, and the shipped fixed-design E2E Fix workflow. Optional pattern templates are examined as first-party constructors, not presumed active in every run.
- Purpose and identity: Let an operator or Manager Agent define, launch, supervise and verify multi-actor agent workflows with durable orchestration, intervention, evidence and bounded human authority.
- Relevant environment: User objectives, changing worker results, concurrent worker demand, stalled or failed actors, execution costs, disputed repair correctness, CI results, recurring operational failures and approvals.
- Standard-distribution boundary: The built Manager/Node/Worker/CLI and host Manager Agent with configured model backend, plus first-party DAG patterns and the separately prepared E2E Fix workflow. A local owner supplies credentials and accepted execution/policy configuration; external GitHub/CI is an evidence service, not the organizational decision owner.
- Credited operating / distribution surfaces: [system overview](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/README.md), [DAG patterns](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/orchestration/dag-patterns.ts), [Manager Agent tool handlers](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/server/host-codex-manager-agent.ts), [DAG actor interventions](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/persistence/dag-actor-interventions.ts), [E2E Fix workflow](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/orchestration/e2e-fix-workflow.ts), [E2E Fix stage enforcement](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/runtime/e2e-fix-stage.ts).
- Adjacent first-party surfaces excluded from ownership: Repository CI/release and maintainers, sample workflows considered without normal runtime reachability, Docker/host test assertions as discretionary agents, externally authored coding-agent wrappers, third-party GitHub maintainers and provider security policies. They may enforce evidence but cannot be borrowed as HomeRail's own higher VSM authorities.
- First-party operating / deployment modes considered: Conversational host Manager Agent with supervised DAG tools; direct `hr` CLI driving persisted workflows; multiple model Worker agents; optional catalog instantiation (`budget-gate`, `compost`, `standing-goal-sentinel`); separately frozen/pinned E2E Fix mode with three independent model reviewers.
- Recursion level: One HomeRail Manager serving a portfolio of DAG task runs and their S1 Worker agents, with an optional higher Manager Agent controlling those runs. E2E Fix is a particular multi-actor execution mode, not a universal review property of every DAG.
- Reviewed revision: `xiaotianfotos/homerail@7b734a06c712b454aad17b36ae385f120cfeb7bb` (frozen source checkout).
- Observation date: 2026-11-10; static source/docs inspection, not a live provider-backed run or real external PR publication.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

HomeRail's Manager persists workflow definitions, DAG runs, actor state, milestones, durable commands, generations and result artifacts. Nodes provision Worker containers, whose configured agent backends execute model-directed steps and exchange typed handoffs. The host Manager Agent can select/instantiate workflow patterns, create a run, inspect run/actor/supervision state and request targeted retries, reassignment, cancellation or checkpoint intervention. The persistence layer fences stale generations and rejects conflicted intervention tokens. These are distinct roles: Worker models own individual task actions; the Manager Agent can own discretionary aggregate current control; durable orchestration transports and enforces the decisions. [README](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/README.md), [Manager Agent handlers](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/server/host-codex-manager-agent.ts), [intervention persistence](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/persistence/dag-actor-interventions.ts).

The pattern catalog supplies actual bounded orchestration templates, including cross-run budget admission, quorum, independent planner/worker fan-out, standing-goal rechecks and evidence-to-proposal `compost`. A pattern being discoverable/instantiable does not mean its workflow is running or its output automatically modifies Manager policy. The separate E2E Fix workflow requires caller-approved design, frozen runtime/policy, trusted offline tests, host-controlled same-PR publication, independent reviewer model sessions and same-head CI. Failed tests/reviews/CI return evidence to a new Fixer session. [pattern source](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/orchestration/dag-patterns.ts), [E2E Fix guide](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/docs/e2e-fix.md).

## Operational model

The Manager Agent can decompose a requested objective into a DAG or reuse a catalog workflow. Task-performing Worker agents choose model-directed work steps, report typed handoffs and are retried or corrected based on persisted outcomes. Several S1 agents share execution capacity and DAG artifacts, and a host supervisor can change active commitments. The pattern library's deterministic gates are not agent judgment. Independent E2E reviewer sessions have explicit audit judgment; they are not conflated with generic scorecard generation. Configuration, approvals and fixed designs are supplied by operators, but no reviewed first-party constitutional authority resolves ultimate HomeRail identity disputes.

## S1 — Operations

- State: A
- Function: Execute a bounded delegated task through a model-directed Worker, using tools and typed handoffs to other DAG actors.
- Disturbance / variety regulated: Novel user tasks, source/code evidence, tool outputs, implementation failures and evolving upstream worker dependencies.
- Decisive decision or feedback right: Choose task-specific tool operations, implementation content, findings and completion handoff within a caller-defined node contract.
- Decision owner: Model-driven Worker agent for its node; the Manager routes and validates work but does not itself author each Worker decision.
- Supporting / enforcement mechanisms: Node-provisioned container, model adapter, DAG input/output ports, persisted actor execution and retry/cancel enforcement.
- Closure path: DAG input → model Worker action/handoff → tool and downstream evidence → persisted result or failure → fresh Worker/next dependent node decision.
- Boundary reachability: `hr run`/Manager `create-and-run` executes installed DAG `agent` nodes via Node/Worker; E2E Fix additionally instantiates actual Fixer/Reviewer model nodes, rather than mere SDK interfaces.
- Why this is / is not agent-owned: Operational content and next task step are model-selected, while deterministic DAG infrastructure admits, runs and records their choices.
- Evidence: [README runtime and CLI](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/README.md), [E2E Fix model nodes](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/orchestration/e2e-fix-workflow.ts), [pattern agent nodes](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/orchestration/dag-patterns.ts).
- Basis: Packaged, wired multi-model DAG execution paths.
- Confidence: High architecturally; no paid-model output quality measured.
- Caveats: Requires host services, credentials, allowed tools and an admitted workflow; individual command/approval nodes are not independently agentic S1s.

## S2 — Coordination

- State: C
- Function: Attenuate competition for a shared finite execution budget between independently operating DAG Worker tasks.
- Disturbance / variety regulated: Concurrent agents/runs collectively admitting more expensive work than the same shared budget can support.
- Decisive decision or feedback right: An atomic budget-reservation gate admits or blocks an individual Work request against a namespaced shared usage ledger before execution.
- Decision owner: First-party deterministic `budget_admit` state node enforcing an operator-selected limit; it does not itself own discretionary organizational bargaining, and an operator must instantiate/wire the pattern to a shared ledger.
- Supporting / enforcement mechanisms: Typed `Work.expected_usage`, state namespace/key, budget threshold, mutually exclusive `admit`/`block` outputs and terminal feedback.
- Closure path: Multiple prospective Worker inputs → shared reservation arbitration → admitted tasks execute, rejected tasks terminate as blocked → their run outcomes/status are available for subsequent task choices.
- Boundary reachability: `budget-gate` is a first-party instantiable Manager DAG pattern, not an arbitrary user-coded hook; `hr patterns instantiate`/Manager Agent pattern tooling can sync and run its workflow.
- Why this is / is not agent-owned: It is genuine capacity-conflict attenuation but its budget and deployment scope are externally configured, and no model allocates resources through the gate; `C` is limited to the shipped constructor.
- Distinct S1 units: Independently model-driven Worker tasks/runs sharing the same configured `budget_key` and Manager state namespace.
- Inter-S1 disturbance: Competing declared `expected_usage` claims can oversubscribe one common budget.
- Attenuating coordination relation: Atomic `budget_admit` reservation determines which claims enter resource-consuming S1 execution and which are blocked.
- Feedback into subsequent S1 behaviour: Admitted Work reaches its model Worker; rejected Work does not run and the caller/Manager sees the blocked DAG outcome for future reallocation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The gate compares **competing claims on the same limited resource** and suppresses over-admission before task execution, whereas a plain DAG edge would only sequence tasks.
- Evidence: [budget-gate pattern nodes/edges](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/orchestration/dag-patterns.ts), [pattern instantiation instructions](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/docs/dag-patterns.md).
- Basis: Narrow first-party conflict-specific constructor, not proof of global live inter-agent conflict negotiation.
- Confidence: Medium; resource gate is explicit but multi-run instance wiring is deployment-dependent.
- Caveats: No claim that generic worker concurrency caps or graph sequencing by themselves establish S2, nor that unrelated arbitrary tools share this gate.

## S3 — Inside-and-now control

- State: A
- Function: Inspect current multi-actor DAG execution and choose corrective interventions in the live portfolio.
- Disturbance / variety regulated: Stalled, failed, misassigned or no-longer-desired actors, changed run priorities and aggregate current commitment deviation.
- Decisive decision or feedback right: Start/supervise a DAG and select run/actor `retry`, `reassign`, `interrupt`, `cancel` or checkpoint intervention based on current status and reported milestones.
- Decision owner: Configured host model Manager Agent using first-party run-supervision and intervention tools; Manager service enforces state token, generation and idempotency constraints.
- Supporting / enforcement mechanisms: `get_dag_supervision`, `list_dag_actors`, `intervene_dag_actor`, `send_dag_actor_command`, `cancel_dag_run`; live Manager APIs, durable intervention ledger and actor-state fencing.
- Closure path: Current run/actor snapshots and milestones → Manager Agent judgment → scoped persisted intervention/command → Manager changes affected actor and DAG state → new actor run/status re-enters supervision.
- Boundary reachability: The built-in host-Codex Manager Agent registers concrete tool handlers that call live Manager `/runs/:id/supervision` and `/actors/:id/interventions` routes; the standard README identifies Manager Agent as the end-to-end orchestration entry, not merely a separately authored coding-agent integration.
- Why this is / is not agent-owned: Manager model chooses **which** actor and corrective action given the live view; state machine mechanics only check and enforce that chosen act. Direct CLI/operator intervention is a separate usage route, not evidence needed for autonomous `A`.
- Whole-system current view: Per-run actor roster, supervision snapshots, durable milestone cursors and current run/command status; aggregate across active DAGs is limited by what the Manager Agent queries.
- Current-control decision scope: Actor assignment, cancellation/retry, live instruction delivery, checkpoint fork and run termination, not merely counting token limits.
- Evidence: [Manager Agent DAG tool handlers](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/server/host-codex-manager-agent.ts), [Manager route mutation](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/server/mutations.ts), [change orchestrator](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/orchestration/change-orchestrator.ts), [intervention state](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/persistence/dag-actor-interventions.ts).
- Basis: First-party model-selected current-control tools and durable return to actor execution.
- Confidence: Medium-high for the configured host-Codex Manager mode.
- Caveats: This establishes *supported* discretionary intervention authority, not proof of an always-on autonomous supervisor that monitors all DAGs without user invocation; direct deterministic scheduler/CLI operation alone would not be S3=A.

## S3* — Complementary audit

- State: A
- Function: Independently inspect a repair candidate's code/change and trusted execution evidence before declaring it acceptable.
- Disturbance / variety regulated: A Fixer's incorrect or unsupported success claim, regression in changed code, incomplete evidence and CI inconsistency.
- Decisive decision or feedback right: Three separate Reviewer model sessions judge the same PR head, its diff, frozen design and trusted test evidence; majority approval (at least two of three in fixed-design mode) determines review passage.
- Decision owner: Independently dispatched Reviewer agents, distinct from Fixer and from each other; trusted deterministic aggregator enforces accepted review count and same-head CI/tests.
- Supporting / enforcement mechanisms: Frozen task design/test/CI policy, pinned model dispatches, per-reviewer immutable outputs, separate session IDs, full source/diff evidence, approvals-with-no-findings invariant and feedback to next Fixer round.
- Closure path: Fixer produces candidate → isolated trusted tests and host same-PR publication → distinct Reviewers inspect diff/source/test evidence → persisted votes/findings → trusted quorum/CI gate either accepts or routes failures to fresh Fixer.
- Boundary reachability: The separately prepared `e2e-fix` command and first-party workflow instantiate fixed `review_a`/`review_b`/`review_c` model nodes; stage code verifies distinct sessions and their completion, not just sample prompts.
- Why this is / is not agent-owned: Reviewers exercise independent substantive correctness/scope judgment; the host-owned policy fixes evaluation scope and aggregates their votes without inventing their decisions.
- Claim being audited: Fixer's proposed source changes satisfy the caller-approved fixed design and trusted tests without unreviewed regressions.
- Ordinary reporting path: Producing Fixer session's source changes, resulting test evidence and host-published same-head PR.
- Complementary access path: Reviewers receive candidate diff and source/test artifacts from host-controlled worktree/runner, plus their own independent model reasoning; CI/test evidence comes from trusted execution rather than Fixer's narrative.
- Independence boundary: Three separate Reviewer IDs and model sessions with no advance access to each other's votes; same model provider may be used, so provider-level independence is **not** claimed.
- Who acts on findings: The trusted `review_evidence`/candidate-judgment stages count votes and feed test/review/CI defects into the next Fixer round or final acceptance.
- Evidence: [fixed-design E2E Fix guide](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/docs/e2e-fix.md), [model node prompts/flow](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/orchestration/e2e-fix-workflow.ts), [vote and session gate](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/runtime/e2e-fix-stage.ts).
- Basis: Installed optional audit-specific workflow, not generic logging/scorecards.
- Confidence: High for source-level independent evidence and returned gate, not empirical accuracy of reviewers.
- Caveats: Only the specific prepared/frozen E2E Fix mode earns this state. No S3* guarantee is imputed to arbitrary user DAGs; reviewer sources are bounded by selected candidate and prepared artifacts.

## S4 — Outside-and-then intelligence

- State: C
- Function: Convert recurring failure and standing-goal evidence into bounded proposals for future changes to operating rules, skills or standing objectives.
- Disturbance / variety regulated: Repeated past failures and degrading standing goals that indicate current capabilities/guardrails may need prospective revision.
- Decisive decision or feedback right: The `compost` proposer model selects future improvement proposals; an authenticated owner must approve the exact bounded proposal, but the pattern stops at an approved terminal and **does not apply** the proposed change.
- Decision owner: Shipped composer/proposer models for option development and an authorized human for proposal approval; subsequent capability update needs external composition, so no closed `A`/`P` owner is claimed.
- Supporting / enforcement mechanisms: Evidence collector, bounded `max_proposals`, status gate, proposal hash, restart-safe authenticated approval node, replay summaries and optional standing-goal rechecks.
- Closure path: Failed-run/trust/goal evidence → model analysis and proposed future rules/skill change → durable proposal-specific human approval/rejection → terminal outcome available to a developer-supplied application step; no standard auto-apply-to-future-run edge.
- Boundary reachability: `compost` is a shipped, discoverable and instantiable catalog workflow with specific S4 roles/ports, not a hypothetical generic graph, but users must supply input evidence and wire the post-approval capability application.
- Why this is / is not agent-owned: The model develops prospective changes rather than simply retrying one failed task, yet the critical implementation/return path is left to composition; this supports S4=C only.
- External distinction: Repeated failures, rejected work, trust and standing-goal evidence from earlier operations.
- Future / prospective distinction: Proposed durable rules, skill changes and standing objectives intended for later runs, as opposed to direct repair of one current candidate.
- Adaptation option generated: At most configured `max_proposals` proposals with evidence references and an exact approved hash.
- Path back into current capability / S3: `human_review.approved` is a typed output that a host workflow **could** wire to update Manager rules/skills; the bundled `compost` ends at `applied` terminal without performing such an update. This is the unsatisfied constructor step, not a falsely claimed closed loop.
- Evidence: [compost workflow and gates](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/orchestration/dag-patterns.ts), [replay improvement suggestions](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/server/replay.ts), [DAG pattern catalog](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/docs/dag-patterns.md).
- Basis: First-party future-adaptation-specific constructor, explicitly incomplete at the activation boundary.
- Confidence: Medium; proposed policy/skill change generation is real but actual durable return to operation is not shipped in this template.
- Caveats: A misleading `applied` terminal name is not proof of applying an actual skill/policy change. Standing-goal rechecks alone verify invariants rather than creating new future capabilities; no S4=P is established without an evidenced returned parent decision.

## S5 — Policy and identity

- State: —
- Function: Would resolve contested ultimate purpose, legitimate identity and constitutional rules for the entire HomeRail organization.
- Disturbance / variety regulated: Conflicts about the whole system's enduring mission, ultimate permissible scope and authority to revise its basic rules.
- Decisive decision or feedback right: No source-supported first-party ultimate-identity adjudication that returns a newly authoritative constitution to future Manager/Worker operation.
- Decision owner: Host owner supplies fixed designs, agent permissions, policies and authenticated approval identities; none of these single-workflow choices amounts to a standing S5 owner.
- Supporting / enforcement mechanisms: Frozen E2E Fix design, immutable test/review policy, authorization gates, intervention tokens, selected actor approvals and maintained package configuration.
- Closure path: A task-scope approval can unblock its DAG node, and a frozen policy restricts repair actions; no identity-level dispute → legitimate authoritative decision → constitution change → durable downstream enforcement loop is demonstrated.
- Why this is / is not agent-owned: Runtime fail-closed policies are powerful constraints but their presence does not establish an internal model or legitimate parent *deciding ultimate organizational identity*.
- Evidence: [frozen repair design and authority](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/docs/e2e-fix.md), [compost approval-only branch](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/orchestration/dag-patterns.ts), [Manager Agent tool affordances](https://github.com/xiaotianfotos/homerail/blob/7b734a06c712b454aad17b36ae385f120cfeb7bb/homerail_manager/src/server/host-codex-manager-agent.ts).
- Basis: Bounded absence at packaged self-hosted Manager recursion.
- Confidence: Medium-high for the inspected shipped modes; external owner governance may be separately implemented.
- Caveats: Authenticated policy approval and task/PR acceptance are not categorically S5; a higher owning organization could add its own constitutional loop outside this harness.

### Absence scope

- Surfaces inspected: Manager Agent runtime/tools, DAG mutation/approval and intervention API, policy-frozen E2E Fix workflow, compost/governance pattern, project README, pattern and multi-round documents.
- Plausible first-party paths checked: Enduring system mission/identity dispute, authenticated authority for constitutional change, parent or internal ultimate-policy judgment, persisted new policy and subsequent enforcement on later DAG runs.
- Why no material first-party path remains: Shipped policies are operator-supplied controls and approval nodes are workflow-scoped; the S4-adjacent compost output is a proposal/approval terminal without a first-party constitution update and returned enforcement.

## Distributed OSS parent arrangement

The assessed recursion is a self-hosted Manager instance, not the loose population of unrelated open-source maintainers and installations. Public GitHub contributor decisions and release policy are adjacent project governance; no shared system-wide S3/S4/S5 parent mandate across independent HomeRail deployments is imported from them.

## Self-hosted and non-human modes

Self-hosting supplies a legitimate operator to configure models, tools, budgets, task designs and authenticated approvals. The host-Codex Manager Agent is a supported autonomous S3 decision mode; a pure operator/CLI mode is also possible, but a distinct parent-governed whole-current control loop is not independently classified on the inspected evidence. Installed model workers can differ in provider. The E2E audit's separate-session independence should not be inflated into independence of provider/training or external organizational authority.

## Recursion

Worker agents are separate S1s, optional shared budget admission is a narrow S2 constructor, and the Manager Agent can supervise their current run state as S3. E2E Fix adds a model-owned complementary verification function over one repair lifecycle; it does not imply all workflows have review. Future-improvement pattern and ultimate mission control remain bounded as above.

## Variety and escalation

Typed handoffs and retry mechanisms contain local execution variety; shared reservation can block resource oversubscription, while supervision exposes live interventions with durable tokens and idempotent fencing. Trusted tests and independent reviewers can reject a Fixer's output and return evidence for revision. Repeated failures may be packaged into prospective proposals, but a final capability/policy application must be separately authorized and implemented.

## Evidence gaps

- Static frozen-source review only; no model/provider-backed workflows, conflict load test, external GitHub repair PR or cross-restart injection was executed here. The asserted states are about reachable shipped mechanisms, not success rates.
- S2=C requires instantiation under a common namespace and shared resource scope; this is a narrow budget admission relation, not general semantic conflict mediation.
- S3=A rests on supported Manager Agent tool registration and live mutation handlers, not demonstrated perpetual background whole-portfolio supervision.
- S3*=A is specific to fixed-design E2E Fix and its trusted evidence path; it cannot be generalized to every HomeRail DAG.
- S4=C is intentionally incomplete: `compost` proposes and obtains approval but does not actually apply its purported policy/skill modification in the template. Reassessment after a shipped return-to-operation path could change this state.
