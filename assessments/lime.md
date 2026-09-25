---
harness_id: lime
project_name: Lime
repository: https://github.com/limecloud/lime
review_ref: 3823e9092d4106c877ae08a1d19d593b647cf27d
reviewed_at: 2026-09-25
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-25
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Lime

## Review boundary

- System in focus: one first-party Lime desktop/App Server deployment at pinned revision `3823e9092d4106c877ae08a1d19d593b647cf27d`, including the current Rust agent runtime, canonical Thread/Turn/Item state, tool runtime, durable AgentControl graph/mailboxes, child-session execution, permissions/approvals, recovery and supported desktop/TUI control surfaces.
- Purpose and identity: execute user objectives through a persistent model/tool agent loop that can operate files, terminal processes, MCP/Skills and other tools, and can decompose current work into durable child-agent sessions.
- Relevant environment: user/operator requests, workspace/filesystem/process state, configured model providers, MCP/tool endpoints, local Skills and other external services reached through tools.
- Standard-distribution boundary: first-party runtime and shipped control surfaces. Internal research/roadmap/exec-plan documents, benchmark harnesses and repository-development verification workflows are adjacent unless frozen production code directly wires them into the assessed runtime.
- Credited operating / distribution surfaces: current provider turn execution, session/thread persistence and restore, AgentControl `spawn_agent`, `send_message`, `followup_task`, `wait_agent`, `interrupt_agent`, `list_agents`, root-scoped child execution limiting/residency, ordinary permissions/approval gates and runtime recovery.
- Adjacent first-party surfaces excluded from ownership: repository-development qcloop/verifier plans, DeepSWE benchmark verification, UI-only/retired team-selection metadata and generic customization from arbitrary prompts when no function-specific runtime closure is supplied.
- First-party operating / deployment modes considered: ordinary single-agent Thread execution and the shipped durable multi-agent root-tree mode in which the root model invokes AgentControl tools to create and supervise child sessions.
- Recursion level: one Lime root-agent tree. The root and each spawned durable child session/thread are S1 operational units. S2 and S3 are assessed at the root-tree recursion rather than inferred from names such as workflow, team or supervisor.
- Reviewed revision: `3823e9092d4106c877ae08a1d19d593b647cf27d`.
- Observation date: 2026-09-25.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Lime's current provider turn executor owns a repeated sampling/tool-feedback cycle. A provider response is materialized into text/reasoning/tool calls, first-party tool execution runs the requested effects, normalized tool results are appended to the same transcript, and the loop samples again. Canonical Thread/Turn/Item and durable session state preserve that operational history across continuation/recovery.

The multi-agent path is also production-wired rather than only a UI concept. `AgentControlGateway` exposes six model-visible controls. `spawn_agent` creates a new durable child thread/session, assigns a durable graph identity and initial mailbox task, commits the spawn and wakes the child through the normal pending-session runtime. Children can later receive queued messages or follow-up turns. `wait_agent` returns child mailbox/result activity and state; `list_agents` returns the current open durable tree with each agent's status and last task; `interrupt_agent` changes a child's active operation.

At this root-tree recursion, child S1s compete for a bounded shared execution resource. `AgentExecutionLimiter` explicitly limits concurrently running child turns per durable root tree: with default total capacity four, the root leaves three child execution slots. Reservation/claim is atomic, excess admission fails, and slots are released at terminal completion. This is a concrete inter-S1 contention/attenuation/feedback path, but the capacity decision is a deterministic configured rule rather than autonomous coordination discretion, so S2 is `C` rather than `A`.

S3 is stronger. The root model itself has a first-party whole-tree current-control surface: it can list every open agent with current status/last task, receive terminal and mailbox feedback, allocate new tasks by spawning children, steer existing children with messages/follow-up work, wait for results and interrupt an active child. The model chooses these interventions from current tree feedback; deterministic graph/mailbox/limiter machinery transports and enforces those choices. Removing the root model leaves the tools but removes the discretionary allocation/intervention judgment, supporting `S3=A`.

