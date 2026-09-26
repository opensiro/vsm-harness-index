---
harness_id: agentharness-alexandrmotologa
project_name: AgentHarness
repository: https://github.com/alexandrmotologa/agent-harness
review_ref: 725ceee14b65bd95365e8e1c2394ac1b245e3b98
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# AgentHarness

## Review boundary

- System in focus: one installed `alexandrmotologa/agent-harness` runtime at pinned revision `725ceee14b65bd95365e8e1c2394ac1b245e3b98`, including its autonomous model/tool loop, sandbox execution, guardrails/HITL, immutable decision DAG, checkpoints, time-travel debugger, persisted run records and shipped CLI/TUI/Web inspection surfaces.
- Purpose and identity: execute a user goal through a sandboxed autonomous agent while preserving deterministic host-side execution evidence and exposing inspection/rewind tooling for debugging and auditability.
- Relevant environment: user goals, workspace/filesystem state, configured model provider, sandbox command/tool outcomes, operator approvals in interactive mode, persisted run DAGs and prior checkpoints.
- Standard-distribution boundary: the packaged Python CLI/runtime and shipped inspection/debugging surfaces at the frozen ref. External model providers are inference dependencies. Repository tests/CI and evaluation suites can corroborate product behavior but are not borrowed as autonomous organizational owners for ordinary runs.
- Credited operating / distribution surfaces: `core/loop.py`, tool registry, sandbox implementations, guardrails/HITL, decision DAG/checkpoint machinery, `engine/debugger.py`, CLI `run`/`inspect`/`rewind`, Web Studio DAG/rewind endpoints and persisted run storage.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests, standalone eval-suite development/testing use, report-generation artifacts as passive exports, documentation claims not implemented by frozen runtime, and any downstream custom provider/tool composition not present in the standard distribution.
- First-party operating / deployment modes considered: ordinary autonomous CLI run; interactive HITL approval mode; persisted inspection; CLI/Web rewind-and-branch debugging; TUI read-only inspection; sandbox variants (process/WASM/container); cassette replay as a deterministic testing/debugging mode.
- Recursion level: one AgentHarness run. The frozen repository exposes one model-driven operational loop per run; no separate first-party worker/subagent organization is established merely by repository `multi-agent` naming/topics.
- Reviewed revision: `725ceee14b65bd95365e8e1c2394ac1b245e3b98`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

`AutonomousLoop` is the operating core. It sends the current conversation and tool definitions to the configured provider, records model thoughts/tool calls in a host-managed DAG, executes requested tools through the sandbox/tool registry, records the resulting observations/checkpoints and feeds tool output back into later model turns. Budget and repeated-call guards can stop execution; optional HITL can deny or modify an individual tool request before execution.

The decision graph is host-authored and content-addressed. Tool calls, observations, interventions and final answers become typed nodes whose hashes derive from parent hashes plus canonical payload. When the sandbox exposes a filesystem jail, the runtime also captures workspace checkpoints after tool execution.

The separate time-travel debugger can select a prior DAG node, restore its checkpoint, create an intervention/branch node, inject a corrected instruction and continue a new `AutonomousLoop` branch. CLI/Web inspection surfaces expose recorded node types, payloads, tool observations, branches, token/cost state and the rewind action. The frozen TUI itself is read-only despite broader README shortcut claims; correction is wired through CLI/Web debugger surfaces.

No first-party subagent/worker/delegation runtime was found in the frozen tree or code search. Sandboxes, multiple persisted runs, provider adapters and DAG branches are not distinct simultaneously operating S1 units.

Primary evidence:

