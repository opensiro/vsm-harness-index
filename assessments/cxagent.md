---
harness_id: cxagent
project_name: CXAgent
repository: https://github.com/nickprotop/cxagent
review_ref: e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1
reviewed_at: 2026-10-12
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# CXAgent

## Review boundary

- System in focus: CXAgent's first-party executable coding-agent product and the `CxAgent.Core` runtime it actually instantiates, including root session, model-tool loop, bundled file/shell tools, persistent child-agent runs, child mailbox/reach tools, workspace mutation path, shared background jobs and first-party built-in specialist types.
- Purpose and identity: perform repository coding work with autonomous model-guided tool use and optional delegated parallel specialist work under local workspace permissions.
- Relevant environment: user and active workspace/files, local shell and background jobs, code/test output, configured external model provider and optional MCP/plugin services.
- Standard-distribution boundary: the supported .NET terminal product and reusable `CxAgent.Core` components wired into it in normal single, fan-out, specialist and background-job modes. The specific first-party concurrency correction and independent built-in `review` specialist are included; examples, uninstalled external plugins, hosted providers, CI and maintainer governance are not separate credited systems.
- Credited operating / distribution surfaces: `cxagent.Core/Core/Agents/Agent.cs`, `AgentHost.cs`, `SubAgentSpawner.cs`, `SubAgentFactory.cs`, `SubAgentStore.cs`, `AgentMailbox.cs`, `AgentReachTools.cs`, `BuiltinAgentTypes.cs`, `cxagent.Core/Core/Jobs/Builtin/FileMutation.cs`, `FileJobExecutor.cs`, `BackgroundJobTools.cs`, first-party session assembly, permission-gated tools, and the shipped terminal entry point.
- Adjacent first-party surfaces excluded from ownership: `cxagent.Tests`, `.github` workflows, website, documentation-only demonstrations, `ROADMAP.md`, `docs/design` development notes, plugin marketplace and user-contributed/third-party plugins; these may corroborate behavior but do not supply missing deployed VSM function owners.
- First-party operating / deployment modes considered: direct local coding session; one session with parallel typed child agents and retained contexts; model-invoked `agent_list`/`agent_send`/`job_list`/`job_kill` paths; builtin `review`, `test`, `explore`, `planner`, `builder` specialists; concurrent write/replace and stale-file error handling; explicit user permission and approval.
- Recursion level: one terminal coding session with a root model decision-maker and, in fan-out mode, multiple subordinate model-driven S1 coding/specialist tasks. Other independent terminal sessions in a UI are adjacent to the chosen single-session recursion except insofar as shared first-party file-lock implementation demonstrates the concrete collision guard.
- Reviewed revision: e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1.
- Observation date: 2026-10-12.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The `Agent` and `AgentHost` own the current prompt/model-tool loop and return tool results to the model. `JobRegistry`, bundled `FileJobExecutor`, shell and HTTP tools implement requested work; permission policy confines actions but does not choose goals. The standard terminal composition instantiates `CxAgent.Core` as an operational coding product, not only an SDK. A root agent may issue independent `agent` spawns in one turn. Child `Agent` objects carry their own durable conversation and tool context, while a shared `SubAgentStore` retains handles and working/busy status so the parent may later use `agent_list` and `agent_send`.

The first-party file mutation utility is explicitly collision-specific: concurrent children share file executor and static per-absolute-path locks across the *full read-modify-write*, preserving a single writer per file. Stale-content checks reject edits computed against superseded bytes and return the conflict to the calling tool/model; the code comments and concurrent tests document silent lost-update failure with this mechanism absent. The lock is a deterministic S2-specific constructor path; it is not assigned autonomous ownership by virtue of being executable.

The root model can list retained subagents with busy state and send follow-up instructions, including mailbox delivery to a still-running child; it can list current background jobs across the session and select `job_kill` for any job begun by the session or its children. Child calls are restricted to their own jobs. This provides a narrowly bounded whole-session current-work resource/commitment view and model-controlled interventions, distinct from the deterministic scheduler and cancellation mechanisms. Model decisions can reassign or redirect subsequent specialist work. It does **not** imply a fleet- or organization-wide multi-session manager.

