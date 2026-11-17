---
harness_id: conductor-agents-security-harness
project_name: Conductor Agents — Security Harness
repository: https://github.com/conductor-oss/conductor-agents
review_ref: f03f18a0e399d3613600ecb56b82afff66e417d6
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Conductor Agents — Security Harness

## Review boundary

- System in focus: The first-party runnable `security-harness/` security-assessment agent in `conductor-oss/conductor-agents`, not the Conductor platform or maintainer organization as a whole.
- Purpose and identity: Authorized, evidence-backed application/API security assessment through tool-using investigative agents, verification, and a bounded report.
- Relevant environment: Target application, deployment identity, authorized testing scope, source/docs when supplied, external security reference feeds and execution infrastructure.
- Standard-distribution boundary: Shipped source entry points `./scan`, `./assess`, `./swarm`, and optional authorized SAST/scanning modes, requiring an operator-provided Conductor server, model provider and workers. No network security testing was performed for this review.
- Credited operating / distribution surfaces: `security-harness/` entry scripts, Conductor workflow definitions, prompts, first-party Python workers, authorization/verification/blackboard/allocator implementation, and persistent campaign state in supported deployment modes.
- Adjacent first-party surfaces excluded from ownership: `coding-harness/` (different agent), `security-harness/bench/` and example vulnerable app (development/evaluation), roadmap/implementation plans, repository contributor/CI/release governance, and external Conductor orchestration service treated as execution infrastructure rather than an in-boundary policy owner.
- First-party operating / deployment modes considered: Authorized surface scan, multi-pass `deep_assess`, source-only SAST where enabled, and the optional documented round-based `swarm_assess` with separate specialist subworkflows.
- Recursion level: One authorized campaign as the whole; independent investigative/scout/exploit/chainer/refuter subworkflows as S1 units in swarm mode. Individual tool calls and the external workflow server are not assumed separate viable systems.
- Reviewed revision: `f03f18a0e399d3613600ecb56b82afff66e417d6`.
- Observation date: 2026-11-17; pinned source/doc/workflow review, without provider-backed integration execution.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The repository packages a security-oriented agent as a runnable Conductor application, combining JSON workflows with `LLM_CHAT_COMPLETE` reasoning tasks and Python tool workers. The CLI authorizes and submits workflows; models formulate hypotheses, determine investigative actions, evaluate observations, and produce findings, while Conductor provides durable task scheduling and fan-out. `deep_assess` iterates understand/hypothesize/exploit/verify/reflect rather than merely replaying a static scan checklist. Swarm mode runs specialist subworkflows with campaign correlation, a shared append-only blackboard, standup assignment, feedback-driven credits, reconciliation, and a skeptical refuter. Persistent memory stores verified/rejected evidence across runs. A user-owned authorization manifest bounds targets, time, permissible operations and capability; deterministic scope/safety enforcement may halt the campaign but must not be confused with agent authority. Separate benchmarks and the `bench/hc_writeback.py` optimizer are developer evaluation machinery rather than an automatically installed run-time adaptation authority.

Primary architecture: [README](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/README.md), [shipped workflow description](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/docs/architecture.md), [conformance boundary](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/CONFORMANCE.md), [swarm runtime](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/workers/swarm/tasks.py).

## Operational model

The accepted result is a reproducible security assessment with bounded experimental actions, verified findings, provenance, and residual uncertainty. In ordinary deep mode the investigative LLM chooses the next hypothesis and subsequent evidentiary work. In swarm mode, distinct specialists pursue delegated investigative hypotheses concurrently; agents supply their observations while deterministic standup and reconciliation arbitrate a shared width limit and next-wave task mix. The audit/verifier model inspects separate replay/oracle results before evidence enters report decisions. Human authority sets authorization and operating limits outside the agent; it is not automatically S3/S5 ownership. These runtime modes do not imply that repository maintainer policy is part of a campaign's VSM recursion.

## S1 — Operations

- State: A
- Function: Authorized investigative work against the scoped application, with reasoning-and-action iterations that produce a security finding or a ruled-out hypothesis.
- Disturbance / variety regulated: Unexpected app behavior, uncertain attack hypotheses, varying API/source evidence and observed failure/success of a permitted investigation.
- Decisive decision or feedback right: The investigator model chooses candidate hypotheses/actions and revises its subsequent experiments from actual tool results and verifier feedback.
- Decision owner: First-party LLM investigator in the supported `deep_assess` path; distinct specialist LLMs in the supported swarm mode.
- Supporting / enforcement mechanisms: Conductor scheduling, typed task definitions, Docker workers, scoped HTTP/browser/code tools, authorization checks, state persistence.
- Closure path: Investigative hypotheses → authorized tool result → verification/reflect feedback → next experiment or report outcome.
- Boundary reachability: `deep_assess` and `swarm_assess` are registered first-party workflow entry modes, not merely benchmark scenarios.
- Why this is / is not agent-owned: The model makes the substantive investigative choice; the workflow, capability gate and typed tools execute and constrain it without making that discretionary choice.
- Evidence: [deep workflow](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/conductor/workflows/deep_assess.json); [swarm workflow](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/conductor/workflows/swarm_assess.json); [architecture](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/docs/architecture.md); [entry and supported modes](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/README.md).
- Basis: structural.
- Confidence: high for the source-defined supported loop; runtime execution was not reproduced.
- Caveats: Requires provider/server configuration and explicit authorization; the source-only SAST shortcut should not be generalized to the entire campaign.

