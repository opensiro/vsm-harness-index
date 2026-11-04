---
harness_id: agentic-factory
project_name: Agentic Factory
repository: https://github.com/bussard76/agentic-factory
review_ref: 7059e8bf028584045ce1274672eca7d50d185e9f
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Agentic Factory

## Review boundary

- System in focus: An installed Agentic Factory project organization produced by init/start: Front agent, unattended Controller, workers and complementary audit/retro under the project owner.
- Purpose and identity: Build and integrate owner-agreed software in a repository/demo environment with independent checks, bounded authority and a single human-facing control surface.
- Relevant environment: Owner requirements/acceptance, project source and tests, concurrent worker changes, host capacity/quotas and runtime/tool failures.
- Standard-distribution boundary: Supported Orca-based init/start bundles, rendered project/Controller/Front handbooks, worker spec templates, steering, capacity/gate/wave scripts, audit/retro and protected-policy decision flow.
- Credited operating / distribution surfaces: Rendered Controller loop and live startup; first-party worker specs; multi-worktree integration/rework; status/inbox return; independent Pipeline Auditor/Retro; human-accepted ADR/policy handling.
- Adjacent first-party surfaces excluded from ownership: Factory repository reviews, extraction history, site and development smoke fixtures corroborate the product but are not owners in an installed project. External Orca/model CLIs provide execution; their unrelated governance is not borrowed.
- First-party operating / deployment modes considered: Supported initialized Orca local/remote worker hosts, Front/Controller bundles, GitHub-issue or task-file steering, autonomous bounded decisions and owner-reserved decisions. Experimental plain-terminal runner is not used to close claims.
- Recursion level: One installed factory project; independent task workers are S1 cells, Controller supplies current management, owner is legitimate parent.
- Reviewed revision: 7059e8bf028584045ce1274672eca7d50d185e9f
- Observation date: 2026-11-04
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The Node CLI renders project governance, Controller and Front bundles, role specs and support scripts from owner setup answers. start installs the support skills/bundles and launches the Controller in the supported Orca mode. The Controller acts on worker events, inbox orders and capacity, creates Developer/Tester/Architect/Auditor/Retro sessions, manages rework and integration waves, and records a full status/journal. Separate worker branches/worktrees and gates enforce integration protocols. Nightly/cluster audits inspect alternative evidence and feed bounded improvements or owner decisions. Owner-governed ADR/document changes constrain protected policies. Source-repository development reviews are separate from these deployed modes.

## Operational model

Developers own operational choices; Controller owns cross-worker coordination and current resource/commitment decisions. A distinct parent current-control mode is returned through Front/inbox. Pipeline Auditor/Retro supplies complementary direct-evidence challenge, while hard rules and governing authority remain with the owner. Internal audit/calibration does not establish a separate S4 path at this recursion.

## S1 — Operations

- State: A
- Function: Produce software/task outcomes through model-directed worker execution and repairs.
- Disturbance / variety regulated: Unknown code, failing requirements/tests, implementation ambiguity and incomplete task results.
- Decisive decision or feedback right: Developer chooses implementation/verification actions within the bounded spec; responds to real tool/test/reviewer feedback and returns a committed result or escalation.
- Decision owner: First-party specified Developer worker model in its own task worktree.
- Supporting / enforcement mechanisms: Orca worker-start, model CLI, task spec, branch/worktree, commands/gates, event/reply transport and Controller.
- Closure path: Ready spec → generated developer instructions → start worker → model action/test/commit loop → worker_done or escalation → Tester/rework → reviewed integration.
- Boundary reachability: init renders/copies the handbooks/spec scripts and start launches the Controller; its loop calls mkspec/start for actual workers. No custom organization prompt must be invented beyond supported installation/configuration.
- Why this is / is not agent-owned: The model decides how to implement and repair the assigned outcome; scripts transport/enforce those choices. Using an external CLI does not import that CLI own metasystem.
- Evidence: [bin/agentic-factory.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/bin/agentic-factory.mjs); [controller/CONTROLLER.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/CONTROLLER.md); [controller/start.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/start.mjs); [controller/templates/mkspec.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/templates/mkspec.mjs); [docs/roles.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/docs/roles.md); [docs/workflow.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/docs/workflow.md)
- Basis: explicit and structural supported installed mode
- Confidence: high
- Caveats: Source/configuration closure, not a newly observed production or model-success run.

