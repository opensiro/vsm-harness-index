---
harness_id: cire-harness
project_name: cire-harness
repository: https://github.com/fathdemr/cire-harness
review_ref: e9fa8adc673ea32783e84ad84769f57bac6ff3fa
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

# cire-harness

## Review boundary

- System in focus: one CLI/TUI coding session, including the supported optional executor delegate.
- Purpose and identity: carry out coding tasks using a strong conversational model and optionally cheaper file-editing executors.
- Relevant environment: user workspace, shell/file state, model providers, configured MCP servers and local context store.
- Standard-distribution boundary: src/cire_harness CLI, TUI, model/tool loop, context, tools/MCP and optional orchestration package at the pinned revision.
- Credited operating / distribution surfaces: run_agent, CLI/TUI wiring and executor delegation loop; provider adapters supply model responses to first-party control flow.
- Adjacent first-party surfaces excluded from ownership: repository contributor AGENTS, smoke/tests, development hooks and PLAN roadmap; none is a runtime audit or policy actor.
- First-party operating / deployment modes considered: one-shot run with approval or --yes; persistent chat/session resume with tool confirmation; configured planner/executor role models and MCP servers.
- Recursion level: one user coding objective; delegated executor episodes are subordinate S1 work, not independent organizations.
- Reviewed revision: e9fa8adc673ea32783e84ad84769f57bac6ff3fa
- Observation date: 2026-10-29
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The Python package exposes Typer CLI and Textual chat. run_agent appends model/tool messages and repeats until a final answer or fixed turn cap. SQLite persists sessions and large output recall; a model summary compacts old history. With an executor model configured, the planner receives delegate: a TaskSpec carries goal, files, constraints and acceptance commands. A fresh file-tool-only executor attempts the work; the runtime executes acceptance commands, checks touched paths and retries once from failure output. A short report returns to the planner. Config maps provider roles and MCP trust; no separate adaptive organization is supplied.

## Operational model

Planner and executor are model-owned operational decisions inside one first-party objective/tool/result loop. Acceptance commands are specified by the planner and enforced deterministically by the same delegation path. Human confirmation selects permission for a tool, not a higher-function parent judgment.

## S1 — Operations

