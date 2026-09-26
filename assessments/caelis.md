---
harness_id: caelis
project_name: Caelis
repository: https://github.com/caelis-labs/caelis
review_ref: 5aebbc6a750b8b2d472a0987fbf2e0942062c6d9
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Caelis

## Review boundary

- System in focus: one first-party Caelis work Session at pinned revision `5aebbc6a750b8b2d472a0987fbf2e0942062c6d9`, including the main Agent Runtime, Control-owned collaboration service, configured native or ACP participants, shared Session messaging/thread observation, approval/Guardian machinery, memory subsystem and the shipped `/review` Reviewer path.
- Purpose and identity: an engineering-agent workspace that executes user-directed software work through a model/tool runtime and can coordinate addressable collaborating Agents inside one Session while preserving Control-owned lifecycle, permissions and controller authority.
- Relevant environment: user objectives and follow-up, the selected local workspace and processes, model providers, configured MCP/external ACP endpoints, participant outputs and messages, approval decisions, persisted Session/task state and optional durable memory.
- Standard-distribution boundary: released Caelis product/runtime code and documented CLI/TUI/AppServer operating surfaces at the frozen revision. Repository CI/evals/tests and maintainer development activity may corroborate contracts but do not own credited VSM decisions. Arbitrary downstream MCP servers and external ACP implementations are environment unless assembled through a first-party Caelis participant/runtime path described below.
- Credited operating / distribution surfaces: `agent-sdk/runtime`, first-party tool/model loop, `app/gatewayapp` runtime composition and system prompt, `control/collaboration`, model-facing `StartThread`/`ListThreads`/`ReadThread`/`WaitThread`/`SendMessage`, native and configured ACP participants, first-party Session/task persistence, the shipped `/review` Reviewer scene, Guardian approval path and built-in memory/runtime bindings.
- Adjacent first-party surfaces excluded from ownership: repository `eval/` regression harnesses, tests, CI/build/release tooling, architecture checks, developer fixtures and documentation-only examples. These are used only to corroborate shipped contracts. Later default-branch behavior after the frozen ref is excluded.
- First-party operating / deployment modes considered: ordinary single-Agent model/tool execution; controller-led multi-participant collaboration with native or configured ACP Agents; running-participant steering where supported; user-started persistent Reviewer; attended/manual and automatic Guardian approval modes; optional built-in memory with Steward/Verifier enrichment.
- Recursion level: one Caelis work Session organization. The main controller and each independently running participant conversation are operational S1 units for S2/S3 analysis, but participant Sessions are not promoted to fully recursive viable systems solely because each can run an Agent loop.
- Reviewed revision: `5aebbc6a750b8b2d472a0987fbf2e0942062c6d9`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Caelis separates product Control from the reusable Agent SDK. `agent-sdk/runtime` owns the model/tool execution mechanics, Session semantics, task/delegation contracts, sandbox/policy primitives and subagent execution. Product Control owns configuration, placement, Agent assembly, endpoint lifecycle, permissions, orchestration, controller selection and handoff. The ordinary main Agent receives a system prompt plus first-party tools and executes a persisted model/tool feedback loop against the workspace.

Collaboration is Session-scoped. The controller alone can create participant work with `StartThread` and observe public participant results with `ReadThread`/`WaitThread`; all participants can discover peers and exchange explicit mail. Start requests are model-visible and require a self-contained task containing goal, scope, constraints, edit permission and expected output. The shipped collaboration prompt tells the controller to create collaborators only for independent work, to retain responsibility for integration/validation and to read participant results before acting on them. Running participants that advertise steering support can receive `SendMessage` input while active.

This collaboration path sits over a shared workspace where concurrent effects are real. Caelis' runtime contract states that a canonical Turn owns its Session execution fence and that overlapping writes require an explicit purpose plus matching revision or fence. The controller's task decomposition therefore determines which operational units are safe to run as independent collaborators and what scope/edit permission they receive; revision/fence machinery constrains effects, while returned results/messages let the controller revise subsequent participant or main-Agent action.

