---
harness_id: rook
project_name: Rook
repository: https://github.com/martian56/rook
review_ref: 82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0
reviewed_at: 2026-10-22
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Rook

## Review boundary

- System in focus: Rook's released Raven-language terminal coding agent with standard model/tool loop, bundled read-only subagents, optional custom `.agents` resources and permissions, not the unrelated Raven programming language, Aviary model provider or an externally orchestrated user team.
- Purpose and identity: answer user coding requests by inspecting project files, changing code and running tests or shell commands with tool feedback and explicit user approval for risky effects.
- Relevant environment: terminal, user repository, model provider, filesystem, shell and background jobs, model-facing tool results, project/global `.agents` guidance and trusted user decisions.
- Standard-distribution boundary: `src/agent`, `src/agents`, `src/tools`, TUI/headless entrypoints and built-in first-party `explorer`, `reviewer`, `planner` subprocess-like nested conversation runs; optional custom resource definitions distinguished from supplied defaults.
- Credited operating / distribution surfaces: root streamed model/tool loop, `dispatch` with synchronous or parallel first-party read-only child models, tool-result aggregation, project source reads/edits, plan/read-only restriction, background shell supervision, user permission prompts, instruction memory and context compaction.
- Adjacent first-party surfaces excluded from ownership: user-authored `tools: all` agents, external MCP/skills/plugins, host/provider model competence, software project maintainer CI and user instructions that describe a future organization.
- Operating modes considered: terminal interactive and headless, ordinary tool-using models, built-in read-only specialists, opt-in custom subagent definition/model override, parallel dispatch, plan mode, trusted project/global permission rules and automated background shell runs.
- Recursion level: one running Rook coding service and directly delegated specialist units, not the OSS project's development governance or a bespoke multi-agent installation.
- Reviewed revision: [`82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0`](https://github.com/martian56/rook/tree/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0), frozen intake #200.
- Observation date: 2026-10-22; pinned source-inspection assessment; no external model execution.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The native Raven-language `run_turn` builds model input with current messages and tool definitions, streams the model reply, executes selected tools, writes tool results into the conversation, and repeats for at most 25 rounds. For a model call with multiple `dispatch` operations, independent `run_subagent` goroutines execute with their own messages, system prompts, tool subsets and a 15-round cap, then the parent waits and inserts results in original request order. Three first-party built-ins are read-only explorer, reviewer and planner. User-defined agents can ask for broader tool access, but are absent by default. There is no nested further dispatch.

Mutating actions enter the parent/UI permission pathway, and concurrent children queue for user approvals. Approval serialization, ordering and sharing one workspace protect operator consent and transcript consistency, but the implementation supplies no conflict-specific agent-owned arbitration of incompatible child work. Default child agents do not write at all. Reviewer findings concern task code correctness, not an independently audited S3-management claim. Context compaction and `AGENTS.md` notes preserve the present task; tools for web search and background shell feedback do not create prospective S4 strategy or S5 identity authority.

Primary evidence: [root turn loop and fan-out](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/turn.rv#L1-L228), [real nested model/tool execution](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/subturn.rv#L1-L195), [built-in read-only agents](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agents/subagents.rv#L105-L181), [permission model](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/tools/permissions.rv#L1-L88).

## Operational model

A root S1 decides which code/file/shell action or subagent to use next. Read-only child S1 models independently explore/plan/review scoped questions; the root receives final answers, optionally runs mutating tools subject to human approval, and continues. Tool ordering and runtime caps prevent local execution errors, but no separate autonomous S2–S5 loop is demonstrably owned within the shipped organization.

## S1

- State: A
- Function: Resolve a user coding request using model-selected project inspection, code edits, shell commands and optional specialist child investigations with tool-result feedback.
- Disturbance / variety regulated: Unknown code structure, missing implementation details, failing shell commands, conflicting source requirements, provider responses and incomplete child research.
- Decisive decision or feedback right: The root model selects tools, whether to dispatch specialists and corrective next steps; each first-party child selects allowed read/search operations based on its own results.
- Decision owner: Rook's primary `run_turn` model, with genuine nested model-driven specialist operating cells.
- Supporting / enforcement mechanisms: Read/grep/tree/edit/shell tools, `dispatch`, individual child message histories, optional web/MCP tools, background shell feedback, session memory/compaction, model-provider gateway.
- Closure path: User coding request → model tool/child call → result or permission-denial text → recorded conversation → subsequent model decision, up to bounded turn completion.
- Why this is / is not agent-owned: Both root and delegated child models autonomously choose task-level actions from tool observations; user policy is an execution constraint rather than the source of all coding choices.
- Boundary reachability: `run_turn` exposes `tools()` including dispatch and runs `_dispatch` against loaded first-party `builtin_subagents`; root waits for child tool results before the next model call.
- Evidence: [main action-feedback loop](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/turn.rv#L24-L225), [dispatch executed](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/turn.rv#L337-L380), [model-executing nested child](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/subturn.rv#L39-L136), [first-party tool definitions](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/tools/registry.rv#L24-L192).
- Basis: structural.
- Confidence: high for model/tool and bundled child operational wiring; no live-provider assessment result.
- Caveats: Provider must support tools and user can deny mutating calls; claimed real-task success is not measured here.

## S2

- State: —
- Function: Dampen specific conflicts or oscillations between independently viable coding S1 units, returning adjustments that change their subsequent activity.
- Disturbance / variety regulated: Possible simultaneous child reads, incompatible custom child writes, shared working-tree actions and concurrent human approval prompts.
- Decisive decision or feedback right: Built-in child units are all read-only. Optional custom writers share the workspace and individually request UI permission; model-mediated child results and approval queue do not decide/return a conflict-specific cross-agent settlement.
- Decision owner: None for qualifying S2. Parent model dispatches scoped tasks, event/state mutex orders result delivery, and human operator approves write effects.
- Supporting / enforcement mechanisms: Parallel `dispatch` fan-out, tool result order preservation, child read-only tool subset, nonrecursive limit, plan mode and user approval queue.
- Closure path: Children execute independent subtask → parent collects final results in original order → next root coding step. No explicit child interference monitor, coordination decision or adjusted subsequent action across affected S1s.
- Why this is / is not agent-owned: A read-only fan and ordered result collection reduce collisions, but do not establish an adaptive inter-S1 regulation function. Mutating custom agents require external policy/approval without first-party conflict arbitration.
- Evidence: [fan-out join without cross-child adjustment](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/turn.rv#L125-L226), [result ordering](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/turn.rv#L276-L336), [safe default agents and custom tool opt-in](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agents/subagents.rv#L71-L181), [per-child approval/deny](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/subturn.rv#L150-L229).
- Basis: structural.
- Confidence: high about default topology; medium-high for bounded S2 absence when optional custom writers are considered.
- Caveats: A downstream user can coordinate custom agents externally, but this would be an independently assessed organization.

### Absence scope

- Surfaces inspected: default agent roster, custom subagent loading, parallel dispatch, subturn tool gates, result join, user approvals, background shells and plan mode.
- Plausible first-party paths checked: child conflicts, shared files, read-only default, user-enabled child mutation, tool-call ordering, conflicting approvals and root feedback.
- Why no material first-party path remains: Source provides independent task processing, transport and human approval but no concrete adaptive conflict attenuation/feedback function among active S1 cells.

## S3

- State: —
- Function: Regulate whole-current commitments, scarce resources and priorities across the coding service's operating units.
- Disturbance / variety regulated: Numerous coding child tasks, overlapping shell jobs, token/context pressure and pending tool calls.
- Decisive decision or feedback right: Root controls present coding-subtask delegation, but no separate portfolio allocator exists; background shell count and subagent rounds are fixed caps, not whole-current operational bargaining.
- Decision owner: Root S1 model for task decomposition, deterministic limits and user for operating settings; no S3-specific manager established.
- Supporting / enforcement mechanisms: 25-round root cap, 15-round child cap, background shell max-running setting, tool approval, `/plan`, transcripts and checklists.
- Closure path: User task → optional child parallelism and tool execution → results back to root. No distinct whole-system commitments/reallocation based on operational pressure.
- Why this is / is not agent-owned: Subagent delegation and a visible checklist are task-execution support, not separate cross-cell management authority.
- Evidence: [root/child round caps](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/turn.rv#L21-L39), [subturn cap](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/subturn.rv#L21-L43), [background shell resource cap](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/README.md#L193-L219).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A human user can schedule many Rook sessions independently; no shared management instance is part of this distribution.

### Absence scope

- Surfaces inspected: root run, children, shell supervisors, `/plan`, todos, local session and configurable resource limits.
- Plausible first-party paths checked: cross-child priorities, budget negotiations, competing coding obligations, shell resource interventions and session-level management.
- Why no material first-party path remains: The root delivers one request and enforces static local limits, without separate whole-current portfolio/commitment authority.

## S3*

- State: —
- Function: Independently challenge and correct S3 management's actual operating view from a complementary evidence source.
- Disturbance / variety regulated: Incorrect source edits, failed code review, bad assumptions and misleading tool transcript summaries.
- Decisive decision or feedback right: The built-in `reviewer` critiques requested code, not a distinct S3 current-resource/commitment decision; the parent chooses whether to act on findings.
- Decision owner: Task-local reviewer model within dispatched S1 work, no independent S3* auditing rights.
- Supporting / enforcement mechanisms: Reviewer prompt, explorer source reads, code/tool outputs, developer tests, git diff, rewind checkpoints.
- Closure path: Parent asks reviewer to inspect patch → child returns findings → parent may revise code. No S3 operating claim → independent reality audit → corrected S3 control loop.
- Why this is / is not agent-owned: Code-review separation is real, but its function and target are local implementation quality, not complementary audit of whole-current management.
- Evidence: [bundled reviewer definition](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agents/subagents.rv#L121-L156), [child result returned to root](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/turn.rv#L336-L379), [child read-only tool caps](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/subturn.rv#L146-L185).
- Basis: structural.
- Confidence: high about reviewer task scope, medium-high for no S3* closure.
- Caveats: Custom reviewers may address other claims, but must establish independent managerial audit evidence first.

### Absence scope

- Surfaces inspected: default reviewer and planner, tool transcripts, git reads, source-test outputs, root decisions and custom definitions.
- Plausible first-party paths checked: adversarial code review, progress reports, independent evidence of managerial state and authority to correct S3 allocations.
- Why no material first-party path remains: There is no operative whole-current S3 to audit, and the shipped reviewer returns code-quality findings only.

## S4

- State: —
- Function: Sense changing future environment, develop adaptation alternatives and return adopted capabilities to S3.
- Disturbance / variety regulated: Changing model/provider availability, evolving project practices, new requirements and future developer workflows.
- Decisive decision or feedback right: Web tools operate on demand during current tasks; model selection, plugin install and `.agents` guidance are human-selected; no standing external-future intelligence/adoption loop.
- Decision owner: Human for provider/skills/plugins/settings; root coding S1 for task investigation, not S4 adaptation.
- Supporting / enforcement mechanisms: Web search/fetch, dynamic skills/commands and source notes, provider list, automatic context compaction, background logs and hooks.
- Closure path: Current prompt → task research/tools or context summary → next coding step; no future change detection → alternative capability design → S3 installation path.
- Why this is / is not agent-owned: Loading tools and summarizing previous turns maintains one task, not a prospective adaptive strategy over an external environment.
- Evidence: [runtime context compaction](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/compact.rv#L1-L75), [memory instruction import](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agents/memory.rv#L1-L65), [web and skill tools](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/tools/registry.rv#L145-L187).
- Basis: structural.
- Confidence: medium-high.
- Caveats: A user may task Rook with future research; that is episodic S1 unless standing S4 rights and return are evidenced.

### Absence scope

- Surfaces inspected: web/tools, memory, context compaction, plugin loading, provider selector, background shell feedback and optional skills.
- Plausible first-party paths checked: external-environment scan, long-range strategy, automatic tool/protocol adaptation, model selection and ongoing capability promotion.
- Why no material first-party path remains: No ongoing prospective external-future option/adoption loop is bundled; existing feedback is local coding-session continuity.

## S5

- State: —
- Function: Legitimately set the coding organization's ultimate purpose and values and send binding governance to operative units.
- Disturbance / variety regulated: Dangerous commands, unauthorized changes, untrusted `.agents` resource instructions, conflicting operator preferences and unsafe model proposals.
- Decisive decision or feedback right: The human operator initiates goals, grants/denies mutating tools and selects model/permission policy. User/project settings may constrain agents but agents lack legitimate final-purpose authority.
- Decision owner: Human operator, project/global trust settings and deterministic permission gate, not a first-party S5 model.
- Supporting / enforcement mechanisms: Allow/deny/ask permission rules, trusted config roots, plan mode, parent approval prompt and subagent tool allowlists.
- Closure path: User instructions and settings → tool preflight/request for consent → allow/deny tool effect. No agent-originated supreme value adjudication with governing return to the whole system.
- Why this is / is not agent-owned: The model chooses particular coding actions while final purpose and permitted autonomy are externally specified.
- Evidence: [deny-overrides-allow gate](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/tools/permissions.rv#L1-L89), [parent approval path](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/turn.rv#L403-L463), [child permission inheritance](https://github.com/martian56/rook/blob/82d7b94231fbcd9ff280e223b2d14ddcaf72c6e0/src/agent/subturn.rv#L155-L224).
- Basis: structural.
- Confidence: high on human final authority.
- Caveats: User granting `tools: all` broadens child operational power but does not transfer legitimate identity or policy ownership.

### Absence scope

- Surfaces inspected: initial user task, project/global permissions, trusted settings, plan mode, child allowlists, UI approvals and instruction memory.
- Plausible first-party paths checked: legitimate purpose setting, prompt role constraints, refusal/approval controls, future goals and project-level policy authority.
- Why no material first-party path remains: First-party decisions are about fulfilling user coding requests under externally set rules; no final values/identity adjudicator is present.

## Distributed OSS parent arrangement

Open-source code, tests and contributors maintain the product, but no shipped operational S3/S4/S5 function is credited from repository activity. Installed plugins and custom agent definitions can change available workers, yet their self-authored coordination is an external assembly.

## Self-hosted and non-human modes

The binary can use multiple providers or a self-hosted model endpoint. Main and built-in child agents run autonomously within tool constraints, with mutating work still gated by a human except preapproved trusted rules. A model lacking tool support may answer but cannot establish the reviewed coding S1 tool closure in that mode.

## Recursion

The main coding loop and each read-only specialist have independent model/tool steps. Parallel fan-out is a task decomposition relation at this level; ordered tool-result collection does not acquire a separate S2 conflict-settlement function. Individual shell actions and context summaries operate within an S1 cell.

## Variety and escalation

Subagents return scoped reports; parent tool results and approval denials inform subsequent model steps. Shell status can be polled, and max rounds constrain runaway execution. Strongest escalation is an operator permission prompt, not whole-current management, prospective adaptation or ultimate policy.

## Evidence gaps

- Exact frozen-source review only; no external model/provider run, parallel-writer collision test or human-approved edit executed.
- Custom agents may request `tools: all` but are not automatically configured in the first-party standard roster; their behavior depends on user-provided definitions.
- Provider success, safety, tool-call reliability and runtime quality are not inferred from README claims.