The built-in `review` child type is declared in first-party code and asks the child to inspect a diff or files for actual correctness faults. It is an independently initialized child agent, not the author's same-context self-review. Given actual first-party `read_file`, `grep`, `run_shell` etc. it can directly inspect the operational artifacts, and its objections return as a tool result to the parent for corrective action. The parent may choose to invoke review; it is not a universally enforced admission gate.

Primary source:
- [cxagent.Core/Core/Agents/Agent.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/Agent.cs)
- [cxagent.Core/Core/Agents/AgentHost.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/AgentHost.cs)
- [cxagent.Core/Core/Agents/SubAgentSpawner.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/SubAgentSpawner.cs)
- [cxagent.Core/Core/Agents/AgentReachTools.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/AgentReachTools.cs)
- [cxagent.Core/Core/Agents/BuiltinAgentTypes.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/BuiltinAgentTypes.cs)
- [cxagent.Core/Core/Jobs/Builtin/FileMutation.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Jobs/Builtin/FileMutation.cs)
- [cxagent.Core/Core/Jobs/Builtin/FileJobExecutor.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Jobs/Builtin/FileJobExecutor.cs)
- [cxagent.Core/Core/Jobs/BackgroundJobTools.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Jobs/BackgroundJobTools.cs)
- [README.md](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/README.md)

## Operational model

The root model owns task execution and, when configured, coordination decisions about its subordinate agents. The child models act on their independent contexts; their stdout, file edits and failures are visible through shared first-party tools and return results. The current session is the selected system; user permissions constrain implementation, and user-directed trust or config does not create an organizational S5 arbiter.

## S1 — Operations

