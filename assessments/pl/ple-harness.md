---
harness_id: ple-harness
project_name: PLE Harness
repository: https://github.com/afei8732-hub/ple-harness
review_ref: 1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# PLE Harness

## Review boundary

- System in focus: One PLE Harness task run using the supplied local runner or WebSocket submission server.
- Purpose and identity: Produce engineering deliverables from the task specification and available workspace evidence.
- Relevant environment: An input task and workdir supplied locally or by an evaluator bridge, plus a compatible language-model endpoint.
- Standard-distribution boundary: The shipped Python task runner, WebSocket protocol adapter and vfh runtime, including the default verifier.
- Credited operating / distribution surfaces: Task assembly, provider calls, native or text-tool action handling, workspace tools, budget and verification/repair integration.
- Adjacent first-party surfaces excluded from ownership: The proxy evaluation suite, comparison runs, verifier ablation study, benchmark organizer and model-service internals.
- First-party operating / deployment modes considered: Local solve/CLI and WebSocket submission use the same action loop. Planner, tools and verifier can be disabled for ablations.
- Recursion level: One task execution. Concurrent server connections create separate task instances.
- Reviewed revision: 1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The two entry points build a bridge, a fresh budget and a toolbox, then instantiate the same Harness. The model call returns a native tool action or text directive. The runtime executes the selected action and feeds the observation back. The default verifier reads generated deliverables and a calculation ledger and reports hard failures to the bounded repair phase.

## Operational model

The task agent owns producing engineering artifacts and the task response. Planning, work and repair are phases of that one executor. The calculation tool and separate verifier supply computation and evidence, while the fixed budget and host protocol bound the run.

## S1 — Operations

