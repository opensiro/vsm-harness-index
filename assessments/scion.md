---
harness_id: scion
project_name: Scion
repository: https://github.com/annex-ai/scion
review_ref: 8a3e21f7d624e13eb5f14a18728c6f98172a5c55
reviewed_at: 2026-09-19
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-19
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: A
autonomy_s5: —
---

# Scion

## Review boundary

- System in focus: one first-party Scion runtime at pinned revision `8a3e21f7d624e13eb5f14a18728c6f98172a5c55`, including the interactive agent, selectable agentic loop patterns, first-party task/team delegation tools, persistent state/memory, Gateway heartbeat/cron services, and the Observe → Reflect → Coach adaptation path that is registered in the shipped Mastra runtime.
- Purpose and identity: operate an autonomous AI assistant that handles software-engineering, analysis and general tasks across messaging channels, self-directs multi-step work, can compose specialist agent teams, proactively regulates unfinished/current work, and adapts future interaction from observed user/environment feedback.
- Relevant environment: user requests and corrections, repositories/files/tools, external web and MCP services, messaging channels, model responses, background processes, persisted task/thread state, deadlines/schedules, and changing user interaction patterns.
- Standard-distribution boundary: first-party code, `.agent` configuration, role/loop instructions, registered agents/workflows/tools, Gateway services and documented self-hosted runtime in `annex-ai/scion` at the pinned revision. External model providers, MCP servers, messaging platforms, user projects and operator-authored schedules/policies are external unless a first-party Scion path itself establishes and closes the mapped function.
- Credited operating / distribution surfaces: `interactiveAgent`; shipped task-based/kimi/team loop instructions; `handoff-to-agent`; task/process tools and memory; the enabled HeartbeatService plus heartbeat alert protocol; registered Observer/Reflector/Coach agents and adaptation workflows; `AdaptationProcessor`; and first-party HTTP/tool invocation surfaces for that adaptation path.
- Adjacent first-party surfaces excluded from ownership: repository contributor/CI/release workflows for developing Scion itself; tests/examples and legacy reflection material where the current runtime does not depend on them; inline security processors and ordinary scorer/observability paths when they merely detect/measure execution; static `IDENTITY.md`/`SOUL.md`/`agent.toml` contents and human configuration edits when they do not close a runtime identity/ultimate-policy function.
- First-party operating / deployment modes considered: default single interactive-agent operation with kimi/task-style self-directed execution; first-party `agent-team` mode selected through `[loop]`; proactive heartbeat operation; agent-managed cron support; enabled adaptation processing with the Observe/Reflect/Coach workflows triggered through a shipped agent tool, HTTP workflow endpoint, or an independently composed schedule.
- Recursion level: one Scion assistant organization. In `agent-team` mode, ephemeral specialist agents are treated as bounded S1 work cells for the duration of the team operation because each receives a role, local task/environment context, optional tools and an autonomous generate loop. Their spawning alone is not treated as a lower viable recursion.
- Reviewed revision: `8a3e21f7d624e13eb5f14a18728c6f98172a5c55`.
- Observation date: 2026-09-19.
- Generated Profile version: `0.2.3`.
- Generated Methodology version: `0.3.5`.
- Current Profile version: `0.2.3`.
- Current Methodology version: `0.3.5`.

## Repository architecture

Scion is a TypeScript/Mastra autonomous-agent runtime. The main `interactiveAgent` loads identity/soul/user context, persistent memory, built-in and MCP tools, selectable loop-pattern instructions, skills/workflows, input/output processors and scorer support. The loop contract gives the model agent substantive authority over decomposition, sequencing, tool choice, delegation, replanning and completion rather than reducing it to a deterministic workflow executor.

The first-party `agent-team` mode creates a stronger organization than generic delegation. The interactive agent becomes team lead, defines complementary roles and shared context, assigns interdependent work through `handoff-to-agent`, reviews specialist outputs, checks interface consistency, returns revision feedback and can add roles or break circular dependencies. Each handoff instantiates a separate model-driven specialist with its own task and optional tool repertoire.

Scion also ships a current-control loop. `HeartbeatService` periodically reads current task/background-process state, identifies blocked, failed, overdue or pending items, and sends a structured alert back into the interactive agent. The heartbeat prompt explicitly leaves the response choice to the agent: resume, reprioritize, retry, investigate, continue, request missing input or escalate. The deterministic service senses and transports the exception; the model-driven agent owns the current-control judgment.

