---
harness_id: forge-agent
project_name: Forge Agent
repository: https://github.com/guoyang1982/forge-agent
review_ref: 9ee359b8f5a1cd172ad358b357238d2174dee12b
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-15
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Forge Agent

## Review boundary

- System in focus: first-party native Forge Agent runtime in the shipped desktop/CLI daemon, not Codex, Claude Code or Cursor integrations selected from the same UI.
- Purpose and identity: local-first interactive coding with project context, guarded edits, tests and optional read-only parallel research agents and reflection.
- Standard-distribution boundary: packaged Forge Agent runReActLoop via the daemon/CLI, optional read-only subagents and configured reviewer reflection; external agent adapters and product team excluded.
- Relevant environment: workspace/files, models/tools, test and shell results, user permissions and child outcomes.
- First-party operating modes considered: native ReAct multi-step coding, subagent research, single-writer changes, optional reviewer profile.
- Recursion: main Forge model/tool loop with independent but read-only child loops; shared daemon session and workspace.
- Frozen ref 9ee359b8f5a1cd172ad358b357238d2174dee12b, Profile 0.2.4 / Methodology 0.3.7.
- Credited operating / distribution surfaces: packages/agent-core/src/loop.ts; apps/daemon/src/services/run-service.ts; native packages/tools; supported CLI and desktop invocation, reflection.ts with configured optional review.
- Adjacent first-party surfaces excluded from ownership: third-party Codex/Claude/Cursor agent adapters; separate user-controlled talent definitions, future roadmap, CI/tests, UI presentation alone, release maintainer governance.


## Repository architecture

Native packages/agent-core/src/loop.ts exports runReActLoop, executing bounded model/tool observations and subsequent model decisions with permissions and tool result records. apps/daemon/src/services/run-service.ts constructs first-party spawnSubagent by invoking a fresh runReActLoop with read-only allowTool and returns subagent final content to the main run; comments explicitly establish single-writer architecture to avoid concurrent filesystem mutation, rather than distributed write negotiation. packages/agent-core/src/reflection.ts optionally runs a reviewerProfile (or the same active model) on final prose and summarized failure tools, with blocker nudges and finite rounds. packs/execution provide runtime run controls. External Codex, Claude Code and Cursor agent integration must not donate their autonomous loops to Forge.

## Operational model

The native model iteratively selects code edits/search/commands under the daemon's tool guards; tool results return for subsequent steps. In supported subagent mode the same first-party ReAct loop runs independently for read-only children and returns text to parent which alone writes shared files. Optional reflection can prompt same-task correction from final-answer and failed-tool summaries; it is ordinary in-band QA rather than independently sourced complementary organizational audit.

## S1 — Operations

- State: A
- Function: Execute adaptive coding tasks through repeated first-party model decisions over tools and results.
- Disturbance / variety regulated: Changing repository/tool state, delegated work results and authority conditions.
- Decisive decision or feedback right: Respond to function-specific feedback by changing subsequent operational action.
- Decision owner: Shipped Forge Agent runReActLoop model actor and daemon/CLI, not borrowed Codex/Claude/Cursor adapter agents.
- Supporting / enforcement mechanisms: runReActLoop, tool dispatch with bounded steps, shared workspace guard, tool outputs and persisted session events.
- Closure path: User coding task → native model/tool choices → guarded tool result → subsequent model call and possible fixes → answer or bounded stop.
- Why this is / is not agent-owned: The model actively chooses and revises code/tool actions; deterministic permissions limit rather than supply those choices.
- Boundary reachability: The declared first-party packaged CLI or runtime directly exposes and runs the described mode without borrowing any external agent task loop.
- Evidence: [packages/agent-core/src/loop.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/packages/agent-core/src/loop.ts); [apps/daemon/src/services/run-service.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/apps/daemon/src/services/run-service.ts); [packages/tools/src/index.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/packages/tools/src/index.ts); [README.md](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/README.md).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: high.
- Caveats: This is a source-bounded structural assessment of standard modes, not a claim about quality or future integrations.

## S2 — Coordination