## S2 — Coordination

- State: A
- Function: Regulate conflicting independently built changes and shared test-capacity interference among workers.
- Disturbance / variety regulated: Separate developers produce branches that conflict or fail when combined; concurrent gates can saturate the host and amplify waits/timeouts.
- Decisive decision or feedback right: Controller chooses which ready/rework/testing tasks may proceed, groups integration waves and routes merge/integration conflict back to the responsible Developer and fresh Tester.
- Decision owner: First-party Controller model, with task Developer making bounded corrective code choices after cross-task feedback.
- Supporting / enforcement mechanisms: Separate worktrees, measured capacity verdict, fair gate slots, serialized integration worktree, wave failure signals and retained review branches.
- Closure path: Independent worker reports/branches → Controller selects wave/order under contention → integration reveals conflict or combined failure → task Developer resolves on its branch → fresh Tester checks → Controller retries a coherent wave. Pressure/gate observations also change later worker launch selection.
- Boundary reachability: Rendered coordinator policy explicitly sends merge conflicts to the task Developer/Tester; Controller loop and start/wave scripts implement the launched-worker/event/combined-state path.
- Why this is / is not agent-owned: The model chooses the concrete coordination/rework response from cross-worker state; worktrees, slots and numerical verdicts only isolate/enforce it. Delegation or sequencing alone is not credited.
- Distinct S1 units: Independently executing Developers and Testers on separate task branches/worktrees sharing an eventual main and finite gate host.
- Inter-S1 disturbance: Incompatible simultaneous changes at integration and contention between heavy test workers.
- Attenuating coordination relation: Controller-managed wave/rework convergence, fresh verification of conflict repairs and capacity-aware launch selection.
- Feedback into subsequent S1 behaviour: Affected Developer receives conflict/failure work and changes its branch; Tester rechecks that repair, and later workers/waves are delayed or selected based on current contention.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: It closes named cross-worker code-combination and host-contention disturbances, not merely a parent task decomposition.
- Evidence: [templates/docs/coordinator.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/templates/docs/coordinator.md); [controller/CONTROLLER.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/CONTROLLER.md); [controller/start.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/start.mjs); [controller/wave.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/wave.mjs); [controller/integ-wave.sh](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/integ-wave.sh); [controller/capacity.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/capacity.mjs); [controller/gate.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/gate.mjs); [docs/workflow.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/docs/workflow.md)
- Basis: explicit and structural
- Confidence: medium-high
- Caveats: No actual concurrent conflict/overload run was reproduced; model compliance and capacity sensor coverage are not guaranteed by the protocol.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate current fleet commitments, priorities, resource use, rework and integration on behalf of the factory project.
- Disturbance / variety regulated: Stalled workers, failed rounds, quota/pressure changes, near-finished work, critical-path blockage and conflicting current demands.
- Decisive decision or feedback right: Autonomous Controller chooses current worker/rework/wave allocation and bounded level-1/2 interventions; owner may change whole-project goals/priorities/resource rules through the supervised mode.
- Decision owner: Base: Controller model inside recorded rules. Parent: legitimate owner via Front/status/inbox; these are distinct bounded control decisions, not simultaneous ownership of one verdict.
- Supporting / enforcement mechanisms: workers.json, event wait/stallwatch, capacity/quotas, start/wave/cleanup, status table, inbox and decision records.
- Closure path: Base reads worker events, capacity and queue, selects priority/rework/escalation/start, observes the next outcomes and revises. Parent sees full project status/needs, returns a priority or resource/commitment decision through Front/inbox, and Controller processes it into subsequent worker operations and records it.
- Boundary reachability: init/start installs and starts the specified Controller with all support scripts; Front is installed to the owner host and explicitly relays answers/orders. Both loops are first-party supported handbooks, not arbitrary user callbacks.
- Why this is / is not agent-owned: The Controller owns discretionary task selection and intervention; fixed meters, caps and scripts do not own those choices. Parent reserved/current directives are reconstructed separately rather than inferred from ordinary Tester approval.
- Whole-system current view: Controller worker table, queue/handover, completed/passed/blocked tasks, current gate/capacity/quota readings, status and owner inbox.
- Current-control decision scope: Critical-path prioritization, allocation among rework/Testers/waves/new work, bounded task decisions, stalls/cleanup and owner-returned current priorities/resource rules.
- Evidence: [controller/CONTROLLER.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/CONTROLLER.md); [front-agent/FRONT_AGENT.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/front-agent/FRONT_AGENT.md); [docs/roles.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/docs/roles.md); [controller/start.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/start.mjs); [controller/wait.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/wait.mjs); [controller/stallwatch.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/stallwatch.mjs); [controller/capacity.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/capacity.mjs); [templates/docs/coordinator.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/templates/docs/coordinator.md)
- Basis: explicit and structural multi-mode closure
- Confidence: high
- Caveats: Deterministic capacity calibration is enforcement/current regulation, not autonomous model ownership by itself. Owner-reserved level-3/policy matters remain outside Controller discretion.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Controller model within recorded level-1/2 scope | Worker event, failure/stall or available capacity | Chooses priority/rework/start/wave, then observes outcomes in later cycles | `controller/CONTROLLER.md`, `start.mjs`, `wait.mjs` |
| Parent (`P`) | Legitimate project owner | Whole-project status, needs or new current orders | Front records owner choice in inbox; Controller consumes/records it and changes subsequent worker work | `front-agent/FRONT_AGENT.md`, `docs/roles.md`, `controller/CONTROLLER.md` |

