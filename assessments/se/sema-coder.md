---
harness_id: sema-coder
project_name: Sema Coder
repository: https://github.com/sema-lisp/sema-coder
review_ref: 284cffba02090f996da2d60524bcbb26651b4ed3
reviewed_at: 2026-10-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-04
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Sema Coder

## Review boundary

- System in focus: the first-party Sema Coder terminal coding-agent runtime at frozen revision `284cffba02090f996da2d60524bcbb26651b4ed3`, including its model/tool coding loop, built-in workspace tools, TUI turn controller, durable input queue/session state, managed background tasks, lifecycle hooks, configuration/extensions and supported one-shot/plain-REPL modes.
- Purpose and identity: complete software-engineering tasks in a selected workspace by letting a model inspect, edit, run and verify code while a human operator may govern the live interactive session's current commitments through the TUI controller.
- Relevant environment: the user's task and follow-ups, selected workspace/source/build/test state, model/provider responses, shell/background-process outcomes, project instructions, session/queue state, connected MCP tools and operator interventions.
- Standard-distribution boundary: `src/agent.sema`, `src/tools.sema`, `src/turn.sema`, the TUI/controller and session/queue machinery, configuration/hooks/extensions, built-in file/search/shell/background-task tools, plain REPL and one-shot modes are inside. External model providers, MCP server implementations, editors and operating-system services are dependencies and cannot donate organizational functions.
- Credited operating / distribution surfaces: `coder.sema`; `src/agent.sema`; `src/tools.sema`; `src/turn.sema`; `src/tui.sema`; `src/session.sema`; `src/commands.sema`; `src/config.sema`; `src/hooks.sema`; `README.md`; `docs/turn-control-design.md`.
- Adjacent first-party surfaces excluded from ownership: repository test suites, CI workflow, roadmap/planning documents, archived design plans, language-friction notes and prototype/demo surfaces. They may corroborate implementation properties but do not close runtime VSM functions unless wired into the supported operating mode.
- First-party operating / deployment modes considered: full-screen interactive TUI; plain non-TTY line REPL; one-shot `-p` execution including structured JSON mode; foreground and managed background shell tools; session resume; queued follow-ups and interrupt-and-send; configuration hot reload, custom commands/tools/plugins/hooks and connected MCP tools.
- Recursion level: one Sema Coder coding session around one workspace is the assessed organization. The model-backed coding actor is its S1. Shell/background processes are tools rather than autonomous S1 units. In TUI mode the human operator is a legitimate parent actor for the distinct current-control S3 mode over the session's active and queued commitments.
- Reviewed revision: `284cffba02090f996da2d60524bcbb26651b4ed3`.
- Observation date: 2026-10-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Sema Coder constructs a first-party model-backed coding agent in `src/agent.sema`. Its system prompt directs the actor to keep working until the task is resolved, inspect before editing, make focused changes, run commands, and verify results. `agent/run` executes turns against built-in tools plus connected MCP tools; tool results return into model history for subsequent action. TUI, plain REPL and one-shot entry paths reuse this agent construction.

The runtime owns workspace read/write/edit/search tools and real shell execution. Shell commands can run foreground or as application-managed background tasks; task status/output/list/stop tools expose those processes back to the coding actor. These jobs extend the S1's action repertoire but are not separate autonomous operational units.

The interactive TUI adds a distinct turn-control layer. It tracks the active turn/input/tool, a durable queue of follow-ups/steers, whether the queue is paused, current background tasks, message/session state and an ordered controller event log. The operator can inspect queued commitments, edit or drop individual queued inputs, clear or resume the queue, and interrupt the current turn while submitting replacement input. Controller decisions persist into session metadata and deterministically alter what turn executes next.

Interrupted turns retain completed history, synthesize correlated terminal results for unfinished tool calls, add a model-visible interruption marker, and pause ordinary queued work until the operator resumes it. Thus the controller is not merely an emergency-stop button: it maintains a whole-session current state and exposes continuing parent authority over the live set/order/content of commitments.

