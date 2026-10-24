---
harness_id: agent-code
project_name: Agent Code
repository: https://github.com/avala-ai/agent-code
review_ref: 2734ab5f18939b20c774b39c4406788383e35255
reviewed_at: 2026-10-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Agent Code

## Review boundary

- System in focus: the first-party Agent Code Rust coding-agent execution engine (`agent-code-lib`) in supported CLI/headless/TUI/HTTP/ACP product operation, including optional built-in `Agent` subagent tool and separately invoked `agent security-scan` MapReduce.
- Purpose and identity: carry out model-directed repository coding work through local tools; optional first-party scan inspects a repository for possible security defects.
- Relevant environment: the operator's local repository, operating-system shell, configured provider endpoint and permissions, persistent sessions, optional project/user agent definitions, worktrees and third-party MCP resources.
- Standard-distribution boundary: shipped Rust engine and supported native client entrypoints, builtin agent definitions, local task manager, the direct `security-scan` CLI. External CI/benchmark consumers, authored custom multi-agent workflows, third-party providers, independently managed editor organizations and human GitHub reviews are excluded.
- Credited operating / distribution surfaces: [README.md](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/README.md); [ARCHITECTURE.md](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/ARCHITECTURE.md); [mod.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/query/mod.rs); [agent.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/agent.rs); [coordinator.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/services/coordinator.rs); [send_message.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/send_message.rs); [executor.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/tasks/executor.rs); [executor.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/executor.rs); [mod.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/amr/mod.rs); [orchestrator.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/amr/orchestrator.rs); [security_scan.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/cli/src/security_scan.rs); [mod.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/permissions/mod.rs); [consolidation.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/memory/consolidation.rs).
- Adjacent first-party surfaces excluded from ownership: `crates/eval` benchmark execution, PR/release CI, developer test fixtures, third-party MCP/tools, user-authored custom agent scripts/manifests, operator review/merge decisions. A separate invoked security-scanner workflow is considered, but its output is not presumed to be a corrective governance decision by the coding agent.
- First-party operating / deployment modes considered: default model→tools coding turn, `Agent` invocation with built-in `general-purpose`, `explore`, `plan` subagent roles and optional worktree isolation, headless/interactive entrypoints, standalone first-party `security-scan` with deterministic SHARD/BATCH and agentic MAP/REDUCE.
- Recursion level: primary coding agent with model-running subordinate task agents when invoked. A read-only MapReduce security scan is a separate analysis workload sharing a tool/agent engine, not automatically a self-governing management tier of the coding organization.
- Reviewed revision: `2734ab5f18939b20c774b39c4406788383e35255`.
- Observation date: 2026-10-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/README.md) and [mod.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/query/mod.rs) establish the installed coding loop: a model returns selected file/shell/search tools, whose outcomes are executed by the Rust tool engine and re-enter the turn. [agent.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/agent.rs) creates independently model-running subordinate query loops and can use optional isolated git worktrees; [coordinator.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/services/coordinator.rs) ships `general-purpose` (write-capable), `explore` and `plan` (read-only) builtin types. The coordination registry can record multiple spawned processes and collect completion results, but a registry by itself does not decide disturbances among active agents. Crucially, the shipped [send_message.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/send_message.rs) `SendMessage` tool explicitly returns a placeholder queued-message string instead of routing the message into the recipient's live conversation; the on-paper inbox in [coordinator.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/services/coordinator.rs) must not be substituted for the unimplemented model-facing return path.

The supported security-scan mode in [security_scan.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/cli/src/security_scan.rs) creates an `EngineAgent` and calls [orchestrator.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/amr/orchestrator.rs). It runs a model-authored PLAN selector, deterministic source SHARD/BATCH, concurrent independent read-only MAP investigation agents over file-scoped batches, and a model REDUCE of the resulting finding set. [batch.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/amr/batch.rs) ensures signals for one file remain in one batch; the scan's concurrency semaphore bounds simultaneous MAP execution and records incomplete coverage when worker output fails. [reduce.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/amr/reduce.rs) deduplicates/normalizes findings and optionally composes cross-shard attack chains. The report is written to output or displayed by a separate CLI command; [security_scan.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/cli/src/security_scan.rs) returns severity/incomplete coverage exit codes. This code-review-like security analysis should not be mistaken for an S3* corrective audit loop back into the live coding manager without such a return path.

