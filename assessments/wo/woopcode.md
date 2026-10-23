---
harness_id: woopcode
project_name: Woopcode
repository: https://github.com/mangit955/woop-code
review_ref: e50bb87facdd8aa4e134da0cadfc361ac6d69ec3
reviewed_at: 2026-10-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-23
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Woopcode

## Review boundary

- System in focus: Woopcode's first-party terminal/headless coding-agent runtime at frozen commit `e50bb87facdd8aa4e134da0cadfc361ac6d69ec3`.
- Purpose and identity: a model-driven local coding assistant which inspects a repository, executes tools with approvals, checks changes and reports task outcomes.
- Relevant environment: user prompts and approvals, repository contents, local or E2B sandbox shell, web/tool outputs, model providers and task constraints.
- Standard-distribution boundary: published Bun CLI (`cli.ts`), terminal Ink UI or `--prompt` execution, `AgentController`, single `agentLoop`, bundled `toolRegistry`, provider adapters, session persistence, plan/build modes and optional sandbox execution.
- Credited operating / distribution surfaces: `cli.ts`, `commands/{agent,agentController}.tsx/.ts`, `runtime/{loop,turnState,executionLog,planMode,approval,sandbox}/`, `config/{config,sessions,systemPrompt}.ts`, `tools/`, supported UI, headless and sandbox modes.
- Adjacent first-party surfaces excluded from ownership: `packages/tests/` fake-provider/script test suites, `harbor_woopcode/` benchmark adapter and test harness, `run-benchmarks.ts`, development verification/build scripts, `site/`, ADR authoring notes and OSS contributor/maintainer decisions. They corroborate mechanics but do not control a production Woopcode task.
- First-party operating / deployment modes considered: interactive Build and Plan modes, headless `-p`/`--prompt` unattended mode, saved/resumed/forked session history, approval modes, local execution and optional E2B sandbox routing, native tools and the three supported provider adapters.
- Recursion level: one Woopcode model/tool operating session. Forked sessions are transcript histories; concurrent tool requests, sandbox processes and benchmark jobs are not additional independently deciding S1 agent cells.
- Reviewed revision: `e50bb87facdd8aa4e134da0cadfc361ac6d69ec3`.
- Observation date: 2026-10-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

`cli.ts` selects interactive/headless entry; each mode constructs one `AgentController`, which assembles bounded repository/session context and passes a provider client, messages, callbacks and current options to `runtime/loop.ts`. `agentLoop` streams model text and tool calls, resolves calls against one first-party `toolRegistry`, returns results into the same conversation and repeats. The registered tools include filesystem inspection/modification, shell and REPL, test/process support, web search/fetch, user questions, a to-do list and image read. Multiple tools may be requested in one model response, but `agentLoop` executes their calls sequentially and returns results to the *same* decision loop; none is a separate model agent.

`AgentController` holds one current-turn cancellation controller, provider/model, session transcript and execution log. Saving, resuming and forking copy the history but do not instantiate a simultaneously governed population. Plan mode deterministically removes writing tools and rejects writes through the remaining shell path. Approval classification/policy and the mandatory edit diff gate implement local human permissions. Optional E2B sandboxing changes where one agent's shell/process tools run; it does not introduce another model decision owner.

The frozen `runtime/loop.ts` contains a verification finish gate and an unattended requirement finish gate. They inspect same-turn work, may inject one prompt asking the *same* model to verify its edits or provide command evidence for stated requirements, then let that model use normal tools again. The guard is a valuable first-party quality mechanism, but it has neither a separate independent auditor nor a management-level audit claim and return. The `docs/adr/0002-finish-gates-for-an-unattended-turn.md` and tests explain the effect and limits; repository benchmark jobs and tests are adjacent evaluation, not the assessed runtime's S3*.

