---
harness_id: pxx
project_name: pxx
repository: https://github.com/cdnwetzel/pxx
review_ref: 172f07248243f35c226ae4e3e9733c8781401204
reviewed_at: 2026-10-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# pxx

## Review boundary

- System in focus: the first-party Python `pxx` **v2** local-first agent loop/session with default native OpenAI-compatible backend and bounded edit→test→review workflow at frozen SHA `172f07248243f35c226ae4e3e9733c8781401204`.
- Purpose and identity: operate an autonomous local coding agent using operator-provided inference, policy-enforced tools, persistent memory and audit evidence.
- Relevant environment: repository files, commands/tests, model outputs, external inference endpoints and optional code reviewer model.
- Standard-distribution boundary: packaged `pxx` native backend and CLI `run_loop` plus optional reviewer, with alternative aider backend treated as external editing dependency and not credited as first-party agent.
- Credited modes: native `run` and bounded `loop` with scope/budget gates and optional review; not eval-only `prototypes/` or external n8n and aide workflows.
- Excluded adjacent surfaces: test/eval fixtures, memory prototypes, maintainer governance and external inference provider internal actors.
- Recursion: one native coding S1; workflow rounds and model tools are not independent S1 agents.
- Profile 0.2.4; Methodology 0.3.7; reviewed 2026-10-15.
- Credited operating / distribution surfaces: Installed first-party CLI/runtime, native model/tool and policy integration under frozen source.
- Adjacent first-party surfaces excluded from ownership: Public CI/evals/test fixtures, standalone docs, maintainer operations and third-party host services.


## Repository architecture

`pxx/backends/native.py` implements a first-party model→tools→response continuation loop, sending normalized requests to a configured Ollama/vLLM/OpenAI-compatible endpoint while pxx owns tool scheduling and enforcement. `pxx/session.py` creates scope/budget/audit/tool gates and appends cross-run evidence; `pxx/loop.py` implements bounded edit/test/review rounds with fail-closed controls. `pxx/review.py` issues structured model reviewer findings against the actual post-round Git diff; optional `ReviewMode.BLOCKING` can require rework, but user selection and model source matter. `pxx/audit_sampling.py` selects some runs for human auditing and `pxx/events.py` writes hash-chained metadata; neither a sampled flag nor a signed log is a separate autonomous auditor. `pxx/backends/aider.py` is an optional external edit backend, not the native S1 positive.

## Operational model

The configured model in the native backend repeatedly selects repository actions and ingests execution results; the host intercepts every tool through policy, budgets, logging and permitted worktree changes. In the outer bounded loop, the executed diff may face tests and an optional independent model reviewer that returns APPROVE or REVISE findings, and the process can iterate. That is a source-grounded autonomous S1. Multiple rounds, checkpoints and reviewer calls are still stages of one task, not autonomous child coding organizations or an S3/S4/S5 management system.

## S1 — Operations

- State: A
- Function: Run an adaptive first-party coding model/tool loop and carry tool observations into renewed model-selected actions.
- Disturbance / variety regulated: Changing code, tool results, model decisions and operator limits in the selected coding task.
- Decisive decision or feedback right: Choose the next code search/edit/command from tool feedback; retry/repair after tests and review when enabled.
- Decision owner: The configured model inside the packaged pxx native execution/session path; the external inference server supplies completions, not an agent harness.
- Supporting / enforcement mechanisms: NativeBackend._run_loop, policy-enforced ToolRegistry, typed events, budgets, worktree and session history.
- Closure path: Task → model and proposed tool → pxx broker authorization and execution → recorded tool outcome → next model choice; outer run_loop can do bounded edit/test/review rounds.
- Why this is / is not agent-owned: The installed NativeBackend owns substantive model-selected tools and observes their results; deterministic broker rules gate actions rather than choosing code edits.
- Boundary reachability: The declared first-party packaged CLI or runtime directly exposes and runs the described mode without borrowing any external agent task loop.
- Evidence: [pxx/backends/native.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/backends/native.py); [pxx/session.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/session.py); [pxx/loop.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/loop.py); [pxx/tools/__init__.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/tools/__init__.py).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: high.
- Caveats: The conclusion applies to the pinned first-party standard distribution and not to external host organizations.

## S2 — Coordination