## S2 — Coordination

- State: C
- Function: Resolve concrete competition between independently executing investigative S1 units for a finite next-wave width while preventing exploration or refutation from starving one another.
- Disturbance / variety regulated: Breadth vs depth, refuter vs exploiter demand, repeated overlapping hypotheses and shared concurrency/budget ceilings among separate swarm agents.
- Distinct S1 units: Scout, exploiter, chainer and refuter subworkflow agents in one campaign.
- Inter-S1 disturbance: Unbounded simultaneous demand on the same wave capacity and repeated attempts on the same hypothesis; a rich hypothesis backlog can crowd out untested areas or peer review.
- Attenuating coordination relation: `allocator.plan_wave` reserves a scout floor and caps refuter occupancy, allocates remaining slots to hypotheses, and deduplicates confirmed/tried signatures; a single-writer reconcile folds wave facts back into a new shared allocation.
- Feedback into subsequent S1 behaviour: Updated per-area credits, coverage, attempted signatures and new hypotheses are read by the following `swarm_standup` and translated into changed roles and task inputs.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The cited capacity conflict and feedback-controlled allocation of scarce shared wave slots are explicit; the blackboard alone does not carry the positive finding.
- Decisive decision or feedback right: Determine which S1 claims compete for and receive the next limited wave's slots.
- Decision owner: A deterministic first-party allocator chooses the normal wave mix; autonomous agents contribute evidence and task proposals but do not directly own the resulting S2 allocation.
- Supporting / enforcement mechanisms: Blackboard append-only facts, Conductor dynamic fan-out, identity/correlation, width/budget cap.
- Closure path: S1 observations/attempts → reconcile credit and remaining-work counts → next standup's constrained role allocation → changed subsequent subworkflow work.
- Boundary reachability: The `swarm_assess` / `swarm_round` installed workflows invoke `swarm_standup` and `swarm_reconcile`; this is specific to the supported optional swarm mode.
- Why this is / is not agent-owned: The decision is fixed by source-defined heuristics, not by the specialist LLMs; construction of a discretionary autonomous coordination owner would still be required. The first-party S2-specific allocator and feedback path justify `C`, not `A`.
- Evidence: [allocator](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/workers/common/allocator.py); [swarm worker](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/workers/swarm/tasks.py); [blackboard](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/workers/common/blackboard.py); [swarm round workflow](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/conductor/workflows/swarm_round.json).
- Basis: structural.
- Confidence: medium; the function-specific allocator is traced, but an actual independently agent-owned coordinating mode is not.
- Caveats: This is a constructor result for a specialized prewired mode, not a general claim that any shared board supplies S2.

## S3 — Inside-and-now control

- State: C
- Function: Maintain a campaign-level current operating view and make bounded allocation/intervention decisions for the next wave.
- Disturbance / variety regulated: A growing campaign-wide backlog, diminishing investigative yield, finite current execution capacity, unresolved verification and capped request/time budgets.
- Whole-system current view: `blackboard.assemble_state` and `campaign_rollup` expose open hypotheses, review candidates, coverage, attempts, findings and spend; `swarm_standup` combines these with the current wave ceiling and budget.
- Current-control decision scope: Current shared width and role slots, task priorities, continuation vs termination, and the enforced authorization envelope.
- Decisive decision or feedback right: Select next wave allocation and whether current campaign work remains worth another pass within hard limits.
- Decision owner: Deterministic `allocator.plan_wave` and `should_continue` in the shipped swarm; operator-authored authorization/limits constrain those rules. The current whole-system supervisory discretion is not demonstrably autonomous-agent-owned.
- Supporting / enforcement mechanisms: Workflow loop, shared board, central reconciliation, `safety_check`, manifests, limits and kill switch. Enforcement alone is not S3 decision ownership.
- Closure path: Current campaign state → standup/continuation decision → next `FORK_JOIN_DYNAMIC` wave or stop.
- Boundary reachability: `swarm_round` and `swarm_assess` invoke the current-state and control path in the documented optional swarm mode; general-purpose task scheduling alone is excluded.
- Why this is / is not agent-owned: The default whole-campaign decision rule is codified rather than chosen/revised by a supervisory agent. The exposed first-party current-state/decision path is specific enough for a composed supervisory constructor, but `A` is not established.
- Evidence: [swarm worker standup/reconcile](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/workers/swarm/tasks.py); [allocator and stop gate](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/workers/common/allocator.py); [blackboard state](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/workers/common/blackboard.py); [workflow](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/conductor/workflows/swarm_round.json); [authorization](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/docs/authorization.md).
- Basis: structural.
- Confidence: medium.
- Caveats: Operator manifest editing and an emergency stop do not establish `S3=P`; no distinct live parent-owned whole-system current-control loop with returned decision is credited.