## Operational model

The coding model decides repository actions and can delegate an independent focused subtask to another model-run child and read its result; command permissions, sandbox constraints, queueing and agent definitions enforce execution. The optional security-scanner chooses code signals/findings during a separate explicit invocation, while the deterministic pipeline batches and joins work. None of these supports a claim that a dedicated current-control owner actively regulates a whole live coding-agent workforce, or that security findings automatically trigger independent source-based adjudication followed by binding corrections to an in-boundary coding organization.

## S1 — Operations

- State: A
- Function: perform discretionary local software engineering investigation, editing, testing and tool choice for a user coding objective.
- Disturbance / variety regulated: uncertain repository state, inconsistent test/tool output, context gaps, tool permission failures, partial implementation work.
- Decisive decision or feedback right: model selects specific calls/arguments and subsequent repair or investigation based on returned local execution evidence; write-capable `general-purpose` children independently implement assigned subtasks.
- Decision owner: active model in the main QueryEngine or a spawned model's own independent query loop; not the tool dispatcher.
- Supporting / enforcement mechanisms: provider transport, Rust query turn management, local tool executor, permission rules, session/history, worktree handling.
- Closure path: user task → model selects file/shell/edit actions → first-party tools operate on repository → tool/test results return to model context → next decision or completion.
- Boundary reachability: `agent`, `agent -p`, TUI/ACP/HTTP product entrypoints reach the library QueryEngine; built-in `Agent` delegates via shipped tools, not solely tests.
- Why this is / is not agent-owned: the runtime enforces tools and displays results but does not select context-sensitive engineering solutions absent the model.
- Evidence: [README.md](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/README.md); [mod.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/query/mod.rs); [agent.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/agent.rs); [executor.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/executor.rs); [coordinator.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/services/coordinator.rs)
- Basis: explicit / structural
- Confidence: high for first-party source-wired operation (no paid-provider task executed)
- Caveats: system commands and read-only exploratory helpers do not independently extend S2/S3 ownership.

## S2 — Coordination

- State: —
- Function: no sufficiently supported first-party feedback loop that identifies specific harmful inter-S1 interaction/oscillation and changes affected siblings' subsequent coding operations.
- Disturbance / variety regulated: concurrent write-capable children could edit a common repository or duplicate work; MAP security-scan workers could share an execution quota, but the evidence shows separate read-only shards rather than an executed interference-correction route among competing coding S1s.
- Decisive decision or feedback right: registry/list/parallel dispatch and subprocess completion do not show conflict-sensitive corrective decision; `SendMessage` is a stub in the product tool layer.
- Decision owner: none demonstrated for an S2-specific conflict response; deterministic task batching and capacity limits serve tool scheduling and analysis.
- Supporting / enforcement mechanisms: agent registry, child-context/worktree isolation, asynchronous team join, MapReduce file partitions and semaphore, task result metadata.
- Closure path: spawned tasks return their own results or scan findings to the caller; no demonstrated inter-S1 disturbance sensor → attenuating correction → affected S1 feedback is wired across the declared supported modes.
- Why this is / is not agent-owned: parallel processing and one-way report aggregation do not automatically supply S2's conflict-specific correction; preventing two read-only scan workers from modifying the same file does not establish that they were independently conflicting.
- Evidence: [agent.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/agent.rs); [coordinator.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/services/coordinator.rs); [send_message.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/send_message.rs); [mod.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/amr/mod.rs); [batch.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/amr/batch.rs); [orchestrator.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/amr/orchestrator.rs); [executor.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/tasks/executor.rs)
- Basis: structural / explicit placeholder comment
- Confidence: medium-high for examined product paths
- Caveats: a subsequently implemented active mailbox/handoff or shipped interference-gated multi-writer mode would merit targeted same-ref investigation.

### Absence scope

- Surfaces inspected: builtin agent registry and child execution, team result/status aggregation, SendMessage product tool, worktree options, scanner SHARD/BATCH/concurrency control.
- Plausible first-party paths checked: distinct active writing S1s and file/work interference; model-facing message delivery; disturbance-specific correction affecting siblings; read-only scan worker resource competition.
- Why no material first-party path remains: the inspected direct message route is a placeholder; isolated/batched concurrent tasks return results without an evidenced interference detector and closed corrective return to competing S1s. Semaphore and shard assignment alone are not counted as inter-S1 regulation.

