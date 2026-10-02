---
harness_id: zeron
project_name: Zeron
repository: https://github.com/zeronsh/zeron
review_ref: 6ecea055877e1f560adbc4545b8d8fd7dffa6d75
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Zeron

## Review boundary

- System in focus: Zeron's Rust engine, session command plane, harness adapters, worktrees, terminals, persistence, sync and remote control.
- Purpose and identity: local-first control plane for running, resuming, steering and observing coding-agent sessions.
- Relevant environment: supported external coding agents/models, repositories, devices and users.
- Standard-distribution boundary: Zeron engine/proto/doc/sync/rpc/ui and harness-adapter code are inside; coding-agent executables/model reasoning loops are external.
- Credited operating / distribution surfaces: README.md; ARCHITECTURE.md; crates/engine; crates/harness; crates/proto; sync and workspace control.
- Adjacent first-party surfaces excluded from ownership: tests/fixtures, contributor/release machinery and relay code that only transports state.
- First-party operating / deployment modes considered: headed engine, headless daemon, local-only and synced profiles, remote steering and worktrees.
- Recursion level: Zeron control plane around external coding-agent sessions.
- Reviewed revision: 6ecea055877e1f560adbc4545b8d8fd7dffa6d75.
- Observation date: 2026-10-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

ARCHITECTURE.md defines the engine as backend owning session/runtime continuity and separately defines `zeron-harness`: Claude Code is driven through its CLI stream protocol and Codex through app-server/exec. Run requests select a harness/model; the harness emits normalized reasoning/tool/result events. Zeron owns transport, persistence, recovery and execution hosting, while the selected external coding-agent runtime owns open-ended task reasoning.

Counterfactual owner test: remove the external coding-agent/model runtimes while retaining the engine, command ledger, sync, worktrees, terminals and journals. Zeron can manage state and processes but cannot interpret an open-ended objective and autonomously choose semantic actions and next actions. First-party S1 does not close.

