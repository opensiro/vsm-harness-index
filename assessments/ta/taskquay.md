---
harness_id: taskquay
project_name: TaskQuay
repository: https://github.com/wrfgup/taskquay
review_ref: d1e2850b5a35968be88ae6db22e5742cffd27679
reviewed_at: 2026-11-10
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: C
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# TaskQuay

## Review boundary

- System in focus: TaskQuay's first-party self-hosted MCP execution/task control plane, its registered workspace tools, managed external-agent lifecycle, execution claims, project work ledger, proof/receipt and local console.
- Purpose and identity: let a remote MCP-capable AI host inspect a local project, optionally delegate bounded coding work to separately configured agent CLIs, prevent overlapping writes/build claims, and return auditable work/usage/acceptance receipts.
- Relevant environment: local project checkout and worktrees, MCP host such as ChatGPT, installed native Codex/Claude/Pi/OpenCode providers and credentials, shared build/output devices, network/OAuth/authentication and human user.
- Standard-distribution boundary: installed source-run `devspace serve` (fork remains `devspace` at CLI/config paths) registers MCP workspace/read/edit/command tools, `work_task` and `agent_task`; host chooses their order. `ExecutionCoordinator` guards participating local operations and external agent launches; `WorkLedger` persists outcomes. Host's reasoning and native model's inference/tool decisions remain external autonomous actors to be composed.
- Credited operating / distribution surfaces: [README.en.md](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/README.en.md), [MCP host workflow](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/docs/chatgpt-coding-workflow.md), [registered agent task](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/agent-task.ts), [registered work task](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/work-task.ts), [MCP host/tool surface](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/codex.ts), [coordination claim manager](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/execution-coordinator.ts), [execution coordination tests](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/execution-coordinator.test.ts), [work ledger](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/work-ledger.ts).
- Adjacent first-party surfaces excluded from ownership: README deployment expectations, developer AGENTS instructions, examples of agent profiles, developer-local experiments, CI/test fixtures and historical reliability writeups. Externally attached ChatGPT/Codex/Claude models or agents may exercise control but do not become first-party decision owners just because the tools admit their commands.
- First-party operating / deployment modes considered: source-built local MCP server with OAuth/HTTPS/tunnel access; host-first direct workspace inspection/actions; optional configured agent delegation with context keys and fresh context; verified read-only parallelism, exclusive writing and shared resource keys; work ledger, evidence/usage receipts, local console and recovery controls.
- Recursion level: one configured TaskQuay-managed local project workstream with multiple external agent sessions and MCP-host control; constructor functions are credited where first-party tools intentionally expose a function-specific path but decisive autonomous composition remains outside.
- Reviewed revision: `d1e2850b5a35968be88ae6db22e5742cffd27679` (intake #3035; stable GitHub repository ID 1359050801).
- Observation date: 2026-11-10.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The [README](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/README.en.md) explicitly calls TaskQuay a self-hosted execution and project-management layer for MCP-capable hosts and says the *host remains the orchestrator*. TaskQuay's source-built server advertises workspace reads/edits/commands, `agent_task`, and `work_task` with structured identity. [Codex](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/codex.ts) and [Claude](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/claude.ts) tool-surface registrations intentionally expose `agent_task` and instruct the host to obtain direct file evidence before delegation. `agent_task` supports `start`, `continue`, `observe`, `list`, `claims`, `steer` and `interrupt`, protects scoped context and captures actual provider receipts. The [MCP workflow](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/docs/chatgpt-coding-workflow.md) composes these actions with host decisions; the first-party server does not independently interpret an open-ended programming goal.

The [ExecutionCoordinator](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/execution-coordinator.ts) has a SQLite transaction-backed claim/waiter registry over canonical checkout roots, access mode, provider agent/thread identity and explicitly declared shared resources. It allows bounded compatible reads, blocks overlapping writers and colliding build/device resource keys, preserves conflicting active claims without stealing on timeout and returns owner/wait guidance. [Tests](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/execution-coordinator.test.ts) explicitly exercise independent clients/processes, same-checkout writer collisions, shared-resource conflicts across distinct worktrees and absence of accidental provider invocation. `WorkLedger` associates work items, child executions, checkpoints, acceptance and usage completeness; it is accountancy, not an independent discretionary S3 or S3* auditor.

## Operational model

- Actual outcome: a local project change/verification or bounded delegated agent task under a host-prepared plan, with source/context links, conflict protection, child progress and task-level receipts.
- S1 units after composition: the MCP host using the direct project tool suite, and optional external native coding-agent sessions via `agent_task`; TaskQuay owns their runnable constructor/transport and safety gate but not their semantic model actions.
- Ownership split: host decides when to inspect, delegate, choose priorities and accept results; native agent decides its own coding steps; TaskQuay implements typed tools, isolation/admission, persistence and receipts. A human administers permissions, allowed roots and provider setup.

## S1 — Operations

- State: C
- Function: first-party constructor for a model-host-controlled iterative coding task that can inspect files, edit/run code, delegate an external coding-agent session and observe its actual results.
- Disturbance / variety regulated: project-specific code and failures, stale context references, provider errors, retries, duplicate task IDs and unknown result states.
- Decisive decision or feedback right: select next inspection/edit/test or delegated agent action from observations. This substantive right resides in the externally attached MCP host or native coding agent, not a first-party TaskQuay model actor.
- Decision owner: missing-to-compose autonomous MCP host (e.g., ChatGPT) and optionally configured native agent; TaskQuay is constructor, enforcement and transport only.
- Supporting / enforcement mechanisms: `open_workspace`, read/context/search, mutation and shell tools, `agent_task` start/observe/continue, `work_task` identity/evidence/receipt, source-hash checks and saved provider session identity.
- Closure path: host instruction → registered MCP read/execute/delegate call → actual workspace or native agent observation → structured tool reply/receipt → host's next model decision. The path is first-party exposed and reachable, but no autonomous actor is packaged by TaskQuay itself.
- Boundary reachability: README `pnpm build`, `node bin/devspace.js serve` and OAuth connection route instantiate actual MCP tools; [tool-surface registrations](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/codex.ts) and [agent_task implementation](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/agent-task.ts) actively expose the full task path, not only an example command.
- Why this is / is not agent-owned: the constructor can supply real project operations and observe results but cannot choose subsequent semantic tasks without a configured external model host; `A` would misattribute external cognition, while `—` would ignore an intentionally complete first-party host-facing task/action/feedback constructor.
- Evidence: [README operating contract](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/README.en.md), [host coding workflow](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/docs/chatgpt-coding-workflow.md), [registered agent loop adapter](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/agent-task.ts), [work task controls](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/work-task.ts).
- Basis: structural function-specific constructor, documented host ownership.
- Confidence: high for real exposed MCP operations and missing first-party decision owner; live host-to-local connection not executed.
- Caveats: no npm release of this fork is implied; operation assumes source-built server, authorized roots, an MCP host and optional native provider.

## S2 — Coordination

- State: C
- Function: specifically designed inter-agent/host-operation conflict regulation using checkout/read-write and shared-resource claims, with explicit conflict/queue feedback to subsequent work.
- Disturbance / variety regulated: two distinct coding S1s writing the same checkout; writers conflicting with verified readers; independent worktrees sharing a build output/device/database; reuse of a busy provider thread; concurrency starvation or reader barging ahead of waiting writer.
- Decisive decision or feedback right: first-party claim arbitration admits a compatible worker or rejects/queues incompatible operations and returns owner/reconciliation hints. The broader adaptive choice to wait, move work to another checkout, serialize or revise the plan remains with the external host; this is why the state is `C`, not `A`.
- Decision owner: first-party `ExecutionCoordinator` deterministically enforces precise interference policy; the missing autonomous S2 actor or host must compose discretionary resource/priority conflict resolution using those facts. No internal model independently chooses tradeoffs.
- Supporting / enforcement mechanisms: canonical checkout identity and path overlap, shared explicit resource names, read/write access verified by adapter (not prompt), SQLite atomic immediate transactions, queue waiter order, non-stealable active claims, bounded concurrency defaults and `agent_task claims` introspection.
- Closure path: competing host/agent operation attempts claim → `exclusiveConflict` tests checkout/thread/resource interference → second operation waits or receives `EXECUTION_CONFLICT` with owner/context → host can observe owner/claim and choose a nonconflicting subsequent action; after release, queued work may acquire without blind retrying a write.
- Why this is / is not agent-owned: the runtime enforces a first-party S2-specific relation rather than general messaging; however policy selection and meaning of alternative commitments are external and no autonomous S2 owner closes that discretion, so `C` is the bounded constructor claim.
- Distinct S1 units: at least two separately model-driven coding sessions launched from different MCP host conversations or native agent IDs, potentially on the same checkout or different worktrees sharing a named build resource; source tests simulate independent clients/processes.
- Inter-S1 disturbance: conflicting writes or reader/writer on overlapping checkout paths and `gradle:shared-output` used by independent worktrees; simultaneous provider thread ownership also conflicts.
- Attenuating coordination relation: `ExecutionCoordinator.exclusiveConflict` and atomic `acquire`/fair `enqueue` gate incompatible operations before they act; shared readers are bounded and writers remain exclusive.
- Feedback into subsequent S1 behaviour: conflicting `agent_task` returns a structured owner, `providerInvoked:false`, `nextAction` observe or inspect claims; waiter admission can then resume when the other owner's claim is released. The host actor must choose its follow-up, making this constructor rather than closed `A`.
- Boundary reachability: `registerAgentTaskTool` is actively registered by both supported MCP tool surfaces; `ExecutionCoordinator.acquire` and `enqueue` are first-party runtime methods integrated with local agent/process session admission, and returned conflict/claim states are exposed to the same host tool surface. The autonomous host's subsequent conflict-resolution judgment still needs composition.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the decisive predicates explicitly compare the *interference* of two active task owners' source access, thread IDs and shared physical outputs, not merely their membership in a task queue; nonconflicting operations can run concurrently while harmful overlap is stopped and reported.
- Evidence: [coordinator conflict predicate/acquire/queue](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/execution-coordinator.ts), [cross-process/read-write/shared-output tests](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/execution-coordinator.test.ts), [agent_task conflict response and claims API](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/agent-task.ts), [README coordination limits](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/README.en.md).
- Basis: explicit S2-specific interference/attenuation witness, transaction-backed source and tests.
- Confidence: high for local claim-level S2 constructor; autonomy of the composed external host was not observed.
- Caveats: this is cooperative participating-task coordination, not an OS sandbox or control of unrelated terminals/editors. The runtime cannot assign true task priorities or guarantee collision freedom without accurate resource labels.

## S3 — Inside-and-now control

- State: —
- Function: no first-party discretionary whole-current resource/commitment manager for the project workstream is established.
- Disturbance / variety regulated: running/queued tasks, incomplete provider receipts, shared-resource claims and child failures are observable in the work ledger and console.
- Decisive decision or feedback right: choosing which whole-project task to advance, reprioritize, cancel or change commitments remains with the external MCP host/human; the server exposes state/control endpoints and enforces fixed safety rules.
- Decision owner: externally attached host for discretionary planning, human user for local approvals; `ExecutionCoordinator` and `WorkLedger` only implement policy/record enforcement.
- Supporting / enforcement mechanisms: project console, work-task ledger and snapshots, `agent_task` list/observe/steer/interrupt, per-run statuses, hard concurrency/read bounds, failure receipts and usage accounting.
- Closure path: status/claims/receipts → host/console read; host may call another task control tool, but no bundled owner with an evidenced whole-project current-control choice and returned adjustment operates independently.
- Why this is / is not agent-owned: task ledger and exact-turn interrupt are infrastructure for an external controller, and the project console is reporting; neither automatically supplies a first-party autonomous or legitimate parent-wide S3 judgment path. The fixed admission gate is classified under S2 constructor, not upgraded to S3.
- Evidence: [README host remains orchestrator](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/README.en.md), [work ledger](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/work-ledger.ts), [work/task observation and interrupt](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/agent-task.ts).
- Basis: structural.
- Confidence: medium-high; no live external host whole-project supervisory mode was configured.
- Caveats: a fully specified external host policy might close S3 in a separate composed system; the first-party TaskQuay release does not own it.

### Absence scope

- Surfaces inspected: project console, agent list/claims/observe, work run ledger, acceptance/usage receipt, concurrency config and control tools.
- Plausible first-party paths checked: overall task status, prioritized waits, forced interrupt, session reuse, global active-agent caps and serialized writer admissions.
- Why no material first-party path remains: no first-party whole-system discretionary plan/resource/commitment decision with corrective return across the portfolio; controls transport host choices and fixed policies.

## S3* — Complementary audit

- State: —
- Function: no separately owned claim-relative independent audit judgment and corrective return to S3 is established.
- Disturbance / variety regulated: possibly stale source hashes, incomplete provider usage, inaccurate completion claims and missing acceptance evidence are tracked and constrained.
- Decisive decision or feedback right: the host may request a fresh-context reviewer and provide explicit acceptance; TaskQuay validates receipts/source hashes and returns evidence but does not independently judge the task's substantive quality.
- Decision owner: external host/human or optional native reviewer; deterministic `WorkLedger`, `publishDelivery`, source-hash checks and review checkpoint code enforce evidence formatting/integrity.
- Supporting / enforcement mechanisms: `work_task record/finish`, acceptance field, delivery source/artifact hash validation, `show_changes`, verification/evidence pages, fresh-context subagent parameter.
- Closure path: tool/source evidence → ledger validation and host receipt → externally authored acceptance decision; no first-party complementary observer with independent operational-evidence judgment and findings returned to an S3 management actor.
- Why this is / is not agent-owned: a second reviewer can be composed, but a generic fresh-context switch plus stored test evidence is not an independent first-party auditor. In particular, a review UI does not imply reviewer independence or returned corrective governance.
- Evidence: [work_task evidence/acceptance fields](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/work-task.ts), [agent_task fresh_context](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/agent-task.ts), [review checkpoints](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/review-checkpoints.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: composable independent review is possible under external host rules but requires proof of complementary evidence, owner and returned findings at that different boundary.

### Absence scope

- Surfaces inspected: work ledger, acceptance/delivery schema, source hash verification, review checkpoints, fresh-context agent controls, console evidence views.
- Plausible first-party paths checked: explicit acceptance, independent session start flag, verification receipts, generated/checked source manifests and post-run trajectory audit scripts.
- Why no material first-party path remains: these guarantee bounded evidence recording or expose a generic reviewer constructor, without an instantiated independent audit judgment and corrective path into current organizational control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party prospective environmental sensing and selected durable adaptation loop for TaskQuay's future organizational capability is established.
- Disturbance / variety regulated: changing external provider capabilities, task context and history recovery affect how current jobs run but are handled by configuration/operational logic.
- Decisive decision or feedback right: choosing new workflow/skill/provider policies is external host/operator/developer work; TaskQuay does not autonomously originate and select future operating rules.
- Decision owner: external host or maintainer; first-party code supports provider profiles, session affinity, capability checks and skill/context transport.
- Supporting / enforcement mechanisms: provider catalog, skills/profile exposure, context-affinity routing, work-item history, agent usage metrics and read-only workspace context.
- Closure path: current context or native catalog feedback → host chooses immediate task/session execution; no first-party outside-and-then option→selection→durable capability-change return to S3/S1 is found.
- Why this is / is not agent-owned: context savings, token usage measurements and dynamic tool discovery are current operational optimization/data, not prospectively owned S4 adaptation.
- Evidence: [README session/context features](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/README.en.md), [MCP workflow/skills](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/docs/chatgpt-coding-workflow.md), [agent task and context choices](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/agent-task.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a future developer/operator may use its telemetry to change policy, but not as an installed first-party autonomous/parent S4 loop.

### Absence scope

- Surfaces inspected: model/provider catalog/config, skills and profiles, context-affinity/reuse, project metrics/receipts, host workflow docs and agent controls.
- Plausible first-party paths checked: cache/usage optimization, provider fallback, skills updates, fresh-context review, task replay prevention and cross-run context reuse.
- Why no material first-party path remains: no specified environmental-foresight actor develops options and commits a selected reusable organizational change as part of runtime.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy decision with a legitimate parent return path is established at this TaskQuay runtime boundary.
- Disturbance / variety regulated: unauthorized remote access, forbidden project roots, risky writes and provider permissions are governed by administrator configuration and OAuth enforcement.
- Decisive decision or feedback right: human owner enables MCP connections, selects permitted roots/providers, authorizes actions and controls source publication; no ultimate constitutional question reaches an S5 policy owner and returns as a revised binding mission/identity decision.
- Decision owner: local human administrator/user and externally configured MCP host; first-party code enforces auth/scope and idempotency.
- Supporting / enforcement mechanisms: OAuth owner approval, local console binding, root scoping, request/task keys, native provider permission profiles, command/claim admission.
- Closure path: connection/tool request → authentication/approval and scope checks → allowed or denied execution; no explicit identity-level issue→authority→policy decision→return to subsequent operation.
- Why this is / is not agent-owned: host-mediated authorization and strong permission gates remain operational controls; they do not establish autonomous S5=A or closed S5=P merely by involving a human.
- Evidence: [README OAuth/host boundary](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/README.en.md), [MCP host-origin scope](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/tool-surfaces/work-task.ts), [execution scope and claims](https://github.com/wrfgup/taskquay/blob/d1e2850b5a35968be88ae6db22e5742cffd27679/src/execution-coordinator.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: legitimacy of a project's actual ultimate policy is external to this local MCP service; no S5 parent/mandate is inferred from app consent.

### Absence scope

- Surfaces inspected: OAuth/setup docs, MCP host/worker authorization, workspace scoping, config and provider permission profiles, source publishing/acceptance tool descriptions.
- Plausible first-party paths checked: owner approval, host plan, project instructions, remote permission checking, task acceptance, user config/roles and provider identities.
- Why no material first-party path remains: these control task execution permission and data provenance, not a constitutional policy-level decision with authoritative return.

## Recursion

TaskQuay is a control-plane constructor around external MCP-host and native coding-agent S1s. It intentionally supplies first-party S1-specific action/observation interfaces and an S2-specific source/resource collision gate; both require an external autonomous actor to own substantive adaptive choices. Separate agent IDs and worktrees are not automatically independently viable organizations, and console task lists are not a packaged S3 executive. The `C` grades distinguish supplied functional constructors from unsupported first-party autonomous closure.

## Variety and escalation

Workspace and provider observations return to the host; incompatible checkout/resource operations receive explicit claim-owner feedback before a conflicting provider is invoked. Queue tickets preserve order without stealing active claims after uncertain disconnect. Missing usage, unknown receipts and unfinished child work block unsupported completion assertions, leaving reconciliation to the host/human. The project exposes precise operational escalation tools but not higher policy or independent audit authorities.

## Evidence gaps

- Static first-party source/README/tests inspection at frozen ref only: no authenticated ChatGPT MCP connection, local Codex inference, concurrent agent execution or acceptance E2E was performed.
- TaskQuay is a source fork with compatibility `devspace` CLI/paths and private package flag; do not infer a published TaskQuay npm product or hosted deployment from README examples.
- S1 and S2 positive `C` claim functional constructor reachability only. Their external autonomous decision owner, concrete orchestration quality and inter-process guarantees outside participating tools require deployment evidence.
