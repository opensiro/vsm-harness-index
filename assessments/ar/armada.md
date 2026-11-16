---
harness_id: armada
project_name: Armada
repository: https://github.com/jchristn/Armada
review_ref: bc1114bc72dfb491793f02ddf9bb2fff381d1bb2
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: P
---

# Armada

## Review boundary

- System in focus: The deployed Armada Admiral and its shipped mission runners, fleet clients, Ask control surfaces, Judge workflow and permission policy.
- Purpose and identity: Coordinate parallel model-backed repository work and decide how reviewed results may land.
- Relevant environment: Repository Git remotes, authenticated tenant operators and admins, configured model endpoints or coding runtimes and optional Harbor execution.
- Standard-distribution boundary: The first-party Admiral with local or supported Harbor runtime modes, operator surfaces, shipped Ask captain and optional Judge/overlap/evaluation controls.
- Credited operating / distribution surfaces: Mission and dock lifecycle, first-party captain adapters, Black Box overlap advisor, Ask MCP policies, Judge/rework pipeline, installed evaluation and CLI permissions.
- Adjacent first-party surfaces excluded from ownership: External agent-provider internals, upstream repository acceptance, external MCP orchestrator implementations, release/development CI and adjacent benchmark-only artifacts.
- First-party operating / deployment modes considered: Standalone and pipeline missions, Black Box serialization, Ask auto-approve or explicit decisions, separate-captain Judge, owner-led routing evaluation and administrator-owned CLI rules.
- Recursion level: One Armada tenant fleet with multiple vessels and active captain mission cells. Tenant/global administrator hierarchy is the parent policy boundary.
- Reviewed revision: `bc1114bc72dfb491793f02ddf9bb2fff381d1bb2`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

Armada's Admiral stores fleet, mission, captain and worktree state. It launches configured model engines, provides a separate dock/branch for work, follows typed pipelines, and records commits, outcomes and resource use. Ask runs a packaged captain with scoped MCP access. Independent Judge options, runtime evidence reports and durable permission rules feed distinct decisions at the fleet level. [`README.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/README.md), [`docs/PIPELINES.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/docs/PIPELINES.md), [`docs/ASK_ARMADA_HOME_BASE.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/docs/ASK_ARMADA_HOME_BASE.md), [`src/Armada.Core/Services/DockService.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/Services/DockService.cs), [`src/Armada.Core/Services/MissionService.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/Services/MissionService.cs).

## Operational model

Model-backed captains perform assigned repository development in docks, and the fleet regulates present assignments, conflicts and landing. Ask captain or operator can change live work through the same control service. Independently selected Judge captains can block inadequate changes and return corrective findings. Routing adjustments and durable effect policy have distinct operator/administrator roles.

## S1 — Operations

