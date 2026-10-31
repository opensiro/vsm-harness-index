---
harness_id: suga
project_name: Suga
repository: https://github.com/inhere/suga
review_ref: 88916d5d23e974f7c02c9dd37f6d02f05b681a31
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Suga

## Review boundary

- System in focus: The current first-party Suga personal-agent product and its supported session/workgroup organization at the pinned revision.
- Purpose and identity: Carry out local coding/investigation work through a persistent model/tool conversation with optional read-only subagents and background tasks.
- Relevant environment: User workspaces, OS processes, inference endpoints, local peer chats, optional MCP/skills/memory backends and the user operating the workgroup.
- Standard-distribution boundary: Current CLI chat/run, ACP and the concrete internal/wiring → personal → agentcore composition; the product's optional local peer-chat protocol is considered as a coordination constructor. Supported modes are distinguished rather than assumed to form one simultaneously deployed organization.
- Credited operating / distribution surfaces: Current runtime/wiring, native operational/subagent/task tools, task feedback, chat task supervision, and the implemented session-message hop gate.
- Adjacent first-party surfaces excluded from ownership: Archived Agent OS/Host/Web control plane, development/dogfood Gofer issue/plan organization, config/agents role sketches not instantiated by the current explore/research tool, evaluation/benchmark/CI and test fixtures. External Gofer job/worker orchestration is outside Suga.
- First-party operating / deployment modes considered: CLI run/chat, ACP and SDK-compatible wiring; synchronous/background read-only agents; the operator's local task supervision; optional peer messaging among same-SUGA_HOME chats. No Gofer features are imported.
- Recursion level: Product-supported session/workgroup level. S3 is explicitly limited to a principal session and its owned background operational commitments; no whole-machine or OSS-organization S3 claim is made. The optional S2 constructor concerns peer workcells that are explicitly connected through the local messaging mode.
- Reviewed revision: `88916d5d23e974f7c02c9dd37f6d02f05b681a31`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Go product has a reusable agentcore kernel below application wiring, personal session/storage logic, chat/CLI and ACP. The kernel builds prompts/context, calls providers, executes tool requests and persists state/transcript. Current wiring adds approvals, workspace tools, MCP/skills, plans, memory, output offloading and session notices. The agent tool starts isolated read-only explore/research actors; a background actor is a session-owned task. The task manager records state/output, delivers notices and exposes list/output/wait/kill to the parent. Chat exposes the same task state and cancellation to the user. Soft token/cost/deadline limits are configured separately from an actor's discretionary intervention.

Local session messaging lists running chats and carries sender identity, deduplicated message IDs and automatic-reply hop depth. A receiving chat holds a message at the configured hop threshold until a person's next input, rather than automatically starting another reply. Single-session gates and cross-process locks separately prevent duplicate writers of one session.

The run delivery pipeline can execute a caller-specified verification command, inject failures for repair, apply deterministic nudge rules and validate output JSON. These are ordinary operational checks. Idle consolidation starts a new summarized segment; long-term memory has provenance/confirmation controls. The documentation explicitly archives the older control plane and assigns wider jobs/workers to external Gofer. [Kernel][R1], [wiring][R2], [agents][R3], [tasks][R5], [current scope][R20], [documentation status][R21].

## Operational model

A model-backed principal owns task-specific tool choices; read-only children own their exploration/research work and report back. The parent may review the full set of its current background commitments and choose to retain, wait for or terminate them. The user has a separate supported supervisory path over that same task set. This is a bounded session/workgroup control claim, not a claim that a principal controls unrelated peer chats.

The local peer-message protocol is an actual S2-specific anti-oscillation constructor: its hop/hold policy is developer/operator-selected and enforced by runtime. No autonomous actor selecting or revising that coordination policy is supplied, so its published state is C. Ordinary delegation, task sequencing, readonly policy and one-session writer locks are not separate S2 evidence.

## S1 — Operations