## S3* — Complementary audit

- State: A
- Function: Challenge claimed findings through a path separate from the original investigator's normal success report.
- Disturbance / variety regulated: False positives, misattributed effects, insufficient cross-identity evidence, stale or unreproducible hypotheses.
- Claim being audited: An investigator's asserted exploitable/security-relevant finding.
- Ordinary reporting path: Specialist or deep-mode investigator returns a candidate finding and its proposed evidence.
- Complementary access path: The `verify_finding` workflow replays the claimed request via an HTTP worker, checks out-of-band receipt and passes those fresh observations to a separate skeptical LLM verifier; swarm adds an adversarial refuter model to challenge candidate assumptions.
- Independence boundary: Different review task/prompt and external observation channel from the producing investigator; the refuter shares an application model and its verdict alone cannot defeat an independently confirmed oracle.
- Who acts on findings: Verify/parsing and the blackboard reconciliation/report path mark candidates as confirmed, rejected or disputed; those distinctions determine subsequent peer review and the accepted dossier.
- Decisive decision or feedback right: The independent skeptical model judges whether replay, differential evidence and OOB checks substantiate the claim, with trusted deterministic oracle receipts retaining precedence.
- Decision owner: First-party distinct LLM verification/refuter tasks for complementary audit judgment; deterministic gate and observation workers only enforce/transport.
- Supporting / enforcement mechanisms: Replay worker, OOB oracle, prompt parser, blackboard's refutation/confirmation state and durable report.
- Closure path: Candidate → fresh replay/OOB observation and skeptical verdict → accepted/rejected/dissent state → campaign report and future review/continuation decisions.
- Boundary reachability: `verify_finding` is an installed workflow of the deep assessment; swarm's `refuter` and `review_candidates` are wired into the next wave.
- Why this is / is not agent-owned: The distinct LLM verifier/refuter makes substantive challenge judgments; deterministic evidence collection and precedence are not falsely counted as the decision owner.
- Evidence: [verification workflow](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/conductor/workflows/verify_finding.json); [refuter workflow](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/conductor/workflows/refuter.json); [refuter prompt](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/prompts/refuter.md); [blackboard precedence](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/workers/common/blackboard.py); [architecture](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/docs/architecture.md).
- Basis: structural.
- Confidence: medium-high for review-path reachability; no live confirmation trace audited in this review.
- Caveats: Model-to-model skepticism alone would be insufficient; the complementary replay/OOB witness is decisive. The bounded audit does not prove two different provider organizations or complete independence from all common inputs.

## S4 — Outside-and-then intelligence

- State: —
- Function: No established first-party operationally closed outside-and-future adaptation of the harness's own capability.
- Disturbance / variety regulated: Changing security threat environment and evaluator/model/tool weaknesses are potential future-capability disturbances but not a demonstrated S4 ownership loop.
- Decisive decision or feedback right: No shipped adaptation authority and return-to-capability path established within the assessed campaign.
- Decision owner: Not established at the campaign boundary.
- Supporting / enforcement mechanisms: Dependency/CVE intelligence feeds, campaign-specific coverage/reflection, persistent per-target memory, `hc_analyze` diagnosis, and separately run benchmark write-back.
- Closure path: No in-boundary externally prospective capability-update closure demonstrated; findings and campaign replanning remain inside the current investigative S1/S3 context.
- Why this is / is not agent-owned: External threat lookup informs a current investigation; a read-only improvement proposal does not itself change subsequent first-party operating capability. The write-back runner is under `bench/`, excluded as developer testing infrastructure.
- Evidence: [conformance](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/CONFORMANCE.md); [hillclimb runtime worker](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/workers/hc/tasks.py); [write-back logic](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/workers/common/hc_writeback.py); [development runner](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/bench/hc_writeback.py); [architecture](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/docs/architecture.md).
- Basis: structural.
- Confidence: medium.
- Caveats: Does not deny that an operator could deploy the optional benchmark runner or that a future release could couple it into a real adaptation mode.

