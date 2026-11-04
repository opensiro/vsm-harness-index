---
harness_id: agent-harness-talktorana
project_name: Agent Harness (talktorana)
repository: https://github.com/talktorana/agent-harness
review_ref: 4d5e11d16e4e9755c4282634778f112c44e21d12
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent Harness (talktorana)

## Review boundary

- System in focus: One first-party talktorana Agent Harness deployment: model-tool task sessions, web console and optional co-resident mission scheduler.
- Purpose and identity: Execute project work and unattended missions with persistent observations, memory and operator supervision.
- Relevant environment: User/workspace, command/Python/browser results, model-provider availability, scheduled work and finite compute/context.
- Standard-distribution boundary: Shipped Python CLI, Agent, tools, session/memory storage, console and scheduler; optional gated deploy tooling is considered as documented, without importing a particular private deployment.
- Credited operating / distribution surfaces: run.py, Agent.run, tools registry, MemoryStore, webui /runs and /settings, run_settings and scheduler.
- Adjacent first-party surfaces excluded from ownership: Unit tests and documentation measurements are corroboration, not autonomous audit actors. Provider engines, arbitrary user project code and separately configured host policies do not donate organizational decisions.
- First-party operating / deployment modes considered: CLI task, browser-served tasks, --serve --schedule in one process; optional child agent and host-applied deployment requests, confirmation and noninteractive modes.
- Recursion level: One installed deployment with independently executing manual/scheduled task sessions as S1 units; child tool work is subordinate unless separately established.
- Reviewed revision: 4d5e11d16e4e9755c4282634778f112c44e21d12
- Observation date: 2026-11-04
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The first-party Python Agent loop composes model calls and a string-returning tool registry. It supports file/git/edit tools, persistent subprocess Python, optional browser/media, bounded child run.py agents and durable sessions. Repo/user/session memory automatically enters task prompts and permits corrections. A stdlib web console runs task threads and an optional scheduler in the same process. Runtime state is separated from reviewed mission declarations, while live operator overrides govern later jobs. Optional deployment requests are staged for a host applier with validation/readiness/rollback. See the per-function pinned evidence for code wiring.

## Operational model

S1 task sessions own local action selection. The first-party memory mutation protocol provides a narrow S2 constructor path. A human operator regulates the current deployment through actual run feedback and live controls (S3=P). Logs, generic child research, memory and deploy gates are not promoted into additional functions.

## S1 — Operations

- State: A
- Function: Perform project tasks and missions through model-selected tools and returned observations.
- Disturbance / variety regulated: Unexpected source/data, command errors, malformed calls and provider failures.
- Decisive decision or feedback right: Select tools/arguments, interpret results, revise next action and decide when to answer.
- Decision owner: Model-backed Agent task loop.
- Supporting / enforcement mechanisms: OpenAI-compatible client, tool handlers, persistent Python subprocess, retry/fallback, step/wall-clock bounds, safety confirmations and session logs.
- Closure path: Agent.run builds task/memory context, calls model, executes returned tool calls, appends tool results and repeats until final response or enforced stop.
- Boundary reachability: run.py, console task threads and scheduler jobs invoke the shipped Agent.run rather than an external agent implementation.
- Why this is / is not agent-owned: The model selects task actions; deterministic handlers and fallback machinery cannot choose a solution without that actor.
- Evidence: [agent.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/agent.py); [tools.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/tools.py); [run.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/run.py); [scheduler.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/scheduler.py); [docs/ARCHITECTURE.md](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/docs/ARCHITECTURE.md)
- Basis: explicit and structural
- Confidence: high
- Caveats: No new paid-provider or live mission run was executed for this assessment.

## S2 — Coordination

- State: C
- Function: Prevent shared-memory updates by distinct concurrent task sessions from silently overwriting one another.
- Disturbance / variety regulated: A console thread and scheduled mission can both read-modify-write the same repo/user memory file, losing one note.
- Decisive decision or feedback right: Serialize conflicting memory mutations while retaining both updates as input to later sessions.
- Decision owner: The first-party MemoryStore critical-section protocol is developer/runtime-defined; no agent chooses/revises coordination discretion.
- Supporting / enforcement mechanisms: Process-wide RLock, atomic temporary-file replacement and documented single-process console+scheduler deployment.
- Closure path: Each mutation holds the shared lock around read-modify-write; the next mutation reads the preceding committed memory; subsequent task prompts load the preserved head.
- Boundary reachability: The supported --serve --schedule mode intentionally co-locates task threads and MemoryStore inside one process. This is an S2-specific conflict path, not a generic storage API.
- Why this is / is not agent-owned: A concrete attenuation/feedback relation ships, but autonomous coordination judgment/authority would need composition; the lock executes a fixed protocol.
- Distinct S1 units: Independently model-driven manual console and scheduled mission sessions sharing the memory root.
- Inter-S1 disturbance: Lost repo/user note when concurrent read-modify-write operations overwrite one another.
- Attenuating coordination relation: Lock the shared mutation critical section and commit atomically.
- Feedback into subsequent S1 behaviour: Both writes survive and are automatically loaded/searched by later model task sessions.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The source names and tests the concrete lost-update conflict among concurrent sessions and implements serialization specifically for it.
- Evidence: [memory.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/memory.py); [test_memory_concurrency.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/test_memory_concurrency.py); [run.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/run.py); [README.md](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/README.md)
- Basis: explicit and structural constructor path
- Confidence: high
- Caveats: The lock does not extend across child processes or two containers. The C credit is confined to the documented single-process mode, not a claim of autonomous S2.

