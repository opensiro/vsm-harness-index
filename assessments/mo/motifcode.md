---
harness_id: motifcode
project_name: Motifcode
repository: https://github.com/TaewoooPark/Motifcode
review_ref: 9fb0d50acf577f60d87592c38b3ae2b57bd9c523
reviewed_at: 2026-10-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Motifcode

## Review boundary

- System in focus: installed first-party Motifcode TypeScript terminal coding-agent harness at frozen `9fb0d50acf577f60d87592c38b3ae2b57bd9c523`; a single local coding task/session with optional built-in child agents.
- Purpose and identity: structure Motif-3-backed code inspection, editing, execution and repair by translating model outputs into validated tools and observations. The external Motif-3 model/hosted Infron endpoint is a model dependency, not an imported coding-agent harness.
- Relevant environment: the operator's filesystem and shell, terminal screen, selected model endpoint, tests, application configuration, permissions, local session journal and optional child scopes.
- Standard-distribution boundary: packaged `motifcode` Node CLI, including `packages/core`, `packages/cli`, `packages/tools`, `packages/protocol`, `packages/agents`, `packages/hooks`, `packages/journal` and TUI, in supported one-shot and interactive modes.
- Credited operating / distribution surfaces: production `runLoop`, `ToolExecutor`, CLI one-shot / chat constructors, `AgentScheduler` and bounded built-in subagent definitions, executable read-only policy/sandbox path, check/repair and journal/checkpoint return.
- Adjacent first-party surfaces excluded from ownership: offline `toolkit/prune`, `toolkit/campaign`, `packages/eval`, benchmarking, replay/eval scripts, repository CI, prompt and protocol golden fixtures, model weights, maintainer activities. Their separate research/review behaviors are not automatically installed supervisory or future-adaptation decisions.
- First-party operating / deployment modes considered: installed CLI interactive chat and direct run, selected toolcall/object/text channels, optional bundled child agents (including reviewer), configured read-only policy and user tool approval. No provider-backed live coding task or autonomous reviewer witness was executed in this source-first inspection.
- Recursion level: one terminal coding-agent session with optional nested child tasks; not the upstream open-source project, the hosted model, or a future aggregate of independently operated deployments.
- Reviewed revision: `9fb0d50acf577f60d87592c38b3ae2b57bd9c523` from Index candidate #379, unchanged.
- Observation date: 2026-10-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The shipped TypeScript monorepo defines its own model/tool loop, protocol parsing and repair, session bookkeeping, CLI/TUI, executable file/shell tools, permission handling, subagent definitions and journal ([README.md](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/README.md), [packages/core/src/loop.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/core/src/loop.ts), [packages/cli/src/main.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/main.ts)). In `packages/core/src/loop.ts`, `runLoop` creates the task conversation, sends model requests, parses actions, rejects invalid payloads, invokes first-party tools through the executor, adds the tool outputs into model-visible session messages, handles failures and continues or finishes. This is the substantive first-party coding execution boundary rather than a thin wrapper around an external coding CLI.

`packages/cli/src/executor.ts` implements the first-party tool dispatcher with approved workspace and execution policies ([packages/cli/src/executor.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/executor.ts), [packages/cli/src/policy.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/policy.ts), [packages/cli/src/sandbox.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/sandbox.ts)). `packages/agents/src/index.ts` defines a capped child-task queue, and `packages/agents/src/builtin.ts` includes optional explorer, reviewer, tester, planner and patcher personas. Both interactive `Chat.makeExecutor` and one-shot CLI `runAgent` can spawn an independent child `runLoop`, with distinct role/system prompt, bounded tool set and a separate journal scope; results return as a `task` tool observation ([packages/cli/src/chat.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/chat.ts), [packages/cli/src/main.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/main.ts), [packages/agents/src/builtin.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/agents/src/builtin.ts)).

`packages/journal` and `packages/core/src/checkpoint.ts` preserve scope/transcript/checkpoint state for continuation; `packages/core/src/compaction.ts` shortens task history ([packages/core/src/compaction.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/core/src/compaction.ts)). The offline `packages/eval` suites and pruning/campaign machinery have separate evaluation and experiment purposes and do not become a live, separately authorized audit or strategic adaptation loop just because they reside in the same repository.

## Operational model

