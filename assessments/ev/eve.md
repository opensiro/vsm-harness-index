---
harness_id: eve
project_name: Eve
repository: https://github.com/vercel/eve
review_ref: d004e6d47e9d25d0380c24b5a47b65a18f8b2784
reviewed_at: 2026-10-30
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

# Eve

## Review boundary

- System in focus: Eve's source-distributed TypeScript agent runtime, including its durable session/turn/step model, first-party model/tool loop, optional declared subagents, channel continuation ownership and workflow tools.
- Purpose and identity: maintain long-lived agents with filesystem-backed tools, communication channels, schedules and durable tool/agent work across requests and process restarts.
- Relevant environment: user/channel messages, model/provider responses, tool/sandbox state, multiple concurrent session-start requests, workflow errors, delayed approvals and subagent outcomes.
- Standard-distribution boundary: `packages/eve` compiler, run/session/harness, subagent and channel modules with the default Workflow-SDK-backed supported local/self-hosted execution; application-authored agents/skills/tools are separate content.
- Credited operating / distribution surfaces: [`execution/session/entry.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/execution/session/entry.ts), [`execution/session-inbox/inbox.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/execution/session-inbox/inbox.ts), [`execution/continuation-conflict-step.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/execution/continuation-conflict-step.ts), [`harness/coordination.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/harness/coordination.ts), [`execution/session/turn-step.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/execution/session/turn-step.ts) and bundled tool/subagent interfaces.
- Adjacent first-party surfaces excluded from ownership: docs-site build, integration tests, application templates, benchmark/evaluation harnesses, release/CI machinery and Vercel platform deployment management; provider models and external workflow/sandbox backends are supporting infrastructure, not separately credited first-party decision owners.
- First-party operating / deployment modes considered: default local self-hosted `eve dev`/`eve start`, supported hosted deployment, channel-session and ID-only sessions, root/declared subagents, optional workflow tools and self-modification extension.
- Recursion level: one durable root agent and optional children/sibling session cells with shared channel continuation namespace; not the Vercel company or all user applications.
- Reviewed revision: `d004e6d47e9d25d0380c24b5a47b65a18f8b2784`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The compiler builds an agent from instructions, model, tools and extension configuration. A session is a durable workflow: each turn invokes the model/action loop and checkpoints completed steps. Tools can invoke sandbox operations or registered external integrations; child sessions have separate state, with synchronous/background paths and returned results. Channel adapters deliver and steer messages through session inbox continuation tokens. `session/entry.ts` claims a stable session token and any channel-address token; when two cold starts compete, the losing candidate cannot operate the same address and `continuation-conflict-step.ts` forwards its accepted send command to the owner. `inbox.ts` guarantees hook claim uniqueness inside the session and supports multiple aliases. Workflow suspension/replay, approval candidates, timeouts and credentials are bounded transport and enforcement mechanisms; they do not automatically prove S3/S3*/S4/S5 authority. The optional `eve/self-modification` extension is a separately installed capability, not evidence of a standard, prospective S4 function by itself.

## Operational model

The model selects answers and actions from tool outputs; Eve maintains a durable lifecycle across steps, sessions and channels. The only positive coordination finding is scoped to **channel-address ownership conflict**, where duplicate session candidates would otherwise independently consume a single continuation; it is not a general claim that every scheduling/delegation primitive is S2. Deterministic address arbitration is not agent-owned and lacks a separately composed autonomous S2 policy actor, yielding `C` rather than `A`. Whole-system current supervision, complementary audit, prospective strategy and constitutional identity are not established by the installed workflow and extension APIs alone.

## S1 — Operations

- State: A
- Function: execute model-chosen steps and tool actions in response to user/channel tasks, preserving continuity between turns.
- Disturbance / variety regulated: changing requests, sandbox/tool observations, provider errors, suspensions, crashes and delegated work results.
- Decisive decision or feedback right: model selects action/text/continuation after tool results; agent can delegate sub-tasks and consume subsequent returned outcomes.
- Decision owner: configured model-backed Eve agent, with user/authored code setting allowed capabilities.
- Supporting / enforcement mechanisms: Workflow SDK checkpointing, tool handlers, sandbox, compiler, session state, retry logic and permission prompts.
- Closure path: inbound message → model turn → tool or subagent decision → executed tool and committed result → later model decision or final answer.
- Boundary reachability: installed package implements durable session turns and built-in tools; user authors instructions/config but does not have to write a separate model/tool runtime.
- Why this is / is not agent-owned: model chooses semantic actions; deterministic state machine carries and limits them without replacing those decisions.
- Evidence: [`execution model`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/docs/concepts/execution-model-and-durability.mdx), [`turn-step.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/execution/session/turn-step.ts), [`subagents`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/docs/subagents/index.mdx).
- Basis: structural.
- Confidence: high for wired execution; no task-quality claim.
- Caveats: model/provider/tool adapters are configured separately by the application.

