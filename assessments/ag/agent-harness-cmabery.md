---
harness_id: agent-harness-cmabery
project_name: agent-harness (CMABERY)
repository: https://github.com/CMABERY/agent-harness
review_ref: 170d4c69a0c4b92c7de76ef8b362c5c4025a1786
reviewed_at: 2026-11-04
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-04
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# agent-harness (CMABERY)

## Review boundary

- System in focus: The standard-library Python coding-agent harness's task-scoped `Agent.run` operation and optional one-level child-agent execution.
- Purpose and identity: Turn a repository change request into model-selected workspace actions, a verified result, or an explicit blocked/budget-exhausted outcome.
- Relevant environment: User task and local Git workspace, file/command results, provider errors and model inference, operator permissions, and repository test/build commands.
- Standard-distribution boundary: The shipped Python package and CLI, with a direct first-party model/tool loop, either an OpenAI-compatible endpoint or its scripted offline provider, file/command tools, plan, shared verification ledger and child delegation.
- Credited operating / distribution surfaces: [`agent/loop.py`](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/loop.py), [`agent/tools.py`](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/tools.py), [`agent/plan.py`](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/plan.py), [`agent/ledger.py`](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/ledger.py), [`agent/policy.py`](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/policy.py) and CLI.
- Adjacent first-party surfaces excluded from ownership: Development-time independent reviews described in `DESIGN.md`, tests and fixture repositories, scripted-model demonstration as proof of real-world model quality, GitHub contribution/CI, and external provider internals. They do not own a deployed VSM function merely by co-location.
- First-party operating / deployment modes considered: CLI with an OpenAI-compatible endpoint; deterministic offline scripted provider; direct agent operation with optional one-level subagent; operator-confirmed destructive commands. No separate always-on organizational controller is shipped.
- Recursion level: One task-scoped coding-agent execution and its optional subordinate task cell, not the repository maintainer organization or arbitrary teams of multiple independently launched processes.
- Reviewed revision: `170d4c69a0c4b92c7de76ef8b362c5c4025a1786`.
- Observation date: 2026-11-04.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The CLI builds an `Agent` with a provider, workspace, runtime clock/command runner, policy and event log. The first-party loop sends a task and tool schema to a model, accepts/rejects batches of tool calls, executes workspace tools, and returns the results to the same model for another decision. The model can update the plan, edit files, issue commands, delegate once to a child agent and call `finish`. A parent and child share wall-clock/model-call/token caps and one verification ledger. The ledger requires successful checks after edits before `done`; the plan tracker freezes further edits after repeated failed attempts until a changed plan arrives. Shell policy checks and optional human confirmation constrain commands, while event records, deterministic compaction and provider retries maintain execution. No external agent service or model backend is credited as this package's own orchestration. [README](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/README.md), [DESIGN.md](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/DESIGN.md), [loop.py](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/loop.py).

## Operational model

One root model-driven task loop is the normal S1 cell: it chooses the code changes and investigations that deliver the requested result. An optional child receives an explicitly delegated subtask and runs a fresh model/tool loop, but its separate budget and ledger are bounded by the parent run. The deterministic runtime enforces budgets, tool syntax and verification; it does not independently decide what repository task or correction to pursue. A person selects the task and may approve destructive commands; those ordinary operational acts are not by themselves S3/S4/S5 at this recursion.

## S1 — Operations

