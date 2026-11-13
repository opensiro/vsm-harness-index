---
harness_id: agent-autoloop
project_name: Agent Autoloop
repository: https://github.com/KKKKhazix/agent-autoloop
review_ref: 55189165943bcdd39b113faceb97b8e1eeacabbd
reviewed_at: 2026-11-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Agent Autoloop

## Review boundary

- System in focus: the installable Node hub with its deterministic event-sourced kernel, worker process and shipped built-in event/CLI agent/channel/delivery plugins; not the external Codex/Claude/DSH platforms or arbitrary user recipes.
- Purpose and identity: keep local command-line agents processing configured events without keeping expensive model sessions open while awaiting human decisions.
- Relevant environment: Node 24, Git, locally signed-in agent CLIs, configured rules, optional Feishu/GitHub and delivery credentials.
- Standard-distribution boundary: shipped kernel, host, worker, protocol, built-in plugins, documented CLI and configuration.
- Credited operating / distribution surfaces: CLI agent adapters and receipt handling, group/lane-aware kernel dispatch, human pause/card/status flow, optional trusted GitHub PR review/delivery.
- Adjacent first-party surfaces excluded from ownership: simulated test facts, example user task Skills, unrelated external agent reasoning, maintainer CI and framework governance.
- First-party operating / deployment modes considered: scheduled/event-driven local hub with built-in Codex/Claude/ACP adapters, optional delivery reviewer plugin, human card pause/resume, and rule-level concurrency controls.
- Recursion level: one installed local hub controlling multiple rule-bound CLI S1 task cells; external provider/agent hosting is supporting infrastructure.
- Reviewed revision: 55189165943bcdd39b113faceb97b8e1eeacabbd.
- Observation date: 2026-11-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The zero-dependency deterministic kernel records state transitions in a SQLite-backed append-only fact log. Node host and plugin adapters ingest cron/external events, apply the administrator's rules, queue work by subject/lane, reserve slots through claimNext and launch external agent processes using first-party worker/adapter code. Agent final messages can carry typed ask/notice/later/events receipts; the hub records and routes them, sleeps without active agent when waiting, then restores the session after the person answers. Optional delivery plugin reads PR diffs in isolated read-only reviewer sessions, records findings and head-provenance, checks CI, and controls merge/ship state. Evidence: [README.en.md](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/README.en.md), [kernel/decide.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/kernel/decide.ts), [plugins/delivery/review.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/plugins/delivery/review.ts), [worker/run.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/worker/run.ts).

## Operational model

External model-backed CLI actors execute discretionary S1 tasks through shipped adapters. The deterministic kernel is a transport, admission, lane-collision and scheduling controller rather than a model-owned S3/S5. A human operator has present workload controls. Optional independent PR reviewer sees raw changes and returns actionable findings to the delivery loop. Agent-emitted later events do not by themselves establish S4.

## S1 — Operations

- State: A
- Function: Run goal-directed tasks in external authenticated CLI agent sessions bound by first-party rule and receipt protocol.
- Disturbance / variety regulated: Scheduled work, source events, code/task novelty, tool feedback and paused human decisions.
- Decisive decision or feedback right: Running CLI agent chooses task solution, next action and structured receipt including ask, later, notice and new follow-up events.
- Decision owner: Configured Codex/Claude/ACP/DSH CLI agent executing in supported first-party worker adapter; kernel only dispatches.
- Supporting / enforcement mechanisms: Rules, Node worker, plugins, event log, durable session references and human card channel.
- Closure path: Rule-matched event → Worker adapter invokes model-backed agent → result/receipt becomes kernel fact → follow-up event/ask/resume returns changed work to agent or its output.
- Boundary reachability: Shipped worker and built-in adapters invoke installed agent processes; README documents real Claude/Codex/ACP multiround runs.
- Why this is / is not agent-owned: No model means deterministic scheduler and receipts cannot solve an open-ended task.
- Evidence: [worker/run.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/worker/run.ts), [worker/agents.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/worker/agents.ts), [README.en.md](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/README.en.md), [plugins/codex/agent.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/plugins/codex/agent.ts)
- Basis: structural and documented tested adapters
- Confidence: high
- Caveats: Model vendors/CLI internals and any user-provided task skill are not first-party owned.

## S2 — Coordination