Evidence: [README](https://github.com/zeronsh/zeron/blob/6ecea055877e1f560adbc4545b8d8fd7dffa6d75/README.md), [ARCHITECTURE](https://github.com/zeronsh/zeron/blob/6ecea055877e1f560adbc4545b8d8fd7dffa6d75/ARCHITECTURE.md), [agent protocol](https://github.com/zeronsh/zeron/blob/6ecea055877e1f560adbc4545b8d8fd7dffa6d75/crates/proto/src/agent.rs).

## S1 — Operations
- State: —
- Function: first-party runtime/control without a first-party open-ended task actor.
- Disturbance / variety regulated: session continuity, process failure, workspace isolation and command delivery.
- Decisive decision or feedback right: choose semantic task actions and the next action from observed results.
- Decision owner: external coding-agent/model runtime.
- Supporting / enforcement mechanisms: engine, durable commands, journals, worktrees, terminals and harness adapters.
- Closure path: command → Zeron host → external agent → actions/results → external next decision → Zeron events.
- Why this is / is not agent-owned: Zeron owns hosting and continuity, not semantic action selection.
- Evidence: ARCHITECTURE.md; crates/proto/src/agent.rs.
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: first-party protocol adapters do not transfer model-loop ownership.

### Absence scope
- Surfaces inspected: engine, harness adapters, command plane, recovery, worktrees, terminals and sync.
- Plausible first-party paths checked: engine actor, watchdog/recovery, command executor and adapters.
- Why no material first-party path remains: open-ended decisions terminate in external agent runtimes.

## S2 — Coordination
- State: —
- Function: first-party routing of sessions/subagents without first-party autonomous coordination judgment.
- Disturbance / variety regulated: parent/child attribution, steering and remote-device routing.
- Decisive decision or feedback right: decide delegation and response to delegated work.
- Decision owner: external parent agent or user.
- Supporting / enforcement mechanisms: subagent event routing, parent bindings, command plane and registry.
- Closure path: external parent delegates → Zeron routes child traffic → external parent continues.
- Why this is / is not agent-owned: deterministic routing preserves external decisions rather than making them.
- Evidence: crates/proto/src/agent.rs; ARCHITECTURE.md.
- Basis: structural negative review.
- Confidence: high.
- Caveats: provider multi-agent activity is not imported.

### Absence scope
- Surfaces inspected: subagent normalization, registry, device routing and steering.
- Plausible first-party paths checked: subagent router, device router and session scheduler.
- Why no material first-party path remains: coordination judgment remains external.

## S3 — Inside-and-now control
- State: —
- Function: lifecycle/recovery control without autonomous whole-system current-control judgment.
- Disturbance / variety regulated: runtime death, stalls, session ownership and recovery.
- Decisive decision or feedback right: discretionary current intervention across operational units.
- Decision owner: user/external agents; engine owns deterministic lifecycle rules.
- Supporting / enforcement mechanisms: journals, watchdog, recovery, registry and command executor.
- Closure path: runtime facts → deterministic recovery or external judgment → engine action.
- Why this is / is not agent-owned: resilience/process control is not whole-system discretionary S3 ownership.
- Evidence: ARCHITECTURE.md; crates/engine.
- Basis: structural negative review.
- Confidence: high.
- Caveats: always-on headless operation improves continuity, not semantic control ownership.

### Absence scope
- Surfaces inspected: session engine, watchdog/recovery, registry and remote control.
- Plausible first-party paths checked: watchdog, recovery and registry supervisor.
- Why no material first-party path remains: no autonomous discretionary controller over first-party S1 units exists.

## S3* — Complementary audit
- State: —
- Function: evidence capture without independent semantic audit judgment.
- Disturbance / variety regulated: transcripts, journals, tool events and diffs expose execution.
- Decisive decision or feedback right: independently accept/challenge semantic results and return correction.
- Decision owner: user or external reviewer agent.
- Supporting / enforcement mechanisms: journals, diff sync, transcript history and status records.
- Closure path: evidence → external/human interpretation → optional new turn.
- Why this is / is not agent-owned: observability is not complementary audit ownership.
- Evidence: ARCHITECTURE.md; crates/proto/src/agent.rs.
- Basis: structural negative review.
- Confidence: high.
- Caveats: an external reviewer remains external.

### Absence scope
- Surfaces inspected: journals, transcripts, diffs and tool events.
- Plausible first-party paths checked: run journal, diff sync and watchdog.
- Why no material first-party path remains: no independent first-party semantic evaluator closes corrective return.

## S4 — Outside-and-then intelligence
- State: —
- Function: persistence/configuration without autonomous prospective adaptation.
- Disturbance / variety regulated: device/network state, harness/model selection and recovery.
- Decisive decision or feedback right: choose a prospective capability adaptation from external intelligence.
- Decision owner: user, maintainer or external agent.
- Supporting / enforcement mechanisms: profiles, model/harness catalogs, recovery and sync.
- Closure path: external/operator choice → configuration → later external-agent run.
- Why this is / is not agent-owned: recovery restores existing capability rather than selecting future adaptation.
- Evidence: ARCHITECTURE.md.
- Basis: structural negative review.
- Confidence: high.
- Caveats: external agents may reason prospectively inside hosted sessions.

### Absence scope
- Surfaces inspected: profiles, sync, catalogs, recovery and session history.
- Plausible first-party paths checked: recovery as adaptation, model switching and multi-device continuity.
- Why no material first-party path remains: no first-party future-model/adaptation chooser is established.

## S5 — Policy and identity
- State: —
- Function: policy enforcement without autonomous identity/ultimate-policy resolution.
- Disturbance / variety regulated: profile scope, device trust and execution permissions.
- Decisive decision or feedback right: resolve ultimate policy/identity tensions and govern operation.
- Decision owner: human/operator.
- Supporting / enforcement mechanisms: authentication/profile state, device identity, trust boundaries and execution settings.
- Closure path: operator policy → engine enforcement → external-agent run.
- Why this is / is not agent-owned: strong trust/scope enforcement applies prior policy; it does not autonomously resolve policy.
- Evidence: ARCHITECTURE.md; README.md.
- Basis: structural negative review.
- Confidence: high.
- Caveats: operator-selected policy is not Methodology S5 closure.

### Absence scope
- Surfaces inspected: auth/profile state, local/synced scope, device trust and permissions.
- Plausible first-party paths checked: workspace scope, device identity and credential management.
- Why no material first-party path remains: no autonomous identity/ultimate-policy resolution loop is established.

## Recursion

Zeron is assessed as a runtime/control layer around external agent sessions.

## Variety and escalation

Zeron attenuates variety through durable commands, recovery, worktrees, terminals, local-first storage and multi-device routing. Input/attention escalates to users or external agents.

## Evidence gaps

Frozen revision only. External agents' own VSM functions are not imported. Sync durability and harness adapters are credited as control/runtime mechanisms, not as semantic decision ownership.

## Assessment summary

At the frozen revision, Zeron is a substantial first-party session/recovery/workspace/multi-device control plane, but its architecture places open-ended reasoning in the external coding-agent runtimes selected through its harness adapters. Proposed terminal disposition: excluded-no-agentic-vsm.

**Vector:** — · — · — · — · — · —