## S2 — Coordination

- State: C
- Function: prevent duplicate operational sessions from independently taking ownership of one channel continuation and reconcile their accepted message delivery into the rightful session.
- Disturbance / variety regulated: two concurrently started session candidates can claim the same Slack/thread/channel continuation address, risking diverging task histories and duplicate responses.
- Distinct S1 units: separate concurrently created root agent sessions/candidates in the same channel-address namespace; only one is permitted to continue as the legitimate operational owner.
- Inter-S1 disturbance: simultaneous hook claims to a shared channel continuation token are structurally mutually exclusive; without arbitration, messages accepted by the losing candidate would be lost or processed by a duplicate cell.
- Attenuating coordination relation: session startup attempts hook ownership; a conflict makes the losing candidate dispose and stop, while the settlement step forwards its already accepted `send` command into the existing owner's inbox.
- Feedback into subsequent S1 behaviour: the owner resumes on the forwarded command and carries on from its durable state; the losing duplicate does not produce a competing operational continuation.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: an explicit conflict-specific ownership/fallback path responds to interference among simultaneous operational session candidates sharing an external channel address, rather than merely queuing unrelated tasks.
- Decisive decision or feedback right: resolve exclusive channel owner and redirect the loser-origin message into the surviving session.
- Decision owner: deterministic first-party hook ownership/settlement primitives; no dedicated agent-owned decision on channel contention is provided as standard behavior.
- Supporting / enforcement mechanisms: Workflow SDK hook claim, `claimSessionHook`, `isHookConflictError`, `settleContinuationConflictStep`, `resumeSessionInbox` and session disposal.
- Closure path: conflicting session claim → winner retained, loser stopped → losing accepted command delivered to winner → subsequent owner model turn processes it.
- Boundary reachability: `session/entry.ts` executes this path during ordinary channel session creation when `continuationConflictCommand` is supplied by the channel delivery route; supported local and deployed runtime handle it, not only a unit-test harness.
- Why this is / is not agent-owned: no model arbitrates address ownership; the first-party coordination relation is specialized and closed deterministically, while independently composed agent governance would be needed for autonomous S2 ownership.
- Evidence: [`session/entry.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/execution/session/entry.ts), [`session-inbox/inbox.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/execution/session-inbox/inbox.ts), [`continuation-conflict-step.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/execution/continuation-conflict-step.ts), [`channel/types.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/channel/types.ts), [`execution-model`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/docs/concepts/execution-model-and-durability.mdx).
- Basis: explicit and structural.
- Confidence: medium, limited to the channel candidate conflict case.
- Caveats: no broader cross-team semantic coordination is credited; most workflow batch scheduling and subagent fan-out alone are not S2.

## S3 — Inside-and-now control

