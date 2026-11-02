---
harness_id: zenith
project_name: Zenith
repository: https://github.com/Intelligent-Internet/zenith
review_ref: a8d9b5786f81e70e73cce7bb164f5f83da84a4b5
reviewed_at: 2026-11-02
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Zenith

## Review boundary

- System in focus: the shipped Zenith MCP/ACP coding-mission harness with a model orchestrator, worker/validator ACP agents, stateful runtime and fresh-context terminal reviewer.
- Purpose and identity: turn a coding request into a mission charter, falsifiable contracts and task DAG, dispatch implementation and independent validation, repair gaps and close only after review.
- Relevant environment: target code workspace, original request, test/command outcomes, provider sessions, structured handoffs, dependency gates, changing work evidence and final product gaps.
- Standard-distribution boundary: zenith init installs provider-specific orchestrator instructions and MCP configuration, a user starts Claude Code or Codex, and Zenith dispatches ACP worker, validator and reviewer subprocesses. Provider services, agent CLI binaries, target project and user remain outside the first-party software boundary.
- Credited paths: zenith/src/zenith_harness/cli.py, server.py, controller.py, coordinator.py, acp_runner.py, storage.py, config.py, models.py and bundled role prompts.
- Adjacent paths excluded: repository development and maintainer governance, specification proposals, mock test dispatcher and no-op fallback, independent user organization and external provider policy.
- Credited operating / distribution surfaces: installed MCP orchestrator and explicit ACP node/terminal-reviewer adapters used by the normal CLI setup.
- Adjacent first-party surfaces excluded from ownership: mock dispatcher/reviewer, no-op emergency fallback, development tests/specs and GitHub repository maintainers.
- Modes considered: Claude/Codex orchestrator with ACP provider workers; serial/parallel task DAG, validator gates, persisted resume and terminal review; no positive inference from unconfigured model adapters.
- Recursion: one mission supervising distinct S1 coding/validation cells; S3 mission oversight and separate S3* final review.
- Frozen source: a8d9b5786f81e70e73cce7bb164f5f83da84a4b5; observed 2026-11-02; Profile 0.2.4; Methodology 0.3.7.

## Repository architecture

The model orchestrator uses seven MCP tools to create a project, submit a mission plan, advance work, inspect whole state, decide attention, request closure or abort. A persisted task DAG schedules eligible work and validate tasks through ACPNodeDispatcher. Validators produce independent assertion verdicts; deterministic gate evaluation rejects missing or dissenting coverage. Failing work, validation and gates create an attention envelope. The orchestrator chooses task patch, retry, continue, abort or next-mission actions; the controller validates and applies those choices. Closure calls a separate ACP terminal reviewer, given the original request and workspace but instructed not to trust/read mission artifacts, whose negative report returns as attention; only a clean report seals done.

Primary sources: [README](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/README.md), [orchestrator prompt](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/bundled/prompts/orchestrator/system_prompt.md), [controller](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/controller.py), [coordinator](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/coordinator.py), [ACP runner](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/acp_runner.py).

## Operational model

Worker models choose substantive coding/tool actions and report results; validator models judge assertion evidence independently. The orchestrator model selects mission topology and answers whole-mission attention. Deterministic scheduling, validation and persistence enforce those choices but do not own their discretionary content. A separate terminal reviewer models product-level gaps independently of internal mission success claims.

## S1 — Operations

- State: A
- Function: implement and test assigned contracted coding tasks in the workspace.
- Disturbance / variety regulated: unfamiliar source structure, failed code/tests, tool errors and new implementation evidence.
- Decisive decision or feedback right: worker ACP model selects edits/tests, interprets outcomes, revises actions and submits a structured end_node handoff.
- Decision owner: configured worker model, not deterministic dispatcher.
- Supporting / enforcement mechanisms: role prompt, ACPNodeRunner.run_node, worker MCP server, task state and handoff persistence.
- Closure path: assigned contract/task → model workspace actions → tool feedback → end_node → persisted handoff → subsequent work/attention.
- Boundary reachability: standard zenith init MCP configuration and production server.main ACPNodeDispatcher wiring.
- Why this is / is not agent-owned: without an ACP worker agent, scheduler and tools cannot choose code changes; development mocks are not credited.
- Evidence: [runner](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/acp_runner.py), [server](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/server.py), [worker prompt](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/bundled/prompts/worker/system_prompt.md).
- Basis: explicit + structural.
- Confidence: high for source wiring; live provider execution unverified.
- Caveats: ACP provider binaries/credentials are external and missing handoffs are failed, not successful.

