---
harness_id: dotcraft
project_name: DotCraft
repository: https://github.com/DotHarness/dotcraft
review_ref: a08c8b35497f6ba9148f6ede80839835dcc8812a
reviewed_at: 2026-09-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-28
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# DotCraft

## Review boundary

- System in focus: one supported self-hosted DotCraft operating deployment at pinned revision `a08c8b35497f6ba9148f6ede80839835dcc8812a`, including the Session/Agent runtime, model/tool execution, subagents, Automations and Goals, Dreams, Agent Profiles, and the built-in Oratorio task/run/review subsystem.
- Purpose and identity: provide an extensible local/self-hosted agent runtime in which model-driven agents perform substantive workspace work, delegate focused tasks, continue scheduled or long-running work, coordinate bounded execution, review code changes, and operate under reusable parent-defined agent roles and capability policies.
- Relevant environment: user requests and approvals, workspace/repository state, configured model providers, tool/MCP/remote-host results, provider rate limits, Oratorio task and source state, GitHub/GitLab pull-request heads and diffs, runtime failures, schedules, stored memory and profile configuration.
- Standard-distribution boundary: first-party DotCraft runtime, AppServer/Desktop-supported features and bundled Oratorio surfaces present at the pinned revision. Repository contributor workflow, tests except as corroboration, design proposals not reached by shipped runtime, external model/provider internals and third-party services are not independently credited.
- Credited operating / distribution surfaces: ordinary DotCraft agent sessions; first-party tool invocation; subagent spawning; server-managed Goals and Automations; Dreams background memory maintenance; saved Agent Profiles; built-in Oratorio implementation/review runs and scheduler; Desktop/AppServer supported control surfaces.
- Adjacent first-party surfaces excluded from ownership: repository CI/release machinery; contributor-only test/eval code; documentation examples; plugin source-development activity unless reached through the shipped plugin-creator/runtime path; external GitHub/GitLab/provider control planes beyond the first-party integration boundary.
- First-party operating / deployment modes considered: interactive Desktop/CLI/AppServer conversations; scheduled Automations; long-running Goals; subagent delegation; Oratorio implementation and review-analysis runs; background Dreams; profile-selected task/conversation execution; supported remote/self-hosted AppServer operation.
- Recursion level: one DotCraft operating deployment is the system-in-focus. Model-driven top-level, subagent and Oratorio work runs that own substantive outcomes are S1 operations. Deployment/runtime schedulers may regulate the current run portfolio. Independent Oratorio review-analysis is assessed as complementary audit. Parent-owned Agent Profiles provide durable role/policy modes returned into later runs.
- Reviewed revision: `a08c8b35497f6ba9148f6ede80839835dcc8812a`.
- Observation date: 2026-09-28.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

DotCraft owns a first-party agent assembly around model clients, tool snapshots, workspace context, approvals, memory, skills, plugins and tracing. `AgentFactory` creates tool-enabled `ChatClientAgent` instances and wraps the model client with `StreamingFunctionInvokingChatClient`, so model-selected tool calls execute and feed observations back through later inference rounds. The same runtime is reachable from Desktop, AppServer and embedded harness modes.

Subagents are separate model-driven workers with their own task prompt, tool surface and child tracing session. `SubAgentManager` explicitly throttles concurrent subagent executions with `SemaphoreSlim` to avoid exceeding provider API rate limits. This is a concrete shared-resource interference path between distinct S1-capable workers rather than a claim based merely on delegation.

Oratorio adds a deployment-level task/run control plane. Its AppServer worker periodically observes active and queued runs across the current Oratorio deployment, counts global, per-repository and per-source load, dispatches only when configured current-capacity limits permit, leases runs, reconciles stalled executions and recovers interrupted work. That establishes constructor-owned current operational regulation above individual model runs.

Oratorio also supplies a materially separate audit path. Pull-request `reviewAnalysis` runs are read-only analyses pinned to the synchronized current PR/MR head and review diff. The review agent submits structured review drafts/findings instead of modifying the implementation. Published open findings are then included in later implementation-run context for the generated PR, while stale review retries are superseded when the target head changes. This closes a complementary reviewer-to-repair loop without treating ordinary operator review UI as autonomous audit.