- State: A
- Function: Model-driven coding work with repeated tool observations and revision decisions until an explicit outcome.
- Disturbance / variety regulated: Unknown repository state, failing checks, malformed tool replies, provider errors, untrusted tool output and changing edit requirements.
- Decisive decision or feedback right: Choose investigations, file edits, commands, plan revisions, delegation and the final `finish` request in response to tool feedback.
- Decision owner: The task-running model agent through the shipped `Agent` loop; command policy and verification ledger enforce its limits and accepted outcome.
- Supporting / enforcement mechanisms: Tool registry and schema, workspace confinement, shell classifier and confirmation, event log, plan tracker, ledger gate, iteration/token/time caps.
- Closure path: Task and workspace context → model-selected tool call → first-party tool execution and accepted result → subsequent model decision or `finish` → verified `done`, `blocked` or budget-exhausted outcome.
- Boundary reachability: `Agent._run` and `_execute` are called in the standard CLI/runtime; the same live path supports the shipped direct provider and scripted provider without needing dogfood agents or an external coding harness.
- Why this is / is not agent-owned: The model chooses substantive task actions after observations. The host and gate can refuse or downgrade outcomes but do not choose the code solution.
- Evidence: [loop.py#L105-L190](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/loop.py#L105-L190), [loop.py#L335-L477](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/loop.py#L335-L477), [tools.py](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/tools.py), [cli.py](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/cli.py).
- Basis: explicit + structural
- Confidence: high for architectural agent/tool closure.
- Caveats: Provider accuracy and success on real tasks were not evaluated; scripted tests demonstrate plumbing, not external model capability.

## S2 — Coordination

- State: —
- Function: No installed regulation of a concrete conflict/oscillation between two autonomous S1 units at this task-scoped recursion.
- Disturbance / variety regulated: Parent and optional child can both change the same workspace, but observed guards mainly enforce a shared verification contract and single-level delegation, not negotiated inter-unit adjustment.
- Decisive decision or feedback right: Select a cross-unit conflict resolution that changes subsequent behaviour of distinct workers; no such specific S2 decision path was identified.
- Decision owner: Root model chooses when to delegate; shared ledger and parent return are deterministic support, not a separate coordination governor.
- Supporting / enforcement mechanisms: Shared run budget/ledger, child-specific gate scope, `delegate` depth cap and serialized parent return.
- Closure path: Child's tool effects and summary return to the parent task. No distinct inter-S1 interference witness → coordinating decision → changed behaviour of both S1 units is wired.
- Why this is / is not agent-owned: A subordinate model loop and shared state alone are not the four-part S2 coordination witness.
- Evidence: [loop.py#L94-L147](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/loop.py#L94-L147), [loop.py#L446-L477](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/loop.py#L446-L477), [ledger.py](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/ledger.py).
- Basis: structural
- Confidence: medium-high for the shipped one-level task mode.
- Caveats: An external composition of concurrent harness runs could require coordination not present in this distribution.

### Absence scope

- Surfaces inspected: Root/child execution path, shared run and verification ledger, tool registry, plan tracker, CLI, README and design notes.
- Plausible first-party paths checked: Delegation, child/parent work sharing, shared caps, edit verification and child-report return.
- Why no material first-party path remains: These paths enforce a single parent-owned task's execution and verification; no first-party regulator specifically attenuates an evidenced conflict between independent S1 units and feeds that resolution back to them.

## S3 — Inside-and-now control

- State: —
- Function: No distinct whole-system current-control discretion over multiple operational commitments at the declared task recursion.
- Disturbance / variety regulated: Iteration/token/wall-clock exhaustion, repeated failed edits and unverified changes are bounded within one requested task.
- Decisive decision or feedback right: Change shared cross-cell resource allocations or commitments based on a whole-current view; not supplied as a distinct regulator.
- Decision owner: Operator chooses initial limits; model revises its local plan; runtime counts, refuses and terminates by preset rules.
- Supporting / enforcement mechanisms: `SharedRun`, `_check_budgets`, `PlanTracker`, command approval policy and verification ledger.
- Closure path: A limit or failed check returns refusal to the same coding loop; no separately owned S3 whole-current decision returns to multiple S1 cells.
- Why this is / is not agent-owned: The model's local replan is S1 task adaptation, and deterministic limit enforcement does not inherit S3 organizational discretion.
- Evidence: [loop.py#L198-L248](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/loop.py#L198-L248), [plan.py](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/plan.py), [cli.py](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/cli.py).
- Basis: explicit + structural
- Confidence: medium-high.
- Caveats: An operator could supervise a portfolio of tasks externally; not wired as an S3 parent mode here.

### Absence scope

- Surfaces inspected: Budget accounting, plan tracker, delegation, ledger, command policy, event log and CLI configuration.
- Plausible first-party paths checked: Shared root/child quotas, edit freeze/replan, terminal outcome, human approval and verification gate.
- Why no material first-party path remains: Decisions are confined to one task or fixed user-selected limits. There is no separate whole-current multi-cell control right and returned intervention path.

## S3* — Complementary audit

- State: —
- Function: No installed complementary and independently owned audit of claims beyond the normal task's verification/reporting path.
- Disturbance / variety regulated: Unverified edits, masked failing command exits and untrusted reports are detected or rejected by routine execution guards.
- Decisive decision or feedback right: Independently inspect operational reality, issue a challenge and return an audit finding for corrective S3 action; not evidenced.
- Decision owner: The ordinary deterministic verification ledger and current task model, not a separated auditor.
- Supporting / enforcement mechanisms: Command exit-status rules, ledger evidence, JSONL events and optional child task execution.
- Closure path: After editing, ordinary first-party checks gate `finish`. No separate evidence-based auditor judgment returns through an independent correction channel.
- Why this is / is not agent-owned: The model and child can run tests, but normal QA and development-time independent reviews are not a shipped independent audit of an S1 report.
- Evidence: [ledger.py#L150-L203](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/ledger.py#L150-L203), [DESIGN.md](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/DESIGN.md), [loop.py#L430-L477](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/loop.py#L430-L477).
- Basis: explicit + structural
- Confidence: medium-high.
- Caveats: A future separate reviewer harness could consume the log, but that is an unshipped composition.

### Absence scope

- Surfaces inspected: Ledger gate, runtime event log, tests, optional child, plan/finish controls and `DESIGN.md` review provenance.
- Plausible first-party paths checked: Successful checks after edits, event replay, child reviewer possibility and three independent developer review passes.
- Why no material first-party path remains: The shipped gate validates ordinary task evidence from the same run; developmental review is adjacent and no independent real-world audit verdict is routed into ongoing control.

## S4 — Outside-and-then intelligence

- State: —
- Function: No shipped external-and-prospective sensing/option process that changes future system capability.
- Disturbance / variety regulated: The model responds to novel repository facts and tool failures inside the current task, not to a persistent external strategy horizon.
- Decisive decision or feedback right: Produce strategic adaptation options from environmental futures and return them to present capability governance; absent.
- Decision owner: Model owns immediate coding diagnosis; developer/operator can alter tools/configuration outside the runtime.
- Supporting / enforcement mechanisms: Plan updates, context compaction, provider retry and task prompts.
- Closure path: Current repository observations → current edit/test loop; no prospectively selected system change returns through a separate S4–S3 path.
- Why this is / is not agent-owned: A model replan or compacted memory is current task regulation, not an outside-and-then intelligence function.
- Evidence: [plan.py](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/plan.py), [context.py](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/context.py), [providers.py](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/providers.py).
- Basis: structural
- Confidence: medium-high.
- Caveats: Human project evolution is a separate maintainer organization, not the runtime S4.

### Absence scope

- Surfaces inspected: Model loop, planning, context management, provider adaptation/retry, README and development design.
- Plausible first-party paths checked: Replanning, tool-result feedback, deterministic compaction and external provider changes.
- Why no material first-party path remains: All supported paths serve the present task or transport already configured providers; none authors future-oriented adaptation options and returns them to current organizational capability.

## S5 — Policy and identity

- State: —
- Function: No established runtime identity/ultimate-policy adjudication and returned authoritative decision path.
- Disturbance / variety regulated: Unsafe commands and untrusted data are constrained by fixed tools and per-command operator consent.
- Decisive decision or feedback right: Resolve a tension about enduring organizational identity or ultimate policy, then govern later operation by the returned decision; not provided.
- Decision owner: Operator sets task and allowed command scope; default policy enforces preselected rules; ordinary confirmation is local tool authorization.
- Supporting / enforcement mechanisms: Tool-safety classifier, explicit allowed-delete paths, human destructive-command confirmation and system prompt.
- Closure path: A command is allowed/refused or a run blocks. No first-party identity-level issue → legitimate parent judgment → durable policy-return path is shipped.
- Why this is / is not agent-owned: An approval scanner and hard-coded safety rules do not constitute discretionary S5 ownership or a closed parent-governed S5 mode.
- Evidence: [policy.py#L801-L848](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/policy.py#L801-L848), [cli.py#L70-L145](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/cli.py#L70-L145), [system.md](https://github.com/CMABERY/agent-harness/blob/170d4c69a0c4b92c7de76ef8b362c5c4025a1786/agent/prompts/system.md).
- Basis: explicit + structural
- Confidence: medium-high.
- Caveats: An enterprise/operator parent could introduce governance around this harness, but it is outside the standard distribution under review.

### Absence scope

- Surfaces inspected: Prompt, CLI limit/options, policy/confirmation scanner, loop termination, workspace and published operating documentation.
- Plausible first-party paths checked: Human command confirmation, immutable safety rules, task stop and operator configuration.
- Why no material first-party path remains: These paths authorize or enforce ordinary operations, not a first-party ultimate-policy matter decided by a legitimate authority and returned as a governing identity change.

## Distributed OSS parent arrangement

The repository has maintainer development and test practices, but it does not ship those contributors or their CI as a governing parent inside a task's execution. A user's optional destructive command approval does not establish S3/S4/S5 parent closure at the assessed recursion.

## Self-hosted and non-human modes

Both the local scripted model and an operator-supplied OpenAI-compatible endpoint use the same first-party loop. The model's substantive tool choices are autonomous S1; the selected provider and human safety gate do not form an independent self-governing metasystem.

## Recursion

An optional one-level child agent executes a local subtask with a fresh conversation and shared run budget/ledger. Spawning it does not establish a separately viable recursion or S2 by itself.

## Variety and escalation

Tool feedback, command execution, optional child delegation and plan revision amplify local response variety. Schema checks, budgets, workspace restrictions and policy gates attenuate unsafe or invalid actions. Failed verification forces replan or a blocked outcome. These are operational safeguards; a stopped/blocked event is not automatically an algedonic, S3 or S5 decision.

## Evidence gaps

- No paid model-provider execution, live quality benchmark or independently commissioned S3* audit was performed. The source demonstrates structure and testable guardrails, not task-quality performance.
- The standard distribution exposes no specific portfolio of independently operating agent cells; additional multi-agent deployment, reviewer independence or human policy governance might exist in a consumer composition but is not credited here.
