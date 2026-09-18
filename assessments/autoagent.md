---
harness_id: autoagent
project_name: AutoAgent
repository: https://github.com/thirdlayerinc/autoagent
review_ref: eb3f185dc9faac276955b4fe5feb93c8f836b644
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# AutoAgent

## Review boundary

- System in focus: AutoAgent's first-party harness-engineering program, mutable single-file `agent.py` harness boundary, benchmark/score experiment contract and keep/discard loop at pinned revision `eb3f185dc9faac276955b4fe5feb93c8f836b644`.
- Purpose and identity: have a meta-agent autonomously improve an agent harness by diagnosing benchmark failures, changing prompts/tools/agent topology/orchestration, rerunning tasks and keeping only better or equally-performing simpler variants.
- Relevant environment: external coding/meta-agent host, Harbor task/verifier environment, model providers, Docker task sandboxes and human-authored `program.md` directive.
- Standard-distribution boundary: first-party `program.md`, editable/fixed `agent.py` boundary and repository experiment conventions. Harbor and the coding-agent host are external dependencies/actors.
- Recursion level: one harness-engineering operation. The mutable `agent.py` runtime is the artifact under evolution and may itself contain subagents after a change, but that does not automatically create VSM recursion for AutoAgent.
- Reviewed revision: `eb3f185dc9faac276955b4fe5feb93c8f836b644`.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.1`.

## Repository architecture

`program.md` instructs a meta-agent to establish an unmodified baseline, read trajectories/verifier logs, group failures, choose one general harness improvement, edit the mutable section of `agent.py`, commit, rerun the benchmark, log the result and keep or discard the change. The editable harness can alter prompt, tools, agent construction, subagent/handoff structure and orchestration; the Harbor adapter/trajectory serializer below the fixed boundary is not part of ordinary mutation.

## Primary evidence

- [`README.md`](https://github.com/thirdlayerinc/autoagent/blob/eb3f185dc9faac276955b4fe5feb93c8f836b644/README.md) — repository boundary, human-programmed meta-agent loop, score-driven keep/discard experiment and Harbor separation.
- [`program.md`](https://github.com/thirdlayerinc/autoagent/blob/eb3f185dc9faac276955b4fe5feb93c8f836b644/program.md) — autonomous meta-agent responsibilities, edit rights, experiment loop, failure analysis and keep/discard rules.
- [`agent.py`](https://github.com/thirdlayerinc/autoagent/blob/eb3f185dc9faac276955b4fe5feb93c8f836b644/agent.py) — mutable harness versus fixed adapter boundary and baseline autonomous task-agent runtime.

## Operational model

The primary transformation is autonomous harness engineering. The external coding/meta-agent is an actor executing the first-party AutoAgent program rather than an owner outside the organizational definition: the program fixes its purpose, experiment loop, edit surface and selection rule while leaving diagnosis and change selection to the model-driven actor. Harbor supplies task execution/verifier evidence; it is not inherited as AutoAgent metasystem functionality.

## S1 — Operations

- State: `A`.
- Function: repeatedly diagnose benchmark failures and transform the target harness toward higher pass count or equivalent performance with lower complexity.
- Disturbance / variety regulated: task failures, verifier mismatches, missing capabilities/tools, orchestration alternatives and regressions across experiment variants.
- Decisive decision or feedback right: the meta-agent groups failure causes, selects a general harness hypothesis, edits the harness and decides the next experiment subject to the first-party keep/discard contract.
- Decision owner: autonomous meta-agent actor executing `program.md`.
- Supporting / enforcement mechanisms: Harbor task runs, verifier scores, Git commits/reverts, results ledger, Docker isolation and the fixed adapter boundary.
- Closure path: kept changes become the next harness baseline; discarded runs still feed task-level failure evidence into the next hypothesis.
- Basis / confidence: explicit + structural; high.

## S2 — Coordination

- State: `—`.
- The baseline `agent.py` exposes one primary autonomous task agent, and the meta-agent may later choose to add handoffs/subagents. Generic ability to construct multi-agent topologies does not establish a supplied disturbance-specific coordination function at this pinned boundary.
- Confidence: high.

## S3 — Inside-and-now control

- State: `—`.
- Experiment scoring, simplicity tie-breaking and keep/discard decisions are part of the primary harness-search operation. They do not establish a separate current-whole regulator over shared operational resources, priorities or commitments.
- Confidence: high.

## S3* — Complementary audit

- State: `—`.
- Harbor verifiers and benchmark scores are the normal production/evaluation feedback by which this optimization operation defines success. The reviewed distribution does not supply an additional sufficiently independent audit path that challenges ordinary operational reporting and then returns corrective findings into a separate current-control loop.
- Confidence: high.

## S4 — Outside-and-then intelligence

- State: `—`.
- Learning from benchmark failures and evolving prompts/tools/orchestration is self-improvement of the primary operation. No externally and prospectively oriented environmental model is established that develops future adaptation options and closes them into present organizational capability.
- Confidence: high.

## S5 — Policy and identity

- State: `—`.
- The human authors `program.md` and may change the directive/model constraint, but this is developer/parent configuration. No first-party runtime path is shown where an identity/ultimate-policy issue reaches legitimate parent authority and the returned decision governs subsequent operation as an S5 loop.
- Confidence: high.

## Recursion

A generated or evolved `agent.py` may itself become a multi-agent harness; it is a separate version/system-in-focus requiring its own evidence rather than automatically lending those functions to AutoAgent.

## Variety and escalation

The meta-agent amplifies design variety through unrestricted changes above the adapter boundary; benchmark/verifier feedback and strict keep/discard rules attenuate that variety. Invalid infrastructure runs are repaired and rerun rather than treated as performance evidence.

## Evidence gaps

The repository does not bundle the external coding/meta-agent host; only the autonomous decisions explicitly assigned to that actor by the first-party program are credited.

## Admission conclusion

Canonical vector: `A — — — — —`.