- State: —
- Function: no demonstrated whole-agent-system current-resource/commitment supervision, despite durable per-session state and cancellation/control APIs.
- Disturbance / variety regulated: concurrency, timeouts and retries are contained locally, but no unified current control decision owner over all operational cells is supplied.
- Decisive decision or feedback right: session runtime enforces fixed task/deadline/turn policies and caller-issued cancel/steer; it does not choose shared strategic priorities/resources from a whole-system view.
- Decision owner: developer/operator for global limits and session policy, runtime for mechanical enforcement, agent for ordinary local task continuation.
- Supporting / enforcement mechanisms: session/task records, background-task cohorts, durable workflow status, delivery policy and tool permissions.
- Closure path: local task/session status returns to its caller; no established whole-of-system view → supervisory decision → changed cross-cell operation.
- Why this is / is not agent-owned: persistence and runtime intervention affordances do not themselves create a metasystem current-control judgment.
- Evidence: [`execution model`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/docs/concepts/execution-model-and-durability.mdx), [`harness/coordination.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/harness/coordination.ts), [`tasks/session-task-cohorts.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/tasks/session-task-cohorts.ts).
- Basis: structural.
- Confidence: medium for bounded standard distribution.
- Caveats: a user-authored orchestration application could supply metasystem decisions through Eve workflow tools, outside the reusable runtime.

### Absence scope

- Surfaces inspected: session/turn workflow, task cohorts, background and subagent results, channel delivery/steering, workflow tools and documentation on self-hosted modes.
- Plausible first-party paths checked: durable current status, task cancel/steer, delivery queue versus steer policies, usage/limits, operator deployment transitions.
- Why no material first-party path remains: shipped paths ensure individual execution lifecycle/transport and continuation; no whole-system current-view decision loop over resource commitments, priorities and accountability is wired into the standard agent runtime.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent direct-inspection and corrective-report path complements ordinary model/task reporting.
- Disturbance / variety regulated: replay/authorization/tool errors are recorded, but logged operational events and approvals are not an independent audit channel.
- Decisive decision or feedback right: `approval-candidates` settles tool permission from authorized principals; tracing and sandbox boundaries enforce/observe normal execution.
- Decision owner: operator/authorization responder and ordinary runtime; no separately independent audit judge.
- Supporting / enforcement mechanisms: trace instrumentation, auth capability checks, approval audit records, security policy.
- Closure path: permission response changes whether an ordinary tool action proceeds; no separate audit assessment of operational reality returns to S3 control.
- Why this is / is not agent-owned: policy approval and deterministic event logging do not supply an independent S3* inspection right.
- Evidence: [`harness/approval-candidates.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/harness/approval-candidates.ts), [`tracing/agent-tool-instrumentation.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/tracing/agent-tool-instrumentation.ts), [`security model`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/docs/concepts/security-model.mdx).
- Basis: structural.
- Confidence: medium.
- Caveats: platform/provider-level audit services are outside the declared first-party runtime.

### Absence scope

- Surfaces inspected: approvals/trace modules, sandbox policy, session workflow, subagent result channels, tests and documentation.
- Plausible first-party paths checked: human authorization, approval audit record, OTel traces, subagent status and task error escalation.
- Why no material first-party path remains: checked paths implement first-line execution/enforcement and ordinary result reporting; no separated independently grounded operational audit with corrective S3 return is shipped.

## S4 — Outside-and-then intelligence

