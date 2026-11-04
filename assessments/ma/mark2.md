---
harness_id: mark2
project_name: mark2
repository: https://github.com/dream-x/mark2
review_ref: 535ffc4710e4583b5657dea94bc970d9d2c05bc3
reviewed_at: 2026-11-04
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

# mark2

## Review boundary

- System in focus: the first-party mark2 Rust library and CLI coding-agent distribution.
- Purpose and identity: transform a user's coding request into workspace inspection, edits, execution and a response using a local/OpenAI-compatible model.
- Relevant environment: user, workspace/files/processes, model server and finite context window.
- Standard-distribution boundary: core/providers/cli crates with shipped tools and supported interactive/print modes, including permission policies, session recording, context compaction and file memory.
- Credited operating / distribution surfaces: Agent::spawn and run_turn, ToolRegistry, CLI event/operation consumer and provider adapter.
- Adjacent first-party surfaces excluded from ownership: crates/bench, bench tasks/results, developer research plans, CI and unit/e2e evaluation machinery. Their checks are not product audit actors.
- First-party operating / deployment modes considered: interactive and headless print; Yolo, AskWrites and ReadOnly permissions; optional file memory and context compaction. Model servers supply inference, not an adjacent metasystem.
- Recursion level: one coding-agent session; tools and provider calls are subordinate mechanisms.
- Reviewed revision: `535ffc4710e4583b5657dea94bc970d9d2c05bc3`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI composes layered TOML configuration, a provider, tools, permissions and append-only JSONL sessions around an event-driven core. UserInput starts a turn; model tool-use messages trigger validated bash/read/grep/write/edit execution and tool results return to the next model call. The model can repair errors and choose a different next action. Max-turn, repeated-call and write-churn guards constrain that loop. Compaction summarizes agent-visible history while preserving the original session; optional file memory is loaded into the next session's prompt. No packaged subagent, scheduler, MCP or independent evaluator is wired into this product revision. The separate bench crate measures models against tasks; it does not supervise the running coding agent. Evidence: [ARCHITECTURE.md](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/ARCHITECTURE.md); [crates/core/src/agent.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/agent.rs); [crates/cli/src/main.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/cli/src/main.rs); [crates/core/src/tools/mod.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/tools/mod.rs); [crates/core/src/session.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/session.rs).

## Operational model

One session is the S1 unit. The model owns task-local selection of tools, arguments, repairs and completion; humans select the goal and permission envelope, while runtime code transports/enforces their constraints. An approval request concerns a particular mutating action. It does not itself grant whole-system current-control or identity-policy closure.

## S1 — Operations

- State: A
- Function: coding work through a model-directed observation/action feedback loop.
- Disturbance / variety regulated: changing file contents, command results, malformed arguments and denied actions.
- Decisive decision or feedback right: choose the next workspace action or completion from returned observations.
- Decision owner: the model-backed agent in the first-party core.
- Supporting / enforcement mechanisms: Provider streaming, ToolRegistry validation/execution, PermissionPolicy, cancellation and SessionRecorder.
- Closure path: UserInput → model tool-use → permission/validation/execution → ToolResult in history → next model decision; no tool-use ends the turn.
- Boundary reachability: both shipped CLI modes construct the core Agent and consume its events; Yolo permits the standard tool loop, and supervised modes retain model action choice with human permission constraints.
- Why this is / is not agent-owned: removing the model leaves no actor choosing how to solve the task; remaining code only applies preselected guards and executes selected tools.
- Evidence: [crates/core/src/agent.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/agent.rs); [crates/core/src/tools/mod.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/tools/mod.rs); [crates/core/src/permission.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/permission.rs); [crates/cli/src/main.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/cli/src/main.rs).
- Basis: explicit and structural.
- Confidence: high.
- Caveats: source-level reachable ownership, not a new live-model success measurement or a claim that all tool effects are autonomous in AskWrites.

## S2 — Coordination

- State: —
- Function: no material first-party function-specific path established at this boundary.
- Disturbance / variety regulated: the nearest examined mechanisms concern one session serializes its own tool calls; no distinct shipped S1 cells interact.
- Decisive decision or feedback right: no qualifying function-level right is exposed by the examined distribution.
- Decision owner: no qualifying owner; task-local model choices and developer/user settings retain their narrower scope.
- Supporting / enforcement mechanisms: agent loop, sequential tools and library/CLI entry points.
- Closure path: no function-specific returned closure; ordinary coding feedback is already S1.
- Why this is / is not agent-owned: Sequential tools, repeated-call suppression and write-churn feedback stabilize one S1, not inter-unit interference. Running multiple independent processes is possible but no shipped cross-session coordination relation closes their conflicts.
- Evidence: [ARCHITECTURE.md](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/ARCHITECTURE.md); [crates/core/src/agent.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/agent.rs); [crates/core/src/tools/mod.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/tools/mod.rs).
- Basis: structural bounded absence after positive and eligible parent-mode checks.
- Confidence: high for the declared product boundary.
- Caveats: a custom external controller could add this function; that hypothetical extension is outside this assessment.