## S3* — Complementary audit

- State: A
- Function: Complementarily challenge the factory control/reporting picture through independent pipeline evidence and session inspection.
- Disturbance / variety regulated: Routine worker/status reports can hide failure clusters, ineffective process changes, wasted capacity and growing risk.
- Decisive decision or feedback right: A separately instantiated read-only Auditor/Retro evaluates raw journal/load/session evidence, judges causes/risks and prior-improvement metrics, and returns corrective findings.
- Decision owner: Model-backed Pipeline Auditor/Retro for the audit judgment; Controller/owner decides the permitted corrective response.
- Supporting / enforcement mechanisms: Nightly/cluster triggers, audit/retro spec generator, separate worker session, journal/load/session sources, audit artifacts and next-audit metric comparison.
- Closure path: Nightly or failure-cluster trigger → separate auditor reads journal/load/reviews/previous audits, or Retro reads raw worker sessions → measured findings/proposals enter status/handover → Controller runs permitted improvement tasks or escalates to owner → later audit checks the metric and ineffective changes are reverted.
- Boundary reachability: Controller handbook mandates audit/retro launches; mkspec emits the role-specific evidence/questions/output contract and start launches the actual worker. init renders these scripts with real paths. This does not rely on developer-only factory-repository reviews.
- Why this is / is not agent-owned: Parsing/logging alone does not judge the claim. The separate model makes evidence-grounded audit judgments, and findings have a prescribed corrective return. Routine per-task Tester QA is not used as the sole S3* witness.
- Claim being audited: Factory process/status explanations and claims that recent improvements improved operation, rather than merely whether a task test passes.
- Ordinary reporting path: worker_done, task reports, Controller status and routine review verdicts.
- Complementary access path: Independent recomputation over event journal, host load log, reports/reviews/debt and raw worker session moments, compared with prior audit success metrics.
- Independence boundary: Separate read-only audit/retro worker cannot fix the code it judges; it has evidence beyond ordinary summarized status. Controller selects triggers and receives findings, so this is complementary operational audit, not institutional independence from all management.
- Who acts on findings: Controller owns bounded level-1 corrective tasks and rollback; owner decides changes to costs/capacity/process policy.
- Evidence: [docs/improvement.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/docs/improvement.md); [controller/CONTROLLER.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/CONTROLLER.md); [controller/templates/mkspec.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/templates/mkspec.mjs); [controller/start.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/start.mjs); [controller/journal.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/journal.mjs); [controller/loadlog.sh](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/loadlog.sh); [docs/roles.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/docs/roles.md)
- Basis: explicit and structural
- Confidence: medium-high
- Caveats: Read-only is a role/protocol separation and runtime-dependent control, not a proven universal security boundary. No real audit or causal improvement result was executed here.