- State: A
- Function: Produce coding/investigation outcomes through the model/tool loop, optionally using read-only research/exploration actors.
- Disturbance / variety regulated: User requests, file and command results, tool refusals, provider errors and evolving task observations.
- Decisive decision or feedback right: Select next tools, delegate exploration, interpret observations and decide the answer or next work.
- Decision owner: The configured model-backed principal and its operational child actors.
- Supporting / enforcement mechanisms: Provider adapters, persistence, workspace/approval guards, transcript/context projection and limits.
- Closure path: Model request → chosen tool/agent action → persisted results or child report → next model request/final answer.
- Boundary reachability: Current wiring instantiates the first-party kernel and tool set for CLI/ACP; enabled agent tooling builds real read-only child runners rather than borrowing an uninstantiated framework.
- Why this is / is not agent-owned: Removing the model actors leaves storage, permissions and transport but no task-specific discretionary choices.
- Evidence: [Kernel][R1], [current wiring][R2], [child construction][R3], [agent tool][R4].
- Basis: structural.
- Confidence: high.
- Caveats: No live inference or agent E2E execution was run. Operational quality and benchmark results are not inferred.

## S2 — Coordination

- State: C
- Function: The local peer-chat protocol attenuates repeated automatic replies between independent workcells.
- Disturbance / variety regulated: One session's peer reply can wake another, whose response wakes the first again without new human work.
- Decisive decision or feedback right: Choose the anti-reply hop policy and when a held exchange may resume.
- Decision owner: The developer/operator supplies max_hops and the continuation policy; the runtime counts/holds. An autonomous coordination-policy actor is not supplied.
- Supporting / enforcement mechanisms: Sender attribution, TurnHops + 1, configured receiving threshold, held-message queue, message IDs/status and per-turn send cap.
- Closure path: Peer reply advances hop depth → receiver reaches max_hops → no new turn is started → held state/status is observable and the message enters only a later human-started turn.
- Boundary reachability: The shipped session_message tool is available by default outside disabled/Gofer-job modes, and the real local chat socket delivery path applies the hold rule. This is a first-party anti-oscillation path, not a hypothetical custom mailbox.
- Why this is / is not agent-owned: The model may choose a message, but the decisive coordination threshold/hold rule remains configured; C records the S2-specific construction/control surface rather than autonomous ownership.
- Evidence: [Native peer tool][R9], [host message construction][R10], [hop context][R11], [receiver hold][R12], [configuration][R13].
- Basis: structural.
- Confidence: high.
- Caveats: Older peer versions may not support hop gating; the tool reports that limitation. This path does not provide shared-file reservations or coordination for arbitrary external runtimes.

- Distinct S1 units: Two or more independently running same-user Suga chat workcells.
- Inter-S1 disturbance: Reciprocal automated responses repeatedly wake peer sessions.
- Attenuating coordination relation: Hop-depth accounting with a configured hold-at-threshold rule and explicitly delayed human continuation.
- Feedback into subsequent S1 behaviour: The threshold delivery starts no turn, is retained for the next person's turn, and has message-status feedback; later operation sees the held context instead of an unbounded automatic reply.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The protocol explicitly identifies and breaks automatic peer-reply chains. Sender/addressing transport and session locks alone are not the witness.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate the principal workgroup's current background operational commitments, including independent subagent tasks.
- Disturbance / variety regulated: Subagents, long commands or watches may remain running, fail, return unhelpful work or consume the current workgroup's time/resources after priorities change.
- Decisive decision or feedback right: Review the current owned-task set, read progress/output, choose which work continues or is killed, and revise subsequent operational action.
- Decision owner: Base mode: the principal model-backed agent. Parent mode: the local user supervising that same session/task organization through chat.
- Supporting / enforcement mechanisms: Session-scoped task manager, task snapshots/output/termination, agent run metadata, task notices, cancellation/process-tree handling and configured budget/time ceilings.
- Closure path: Task list/output/notice → principal or operator selects current intervention → task kill/cancellation and resulting snapshot/notice → subsequent model work proceeds with revised commitments.
- Boundary reachability: CLI/run/chat/ACP wiring installs native task controls when the first-party task manager is present; agent background runs use that manager. Chat's :tasks/-k commands directly expose the same session task state and termination path to the user.
- Why this is / is not agent-owned: The model chooses whether to retain or terminate current owned work; the manager only executes the choice. Configured hard limits do not own those discretionary decisions. Human supervision is separately evidenced, rather than inferred from write approval.
- Evidence: [Tool current-view/intervention][R5], [manager List/Kill][R6], [model feedback][R7], [chat view/cancellation][R8], [task wiring][R23], [actor construction][R3].
- Basis: structural.
- Confidence: medium.
- Caveats: Scope is one principal session's owned background workgroup. This does not establish a regulator over all independent chats or external Gofer jobs; a lone foreground run need not exercise this mode.