- State: ?
- Function: Attenuate interference between distinct model-running subagents and a single mutable shared workspace.
- Disturbance / variety regulated: Changing repository/tool state, delegated work results and authority conditions.
- Decisive decision or feedback right: Respond to function-specific feedback by changing subsequent operational action.
- Decision owner: Daemon implements single-writer admission; the parent model receives child textual results. A distinct adaptive inter-S1 conflict mediator remains unproven.
- Supporting / enforcement mechanisms: spawnSubagent executes own model/tool loop with allowTool restricted to read_file/list_dir/grep/echo; main agent handles writes; concurrency-safe read/tool batches.
- Closure path: Parent spawns read-only children → independent observations/answers returned → parent controls edits. This prevents concurrent child writes by construction but does not evidence dynamically diagnosing concrete conflicting child work and rescoping multiple S1s.
- Why this is / is not agent-owned: Read-only child ReAct loops plus single-writer main agent are a real interference-avoidance design, but no model-owned conflict event → revised inter-child coordination loop is shown.
- Evidence: [apps/daemon/src/services/run-service.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/apps/daemon/src/services/run-service.ts); [packages/agent-core/src/loop.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/packages/agent-core/src/loop.ts); [packages/tools/src/index.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/packages/tools/src/index.ts).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: unresolved.
- Caveats: This is a source-bounded structural assessment of standard modes, not a claim about quality or future integrations.

## S3 — Inside-and-now control

- State: —
- Function: Govern whole-current active subordinate S1 tasks and resource obligations with discretionary intervention.
- Disturbance / variety regulated: Changing repository/tool state, delegated work results and authority conditions.
- Decisive decision or feedback right: Respond to function-specific feedback by changing subsequent operational action.
- Decision owner: No independent first-party actor with this complete function-specific authority is established in the shipped mode.
- Supporting / enforcement mechanisms: Bounded run/session state, model/tools, events, policy gates and operator decisions.
- Closure path: A bounded part of the path exists, but function-specific ownership and decision return are not fully demonstrated.
- Why this is / is not agent-owned: Single-session limits and event timelines report execution; distinct whole-current delegated-work resource/priority controller is not proven.
- Evidence: [apps/daemon/src/services/run-service.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/apps/daemon/src/services/run-service.ts); [packages/agent-core/src/loop.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/packages/agent-core/src/loop.ts); [packages/execution/src/forge-agent-adapter.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/packages/execution/src/forge-agent-adapter.ts).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: This is a source-bounded structural assessment of standard modes, not a claim about quality or future integrations.

### Absence scope

- Surfaces inspected: daemon live run records, ReAct max steps, child progress events, optional talents and dispatch DAG.
- Plausible first-party paths checked: parent spawning read-only children as a whole-system controller, talents/dag dispatch, user dashboard controls.
- Why no material first-party path remains: task orchestration/run caps do not demonstrate model-owned whole-current portfolio feedback and returned resource/commitment intervention across live S1s.

## S3* — Complementary audit

- State: —
- Function: Complementary independent audit of current operational reports with a returned corrective judgment to S3.
- Disturbance / variety regulated: Changing repository/tool state, delegated work results and authority conditions.
- Decisive decision or feedback right: Respond to function-specific feedback by changing subsequent operational action.
- Decision owner: No independent first-party actor with this complete function-specific authority is established in the shipped mode.
- Supporting / enforcement mechanisms: Reflection gate, optional reviewerProfile (same-model fallback), collectToolEvidence failed-tool summary, limited rounds, fail-open reviewer errors.
- Closure path: Candidate final text and failure snippets → optional reviewer verdict → possible same-task model nudge. Not a complementary independent S3 organizational challenge of direct evidence.
- Why this is / is not agent-owned: Optional reflection model sees candidate answer and a compact summary of failed tool messages; it judges routine task completeness and may nudge rework but lacks independent raw-artifact reality inspection or corrective S3 authority.
- Evidence: [packages/agent-core/src/reflection.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/packages/agent-core/src/reflection.ts); [packages/agent-core/src/loop.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/packages/agent-core/src/loop.ts); [apps/daemon/src/services/run-service.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/apps/daemon/src/services/run-service.ts).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: This is a source-bounded structural assessment of standard modes, not a claim about quality or future integrations.

### Absence scope

- Surfaces inspected: reflection configuration, reviewer prompt/evidence, normal ReAct loop, daemon session logs and optional review workflow.
- Plausible first-party paths checked: optional separate reviewerProfile, review talent/child, change timeline and QA/test output.
- Why no material first-party path remains: the active reviewer inspects task-level answer and failure snippets without an independent audit of operational reality and a returned S3 current-control decision.

## S4 — Outside-and-then intelligence

