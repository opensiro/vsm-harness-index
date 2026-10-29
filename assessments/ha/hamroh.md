---
harness_id: hamroh
project_name: Hamroh
repository: https://github.com/Rustam-Z/hamroh
review_ref: 0970d3a3dc8ff50970998515afe4ef79510f397e
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: P
---

# Hamroh

## Review boundary

- System in focus: one self-hosted Hamroh Telegram assistant deployment: first-party engine, Claude worker adapter, prompts/playbooks, local MCP tools/stores, scheduler and owner controls.
- Purpose and identity: a persistent operator-owned conversational assistant serving authorized chats with memory, tools and scheduled work.
- Relevant environment: Telegram users/reactions/corrections, tasks, external model/web/MCP services, pending work, failures, operator oversight and future conversational situations.
- Standard-distribution boundary: documented Docker/local deployment with Claude Code as the configured operational agent dependency. No higher functions are borrowed from Claude Code internals or external MCP products.
- Credited operating / distribution surfaces: hamroh runtime/tool/store modules; prompts/system.md and project overlay; packaged self-reflection skill; owner commands and documented restart/reload paths.
- Adjacent first-party surfaces excluded from ownership: tests/e2e, test fake MCP servers/evaluators, developer .claude workflow, repo maintenance/sync/release scripts and upstream authors' own private assistant instance.
- First-party operating / deployment modes considered: default one-turn assistant; owner-supervised controls; optional first-party subagents=true configuration with reflection enabled and packaged skills/tools available. S4=P is credited only to this supported enabled configuration; default plugins example disables Agent while the heavy-skill prompt requires it.
- Recursion level: one installed assistant across its authorized chats, current work and scheduled routines; owner is legitimate parent of that deployment.
- Reviewed revision: `0970d3a3dc8ff50970998515afe4ef79510f397e`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Telegram ingestion authenticates access, persists messages/reactions and submits formatted batches to one Engine. Engine debounces/buffers input, injects updates during active work and handles structured stop/skip/heartbeat results. CcWorker spawns/resumes the configured Claude Code process with first-party prompts, an exclusive tool surface and strict MCP configuration. That configured agent supplies task discretion; Hamroh supplies its reachable local tools, identity and feedback channels. Worker restart/liveness/error handling is deterministic support, not autonomous whole-system governance.

SQLite stores chat/reminder/tool observations; file stores retain memory, skills and the operator's project overlay. Due reminders are claimed and injected into the same engine, with success/failure callbacks preventing duplicate or lost delivery. Health/access/audit and pause/resume/reset commands bypass the conversational engine for the authenticated owner. Health exposes deployment-wide last send, reflection schedule, rate-limit notices, current turn duration and queued-message count. Owner pause/resume changes subsequent inbound admission across chats, and reset replaces the shared worker session while retaining history/memory.

The packaged reflection skill reads user corrections/reactions and recent outputs, proposes general lessons, tests 10–20 hypothetical future scenarios, records reasoning, and asks the owner to approve/refine/reject/redirect each option. Approved facts update memory; procedures update skills; standing behavior rules update project.md with backups. Skills/memory are readable through first-party tools, while prompt/skill-index changes require the documented operator restart. The worker's prompt composer reads the returned overlay on a fresh spawn. Instruction/skill write authorization is primarily model-enforced policy, not a code-level owner check, which limits the assurance of this ownership arrangement.

## Operational model

Ordinary S1 is the configured Claude-backed assistant choosing tool/response actions within Hamroh's first-party deployment contract. The optional child mode provides task delegation, not proof of recursive viability. Current whole-deployment intervention belongs to the owner, who sees aggregated operational state and can alter admission/session continuity. In the enabled reflection mode, the agent investigates proposed adaptations but the owner retains the decisive adoption right. Deployment identity/standing-policy changes likewise require the legitimate owner and return through a durable overlay; ordinary task approval is not the evidence for that S5 finding.

## S1 — Operations

