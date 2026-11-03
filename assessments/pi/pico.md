---
harness_id: pico
project_name: pico
repository: https://github.com/Picom-code/pico
review_ref: aae16319e117cd04a2b5c17ce87a3b5ad314cb71
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# pico

## Review boundary

- System in focus: The installed Pico Python engine, Hermes agent bridge, lean prompt/tool configuration, local sessions and optional Hermes delegation interface; not Hermes' upstream agent implementation independently of Pico.
- Purpose and identity: Supply a compact, model-flexible local assistant for coding and everyday task completion from terminal, desktop and browser.
- Relevant environment: User instructions, local files, terminal command results, chosen model/provider, tool approvals, conversation history and optional background turns.
- Standard-distribution boundary: Pico installs a pinned Hermes dependency, starts a first-party engine, instantiates Hermes `AIAgent`, maps its real model/tool turn stream into Pico session events, and persists session/checkpoint state. The lean profile changes prompt/tool exposure but not Hermes' core agent reasoning loop.
- Credited operating / distribution surfaces: [agent_bridge.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/agent_bridge.py), [server.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/server.py), [lean.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/lean.py), [slash.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/slash.py), [subagents.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/subagents.py), [loops.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/loops.py).
- Adjacent first-party surfaces excluded from ownership: Evals and performance claims under `eval/` and `docs/EVAL.md`; future roadmap entries; deterministic desktop/terminal rendering; generic Hermes agent code, memory and subagent tool implementation not added by Pico.
- First-party operating / deployment modes considered: Interactive and headless agent turns, lean and standard Hermes configurations, user-approved `/plan`, `/goal`, `/loop` and `/cron`, optional delegated child tasks, user `undo`/approval and model selection.
- Recursion level: One Pico interactive/automation agent session, with optional delegated operational helper turns; no evidenced distinct viable metasystem.
- Reviewed revision: `aae16319e117cd04a2b5c17ce87a3b5ad314cb71`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The engine hosts sessions and invokes a pinned Hermes `AIAgent` on worker threads. Pico's `Bridge` configures provider, selected tools, prompt profile, approvals and SSE callbacks, while Hermes implements the model/tool feedback loop and optional `delegate_task`. The local engine adds plan/goal prompts, resumable sessions, recurring single-session turns, context compaction, file pre-image checkpoints and UI surfaces. Subagent settings are explicitly forwarded to Hermes' delegation configuration, including concurrency and one-level depth; they do not constitute an independently designed cross-agent coordination protocol. [README.md](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/README.md), [agent_bridge.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/agent_bridge.py), [subagents.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/subagents.py).

## Operational model

The user selects a model and supplies a task. Pico instantiates a Hermes-backed tool-using agent within Pico's packaged configuration; the model chooses tool calls, observes returned data, and continues until it responds or stops. The user may ask it to plan first or repeat a prompt periodically. An optional child agent is an operational delegation inside Hermes, not evidence of a first-party conflict-resolution layer. The user owns command permissions, approval, plan go/no-go, goal and updates. [agent_bridge.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/agent_bridge.py), [server.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/server.py), [slash.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/slash.py).

## S1 — Operations

- State: A
- Function: Choose actions and tools to complete a user's coding or other immediate task.
- Disturbance / variety regulated: Unspecified task details, changing file/terminal output, incomplete knowledge and tool errors.
- Decisive decision or feedback right: The model selects tool calls and next reasoning/action steps based on actual tool responses.
- Decision owner: The model-bearing Hermes `AIAgent` instantiated as the normal Pico runtime agent, under Pico's first-party bridge, prompt/tool configuration and session controls.
- Supporting / enforcement mechanisms: `Bridge._make_agent`, `Bridge.run_turn`, configured toolsets and approvals, local session stream, file checkpoints and user steering.
- Closure path: User task → Pico creates Hermes model agent → model selects tools and receives results → revises action or answer → Pico records and presents result.
- Boundary reachability: Pico's installed engine always invokes `AIAgent` in its supported standard or lean mode; this is not mere exposure of an unused SDK example, though model cognition is inherited from the pinned Hermes dependency.
- Why this is / is not agent-owned: A real model chooses tools and interprets feedback; Pico's SSE event emitter, local llama server or file checkpoint code are not themselves S1 decision owners.
- Evidence: [agent_bridge.py, `_make_agent` and `run_turn`](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/agent_bridge.py), [server.py, session turn path](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/server.py), [README.md](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/README.md).
- Basis: explicit + structural.
- Confidence: high for shipped invocation; no real provider-backed tool turn executed in this assessment.
- Caveats: Pico's first-party ownership is of the assembled operating mode and boundaries; Hermes supplies core agent execution capabilities.

## S2 — Coordination