- State: A
- Function: Produce workdir artifacts and a task answer from a supplied engineering request.
- Disturbance / variety regulated: Variable file formats, incomplete task drafts, tool feedback and failed actions.
- Decisive decision or feedback right: Choose task actions, repair steps and when to end model-directed work.
- Decision owner: The model in the shipped Harness action loop.
- Supporting / enforcement mechanisms: Local/WebSocket bridges, tool dispatch, budget checks and filesystem access.
- Closure path: Model-selected actions change or inspect the workspace. Observations re-enter the conversation until the agent finishes or the runtime limit stops the run.
- Boundary reachability: Both first-party entry points construct the loop and tools. Selecting a compatible model endpoint completes setup.
- Why this is / is not agent-owned: Without model decisions the runtime can meter and verify, but cannot choose the task actions or generate the requested artifacts.
- Evidence: [harness.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/harness.py#L36-L69), [serve.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/serve.py#L84-L95), [vfh/agent.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/vfh/agent.py#L297-L331)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: Provider behavior and submitted deliverable correctness were not executed or measured.

## S2 — Coordination

- State: —
- Function: Inter-S1 disturbance regulation was sought among incoming task instances and the work phases of one task.
- Disturbance / variety regulated: Possible same-workspace or shared-resource interference across tasks.
- Decisive decision or feedback right: No shipped coordination discretion identified.
- Decision owner: No inter-task coordination owner is instantiated.
- Supporting / enforcement mechanisms: The WebSocket handler and per-task budgets run independently.
- Closure path: Each task receives only its own operational results.
- Why this is / is not agent-owned: There is one model decision loop per task and no shipped inter-loop interference response.
- Evidence: [serve.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/serve.py#L3-L14), [serve.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/serve.py#L84-L95), [vfh/agent.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/vfh/agent.py#L253-L295)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: Multiple connections may coexist.

### Absence scope

- Surfaces inspected: The local runner, per-connection server setup, and planning/work/repair control.
- Plausible first-party paths checked: Distinct workers inside phases, shared budget ownership and interference feedback across task instances.
- Why no material first-party path remains: Each connection builds its own loop and budget. The shipped event flow contains no interference response joining independent task agents.

## S3 — Inside-and-now control

- State: —
- Function: Current whole-system allocation or intervention was sought at the task-run recursion.
- Disturbance / variety regulated: A run may need more time or corrective actions while work is ongoing.
- Decisive decision or feedback right: No current-control owner above task-local work identified.
- Decision owner: The caller selects initial limits and the runtime applies them.
- Supporting / enforcement mechanisms: Budget checks, cancellation and deterministic repair bounds.
- Closure path: The worker stops or executes another bounded repair before delivery.
- Why this is / is not agent-owned: These decisions are immediate task execution or execution of preselected constraints.
- Evidence: [vfh/budget.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/vfh/budget.py#L99-L124), [vfh/agent.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/vfh/agent.py#L333-L364), [serve.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/serve.py#L100-L123)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: The evaluator can cancel an individual task.

### Absence scope

- Surfaces inspected: Budget binding, verification/repair transitions, model finish and WebSocket cancellation.
- Plausible first-party paths checked: Agent- or parent-owned reprioritization of commitments, live budget reallocation and returned current-control decisions.
- Why no material first-party path remains: The budget and repair policy are preselected, and the host cancellation path returns a final answer for one task. Task planning and repair do not supply a separate whole-system discretion.

## S3* — Complementary audit

- State: C
- Function: Check the producing agent's artifact and calculation claims with direct, complementary evidence and feed actionable findings into repair.
- Disturbance / variety regulated: A task summary or ledger can overstate completeness, misreport a value or omit a deliverable.
- Decisive decision or feedback right: Select the scope and disposition of an independent audit beyond the verifier's fixed rubric.
- Decision owner: The shipped verifier supplies a callable constructor and structured findings. An autonomous audit judgment owner would require composition.
- Supporting / enforcement mechanisms: Independent numerical route, file and format readers, checker report and the bounded repair prompt.
- Closure path: The verifier reads artifacts and checks the ledger independently. Hard findings feed the original agent's repair phase, after which the verifier reruns.
- Boundary reachability: Verification is enabled in the default task configuration and assembled into both entry points. The verifier API and report are first-party.
- Why this is / is not agent-owned: The producing agent selects repairs. The checker applies fixed rules. Composing a separate decision owner would be needed for agent-owned audit.
- Claim being audited: The run produced the requested artifacts and reported calculationally consistent results.
- Ordinary reporting path: Model finish summary, action notes and final delivery.
- Complementary access path: Direct readers examine artifact contents and file formats. A separate exact-rational route re-evaluates supported ledger expressions.
- Independence boundary: Fixed checker code can contradict the producing model's report. Inputs and checks remain task-local and known to the harness.
- Who acts on findings: The runtime prompts the same task agent to repair hard failures and checks the files again.
- Evidence: [vfh/config.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/vfh/config.py#L60-L69), [vfh/verify/__init__.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/vfh/verify/__init__.py#L23-L61), [vfh/verify/numeric.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/vfh/verify/numeric.py#L144-L205), [vfh/agent.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/vfh/agent.py#L333-L374)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: Coverage is rule-specific. The repair budget can expire with hard failures still open. No independent model auditor ships.

## S4 — Outside-and-then intelligence

- State: —
- Function: Outside-and-then adaptation was sought across tasks and model environments.
- Disturbance / variety regulated: Changes in future task patterns or provider capabilities.
- Decisive decision or feedback right: No shipped prospective capability decision identified.
- Decision owner: No prospective adaptation owner ships in the inspected runner.
- Supporting / enforcement mechanisms: Provider settings, temporary context and per-run report files.
- Closure path: The report ends with the current task. Later runs load externally supplied configuration.
- Why this is / is not agent-owned: Operational observations and manual tuning do not reach a supplied adaptation decision loop.
- Evidence: [vfh/config.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/vfh/config.py#L74-L118), [vfh/agent.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/vfh/agent.py#L253-L295), [vfh/agent.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/vfh/agent.py#L388-L403), [README.md](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/README.md#L101-L142)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: Current-task workspace sensing and adoption of tool-call format are operational adaptations.

### Absence scope

- Surfaces inspected: Configuration and model options, workspace indexing, saved reports and the adjacent benchmark/ablation workflow.
- Plausible first-party paths checked: Cross-task learning from reports, outside scanning with prospective impact and an operator return path into future capability.
- Why no material first-party path remains: The task run saves evidence and receives configuration. No supported path turns future-oriented findings into an approved change to subsequent capability.

## S5 — Policy and identity

- State: —
- Function: Ultimate identity or policy governance was sought for the installed runner.
- Disturbance / variety regulated: Conflicting mission or ultimate-policy requirements.
- Decisive decision or feedback right: No shipped identity decision and return loop identified.
- Decision owner: No actor receives and resolves ultimate-policy matters in this runner.
- Supporting / enforcement mechanisms: Fixed prompts, operator configuration and evaluator protocol.
- Closure path: A task or limit enters run setup. No identity-level decision returns to operation.
- Why this is / is not agent-owned: The provider chooses actions inside the supplied task and limits.
- Evidence: [vfh/config.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/vfh/config.py#L44-L72), [serve.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/serve.py#L74-L95), [harness.py](https://github.com/afei8732-hub/ple-harness/blob/1fa2ad473f5f4fc48b7be01b0b933c6fa3f486c9/harness.py#L75-L99)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: The caller sets a task and operating limits.

### Absence scope

- Surfaces inspected: Configuration, task intake, run limits and submission documentation.
- Plausible first-party paths checked: A parent policy authority receiving an identity-level exception and returning an authoritative change to future operation.
- Why no material first-party path remains: Task text, model settings and fixed prompts set operating conditions. No installed route elevates an identity dispute and applies a returned binding policy.

## Recursion

The credited recursion is the individual engineering task run. The evaluator supplies tasks and receives results at the boundary. The proxy evaluation suite and study of the codebase have a separate purpose.

## Variety and escalation

Native/text tool handling, workspace summaries, tool results and repair findings absorb task variety. Static budgets and cancellation constrain work. Reported limits and hard failures are scoped to the task.

## Evidence gaps

Static source assessment. No provider execution, live submission, scoring replication or coverage measurement was performed. Verification findings are conditional on the supplied artifacts and supported checks.