## S2 — Coordination

- State: —
- Function: no material first-party peer-interference attenuation loop distinguishable from scheduling and S3 mission management established.
- Disturbance / variety regulated: dependency and shared-workspace conflicts are possible, but no concrete interaction-driven peer conflict witness with coordinated feedback found.
- Decisive decision or feedback right: no S2-specific inter-S1 coordination discretion established.
- Decision owner: none established; mission task graph choices belong to orchestrator S3.
- Supporting / enforcement mechanisms: depends_on, max_parallel_nodes, batch dispatch, gate scheduling and same-project MCP mutation lock.
- Closure path: no S2-specific measured peer interference → adjustment of affected S1 units.
- Boundary reachability: no positive S2 mode claimed.
- Why this is / is not agent-owned: a DAG and scheduler alone do not prove regulation of concrete peer collision or oscillation.
- Evidence: [coordinator](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/coordinator.py), [server](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/server.py).
- Basis: bounded structural absence.
- Confidence: medium-high.
- Caveats: a prompted orchestrator may avoid anticipated collisions, but that is not an evidenced separate shipped S2 feedback relation.

### Absence scope

- Surfaces inspected: DAG task dependencies, serial/parallel dispatch, workspace paths, task state, gates, attention and model decisions.
- Plausible first-party paths checked: worktree isolation, peer conflicts/merge mediation, inter-agent interference detection, peer adjustment and resource collision resolution.
- Why no material first-party path remains: shipped mechanisms plan and dispatch work and test outputs, with no explicit S2-specific disturbance-to-peer-adjustment closure.

## S3 — Inside-and-now control

- State: A
- Function: supervise whole-mission current commitments across work, independent validation, gates, repair and closure readiness.
- Disturbance / variety regulated: failed tasks, insufficient validation, blockers, evidence changes, missed requirements and competing commitments.
- Decisive decision or feedback right: model orchestrator authors contract/task topology, inspects the entire mission envelope and chooses patch/retry/continue/abort/next-mission responses to outstanding attention.
- Decision owner: configured orchestrator model; controller enforces decision schema and persists outcome.
- Supporting / enforcement mechanisms: inspect_project, submit_plan, advance_project, decide_attention, attention queue and DAG/gate constraints.
- Closure path: mission envelope → model decision → controller applies and dispatches → worker/validator outcomes → updated envelope and further decisions.
- Boundary reachability: provider-specific orchestrator prompt and installed MCP server are the documented standard flow.
- Why this is / is not agent-owned: removing the orchestrator leaves a deterministic engine waiting for the mission's plan and discretionary attention resolution.
- Evidence: [orchestrator prompt](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/bundled/prompts/orchestrator/system_prompt.md), [controller](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/controller.py), [envelope](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/envelope.py).
- Basis: explicit + structural.
- Confidence: high for decision ownership and source closure.
- Caveats: user confirmation of a mission brief is an ordinary scope input, not a distinct parent-governed whole-current-control mode.
- Whole-system current view: inspect_project/attention envelope includes current mission state, contract coverage, task graph and open blockers across all active nodes.
- Current-control decision scope: task ownership and dependencies, repair/retry/continuation, accepted risk handling, cancellation and validation gates for the whole mission.

## S3* — Complementary audit

