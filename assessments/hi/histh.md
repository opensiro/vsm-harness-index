---
harness_id: histh
project_name: Histh
repository: https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness
review_ref: f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: C
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Histh

## Review boundary

- System in focus: Histh/FreeCode supplied CLI backend and its coding-agent/overnight-run modes, not the repository's development agents or benchmark organization.
- Purpose and identity: carry out user-selected repository tasks, optionally through child agents and bounded multi-iteration night runs.
- Relevant environment: workspace and Git state, providers, users, MCP/extension tools, project checks and permission rules.
- Standard-distribution boundary: apps/core CLI/AgentLoop/providers/tools/session/permissions/memory; synchronous child-agent mode, verifier and night CLI wiring. Frontends are presentation clients.
- Credited operating / distribution surfaces: createAgentLoop tool feedback; safe readonly/serial-writing delegation; night CLI → runNight acceptance/reset/current-budget controller; verifyChanges fresh read-only actor and FAIL return.
- Adjacent first-party surfaces excluded from ownership: root .claude/.codex/AGENTS contributor setup, bench/evals and provider judges, CI/release scripts, web benchmark presentation and third-party browser/subscription service internals.
- First-party operating / deployment modes considered: interactive/headless core, plan/build/review/explore/danger permissions, configured providers, direct and background child tools, default verifier for nontrivial changes and optional night/detached/worktree mode.
- Recursion level: one local coding work system or bounded night run; child subtasks/iterations are not claimed recursively viable systems.
- Reviewed revision: `f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[agent/loop.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/agent/loop.ts) builds provider requests, persists assistant/tool messages, batches safe calls, executes tool decisions and returns their results to subsequent turns. Tool and permission layers enforce mode rules, envelopes, approvals and project bounds. [tools/agent.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/tools/agent.ts) supports fresh/forked, readonly/writing, synchronous/background child agents with a global per-root roster; send/stop controls return activity to the spawning model. Synchronous writing delegates run alone while readonly agents can share a parallel batch. [agent/subagent.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/agent/subagent.ts) implements a separate read-only verifier for nontrivial changes, distinct from ordinary typecheck/test gates. Its direct code/reachability judgment can force a bounded repair/re-review. [cli/commands/night-run.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/cli/commands/night-run.ts) wires [autonomous/orchestrator.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/autonomous/orchestrator.ts), which aggregates iteration usage/status, enforces run commitments, verifies prospective commits, resets failures and returns notes into later iterations. Model redirection supplies optional advice with no budget/stop authority. Persistent memory/graph/extraction/consolidation refine operational context; repo-level eval judges remain outside runtime ownership.

## Operational model

The root model and appropriately delegated child agents own coding operations. The runtime's interference-specific delegation path and optional night current-control path are constructor/deterministic arrangements, not autonomous meta-decisions. A fresh verifier separately owns a bounded completion audit judgment. Human approvals and upfront night limits do not by themselves form parent S3/S4/S5 modes.

## S1 — Operations

- State: A
- Function: Repository task transformation by model-directed coding agents.
- Disturbance / variety regulated: Different user requests, current source state, command errors, child results and repair feedback.
- Decisive decision or feedback right: Choose concrete tools/arguments/delegation and revise work from results.
- Decision owner: Configured root/child model actors under their inherited permissions.
- Supporting / enforcement mechanisms: Provider driver, tool registry, session store, execution envelope, shell/files, queue/batch planner and run caps.
- Closure path: Provider tool proposals execute and their model-visible results append to history; subsequent provider turns select further actions or a final answer.
- Boundary reachability: The shipped core CLI builds AgentLoop and registers real file/shell/agent tools; it does not merely instruct an outside coding agent to do the work.
- Why this is / is not agent-owned: Without the model, transport/storage/gates do not choose task-specific file changes or repair decisions.
- Evidence: [agent/loop.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/agent/loop.ts); [tools/agent.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/tools/agent.ts); [cli/create-cli.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/cli/create-cli.ts)
- Basis: structural
- Confidence: high for source wiring
- Caveats: No native Node execution or live model provider was tested; provider-specific service behavior remains unverified.

## S2 — Coordination

- State: C
- Function: Prevent shared-tree mutation races among synchronous delegated work units.
- Disturbance / variety regulated: Parallel writer agents can race on the same project tree; readonly child operations can safely overlap.
- Decisive decision or feedback right: Select readonly parallel batching versus exclusive synchronous writer execution.
- Decision owner: Developer-selected concurrencySafeFor and runtime batch protocol; no autonomous inter-agent coordinator.
- Supporting / enforcement mechanisms: Agent readOnly defaults, explore-mode tool removal, per-call safety classification and awaited sequential/parallel execution.
- Closure path: A writer delegate's tool batch completes before subsequent batches proceed; readonly results are collected together and returned to the parent model before its next step.
- Boundary reachability: Agent tool supplies concurrencySafeFor(readOnly); AgentLoop uses the actual planToolBatches result to await calls, and child mode physically withholds mutating tools for readonly work.
- Why this is / is not agent-owned: C marks the supplied interference-specific path. The model selects work, but does not own the serialization or change a joint coordination policy.
- Evidence: [tools/agent.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/tools/agent.ts); [tools/batching.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/tools/batching.ts); [agent/loop.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/agent/loop.ts); [permission/mode-policy.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/permission/mode-policy.ts)
- Basis: structural
- Confidence: medium-high for synchronous delegation
- Caveats: Background writable delegates are outside this mutual-exclusion guarantee; no cross-process/global shared-file reservation or complete semantic merge protocol is claimed.
- Distinct S1 units: Independently tasked root and child model work units; multiple readonly delegates may run concurrently.
- Inter-S1 disturbance: Concurrent writable subagents operating on the same tree can race, explicitly identified in the agent tool's concurrency contract.
- Attenuating coordination relation: Readonly agents share safe batches; readOnly:false agents run in an exclusive awaited batch, with readonly modes physically excluding edit/write/bash.
- Feedback into subsequent S1 behaviour: Parent waits for the writer result before later batch/model decisions; readonly evidence is merged into returned tool results.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The scheduling distinction is explicitly tied to write interference and enforced through the child tool set and per-call safety, rather than credited merely from delegation.

## S3 — Inside-and-now control

- State: C
- Function: Whole-night-run current acceptance, budget and intervention control.
- Disturbance / variety regulated: Iterations can spend a shared run budget, repeatedly fail, produce unverifiable changes or leave uncommitted/unsafe work across successive task cells.
- Decisive decision or feedback right: Continue/retry/wait/stop the run and commit versus reset iteration work according to its current aggregate state and selected verification constraints.
- Decision owner: Developer-authored runNight state machine under operator-supplied goals, bounds and verify criterion; no autonomous regulatory policy selector established.
- Supporting / enforcement mechanisms: Manifest/usage records, run limits, Git commit/reset, notes, verification command and quota-wait plan.
- Closure path: Current outcome/usage/Git/check results select commit/reset/repair/stop; failure notes and repairPending return into the next iteration, or termination prevents further spending.
- Boundary reachability: freecode night CLI imports runNight/runIteration and wires real Git, provider/agent iteration, clock/store and operator controls. Injected dependencies are supplied by the shipped CLI, not only test fixtures.
- Why this is / is not agent-owned: Runtime can enforce a preselected regulatory policy, but neither the budget monitor nor an advisory model supervisor owns the underlying shared commitments. C records this S3-specific constructor path; no agent-owned policy optimization is inferred.
- Evidence: [autonomous/orchestrator.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/autonomous/orchestrator.ts); [cli/commands/night-run.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/cli/commands/night-run.ts); [autonomous/iteration.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/autonomous/iteration.ts); [autonomous/budget.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/autonomous/budget.ts)
- Basis: structural
- Confidence: medium-high within one bounded night run
- Caveats: Not whole-project/organization governance. Upfront user limits and a cancel/status command do not independently establish a closed parent S3 mode.
- Whole-system current view: The night controller aggregates iteration number, cumulative USD, consecutive failures, quota-wait allowance, verification outcome and current dirty Git state for the entire declared run.
- Current-control decision scope: Accept/discard work, allocate another iteration or retry, carry repair notes, stop on current resource/commitment bounds and refuse unverifiable commits.

## S3* — Complementary audit

- State: A
- Function: Complementary direct-artifact challenge of a coding agent's completion claim.
- Disturbance / variety regulated: A nontrivial change may be broken, fabricated or technically present but unreachable despite ordinary typecheck/test success.
- Decisive decision or feedback right: Assign PASS/FAIL/PARTIAL after independently checking changed source against the original request and actual entry-to-effect reachability.
- Decision owner: Fresh read-only verifier model; parent cannot self-assign its verdict.
- Supporting / enforcement mechanisms: Changed-file list, original task, optional observed tests/prior report, bounded isolated child loop, verdict parser and capped repair gate.
- Closure path: AgentLoop invokes verifyChanges after at least three changed files; FAIL report becomes a pending reminder, advances to another operational model turn, and can be rechecked up to two attempts.
- Boundary reachability: The supplied core completion path directly calls verifyChanges; executeSubagent constructs the verifier's separate loop/read-only identity with a narrower inherited envelope. Bench/eval judges and contributor agents are not used.
- Why this is / is not agent-owned: The verifier judges raw source and reachable behavior using its own reads; deterministic tests/parsing merely support or enforce that judgment.
- Evidence: [agent/subagent.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/agent/subagent.ts); [agent/loop.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/agent/loop.ts); [permission/mode-policy.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/permission/mode-policy.ts)
- Basis: structural
- Confidence: high for bounded source path
- Caveats: Same provider/model may be shared; verifier receives task/files/test/prior-audit context, not unrestricted institutional independence. Gate is thresholded/capped and PARTIAL can proceed; no audit-effectiveness claim.
- Claim being audited: Main coding work is complete, correct and actually wired into requested behavior.
- Ordinary reporting path: Root model's final no-tool answer and routine deterministic typecheck/test evidence.
- Complementary access path: Fresh read-only verifier reads changed source, callers and user entry-point reachability and can contradict the parent's success claim.
- Independence boundary: Separate generated session/context and read-only actor; parent cannot choose its verdict. Verification disables nested completion features to avoid recursive self-audit.
- Who acts on findings: Root operational agent receives FAIL findings and performs another fix/review cycle under the runtime cap.

## S4 — Outside-and-then intelligence

- State: —
- Function: External/prospective capability adaptation is not established at this harness boundary.
- Disturbance / variety regulated: Memory extraction/consolidation and graphs preserve experience; advisory redirection proposes task routes; night iterations improve a user-selected project objective.
- Decisive decision or feedback right: No qualifying function-specific decisive decision and return path supplied.
- Decision owner: No credited owner; operator/developer configuration and task-level model decisions remain distinct.
- Supporting / enforcement mechanisms: Permissions, hooks, provider/model configuration, memory state and runtime enforcement.
- Closure path: No qualifying function-specific metasystem closure.
- Why this is / is not agent-owned: Memory extraction/consolidation and graphs preserve experience; advisory redirection proposes task routes; night iterations improve a user-selected project objective.
- Evidence: [memory/consolidate.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/memory/consolidate.ts); [agent/redirect/supervisor.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/agent/redirect/supervisor.ts); [autonomous/orchestrator.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/autonomous/orchestrator.ts)
- Basis: structural
- Confidence: high within the inspected supported modes
- Caveats: Future extensions, external organizations and contributor workflows are outside the assessment.

### Absence scope

- Surfaces inspected: Core CLI/AgentLoop/tool batching and agent spawn/control/registry; verifier and deterministic finish tests; night CLI/orchestrator/limits/iteration/manifest; redirection supervisor, memory extraction/consolidation, permission modes/envelopes, hooks and repo evaluation/development boundaries.
- Plausible first-party paths checked: memory/claim judges and promotions, graph recall, models.dev discovery, redirect options, night notes/iteration improvements, runtime extensions and skills
- Why no material first-party path remains: These paths refine operational context or pursue assigned work. No supplied environmental/future model selects an organizational capability adaptation and returns it through current regulation. Repo benchmark/dogfood evolution is explicitly adjacent.

## S5 — Policy and identity

- State: —
- Function: Identity/ultimate-policy closure is not established at this harness boundary.
- Disturbance / variety regulated: Mode policies, immutable child ceilings, allow/ask/deny rules, night safety constraints and ordinary user approvals regulate task rights.
- Decisive decision or feedback right: No qualifying function-specific decisive decision and return path supplied.
- Decision owner: No credited owner; operator/developer configuration and task-level model decisions remain distinct.
- Supporting / enforcement mechanisms: Permissions, hooks, provider/model configuration, memory state and runtime enforcement.
- Closure path: No qualifying function-specific metasystem closure.
- Why this is / is not agent-owned: Mode policies, immutable child ceilings, allow/ask/deny rules, night safety constraints and ordinary user approvals regulate task rights.
- Evidence: [permission/mode-policy.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/permission/mode-policy.ts); [permission/envelope.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/permission/envelope.ts); [autonomous/envelope.ts](https://github.com/ayandexyz/Honey-I-Shrunk-the-Harness/blob/f2aff641e55c2e6bb8c55a8fb82b67bdf2addd1a/apps/core/src/autonomous/envelope.ts)
- Basis: structural
- Confidence: high within the inspected supported modes
- Caveats: Future extensions, external organizations and contributor workflows are outside the assessment.

### Absence scope

- Surfaces inspected: Core CLI/AgentLoop/tool batching and agent spawn/control/registry; verifier and deterministic finish tests; night CLI/orchestrator/limits/iteration/manifest; redirection supervisor, memory extraction/consolidation, permission modes/envelopes, hooks and repo evaluation/development boundaries.
- Plausible first-party paths checked: plan/build/review/explore/danger, inherited envelopes, permission requests, objective/limit settings, role definitions and contributor governance
- Why no material first-party path remains: The shipped runtime has authority constraints but no identity/ultimate-policy issue-to-legitimate-authority-to-returned-policy circuit. Ordinary permission choice or an upfront objective is not S5.

## Distributed OSS parent arrangement

MIT-licensed OSS contributors and repository-level development assistants remain outside the user-installed harness. No organization-level parent mode is inferred from their existence.

## Self-hosted and non-human modes

Core clients and night mode use the same provider/tool stack with explicit permissions. Detached/worktree mode changes process/isolation support; it does not grant identity authority. Third-party OAuth/browser service internals are outside credited evidence.

## Recursion

Root/child agent trees and successive night iterations prove task decomposition and operating continuity; no child's complete local metasystem or recursively viable organization is established.

## Variety and escalation

Readonly ceilings, safe batching, retry/recovery, false-finish checks, adversarial FAIL return, quota waits, manifests and cancellation preserve operational signals. Advisory redirect has no tools/budget/stop authority. None of those status surfaces alone is an algedonic channel.

## Evidence gaps

Static source assessment only. Node/pnpm/tsx are unavailable in the execution environment, so native build/unit tests were not run; no live provider, browser/subscription path, overnight run or external action was executed. Test/eval fixtures corroborate intent without supplying claimed operating ownership. S2 is limited to the synchronous safe-delegation mode, S3 to supplied night current-control construction and S3* to the thresholded fresh-verifier path. Package metadata retains the historical ayandexyz/freecode label; the source API identity and catalog deduplication use stable repository ID 1374012409 and the frozen current canonical repository, with no matching catalog alias.