Frozen primary sources: [`runtime/loop.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/runtime/loop.ts), [`commands/agentController.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/commands/agentController.ts), [`tools/index.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/tools/index.ts), [`runtime/turnState.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/runtime/turnState.ts), [`runtime/approval/policy.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/runtime/approval/policy.ts), [`runtime/sandbox/control.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/runtime/sandbox/control.ts), [`config/sessions.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/config/sessions.ts), [`docs/adr/0002-finish-gates-for-an-unattended-turn.md`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/docs/adr/0002-finish-gates-for-an-unattended-turn.md).

## Operational model

One model has discretion over task steps and tool choices, subject to first-party safety/approval mechanisms. Tool results, failures, test outcomes, execution logs and injected same-model verification/requirement prompts affect its next decisions. Human approvals are per-action boundaries, not evidence of a closed whole-organization parent-control or ultimate identity policy loop. Unattended mode changes the finish gate but not the number of operational decision owners. E2B shell isolation is an execution environment, not a second S1. No native subagent tool, multi-agent work roster or separate reviewer is registered in the first-party distribution.

## S1 — Operations

- State: A
- Function: deliver coding and repository tasks through adaptive model-selected tool actions.
- Disturbance / variety regulated: unfamiliar repository structure, unknown implementation steps, tool errors, changing files, tests and user constraints.
- Decisive decision or feedback right: the provider-backed model selects tool names/arguments and decides whether to inspect, edit, verify, retry or answer after feedback.
- Decision owner: the running Woopcode `AgentController`'s model/tool loop.
- Supporting / enforcement mechanisms: provider adapters, first-party tool registry, diff/approval guards, sandbox executor, session history, turn budgets, requirement and verification reminders.
- Closure path: task/context → model chooses tool calls → registered tool returns result/error → result enters model history → model chooses next action or finishes.
- Boundary reachability: CLI and headless paths both create `AgentController` and call the same native `agentLoop` with the registered tools; offline fake-provider runtime tests exercise multiple model/tool feedback iterations.
- Why this is / is not agent-owned: action choice changes after observations; model discretion would disappear if the model were removed, while approval/executor machinery would only enforce previously requested actions.
- Evidence: [`commands/agentController.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/commands/agentController.ts); [`runtime/loop.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/runtime/loop.ts); [`tools/index.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/tools/index.ts); [`packages/tests/runtime/agentLoop.test.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/packages/tests/runtime/agentLoop.test.ts).
- Basis: explicit + structural + deterministic fake-provider script tests.
- Confidence: high.
- Caveats: no real LLM-agent run or task success-rate measurement; source docs describing earlier limits are secondary to the frozen implementation.

## S2 — Coordination

- State: —
- Function: no first-party inter-S1 conflict/oscillation attenuation path is established at this recursion.
- Disturbance / variety regulated: multiple calls could affect a shared repository, but are selected by one model turn, not independently deciding S1 cells.
- Decisive decision or feedback right: the one working model chooses all requested calls; sequential tool execution and sandbox syncing implement its actions.
- Decision owner: no separate S2 function owner.
- Supporting / enforcement mechanisms: sequential `executeToolCall` loop, safe file path resolution, edit approvals, plan-mode gate, sandbox executor and saved-session forks.
- Closure path: tool outputs return to one S1; no distinct-S1 interference witness → coordination response → changed peer-S1 behavior is shipped.
- Why this is / is not agent-owned: batching tools and forking *history* are not live independent operational units, and permissions protect actions against the environment rather than coordinating different S1s.
- Evidence: [`runtime/loop.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/runtime/loop.ts); [`commands/agentController.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/commands/agentController.ts); [`config/sessions.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/config/sessions.ts).
- Basis: structural bounded absence review.
- Confidence: high.
- Caveats: external operators can run independent instances; their ad hoc coordination is not packaged as this first-party harness's S2.

### Absence scope

