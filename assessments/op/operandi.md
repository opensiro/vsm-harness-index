---
harness_id: operandi
project_name: Operandi
repository: https://github.com/modus-lisp/operandi
review_ref: 1d1c6b5c28ff4f5cb80a31aed709145527c1a78f
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Operandi

## Review boundary

- System in focus: the first-party Operandi coding-agent distribution at frozen revision `1d1c6b5c28ff4f5cb80a31aed709145527c1a78f`, including the Common Lisp ReAct loop, built-in coding tools, Task/Fan/Investigate/Spawn delegation, session persistence, ACP surface, and the optional first-party MCP fan/swarm server where it supplies a function-specific constructor path.
- Purpose and identity: complete software and knowledge-work tasks through a model-driven tool loop that can read/write code, execute commands and Lisp, search, delegate bounded work, preserve session state, and expose the loop to terminal, ACP and MCP callers.
- Relevant environment: user/caller objectives, repository/filesystem state, shell and Lisp runtime state, provider/model responses, web/search results, tests/oracles, child-agent results, session history, and operator permission decisions in ACP mode.
- Standard-distribution boundary: shipped Operandi Common Lisp runtime plus its bundled MCP server and documented CLI/TUI/ACP modes are inside. External MCP clients/calling models, model-provider internals, host-repository governance, user-authored cron schedules and target-project merge policy are environment or parent composition rather than Operandi-owned actors.
- Credited operating / distribution surfaces: `README.md`; `src/engine.lisp`; `src/tools.lisp`; `src/subagent.lisp`; `src/session.lisp`; `src/sessiontree.lisp`; `src/cron.lisp`; `mcp/server.js`; documented CLI/TUI/ACP entry points.
- Adjacent first-party surfaces excluded from ownership: `docs/swarm-queue-spec.md` where it is explicitly proposal/pick-up-ready rather than shipped native runtime; inspect/test artifacts; repository development plans; host project governance; external MCP client behavior.
- First-party operating / deployment modes considered: library/CLI ReAct execution, interactive TUI, resumable sessions, Task/Fan/Investigate/Spawn delegation, ACP server, optional MCP `operandi_run`/`operandi_fan`/`operandi_swarm`, and empty-by-default in-image cron support.
- Recursion level: one Operandi task/caller mission. The main model loop is an S1; delegated child Operandi loops and MCP swarm workers can be additional bounded S1 units when they perform independent environment-facing work.
- Reviewed revision: `1d1c6b5c28ff4f5cb80a31aed709145527c1a78f`.
- Observation date: 2026-10-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Operandi's core is a ReAct-style loop in `src/engine.lisp`: the selected model receives conversation state and tool schemas, chooses tool calls, receives first-party tool results and continues until a final answer or execution bound. Built-ins include file operations, shell, grep/glob, web access, persistent notes/TODOs and arbitrary Lisp evaluation inside the host image. Tool pre/post hooks and SQLite logging support observability; tool limits and ACP permission gates constrain execution without owning the model's substantive choices.

`src/subagent.lisp` adds multiple delegation modes. `Task` runs one fresh child loop; `Fan` runs independent child prompts concurrently; `Investigate` assigns independent hypotheses to workers and gathers explicit verdict records; `Spawn` plus `SendMessage` retains a child conversation for follow-up. These mechanisms reset context and fan work out, but ordinary delegation alone is not treated as S2 or S3.

The bundled MCP server is a distinct supported surface. `operandi_fan` executes caller-carved independent tasks concurrently. `operandi_swarm` is more specific: each unit runs in its own isolated copy, performs a worker edit/oracle/fix loop, and then the server independently re-runs the supplied oracle in that copy before reporting a verdict. The caller still owns decomposition and canonical merge; the first-party server intentionally does not merge.

The repository also contains `docs/swarm-queue-spec.md`, which describes a larger durable agenda with atomic claims, leases, merge membrane and 100-worker operation, but that document labels itself proposal/pick-up-ready. It is useful boundary evidence but is not credited as shipped closure.

## Operational model

