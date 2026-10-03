---
harness_id: pasclaude
project_name: PasClaude
repository: https://github.com/seanrobertwright/PasClaude
review_ref: 9ea5295a10fcdd6343e2a0e2012aab4790136488
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# PasClaude

## Review boundary

- System in focus: the first-party PasClaude Free Pascal coding-agent runtime at frozen revision 9ea5295a10fcdd6343e2a0e2012aab4790136488, including its model/tool loop, built-in coding tools, permission/path/sandbox enforcement, durable session/rewind/compaction state, synchronous read-only task subagent, SDK/headless entry points, and supported read-only GitHub-mention automation.
- Purpose and identity: perform software-engineering work in a selected project by turning user intent and repository evidence into model-selected reads, searches, edits and commands, then returning tool results to the model until it answers or the run stops.
- Relevant environment: the user request, selected repository and allowed directories, filesystem/source/build/test state, shell processes, model/provider responses, operator permissions, persisted session/context state, optional first-party skills/hooks/plugins, and supported external information/tool interfaces.
- Standard-distribution boundary: PasClaude's TAgent loop, uTools built-ins, permission modes and deny rules, path guards, sandbox/job control, session/resume/rewind/compaction, subagent implementation, SDK/stream-json/headless interfaces and shipped GitHub-mention template are inside. Anthropic/model services, GitHub services and external MCP server implementations are dependencies and cannot donate organizational functions.
- Credited operating / distribution surfaces: README.md; src/uAgent.pas; src/uTools.pas; src/uSdk.pas; src/uSandbox.pas; src/uHooks.pas; src/uMcp.pas; src/uCi.pas; src/pasclaude.lpr; examples/embed.lpr; examples/github/pasclaude-mention.yml.
- Adjacent first-party surfaces excluded from ownership: repository unit/fuzz/network/UX tests, build/test scripts, comparison/roadmap documents and contributor/development activity. They may corroborate implementation properties but do not own runtime VSM functions. External provider inference, GitHub authorization/event delivery/comment posting and external MCP programs are also excluded as organizational owners.
- First-party operating / deployment modes considered: interactive REPL in ask, plan, accept-edits and session bypass modes; scripted -p and stream-json/SDK runs including --dangerously-skip-permissions; synchronous task subagent use; background shell jobs; local /review; and the shipped read-only GitHub mention workflow.
- Recursion level: one PasClaude coding session around one selected project/task is the assessed organization. Tool calls, background OS processes and deterministic safety mechanisms are components rather than independent S1 units. The nested task agent is a bounded synchronous read-only helper; even if treated as a subordinate operational unit, the reviewed distribution does not compose a concurrent multi-S1 organization around it.
- Reviewed revision: 9ea5295a10fcdd6343e2a0e2012aab4790136488.
- Observation date: 2026-10-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

PasClaude owns a Free Pascal model/tool loop over the Anthropic Messages API. The model receives system/project context and tool declarations, chooses a built-in or approved extension tool, receives each tool_result, and may continue until it returns a final response. Built-ins cover repository reads/search, edits, notebook edits, shell execution, background-process polling/termination, fetch, task tracking, skills and a nested read-only task agent.

Side effects are governed separately from the model's operational judgment. Paths are constrained to the session root and explicit added roots; deny rules sit above permission grants; plan structurally blocks mutating tools; ask can grant once/always; and bypass can make the coding loop unattended while deny/path/subagent boundaries remain. Sandbox/job objects constrain spawned processes but do not choose the coding action.

Session state is durable and recoverable through autosave, resume/continue, named saves, edited-file snapshots for rewind, changed-file/background-job state and context compaction. These preserve one coding loop rather than establish separate higher VSM functions.

The task tool launches one nested agent synchronously inside the parent's tool call. It gets its own conversation but only read_file, list_dir and search, is depth/round bounded, and returns one final answer. The shipped GitHub-mention workflow is intentionally read-only: CI preparation/reporting are deterministic, the actual model step is an ordinary -p --permission-mode plan --no-project-context run, and the workflow can post one comment but cannot patch, push, approve or merge.

