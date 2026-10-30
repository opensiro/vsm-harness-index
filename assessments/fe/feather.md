---
harness_id: feather
project_name: Feather
repository: https://github.com/paper-instruments/feather-train
review_ref: cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Feather

## Review boundary

- System in focus: the independently installable Feather Harness production (`prod`) local agent runtime, including its optional first-party single-level subagents.
- Purpose and identity: complete user-directed knowledge-work tasks in a local workspace with a model-driven tool loop and supported document/file/process skills.
- Relevant environment: user-supplied files and task instructions, shell and filesystem outcomes, optional MCP/web providers, model responses and context limits.
- Standard-distribution boundary: `feather-harness` local CLI and Python runtime with the `prod` profile; the separate `train` profile is compared but not used to donate production control.
- Credited operating / distribution surfaces: `cli.py`, `local/__init__.py`, `core/runner.py`, `core/compaction.py`, `tools/*`, `subagents.py`, production instructions and bundled skills.
- Adjacent first-party surfaces excluded from ownership: `feather-train` rollouts/Tinker/verifiers, `feather-eval`/Harbor grading, repository tests, CI, installer/release workflow and Paper package development. These do not execute as production S3*/S4 within this boundary.
- First-party operating / deployment modes considered: default `prod` single agent, optional `prod` subagents with parent-owned lifetime, minimal `train` profile, optional MCP/web and image tools, local user/operator configuration.
- Recursion level: one local user-task execution with a parent agent and, optionally, bounded operational child agents; not the Paper organization or external provider.
- Reviewed revision: `cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`run_local` assembles a production system prompt, model, local file/shell tools, todo state, optional MCP/web tools, compaction and optional child-agent lifecycle. `FeatherAgent._run_loop` repeatedly obtains model-selected tool calls, invokes tools, returns observations, and terminates on an answer, limit or failure. Tool execution and concurrency limits are deterministic support rather than ownership of the model's decisions. The optional parent agent has `spawn_agent`, `list_agents`, `wait_agent`, `followup_agent` and `stop_agent` tools; children have independent contexts and no further delegation. Child status/results return to the parent, which can reassign, follow up, or stop work. `TodoList` is session-local planning state; the compactor summarizes context with task state, not a future-facing adaptive policy. The training/evaluation packages are separate independently installable products.

## Operational model

The parent agent chooses task steps and tools from local observations. In subagent mode, children act on delegated portions of the task while the parent retains a current view of their reported status and chooses follow-up or cancellation within configured limits. A developer-selected concurrency cap is enforced without itself making those organizational judgments. Parallel child access to the same workspace is accompanied by prompt-level caution against colliding writes, but the shipped tools do not establish a specific inter-child reservation/conflict attenuation loop. Operator instructions, provider configuration and model limits remain external constraints rather than automatically credited policy ownership.

## S1 — Operations

- State: A
- Function: perform user-requested workspace work through agent-directed inspection, file edits, shell commands and document skills.
- Disturbance / variety regulated: heterogeneous user tasks, unknown file content, tool output, failures and iterative corrections.
- Decisive decision or feedback right: choose actions, tool arguments, follow-up inspections and final response based on observations.
- Decision owner: the model-driven Feather parent agent and, when enabled, delegated child agents for their local task scopes.
- Supporting / enforcement mechanisms: `FeatherAgent` loop, tool registry, file/process runtimes, model client, turn/token limits and transcript saving.
- Closure path: model-selected tool call → local execution → tool result in subsequent model context → new choice or completed response.
- Boundary reachability: the shipped CLI calls `run_local`, which constructs and invokes `FeatherAgent` with real file/process tools in the supported `prod` profile; no training-only evaluator is needed.
- Why this is / is not agent-owned: the model chooses work and correction steps; shell/filesystem transports execute those choices without selecting them.
- Evidence: [CLI](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/cli.py), [local composition](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/local/__init__.py), [agent loop](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/core/runner.py).
- Basis: structural.
- Confidence: high for shipped path, not measured task effectiveness.
- Caveats: no live model/provider-backed execution performed.

## S2 — Coordination

- State: —
- Function: no material first-party loop specifically attenuating interference between distinct operational child agents is established.
- Disturbance / variety regulated: parallel children can edit the same workspace or rely on one another's incomplete work, but supplied guidance is generic caution.
- Decisive decision or feedback right: no S2-specific autonomous collision arbitration/reservation decision identified; the parent receives reports and chooses task management.
- Decision owner: no separate inter-S1 coordination right established at this boundary.
- Supporting / enforcement mechanisms: child concurrency caps, queues, parent wait/follow-up tools, separate contexts and instructions not to write the same file concurrently.
- Closure path: task results return to the parent, but no evidence ties a specific collision witness to a first-party exclusion/negotiation response modifying subsequent child work.
- Why this is / is not agent-owned: dispatch, polling and generic warnings do not independently demonstrate the S2 function.
- Evidence: [subagent guidance and manager](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/subagents.py), [subagent tools](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/tools/agents.py), [local composition](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/local/__init__.py).
- Basis: structural.
- Confidence: medium-high within shipped local modes.
- Caveats: a user could design task-specific coordination using these primitives, but that hypothetical extension is outside this assessment.

### Absence scope

- Surfaces inspected: parent/child manager, guidance, agent tools, local tool assembly, current todo state and runner.
- Plausible first-party paths checked: concurrent child scheduling, same-file write caution, shared workspace, child status/follow-up, wait and stop.
- Why no material first-party path remains: the concrete shipped mechanisms enforce capacity or transport results, but do not implement a function-specific inter-child collision/oscillation witness with corrective feedback. This is bounded to the assessed standard distribution, not a universal impossibility claim.

## S3 — Inside-and-now control

- State: A
- Function: maintain current delegated task commitments and child resource participation under one parent agent.
- Disturbance / variety regulated: too many active children, stalled/failed work, incomplete delegated results and changing task priorities during the run.
- Decisive decision or feedback right: select which children to start, query, follow up or terminate and whether to revise task assignments from their reported outcomes.
- Decision owner: the parent model-driven agent when optional first-party subagents are enabled; `Subagents` enforces developer-selected lifetime/concurrency limits.
- Supporting / enforcement mechanisms: `list_agents`, `wait_agent`, `followup_agent`, `stop_agent`, child-status manifest, bounded task queue and configured caps.
- Closure path: parent observes child statuses/reports → chooses follow-up/cancellation/new delegation → manager enacts that choice → subsequent child operation or parent task plan changes.
- Boundary reachability: the CLI accepts `subagents` configuration in `prod`; `run_local` binds the live manager tools to the parent and returns child reports in the same local execution.
- Why this is / is not agent-owned: unlike a fixed scheduler, the parent selects the corrective/current commitment decision; manager constraints merely enforce it. Without the parent, status storage and caps do not choose a revised task strategy.
- Whole-system current view: the parent's own task state plus all currently managed child statuses, completion reports, failures and remaining turn budget for its task run.
- Current-control decision scope: child assignments, follow-ups, stops and bounded current work commitments within this one task; not developer-defined global resource policy.
- Evidence: [local agent wiring](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/local/__init__.py), [subagent lifecycle](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/subagents.py), [parent tools](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/tools/agents.py).
- Basis: structural.
- Confidence: medium; multi-agent mode optional and code supports parent current control, not an observed production coordination outcome.
- Caveats: task decomposition alone would not count; the positive mapping is limited to the parent's full current child-status and intervention loop.

## S3* — Complementary audit

- State: —
- Function: no complementary audit of operational claims independently reaches production current control.
- Disturbance / variety regulated: potential false task completion/tool claims; routine agent testing and separate evaluation infrastructure exist.
- Decisive decision or feedback right: no production S3*-specific independent audit judgment and returned intervention identified.
- Decision owner: none evidenced for the assessed local distribution.
- Supporting / enforcement mechanisms: transcripts, agent tool observations, test/eval modules and Harbor grading outside the runtime.
- Closure path: ordinary tool feedback enters the agent loop; offline evaluations do not automatically return independent audit findings into production current control.
- Why this is / is not agent-owned: tests, logs and external grading in a separate package are not automatically an operational complementary audit channel.
- Evidence: [README package split](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/README.md), [runner transcript path](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/core/runner.py), [Harbor package](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-eval/README.md).
- Basis: structural.
- Confidence: medium-high, bounded to installed production runtime.
- Caveats: no independent audit run is claimed.

### Absence scope

- Surfaces inspected: production agent/tool/trace loop, package README, `feather-eval`, training/validation integration and tests.
- Plausible first-party paths checked: transcript review, task verification tools, external eval grading, child status reports and replay/export.
- Why no material first-party path remains: these are ordinary self-observation, offline evaluation or adjacent training systems; no separately owned complementary audit path is wired to intervene in the credited production organization.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally prospective model-to-capability adaptation loop is supplied within the production harness.
- Disturbance / variety regulated: current user-task changes, context growth and tool feedback, not future environmental capability shifts.
- Decisive decision or feedback right: the agent can revise an immediate task plan; separately packaged training can update models outside the assessed runtime.
- Decision owner: no S4-specific owner established in the production boundary.
- Supporting / enforcement mechanisms: todo state, context compaction, optional web fetching, separately installed rollout/training package.
- Closure path: current-task research and compaction feed present execution; no first-party future adaptation option returns to alter production capability through S3.
- Why this is / is not agent-owned: forecasting for a user task or training in an adjacent package does not by itself close harness S4.
- Evidence: [todo tool](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/tools/todo.py), [compaction](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/core/compaction.py), [package split](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/README.md).
- Basis: structural.
- Confidence: medium-high within production mode.
- Caveats: adjacent model-training effects are excluded from this specific system-in-focus.

### Absence scope

- Surfaces inspected: shipped production tools, todo/compaction, model client, CLI config, README and train/eval package boundaries.
- Plausible first-party paths checked: web search, task planning, context summary, automatic retries, model training and benchmark feedback.
- Why no material first-party path remains: no production path develops prospective external adaptation options and returns an authorized capability change into the current harness; train/eval are adjacent products.

## S5 — Policy and identity

- State: —
- Function: no explicit runtime identity/ultimate-policy decision closure is established.
- Disturbance / variety regulated: task instructions, workspace limits, provider choice and process permissions rather than identity-level disputes.
- Decisive decision or feedback right: users/developers configure model, profile, tools and instruction text; the agent executes within these constraints.
- Decision owner: no in-boundary identity/ultimate-policy owner/path established.
- Supporting / enforcement mechanisms: system prompts, CLI configuration, process permissions, concurrency/turn caps and user task boundary.
- Closure path: configuration constrains the run; no shipped identity/policy issue→legitimate authority→returned decision→subsequent operation governance loop identified.
- Why this is / is not agent-owned: a system prompt and configurable safety/role constraints are not S5 decisions merely by being present.
- Evidence: [CLI configuration](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/cli.py), [production instructions](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/production.py), [local assembly](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/local/__init__.py).
- Basis: structural.
- Confidence: medium-high within reviewed mode.
- Caveats: parent human configuration could create a different organization, but generic external user authority alone is not the Methodology's `P` loop.

### Absence scope

- Surfaces inspected: local CLI/config, production prompts, agent runtime, parent/child guidance, shell permissions and README deployment choices.
- Plausible first-party paths checked: user instruction changes, workspace selection, child permissions/caps, model/profile selection, task completion and escalation to user.
- Why no material first-party path remains: these bound work and implementation; no explicit first-party identity/ultimate-policy dispute resolution with authoritative return-to-operation is supplied.

## Distributed OSS parent arrangement

Repository contributors, its maintainer, CI and Paper training organization are outside the local Feather task-run recursion. The optional child manager is not an organization-level parent. No contributor approval or local user configuration is promoted to a `P` state.

## Self-hosted and non-human modes

The self-hosted `prod` CLI uses user-selected model/config with agent-owned S1 and optionally parent-agent S3. The `train` profile and separate rollout/grading packages do not donate production audit/adaptation ownership. No qualifying S3/S4/S5 parent mode is demonstrated merely by operator configuration.

## Recursion

Children run nested task portions with independent contexts, but nesting and parallelism do not alone establish recursively viable organizations. The assessment remains the one local task-run boundary.

## Variety and escalation

Tool results, stop/failure states, and child reports feed current task decisions. A failed model response can trigger one bounded recovery. CLI errors, max turns and canceled child tasks bound/stop execution; these are not automatically algedonic or S5 signals.

## Evidence gaps

No provider-backed agent run or E2E performance test was executed. Source inspection establishes shipped control paths rather than verified task success or reliable inter-child conflict prevention; no separate independent semantic reviewer or S3* audit is claimed.