- State: —
- Function: no evidenced external-and-future intelligence loop deciding prospective changes to current organizational capability.
- Disturbance / variety regulated: evolving user prompts, installed skills and application source code may change, but the standard runtime does not assess external future threats/opportunities.
- Decisive decision or feedback right: models can write files and, if an extension is explicitly installed, edit local agent source while developing; no shipped external-trend sensing and strategic option approval is established.
- Decision owner: user/operator for app installation/deployment, model for task-local edits, no identified separate S4 authority.
- Supporting / enforcement mechanisms: filesystem tools, skill dynamic loading, optional self-modification extension, workflow checkpointing.
- Closure path: edited skills/source may change later code, but without an outside/future option-development and S3 feedback loop this is operational adaptation rather than proven S4.
- Why this is / is not agent-owned: generic self-modification and memory persist experience, not necessarily a future-oriented organizational intelligence function.
- Evidence: [`self-modification README`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve-self-modification/README.md), [`execution model`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/docs/concepts/execution-model-and-durability.mdx), [`compiler/compile-agent.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/compiler/compile-agent.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: a particular deployed agent may self-direct strategic evolution, but no such app-specific actor is credited without a pinned artifact.

### Absence scope

- Surfaces inspected: self-modification extension and integration instructions, dynamic skills, schedules, workflow tools and durable history documentation.
- Plausible first-party paths checked: code editing, skill loading, periodic schedules, long-term session memory and replay/redeployment.
- Why no material first-party path remains: all are capabilities to perform user/developer-defined work; a standard prospective future-environment sensing/alternatives/return circuit is not wired by Eve.

## S5 — Policy and identity

- State: —
- Function: no established identity/ultimate-policy arbitration with authoritative return across later agent operations.
- Disturbance / variety regulated: tool approval, credential boundaries and instruction/configuration changes are operational permissions, not ultimate mission/value deliberation.
- Decisive decision or feedback right: developer/administrator configures tools and credentials; authorized user approves individual operations; no policy-level conflict goes through a legitimate parent ratification circuit.
- Decision owner: application operator/developer for static policy and per-tool permission; not a first-party identity-governing agent or parent mode.
- Supporting / enforcement mechanisms: per-tool approval candidate state, channel auth, sandbox credential brokering, session capabilities and model instructions.
- Closure path: approval permits/denies actions within an existing policy; no future operation is governed by returned ultimate-policy adjudication.
- Why this is / is not agent-owned: executable code and approval gates are enforcement/support, not constitutional decision rights.
- Evidence: [`approval-candidates.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/harness/approval-candidates.ts), [`channel/types.ts`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/packages/eve/src/channel/types.ts), [`security model`](https://github.com/vercel/eve/blob/d004e6d47e9d25d0380c24b5a47b65a18f8b2784/docs/concepts/security-model.mdx).
- Basis: structural.
- Confidence: medium.
- Caveats: an enterprise application built on Eve can implement a higher parent authority; that is distinct from this reusable framework's standard boundary.

### Absence scope

- Surfaces inspected: session auth/capabilities, tool approval, security model, self-modification, channel and deployment configuration.
- Plausible first-party paths checked: identity in auth tokens, tool owner approvals, application environment policy, runtime self-editing and release governance.
- Why no material first-party path remains: these authorize access and shape application operation, but no first-party ultimate-policy issue/judgment/return cycle governs the agent's identity.

## Distributed OSS parent arrangement

Eve's open-source maintainers, Vercel deployment admins and independently hosted application owners are not a single parent VSM wired to a session's ultimate-policy path. No organization-level `(P)` notation is inferred from code ownership or external platform terms.

## Self-hosted and non-human modes

Both local Workflow SDK world and hosted modes preserve the model-led session loop. Operator policies and approval responders may pause individual tool actions, but they do not automatically supply whole-system S3 or ultimate S5. The S2 constructor claim specifically requires a channel route with a continuation-address conflict and command forwarding.

## Recursion

Root sessions, declared subagents and workflow tasks create operational subcells with durable state, but no evidence establishes independently viable S3–S5 metasystems at every nested level. Shared continuation address arbitration remains at the runtime/session recursion.

## Variety and escalation

Checkpointing attenuates crash/replay variety; inbox ownership attenuates duplicate agent response to one channel; approval suspensions and credential brokering bound tool risk. Tool denials and background task updates are ordinary runtime feedback, not by themselves independent audit or algedonic/governance escalation.

## Evidence gaps

- Pinned source and documentation only; no production Vercel deployment, paid model/tool calls or live multi-session collision experiment was executed.
- S2=C is bounded to explicit *channel continuation claim races* with accepted-command forwarding; ordinary workflow fan-out/fan-in or shared queues were not counted as S2.
- S4 remains bounded negative despite optional self-modification because no autonomous future-external strategic loop is supplied by the standard runtime itself.
