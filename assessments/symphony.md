---
harness_id: symphony
project_name: Symphony
repository: https://github.com/openai/symphony
review_ref: be10a1b79df723d6d7612b5651c8522704dafb2e
reviewed_at: 2026-09-16
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: P
---

# Symphony

## Review boundary
The system-in-focus is Symphony's work-level orchestration loop plus the bundled runnable Elixir reference implementation. Codex supplies operational worker cognition; issue trackers, GitHub review/CI and human reviewers are environmental/parent systems.

## Repository architecture
The orchestrator polls tracker work, maintains running/claimed/blocked/retry state, sorts eligible work, enforces capacity, creates isolated runs, reconciles tracker/runtime state, restarts stalled agents with backoff and blocks workers requiring operator input. `WORKFLOW.md` defines implementation/review/landing protocol.

## Primary evidence
- [`elixir/lib/symphony_elixir/orchestrator.ex`](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/lib/symphony_elixir/orchestrator.ex#L20-L205): running/claimed/blocked/retry state and completion/retry control.
- [`elixir/lib/symphony_elixir/orchestrator.ex`](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/lib/symphony_elixir/orchestrator.ex#L365-L705): reconciliation, stopping, stall detection and operator-input blocking.
- [`elixir/lib/symphony_elixir/orchestrator.ex`](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/lib/symphony_elixir/orchestrator.ex#L775-L1045): priority dispatch, capacity/claims/state limits and retry scheduling.
- [`elixir/lib/symphony_elixir/linear/client.ex`](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/lib/symphony_elixir/linear/client.ex#L460-L510): active blockers prevent dispatch.
- [`elixir/WORKFLOW.md`](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/WORKFLOW.md#L220-L310): validation/feedback closure and human approval before merging.

## Operational model
Each dispatchable issue becomes an isolated autonomous implementation run. Symphony selects work subject to capacity/blocker constraints, launches workers, stops stale/ineligible work, retries recoverable failures and preserves true operator-input requests as blocked. Humans retain final review/merge authority.

## S1 — Operations
`A`: dispatched Codex workers autonomously implement, test and prepare work. Proof: [autonomous workflow](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/WORKFLOW.md#L30-L145), [dispatch](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/lib/symphony_elixir/orchestrator.ex#L920-L1005). Confidence: high.

## S2 — Coordination
`C`: claims, capacity constraints and blocker semantics regulate interference/dependencies among operational runs under configured rules. Proof: [capacity/claim gating](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/lib/symphony_elixir/orchestrator.ex#L775-L900), [blocker dispatch](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/lib/symphony_elixir/linear/client.ex#L460-L510). Confidence: high.

## S3 — Inside-and-now control
`C`: orchestrator owns priority, dispatch, capacity, running/blocked state, termination, stall detection and retry/backoff under constructor-configured policy. Proof: [reconciliation](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/lib/symphony_elixir/orchestrator.ex#L365-L705), [dispatch/retry](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/lib/symphony_elixir/orchestrator.ex#L775-L1045). Confidence: high.

## S3* — Complementary audit
`—`: tests, CI, feedback sweeps and self-review are ordinary implementation/review paths rather than a Symphony-owned independent audit channel. Proof: [feedback/validation path](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/WORKFLOW.md#L220-L270). Confidence: high.

## S4 — Outside-and-then intelligence
`—`: tracker polling, retry, stall recovery and Rework respond to current work-state changes; no distinct prospective adaptation loop is established. Proof: [current-state reconciliation](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/lib/symphony_elixir/orchestrator.ex#L365-L705). Confidence: high.

## S5 — Policy and identity
`P`: autonomous progression stops at `Human Review`; human movement to `Merging` supplies approval, and operator-input events remain blocked. Proof: [human approval](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/WORKFLOW.md#L250-L285), [operator-input blocking](https://github.com/openai/symphony/blob/be10a1b79df723d6d7612b5651c8522704dafb2e/elixir/lib/symphony_elixir/orchestrator.ex#L570-L705). Confidence: high.

## Recursion, variety, escalation
Multiple autonomous issue-level S1s are constrained by capacity, claims, blockers, isolated workspaces and reconciliation. Retry/backoff absorbs recoverable failures; approval/input-required events escalate to the parent.

## Deep-review conclusion
Signature at the pinned revision: `A C C — — P`. This new-ref reassessment closes deterministic coordination/current-control around autonomous workers and identifies explicit parent-governed review/approval authority.