No equally strong S3*, S4 or S5 closure was found. Generic child agents can be prompted to review work, and the repository contains verifier/team-profile and development-evaluation material, but the standard AgentControl constructor exposes generic children rather than a function-specific complementary-audit path with an established independent access boundary and corrective return. Skills/provider/model configuration and task research extend current operations but do not establish an external-and-prospective organizational adaptation loop. Permissions, prompts, profiles and operator approvals do not establish identity/ultimate-policy closure.

Primary evidence:

- [`lime-rs/crates/agent-runtime/src/provider_turn.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/agent-runtime/src/provider_turn.rs) — repeated provider sampling, tool execution, tool-result reinsertion and next-step feedback.
- [`lime-rs/crates/tool-runtime/src/agent_control.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/tool-runtime/src/agent_control.rs) — model-visible durable multi-agent control contract: spawn, message, follow-up, wait, interrupt and list.
- [`lime-rs/crates/app-server/src/runtime/agent_control_gateway.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/app-server/src/runtime/agent_control_gateway.rs) — durable child creation, graph identity, mailbox delivery, normal runtime wake-up, tree listing/current status and recovery.
- [`lime-rs/crates/app-server/src/runtime/agent_control_gateway/wait.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/app-server/src/runtime/agent_control_gateway/wait.rs) — child-result/mailbox/state feedback returned to the supervising agent.
- [`lime-rs/crates/app-server/src/runtime/agent_execution.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/app-server/src/runtime/agent_execution.rs) — root-scoped bounded child execution slots and atomic reserve/claim/release.
- [`src/components/agent/chat/utils/teamPresets.ts`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/src/components/agent/chat/utils/teamPresets.ts) — reviewer/verifier role metadata inspected but not promoted to S3* without a qualifying production audit closure.
- [`README.md`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/README.md) — shipped product boundary and Thread/Turn/Item, tools, Skills, restore and multi-agent claims, used only where corroborated by frozen implementation.

## Operational model

The root Thread is an autonomous operational agent and, when it spawns children, also becomes the current-control owner for that durable root tree. Each child is a separately persisted agent session executing the same model/tool feedback machinery. Runtime-owned graph, mailbox, admission and residency mechanisms maintain bounded, recoverable concurrency. The root agent receives child states/results and decides current decomposition, steering and intervention.

## S1 — Operations

- State: A
- Function: transform an objective into tool-mediated environmental outcomes through repeated model reasoning/sampling, tool action and observation feedback.
- Disturbance / variety regulated: changing task requirements, workspace/file/process state, tool results and failures, provider output, permissions, user steering and durable mailbox input.
- Decisive decision or feedback right: choose the next substantive action/tool and revise subsequent work from returned tool/environment evidence.
- Decision owner: the active Lime model agent in each root or child session.
- Supporting / enforcement mechanisms: provider adapter, current provider turn loop, tool runtime, Thread/Turn/Item projection, session loop, permissions/approvals and persistence/recovery.
- Closure path: objective/context → provider/model chooses tool or output → tool runtime applies action → normalized result is appended to the same transcript → subsequent sampling observes the result and chooses the next action → task/environment state changes.
- Boundary reachability: standard first-party runtime path used by ordinary root and spawned child sessions.
- Why this is / is not agent-owned: deterministic tooling executes and bounds actions, but removing the model removes the substantive next-action judgment while leaving only enforcement machinery.
- Evidence: [`provider_turn.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/agent-runtime/src/provider_turn.rs); [`README.md`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/README.md).
- Basis: explicit + structural
- Confidence: high
- Caveats: model inference can be external, but Lime owns the persistent first-party action/feedback loop and applies model decisions to its environment.

## S2 — Coordination