## S3 — Inside-and-now control

- State: —
- Function: no material whole-current operational manager demonstrated at a subordinate multi-S1 system level.
- Disturbance / variety regulated: competing live coding commitments, worker failures, current resource/task tradeoffs requiring corrective assignment.
- Decisive decision or feedback right: no executable model-owned whole-team supervisory decision is evidenced across an up-to-date collective roster/commitments with applied corrective return.
- Decision owner: primary caller delegates its current task; deterministic team collector reports completion, but neither owns managerial whole-current decisions proven here.
- Supporting / enforcement mechanisms: spawned agent result aggregation, task status, workflow commands, separate MapReduce reducer's cross-shard synthesis.
- Closure path: child output comes back to the requesting coding agent and scan REDUCE aggregates findings; no distinct current-management choice that reassigns active S1 commitments on collective information and feeds back to execution was established.
- Why this is / is not agent-owned: a parent handing out one-time subtasks and aggregating reports is task execution; MAP/REDUCE synthesis determines the scan output, not live inside-and-now metasystem management.
- Evidence: [mod.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/query/mod.rs); [agent.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/agent.rs); [coordinator.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/services/coordinator.rs); [executor.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/tasks/executor.rs); [orchestrator.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/amr/orchestrator.rs); [security_scan.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/cli/src/security_scan.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: capable bespoke agent workflows may be built by an operator using this engine but do not donate first-party product ownership.

### Absence scope

- Surfaces inspected: coordinator instance tracking, run_team spawn/join, model `Agent` and task tools, MapReduce PLAN/MAP/REDUCE stages.
- Plausible first-party paths checked: whole-active-S1 current view → discretionary priorities/commitments decision → changed work in several agents → returned feedback.
- Why no material first-party path remains: inspected built-in flows dispatch isolated children and collect responses; the scanner processes fixed analysis stages, not an adaptive current-control supervisory loop over active coding workers.

## S3* — Complementary audit

- State: —
- Function: no separately owned first-party evidence auditor with a demonstrated return into corrective management of this coding-agent organization's claims.
- Disturbance / variety regulated: unverified implementation correctness or false claims of code completion would call for an independent challenger with direct evidence.
- Decisive decision or feedback right: the separate security-scan mode forms vulnerability judgments over source, but yields a standalone report/exit code to the invoker; no attached independent claim-checking review/decision with corrective management return is established for normal coding turns.
- Decision owner: ordinary verification depends on coding model/operator; an optional standalone scan model can own its own security findings without becoming an S3* auditor of the coding organization's management.
- Supporting / enforcement mechanisms: read-only MAP security scan, REDUCE report and command exit codes, optional model-driven review slash workflows and external CI.
- Closure path: security-scan → human/CI-facing findings (at or above severity threshold), not evidenced as independent source-first audit → separate S3 owner decision → changed current coding workforce operation.
- Why this is / is not agent-owned: review/audit vocabulary or a standalone scanner is not sufficient for a canonical complementary audit without actual corrective return; deterministic task tests and plugin review workflows are likewise not sufficient.
- Evidence: [security_scan.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/cli/src/security_scan.rs); [orchestrator.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/amr/orchestrator.rs); [mod.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/amr/mod.rs); [reduce.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/amr/reduce.rs); [coordinator.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/services/coordinator.rs); [mod.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/query/mod.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: the scan is substantive and its incomplete-coverage exit gate is real; the negative claim is limited to absence of an internal independent audit-to-management correction, not an assertion that no code audit is possible.

### Absence scope

- Surfaces inspected: shipped security-scan CLI, MapReduce workers/reducer, standard coding QueryEngine, built-in subagent types and tool result return.
- Plausible first-party paths checked: separate code-evidence reviewer examines coding S1 completion claim, independently challenges it, sends findings to an active manager whose next action repairs the system.
- Why no material first-party path remains: the scan terminates by report/exit status for its own user or CI; the built-in registry lacks a hard-wired separate challenger integrated with a returned current-control correction of an implementer's claim.

## S4 — Outside-and-then intelligence

- State: —
- Function: no separately evidenced adaptive future-capability decision/enactment cycle at the declared agent organizational boundary.
- Disturbance / variety regulated: future provider/coding-task environment variation, new tools, changed engineering requirements.
- Decisive decision or feedback right: no agentic strategic investment/organizational adaptation selection and return to changed capacity.
- Decision owner: human/operator config and project maintainers control model/provider, built-in or custom agent definitions and skill/plugin ecosystems.
- Supporting / enforcement mechanisms: persistent memory consolidation, history compaction, provider fallback, skill/manifests and scheduled tasks.
- Closure path: memory and configuration can inform later task decisions, but prospective outside signal → deliberate capability revision → organizational implementation remains unestablished.
- Why this is / is not agent-owned: remembering code details or switching provider on request does not mean choosing future organizational capabilities.
- Evidence: [README.md](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/README.md); [consolidation.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/memory/consolidation.rs); [schema.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/config/schema.rs); [mod.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/skills/mod.rs); [mod.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/query/mod.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: adding a new long-horizon self-reconfiguration product mode would change the assessment boundary.

### Absence scope

- Surfaces inspected: memory extraction/consolidation, provider settings, skills/custom agent loading, model/tool command scheduler and code session context.
- Plausible first-party paths checked: prospective environmental sensing, discretionary adaptation of organizational capacity, actual adoption and returned capability.
- Why no material first-party path remains: inspected persistence and configurations support current/future individual coding tasks but do not close a first-party organizational S4 intelligence/adaptation loop.

## S5 — Policy and identity

- State: —
- Function: no ultimate mission, identity or binding constitutional policy owner within the product organization.
- Disturbance / variety regulated: conflicts over organizational purpose beyond permission for local tool operations.
- Decisive decision or feedback right: no legitimate S5 actor decides and enacts mission/identity conflict resolutions in the running agent system.
- Decision owner: human operator and developer/project configuration set scope, allowed providers and permissions.
- Supporting / enforcement mechanisms: permission rules, plan/read-only modes, protected paths, per-agent model/tool restrictions and sandbox.
- Closure path: permission checks can deny a shell/file effect or allow one; no purpose/identity matter escalates to a constitutional decision owner and returns as binding policy to the organization.
- Why this is / is not agent-owned: local code security and per-call approval are not ultimate policy/identity governance.
- Evidence: [README.md](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/README.md); [mod.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/permissions/mod.rs); [coordinator.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/services/coordinator.rs); [schema.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/config/schema.rs); [agent.rs](https://github.com/avala-ai/agent-code/blob/2734ab5f18939b20c774b39c4406788383e35255/crates/lib/src/tools/agent.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: repository governance and enterprise administrator policy are outside the agent organization.

### Absence scope

- Surfaces inspected: product permission enforcement, config, agent definition policy, headless/TUI and external contributor/release governance.
- Plausible first-party paths checked: constitutional/identity dispute → legitimate decision owner → binding purpose/policy enactment → changed operations.
- Why no material first-party path remains: permission/sandbox enforcement and user-authored task policies constrain effects without establishing a first-party constitutional owner or a return path.

## Recursion

One QueryEngine model executing local tools constitutes normal S1. Optional `Agent` can create independently model-running subordinate coding workers, including write-capable `general-purpose`, but the inspected shipped orchestration does not alone establish distinct inter-S1 disturbance regulation or whole-team management. The security-scan MapReduce organizes a bounded read-only investigator population around one analysis; its REDUCE reports findings, not autonomous multi-level governance. Upstream operator and developer organization are external.

## Variety and escalation

Model and local tools exchange coding work results; permission failures constrain or escalate to the user. Agent outputs return to the requesting main coding turn. The optional scanner reports incomplete coverage and non-clean threshold breaches with distinct exit statuses; this is valuable reliability evidence without proving that current coding S1 ownership is reallocated or corrected by a separate in-boundary manager. Provider choices and saved context remain task-support mechanisms.

## Evidence gaps

Source-first assessment of frozen Rust revision; no paid-provider full runtime run. The shipped `SendMessage` model tool is explicitly a placeholder even though coordinator internals implement an inbox, so no imagined message-return integration is credited. The scan's concurrency semaphore and immutable per-file batches are verified, but a true S2 interference-specific control-and-correct loop is not inferred solely from parallel read-only tasks. Separate security-scan output is not assumed to feed live agent management. Custom external integrations may implement richer S2/S3/S3* arrangements outside this native boundary; the negative conclusions are bounded to reviewed first-party shipped product modes.