## S4 — Outside-and-then intelligence

- State: —
- Function: No material first-party outside-and-then intelligence path at the declared supported boundary.
- Disturbance / variety regulated: Internal throughput/failure learning, fixed-tier model calibration and user-directed feature design can change current work.
- Decisive decision or feedback right: No qualifying function-level decision/feedback right reconstructed after checking supported positive and eligible parent modes.
- Decision owner: No qualifying owner at this function; narrower operational or configuration choices remain as described.
- Supporting / enforcement mechanisms: Nightly internal audit, retros, fast-lane repairs, measured tier/host calibration, outside-in feature design and generic architecture/research skills.
- Closure path: No function-specific returned closure is supplied by the checked paths.
- Why this is / is not agent-owned: Audit/retro/calibration use current internal failures, load and preconfigured model tiers; they do not establish externally/prospectively grounded factory capability options and an S3 conversation. Outside-in requirements/architecture decisions produce the software the factory is organized to build (S1 at this recursion), not a supplied strategic adaptation loop for the factory organization. Parent process decisions and generic research tools do not add a distinct S4 mode without that witness.
- Evidence: [docs/improvement.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/docs/improvement.md); [controller/calibrate-models.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/calibrate-models.mjs); [controller/capacity.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/capacity.mjs); [front-agent/FRONT_AGENT.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/front-agent/FRONT_AGENT.md); [docs/outside-in.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/docs/outside-in.md); [templates/docs/coordinator.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/templates/docs/coordinator.md)
- Basis: structural bounded absence
- Confidence: medium-high
- Caveats: A custom external organization could add the function; hypothetical extensions are outside this assessment.

### Absence scope

- Surfaces inspected: docs/improvement.md, controller/calibrate-models.mjs, controller/capacity.mjs, front-agent/FRONT_AGENT.md, docs/outside-in.md, templates/docs/coordinator.md
- Plausible first-party paths checked: Nightly internal audit, retros, fast-lane repairs, measured tier/host calibration, outside-in feature design and generic architecture/research skills.
- Why no material first-party path remains: Audit/retro/calibration use current internal failures, load and preconfigured model tiers; they do not establish externally/prospectively grounded factory capability options and an S3 conversation. Outside-in requirements/architecture decisions produce the software the factory is organized to build (S1 at this recursion), not a supplied strategic adaptation loop for the factory organization. Parent process decisions and generic research tools do not add a distinct S4 mode without that witness.

## S5 — Policy and identity

