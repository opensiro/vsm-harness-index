---
harness_id: clutch
project_name: Clutch
repository: https://github.com/fancy1108/Clutch
review_ref: d4d23af46e871a663886743535956d5c331313db
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Clutch

## Review boundary

- System in focus: the installed local Clutch desktop/workflow supervisor, with configured CLI/LLM participants inside a user-selected workspace and workflow, not the GitHub development project.
- Purpose and identity: let a developer define, execute and supervise local agent-based coding/automation SOPs, inspect results and intervene in running work.
- Relevant environment: local repositories and terminal, configured external Claude/Codex/other CLIs and model APIs, MCP services, workflow checks and risky file/command outcomes.
- Standard-distribution boundary: packaged Tauri/React application, its Python FastAPI/LangGraph sidecar, user-defined workflow compiler, provider/CLI/MCP adapters, worktree UI/API, state store and human approval/stop controls. Model cognition is externally provided.
- Credited operating / distribution surfaces: `services/orchestrator/src/` compiler, `engine_router.py`, `agent_executor.py`, `chat_runner.py`, `routes/worktree.py`, `run_control.py`, state/API/sidecar; `apps/desktop/src/` Chat, Flow, terminal, diffs and intervention controls.
- Adjacent first-party surfaces excluded from ownership: example `workflows/*.json` named Builder/Evaluator, archived specs/proposals, design research/roadmaps, E2E and benchmark fixtures, CI/release, repo maintainers and unverified Windows native runtime behavior.
- First-party operating / deployment modes considered: local desktop chat with built-in Clutch Agent or connected external agent CLI; user-authored LangGraph workflows, custom agent/tool configs, terminal lanes, human interrupts, explicit optional parallel Git worktrees, standalone verification/report cards, model/API routes, packaged macOS and Windows builds.
- Recursion level: one local workspace/workflow operating unit with one or more invoked agents and a single owner/operator supervision console; different installed desktops or developer teams are not presumed coordinated.
- Reviewed revision: `d4d23af46e871a663886743535956d5c331313db`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Clutch packages a Tauri desktop UI with a loopback-only Python FastAPI sidecar. Operators configure models, external coding CLIs, tools and workflows in Settings and a visual canvas. The sidecar compiles workflow JSON into LangGraph nodes; an `agent_task` routes to a configured provider/CLI/MCP invocation, a `check` performs specified deterministic checks and a `human_gate` interrupts until the operator decides. Chat can alternatively run a single model-backed agent tool loop. The desktop displays workflow status, terminal traces, file changes/diffs and a supervision control surface; UI decisions return via sidecar endpoints and events. Users can explicitly create/select isolated worktrees and merge/discard them. `submit_verification` is an agent-triggered report combined with harness tests/file-presence checks, rather than an independent auditor agent. A workflow called Evaluator in the examples is not a fixed production auditor. Source ownership of agents' task-specific model decisions remains with configured external providers.

Primary evidence: [architecture](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/docs/ARCHITECTURE.md), [end-user capabilities](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/docs/PRODUCT_INTRO.md), [engine routing](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/services/orchestrator/src/engine_router.py), [worktree API](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/services/orchestrator/src/routes/worktree.py).

## Operational model

Configured LLM/CLI agents own task-level tool selection and response to execution feedback; Clutch's graph machinery routes and records work without itself deciding solutions. User-defined workflow graph edges/checks determine most sequencing. The operator sees live status and intervenes in current work through stop, resume, approval/reject/retry and workspace controls, yielding a separately reachable parent-operated S3 mode. Manual worktree creation is a concrete isolation mechanism, but no shipped agent-owned policy deciding when peer writers need isolation was established. Routine verification is not independent S3* audit; optional workflow reconfiguration is not evidence of a prospective S4 loop.

## S1 — Operations