Caelis also ships a separate Reviewer scene. `/review` starts a persistent background Reviewer with a fixed workspace-review prompt covering staged, unstaged and untracked changes, concrete correctness/regression/maintainability/architecture/test findings, and an instruction not to modify code unless explicitly asked. The Reviewer can be backed by its own configured model or ACP Agent and retains a separate child context for follow-up. Because the standard invocation is the user `/review` surface rather than an autonomous system-owned audit trigger, the complementary audit function is present as a constructor path rather than autonomous S3* ownership.

The optional memory subsystem and Guardian are not promoted beyond their evidenced functions. Memory Steward/Verifier organize internal durable memory and validate memory-enrichment proposals; they do not establish an external-and-prospective adaptation loop. Guardian classifies concrete approval requests and may inspect evidence, but the architecture explicitly states that Guardian does not independently audit task completion. Static identity/workflow prompts, permissions, approval policy and Control-owned controller selection constrain operation but do not close an identity/ultimate-policy issue through a runtime S5 authority.

Primary evidence:

- [`agent-sdk/runtime/runtime.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/agent-sdk/runtime/runtime.go) — first-party Runtime, persisted Session/Run execution, Agent factory, tools/tasks/subagents, policies, approvals and controller integration.
- [`app/gatewayapp/internal/promptassembly/prompt.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/app/gatewayapp/internal/promptassembly/prompt.go) — shipped main-Agent workflow/identity/workspace instructions and the collaboration rule limiting `StartThread` to independent work while retaining integration and validation with the controller.
- [`agent-sdk/tool/builtin/spawn/tool.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/agent-sdk/tool/builtin/spawn/tool.go) — model-visible `StartThread`; each task prompt includes goal, scope, constraints, edit permission and expected output.
- [`control/collaboration/tools.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/control/collaboration/tools.go) — controller-only `ReadThread`/`WaitThread`, shared roster/mail tools and model-facing thread status/result feedback.
- [`control/collaboration/controller.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/control/collaboration/controller.go) — current-controller grant required for creation and controller prompt slice establishing creation/observation responsibility.
- [`docs/agent-sdk-boundary.md`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/docs/agent-sdk-boundary.md) — Control/SDK ownership boundary, child-vs-controller tool rights, controller selection/handoff, concurrency/effect fencing, Guardian limits and durable-runtime contracts.
- [`docs/participants.md`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/docs/participants.md) — participant topology, controller-exclusive start/result observation, messaging, Reviewer mode and fixed participant roles.
- [`internal/controlprompt/review.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/internal/controlprompt/review.go) — fixed independent workspace-review instructions.
- [`internal/controlprompt/appserveradapter/participant.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/internal/controlprompt/appserveradapter/participant.go) — `/review` starts a persistent background Reviewer Task; follow-ups retain the same child context.
- [`app/gatewayapp/review_scene.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/app/gatewayapp/review_scene.go) — Reviewer is materialized as a separately configured model or ACP Agent in the fixed reviewer scene.
- [`docs/architecture.md`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/docs/architecture.md) — Control ownership, runtime composition, memory Steward/Verifier behavior and lifecycle boundaries.

## Operational model

The main Caelis model is the ordinary S1 owner: it chooses substantive tools/actions and updates later choices from tool/environment feedback. In collaboration mode, `StartThread` creates additional operational Agent conversations. The main model remains the controller: it decides which independent tasks to delegate, supplies each task's scope and edit permission, observes the roster/current participant state and public results, can send further input/steering, and owns integration/validation of the combined work. Control authenticates and enforces that topology but does not make the task-specific decomposition or integration decision for the model.

The same product supplies a materially separate workspace Reviewer, but ordinary audit invocation is a user command. Memory, approvals, policy and handoff machinery provide support/governance constraints without establishing the missing S4/S5 functions at this review boundary.

## S1 — Operations