The user specifies a coding objective and optional constraints. A first-party runtime forms a Motif-3-specific prompt/protocol request, model output selects tool calls or completion; protocol validation, tool execution and user authorization produce observations. Those results return into the session for the model to choose the next engineering action, produce repairs or finish. A `done` action can require confirmation by the same agent, which is an ordinary completion guard, not a second independent auditor.

When asked via the `task` tool, a built-in reviewer child has read-only workspace access and a distinct instruction to report concrete code-correctness findings. Its result returns to the parent agent for possible correction. The decision to invoke this optional review belongs to the parent; evidence of a standing complementary audit function with claim-relative independent access and an accountable subsequent control/repair loop remains unresolved. Generic child scheduling is not itself interference regulation among distinct S1 divisions.

## S1 — Operations

- State: A
- Function: perform an open-ended coding task through model-chosen inspection/edit/shell actions and observations fed to subsequent model turns.
- Disturbance / variety regulated: unknown repository layout, changing file contents, rejected tool payloads, program output, failed commands and incomplete code.
- Decisive decision or feedback right: choose next coding/tool action, arguments, repair response, or task completion from newly observed results.
- Decision owner: model-directed first-party Motifcode coding actor; the model endpoint supplies inference, while `runLoop` and `ToolExecutor` structure and execute decisions.
- Supporting / enforcement mechanisms: channel/protocol codecs, schema validator, BreakageBudget, policies, journal/checkpoint, permissions, local file/shell tools and transport retry.
- Closure path: user task → `runLoop` → `transport.complete` → parsed/validated action → `executor.run` → `serializeObservation` into session → next model turn / confirmed finish.
- Boundary reachability: normal packaged direct and interactive CLI code invokes `runLoop`; tool execution is first-party and does not rely on a third-party coding harness.
- Why this is / is not agent-owned: the evolving model-selected coding operations are not a predetermined deterministic workflow; guardrails limit but do not author the task plan.
- Evidence: [packages/core/src/loop.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/core/src/loop.ts), [packages/cli/src/main.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/main.ts), [packages/cli/src/executor.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/executor.ts).
- Basis: explicit source-level model/tool/observation loop.
- Confidence: high for implemented path; live provider behavior not executed.
- Caveats: actual model performance, endpoint access and operator grants are outside this source-only result.

## S2 — Coordination

- State: —
- Function: no distinct S2 relation attenuating evidenced interference or oscillation among separate operational S1 divisions.
- Disturbance / variety regulated: concurrent children competing for model endpoint capacity, queued work, possible child-task scope interactions; no independently established inter-S1 disturbance/attenuation loop.
- Decisive decision or feedback right: S2 would require judgment or first-party relation that changes competing S1 behaviors in response to a specific shared disturbance; not evidenced here.
- Decision owner: `AgentScheduler` applies a generic concurrency cap and FIFO-like waiting; parent model selects tasks and consumes children.
- Supporting / enforcement mechanisms: scheduler queue, `concurrencyFor` local/remote endpoint limits, child scope journal, per-child read-only execution.
- Closure path: child finishes and returns result; scheduler releases capacity, but no S2-specific conflict-resolution decision with corrective return to distinct S1 units is shown.
- Why this is / is not agent-owned: capacity serialization and generic delegation are not by themselves S2-specific feedback over an identified inter-S1 interference.
- Evidence: [packages/agents/src/index.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/agents/src/index.ts), [packages/cli/src/chat.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/chat.ts), [packages/cli/src/main.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/main.ts).
- Basis: bounded negative, source-first.
- Confidence: moderate, at one-session recursion.
- Caveats: user-designed multi-agent workflows could create distinct S1 interference, but are not source-proven here.

### Absence scope

- Surfaces inspected: normal `runLoop`, parent/child orchestration, AgentScheduler queue, task tool dispatch, tool/sandbox policy and journal scope.
- Plausible first-party paths checked: concurrent child scheduling, common model capacity, nested task outcomes, per-child roles/policies and parent-child feedback.
- Why no material first-party path remains: scheduling solves general capacity/transport rather than a specific distinct-S1 conflict and substantive coordination relation with returned changed inter-S1 behavior.

## S3 — Inside-and-now control