- State: A
- Function: perform conversational, retrieval, memory and scheduled assistant work.
- Disturbance / variety regulated: changing requests, external observations, chat context, tool failures and incomplete long tasks.
- Decisive decision or feedback right: select tools, interpret their results, send/withhold an answer and continue long work through heartbeat.
- Decision owner: configured model-backed Claude agent running as the deployment's S1 actor.
- Supporting / enforcement mechanisms: Engine buffering, worker stream transport, local MCP tools, SQLite/memory, tool allowlists and failure recovery.
- Closure path: inbound messages/reminders reach worker.send; agent tool results and further messages drive subsequent decisions; structured turn results return to Engine and user-facing tools deliver outcomes.
- Boundary reachability: startup builds the shipped worker/tool/prompt configuration and CcWorker.start launches that operational actor. This credits the assembled Hamroh mode, not uninspected Claude governance.
- Why this is / is not agent-owned: Hamroh's transport alone cannot choose task-dependent tool calls or useful replies; those choices are made by its configured agent.
- Evidence: [hamroh/startup.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/startup.py); [hamroh/cc_worker/spec.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/cc_worker/spec.py); [hamroh/cc_worker/worker.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/cc_worker/worker.py); [hamroh/engine/engine.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/engine/engine.py); [prompts/system.md](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/prompts/system.md).
- Basis: structural.
- Confidence: high.
- Caveats: Claude Code/model service is a required external implementation dependency; no live provider execution or inherited higher-function claim.

## S2 — Coordination

- State: —
- Function: no shipped function-specific inter-S1 interference regulation is established.
- Disturbance / variety regulated: one shared conversation engine serializes ordinary turns; optional subagents perform delegated tasks.
- Decisive decision or feedback right: no specific cross-unit conflict-resolution right is packaged.
- Decision owner: parent agent chooses subtask scope; developer selects queue/tool restrictions.
- Supporting / enforcement mechanisms: single-turn buffer, reminder row claims, shared tool surface and read-only-by-default subagent guidance.
- Closure path: child results return as task data; reminder callbacks regulate delivery lifecycle, not distinct operational units' mutual adjustment.
- Why this is / is not agent-owned: message sequencing, duplicate-reminder prevention and generic delegation safety are not an S2-specific organizational path.
- Evidence: [hamroh/engine/engine.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/engine/engine.py); [hamroh/scheduler/reminder_scheduler.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/scheduler/reminder_scheduler.py); [prompts/subagents.md](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/prompts/subagents.md); [plugins.json.example](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/plugins.json.example).
- Basis: structural.
- Confidence: high.
- Caveats: The shared-identity destructive-write warning is real exposure, but no actual inter-unit conflict/oscillation and corrective coordination relation is reconstructed.

### Absence scope

- Surfaces inspected: Engine submit/control loop, scheduler claim/callbacks, optional child documentation and tool configuration.
- Plausible first-party paths checked: Concurrent chats, duplicate reminder dispatch, child results/shared tools, read-only delegation guidance.
- Why no material first-party path remains: Ordinary work is one serialized S1; child guidance constrains task safety without a specific inter-S1 disturbance/returned mutual adjustment mechanism. No S2-specific constructor is exposed.

## S3 — Inside-and-now control