### Absence scope

- Surfaces inspected: Shipped deep/swarm workflows, first-party HC worker, common hillclimb and write-back utilities, development benchmark runner, source conformance and architecture.
- Plausible first-party paths checked: External CVE/EPSS feed → task hypotheses, prior-campaign memory → new target testing, trace diagnoses → candidate config improvements, benchmark promotion → future config edition.
- Why no material first-party path remains: Current threat sensing and reflection govern immediate investigation; the installed HC worker emits read-only proposals, and the executable write-back is an adjacent benchmark operation without an evidenced standard campaign adaptation owner/activation cycle.

## S5 — Policy and identity

- State: —
- Function: No first-party loop that raises identity-level or ultimate-policy tensions to legitimate authority and returns a new authoritative identity decision to subsequent campaign operation.
- Disturbance / variety regulated: Changes in authorization legitimacy and identity/ethical boundaries could require ultimate-policy judgment, but the shipped paths enforce preselected engagement constraints.
- Decisive decision or feedback right: Authorize an engagement, choose scope and capability ceiling; these are pre-run ordinary operating permissions, not a demonstrated first-party identity/ultimate-policy revision loop.
- Decision owner: External operator for the manifest; deterministic enforcement in the harness. No qualifying in-boundary S5 decision owner established.
- Supporting / enforcement mechanisms: Manifest, authorization gate, scope and capability validators, safety governor, immutable audit log.
- Closure path: Manifest → validated run/blocked action is a permission-enforcement path, not policy conflict escalation → legitimate parent judgment → changed ultimate policy → returned operation.
- Why this is / is not agent-owned: The agent cannot self-escalate capability; static authorization and operator configuration are not evidence that it owns ultimate identity/policy decisions. Repository contributor governance is another recursion.
- Evidence: [authorization contract](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/docs/authorization.md); [manifest code](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/workers/common/authz.py); [safety worker](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/workers/safety/tasks.py); [conformance](https://github.com/conductor-oss/conductor-agents/blob/f03f18a0e399d3613600ecb56b82afff66e417d6/security-harness/CONFORMANCE.md).
- Basis: structural.
- Confidence: medium.
- Caveats: This bounded negative does not evaluate the governance of the external Conductor organization or all users' private deployment policies.

### Absence scope

- Surfaces inspected: Supported CLI entry modes, manifest and permission validation, safety worker/halt loop, source conformance, and first-party campaign workflows.
- Plausible first-party paths checked: Operator engagement authorization, capability-level escalation, kill-switch response, prohibited-operation detection, and repository governance.
- Why no material first-party path remains: These paths preselect/enforce permissible actions or terminate current work; none supplies the identity-level question, legitimate parent decision, and returned ultimate-policy change at the campaign recursion. Developer governance/CI is an adjacent recursion.

## Distributed OSS parent arrangement

Conductor Agents maintainers and users can hold ordinary authority over releases, manifests and deployments. The assessment does not borrow this development-level governance to claim S3/S4/S5 parent ownership of a single running campaign. No organizationally shared private runtime was assumed.

## Self-hosted and non-human modes

Self-hosted Conductor deployments require operator-supplied credentials, authorization manifest, model and worker execution. The documented swarm mode uses multiple autonomous S1 investigative units but relies on deterministic S2/S3 resource assignment; it does not automatically acquire parent-mode notation from user-configured limits. External workflow-server availability is an operational prerequisite, not an independent autonomous governance owner.

## Recursion

A campaign is the system in focus. Its investigative specialist subworkflows have distinguishable tasks and observation environments but are not automatically independently viable organizations with complete S2–S5 systems. The Conductor server's scheduling layer and the repository's development organization are adjacent higher/lower boundaries.

## Variety and escalation

Input uncertainty is absorbed in agent hypothesis/testing loops, review uncertainty is reduced by replay/oracle/refuter audit, and finite shared wave capacity is attenuated by standup allocation. Runtime authorization violations are hard-enforced or halted; this does not establish an identity-policy escalation channel. Evaluation/capability self-improvement is separable from campaign execution.

## Evidence gaps

- Provider-backed execution and real multi-wave traces were not produced; only fixed-ref source, wired workflow and documentation paths were inspected.
- Whether the pure allocator's specialized S2 and S3 constructor interfaces warrant `C` rather than a stricter negative under a future independent semantic review is open for reviewer challenge; no `A` is inferred from deterministic allocation.
- The delivered `bench/hc_writeback.py` could be run in a separate operator-managed development process; the absence scope intentionally excludes it from campaign S4 ownership.
- The original source is a security-testing agent; no live scanning or target interactions were performed for this classification.
