---
harness_id: cast
project_name: cast
repository: https://github.com/aa-blinov/cast
review_ref: 8eb5142ed05b2d835c4da64487b12aff4712c6c7
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# cast

## Review boundary

- System in focus: `aa-blinov/cast` v0.47.1's first-party local TypeScript coding-agent distribution at frozen commit `8eb5142ed05b2d835c4da64487b12aff4712c6c7`, including CLI/TUI/headless and local web-server modes, model/tool loop, shipped personas, model-facing `task`/subagents, local session and actor registry, permission rules, native review, and optional model-backed memory/dream/distill maintenance.
- Purpose and identity: execute and review software-engineering work through model-directed repository tools, with selectable specialist personas, independent children, an optional human control room, and durable project capabilities.
- Relevant environment: project files and changes, current task and user, provider responses, tool/test/permission outcomes, concurrent children's work on one host, shared terminal confirmation input, past session trajectories, and user-selected model/provider settings.
- Standard-distribution boundary: first-party `src/core`, `src/core/tools`, `src/server`, `src/ui`, and shipped `prompts/personas` and `prompts/subagents` in supported modes. External OpenAI-compatible model providers, Ollama/vLLM, external MCP servers, host filesystem/process/SSH services, downstream project code and third-party skills/plugins are dependencies, not VSM owners.
- Credited operating / distribution surfaces: `src/core/loop.ts`, `src/core/tools.ts`, `src/core/tools/task.ts`, `src/core/actors.ts`, `src/core/subagents.ts`, `src/core/personas.ts`, `src/server/server.ts`, `src/server/bridge.ts`, `src/core/memory.ts`, `src/core/skills.ts`, `src/core/review.ts`, `src/core/settings.ts`, built-in `coder-with-subagents` and `review` prompts, and their CLI/TUI/web wiring.
- Adjacent first-party surfaces excluded from ownership: repository CI, tests, release/install scripts, benchmarks/evals, documentation-site development, repository maintainer organization, user-installed extensions, and the target project. Tests and docs corroborate but cannot lend unshipped runtime authority.
- First-party operating / deployment modes considered: ordinary `senior` coding; selectable `coder-with-subagents` with parallel/foreground/background `task`; built-in `review` child; `/plan` and `/build`; interactive permission gates; local web UI with session child list/cancel; manual `/dream` and `/distill`, plus supported opt-in automatic memory maintenance.
- Recursion level: one cast-assisted current project/session organization. Model-backed foreground and separately spawned mutating `task` children can be operational S1 units; a review-only child is a complementary audit actor. A task record, one tool call, a persona definition, or a background bash job alone is not promoted to S1.
- Reviewed revision: `8eb5142ed05b2d835c4da64487b12aff4712c6c7`.
- Observation date: 2026-10-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The main `runLoop` constructs persona-filtered tool definitions, sends model requests through its provider abstraction, dispatches model-selected tools, inserts concrete results back into the conversation, and continues. A first-party permission engine, plan/build mode, durable sessions, context compaction, tool hooks, web controls, and user configuration bound this operation. The seven shipped personas adjust roles, and the `coder-with-subagents` persona explicitly enables the normal model-visible `task` tool.

`task` starts an isolated child model loop with a separate session/transcript and chosen built-in subagent prompt. Children inherit project grounding and narrowed tools; the foreground parent sees a final report rather than the child's private reasoning. The shipped `review` child has its own read/search/Git-inspection role and is instructed to return severity-sorted `file:line` findings for the parent to act on. Four task slots cap simultaneous children per parent session. A first-party confirmation serializer prevents several subagent bash approvals from racing the shared terminal; it returns the individual approval decision to the correct child. Those deterministic contention controls do not by themselves turn the parent's ordinary task decomposition into autonomous S2 coordination.

For current supervision, the supported local web server exposes all child sessions for one parent session via `GET /api/sessions/:id/agents`, including a running flag, and an operator-owned `POST .../agents/:taskId/cancel` path. The latter calls `cancelTask` on the actual live child actor. By contrast the model's `task` interface can start a child, receive/continue a known child by ID, and steer that child, but it exposes no equivalent comprehensive model-facing list/cancel control over the current population.

