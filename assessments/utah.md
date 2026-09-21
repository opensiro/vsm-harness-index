---
harness_id: utah
project_name: Utah
repository: https://github.com/inngest/utah
review_ref: b3aeb81c076f2a03d78fc291417c55439f796d61
reviewed_at: 2026-09-21
generated_profile_version: 0.2.3
generated_assessment_procedure_version: 0.3.5
profile_version: 0.2.3
assessment_procedure_version: 0.3.5
assessment_changed_at: 2026-09-21
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: A
autonomy_s5: —
---

# Utah

## Review boundary

- System in focus: one shipped Utah personal/event-driven agent-harness installation at frozen revision `b3aeb81c076f2a03d78fc291417c55439f796d61`, including the first-party think/act/observe loop, message/sub-agent functions, workspace memory/skills surfaces and the `utah-sidecar` dynamic function loader.
- Purpose and identity: receive user or event work, perform model-driven tool action, preserve useful operating knowledge, and extend future operation with durable skills and event/scheduled functions.
- Relevant environment: users and messaging channels, external web/tool targets, model providers, Inngest Cloud, channel APIs, filesystem/workspace state, recurring schedules and external events.
- Standard-distribution boundary: repository-shipped TypeScript worker, main agent loop, first-party Inngest function definitions, workspace/context/skill machinery, sidecar loader and bundled skill guides. Inngest Cloud, `pi-ai`, `pi-coding-agent`, external model providers, channel services and user-authored external services remain dependencies rather than inherited organizational owners.
- Credited operating / distribution surfaces: `src/agent-loop.ts`, `src/functions/message.ts`, first-party sub-agent invocation paths, `src/lib/tools.ts`, context/skill loading, the bundled skill-authoring guides and `src/sidecar/sidecar.ts`.
- Adjacent first-party surfaces excluded from ownership: repository CI/tests/development workflows, documentation-only examples not wired into runtime, and generated downstream user functions considered only after the shipped Utah runtime creates/loads them through the supported workspace path.
- First-party operating / deployment modes considered: channel/message execution, synchronous/async/scheduled sub-agent delegation, persistent workspace skill use, and sidecar-loaded cron/event workflows.
- Recursion level: one Utah installation. The main model/tool loop is the primary S1. First-party sub-agent invocations can execute subordinate operational loops, but their plurality is not itself evidence of S2 or S3. Sidecar functions are future capability mechanisms unless a particular function independently satisfies an organizational-function test.
- Reviewed revision: `b3aeb81c076f2a03d78fc291417c55439f796d61`.
- Observation date: 2026-09-21.
- Generated Profile version: 0.2.3.
- Generated Methodology version: 0.3.5.
- Current Profile version: 0.2.3.
- Current Methodology version: 0.3.5.

## Repository architecture

Utah ships its own durable model/tool execution loop rather than only configuring another agent product. `createAgentLoop()` loads workspace context and session history, asks the model for the next action, executes model-selected tools as Inngest steps, feeds tool results back into the conversation, and repeats until the model returns text or reaches the configured bound. `agent-handle-message` persists incoming work and the resulting response around that loop.

Utah also exposes synchronous, asynchronous and scheduled sub-agent delegation. Those paths create real additional operational runs, but they are task-distribution mechanisms: the reviewed standard distribution does not expose a whole-current subordinate portfolio regulator or a concrete inter-S1 disturbance/attenuation relation merely because multiple runs can exist.

The distinctive future-adaptation path is the workspace plus sidecar. The main agent has first-party `write`, `edit` and `bash` access to the workspace. Bundled skill guidance explicitly tells the agent to create persistent skills when it learns a reusable process, convention, technique or repeatable workflow. The bundled Inngest-function guide teaches it to write cron/event/multi-step functions under `workspace/functions/`. `utah-sidecar` watches that directory, dynamically imports changed functions and reconnects them to Inngest without a restart, deploy step or human action. A generated future function can itself emit `agent.message.received`, returning environmental findings to the main operational loop.

