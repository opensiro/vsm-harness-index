---
harness_id: get-shit-done
project_name: get-shit-done
repository: https://github.com/open-gsd/gsd-core
review_ref: 4f487e4e75276ad50fc13796cef8d23148cd8830
reviewed_at: 2026-09-16
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 652796e903c630d7ac367fc57de6a0c11da4b1c2
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-16
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# GSD

## Review boundary
GSD Core at pinned revision `4f487e4e75276ad50fc13796cef8d23148cd8830`, assessed as the shipped context/spec-driven development runtime and its standard Discuss → Plan → Execute → Verify → Ship phase loop. The review treats dependency-wave scheduling as execution decomposition unless a genuine S2 regulation loop exists, and treats project research/planning as S4 only if it forms an autonomous prospective adaptation function rather than task-local preparation.

## Repository architecture
GSD separates fresh-context planner, executor, checker and verifier roles. `execute-phase` discovers plan dependencies, groups work into waves, dispatches executors, reconciles artifacts, then runs tail gates. Phase completion includes an explicit `verify_phase_goal` step that spawns `gsd-verifier` after execution. The verifier works goal-backward from roadmap success criteria and plan must-haves, reads the actual codebase rather than trusting summaries, classifies blockers/warnings, and writes `VERIFICATION.md`. A non-passing verdict keeps the phase pending; detected gaps feed `plan-phase --gaps`, then `execute-phase --gaps-only`, after which verification runs again.

## Primary evidence
- `README.md`: context/spec-driven phase lifecycle, fresh role agents and execution/verification separation.
- `docs/explanation/the-phase-loop.md`: Discuss → Plan → Execute → Verify → Ship lifecycle, dependency-aware execution waves and post-execution verification.
- `docs/how-to/verify-and-ship.md`: verification/UAT/fix routing and ship gating.
- `commands/gsd/execute-phase.md`: standard execution command requires verification work and preserves verification/state-update routing after wave execution.
- `gsd-core/workflows/execute-phase.md`: executor dispatch, overlap avoidance, mandatory phase-goal verification, `gsd-verifier` spawn, status routing, completion gate and explicit gap-closure cycle.
- `agents/gsd-verifier.md`: independent goal-backward verifier role, adversarial stance, instruction not to trust `SUMMARY.md`, direct codebase evidence checks, blocker/warning classifications and re-verification mode.

## Operational model
Executor agents are S1 units implementing bounded plans. The orchestrator analyzes dependencies and prevents unsafe parallel writes by placing overlapping plans sequentially; that is task scheduling/conflict avoidance, not an S2 mutual-regulation function. The verifier is a distinct post-execution actor with fresh context and an explicit mandate to challenge executor claims against actual code. Its verdict controls whether the phase may complete and can route work into a corrective planning/execution/re-verification loop.

## S1 — Operations
`A`: executor agents autonomously implement bounded plans, modify the codebase, run checks and commit artifacts in the standard phase flow. Confidence: high.

## S2 — Coordination
`—`: dependency waves, declared `depends_on`, file-overlap checks, worktree isolation and sequential fallback prevent conflicting execution. They do not constitute an agent-owned mutual-adjustment loop that observes and dampens ongoing interference among operational peers. Confidence: high.

## S3 — Inside-and-now control
`—`: the phase orchestrator sequences plans, gates and artifacts, but its current-whole behavior is a predetermined workflow/control plane rather than an autonomous managerial actor with decision rights over shared resources, commitments and priorities. Planner/executor supervision therefore does not by itself establish Beer S3. Confidence: medium-high.

## S3* — Complementary audit
`A`: `execute-phase` obligatorily spawns a separate `gsd-verifier` after execution. The verifier receives fresh context, reads plans/summaries/requirements but is explicitly told not to trust executor summaries, inspects the actual codebase goal-backward, and produces a distinct `VERIFICATION.md` verdict. A non-passing result prevents phase completion; gaps are converted into gap-closure plans, re-executed, and then re-verified. This provides an independent, agent-owned audit path with a concrete corrective closure loop. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: research, discussion and planning roles gather information useful to a phase, but at the pinned revision they remain project/task-local preparation. There is no persistent agent-owned function that continuously models the external/future environment, compares it with internal capability and drives organizational adaptation into S3. Confidence: medium-high.

## S5 — Policy and identity
`—`: phase goals, roadmap success criteria, project decisions, workflow rules and acceptance policy are supplied by the user/project or fixed by GSD. No agent is granted final authority to define or reconcile organizational identity, purpose or constitutional policy. Confidence: high.

## Recursion, variety, escalation
Fresh role contexts deliberately separate planning, execution and verification variety, but they are workflow roles rather than recursive viable systems. Escalation is explicit: uncertain/human-needed items route to UAT, blockers/gaps keep the phase pending, and failed truths route back through gap planning and bounded re-execution before a new verifier pass.

## Deep-review conclusion
Signature at the pinned revision: `A — — A — —`. The existing S3* classification survives deep review and is stronger than a routine “checker” label because verification is a separate actor, reads primary implementation evidence, gates completion, and closes findings through replanning/re-execution. The former `?` values for S3/S4/S5 resolve to `—`: the inspected first-party runtime provides workflow orchestration, task research and user-owned policy, not those VSM functions.