### Absence scope

- Surfaces inspected: ARCHITECTURE.md, crates/core/src/agent.rs, crates/core/src/tools/mod.rs, README and supported mode description.
- Plausible first-party paths checked: agent loop, sequential tools and library/CLI entry points.
- Why no material first-party path remains: Sequential tools, repeated-call suppression and write-churn feedback stabilize one S1, not inter-unit interference. Running multiple independent processes is possible but no shipped cross-session coordination relation closes their conflicts.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party function-specific path established at this boundary.
- Disturbance / variety regulated: the nearest examined mechanisms concern task/session execution guards rather than a whole-system commitment regulator.
- Decisive decision or feedback right: no qualifying function-level right is exposed by the examined distribution.
- Decision owner: no qualifying owner; task-local model choices and developer/user settings retain their narrower scope.
- Supporting / enforcement mechanisms: max_turns, cancellation, permission approval, context thresholds and CLI configuration.
- Closure path: no function-specific returned closure; ordinary coding feedback is already S1.
- Why this is / is not agent-owned: The examined controls enforce user/developer choices over one coding turn. Neither an autonomous current-control actor nor a parent-facing whole-system observation → commitment/resource decision → returned intervention mode is supplied. Generic library operations do not constitute an S3-specific constructor.
- Evidence: [crates/core/src/agent.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/agent.rs); [crates/core/src/permission.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/permission.rs); [crates/core/src/config.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/config.rs); [crates/cli/src/interactive.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/cli/src/interactive.rs).
- Basis: structural bounded absence after positive and eligible parent-mode checks.
- Confidence: high for the declared product boundary.
- Caveats: a custom external controller could add this function; that hypothetical extension is outside this assessment.

### Absence scope

- Surfaces inspected: crates/core/src/agent.rs, crates/core/src/permission.rs, crates/core/src/config.rs, crates/cli/src/interactive.rs, README and supported mode description.
- Plausible first-party paths checked: max_turns, cancellation, permission approval, context thresholds and CLI configuration.
- Why no material first-party path remains: The examined controls enforce user/developer choices over one coding turn. Neither an autonomous current-control actor nor a parent-facing whole-system observation → commitment/resource decision → returned intervention mode is supplied. Generic library operations do not constitute an S3-specific constructor.

## S3* — Complementary audit

- State: —
- Function: no material first-party function-specific path established at this boundary.
- Disturbance / variety regulated: the nearest examined mechanisms concern ordinary tool feedback and adjacent benchmark checking.
- Decisive decision or feedback right: no qualifying function-level right is exposed by the examined distribution.
- Decision owner: no qualifying owner; task-local model choices and developer/user settings retain their narrower scope.
- Supporting / enforcement mechanisms: SessionRecorder, ToolResult errors, write-churn nudges, unit/e2e tests and bench crate boundary.
- Closure path: no function-specific returned closure; ordinary coding feedback is already S1.
- Why this is / is not agent-owned: The model sees its ordinary execution feedback. No separate actor obtains complementary raw evidence to challenge an operational completion claim and return findings into control; the benchmark is outside the installed product loop.
- Evidence: [crates/core/src/session.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/session.rs); [crates/core/src/agent.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/agent.rs); [crates/bench/src/runner.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/bench/src/runner.rs); [ARCHITECTURE.md](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/ARCHITECTURE.md).
- Basis: structural bounded absence after positive and eligible parent-mode checks.
- Confidence: high for the declared product boundary.
- Caveats: a custom external controller could add this function; that hypothetical extension is outside this assessment.

### Absence scope