- State: C
- Function: attenuate contention among distinct child S1 operations for bounded concurrent execution capacity within one durable root-agent tree.
- Disturbance / variety regulated: multiple child S1s can concurrently demand execution beyond the root-tree child capacity, creating resource contention and unbounded parallel admission.
- Decisive decision or feedback right: admit or reject a child turn against root-scoped capacity and release/reuse that capacity as children terminate.
- Decision owner: no autonomous S2 actor owns discretionary coordination; the standard path deterministically enforces the configured root-scoped limit.
- Supporting / enforcement mechanisms: `AgentExecutionLimiter` reservations/claims/guards, child residency handling, durable root/thread identity and AgentControl error return.
- Closure path: distinct child sessions request execution → limiter observes shared root-scoped active/pending occupancy → atomic reservation admits up to the bound or returns `AgentLimitReached` → the failed/successful result returns through the AgentControl tool/runtime → the root/child execution pattern changes; completed work releases capacity for later S1 execution.
- Boundary reachability: the S2-specific admission/limiting relation is directly on the shipped AgentControl child-execution path: model-visible spawn/follow-up requests reserve or claim root-scoped child slots in App Server before child turns run, and admission failure returns through the ordinary tool/error path; no downstream composition is required to make the contention regulator operative.
- Distinct S1 units: each spawned child receives its own durable thread/session and is woken through the normal agent session runtime, so it is a complete operational loop rather than a one-shot model call.
- Inter-S1 disturbance: child sessions belonging to the same root compete for the finite child execution slots.
- Attenuating coordination relation: first-party root-scoped atomic reserve/claim/release prevents excess simultaneous child execution.
- Feedback into subsequent S1 behaviour: admission failure is returned as `AgentLimitReached`; terminal/released slots permit later child/follow-up work. Root model behavior can therefore change after the coordination result.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation specifically regulates an evidenced interaction disturbance between multiple S1 operations — contention for the same bounded execution capacity — rather than merely carrying messages or ordering arbitrary work.
- Why this is / is not agent-owned: the function-specific path is first-party and complete enough to establish S2, but the decisive capacity rule is deterministic/configured. A developer would need to compose an autonomous coordinator/authority to own that discretion, so publication state is `C`.
- Evidence: [`agent_execution.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/app-server/src/runtime/agent_execution.rs); [`agent_control_gateway.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/app-server/src/runtime/agent_control_gateway.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: mailbox messaging and delegation are not the basis of the S2 result; the bounded shared-capacity conflict is.

## S3 — Inside-and-now control

- State: A
- Function: supervise the current root-agent organization by observing the active durable agent tree and changing current task allocation, child commitments and interventions.
- Disturbance / variety regulated: changing child progress/state, completed/failed work, queued mailbox activity, need for additional parallel capacity, misdirected/obsolete child work and current decomposition of the root objective.
- Decisive decision or feedback right: decide when/what child to spawn, which existing child receives follow-up/current steering, when to wait for results, and when to interrupt a child.
- Decision owner: the root model agent through model-visible AgentControl tools.
- Supporting / enforcement mechanisms: durable graph/identity store, mailboxes, child session lifecycle, result/state projections, execution limiter, recovery and tool gateway.
- Closure path: root agent lists/observes the open tree and/or receives child result/mailbox state → model judges current decomposition/progress → calls spawn/message/follow-up/wait/interrupt → runtime applies the decision to child sessions → child commitments/current operation change → status/result feedback becomes available to the root again.
- Boundary reachability: standard model-visible tools are injected into the ordinary first-party runtime and are backed by the App Server's durable graph/session implementation.
- Whole-system current view: `list_agents` enumerates the current open durable root tree and returns each agent's status and last task message; `wait_agent` returns current child activity/results and state facts.
- Current-control decision scope: root can allocate new child commitments, steer existing work, trigger follow-up turns and interrupt active child turns across its current organization.
- Why this is / is not agent-owned: graph/mailbox/session machinery enforces decisions, but the model chooses whether and how to allocate/steer/intervene from current whole-tree feedback. Removing the root model leaves control primitives without the discretionary S3 judgment.
- Evidence: [`agent_control.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/tool-runtime/src/agent_control.rs); [`agent_control_gateway.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/app-server/src/runtime/agent_control_gateway.rs); [`wait.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/app-server/src/runtime/agent_control_gateway/wait.rs).
- Basis: explicit + structural
- Confidence: high
- Caveats: S3 is credited at the root-tree recursion, not at an unrelated deployment-wide aggregation across independent user roots.

## S3* — Complementary audit

- State: —
- Function: no material first-party complementary-audit path is established at the assessed root-tree recursion.
- Disturbance / variety regulated: not established as an independent discrepancy between ordinary current-control reporting and operational reality.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S3*.
- Supporting / enforcement mechanisms: arbitrary child agents can inspect workspace state; UI metadata includes verifier/reviewer profiles; repository development/benchmark surfaces contain verification machinery. These do not by themselves establish S3*.
- Closure path: not applicable; no reviewed standard runtime path establishes complementary access → materially independent audit judgment → finding returned into root S3/control.
- Claim being audited: no function-specific first-party audit claim is wired into standard root-tree operation.
- Ordinary reporting path: child status, last task, mailbox results and canonical Thread/Turn/Item events flow through the ordinary AgentControl/runtime substrate.
- Complementary access path: generic children can be asked to review and can inherit/fork context, but `spawn_agent` exposes a generic task/message/model constructor rather than a function-specific independent audit path; generic prompt expressiveness does not meet Methodology `C`.
- Independence boundary: no standard audit-specific actor, sensor boundary or independently owned verifier closure was established.
- Who acts on findings: a root or user could act on an arbitrary review response, but that is a possible downstream composition rather than a first-party S3* closure.
- Why this is / is not agent-owned: no S3* function is established before ownership classification.
- Evidence: [`agent_control.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/tool-runtime/src/agent_control.rs); [`teamPresets.ts`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/src/components/agent/chat/utils/teamPresets.ts).
- Basis: explicit + structural absence review
- Confidence: medium-high
- Caveats: downstream task design can construct reviewer children; that does not make the frozen standard distribution S3* by default or meet the narrow constructor threshold.

### Absence scope

- Surfaces inspected: AgentControl child construction, mailbox/result feedback, Thread/Turn/Item projections, verifier/reviewer team metadata, provider model-verification events, development qcloop/verifier material and DeepSWE benchmark verification surfaces.
- Plausible first-party paths checked: dedicated reviewer child, independent workspace inspection, provider verification metadata and offline harness/evaluation verification.
- Why no material first-party path remains: production AgentControl is generic and does not intentionally expose an S3*-specific independence/judgment/return path; adjacent development/evaluation surfaces are outside the assessed operating boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective organizational adaptation loop is established at the assessed recursion.
- Disturbance / variety regulated: not established as future/external change requiring adaptation of the root-agent organization's capability or structure.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S4.
- Supporting / enforcement mechanisms: web/MCP/tool research, provider/model selection, Skills discovery/install/configuration, reusable procedures and persistent task context can extend operation but do not by themselves establish S4.
- Closure path: not applicable; no standard first-party path closes external/prospective sensing → generation of organizational adaptation options → S4 judgment → returned capability/current-control change.
- Why this is / is not agent-owned: model research and Skill/tool use are available to S1 tasks; current task learning or user-driven capability configuration is not automatically organizational adaptation.
- Evidence: [`README.md`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/README.md); [`lime-rs/crates/app-server/src/runtime/skills.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/app-server/src/runtime/skills.rs).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: Lime is highly extensible; this result distinguishes capability extensibility from an autonomous outside-and-then adaptation conversation.

### Absence scope

- Surfaces inspected: Skills runtime/configuration, remote/local skill facilities, MCP/tool discovery, provider/model routing, persistent context and multi-agent task decomposition.
- Plausible first-party paths checked: agent-discovered capability use, Skill creation/install/reload, research/tool use and provider/model changes.
- Why no material first-party path remains: inspected mechanisms support current operation or operator-driven capability configuration; no first-party organization-level prospective adaptation loop with selected return into current capability/control was established.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy decision loop is established at the assessed recursion.
- Disturbance / variety regulated: not established as an identity/constitutional/ultimate-policy matter.
- Decisive decision or feedback right: not established.
- Decision owner: none established for S5.
- Supporting / enforcement mechanisms: system prompts, model/provider configuration, permissions/approval gates, tool policies, Skills/profile metadata and user constraints govern operational behavior but do not establish ultimate-policy authority.
- Closure path: not applicable; no reviewed path shows an identity/ultimate-policy issue reaching legitimate ultimate authority and returning as authoritative policy governing later root-tree operation.
- Why this is / is not agent-owned: root and child models act within configured operational constraints; they are not shown owning the legitimacy/identity of those constraints.
- Evidence: [`README.md`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/README.md); [`agent_control.rs`](https://github.com/limecloud/lime/blob/3823e9092d4106c877ae08a1d19d593b647cf27d/lime-rs/crates/tool-runtime/src/agent_control.rs).
- Basis: explicit + structural absence review
- Confidence: high
- Caveats: user approval over an operational action is not S5 merely because the user has final say over that action.

### Absence scope

- Surfaces inspected: permission/approval gates, system/task prompts, model/provider configuration, team/profile metadata, Skills, AgentControl and root/child authority boundaries.
- Plausible first-party paths checked: user approval, root supervision, policy/configuration changes and role/profile selection.
- Why no material first-party path remains: these paths regulate current execution or configuration, not identity/ultimate-policy closure at the assessed organization boundary.

## Distributed OSS parent arrangement

Repository maintainers and contributor workflows were not used to infer runtime parent governance. The system in focus is one operating Lime root-agent tree; upstream product/release governance is adjacent unless a first-party runtime return loop makes it part of that organization's S3/S4/S5 closure.

## Self-hosted and non-human modes

Lime exposes operator approvals, permissions and runtime controls, but a human's ability to approve an action, configure a provider or stop work does not by itself establish a qualifying parent-governed S3/S4/S5 mode. The positive S3 result is instead the autonomous root-agent current-control mode over its spawned child organization.

## Recursion

At the selected recursion, the root model and spawned durable child sessions are operational S1 units. The deterministic root-scoped limiter coordinates a real shared-capacity disturbance (`S2=C`), while the root model has whole-tree visibility and current intervention rights (`S3=A`). A child contains its own internal model/tool S1 loop; its local turn/tool machinery is not independently promoted to the root-tree metasystem.

## Variety and escalation

Operational variety is amplified by model reasoning, tool access, provider choice and parallel child agents. Lime attenuates it through permissions/approvals, bounded provider turns, durable session state, child execution limits, canonical graph identities, mailbox delivery and interrupt/recovery controls. Child results and states return to the root model, which can reallocate or terminate current work. Human approvals handle operational exceptions but are not treated as S5.

## Evidence gaps

- No fresh live Lime run was executed inside this assessment environment; positive findings rely on pinned primary source and tests/docs at the frozen revision.
- S2 is narrowly credited to root-scoped shared execution-capacity contention, not to delegation/mailboxes by themselves.
- S3 is credited at one durable root-agent-tree recursion; the assessment does not claim deployment-wide S3 across unrelated roots/users.
- Generic reviewer children and verifier labels were inspected but do not meet the Methodology's narrow S3* constructor threshold without a function-specific independent audit path.
- Skills, MCP, model routing and persistent context were inspected for S4 but remain current-operation/extensibility surfaces rather than a demonstrated prospective organizational adaptation loop.
- No identity/ultimate-policy closure was found for S5.