Cast also ships a separate future-capability path. `/distill` and optional `memoryDistillAuto` examine cross-session project trajectories and existing project assets, let a model identify repeated workflows, and create reusable `.cast/skills/*/SKILL.md` or `.cast/personas/*.md` artifacts after evidence checks. Subsequent project trust and skill/persona loading make those capabilities available to later coding sessions. `/dream` separately consolidates memory rather than creating new skills. The automatic path is opt-in, not an always-on default.

Primary source evidence:

- [`README.md`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/README.md)
- [`src/core/loop.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/loop.ts)
- [`src/core/tools/task.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/tools/task.ts)
- [`src/core/tools.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/tools.ts)
- [`prompts/subagents/review.md`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/prompts/subagents/review.md)
- [`src/server/server.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/server/server.ts)
- [`src/server/bridge.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/server/bridge.ts)
- [`src/core/memory.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/memory.ts)

## Operational model

In an ordinary coding turn the model chooses how to inspect, edit, execute, and verify against project feedback. In the supported delegation persona, the same model may dispatch separate operational child loops and receive their results. A review child is a separate, non-implementing evidence path rather than another independent coding S1. Shared terminal confirmation input receives deterministic serialization, while optional web operation gives a human the live child list and the power to stop current children. A distinct opt-in memory-distillation model proposes and materializes reusable future skills/personas from past work patterns; this is separate from current coding and from static configuration.

## S1 — Operations