- State: —
- Function: Sense future external conditions and adapt Forge's strategic operating capabilities.
- Disturbance / variety regulated: Changing repository/tool state, delegated work results and authority conditions.
- Decisive decision or feedback right: Respond to function-specific feedback by changing subsequent operational action.
- Decision owner: No independent first-party actor with this complete function-specific authority is established in the shipped mode.
- Supporting / enforcement mechanisms: Bounded run/session state, model/tools, events, policy gates and operator decisions.
- Closure path: A bounded part of the path exists, but function-specific ownership and decision return are not fully demonstrated.
- Why this is / is not agent-owned: Agent planning/review, skills and automation are current task aids or user configuration, not autonomous external future strategy selection and promotion.
- Evidence: [packages/agent-core/src/loop.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/packages/agent-core/src/loop.ts); [apps/daemon/src/services/run-service.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/apps/daemon/src/services/run-service.ts); [README.md](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/README.md).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: This is a source-bounded structural assessment of standard modes, not a claim about quality or future integrations.

### Absence scope

- Surfaces inspected: current run orchestration, provider/skill/tool extensibility, long-memory and automation interfaces.
- Plausible first-party paths checked: automatic skill extension, model self-improvement, external threat or ecosystem sensing.
- Why no material first-party path remains: future choices remain product maintainer/operator tasks and no prospectively owned sensing → option → capability adoption feedback path is established.

## S5 — Policy and identity

- State: —
- Function: Legitimately decide ultimate shared purpose and binding identity/policy disputes.
- Disturbance / variety regulated: Changing repository/tool state, delegated work results and authority conditions.
- Decisive decision or feedback right: Respond to function-specific feedback by changing subsequent operational action.
- Decision owner: No independent first-party actor with this complete function-specific authority is established in the shipped mode.
- Supporting / enforcement mechanisms: Bounded run/session state, model/tools, events, policy gates and operator decisions.
- Closure path: A bounded part of the path exists, but function-specific ownership and decision return are not fully demonstrated.
- Why this is / is not agent-owned: User/operator supplied permission presets, patch gates and confirmation prompts enforce existing authority rather than resolve ultimate organizational policy disputes.
- Evidence: [packages/agent-core/src/loop.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/packages/agent-core/src/loop.ts); [packages/tools/src/index.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/packages/tools/src/index.ts); [apps/daemon/src/services/run-service.ts](https://github.com/guoyang1982/forge-agent/blob/9ee359b8f5a1cd172ad358b357238d2174dee12b/apps/daemon/src/services/run-service.ts).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: This is a source-bounded structural assessment of standard modes, not a claim about quality or future integrations.

### Absence scope

- Surfaces inspected: tool permissions, workspace guards, confirmation dialogs, daemon user session controls.
- Plausible first-party paths checked: model override of tool policy, UI approvals as institutional purpose decisions, release maintainer governance.
- Why no material first-party path remains: these rights concern specific tool execution under existing configuration, not institutionally legitimate purpose conflict → binding changed policy return.

## Distributed OSS parent arrangement

Operators of native Forge and public source maintainers do not share one first-party governing model. Integrated third-party coding engines keep their own autonomy and policy authorities, which are not credited.

## Self-hosted and non-human modes

Local daemon/CLI native model and tools implement S1. Optional child loops are read-only single-writer research workers; configured external agent providers may be separate autonomous products but cannot supply missing first-party S2-S5 ownership.

## Recursion

One root coding ReAct session and optional independently iterating read-only child research loops. This creates plausible inter-S1 coordination challenges but no proven returned adaptive conflict management or whole-current governing metasystem.

## Variety and escalation

Changing files/test results affect the native next model action. Workspace/tool permission gates, human network/shell confirmation and reviewer blocker nudges constrain operation. These are not S5 or S3* by name.

## Evidence gaps

Source-first structural review only; no live paid-provider benchmark. Actual read-only child overlap avoidance is evidenced, while an agent-owned cross-child feedback/rescope loop is not; S2 remains ?. Reviewer considers textual completion and failed-tool excerpts, not direct independent artifact audit; S3*=—.

## Assessment summary

**Proposed included**, VSM `S1=A / S2=? / S3=— / S3*=— / S4=— / S5=—`. The native Forge ReAct loop is first-party; third-party integrated coding agents are not borrowed and safety/review labels do not establish organizational metasystems.