## S3 — Inside-and-now control

- State: P
- Function: Operator current-control of the deployment mission workload and resource/commitment envelope.
- Disturbance / variety regulated: Runs repeatedly hitting step ceilings, a cadence too tight for run duration and unsuitable current model choice.
- Decisive decision or feedback right: Choose the next-run model, step ceiling and mission cadence after inspecting live schedule/run outcomes; optionally hold the scheduler.
- Decision owner: Legitimate human deployment operator in the supported console/host mode.
- Supporting / enforcement mechanisms: /runs and /runs.json visibility, validated /settings and /model writes, persisted override files, scheduler state and operator hold file.
- Closure path: Whole-deployment run/schedule view → operator changes settings/model or hold → saved override → Agent._effective_max_steps and scheduler/model resolution read it at use time → later jobs execute under the returned constraint.
- Boundary reachability: These are shipped console endpoints and runtime readers; no redeploy or arbitrary external code is needed for the supervisory loop.
- Why this is / is not agent-owned: The operator chooses current workload controls; validation, scheduling and retry merely enforce/read those choices. No separate autonomous whole-deployment control actor or S3-specific autonomous constructor is supplied.
- Whole-system current view: Console schedule and recent task-run records, outcomes, overdue reasons, durations and effective configuration provenance for one deployment.
- Current-control decision scope: Mission firing cadence, task step ceilings, inference-route choice and scheduler pause; ordinary per-command approvals are not used as the S3 witness.
- Evidence: [webui.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/webui.py); [run_settings.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/run_settings.py); [scheduler.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/scheduler.py); [agent.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/agent.py); [README.md](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/README.md)
- Basis: explicit and structural parent-governed closure
- Confidence: medium-high
- Caveats: P concerns this local installed deployment, not the GitHub contributor organization. The operator view can be incomplete if external processes are run outside the supported one-process boundary.

## S3* — Complementary audit

- State: —
- Function: No material first-party complementary audit path at the declared supported boundary.
- Disturbance / variety regulated: Operational mistakes and failed deployment verification can be logged or rolled back, but no independent audit judgment is shipped.
- Decisive decision or feedback right: No qualifying function-level decision/feedback right reconstructed after checking the supported modes.
- Decision owner: No qualifying owner for this function; narrower task or developer/operator choices remain as described.
- Supporting / enforcement mechanisms: Session replay/search, tool error records, host verify/rollback and child-agent delegation.
- Closure path: No function-specific return loop; the examined operational feedback is narrower.
- Why this is / is not agent-owned: These are ordinary execution reports, deterministic verification and parent-scoped child work. No separately scoped auditor challenges the routine claims with complementary evidence and returns a discretionary finding into control. A host verify command is configuration, not a supplied independent audit actor.
- Evidence: [session.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/session.py); [tools_session.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/tools_session.py); [deploy_applier.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/deploy_applier.py); [docs/ARCHITECTURE.md](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/docs/ARCHITECTURE.md)
- Basis: structural, bounded negative adjudication after positive and eligible parent-mode checks
- Confidence: medium-high
- Caveats: A custom external organization could add the function; generic extensibility alone is not credited.

### Absence scope

- Surfaces inspected: session.py, tools_session.py, deploy_applier.py, docs/ARCHITECTURE.md
- Plausible first-party paths checked: Session replay/search, tool error records, host verify/rollback and child-agent delegation.
- Why no material first-party path remains: These are ordinary execution reports, deterministic verification and parent-scoped child work. No separately scoped auditor challenges the routine claims with complementary evidence and returns a discretionary finding into control. A host verify command is configuration, not a supplied independent audit actor.

## S4 — Outside-and-then intelligence

