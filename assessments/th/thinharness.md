---
harness_id: thinharness
project_name: ThinHarness
repository: https://github.com/ryanbbrown/thinharness
review_ref: b1d82f05567097e335f88dd974f207189c06db57
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# ThinHarness

## Review boundary

- System in focus: the installable ThinHarness Python SDK, including its supported built-in plugins.
- Purpose and identity: execute bounded model-directed automation with typed tools and resumable results.
- Relevant environment: caller tasks, workspace files, tool failures, model/provider responses, optional MCP servers and host approval decisions.
- Standard-distribution boundary: `thinharness*` packages selected by [pyproject.toml](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/pyproject.toml); the public `Harness` API with explicit plugins, optional child agents, tracing and tool approval/resume.
- Credited operating / distribution surfaces: [thinharness/core.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/core.py), [thinharness/turns.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/turns.py), [thinharness/runtime.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/runtime.py), provider/session interfaces, tool execution and packaged plugins.
- Adjacent first-party surfaces excluded from ownership: `benchmarks/`, `experiments/`, `.plans/`, examples, unit/E2E tests, build/release workflows and repository maintainer decisions. Benchmarks may run additional agents but are not installed product owners.
- First-party operating / deployment modes considered: async/sync SDK invocation; provider-backed model/tool loop; optional filesystem, bash, MCP, skills, subagent and parallel-LLM plugins; host-mediated approval resume. Applications supplying custom plugins/hooks are outside the shipped decision content.
- Recursion level: one SDK-composed task execution and its bounded delegated child runs.
- Reviewed revision: `b1d82f05567097e335f88dd974f207189c06db57`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`HarnessConfig` chooses provider/model, system prompt, workspace, limits, retries and tracing; `Harness` binds explicit plugin contributions and opens a model session. `advance_until_terminal` interprets model turns, executes requested tools, sends tool outputs back, retries malformed structured answers and returns final output or an approval pause. Provider adapters implement the model protocol; the model service itself remains external infrastructure.

Tool batches preserve result order, run sequentially for tools marked sequential, otherwise use bounded concurrency. Hooks inspect or cancel prompt/tool/child/limit events; their actual policy is caller-supplied code. Transcripts/resume state and local/OTel traces support continuity and observation. Approval-required calls yield a serialized envelope; the host supplies approved/rejected decisions to resume. This is an action-permission interface, not a shipped whole-system parent regulator.

The optional SubagentsPlugin registers static child recipes. The model chooses child/task arguments; the host builds an isolated child with approved inherited/plugin tools, runs it and returns its outcome. Children cannot recursively configure the same delegation plugin. Skills expose a constructor-time catalog; parallel-LLM provides independent one-shot prompts. No bundled organization-wide strategic or ultimate-policy process is installed. README documents installation and invocation; package configuration excludes benchmark/evaluation code from the distributed package.

## Operational model

The operational unit is the model-directed task loop: it decides which tool or child to use, reads the result and chooses its next action or answer. A delegated child is another bounded task loop when enabled; child configuration is developer-owned. Runtime limits, approval enforcement and lifecycle cleanup support these decisions. Plurality of tool calls/children does not establish cross-unit cohesion, independent audit, prospective adaptation or ultimate authority.

## S1 — Operations