- State: —
- Function: No evidenced first-party adaptive attenuation loop for interference between distinct model-bearing S1 workers.
- Disturbance / variety regulated: Parallel Hermes child tasks could compete for a file, tool or budget, but Pico's inspected logic only configures child concurrency and inheritance.
- Decisive decision or feedback right: Resolve inter-S1 collisions and feed decisions back into each worker's commitments; not established.
- Decision owner: Hermes delegation implementation and user-supplied tasks outside a Pico-specific S2 coordination loop.
- Supporting / enforcement mechanisms: `subagents.max_parallel`, child timeout/depth settings and per-session model/provider configuration.
- Closure path: `subagents.py` forwards configuration to Hermes; no Pico first-party detect-conflict → model-owned mutual-adjustment → changed work path is shown.
- Why this is / is not agent-owned: Generic parallel delegation and limits are not the same as a relation that attenuates interference among S1 units.
- Evidence: [subagents.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/subagents.py), [agent_bridge.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/agent_bridge.py), [README.md](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/README.md).
- Basis: structural.
- Confidence: medium-high for Pico's reviewed first-party boundary.
- Caveats: Upstream Hermes may contain richer delegation semantics, which cannot be silently assigned to Pico's own S2 ownership.

### Absence scope

- Surfaces inspected: Pico delegation settings/sync, bridge toolsets, session server and recurring turns.
- Plausible first-party paths checked: Concurrent helper settings, provider inheritance, timeouts, background loop scheduling and per-session steering.
- Why no material first-party path remains: None couples a named *inter-worker* disturbance to a Pico-owned reciprocal feedback/replanning decision; they configure or schedule tasks.

## S3 — Inside-and-now control

- State: —
- Function: No separately established whole-system current resource/commitment controller for multiple S1 units.
- Disturbance / variety regulated: Current chat workload, one pinned goal, periodic retries and user approvals, not whole operational unit commitments.
- Decisive decision or feedback right: Allocate/reassign tasks across the entire agent organization or determine resource synergy from a whole-system view; not evidenced.
- Decision owner: User sets goal/model, and Hermes handles single-agent plan/tool choices; engine schedules loops and tracks sessions mechanically.
- Supporting / enforcement mechanisms: `/goal`, `/plan`, `todo_list`, session database, model picker, subagent cap and `/loop` scheduler.
- Closure path: A prompted plan/todo operates inside the current S1 objective; loop state uses deterministic limits and completion marker, without a separate whole-system current-control return.
- Why this is / is not agent-owned: A single agent planning its own tools or a timer reissuing the same prompt does not establish distinct S3 authority over the whole deployment.
- Evidence: [slash.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/slash.py), [loops.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/loops.py), [server.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/server.py).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A user can manage several Pico sessions externally; that does not create a Pico first-party organization-level S3.

### Absence scope

- Surfaces inspected: Session/plan state, goal prompts, task loops, Hermes bridge and child concurrency configuration.
- Plausible first-party paths checked: Model-generated todo checklist, user goal banner, recurring runs and delegated helpers.
- Why no material first-party path remains: Each is single-objective operation or mechanical scheduling, without an owned whole-system feedback/commitment decision path.

## S3* — Complementary audit

- State: —
- Function: No evidenced complementary independent auditor of S1 outcome reports with authority to return correction to current operations.
- Disturbance / variety regulated: Bad tool results and unwanted file edits are observable, but are handled by the task agent/user rather than a separate source-checking auditor.
- Decisive decision or feedback right: Independently challenge a worker's success claim with evidence and return a mandatory corrective decision; absent.
- Decision owner: Original agent/user; checkpoint/undo machinery merely records pre-images and restores on explicit request.
- Supporting / enforcement mechanisms: Per-turn file checkpoints, tool events and diffs, user `/undo`, console approvals and eval fixtures.
- Closure path: Tool events and checkpoints can inform the user or same chat, but no separately owned inspect → audit finding → S1 correction loop is supplied.
- Why this is / is not agent-owned: Capturing diffs or running benchmark tests is instrumented observation, not an independent model-bearing audit authority.
- Evidence: [checkpoints.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/checkpoints.py), [agent_bridge.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/agent_bridge.py), [README.md](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/README.md).
- Basis: structural.
- Confidence: high within inspected installed modes.
- Caveats: A user may ask a model to review code; that prompt does not provide a distinct harness-owned complementary audit function.

### Absence scope

- Surfaces inspected: Tool event callbacks, checkpoint/undo flows, plan/goal commands, eval boundary and subagents configuration.
- Plausible first-party paths checked: Tool diff views, file restore, test bench, second Hermes helper, human command approvals.
- Why no material first-party path remains: These do not establish an independently assigned claim-checking decision and corrective return to the original worker.