- State: —
- Function: No material first-party outside-and-then intelligence path at the declared supported boundary.
- Disturbance / variety regulated: Memory, retry/model fallback, adaptive reasoning depth and self-edit/deploy work change current task behavior.
- Decisive decision or feedback right: No qualifying function-level decision/feedback right reconstructed after checking the supported modes.
- Decision owner: No qualifying owner for this function; narrower task or developer/operator choices remain as described.
- Supporting / enforcement mechanisms: Correctable notes, history compaction, route failure adaptation, bounded child research and gated changes to deployment files.
- Closure path: No function-specific return loop; the examined operational feedback is narrower.
- Why this is / is not agent-owned: The shipped loop uses past observations and configured fallbacks to complete current work. It does not prescribe or wire an external/prospective sensing → capability options → current-control adaptation conversation. A user could give such a mission, but generic tools and editable code are not an S4-specific constructor or closed parent adaptation mode.
- Evidence: [agent.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/agent.py); [memory.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/memory.py); [tools_delegate.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/tools_delegate.py); [tools_deploy.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/tools_deploy.py); [docs/ARCHITECTURE.md](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/docs/ARCHITECTURE.md)
- Basis: structural, bounded negative adjudication after positive and eligible parent-mode checks
- Confidence: medium-high
- Caveats: A custom external organization could add the function; generic extensibility alone is not credited.

### Absence scope

- Surfaces inspected: agent.py, memory.py, tools_delegate.py, tools_deploy.py, docs/ARCHITECTURE.md
- Plausible first-party paths checked: Correctable notes, history compaction, route failure adaptation, bounded child research and gated changes to deployment files.
- Why no material first-party path remains: The shipped loop uses past observations and configured fallbacks to complete current work. It does not prescribe or wire an external/prospective sensing → capability options → current-control adaptation conversation. A user could give such a mission, but generic tools and editable code are not an S4-specific constructor or closed parent adaptation mode.

## S5 — Policy and identity

- State: —
- Function: No material first-party identity/ultimate-policy governance path at the declared supported boundary.
- Disturbance / variety regulated: Read-only mission declarations and forbidden deployment files constrain operational self-modification.
- Decisive decision or feedback right: No qualifying function-level decision/feedback right reconstructed after checking the supported modes.
- Decision owner: No qualifying owner for this function; narrower task or developer/operator choices remain as described.
- Supporting / enforcement mechanisms: Mission/system prompt, approval flags, deploy-policy allow/refuse rules, outbox requests and host applier.
- Closure path: No function-specific return loop; the examined operational feedback is narrower.
- Why this is / is not agent-owned: The agent cannot authorize rewriting its own guardrails in the gated deployment. The supplied flow accepts/refuses individual deployment changes under preset policy; it supplies no identity/ultimate-policy issue adjudication and returned governing-policy decision. Human ability to edit the brief or source is not a packaged function-specific S5 loop.
- Evidence: [prompts.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/prompts.py); [make_schedule.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/make_schedule.py); [scheduler.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/scheduler.py); [tools_deploy.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/tools_deploy.py); [deploy_applier.py](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/deploy_applier.py); [deploy_policy.json.example](https://github.com/talktorana/agent-harness/blob/4d5e11d16e4e9755c4282634778f112c44e21d12/deploy_policy.json.example)
- Basis: structural, bounded negative adjudication after positive and eligible parent-mode checks
- Confidence: medium-high
- Caveats: A custom external organization could add the function; generic extensibility alone is not credited.

### Absence scope

- Surfaces inspected: prompts.py, make_schedule.py, scheduler.py, tools_deploy.py, deploy_applier.py, deploy_policy.json.example
- Plausible first-party paths checked: Mission/system prompt, approval flags, deploy-policy allow/refuse rules, outbox requests and host applier.
- Why no material first-party path remains: The agent cannot authorize rewriting its own guardrails in the gated deployment. The supplied flow accepts/refuses individual deployment changes under preset policy; it supplies no identity/ultimate-policy issue adjudication and returned governing-policy decision. Human ability to edit the brief or source is not a packaged function-specific S5 loop.

## Distributed OSS parent arrangement

The local operator owns the evidenced S3 supervision loop. No cross-contributor institutional governance or organization-wide parent authority is imported from GitHub activity.

## Self-hosted and non-human modes

Interactive and unattended self-hosting share the core task loop. The supported console+scheduler process is significant for memory coordination. Gated host deployment tooling enforces operator policy but is not itself an autonomous higher recursion.

## Recursion

Child run.py processes receive fresh bounded task sessions and return answers. This is delegation; a recursively viable child metasystem is not established.

## Variety and escalation

Transient provider errors retry and move along configured routes; command safety gates, Python timeouts, step/run bounds and operator holds constrain work. Failures return as observations or explicit failed-run records. Irreversible actions without an approval path are refused and handed to a human; this operational escalation is not S5 by itself.

## Evidence gaps

Pinned code/docs and concurrency tests were inspected; no hosted model, browser or host deployment was executed. Cross-process memory arbitration is explicitly absent from the credited mode. The supported source boundary is sufficient for the bounded negative findings; no claims are made for private mission deployments.