- State: A
- Function: produce coding/file outcomes from user tasks and executor specifications.
- Disturbance / variety regulated: unknown repository state, failing commands and incomplete edits.
- Decisive decision or feedback right: select tools/edits, interpret returned results and choose next action or completion.
- Decision owner: model-backed planner and optional executor actors.
- Supporting / enforcement mechanisms: Python run loop, tool registry, permission callback, context store, provider adapters and deterministic acceptance/retry.
- Closure path: run_agent appends tool results to model history; executor failures create a new repair prompt and Report returns observations to planner.
- Boundary reachability: CLI run and TUI ask call the shipped loop; configuring executor directly registers delegate_tool, which calls the same loop with first-party task/role messages.
- Why this is / is not agent-owned: model selects task-specific actions; removing it leaves generic validation/dispatch, not the operational decisions.
- Evidence: [src/cire_harness/loop/loop.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/loop/loop.py); [src/cire_harness/cli.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/cli.py); [src/cire_harness/orchestration/executor.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/orchestration/executor.py); [src/cire_harness/tui/app.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/tui/app.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

## S2 — Coordination

- State: —
- Function: No supplied coordination among distinct operational units path at this boundary.
- Disturbance / variety regulated: competing independent writers or oscillating inter-unit commitments.
- Decisive decision or feedback right: No function-specific decisive right established.
- Decision owner: none established; operational model/developer/user rights are not reassigned.
- Supporting / enforcement mechanisms: planner/executor delegation, sequential tool dispatch, TaskSpec file constraints and executor touched tracking.
- Closure path: No qualifying closure; synchronous delegate/report and one retry are S1/configuration mechanisms.
- Why this is / is not agent-owned: Positive and parent alternatives were checked first; function-first evidence does not justify agent/constructor/parent ownership.
- Evidence: [src/cire_harness/orchestration/executor.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/orchestration/executor.py); [src/cire_harness/orchestration/spec.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/orchestration/spec.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: planner/executor delegation, sequential tool dispatch, TaskSpec file constraints and executor touched tracking.
- Plausible first-party paths checked: synchronous delegate/report and one retry.
- Why no material first-party path remains: The supplied delegate follows the planner's one objective synchronously. File allowlists test a subordinate's scope after execution, not inter-S1 interference; no collision-specific coordinating relation or mutual feedback is supplied.

## S3 — Inside-and-now control

- State: —
- Function: No supplied whole-system current resource/commitment control path at this boundary.
- Disturbance / variety regulated: shared-resource or cross-cell commitment pressure.
- Decisive decision or feedback right: No function-specific decisive right established.
- Decision owner: none established; operational model/developer/user rights are not reassigned.
- Supporting / enforcement mechanisms: planner role, executor model config, token stats, max turns, permission callbacks and TUI stop.
- Closure path: No qualifying closure; delegation/model choice, acceptance checks and cancellation are S1/configuration mechanisms.
- Why this is / is not agent-owned: Positive and parent alternatives were checked first; function-first evidence does not justify agent/constructor/parent ownership.
- Evidence: [src/cire_harness/cli.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/cli.py); [src/cire_harness/tui/app.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/tui/app.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: planner role, executor model config, token stats, max turns, permission callbacks and TUI stop.
- Plausible first-party paths checked: delegation/model choice, acceptance checks and cancellation.
- Why no material first-party path remains: These regulate one coding task and developer-selected caps. No current whole-system operational portfolio/control authority or function-specific parent resource-return loop is supplied; naming the model planner does not establish it.

## S3* — Complementary audit

- State: —
- Function: No supplied complementary independent audit path at this boundary.
- Disturbance / variety regulated: unreliable operational claims outside routine completion checks.
- Decisive decision or feedback right: No function-specific decisive right established.
- Decision owner: none established; operational model/developer/user rights are not reassigned.
- Supporting / enforcement mechanisms: executor verification/report, source allowlist, acceptance commands, CLI/TUI reporting and repository tests.
- Closure path: No qualifying closure; runtime-run acceptance commands and planner verification of delegated output are S1/configuration mechanisms.
- Why this is / is not agent-owned: Positive and parent alternatives were checked first; function-first evidence does not justify agent/constructor/parent ownership.
- Evidence: [src/cire_harness/orchestration/verify.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/orchestration/verify.py); [src/cire_harness/orchestration/delegate.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/orchestration/delegate.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: executor verification/report, source allowlist, acceptance commands, CLI/TUI reporting and repository tests.
- Plausible first-party paths checked: runtime-run acceptance commands and planner verification of delegated output.
- Why no material first-party path remains: The planner supplies the acceptance commands, the deterministic gate is mandatory in the same production path and feedback returns for routine repair. No independent complementary audit judgment/access-control arrangement is supplied; lack of executor shell authority is not sufficient independence.

## S4 — Outside-and-then intelligence

- State: —
- Function: No supplied outside-and-then capability adaptation path at this boundary.
- Disturbance / variety regulated: future environment changes requiring adaptation options.
- Decisive decision or feedback right: No function-specific decisive right established.
- Decision owner: none established; operational model/developer/user rights are not reassigned.
- Supporting / enforcement mechanisms: context store/recall, compactor, model roles, CLI configuration and development roadmap.
- Closure path: No qualifying closure; conversation summary, per-session /model and executor selection are S1/configuration mechanisms.
- Why this is / is not agent-owned: Positive and parent alternatives were checked first; function-first evidence does not justify agent/constructor/parent ownership.
- Evidence: [src/cire_harness/context/compactor.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/context/compactor.py); [src/cire_harness/config.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/config.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: context store/recall, compactor, model roles, CLI configuration and development roadmap.
- Plausible first-party paths checked: conversation summary, per-session /model and executor selection.
- Why no material first-party path remains: These retain task context or execute already-chosen configuration. No external prospective distinctions, option development and return into a current-capability regulator are shipped, including in an owner-governed mode.

## S5 — Policy and identity

- State: —
- Function: No supplied runtime identity/ultimate-policy adjudication path at this boundary.
- Disturbance / variety regulated: unresolved ultimate-purpose/policy tensions.
- Decisive decision or feedback right: No function-specific decisive right established.
- Decision owner: none established; operational model/developer/user rights are not reassigned.
- Supporting / enforcement mechanisms: executor SYSTEM/TaskSpec, provider and MCP trust config, CLI/TUI approval, contributor guidance.
- Closure path: No qualifying closure; tool confirmation, --yes/trusted overrides, goal/file constraints and config changes are S1/configuration mechanisms.
- Why this is / is not agent-owned: Positive and parent alternatives were checked first; function-first evidence does not justify agent/constructor/parent ownership.
- Evidence: [src/cire_harness/config.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/config.py); [src/cire_harness/tui/app.py](https://github.com/fathdemr/cire-harness/blob/e9fa8adc673ea32783e84ad84769f57bac6ff3fa/src/cire_harness/tui/app.py)
- Basis: structural
- Confidence: medium-high
- Caveats: Source-relative ownership/reachability finding; no live model or effectiveness test.

### Absence scope

- Surfaces inspected: executor SYSTEM/TaskSpec, provider and MCP trust config, CLI/TUI approval, contributor guidance.
- Plausible first-party paths checked: tool confirmation, --yes/trusted overrides, goal/file constraints and config changes.
- Why no material first-party path remains: These express task authorization and static restrictions. No identity-policy matter reaches legitimate ultimate authority and returns a governing settlement; developer/contributor rules belong to adjacent development.

## Distributed OSS parent arrangement

No parent-governed S3/S4/S5 function is established. Maintainer governance and ordinary tool approvals remain separate from the assessed session.

## Self-hosted and non-human modes

Local provider/Ollama and remote provider adapters are supported. Self-hosting changes inference location, not organizational ownership; no autonomous non-human metasystem is inferred.

## Recursion

TaskSpec delegation is task decomposition. No child local environment/identity/metasystem sufficient to establish VSM recursion is shown.

## Variety and escalation

Tools return failures into the next model turn; executor verification retries return concrete failure output. Store masking/recall and compaction manage context size. Turn caps, tool approvals, timeout and provider configuration constrain local execution without deciding whole-system commitments.

## Evidence gaps

No live model task or quality benchmark was run. External MCP internals and provider behavior lie outside first-party evidence. Acceptance may be empty and the file-set check occurs after writes; this limits guarantees but does not remove the demonstrated S1 action/feedback ownership. The reviewed compact runtime supplies no concrete unresolved higher-function path requiring ?. No third-party runtime conclusions were borrowed.