- State: A
- Function: Produce repository changes through a model-directed mission and return artifacts for integration.
- Disturbance / variety regulated: Variable task briefs, code/repo state, test feedback and available runtime tools.
- Decisive decision or feedback right: Select task-local code and tool actions and respond to execution feedback.
- Decision owner: The assigned model-backed captain under the packaged launch route.
- Supporting / enforcement mechanisms: Mission identity/state, worktree provisioning, tool policies, launch adapters, handoff and completion processing.
- Closure path: Captain acts in its dock and returns output and Git changes. Runtime records the produced work and passes verified state to the next stage or landing path.
- Why this is / is not agent-owned: Removing the model leaves lifecycle handlers and launch adapters without a discretionary implementation actor.
- Evidence: [`README.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/README.md#L390-L448), [`docs/CAPTAINS.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/docs/CAPTAINS.md), [`src/Armada.Server/CaptainLaunchRouter.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Server/CaptainLaunchRouter.cs), [`src/Armada.Core/Services/MissionService.Completion.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/Services/MissionService.Completion.cs#L78-L122)
- Basis: structural
- Confidence: High
- Caveats: Provider/runtime internals and repository maintainers' acceptance rights are outside the ownership claim.
- Boundary reachability: The deployed Admiral routes Worker missions to supported first-party captain launch adapters, including model endpoints and configured external CLIs.

## S2 — Coordination

- State: C
- Function: Attenuate live conflicts between independent missions operating on one repository.
- Disturbance / variety regulated: Different agents can target the same paths in separate branches and cause incompatible edits or landing collisions.
- Decisive decision or feedback right: Choose the vessel's conflict policy and response when suspected overlap requires a dependency or scope change.
- Decision owner: The operator configures the vessel serialization policy and the caller can act on overlap findings. The dispatch advisor deterministically applies the configured rule.
- Supporting / enforcement mechanisms: Separate worktrees and branches, active MissionOverlapAnalyzer, warning/preview, and a dependency inserted before admission when configured.
- Closure path: Advisor compares proposed files against active work and, when enabled, inserts a predecessor dependency. The later mission waits for its prerequisite/terminal stage and can receive updated work context. Independent docks prevent working-tree interference.
- Why this is / is not agent-owned: The product ships a conflict-specific sensor and dependency control. The credited path is constructor-owned because the decisive policy choice is configured, with no requirement that a model choose an answer.
- Evidence: [`docs/BLACKBOX.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/docs/BLACKBOX.md#L860-L884), [`src/Armada.Core/BlackBox/MissionOverlapAnalyzer.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/BlackBox/MissionOverlapAnalyzer.cs), [`src/Armada.Core/BlackBox/BlackBoxDispatchAdvisor.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/BlackBox/BlackBoxDispatchAdvisor.cs#L52-L73), [`src/Armada.Core/Services/DockService.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/Services/DockService.cs#L70-L90), [`src/Armada.Server/Mcp/Tools/McpMissionTools.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Server/Mcp/Tools/McpMissionTools.cs#L102-L125)
- Basis: structural
- Confidence: High
- Caveats: File estimates have coverage limits. Unnamed or incorrectly estimated paths can still conflict later.
- Boundary reachability: The shipped dispatch advisor and overlap API are wired into the Admiral. Serialization is a supported vessel setting and uses the mission dependency consumed by admission.
- Distinct S1 units: Independently assigned model-backed coding missions on the same vessel.
- Inter-S1 disturbance: Two missions may both edit the same named or changed files and contend during landing despite separate checkouts.
- Attenuating coordination relation: Compare the prospective mission with active briefs and branch file changes, warn on overlaps and conditionally chain the prospective mission after the existing one.
- Feedback into subsequent S1 behaviour: The returned warning can revise a dispatch, and a persisted dependency delays a conflicting worker until the preceding mission settles.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The configured ordering arises from observed or inferred conflicting files between actual missions, and changes which mission may run next.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate current fleet commitments in response to running status, failures and resource availability.
- Disturbance / variety regulated: Missions fail, stall, need changed scope or require a different routing/priority choice while other work is active.
- Decisive decision or feedback right: Choose whether to redispatch, cancel or revise portfolio commitments based on the fleet's current state.
- Decision owner: In configured Ask auto-approve mode the Ask captain decides the calls. In the approval/direct operator mode the authenticated operator owns the binding decision.
- Supporting / enforcement mechanisms: Fleet status, work cards, scoped MCP tools, proposal receipts, dispatcher and mission recovery machinery.
- Closure path: A selected restart/cancel/dispatch enters the same Admiral handlers, changes a mission or queue and returns current integration state to the actor. The operator can approve/deny exact proposals on the visible current portfolio.
- Why this is / is not agent-owned: The captain makes bounded current-control choices when allowed direct MCP effects. In the distinct operator mode a decision does not take effect until the operator confirms or issues it.
- Evidence: [`README.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/README.md#L495-L527), [`docs/ASK_ARMADA_HOME_BASE.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/docs/ASK_ARMADA_HOME_BASE.md), [`src/Armada.Server/CaptainChatService.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Server/CaptainChatService.cs#L141-L195), [`src/Armada.Server/Ask/AskActionService.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Server/Ask/AskActionService.cs#L236-L272), [`src/Armada.Server/Ask/AskActionService.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Server/Ask/AskActionService.cs#L545-L590), [`src/Armada.Server/Mcp/Tools/McpMissionTools.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Server/Mcp/Tools/McpMissionTools.cs#L455-L495)
- Basis: structural
- Confidence: High
- Caveats: The A mode requires an eligible configured runtime and a thread whose effect policy permits the calls. Deterministic retry policies are support evidence, not the credited owner.
- Boundary reachability: Ask is shipped with dashboard/TUI/mobile. Its captain uses the Admiral's scoped MCP tools. The same surface supports an explicit owner-decision mode and direct user quick actions.
- Whole-system current view: Ask reads fleet/captain and mission status, sees failed/live work and receives durable work-card status for chosen actions.
- Current-control decision scope: Restart or cancel current missions, change instructions for restart, and dispatch replacement or follow-on commitments across leads/vessels.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Authorized Ask captain with auto-approval enabled | Current mission state calls for a workload or recovery decision | Scoped MCP choice updates live mission and returns its state | [Ask workflow](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/README.md#L495-L527) |
| Parent (`P`) | Authenticated fleet operator | Live status, failure or proposal requiring operator decision | Confirmed/direct call changes the current portfolio and returns its result | [Approval handler](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Server/Ask/AskActionService.cs#L236-L272) |

## S3* — Complementary audit

- State: A
- Function: Challenge the claim that a committed implementation satisfies its mission and may progress.
- Disturbance / variety regulated: The Worker can report completion while the actual diff violates scope or a verifiable requirement despite routine build/test signals.
- Decisive decision or feedback right: Judge then issue a substantiated `PASS`, `NEEDS_REVISION`, `FAIL` or specification-conflict finding based on the candidate.
- Decision owner: A separately selected model-backed Judge captain in the author-excluded mode.
- Supporting / enforcement mechanisms: Artifact handoff with actual Git diff/commit or pointer, separate captain selection, typed verdict/affected-case checks and branch-bound rework scheduling.
- Closure path: A substantiated rejection can send the same branch to a new Worker stage with the evidence, schedule a new review and block subsequent pipeline progress. A valid pass can advance the gate.
- Why this is / is not agent-owned: The model Judge owns the audit judgment. The parser validates its form and the coordinator implements rework or fail-closed handling.
- Evidence: [`README.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/README.md#L583-L613), [`README.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/README.md#L1104-L1107), [`src/Armada.Core/Services/MissionService.CaptainRouting.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/Services/MissionService.CaptainRouting.cs#L58-L95), [`src/Armada.Core/Services/HandoffArtifactBuilder.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/Services/HandoffArtifactBuilder.cs#L91-L142), [`src/Armada.Core/Services/MissionService.Completion.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/Services/MissionService.Completion.cs#L586-L684), [`src/Armada.Core/Services/MissionService.Rework.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/Services/MissionService.Rework.cs#L85-L171)
- Basis: structural
- Confidence: High
- Caveats: The credited path uses `ExcludeReviewAuthorsFromJudge` and the supported no-human-intermediate-gate configuration. Default fallback may allow the author. Human landing or specification scope decisions can still exist.
- Boundary reachability: A shipped Judge persona runs through the ordinary pipeline/dispatch path. The strict independence setting and gate configuration are available deployment options.
- Claim being audited: The produced code at the reviewed branch/revision meets the original mission scope and behavior before progress.
- Ordinary reporting path: Worker completion, produced artifact snapshots and ordinary stage build/test output.
- Complementary access path: The Judge receives primary Git evidence and original mission requirements and can inspect the actual checked-out candidate and provide an affected case.
- Independence boundary: With author exclusion, prior stage captains cannot be assigned as Judge for their own chain. Evidence is tied to the actual product diff.
- Who acts on findings: Admiral applies the Judge verdict and schedules Worker rework and a new Judge or leaves the work blocked. Later work follows the new handoff dependency.

## S4 — Outside-and-then intelligence

- State: P
- Function: Select future captain capabilities and routing for the fleet under changing provider/runtime conditions.
- Disturbance / variety regulated: New or changing model/runtime backends can differ in tool support, context, reliability and future persona fit.
- Decisive decision or feedback right: Use observed evaluation alternatives to choose which runtime/endpoint candidates are eligible or preferred for future persona work.
- Decision owner: A fleet operator or administrator configuring persona priority/routing.
- Supporting / enforcement mechanisms: Quick/full evaluation requests, provider probes/fixture outcomes, persisted reports, persona priority editors and eligibility selector.
- Closure path: A user evaluates concrete captain/endpoint candidates for a future persona. Updating the ordered priority binds later mission admission to the approved operating decision, while later evaluations or observed missions can inform another update.
- Why this is / is not agent-owned: Actors benchmark and report candidate capability. The human chooses and commits a future routing change.
- Evidence: [`README.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/README.md#L163-L177), [`src/Armada.Core/Services/ModelProbeService.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/Services/ModelProbeService.cs#L134-L237), [`docs/CAPTAIN_ROUTING.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/docs/CAPTAIN_ROUTING.md#L5-L53), [`docs/CAPTAIN_ROUTING.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/docs/CAPTAIN_ROUTING.md#L160-L176), [`src/Armada.Core/Services/PersonaCaptainPrioritySelector.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/Services/PersonaCaptainPrioritySelector.cs)
- Basis: structural
- Confidence: High
- Caveats: The needed parent judgment is supplied by the operator. The metric or report itself does not select future production routing.
- Boundary reachability: The shipped Evaluate surfaces and persona routing controls are available in the deployed dashboard and corresponding API/clients.
- External distinction: Evaluate tests selected external model/provider/runtime combinations and their actual context/tool/format behavior.
- Future / prospective distinction: An evaluation can be run before assigning an engine to a persona for later real missions.
- Adaptation option generated: Separate evaluated backends and role-specific outcomes make candidate routing hierarchies concrete and comparable.
- Path back into current capability / S3: The parent edits ordered persona alternatives and the persisted settings drive the later mission captain selector.

## S5 — Policy and identity

- State: P
- Function: Govern which categories of CLI effects may be durably authorized for the tenant fleet.
- Disturbance / variety regulated: A live captain can request authority for an effect outside its existing standing envelope. The deployment may need to decide whether this category should be authorized in future missions.
- Decisive decision or feedback right: Decide if authority is granted once or established as an enduring policy rule, and set the scope and rule action.
- Decision owner: Global admin or tenant admin for their respective scope. Mission/thread tokens do not own policy decisions.
- Supporting / enforcement mechanisms: Permission requests/inbox, role-scoped deciding routes, persisted rules and matcher.
- Closure path: A qualifying prompt reaches authorized administration. Allow-and-remember commits an ongoing rule, which the policy resolver/matcher uses for later matching prompts. The admin can later edit or revoke the rule.
- Why this is / is not agent-owned: An operator may approve an action once if delegated. Durable authorization remains a different administrator-held authority and constrains later model work.
- Evidence: [`docs/REST_API.md`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/docs/REST_API.md#L4633-L4655), [`src/Armada.Server/Routes/CliPermissionRoutes.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Server/Routes/CliPermissionRoutes.cs#L105-L133), [`src/Armada.Server/Routes/CliPermissionRoutes.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Server/Routes/CliPermissionRoutes.cs#L168-L260), [`src/Armada.Core/Services/CliPermissionService.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/Services/CliPermissionService.cs#L321-L382), [`src/Armada.Core/Services/CliPermissionRuleMatcher.cs`](https://github.com/jchristn/Armada/blob/bc1114bc72dfb491793f02ddf9bb2fff381d1bb2/src/Armada.Core/Services/CliPermissionRuleMatcher.cs)
- Basis: structural
- Confidence: High
- Caveats: This is about standing tenant effect authority in `ApproveInArmada` and supported CLI paths. One-time tool or deployment approval is a separate act.
- Boundary reachability: Supported embedded CLI permission prompts and the first-party Approvals center use the same authorized Armada service.
- Identity / ultimate-policy issue: Whether an effect category can become an enduring permission of future fleet missions versus a one-time operational exception.
- Ultimate authority in each claimed mode: Tenant/global administrator at its actual decision scope. No model or ordinary scoped token may change standing policy.
- Return-to-operation path: A remembered rule persists and applies to later matching requests. Rule deletion/update changes later authorization.

## Recursion

Captain missions perform local operations. Vessel and fleet controls regulate the resulting work portfolio. A tenant/global administrator decides standing authority above the individual mission. External Git owners govern independent repositories.

## Variety and escalation

Docks and overlap-derived dependencies attenuate mission interference. Branch-bound Judge findings drive bounded rework. Fleet status, scoped restart and approval surfaces feed operator or agent current control. Specification conflicts can reach a person under the pipeline's documented gates.

## Evidence gaps

The assessment inspects the pinned production code, operator docs and test surfaces. No provider or deployed Armada fleet was run. Scope is limited to supported configurations and the evidence-backed ownership paths described here.