- Surfaces inspected: crates/core/src/session.rs, crates/core/src/agent.rs, crates/bench/src/runner.rs, ARCHITECTURE.md, README and supported mode description.
- Plausible first-party paths checked: SessionRecorder, ToolResult errors, write-churn nudges, unit/e2e tests and bench crate boundary.
- Why no material first-party path remains: The model sees its ordinary execution feedback. No separate actor obtains complementary raw evidence to challenge an operational completion claim and return findings into control; the benchmark is outside the installed product loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party function-specific path established at this boundary.
- Disturbance / variety regulated: the nearest examined mechanisms concern context retention and task-local repair.
- Decisive decision or feedback right: no qualifying function-level right is exposed by the examined distribution.
- Decision owner: no qualifying owner; task-local model choices and developer/user settings retain their narrower scope.
- Supporting / enforcement mechanisms: file-memory loading/writing, compaction, provider configuration and research/benchmark separation.
- Closure path: no function-specific returned closure; ordinary coding feedback is already S1.
- Why this is / is not agent-owned: Memory and summaries preserve operational context. Choosing the next coding action or a configured model is not prospective environment-facing adaptation of the harness. No supported autonomous or parent-governed external sensing → adaptation options → changed present capability loop is supplied.
- Evidence: [crates/core/src/memory.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/memory.rs); [crates/core/src/prompt.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/prompt.rs); [crates/core/src/compact.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/compact.rs); [crates/core/src/config.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/config.rs); [ARCHITECTURE.md](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/ARCHITECTURE.md).
- Basis: structural bounded absence after positive and eligible parent-mode checks.
- Confidence: high for the declared product boundary.
- Caveats: a custom external controller could add this function; that hypothetical extension is outside this assessment.

### Absence scope

- Surfaces inspected: crates/core/src/memory.rs, crates/core/src/prompt.rs, crates/core/src/compact.rs, crates/core/src/config.rs, ARCHITECTURE.md, README and supported mode description.
- Plausible first-party paths checked: file-memory loading/writing, compaction, provider configuration and research/benchmark separation.
- Why no material first-party path remains: Memory and summaries preserve operational context. Choosing the next coding action or a configured model is not prospective environment-facing adaptation of the harness. No supported autonomous or parent-governed external sensing → adaptation options → changed present capability loop is supplied.

## S5 — Policy and identity

- State: —
- Function: no material first-party function-specific path established at this boundary.
- Disturbance / variety regulated: the nearest examined mechanisms concern static prompt and permissions plus ordinary tool approval.
- Decisive decision or feedback right: no qualifying function-level right is exposed by the examined distribution.
- Decision owner: no qualifying owner; task-local model choices and developer/user settings retain their narrower scope.
- Supporting / enforcement mechanisms: project AGENTS.md loading, system prompt, Yolo/AskWrites/ReadOnly policies and Approve/Interrupt operations.
- Closure path: no function-specific returned closure; ordinary coding feedback is already S1.
- Why this is / is not agent-owned: The runtime applies preselected instructions and individual action decisions; it supplies no identity/ultimate-policy issue submission and authoritative returned decision governing later operation. File editability and ordinary source maintenance do not establish a packaged parent governance mode.
- Evidence: [crates/core/src/prompt.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/prompt.rs); [crates/core/src/permission.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/permission.rs); [crates/core/src/event.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/core/src/event.rs); [crates/cli/src/interactive.rs](https://github.com/dream-x/mark2/blob/535ffc4710e4583b5657dea94bc970d9d2c05bc3/crates/cli/src/interactive.rs).
- Basis: structural bounded absence after positive and eligible parent-mode checks.
- Confidence: high for the declared product boundary.
- Caveats: a custom external controller could add this function; that hypothetical extension is outside this assessment.

### Absence scope

- Surfaces inspected: crates/core/src/prompt.rs, crates/core/src/permission.rs, crates/core/src/event.rs, crates/cli/src/interactive.rs, README and supported mode description.
- Plausible first-party paths checked: project AGENTS.md loading, system prompt, Yolo/AskWrites/ReadOnly policies and Approve/Interrupt operations.
- Why no material first-party path remains: The runtime applies preselected instructions and individual action decisions; it supplies no identity/ultimate-policy issue submission and authoritative returned decision governing later operation. File editability and ordinary source maintenance do not establish a packaged parent governance mode.

## Distributed OSS parent arrangement

Maintainers and users can revise source and project configuration. No organization-level S3/S4/S5 return loop is wired into the assessed CLI merely by that OSS arrangement; individual tool approval is not such governance.

## Self-hosted and non-human modes

Local model servers and Yolo/AskWrites/ReadOnly operation are inspected above. They change inference location or action constraints, without adding a function-specific parent or non-human metasystem.

## Recursion

No recursively viable child organization is evidenced. Provider, tool and crate boundaries are technical decomposition.

## Variety and escalation

Tool errors, permission denials, compaction, cancellation, turn caps and loop/write-churn signals return local disturbances or terminate the turn. The model can alter the next operational action; exceptional organizational escalation to a higher decisive authority is not implemented by those events alone.

## Evidence gaps

This is pinned-source analysis. No local-model inference, platform benchmark, production behavior or product-safety claim was independently measured. The inspected supported surfaces are sufficient for the bounded negative findings; future roadmap consumers are not credited as shipped modes.