## S4 — Outside-and-then intelligence

- State: —
- Function: No evidenced separate prospective external-environment scan and authorized future capability adaptation loop at Pico level.
- Disturbance / variety regulated: Provider availability, context growth and recurring work are immediate operation or user configuration rather than alternative future capabilities.
- Decisive decision or feedback right: Decide a prospective capability change and integrate it into sustained future operations; not established.
- Decision owner: User selects models, updates and skills; Hermes may provide memory but Pico does not establish a distinct first-party adaptive S4 owner and closure.
- Supporting / enforcement mechanisms: Lean prompt selection, memory/skills toolsets, hardware model scan, update notices, `/compact`, `/cron` and `/loop`.
- Closure path: Context compaction sustains current chat; update notices invite the user to install, and cron repeats tasks. No Pico-shipped external-prospect → evaluated option → authorized durable capability return is evidenced.
- Why this is / is not agent-owned: Selecting a model for this task, retaining memory or showing a roadmap is not in itself a prospective organizational learning/adaptation decision.
- Evidence: [agent_bridge.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/agent_bridge.py), [runtime.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/runtime.py), [README.md](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/README.md).
- Basis: structural.
- Confidence: medium for inspected first-party modes; Hermes upstream memory semantics not reattributed.
- Caveats: Future catalog agent in README is marked as not yet implemented; no positive S4 inferred from plans.

### Absence scope

- Surfaces inspected: Model selection/runtime updates, lean profile, skills/memory bridge, cron/loop and roadmap.
- Plausible first-party paths checked: Local model scan, periodic jobs, long-term memory, compaction and scheduled capability selection.
- Why no material first-party path remains: The checked paths do not return an authored prospective capability change under an evidenced agent or legitimate parent adaptation right.

## S5 — Policy and identity

- State: —
- Function: No evidenced Pico-governed purpose/ultimate-policy conflict resolution with a binding return into operations.
- Disturbance / variety regulated: Tool risks, API credentials, approval choices and model costs, not constitutional identity conflicts.
- Decisive decision or feedback right: Reauthorize purpose, higher-level constraints or binding identity policy from a legitimate internal/parent decision mode; not established.
- Decision owner: The user chooses commands, permissions, update and model policies outside the agent; model obeys these settings.
- Supporting / enforcement mechanisms: Approval callback, `yolo` mode, isolated Hermes credentials, provider settings and future roadmap declarations.
- Closure path: Human grants or denies a command/model; that safeguards an S1 action but is not an identity-question → legitimate ultimate authority → returned binding policy loop.
- Why this is / is not agent-owned: Tool authorization is bounded operational control, not a first-party constitutional decision with organizational reach.
- Evidence: [agent_bridge.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/agent_bridge.py), [server.py](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/engine/pico/server.py), [README.md](https://github.com/Picom-code/pico/blob/aae16319e117cd04a2b5c17ce87a3b5ad314cb71/README.md).
- Basis: structural.
- Confidence: high for local configuration/approval scope.
- Caveats: An external organization can govern human users and their Pico instances; no organization-level S5 closure is asserted here.

### Absence scope

- Surfaces inspected: Approval/model configuration, interactive plan/goal modes, credentials isolation and user-facing runtime policies.
- Plausible first-party paths checked: User permission prompts, safety restrictions, model update choices, pinned goals and plan approval.
- Why no material first-party path remains: Each concerns task authorization/configuration; no shipped identity/ultimate-policy dispute procedure or returned binding decision exists.

## Distributed OSS parent arrangement

Each independent Pico deployment is owned by its operator; open-source contributor governance and optional Hermes extensions are not a shared first-party parent metasystem for the reviewed local session. Ordinary user permission and model choice do not justify S3/S4/S5 parent modifiers.

## Self-hosted and non-human modes

The local engine may serve terminal, web and desktop on one machine and can connect to local llama.cpp or remote models. Model selection, approvals and installed Hermes availability remain external prerequisites. No evidence of a fully non-human metasystem that governs organization-level purpose or future capability was found.

## Recursion

Optional Hermes delegated helpers remain task-level agents under the parent chat. Different UI clients, session IDs, timer jobs or model backends are not separate complete viable organizations.

## Variety and escalation

The model absorbs immediate task variety, while the bridge enforces session/approval boundaries and retries repetitive loops. Missing authorization or provider configuration returns to the user; neither automatic scheduling nor inherited subagent fanout creates an additional S2–S5 decision owner.

## Evidence gaps

- No live paid-provider model/tool trace was executed; this review is structural at the frozen source ref.
- The pinned Hermes dependency's internal child coordination and memory-learning semantics were not credited as standalone Pico first-party governance functions.
- Reported performance/evaluation numbers were not independently reproduced and do not determine VSM ownership.
