---
harness_id: ralphify
project_name: Ralphify
repository: https://github.com/computerlovetech/ralphify
review_ref: 3734146c6bb8e97b97e6e26c473d44eabd2b67f7
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Ralphify

## Review boundary

- System in focus: One Ralphify `ralph run` loop executing a user-authored `RALPH.md` through a configured external agent CLI, with optional first-party concurrent-run management.
- Purpose and identity: Repeatedly perform a scoped coding/work objective with fresh model context and current command-derived project observations until interrupted or a configured limit/error condition is reached.
- Relevant environment: changing project files, failing tests, CLI agent behavior, command outputs, operator edits, subprocess failures and timeouts.
- Standard-distribution boundary: shipped Python CLI, frontmatter resolver, iteration engine, subprocess launcher, RunState and RunManager; an installed external model agent CLI is an explicit required execution dependency.
- Credited operating / distribution surfaces: `src/ralphify/cli.py`, `engine.py`, `_agent.py`, `_runner.py`, `_resolver.py`, `_run_types.py` and `manager.py` in documented installed-mode loops.
- Adjacent first-party surfaces excluded from ownership: contributor/release/brand skills, Cowork setup assistant, docs website, research/ralph-loops analysis, test fake-Claude binary and CI; none is automatically active in a launched Ralphify work loop.
- First-party operating / deployment modes considered: standard `ralph run` with a configured Codex/Claude/Pi-compatible agent; `commands` observations and repeated fresh-context iterations; optional `-n`, stop-on-error, pause/resume; concurrent independent runs through `RunManager`.
- Recursion level: one continuing user-defined work loop. Each fresh agent subprocess is another bounded turn of that S1, not a separate S1 organization merely because it is a new process.
- Reviewed revision: `3734146c6bb8e97b97e6e26c473d44eabd2b67f7`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Ralphify reads a directory-local `RALPH.md` definition containing an external agent command and optional observation commands. Before each iteration `engine.run_loop` runs the configured commands, interpolates their output plus user arguments and loop counters into the freshly read prompt, then passes that prompt to an agent subprocess. `_agent.py` handles streaming/blocking subprocess execution, timeouts, result capture and log output. The loop records outcome counters/events and repeats or stops on a limit, explicit request or configured failure. `RunManager` can host several independent loops in threads and expose pause/stop/status controls, but it does not schedule collaborative work or make organization-wide decisions. Users own the loop definition and may edit its prompts between iterations. The repository itself declares educational/non-production maintenance status, which does not change the pinned functional assessment.

Primary frozen sources:

- [README: supported loop format and agent-CLI dependency](https://github.com/computerlovetech/ralphify/blob/3734146c6bb8e97b97e6e26c473d44eabd2b67f7/README.md)
- [Engine: fresh command feedback, prompt assembly, agent phase and loop control](https://github.com/computerlovetech/ralphify/blob/3734146c6bb8e97b97e6e26c473d44eabd2b67f7/src/ralphify/engine.py)
- [Agent subprocess execution and results](https://github.com/computerlovetech/ralphify/blob/3734146c6bb8e97b97e6e26c473d44eabd2b67f7/src/ralphify/_agent.py)
- [Configured observations/timeout behavior](https://github.com/computerlovetech/ralphify/blob/3734146c6bb8e97b97e6e26c473d44eabd2b67f7/src/ralphify/_runner.py)
- [Prompt placeholders and frontmatter parsing](https://github.com/computerlovetech/ralphify/blob/3734146c6bb8e97b97e6e26c473d44eabd2b67f7/src/ralphify/_resolver.py)
- [Independent concurrent-run manager](https://github.com/computerlovetech/ralphify/blob/3734146c6bb8e97b97e6e26c473d44eabd2b67f7/src/ralphify/manager.py)
- [Contributor architecture and non-creditable surfaces](https://github.com/computerlovetech/ralphify/blob/3734146c6bb8e97b97e6e26c473d44eabd2b67f7/docs/contributing/codebase-map.md)
- [Loop definitions: execute tasks](https://github.com/computerlovetech/ralphify/blob/3734146c6bb8e97b97e6e26c473d44eabd2b67f7/ralphs/execute-tasks/RALPH.md)

## Operational model

A human authors the loop objective and configures an external model agent binary. Each iteration a deterministic Python engine reads the current task/test information and assembles a new prompt; the invoked agent makes task-specific code/tool choices and can affect files or commits. The next fresh subprocess sees the new project state through configured commands and files. Runtime flags, pause/stop, metrics, logs and concurrent RunManager controls are caller/constructor machinery; they do not change who owns the actual task action or create a multi-unit metasystem.

## S1 — Operations

- State: A
- Function: agent-driven iterative task execution within the user-selected project environment, with current external command observations on every loop turn.
- Disturbance / variety regulated: newly discovered code defects, test failures, changing task lists, tool feedback and context-window limits.
- Decisive decision or feedback right: choose task-specific next code/tool action after reading the freshly assembled prompt and live project state.
- Decision owner: configured external model-based CLI agent (Claude, Codex, Pi or equivalent) actually invoked by `_run_agent_phase`; Ralphify supplies the repeat/observation wrapper.
- Supporting / enforcement mechanisms: `RALPH.md` prompt and command definitions, `execute_agent`, subprocess timeouts, resolver, RunState stop-on-error/max-iteration and event/log emitters.
- Closure path: current observation commands → interpolated prompt → agent CLI chooses/executes task action → changed files/test outcomes → next observation commands and fresh model prompt.
- Boundary reachability: the documented normal `ralph run` mode requires/configures an agent binary and executes it from the shipped engine; the loop commands and prompt refresh are first-party and reachable.
- Why this is / is not agent-owned: the agent subprocess chooses substantive work; the Python wrapper only determines when to invoke it and how to supply observations.
- Evidence: README, engine.py `_run_iteration`/`_run_agent_phase`, _agent.py and example RALPH.md definitions.
- Basis: structural first-party invocation/feedback path with explicit external-agent dependency.
- Confidence: high for supported assembled mode, no task success measurement.
- Caveats: without an installed configured agent CLI this is only a deterministic runner; not every user prompt produces a viable autonomous agent.

## S2 — Coordination

- State: —
- Function: the core product repeats one work cell; optional RunManager runs independent loops but supplies no conflict-aware relationship among their S1 decisions.
- Disturbance / variety regulated: potential concurrent edits or resource collisions between independently launched Ralph loops.
- Decisive decision or feedback right: resolve a concrete inter-S1 interference and feed the negotiated/serialized result into later distinct S1 behavior.
- Decision owner: no first-party S2 owner established; the operator must avoid colliding concurrent loops or provide coordination in their custom agents/scripts.
- Supporting / enforcement mechanisms: RunManager thread-safe registry lock, unique run IDs and per-run pause/stop/status handles.
- Closure path: `RunManager` prevents duplicate start of the same registered run and records each run separately, but does not coordinate conflicts between different launched agents.
- Why this is / is not agent-owned: process registry locking is implementation safety, not an inter-agent oscillation regulator.
- Evidence: manager.py, engine.py, docs/contributing/codebase-map.md.
- Basis: inspected independent-run boundaries and absence of cross-run conflict policy.
- Confidence: high for the shipped runner and manager.
- Caveats: a user could add file locks or agent messaging in `RALPH.md`, outside credited standard operation.

### Absence scope

- Surfaces inspected: core engine iteration, RunManager concurrency methods, event emitter, CLI controls, loop definitions and helper skills.
- Plausible first-party paths checked: concurrent loop registry as S2, prompt/command sharing as S2, pause/resume as coordination, independent worktree discipline.
- Why no material first-party path remains: no implemented inter-S1 disturbance recognition, arbitration and corrective return exists across different loop agents; one-at-a-time iterations are not distinct coordinated S1s.

## S3 — Inside-and-now control

- State: —
- Function: whole-system current management of multiple operational units' resources, commitments, priorities or constraints.
- Disturbance / variety regulated: competing work-loop goals, budget/capacity limits and failed obligations across agents.
- Decisive decision or feedback right: choose/revise a group-level current work plan or resource allocation based on a view of all S1 outcomes.
- Decision owner: the human or external application decides which loops to launch/pause/stop; no model/constructor/first-party parent S3 current judgment path is included.
- Supporting / enforcement mechanisms: RunManager `list_runs/get_run`, stop/pause flags, max iterations, timeout and failure counters.
- Closure path: calls to individual run controls affect local loops; no shipped aggregate supervisor consumes multi-loop results and decides collective corrective commitments.
- Why this is / is not agent-owned: counters and start/stop methods expose a control interface but do not exercise whole-system management discretion.
- Evidence: manager.py, _run_types.py, engine.py and CLI run options.
- Basis: current-control path tracing across managed runs.
- Confidence: high for reviewed standard modes.
- Caveats: a separate control-plane application could use RunManager as construction support, not part of the assessed first-party mode.

### Absence scope

- Surfaces inspected: RunManager, CLI flags, loop outcome events and per-run RunState.
- Plausible first-party paths checked: manager class as S3, max iteration/error stop as current regulation, user pause as parent S3.
- Why no material first-party path remains: those are external commands and fixed local thresholds with no whole-system current view plus responsible organization-level discretionary return.

## S3* — Complementary audit

- State: —
- Function: independent and complementary challenge to routine operational reports.
- Disturbance / variety regulated: agent falsely claiming completion, hidden regressions and untrustworthy test output.
- Decisive decision or feedback right: distinct auditor examines operational reality and challenges an ordinary success account with findings returned to current control.
- Decision owner: no independent first-party audit actor; test commands and agent stdout/stderr share the same ordinary task-feedback loop.
- Supporting / enforcement mechanisms: command output capture, events, logs, exit codes and optional user-authored tests.
- Closure path: tests may inform the *same next S1 prompt*; no independently governed complementary access and S3 control response is shipped.
- Why this is / is not agent-owned: normal test commands and logs are useful quality feedback, not independent S3* judgment.
- Evidence: engine.py command and agent phases; _runner.py, _events.py, manager.py.
- Basis: independence and separate-access test.
- Confidence: high for inspected product.
- Caveats: a custom RALPH.md may call external auditors, uncredited without specific shipped integration.

### Absence scope

- Surfaces inspected: configured commands, agent output/logs, emitter, example test loops and RunManager.
- Plausible first-party paths checked: command validation as S3*, stdout trace as independent audit, fresh context as independent reviewer.
- Why no material first-party path remains: observations come from the ordinary loop/task path, without separate auditor control, complementary access and a corrective challenge channel to S3.

## S4 — Outside-and-then intelligence

- State: —
- Function: model external future change into strategic options that alter the current operational capability.
- Disturbance / variety regulated: emerging tool choices, changing project ecosystem and long-horizon environment.
- Decisive decision or feedback right: generate prospective adaptations with a return path to whole-system present control.
- Decision owner: no shipped S4 owner; the user may rewrite the next prompt/agent command and the model may plan its local task.
- Supporting / enforcement mechanisms: re-reading `RALPH.md`, live command interpolation, context refresh and user-adjusted loop configuration.
- Closure path: external prompt edits take effect next iteration, but no first-party prospective environment model forms a governing adaptation option and returns it to S3.
- Why this is / is not agent-owned: fresh-context local task planning and repeat adaptation to test failures is S1, not outside-and-then intelligence.
- Evidence: README, engine.py prompt reload and _resolver.py.
- Basis: task-local vs prospective adaptation boundary.
- Confidence: high.
- Caveats: a user can *write* an S4-focused prompt or install an outside planner; neither is automatically a shipped Ralphify S4 unit.

### Absence scope

- Surfaces inspected: prompt template, command/iteration engine, example loops, manager and bundled contributor/helper skills.
- Plausible first-party paths checked: repeat feedback as learning, user-editable prompt as S4, loop engineering/research notes as prospective agent intelligence.
- Why no material first-party path remains: no first-party separate future-environment scan/options process and present-capability return is wired into the runtime.

## S5 — Policy and identity

- State: —
- Function: legitimate ultimate policy and identity closure for an organization of agent loops.
- Disturbance / variety regulated: changes of goal, unsafe operations, unresolved current-versus-future policy tensions.
- Decisive decision or feedback right: adjudicate a real identity or constitutional rule dispute and return binding direction to operation.
- Decision owner: human author of `RALPH.md` and agent permissions remains the external principal; no first-party S5 decision path or positive parent `P` return is established.
- Supporting / enforcement mechanisms: configured agent command/permissions, editable prompt, max iterations, stop-on-error and operator interrupt.
- Closure path: edits or operator stop affect next iteration, but an ordinary task change or safety command is not a routed identity-policy case.
- Why this is / is not agent-owned: user-authored prompt and a permissive sample CLI flag set bounds; they do not grant legitimate model policy sovereignty.
- Evidence: README configuration and editing guidance, engine.py, cli.py.
- Basis: operator control versus identity-level function test.
- Confidence: high.
- Caveats: the operator's wider organization may close S5 outside this product, not counted here.

### Absence scope

- Surfaces inspected: loop configuration, CLI options, pause/stop, sample ralph definitions and runner/research materials.
- Plausible first-party paths checked: human prompt edits as S5=P, static safety/stop limits as ultimate policy, Cowork setup as identity governance.
- Why no material first-party path remains: no shipped identity disturbance escalation, legitimate adjudicator and returned policy-to-operation closure beyond ordinary prompt editing.

## Recursion

The durable loop is one S1 whose agent process can restart with fresh context. Several independent `RunManager` threads are parallel runs, not evidence of recursive viable units or a shared agent metasystem.

## Variety and escalation

The user-specified command probes attenuate project-state complexity before model inference and allow fresh error feedback. Timeouts, stop-on-error, pause/resume and operator edits constrain or interrupt the loop. No supplied independent coordination, current-control, audit, external-prospective or ultimate-policy decision rights are inferred from those support mechanisms.

## Evidence gaps

- Source-first inspection at exact pinned revision; no live Claude/Codex/Pi provider call, paid E2E loop, real code mutation or production deployment was performed.
- No guarantee that arbitrary `RALPH.md` scripts or external agent CLIs are safe, non-destructive or effective.
- Research chapters and maintainer helper skills were inspected as adjacent materials; their prescriptions do not create shipped runtime S2–S5 ownership.
