---
harness_id: jcode
project_name: jcode
repository: https://github.com/1jehuang/jcode
review_ref: 5f33d6239b56b3d381d6b2c0e9b151eef0b54cbe
reviewed_at: 2026-09-17
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# jcode

## Review boundary
Pinned jcode runtime, including autonomous coding-agent operation, shared swarm plan/DAG state, assignment/dependency/progress machinery, coordinator-driven worker lifecycle and the documented Ambient Mode. Design-only safety proposals are not credited as implemented runtime closure.

Reviewed revision: `5f33d6239b56b3d381d6b2c0e9b151eef0b54cbe`. Contract: Profile `0.2.2`, Methodology `0.3.1`.

## Primary evidence
- [`crates/jcode-plan/src/lib.rs`](https://github.com/1jehuang/jcode/blob/5f33d6239b56b3d381d6b2c0e9b151eef0b54cbe/crates/jcode-plan/src/lib.rs) — authoritative shared swarm plan, dependencies, assignment/progress, typed gates/artifacts and bounded dead-assignee reclamation.
- [`docs/AMBIENT_MODE.md`](https://github.com/1jehuang/jcode/blob/5f33d6239b56b3d381d6b2c0e9b151eef0b54cbe/docs/AMBIENT_MODE.md) — implemented proactive scout/worker mode and memory derived from approvals/rejections.
- [`docs/SAFETY_SYSTEM.md`](https://github.com/1jehuang/jcode/blob/5f33d6239b56b3d381d6b2c0e9b151eef0b54cbe/docs/SAFETY_SYSTEM.md) — explicitly design-stage validation/permission architecture, therefore not evidence of implemented S5 closure.

## S1 — Operations
`A`. jcode owns autonomous coding-agent sessions that execute repository work and can spawn/participate in swarm work. Confidence: high.

## S2 — Coordination
`A`. The shared live plan carries explicit blockers, assignments and task state; worker outcomes and plan mutations change which nodes become runnable and which agent receives later work. Dependency and gate state therefore regulates inter-S1 ordering/conflict rather than merely routing messages. Confidence: high.

## S3 — Inside-and-now control
`A`. The coordinator owns the current shared plan and worker population, assigns/spawns work, observes progress/heartbeats and reclaims stranded assignments when workers die. This supplies autonomous whole-swarm current regulation. Confidence: high.

## S3* — Complementary audit
`—`. Gate/verify node kinds and artifact checks occur inside the normal swarm execution path; no materially independent reviewer/auditor with distinct access and corrective authority was established at the pin. Confidence: medium-high.

## S4 — Outside-and-then intelligence
`—`. Ambient Mode proactively inspects recent project activity and can launch useful maintenance work, while its memory learns from approvals/rejections. That is ongoing S1 work plus internal experiential memory, not a distinct outside-looking prospective loop that develops and feeds changed organizational capability into current regulation. Confidence: high.

## S5 — Policy and identity
`—`. The safety/approval architecture at the pin is explicitly a design document; moreover action permission by itself is not identity/ultimate-policy closure. No implemented S5 tension-resolution loop was established. Confidence: high.

## Recursion, variety, and escalation
Swarm sessions and plan expansion amplify execution variety; dependencies, gates, assignments, heartbeats and reclamation attenuate it into a bounded shared plan. Ambient work increases temporal autonomy without creating a separate S4 layer.

## Admission conclusion
Canonical vector: `A A A — — —`.

This resolves the parked provisional `A A A ? ? ?`: targeted recheck found no independent S3*, no prospective S4 capability-adaptation loop, and no implemented S5 closure at the pinned revision.