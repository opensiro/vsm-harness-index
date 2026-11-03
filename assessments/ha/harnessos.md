---
harness_id: harnessos
project_name: HarnessOS
repository: https://github.com/JankinLee/harness-os
review_ref: 7f576f5614a066e0bd5797553b0923665aaaefc1
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# HarnessOS

## Review boundary

- System in focus: HarnessOS's first-party Feishu-topic event host, workflow/approval/scheduling machinery, session store, workspace guards and CLI subprocess coordination at the pinned commit.
- Purpose and identity: make externally installed coding agents manageable through a persistent, auditable collaboration and delivery channel.
- Relevant environment: Feishu users/topics, workspaces, Git, external Claude Code and Codex CLI runtimes, credentials and remote model providers.
- Standard-distribution boundary: shipped Node/TypeScript host launched via its own runtime. Claude Code/Codex processes remain external autonomous operational systems.
- Credited operating / distribution surfaces: `src/app/runtime.ts`, `src/app/cli-execution.ts`, `src/cli/runner.ts`, `src/core/workspace-lock-manager.ts`, approval, scheduler and session/store modules.
- Adjacent first-party surfaces excluded from ownership: tests, CI, contribution workflow, design/spec documents and experimental simulations; also the external CLI/model/tool runtime regardless of host launch.
- First-party operating / deployment modes considered: Feishu topic sessions, headless external CLI execution, approvals/continuations, queue/scheduled tasks, cross-workspace arbitration, lock/retry and event logging.
- Recursion level: the repository's host/control layer, not the composed organization that would include Claude/Codex agents.
- Reviewed revision: `7f576f5614a066e0bd5797553b0923665aaaefc1`.
- Observation date: 2026-11-03.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The host maps Feishu topics and workspaces to CLI sessions, accepts requests, submits prompts to independently installed coding agents, intercepts risky tool calls for operator approvals, applies locks, monitors process/liveness loops and preserves run state. Its runtime does substantial orchestration and governance work, but `runCli` constructs a command using the selected external `CliAdapter` and invokes `spawnCli(adapter.command, ...)`. The reply/tool decisions arrive through that child process's stdout, not from a model/tool loop defined by HarnessOS. The lock manager, runaway detector and approval stores regulate the subprocess and its workspace; they do not select its substantive coding actions. Tests and simulations are corroborating control evidence, not a separate supported first-party agent distribution.

Primary evidence: [README](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/README.md), [CLI runner](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/cli/runner.ts), [CLI execution wrapper](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/app/cli-execution.ts), [approval runner](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/app/approval-runner.ts), [workspace lock](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/core/workspace-lock-manager.ts).

## Operational model

The host's local output is a controlled, logged external-agent work session. The actual operational unit that interprets an open-ended software goal and decides coding-tool calls resides in Claude Code/Codex. Removing that subprocess while retaining topic routing, locks, approvals, scheduling, storage and reporting leaves orchestration and transport but no first-party goal-directed agent loop. Thus the first-party boundary does not meet the autonomous-harness S1 admission requirement. This is an evidence-backed **proposed exclusion**, not a claim that a wider HarnessOS-plus-CLI deployment cannot realize other VSM functions.

## S1 — Operations