A separate adaptation subsystem implements Observe → Reflect → Coach. The Observer reads persisted conversation exchanges directly and extracts corrections, frustration, repeated requests, workflow friction, preferences and coaching opportunities. The Reflector independently synthesizes those observations into persistent patterns/guidance and contradictions. The Coach turns sufficiently supported patterns into future suggestions. `AdaptationProcessor` then injects learned patterns and matching suggestions into later interactive-agent system context and records implicit user response. This is a closed prospective adaptation path. The same direct-transcript Observer path also supplies a function-specific complementary audit construction path, but the standard runtime does not make independent audit invocation an unavoidable part of the ordinary production lifecycle, so S3* is published as `C`, not `A`.

Primary evidence:

- [`README.md`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/README.md) — autonomous runtime architecture, multi-agent roles, loop patterns, tool surface, Gateway services and adaptation overview.
- [`.agent/agent.toml`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/.agent/agent.toml) — shipped identity, loop/team limits, enabled heartbeat/cron/reflection services and enabled adaptation configuration.
- [`src/mastra/agents/interactive.ts`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/src/mastra/agents/interactive.ts) — primary agent registration, loop/heartbeat instructions, memory/tools/workflows, adaptation input processor and ordinary scorers.
- [`src/mastra/lib/loop-patterns/task-based.ts`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/src/mastra/lib/loop-patterns/task-based.ts) — explicit agent authority over decomposition, task priority, tools, delegation, replanning and STOP/CONTINUE.
- [`src/mastra/lib/loop-patterns/agent-team.ts`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/src/mastra/lib/loop-patterns/agent-team.ts) — team composition, dependencies, interface-consistency review, revision feedback and deadlock handling.
- [`src/mastra/tools/handoff-agent.ts`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/src/mastra/tools/handoff-agent.ts) — first-party ephemeral specialist creation with role/task/shared context and autonomous generation.
- [`docs/HEARTBEAT_SYSTEM.md`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/docs/HEARTBEAT_SYSTEM.md) and [`src/mastra/lib/instructions/heartbeat.ts`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/src/mastra/lib/instructions/heartbeat.ts) — current-state sensing and agent-owned resume/retry/escalation response.
- [`docs/ADAPTATION_SYSTEM.md`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/docs/ADAPTATION_SYSTEM.md) — Observe → Reflect → Coach architecture, pattern lifecycle, delivery and feedback.
- [`src/mastra/workflows/observe-workflow.ts`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/src/mastra/workflows/observe-workflow.ts), [`src/mastra/agents/observer.ts`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/src/mastra/agents/observer.ts), [`src/mastra/workflows/reflect-workflow.ts`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/src/mastra/workflows/reflect-workflow.ts), and [`src/mastra/workflows/coach-workflow.ts`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/src/mastra/workflows/coach-workflow.ts) — separate observation, synthesis and adaptation-option judgments.
- [`src/mastra/processors/adaptation-processor.ts`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/src/mastra/processors/adaptation-processor.ts) — learned-pattern/suggestion return path into future operational context and implicit feedback.
- [`src/mastra/client.ts`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/src/mastra/client.ts) and [`src/mastra/tools/index.ts`](https://github.com/annex-ai/scion/blob/8a3e21f7d624e13eb5f14a18728c6f98172a5c55/src/mastra/tools/index.ts) — Observer/Reflector/Coach and adaptation workflows are registered in the standard runtime; `trigger-adaptation` is exposed to the main agent.

## Operational model

The ordinary S1 is the interactive agent executing user or proactive tasks through its model/tool loop. In `agent-team` mode, the lead dynamically creates specialist S1 work cells for interdependent components. Those specialists are not counted merely because they are spawned: the positive S2 witness rests on the first-party team contract that gives them distinct role-specific outcomes and explicitly regulates dependency/interface interference among their outputs.

Current-control variety is handled through two connected paths. During active team work, the lead owns task assignments, dependency order, revision decisions and team changes. Across ongoing assistant work, HeartbeatService provides a current exception view of pending/blocked/high-priority tasks and failed/long-running background work, while the interactive agent decides the intervention. The heartbeat scheduler itself therefore supports S3 but does not own it.

The adaptation organization is distinct from ordinary task execution. It reads actual conversation history, produces model-driven observations/patterns/options, persists them, and returns them into subsequent operational context. This closes S4. For S3*, the same raw-history path is materially complementary to the main agent's ordinary self-report/output, but an independently controlled audit trigger still requires deployment composition; Scion therefore exposes an S3*-specific constructor path rather than a fully autonomous audit mode.

## S1 — Operations

- State: A
- Function: autonomously execute bounded user or proactive work through iterative reasoning, tool use, state updates, delegation and completion decisions.
- Disturbance / variety regulated: request ambiguity, repository/tool/environment results, failures, changing intermediate state, background-process output and newly discovered subtasks.
- Decisive decision or feedback right: choose decomposition and priorities, select tools/actions, delegate when useful, replan after observations and decide whether to continue or declare the operational goal complete.
- Decision owner: the model-driven Scion interactive agent.
- Supporting / enforcement mechanisms: Mastra Agent runtime, configured iteration/step/retry limits, task tools, memory, MCP/local tools, process registry, skills/workflows and deterministic stop/enforcement plumbing.
- Closure path: request/proactive alert enters the interactive agent → agent creates/chooses work and tool actions → environment/tool results return → agent updates state/replans/continues → final operational result or justified escalation is returned.
- Boundary reachability: `interactiveAgent`, its loop instructions, tools, memory and registered workflows are shipped and wired in the standard self-hosted runtime at the pinned revision.
- Why this is / is not agent-owned: configuration bounds the repertoire, but the substantive next-action, task-priority, tool, delegation, replan and completion choices are explicitly assigned to the model agent.
- Evidence: `src/mastra/agents/interactive.ts`, `src/mastra/lib/loop-patterns/task-based.ts`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: external model inference and tool services are dependencies; the ownership claim concerns the running Scion agent organization and its first-party control contract.

## S2 — Coordination

- State: A
- Function: regulate dependency and interface interference among multiple role-specific specialist work cells in the shipped `agent-team` mode so their independently produced components remain mutually coherent.
- Disturbance / variety regulated: specialists working on interconnected components can produce mismatched interfaces, inconsistent assumptions, circular dependencies, missing cross-context or outputs that require revision after another member's result becomes known.
- Decisive decision or feedback right: define team roles/shared context, assign work and dependency order, evaluate cross-member consistency, decide whether revision is needed, return updated constraints/context, add or change a role, and break deadlocks with intermediate artifacts.
- Decision owner: the model-driven interactive agent acting as team lead.
- Supporting / enforcement mechanisms: `handoff-to-agent`, shared-context fields, configurable team/member limits, role-specific ephemeral Agent instances and returned specialist results.
- Closure path: lead decomposes an interdependent goal into specialist roles → specialists independently execute assigned work → results return to lead → lead checks dependencies/interfaces → mismatches trigger revised handoffs or team changes with updated context → coherent outputs are finally compiled.
- Boundary reachability: `agent-team` is a shipped selectable loop pattern and `handoff-to-agent` is registered in the standard tool set; choosing the supported pattern does not require an adopter to implement a new coordination actor or feedback loop.
- Why this is / is not agent-owned: once the first-party team mode is selected, the lead agent owns concrete composition, dependency, review and revision decisions; deterministic handoff code only instantiates and transports those decisions.
- Evidence: `src/mastra/lib/loop-patterns/agent-team.ts`, `src/mastra/tools/handoff-agent.ts`, `.agent/agent.toml`, `README.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: generic `delegate-to-agent` or mere spawning would not establish S2. The positive mapping depends on the explicit shared-context/dependency/interface-review/revision relation of `agent-team`.
- Distinct S1 units: two or more handoff-created specialist Agents, each with a separate role, bounded assignment, local context/tool repertoire and model-driven work outcome, under the team lead for the duration of the operation.
- Inter-S1 disturbance: interdependent specialist outputs can disagree at component interfaces, depend on unavailable results, form circular dependencies or become inconsistent as another member's completed work changes the shared constraints.
- Attenuating coordination relation: the lead supplies common project context, manages dependency order, reviews interfaces and consistency, issues revision handoffs with other members' updated outputs, and can create intermediate artifacts to break deadlock.
- Feedback into subsequent S1 behaviour: specialist results enter the lead's review; failed consistency checks cause new/revised handoffs carrying explicit feedback and updated cross-member context, changing the next specialist execution.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the first-party pattern explicitly names and repairs concrete cross-unit dependency/interface mismatches and deadlocks rather than only assigning independent subtasks or moving messages.

## S3 — Inside-and-now control

- State: A
- Function: maintain a current view of Scion's active commitments and intervene on behalf of the whole assistant/team when work is pending, blocked, failing, stalled or internally inconsistent.
- Disturbance / variety regulated: competing/pending tasks, blocked commitments, high-priority work, failed or long-running background processes, team dependency changes, quality gaps and work requiring reallocation/revision.
- Decisive decision or feedback right: choose what current work to resume or prioritize, whether to continue/retry/investigate/escalate, how to change team composition/assignments/dependencies, and whether specialist output requires revision before the organization proceeds.
- Decision owner: the model-driven interactive agent/team lead.
- Supporting / enforcement mechanisms: HeartbeatService current-state scans, persisted heartbeat/task/process state, alert thresholds/deduplication, task/process tools, team limits and handoff machinery.
- Closure path: heartbeat/team results expose current commitments/exceptions → interactive agent evaluates them in current context → agent resumes/retries/reprioritizes/reassigns/revises or escalates → task/team/background-process behavior changes → updated state/results feed later heartbeat/team decisions.
- Boundary reachability: HeartbeatService is enabled in the shipped configuration and returns alerts directly to the registered interactive agent; the team-lead control contract and task/process tools are likewise standard first-party runtime surfaces.
- Why this is / is not agent-owned: the heartbeat service deterministically detects and transports current exceptions, but its documentation and injected protocol explicitly leave the substantive action choice to the agent; team limits similarly enforce bounds without owning prioritization/revision decisions.
- Evidence: `docs/HEARTBEAT_SYSTEM.md`, `src/mastra/lib/instructions/heartbeat.ts`, `src/mastra/lib/loop-patterns/agent-team.ts`, `src/mastra/lib/loop-patterns/task-based.ts`, `.agent/agent.toml`.
- Basis: explicit + structural
- Confidence: high
- Caveats: this assessment does not treat a scheduler, threshold or process kill mechanism as S3 ownership; `A` rests on the model-driven response and current team/commitment decisions.
- Whole-system current view: the agent receives persisted task-state distinctions (pending/high-priority/blocked), background-process failure/stall distinctions and, in team mode, the current plan/assignments/dependencies/member outputs being coordinated.
- Current-control decision scope: active task priority, resume/retry/investigate/escalate choices, current team composition and assignment/dependency changes, specialist revision acceptance and replanning after blockers/failures.

## S3* — Complementary audit

- State: C
- Function: provide a complementary path that can challenge the ordinary interactive agent's own account/output quality by reading persisted user/assistant interaction evidence directly and identifying corrections, frustration, repeated requests, workflow friction and contradictory learned patterns.
- Disturbance / variety regulated: ordinary completion/self-assessment can miss evidence that the result or interaction was unsatisfactory, repeatedly misunderstood, inefficient or contradicted by later user feedback.
- Decisive decision or feedback right: independently inspect raw conversation exchanges, classify material challenge signals, synthesize/revise patterns and contradictions, then return findings into later operational context/coaching.
- Decision owner: the first-party Observer and Reflector agents supply the audit judgments once the audit/adaptation workflow is independently invoked; the deployment still owns composition of a sufficiently independent trigger relative to the main production path.
- Supporting / enforcement mechanisms: persistent memory-store access, Observe/Reflect workflow orchestration, adaptation storage/state machine, HTTP workflow endpoint, `trigger-adaptation` tool and `AdaptationProcessor` return path.
- Closure path: persisted raw exchanges are read outside the main response path → Observer extracts corrective/challenge evidence → Reflector matches/revises/contradicts patterns → findings persist → `AdaptationProcessor` injects the resulting learned guidance into later main-agent context and behavior.
- Boundary reachability: the Observer/Reflector agents and Observe/Reflect/adaptation workflows are registered in the standard Mastra runtime and can be reached through first-party HTTP/tool surfaces; an adopter does not need to implement the audit logic itself, only establish an appropriately independent invocation arrangement if S3* independence is required.
- Why this is / is not agent-owned: audit judgment is model-driven and separate from the producing interactive agent, but the pinned standard lifecycle does not force an independently controlled audit run after ordinary operation. That missing independence composition prevents `A` while the audit-specific first-party path supports `C`.
- Evidence: `src/mastra/client.ts`, `src/mastra/workflows/observe-workflow.ts`, `src/mastra/agents/observer.ts`, `src/mastra/workflows/reflect-workflow.ts`, `docs/ADAPTATION_SYSTEM.md`, `src/mastra/processors/adaptation-processor.ts`.
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: the path is also part of S4 adaptation, but the S3* mapping uses a distinct organizational right: complementary challenge of ordinary interaction claims from raw persisted evidence. Inline toxicity/relevancy/security scorers are not used as the positive S3* witness.
- Claim being audited: that the ordinary interactive agent's prior interaction/output behavior adequately served the user without persistent misunderstandings, correction signals or workflow friction that its own completion path failed to surface.
- Ordinary reporting path: the interactive agent executes a request, self-assesses/declares completion and returns its output through the normal conversation path.
- Complementary access path: Observe reads persisted raw user/assistant exchanges directly from the memory store and sends them to a separately prompted Observer agent; Reflector then analyzes the extracted evidence against durable patterns, including contradictions.
- Independence boundary: judgment is separated into dedicated Observer/Reflector agents with direct transcript access rather than relying on the interactive agent's self-report, but invocation independence from that main agent is not guaranteed by the pinned default lifecycle and therefore remains constructor work.
- Who acts on findings: the interactive agent subsequently receives the persisted learned pattern/guidance and matching coaching via `AdaptationProcessor`; deployment can additionally inspect or trigger the workflow through the first-party HTTP surface.

## S4 — Outside-and-then intelligence

- State: A
- Function: model changing user/environment interaction patterns and develop future-facing adaptations that alter how the current assistant behaves in later conversations.
- Disturbance / variety regulated: repeated user corrections, frustration, preference drift, workflow friction, recurring skill gaps, coaching opportunities and evidence that previously useful patterns are becoming stale or contradictory.
- Decisive decision or feedback right: identify which environmental interaction signals matter, synthesize/reinforce/contradict durable patterns, generate guidance/coaching options from sufficiently supported patterns and allow those options to shape later operational responses.
- Decision owner: the model-driven Observer, Reflector and Coach agents across the first-party adaptation pipeline.
- Supporting / enforcement mechanisms: conversation-memory access, adaptation workflow orchestration, locks/storage, confidence/occurrence thresholds, pattern state machine, preference filters, deduplication, trigger matching and the `AdaptationProcessor` context injection mechanism.
- Closure path: past user/environment interactions → Observer extracts signals → Reflector develops/updates future-relevant patterns and guidance → Coach generates adaptation suggestions → persisted patterns/suggestions are injected into later interactive-agent system context → subsequent responses change and user engagement feeds adaptation metrics.
- Boundary reachability: all three adaptation agents/workflows are registered in the standard runtime, adaptation is enabled in the shipped config, and `AdaptationProcessor` is wired into every interactive-agent input; workflow execution is exposed through first-party tool/HTTP/scheduling surfaces.
- Why this is / is not agent-owned: deterministic thresholds, storage and filtering constrain the path, but the material observation, pattern/guidance synthesis and coaching-option judgments are made by dedicated model agents, and the return path into future capability is already wired.
- Evidence: `docs/ADAPTATION_SYSTEM.md`, `.agent/agent.toml`, `src/mastra/workflows/observe-workflow.ts`, `src/mastra/agents/observer.ts`, `src/mastra/workflows/reflect-workflow.ts`, `src/mastra/workflows/coach-workflow.ts`, `src/mastra/processors/adaptation-processor.ts`, `src/mastra/client.ts`.
- Basis: explicit + structural
- Confidence: high
- Caveats: this is not credited merely because Scion has memory or a component named adaptation. The positive mapping rests on environment-derived distinctions, generated future guidance/options, and their first-party return into later operation. No distinct parent-owned S4 decision mode is established by user coaching preferences or manual HTTP triggering alone.
- External distinction: actual user corrections, frustration, repeated requests, positive feedback, workflow friction, preference signals and coaching opportunities extracted from conversation history.
- Future / prospective distinction: durable pattern validation/staleness/contradiction plus coaching generation are explicitly intended to improve future interactions rather than only summarize past state.
- Adaptation option generated: learned guidance attached to synthesized patterns and structured coaching suggestions with future trigger conditions, filtered using user preference and acceptance history.
- Path back into current capability / S3: `AdaptationProcessor` injects active/validated learned patterns and matching coaching opportunities as system context for later interactive-agent turns, changing the information and guidance under which present operation is chosen.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy decision loop is established at the reviewed assistant boundary.
- Disturbance / variety regulated: Scion has identity, soul, personality, security and user-preference configuration, but the reviewed runtime does not expose a function-specific process in which an identity/ultimate-policy issue is recognized, decided by legitimate ultimate authority and returned to govern later operation.
- Decisive decision or feedback right: none established for a qualifying S5 function.
- Decision owner: none established.
- Supporting / enforcement mechanisms: `.agent/IDENTITY.md`, `.agent/SOUL.md`, `.agent/agent.toml`, security processors/feature flags, user preferences, generic file-edit tools and operator configuration.
- Closure path: not applicable; these surfaces load or enforce previously supplied identity/constraints, but no reviewed first-party path closes a runtime identity/ultimate-policy dispute/proposal into a new authoritative policy decision.
- Why this is / is not agent-owned: the interactive agent operates under loaded identity/soul text and can update ordinary user preferences, but a prompt/configuration file or editable constraint is not itself ultimate policy authority.
- Evidence: `README.md`, `.agent/agent.toml`, `src/mastra/agents/interactive.ts`, `src/mastra/processors/user-preferences.ts` and the Soul/configuration documentation paths inspected at the pinned revision.
- Basis: explicit + absence review
- Confidence: high
- Caveats: an operator can edit identity/config files and the agent has generic file tools, but neither is a function-specific S5 closure path under Profile 0.2.3.

### Absence scope

- Surfaces inspected: identity/soul/user configuration, interactive-agent instruction loading, user-preference update path, security configuration/processors, generic file/tool authority, agent-team/heartbeat escalation paths, adaptation subsystem, Gateway/HTTP control and repository governance-adjacent material.
- Plausible first-party paths checked: runtime identity hot reload, preference updates, operator config edits, security blocking, user escalation, tool-mediated self-editing and adaptation-generated guidance.
- Why no material first-party path remains: each inspected path either supplies static/dynamic context, ordinary preference/safety control or task-level escalation. None establishes an identity/ultimate-policy issue → legitimate ultimate authority → authoritative decision → returned operation loop at the assessed recursion.

## Recursion

Scion can instantiate task agents and ephemeral team-member agents, but spawning/nesting is not sufficient evidence of VSM recursion. The handoff specialists have meaningful local operational autonomy and therefore can serve as S1 units at the assistant-team boundary, yet the pinned evidence does not show each such transient unit independently closing its own S2-S5 metasystem and durable identity/environment relation. No lower fully viable recursion is credited.

## Variety and escalation

Scion attenuates task/environment variety through skills, shared team context, memory, task state, tool boundaries and configurable loop limits, while amplifying response capacity through model-driven replanning, specialist handoffs, MCP/local tools and proactive services. In team mode, dependency/interface conflicts are returned to the lead for alignment/revision instead of being left to mutually unaware workers.

Heartbeat creates an explicit exception channel for high-priority, blocked, failed, long-running and pending work. The main agent owns the response within its authority: resume, retry, investigate or change the current plan. When the condition cannot be resolved locally — for example a blocked task requiring missing user input or a permanent background failure — the heartbeat protocol requires escalation to the user. This is evidence of bounded escalation, not S5 by itself.

The adaptation path preserves a different kind of variety: user corrections, frustration and workflow friction are not compressed into generic memory alone; separate observers classify them, patterns can be contradicted/staled, and later guidance returns into operation.

## Evidence gaps

- The pinned documentation describes the adaptation master as typically scheduled and exposes HTTP/tool invocation, while the inspected standard Gateway lifecycle does not show an unavoidable dedicated adaptation scheduler comparable to HeartbeatService. This is why S3* is `C` rather than `A`; an independently controlled audit trigger must still be composed.
- The S2 mapping depends on the supported `agent-team` operating mode rather than the default `kimi-loop`. The path is first-party and complete once selected, so this affects mode scope rather than ownership.
- Ephemeral team-member agents are credited only as bounded S1 work cells at the parent assistant-team recursion; no lower recursive viability is inferred.
- Inline security processors and response scorers were inspected but not promoted to S3* because they are ordinary production-path checks/measurements rather than the complementary audit witness used here.
- No first-party parent-governed S3/S4/S5 mode was established merely from operator configuration, user preferences, HTTP triggering or generic human interaction.