- [`src/agent_harness/core/loop.py`](https://github.com/alexandrmotologa/agent-harness/blob/725ceee14b65bd95365e8e1c2394ac1b245e3b98/src/agent_harness/core/loop.py) — model/tool feedback loop, host-side DAG recording, checkpoints, guardrails and HITL interception.
- [`src/agent_harness/graph/decision_dag.py`](https://github.com/alexandrmotologa/agent-harness/blob/725ceee14b65bd95365e8e1c2394ac1b245e3b98/src/agent_harness/graph/decision_dag.py) — typed immutable trajectory nodes and host-computed content hashes.
- [`src/agent_harness/graph/checkpoint.py`](https://github.com/alexandrmotologa/agent-harness/blob/725ceee14b65bd95365e8e1c2394ac1b245e3b98/src/agent_harness/graph/checkpoint.py) — host workspace snapshots/restoration.
- [`src/agent_harness/engine/debugger.py`](https://github.com/alexandrmotologa/agent-harness/blob/725ceee14b65bd95365e8e1c2394ac1b245e3b98/src/agent_harness/engine/debugger.py) — rewind, branch, corrected-instruction injection and resumed execution.
- [`src/agent_harness/cli.py`](https://github.com/alexandrmotologa/agent-harness/blob/725ceee14b65bd95365e8e1c2394ac1b245e3b98/src/agent_harness/cli.py) — shipped run/inspect/rewind/TUI/Web/eval entry points and run persistence.
- [`src/agent_harness/web/server.py`](https://github.com/alexandrmotologa/agent-harness/blob/725ceee14b65bd95365e8e1c2394ac1b245e3b98/src/agent_harness/web/server.py) — Web Studio DAG inspection and corrective rewind endpoint.
- [`src/agent_harness/tui/app.py`](https://github.com/alexandrmotologa/agent-harness/blob/725ceee14b65bd95365e8e1c2394ac1b245e3b98/src/agent_harness/tui/app.py) — frozen read-only trajectory/tool-observation inspection surface.
- [`docs/time-travel-debugger.md`](https://github.com/alexandrmotologa/agent-harness/blob/725ceee14b65bd95365e8e1c2394ac1b245e3b98/docs/time-travel-debugger.md) — intended causal debugging relation and checkpoint/branch workflow.
- [`README.md`](https://github.com/alexandrmotologa/agent-harness/blob/725ceee14b65bd95365e8e1c2394ac1b245e3b98/README.md) — supported product modes and runtime purpose.

## Operational model

The model is the S1 decision owner. It chooses task-specific tool calls and reacts to host-returned observations. The harness controls execution admission, sandboxing, cost/repetition limits, optional human interception and durable evidence recording, but those controls do not replace the model's substantive task judgment.

The debugger/inspection plane is complementary to ordinary model reporting: the final answer is not the only source of evidence about what occurred. Host-recorded tool calls, tool outputs, hashes and checkpoints can be inspected independently, and the shipped debugger can feed a finding back by restoring a prior operational state and launching a corrected branch. At this ref the product does not supply a separate autonomous auditor or independent verdict actor, so this is a constructor S3* path rather than autonomous S3*.

## S1 — Operations

- State: A
- Function: perform the user's goal through iterative model-selected sandboxed tool actions and feedback until completion or a bounded stop.
- Disturbance / variety regulated: heterogeneous user goals, changing workspace/process state, tool success/failure, model uncertainty, context pressure, operator denial/modification, repeated-call loops and budget limits.
- Decisive decision or feedback right: choose the next substantive tool/action and its task-specific arguments, then revise later action from returned tool observations.
- Decision owner: the configured active model agent.
- Supporting / enforcement mechanisms: `AutonomousLoop`, provider adapters, `ToolRegistry`, sandbox execution, context manager, budget/repetition guardrails, optional HITL, decision DAG and checkpoints.
- Closure path: user goal/context → model selects a tool/action → host validates/intercepts/executes → observation is recorded and appended to context → later model turn changes or continues operation → final answer/finish or bounded stop.
- Boundary reachability: `agent-harness run` directly constructs and executes `AutonomousLoop` in the shipped CLI using the selected standard provider/sandbox; no development-only composition is required.
- Why this is / is not agent-owned: deterministic sandbox/guardrail/HITL machinery constrains or may veto an attempted action, but removing the model removes the task-specific choice of what substantive action to attempt next and how to respond to its result.
- Evidence: `core/loop.py`, `cli.py`, provider and tool registry code.
- Basis: explicit + structural
- Confidence: high
- Caveats: interactive human approval can modify individual tool arguments, but that does not displace the model as ordinary S1 owner or create a parent publication state for S1.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function is established at the assessed run boundary.
- Disturbance / variety regulated: no concrete interference/conflict/oscillation among two or more distinct concurrently operating S1 units is established.
- Decisive decision or feedback right: none established for inter-S1 attenuation.
- Decision owner: none established.
- Supporting / enforcement mechanisms: single-loop tool sequencing, sandboxes, DAG branches, persisted runs and provider adapters.
- Closure path: no S2-specific multi-S1 feedback loop identified.
- Why this is / is not agent-owned: multiple tools, providers, DAG branches or saved runs are not independent concurrent operations requiring coordination; code search at the frozen ref exposes no first-party worker/subagent/delegation runtime.
- Evidence: frozen repository tree, `core/loop.py`, `cli.py`, `decision_dag.py`.
- Basis: scoped absence
- Confidence: high
- Caveats: repository metadata uses `multi-agent` language, but function is classified from implemented relationships, not vocabulary.

### Absence scope

- Surfaces inspected: full frozen tree, README/architecture/debugger docs, runtime loop, CLI, DAG/debugger, sandboxes, MCP, TUI/Web, tests/eval structure and repository code search for subagent/worker/spawn/delegation paths.
- Plausible first-party paths checked: DAG branches as multiple S1s; multiple saved runs; sandbox processes/containers; MCP clients/servers; evaluation cases; repository `multi-agent` naming/topics.
- Why no material first-party path remains: these surfaces sequence or inspect one model-driven run or represent separate historical/test executions; no shipped relation among distinct current S1 units regulates a specific inter-S1 disturbance.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-system inside-and-now control loop is established above the single operational agent.
- Disturbance / variety regulated: budget, repetition, tool approval and rewind controls regulate one run/trajectory, not a portfolio of current operational units/commitments.
- Decisive decision or feedback right: no whole-system resource/commitment/priority intervention right established at the assessed recursion.
- Decision owner: none established for S3.
- Supporting / enforcement mechanisms: cost/step/repetition guardrails, HITL, run inspection, checkpoint rewind and branch execution.
- Closure path: individual action/run state can be constrained or corrected, but no whole-system current view plus metasystemic control relation closes.
- Why this is / is not agent-owned: a debugger, budget circuit breaker or human tool approval does not become S3 merely because it can interrupt or redirect one S1 trajectory.
- Evidence: `core/loop.py`, `engine/debugger.py`, `cli.py`, Web Studio.
- Basis: scoped absence
- Confidence: high
- Caveats: time-travel control is important recovery behavior, but function-first mapping keeps it at S1 correction/S3* feedback rather than promoting it to S3.

### Absence scope

- Surfaces inspected: runtime loop, guardrails, HITL, run storage, inspection UI, debugger/rewind, eval runner and sandbox lifecycle.
- Plausible first-party paths checked: budget controller as resource management; TUI/Web as whole-system view; rewind/branch as intervention; user approval as parent S3.
- Why no material first-party path remains: every current-control candidate is scoped to one operational run/action and lacks a whole-system view plus authority over distinct current commitments/resources at the declared recursion.

## S3* — Complementary audit

- State: C
- Function: provide a first-party complementary evidence-and-correction path for checking an agent run against host-recorded execution reality rather than relying only on the model's final narrative.
- Disturbance / variety regulated: an agent can reach an incorrect conclusion or mischaracterize what happened after earlier faulty assumptions/tool actions; relying only on its final answer would hide the causal execution record.
- Decisive decision or feedback right: inspect host-recorded tool calls/observations/checkpoints and select a prior point for corrective branch execution with a changed instruction.
- Decision owner: the standard distribution supplies the audit evidence and corrective primitive, but no autonomous independent auditor owns the judgment/verdict at this ref; an operator/developer must interpret the evidence or a downstream composition must supply an auditor, so the state is Constructor rather than Autonomous.
- Supporting / enforcement mechanisms: typed content-addressed DAG, host-captured observation nodes, filesystem checkpoints, persisted run files, CLI/TUI/Web inspectors, branch comparison and `TimeTravelDebugger` rewind.
- Closure path: model executes and reports → host independently preserves tool/effect trajectory → inspector exposes the evidence → a finding can select a prior checkpoint and corrected instruction → debugger restores state and starts a new branch → subsequent S1 behavior changes. Autonomous audit judgment remains uncomposed.
- Boundary reachability: inspection and rewind are installed CLI/Web product commands/endpoints over the same persisted run DAG produced by standard `AutonomousLoop`; the constructor path does not rely on CI/tests.
- Why this is / is not agent-owned: evidence capture is host-owned and independent of the model's final self-report, but the product has no separate audit agent or autonomous verdict step. The first-party function-specific path is therefore usable for S3* composition without establishing `A`.
- Evidence: `core/loop.py`, `decision_dag.py`, `checkpoint.py`, `engine/debugger.py`, `cli.py`, `web/server.py`.
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: the frozen CLI/Web rewind helper constructs a mock provider for resumed debugging, reinforcing that the shipped path is a debugging/audit constructor rather than a general autonomous production auditor. The frozen TUI is inspect-only.
- Claim being audited: that the run's final conclusion/result is supported by the actual sequence of model-requested actions and host-observed tool effects.
- Ordinary reporting path: the active model's assistant/final-answer content produced inside the normal loop.
- Complementary access path: host-persisted typed tool-call and observation nodes, content hashes and filesystem checkpoint metadata exposed independently through inspection surfaces.
- Independence boundary: the harness records tool observations/checkpoints outside the model and computes graph hashes host-side; the final model answer is not accepted as proof of those effects.
- Who acts on findings: an operator/developer may invoke shipped rewind with a corrected instruction; an autonomous auditor is not supplied at the frozen ref.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective organizational adaptation loop is established.
- Disturbance / variety regulated: current-run errors can be replayed/rewound and eval suites can measure scenarios, but no path converts external/future distinctions into persistent live capability change for subsequent ordinary runs.
- Decisive decision or feedback right: none established for prospective capability adaptation.
- Decision owner: none established.
- Supporting / enforcement mechanisms: rewind/branch debugging, cassette replay, standalone eval suites, provider/model configuration and context management.
- Closure path: current-run correction and offline evaluation do not return a generated adaptation into the standard future capability set.
- Why this is / is not agent-owned: changing a branch instruction or replaying a historical trajectory repairs/tests execution; it does not constitute an outside-and-then loop that modifies the organization's reusable future capability.
- Evidence: `engine/debugger.py`, `eval/runner.py`, `cli.py`, README/docs.
- Basis: scoped absence
- Confidence: high
- Caveats: developers can manually change code/config after inspection, but repository maintainership is adjacent to the assessed runtime and is not borrowed as S4 closure.

### Absence scope

- Surfaces inspected: debugger/rewind, cassette recorder/replay, eval package/CLI, provider/configuration surfaces, context manager, reports and repository development tooling.
- Plausible first-party paths checked: branch comparison as learning; eval suites as adaptation; replay as policy improvement; manual developer changes after audit.
- Why no material first-party path remains: none of these first-party runtime surfaces generates and activates a persistent prospective capability change into later standard runs.

## S5 — Policy and identity

- State: —
- Function: no material runtime identity/ultimate-policy closure is established.
- Disturbance / variety regulated: static system prompt, sandbox rules, budgets and approval policy constrain operation but do not decide/revise the organization's identity or highest-level policy through a closed authority loop.
- Decisive decision or feedback right: none established for identity/ultimate-policy choice at runtime.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: fixed `SYSTEM_PROMPT`, `HarnessConfig`, sandbox configuration, guardrails, HITL approval policy and user goal.
- Closure path: configuration is loaded/applied to operation; no identity/policy issue is elevated to a legitimate authority and returned as an authoritative changed constitution for subsequent operation.
- Why this is / is not agent-owned: a prompt, safety policy or per-tool human approval constrains execution without becoming S5; the model cannot revise its ultimate identity/policy and no first-party parent S5 loop is supplied.
- Evidence: `core/loop.py`, `config.py`, `core/hitl.py`, `core/guardrails.py`.
- Basis: scoped absence
- Confidence: high
- Caveats: the user defines a task goal, but task specification is not organizational identity closure.

### Absence scope

- Surfaces inspected: system prompt, configuration, guardrails, HITL policy, sandbox policy, CLI options, debugger interventions, MCP and repository governance/development surfaces.
- Plausible first-party paths checked: system prompt as identity; HITL as parent S5; sandbox/budget policy as ultimate policy; developer edits as governance closure.
- Why no material first-party path remains: all inspected controls are static/developer configuration, action-scoped approval or current-task correction; no runtime identity/ultimate-policy issue→authority→returned policy loop exists at the assessed boundary.

## Recursion

No positive recursive viable-system claim is made. A DAG branch is an alternate trajectory of the same run, not a nested organization. Separate saved runs and sandbox processes likewise do not establish VSM recursion.

## Variety and escalation

Operational variety is attenuated by tool schemas, sandbox confinement, context pruning, repeated-call detection, cost/step caps and optional human action approval. Errors or suspicious actions may stop or reach the operator; post-run findings can also be escalated through inspection and rewind. These are recorded by function rather than treated as additional S-functions.

## Evidence gaps

- Repository description/topics say `multi-agent`, but the frozen implementation exposes no first-party subagent/worker/delegation runtime; no S2/S3 credit is inferred from naming.
- README describes richer TUI rewind/diff shortcuts than frozen `tui/app.py` implements. Assessment credits CLI/Web rewind and TUI inspection only where code establishes them.
- Cross-branch `file_diff` is declared in `BranchComparison` but frozen `compare_branches()` does not populate it; S3* credit does not rely on an implemented automatic file-diff verdict.
- The rewind helper uses a mock provider in the frozen CLI/Web paths; this limits the strength of the audit-correction path and is why no autonomous/general production S3* closure is claimed.
