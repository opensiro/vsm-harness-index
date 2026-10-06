---
harness_id: sharpcoder
project_name: SharpCoder
repository: https://github.com/robkaandorp/SharpCoder
review_ref: f35e4003b41020204897aa8f6da3ba9bc1cdf590
reviewed_at: 2026-10-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-06
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SharpCoder

## Review boundary

- System in focus: the first-party SharpCoder .NET coding-agent runtime at frozen revision \`f35e4003b41020204897aa8f6da3ba9bc1cdf590\`, including the main model/tool loop, built-in coding tools, persistent/forkable sessions, auto-compaction, configured background subagents, lifecycle/status events and supported host-facing library surfaces.
- Purpose and identity: provide an embeddable autonomous coding loop that can inspect, edit and execute within a workspace and optionally delegate bounded self-contained analysis/research/coding tasks to background sub-sessions.
- Relevant environment: caller/user goals, repository/workspace files, shell/tool/test results, provider/model responses, context pressure, subagent statuses/summaries, cancellation and host configuration.
- Standard-distribution boundary: shipped SharpCoder library/runtime and repository-owned tools, sessions, compaction and subagent manager/tool surfaces. External \`IChatClient\` model providers, the host application, operating-system programs and the user's repository are dependencies and cannot donate organizational functions.
- Credited operating / distribution surfaces: \`src/SharpCoder/CodingAgent.cs\`, built-in tools, \`AgentSession\`, \`ContextCompactor\`, \`src/SharpCoder/SubAgents/\` and public host-facing lifecycle/status APIs.
- Adjacent first-party surfaces excluded from ownership: tests, release/CI infrastructure, changelog prose except as corroboration, consuming host applications and any user-written custom tools/agents not instantiated by the shipped runtime.
- First-party operating / deployment modes considered: ordinary single-agent execution; persistent/resumed/forked sessions; configured subagent mode with background children; optional write-enabled child configuration within the parent's capability ceiling; separate compaction-client mode.
- Recursion level: one SharpCoder coding-agent instance plus any first-party sub-sessions it starts. The main model loop is the primary S1; a child sub-session is an additional S1 only when its bounded task itself constitutes an operational outcome.
- Reviewed revision: \`f35e4003b41020204897aa8f6da3ba9bc1cdf590\`.
- Observation date: 2026-10-06.
- Generated Profile version: \`0.2.4\`.
- Generated Methodology version: \`0.3.6\`.
- Current Profile version: \`0.2.4\`.
- Current Methodology version: \`0.3.6\`.

## Repository architecture

SharpCoder wraps an \`IChatClient\` with a first-party coding loop and built-in read/write/edit/glob/grep/bash/skills tools. \`AgentSession\` persists multi-turn conversation state and can save/load/fork it. \`ContextCompactor\` summarizes old history when context grows too large, optionally using a separate compaction model.

When \`AgentOptions.SubAgents\` is configured, the main agent gains four tools: \`start_sub_agent\`, \`await_sub_agents\`, \`get_sub_agent_status\`, and \`list_sub_agent_models\`. A shared \`SubAgentManager\` accepts background sub-sessions, limits concurrency with a semaphore, records lifecycle state and returns summaries/status rather than full child transcripts. Children are read-only by default, but configured file writes can be enabled up to the parent capability ceiling.

The subagent surface is delegation/lifecycle transport rather than a complete metasystem. There is no first-party peer collision/lease/worktree mechanism for write-enabled children, no model-callable selective cancel/reprioritize tool, and no dedicated independent reviewer/verifier constructor. Cancelling an enclosing execution deliberately does not cancel already-running subagents; disposing the whole CodingAgent cancels all running children as shutdown behavior.

## Operational model

The model-backed main agent owns open-ended coding/tool decisions and may decide to start bounded children, poll their status, await their summaries and use those summaries in later coding decisions. Child agents independently execute their assigned task within clamped capabilities.

Concurrency limits, timeouts, status events, disposal cancellation and compaction are deterministic support mechanisms. They constrain or summarize work but do not by themselves establish S2/S3/S3*/S4/S5 ownership.

## S1 — Operations

- State: A
- Function: autonomously inspect, modify and verify software in response to a coding objective, directly or through bounded delegated sub-sessions.
- Disturbance / variety regulated: unfamiliar code, implementation choices, test/tool outcomes, context overflow, provider/model behavior and delegated analysis/research tasks.
- Decisive decision or feedback right: choose substantive coding/tool actions, interpret returned evidence, decide when delegation is useful and decide when the requested operational outcome is complete.
- Decision owner: the active model-backed SharpCoder coding agent; configured child model sessions own decisions inside their bounded delegated tasks.
- Supporting / enforcement mechanisms: built-in tools, path-safety/tool capability configuration, session persistence/forking, context compaction, subagent concurrency/timeouts and provider wrappers.
- Closure path: caller request → model selects repository/tool action or bounded subagent → first-party runtime executes and returns tool evidence or child summary → model revises work → model completes the request.
- Boundary reachability: the normal public \`CodingAgent.ExecuteAsync\` / streaming paths instantiate the model/tool loop, and configured subagent tools are injected into that same shipped execution path.
- Why this is / is not agent-owned: deterministic runtime code transports and constrains actions, but removing the model actors removes the open-ended implementation/investigation/completion judgments.
- Evidence: [README.md](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/README.md); [src/SharpCoder/CodingAgent.cs](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/src/SharpCoder/CodingAgent.cs); [src/SharpCoder/SubAgents/SubAgentManager.cs](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/src/SharpCoder/SubAgents/SubAgentManager.cs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: subagents are optional and read-only by default; the core positive S1 claim does not depend on enabling them.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination loop is established.
- Disturbance / variety regulated: configured write-enabled children could contend in one workspace, but the reviewed runtime does not place such peer interference under a function-specific attenuation/feedback relation.
- Decisive decision or feedback right: none established for S2.
- Decision owner: none established.
- Supporting / enforcement mechanisms: \`MaxConcurrentSubAgents\` semaphore, child capability ceilings, per-run immutable option snapshots and result/status collection bound concurrency and capability but do not coordinate concrete peer conflicts.
- Closure path: not applicable.
- Boundary reachability: no positive S2 path claimed.
- Why this is / is not agent-owned: the main agent may decide to start multiple tasks, while the runtime limits how many run; neither path supplies a concrete collision detector/reservation/worktree/negotiation loop that feeds mutual adjustment back into peer S1 behavior.
- Evidence: [README.md](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/README.md); [src/SharpCoder/SubAgents/SubAgentManager.cs](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/src/SharpCoder/SubAgents/SubAgentManager.cs); [src/SharpCoder/SubAgents/SubAgentOptions.cs](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/src/SharpCoder/SubAgents/SubAgentOptions.cs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: serialization by a concurrency semaphore is generic load control, not evidence that an actual inter-S1 interference mode is being attenuated.

### Absence scope

- Surfaces inspected: subagent manager/options/tools, main tool injection, workspace/capability handling, lifecycle/status events and tests/docs describing concurrent child execution.
- Plausible first-party paths checked: file/path leases, per-child worktrees, collision detection, dependency ordering, peer negotiation, shared mutation arbitration and merge/integration control.
- Why no material first-party path remains: located controls limit concurrency/capability and collect results; they do not close a concrete inter-S1 interference/feedback loop.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party whole-system current-control loop is established over the active child set.
- Disturbance / variety regulated: child status, timeout and completion are observable, but no actor is shown owning substantive live reallocation/intervention over the whole current set of commitments.
- Decisive decision or feedback right: none established for S3.
- Decision owner: none established.
- Supporting / enforcement mechanisms: \`start_sub_agent\`, \`await_sub_agents\`, \`get_sub_agent_status\`, lifecycle events, timeout state and host-visible \`ActiveSubAgentManager\`.
- Closure path: not applicable.
- Boundary reachability: no positive S3 path claimed.
- Why this is / is not agent-owned: the main model can create work, poll it and await summaries, but the shipped model toolset has no selective live cancel/retry/reprioritize/reallocate operation over already-running children. \`DisposeAsync\` cancels all children as shutdown, and caller-token cancellation explicitly leaves running children alive.
- Evidence: [src/SharpCoder/SubAgents/SubAgentTools.cs](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/src/SharpCoder/SubAgents/SubAgentTools.cs); [src/SharpCoder/SubAgents/SubAgentManager.cs](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/src/SharpCoder/SubAgents/SubAgentManager.cs); [src/SharpCoder/CodingAgent.cs](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/src/SharpCoder/CodingAgent.cs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: lifecycle visibility and stop-all disposal are useful controls but do not satisfy the Methodology 0.3.6 whole-current view + substantive current-control decision threshold.

### Absence scope

- Surfaces inspected: model-callable subagent tools, manager lifecycle/status API, agent-level events, cancellation semantics, timeout handling and disposal.
- Plausible first-party paths checked: selective child cancel, live retry, reprioritization, task reassignment, resource reallocation, parent current-work dashboard/control and model-owned supervisor loop.
- Why no material first-party path remains: the standard paths expose spawn/wait/status/shutdown rather than a substantive whole-system current-control decision and return path.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit path is established.
- Disturbance / variety regulated: no dedicated independent reviewer/verifier is wired to challenge an implementation claim and return findings into corrective operation.
- Decisive decision or feedback right: none established for S3*.
- Decision owner: none established.
- Supporting / enforcement mechanisms: generic subagents, normal test/tool execution, session forks and a separate compaction model may provide additional computation but are not function-specific independent audit constructors.
- Closure path: not applicable.
- Boundary reachability: no positive S3* path claimed.
- Why this is / is not agent-owned: any child can be asked ad hoc to review, but the shipped runtime provides only generic task delegation; it does not establish an authorship-independent reviewer role, complementary evidence path and corrective verdict loop.
- Evidence: [README.md](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/README.md); [src/SharpCoder/SubAgents/SubAgentTools.cs](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/src/SharpCoder/SubAgents/SubAgentTools.cs); [src/SharpCoder/AgentSession.cs](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/src/SharpCoder/AgentSession.cs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: generic user/model-authored review prompts remain S1 composition unless the distribution supplies the distinct audit relation itself.

### Absence scope

- Surfaces inspected: subagent roles/tools/options, session forking, ordinary testing/tool paths, compaction-client path and repository tree/search for reviewer/verifier constructs.
- Plausible first-party paths checked: fresh-context reviewer, separate evidence access, fixed verification role, second-model critique and audit verdict feeding repair/acceptance.
- Why no material first-party path remains: no dedicated standard first-party path closes the independent claim→audit→corrective-return relation.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective adaptation loop is established.
- Disturbance / variety regulated: no external/future distinction is transformed into organizational adaptation options and returned into present capability.
- Decisive decision or feedback right: none established for S4.
- Decision owner: none established.
- Supporting / enforcement mechanisms: persistent sessions, session forking, context compaction, skills and model configuration preserve/reduce context or supply current capabilities but do not close S4.
- Closure path: not applicable.
- Boundary reachability: no positive S4 path claimed.
- Why this is / is not agent-owned: a compaction model summarizes past conversation for current continuity, and persisted sessions can be resumed later, but neither mechanism develops prospective adaptation options from changing external conditions.
- Evidence: [src/SharpCoder/ContextCompactor.cs](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/src/SharpCoder/ContextCompactor.cs); [src/SharpCoder/AgentSession.cs](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/src/SharpCoder/AgentSession.cs); [README.md](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: persistence and context summarization can improve future turns, but memory reuse/compression is not sufficient S4 under the active Profile.

### Absence scope

- Surfaces inspected: sessions/save-load/fork, context compaction, skills, model/subagent configuration and lifecycle events.
- Plausible first-party paths checked: external environment sensing, learned durable strategy update, autonomous capability reconfiguration, future option generation and return-to-current-control.
- Why no material first-party path remains: inspected paths preserve or compress state and accept externally configured capabilities rather than close an outside-and-then adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy governance loop is established.
- Disturbance / variety regulated: no identity-level policy conflict is routed to an authoritative S5 owner and returned as governing policy.
- Decisive decision or feedback right: none established for S5.
- Decision owner: none established.
- Supporting / enforcement mechanisms: \`AgentOptions\`, tool/capability flags, path safety and host-supplied system/custom instructions constrain execution but do not create identity governance.
- Closure path: not applicable.
- Boundary reachability: no positive S5 path claimed.
- Why this is / is not agent-owned: the coding agent operates within host/developer-provided policy and capability settings and cannot authoritatively redefine SharpCoder's identity or ultimate operating principles.
- Evidence: [README.md](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/README.md); [src/SharpCoder/AgentOptions.cs](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/src/SharpCoder/AgentOptions.cs); [src/SharpCoder/CodingAgent.cs](https://github.com/robkaandorp/SharpCoder/blob/f35e4003b41020204897aa8f6da3ba9bc1cdf590/src/SharpCoder/CodingAgent.cs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: callers legitimately configure policy/capability constraints, but generic host configuration is not an identity/ultimate-policy decision loop.

### Absence scope

- Surfaces inspected: AgentOptions, tool/capability configuration, path safety, system/custom instructions, lifecycle/disposal and session configuration.
- Plausible first-party paths checked: autonomous constitutional revision, parent identity governance, runtime policy-authoring agent and authoritative policy feedback.
- Why no material first-party path remains: all observed policy surfaces are static/external operating constraints rather than a closed S5 governance function.

## Distributed OSS parent arrangement

The assessed organization is the running SharpCoder library instance, not the GitHub maintainer/contributor project. Repository development and release processes are not imported as runtime metasystem ownership.

## Self-hosted and non-human modes

SharpCoder is provider-agnostic and embeddable. The positive S1 claim is independent of the chosen \`IChatClient\`. No parent-governed S3/S4/S5 state is inferred from a consuming application's ability to subscribe to events or dispose the library instance.

## Recursion

The declared boundary contains the main coding agent and optional bounded child sub-sessions. Each child can be operational S1 when it owns a concrete delegated outcome. The manager, semaphore, lifecycle events and compactor remain support mechanisms rather than positive higher VSM functions.

## Variety and escalation

S1 absorbs coding/tool variety and can delegate bounded work. Concurrency caps, timeouts, context compaction, lifecycle events and shutdown prevent or expose runtime failures, but at the frozen boundary they do not establish S2/S3/S3*/S4/S5.

## Evidence gaps

No \`?\` state is required. The frozen implementation exposes the public subagent tools, manager/cancellation semantics, session/compaction behavior and configuration surfaces broadly enough to support the positive S1 and bounded negative conclusions for the remaining functions.