- State: A
- Function: perform open-ended coding/automation tasks via configured model/CLI agent sessions and tool access inside a selected local workspace.
- Disturbance / variety regulated: user requirements, changing source files, tool outputs, failing shell/MCP actions and unexpected provider responses.
- Decisive decision or feedback right: choose and revise next task action, tool invocation and produced artifact based on context/result.
- Decision owner: connected model/CLI agent (or built-in provider-backed agent loop), not deterministic LangGraph edges or desktop UI.
- Supporting / enforcement mechanisms: `engine_router`, `agent_executor`, CLI adapters, MCP tools, session/context continuation, human permission gates, workspace path and logs.
- Closure path: an agent instruction reaches a configured provider/CLI, its actions execute against the local workspace, feedback returns to that agent's subsequent turn, and task artifacts/messages are stored.
- Boundary reachability: end-user Settings enable configured agent CLI/provider and the supported direct Chat/`agent_task` workflow modes run them in the distributed sidecar.
- Why this is / is not agent-owned: the task-specific choice is made by the model/CLI; Clutch owns transport/checkpoints and user-defined graph control, not that cognitive choice.
- Evidence: [workflow `agent_task` and operating modes](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/docs/ARCHITECTURE.md#L142-L204), [execution adapter](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/services/orchestrator/src/agent_executor.py#L120-L398), [Chat tools](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/docs/PRODUCT_INTRO.md#L200-L214).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: provider/CLI availability requires local installation and configuration. No live coding/model/provider execution was performed.

## S2 — Coordination

- State: —
- Function: no model-owned or agent-callable first-party cross-agent interference-regulation decision path established for supported local workflows.
- Disturbance / variety regulated: parallel CLI agents may overwrite shared files, contend for the same workspace or deliver incompatible edits.
- Decisive decision or feedback right: explicit worktree creation/merge/discard is selected by a desktop operator, not by a shipped S2 coordination agent or agent-usable collision policy in the assessed workflow.
- Decision owner: no autonomous S2 owner established; operator chooses isolation outside the S2 publication state.
- Supporting / enforcement mechanisms: user-authored graph edges, per-run workspace context, optional worktree selection API, file watcher, LangGraph ordered/parallel node execution and UI message routing.
- Closure path: the user selects a new worktree and runs a session there, preventing those filesystem writes colliding; no automated detection-and-response loop owned by an in-boundary agent changes the choices of two active S1 units.
- Why this is / is not agent-owned: user-chosen isolation is relevant and real, but graph sequencing and worktree menu actions alone do not establish first-party autonomous S2 ownership.
- Distinct S1 units: simultaneous configured agent invocations or separate terminal lanes.
- Inter-S1 disturbance: overlapping writes to the same source tree are a concrete potential collision.
- Attenuating coordination relation: separate Git worktrees create distinct directory trees at operator request, without a demonstrated agent-owned decision rule for applying them to contending peers.
- Feedback into subsequent S1 behaviour: a selected worktree sets the later session's file boundary, and a human can merge/reject the branch; there is no shown peer-feedback reconciliation autonomous path.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: an independently agent-controlled collision-specific relation is missing; manual safe-workspace configuration cannot be promoted merely because it prevents interference when selected.
- Evidence: [worktree UI and parallel isolation](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/docs/PRODUCT_INTRO.md#L100-L112), [worktree controller](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/services/orchestrator/src/routes/worktree.py#L25-L108), [workflow is operator-authored](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/docs/ARCHITECTURE.md#L17-L27).
- Basis: explicit and structural.
- Confidence: medium-high.
- Caveats: the product provides useful worktree separation, but Methodology S2 cannot publish human-only `P`. Custom scripts or external CLI agents might compose their own S2 decisions; none was credited without source evidence.

### Absence scope

- Surfaces inspected: workflow compiler/graph routing, CLI adapters, terminal lanes, run state, isolated worktree endpoints and product worktree UI.
- Plausible first-party paths checked: built-in workflows, direct chat, optional parallel worktrees, per-step check nodes and human merge/discard.
- Why no material first-party path remains: these are static/user choices, per-workspace isolation and task routing; no integrated agent-owned response to actual inter-agent contention is established.

## S3 — Inside-and-now control

- State: P
- Function: give the legitimate local operator whole-run/workflow supervisory control over live multi-agent activity and current risk.
- Disturbance / variety regulated: running steps fail, unsafe operations require approval, execution must stop/retry, and results/checks require operator disposition.
- Decisive decision or feedback right: approve/reject/retry at human gates, pause/stop and resume current workflow execution, change the active workspace/worktree or refine the flow.
- Decision owner: local desktop user/operator supervising the configured workflow; LangGraph and UI merely implement the selected intervention.
- Supporting / enforcement mechanisms: `ClutchState`, workflow Flow/Chat/Terminal/Changes panels, run checkpoint/interrupt, `human_required` messages, stop/run controls, `human_decision` and file/diff evidence.
- Closure path: sidecar publishes a live run state/interrupt, the operator inspects current status or artifact and chooses stop/approve/retry, the compiled graph/run subprocess changes state, and subsequent progress/reporting returns to the desk.
- Boundary reachability: documented supervision, Human Gate and stop controls are normal supported desktop workflows, not only a contributor script or speculative design.
- Why this is / is not agent-owned: the discretionary whole-workflow intervention comes from the legitimate operator; automatic safety check/fuse and routing enforcement do not move that right to an autonomous meta-agent.
- Whole-system current view: `ClutchState` joins current workflow node/agent, messages, terminal events, changed files, failure/status and pending human decision at one desk.
- Current-control decision scope: live workflow/run admission and interruption across configured steps/agents, not merely a single model turn's tool choice.
- Evidence: [LangGraph human interrupt/decision](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/services/orchestrator/src/compiler/compiler.py#L285-L310), [interrupt/resume](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/services/orchestrator/src/compiler/compiler.py#L415-L540), [current state and operator actions](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/docs/ARCHITECTURE.md#L228-L340).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: this is parent-governed control, not an autonomous S3 model. A default single chat may bypass workflow gates; the state is claimed for explicitly supported supervisory workflow mode.

## S3* — Complementary audit

- State: —
- Function: no separate independently controlled complementary audit of work claims with systemic corrective return established.
- Disturbance / variety regulated: an implementing agent may claim a successful output while files/tests disagree.
- Decisive decision or feedback right: same-run deterministic test/file checks can veto a green verification card, but no separately controlled auditor judgment is established.
- Decision owner: none at an independent S3* layer; agent `submit_verification` and sidecar checks share normal delivery path.
- Supporting / enforcement mechanisms: check nodes, `submit_verification`, deterministic test suite and file presence validation, diff/verification card UI.
- Closure path: failing checks cause a failed report/human retry; no independent auditor takes complementary evidence and controls corrective supervision separately from routine execution/QA.
- Why this is / is not agent-owned: independently inspecting actual tests is useful enforcement, but a same-agent verification call and scripted QA do not establish a separate audit owner.
- Evidence: [verification behavior and reporting](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/docs/PRODUCT_INTRO.md#L210-L215), [workflow `check` node semantics](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/docs/ARCHITECTURE.md#L145-L185), [verification cards](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/services/orchestrator/src/chat_runner.py#L859-L901).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: a user-authored workflow can configure additional agents; no default independently governed nonroutine audit is implied by naming one Evaluator.

### Absence scope

- Surfaces inspected: workflow `check` and `human_gate` nodes, verification reports, chat runner, example evaluator roles and diff/traces.
- Plausible first-party paths checked: example Builder/Evaluator template, `submit_verification`, test-suite gating and operator review of Changes.
- Why no material first-party path remains: templates do not ship fixed auditor roles; verification is same-run routine QA, with no independent agent-owned complementary probe and returned supervisory decision.

## S4 — Outside-and-then intelligence

- State: —
- Function: no operationally closed environmental scanning and prospective capability-adaptation decision path established for the local product.
- Disturbance / variety regulated: future CLI/provider/tool requirements and changes in surrounding workflows.
- Decisive decision or feedback right: no shipped agent/parent S4 actor shown selecting a longer-term adaptive capability change based on external scanning.
- Decision owner: none established at S4; user workflow editing is configuration, not a closed adaptation function.
- Supporting / enforcement mechanisms: mutable visual workflows, Skills/MCP registry, model settings, workflow refinement and release updater.
- Closure path: users can manually edit future SOPs and maintainers release versions, but an integrated outside-and-then decision returning new capability to the active system is not shown.
- Why this is / is not agent-owned: fixing present task artifacts and iterating a failing workflow step is not external prospective strategy.
- Evidence: [product editable SOP positioning](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/README.md), [workflow config and UI](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/docs/ARCHITECTURE.md).
- Basis: structural.
- Confidence: medium.
- Caveats: externally instructed long-horizon tasks could be executed, but they are user tasks, not an S4 adaptation function of Clutch itself.

### Absence scope

- Surfaces inspected: workflow/agent and skill configuration, chat task loop, refinements, updater, roadmap/specs and operator control.
- Plausible first-party paths checked: reusable workflows, runtime recovery, sidecar/CLI updates, human workflow revision and planned hybrid enhancements.
- Why no material first-party path remains: these operations are present-task or manual/developer configuration; the code does not establish an independent future-environment sensing, option decision and deployment loop.

## S5 — Policy and identity

- State: —
- Function: no distinct legitimate ultimate-purpose/identity adjudication path for the deployed local workspace runtime.
- Disturbance / variety regulated: fundamental dispute about workspace charter/identity rather than tool permissions or current workflow goals.
- Decisive decision or feedback right: no ultimate-policy matter, identified S5 owner and consequent policy closure found.
- Decision owner: none established; operator, maintainer and OS credential authorities govern adjacent ordinary matters.
- Supporting / enforcement mechanisms: permission modes, sensitive command prompts, workflow controls, user configuration and contributor documents.
- Closure path: an operator approves a risky operation or edits a flow but does not thereby decide the workspace's ultimate organizational identity as a separate feedback loop.
- Why this is / is not agent-owned: safety guardrails and permission prompts are not S5; a descriptive project mission in README is not operational identity governance.
- Evidence: [architecture security/supervision](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/docs/ARCHITECTURE.md), [permission boundary](https://github.com/fancy1108/Clutch/blob/d4d23af46e871a663886743535956d5c331313db/README.md#L191-L210).
- Basis: structural.
- Confidence: medium.
- Caveats: user or upstream maintainer normative decisions are outside this runtime assessment, not impossible in society.

### Absence scope

- Surfaces inspected: desktop permissions, agent settings, product purpose, workflow approvals, local credential handling, GitHub governance.
- Plausible first-party paths checked: owner-set configuration, human intervention, project/release policy, credential rules and workflow editing.
- Why no material first-party path remains: no nonroutine fundamental charter dispute reaches a recognized parent identity-level decision with returned operating policy at the declared recursion.

## Distributed OSS parent arrangement

The upstream MIT-licensed project has human maintainers and release/PR rules, but these are not the S5 of a user's deployed desktop workflow. A local owner legitimately performs supported S3 supervision within the product, without the OSS development team becoming the current-run manager.

## Self-hosted and non-human modes

Clutch operates locally with sidecar and external CLI/model dependencies. A configured agent may run many steps unattended within limits; supervisory workflow mode explicitly supports human-run S3 decisions. The README cautions that some external CLIs launch with permission-bypass flags, while the built-in MCP permission UI does not govern those external CLI flags. No implicit security assurance is inferred.

## Recursion

One workflow may contain multiple agent tasks, but fixed graph nodes and named templates are not independent viable systems. The local operator oversees the one workflow/state domain; unrelated windows/instances and upstream maintainers are outside this recursion.

## Variety and escalation

Model/tool feedback goes to operating agents. LangGraph conditions and run fuses reduce routine failure variety; a high-risk change or failed check can stop at a Human Gate and return after operator approval/retry. Git worktree isolation is available when the user elects it. Verification failures and human checks do not automatically imply S2/S3*/S4 or S5 ownership.

## Evidence gaps

- Positive S3 depends on the explicitly supported multi-agent workflow supervision mode; a bare direct-chat-only use need not exercise the same parent function.
- Optional worktrees are selected through UI/API but the inspected modes do not provide a separate autonomous collision-handling agent; S2 remains bounded negative.
- No independent complementary audit agent was located in the shipped QA path; named Evaluator roles belong to examples/configurable agents.
- Windows installers are generated but the README notes missing physical-device verification; source architecture, not platform-level reliability, was assessed.
- No live external CLI, LLM, native installer, agent E2E or quality evaluation was run.