Primary evidence:

- [README.md](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/README.md)
- [src/uAgent.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uAgent.pas)
- [src/uTools.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uTools.pas)
- [src/uSdk.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uSdk.pas)
- [src/uSandbox.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uSandbox.pas)
- [src/uCi.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uCi.pas)
- [examples/github/pasclaude-mention.yml](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/examples/github/pasclaude-mention.yml)

## Operational model

A turn begins with user intent plus current transcript/project context. The model chooses a tool or answer. Tool calls pass first-party validation, path and permission policy, execute through PasClaude, and return typed results to the same conversation. The model observes those results and chooses the next action. In interactive modes a human may gate a side effect; in explicit bypass/unattended mode the same model-owned coding decisions proceed without per-action parent approval.

## S1 — Operations

- State: A
- Function: perform environment-facing coding work in the selected project by inspecting repository state, choosing task-specific reads/edits/commands, observing results and iterating toward a response or completed change.
- Disturbance / variety regulated: heterogeneous source/build/test state, ambiguous implementation choices, search evidence, command outcomes, edit failures, long-session context pressure, asynchronous command progress and user task changes.
- Decisive decision or feedback right: choose the next task-specific repository/tool action and integrate returned evidence into later coding decisions and the final answer.
- Decision owner: the model-backed PasClaude coding actor. Interactive modes may parent-gate side effects; explicit bypass/unattended mode establishes model ownership of the operational action sequence without per-action parent approval.
- Supporting / enforcement mechanisms: built-in tool dispatch, path-root guard, deny rules, permission modes, sandbox/job objects, provider transport/retries, session persistence, rewind snapshots, compaction, background-job registry and tool/subagent bounds.
- Closure path: user task/current context → model selects tool/action → first-party validation and permission enforcement → tool executes → tool_result/environment evidence returns to model → next action or final response.
- Boundary reachability: the shipped REPL directly instantiates this loop, while -p --dangerously-skip-permissions and SDK surfaces expose the same first-party loop as an explicitly unattended supported mode; no external coding-agent runtime is required.
- Why this is / is not agent-owned: removing the model actor while retaining permissions, sandbox, persistence and tools leaves enforcement/callable primitives but removes the open-ended judgment that selects and sequences task-specific coding actions.
- Evidence: [README.md](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/README.md); [src/uAgent.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uAgent.pas); [src/uTools.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uTools.pas); [src/uSdk.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uSdk.pas).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: default interactive operation can parent-gate mutations and deterministic boundaries can refuse model choices, but those mechanisms constrain execution rather than supply the model's open-ended coding decision.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 coordination function was established at the selected recursion.
- Disturbance / variety regulated: not established because the standard session exposes no multiple concurrently interacting coding S1s with a concrete conflict/oscillation requiring attenuation.
- Decisive decision or feedback right: not established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: synchronous task helper, subagent depth/round caps, read-only subagent allowlist, background-job registry, permission gates and shared root/path rules regulate bounded execution but do not coordinate a population of interacting S1 units.
- Closure path: not applicable; no distinct-S1 disturbance → coordination response → changed subsequent S1 behaviour loop was found.
- Why this is / is not agent-owned: the parent can delegate one investigation, but the helper runs one-at-a-time synchronously and cannot mutate the workspace. Background shell jobs are tools/processes, not autonomous coding S1s.
- Evidence: [README.md](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/README.md); [src/uTools.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uTools.pas); [src/uAgent.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uAgent.pas).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: the nested helper has its own conversation, but its synchronous read-only construction still supplies no concrete multi-S1 interference/attenuation relation.

### Absence scope