- State: —
- Function: no separately owned whole-session current-regulation function over commitments, priorities, resource allocations or system-wide operational tradeoffs.
- Disturbance / variety regulated: tool failures, parse errors, turn caps, transport errors, completion claims, approval decisions and nested job capacity are local execution disturbances.
- Decisive decision or feedback right: substantive current whole-system operational commitment/constraint choices beyond the action loop; not located.
- Decision owner: parent coding model executes task-level planning and delegation; operator grants tool permissions; deterministic loop enforces budgets and retries.
- Supporting / enforcement mechanisms: `BreakageBudget`, `LoopGuard`, `AgentScheduler`, permission policy, abort and channel downgrade.
- Closure path: local guard rejects or re-prompts an action; no independent whole-current S3 decision/feedback to subsequent subordinate S1 operation established.
- Why this is / is not agent-owned: global task counter and self-correcting parser are local S1 execution management, not organizational S3 governance.
- Evidence: [packages/core/src/loop.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/core/src/loop.ts), [packages/core/src/budget.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/core/src/budget.ts), [packages/agents/src/index.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/agents/src/index.ts), [packages/cli/src/policy.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/policy.ts).
- Basis: bounded negative, tested against current-control interpretation.
- Confidence: moderate.
- Caveats: the parent model owns task selection, not a source-identified distinct whole-system regulatory mandate.

### Absence scope

- Surfaces inspected: task loop and budgets, CLI chat supervisor, scheduler and subagent permissions, journal, config, failure repair.
- Plausible first-party paths checked: root task orchestration, run-level recovery, budget/cap enforcement and operator approval.
- Why no material first-party path remains: no distinct S3 current regulatory owner, discretionary shared commitments, system view and returned S3-to-S1 decision path outside the coding-task workflow.

## S3* — Complementary audit

- State: ?
- Function: an optional separately iterating reviewer child can perform grounded correctness review, but the evidence does not conclusively establish a first-party complementary audit organizational path with independent claim access and accountable findings disposition at the selected default session boundary.
- Disturbance / variety regulated: unverified or incorrect code change claims, missed edge cases and defects in the producer's edited files.
- Decisive decision or feedback right: reviewer may inspect code under read-only tools and report concrete failing inputs; parent receives the child's summary, but an audit-specific obligatory/recognized subsequent governance or repair outcome is not demonstrated.
- Decision owner: optional dedicated child model `reviewer` decides findings using a distinct system prompt/tool subset; parent main coding model chooses whether to invoke and how to act. It is a separate invocation, though neither automatic trigger nor independent organizational authority follows from the name.
- Supporting / enforcement mechanisms: built-in reviewer task definition, `task` dispatch, per-child `runLoop` and journal scope, read-only policy, result summary and failure handling.
- Closure path: parent voluntarily requests reviewer `task` → reviewer operates code-inspection tools → child `done` summary → `ToolExecutor.run` returns a tool observation to parent. Actual independent audit findings reaching S3 or an accountable remedial decision are not established from this generic optional path.
- Why this is / is not agent-owned: optional reviewer owns analysis within its child task, but the shipped ordinary mode does not prove complementary audit-function ownership, independence conditions and feedback distinct from model-selected S1 code review.
- Evidence: [packages/agents/src/builtin.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/agents/src/builtin.ts), [packages/cli/src/chat.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/chat.ts), [packages/cli/src/main.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/main.ts), [packages/cli/src/executor.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/executor.ts), [packages/cli/src/policy.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/policy.ts).
- Basis: confirmed shipped alternative audit constructor, uncertain qualifying ownership and full return.
- Confidence: high for optional reviewer wiring; incomplete for S3* functional attribution.
- Caveats: `packages/eval`, replay tooling and repo CI are offline/development/benchmark surfaces; they cannot supply independent audit ownership of ordinary user sessions.
- Claim being audited: correctness/completion of changes made by root coding agent.
- Ordinary reporting path: parent agent tool output and task-completion summary.
- Complementary access path: separate read-only reviewer child can read workspace files and return structured code findings, conditional on parent delegation.
- Independence boundary: child receives different instructions, restricted read-only executor and distinct journal scope; still uses the shared selected inference endpoint and voluntarily receives scope from root, with no independently attested assignment.
- Who acts on findings: parent coding agent may follow the result; no mandatory auditor-to-current-control disposition pathway established.

## S4 — Outside-and-then intelligence