- State: A
- Function: independently challenge proposed mission completion against original user-facing product requirements.
- Disturbance / variety regulated: false green task/validator evidence, hidden gaps and unimplemented user-scope promises.
- Decisive decision or feedback right: fresh-context terminal ACP reviewer inspects product workspace and returns its own done or gap verdict.
- Decision owner: separate terminal-reviewer model session, whose prompt excludes mission artifacts and prior team claims.
- Supporting / enforcement mechanisms: ACPTerminalReviewer, dedicated MCP submit_terminal_review, saved report, fail-closed reviewer crash and coordinator closure gate.
- Closure path: end_mission → independent workspace review → negative report raises orchestrator attention/repair or clean verdict seals done.
- Boundary reachability: production server constructs ACPTerminalReviewer, and coordinator calls it during mandatory terminal review.
- Why this is / is not agent-owned: a distinct model makes substantive gap judgment; coordinator only enforces and routes the report.
- Evidence: [reviewer prompt](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/bundled/prompts/terminal-reviewer/system_prompt.md), [runner](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/acp_runner.py), [coordinator](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/coordinator.py).
- Basis: explicit + structural.
- Confidence: high for installed independent feedback loop, no empirical reviewer accuracy claim.
- Caveats: provider may be same brand but session and evidence boundary are separate; a reviewer crash fails mission closure.
- Claim being audited: model supervisor's assertion that user-requested product behavior is ready for mission closure.
- Ordinary reporting path: worker end_node outputs, validator handoffs, gate results and mission artifacts reported into the controller.
- Complementary access path: independent ACP reviewer gets original user request and current product workspace, can inspect source/tests and run checks.
- Independence boundary: fresh model session explicitly forbidden to consume contracts, worker reports, runtime/mission state or prior validator conclusions.
- Who acts on findings: coordinator blocks closure and opens terminal_review attention; orchestrator model repairs/replans and requests a new review.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct externally grounded prospective adaptation cycle established.
- Disturbance / variety regulated: in-mission discoveries are handled via S3 replan; external future shifts are not continuously sensed.
- Decisive decision or feedback right: no demonstrated horizon-sensing → future-option authority.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: persisted mission memory, skills, adaptive prompts and next-mission lifecycle.
- Closure path: no first-party external future distinction → capability option → returned operation path.
- Boundary reachability: no positive S4 mode claimed.
- Why this is / is not agent-owned: changes to task contracts and guidance from immediate implementation evidence are present-mission corrections, not an outside-and-then loop.
- Evidence: [prompt](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/bundled/prompts/orchestrator/system_prompt.md), [storage](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/storage.py).
- Basis: bounded structural absence.
- Confidence: medium-high.
- Caveats: an operator may assign strategic research as a task, which does not install standing S4 feedback.

### Absence scope

- Surfaces inspected: mission lifecycle, plan/replan, memory and skills, terminal closure and configured provider roles.
- Plausible first-party paths checked: external environmental change signals, future options, comparative adaptation choices, durable capability changes returned to S3.
- Why no material first-party path remains: documented adaptation concerns current mission failures and scope, without demonstrated future-external intelligence cycle.

## S5 — Policy and identity

- State: —
- Function: no separate ultimate identity/organizational-policy decision loop established within a running mission.
- Disturbance / variety regulated: user scope/risk confirmation regulates task contract, not demonstrated ultimate-policy conflict.
- Decisive decision or feedback right: none for identity-level policy at the assessed recursion.
- Decision owner: none established; user/operator and model hold ordinary mission rights.
- Supporting / enforcement mechanisms: mission.md scope charter, user approval guidance, task contracts, abort tools and runtime limits.
- Closure path: no identity-level proposal → legitimate ultimate authority → revised policy return.
- Boundary reachability: no positive S5 mode claimed.
- Why this is / is not agent-owned: ordinary user approval, task scope and stop choices do not establish an S5 parent mode or internal ultimate-policy identity.
- Evidence: [prompt](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/bundled/prompts/orchestrator/system_prompt.md), [controller](https://github.com/Intelligent-Internet/zenith/blob/a8d9b5786f81e70e73cce7bb164f5f83da84a4b5/zenith/src/zenith_harness/controller.py).
- Basis: bounded structural absence.
- Confidence: medium-high.
- Caveats: a user may change instructions or cancel; those are not evidenced legitimate S5 cycles.

### Absence scope

- Surfaces inspected: scope-confirmation method, risk/stop decisions, controller state changes and provider configuration.
- Plausible first-party paths checked: identity-level proposal, ultimate authority, policy adjudication and enforceable return to operating agents.
- Why no material first-party path remains: shipped rights govern specific mission delivery and permission, not a distinct identity-policy loop.

## Distributed OSS parent arrangement

Repository maintainers can release changes, but their development governance is adjacent to the deployed mission. No distributed OSS S3/S4/S5 parent loop is inferred from GitHub contributors alone.

## Self-hosted and non-human modes

Zenith runs locally against selectable ACP models. Human scope consultation and provider configuration do not form a distinct operationally closed parent S3/S5 mode; the demonstrated S3 right belongs to the orchestrator model.

## Recursion

One mission contains model-driven S1 task cells, an S3 model orchestrator and a distinct S3* model reviewer. Generic tool use within an ACP worker does not by itself establish another nested viable organization.

## Variety and escalation

Worker failures, negative validation and gate dissent raise persisted attention to the model S3. Negative terminal product audit reopens the repair loop; missing reviewer verdict prevents done. The source does not establish S2-specific conflict attenuation or higher S4/S5 closures.

## Evidence gaps

Frozen-ref source assessment, not a credentialed Claude/Codex end-to-end mission run. Source and tests substantiate first-party entry, role dispatch and review return paths without proving provider quality. The no-op fallback/mock dispatcher is not counted as autonomous operation.
