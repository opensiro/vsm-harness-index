---
harness_id: get-shit-done
project_name: get-shit-done
repository: https://github.com/open-gsd/gsd-core
review_ref: 4f487e4e75276ad50fc13796cef8d23148cd8830
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: A
autonomy_s4: ?
autonomy_s5: ?
---

# get-shit-done

## Review boundary
GSD Core at the pinned revision as a context/spec-driven development system driving coding agents through Discuss→Plan→Execute→Verify→Ship.

## Repository architecture
Fresh-context researchers/planners/checkers/executors/verifiers perform separated phase roles. Execution uses dependency waves with non-overlapping plans. After execution, a distinct verifier checks phase goal, decisions, plans and implementation, writes `VERIFICATION.md`, and discrepancies produce fix plans. Verification fingerprints covered implementation/planning files; later changes make a passing report stale.

## Primary evidence
- `README.md`: phase loop, fresh subagents, parallel execution and verification.
- `docs/explanation/the-phase-loop.md`: separate plan-checker/executors/verifier, verification coverage and fix-plan feedback.
- `docs/how-to/verify-and-ship.md`: UAT/debug/fix loop; verification status; content fingerprints over implementation/planning files and stale-on-change behavior.

## Operational model
Executors are S1 units. Phase-wave decomposition and orchestrator merging are workflow/task decomposition rather than S2. The post-execution verifier is a distinct fresh-context audit role with direct access to covered artifacts and a corrective path.

## S1 — Operations
`A`: executor agents autonomously implement bounded plans and commit results. Confidence: high.

## S2 — Coordination
`—`: dependency waves/non-overlap/orchestrator merge mechanically avoid conflicts; they do not establish agent-owned mutual adjustment among S1s.

## S3 — Inside-and-now control
`?`: the phase orchestrator/planner does not demonstrate whole-system resource/accountability authority in the Beer S3 sense.

## S3* — Complementary audit
`A`: a separate verifier agent with fresh context examines requirements/decisions/plans and actual covered implementation artifacts after execution, produces a distinct verification record, and routes discrepancies into targeted fix plans. Content fingerprints independently detect post-verification drift and invalidate stale verdicts. Confidence: high.

## S4 — Outside-and-then intelligence
`?`: research/planning stages support project planning but do not establish a persistent external/prospective intelligence function coupled to S3.

## S5 — Policy and identity
`?`: phase goals/decisions/acceptance ultimately remain user/project-owned.

## Recursion, variety, escalation
Fresh role agents are phase-specific operational/audit workers; their separation improves context independence but does not establish recursive viability.