- State: A
- Function: interpret a coding request, read/modify files, run tools/tests, handle failures and adapt the next step.
- Disturbance / variety regulated: task-specific requirements, repository contents, tests and shell/tool results, permissions, model messages, tool errors and background task outcomes.
- Decisive decision or feedback right: select next tool action or delegate child operation and revise based on observed result.
- Decision owner: root model in a normal coding session; bounded child models in fan-out mode.
- Supporting / enforcement mechanisms: .NET host, model provider transport, session persistence, file/shell job executor, permission layer and child spawner.
- Closure path: operator request → root model → first-party permission-gated tool/delegate action → file/test/child feedback → model correction or output.
- Boundary reachability: included in the supported executable `cxagent` terminal session, and in `CxAgent.Core` as composed by that session.
- Why this is / is not agent-owned: a model chooses task-specific actions and responses; deterministic host only executes and constrains them.
- Evidence: [cxagent.Core/Core/Agents/Agent.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/Agent.cs), [cxagent.Core/Core/Agents/AgentHost.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/AgentHost.cs), [cxagent.Core/Core/Jobs/Builtin/FileJobExecutor.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Jobs/Builtin/FileJobExecutor.cs), [README.md](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/README.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: third-party model/provider is the decision engine reached through first-party harness, not a separate imported organization.

## S2 — Coordination

- State: C
- Function: attenuate concurrent S1 code-writing interference on the same workspace file, making incompatible stale edits visible instead of silently losing one worker's change.
- Distinct S1 units: independent concurrently executing model-driven child agents instantiated by a root session and sharing the shipped file executor/workspace.
- Inter-S1 disturbance: simultaneous children can read one file, form edits on the same original bytes, then overwrite one another; the first-party commentary records this and a real concurrent-replace regression test.
- Attenuating coordination relation: a static per-canonical-path lock spans the entire read-modify-write and stale-content validation; `WriteIfUnchangedAsync` refuses obsolete edits.
- Feedback into subsequent S1 behaviour: a stale edit produces a specific refusal explaining that nothing was written and instructing reread/revise; that tool result enters the child's model feedback loop, allowing a new edit against current bytes, and parent sees outcomes.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism directly handles **conflicting writes by distinct simultaneous coding S1s** on one shared artifact, not merely dispatching messages or serializing unrelated jobs.
- Disturbance / variety regulated: races in shared-file mutation and loss of independent children's implemented changes.
- Decisive decision or feedback right: coordinate which writer may hold the file path, reject stale operation and return corrective signal; agent chooses subsequent remediation, not lock policy itself.
- Decision owner: first-party deterministic `FileMutation` chooses lock/admission; autonomous children can respond to returned conflict, but the S2-specific policy choice is not dynamically agent owned.
- Supporting / enforcement mechanisms: static `SemaphoreSlim` map, file snapshots, `StaleContentException`, shared `FileJobExecutor`.
- Closure path: competing child edits → per-path exclusion/validation → conflict refusal or sequential safe result → next child-model correction on returned evidence.
- Boundary reachability: first-party normal `replace_in_file`/write operations and fan-out children share this executable file mutation path; not a dev-only test helper.
- Why this is / is not agent-owned: the structural interference response is supplied and selected by deterministic shipped code; `C` credits a function-specific constructor path, not autonomous S2 policy ownership.
- Evidence: [cxagent.Core/Core/Jobs/Builtin/FileMutation.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Jobs/Builtin/FileMutation.cs), [cxagent.Core/Core/Jobs/Builtin/FileJobExecutor.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Jobs/Builtin/FileJobExecutor.cs), [cxagent.Tests/TwoSessionsTests.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Tests/TwoSessionsTests.cs), [cxagent.Tests/FileJobExecutorTests.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Tests/FileJobExecutorTests.cs).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: per-file safety is narrower than negotiated scheduling over whole-repository edits. Across distinct processes the in-process lock does not apply; stale-content check remains a separate guard.

## S3 — Inside-and-now control

- State: A
- Function: within one multi-child session, inspect currently committed child/background work and intervene on present operational commitments or available resources.
- Whole-system current view: model-facing `agent_list` reports retained child identities, specialist types and busy state; `job_list` reports all live background commands, ownership, timing, output paths and concurrency use across the session.
- Current-control decision scope: root model may use `agent_send` to redirect an existing child with preserved context, deliver to busy child mailbox, or kill any session/child-created background job rather than simply wait for completion; it can choose follow-on delegation and priority in response to statuses.
- Disturbance / variety regulated: runaway/surplus background work, stale or blocked commitments, changing task priorities and subsidiary agents requiring correction.
- Decisive decision or feedback right: select operational intervention, new instruction or job termination using whole-session current facts, not only run a static queue.
- Decision owner: autonomous root model when it invokes the bundled live view/control tools in fan-out mode.
- Supporting / enforcement mechanisms: child store, busy-claim mutex, mailbox, process registry, runtime permission and job ownership checks.
- Closure path: child/work registry state → `agent_list`/`job_list` → root model's follow-up/`job_kill` decision → child mailbox/future turn or terminated background process → updated current operation.
- Boundary reachability: all named tools are offered by first-party root-agent runtime in the shipped fan-out/session mode, not hypothetical external dashboard APIs.
- Why this is / is not agent-owned: parent chooses which child to redirect or process to stop, while runtime only keeps the list/ownership boundaries and enforces specific actions.
- Evidence: [cxagent.Core/Core/Agents/AgentReachTools.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/AgentReachTools.cs), [cxagent.Core/Core/Agents/SubAgentStore.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/SubAgentStore.cs), [cxagent.Core/Core/Agents/AgentMailbox.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/AgentMailbox.cs), [cxagent.Core/Core/Jobs/BackgroundJobTools.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Jobs/BackgroundJobTools.cs), [cxagent.Core/Core/Agents/Agent.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/Agent.cs).
- Basis: explicit + structural.
- Confidence: medium.
- Caveats: synchronous tool result barrier means the model may not inspect every executing child continuously during the original spawn turn; the credited current-control path is session-local, based on retained children, mailbox and concurrent background jobs. Not global control across separate UI sessions.

## S3* — Complementary audit

- State: A
- Function: a separately running bundled `review` child checks actual source/diff evidence and challenges the implementer's correctness claim before the parent acts on findings.
- Claim being audited: another agent or root implementer has produced code that is correct for the requested change.
- Ordinary reporting path: author's own completion report, observed tool/test outputs and normal coding trace.
- Complementary access path: distinct first-party child `Agent` with fresh conversation, builtin `review` type and direct read/grep/shell tools inspects named changed files or diff and returns specific objections with failing cases.
- Independence boundary: the built-in type is supplied by product code, receives its own model context and can inspect artifact bytes rather than relying solely on original developer's narration. It may use the same base provider/model; independence here is execution/context and evidence access, not guaranteed distinct vendor.
- Who acts on findings: root model receives review subagent result in normal tool feedback and may modify code, run checks or redirect work.
- Disturbance / variety regulated: silent correctness defects, incomplete implementation and overconfident author claims.
- Decisive decision or feedback right: choose an artifact-grounded judgment independently of implementation context, return objections as new information for corrective control.
- Decision owner: reviewer child model for its audit judgment; parent owns corrective task choices.
- Supporting / enforcement mechanisms: builtin review profile/type, separate child context, shared read tools, first-party subagent-result envelope and parent continuation.
- Closure path: parent requests independent review → first-party reviewer reads operational artifacts → model reports concrete verified issues → parent model receives and can correct subsequent implementation.
- Boundary reachability: `review` is a shipped built-in agent type in `BuiltinAgentTypes.cs`; ordinary `agent` subagent factory/spawner can instantiate it in product's standard fan-out mode.
- Why this is / is not agent-owned: child model makes the differential correctness judgment from direct workspace evidence; deterministic return path does not choose its findings.
- Evidence: [cxagent.Core/Core/Agents/BuiltinAgentTypes.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/BuiltinAgentTypes.cs), [cxagent.Core/Core/Agents/SubAgentSpawner.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/SubAgentSpawner.cs), [cxagent.Core/Core/Agents/SubAgentFactory.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/SubAgentFactory.cs), [cxagent.Core/Core/Agents/Agent.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/Agent.cs), [README.md](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/README.md).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: role invocation is optional and parent-chosen, not an always-on merge admission or externally guaranteed neutral auditor. Distinct context and raw file access, not naming alone, underpin this classification.

## S4 — Outside-and-then intelligence

- State: —
- Function: no evidenced first-party closed external-prospective adaptation loop changing the system's *future organizational capability* at this chosen session boundary.
- Disturbance / variety regulated: not established as organizational S4; task-local web fetch, model selection and extension loading address present work or developer/user-supplied capabilities.
- Decisive decision or feedback right: no supported agent-owned future-environment interpretation and returned capability adaptation identified.
- Decision owner: no S4 owner established.
- Supporting / enforcement mechanisms: web/HTTP fetch tools, session context, model catalogs, skills and plugin loading, user configuration, project docs and development roadmap.
- Closure path: none qualifying S4; local task results inform immediate coding decisions rather than durable future capability design owned by the agent.
- Boundary reachability: no positive S4 claim.
- Why this is / is not agent-owned: externally authored extensions and model/provider changes can alter capability but do not prove an agent-led prospective outside-and-then loop in the supported distribution.
- Evidence: [cxagent.Core/Core/Llm/ProviderCatalog.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Llm/ProviderCatalog.cs), [cxagent.Core/Core/Agents/Agent.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/Agent.cs), [cxagent.Core/Core/Sessions/Session.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Sessions/Session.cs), [README.md](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: optional contributor-authored/adaptive plugins not included unless actually wired in a first-party shipped autonomous mode.

### Absence scope

- Surfaces inspected: agent context/session/skills, shipped tools and model catalogs, plugin loading and user configuration, documentation and operator modes.
- Plausible first-party paths checked: web-fetch for current tasks, provider selection, retained child context, user-driven plugin installation, skills/context compaction and roadmap text.
- Why no material first-party path remains: no inspected mode makes external prospective distinction, produces a proposed adaptation and closes that decision into future organizational capability rather than servicing present requests or externally chosen configuration.

## S5 — Policy and identity

- State: —
- Function: no first-party organizational constitutional arbiter for the system's enduring purpose/ultimate policy, with authoritative feedback into operation.
- Disturbance / variety regulated: permission/trust exceptions and task constraints exist, but identity- or mission-level policy conflicts are not evidenced.
- Decisive decision or feedback right: none meeting S5 ultimate purpose/identity at selected session recursion.
- Decision owner: none established; user and config supply ordinary execution trust and tool permissions.
- Supporting / enforcement mechanisms: folder permissions, trusted commands, model classifier in auto mode, builtin agent type briefings, user-defined config and plugin gates.
- Closure path: runtime enforces user-set local rules; no identity/purpose proposal → legitimate authority → constitutional decision → returned policy loop found.
- Boundary reachability: no positive S5 claim.
- Why this is / is not agent-owned: removing model still leaves configuration and guard rules; removing operator consent does not expose autonomous ultimate-purpose decision right.
- Evidence: [cxagent.Core/Core/Permissions/PermissionPolicy.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Permissions/PermissionPolicy.cs), [cxagent.Core/Core/Permissions/PermissionDecider.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Permissions/PermissionDecider.cs), [cxagent.Core/Core/Agents/BuiltinAgentTypes.cs](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/cxagent.Core/Core/Agents/BuiltinAgentTypes.cs), [COMMANDS.md](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/COMMANDS.md), [README.md](https://github.com/nickprotop/cxagent/blob/e2b2551fc8897d5be5833441e9ec6e3c4e63cdf1/README.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: external project/human governance is outside this standard session boundary.

### Absence scope

- Surfaces inspected: permissions and approval modes, model-based command safety classifier, fixed system prompts, builtin type instructions, session configuration and user plugins.
- Plausible first-party paths checked: human trust choices, user questions, child role briefings, tool gating, allowed/restricted commands and loaded project instructions.
- Why no material first-party path remains: present trust/permission mechanisms regulate current operational authority, not lasting system purpose and ultimate policy with a legitimate constitutional return path.

## Recursion

At the product-session recursion, the root coding agent and its separately executing child workers supply the operational set. A child retains its own context and handles local coding/review variance. The shared file mutation guard, root's current-work controls and optional independent reviewer are functionally different from ordinary local S1 behavior. Multi-session UI tabs and external development organizations remain outside this one-session conclusion.

## Variety and escalation

Autonomous agents absorb task-level coding variety; static per-file locks and stale edit exceptions attenuate parallel overwrite risk; child context/messaging and process registry support root intervention. User trust/permission prompts and optional model classifiers constrain dangerous tools, but no S5 is inferred. Ordinary telemetry/status, error reports and pipeline events are not by themselves algedonic or an additional S-function.

## Evidence gaps

- Positive S2 is intentionally scoped to in-process shared-file write interference and the documented stale-error feedback, not broad inter-team coordination or cross-process worktree ownership. Secondary review should test that this qualifies `C` rather than `A`, given autonomous retry choices but deterministic admission.
- S3 depends on a concrete root-agent *active work* session mode with session-local subagent/job listing, model-led intervention and returned feedback. A synchronous spawn result barrier limits when it can intervene; review should verify that the reachable model-facing status/job controls satisfy the whole-current threshold rather than only task-level operations.
- S3* credits the optional built-in distinct-context `review` child with direct workspace tools. No claim is made of an external independently executing OpenSiro assessor or default mandatory approval.
- Runtime end-to-end live provider execution was not performed; this is a frozen revision primary-code/source-first assessment.