- State: —
- Function: Coordinate conflicts between distinct first-party operating S1 agents.
- Disturbance / variety regulated: Changing code, tool results, model decisions and operator limits in the selected coding task.
- Decisive decision or feedback right: Make task-specific model or control decisions based on current operating evidence.
- Decision owner: No independent first-party actor with the required organizational decision right is established.
- Supporting / enforcement mechanisms: Configured policy, runtime state, event/audit logs and deterministic safety gates.
- Closure path: The supported mechanism executes or reports its own bounded task step without the full function-specific decision/feedback return.
- Why this is / is not agent-owned: Workflow nodes, tool batches and externally delegated aider do not establish a distinct local population of continuing independent S1 agents with interference adaptation.
- Evidence: [pxx/loop.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/loop.py); [pxx/session.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/session.py); [pxx/workflow.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/workflow.py).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: The conclusion applies to the pinned first-party standard distribution and not to external host organizations.

### Absence scope

- Surfaces inspected: native model/tool loop, goal/workflow graph, backend factory and worktree safety net.
- Plausible first-party paths checked: parallel workflow steps, optional aider engine, concurrent tasks and shared-scope policy.
- Why no material first-party path remains: no shipped first-party inter-agent conflict sensor, coordinator decision and return into distinct adaptive child S1 behaviours is established.

## S3 — Inside-and-now control

- State: —
- Function: Control whole-current commitments and resources over independently operating S1 agents.
- Disturbance / variety regulated: Changing code, tool results, model decisions and operator limits in the selected coding task.
- Decisive decision or feedback right: Make task-specific model or control decisions based on current operating evidence.
- Decision owner: No independent first-party actor with the required organizational decision right is established.
- Supporting / enforcement mechanisms: Configured policy, runtime state, event/audit logs and deterministic safety gates.
- Closure path: The supported mechanism executes or reports its own bounded task step without the full function-specific decision/feedback return.
- Why this is / is not agent-owned: BudgetGuard, gates and bounded retries regulate a single workflow, not model-owned whole-current operational portfolio decisions.
- Evidence: [pxx/loop.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/loop.py); [pxx/cost.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/cost.py); [pxx/safety.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/safety.py); [pxx/session.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/session.py).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: The conclusion applies to the pinned first-party standard distribution and not to external host organizations.

### Absence scope

- Surfaces inspected: run-level budgets, current workflow state, executor checks, per-round verification and result receipts.
- Plausible first-party paths checked: risk/cost quotas as S3 control, approval gate as parent control, watchdog/recovery and externally managed jobs.
- Why no material first-party path remains: these act per current coding task under preset policy; no first-party supervisory owner chooses team-wide commitments from an observed multi-S1 current state.

## S3* — Complementary audit

- State: ?
- Function: A separate model reviewer may inspect direct post-edit diff and return an independent, cited finding into the bounded review and correction loop.
- Disturbance / variety regulated: Work product defects and gaps between agent claims, actual git diff and test outcomes.
- Decisive decision or feedback right: Independent code judgment and corrective veto; in blocking mode REVISE or reviewer unavailability prevents normal completion.
- Decision owner: Optional NativeReviewer over configured inference route, with first-party review/loop policy; model identity separation and parent S3 corrective authority are not proven.
- Supporting / enforcement mechanisms: ReviewResult structured findings, Git diff, ReviewMode BLOCKING/ADVISORY, bounded rework and audit samples.
- Closure path: Post-round diff → configured reviewer verdict → fail-closed gate or rework round; this is a real QA return but complementary S3* organization is uncertain.
- Why this is / is not agent-owned: A separate reviewer does issue structured diff-based semantic judgments, but whether it is an independently owned complementary organizational audit rather than routine in-band QA—and whether its correction returns through an actual S3—remains unresolved.
- Evidence: [pxx/review.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/review.py); [pxx/loop.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/loop.py); [pxx/audit_sampling.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/audit_sampling.py); [pxx/verify.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/verify.py).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: unresolved.
- Caveats: The conclusion applies to the pinned first-party standard distribution and not to external host organizations.

## S4 — Outside-and-then intelligence