- State: —
- Function: no installed feedback cycle from external/future environmental change to a selected future change of the harness's own capability.
- Disturbance / variety regulated: conversation growth, protocol parse failures and task output errors are current-session conditions, not independently outside-and-then intelligence.
- Decisive decision or feedback right: select and return prospective capability adaptations into operating mode based on environmental analysis; not evidenced.
- Decision owner: no separate S4 agent/constructor; runtime applies fixed compaction and retry policies; offline researchers can change model/toolkit outside credited installed session.
- Supporting / enforcement mechanisms: session compaction, channel fallback, journaling, static skills, optional hooks and offline `toolkit/prune` experiments.
- Closure path: runtime adapts parser/channel for a failed current task and preserves history; does not establish an external/future strategy choice returned into durable capability.
- Why this is / is not agent-owned: current-task recovery and separate model-pruning research do not supply source-proven first-party S4 remit or return at the declared boundary.
- Evidence: [packages/core/src/compaction.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/core/src/compaction.ts), [packages/core/src/loop.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/core/src/loop.ts), [toolkit/README.md](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/toolkit/README.md), [packages/skills/src/registry.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/skills/src/registry.ts).
- Basis: bounded negative.
- Confidence: moderate.
- Caveats: explicitly excluded experimental pruning may affect later releases but is not a proven deployed adaptation loop.

### Absence scope

- Surfaces inspected: core channel repair, compaction, checkpoint and task resume, bundled skill/agent definitions, offline toolkit/eval entrypoints and CLI configuration.
- Plausible first-party paths checked: automatic channel downgrade, task replanning after failure, model-pruning campaigns, user-installed skills and prompt changes.
- Why no material first-party path remains: these are reactive present-task fixes or separate offline development, with no dedicated outside/future intelligence judgment returned to current installed harness capability.

## S5 — Identity and ultimate policy

- State: —
- Function: no distinct organizational ultimate-policy and identity judgment right/closure inside the first-party user-session architecture.
- Disturbance / variety regulated: unsafe tool access, sandbox escape and ambiguous human approval are bounded operational security risks, not themselves S5 identity governance.
- Decisive decision or feedback right: legitimate parent arbitration and return of ultimate system identity/purpose/policy when contested; no first-party path identified.
- Decision owner: human operator selects model, task and approvals; deterministic `ExecutionPolicy` and read-only sandbox enforce limits.
- Supporting / enforcement mechanisms: policy roots, allowed tools, approval, credentials, sandbox and settings.
- Closure path: a tool request is allowed or denied; no separate ultimate organizational policy ruling returns to set identity and constrain ongoing S1/S3.
- Why this is / is not agent-owned: human permission decisions and config are task-level governance, not evidenced legitimate S5 organizational control.
- Evidence: [packages/cli/src/policy.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/policy.ts), [packages/cli/src/sandbox.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/sandbox.ts), [packages/cli/src/settings.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/settings.ts), [packages/cli/src/executor.ts](https://github.com/TaewoooPark/Motifcode/blob/9fb0d50acf577f60d87592c38b3ae2b57bd9c523/packages/cli/src/executor.ts).
- Basis: bounded negative.
- Confidence: moderate.
- Caveats: a host organization may govern Motifcode instances externally; those rights are not claimed as first-party here.

### Absence scope

- Surfaces inspected: runtime policy, sandbox and approvals, configuration, credentials, child executor policies, CLI commands and developer/maintainer surfaces.
- Plausible first-party paths checked: tool-level operator approval as parent mode, read-only sandbox, user config and externally set prompts/model endpoints.
- Why no material first-party path remains: no first-party organizational policy/identity adjudication function and decisive parent return is specified beyond task/tool access restrictions.

## Evidence gaps

- No provider-backed model run or separate commissioned review was executed. The classification is source-relative at the pinned revision.
- The `reviewer` child is a stronger potential S3* audit constructor than mere transcript logging; `?` records uncertainty about functional independence and findings disposition rather than asserting the reviewer is absent.
- The exact optional built-in review trigger and corrective return would need claim-specific operating evidence to justify a positive complementary audit ownership state; no generic audit review gate is introduced into the Index workflow.

## Conclusion

Motifcode has an explicit first-party model/tool/observation coding loop (`S1=A`), generic child scheduling, execution guardrails, optional independent reviewer role and durable session state. These support task execution but do not establish S2 inter-S1 interference regulation, a separately owned whole-current S3 regulatory function, outside/future S4 adaptation or S5 identity/ultimate policy. A potentially complementary reviewer constructor is reachable, but its S3* independence and organizational return are not sufficiently proved to move beyond `?`. No external toolkit, model provider or offline evaluation is credited as first-party session ownership.