- State: P
- Function: Maintain the factory purpose, hard risk/data boundaries and ultimate rule/authority envelope under its legitimate owner.
- Disturbance / variety regulated: Proposed changes to governing instructions, protected guardrails, role authority or permitted real-world effects exceed bounded worker/Controller rights.
- Decisive decision or feedback right: Owner accepts/rejects a governing-policy/authority proposal and authorizes the returned durable rule version.
- Decision owner: Project owner; Front asks/relays and Controller records/applies within that mandate.
- Supporting / enforcement mechanisms: Needs-owner questions, status/inbox return, options/recommendation ADR, accepted/Decided-by provenance, protected-file commit checks, authoritative project docs and subsequent worker spec generation.
- Closure path: Policy/authority matter is reserved and raised with options → Front obtains legitimate owner choice → answer returns through inbox → accepted owner-attributed ADR and governing docs record the choice → protected change references it → Controller/worker handbooks and later specs operate under the changed rule.
- Boundary reachability: The rendered handbooks explicitly reserve human rules and authority; first-party Front/Controller return and decision-record paths ship with protected-file checks. This is more than a static AGENTS file or a task permission prompt.
- Why this is / is not agent-owned: Controller may repair internal templates but cannot decide the owner risk/policy envelope. The parent owns the verdict; a local hook checks documentation shape and supports its effect rather than supplying legitimacy itself.
- Identity / ultimate-policy issue: Factory no-outward-effects/real-data boundary, protected governing instructions and who may alter its hard rules or authority; ordinary level-3 design tasks are not automatically treated as S5.
- Ultimate authority in each claimed mode: Legitimate human project owner for governing-policy decisions; no autonomous ultimate-policy mode established.
- Return-to-operation path: Owner decision is relayed, recorded in accepted ADR/coordinator/workflow documents and applied to following Controller/worker operations; protected-file hooks require that recorded decision for governing changes.
- Evidence: [templates/AGENTS.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/templates/AGENTS.md); [controller/CONTROLLER.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/controller/CONTROLLER.md); [front-agent/FRONT_AGENT.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/front-agent/FRONT_AGENT.md); [docs/decisions.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/docs/decisions.md); [templates/tools/factory-guardrails.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/templates/tools/factory-guardrails.mjs); [templates/docs/adr/0001-adopt-agentic-factory.md](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/templates/docs/adr/0001-adopt-agentic-factory.md); [bin/agentic-factory.mjs](https://github.com/bussard76/agentic-factory/blob/7059e8bf028584045ce1274672eca7d50d185e9f/bin/agentic-factory.mjs)
- Basis: explicit and structural parent-governed policy closure
- Confidence: medium-high
- Caveats: Local hooks are cooperative controls, and a Decided-by line is not cryptographic proof of legitimate consent. The assessment credits the explicit supported owner-governed protocol, not tamper-proof enforcement or every architecture approval as S5.

## Distributed OSS parent arrangement

The legitimate parent here is the owner of one installed factory project. Factory upstream maintainers, model vendors and unrelated private contexts do not donate parent authority. Front/Controller handbooks make returned owner decisions visible at the chosen project recursion.

## Self-hosted and non-human modes

Supported Orca installations can place Controller/workers locally or on remote hosts. Model/runtime adapters and orchestration skills execute the first-party actor protocols. Experimental plain-terminal runner is excluded as a closure witness. The unattended Controller retains bounded S2/S3 discretion while policy and separately returned current orders remain parent-governed.

## Recursion

Independent worker worktrees represent S1 task cells. Technical child processes, role names and the Controller hierarchy do not prove each worker contains a viable metasystem of its own. The software being built is a work product/environment at this factory recursion, not automatically its strategic S4.

## Variety and escalation

Tool/test/review feedback returns to task rework; capacity and combined-state outcomes change subsequent scheduling and integration. Bounded level-1/2 decisions stay with workers/Controller. Owner-reserved policy, costs and major decisions reach the Front/status/inbox path; after return they constrain later work. Audits challenge routine reporting and have a separate corrective feedback cycle.

## Evidence gaps

This is pinned-source analysis. Native offline `npm test` on Node 24.22.1 ran 30 smoke tests: 26 passed, 4 failed. The failed cases were fresh-clone initialization/unreviewed-push setup (the temporary bare remote had no checked-out HEAD), Husky-v9 doctor, empty-repository reinitialization/stale-remote detection, and keep-own-hooks doctor. The two doctor cases reported the required Orca CLI missing; other failures remain test/setup limitations without a complete root-cause determination. No upstream source was changed to force a pass. These results limit installation assurance and are not reported as full native validation. No model, Orca fleet, remote deployment or empirical long-running audit was executed. Local hook/read-only controls have the source's own limitations. Internal process adaptation is not evidence of externally/prospectively oriented S4, and structural audit availability does not prove beneficial outcomes or institutional independence.
