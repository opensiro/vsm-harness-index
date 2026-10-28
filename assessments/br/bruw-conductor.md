---
harness_id: bruw-conductor
project_name: Conductor
repository: https://github.com/bruw/workflow-conductor
review_ref: 16076f7517bf13b3c5b7e492c3f6c5df800be871
reviewed_at: 2026-10-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Conductor

## Review boundary

- System in focus: the installed workflow-conductor Claude Code plugin itself: project designer, handoff, lints and run visualization; not the host Claude Code agent/Workflow engine or scripts it writes.
- Purpose and identity: help a user design, inspect, hand off and monitor multi-agent workflows in a terminal board.
- Relevant environment: user keyboard/mouse and submitted prompts, local project JSON, host tool events, Workflow scripts and journal files.
- Standard-distribution boundary: .claude-plugin manifest, hooks/project.tsx and hooks/run.tsx, project model/session/handoff/offer tools and run tracker/reducer/journal.
- Credited operating / distribution surfaces: src/project/*, src/run/* and loaded hooks implement deterministic UI/data/control adapters.
- Adjacent first-party surfaces excluded from ownership: fixtures/replays, tests, rendered demo media and dev-session tooling; host agent inference and Workflow script execution are external even when shown on the board.
- First-party operating / deployment modes considered: manual board; /conductor description draft; q design review; r user-submitted implementation handoff; live tracking; script save after run; subagent/noninteractive standard-answer mode.
- Recursion level: one UI plugin attached to an independently supplied agent session; graph nodes are design data, not proof of operative viable units.
- Reviewed revision: `16076f7517bf13b3c5b7e492c3f6c5df800be871`.
- Observation date: 2026-10-28.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Conductor ships a terminal workflow editor inside Claude Code. Project JSON stores named blocks, logic, model/effort/isolation knobs and nesting. Pure lints flag structural issues without blocking execution. Handoff code puts a sentence into the prompt box; the human must send or edit it. The host Claude agent then reads project data through plugin tools, writes a Workflow script and invokes the host Workflow tool. Hooks pass those host tool calls/results onward and correlate run IDs, subagent IDs, usage, journal phases and terminal statuses to graph nodes. The tracker writes visual state, not an agent decision or execution command. After a run, an explicit save choice copies the host-generated script to the allowed workflow path. The README expressly states that the plugin makes no network requests, runs no program and never submits a prompt; source handoff/hooks/tracker corroborate that boundary.

## Operational model

Disposition proposed for admission: excluded-no-agentic-vsm. The plugin produces an edited plan, handoff context and observed run board. Its standard distribution does not itself supply or launch an autonomous operational actor. User-submitted host reasoning, host script generation and host Workflow runtime provide the goal/reason/action/feedback loop. They are not credited as first-party Conductor S1 merely because Conductor displays or describes them. Review/Research/Judge templates and agent-kind names are design instructions, not installed independent actor/closure evidence.

## S1 — Operations

- State: —
- Function: no first-party autonomous operational decision/action loop inside the plugin boundary.
- Disturbance / variety regulated: malformed/changed plans, user edits and host workflow event updates.
- Decisive decision or feedback right: user selects/edits/submits the handoff; external Claude writes and runs the script.
- Decision owner: human and external Claude Code/Workflow engine; plugin applies deterministic edits and observations.
- Supporting / enforcement mechanisms: project schema/tools, handoff context, prompt-box insertion, lints and tracking hooks.
- Closure path: board → visible handoff sentence → human Enter → external host agent/script/run → plugin observes status; autonomous execution closes outside the plugin.
- Why this is / is not agent-owned: the package never submits prompts, calls a model or starts a program; removing the host agent leaves a usable deterministic editor/monitor.
- Caveats: exclusion is boundary-relative and does not say the external composed Claude workflow lacks agency.
- Evidence: [README.md](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/README.md); [src/project/handoff.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/handoff.ts); [hooks/project.tsx](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/hooks/project.tsx); [hooks/run.tsx](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/hooks/run.tsx); [src/run/tracker.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/run/tracker.ts).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: Manifest, README runtime/touch boundaries, project/handoff/offer/session tools, loaded hooks and tracker.
- Plausible first-party paths checked: draft/design review/run handoffs, plugin project tool, intercepted Write/Edit/Workflow calls, tracked subagents and saved-script replay.
- Why no material first-party path remains: every cognitive/executable path is explicitly performed by the external host after user submission; the plugin supplies no autonomous S1 owner at its own boundary.

## S2 — Coordination

- State: —
- Function: no first-party inter-S1 conflict regulation with agent-owned or specific constructor feedback.
- Disturbance / variety regulated: graph ordering and concurrent node design may imply intended task dependencies; edits while a project is running could desynchronize its display.
- Decisive decision or feedback right: project locks/lints preserve editor consistency; script/host decides execution and coordination.
- Decision owner: user/designer and external host engine, not an in-plugin coordination actor.
- Supporting / enforcement mechanisms: nested project blocks, pipeline/parallel labels, edit-during-run refusal and run-node mapping.
- Closure path: design data passes to external script composition; runtime events map back to display.
- Why this is / is not agent-owned: a workflow graph and edit lock do not establish distinct first-party operational units plus inter-unit corrective return.
- Caveats: generated scripts can implement coordination externally; their semantics are not supplied as a universal first-party plugin mode.
- Evidence: [src/project/model.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/model.ts); [src/project/lints.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/lints.ts); [src/project/session.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/session.ts); [hooks/project.tsx](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/hooks/project.tsx).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: Project blocks/templates/knobs, advisory lints, project write guards and tracking mappings.
- Plausible first-party paths checked: parallel/pipeline/loop design, dependency warnings, shared project edits and host agent result mapping.
- Why no material first-party path remains: there are no first-party autonomous S1 cells to coordinate; editor consistency and generic workflow sequencing do not close an inter-S1 regulation path.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current-control decision loop owned by this plugin.
- Disturbance / variety regulated: unbounded workflow designs, estimated cost, failed/stopped host runs and stale telemetry.
- Decisive decision or feedback right: operator chooses execution; external Claude selects script behavior; plugin reports warnings and observed usage/status.
- Decision owner: human and host engine; deterministic lints/tracker do not own resource decisions.
- Supporting / enforcement mechanisms: worst-case design hints, token/elapsed telemetry, run state, UI navigation and project lock.
- Closure path: warning/telemetry → human/host interpretation outside the plugin, without a first-party applied current-control decision over a portfolio.
- Why this is / is not agent-owned: visualizing budgets or showing failure is not autonomous S3 or a specific closed parent current-control mode.
- Caveats: the host may expose stop/control independently, which is not a Conductor-owned right.
- Evidence: [src/project/lints.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/lints.ts); [src/project/handoff.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/handoff.ts); [src/run/tracker.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/run/tracker.ts); [hooks/run.tsx](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/hooks/run.tsx).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: Design checks/handoff review question, tracker/reducer, run-end/save hooks and documented touch boundary.
- Plausible first-party paths checked: cost/agent-count estimates, budget loop kind, stopped/stale/failed statuses and user run/save choices.
- Why no material first-party path remains: these expose design or observability, without whole-system discretionary resource/commitment intervention returned by this plugin into its own operations.

## S3* — Complementary audit

- State: —
- Function: no complementary independent audit over first-party operational claims.
- Disturbance / variety regulated: structural graph defects and externally reported run failures.
- Decisive decision or feedback right: q inserts a design-review request to the external host; lints inspect graph structure only.
- Decision owner: external Claude/user for semantic design review; developer rules for structural lints.
- Supporting / enforcement mechanisms: review prompt, verify/judge/critic template labels and journal/status replay.
- Closure path: request/template reaches host model; plugin receives ordinary run telemetry and displays it.
- Why this is / is not agent-owned: the plugin has no independent auditor, raw-operation evidence probe or corrective audit verdict path of its own.
- Caveats: a generated review workflow may be useful audit at a different composed boundary; it is not automatically this plugin S3*.
- Evidence: [src/project/handoff.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/handoff.ts); [src/project/templates.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/templates.ts); [src/project/lints.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/lints.ts); [src/run/journal.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/run/journal.ts).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: q review handoff, Review/Judge templates, structural lints, run-event/journal replay and hooks.
- Plausible first-party paths checked: verify/critic patterns, review request, result journal reconstruction and design warnings.
- Why no material first-party path remains: templates and ordinary reporting do not compose a first-party independent audit judgment/access/returned-control loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally and prospectively oriented capability-adaptation loop.
- Disturbance / variety regulated: learning workflow patterns and revising plans for current tasks.
- Decisive decision or feedback right: user or external host revises project design; plugin stores that design or copies a script on explicit save.
- Decision owner: user/external host model; no plugin adaptation owner.
- Supporting / enforcement mechanisms: pattern teaching, templates, project history, undo/redo, review question and saved scripts.
- Closure path: current design changes are persisted and reused, without environmental foresight/options entering present-capability regulation.
- Why this is / is not agent-owned: teaching/plan refinement and reusable scripts alone do not satisfy S4.
- Caveats: an external agent can design adaptive workflows; this package does not supply their autonomous adaptation closure.
- Evidence: [src/project/teach.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/teach.ts); [src/project/templates.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/templates.ts); [src/project/history.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/history.ts); [src/project/offer.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/offer.ts).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: Pattern teaching/templates, design review/handoff, history and script save/reuse.
- Plausible first-party paths checked: research template, convergence/target/budget loops, learned design refinements and saving future reusable scripts.
- Why no material first-party path remains: these are user/host task design and file persistence; no first-party external/prospective distinction-to-adaptation decision-to-current capability loop remains.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy authority and return loop.
- Disturbance / variety regulated: workflow goal/settings and user choice whether to design/run/save.
- Decisive decision or feedback right: user supplies project goal and handoff consent; host supplies agent permissions and execution policy.
- Decision owner: human owns local design choices; external host owns its governance; plugin has no identity adjudicator.
- Supporting / enforcement mechanisms: start/goal block, before_workflow offer, named output paths, manifest and safe prompt/file boundaries.
- Closure path: project choice reaches external host through a human-submitted prompt; no identity/ultimate-policy issue returns as Conductor governance.
- Why this is / is not agent-owned: task goals, safe write paths and an execution offer are not S5 merely because a human chooses them.
- Caveats: no organization-level or external Claude policy rights are inferred.
- Evidence: [src/project/model.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/model.ts); [src/project/offer.ts](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/src/project/offer.ts); [hooks/offer.tsx](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/hooks/offer.tsx); [.claude-plugin/plugin.json](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/.claude-plugin/plugin.json); [README.md](https://github.com/bruw/workflow-conductor/blob/16076f7517bf13b3c5b7e492c3f6c5df800be871/README.md).
- Basis: structural
- Confidence: medium-high for source topology; live agent efficacy unmeasured.

### Absence scope

- Surfaces inspected: Project goal/schema, before_workflow user offer, save consent, manifest and documented file/prompt restrictions.
- Plausible first-party paths checked: goal/start block, design-first offer, user run decision and accepted save target.
- Why no material first-party path remains: these regulate ordinary task/UI interaction and static scope, not a routed identity/ultimate-policy decision governing the assessed plugin operations.

## Distributed OSS parent arrangement

Maintainer development governance and user operation remain adjacent. An installed plugin shares the host process but does not inherit its parent organization or agent identity/ultimate-policy loop.

## Self-hosted and non-human modes

Requires Claude Code with Workflow support. Manual and interactive handoffs keep human submission; subagent/noninteractive hooks return standard context instead of adding a new plugin-owned model actor. No self-hosted autonomous or non-human mode is supplied.

## Recursion

Nested graph containers and displayed spawned agents belong to host-run scripts. They do not establish recursive viable organizations inside the editor/monitor.

## Variety and escalation

Schema parsing, structural warnings, project locks, bounded UI state, journal/event correlation, stale-run detection and visible handoff boundaries handle editor/telemetry variety. Execution failure and cost remain observable host outcomes, not a new in-plugin regulatory owner.

## Evidence gaps

No live Claude/Workflow/provider/Browser run. Native plugin validation/typecheck/tests require unavailable Claude Code tooling and generated .claude-plugin/types; no native PASS is claimed. Handoff/tracker/hook test source was inspected as corroboration. Native preflight CLI retrieval returned HTTP 403 twice; fresh issue/comments were obtained through the GitHub connector and the unmodified canonical build_envelope function passed with row 5, exact repository/ref and active contract. This is a transport recovery, not a changed queue or waived structural gate. Final exclusion has no positive autonomy grade or signature.