- State: —
- Function: first-party goal-directed autonomous work is not supplied by the host.
- Disturbance / variety regulated: diverse user coding tasks enter Feishu; the host regulates session and workspace safety, while the external CLI regulates task content.
- Decisive decision or feedback right: choose next substantive coding/tool action based on model and tool observations.
- Decision owner: external Claude Code/Codex runtime.
- Supporting / enforcement mechanisms: `executeCli`, subprocess spawn, workspace locks, prompts, approvals, stop tools and session logging.
- Closure path: topic request → host submits prompt to external CLI → CLI makes model/tool decisions → host records/relays outcome.
- Why this is / is not agent-owned: there is no first-party actor for the substantive task-level discretion; host logic constrains the independently executing CLI.
- Evidence: [runner](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/cli/runner.ts), [execution](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/app/cli-execution.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: the composed host-plus-installed-CLI system would have a different assessment boundary.

### Absence scope

- Surfaces inspected: README, runtime/CLI entrypoints, process runner, approval/locking, schedulers, session stores and source/test inventory.
- Plausible first-party paths checked: Feishu host as agent, automated scheduled tasks, approval continuation, arbitration and runaway recovery as goal-deciding S1.
- Why no material first-party path remains: each substantive work path submits to external CLI; local paths decide host lifecycle/enforcement, not model-directed work.

## S2 — Coordination

- State: —
- Function: a first-party inter-S1 anti-oscillation function is not established for internal autonomous operational units.
- Disturbance / variety regulated: concurrent sessions may contend for the same workspace; the host serializes writes with a read/write lock.
- Decisive decision or feedback right: select coordination responses to interference between qualifying first-party S1 units.
- Decision owner: external workers for task choices; deterministic host lock policy for filesystem exclusion.
- Supporting / enforcement mechanisms: workspace lock manager, session queues, task routing.
- Closure path: conflicting requests are queued, timed out or granted lock admission; no internal agent-level S1 coordination response is owned here.
- Why this is / is not agent-owned: a concrete conflict attenuator exists, but participating goal-directed S1 agents lie outside the first-party boundary; the lock is infrastructure enforcement.
- Evidence: [lock manager](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/core/workspace-lock-manager.ts), [execution](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/app/cli-execution.ts).
- Basis: structural.
- Confidence: high.
- Caveats: wider composite agent teams could have qualifying S2.

### Absence scope

- Surfaces inspected: workspace locks, queueing, collaboration and orchestration paths.
- Plausible first-party paths checked: lock conflict regulation, topic messaging and arbitration as S2.
- Why no material first-party path remains: the operational agents are external; internal host mechanics do not coordinate distinct first-party agentic S1 units.

## S3 — Inside-and-now control

- State: —
- Function: no first-party agent-owned whole-system current operational control is established at this host boundary.
- Disturbance / variety regulated: permissions, concurrent CLI sessions, task state, high-risk actions and runaway calls.
- Decisive decision or feedback right: revise operational commitments/priorities/resources for a whole of qualifying S1 units.
- Decision owner: human topic operators/configuration and external coding agents; deterministic host checks enforce restrictions.
- Supporting / enforcement mechanisms: approval cards, scheduler, run states, runtime policy and lock controls.
- Closure path: host enforces preselected limits or returns operator approval to a CLI subprocess, not a first-party whole-system agent control decision.
- Why this is / is not agent-owned: runtime enforcement and operational approvals are not autonomous S3 decision ownership; a supported qualifying parent S3 closure over internal S1 was not found.
- Evidence: [approval](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/app/approval-runner.ts), [runtime](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/app/runtime.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: controls may be part of S3 in a broader composed system.

### Absence scope

- Surfaces inspected: approval, scheduling, workspace and runtime orchestration.
- Plausible first-party paths checked: operator approvals as S3 parent mode; host budget/scheduler as S3; arbitrator path as whole-system current view.
- Why no material first-party path remains: no internal S1 whole and decision owner/returned S3 closure at this recursion; task approvals and deterministic limits are narrower.

## S3* — Complementary audit

- State: —
- Function: no separate sufficiently independent complementary audit judgment of an internal operational organization is established.
- Disturbance / variety regulated: tool safety, runaway loops, traceability and revision quality.
- Decisive decision or feedback right: challenge ordinary S1/S3 reports from distinct access and return corrective findings.
- Decision owner: host detectors and operator gates for checks; not a reconstructable independent S3* owner of internal S1 operation.
- Supporting / enforcement mechanisms: logs, trace receipts, runaway detector, approval/revision workflows.
- Closure path: observed CLI tool events are checked/enforced or sent for operator handling, not an independent audit path into internal S1 control.
- Why this is / is not agent-owned: monitoring and routine checks do not establish independent challenge, and the operational source itself is external.
- Evidence: [runner](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/cli/runner.ts), [approval](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/app/approval-runner.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: audited external CLI outputs could form an S3* path under a broader boundary.

### Absence scope

- Surfaces inspected: logs, runaway detector, high-risk interception, revision and approval paths.
- Plausible first-party paths checked: traces as audit, tool interception as independent audit, product revision as complementary evaluator.
- Why no material first-party path remains: these host mechanisms monitor or gate external CLI events; no distinct independent claim/challenge/returned corrective S3* owner is established for internal agentic S1.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party externally oriented prospective adaptation loop into internal operational capability is established.
- Disturbance / variety regulated: changing task needs, scheduled requests and revision feedback.
- Decisive decision or feedback right: develop environmental options and adapt present internal S1 capability.
- Decision owner: humans and external coding CLIs for revision choices.
- Supporting / enforcement mechanisms: request/schedule triggers and persistent session/workspace metadata.
- Closure path: revisions and requests are forwarded into external work processes; no first-party S4→S3 adaptation decision/return exists.
- Why this is / is not agent-owned: request planning/revision is not independently a future-environment intelligence loop at the host boundary.
- Evidence: [revision runner](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/app/product-revision-runner.ts), [scheduler](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/app/scheduler.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: project governance might adapt host code externally but is adjacent, not runtime S4.

### Absence scope

- Surfaces inspected: scheduler, revision/feedback workflows, planning and state persistence.
- Plausible first-party paths checked: scheduled tasks as future sensing; product revision as S4; contributor evolution as first-party adaptive runtime.
- Why no material first-party path remains: trigger/revision machinery carries user/external-agent work, not a supported first-party S4 option-generation and capability-update feedback loop.

## S5 — Policy and identity

- State: —
- Function: no returned first-party identity/ultimate-policy decision path is established at the host recursion.
- Disturbance / variety regulated: configured tool permissions, credentials, high-risk approvals and workspace authorization.
- Decisive decision or feedback right: determine or revise ultimate identity/policy of the operational organization.
- Decision owner: human administrators/configuration; ordinary approvals govern tasks, not identity/ultimate-policy matters.
- Supporting / enforcement mechanisms: policy gates, runtime env, approval and access stores.
- Closure path: selected rules constrain later external CLI invocations; no evidenced identity-level issue→legitimate parent decision→returned governance loop.
- Why this is / is not agent-owned: enforcement of static policies and ad hoc human approvals is not S5; no qualifying autonomous or parent-governed S5 mode was found.
- Evidence: [README](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/README.md), [approval](https://github.com/JankinLee/harness-os/blob/7f576f5614a066e0bd5797553b0923665aaaefc1/src/app/approval-runner.ts).
- Basis: structural.
- Confidence: medium-high.
- Caveats: operator governance outside this host can be meaningful at a larger recursion.

### Absence scope

- Surfaces inspected: runtime configuration, approvals, workspace and credential restrictions, product discussion paths.
- Plausible first-party paths checked: policy files as S5; approvals as parent S5; cross-workspace arbitration as ultimate governance.
- Why no material first-party path remains: none demonstrates an identity-level authoritative decision returned to govern a qualifying internal agentic organization.

## Distributed OSS parent arrangement

No organization-level parent S3/S4/S5 arrangement is inferred from GitHub maintenance or local operator approval. Those systems are adjacent to this host-only assessment.

## Self-hosted and non-human modes

Local host deployments support human approvals, but they concern action permissions and CLI continuation; no function-specific parent mode with the required organization-level return path is established.

## Recursion

External coding agents can be S1 in a composite system; repository containment, topic nesting and sessions are not proof of nested viable systems within HarnessOS.

## Variety and escalation

The host attenuates request/workspace/permission variety with locks, scheduler and approval gates. Escalation goes to a human topic operator, but substantive task variety is delegated to the external CLI. No algedonic or higher-function ownership is inferred from a warning, status or queue.

## Evidence gaps

Live Feishu/model-provider end-to-end traces were not exercised; source-level subprocess/decision boundaries are explicit enough for the bounded negative admission. A broader deployed system including actual CLI agents requires a new system-in-focus.