Configuration, AGENTS.md/CLAUDE.md, hooks, plugins, custom tools and MCP connections extend or constrain the current agent. Lifecycle hooks are observers whose return value is ignored; generic extension mechanisms do not by themselves create S2/S3*/S4/S5.

Primary evidence:

- [README.md](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/README.md)
- [coder.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/coder.sema)
- [src/agent.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/agent.sema)
- [src/tools.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/tools.sema)
- [src/tui.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/tui.sema)
- [src/turn.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/turn.sema)
- [src/session.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/session.sema)
- [src/commands.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/commands.sema)
- [docs/turn-control-design.md](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/docs/turn-control-design.md)

## Operational model

The coding actor receives user intent plus project instructions/current history, chooses tools through `agent/run`, observes their results and continues until the task resolves or the turn terminates. In TUI mode a separate operator-facing controller surrounds this S1: it makes the complete current turn/queue state inspectable and lets the parent revise the session's active or pending commitments. Those parent decisions are persisted and directly determine later turn execution.

## S1 — Operations

- State: A
- Function: perform environment-facing software-engineering work by selecting repository reads/searches/edits, shell/test actions and verification steps, observing their results and iterating toward the requested outcome.
- Disturbance / variety regulated: heterogeneous source/build/test state, ambiguous implementation choices, command/tool outcomes, background-process state, provider errors, context/history changes and project instructions.
- Decisive decision or feedback right: choose the next task-specific coding/tool action and integrate returned evidence into subsequent actions and the final response.
- Decision owner: the model-backed Sema Coder agent.
- Supporting / enforcement mechanisms: `agent/run`, built-in tool registry, workspace path checks for file/search tools, max-turn bounds, model/provider configuration, project instructions, turn recovery, shell/background-task lifecycle and operator-visible event plumbing.
- Closure path: user task/current history → model selects coding/tool action → first-party execution → tool/environment evidence returns into model history → model chooses the next action or completes the task.
- Boundary reachability: TUI, plain REPL and one-shot modes all construct and run the packaged first-party Sema Coder agent and its tools; the coding action loop does not depend on an external coding-agent runtime.
- Why this is / is not agent-owned: removing the model actor while leaving tools, sessions, controller and configuration intact removes the discretionary coding decisions and sequencing; the remaining machinery only executes, constrains or transports previously selected actions.
- Evidence: [src/agent.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/agent.sema); [src/tools.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/tools.sema); [coder.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/coder.sema).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the interactive operator can interrupt/redirect work through the separate S3 parent mode; that does not transfer ordinary S1 action selection to the parent.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established at the selected recursion.
- Disturbance / variety regulated: not established because the runtime exposes one primary coding agent rather than multiple interacting operational S1 units with a specific conflict/oscillation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: queued user messages, foreground/background process ownership, ordered tool execution, task IDs and controller queue ordering.
- Closure path: not applicable; no distinct-S1 disturbance → coordination response → changed subsequent S1 behaviour path was found.
- Why this is / is not agent-owned: queued follow-ups are parent inputs to one coding actor, and background shell processes are tools/processes without their own coding-agent decision loops.
- Evidence: [src/tui.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/tui.sema); [src/tools.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/tools.sema); [docs/turn-control-design.md](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/docs/turn-control-design.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the controller has a queue and process registry, but component ordering is not S2 without distinct S1 units and a concrete inter-S1 disturbance.

### Absence scope

- Surfaces inspected: coding agent construction; tool/background-process model; turn controller; durable input queue; session state; MCP/tool extension; lifecycle hooks.
- Plausible first-party paths checked: parallel coding workers, queued messages as workers, background tasks as S1 units, MCP tools as S1 units, shared-workspace collision handling and controller queue ordering.
- Why no material first-party path remains: all located concurrent/queued entities remain tools or parent-provided inputs for one coding S1; no first-party multi-S1 interference-and-attenuation loop is supplied.

## S3 — Inside-and-now control

- State: P
- Function: regulate the interactive session's current commitments and interventions across the active coding turn, pending follow-ups/steers and managed background activity on behalf of the whole session.
- Disturbance / variety regulated: the active agent may continue on a now-obsolete direction, queued commitments may become outdated or incorrectly ordered, interrupted tool work may leave partial side effects, and pending work may need to be paused, revised, dropped or resumed as current priorities change.
- Decisive decision or feedback right: decide whether the active turn should continue or be interrupted/replaced, and decide the retained content/order/execution state of the session's pending commitments by editing, dropping, clearing or resuming queued work.
- Decision owner: the human user/operator as legitimate parent authority in the supported interactive TUI mode.
- Supporting / enforcement mechanisms: `turn-controller-state`; stable queue IDs; active-turn IDs; pause flag; controller event log; persisted session metadata; `/queue` inspect/edit/drop/clear/resume commands; interrupt-and-send; correlated interruption recovery; managed background-task state.
- Closure path: controller exposes active turn/tool + pending queue + background/session state → operator chooses current-control intervention → runtime persists/executes interrupt, queue edit/drop/clear/pause/resume decision → subsequent turn selection/history/queue execution follows the returned parent decision.
- Boundary reachability: the TUI, queue controls, interrupt-and-send behavior, debug state and durable queue/session fields are packaged first-party operating features, not development-only test infrastructure.
- Why this is / is not agent-owned: the runtime enforces queue ordering, cancellation and persistence, but the discretionary decision to revise/stop/resume the whole session's current commitments belongs to the operator; without that parent choice the same intervention is not selected.
- Evidence: [src/tui.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/tui.sema); [src/commands.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/commands.sema); [src/session.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/session.sema); [src/turn.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/turn.sema); [docs/turn-control-design.md](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/docs/turn-control-design.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary prompting, one-off confirmation and a bare stop button are not credited. The positive witness is the distinct TUI controller that keeps a whole-session current view and recurring authority over active and queued commitments with durable return into execution.
- Whole-system current view: `turn-controller-state` exposes the current status/phase, active turn/input/tool, interruption mode, pending queue and pause state, managed background tasks, message/session state and ordered controller events; `/queue` and debug commands expose the relevant state to the operator.
- Current-control decision scope: revise the session's live commitments by interrupting/replacing an active turn, editing or deleting queued work, clearing the commitment queue, and controlling whether paused pending work resumes.
- Parent mode: in the supported interactive TUI, the human operator holds these current-control rights; the controller transports and enforces the returned decision so later execution obeys it.
- No autonomous/constructor base mode is claimed: the coding agent autonomously manages its local S1 actions, but no first-party autonomous manager or S3-specific constructor path independently governs the whole current session's commitments; generic hooks/plugins/extensions do not satisfy that threshold.

## S3* — Complementary audit

- State: —
- Function: no material complementary and sufficiently independent runtime audit path was established.
- Disturbance / variety regulated: not established at S3* level.
- Decisive decision or feedback right: not established. The coding actor is instructed to verify its own work and can inspect command/test results, while repository tests/CI audit the product during development rather than another live Sema Coder operation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: model-requested tests/readback, debug state/transcript/session surfaces, controller event log, repository tests and CI.
- Closure path: not applicable; no independent auditor judgment → corrective return into ordinary runtime control path was found.
- Why this is / is not agent-owned: runtime verification is produced/consumed by the same coding actor, and development tests/CI are adjacent to the assessed operating boundary.
- Evidence: [src/agent.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/agent.sema); [src/commands.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/commands.sema); [README.md](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: rich debug/controller state improves observability but is not a complementary auditor judgment.

### Absence scope

- Surfaces inspected: system prompt verification guidance; debug status/session/transcript/tasks; turn event log; tests/audit-regression tests; CI; hooks/plugins.
- Plausible first-party paths checked: separate reviewer/verifier agent, independent live replay/checker, controller event audit, development audit-regression tests and external CI verdict feedback.
- Why no material first-party path remains: ordinary verification remains in-band with S1, while independent-looking tests/CI are development surfaces not wired as an audit-return path in supported runtime operation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective organizational adaptation loop was established.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. Model/MCP/plugin/tool/configuration changes are operator/developer extension mechanisms, and roadmap/product research is adjacent development evidence rather than a live adaptation owner.
- Decision owner: not established.
- Supporting / enforcement mechanisms: MCP connections, plugins, autoloaded tools, hot-reloaded config, model selection, hooks, roadmap/design documents.
- Closure path: not applicable; no external/future distinction → adaptation option → adopted change to present organizational capability/control path was found inside the assessed runtime.
- Why this is / is not agent-owned: the coding agent uses whatever capabilities are currently configured; it does not own a persistent future-facing process that evaluates environmental change and revises Sema Coder's organizational capabilities.
- Evidence: [src/config.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/config.sema); [src/agent.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/agent.sema); [README.md](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the extension architecture makes manual adaptation easy, but generic extensibility is not an S4 constructor without an established outside-and-then loop.

### Absence scope

- Surfaces inspected: config hot reload; model catalog/switching; MCP management; custom tools/commands/plugins/hooks; project instructions; roadmap/design docs.
- Plausible first-party paths checked: autonomous capability acquisition, external trend sensing, future-oriented option generation, model/provider adaptation, plugin/tool self-installation and roadmap-to-runtime feedback.
- Why no material first-party path remains: durable capability changes remain operator/developer-authored, while product research/roadmap work is adjacent to runtime rather than a closed live S4 path.

## S5 — Identity and ultimate policy

- State: —
- Function: no material identity/ultimate-policy decision-and-return function was established at the selected session recursion.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. Project instructions, config, model selection, hooks, permissions and operator turn control govern operational behavior/current commitments rather than identity or ultimate policy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: AGENTS.md/CLAUDE.md prompt injection, config, hooks, plugin/tool trust choices, MCP connection choices, model/effort selection and TUI controls.
- Closure path: not applicable; no identity/ultimate-policy issue → legitimate authority decision → returned governance of subsequent operation path was found.
- Why this is / is not agent-owned: human control is substantial in the TUI, but its evidenced decision scope is current session control (S3), not identity/ultimate policy; static context/policy/configuration text is insufficient for S5.
- Evidence: [src/agent.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/agent.sema); [src/config.sema](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/src/config.sema); [README.md](https://github.com/sema-lisp/sema-coder/blob/284cffba02090f996da2d60524bcbb26651b4ed3/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the operator is a legitimate parent for S3, but parent presence does not automatically create S5.

### Absence scope

- Surfaces inspected: project instructions/system prompt; configuration; hooks/plugins/custom tools; MCP/model selection; TUI current-control paths; roadmap/governance-adjacent documentation.
- Plausible first-party paths checked: identity/purpose escalation, constitutional policy change, project instructions as ultimate authority, plugin/MCP trust as policy and operator intervention as S5.
- Why no material first-party path remains: evidence closes current operational control but not an identity/ultimate-policy issue path with authoritative decision and returned governance.

## Recursion, variety, escalation and unresolved evidence

- Recursion: one coding session is the assessed organization. The model-backed agent is the S1; shell/background processes remain tools. The TUI operator sits at a legitimate parent recursion for the distinct current-control S3 mode.
- Variety: source/build/test state, tool/process outcomes, queued follow-ups, interruption/partial-side-effect state, context/history, configuration and provider/tool errors are absorbed by S1 plus the parent current-control layer.
- Escalation: current-session conflicts or changed intent can be expressed through queue edits, pause/resume and interrupt-and-send; tool/process failures return to S1. These current-control paths are classified as S3 rather than S5.
- Unresolved evidence: no material gap required `?`. Positive credit is limited to autonomous S1 and parent-governed S3; no qualifying S2, S3*, S4 or S5 path was established.

## Assessment vector

**A · — · P · — · — · —**