- State: A
- Function: perform caller-requested automation through iterative model decisions and concrete tools.
- Disturbance / variety regulated: uncertain workspace contents, tool errors, incomplete answers and intermediate task results.
- Decisive decision or feedback right: select tool calls and arguments, interpret returned observations and decide subsequent action/final response.
- Decision owner: model-backed agent executing inside the first-party Harness session.
- Supporting / enforcement mechanisms: provider adapters, typed tools, hook dispatch, retry/request/tool limits, ordered tool-output transport and optional host approvals.
- Closure path: [thinharness/turns.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/turns.py#L141-L210) executes the model's tool batch and calls `continue_with_tools`; final/retry branches retain the same task loop.
- Boundary reachability: `Harness.run`/stream creates this execution directly; [README.md](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/README.md) supplies a FilesystemPlugin quick start. No benchmark agent or external coding harness is required.
- Why this is / is not agent-owned: removing the model's action selection leaves typed transport and enforcement, without the task-dependent tool choice or answer judgment.
- Evidence: [thinharness/core.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/core.py#L450-L590), [thinharness/turns.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/turns.py#L111-L210), [thinharness/tool_execution.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/tool_execution.py#L77-L105), [thinharness/plugins/subagents.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/plugins/subagents.py#L138-L178).
- Basis: structural.
- Confidence: high.
- Caveats: provider-backed operation is established from source, not a live model run; outcomes depend on the configured model/tools.

## S2 — Coordination

- State: —
- Function: no shipped function-specific regulation of interference between distinct operational units is established.
- Disturbance / variety regulated: actual surfaces address tool-batch execution order and child composition rather than an identified inter-S1 oscillation.
- Decisive decision or feedback right: no packaged conflict-sensing/coordination-response right identified.
- Decision owner: developer chooses tool sequential flags and child recipes; parent model chooses task delegation.
- Supporting / enforcement mechanisms: sequential tool flag, bounded workers, child registration/inheritance checks and returned child results.
- Closure path: tool/child results return to ordinary S1 reasoning; no separate inter-unit corrective channel is shipped.
- Why this is / is not agent-owned: generic task dispatch and batch safety do not establish an S2 organizational function.
- Evidence: [thinharness/tool_execution.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/tool_execution.py#L77-L142), [thinharness/children.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/children.py#L148-L199), [thinharness/plugins/subagents.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/plugins/subagents.py#L138-L220).
- Basis: structural.
- Confidence: high.
- Caveats: an application can add a coordination plugin, but that would add decision content beyond the assessed distribution.

### Absence scope

- Surfaces inspected: public package exports, child host/recipes, SubagentsPlugin, tool-batch executor, plugin contracts and README supported modes.
- Plausible first-party paths checked: shared child tools, parallel model/tool batches, sequential flags, registered child results and inheritance restrictions.
- Why no material first-party path remains: these supply task decomposition, static tool-execution safety and generic composition, without a specific inter-S1 conflict and a corresponding mutual-adjustment/returned coordination path. No S2-specific constructor is exposed.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system resource/commitment regulator is supplied beyond bounded execution policy.
- Disturbance / variety regulated: request/tool/retry counts, cancellation, output failures and individual side-effect permissions.
- Decisive decision or feedback right: limits, tool composition and approval policy are selected by the caller; no shipped supervisory actor revises whole-system commitments.
- Decision owner: application developer/host for static configuration and particular approval decisions.
- Supporting / enforcement mechanisms: RunContext counters/notices, hooks, cancellation, approval envelopes and child limits.
- Closure path: limits terminate/warn a run and host approvals resume a specific tool batch; neither is a first-party whole-system supervisory conversation.
- Why this is / is not agent-owned: task reasoning/delegation and deterministic constraint enforcement are not whole-system current-control ownership.
- Evidence: [thinharness/core.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/core.py#L149-L175), [thinharness/runtime.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/runtime.py), [thinharness/approvals.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/approvals.py), [thinharness/turns.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/turns.py#L214-L322).
- Basis: structural.
- Confidence: high.
- Caveats: hooks can implement additional control, but no function-specific whole-system controller or complete parent supervisory mode is packaged.

### Absence scope

- Surfaces inspected: configuration, run counters/limits, approval/resume API, child construction, lifecycle hooks and documented SDK invocation.
- Plausible first-party paths checked: resource warnings/stops, child budgets, host approval return, tool cancellation and dynamic model task choices.
- Why no material first-party path remains: the shipped return paths enforce caller-selected per-run limits/permissions or ordinary task decisions; they provide no whole-system current view plus discretionary shared commitment/resource regulation. A host callback alone does not establish parent S3.

## S3* — Complementary audit

- State: —
- Function: no independent challenge of ordinary operational claims with corrective control is supplied.
- Disturbance / variety regulated: observable model/tool failures and structured-output validity are routine execution concerns.
- Decisive decision or feedback right: no shipped independent audit judgment or findings-to-control owner identified.
- Decision owner: task model for ordinary reasoning; caller for custom hook logic.
- Supporting / enforcement mechanisms: JSONL/OTel tracing, events, output validation, model retries and optional generic children.
- Closure path: retry errors return to the producing loop; traces expose the same execution and do not commission a complementary audit.
- Why this is / is not agent-owned: another arbitrary child prompt could inspect an artifact, but a first-party audit-specific independent decision/return path is not supplied.
- Evidence: [thinharness/tracing.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/tracing.py), [thinharness/turns.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/turns.py#L173-L198), [thinharness/plugins/subagents.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/plugins/subagents.py), [thinharness/hooks.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/hooks.py).
- Basis: structural.
- Confidence: high.
- Caveats: repository benchmark evaluators and developer tests are adjacent evidence, not installed product auditors.

### Absence scope

- Surfaces inspected: tracing/events, structured-output retry, lifecycle hooks, generic child plugin, package inclusion rules and benchmark separation.
- Plausible first-party paths checked: raw trace observation, after-tool interception, independent child configuration and output-verification feedback.
- Why no material first-party path remains: observations and retries follow the production path; generic extensibility supplies no independent audit mandate, alternative access/judgment and findings-to-control process in the assessed mode.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective environment-to-capability adaptation loop is supplied.
- Disturbance / variety regulated: tools can retrieve external facts for the current task, while resume state preserves prior execution.
- Decisive decision or feedback right: no shipped decision converts future-relevant distinctions into adaptation options adopted by present capability.
- Decision owner: application caller selects models, plugins and constructor-time skills; task model selects operational tools.
- Supporting / enforcement mechanisms: skill catalog, filesystem/MCP tools, transcript replay, generic plugin hooks and provider configuration.
- Closure path: retrieved information affects the task answer; plugin/configuration construction remains caller-owned without a first-party adaptation conversation.
- Why this is / is not agent-owned: external information use and persistent transcripts do not establish prospective adaptation.
- Evidence: [thinharness/plugins/skills.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/plugins/skills.py#L25-L93), [thinharness/plugins/base.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/plugins/base.py), [thinharness/core.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/core.py), [README.md](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: benchmark optimization/research and arbitrary caller-written capability plugins are outside this SDK ownership boundary.

### Absence scope

- Surfaces inspected: runtime/session replay, providers, plugin contracts, skills registry/binding, child and parallel-LLM plugins and README mode documentation.
- Plausible first-party paths checked: external tool sensing, skill selection, replay-based continuity and caller/plugin capability replacement.
- Why no material first-party path remains: the installed API offers task execution and static capability composition, without a shipped future/environment distinction → adaptation-option decision → capability adoption path or complete parent alternative.

## S5 — Policy and identity

- State: —
- Function: no identity or ultimate-policy deliberation and authoritative return process is supplied.
- Disturbance / variety regulated: configured instructions, access scopes and ordinary tool approval.
- Decisive decision or feedback right: no runtime identity-level issue is routed to an ultimate authority and returned as governing policy.
- Decision owner: caller/developer selects system prompt, plugins, paths and approval requirements.
- Supporting / enforcement mechanisms: immutable plugin configuration, typed validation, path policy, approval-state validation and resumed tool execution.
- Closure path: host decisions approve/reject particular side effects; they do not resolve identity or ultimate-policy matters.
- Why this is / is not agent-owned: prompt/instruction execution and action approval do not confer ultimate policy ownership.
- Evidence: [thinharness/defaults.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/defaults.py#L1-L7), [thinharness/approvals.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/approvals.py), [thinharness/plugins/base.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/plugins/base.py), [thinharness/plugins/filesystem.py](https://github.com/ryanbbrown/thinharness/blob/b1d82f05567097e335f88dd974f207189c06db57/thinharness/plugins/filesystem.py).
- Basis: structural.
- Confidence: high.
- Caveats: developer policy can bound an agent strongly without creating an S5 closure process.

### Absence scope

- Surfaces inspected: configuration/default prompt, plugin binding, path policy and approval/resume contracts.
- Plausible first-party paths checked: host approval envelopes, instruction/hook injection, immutable plugin identities and caller changes to future runs.
- Why no material first-party path remains: these are configuration and operational permission mechanisms, with no shipped identity-policy issue → legitimate parent decision → governing return loop or internal ultimate-policy actor.

## Distributed OSS parent arrangement

Repository maintainers and contributors own software development. No evidence makes that adjacent development organization the parent metasystem of every installed SDK execution. No organization-level parent state is inferred.

## Self-hosted and non-human modes

Local SDK hosts choose credentials, tools and optional approval decisions. Those supported modes were checked; ordinary approvals do not establish S3/S4/S5 parent modes. No intentionally non-human organization is shipped.

## Recursion

Parent/child execution provides nested task delegation. Children lack their own evidenced metasystem; recursive viability is not established.

## Variety and escalation

Typed errors, tool feedback, bounded retries, notices, host approval pauses and cancellation attenuate operational variety. The model retains task-local discretion. Events and stop states are not by themselves algedonic channels or higher functions.

## Evidence gaps

Static source assessment only; no live provider-backed/E2E or benchmark execution. Actual model competence and application-specific plugins/hooks are not established. No concrete unresolved shipped higher-function path was found at this package boundary; the negative states are bounded absence claims, not claims that custom applications cannot add these functions.