- Surfaces inspected: main agent loop; task subagent construction/tool limits; background shell jobs; tool registry; permission/path/sandbox machinery; SDK session constraints; GitHub mention mode.
- Plausible first-party paths checked: concurrent subagents, writable worker teams, shared-workspace collision control, parent/subagent mutual adjustment, background jobs as workers, multiple SDK sessions and mention-triggered runs.
- Why no material first-party path remains: the reviewed distribution has one primary coding actor plus one synchronous read-only helper and no coordinated set of simultaneously environment-facing S1s or mechanism tied to a specific inter-S1 disturbance.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-current organizational control function distinct from one coding S1 and deterministic runtime safeguards was established.
- Disturbance / variety regulated: not established at S3 level; located controls regulate one session/tool loop rather than current commitments/resources across an operational population.
- Decisive decision or feedback right: not established. The model can create/poll/kill background commands and delegate one investigation, while operator/runtime controls permissions and bounds, but none is whole-system current management across S1 units.
- Decision owner: not established.
- Supporting / enforcement mechanisms: todo display state, background-job IDs/status/kill, permission modes, deny rules, sandbox/job limits, session status, context compaction and subagent bounds.
- Closure path: not applicable; no whole-system current view → substantive resource/commitment/prioritization decision → organization-wide operational change loop was found.
- Why this is / is not agent-owned: model decisions around commands, todos and one nested investigation remain S1 task execution. Deterministic controls enforce code/operator-selected limits rather than supply an agent-owned S3 manager.
- Evidence: [README.md](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/README.md); [src/uTools.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uTools.pas); [src/uSdk.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uSdk.pas).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: PasClaude has substantial current-state observability/enforcement, but the Profile requires whole-current organizational control rather than a feature named status, jobs, plan or permissions.

### Absence scope

- Surfaces inspected: todos/status, background jobs, permission/deny modes, subagent delegation, SDK session state, context management, CI/headless modes and runtime diagnostics.
- Plausible first-party paths checked: parent agent as manager, job kill/status as commitment control, todo portfolio view, subagent delegation, session supervisor, CI controller and deterministic permission/sandbox controller.
- Why no material first-party path remains: located decisions either choose work inside one coding S1 or enforce operator/developer-selected constraints. No first-party actor governs a whole operational population's current commitments/resources.

## S3* — Complementary audit

- State: —
- Function: no material complementary and sufficiently independent audit path with corrective return into ordinary PasClaude operation was established.
- Disturbance / variety regulated: not established at S3* level.
- Decisive decision or feedback right: not established. /review sends a local diff to the same model-backed coding actor; tests/diagnostics and GitHub mention execution are validation/support or separate read-only runs rather than an independent auditor whose judgment feeds current control.
- Decision owner: not established.
- Supporting / enforcement mechanisms: /review, /pr-comments, tests, /doctor, CI prepare/report parsing, read-only GitHub mention execution and tool-result evidence.
- Closure path: not applicable; no complementary independent access → audit judgment → corrective-control return path is wired into the normal coding session.
- Why this is / is not agent-owned: a second prompt to the same operational actor is self-review, not an independent audit owner. CI preparation/reporting are deterministic safety functions, and mention mode answers a request rather than auditing another live PasClaude S1.
- Evidence: [README.md](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/README.md); [src/uCi.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uCi.pas); [examples/github/pasclaude-mention.yml](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/examples/github/pasclaude-mention.yml).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: local review, diagnostics and CI hardening are useful checks, but independence plus corrective closure required for S3* is absent.

### Absence scope

- Surfaces inspected: /review; pull-request comment ingestion; tests/diagnostics; CI prepare/report; GitHub mention template; coding loop/tool-result feedback; session/rewind evidence.
- Plausible first-party paths checked: separate reviewer/judge agent, independent diff evaluator, protected CI audit returned to a live session, mention-mode audit, test/doctor verdicts as complementary access.
- Why no material first-party path remains: checks remain in the same actor/operational evidence path or are adjacent executions with no audit verdict wired back into current PasClaude control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material external-and-prospective organizational adaptation loop was established in the supported runtime.
- Disturbance / variety regulated: not established at S4 level.
- Decisive decision or feedback right: not established. The model may fetch/search external information and the runtime may enumerate models, but these support the current task/session rather than generate and adopt future-oriented changes to PasClaude capability/strategy.
- Decision owner: not established.
- Supporting / enforcement mechanisms: optional fetch/web search, live model listing, skills/plugins, session compaction, project memory/instructions and external tool integrations.
- Closure path: not applicable; no external/future sensing → adaptation option → change to current organizational capability/control loop was found.
- Why this is / is not agent-owned: external information is ordinary S1 task evidence. Model selection and skill/plugin enablement are operator/runtime configuration, not an autonomous prospective adaptation program.
- Evidence: [README.md](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/README.md); [src/uAgent.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uAgent.pas); [src/uTools.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uTools.pas).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: web access and extensibility increase present-task variety absorption without satisfying outside-and-then adaptation.