- Whole-system current view: task list returns all tasks of the principal session with kind, summary, running/end state, duration and output/progress; output/wait and task notices supply details. Chat :tasks/-a exposes that same bounded workgroup to the user.
- Current-control decision scope: Current commitments and resource use of owned background subagents, commands and watches; task kill changes what continues, while later launches and instructions can revise the work mix.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Principal model-backed agent | Current task state/output indicates work should wait, continue or stop | Agent uses task list/output/wait/kill; manager changes running commitments and returns state/feedback | [Task tool][R5], [manager][R6], [notices][R7] |
| Parent (`P`) | User operating the local session/workgroup | User reviews running/recent task snapshots and chooses an intervention | :tasks -k calls the same session manager Kill path; changed task state appears in later operation | [Chat commands][R8], [manager][R6] |

## S3* — Complementary audit

- State: —
- Function: No first-party audit-specific independent judgment with corrective current-control return is supplied.
- Disturbance / variety regulated: Incorrect completion claims, missed tests, malformed output or defects in produced artifacts.
- Decisive decision or feedback right: No installed independent audit owner adjudicates an operational claim through a complementary channel.
- Decision owner: The producer and configured delivery checks handle ordinary validation; explore/research children are general operational helpers.
- Supporting / enforcement mechanisms: Caller-selected --verify command, fixed nudge rules, JSON-schema checks, traces, raw transcript access and read-only child tools.
- Closure path: Failed delivery checks re-enter the same producing session. There is no supplied independent audit judgment/authority loop.
- Why this is / is not agent-owned: Deterministic schema/nudge/verification and generic child exploration are not complementary S3*. The config/agents reviewer sketch is not one of the current tool's instantiated actor types.
- Evidence: [Delivery verification][R14], [nudge][R15], [output contract][R16], [actual child types][R3], [agent interface][R4], [current/archive boundary][R21].
- Basis: structural.
- Confidence: high.
- Caveats: A caller can compose an independent reviewer around direct evidence, but that application is not supplied by the reviewed current product.

### Absence scope

- Surfaces inspected: Current kernel/wiring and personal session/task/budget/trace/memory/context code; CLI verification/output contract, chat nudge/idle/supervision; native agent/task/session-message tools; current documentation and archived/config/evaluation boundary
- Plausible first-party paths checked: Checked verification-command feedback, nudge evidence, JSON judge terminology, trace/transcript inspection, explore/research actors, config role sketches and offline evals for independent audit ownership and corrective control.
- Why no material first-party path remains: The shipped checks are ordinary delivery validation and diagnostics. Generic readonly helpers supply no audit-specific verdict/authority contract, and archived/dogfood/eval actors are outside current distribution ownership.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: External research results, user feedback and long-session context pressure are operational inputs rather than a supplied future-capability model.
- Decisive decision or feedback right: No intelligence actor develops adaptation alternatives and closes their return into present capability/current control.
- Decision owner: The principal performs requested research and writes permitted memory; user/maintainer selects configuration and releases.
- Supporting / enforcement mechanisms: Web research child, feedback/reference memory kinds, summaries, handoff/context segments, idle consolidation and provider settings.
- Closure path: Stored memory and compressed context enter later requests; no prospective adaptation-option-to-capability decision path is supplied.
- Why this is / is not agent-owned: Remembering corrections, summarizing history or doing a current research task does not by itself establish S4. No function-specific parent adaptation loop is evidenced.
- Evidence: [Research construction][R3], [memory controls][R19], [idle consolidation][R17], [segment break][R18], [product scope][R20].
- Basis: structural.
- Confidence: high.
- Caveats: Developer optimization/evaluation and archived learning/self-loop documents are not runtime product owners.

### Absence scope