Static identity/context files, retries, singleton execution, observability and memory distillation are inspected below by function rather than promoted from their labels.

## Operational model

A user/channel event reaches `agent-handle-message`, which persists the input and starts Utah's first-party loop. The model chooses substantive tool actions; Utah executes them and returns observations to the next model call. The resulting response is persisted and emitted back through the configured channel.

When the model encounters a reusable future need, the shipped workspace/tool/skill arrangement gives it a direct route to encode that adaptation. It can write a persistent skill for later prompt-time use and/or author a durable sidecar function triggered by future time or events. The sidecar detects the file change and makes that function operational automatically. This is credited as S4 because it changes future operating repertoire from learned/environmental distinctions; mere memory persistence is not the witness.

## S1 — Operations

- State: A
- Function: perform user- or event-directed work through a model-driven think/action/tool-observation loop.
- Disturbance / variety regulated: ambiguous requests, external web/filesystem/tool state, tool failures, model responses, changing conversation context and returned subordinate results.
- Decisive decision or feedback right: choose substantive next tool/action steps from current context and observations and decide when to return an operational result.
- Decision owner: the running Utah model agent.
- Supporting / enforcement mechanisms: `createAgentLoop`, first-party tool dispatch, Inngest durable steps/retries, session/context persistence, compaction/pruning, model-provider adapter and channel/event transport.
- Closure path: user/event work → model decision → selected tool/sub-agent action → first-party execution → observation returned to the model → revised action or final response → persisted/emitted result.
- Boundary reachability: the repository-shipped worker enters `agent-handle-message`, which directly invokes the first-party Utah loop; no downstream harness implementation is required.
- Why this is / is not agent-owned: Inngest and Utah runtime code provide durable execution and enforce bounds, while the model actor owns the discretionary choice of substantive next action from current evidence.
- Evidence: [`README.md`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/README.md), [`src/agent-loop.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/agent-loop.ts), [`src/lib/tools.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/lib/tools.ts), [`src/functions/message.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/functions/message.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `pi-ai`, `pi-coding-agent` and model providers supply execution/tool substrate but are not imported as organizational owners.

## S2 — Coordination

- State: —
- Function: no material first-party path establishes regulation of a concrete interference, conflict or oscillation among at least two distinct S1 units.
- Disturbance / variety regulated: not established as S2 at the reviewed recursion.
- Decisive decision or feedback right: not established for S2.
- Decision owner: not established for S2.
- Supporting / enforcement mechanisms: per-session singleton cancellation, synchronous/async/scheduled delegation, event routing and shared workspace state exist, but none is credited without the Profile-required inter-S1 disturbance relation.
- Closure path: not applicable.
- Why this is / is not agent-owned: `singleton: { key: sessionKey, mode: "cancel" }` prevents overlapping runs of the same conversation, but duplicate/current runs of one conversational unit are not evidence of two distinct S1 units. Delegation and event transport likewise do not establish S2 by themselves.
- Evidence: [`src/functions/message.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/functions/message.ts), [`src/agent-loop.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/agent-loop.ts), [`src/lib/tools.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/lib/tools.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a downstream organization of multiple Utah agents could add an S2 relation, but that relation is not supplied by the reviewed standard distribution.

### Absence scope

- Surfaces inspected: same-session singleton/cancel semantics, sync/async/scheduled sub-agent delegation, event-driven function composition, shared workspace/memory and sidecar function execution.
- Plausible first-party paths checked: singleton cancellation as coordination; sub-agent delegation as coordination; event bus/message routing as coordination; shared filesystem state as coordination.
- Why no material first-party path remains: the inspected mechanisms prevent duplicate same-unit work or distribute/transport work, but do not establish two distinct S1 units plus a specific cross-unit disturbance, S2-specific attenuation and feedback into subsequent S1 behaviour.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party path establishes whole-system current regulation over a portfolio of operational units or commitments.
- Disturbance / variety regulated: not established as S3 at the reviewed recursion.
- Decisive decision or feedback right: not established for whole-current-system control.
- Decision owner: not established for S3.
- Supporting / enforcement mechanisms: the main agent can start sync/async/scheduled sub-agent work; Inngest enforces retries/singleton/cancellation; failure and heartbeat functions maintain execution continuity.
- Closure path: not applicable as S3.
- Why this is / is not agent-owned: creating a subordinate task is delegation, not whole-system regulation. The reviewed Utah tool surface does not give the model a first-party current portfolio view plus discretionary list/inspect/reprioritize/cancel/reallocate authority across ongoing subordinate commitments.
- Evidence: [`src/agent-loop.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/agent-loop.ts), [`src/lib/tools.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/lib/tools.ts), [`src/functions/message.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/functions/message.ts).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: Inngest may expose infrastructure-level run management outside Utah, but external platform controls are not inherited as Utah-owned S3.

### Absence scope

- Surfaces inspected: delegation tools and their execution paths, message singleton/cancel, retries, scheduled events, sidecar connection/reload behavior, heartbeat/failure handling and user-facing tool set.
- Plausible first-party paths checked: parent delegation as S3; singleton/cancel as S3; retries/failure handling as S3; scheduled sub-agents as current portfolio control; sidecar lifecycle as current-control authority.
- Why no material first-party path remains: these mechanisms create, transport, retry or cancel specific execution paths but do not provide an autonomous whole-current-system view and regulatory choice over the operational portfolio.

## S3* — Complementary audit

- State: —
- Function: no material first-party path establishes sufficiently independent complementary access to operational reality plus corrective return into S1/S3.
- Disturbance / variety regulated: not established as S3* at the reviewed boundary.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: durable step observability, retries, failure notification, session logs, memory distillation and optional user-authored review functions provide execution evidence or future extensibility rather than a shipped independent auditor.
- Closure path: not applicable.
- Why this is / is not agent-owned: ordinary tool results are already the production feedback path; Inngest observability/retry is execution infrastructure; memory summarization changes retained context; a hypothetical generated review loop is not a standard-distribution audit owner until such a loop actually exists and closes the S3* function.
- Evidence: [`README.md`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/README.md), [`src/agent-loop.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/agent-loop.ts), [`src/sidecar/sidecar.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/sidecar/sidecar.ts).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: the sidecar makes independent review workflows constructible, but constructor/extensibility potential is not a positive S3* mapping without the function-specific closing path.

### Absence scope

- Surfaces inspected: tool-observation loop, retries/failure handling, Inngest observability, session/history storage, memory heartbeat/distillation, sidecar-loaded functions and documented review-function examples.
- Plausible first-party paths checked: observability as audit; retry/failure notification as audit; memory distillation as audit; generated `*-review` functions as audit.
- Why no material first-party path remains: no shipped path adds materially independent operational-reality access and a distinct judgment that is returned into corrective current control.

## S4 — Outside-and-then intelligence

- State: A
- Function: turn learned or anticipated reusable environmental/workflow distinctions into persistent future capabilities that change later Utah operation.
- Disturbance / variety regulated: recurring external events, monitoring needs, repeated workflows, newly learned API/codebase/process patterns, user-taught reusable practices and techniques that should survive the current conversation.
- Decisive decision or feedback right: decide that a learned/current distinction warrants durable future adaptation and choose what reusable skill or event/scheduled function to create or update.
- Decision owner: the running Utah model agent, using its normal first-party workspace tools under the bundled adaptation guidance.
- Supporting / enforcement mechanisms: first-party `write`/`edit`/`bash` tool access to the workspace, `creating-skills.md`, `inngest-functions.md`, prompt-time skill indexing/loading, the sidecar file watcher/dynamic import/reconnect path and Inngest's durable event/cron execution substrate.
- Closure path: operational/user/environmental experience → model recognizes a reusable or prospective need → agent writes/updates a workspace skill and/or `workspace/functions/*.ts` function → later conversations load the changed skill and/or `utah-sidecar` hot-loads the function → future cron/event executes the new capability → resulting action or `agent.message.received` event changes later operation.
- Boundary reachability: the standard main agent already has the file tools required to mutate its workspace, bundled Utah skills explicitly teach the agent when/how to create persistent skills and dynamic functions, and the shipped sidecar watches/loads those functions without downstream deployment code or human approval.
- Why this is / is not agent-owned: Inngest supplies durable scheduling/execution and the sidecar mechanically loads valid files, but the model agent owns the discretionary adaptation decision and authors the new future-facing repertoire. Removing that agent leaves the loader but not the choice of what learned capability to create.
- Evidence: [`README.md`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/README.md), [`src/lib/tools.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/lib/tools.ts), [`src/lib/context.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/lib/context.ts), [`skills/creating-skills.md`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/skills/creating-skills.md), [`skills/inngest-functions.md`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/skills/inngest-functions.md), [`src/sidecar/sidecar.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/sidecar/sidecar.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: memory distillation, self-editing and file writing are not credited alone. The positive mapping rests on the prospective adaptation loop that introduces durable reusable skills/functions into future execution.
- External distinction: recurring environmental events, reusable workflow patterns, newly learned techniques and user-taught practices that matter beyond the present conversation.
- Future / prospective distinction: the selected adaptation is encoded for later conversations, scheduled times or future events rather than only repairing the current turn.
- Adaptation option generated: create or revise a persistent workspace skill and/or author a new durable Inngest cron/event/multi-step function.
- Path back into current capability / S3: later prompt construction loads changed skills; the sidecar hot-loads changed functions, whose future execution can act directly or emit `agent.message.received` back into Utah's operational loop.

## S5 — Policy and identity

- State: —
- Function: no material first-party path establishes identity- or ultimate-policy-level adjudication that closes unresolved present/future tension for the Utah organization.
- Disturbance / variety regulated: not established as S5 at the reviewed recursion.
- Decisive decision or feedback right: not established for identity/ultimate policy.
- Decision owner: not established for S5.
- Supporting / enforcement mechanisms: `IDENTITY.md`, `SOUL.md`, `USER.md`, environment configuration and ordinary user instructions shape behavior; the agent's file tools can modify workspace files.
- Closure path: not applicable as S5.
- Why this is / is not agent-owned: editable identity/persona text is configuration and context. The reviewed runtime does not establish a legitimate identity-level issue/proposal → ultimate authority → returned policy decision path, nor an autonomous actor authorized to settle S3–S4 tension at that level.
- Evidence: [`README.md`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/README.md), [`src/lib/context.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/lib/context.ts), [`src/lib/tools.ts`](https://github.com/inngest/utah/blob/b3aeb81c076f2a03d78fc291417c55439f796d61/src/lib/tools.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a parent user can edit identity/policy files, but generic configuration authority is not S5 without a qualifying identity/ultimate-policy decision and closure path.

### Absence scope

- Surfaces inspected: `IDENTITY.md`/`SOUL.md`/`USER.md` prompt assembly, workspace write/edit/bash capability, environment configuration, user messages, sidecar/skill self-modification and documented operating guidance.
- Plausible first-party paths checked: SOUL/IDENTITY files as S5; model self-editing as S5; user instruction as parent-governed S5; sidecar function creation as policy evolution.
- Why no material first-party path remains: each candidate path supplies configuration, ordinary operational instruction or capability adaptation; none establishes identity/ultimate-policy adjudication with legitimate authority and returned closure.

## Overall finding

Utah is a first-party autonomous agent harness with a strong prospective adaptation path. The core model/tool loop closes S1 autonomously, and the shipped workspace/skill/sidecar arrangement lets that same agent convert learned or anticipated reusable needs into persistent capabilities that affect future conversations, cron jobs and event-triggered work, supporting S4=A.

The remaining higher functions do not follow from the surrounding mechanisms. Singleton cancellation prevents same-session races but does not coordinate distinct S1 units; delegation lacks whole-current portfolio regulation; observability/retries are not complementary audit; and editable identity/persona files do not establish ultimate-policy closure.

**Proposed autonomy vector:** `A — — — A —`.
