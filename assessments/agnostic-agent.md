---
harness_id: agnostic-agent
project_name: agnostic-agent
repository: https://github.com/ucsandman/agnostic-agent
review_ref: 8b1f4d85c9220822aacea3921a78c4c2f0c58491
reviewed_at: 2026-10-11
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# agnostic-agent

## Review boundary

- System in focus: the first-party Python `agnostic` terminal coding-agent session, with its `AgentLoop`, tools, headless and TUI consumers, default subagents and supported optional adaptive orchestration. Focus is the coding organization executed in one workspace, not every external tool/provider/maintainer.
- Purpose and identity: carry out user-directed repository coding, investigation, code repair and verification, sometimes using multiple bounded child agents.
- Relevant environment: project filesystem/git checkout, shell/tests, model endpoints and subscription CLIs, user/operator, installed custom MCP tools, provider availability and configured safety limits.
- Standard-distribution boundary: packaged TUI and headless CLI, default first-party agent loop and tools, `/research`, `/review`, `/swarm`, `/test` and `/fix`, plus shipped optional `/org on` / role/profile orchestration. `/org` is **disabled by default** but wired by `AgentLoop.configure_orchestration` and actively usable in the shipped CLI; positive optional-mode claims say so.
- Credited operating / distribution surfaces: [agent/loop.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/loop.py#L38-L200), [agent/loop.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/loop.py#L400-L620), [agent/headless.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/headless.py#L99-L171), [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L127-L255), [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L599-L685), [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L954-L1059), [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L1096-L1332), [agent/orchestration/config.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/config.py#L82-L130), [agent/tools/subagent.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/tools/subagent.py#L201-L367), [agent/cli.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/cli.py#L830-L1100), [agent/governance/guard.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/governance/guard.py#L69-L145).
- Adjacent first-party surfaces excluded from ownership: [.github/workflows/ci.yml](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/.github/workflows/ci.yml), [tests/test_orchestration.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/tests/test_orchestration.py), [tests/test_orchestration_hardening.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/tests/test_orchestration_hardening.py), contributor development [CONTRIBUTING.md](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/CONTRIBUTING.md), documentation-only hypothetical [docs/orchestration.md](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/docs/orchestration.md) examples, external `AGNOSTIC_HARNESS_ROOT` / provider CLI / installed MCP server implementations not in the shipped session.
- First-party operating / deployment modes considered: default agent loop with nested helper subagents, operator-triggered `/swarm`/test/fix; interactive `/org on` and auto/hierarchy/advisor modes with typed role-specific agent executors; `agnostic -p` single prompt/headless. Do not borrow an external Claude Code team's governance from optional model target names or supplied policy files.
- Recursion level: one root user-directed coding session whose subagents are task-scoped independent S1 candidates; the repository maintainer team and user across all workplaces are adjacent recursions.
- Reviewed revision: `8b1f4d85c9220822aacea3921a78c4c2f0c58491`.
- Observation date: 2026-10-11.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The root `AgentLoop.run_turn` owns a model/tool/feedback loop. It streams a model response, dispatches first-party tools, appends results to history and lets the model select next operations; read-only tools in one model response may execute concurrently while mutating tools are sequential. The tool layer also includes file edits, shell commands, MCP integration, project memory, safety checks and governance action logs. Headless mode runs the same loop rather than wrapping another coding-agent executable. [agent/loop.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/loop.py#L38-L76); [agent/loop.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/loop.py#L400-L610); [agent/headless.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/headless.py#L99-L169).

A `SubagentManager` creates distinct model contexts and uses `OrchestrationManager` with a graph of parent/child roles, bounded agent counts, provider fallback, cancellation, permissions and workspace leases. In the **optional** `/org` mode, the root's orchestration tools include `delegate_agent`, `delegate_parallel`, `consult_advisor` and `route_task`; profiles distinguish permission to mutate, child authority and model target. Flat legacy subagents remain reachable when organization is off. [agent/loop.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/loop.py#L115-L201); [agent/tools/subagent.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/tools/subagent.py#L201-L369); [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L599-L640); [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L1437-L1568).

Parallel child jobs may write in a shared checkout. The first-party orchestrator detects *more than one mutating sibling* trying to inherit the same workspace and rejects the fan-out unless explicitly allowed; branch-mode child leases are isolated, and unavailable required isolation fails closed. Child status and patch artifacts return to parent. This is a specifically identified interference/attenuation cycle between distinct coding S1 units, but it is enforced by deterministic constructor policy rather than autonomous negotiation. [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L127-L195); [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L1096-L1196); [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L1255-L1332).

The governance `AuditManager` records and formats the session's *own* events and `/retro` report; `AutoTestRunner` runs a normal operational test/fix loop. `Learner.record_lesson` records manual correction candidates and increments a simple sightings tier. These do not without more evidence amount to a separately owned S3* complementary audit or externally prospective S4 adaptation loop. [agent/governance/audit.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/governance/audit.py#L38-L105); [agent/workflows/tester.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/workflows/tester.py#L17-L125); [agent/governance/learn.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/governance/learn.py#L19-L87).

## Operational model

The root model receives an operating purpose from a user and chooses coding tools/optional delegation. Children individually choose actions inside scoped permissions; a returned report/patch is handed back to the root for task-level integration. The deterministic runtime tracks active child counts, worktree leases and call budget and rejects invalid interference-prone parallel plans. The human/agent hierarchy distinction is explicit: a root agent chooses tasks/routes when it calls tool functions, but the constructor chooses/executes hard invariants; users define policies/role config and issue ordinary intervention. No inherited autonomy is credited from provider subscription models, CI or nearby development harnesses.

## S1 — Operations

- State: A
- Function: first-party model-directed coding, search, edit, test and repair of a user-selected workspace.
- Disturbance / variety regulated: source contents, tool failures, project goals, change requests, test feedback, provider/tool exceptions and context pressure.
- Decisive decision or feedback right: choose next coding tool/task and revision based on returned source/shell/test evidence; supported children choose their own scoped task actions.
- Decision owner: root or dispatched child model-guided agent as relevant within first-party owned execution loop.
- Supporting / enforcement mechanisms: ToolRegistry, safety guard, worktree lease manager, model-client adapter, context and bounded call counts.
- Closure path: tool observations / errors → history messages → next root/child model call → revised tool/action.
- Boundary reachability: TUI and `agnostic -p` construct `AgentLoop` and run its first-party `run_turn`; no third-party coding-agent CLI is required to own that loop.
- Why this is / is not agent-owned: model actor independently selects next coding action subject to constructor limits; removing actor removes meaningful task discretion.
- Evidence: [agent/loop.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/loop.py#L400-L615); [agent/headless.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/headless.py#L99-L169); [agent/workflows/tester.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/workflows/tester.py#L17-L125); [agent/tools/subagent.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/tools/subagent.py#L121-L199)
- Basis: structural
- Confidence: high for runtime-discretion ownership; no benchmark performance claim.
- Caveats: providers determine model tokens; subscribed Claude/Codex external engines are not imported as first-party harness ownership.

## S2 — Coordination

- State: C
- Function: attenuate concrete destructive workspace collision among concurrently operating independent child coding S1 units, with isolated or explicitly disallowed shared mutations.
- Distinct S1 units: two or more simultaneously delegated `AgentExecutor` child nodes from `delegate_parallel` / `spawn_parallel`, each with a separate context and task packet; branch-mode units have independently tracked workspaces.
- Inter-S1 disturbance: multiple mutating children writing in the same inherited git checkout risk overwriting or contaminating one another's file changes; concurrent children also compete for bounded active/parallel slots.
- Attenuating coordination relation: before fan-out, `spawn_parallel` rejects more than one mutating inherited sibling unless `allow_shared_mutation` is deliberately selected; `delegate` establishes mandatory isolated worktree lease for mutating branch-mode child and fails closed if required isolation cannot be created.
- Feedback into subsequent S1 behaviour: eligible child receives separated workspace for execution; an unsafe batch returns `OrchestrationError` and must be replanned; child report and captured patch are returned to parent before workspace cleanup, limiting unintended cross-child interference.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the code tests a *specific pairwise shared-write collision* among distinct operating S1 workers and selects a regulating response (reject or isolate), not merely choosing a role or moving a message.
- Disturbance / variety regulated: interference among concurrent mutating workstreams and shared workspace access.
- Decisive decision or feedback right: choose whether a parallel multiwriter batch is admissible under selected isolation policy and bind separated workspaces; choice is deterministic, with optional human configuration `allow_shared_mutation`.
- Decision owner: first-party deterministic orchestration constructor, not an autonomous model selecting collision-control policy.
- Supporting / enforcement mechanisms: workspace manager worktree leases, per-agent counters, graph status and permission model.
- Closure path: proposed parallel children → conflict predicate / workspace-mode resolution → rejection or independent worktrees → child output/patch returned to parent for further coordinated task work.
- Boundary reachability: shipping `/org on` enables `delegate_parallel` tool from root; root and child agents are created by `AgentLoop` / `SubagentManager`. Legacy `/swarm` also supports git worktree operation.
- Why this is / is not agent-owned: the root model chooses tasks, while the conflict relation and enforcement remain the same without its organizational judgment; positive S2 function is constructor-owned, hence C.
- Evidence: [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L1255-L1332); [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L154-L196); [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L1096-L1196); [agent/loop.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/loop.py#L176-L201); [agent/orchestration/config.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/config.py#L104-L116); [agent/tools/subagent.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/tools/subagent.py#L337-L367)
- Basis: structural
- Confidence: high for collision predicate and feedback in optional enabled orchestration; medium for broader real-world effect.
- Caveats: no claim that S2 is autonomously negotiated, always enabled, or proven effective by independent benchmark. Counterexample `allow_shared_mutation: true` opts out of the attenuation.

## S3 — Inside-and-now control

- State: —
- Function: no demonstrated independently owned whole-current management decision cycle across ongoing S1 commitments at this session recursion.
- Disturbance / variety regulated: current model capacity, costly agents, failures, active child counts, resource slots, cancellations and worktree lifetime.
- Decisive decision or feedback right: operator chooses budgets/role limits and tool permission policy; deterministic `_reserve` enforces them. `route_task` offers a heuristic based on caller-supplied signals rather than authoritatively revising whole-system commitments from a reconciled current view.
- Decision owner: constructor limit config / caller's task-level discretion; no demonstrated S3 whole-current authority exercising a control decision and binding returned shared resource/priority changes.
- Supporting / enforcement mechanisms: ExecutionGraph status snapshot, child counters, workspace lease and timeout/cancel, rate or expensive-model limits, routing tool.
- Closure path: local child reservation accepts/rejects a specific request, or provides task guidance; no evidenced manager-level S3 resource bargaining/intervention with subsequent whole-current accountability.
- Why this is / is not agent-owned: a root/manager role name and child result synthesis alone are task orchestration; fixed capacity checks and status dashboards do not transfer discretionary S3 authority to an agent.
- Evidence: [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L319-L381); [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L954-L1059); [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L1334-L1435); [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L1536-L1568)
- Basis: structural
- Confidence: medium; optional hierarchy supplies real current-operation instrumentation, but not a proven whole-system S3 closure.
- Caveats: S2-specific isolated workspace and resource-safety rights should not be promoted to S3 merely because both execute in OrchestrationManager.

### Absence scope

- Surfaces inspected: optional orchestration graph/status/counters, reservation/routing, manager/executive profiles, workspace leases and cancellation, TUI `/org` and `/agents` paths.
- Plausible first-party paths checked: manager/executive role, graph snapshot, `route_task` previous_failures/current_worker_count, limits and model fallback, child task packet and parent result handling.
- Why no material first-party path remains: the observable view is available but no structurally evidenced whole-system discretionary decision over shared current priorities/commitments is coupled to returned supervisory reallocation; fixed configured limits enforce rather than own resource governance.

## S3* — Complementary audit

- State: —
- Function: no separately attributable complementary judgment channel with obligatory or established corrective findings-return beyond normal code/test review.
- Disturbance / variety regulated: bugs, hallucinated task completions, unsafe changes and inaccurate agent claims; tools provide normal review, test results and session audit logs.
- Decisive decision or feedback right: optional read-only `reviewer` and `verification-manager` roles may inspect artifacts when delegated, `/review` invokes a requested child, and `AuditManager` prints recorded operational events; no first-party mandatory independent claim-relative audit verdict owner/closure is evidenced.
- Decision owner: task agent/operator for optional reviewer invocation; audit log merely records its own events, role descriptions do not instantiate an independent auditor.
- Supporting / enforcement mechanisms: reviewer/tester/verification-manager role definitions, file diff and test tools, `/audit` retrospective log.
- Closure path: generic review or test report to requester/task context; no independent complementarily sourced audit findings channel with consequential control closure.
- Why this is / is not agent-owned: a code reviewer and a role called `verification-manager` could be used to build S3*, but an ordinary delegated first-party task and self-generated audit log alone cannot claim this function.
- Evidence: [agent/orchestration/config.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/config.py#L489-L520); [agent/tools/subagent.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/tools/subagent.py#L219-L230); [agent/cli.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/cli.py#L830-L845); [agent/governance/audit.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/governance/audit.py#L38-L105); [agent/workflows/tester.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/workflows/tester.py#L17-L125)
- Basis: structural
- Confidence: medium; reviewed real optional review/audit features and did not equate a role label with audit ownership.
- Caveats: a private workflow could instruct children to conduct complementary audits, but the current pinned distribution does not wire a claim-relative independent audit and downstream authority.

### Absence scope

- Surfaces inspected: role definitions, reviewer/tester/verification-manager dispatch, `/review`, `/audit` event logging, test/fix cycle, governance hard-stop records and CI tests.
- Plausible first-party paths checked: read-only reviewer direct raw source access, independent verification-manager by description, after-the-fact `/retro` report, auto test and security guard.
- Why no material first-party path remains: no shipped binding turns one of these optional task-oriented checks into independently controlled complementary evidence judgment with a consequential return to organizational current control; audit report is generated from the same event stream it documents.

## S4 — Outside-and-then intelligence

- State: —
- Function: no evidenced external-and-future-oriented option-generation and accepted adaptation loop into present system capability.
- Disturbance / variety regulated: task errors, test regressions, remembered project decisions, changing models or external search results.
- Decisive decision or feedback right: agent may request new task research or fix current tests; `Learner` logs repeated lessons as tiered candidates. No agent/operator-authorized prospective capability change has a first-party S4 closure.
- Decision owner: user/operator for model configuration and task direction, model agent for current coding and test fixes, deterministic memory entry counting.
- Supporting / enforcement mechanisms: persistent MemoryStore, `Learner.record_lesson`, `/model` picker, browsing tools, context compactor.
- Closure path: memory and lessons may inform later task context; no demonstrated scanned external trend → considered future capability options → adopted change to operating capability.
- Why this is / is not agent-owned: storing feedback, changing providers or auto-repairing today's tests is not necessarily prospective adaptation.
- Evidence: [agent/governance/learn.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/governance/learn.py#L19-L87); [agent/governance/memory.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/governance/memory.py#L59-L232); [agent/workflows/tester.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/workflows/tester.py#L107-L145); [agent/cli.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/cli.py#L625-L765)
- Basis: structural
- Confidence: medium-high for bounded no-S4 shipped path.
- Caveats: external providers, contributor changes and an optional private workflow may enable strategic learning outside assessed recursion.

### Absence scope

- Surfaces inspected: learning candidate recording, memory index, context manager, test/fix workflow, model/provider picker, orchestration routing and model fallback.
- Plausible first-party paths checked: tiered lesson candidate store, `/learn`, retrospective audits, research/web tools, saved preference/fact memory, adaptive model-selection failures.
- Why no material first-party path remains: positive mechanisms regulate current tasks or store historical feedback, but there is no source-closed external/prospective adaptation-decision loop that reconfigures future S1 capacity.

## S5 — Policy and identity

- State: —
- Function: no established ultimate-identity issue and legitimate deciding authority whose binding decision returns as operating policy within one AshCode-equivalent agnostic-agent session.
- Disturbance / variety regulated: unsafe shell/file access, secrets, per-session trust, provider and role settings, user guidance and shared work safety.
- Decisive decision or feedback right: static shipped `guards.json`, environment/operator overrides and interactive confirmations set/enforce safety bounds; no evidenced S5-specific identity/policy adjudication cycle.
- Decision owner: operator/developer for configured safety and purpose, deterministic guard for policy application; ordinary task approvals do not imply ultimate authority.
- Supporting / enforcement mechanisms: SafetyGuard trust tiers, guarded tool interception, role permission matrix and system prompt source.
- Closure path: per-tool access is allowed/rejected under configured policy, but no first-party identity/policy issue escalates to legitimate higher authority and returns a revised binding ultimate-policy decision.
- Why this is / is not agent-owned: a packaged `guards.json` or root `executive` role is not S5 simply because it carries safety limits or a hierarchy name.
- Evidence: [agent/governance/guard.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/governance/guard.py#L29-L111); [agent/governance/interceptor.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/governance/interceptor.py#L52-L132); [agent/orchestration/config.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/config.py#L415-L439); [agent/cli.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/cli.py#L340-L390)
- Basis: structural
- Confidence: medium-high
- Caveats: maintainer policies belong to a higher project recursion; optional external governance integrations are not silently borrowed.

### Absence scope

- Surfaces inspected: packaged guard rules, trust-tier changes, interceptor, role permissions and operator root config, system prompt, related project documentation.
- Plausible first-party paths checked: user policy override, /trust, governance hard stops, role capability graph, model/prompt owner, upstream maintainer policy.
- Why no material first-party path remains: these paths gate ordinary execution under preselected constraints, without a source-observed first-party ultimate-policy deliberation and returned authoritative change at the declared recursion.

## Recursion

In the supported optional orchestration mode, each delegated `AgentExecutor` has its own model context, scoped tools, objective, graph node and (optionally) isolated worktree. This is evidence for multiple interacting operational units. A nested agent should not automatically be described as a complete recursively viable organization: its purpose, wider S3/S4/S5 autonomy, identity and return to the parent are explicitly bounded. [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L290-L381); [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L425-L598).

## Variety and escalation

Concurrent workspace mutation variety is attenuated by refusing unsafe shared-writer fan-out or allocating owned git worktrees; child patches/reports are returned to the parent for integration. Active agent limits, expensive-model availability, failure routing and cancellation constrain operational variety, but may remain deterministic support rather than S3 ownership. A repeated failure can route to a stronger-model advisor or task escalation by configured policy; this is not automatically S3 policy closure or an algedonic channel. [agent/orchestration/runtime.py](https://github.com/ucsandman/agnostic-agent/blob/8b1f4d85c9220822aacea3921a78c4c2f0c58491/agent/orchestration/runtime.py#L1255-L1435).

## Evidence gaps

- This is first-party source mapping at an immutable upstream commit, not a recorded production trace or independent performance audit. No hidden private orchestration or external subscription agent's organizational choices are imported.
- The S2=C positive is **limited to shipped opt-in orchestration**, not the default `/org off` mode; structural evidence identifies multi-writer conflict and a hard isolation/rejection loop. Autonomy ownership is not upgraded from the deterministic enforcer.
- S3 whole-current authority is deliberately not inferred from aggregate counters/manager role labels. An independently observed operator or manager control cycle could motivate future same-ref re-review, but no concrete unresolved shipped closure was found to force `?` under Methodology 0.3.7.
- S3* reviewer/tester/verification-manager labels and `/audit` logging were actively examined; no source-evidenced independent *claim-relative complementary audit judgment plus downstream consequential control* is established in the shipped workflow.
