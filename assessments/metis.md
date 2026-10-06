---
harness_id: metis
project_name: Metis
repository: https://github.com/Wholiver/metis
review_ref: 8dc0d6da31e878b620ef3c3a412a5c7dff8164a2
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Metis

## Review boundary

- System in focus: the first-party Metis coding runtime at frozen revision \`8dc0d6da31e878b620ef3c3a412a5c7dff8164a2\`, including the root coding session, named recursive agents, Performance admission/gates, spawn/management tools, workspace/worktree isolation, verification roles, memory coordinator, sessions and supported terminal/desktop/headless/RPC/server modes.
- Purpose and identity: perform software-engineering work through a root coding agent that can admit complex work, decompose it into governed lanes, dispatch specialist coding agents, control their lifecycle, isolate parallel mutation and require independent review/verification before completion.
- Relevant environment: user objectives/approvals, repository/worktree state, child process status/results, test/typecheck/runtime evidence, dependency/lane state, provider/model responses, persisted sessions and memory, extension/MCP services and host operating-system tools.
- Standard-distribution boundary: shipped Metis runtime and built-in roles/tools/governance. External model providers, MCP/extensions, benchmark tasks, host tools and the user's repository are dependencies and cannot donate ownership.
- Credited operating / distribution surfaces: \`src/core/agent-session.ts\`, \`src/core/agent-definition.ts\`, \`src/core/tools/spawn_agent.ts\`, \`src/core/tools/agent-management.ts\`, \`src/core/workspace-probe.ts\`, \`src/core/worktree.ts\`, \`src/core/performance-runtime.ts\`, \`src/core/performance-mode.ts\`, system prompts, memory coordinator and supported user interfaces.
- Adjacent first-party surfaces excluded from ownership: benchmark/adapters as evaluation evidence, repository CI/release workflows and development-only tests unless the corresponding runtime mechanism is shipped and reachable.
- First-party operating / deployment modes considered: ordinary root coding; Performance T0–T3 governed mutation; recursive named agents; async child execution; isolated/shared workspace modes; reviewer/verifier assurance; terminal/desktop/headless/RPC/server execution; durable memory enabled mode.
- Recursion level: one Metis coding organization rooted at a user session. Root/coordinator and write-capable implementer agents can own operational outcomes; coordinator/root current-control decisions regulate the instantiated worker set; reviewer/verifier roles are complementary assurance actors.
- Reviewed revision: \`8dc0d6da31e878b620ef3c3a412a5c7dff8164a2\`.
- Observation date: 2026-10-06.
- Generated Profile version: \`0.2.4\`.
- Generated Methodology version: \`0.3.6\`.
- Current Profile version: \`0.2.4\`.
- Current Methodology version: \`0.3.6\`.

## Repository architecture

Metis ships a model/tool coding session plus a native named-agent subsystem. Built-in roles include coordinator, planner, implementer, reviewer and verifier. The root or admitted coordinator can dispatch children synchronously or asynchronously through \`spawn_agent\`, and the agent-management tools expose live child status, waiting, termination and guidance messages.

For complex Performance work, admission creates typed lanes with explicit dependencies, owned paths, acceptance criteria and verification commands. T3 permits parallel implementation only for dependency-ready lanes with pairwise-disjoint owned paths and no shared mutable state. Runtime workspace policy can place mutating children into isolated worktrees; shared-cwd mutation also has a registry that rejects overlapping ownership claims. The coordinator decides the substantive decomposition/lane dispatch, while deterministic runtime code enforces those decisions.

Independent assurance is first-party and explicit. Reviewer and verifier are separate built-in model roles. Performance G5 requires an independent reviewer; G6 requires an independent verifier, both against the integrated/current workspace. Negative review or verification routes work back to implementation/planning instead of allowing completion.

The frozen runtime also contains a durable SQLite-backed memory coordinator that extracts/stores verified procedures, known failures/fixes, preferences and searchable memory summaries for later sessions. This is useful persistence and retrieval, but no distinct frozen first-party mechanism was found that turns changing outside/future conditions into adaptation options for the current organization; memory alone therefore is not promoted to S4.

## Operational model

The root model owns ordinary coding actions. When work requires multiple operational units, the admitted coordinator determines dependency-safe lanes and dispatches specialized children. Child lifecycle/status is observable through the first-party management API, and the parent can wait, kill, or message individual children. Results and assurance verdicts feed back to the parent/current Performance frontier.

Coordination and control are separated from enforcement. Worktree creation, owned-path overlap rejection, process-group termination, concurrency caps and gate persistence enforce decisions. The positive S2/S3 claims rely on model-owned decomposition/current worker decisions that use those mechanisms, not on deterministic machinery alone.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and verify software through model-selected repository/tool actions, directly at root or in bounded implementation agents.
- Disturbance / variety regulated: unfamiliar code, implementation decisions, build/test/runtime failures, tool/process errors, context pressure, model/provider variability and bounded delegated work.
- Decisive decision or feedback right: choose substantive engineering actions, interpret repository/test evidence, select repairs and decide when an assigned operational objective is complete.
- Decision owner: the active model-backed root coding agent and write-capable implementer agents within their admitted boundaries.
- Supporting / enforcement mechanisms: tool runtime, permissions, model routing, sessions/compaction, spawn guard, worktrees, Performance lane contracts and verification tools.
- Closure path: user/current parent objective → model chooses direct or delegated implementation actions → first-party runtime executes and returns evidence → agent revises/repairs → operational result returns to parent or closes the root task.
- Boundary reachability: ordinary and governed Performance modes instantiate the shipped AgentSession/tool runtime; implementer is a built-in named agent.
- Why this is / is not agent-owned: deterministic host machinery constrains execution, but the model chooses and interprets the open-ended engineering work.
- Evidence: [README.md](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/README.md); [src/core/agent-session.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/agent-session.ts); [src/core/agent-definition.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/agent-definition.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: T0/T1 may remain single-root operation; positive multi-agent functions are claimed only for reachable governed modes that instantiate them.

## S2 — Coordination

- State: A
- Function: attenuate destructive interference among concurrently active coding S1 lanes by choosing dependency-safe ownership boundaries and enforcing non-overlapping mutation/isolation.
- Disturbance / variety regulated: concurrent agents editing overlapping paths, shared mutable-state collisions, integration drift and dependency-order violations.
- Decisive decision or feedback right: choose operational lane decomposition, dependencies and owned paths, determine which lanes may run in parallel, and select isolated versus shared execution under admitted runtime policy.
- Decision owner: the model-backed coordinator/root operating from the typed Performance admission and current roadmap.
- Supporting / enforcement mechanisms: T3 disjoint-owned-path admission checks, SharedMutatingOwnerRegistry overlap rejection, worktree snapshot/isolation, SpawnGuard concurrency/depth caps and child workspace cleanup/retention.
- Closure path: coordinator decomposes current work into owned lanes → runtime checks dependencies/overlap and creates isolated workspaces where required → peer workers execute without shared mutation → their results/integrated workspace return → coordinator proceeds with integration/assurance or repairs rejected lanes.
- Boundary reachability: built-in coordinator and Performance T2/T3 routes are shipped; \`spawn_agent\` exposes lane/worktree bindings and the runtime enforces admitted ownership.
- Why this is / is not agent-owned: the runtime rejects illegal overlap, but the coordinator owns the discretionary task partition, lane boundaries and parallelization decisions that define the coordination relation.
- Distinct S1 units: root/implementer coding agents operating admitted implementation lanes.
- Inter-S1 disturbance: overlapping writes/shared mutable state can corrupt or invalidate parallel work; frozen Performance admission explicitly rejects overlapping T3 lane paths and shared mutable state.
- Attenuating coordination relation: dependency/owned-path partition plus physical worktree isolation or shared-cwd exclusive mutation claims.
- Feedback into subsequent S1 behaviour: conflicting ownership prevents launch/parallelization; child results and integrated state determine whether lanes can advance to assurance or require repair.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism is explicitly tied to a concrete peer-S1 mutation/interference risk and changes whether/how those peer units may execute.
- Evidence: [src/core/agent-definition.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/agent-definition.ts); [src/core/performance-runtime.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/performance-runtime.ts); [src/core/tools/spawn_agent.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/tools/spawn_agent.ts); [src/core/workspace-probe.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/workspace-probe.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: worktree/ownership enforcement is deterministic; the A classification rests on the model coordinator's discretionary decomposition and parallelization authority.

## S3 — Inside-and-now control

- State: A
- Function: maintain a whole-current view of delegated work and regulate active commitments through dispatch, wait, guidance, termination, backtracking and gate/frontier decisions.
- Disturbance / variety regulated: failed, blocked, timed-out or runaway workers; incomplete dependencies; reviewer/verifier rejection; active-child capacity; lanes that need repair or replanning.
- Decisive decision or feedback right: inspect the current worker set/status/results, message or kill a selected worker, wait/collect groups, decide which dependency-ready lane to dispatch, stop completed workers and route failed assurance back to implementation/planning.
- Decision owner: the model-backed root/coordinator in reachable multi-agent Performance modes.
- Supporting / enforcement mechanisms: \`list_agents\`, \`wait_agent\`, \`kill_agent\`, \`message_agent\`, SpawnGuard lifecycle state, Performance frontier/gates, child result schema and process-group cleanup.
- Closure path: root/coordinator observes current frontier plus child statuses/results → makes a current commitment/control decision (dispatch/wait/message/kill/backtrack/advance) → runtime executes it → updated worker/frontier evidence returns → parent makes the next current decision.
- Boundary reachability: agent-management tools are first-party model-callable tools; the built-in coordinator prompt explicitly requires current worker lifecycle management and zero live children at handoff.
- Why this is / is not agent-owned: deterministic lifecycle/state machinery exposes and enforces controls, but the coordinator chooses the substantive response to current worker/gate state.
- Whole-system current view: Performance state supplies current frontier/admission/lane state while \`list_agents\` exposes tracked children, status, parent/depth, elapsed time, exit/result/error.
- Current-control decision scope: current lane dispatch, collection, targeted guidance, kill/cascade, retry/backtrack after failed assurance and final convergence/handoff.
- Evidence: [src/core/tools/agent-management.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/tools/agent-management.ts); [src/core/agent-definition.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/agent-definition.ts); [src/core/performance-runtime.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/performance-runtime.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: hard concurrency/depth/timeout limits themselves are not S3 owners; they support the coordinator's live current-control decisions.

## S3* — Complementary audit

- State: A
- Function: independently challenge implementation claims through author-independent review and grounded verification before the Performance frontier can converge.
- Disturbance / variety regulated: incorrect implementation claims, scope creep, security/regression risks, missing tests and false completion despite failing real-system evidence.
- Decisive decision or feedback right: independently inspect the integrated repository/diff or run real verification and return pass/reject/failure evidence that determines whether work may advance.
- Decision owner: separate built-in reviewer and verifier/fresh-verifier model agents.
- Supporting / enforcement mechanisms: dedicated read-only/restricted role toolsets, fresh child contexts, G5/G6 Performance gates, real repository/test access, typed child results and backtracking rules.
- Closure path: implementation reaches assurance frontier → root/coordinator dispatches fresh reviewer and verifier → those agents independently inspect integrated code/run evidence → verdicts return to host → failures backtrack to implementer/planner; passing assurance permits frontier advance.
- Boundary reachability: reviewer/verifier are built-in roles and explicitly admitted by Performance routes; frozen runtime maps reviewer to G5 and verifier/fresh-verifier to G6.
- Why this is / is not agent-owned: substantive audit/verifier judgments come from separate model contexts with direct repository/runner access; the host gate only validates/routes their result.
- Claim being audited: implementation correctness/completeness and readiness of the integrated change.
- Ordinary reporting path: implementer's own ChildResult and implementation/test account.
- Complementary access path: reviewer directly reads/searches/diffs the repository; verifier executes grounded tests/typechecks/runtime checks against the integrated workspace.
- Independence boundary: author-independent named roles, fresh child processes/contexts, role-specific tools and explicit G5/G6 assurance gates.
- Who acts on findings: root/coordinator/Performance host routes failures back to implementation/planning and only advances on passing assurance.
- Evidence: [src/core/agent-definition.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/agent-definition.ts); [src/core/performance-mode.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/performance-mode.ts); [src/core/performance-runtime.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/performance-runtime.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: host-side deterministic gate validation is support; S3* ownership rests on the independent reviewer/verifier judgments and evidence paths.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established at the assessed frozen revision.
- Disturbance / variety regulated: no qualifying changing outside/future condition is shown being transformed by a distinct intelligence owner into adaptation options that return into current S3 capability.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: SQLite memory extraction, searchable durable records, memory map/overview, session resume, provider/model configuration and extensions preserve/retrieve experience but do not by themselves close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: the memory coordinator extracts and stores procedures/failures/preferences and can inject/retrieve them later, but the frozen \`src/core\` exposes no separate adaptation mechanism that converts external/future distinctions into prospective organizational options returned to current control.
- Evidence: [src/core/memory-coordinator.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/memory-coordinator.ts); [src/core/tools/query-memory-db.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/tools/query-memory-db.ts); [README.md](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: later repository revisions may add stronger self-learning/adaptation machinery; that cannot be backported into this frozen review.

### Absence scope

- Surfaces inspected: memory coordinator/extraction/search, memory overview injection, sessions/compaction, provider/model selection, extensions/MCP, Performance admission and named-agent definitions.
- Plausible first-party paths checked: autonomous learned workflow/policy revision, adaptation proposals, environment scanning, capability reconfiguration and future-option feedback into S3.
- Why no material first-party path remains: frozen core paths store/retrieve verified experience or configure current execution; no distinct outside-and-then option-development return loop was found.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level or ultimate-policy dispute is routed to an authoritative S5 owner and returned as governing organizational policy.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: Performance admission, system prompts, role/tool allowlists, trust/security settings and user/project configuration strongly govern execution but operate below identity/ultimate-policy closure.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: root/coordinator can govern task execution and assurance but cannot authoritatively redefine Metis's identity or ultimate operating principles.
- Evidence: [src/core/system-prompt.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/system-prompt.ts); [src/core/performance-runtime.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/performance-runtime.ts); [src/core/agent-definition.ts](https://github.com/Wholiver/metis/blob/8dc0d6da31e878b620ef3c3a412a5c7dff8164a2/src/core/agent-definition.ts).
- Basis: structural absence review.
- Confidence: high.
- Caveats: strong execution governance is not automatically S5; no ultimate identity-policy issue/authority/return path is established.

### Absence scope

- Surfaces inspected: system prompts, Performance governance, named-agent role definitions, tool allowlists, trust/security/configuration, memory and user/project settings.
- Plausible first-party paths checked: autonomous constitution revision, organizational identity adjudication, ultimate-policy conflict resolution and authoritative policy feedback.
- Why no material first-party path remains: located governance determines task execution/admission/assurance rather than system identity or ultimate policy.

## Distributed OSS parent arrangement

The assessed organization is the running Metis agent organization, not its GitHub maintainer project. Repository contribution/release governance and benchmark operators are not imported as runtime parent functions.

## Self-hosted and non-human modes

Metis supports multiple local/hosted providers and headless/server/RPC operation. The positive S2/S3/S3* claims use first-party runtime/model-agent paths and do not depend on a human operator.

## Recursion

The root session is the viable-unit boundary. Root/implementer agents are S1 when owning coding outcomes; coordinator/root owns S2/S3 over current operational lanes; independent reviewer/verifier roles supply S3*. Recursive child depth alone is not treated as a higher VSM function.

## Variety and escalation

S1 handles local engineering variety. S2 attenuates cross-worker mutation/dependency interference. S3 regulates current worker/frontier commitments and backtracking. S3* independently challenges implementation claims with direct repository/runner evidence. Memory, limits and governance support execution but do not establish S4/S5 at this frozen ref.

## Evidence gaps

No \`?\` state is required. The frozen runtime directly exposes the named-agent, worktree/ownership, management and assurance paths needed for the positive S1/S2/S3/S3* claims, and its memory/governance surfaces are broad enough to support the bounded S4/S5 absence conclusions.