- State: A
- Function: produce and revise project-facing implementation/research actions through an open-ended model/tool loop.
- Disturbance / variety regulated: repository state, task ambiguity, external model responses, tool errors, tests, permissions, context limitations, changed requirements, and child findings.
- Decisive decision or feedback right: choose next repository tool/action and change course after observing its real result.
- Decision owner: active model-backed cast coding persona, or each model-backed mutating child within its delegated task.
- Supporting / enforcement mechanisms: provider adapter; model-specific tool schemas; first-party read/write/edit/bash/search; permissions; plan/build mode; session store; tool hooks; context/memory; child task transport.
- Closure path: user/project context → model selects tool/subtask → first-party dispatch/permission path → code or environment result → result reenters the model's later choices, or the model completes.
- Boundary reachability: the shipped CLI/headless/web entrypoints instantiate the ordinary loop; `coder-with-subagents` is shipped and enables the model-visible `task` path in supported runtime modes.
- Why this is / is not agent-owned: without the model actor, tool definitions and deterministic gates cannot choose arbitrary task-specific edits and iterative debugging steps.
- Evidence: [`src/core/loop.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/loop.ts); [`src/core/tools.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/tools.ts); [`src/core/tools/task.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/tools/task.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is code-level evidence for shipped behavior; no live provider-backed agent or tool mutation was run in this assessment.

## S2 — Coordination

- State: C
- Function: dampen a concrete conflict between separately running child S1s contending for the same interactive bash approval input.
- Disturbance / variety regulated: concurrent subagent confirmation prompts could race for the shared terminal/stdin and apply the wrong approval or interleave prompts, disturbing child work.
- Distinct S1 units: separate `task` children each execute their own model/tool loop and may request bash confirmation while active concurrently.
- Inter-S1 disturbance: the `task` runtime explicitly documents confirmation races between concurrently running subagents sharing one terminal.
- Attenuating coordination relation: `serializeConfirm` chains their shared-terminal confirmation calls, forcing each to finish before the next begins. Per-session `acquireSlot` additionally caps child model streams, but slot count alone is not the reason for S2 credit.
- Feedback into subsequent S1 behaviour: after its serialized approval or rejection, each child receives its own permission result and can continue or revise its next action; a failed/aborted child result propagates to parent tools.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the serializer is expressly keyed to actual cross-child contention over one approval input, not mere message passing or fan-out. Its effect is on tool authorization for the independent children.
- Decisive decision or feedback right: establish which simultaneous child's approval interaction may occupy the shared input at a time, preserving correct response routing.
- Decision owner: deterministic first-party confirmation serializer orders the requests; no model-decided conflict-specific reprioritization or autonomous coordination owner for that channel is established.
- Supporting / enforcement mechanisms: promise-chain serialization, child tool confirmation callbacks, bounded slots and actor lifecycles. The human still owns individual allow/deny choices where permissions ask; those are operational authorizations, not autonomous S2 arbitration.
- Closure path: competing child bash confirmations → per-process serialized confirmation queue → one prompt and response at a time → correct child's model/tool loop observes approval/rejection → later child action reflects that outcome.
- Boundary reachability: the `task` tool passes `serializeConfirm` to its child `runAgentLoop` directly in the shipped CLI/interactive execution path; no external plugin is needed.
- Why this is / is not agent-owned: remove the parent model but keep active children and serializer: FIFO interference attenuation still occurs. The exposed S2-specific path is real, but agent-owned coordination discretion is not closed; this is a constructor/support-level `C`, not `A`.
- Evidence: [`src/core/tools/task.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/tools/task.ts); [`src/core/loop.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/loop.ts).
- Basis: structural + explicit code comment.
- Confidence: medium.
- Caveats: child file-write scopes are advisory prompts, not first-party workspace collision arbitration; no broader inter-agent semantic coordination is inferred. In unattended modes without interactive confirmations the cited S2 path may be dormant.

## S3 — Inside-and-now control

- State: P
- Function: supervise and intervene in the current bounded population of subordinate model-backed work units from the local operator control room.
- Disturbance / variety regulated: out-of-date or unproductive active child commitments, conflicting immediate priorities, and unwanted background agents consuming current effort.
- Whole-system current view: the web server lists all child sessions of the selected parent session, with task ID, subagent/persona, model and running status; the operator can inspect their separate session histories. This is whole-current only for the declared one-session organization, not a multi-project company control plane.
- Current-control decision scope: the operator can choose an identified running child to stop; the server checks that the child belongs to that parent and calls `cancelTask`, which aborts the live actor. Supported web controls also permit changing which project/session work is attended next.
- Decisive decision or feedback right: decide which current subordinate commitments should remain active or be terminated based on the parent session's live child list.
- Decision owner: the human operator of the built-in local web mode (`P`).
- Supporting / enforcement mechanisms: `listSubagentSessions`; `runningTaskIds`; `cancelTask`; actor registry and abort signals; authenticated web endpoint/session UI; durable session records.
- Closure path: current child population/status visible through `/api/sessions/:id/agents` → operator chooses a child to cancel → `/api/sessions/:id/agents/:taskId/cancel` → actual actor receives cancellation → later population/status and work change.
- Boundary reachability: both child-list and cancel endpoints are implemented in the shipped `cast web` server and call the first-party session and actor state. No independent operator application is required.
- Why this is / is not agent-owned: the model-facing `task` can delegate and steer child IDs, but lacks an equivalent model-visible whole-population list/cancel path; delegation alone is not sufficient S3. Removing the web operator eliminates the established whole-current intervention decision without changing the lower-level deterministic actor registry.
- Evidence: [`src/server/server.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/server/server.ts); [`src/server/bridge.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/server/bridge.ts); [`src/core/tools/task.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/tools/task.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: this is local attended supervision. It does not support a claim of autonomous S3 or a cross-workspace whole-organization manager.

## S3* — Complementary audit

- State: A
- Function: independently challenge the implementing actor's correctness, security, test coverage and design claims using a separately instantiated review child.
- Disturbance / variety regulated: overlooked regressions, missing tests, insecure shell/code changes and implementer self-confirmation.
- Claim being audited: the parent coding result is adequately correct and safe to finish or present.
- Ordinary reporting path: the implementation parent's own tool output and completion narrative, plus same-loop `/review` machinery where explicitly requested.
- Complementary access path: the model-visible `task` chooses `subagent="review"`; `execTask` loads the shipped separate reviewer system prompt, starts a separate model/session/context with read/grep/glob/ls/bash inspection tools, and returns its own file/line findings as a tool result.
- Independence boundary: the reviewer has isolated context and cannot see the parent's reasoning; it inspects direct repo files. The reviewer role omits `write`, `edit` and recursive `task`. It may use the same model/provider and its inspection-only bash restriction is partly prompt-enforced, not a separate sandbox; these limit strength, not the independent judgment channel.
- Who acts on findings: parent receives the review report as an ordinary `task` tool result and can revise code/tests, request a follow-up, or challenge completion.
- Decisive decision or feedback right: independently judge defects and severity from direct repo evidence rather than accept implementer summary.
- Decision owner: model-backed built-in `review` subagent.
- Supporting / enforcement mechanisms: role-specific prompt, tool allowlist, `execTask` session/actor isolation, `extractTaskResult`, child-result `taskBlock`, parent tool loop.
- Closure path: implementation performed → parent model invokes reviewer with project scope → isolated read/search/Git review → reviewer returns severity/location findings → parent model receives the findings and can correct/retest/re-review.
- Boundary reachability: `coder-with-subagents` is an included persona with `subagents: true`; `review` is a shipped subagent prompt and appears in the standard `task` schema, which is enforced both on advertisement and execution.
- Why this is / is not agent-owned: removing the reviewer model leaves only isolation and tool plumbing, not an autonomous substantive code-defect judgment.
- Evidence: [`prompts/subagents/review.md`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/prompts/subagents/review.md); [`prompts/personas/coder-with-subagents.md`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/prompts/personas/coder-with-subagents.md); [`src/core/tools/task.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/tools/task.ts); [`src/core/loop.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/loop.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: selecting the ordinary `qa` persona or calling `/review` in the same active loop alone is not this positive path; the separately spawned review child is.

## S4 — Outside-and-then intelligence

- State: A
- Function: detect repeated patterns in the changing project/task environment and package prospective reusable workflow capabilities for later sessions.
- Disturbance / variety regulated: recurring user-project needs, repeated costly operations, stale memories and loss of prior project practice when sessions change.
- External distinction: incoming real user/project trajectory across previous sessions, project memory, and existing project assets are compared rather than only the current model turn; the model sees repeated environmental demand for a workflow.
- Future / prospective distinction: the distillation prompt explicitly selects workflows worth applying in future work, ordinarily requiring recurrence rather than a one-off task.
- Adaptation option generated: model chooses a bounded reusable skill or persona, or declines to create one when evidence is weak.
- Path back into current capability / S3: first-party materialization writes `.cast/skills/<name>/SKILL.md` or `.cast/personas/<name>.md`; trusted-project skill/persona discovery loads these for subsequent coding sessions, expanding the available operating repertoire.
- Decisive decision or feedback right: judge which historical environment patterns merit adoption as future runtime skills/personas and author the reusable capability.
- Decision owner: model-backed first-party maintenance/distillation run. Deterministic parsing, repeated-evidence checks, file validation and project leases constrain its adoption.
- Supporting / enforcement mechanisms: `/distill`; optional `memoryDistillAuto`; scheduled maintenance actor; trajectory/memory retrieval; `hasRepeatedWorkflowEvidence`; materialization and later skill/persona discovery; project-trust gate.
- Closure path: multiple sessions' project/environment evidence → model-based distillation selects future workflow capability → first-party writer materializes trusted project skill/persona → subsequent runtime reload/discovery exposes it to later models → operating capability changes.
- Boundary reachability: this is packaged in `src/core/memory.ts`, wired to the first-party `/distill` command and opt-in automatic maintenance at new sessions; it does not borrow a separate research harness or marketplace plugin.
- Why this is / is not agent-owned: without the maintenance model, deterministic interval scheduling and file checks cannot decide which reusable workflow to invent or distill from varied project trajectories.
- Evidence: [`src/core/memory.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/memory.ts); [`src/ui/commands.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/ui/commands.ts); [`src/core/settings.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/settings.ts); [`src/core/personas.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/personas.ts); [`src/core/skills.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/skills.ts); [`prompts/memory-distill.md`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/prompts/memory-distill.md).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: `memoryDistillAuto` defaults off and opt-in/manual activation is required; the prospective horizon is future local project workflows, not autonomous market reconnaissance. Source wiring supports the claim but the quality of generated adaptations was not experimentally tested here.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime ultimate identity/policy decision-and-return loop is established for the assessed one-project organization.
- Disturbance / variety regulated: trust, tool permissions, personas and user-authored rules constrain actions, but an identity/ultimate-policy conflict is not adjudicated through a legitimate internal or parent S5 circuit.
- Decisive decision or feedback right: none established at S5 level; user/developer-authored settings supply fixed limits or ordinary tool approval.
- Decision owner: not established in the assessed operating boundary.
- Supporting / enforcement mechanisms: project trust; permissions; persona allowlists; read-only plan mode; custom skills/rules; system prompts and user configuration.
- Closure path: configuration and permissions are loaded/enforced, but no first-party ultimate-policy issue → legitimate decision owner → authoritative resolution → system-wide governed return was found.
- Why this is / is not agent-owned: generic operator approval, trust toggling and changing a persona do not create identity-level legitimate authority or an S5 closure path.
- Evidence: [`src/core/permissions.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/permissions.ts); [`src/core/personas.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/personas.ts); [`src/core/plan.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/plan.ts); [`src/core/settings.ts`](https://github.com/aa-blinov/cast/blob/8eb5142ed05b2d835c4da64487b12aff4712c6c7/src/core/settings.ts).
- Basis: explicit configuration + structural absence review.
- Confidence: medium-high.
- Caveats: repository maintainer and user ultimate-policy authority exist externally, but their governance is not a closed first-party runtime identity circuit at this recursion.

### Absence scope

- Surfaces inspected: tool permissions, project trust, persona prompts/frontmatter, plan/build modes, local web control, session governance, skills/rules, maintenance/dream/distill capability, and repository contributor/CI adjacency.
- Plausible first-party paths checked: runtime self-modification of constitutional purpose, privileged user/owner identity decisions, durable parent identity-policy escalation with authoritative return, persona-editing as possible policy change, and routine approval as possible S5.
- Why no material first-party path remains: reviewed paths choose or enforce operating settings/capabilities, not an ultimate identity-policy judgment and return. The supplied developer/user decisions are adjacent authority/configuration rather than a packaged identity-governance feedback loop.

## Recursion

Mutating `task` children have distinct model loops, transcripts, tool action choices and project environment, which supports subordinate S1 cells. Reviewer children are complementary assurance participants and do not become S1 solely from being another process. Persistent actor/session IDs or nested prompts do not by themselves establish full recursive VSM viability.

## Variety and escalation

Cast amplifies operational variety through multiple role prompts, tools/MCP, optional web search, independent child model loops, and learned future project skills. It attenuates variety through permissions, role allowlists, isolated child contexts, bounded concurrency, serialized confirmations, project trust, plan/build stages and deterministic evidence/materialization checks. Child findings feed the parent model; a human can intervene in the current child population from the local web control room. Distillation turns repeated external project demands into new future reusable capabilities, whereas project identity and ultimate policy stay outside the runtime.

## Evidence gaps

- The first-party S2 witness is narrowly the shared interactive terminal confirmation race; it does not establish workspace/file-conflict control between mutating children. The definitive owner of individual permission grants is the operator, while queue ordering is deterministic.
- S3 parent closure depends on attended local web mode; `task` alone does not give the model a whole-current list/cancel action. This is `P`, not `A(P)`.
- S3* review-child independence is role/context/evidence-path separation, not provider independence or a guaranteed read-only bash sandbox.
- S4 prospective reach is restricted to recurring future project workflows under manual/opt-in maintenance. No measured improvement from those adaptations is claimed.
- The assessment is static and exact-ref source-backed; no live LLM agents or providers were executed.

## Assessment summary

At the pinned source boundary, cast closes model-driven coding S1 and a model-backed complementary reviewer S3*. Its shared-input approval serializer has a concrete but deterministic inter-child S2 coordination path (`C`), while the local web operator owns current whole-session child intervention (`S3=P`). The first-party optional model distillation path can adopt reusable future project skills/personas from repeated historical demand (`S4=A`). Settings and personas do not close ultimate-policy S5.

Proposed vector: **`A · C · P · A · A · —`**
