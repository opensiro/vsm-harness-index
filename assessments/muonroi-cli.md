---
harness_id: muonroi-cli
project_name: muonroi-cli
repository: https://github.com/muonroi/muonroi-cli
review_ref: 0e263b8c8ff142b1d643e64a6b0825fdf477c626
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# muonroi-cli

## Review boundary

- System in focus: the first-party muonroi-cli coding runtime at frozen revision `0e263b8c8ff142b1d643e64a6b0825fdf477c626`, including its top-level coding Agent, built-in tools, foreground task subagents, detached read-only delegations, Prompt Intelligence Layer, Council, supported Experience Engine client/tool/hook loop, session/flow persistence, routing and interactive/headless execution.
- Purpose and identity: execute software-engineering work through a model-owned coding loop that may decompose work into focused subagents, regulate current work commitments, invoke an adversarial multi-model Council for complementary challenge, and reuse recorded operational experience in later decisions.
- Relevant environment: user requests/steering/approvals, repository state and tool results, subagent/delegation status and returned outputs, provider/model availability, Council evidence/disagreement, prior experience records and feedback, context/tool load, persisted sessions and flow state.
- Standard-distribution boundary: shipped muonroi-cli runtime and its repository-owned orchestrator, tools, task/delegation paths, Council, PIL, EE client/native tools/hooks, persistence and routing. External model endpoints, configured MCP servers, operating-system tools and the external Experience Engine storage/search service are dependencies and cannot donate VSM ownership; the decisive S4 write/feedback/recall choices credited here are made by the first-party coding agent and returned through first-party prompt/tool wiring.
- Credited operating / distribution surfaces: `src/orchestrator/`, `src/tools/`, `src/council/`, `src/pil/`, `src/ee/`, `src/hooks/`, `src/router/`, `src/storage/`, `src/flow/`, the shipped TUI/headless paths and documented built-in agent operating contract.
- Adjacent first-party surfaces excluded from ownership: CI/release workflows, repository tests, planning/retrospective files, dogfood records and development-only experiments unless the corresponding mechanism is wired into the shipped runtime.
- First-party operating / deployment modes considered: ordinary top-level coding-agent turns; foreground `task` subagents; detached read-only `delegate` exploration; agent-convened Council; configured Experience Engine recall/write/feedback mode; interactive/headless sessions and supported model/provider routing.
- Recursion level: one muonroi-cli coding session and the first-party operational units it creates for that session. The top-level coding agent is an S1 and may instantiate additional focused S1 task/delegation agents; the top-level agent also owns current-control decisions over those commitments.
- Reviewed revision: `0e263b8c8ff142b1d643e64a6b0825fdf477c626`.
- Observation date: 2026-10-06.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

muonroi-cli ships a top-level `Agent` that owns the current model/tool coding conversation and can create focused child agent loops. Foreground `task` work runs a fresh `StreamRunner` child and returns a ToolResult. Detached `delegate` work spawns a separate read-only explore process, persists its status/result, and exposes list/read/kill operations so the parent can incorporate or terminate that commitment.

The runtime also contains a multi-model Council. Agent-convened `convene_council` is a model-callable tool: the Council resolves a reachable panel, can research with tools, runs adversarial rounds with verify-then-refute behavior and leader evaluation, synthesizes a conclusion, and returns that synthesis into the live tool call so the calling agent decides what happens next. Agent-convened paths deliberately suppress human post-debate decision cards.

The optional Experience Engine mode provides native `ee_query`, `ee_feedback` and `ee_write` capabilities plus PreToolUse/PostToolUse hooks. Prior principles/behavioral records can be recalled and injected into later prompts; the agent is instructed to recall before unfamiliar/risky work, rate used recalls, and write a concise reusable lesson after discovering a mistake/fix. Runtime observation also records tool outcomes and feedback signals. The external service persists/searches those records, but the coding agent owns the discretionary decision to query, rate and write experience and consumes the returned guidance in subsequent operation.

## Operational model

The top-level model-backed Agent owns open-ended coding decisions and can decide that a focused subtask should be delegated, retrieve its result, terminate a detached delegation, or convene a Council for an adversarial check. Subagents remain bounded by their assigned task/tool surface. The parent model therefore has a whole-session current view and a first-party decision path over current work commitments rather than merely receiving a fixed scheduler decision.

Council participants are complementary decision/audit actors, not additional coding S1s merely because they are multiple models. Conversely, foreground task/delegation children are operational units, but their isolation and task/result channels do not by themselves establish S2; the reviewed source does not show a distinct interference-feedback loop among those S1s.

## S1 — Operations