- State: P
- Function: owner-governed current regulation of the whole installed assistant's admission and shared execution continuity.
- Disturbance / variety regulated: long/stuck shared turns, growing inbound queue, degraded delivery and continuing commitments across authorized chats.
- Decisive decision or feedback right: interpret global operational state and choose pause/resume of inbound operations or replacement of the shared execution session.
- Decision owner: authenticated deployment owner identified by HAMROH_OWNER_ID.
- Supporting / enforcement mechanisms: health readout, owner-ID command guard, dispatcher paused gate, worker reset/restore and status replies.
- Whole-system current view: health combines current engine duration/queue with deployment-wide last send, reflection reminder status and rate-limit notices; audit/log views add failures and storage changes.
- Current-control decision scope: all Telegram inbound admission for this bot and the common Claude session; not per-tool approval and not a claim that pause also stops the reminder scheduler.
- Closure path: owner observes current readout and selects a command; pause/resume changes dispatcher._on_message handling, and reset_session restarts the shared worker with restore context. Subsequent operations use that returned state.
- Boundary reachability: registered owner commands are direct runtime handlers available in the documented self-hosted mode, without composing a new supervisor.
- Why this is / is not agent-owned: the owner exercises current intervention discretion; deterministic worker recovery, health transport and command enforcement do not own that judgment.
- Evidence: [hamroh/telegram_io/commands.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/telegram_io/commands.py); [hamroh/telegram_io/dispatcher.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/telegram_io/dispatcher.py); [hamroh/engine/engine.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/engine/engine.py); [hamroh/cc_worker/worker.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/cc_worker/worker.py); [docs/documentation.md](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/docs/documentation.md).
- Basis: structural.
- Confidence: high.
- Caveats: Parent mode is a supported human control loop, not evidence of autonomous S3, a recorded intervention trace, or every kill/permission command being S3.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent complementary audit judgment with returned corrective control is established.
- Disturbance / variety regulated: the same assistant reviews prior outputs and owners can request diagnostic readouts.
- Decisive decision or feedback right: reflection judgment belongs to the producing assistant; /audit formats failures/backups/footprint without a separate audit mandate/judgment loop.
- Decision owner: same operational agent for self-review; owner for subsequent supervision.
- Supporting / enforcement mechanisms: raw message/reaction database, /audit and /logs, backups and reflection reasoning records.
- Closure path: self-review proposals enter owner adaptation/policy decisions; deterministic diagnostics expose data but do not install independent audit ownership.
- Why this is / is not agent-owned: self-reflection or a command named audit is not sufficiently independent complementary audit.
- Evidence: [skills/self-reflection/SKILL.md](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/skills/self-reflection/SKILL.md); [hamroh/telegram_io/commands.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/telegram_io/commands.py); [hamroh/tools/database_query.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/tools/database_query.py); [prompts/system.md](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/prompts/system.md).
- Basis: structural.
- Confidence: high.
- Caveats: Optional child isolation is task-context isolation; it does not by itself supply an independent auditor or different operational access.

### Absence scope

- Surfaces inspected: Reflection data/checklist/approval process, owner audit/log handlers, database access, child instructions and test separation.
- Plausible first-party paths checked: Raw outbound/reaction review, separate-context reflection child, diagnostic command and external test/eval surfaces.
- Why no material first-party path remains: Shipped self-review remains controlled by the assistant's own operation; diagnostics provide no independent audit judgment with a function-specific findings-to-control path. Tests are adjacent; generic child/MCP extensibility is insufficient.

## S4 — Outside-and-then intelligence

- State: P
- Function: owner-governed prospective adaptation of assistant behavior/procedures to its user environment.
- Disturbance / variety regulated: recurring user corrections, negative reactions, language/tone mismatches and rules that would misfire in future situations.
- Decisive decision or feedback right: approve, reject, refine or redirect the proposed capability/behavior change after scenario testing.
- Decision owner: deployment owner; agent owns investigation, scenario generation and proposal, not final adoption.
- Supporting / enforcement mechanisms: protected reminder seed, skill loader, SQL/memory access, reflection log, skill/instruction write tools and restart/reload.
- External distinction: actual Telegram user corrections/reactions and observed mismatches with user/group expectations, rather than internal memory growth alone.
- Future / prospective distinction: each candidate is tested on 10–20 on-target, adjacent, off-target and boundary scenarios to anticipate later misapplication.
- Adaptation option generated: proposed refined standing rule, reusable skill/playbook or environment-specific memory update with an explicit proposed destination.
- Path back into current capability / S3: owner reply selects the option/target; agent writes the approved skill or rule; current tools read memory/skills and owner restarts the worker to load modified overlay/index.
- Closure path: reflection steps 4–6 route options to the owner, parse the returned decision and execute only approved changes; step 7 states activation/restart and rollback. Subsequent work uses the changed procedure/instructions.
- Boundary reachability: startup auto-seeds the packaged skill; scheduler injects a real reminder; plugins.tool_groups.subagents=true exposes the Agent tool required by the heavy-skill prompt. This is a supported first-party flag, not custom authority wiring.
- Why this is / is not agent-owned: without owner adoption the proposals remain pending; agent scenario reasoning and storage machinery do not own the adaptation decision.
- Evidence: [skills/self-reflection/SKILL.md](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/skills/self-reflection/SKILL.md); [prompts/system.md](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/prompts/system.md); [hamroh/startup.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/startup.py); [hamroh/scheduler/reminder_scheduler.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/scheduler/reminder_scheduler.py); [hamroh/tools/skills.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/tools/skills.py); [hamroh/tools/instructions.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/tools/instructions.py); [hamroh/cc_worker/spec.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/cc_worker/spec.py); [docs/tools.md](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/docs/tools.md).
- Basis: structural.
- Confidence: high.
- Caveats: S4=P is for the supported subagents-enabled reflection mode. Default example disables Agent despite prompt-required background spawning; no successful default-mode reflection run is asserted. Write authorization is prompt-enforced and restart is human-owned.