- Surfaces inspected: TUI/headless construction, `AgentController`, model/tool loop, complete native tool registry, session forking, process tool and sandbox executor/sync.
- Plausible first-party paths checked: native subagents, parallel agent runs, tool batching as coordination, fork as live child, sandbox process as operational peer and queue/resource interference attenuation.
- Why no material first-party path remains: supported runtime controls one deciding agent per session; neither additional S1 units nor a conflict-specific feedback relation between them is wired into the assessed mode.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-current management control over a population of autonomous S1 units is established.
- Disturbance / variety regulated: repeated local tools and excessively long turns are regulated, but at the single operating-task level rather than shared agent commitments or resources.
- Decisive decision or feedback right: the model can replan its own task; an interactive operator can approve, cancel, change mode or extend one current turn.
- Decision owner: the local S1 model and local user; no first-party S3 management owner at this recursion.
- Supporting / enforcement mechanisms: wall-clock and iteration budgets, duplicate suppression, `AgentController` cancellation, turn usage/status, session persistence, sandbox on/off control.
- Closure path: current task feedback regulates the same task; no whole-agent-population view → management choice → returned resource/priority/commitment change is wired.
- Why this is / is not agent-owned: a single turn's budget/cancel gate cannot supply whole-system S3 merely because it is called a controller. Parent approval concerns one task action, not multi-unit current regulation.
- Evidence: [`commands/agentController.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/commands/agentController.ts); [`runtime/loop.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/runtime/loop.ts); [`runtime/sandbox/control.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/runtime/sandbox/control.ts).
- Basis: explicit + structural bounded absence review.
- Confidence: high.
- Caveats: user-operated independent Woopcode sessions may be coordinated externally; no qualifying first-party `P` management mode was found.

### Absence scope

- Surfaces inspected: controller, TUI callbacks, session commands, turn budgets, process/sandbox mode, runtime usage counters and headless automation mode.
- Plausible first-party paths checked: multi-agent live roster, job ownership/prioritization, session fork as portfolio, operator cancellation and budget continuation as S3 parent control.
- Why no material first-party path remains: available controls regulate a single operating loop, with neither the necessary whole-current multi-S1 view nor substantive shared management right at the declared recursion.

## S3* — Complementary audit

- State: —
- Function: no sufficiently independent operational reality-checking channel with accountable S3 corrective return is packaged.
- Disturbance / variety regulated: incorrect edits or false completion claims are challenged by a one-time finish gate, but within the same operating model/task.
- Decisive decision or feedback right: `finishTurn` injects a deterministic reminder and the original model chooses its own verification commands and interpretation; no independent auditor controls a complementary claim check.
- Decision owner: the same S1 model, with deterministic runtime prompting rather than S3* audit ownership.
- Supporting / enforcement mechanisms: `hasUnverifiedEdits`, unattended requirement reminder, pinned initiating task, execution log, test tool and developer benchmark/test suites.
- Closure path: same-loop self-check → same model's further tool calls/answer. There is no independent ground-truth sampling → S3 judgment → audited operational correction circuit.
- Why this is / is not agent-owned: verifying one's own edits against self-selected commands is ordinary S1 quality feedback, even when the reminder itself is hard-coded; outside benchmark scoring lives in adjacent development machinery.
- Evidence: [`runtime/loop.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/runtime/loop.ts); [`runtime/turnState.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/runtime/turnState.ts); [`docs/adr/0002-finish-gates-for-an-unattended-turn.md`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/docs/adr/0002-finish-gates-for-an-unattended-turn.md); [`packages/tests/runtime/requirementGate.test.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/packages/tests/runtime/requirementGate.test.ts).
- Basis: explicit + structural, corroborated by first-party script tests.
- Confidence: high.
- Caveats: the finish gates may measurably improve local correctness; this does not establish independent S3* or effectiveness without a controlled task experiment.

### Absence scope

- Surfaces inspected: finish gates, task pin, execution log, model/tool loop, `run_tests`, diff approvals, provider adapters, test and benchmark adjacency.
- Plausible first-party paths checked: verification reminder as reviewer, requirement gate as independent checker, user approval as audit, replay benchmark as live audit and logs as audit evidence.
- Why no material first-party path remains: checks use the producer model's own commands/evidence; benchmark/test evaluation does not return an independently owned audit finding to a first-party S3 control circuit in production.

## S4 — Outside-and-then intelligence

