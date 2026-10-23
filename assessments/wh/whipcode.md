---
harness_id: whipcode
project_name: WhipCode
repository: https://github.com/context-labs/whip
review_ref: 801b3a4f9412356cf36934701bce67a1fe30f6bb
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# WhipCode

## Review boundary

- System in focus: the first-party installed WhipCode coding harness (`context-labs/whip`) at the frozen revision, comprising a daemon-owned recursive agent tree and its supported CLI, TUI, Desktop and Web control clients.
- Purpose and identity: perform coding and repository-development work through model-directed tool cells; delegate bounded subwork to persistent child agents under a common permission, state, message and budget runtime.
- Relevant environment: changing user goals, repository files, shell results, tool/provider failures, concurrent edits, child progress, permission choices, project instructions, persistent session state and current operator interventions.
- Standard-distribution boundary: built-in `Coding()` / optional `JuniorDeveloper` definition, native `AgentSession` runtime, host modules, daemon/session store and first-party control clients. Inference providers, browser/computer backends, MCP servers, OS/Git and user-authored agent definitions/skills provide services or configurations rather than additional first-party independent governing actors.
- Credited operating / distribution surfaces: `internal/agentdef/`, `internal/agent/`, `internal/daemon/recursive_runtime.go`, `internal/daemon/agent_session.go`, `internal/daemon/client_control.go`, `internal/session/{swarm,mailbox,state}.go`, `internal/rlm/`, `internal/protocol/`, `packages/app/src/details/{observation,session-controls}.tsx` and shipped CLI/TUI/SDK application bindings.
- Adjacent first-party surfaces excluded from ownership: `evals/` and its separate verifier/benchmark workloads, development and dogfood notes, repository contributor instructions/CI/release pipelines, feature-roadmap proposals and tests/fixtures. They can corroborate runtime behavior but do not become operational review, strategy or governance agents in an installed session.
- First-party operating / deployment modes considered: coding root with recursive `agents.spawn/submit/list/inspect/stop`, child message and shared-state coordination, delegated read/write limits, operator inspection/steer/stop/revoke, optional named definitions and local skill discovery, goal/schedule facilities, headless CLI, TUI, Desktop and Web.
- Recursion level: one root session and its retained child/grandchild S1 agents (default two delegation edges), assessed at each parent–direct-child coordination/control boundary. Different user installations and upstream OSS maintainers are not one supervising operational system.
- Reviewed revision: `801b3a4f9412356cf36934701bce67a1fe30f6bb` (batch #1006 frozen row 3).
- License screen: root `LICENSE` is Apache-2.0.
- Observation date: 2026-10-23.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The daemon constructs the first-party `Coding()` agent with model-facing `rlm_exec` and installed modules for files, shell, models, child agents, messaging, state, permissions and external integrations. One `AgentSession` type serves root and child. The provider decides which bounded Starlark/QuickJS cell to run next in response to returned host results; runtime policy and capabilities admit or deny actual effects. `agents.spawn` creates independent retained sessions with narrowed capabilities and budgets. Spawned workers execute concurrently, preserve private transcripts and deliver completion/failure notices and optional reports through a durable mailbox.

Within the tree, independently deciding children can interact through message delivery and a shared blackboard with append, compare-and-swap, version-conflict rejection and subscriptions. The daemon also serializes same-path file mutations, while explicitly leaving decomposition of parallel shell/edit work to the parent. The model-facing `agents.list/inspect` exposes the current direct-child cohort and budgets; `agents.submit` steers or queues changed work; `agents.stop/delete` terminalizes a child subtree. Desktop/Web inspector and other clients show the current tree, progress, messages, budgets and effective grants and allow a human to stop a subtree, cancel a turn, submit work and revoke a delegated grant.

Whip's docs illustrate spawning an ad hoc read/shell-limited `reviewer` child. The shipped `Coding()` definition, however, is a generic coding persona, and the example does not establish a dedicated installed claim-relative reviewer protocol, a complementary-evidence requirement or audit findings linked to correction. The specialized `reviewer` named child found in `internal/agentdef/definition_test.go` is a test-only fixture. Likewise the separate evaluation verifier under `evals/` benchmarks the harness as a product; it does not audit ordinary end-user coding operations.

Primary frozen sources: [runtime documentation](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/docs/rlm-runtime.md), [concurrency](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/docs/concurrency.md), [tools](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/docs/tools.md), [coding definition](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/agentdef/coding.go), [recursive runtime](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/daemon/recursive_runtime.go), [shared state](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/session/state.go).

## Operational model

Model-backed root and child sessions perform and revise real coding actions (`S1=A`). The parent has a substantive coordination option over concurrently operating children: assign disjoint tasks/tools and respond to versioned shared-state conflicts or incoming reports (`S2=A`). The parent model can additionally observe the active direct-child portfolio and redirect, stop or reprioritize current commitments; the installed human-facing control client offers a distinct supervisory view and intervention loop (`S3=A(P)`). Generic reviewer composition, present-task memory/scheduling and action-level permission enforcement do not on their own complete separate S3*, S4 or S5 functions.

## S1 — Operations

- State: A
- Function: independently choose, execute, inspect and revise substantive coding and repository actions in a bounded session or delegated child task.
- Disturbance / variety regulated: changing code, instructions, tool errors, model responses, failed host operations, rejected permissions, children and new user messages.
- Decisive decision or feedback right: the root/child model selects `rlm_exec` cells, file/shell/agent calls, retry or alternative action from observed host output.
- Decision owner: configured inference model in each first-party `AgentSession`; fixed host modules admit and enforce but do not choose the coding solution.
- Supporting / enforcement mechanisms: `AgentSession.RunTurn`, single `rlm_exec` tool, isolated kernels, durable transcript/context handles, typed host modules, scoped permissions and goal-loop support.
- Closure path: coding request/current context → model-chosen host operation → file/tool result, failure or denial → subsequent model operation or returned completion.
- Boundary reachability: built-in `Coding()` is the default shipped definition; daemon binding gives both normal roots and spawned child sessions this model/tool loop, and production modes route through the same recursive runtime.
- Why this is / is not agent-owned: substantive operations vary with inference decisions, rather than being entirely predetermined by a script.
- Evidence: [agent-loop documentation](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/docs/agent-loop.md), [coding definition](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/agentdef/coding.go), [agent session](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/daemon/agent_session.go).
- Basis: frozen production-source tracing and documented shipped operating model.
- Confidence: high for operative construction, not live model performance.
- Caveats: no model/provider endpoint or live Whip agent was run.

## S2 — Coordination

- State: A
- Function: attenuate cross-child interference over shared work and coordinate changes to delegated task boundaries while children make independent operating decisions.
- Disturbance / variety regulated: two workers attempting incompatible shared-state writes, concurrent file edits, stale progress updates, overlapping responsibilities and changed dependent task results.
- Decisive decision or feedback right: the parent model chooses which independently deciding child tackles which files/tasks, what capabilities are delegated, and how to react to returned failures or shared blackboard conflict; children can reread a rejected CAS and revise their own update.
- Decision owner: root or intermediate parent model for task partition/repartition; each child model for retry after observed conflict; daemon/SQLite owns atomic enforcement only.
- Supporting / enforcement mechanisms: `agents.spawn/submit`, one-hop durable mailbox, blackboard CAS/version and subscriptions, file mutation coordination locks, child budgets and delegated authority.
- Closure path: concurrent child work reveals overlap, stale version or result dependency → shared-state CAS rejects a stale update and mail/subscriptions expose changed state → model rereads and can change its update, ownership partition or child instructions → revised S1 action.
- Boundary reachability: `Coding()` installs `agents`, `messages`, `state` and file operations for real root and child kernels; shared-state CAS and subscriptions are wired into the daemon host. Direct-child messages and parent follow-up invoke retained production agents.
- Why this is / is not agent-owned: atomic CAS and same-path locking alone would only be deterministic support; here an actual model has task-partition authority and can use failure/version feedback to alter subsequent independent child work. This is bounded to conflicts visible through the supplied coordination surfaces, not automatic semantic merging of arbitrary shell edits.
- Evidence: [concurrency ownership](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/docs/concurrency.md), [host tools and CAS contract](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/docs/tools.md), [shared-state store](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/session/state.go), [boundary regression](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/daemon/recursive_runtime_boundaries_test.go).
- Basis: runtime source, shipped guidance and deterministic regression source inspection.
- Confidence: medium-high for an optional model-owned conflict regulation path.
- Caveats: the parent must actually choose suitable decomposition/reconciliation; the runtime does not independently make semantic cross-file conflict judgments.
- Distinct S1 units: concurrent independently model-driven retained child `AgentSession` workers, with local prompts/transcripts and side-effect capabilities.
- Inter-S1 disturbance: incompatible updates to blackboard/work files or reassignment of work after a sibling reports a result.
- Attenuating coordination relation: atomic CAS and file locks refuse stale/shared mutations, while parent model-directed task partition and follow-up steering change who works on what.
- Feedback into subsequent S1 behaviour: CAS error includes the current version; state subscriptions deliver updates; child completion/failure and custom messages wake the parent, which can steer children or change subsequent delegation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: two simultaneous operational owners and a concrete stale-write/overlapping-task disturbance are identified; CAS refusal and subsequent agent-owned repartition/retry regulate that interference. Mere mail delivery is not credited independently.

## S3 — Inside-and-now control

- State: A(P)
- Function: supervise current commitments and constraints of the active root/child organization, selecting targeted intervention while work is already in progress.
- Disturbance / variety regulated: stuck or unproductive children, resource oversubscription, wrong delegation, changing user priority and current permission exposure.
- Decisive decision or feedback right: parent model chooses from `agents.list/inspect` results whether to submit revised work, stop/delete a subtree, change follow-on delegation or narrow capability/budget; in a separate human-client mode the operator can inspect the entire agent tree and cancel/stop/revoke.
- Decision owner: the parent inference model in autonomous mode; the session's legitimate human operator in client-governed mode. Daemon actors only serialize and enforce the selected change.
- Supporting / enforcement mechanisms: current agent statuses, budget accounting, `agents.submit/stop/delete`, subtree terminalization, shared notices; inspector tree, active-turn cancellation, grant revocation and protocol controls.
- Closure path: currently observed child state/message/budget → model or human decision to steer, stop, cancel or revoke → daemon admits an authorized control → active/queued child work or effective authority changes → further state is observable.
- Boundary reachability: `Coding()` installs current-control `agents` tools and production runtime implements `list/inspect/submit/stop`; the shipped `packages/app` inspector maps live snapshot permissions to concrete stop/cancel/revoke commands. Both modes are connected to the same session store, not test-only controllers.
- Why this is / is not agent-owned: model-decided supervision is a higher current-cohort regulation loop beyond assigning one new task; the operator mode is legitimately parent-owned and separately closed. Fixed worker admission, kernel pools and quota checks alone are not the S3 owner.
- Evidence: [recursive runtime controls](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/daemon/recursive_runtime.go), [protocol client control](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/daemon/client_control.go), [agent inspector](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/packages/app/src/details/observation.tsx), [budget and grant inspector](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/packages/app/src/details/session-controls.tsx).
- Basis: source-traced model and first-party human-client ownership modes.
- Confidence: high for current-control rights and return; actual quality of prioritization unmeasured.
- Caveats: a root model can inspect/control its direct children, not bypass ancestry to arbitrary grandchild transcripts; every recursion is governed by its immediate parent. Operator intervention requires a connected authorized client.
- Whole-system current view: model sees the active direct-child set and per-child status/budgets/messages at its recursion; operator tree view shows all retained descendants and active turns with effective controls.
- Current-control decision scope: selective stop/delete, midturn steer, new queued input, child task redistribution, capability revocation and budget/permission constraints rather than only mechanically scheduled execution.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Parent model | Agent list, status, message or budget indicates changed current work | Model calls `agents.submit/stop/delete` or revises commitments; daemon changes child work | [`recursive_runtime.go`](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/daemon/recursive_runtime.go) |
| Parent (`P`) | Human operator of root session | Live tree/budget/grant view and current user judgment | Stop/cancel/revoke/submit client command is enforced and reflected in future agent status | [`observation.tsx`](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/packages/app/src/details/observation.tsx), [`client_control.go`](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/daemon/client_control.go) |

## S3* — Complementary audit

- State: —
- Function: no installed first-party complementary audit function is established for claims or actual consequences of normal coding work.
- Disturbance / variety regulated: unsupported success or correctness claims could require a reviewer; the frozen runtime provides generic tools to create one, not a material audit-specific owner/return by default.
- Decisive decision or feedback right: an ad hoc spawned child can be asked to review, but no first-party auditor-specific mode, independent inspection requirement, verdict contract or application of findings is packaged.
- Decision owner: an external user/workflow designer would have to supply an actual auditor prompt, evidence scope and follow-up policy; `Coding()` and the daemon supply only general-purpose model/task primitives.
- Supporting / enforcement mechanisms: optional `agents.spawn` with narrowed `read/shell` capabilities, `models.batch` independent completions, messages, transcripts, context handles, tests and eval verifier.
- Closure path: a user-composed reviewer might inspect files and send a message, but neither a first-party claim-relative independent judgment nor the findings-to-correction circuit is bound as a supported audit-specific runtime path.
- Why this is / is not agent-owned: multiple independent model calls and a child literally named `reviewer` are insufficient without function-specific audit ownership and complementary operational evidence access. This is a bounded no-path result, not an impossibility of composing a review externally.
- Evidence: [generic reviewer example](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/docs/tools.md), [built-in coding definition](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/agentdef/coding.go), [named reviewer test fixture](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/agentdef/definition_test.go), [evaluation workflow](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/docs/features.md).
- Basis: first-party definition, actual exposed modules, documented composition and adjacent evaluation boundaries.
- Confidence: medium for scoped negative; generic composability should not be confused with a first-party S3* constructor.
- Caveats: a user-installed audit-specific custom definition could change another deployment's assessed boundary, but it is not in the frozen standard distribution.

### Absence scope

- Surfaces inspected: built-in coding/junior definitions, recursive spawn and named-child definitions, reviewer examples, state/mailbox, project/user skills, model fan-out, host audit events, UI transcript/progress inspectors, `evals/` verifier and development-only tests.
- Plausible first-party paths checked: read-only `reviewer` child from tools documentation as optional S3*=C, `models.batch` as second opinion, named reviewer from unit fixtures, program evaluation verifier as separate operational auditor, inspector and logging as complementary observation.
- Why no material first-party path remains: the only reviewer assembly is an unconstrained example of generic user-composable delegation; no shipped auditor-specific operational claim, alternative sampling, decision contract and returned corrective authority are jointly established. Benchmark-verifier and fixture code run at a separate product-development recursion.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party future-facing external sensing, adaptation option judgment and return into operational capability was established.
- Disturbance / variety regulated: new providers, MCP tools, coding conventions and later tasks could require future adaptation, but inspected mechanisms process current configuration and tasks.
- Decisive decision or feedback right: model can inspect existing catalogued skills/tools and create present-task schedules; users can import existing skills/MCP configuration. No first-party prospective external-capability selection and closed adoption cycle was observed.
- Decision owner: operator for available skill/provider integration and user instructions; task model for current coding choices.
- Supporting / enforcement mechanisms: `schedules` module, project/standing instructions and skills discovery, MCP selection/import, persistent `me.md` notes, context compaction, model/provider choice, goals.
- Closure path: current user/project configuration is loaded or a future timed task is queued; no evidenced outside/future options → evaluation → capability-change decision → return to present S1/S3 ability.
- Why this is / is not agent-owned: remembering task facts and loading existing instructions are not the strategic prospective adaptation function.
- Evidence: [runtime environment assembly](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/docs/rlm-runtime.md), [feature and skills contract](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/docs/features.md), [memory](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/memory/memory.go), [coding definition](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/agentdef/coding.go).
- Basis: installed-module and supported-configuration review.
- Confidence: medium-high for bounded negative.
- Caveats: users may design and install specialized future-scanning agents; this is external composition, not credited first-party closure.

### Absence scope

- Surfaces inspected: scheduling, goals, memory, skills discovery/import, MCP runtime, provider/model selection, instructions, agent definitions and developer learning notes.
- Plausible first-party paths checked: scheduled future goals as S4, `me.md` as organizational learning, `models.batch` alternatives as future modeling, external MCP catalog import as proactive adaptation and custom agent definitions as self-modifying capability.
- Why no material first-party path remains: all located paths either execute delayed/present user tasks or load operator-supplied configuration; none supplies a first-party owner of prospective outside intelligence whose chosen option is adopted into changed present capability.

## S5 — Policy and identity

- State: —
- Function: no internal or formally returned parent decision loop over ultimate organizational identity, mission and governing policy is established within an installed coding session.
- Disturbance / variety regulated: operations can raise safety/permission conflicts, but the handled issues concern authorizing particular tools and resources, not adjudicating the organization's ultimate purpose.
- Decisive decision or feedback right: operator grants/denies current tool actions or revokes child authority; developers set fixed default policies; no first-party ultimate-identity dispute process and binding decision return is exposed.
- Decision owner: user/developer for current permissions, project goals and configuration, without a separately instantiated S5 governance function.
- Supporting / enforcement mechanisms: recursive permission grants, capability issuer chains, modes, `user.ask`, kernel limits, provenance, instruction hierarchy, audit trail and operator control.
- Closure path: requested side effect → permission grant/denial → operation permitted or blocked; this is tactical authorization, not identity/policy dispute → legitimate final authority → returned constitutional ruling.
- Why this is / is not agent-owned: strong deterministic boundaries and the human's ownership of a requested task do not automatically create ultimate organization-level S5.
- Evidence: [permission and authority runtime](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/docs/rlm-runtime.md), [concurrency/authority](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/docs/concurrency.md), [client policy/control](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/daemon/client_control.go), [definition/identity](https://github.com/context-labs/whip/blob/801b3a4f9412356cf36934701bce67a1fe30f6bb/internal/agentdef/definition.go).
- Basis: first-party trust boundary and control-plane source review.
- Confidence: medium-high for bounded negative.
- Caveats: a human can change the task and software settings, but this does not evidence a complete S5=P loop at the session recursion.

### Absence scope

- Surfaces inspected: agent definition identity, prompts/instructions, first-run mode and model choice, permission/revocation, user.ask, host limits, client configuration and upstream contributor policy.
- Plausible first-party paths checked: permission prompts and human revocation as parent S5, user-defined instructions as a constitution, session goal changes as identity revisions, agent-definition customization as standing policy and upstream maintainer release decisions as operational governing S5.
- Why no material first-party path remains: these govern routine capabilities, requested work or upstream product development at a different recursion. No shipped session path presents an ultimate-policy matter to a recognized authority and applies a returned authoritative governing decision.

## Distributed OSS parent arrangement

Independent upstream contributors and distinct WhipCode users do not share one private runtime tree or a project-level control loop. GitHub contribution review, CI and release-policy work belong to the separate development organization and are not imported as S3*/S4/S5 for the installed session.

## Self-hosted and non-human modes

In headless mode the recursive model and daemon can operate without an attending human, supporting `S1=A`, `S2=A` and current-control `S3=A`. When a first-party UI client is connected, the legitimate session operator can inspect the actual agent cohort, cancel work, stop descendants, steer and revoke grants: this establishes the distinct `S3=P` mode encoded in `A(P)`. An external model provider serves inference rather than an independent Whip governance entity.

## Recursion

Root and children use one retained `AgentSession` abstraction; each child may itself spawn children within the ancestry limit. Parent control addresses direct children, whose own S3 can control their children. Shared root scope, budgets, coordinated file mutations and durable mailbox define the organizational boundary; multiple installations and product-development infrastructure sit outside it.

## Variety and escalation

Tool and permission failures return to the operating model; stale shared-state CAS and subscribed change messages can induce reinspection/repartition at S2; child state, completion, failure and budget reports allow targeted autonomous or human current control at S3. Provider quota and kernel/capability enforcement remain deterministic support. There is no evidenced mandatory independent audit findings gate, prospective S4 adaptation loop or identity-level S5 escalation.

## Evidence gaps

- Source was checked out at exact frozen SHA `801b3a4f9412356cf36934701bce67a1fe30f6bb`; source-code analysis, shipped documentation and existing deterministic test assertions inform the mapping. No live model/agent task was run.
- The local environment and accessible development host did not expose the required Go 1.27 executable, so native Go unit tests at this frozen SHA were **not executed**. Citing bundled regression tests is source inspection, not a claim of passing them.
- The positive S2 claim concerns exposed optional model-controlled task decomposition plus version/conflict feedback, not automatic conflict-free completion of arbitrarily parallel shell commands.
- S3 model control is bounded to direct descendants at each recursion; human inspector displays the broader tree. Cross-recursion control is not inferred from unrestricted global transcript access.
- A user may assemble their own independent audit actor with generic spawn tools, but neither a dedicated first-party review definition nor an operational claim-to-complementary-evidence-to-correction circuit was found in the default shipped runtime. The `evals/` verifier is explicitly outside the assessed operating boundary.
