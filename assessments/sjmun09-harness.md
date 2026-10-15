---
harness_id: sjmun09-harness
project_name: Harness
repository: https://github.com/sjMun09/Harness
review_ref: c1bc066f5608167790d229f818d989a15a265ad4
reviewed_at: 2026-10-11
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

# Harness (sjMun09)

## Review boundary

- System in focus: bundled Rust `harness-cli` with owned core model/tool loop, registered tools, permissions, hooks, plan gate, transaction and nested read-only subagent host.
- Purpose and identity: execute coding tasks on a local workspace by model-directed reading, changing files and observing shell/tool outputs.
- Relevant environment: user/operator, local git/file system, tool commands, external LLM provider, optional operator hook scripts.
- Standard-distribution boundary: built and packaged CLI and supporting first-party Rust crates at pinned revision, not external CI or another repo sharing the project name.
- Credited operating / distribution surfaces: [crates/harness-core/src/engine.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/engine.rs), [crates/harness-core/src/subagent.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/subagent.rs), [crates/harness-cli/src/subagent_host.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-cli/src/subagent_host.rs), [crates/harness-core/src/plan_gate.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/plan_gate.rs), [crates/harness-core/src/hooks.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/hooks.rs), [crates/harness-tools/src/edit.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-tools/src/edit.rs).
- Adjacent first-party surfaces excluded from ownership: [.github/workflows/ci.yml](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/.github/workflows/ci.yml), [bench/README.md](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/bench/README.md), [crates/harness-testkit/src/lib.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-testkit/src/lib.rs), [PLAN.md](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/PLAN.md) and external custom hooks/tool providers.
- First-party operating / deployment modes considered: interactive or line-mode CLI coding, opt-in child sub-turns, permissions, project-plan verification hints, configured hooks, transaction/rollback.
- Recursion level: one coding session with bounded lower-level child investigators, not developer organization.
- Reviewed revision: `c1bc066f5608167790d229f818d989a15a265ad4`.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.
- Name-collision note: `assessments/harness.md` already belongs to `sausheong/harness` at catalog #306, a different upstream; unique `sjmun09-harness` ID preserves both without overwriting.

## Repository architecture

`run_turn_with_outcome` streams model responses, extracts tool use, dispatches via first-party registry and feeds results back for further decisions. The CLI wires a reusable `CliSubagentHost`, which starts a restricted read-only child `run_turn`, generates distinct session records and returns bounded text. The engine concurrently dispatches individual tool calls, but generic parallel tools are not equivalent to distinct coordinated coding S1s. Plan gates, configured hooks, permission checks, transaction staging and provider retries are deterministic support. Primary files: [crates/harness-core/src/engine.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/engine.rs), [crates/harness-cli/src/subagent_host.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-cli/src/subagent_host.rs), [crates/harness-core/src/subagent.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/subagent.rs), [crates/harness-core/src/tx.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/tx.rs).

## Operational model

The root model actor owns next coding choices and can invoke a bounded investigation child; results/denials feed the same session's subsequent operation. Nested children have no Bash/recursive subagent by default and do not govern multiple workstream commitments. The human owns permission configuration, which is enforced by the Rust runtime.

## S1 — Operations

- State: A
- Function: Model-driven coding file/shell operations and delegated codebase investigation.
- Disturbance / variety regulated: Task variety, source changes and tool/error responses.
- Decisive decision or feedback right: Choose tool/action after seeing model and tool results.
- Decision owner: Root model-guided coding agent; optional read-only child agent when spawned.
- Supporting / enforcement mechanisms: Tool map, retry, permission, context compaction, bounded-turn guard.
- Closure path: selected tool → dispatch → tool result appended → model chooses next operation.
- Why this is / is not agent-owned: Kernel alone does not select task-relevant source edits.
- Evidence: [crates/harness-core/src/engine.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/engine.rs), [crates/harness-cli/src/subagent_host.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-cli/src/subagent_host.rs)
- Basis: structural
- Confidence: high
- Caveats: Bounded frozen first-party source, no empirical capability claims.
- Boundary reachability: CLI constructs first-party Rust run_turn and tool context; child host is reachable in supported CLI operation.

## S2 — Coordination