## S5 — Policy and identity

- State: P
- Function: parent-governed deployment identity and durable operating-policy closure.
- Disturbance / variety regulated: proposed changes to bot persona, language/ethos and session-wide standing behavior, including policy proposals produced by reflection.
- Decisive decision or feedback right: the legitimate owner chooses which standing identity/behavior rule governs this bot and may dictate wording or reject it.
- Decision owner: deployment owner for ultimate policy within the parent-supplied immutable base constraints; no agent-owned ultimate authority is established.
- Supporting / enforcement mechanisms: owner metadata instructions, project overlay read/append/rewrite, backups, size/path restrictions and fresh-spawn prompt composition.
- Identity / ultimate-policy issue: whether to change the bot's identity/personality or a durable behavior default for every session, not whether one ordinary tool call may proceed.
- Ultimate authority in each claimed mode: HAMROH_OWNER_ID holder governs the installed bot's project overlay; base system.md and host-level enablement remain higher/developer constraints.
- Return-to-operation path: owner request or approved/refined reflection proposal → first-party instruction tools update project.md → owner restart/new spawn → _compose_system_prompt concatenates the returned identity/policy overlay for subsequent operation.
- Closure path: documented owner persona edits and rule adoption are persisted with backups; the worker loads that decision on the next spawn, rather than merely displaying a policy file.
- Boundary reachability: the shipped project example explicitly holds Identity & personality; system.md exposes the owner-only editing process and startup wires InstructionsStore into the local tool surface.
- Why this is / is not agent-owned: the agent applies the owner's standing decision; it cannot unilaterally promote the rule or alter immutable base policy.
- Evidence: [prompts/project.md.example](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/prompts/project.md.example); [prompts/system.md](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/prompts/system.md); [skills/self-reflection/SKILL.md](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/skills/self-reflection/SKILL.md); [hamroh/tools/instructions.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/tools/instructions.py); [hamroh/storage/instructions_store.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/storage/instructions_store.py); [hamroh/startup.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/startup.py); [hamroh/cc_worker/spec.py](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/hamroh/cc_worker/spec.py); [docs/documentation.md](https://github.com/Rustam-Z/hamroh/blob/0970d3a3dc8ff50970998515afe4ef79510f397e/docs/documentation.md).
- Basis: structural.
- Confidence: high.
- Caveats: P is bounded to the installed bot's identity/standing policy. Owner-only instruction writes rely on model policy, not a cryptographic/code authorization check; this is not a security guarantee or blanket S5 credit for access settings.

## Distributed OSS parent arrangement

The legitimate parent here is one installed bot's configured owner. Repository contributors and maintainer governance are adjacent; no organization-recursion parent arrangement is inferred.

## Self-hosted and non-human modes

Supported operator controls and durable identity editing close P modes. S4 additionally requires the documented subagents-enabled mode to satisfy the shipped heavy-skill delegation instruction. Purely default configuration is not claimed to close reflection. No internal A/C base is established for S3/S4/S5, hence standalone P rather than a composite state. No intentionally non-human organization is established.

## Recursion

Optional child tasks and background skills are bounded delegation. A fresh context window does not establish a recursively viable metasystem.

## Variety and escalation

The engine transduces chat/reminder input into worker messages; restore contexts and persistent memory preserve continuity. Backoff, liveness and tool-error recovery enforce fixed runtime bounds. Classified failures can notify the owner, but logs/alerts are not themselves S3/S4/S5. Supervisory and adaptation rights are credited only through the distinct parent return paths above.

## Evidence gaps

Source-only assessment: no Telegram, Claude/provider, browser or E2E runs. No successful reflection/policy-change trace is asserted. The shipped prompt requires background Agent for heavy reflection while plugins.json.example disables subagents; enabled optional mode is the credited S4 boundary. Prompt-enforced instruction/skill ownership can fail in practice and is not code-enforced. Changes needing restart are not effective mid-session. These limitations restrict claims without erasing the reconstructed supported parent modes.