- State: A
- Function: perform user-directed engineering work through repeated model-selected tool actions against the workspace and other admitted resources, incorporating tool/environment observations until the task concludes.
- Disturbance / variety regulated: heterogeneous user goals, repository/workspace state, command and file outcomes, external tool/provider responses, approval/sandbox conditions, task failures and follow-up input.
- Decisive decision or feedback right: choose the next substantive model/tool action and its task-specific arguments, then revise later action from returned evidence.
- Decision owner: the active Caelis Agent model in the main Runtime; each started collaborator independently owns the same local operational discretion within its assigned task.
- Supporting / enforcement mechanisms: Agent SDK Runtime, tool definitions/execution wrappers, Session/event persistence, sandbox/policy and approval gates, task lifecycle, compaction and Control-owned runtime composition.
- Closure path: user/session context → model chooses action/tool → Runtime validates and executes or requests approval → result/event is persisted and returned into model context → the Agent chooses its next action or final response.
- Boundary reachability: this is the normal shipped Caelis Runtime assembled by the product; no eval or developer-only runner is required to exercise the model/tool loop.
- Why this is / is not agent-owned: policy/sandbox/approval machinery can constrain an attempted action, but removing the model removes the task-specific choice of what operational action to take next and how to respond to its result.
- Evidence: [`agent-sdk/runtime/runtime.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/agent-sdk/runtime/runtime.go); [`app/gatewayapp/internal/promptassembly/prompt.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/app/gatewayapp/internal/promptassembly/prompt.go); [`docs/agent-sdk-boundary.md`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/docs/agent-sdk-boundary.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: Control and the Runtime own admission, persistence and enforcement; those mechanisms do not inherit the Agent's substantive S1 decision right.

## S2 — Coordination

- State: A
- Function: attenuate interference among concurrently operating participant S1 units by limiting parallel delegation to independent work, assigning task-specific scope/edit authority and allowing explicit steering/integration when participant work interacts.
- Disturbance / variety regulated: multiple participant Agents can otherwise perform dependent or overlapping work in the same delivery workspace, duplicate effort, act on stale assumptions or create conflicting effects/results that cannot be safely integrated.
- Decisive decision or feedback right: decide which work is sufficiently independent to run as a collaborator, define its self-contained goal/scope/constraints/edit permission, and send task-specific follow-up/steering when participant findings require coordination.
- Decision owner: the main controller Agent model. The shipped prompt makes independence and integration its responsibility; the `StartThread` schema exposes the scope/edit-permission decision to that model.
- Supporting / enforcement mechanisms: Control-authenticated participant topology, Session execution fencing, revision/fence requirements for overlapping writes, `StartThread`, `SendMessage`, shared mailbox/roster, public-result observation and durable Session/task identities.
- Closure path: controller model identifies independent work and specifies scope/edit permission → participant S1 executes within that assignment → shared messages or thread outcomes expose relevant interaction/results → controller can steer with `SendMessage`, wait/read the participant and change subsequent participant/main work → controller performs integration/validation before user delivery.
- Boundary reachability: the independence rule is injected into the shipped main-Agent system prompt and `StartThread`/mail/thread tools are part of the first-party collaboration runtime; no downstream coordinator is required.
- Why this is / is not agent-owned: deterministic fencing/revision rules enforce effect safety, but they do not decide task-specific independence, participant scope or how returned findings should alter concurrent work. Those coordination judgments belong to the controller model.
- Evidence: [`app/gatewayapp/internal/promptassembly/prompt.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/app/gatewayapp/internal/promptassembly/prompt.go); [`agent-sdk/tool/builtin/spawn/tool.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/agent-sdk/tool/builtin/spawn/tool.go); [`control/collaboration/tools.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/control/collaboration/tools.go); [`docs/agent-sdk-boundary.md`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/docs/agent-sdk-boundary.md).
- Basis: explicit + structural
- Confidence: medium-high
- Caveats: Caelis does not expose TaiXu-style per-child write leases or a global conflict scheduler. S2 credit rests on the shipped model-owned independent-work/scope/steering relation plus concrete shared-workspace effect fencing, not on generic messaging alone.
- Distinct S1 units: the main controller Agent plus two or more independently running participant Agent conversations created with `StartThread`, each executing its own assigned task and returning a public result.
- Inter-S1 disturbance: dependent or overlapping participant work can duplicate effort, use conflicting assumptions or attempt overlapping workspace effects; the runtime explicitly treats overlapping writes as requiring a matching revision/fence.
- Attenuating coordination relation: the controller is instructed to spawn only independent work, defines each participant's scope/edit permission, can exchange targeted messages/steering and retains integration/validation responsibility; runtime revision/fence rules enforce concurrent effect consistency.
- Feedback into subsequent S1 behaviour: participant mail/status/results return through `SendMessage`/`ReadThread`/`WaitThread`; the controller uses them to steer or revise later participant/main action and to decide what can be integrated into final delivery.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited path is not the mailbox by itself; it is the explicit independent-work and scope/edit-permission relation tied to a structurally evidenced shared-workspace concurrency disturbance and returned steering/integration feedback.

## S3 — Inside-and-now control

- State: A
- Function: maintain current control over the Session's active participant organization by creating commitments, observing current participant state/results, steering work and deciding how participant outcomes are integrated into the live user task.
- Disturbance / variety regulated: changing participant roster/state, running versus blocked/attention-needing/completed work, partial or conflicting findings, participant capabilities, newly discovered facts and the need to reallocate current task commitments.
- Decisive decision or feedback right: create or withhold participant commitments, select participant/task/scope, observe live thread state/results, send follow-up/steering, wait for selected work and decide whether to integrate, redirect or continue the current job.
- Decision owner: the main controller Agent model for task-specific current-control decisions; Control authenticates the current controller epoch and enforces exclusive controller capabilities.
- Supporting / enforcement mechanisms: `ListThreads`, controller-only `ReadThread`/`WaitThread`, `StartThread`, `SendMessage`, current-controller grants, participant/task state, Session persistence, Control-owned placement/lifecycle and controller-epoch enforcement.
- Closure path: controller creates a set of current participant commitments → participants execute and update status/results/messages → controller observes roster plus selected current results/attention states → controller steers, waits, launches changed work or integrates outcomes → later S1 execution follows the revised current-control decision.
- Boundary reachability: controller-only capabilities are wired into the standard first-party collaboration surface and injected into the parent Agent; they are not test-only lifecycle APIs.
- Why this is / is not agent-owned: Control owns topology security, placement and controller selection, but does not choose the task-specific portfolio, delegation content, steering or integration response. Removing the controller model leaves enforcement but not materially the same discretionary current-control decisions.
- Evidence: [`control/collaboration/controller.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/control/collaboration/controller.go); [`control/collaboration/tools.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/control/collaboration/tools.go); [`docs/participants.md`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/docs/participants.md); [`docs/agent-sdk-boundary.md`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/docs/agent-sdk-boundary.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: model-facing collaboration does not expose an arbitrary hard kill/reassignment API; S3 is established through commitment creation, current whole-roster/thread observation, steering and integration authority rather than deterministic cancellation machinery.
- Whole-system current view: `ListThreads` exposes the Session participant roster; controller-only `ReadThread` returns a participant's latest public result and status, while `WaitThread` waits across selected threads for completion or attention. Together these let the controller inspect the current operational portfolio rather than only a final batch result.
- Current-control decision scope: choose active participant commitments and their task/scope, send steering or follow-up input where supported, wait/read selected work, start changed/additional participant work and decide how current outputs affect the main task's integration and completion.

## S3* — Complementary audit

- State: C
- Function: independently review current workspace changes through a separate Reviewer Agent/context rather than relying only on the main Agent's own completion/reporting path.
- Disturbance / variety regulated: the main operational Agent may miss correctness defects, regressions, maintainability/architecture issues or inadequate tests in the current staged/unstaged/untracked workspace delta.
- Decisive decision or feedback right: inspect the current workspace change from the fixed Reviewer scene and produce a separate findings judgment that can challenge the main Agent's ordinary delivery assessment.
- Decision owner: the configured Reviewer model or ACP Agent owns the review judgment once invoked; however, standard audit initiation is the user `/review` path, so an autonomous system-owned invocation/closure is not established at this ref.
- Supporting / enforcement mechanisms: fixed reviewer scene/instructions, separately materialized Reviewer placement, persistent background Reviewer Task, separate child context and follow-up routing.
- Closure path: user invokes `/review` → Control starts a persistent Reviewer with the fixed workspace-review prompt → Reviewer independently inspects and reports findings → the result is available in the same Session for human/controller follow-up and can change subsequent work. The first-party audit path exists, but autonomous invocation is left open.
- Boundary reachability: `/review` is a shipped Caelis control surface and Reviewer materialization is first-party runtime code supporting either a configured model or ACP Agent; no repository CI reviewer is borrowed.
- Why this is / is not agent-owned: the audit judgment itself is made by a distinct Reviewer Agent rather than deterministic parsing, but the ordinary path does not give the operating organization an independent autonomous right to trigger that audit. This is therefore `C`, not `A`.
- Evidence: [`internal/controlprompt/review.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/internal/controlprompt/review.go); [`internal/controlprompt/appserveradapter/participant.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/internal/controlprompt/appserveradapter/participant.go); [`app/gatewayapp/review_scene.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/app/gatewayapp/review_scene.go); [`docs/participants.md`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/docs/participants.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: Guardian is not credited here; the architecture explicitly limits Guardian to approval/risk review and states that it does not independently audit task completion.
- Claim being audited: that the current workspace delta is correct, regression-safe, maintainable, architecturally sound and sufficiently tested for delivery.
- Ordinary reporting path: the main Agent executes the user task, performs its own verification/integration and returns the user-facing result through its normal model/tool Session.
- Complementary access path: a separately materialized Reviewer Agent receives a fixed prompt to inspect staged, unstaged and untracked workspace changes and lead with concrete findings.
- Independence boundary: separate Reviewer model/ACP placement, background Task and retained child context; it is not the main Agent merely re-reading its own final answer. Invocation remains user-owned at the standard `/review` surface.
- Who acts on findings: the human/controller can continue the Reviewer and change subsequent main/participant work based on findings; the standard path does not itself grant Reviewer authority to commit or close the parent task.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective organizational adaptation loop was established at the reviewed standard-distribution boundary.
- Disturbance / variety regulated: not established for an S4 loop. Caelis can search/use external tools and can organize memory, but those mechanisms serve current work or internal recall rather than a future-oriented environmental adaptation function.
- Decisive decision or feedback right: not established for changing present organizational capability from an external/prospective adaptation judgment.
- Decision owner: none established for S4 at this boundary.
- Supporting / enforcement mechanisms: MCP/tool discovery, configurable models/agents, skills, memory `Remember`/`Recall`, optional Memory Steward and Memory Verifier, runtime configuration snapshots and ordinary human configuration.
- Closure path: no qualifying external/prospective signal → adaptation option → present capability change closure was found in the shipped runtime.
- Why this is / is not agent-owned: tool selection, retrieval, semantic memory organization and provider configuration can improve current execution context, but no evidenced first-party actor owns a distinct outside-and-then adaptation judgment whose result changes the organization's future capability.
- Evidence: [`docs/architecture.md`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/docs/architecture.md); [`docs/agent-sdk-boundary.md`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/docs/agent-sdk-boundary.md); [`app/gatewayapp/internal/promptassembly/prompt.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/app/gatewayapp/internal/promptassembly/prompt.go).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: future/default-branch capability evolution is outside this frozen review; generic extensibility or a downstream skill/MCP that implements adaptation would be a separate system-in-focus.

### Absence scope

- Surfaces inspected: README and architecture/participant/SDK-boundary docs; Agent Runtime and runtime composition; model-facing tool/prompt surfaces; collaboration/control; skills/MCP discovery; memory Steward/Verifier description; Reviewer/Guardian behavior; configuration and participant placement.
- Plausible first-party paths checked: memory enrichment as possible learning/adaptation, ToolSearch/MCP discovery as possible environmental intelligence, configurable participant/model placement, skills and persistent Session state, and any documented autonomous scheduler/background mechanism that could change future capability.
- Why no material first-party path remains: inspected memory paths reorganize internal task evidence/recall, external tools serve current requests, and configuration/skills require pre-existing capability or external/operator changes. No shipped path closes external distinction plus prospective option generation back into a changed present capability under an S4 decision owner.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity/ultimate-policy closure was established at the reviewed Session recursion.
- Disturbance / variety regulated: static identity, user objectives, sandbox/approval constraints, controller selection and configuration are present, but no runtime issue path decides what the organization ultimately is or which ultimate policy should govern it.
- Decisive decision or feedback right: not established for S5 identity/ultimate-policy judgment.
- Decision owner: none established for S5 at this boundary.
- Supporting / enforcement mechanisms: built-in identity/workflow prompts, user/workspace instruction precedence, sandbox/policy registry, Guardian/manual approvals, Control-owned controller selection/handoff and operator configuration.
- Closure path: ordinary user/configuration/approval inputs can constrain subsequent actions, but no qualifying identity/ultimate-policy issue is routed to a legitimate S5 authority and returned as authoritative organizational policy closure.
- Why this is / is not agent-owned: the main model interprets tasks within a predefined identity/policy envelope; it does not own authority to redefine that envelope. Control enforces controller/policy state but no first-party runtime process establishes a separate ultimate-policy judgment loop.
- Evidence: [`app/gatewayapp/internal/promptassembly/prompt.go`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/app/gatewayapp/internal/promptassembly/prompt.go); [`docs/agent-sdk-boundary.md`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/docs/agent-sdk-boundary.md); [`docs/architecture.md`](https://github.com/caelis-labs/caelis/blob/5aebbc6a750b8b2d472a0987fbf2e0942062c6d9/docs/architecture.md).
- Basis: explicit + structural absence
- Confidence: high
- Caveats: generic operator/user authority is not published as S5 without a first-party function-specific identity/policy closure; downstream organizational governance is outside this standalone harness assessment.

### Absence scope

- Surfaces inspected: built-in identity/workflow prompts; user/workspace/global instruction precedence; policy/sandbox and approval/Guardian paths; Control controller selection/handoff; participant roles and runtime configuration; memory and durable Session state.
- Plausible first-party paths checked: main-Agent system prompt as possible identity closure, user approval as possible parent governance, Guardian as possible policy authority, Control controller-selection/handoff as possible ultimate authority, and configuration/memory as possible persistent policy change.
- Why no material first-party path remains: these surfaces either statically define/constrain operation, decide concrete action approval, or select current controller placement. None exposes a first-party runtime loop for an identity/ultimate-policy issue whose authoritative resolution governs subsequent operation at the declared Session recursion.

## Recursion

The assessed recursion is one Caelis work Session. Participant conversations are distinct operational units with their own model/tool activity and persistent identities, but Caelis explicitly preserves one-level collaboration authority: started participants can discover/message peers yet cannot create/observe work like the parent controller. That supports S1 plurality without assuming each participant is a complete recursive viable system.

## Variety and escalation

Caelis absorbs operational variety through model-selected tools, sandbox/policy checks, approvals, durable task/session state, participant delegation, explicit peer mail, controller observation/steering and optional Reviewer/Guardian/memory services. Escalation is function-specific: concrete risky tool requests can route through approval/Guardian; participants can message parent/peers; current participant states/results return to the controller; user `/review` can invoke complementary audit. These escalation mechanisms are not independently promoted to S4 or S5.

## Evidence gaps

The frozen ref provides strong source/doc evidence for the shipped collaboration and Reviewer contracts. The main semantic sensitivity is S2: Caelis does not expose a dedicated per-participant write-lease scheduler; the positive mapping depends on the explicit first-party rule that only independent work is parallelized, model-owned task scope/edit permission, concrete overlapping-write revision/fence semantics and returned steering/integration feedback. If future evidence showed those controller instructions were not actually reachable by the shipped main Agent, S2 would require reassessment. S3* remains `C` because the reviewed standard path requires user `/review` initiation; a later system-owned independent audit trigger would require a new-ref reassessment rather than silently upgrading this artifact.