- State: —
- Function: Anticipate external future changes and autonomously promote strategy/capability adaptations into subsequent pxx operation.
- Disturbance / variety regulated: Changing code, tool results, model decisions and operator limits in the selected coding task.
- Decisive decision or feedback right: Make task-specific model or control decisions based on current operating evidence.
- Decision owner: No independent first-party actor with the required organizational decision right is established.
- Supporting / enforcement mechanisms: Configured policy, runtime state, event/audit logs and deterministic safety gates.
- Closure path: The supported mechanism executes or reports its own bounded task step without the full function-specific decision/feedback return.
- Why this is / is not agent-owned: Recorded memory, model calibration and external governance tools do not form the required future/outside option-selection and operational adoption loop.
- Evidence: [pxx/memory/store.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/memory/store.py); [pxx/loop.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/loop.py); [pxx/governance.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/governance.py); [pxx/calibration.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/calibration.py).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: The conclusion applies to the pinned first-party standard distribution and not to external host organizations.

### Absence scope

- Surfaces inspected: cross-session memory, calibration/eval, governance scan, current run and repository project procedures.
- Plausible first-party paths checked: history-derived strategy adaptation, autonomous skill/policy promotion, trend scanning and config rewriting.
- Why no material first-party path remains: future decisions remain user/maintainer-governed or run-specific; no first-party external sensing-to-authorized capability-change closure is demonstrated.

## S5 — Policy and identity

- State: —
- Function: Resolve ultimate organizational identity and binding policy tradeoffs rather than enforcing preauthored rules.
- Disturbance / variety regulated: Changing code, tool results, model decisions and operator limits in the selected coding task.
- Decisive decision or feedback right: Make task-specific model or control decisions based on current operating evidence.
- Decision owner: No independent first-party actor with the required organizational decision right is established.
- Supporting / enforcement mechanisms: Configured policy, runtime state, event/audit logs and deterministic safety gates.
- Closure path: The supported mechanism executes or reports its own bounded task step without the full function-specific decision/feedback return.
- Why this is / is not agent-owned: Deterministic scope/hooks and gate policy constrain the model; memory is explicitly context rather than normative policy authority.
- Evidence: [pxx/safety.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/safety.py); [pxx/broker.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/broker.py); [pxx/governance.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/governance.py); [pxx/memory/inject.py](https://github.com/cdnwetzel/pxx/blob/172f07248243f35c226ae4e3e9733c8781401204/pxx/memory/inject.py).
- Basis: source-first structural evidence of pinned standard-distribution modes.
- Confidence: medium-high.
- Caveats: The conclusion applies to the pinned first-party standard distribution and not to external host organizations.

### Absence scope

- Surfaces inspected: scope limits, budget permissions, hooks, approval and governance scanning, memory-policy precedence.
- Plausible first-party paths checked: safety-policy change, operator approval as ultimate decision, long-term memory promoted as policy.
- Why no material first-party path remains: policy remains externally selected and enforced at execution time; no legitimate ultimate identity dispute, binding decision and returned new operation rights is owned by pxx.

## Distributed OSS parent arrangement

Public maintainers and local operators separately own releases, repository policy and model credentials. The observed pxx tool runtime does not own their combined institution or a cross-installation legitimate S5 parent.

## Self-hosted and non-human modes

The native model/tool loop can use self-hosted Ollama/vLLM or OpenAI-compatible services without delegating first-party tool control to the provider. Optional aider and scoring/reviewer endpoints remain separate dependencies with restricted claims.

## Recursion

A single coding session is the evaluated S1 recursion. Edit/test/review rounds, policy brokers and workflows are nested stages, not automatically independent viable child agents.

## Variety and escalation

Unanticipated source and model/tool variety is handled via native model action/feedback; budgets/scope/protected paths constrain execution. Test regressions, reviewer REVISE and hook denials can block or prompt another bounded attempt; approval and sampled audit events are not S5.

## Evidence gaps

No external model-backed benchmark was run. Separate diff-reviewer model can be configured and can return actionable findings, but function-specific S3* complementary independence and binding S3 correction are not demonstrated. Source and negative grades apply only to frozen v2 standard distribution.

## Assessment summary

**Proposed included**, vector `S1=A / S2=— / S3=— / S3*=? / S4=— / S5=—`. The first-party local native agent operates with model/tool feedback. The bounded, optional diff-review feedback is real but does not automatically establish complementary organizational S3*.