- State: —
- Function: no bounded first-party prospective adaptation of Woopcode's own future operating capability from an external environment model is shipped.
- Disturbance / variety regulated: external web pages, repository changes and tool outputs may alter a task solution, but are consumed by that current S1 rather than a separate outside-and-then adaptation function.
- Decisive decision or feedback right: the operating model may search/fetch for its immediate request or write a plan; no durable prospective capability-adaptation decision/path exists.
- Decision owner: current S1 model for local task investigation and external user/developer for software evolution.
- Supporting / enforcement mechanisms: `web_search`, `web_fetch`, repository context and plan mode, session/execution logs and configurable providers.
- Closure path: retrieved data → same task's next choice; no environmental projection → adaptation option → incorporated later harness capability route.
- Why this is / is not agent-owned: mere external search, internal planning, retained history or repository maintainers' product roadmap are not an S4 function at the stated runtime boundary.
- Evidence: [`tools/index.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/tools/index.ts); [`runtime/planMode.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/runtime/planMode.ts); [`commands/agentController.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/commands/agentController.ts).
- Basis: explicit + bounded source absence review.
- Confidence: medium-high.
- Caveats: an agent could be tasked externally with making future research notes, but that user-defined task would not establish a shipped harness-owned S4 mode.

### Absence scope

- Surfaces inspected: prompt/context assembler, tools including web search/fetch, task planning and memory/session paths, provider configuration, runtime gates and contributor docs vicinity.
- Plausible first-party paths checked: web browsing as environmental scan, plan mode as prospective strategy, execution logs and persistent sessions as adaptation, external benchmark findings as product improvement.
- Why no material first-party path remains: each reachable production path applies external information to the current user task; there is no first-party model of future environmental distinctions turned into durable new harness capabilities and returned into current operation.

## S5 — Policy and identity

- State: —
- Function: no closed runtime identity/ultimate-policy adjudication and authoritative return path is supplied.
- Disturbance / variety regulated: risky file/terminal operations and plan-mode writes are gated, but these permissions are action-specific rather than identity- or ultimate-policy-level issues.
- Decisive decision or feedback right: human selects approval mode, accepts/rejects individual diffs or commands, configures providers and changes Plan/Build mode; no particular ultimate-policy question is decided by a legitimate parent and returned as such.
- Decision owner: external user for operational permissions/settings and project maintainers for software distribution, not an established in-boundary S5 closure.
- Supporting / enforcement mechanisms: command classifier/policy, mandatory edit diff review, workspace/sandbox containment, settings validation and TUI approval callbacks.
- Closure path: ordinary operator approval/denial affects a proposed action; no ultimate identity/policy issue → legitimate authority decision → system-wide governing return is wired.
- Why this is / is not agent-owned: deterministic fail-closed approval and fixed prompts do not become S5 policy ownership merely because they constrain the model.
- Evidence: [`runtime/approval/policy.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/runtime/approval/policy.ts); [`runtime/approval/classifier.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/runtime/approval/classifier.ts); [`commands/agentController.ts`](https://github.com/mangit955/woop-code/blob/e50bb87facdd8aa4e134da0cadfc361ac6d69ec3/commands/agentController.ts).
- Basis: explicit + structural bounded absence review.
- Confidence: medium-high.
- Caveats: an organization may govern its use of Woopcode externally; no first-party organization-recursion S5 parent mode was evidenced.

### Absence scope

- Surfaces inspected: approval classifier and policy, file/diff approvals, CLI configuration, Plan/Build selection, sandbox and workspace constraints, project context and maintainer docs vicinity.
- Plausible first-party paths checked: interactive approval as `P`, tool risk classification as autonomous S5, system prompt constraints, provider/settings choice and OSS maintainer governance.
- Why no material first-party path remains: none accepts, adjudicates and closes an identity/ultimate-policy issue for the whole assessed runtime; all reachable decisions are local permissions, task modes or adjacent product maintenance.

## Distributed OSS parent arrangement

Multiple developers/users can independently run Woopcode, but their separate terminals, history forks and OSS contributions are not a shipped first-party organization of current S1 agents. Project governance and developer benchmark feedback remain adjacent to the assessed runtime; no positive S3/S4/S5 parent mode is inherited from the repository's maintainers.

## Self-hosted and non-human modes

The product runs locally with human approval controls, or unattended in headless mode; either way the operating model/tool cycle remains one S1. E2B sandbox, shell approval modes and the unattended finish gates alter enforcement and task feedback but not metasystemic ownership. No all-agent management, independent auditor or S5 governance actor is packaged into either supported mode.

## Recursion

The terminal coding task is enacted by one S1 decision process; tools, subprocesses, sandbox execution and forked session records are subordinate mechanisms or stored alternative histories, not independent autonomous units. The target software project and the OSS maintainer organization are separate recursions.

## Variety and escalation

The current agent adapts after file/shell/model feedback and can re-run checks on finish-gate prompts. Action risks and diff modifications reach the user for approval; plan mode blocks writes, and cancellations/deadlines stop current work. These regulate local task variety and safety. The owner of organizational current-control, independent audit, future adaptation and ultimate policy is not established by the native distribution.

## Evidence gaps

- No live LLM-agent was run or judged; only frozen-source inspection, first-party Bun fake-provider/runtime script tests (387/387 PASS across 23 files) and TypeScript `tsc --noEmit` PASS were used.
- The frozen implementation's current maximum step/duplicate limits differ from some static documentation examples; runtime source and script tests were preferred to overview prose.
- The repository's benchmark evaluations document task outcomes but are adjacent, not a continuously running independent S3* loop inside published Woopcode.
- Existing external operator orchestration or later plugins/versions may add functions, but none is imported into this pinned first-party operating boundary.