The ordinary Operandi actor owns open-ended coding decisions: which evidence to inspect, which built-in tool to invoke, what edits/commands to make and when to delegate. The deterministic runtime executes, logs, bounds or refuses those calls and returns results into the next model turn.

When an external first-party MCP deployment uses `operandi_swarm`, multiple worker S1s receive isolated working copies. The bundled server protects them from shared-tree write interference and independently re-runs each unit's oracle after the worker terminates. However, the calling model/application supplies the unit decomposition and later merge/collection decision, so those function-specific paths do not become autonomous Operandi ownership.

## S1 — Operations

- State: A
- Function: perform environment-facing coding/analysis work through a model-driven loop that reads state, chooses tools, mutates files or the running Lisp image, runs commands and incorporates returned results.
- Disturbance / variety regulated: arbitrary codebase structure, failing commands/tests, runtime errors, external search results, incomplete information, tool failures and implementation alternatives.
- Decisive decision or feedback right: choose the next substantive tool/action, interpret returned evidence, revise the approach and determine when the bounded task is ready for a final response.
- Decision owner: the active model-backed Operandi actor; delegated child loops own the same local decision right for their assigned bounded subtasks.
- Supporting / enforcement mechanisms: OpenAI-compatible provider transport; tool registry; hooks/audit DB; timeouts and file-size limits; context compaction; session persistence; TUI/ACP/MCP adapters.
- Closure path: task/current state → model turn → selected first-party tool → runtime executes or returns refusal/error → tool result is appended → later model turn changes subsequent operation.
- Boundary reachability: `operandi.engine:run` and the same tool loop are the documented library/CLI/TUI core, with ACP/MCP adapters invoking shipped Operandi execution rather than requiring an application to implement a separate agent.
- Why this is / is not agent-owned: without the model actor, the deterministic runtime retains tools, logs and bounds but no longer chooses open-ended coding actions or interprets their results.
- Evidence: [`README.md`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/README.md); [`src/engine.lisp`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/src/engine.lisp); [`src/tools.lisp`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/src/tools.lisp).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: provider inference is external; the credited organizational loop is Operandi's first-party tool/action composition.

## S2 — Coordination

- State: C
- Function: protect concurrent worker S1s from destructive shared-tree interference by assigning each `operandi_swarm` unit its own isolated working copy before the worker edit/oracle loop executes.
- Disturbance / variety regulated: concurrently running coding workers can otherwise modify the same files/tree and overwrite or invalidate each other's assumptions.
- Decisive decision or feedback right: determine the decomposition/edit scopes that should be run as distinct units and therefore placed into separate isolated copies.
- Decision owner: not autonomously owned by Operandi in this mode. The external MCP caller supplies the unit decomposition; Operandi's first-party server exposes and enforces the S2-specific isolated-worker path.
- Supporting / enforcement mechanisms: per-unit temporary working directories/copies; independent worker processes; bounded fan-out queue; per-unit status; isolated oracle execution.
- Closure path: caller supplies multiple concurrently executable units → first-party swarm server creates a separate copy/cwd per unit → each worker's subsequent file/tool operations occur only in its assigned copy → per-unit results and green working directories return to the caller for downstream collection.
- Boundary reachability: `mcp/server.js` ships with the repository and README documents the MCP server and `operandi_swarm` surface; the isolation path is executable first-party behavior rather than a design-only proposal.
- Why this is / is not agent-owned: the first-party primitive is specifically aimed at a real inter-worker edit collision, but the autonomous authority that decides the semantic decomposition/edit scopes is supplied by the caller, so the path meets the constructor threshold rather than `A`.
- Evidence: [`README.md`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/README.md); [`mcp/server.js`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/mcp/server.js).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `Fan`, Task and message passing alone are not the witness; the positive mapping uses the swarm server's concrete isolated-copy response to concurrent edit interference.
- Distinct S1 units: separate Operandi worker processes, each running a model/tool loop on one coding unit.
- Inter-S1 disturbance: simultaneous workers modifying one canonical/shared tree could collide, overwrite changes or consume stale shared state.
- Attenuating coordination relation: first-party `operandi_swarm` creates a distinct working copy and cwd for each worker unit.
- Feedback into subsequent S1 behaviour: the isolation decision changes the filesystem environment observed by every later tool call of that worker; returned per-unit verdict/copy paths keep results separated for the caller's next step.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited primitive is explicitly tied to preventing cross-worker edit interference, not merely to launching or routing several tasks.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-control loop was established at the selected recursion.
- Disturbance / variety regulated: not established at S3 level.
- Decisive decision or feedback right: no first-party actor was found with both a whole-system current view and discretionary authority to reprioritize resources/commitments or intervene on behalf of the whole during active multi-S1 execution.
- Decision owner: not established.
- Supporting / enforcement mechanisms: iteration limits; timeouts; fan batching; swarm worker queue; per-job status/kill path; subagent depth caps; usage accounting.
- Closure path: not applicable; located mechanisms enforce fixed limits or caller-issued task decisions rather than a first-party whole-system S3 judgment loop.
- Why this is / is not agent-owned: the main model can choose to delegate work, but task decomposition and result synthesis alone do not establish S3; the MCP caller, not Operandi, owns multi-unit carve/merge authority in the swarm mode.
- Evidence: [`src/subagent.lisp`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/src/subagent.lisp); [`mcp/server.js`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/mcp/server.js); [`README.md`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/README.md).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: the proposal-only native swarm agenda describes richer control but is excluded from shipped ownership.

