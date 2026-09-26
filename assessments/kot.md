---
harness_id: kot
project_name: KOT
repository: https://github.com/Loqira-Labs/agentkot
review_ref: 7cf18c4b8389a81ea2f15ab70d1b0bb31b44b6ab
reviewed_at: 2026-09-26
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-26
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# KOT

## Review boundary

- System in focus: one first-party KOT deployment at pinned revision `7cf18c4b8389a81ea2f15ab70d1b0bb31b44b6ab`, including the shipped executable, ordinary model/tool session loop, persistent sessions/history/memory, Plan task boards, subagent/delegate/teammate orchestration, durable workflows, worktree isolation, provider/model routing and the `until` worker-check-supervisor loop.
- Purpose and identity: a local general/coding agent harness that performs user work directly on the host, persists task/session context and can organize multiple agents across providers into concurrent delegated work and durable pipelines.
- Relevant environment: user objectives, local workspace/files/processes, configured model providers, git/ripgrep, persistent session/task/memory state, child-agent workspaces, command/test outcomes and human owners of optional workflow ask/escalation gates.
- Standard-distribution boundary: the prebuilt Linux/macOS/Windows KOT executable and the detailed first-party tool/runtime contracts shipped in this repository at the frozen ref. The runtime source is not published in the reviewed tree, so no positive claim depends on undocumented binary internals.
- Credited operating / distribution surfaces: the shipped executable and Web UI; documented Agent, Plan, History, Memory, Files, Shell, Search and other built-in tool contracts; child/teammate lifecycle and mail; workflow status/stop/resume; model/provider switching; worktree isolation; `until` direct checks and supervisor verdicts.
- Adjacent first-party surfaces excluded from ownership: benchmark results and benchmark repositories; marketing comparisons; translated duplicate documentation; external model providers as organizational owners; environment-supplied containers/VMs/sandboxes; project-maintainer development activity; any behavior hidden inside the binary that is not established by the public first-party shipped contract.
- First-party operating / deployment modes considered: ordinary single-agent sessions; synchronous `spawn`; background `delegate`; persistent `hire` teammates; shared-team Plan boards; worktree-isolated children; durable workflow DAGs; `delegate` with `until` direct check and optional supervisor; resumed sessions/workflows; live teammate model/provider switching.
- Recursion level: one KOT lead session and its owned child/delegate/teammate organization. Child sessions are distinct S1 units for S2/S3 analysis, but child nesting or nested workflows are not promoted to complete VSM recursion by themselves.
- Reviewed revision: `7cf18c4b8389a81ea2f15ab70d1b0bb31b44b6ab`.
- Observation date: 2026-09-26.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

KOT is distributed here primarily as prebuilt executables plus detailed first-party contracts for every major built-in tool. The standard product exposes a persistent model/tool agent session with file editing, shell/process control, search, history recovery, memory, planning, media and dynamic tools. Session history can be resumed or rewound; persistent Memory notes and task graphs survive sessions; the Web UI exposes live tool/background/child state and interruption.

The Agent tool creates several distinct child modes. `spawn` blocks for a child's report; `delegate` launches a background child whose terminal result later arrives as a task notification; `hire` creates a persistent wakeable teammate with its own session. The main/orchestrating session alone can create arbitrary children and workflows. It can inspect the current owned roster and live state, send follow-up mail, stop children, and switch a live teammate's provider/model for its next turn.

Parallel operational work can share one project working directory. Child `cwd` is inherited unless overridden; workflow-ready steps run concurrently; each child has an isolated session/virtual file layer but syncs edits to disk. The model-facing Agent contract therefore exposes `isolation:"worktree"`, creating a separate git worktree/branch and making it the child's cwd. Workflow agent/team steps can likewise be `transactional`, using worktree transactionality. The task-specific choice to isolate a potentially interfering child is supplied by the orchestrating model/declaration, while KOT supplies the enforcement.

KOT also ships a complementary completion-audit path. A delegated worker can run under an `until` gate: after each worker turn KOT executes a declared command directly in the worker's working directory. A failing check feeds its output into the next worker turn. Even after the direct check passes, an optional separate supervisor agent produces `VERDICT: accept|continue|escalate`; `continue` returns corrective specifics into the worker, `escalate` fails the loop, and malformed verdicts fail loudly. The built-in `arbiter` is explicitly the judge role and can run on a separate model/provider.

Primary evidence:

- [`README.md`](https://github.com/Loqira-Labs/agentkot/blob/7cf18c4b8389a81ea2f15ab70d1b0bb31b44b6ab/README.md) — shipped executable/product boundary, standard Web/session controls, multi-agent/provider operation and built-in tool inventory.
- [`tools/Agent.md`](https://github.com/Loqira-Labs/agentkot/blob/7cf18c4b8389a81ea2f15ab70d1b0bb31b44b6ab/tools/Agent.md) — child modes, mail/stop/status/model-switch control, worktree isolation, durable workflows, `until` worker-check-supervisor loop and `arbiter` judge role.
- [`tools/Plan.md`](https://github.com/Loqira-Labs/agentkot/blob/7cf18c4b8389a81ea2f15ab70d1b0bb31b44b6ab/tools/Plan.md) — persistent task graph, owners/dependencies, shared team boards and serialized mutation.
- [`tools/History.md`](https://github.com/Loqira-Labs/agentkot/blob/7cf18c4b8389a81ea2f15ab70d1b0bb31b44b6ab/tools/History.md) — persistent session history, cross-session recovery/fork and compaction.
- [`tools/Memory.md`](https://github.com/Loqira-Labs/agentkot/blob/7cf18c4b8389a81ea2f15ab70d1b0bb31b44b6ab/tools/Memory.md) — persistent notes, scoped search and session-start prefetch.

## Operational model

The active session model owns ordinary next-action selection. The lead model can create and currently regulate several child S1s, while deterministic KOT services persist sessions/tasks, deliver mail, execute lifecycle changes and enforce selected worktree boundaries. Direct command checks and an optional independent supervisor provide a separate challenge path to a worker's completion. Persistent memory/history support later operation but do not by themselves constitute organizational adaptation or identity-policy authority.

## S1 — Operations

- State: A
- Function: transform user objectives into code/file/process/research outcomes through repeated model-selected tool actions and returned operational evidence.
- Disturbance / variety regulated: heterogeneous user requests, changing workspace/process state, tool errors/results, provider/model outputs, prior session evidence, context pressure and follow-up input.
- Decisive decision or feedback right: choose the next substantive tool/action, arguments and stopping point, revising later actions from returned tool/environment evidence.
- Decision owner: the active KOT session model; child models own the same local operational discretion within their assigned work.
- Supporting / enforcement mechanisms: shipped executable, built-in tool schemas/executors, persistent sessions, History/Memory/Plan, background-process management, provider adapters and Web UI.
- Closure path: user/session context → model selects tool/action → KOT executes and records the result → later model step observes that evidence → model revises the next operation or concludes.
- Boundary reachability: the executable and built-in model/tool surface are the standard shipped product, not benchmark/development-only machinery.
- Why this is / is not agent-owned: removing the model removes task-specific selection of tools, arguments and completion; the runtime executes and persists those choices rather than replacing them with a fixed procedure.
- Evidence: `README.md`; `tools/Agent.md`; built-in tool documentation.
- Basis: explicit
- Confidence: high
- Caveats: the frozen repository does not publish runtime source, so this assessment relies on first-party shipped contracts rather than inferred internal implementation details.

## S2 — Coordination

- State: A
- Function: attenuate interference among concurrently executing child S1s by assigning dependencies/owners and, when operations may collide in a shared project, selecting isolated worktree execution.
- Disturbance / variety regulated: ready workflow steps/delegates/teammates can operate concurrently; without isolation, inherited child cwd and disk-synced edits can overlap in the same project state and invalidate peer work.
- Decisive decision or feedback right: choose which child work may run concurrently and whether a child/step receives `isolation:"worktree"` / transactional worktree execution, plus define task dependencies that delay dependent work.
- Decision owner: the orchestrating lead model when issuing Agent/Plan calls; for declared workflows, the first-party workflow declaration supplies the chosen dependency/isolation relation and KOT enforces it.
- Supporting / enforcement mechanisms: separate child sessions, git worktree creation/cleanup, workflow DAG dependency scheduler, shared Plan board, serialized task mutation and child result/mail feedback.
- Closure path: lead identifies/decomposes multiple tasks → assigns dependencies and/or selects a dedicated worktree for an interfering child → KOT schedules ready work and enforces isolated cwd/branch where selected → child results/status return to the lead/shared board → subsequent work is integrated, redirected or delayed accordingly.
- Boundary reachability: `Agent{spawn|delegate|hire}` and workflow transactional/worktree controls are documented built-in capabilities of the shipped executable; no downstream coordinator is required.
- Why this is / is not agent-owned: KOT deterministically creates the requested worktree and respects declared DAG edges, but the task-specific judgment that work is independent or needs isolation/dependency belongs to the lead model/declaration. The runtime does not infer equivalent semantic isolation from the task text.
- Evidence: `tools/Agent.md`; `tools/Plan.md`.
- Basis: explicit + structural
- Confidence: high
- Caveats: worktree isolation is optional; credit is for the shipped model-selectable coordination relation, not for generic concurrency or messaging alone.
- Distinct S1 units: the lead session plus multiple separately running child/delegate/teammate sessions, each driven by its own model and tool loop.
- Inter-S1 disturbance: concurrently ready children may otherwise edit the same inherited project workspace or consume/alter shared operational state in incompatible ways.
- Attenuating coordination relation: model/declaration-selected git-worktree isolation, plus explicit workflow/Plan dependencies and owners that constrain which work becomes ready together.
- Feedback into subsequent S1 behaviour: child terminal notifications, mail, shared task-board state and workflow state return coordinated outcomes; failed/dependent/isolation outcomes alter later lead/child work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited relation targets a concrete concurrent shared-workspace interference mode and changes where/when affected S1 units may operate; mail and child spawning alone are not credited.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current portfolio of owned child/delegate/teammate work, including commitments, lifecycle, task ownership and model/provider resources.
- Disturbance / variety regulated: changing child progress/liveness, pending mail, failed or obsolete commitments, blocked tasks, provider/model suitability, workflow pause/failure and need to redirect or terminate current work.
- Decisive decision or feedback right: create/withhold child commitments; inspect current owned-agent status; send new instructions; stop work; change a live teammate's model/provider; mutate task owners/dependencies; inspect/stop/resume workflows.
- Decision owner: the lead/orchestrating model for its owned domain, with optional human ownership only where an explicit workflow `ask`/escalation step is declared.
- Supporting / enforcement mechanisms: Agent `status/send/stop/set_model`, durable child registry/session ids, shared Plan board, workflow `status/stop/resume`, mail router and Web current-state panels.
- Closure path: lead creates current commitments → status/task/workflow views return present state → lead chooses steering, reassignment, resource/model change, stop or further delegation → KOT applies it → subsequent child/workflow operation changes.
- Boundary reachability: these operations are model-facing built-ins of the shipped Agent/Plan surface and are also exposed in standard Web controls.
- Why this is / is not agent-owned: lifecycle services enforce stop/mail/model transitions, but the substantive current-control choice over which commitment to redirect, terminate or re-resource is made by the lead model.
- Evidence: `tools/Agent.md`; `tools/Plan.md`; `README.md`.
- Basis: explicit
- Confidence: high
- Caveats: KOT intentionally prevents arbitrary child re-orchestration; S3 is centered at the main lead session's declared ownership domain.
- Whole-system current view: `Agent{status}` lists the lead's teammates and delegates with lifecycle/live state, model/provider, pending mail and wake errors; the Plan board and workflow status expose current task ownership/dependencies/run state for the same organization.
- Current-control decision scope: child/team creation, current instruction steering, interruption/removal, task ownership/dependency mutation, workflow stop/resume and live teammate model/provider allocation.

## S3* — Complementary audit

- State: A
- Function: independently challenge a delegated worker's claim/readiness for completion against direct operational checks and, when configured, a separate judge verdict before the loop is accepted.
- Disturbance / variety regulated: a worker can report plausible completion while the actual workspace fails the declared command/test or while a separate judge identifies a material reason to continue/escalate despite a passing direct check.
- Decisive decision or feedback right: after direct working-directory verification, independently choose `accept`, `continue` with corrective specifics, or `escalate` failure.
- Decision owner: the configured supervisor agent; the built-in `arbiter` is explicitly the judge role and may use a distinct model/provider. The direct command check is deterministic evidence/support rather than the autonomous judgment owner.
- Supporting / enforcement mechanisms: `delegate` `until` loop, direct command execution in worker cwd after every turn, no-progress detection, strict verdict parser and worker feedback/retry loop.
- Closure path: worker turn → KOT independently executes declared check in worker cwd → failed check output returns to worker, or passing check reaches supervisor → supervisor verdict `continue` returns specifics to next worker turn, `escalate` fails, `accept` permits completion.
- Boundary reachability: `until` and supervisor are standard documented parameters of the shipped `delegate` operation; `arbiter` is a built-in agent type, so no downstream reviewer implementation is required.
- Why this is / is not agent-owned: deterministic exit-code evaluation supplies complementary operational evidence, while the optional separate supervisor owns the discretionary post-check audit verdict; removing that supervisor removes the independent accept/continue/escalate judgment while leaving the check machinery intact.
- Evidence: `tools/Agent.md`.
- Basis: explicit
- Confidence: high
- Caveats: S3* is established in the supported `delegate`+`until`+supervisor mode; ordinary delegates need not exercise it.
- Claim being audited: that the delegated worker's assigned result satisfies the declared completion condition and is ready to be accepted.
- Ordinary reporting path: worker turns and the delegate's eventual task notification/report.
- Complementary access path: KOT executes the declared command directly in the worker's working directory after each turn; a separate supervisor then receives the passing-gate situation and issues a strict verdict.
- Independence boundary: the check observes workspace behavior outside the worker's self-report, and the supervisor is a separately launched agent/judge that can use a different model/provider and has its own tools/context.
- Who acts on findings: KOT feeds failed-check or `continue` findings into the worker's next turn; `escalate` fails the loop; only `accept` closes completion.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective organizational adaptation loop is established in the shipped KOT boundary.
- Disturbance / variety regulated: external information, prior sessions, persistent notes and available provider/model catalogs can inform current work, but no shipped mechanism closes a future-oriented change to KOT's organizational capability or governing structure.
- Decisive decision or feedback right: not established for S4.
- Decision owner: none established at this boundary.
- Supporting / enforcement mechanisms: Search, History, Memory, model/provider discovery, user model overrides and durable workflows expand/reconfigure current task capability but do not by themselves own adaptation.
- Closure path: no qualifying external/prospective option → adaptation decision → present capability change → subsequent operation loop was found.
- Why this is / is not agent-owned: persistent memory and retrieval carry knowledge forward, but they do not establish a distinct external intelligence function with authority to redesign current organizational capability.
- Evidence: `README.md`; `tools/Memory.md`; `tools/History.md`; `tools/Agent.md`.
- Basis: explicit + structural absence
- Confidence: high
- Caveats: README explicitly positions KOT as a tool that "will not adapt to your process"; user/developer updates to configuration or binaries remain external maintenance rather than a first-party S4 closure.

### Absence scope

- Surfaces inspected: complete shipped tool inventory in README; Agent/provider/model routing; Memory; History; Plan/workflows; Search/tool extensibility descriptions; Web/session lifecycle and repository release boundary.
- Plausible first-party paths checked: self-improvement, automatic skill/tool creation from environmental trends, persistent learned policy/capability mutation, cross-session behavioral adaptation and parent-governed future-capability review.
- Why no material first-party path remains: KOT persists information and exposes current configuration/tool extension, but the documented standard distribution has no closed external-and-prospective adaptation authority returning a decision into changed organizational capability.

## S5 — Policy and identity

- State: —
- Function: no material first-party runtime identity / ultimate-policy closure is established for the KOT organization.
- Disturbance / variety regulated: model/provider/settings, user notes, workflow ask gates and host operating rights constrain individual operation but do not constitute an identity/ultimate-policy issue resolved by legitimate ultimate authority and returned into later operation.
- Decisive decision or feedback right: not established for S5.
- Decision owner: none established at the assessed recursion.
- Supporting / enforcement mechanisms: configuration files, provider/model selection, persistent user-scope Memory notes, workflow ask/escalation and ordinary user control of the host process.
- Closure path: no qualifying identity/ultimate-policy issue → ultimate authority → authoritative policy decision → returned operational governance loop was found.
- Why this is / is not agent-owned: the lead model can select operational resources and record memory but does not own the ultimate right to redefine KOT's organizational identity or governing policy.
- Evidence: `README.md`; `tools/Memory.md`; `tools/Agent.md`.
- Basis: explicit + structural absence
- Confidence: high
- Caveats: KOT intentionally has no built-in sandbox/allow-deny permission regime; generic user configuration, workflow approval and behavioral notes are not promoted to S5.

### Absence scope

- Surfaces inspected: README product-position/security boundary, configuration/model routing, Agent/workflow ask/escalation, Memory user-feedback notes, Plan, Web/session controls and shipped tool inventory.
- Plausible first-party paths checked: agent-owned identity revision, ultimate-policy arbitration, parent-governed policy escalation and persistent authoritative return into subsequent operation.
- Why no material first-party path remains: documented controls are operational settings/context or task-specific human gates. None closes an identity/ultimate-policy function at the declared recursion.

## Recursion

KOT can run children, teams and nested workflows, but nesting is not VSM recursion. The assessed recursion is one lead-session organization with owned child S1 units and its current-control/audit mechanisms. A nested workflow remains an execution structure unless independently evidenced as a complete viable subsystem.

## Variety and escalation

KOT absorbs operational variety through tool choice, multiple providers/models, persistent sessions/history/memory, task DAGs, parallel delegation, worktree isolation, mail/stop/model switching and direct completion checks. Workflow `on_error.action="escalate"` can pause and mail the owner, and `ask` can request a human gate; those are task-level escalation paths and do not automatically create S5. The `until` supervisor escalation belongs to S3* completion audit.

## Evidence gaps

The frozen public repository does not include runtime source code. This limits claims about implementation internals, but the shipped executable and detailed first-party tool contracts establish the public operating surfaces used for all positive mappings above. No undocumented binary behavior is used to upgrade a state. The public tool inventory is broad enough to support the scoped S4/S5 absence conclusions rather than `?`.