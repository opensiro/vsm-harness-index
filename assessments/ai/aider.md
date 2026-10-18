---
harness_id: aider
project_name: Aider
repository: https://github.com/Aider-AI/aider
review_ref: 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
reviewed_at: 2026-09-15
status: included
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 5dc9490bb35f9729ef2c95d00a19ccd30c26339c
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Aider

## Review boundary
Aider at the pinned revision as a terminal coding-agent harness operating on one codebase/session.

## Repository architecture
Aider is centered on one coding operation with repository context, editing, Git integration and optional automated lint/test feedback. Architect mode can use one model to propose a solution and instantiate an editor coder to apply it, but this is a sequential internal role split inside the same coding operation rather than a set of independently regulated S1 units.

## Primary evidence
- `aider/coders/architect_coder.py`: `ArchitectCoder.reply_completed()` optionally accepts the architect response, creates an `editor_coder`, then invokes that coder with the architect content; this is planner/editor task handoff inside one session.
- `aider/coders/base_coder.py`: `Coder` owns the operational repository loop, repo map, Git state, message state and edit execution.
- `aider/coders/base_coder.py`: `auto_lint` runs `lint_edited()` after edits and can ask to attempt a repair; `auto_test` invokes the configured test command and can feed failures into a repair attempt.
- `aider/linter.py`, `aider/commands.py`, and the pinned test suite exercise ordinary lint/test/tool behavior rather than a distinct audit organization.

## Operational model
The coding session is one S1. Architect/editor role separation, Git, linting and tests attenuate or expose operational variety inside that S1 but do not create a multi-S1 metasystem.

## S1 — Operations
`A`: the coding agent autonomously proposes/applies repository changes and reacts to repository, lint and optional test feedback inside configured bounds. Confidence: high.

## S2 — Coordination
`—`: architect→editor handoff is sequential task decomposition inside one coding operation. No inspected path regulates interference or oscillation among multiple autonomous S1 units. Confidence: high.

## S3 — Inside-and-now control
`—`: Git state, edit controls, reflection limits, linting and tests regulate the local coding loop; there is no whole-system regulator with authority over shared resources or commitments across several S1s. Confidence: high.

## S3* — Complementary audit
`—`: automatic lint/test checks are routine production QA invoked by the same `Coder` loop and operate on the same work products. They do not provide a sufficiently independent complementary channel to operational reality. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: repo maps, URLs and model context support the present coding task. No first-party runtime loop models external/future changes, develops adaptation options and couples them back to S3. Confidence: high.

## S5 — Policy and identity
`—`: model prompts, CLI configuration, user confirmations and repository permissions are parent-owned constraints rather than runtime ultimate-policy authority. Confidence: high.

## Recursion, variety, escalation
Architect/editor composition and coder cloning are internal specialization, not recursive viability. User confirmations are escalation to the parent human boundary.