- State: A
- Function: autonomously perform software-engineering work through model-selected repository/tool actions and focused subagent execution.
- Disturbance / variety regulated: unfamiliar codebases, implementation choices, tool/process failures, incomplete evidence, provider/model variability, context pressure and task decomposition.
- Decisive decision or feedback right: select substantive coding/tool actions, interpret returned evidence, decide whether to delegate focused work and determine when the task is complete.
- Decision owner: the active top-level model-backed muonroi-cli Agent; focused task/delegation agents autonomously execute their assigned operational subtasks.
- Supporting / enforcement mechanisms: tool engine, permissions/safety gates, session persistence, model routing, compaction, retries, flow state and deterministic limits.
- Closure path: user request → top-level agent chooses direct action or focused subtask → first-party tool/subagent path executes → evidence/result returns to the live agent conversation → agent revises implementation or completes the request.
- Boundary reachability: ordinary shipped coding turns construct the Agent/tool loop, and task/delegate capabilities are wired as first-party tools rather than development-only helpers.
- Why this is / is not agent-owned: removing the model actors leaves enforcement, storage and routing but no open-ended choice of implementation, investigation or delegated work.
- Evidence: [AGENTS.md](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/AGENTS.md); [src/orchestrator/orchestrator.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/orchestrator/orchestrator.ts); [src/orchestrator/delegations.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/orchestrator/delegations.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: permission and safety machinery can block or constrain actions; that enforcement does not replace the agent's substantive operational decision right.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function satisfying the S2 disturbance/feedback test is established.
- Disturbance / variety regulated: no concrete recurring interference, conflict or oscillation among peer operational S1 units is placed under a distinct coordination feedback loop.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: foreground task result channels, detached read-only exploration, write serialization/mutation gates, task boundaries and delegation lifecycle APIs reduce collision opportunities but do not constitute a distinct S2 owner.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: the parent can allocate/terminate work (S3), while child isolation/read-only policy prevents classes of conflict deterministically. Evidence does not show an autonomous coordinator sensing an actual inter-S1 disturbance and feeding an attenuation decision back to the affected S1 units.
- Evidence: [src/orchestrator/delegations.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/orchestrator/delegations.ts); [docs/agent-harness/CONTEXT-CONTROL-LAYERS.md](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/docs/agent-harness/CONTEXT-CONTROL-LAYERS.md); [src/orchestrator/tool-engine.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/orchestrator/tool-engine.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: multi-agent count, a queue/result channel, write mutex, read-only isolation and Council speaker sequencing are mechanisms; none is promoted without the Methodology 0.3.6 S2 witness.

### Absence scope

- Surfaces inspected: task/delegate execution and lifecycle, tool parallelism/serialization, reactive sub-session path, Council participant orchestration, session/flow state and parent result channels.
- Plausible first-party paths checked: parallel subagents, background delegation notifications, shared worktree mutation controls, Council rounds, write mutex/mutation gate and task/dependency channels.
- Why no material first-party path remains: the evidence either prevents interference structurally, routes results upward to S3, or coordinates complementary Council voices rather than regulating interaction among peer operational S1 units.

## S3 — Inside-and-now control

- State: A
- Function: regulate current session commitments by deciding when to keep work in the parent, spawn a focused operational subagent, start/read/kill detached exploration, and consume those results into the live task.
- Disturbance / variety regulated: excessive current-task breadth/tool load, need for isolated investigation, unfinished background commitments, subtask status/failure and context pressure that would otherwise overload the top-level operation.
- Decisive decision or feedback right: allocate current work to task/delegate agents, choose the delegated objective, inspect returned/current status, terminate a detached commitment and decide how its result changes the parent task.
- Decision owner: the top-level model-backed Agent through its model-callable task/delegate/delegation lifecycle tools.
- Supporting / enforcement mechanisms: DelegationManager process/status storage, subagent model-tier routing, reactive load thresholds, tool/result transport, notifications and caps.
- Closure path: parent observes current task/evidence → decides to create/manage a focused work commitment → child executes and status/result becomes available → parent reads/uses or terminates it → subsequent current operation changes.
- Whole-system current view: the top-level Agent retains the live parent-session conversation, current model/tool state, subagent lifecycle/status channels, delegation records/notifications and returned child results needed to decide how the current coding organization should proceed.
- Current-control decision scope: the top-level model decides whether current work stays local or becomes a focused task/delegation, defines the child commitment, may retrieve or terminate detached work, and decides how returned results change the parent session's present priorities/actions.
- Boundary reachability: `runTask` and `runDelegation` are wired into the shipped tool set; detached results expose list/read/kill and completion notifications.
- Why this is / is not agent-owned: deterministic components launch, persist and cap work, but the top-level agent chooses the substantive delegation/commitment and acts on its returned result.
- Evidence: [src/orchestrator/orchestrator.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/orchestrator/orchestrator.ts); [src/orchestrator/delegations.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/orchestrator/delegations.ts); [docs/agent-harness/CONTEXT-CONTROL-LAYERS.md](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/docs/agent-harness/CONTEXT-CONTROL-LAYERS.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: reactive sub-session escalation and hard caps are deterministic supporting mechanisms; the positive S3 claim rests on the model-owned work-allocation/lifecycle path, not on those thresholds.

## S3* — Complementary audit

- State: A
- Function: independently challenge high-stakes/conflicting current conclusions through a multi-model adversarial Council and return the synthesized audit judgment to the coding agent.
- Disturbance / variety regulated: weakly grounded plans, unresolved disagreement, one-model blind spots, unsupported claims and known prior mistakes relevant to a consequential decision.
- Decisive decision or feedback right: Council participants independently research/argue/refute; the leader evaluates debate evidence and synthesizes a conclusion that the calling agent must then interpret.
- Decision owner: the first-party Council's independently instantiated model participants plus leader synthesis, invoked autonomously by the main agent through `convene_council`.
- Supporting / enforcement mechanisms: task-aware panel selection, research tools, round budgets, convergence/evidence-density evaluation, Experience Auditor stance and deterministic EE heuristic scoring.
- Closure path: main agent identifies a high-stakes/conflicting issue → calls `convene_council` → separate panel researches and adversarially challenges positions → leader synthesis returns as the tool result → the main agent decides and continues operation using the findings.
- Claim being audited: the main coding agent's current high-stakes/conflicting plan, interpretation, recommendation or implementation decision that it has chosen to submit to Council challenge.
- Ordinary reporting path: without Council, repository/tool observations and ordinary subagent results return directly to the top-level coding agent through its normal tool/result conversation.
- Complementary access path: Council participants receive a separately constructed debate/research context, can use first-party research tools, produce independent opening positions and verify-then-refute exchanges, and are synthesized by a leader before the result returns to the caller.
- Independence boundary: Council participants are separate model calls/instances with separately assigned stances and research/debate turns; they do not merely echo the main agent's ordinary tool-result channel, and agent-convened mode suppresses a human post-debate decision surface.
- Who acts on findings: the top-level coding agent receives the Council synthesis as the `convene_council` tool result and owns the subsequent operational response.
- Boundary reachability: the agent operating contract explicitly exposes `convene_council`; agent-convened paths suppress human decision cards and return the Council conclusion directly into the live tool call.
- Why this is / is not agent-owned: the audit judgment is produced by separate model instances with complementary research/debate access, not by the ordinary coding agent merely rereading its own work.
- Evidence: [docs/Council.md](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/docs/Council.md); [src/council/index.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/council/index.ts); [src/council/debate.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/council/debate.ts); [src/pil/agent-operating-contract.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/pil/agent-operating-contract.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the deterministic `judgeCouncilOutcome` heuristic is supporting quality telemetry, not the owner of S3*; independence comes from the separate Council model/research/debate path.

## S4 — Outside-and-then intelligence

- State: A
- Function: retain operational lessons, recall them in later work, evaluate whether recalled guidance helped and write newly discovered mistake→fix lessons so subsequent agent behavior can adapt.
- Disturbance / variety regulated: recurring mistakes, stale/noisy prior guidance, unfamiliar/risky code areas, previously learned project-specific constraints and context lost across sessions/compaction.
- Decisive decision or feedback right: the coding agent can decide when prior experience is relevant, query it, rate a recalled item as followed/ignored/noise and write a new reusable lesson after discovering a working fix.
- Decision owner: the model-backed coding agent using first-party native `ee_query`, `ee_feedback` and `ee_write` paths; deterministic observation/judge machinery supplies additional feedback signals.
- Supporting / enforcement mechanisms: EE client transport/storage/search dependency, recall ledger, PreToolUse/PostToolUse hooks, MistakeDetector, PIL experience injection, behavioral/principle collections and Council Experience Auditor injection.
- Closure path: prior operational outcome/mistake → first-party agent/runtime records or rates experience → retained experience is retrieved on a later relevant task → PIL/native recall returns it into model context → agent changes subsequent investigation/tool choices and can feed back whether the guidance was useful.
- External distinction: the loop distinguishes present repository/task context and tool outcomes from retained cross-turn/cross-session behavioral principles, past mistake/fix records and experience relevance returned by the configured Experience Engine.
- Future / prospective distinction: recalled lessons are evaluated for whether they should shape a later task or risky step, rather than only correcting the already-finished tool call that generated the lesson.
- Adaptation option generated: the agent can change later investigation/delegation/tool choices, invoke prior proven constraints, rate/prune misleading guidance, or write a new reusable mistake→fix lesson for future retrieval.
- Path back into current capability / S3: recalled principles, behavioral lessons and rated experience are injected into a later turn's PIL/native recall context, where the top-level agent uses them to change present task decomposition, tool choice, Council escalation or other current operational commitments.
- Boundary reachability: the native experience tools are part of the shipped coding-agent tool surface and the built-in operating contract explicitly instructs recall-before-risk, feedback-after-use and write-after-fix behavior.
- Why this is / is not agent-owned: the external Experience Engine service stores/searches records, but the organizational adaptation judgment credited here is the coding agent's discretionary query/write/feedback use and later consumption; storage transport does not own that choice.
- Evidence: [src/orchestrator/prompts.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/orchestrator/prompts.ts); [src/tools/native-tools.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/tools/native-tools.ts); [src/hooks/index.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/hooks/index.ts); [src/pil/layer3-ee-injection.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/pil/layer3-ee-injection.ts); [src/ee/mistake-detector.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/ee/mistake-detector.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the Experience Engine is optional and fails open when unavailable, so S4 is a supported configured standard-distribution mode rather than a guarantee for every run. The reviewed TUI imports user-noise-feedback helpers but no reachable distinct parent feedback mode was established from the frozen source, so no `(P)` modifier is claimed.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established at the assessed session recursion.
- Disturbance / variety regulated: no identity-level dispute or ultimate-policy matter is shown reaching an authoritative runtime owner and returning as governing policy.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: AGENTS/system instructions, permission modes, user/project settings, PIL operating rules, safety gates and model/provider configuration constrain execution but are not an identity-governance loop.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: the coding agent operates under developer/user-authored rules and may adapt tactics/experience, but it lacks authority to redefine the system's ultimate identity or governing principles.
- Evidence: [AGENTS.md](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/AGENTS.md); [src/pil/agent-operating-contract.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/pil/agent-operating-contract.ts); [src/orchestrator/orchestrator.ts](https://github.com/muonroi/muonroi-cli/blob/0e263b8c8ff142b1d643e64a6b0825fdf477c626/src/orchestrator/orchestrator.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: user configuration and permission choices are legitimate parent constraints over local execution, but no identity/ultimate-policy issue and authoritative return loop is established.

### Absence scope

- Surfaces inspected: AGENTS/system prompts, permission/safety modes, model/provider configuration, PIL operating contract, Experience/WhoAmI preference paths, Council decisions, session/flow state and project settings.
- Plausible first-party paths checked: autonomous constitutional revision, parent identity policy, WhoAmI profile, Experience principles, Council governance and user configuration.
- Why no material first-party path remains: those surfaces govern task behavior, preferences, safety or learned tactics; none establishes authority over the runtime's identity/ultimate policy with a closed return path.

## Distributed OSS parent arrangement

The assessed organization is the running muonroi-cli coding organization rather than its GitHub maintainer/contributor project. Repository planning, PR governance and release decisions are not imported as parent S3/S4/S5 merely because they are first-party development artifacts.

## Self-hosted and non-human modes

The runtime can use local or hosted model providers and can operate headlessly. The positive S3/S3*/S4 claims rely on model-owned first-party runtime paths rather than a human operator. Human steering, approvals and configuration remain optional constraints and are not used to manufacture parent modifiers.

## Recursion

The top-level coding session is the viable-unit boundary. Its main coding agent and focused operational task/delegation children are S1 units when instantiated. The top-level agent owns current work allocation/lifecycle (S3); the Council is a complementary audit/intelligence mechanism rather than a peer coding S1; Experience mechanisms provide prospective adaptation (S4).

## Variety and escalation

Ordinary coding variety remains in S1. Current workload/context variety can be decomposed into focused subagents under S3. High-stakes disagreement can escalate to the independent Council under S3*. Recurring mistakes and prior lessons can be recalled/updated through the Experience loop under S4. Deterministic caps, mutexes, permissions and routing enforce bounds but are not credited as autonomous organizational owners.

## Evidence gaps

No `?` state is required. Frozen source establishes the autonomous S1, S3, S3* and configured S4 paths directly. The same boundary also provides enough negative evidence to conclude that generic isolation/sequencing does not close S2 and that task/safety/preference rules do not close S5.
