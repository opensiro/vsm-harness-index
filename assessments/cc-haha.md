---
harness_id: cc-haha
project_name: cc-haha
repository: https://github.com/NanmiCoder/cc-haha
review_ref: 0676c194e84b2da77c94d3992eadbf6e5eb9d7cb
reviewed_at: 2026-09-17
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# cc-haha

## Review boundary
Pinned first-party cc-haha runtime/workbench at `0676c194e84b2da77c94d3992eadbf6e5eb9d7cb`, including its own multi-agent workflow runtime, Agent Teams/swarm task machinery and built-in verification agent. Claude models/services remain external providers; cc-haha-owned orchestration/control behavior is assessed rather than credited merely because it can interoperate with Claude Code concepts.

Observation date: 2026-09-17. Generated/current contract: Profile `0.2.2`, Methodology `0.3.1`.

## Primary evidence
- [`README.en.md`](https://github.com/NanmiCoder/cc-haha/blob/0676c194e84b2da77c94d3992eadbf6e5eb9d7cb/README.en.md) — shipped multi-session/worktree, Agent Teams and dynamic workflow surfaces.
- [`src/utils/workflows/harness.ts`](https://github.com/NanmiCoder/cc-haha/blob/0676c194e84b2da77c94d3992eadbf6e5eb9d7cb/src/utils/workflows/harness.ts) — first-party `agent()` / `parallel()` / `pipeline()` execution, shared concurrency, budgets, failure propagation, abort/control and journaling/resume.
- [`src/utils/swarm/inProcessRunner.ts`](https://github.com/NanmiCoder/cc-haha/blob/0676c194e84b2da77c94d3992eadbf6e5eb9d7cb/src/utils/swarm/inProcessRunner.ts) — teammate work acquisition, dependency-aware availability and atomic task claiming that prevents competing workers from taking the same task.
- [`src/tools/TaskUpdateTool/TaskUpdateTool.ts`](https://github.com/NanmiCoder/cc-haha/blob/0676c194e84b2da77c94d3992eadbf6e5eb9d7cb/src/tools/TaskUpdateTool/TaskUpdateTool.ts) — task ownership, `blocks`/`blockedBy`, atomic mutation, assignment notifications and structural verification nudge when a multi-task run closes without verification.
- [`src/tools/TeamCreateTool/prompt.ts`](https://github.com/NanmiCoder/cc-haha/blob/0676c194e84b2da77c94d3992eadbf6e5eb9d7cb/src/tools/TeamCreateTool/prompt.ts) — team-lead coordination/assignment responsibility.
- [`src/tools/AgentTool/built-in/verificationAgent.ts`](https://github.com/NanmiCoder/cc-haha/blob/0676c194e84b2da77c94d3992eadbf6e5eb9d7cb/src/tools/AgentTool/built-in/verificationAgent.ts) — separate non-editing verification specialist with mandatory executable checks/adversarial probes and `PASS`/`FAIL`/`PARTIAL` verdict.

## Repository architecture
cc-haha ships its own agent/workflow harness rather than only a GUI around another runtime. Dynamic workflows create agent, parallel and pipeline phases under a shared concurrency/budget controller with failure propagation and resumable journal state. Agent Teams/swarm mode maintains shared task ownership/dependencies and teammate mailboxes. A built-in verifier is intentionally separated from implementation work and is structurally invoked before final completion when a non-trivial task list otherwise lacks verification.

## Operational model
Multiple agent S1s can execute task units concurrently. The task system prevents duplicate claims and blocks work whose dependencies are incomplete. A team lead/current controller allocates and steers active work. A separate verifier then challenges completed implementation using direct executable evidence and returns a verdict/findings to the parent path before completion.

## S1 — Operations
`A`. First-party agent actors autonomously execute coding/workflow tasks through the shipped tool/runtime boundary. Confidence: high.

## S2 — Coordination
`A`. Distinct teammate S1s compete for available work and can be constrained by task dependencies. The runtime identifies ready tasks, excludes blocked/owned work and uses atomic claim semantics so two peers do not take the same task; `blocks`/`blockedBy` changes feed back into later task availability/selection. This directly attenuates duplicate-claim and dependency-order interference rather than merely providing a mailbox or router. The coordination closure is first-party and used autonomously by the swarm workers. Confidence: high.

## S3 — Inside-and-now control
`A`. The team-lead/workflow control path has a current view of the shared task/agent system and discretionary authority over assignments, follow-up/steering, team lifecycle and shutdown, while the workflow harness additionally enforces concurrency/budget/failure policy. The decisive live-work choices are agent/lead-owned; deterministic pool/budget machinery is supporting enforcement, not ownership. Decisions return through task ownership/messages/controllers and change subsequent work. Confidence: high.

## S3* — Complementary audit
`A`. The built-in verification agent is explicitly separated from implementation: it cannot edit/write project files, must independently run the build/tests and direct/adversarial probes, and must produce an evidence-backed `PASS`, `FAIL` or `PARTIAL` verdict. The task runtime detects when a non-trivial multi-task run closes without a verification step and directs the main actor to spawn that verifier before final summary. Its findings/verdict return to the caller, providing a distinct complementary evidence path that can trigger correction before completion. Confidence: high.

## S4 — Outside-and-then intelligence
`—`. Workflow generation, schedules, journaling/resume and learned/current context may change future execution, but the reviewed evidence does not establish an external-and-prospective environment intelligence loop that generates adaptation options and returns them into present organizational capability. Confidence: high.

## S5 — Policy and identity
`—`. Permissions, prompts, workflow configuration and user/parent authority constrain execution but do not establish an operationally closed identity/ultimate-policy function at this boundary. Confidence: high.

## Recursion, variety, and escalation
Parallel agents amplify operational variety; dependency gating, atomic claiming, shared concurrency and failure propagation attenuate it. Team-lead control escalates unresolved/current work, while the verifier creates a separate challenge path before completion. Spawned agents are nested operational actors; nesting alone is not credited as VSM recursion.

## Admission conclusion
Canonical vector: `A A A A — —`.

Unlike a generic multi-agent wrapper, the positive S2/S3/S3* states are tied to specific first-party closure paths: dependency/claim interference regulation, live team control, and independent non-editing verification with returned findings.