### Absence scope

- Surfaces inspected: main agent loop; Task/Fan/Investigate/Spawn/SendMessage; MCP job registry/fan/swarm; iteration/cost/depth bounds; cron; sessions/TUI/ACP.
- Plausible first-party paths checked: live task-tree supervision, dynamic reprioritization, shared resource allocation, stop/steer authority across running children, workflow-wide intervention and autonomous merge control.
- Why no material first-party path remains: shipped runtime exposes delegation, fixed enforcement and caller-facing job/swarm status, but no Operandi-owned actor was found that observes the active multi-S1 whole and closes discretionary current-control decisions over shared commitments/resources.

## S3* — Complementary audit

- State: C
- Function: independently check whether a coding worker's claimed unit satisfies its explicit oracle before that unit is reported as green.
- Disturbance / variety regulated: a model worker can claim success while tests/oracle still fail, or can leave a result whose self-report is not trustworthy.
- Decisive decision or feedback right: accept or reject the unit's verification status based on a fresh post-worker oracle execution in the isolated copy.
- Decision owner: first-party deterministic MCP swarm code owns the exit-code verdict; no autonomous audit actor is supplied by Operandi for this path.
- Supporting / enforcement mechanisms: isolated per-unit copy; fresh-cache oracle subprocess; worker lifecycle/status record; per-unit result rendering.
- Closure path: worker finishes its edit/oracle/fix attempt → first-party server independently runs the supplied oracle again in that worker's copy → exit code becomes the authoritative unit verdict → only independently passing copies are returned as green for downstream collection.
- Boundary reachability: README documents the bundled MCP server; `operandi_swarm` and its post-worker independent re-verification are implemented in shipped `mcp/server.js`.
- Why this is / is not agent-owned: removing the external worker's self-report still leaves the independent first-party oracle verdict, so the worker does not own audit acceptance. Conversely, the audit judgment is deterministic rather than a separate autonomous auditor, making this a constructor-owned audit path.
- Evidence: [`mcp/server.js`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/mcp/server.js); [`README.md`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary tests run by the same worker are not credited; the witness is the distinct post-worker re-verification run.
- Claim being audited: that a worker's isolated coding unit satisfies the caller-supplied oracle.
- Ordinary reporting path: worker executes its own edit/oracle/fix loop and terminates with an answer/status.
- Complementary access path: the MCP swarm server launches a fresh oracle subprocess after worker completion, directly against the worker's isolated filesystem state.
- Independence boundary: the re-verification is outside the worker model/tool loop and does not rely on the worker's verbal success claim.
- Who acts on findings: the first-party swarm server labels the unit done/error and exposes only passing copies in `green_wds`; the caller can then collect/merge those results.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party prospective adaptation loop was established at the selected task recursion.
- Disturbance / variety regulated: not established at S4 ownership level.
- Decisive decision or feedback right: not established. Web search, durable notes, session branching, context compaction and cron can feed later work, but no shipped actor was found that turns external/future distinctions into adaptation options and changes Operandi's present capability/strategy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: WebSearch/WebFetch; Remember; session persistence/session-tree branching; cron scheduler; context compaction; Eval extensibility.
- Closure path: not applicable; no prospective intelligence → selected adaptation → returned capability/S3 change loop was established.
- Why this is / is not agent-owned: the operational agent can use new information inside its current task, while host code/configuration can change capabilities; neither by itself establishes an S4 organizational function.
- Evidence: [`README.md`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/README.md); [`src/engine.lisp`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/src/engine.lisp); [`src/sessiontree.lisp`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/src/sessiontree.lisp); [`src/cron.lisp`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/src/cron.lisp).
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: the session-tree comment mentions a possible self-improvement review-fork, but the generic custom-entry/branch primitive is not a closed self-improvement loop.

### Absence scope

- Surfaces inspected: web/search tools, Remember/TODO, sessions/sessiontree, context compaction, cron, Eval, delegation and MCP surfaces.
- Plausible first-party paths checked: durable learning, self-review forks, scheduled research, model/config/tool changes, automatic self-improvement and adaptation of future capability.
- Why no material first-party path remains: shipped mechanisms provide information, persistence, scheduling or generic extensibility; no first-party prospective actor/decision loop was found that selects and returns an adaptation into durable organizational capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure was established at the selected recursion.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. Base system prompts, tool lists, ACP permissions, caller tasks and host-loaded packages constrain operation but do not form a runtime identity/ultimate-policy resolution loop.
- Decision owner: not established inside Operandi.
- Supporting / enforcement mechanisms: system prompt/configuration; tool restrictions passed to subagents; ACP permission gate; timeouts/depth caps; host package loading; caller/operator instructions.
- Closure path: not applicable; no identity/policy issue → legitimate ultimate authority → authoritative decision → returned governance loop was established.
- Why this is / is not agent-owned: the model works within configured prompts/tools and may evaluate Lisp, but generic mutability/extensibility does not give it a legitimate S5 decision right.
- Evidence: [`README.md`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/README.md); [`src/tools.lisp`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/src/tools.lisp); [`src/subagent.lisp`](https://github.com/modus-lisp/operandi/blob/1d1c6b5c28ff4f5cb80a31aed709145527c1a78f/src/subagent.lisp).
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: operator/caller authority exists in the surrounding system, but generic task/configuration/permission control is not enough for Methodology 0.3.6 parent-mode S5.

### Absence scope

- Surfaces inspected: base system prompt; model/tool configuration; ACP permissions; CLI/TUI controls; Eval; host application package exposure; subagent restrictions; session branching.
- Plausible first-party paths checked: autonomous mission/identity revision, ultimate-policy proposals, parent policy escalation/return, policy exception handling and persistent governance changes.
- Why no material first-party path remains: located controls specify or enforce execution context and permissions; no function-specific identity/ultimate-policy issue-resolution loop is supplied in the standard distribution.

## Recursion

The selected recursion is one Operandi task/caller mission. Main and child agent loops are operational units. The optional MCP swarm is a first-party deployment mode but retains caller-owned decomposition and merge authority. Repository development and the proposal-only native swarm agenda are outside ownership.

## Variety and escalation

Operandi absorbs coding variety through model/tool discretion, Lisp evaluation, search, context compaction and delegation. Bounds such as iteration/depth/timeouts and ACP permission refusal can stop or constrain operation. The MCP swarm adds per-unit isolation and independent oracle re-verification, while downstream integration remains with the caller.

## Evidence gaps

The frozen source is sufficient for high-confidence S1 and constructor-owned S2/S3* paths. The main ambiguity is whether future native swarm work would add S3 or other functions, but the available swarm agenda is explicitly proposal status and therefore cannot be imported into the frozen standard-distribution classification.