### Absence scope

- Surfaces inspected: web/fetch integration; live model discovery; skills/plugins/MCP; project/user memory; compaction; mention automation; configuration and session continuation.
- Plausible first-party paths checked: autonomous model/provider adaptation, future-state planning, self-improvement, learned policy/configuration changes, external trend sensing, plugin/skill acquisition and CI-driven capability change.
- Why no material first-party path remains: external sensing/extension is used for current work or selected by an operator. No first-party runtime loop turns prospective distinctions into adopted organizational changes returned to current control.

## S5 — Identity and ultimate policy

- State: —
- Function: no material identity/ultimate-policy decision-and-return function was established at the selected PasClaude-session recursion.
- Disturbance / variety regulated: not established at S5 level.
- Decisive decision or feedback right: not established. Deny rules, permission modes, project instructions, hook/MCP trust prompts and system-prompt configuration bound execution but do not form an identity/ultimate-policy deliberation closed by legitimate S5 authority.
- Decision owner: not established.
- Supporting / enforcement mechanisms: deny rules, mode selection, persisted narrow approvals, session bypass, path boundary, project-context toggle, hook/MCP trust, sandbox configuration and prompt construction.
- Closure path: not applicable; no identity/ultimate-policy issue → legitimate authority decision → returned governance of subsequent organization path was found.
- Why this is / is not agent-owned: the model cannot lift deny/path/subagent boundaries or leave plan mode by tool call. Human choices around permissions, model, roots and extensions are operational authorization/configuration rather than an explicit identity/purpose governance loop.
- Evidence: [README.md](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/README.md); [src/uTools.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uTools.pas); [src/uSdk.pas](https://github.com/seanrobertwright/PasClaude/blob/9ea5295a10fcdd6343e2a0e2012aab4790136488/src/uSdk.pas).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: PasClaude has strong policy/trust boundaries, but constraints and ordinary human approval are not S5 without identity/ultimate-policy closure.

### Absence scope

- Surfaces inspected: permission modes, deny rules/approvals, path/sandbox policy, project/user instructions, model selection, roots, hook/MCP trust, CI security floor, SDK project-context decisions and persisted configuration.
- Plausible first-party paths checked: autonomous policy revision, parent-governed identity decision, constitutional/purpose change, operator approval escalation, project instructions as ultimate authority, trusted extension decisions and model choice as identity policy.
- Why no material first-party path remains: the distribution enforces or accepts externally selected operational constraints but exposes no first-party identity/ultimate-policy issue → decision → returned governance loop.

## Recursion, variety, escalation and unresolved evidence

- Recursion: one PasClaude coding session is the assessed organization. task can create one nested read-only investigation agent, but it runs synchronously inside the parent tool call and does not create a coordinated worker population at this boundary.
- Variety: repository/source state, task ambiguity, model proposals, search evidence, edit/command outcomes, asynchronous command progress, context growth, permission outcomes, extension tools and session failures are absorbed primarily by S1 plus deterministic supporting machinery.
- Escalation: mutating/tool-trust questions can escalate to the operator; denials/plan boundaries return errors to the agent; bypass removes per-action approval while preserving hard boundaries. These operational safety paths are not automatically S3/S4/S5.
- Unresolved evidence: no material evidence gap remained that required ?. Positive credit is limited to the first-party coding loop; review, CI, policy, persistence and extension mechanisms were not promoted without required closure.

## Assessment vector

**A · — · — · — · — · —**
