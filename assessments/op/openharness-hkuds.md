---
harness_id: openharness-hkuds
project_name: OpenHarness (HKUDS)
repository: https://github.com/HKUDS/OpenHarness
review_ref: 9b2efd795c6aa09f88b0c257d269a9e518da6ae7
reviewed_at: 2026-09-15
status: included
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 9b2efd795c6aa09f88b0c257d269a9e518da6ae7
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-16
last_reassessment_round: R2
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# OpenHarness (HKUDS)

## Review boundary
HKUDS/OpenHarness at the pinned revision, including core agent loop, governance, standard swarm/team primitives and coordinator mode; roadmap-only integrations are excluded. The system-in-focus is the coordinator-mode software-engineering organization: the coordinator plus its spawned worker agents operating on the shared task/repository environment.

## Repository architecture
OpenHarness supplies a streaming tool-call agent loop, memory/context and governance plus two substantive multi-agent surfaces. Its swarm runtime has team lifecycle, durable mailboxes/messages, tasks and background teammates. Coordinator mode injects a model-driven coordinator prompt into the runtime and gives that coordinator worker status/results plus authority to spawn, continue or stop workers, synthesize their findings, run independent work in parallel, serialize conflicting write-heavy work and commission fresh verification workers.

## Primary evidence
- `src/openharness/tools/agent_tool.py`: the `agent` tool spawns real local agent subprocesses with their own prompt, model/tool context and task identity; these workers execute delegated research, implementation or verification work rather than acting as labels in one deterministic workflow.
- `src/openharness/coordinator/coordinator_mode.py`: coordinator mode is explicitly model-driven; it directs research/implementation/verification workers, synthesizes their results, owns spawn/continue/stop decisions, runs independent research in parallel, and serializes write-heavy implementation one worker at a time per conflicting file set.
- `src/openharness/prompts/context.py`: `build_runtime_system_prompt()` actually injects `get_coordinator_system_prompt()` whenever coordinator mode is active, so the concurrency/coordination policy is part of the executable standard path rather than documentation-only guidance.
- `src/openharness/swarm/mailbox.py`: first-party per-agent asynchronous mailboxes carry typed sender/recipient messages with atomic persistence, supporting communication among team actors without owning the coordination decision.
- `src/openharness/coordinator/coordinator_mode.py`: verification guidance requires proving behavior independently and recommends a fresh verification worker rather than reusing implementation context, creating a complementary audit path.
- `src/openharness/tools/task_update_tool.py`: agents can update shared task progress/status metadata used by the coordination/control surface.

## Operational model
Spawned workers are S1 units: each autonomous subprocess receives an outcome-oriented prompt, operates with tools against the repository/task environment, and absorbs local implementation or research variety. The coordinator is the metasystemic actor above those S1s. Mailboxes, task state and subprocess/task machinery support coordination, but the model-driven coordinator owns the discretionary decision over which independent work may proceed concurrently and which conflicting write-heavy work must be serialized. The same coordinator maintains whole-task state, exercises assignment/stop/continue/failure-recovery authority, and can commission a fresh verifier with separate context.

## S1 — Operations
`A`: the harness supplies ready autonomous tool-using worker agents that execute delegated outcomes against the repository/task environment. Confidence: high.

## S2 — Coordination
`A`: the relevant disturbance is destructive interference among concurrently active worker S1s, especially overlapping write-heavy implementation. The decisive coordination right is the choice to parallelize independent work while serializing conflicting work by file area. Coordinator mode assigns that choice to the model-driven coordinator, which has the operational spawn/continue/stop authority needed to close it. Mailboxes, task state and subprocess scheduling are supporting transport/execution mechanisms; they do not make the decision themselves. Counterfactual owner test: if the coordinator model is removed while those mechanisms remain, no actor remains that interprets work overlap and chooses the same conflict-sensitive parallel-versus-serial policy. Confidence: high.

## S3 — Inside-and-now control
`A`: coordinator mode gives a model-driven actor whole-task current context and explicit authority to allocate workers, sequence conflicting write-heavy work, stop/continue agents, synthesize current results and intervene on failures. The decisive current-regulation choices are coordinator-owned; task/subprocess machinery enforces their execution. Confidence: high.

R2 ownership-mode revalidation: ordinary user messages can change requirements and thereby cause the coordinator to stop, redirect or continue workers, but the first-party current-control tools and the discretionary choice over which worker action to take remain on the model-driven coordinator path. The reviewed repository does not expose a separate parent mode that independently closes the same whole-task allocation/sequence/recovery right, so S3 remains plain `A` rather than `A(P)`.

## S3* — Complementary audit
`A`: the coordinator workflow explicitly separates verification from implementation, instructs verification to prove behavior rather than rubber-stamp it, and recommends spawning a fresh worker so it can inspect code/tests with independent context; findings then steer corrective work through the coordinator. The fresh verifier owns the audit judgment while coordinator/task machinery closes the result into subsequent control. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: cron/autodream/memory and external tools do not establish a distinct external-and-prospective adaptation loop coupled to current control.

## S5 — Policy and identity
`—`: permissions, policies, worker tools and ultimate task goals are configured externally; the coordinator does not hold legitimate identity-level/ultimate-policy authority.

## Recursion, variety, escalation
Worker subprocesses are operational units at this system boundary; their spawning or team nesting does not by itself prove recursive viability. Coordinator escalation/failure handling remains current-task regulation rather than S5 closure.