- State: —
- Function: No evidenced distinctive interaction-induced S1 interference regulation and return.
- Disturbance / variety regulated: Several tool calls may run concurrently, but they are actions inside one S1 session, not proof of interacting autonomous S1 operational units.
- Decisive decision or feedback right: Parent delegates child investigation; dispatcher gathers outputs without regulating child-versus-child conflicts.
- Decision owner: Task model for delegation, runtime for depth/allowlist/dispatch.
- Supporting / enforcement mechanisms: Read-only subagent tools, child cancellation, async join_all.
- Closure path: Child output reaches parent as a tool result, not an inter-S1 coordination corrective response.
- Why this is / is not agent-owned: Generic parallel tool dispatch and read-only bounds do not establish S2.
- Evidence: [crates/harness-core/src/engine.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/engine.rs), [crates/harness-core/src/subagent.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/subagent.rs), [crates/harness-cli/src/subagent_host.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-cli/src/subagent_host.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded frozen first-party source, no empirical capability claims.

### Absence scope

- Surfaces inspected: engine concurrent dispatcher, CLI subagent host, child default tool allowlist, tool context and cancellation
- Plausible first-party paths checked: parallel tool execution, nested agents, shared workspace and output feedback
- Why no material first-party path remains: No source-evidenced coordination right resolves a concrete interference among distinct independent S1 coding units and feeds that resolution to their subsequent operation.

## S3 — Inside-and-now control

- State: —
- Function: No whole-system discretionary authority over currently competing S1 commitments/resources.
- Disturbance / variety regulated: Current token budgets, tool risk, planning and provider failures.
- Decisive decision or feedback right: Operator-defined limits and permission outcomes govern local operation, not shared operational priorities.
- Decision owner: Operator for config, deterministic runtime for enforcement; root model for coding task decisions.
- Supporting / enforcement mechanisms: Plan gate, hooks, permission snapshot, transactions and retries.
- Closure path: Per-operation reject/retry/rollback affects local execution; no returned S3 whole-current control decision.
- Why this is / is not agent-owned: A configured gate cannot claim ownership of the decisions it enforces.
- Evidence: [crates/harness-core/src/engine.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/engine.rs), [crates/harness-core/src/plan_gate.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/plan_gate.rs), [crates/harness-core/src/tx.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/tx.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded frozen first-party source, no empirical capability claims.

### Absence scope

- Surfaces inspected: run_turn state, permissions, plan gate, token budgets, transaction and hooks
- Plausible first-party paths checked: whole current operation view, resource bargaining, parent intervention, tool/run controls
- Why no material first-party path remains: No separately owned whole-system decision authority and accountable returned reallocation of current S1 resource commitments.

## S3* — Complementary audit

- State: —
- Function: No independently judged complementary audit over routine claims with consequential corrective closure.
- Disturbance / variety regulated: False completion or untested file changes may be detected by routine tools.
- Decisive decision or feedback right: Test reminders, external hook scripts and logs can support a check but do not own a separate audit finding.
- Decision owner: Operator scripts and deterministic plan gate, not a first-party independent auditor.
- Supporting / enforcement mechanisms: HARNESS.md verification reminders, CI/testing, event streams, child JSONL logs.
- Closure path: Test/permission outcomes feed task context; no complementary audit → authoritative returned correction pathway.
- Why this is / is not agent-owned: Normal test prompts, review labels and lifecycle hooks alone do not establish S3*.
- Evidence: [crates/harness-core/src/plan_gate.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/plan_gate.rs), [crates/harness-core/src/hooks.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/hooks.rs), [crates/harness-cli/src/subagent_host.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-cli/src/subagent_host.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded frozen first-party source, no empirical capability claims.

### Absence scope

- Surfaces inspected: plan verification, post-tool hooks, subagent logs, test runner and developer CI
- Plausible first-party paths checked: independent direct inspection, verifier judgment, audit findings and returned operating controls
- Why no material first-party path remains: Shipped checks are task-local enforcement or caller-installed scripts, without first-party independent complementary audit judgment and consequential control closure.

## S4 — Outside-and-then intelligence

- State: —
- Function: No externally prospective future capability-adaptation decision path.
- Disturbance / variety regulated: Changing tools/models and future conditions beyond the current coding task.
- Decisive decision or feedback right: Compaction, provider retry and project guidance update current execution only.
- Decision owner: Operator config and root task model; no future-oriented adaptation owner.
- Supporting / enforcement mechanisms: Session memory, compactor, hooks, provider failover/backoff.
- Closure path: Immediate task turns continue; no external future option generates an installed capability change.
- Why this is / is not agent-owned: State trimming/retry is not S4.
- Evidence: [crates/harness-core/src/engine.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/engine.rs), [crates/harness-core/src/memory.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/memory.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded frozen first-party source, no empirical capability claims.

### Absence scope

- Surfaces inspected: runtime memory, prompts, plan gate, provider retry and context compaction
- Plausible first-party paths checked: environmental scanning, future option proposal and update to active capability
- Why no material first-party path remains: No prospective adaptation loop across source-distinct environment/options/current capability was found in shipped standard paths.

## S5 — Policy and identity

- State: —
- Function: No ultimate policy/identity deliberation → legitimate authority → binding return.
- Disturbance / variety regulated: Security/trust conflicts, unsafe tools, project policy.
- Decisive decision or feedback right: Operators select permission/plan/hook policy and confirm calls.
- Decision owner: External user/developer for policy, deterministic runtime for enforcement.
- Supporting / enforcement mechanisms: PermissionSnapshot, HookDispatcher, prompt and trust mode.
- Closure path: Tool requests allowed/denied, with no identity-level decision return.
- Why this is / is not agent-owned: A static policy file and per-task confirmation do not establish S5.
- Evidence: [crates/harness-core/src/engine.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/engine.rs), [crates/harness-core/src/hooks.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/hooks.rs), [crates/harness-cli/src/trust.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-cli/src/trust.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded frozen first-party source, no empirical capability claims.

### Absence scope

- Surfaces inspected: CLI trust, permission, hook and plan configuration, prompt, source and tests
- Plausible first-party paths checked: user confirmation, allow-always, external hook and project instructions
- Why no material first-party path remains: No first-party ultimate authority adjudicates identity/policy issues and returns a new governance decision at this recursion.

## Recursion

Child sub-turns have scoped independent inference and investigation, but a bounded depth, no Bash/child spawn and ordinary parent result return; no automatically recursively viable higher organization. [crates/harness-core/src/subagent.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-core/src/subagent.rs), [crates/harness-cli/src/subagent_host.rs](https://github.com/sjMun09/Harness/blob/c1bc066f5608167790d229f818d989a15a265ad4/crates/harness-cli/src/subagent_host.rs).

## Variety and escalation

Tool errors and prompt feedback enter later S1 turns, while permission rejections and hard limits restrict harmful variety. These constraints do not prove organizational S3 or algedonic response. Optional user custom hooks do not become first-party organizational owners.

## Evidence gaps

- Static frozen Rust repository, not observed benchmark or trace.
- `sjmun09-harness` is intentionally separate from `sausheong/harness` despite same display name.
- User-created hooks and third-party runtime composition could add functions beyond this assessed standard first-party boundary, but do not require `?` solely by their hypothetical extensibility.