Dreams is substantive background adaptation of context, but its input is workspace history, explicit memory, recent sessions and current repository/spec/docs evidence. It produces reviewable passive inferred memory and may make a generated store prompt-visible after user apply or configured auto-apply. That improves future S1 context from internal operational evidence but does not establish a distinct external-and-prospective S4 intelligence loop.

Durable identity/policy is supplied through Agent Profiles. A saved profile defines role instructions, tools, skills, model defaults, MCP access and approval behavior, and a later conversation, Goal or Automation can run under that saved role/capability set. Agent Builder can help draft the profile, but the parent operator creates/edits/selects the authoritative saved profile. Ultimate policy ownership is therefore parent-held.

## Operational model

At this recursion, model-driven session/subagent/Oratorio executions are S1 units. Provider-capacity throttling supplies deterministic S2 coordination for a concrete interference mode. Oratorio's scheduler supplies deterministic S3 current-control over the live run portfolio. A separate model-driven read-only review-analysis path supplies S3* audit and feeds findings into subsequent implementation work. Dreams and plugin authoring do not close S4's outside-and-then threshold. Saved Agent Profiles close S5 through parent-owned durable role and capability policy returned into later operation.

## S1 — Operations

- State: A
- Function: perform substantive workspace/project work through model-driven reasoning, tool selection, observation and iterative continuation.
- Disturbance / variety regulated: heterogeneous user and task objectives, changing files/repositories, tool and remote-service results, provider responses, approval outcomes, runtime failures and long-running task state.
- Decisive decision or feedback right: choose task-specific model actions/tool calls and change later actions from returned observations until a bounded work result is produced.
- Decision owner: model-driven DotCraft agent actors created through the first-party agent/session runtime.
- Supporting / enforcement mechanisms: `AgentFactory`, effective tool snapshots, `StreamingFunctionInvokingChatClient`, approvals, workspace/tool sources, memory/skills, Session/AppServer lifecycle and Oratorio worktree/runtime integration.
- Closure path: task + assembled runtime context → model chooses action/tool → DotCraft dispatches the permitted tool → result returns through the function-invocation/model pipeline → later model action changes from the observation → workspace/task outcome advances.
- Boundary reachability: normal Desktop/AppServer/harness operation constructs the same first-party model/tool runtime; subagent and Oratorio task paths also invoke model-driven agents for substantive work.
- Why this is / is not agent-owned: deterministic code assembles tools and enforces approvals, but the model actor decides the task-specific semantic action sequence rather than following a fixed workflow result.
- Evidence: [`README.md`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/README.md); [`src/DotCraft.Core/Agents/Runtime/AgentFactory.cs`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/src/DotCraft.Core/Agents/Runtime/AgentFactory.cs); [`src/DotCraft.Core/Agents/SubAgents/SubAgentManager.cs`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/src/DotCraft.Core/Agents/SubAgents/SubAgentManager.cs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external provider inference remains a dependency. The autonomy state credits the model actor reached through DotCraft's shipped first-party runtime, not organizational functions internal to the provider.

## S2 — Coordination

- State: C
- Function: attenuate a concrete shared-provider interference mode among concurrently executing S1-capable subagents by bounding how many may execute at once.
- Disturbance / variety regulated: concurrent subagent model executions can collectively exceed provider API rate limits and thereby disrupt sibling work.
- Decisive decision or feedback right: admit or hold a child execution at the concurrency gate so the number of simultaneous subagent runs stays within the configured bound.
- Decision owner: deterministic first-party `SubAgentManager` runtime policy.
- Supporting / enforcement mechanisms: `SemaphoreSlim(maxConcurrency, maxConcurrency)`, wait-before-run/release-after-run lifecycle, independent child task prompts/tracing sessions and model/tool execution.
- Closure path: parent spawns multiple distinct task-owning subagents → shared provider-rate-limit pressure creates structural interference risk → concurrency gate holds excess child executions → admitted children complete and release capacity → waiting children then continue their model/tool work.
- Boundary reachability: subagent delegation is a shipped built-in runtime capability and the concurrency gate is part of its ordinary manager implementation.
- Why this is / is not agent-owned: the coordination relation persists independently of model judgment; deterministic runtime code owns admission and release, so the state is `C` rather than `A`.
- Distinct S1 units: concurrently spawned subagents, each given a self-contained task and its own model/tool execution context, capable of producing substantive workspace results.
- Inter-S1 disturbance: aggregate simultaneous provider calls can exceed API rate limits, causing one worker's execution demand to impair sibling execution.
- Attenuating coordination relation: first-party bounded concurrency serializes excess work at the subagent manager boundary.
- Feedback into subsequent S1 behaviour: held workers begin only after capacity is released, allowing their later model/tool actions to proceed instead of colliding with the bounded provider resource.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the positive mapping rests on an explicit shared-resource interference statement in first-party code and a mechanism specifically documented as preventing that interference; delegation itself is not credited.
- Evidence: [`src/DotCraft.Core/Agents/SubAgents/SubAgentManager.cs`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/src/DotCraft.Core/Agents/SubAgents/SubAgentManager.cs); [`docs/features/agent-system/subagents.md`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/docs/features/agent-system/subagents.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this is a narrow capacity-coordination function; subagent delegation, result return and separate contexts are not independently treated as S2.

## S3 — Inside-and-now control

- State: C
- Function: regulate the current Oratorio operational portfolio by observing active/queued work, applying deployment and repository/source capacity limits, dispatching eligible work and recovering or interrupting unhealthy active runs.
- Disturbance / variety regulated: concurrent task demand, finite execution capacity, per-repository/source concentration, stalled heartbeats, interrupted runner processes, stale review retries and changing run lifecycle state.
- Decisive decision or feedback right: decide which queued runs may enter `Dispatching`, which remain queued under capacity constraints, which stalled/interrupted executions are terminated or failed, and which obsolete review retries are superseded.
- Decision owner: deterministic first-party Oratorio `AppServerRunWorker` scheduler/recovery policy.
- Supporting / enforcement mechanisms: periodic scheduler tick, deployment-wide active-run query, global/per-repository/per-source counters and caps, leases, heartbeats, run state transitions, retry/recovery logic and active task registry.
- Closure path: live Oratorio portfolio state + configured current-capacity limits → scheduler computes current admissible work → eligible queued runs receive leases and start while constrained runs wait → heartbeat/interruption/current-head changes feed later recovery, cancellation or dispatch decisions → current operational portfolio is regulated.
- Boundary reachability: the worker is the shipped Oratorio AppServer execution path behind the built-in Desktop/project-board product, not contributor-only CI machinery.
- Why this is / is not agent-owned: the whole-portfolio judgment and enforcement are algorithmic scheduling/recovery policy rather than a model actor's discretionary management decision; therefore ownership is constructor/runtime `C`.
- Current-control decision scope: the scheduler decides current admission, holding, dispatch, recovery, interruption and stale-retry supersession across the active/queued Oratorio run portfolio using global, per-repository and per-source capacity plus live heartbeat/run state.
- Whole-system current view: active AppServer runs across the Oratorio deployment plus queued candidates and their repository/source/current-state metadata.
- Resources / commitments / priorities regulated: global active-run capacity, per-repository capacity, per-source capacity, queued execution commitments, leases, heartbeat health and retry eligibility.
- Authority over current operations: scheduler marks runs dispatching, starts work, holds candidates under limits, interrupts/reconciles stalled work and supersedes obsolete review retries.
- Evidence: [`src/DotCraft.Oratorio/Integrations/AppServerRunWorker.cs`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/src/DotCraft.Oratorio/Integrations/AppServerRunWorker.cs); [`docs/features/oratorio.md`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/docs/features/oratorio.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Goals regulate one thread and Automations trigger individual work; they support operational persistence but are not the basis for the S3 claim.

## S3* — Complementary audit

- State: A
- Function: independently inspect pull-request/merge-request code at a pinned current head and diff through a separate read-only model run, produce evidence-backed findings, and return unresolved findings into later implementation work.
- Disturbance / variety regulated: implementation agents or external contributors can produce code that appears complete while containing correctness, security, workflow or maintainability defects not visible through the implementation actor's ordinary reporting path.
- Decisive decision or feedback right: perform a dedicated review-analysis judgment over the actual synchronized review target, submit accepted structured findings, and preserve those findings for publication and later repair context.
- Decision owner: model-driven agent executing the first-party Oratorio `ReviewAnalysis` run.
- Supporting / enforcement mechanisms: separate `RunPurpose.ReviewAnalysis`; current-head synchronization; review diff/base/head context; read-only review mode; structured `SubmitReviewDraft`; anchor validation; safe publication gates; stale-head supersession; persisted open findings injected into follow-up implementation context.
- Closure path: implementation/external PR reaches Oratorio → distinct read-only review-analysis run inspects the current pinned head/diff and submits findings → Oratorio persists/publishes accepted findings and rejects stale target assumptions → later implementation run for the generated PR receives unresolved findings/comments after the last implementation → subsequent S1 work can repair the audited defects.
- Boundary reachability: Oratorio is a bundled product surface; reviews can be started from the Board, Auto Review, or an authorized `@dotcraft-ai review` command, all through the first-party review-analysis path.
- Why this is / is not agent-owned: deterministic code pins the target, restricts the mode and validates/publishes drafts, but the substantive code-review finding judgment is made by the separate model-driven review agent.
- Claim being audited: that the current implementation/PR head is suitable and does not contain material actionable defects within the requested review scope.
- Ordinary reporting path: implementation run summary/draft and the normal task/run lifecycle or external contributor PR description.
- Complementary access path: dedicated read-only review run receives repository/worktree and exact diff/head context and independently inspects code rather than trusting the implementation summary.
- Independence boundary: `ReviewAnalysis` is a distinct run purpose and read-only operating mode with a separate review prompt/tool contract; it does not modify the implementation as part of the audit.
- Who acts on findings: Oratorio persists/publishes them; open findings are carried into later implementation context and operator decision/re-review paths, changing subsequent work.
- Evidence: [`specs/features/oratorio/github-mention-review.md`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/specs/features/oratorio/github-mention-review.md); [`src/DotCraft.Oratorio/Integrations/AppServerPromptBuilder.cs`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/src/DotCraft.Oratorio/Integrations/AppServerPromptBuilder.cs); [`src/DotCraft.Oratorio/Integrations/AppServerRunWorker.cs`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/src/DotCraft.Oratorio/Integrations/AppServerRunWorker.cs); [`docs/features/oratorio/workflow.md`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/docs/features/oratorio/workflow.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: operator approval/request-changes/reject is a parent decision surface and is not used to manufacture the autonomous S3* state; the positive claim is the separate model-driven read-only audit itself plus its feedback path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material distinct external-and-prospective intelligence/adaptation loop is established at the assessed deployment recursion.
- Disturbance / variety regulated: DotCraft can search the web during S1 work, consolidate memory, run Dreams over workspace history/repository evidence, build plugins on request and keep Goals/Automations active over time; these mechanisms do not by themselves create a separate S4 owner.
- Decisive decision or feedback right: no qualifying function is shown that independently models the external/future environment and uses that model to redesign present organizational capability or policy for later operations.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: Dreams, long-term memory consolidation, web tools, plugin creator, Goals, Automations and Agent Builder were inspected as plausible paths but fail the outside-and-then separation/closure threshold.
- Closure path: not applicable for the negative finding.
- Why this is / is not agent-owned: Dreams uses internal workspace history, explicit memory, recent sessions and current repository/spec/docs evidence to generate passive context; plugin creation is invoked when the user asks to create or maintain a plugin. Neither establishes an autonomous external/prospective intelligence loop feeding organizational redesign.
- Evidence: [`specs/features/dreams.md`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/specs/features/dreams.md); [`src/DotCraft.Core/Skills/BuiltIn/plugin-creator/SKILL.md`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/src/DotCraft.Core/Skills/BuiltIn/plugin-creator/SKILL.md); [`docs/features/agent-system/automations.md`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/docs/features/agent-system/automations.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a composed deployment could use DotCraft tools to perform strategic research, but task-level external research is S1 activity unless a distinct first-party S4 organizational loop is established.

### Absence scope

- Surfaces inspected: Dreams scheduling/input/generation/apply flow; explicit memory consolidation; web/search tools; Agent Builder/Profile editing; plugin-creator/self-extension path; Goals; Automations; Oratorio source synchronization and review; planning/workflows.
- Plausible first-party paths checked: Dreams as adaptation; repository/spec evidence as environmental sensing; web tools as intelligence; generated plugins as capability redesign; Agent Builder as self-redesign; scheduled checks as prospective scanning; Goals as strategic direction.
- Why no material first-party path remains: the reviewed adaptation surfaces are driven by internal operational history/current workspace evidence or explicit user/task requests. No separate function owns external/future modeling and closes that intelligence into redesign of current DotCraft organizational capability at this recursion.

## S5 — Policy / identity

- State: P
- Function: define and select durable agent role, instructions, capabilities and approval behavior that govern later DotCraft conversations/tasks through saved Agent Profiles.
- Disturbance / variety regulated: different work contexts require different standing roles, behavioral instructions, tool/skill access, model defaults, MCP access and approval boundaries while preserving a reusable agent identity across future runs.
- Decisive decision or feedback right: create/edit/save the authoritative profile definition and select which saved role/capability policy a later conversation, Automation or Goal will operate under.
- Decision owner: legitimate parent operator through Agent Builder/editor/profile-selection surfaces.
- Supporting / enforcement mechanisms: saved Agent Profile definition; role instructions; tools/skills/MCP/model/approval configuration; profile picker; binding to Automations/Goals; runtime rule that updated profiles apply to refreshed/new conversations/tasks.
- Closure path: parent defines or edits saved profile → profile persists durable role/policy and capability constraints → parent selects/binds it for later work → new/refreshed DotCraft conversation/task is assembled under that profile → subsequent S1 behaviour is governed by the changed standing role/policy.
- Boundary reachability: Agent Profiles are a shipped Desktop/runtime feature and may be used by normal chats, Automations and Goals.
- Why this is / is not agent-owned: Agent Builder can help draft a profile conversationally, but the authoritative save/edit/select decision remains with the parent operator; no first-party autonomous path is established that can unilaterally redefine ultimate deployment identity/policy for future operation.
- Identity / ultimate-policy issue: which durable role, instructions, model/tool/skill/MCP capability set and approval behavior should govern future DotCraft work performed under a saved Agent Profile.
- Ultimate authority in each claimed mode: the legitimate parent operator has ultimate authority to create, edit, save, select or bind the authoritative profile; Agent Builder may assist with drafting but does not own the final policy decision.
- Identity / policy surface: saved role instructions together with the profile's standing tool, skill, MCP, model and approval behavior.
- Legitimate amendment path: parent edits the structured profile or uses Agent Builder to refine the draft, saves it and selects/binds it for future runs.
- Return-to-operation path: the saved/updated profile is selected or bound to a new/refreshed conversation, Automation or Goal, whose runtime is then assembled with that profile's role instructions, capabilities, model defaults and approval behavior; already-running conversations retain their prior setup until refresh/restart.
- Evidence: [`docs/features/agent-system/agent-profiles.md`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/docs/features/agent-system/agent-profiles.md); [`docs/features/agent-system/automations.md`](https://github.com/DotHarness/dotcraft/blob/a08c8b35497f6ba9148f6ede80839835dcc8812a/docs/features/agent-system/automations.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model-authored plugin code, plans, task prompts and one-off instructions are not treated as S5 merely because they influence later execution; S5 credits the durable parent-authorized role/policy surface.

## Structural profile

| System | Autonomy | Basis | Notes |
|---|---:|---|---|
| S1 | A | explicit + structural | Model/tool actors own substantive task action loops. |
| S2 | C | explicit + structural | Runtime concurrency gate attenuates shared-provider rate-limit interference among subagents. |
| S3 | C | explicit + structural | Oratorio scheduler regulates the live run portfolio and deployment/repository/source capacity. |
| S3* | A | explicit + structural | Separate read-only model review analyzes pinned PR/MR heads and returns findings into later implementation. |
| S4 | — | explicit + structural negative search | Dreams/internal memory and user-directed self-extension do not establish outside-and-then intelligence. |
| S5 | P | explicit + structural | Parent-saved Agent Profiles define durable role/capability policy for later runs. |

## Overall

DotCraft is a broad self-hosted agent runtime with autonomous model/tool operations, constructor-owned coordination and current-control layers, a separate autonomous Oratorio code-review audit path, and parent-owned durable Agent Profile policy. Its strongest positive higher-order evidence is not the feature labels themselves: S2 rests on an explicit provider-rate-limit interference attenuator, S3 on deployment-wide current run scheduling/recovery, and S3* on a pinned read-only review-analysis path whose findings return to later implementation. Dreams, memory and plugin self-extension remain below the S4 threshold because they do not establish a distinct external-and-prospective adaptation function.