- State: C
- Function: Subject-scoped suppression of competing concurrently executing agent jobs routed into the same lane.
- Disturbance / variety regulated: Two asynchronous S1 workers may process duplicate events or mutate one subject concurrently.
- Distinct S1 units: Independent worker invocations for queued runs, potentially multiple configured agents and rule groups.
- Inter-S1 disturbance: A second run on the same (group,lane) could conflict with in-flight work; repeat event for queued subject could be redundant.
- Attenuating coordination relation: Kernel enqueue consolidates queued same-rule/lane events; claimNext forbids claimed run with equal group and lane, respecting group/rule/agent capacity.
- Feedback into subsequent S1 behaviour: A claimed/finished run changes subsequent claim eligibility, allowing deferred worker invocation after the earlier owner releases lane.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Conflict witness is shared subject-lane exclusivity, not merely a global worker-count limit; the same-subject lock prevents concurrent S1 attempts.
- Decisive decision or feedback right: First-party group/lane coordination construction and worker lifecycle return are real, but agent-owned discretion over coordination is not shipped.
- Decision owner: Deterministic kernel owns enforcement and developer composes agent task policy/subject granularity, so C rather than A.
- Supporting / enforcement mechanisms: Event-sourced facts, queued/claimed run state, rules group, lane and maxActive.
- Closure path: Source subject → enqueue/claimNext → exclusive lane reservation → worker finish/retry record → next queued run becomes eligible.
- Boundary reachability: Run rules and claimNext execute in shipped kernel/host for configured worker adapters; unlike merely exposing a generic queue, lane exclusivity is function-specific.
- Why this is / is not agent-owned: Removing the CLI models leaves materially same fixed conflict-avoidance policy; no agent selects coordination policy.
- Evidence: [kernel/decide.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/kernel/decide.ts), [kernel/rules.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/kernel/rules.ts), [README.en.md](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/README.en.md)
- Basis: structural
- Confidence: medium
- Caveats: No general semantic conflict detection or agent-owned negotiation of mutually inconsistent goals; a pure scheduler-only reading would limit this state.

## S3 — Inside-and-now control

- State: P
- Function: Human supervision of current hub-wide processing commitments and operating constraints.
- Disturbance / variety regulated: Failed or blocked rounds, pending human decisions, unavailable agents, excess work and unreliable active rules.
- Whole-system current view: CLI status/runs/why supplies current agent/rule workloads, pending cards, failures, usage and durations.
- Current-control decision scope: Owner pauses/resumes particular rule, may replay skipped event scope, changes agent/rule concurrency and answers/halts in-flight decisions.
- Decisive decision or feedback right: Owner selects which present workloads run and at what rule-level capacity.
- Decision owner: Legitimate local human owner of the hub config and CLI.
- Supporting / enforcement mechanisms: Status CLI, versioned rules, pause facts, claimNext gates, app notifications and cards.
- Closure path: Current status/pending work → parent pause/answer/rule update → kernel facts and dispatch gate → subsequent running/queued work changes.
- Boundary reachability: Shipped status, pause/resume, config hot reload and card-answer commands connect to active Node hub.
- Why this is / is not agent-owned: Configured CLI agents act inside their assigned tasks; no first-party model chooses hub-wide current operating constraints.
- Evidence: [README.en.md](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/README.en.md), [kernel/decide.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/kernel/decide.ts), [host/runtime.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/host/runtime.ts), [cli/explain.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/cli/explain.ts)
- Basis: structural
- Confidence: medium
- Caveats: Particular card approval alone does not establish S3; credited parent view and rule-wide workload intervention do.

## S3* — Complementary audit

