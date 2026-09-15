---
harness_id: openharness-hkuds
project_name: OpenHarness (HKUDS)
repository: https://github.com/HKUDS/OpenHarness
review_ref: 9b2efd795c6aa09f88b0c257d269a9e518da6ae7
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# OpenHarness (HKUDS)

## Review boundary
HKUDS/OpenHarness at the pinned revision, including core agent loop, governance, standard swarm/team primitives and coordinator mode; roadmap-only integrations are excluded.

## Repository architecture
OpenHarness supplies a streaming tool-call agent loop, memory/context and governance plus two substantive multi-agent surfaces. Its swarm runtime has team lifecycle, durable mailboxes/messages, tasks and background teammates. Coordinator mode gives a model-driven coordinator worker status/results and authority to spawn, continue or stop workers, synthesize their findings, serialize conflicting write-heavy work and commission fresh verification workers.

## Primary evidence
- `src/openharness/swarm/mailbox.py`: first-party per-agent asynchronous mailboxes carry typed sender/recipient messages with atomic persistence, forming a concrete constructor channel among team actors.
- `src/openharness/coordinator/coordinator_mode.py`: coordinator mode is explicitly model-driven; it directs research/implementation/verification workers, synthesizes their results, manages concurrency/failures, continues or stops workers and retains whole-task context.
- `src/openharness/coordinator/coordinator_mode.py`: verification guidance requires proving behavior independently and recommends a fresh verification worker rather than reusing implementation context, creating a complementary audit path.
- `src/openharness/tools/task_update_tool.py`: agents can update shared task progress/status metadata used by the coordination/control surface.

## Operational model
Workers are S1 units. Mailboxes/tasks expose a constructor-level coordination substrate. Above them, coordinator mode is a genuine autonomous current-control role: it observes results/status across workers and exercises assignment, sequencing, stop/continue and failure-recovery authority on behalf of the whole task. Its explicit fresh-worker verification path supplies sufficiently separate operational access to challenge implementation claims.

## S1 — Operations
`A`: the harness supplies a ready autonomous tool-using agent loop. Confidence: high.

## S2 — Coordination
`C`: durable addressed mailboxes plus shared task/status mechanisms expose a concrete first-party path for inter-agent coordination, but the default swarm substrate does not by itself close a peer mutual-adjustment/anti-oscillation policy; the coordinator typically supplies the higher-level regulation. Confidence: high.

## S3 — Inside-and-now control
`A`: coordinator mode gives a model-driven actor whole-task current context and explicit authority to allocate workers, sequence conflicting write-heavy work, stop/continue agents, synthesize current results and intervene on failures. This is active whole-system current regulation, not merely a deterministic router. Confidence: high.

## S3* — Complementary audit
`A`: the coordinator workflow explicitly separates verification from implementation, instructs verification to prove behavior rather than rubber-stamp it, and recommends spawning a fresh worker so it can inspect code/tests with independent context; findings then steer corrective work through the coordinator. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: cron/autodream/memory and external tools do not establish a distinct external-and-prospective adaptation loop coupled to current control.

## S5 — Policy and identity
`—`: permissions, policies, worker tools and ultimate task goals are configured externally; the coordinator does not hold legitimate identity-level/ultimate-policy authority.

## Recursion, variety, escalation
Subprocess teammates and background tasks are operational units; coordinator/team nesting does not by itself prove recursive viability.