- Surfaces inspected: Current kernel/wiring and personal session/task/budget/trace/memory/context code; CLI verification/output contract, chat nudge/idle/supervision; native agent/task/session-message tools; current documentation and archived/config/evaluation boundary
- Plausible first-party paths checked: Inspected web/research actors, feedback/user/reference/project memory, memory writes/confirmation, idle consolidation, handoff and evaluation/history notes for external/future distinctions, adaptation options and current-capability return.
- Why no material first-party path remains: The current paths provide task research, retention and context maintenance. No supplied outside-and-then adaptation judgment and returned capability change remains.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy adjudication-and-return loop is supplied.
- Disturbance / variety regulated: Write permissions, external-origin taint, protected paths, agent instructions and memory confirmation.
- Decisive decision or feedback right: No identity-level matter is specifically routed to legitimate ultimate authority and returned as a governing policy decision.
- Decision owner: User/developer supplies prompt, approval and tool/memory rules; agents own bounded local action choices.
- Supporting / enforcement mechanisms: Read-only registration, strongest approval rules, dangerous-action confirmation, taint guards, rules loading and session state.
- Closure path: Allow/deny/confirm outcomes govern actions or memory writes, not ultimate identity or S3–S4 tension resolution.
- Why this is / is not agent-owned: Static rules, user approval and a memory kind called user/feedback are not S5. The narrower user current-task supervision supports S3 only.
- Evidence: [Wiring and approval assembly][R2], [child policy snapshot][R3], [memory confirmation][R19], [documented permissions][R20].
- Basis: structural.
- Confidence: high.
- Caveats: The public project/development organization and external Gofer governance are outside this product-level assessment.

### Absence scope

- Surfaces inspected: Current kernel/wiring and personal session/task/budget/trace/memory/context code; CLI verification/output contract, chat nudge/idle/supervision; native agent/task/session-message tools; current documentation and archived/config/evaluation boundary
- Plausible first-party paths checked: Checked prompt/rule loading, chat/ACP approvals, memory confirmation, protected paths, child policy inheritance, local supervision and current/archive scope for an identity-level issue, legitimate decision owner and authoritative return.
- Why no material first-party path remains: All supported paths are pre-authored constraints, ordinary approval or current-work supervision. No identity/ultimate-policy feedback loop is shipped.

## Distributed OSS parent arrangement

Public MIT development and the repository's Gofer-based issue/plan practice are adjacent to the installed product. The S3 parent mode is explicitly the user of a local session/workgroup. It is not project/organization-level parent governance and does not justify S4/S5 parent notation.

## Self-hosted and non-human modes

CLI chat/run and ACP wire the same core with mode-specific approval/notification behavior. Native background-task supervision supports alternative agent-owned and user-owned S3 modes within one workgroup. Optional local chat coordination uses a configured hop policy; Methodology 0.3.x does not publish a parent modifier for S2. No mandatory human contribution to ordinary S1 choices is inferred.

## Recursion

Child sessions have independent contexts and read-only tool discretion, but no complete child metasystem is evidenced. Per-workgroup task regulation is not promoted to an installation-wide hierarchy; local peer-message construction does not imply that every same-SUGA_HOME chat belongs to one governed mission.

## Variety and escalation

Tool schemas, permission rules, budgets and output offloading attenuate presented variety. Research/tools and multiple child contexts expand operational repertoire. Task notices return active-work distinctions to the principal, and the reply-hop gate interrupts a concrete peer-message oscillation. A held peer message or warning is a status/control mechanism, not automatically an algedonic channel. Current user task control and ordinary safety confirmations remain distinct from ultimate policy.

## Evidence gaps

Pinned static-source assessment; no provider/LLM-agent E2E or upstream benchmark was executed. Current tests were inspected as corroboration, not as autonomous actors. S2 is a first-party configured constructor with legacy-peer limitations. S3 is confined to a principal's owned background workgroup, with separately reconstructed local user supervision; it does not claim authority over unrelated peer chats. No unresolved active audit/adaptation/identity path was found in the declared current distribution; archived and external systems are excluded explicitly.

[R1]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/pkg/agentcore/runtime.go
[R2]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/wiring/runtime.go
[R3]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/wiring/subagent.go
[R4]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/pkg/agentcore/tools/native/agent.go
[R5]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/pkg/agentcore/tools/native/task.go
[R6]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/pkg/agentcore/tasks/tasks.go
[R7]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/personal/tasks.go
[R8]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/chat/chat_commands.go
[R9]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/pkg/agentcore/tools/native/session_message.go
[R10]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/wiring/session_message.go
[R11]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/personal/hops.go
[R12]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/chat/session_message.go
[R13]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/config/sessionmessage.go
[R14]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/cli/verify.go
[R15]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/personal/nudge.go
[R16]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/personal/outschema/contract.go
[R17]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/chat/chat_idle.go
[R18]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/personal/compact.go
[R19]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/wiring/memory_runtime.go
[R20]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/README.md
[R21]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/docs/README.md
[R22]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/personal/gate.go
[R23]: https://github.com/inhere/suga/blob/88916d5d23e974f7c02c9dd37f6d02f05b681a31/internal/wiring/tasks.go