- State: A
- Function: Conduct a separate model-judged review of PR changes before optional merge/delivery.
- Disturbance / variety regulated: An authoring agent's report may conceal defects or unsafe changes.
- Claim being audited: Changed PR code is sufficiently correct and safe for delivery under trusted main-branch policy.
- Ordinary reporting path: Author PR description and status/CI.
- Complementary access path: Review plugin captures actual read-only Git commit diff and review points from trusted main, not executing untrusted PR code.
- Independence boundary: A dedicated ephemeral Codex/reviewer process reads isolated snapshot, with no checkout or code writes, separate from authoring CLI agent; review exemption is explicit policy.
- Who acts on findings: Delivery flow returns findings to author for new commit/re-review or blocks merge until findings disposition is recorded; main gate governs merge.
- Decisive decision or feedback right: Reviewer model produces structured findings on direct diff evidence and its result controls subsequent delivery.
- Decision owner: Configured independent reviewer agent instantiated by first-party delivery plugin.
- Supporting / enforcement mechanisms: Review ledger, signed head-specific status receipts, trusted review policy, scope/mode parser, full CI and delivery state machine.
- Closure path: PR head → independent source snapshot and review → findings/ledger and GitHub status → remediate/refresh PR → review and merge gate.
- Boundary reachability: Shipped delivery adapter and review.ts executes configured external CLI model in read-only isolated process when delivery rules are enabled.
- Why this is / is not agent-owned: A deterministic diff filter does not author discretionary findings; separate model reviewer does.
- Evidence: [plugins/delivery/review.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/plugins/delivery/review.ts), [plugins/delivery/review-policy.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/plugins/delivery/review-policy.ts), [plugins/delivery/delivery.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/plugins/delivery/delivery.ts), [README.en.md](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/README.en.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Optional delivery feature requires setup and can exempt reviewers under explicit policy. No live PR review replay in this assessment.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospectively generated option for changing the hub's own future organizational capability.
- Disturbance / variety regulated: Event feeds and history show changing environment but current tasks and future scheduled runs are not system adaptation.
- External distinction: Incoming GitHub/webhook events, cron schedule and worker errors.
- Future / prospective distinction: Scheduled later receipt addresses future task execution, not future organization design.
- Adaptation option generated: No built-in adaptation hypothesis and capability-change decision traced.
- Path back into current capability / S3: Operator can edit rules and plugins directly but not from a supported S4-specific prospective feedback loop.
- Decisive decision or feedback right: Not present as S4.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Rules hot reload, events and periodic schedules.
- Closure path: Current task outputs may schedule more work; this is S1 continuation, not S4 capability adaptation.
- Why this is / is not agent-owned: A schedule and self-emitted task events do not establish autonomous future-environment option selection.
- Evidence: [kernel/decide.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/kernel/decide.ts), [kernel/rules.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/kernel/rules.ts), [README.en.md](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/README.en.md)
- Basis: structural negative
- Confidence: medium-high
- Caveats: Users can externally program future-review or self-upgrade tasks with plugins, but hypothetical compositions are not credited.

### Absence scope

- Surfaces inspected: kernel, host, worker, event rules, builtin plugins, CLI and documented standard modes.
- Plausible first-party paths checked: scheduled later events, worker reports, rules hot reload, plugin updates and human monitoring.
- Why no material first-party path remains: these are ongoing task operations or manual setup, without a prospective organizational adaptation decision and return.

## S5 — Policy and identity

- State: —
- Function: No first-party substantive identity/ultimate-policy decision-and-return path at the deployed hub recursion.
- Disturbance / variety regulated: Who handles events, agent capabilities and sensitive action approval are configured and enforced as task/operating rules.
- Identity / ultimate-policy issue: No described in-boundary mechanism for raising and deciding changes to the overarching system's charter and legitimate ultimate authority.
- Ultimate authority in each claimed mode: Human local administrator owns rules.json and installed agent credentials, but mere config edits do not establish S5 parent governance.
- Return-to-operation path: Changed dispatch rules are enforced by hot reload, but this is not an evidenced policy-level proposal → legitimate deciding parent → returned charter decision.
- Decisive decision or feedback right: No separately constructed S5 right beyond external rule ownership.
- Decision owner: No positive S5 mode established within reviewed first-party boundary.
- Supporting / enforcement mechanisms: Rules validation, local config, actor authorization, event data isolation and human cards.
- Closure path: No evidenced identity-level decision loop; settings changes simply alter execution behavior.
- Why this is / is not agent-owned: CLI agent cannot redefine system purpose; operator changing a rule is not sufficient to infer an ultimate-policy governance arrangement.
- Evidence: [README.en.md](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/README.en.md), [host/config.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/host/config.ts), [kernel/rules.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/kernel/rules.ts), [protocol/rules.ts](https://github.com/KKKKhazix/agent-autoloop/blob/55189165943bcdd39b113faceb97b8e1eeacabbd/protocol/rules.ts)
- Basis: structural negative
- Confidence: medium
- Caveats: An embedding company may supply a separate S5 parent process beyond this local hub.

### Absence scope

- Surfaces inspected: kernel, host, worker, event rules, builtin plugins, CLI and documented standard modes.
- Plausible first-party paths checked: rules.json governance, administrator ownership, credential policy, card approval and rule revisions.
- Why no material first-party path remains: no in-boundary identity-charter matter reaches a legitimate parent decision process with evidenced returned ultimate-policy closure.

## Distributed OSS parent arrangement

A local hub is supervised by its own operator. External contributors, GitHub maintainers or providers do not become one shared first-party parent merely by supplying plugins or accounts.

## Recursion

Rule-triggered worker agent executions are separate S1 cells; kernel subject-lane exclusivity attenuates conflicts, and human parent controls current hub operation. Optional PR reviewer acts on a separate evidence channel before delivery.

## Variety and escalation

Rules and hop limits bound event storms. Persistent facts survive restart, ask cards suspend the costly agent process, human answers resume the original session. Subject-lane ownership and bounded maxActive gates reduce collisions; none makes the deterministic kernel an autonomous deliberating manager.

## Evidence gaps

- CLI adapters are reported tested by the project, but no live vendor or Feishu/delivery event was replayed here.
- S2 C rests on the shipped same-subject exclusive coordination constructor rather than global semantic task negotiation; actual actor/role composition stays with the deployer.
- Optional delivery review's actual run depends on configured GitHub and reviewer policy; no assertion that every PR is audited.
- No independent project-wide ultimate-policy loop or autonomous future capability adaptation observed.
