---
harness_id: bluecollar
project_name: bluecollar
repository: https://github.com/yeomyeonggeori/bluecollar
review_ref: 1aad1e6f77e7d81d9664df2e4461344aeac1a574
reviewed_at: 2026-11-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# bluecollar

## Review boundary

- System in focus: A bluecollar task harness with its first-party command-line and ACP wrappers.
- Purpose and identity: Execute unattended model-directed work and return grounded task outcomes.
- Relevant environment: A local tool host or ACP client, configured model provider, task store and requester authority.
- Standard-distribution boundary: Go kernel, first-party CLI/ACP commands and shared blueprotocol contracts at the recorded gitlink.
- Credited operating / distribution surfaces: First-party CLI tool and approval wiring, ACP hosting path, kernel and task outcome/ledger path.
- Adjacent first-party surfaces excluded from ownership: Benchmarks, tape/evaluation fixtures, development workflows, external ACP client/provider and optional host-supplied extensions beyond the shipped surfaces.
- First-party operating / deployment modes considered: CLI one-shot and REPL, ACP sessions, and embeddable kernel as a composition boundary.
- Recursion level: One task-running agent arrangement. Delegated child turns are scoped within the originating task.
- Reviewed revision: 1aad1e6f77e7d81d9664df2e4461344aeac1a574
- Observation date: 2026-11-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The CLI constructs its language-model provider, task storage, tool set, gate and kernel. The ACP wrapper receives its tool catalog and execution context through the client-facing path. Intake classifies the work and the kernel turns model actions and host observations into a task ledger. The completion path checks declared effects/attachments and can withhold completion or return a missing effect to the model.

## Operational model

The operating unit delivers task effects, artifacts, answers or an explicit waiting/blocked status. The model chooses task actions, including any permitted delegated operation. The host implements tools and requester isolation, while approval and completion rules constrain execution and claims.

## S1 — Operations

- State: A
- Function: Execute a submitted task and return evidence-backed changes, artifacts, a reply, or a named unresolved condition.
- Disturbance / variety regulated: Changing tool/effect requirements, incomplete user information, rejected completion and tool failures.
- Decisive decision or feedback right: Choose tool actions and repair work after failed actions or a completion refusal; issue the terminal answer.
- Decision owner: The configured execution model in a bluecollar task run.
- Supporting / enforcement mechanisms: Shipped request router and kernel, standalone CLI tool set, task ledger, approval checks and completion gate.
- Closure path: The host executes the chosen action under requester scope. Observations enter the task ledger and next model step. Completion checks can return unmet changes to the loop, or settle a completed, blocked or waiting outcome.
- Boundary reachability: The CLI builds task stores, registers tools, configures the provider and launches RunPlannedTurn in the checked-in entry point. The packaged ACP adapter also exposes the loop with host-supplied tools.
- Why this is / is not agent-owned: The model selects operational action and recovery after observations. Host approvals arbitrate particular effects and the kernel validates eligible completion.
- Evidence: [cmd/bluecollar/repl.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/cmd/bluecollar/repl.go#L38-L104), [cmd/bluecollar/main.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/cmd/bluecollar/main.go#L191-L207), [acpagent/agent.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/acpagent/agent.go#L116-L153), [loop/tool_invocation.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/loop/tool_invocation.go#L30-L101), [loop/completion_changes.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/loop/completion_changes.go#L16-L69), [DOCS.md](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/DOCS.md#L307-L323)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Core embedding depends on host composition. The positive judgement is grounded in the shipped executable CLI, with ACP constraints identified separately.

## S2 — Coordination

- State: —
- Function: No material inter-S1 coordination relation is shipped.
- Disturbance / variety regulated: A configured parent can request a bounded delegated task; a single action can also batch independent tool calls.
- Decisive decision or feedback right: No distinct function-specific decision or feedback right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Delegation limit, shared host tool/identity boundary, and synchronous parent-child invocation.
- Closure path: A child turn returns its result, attachment or failure to the parent as a task observation.
- Why this is / is not agent-owned: The optional child has an outcome contract, but parent selection and waiting supply task delegation without a specific inter-agent interference detector or correction loop.
- Evidence: [loop/delegation.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/loop/delegation.go#L13-L109), [DOCS.md](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/DOCS.md#L288-L297), [cmd/bluecollar/repl.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/cmd/bluecollar/repl.go#L38-L67)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Finding is bounded to the pinned first-party operating surfaces.

### Absence scope

- Surfaces inspected: Loop scheduling, action batching, delegation and CLI/ACP configuration.
- Plausible first-party paths checked: Agent coordination through delegated children, shared tools or parallel calls, including concurrent workspace work.
- Why no material first-party path remains: The inspected child path runs one scoped call and returns one outcome. No mechanism regulating conflicting current obligations or shared-resource contention between S1 units was found.

## S3 — Inside-and-now control

- State: —
- Function: No distinct inside-and-now whole-system control function is supplied.
- Disturbance / variety regulated: The kernel encounters elapsed budget, stalls, missing inputs and caller cancellation.
- Decisive decision or feedback right: No distinct function-specific decision or feedback right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Task-tier budget, approval pause, ACP cancellation and recovery caps.
- Closure path: A task continues within its allowance, pauses for an answer, or records a stop.
- Why this is / is not agent-owned: These are individual task gates and budget rules. The CLI, ACP host and embeddable interfaces do not supply a decision over portfolio priorities, resource redistribution or accountability.
- Evidence: [loop/agent_kernel.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/loop/agent_kernel.go#L690-L759), [loop/limit_stop.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/loop/limit_stop.go#L18-L76), [acpagent/agent.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/acpagent/agent.go#L250-L268), [DOCS.md](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/DOCS.md#L355-L367)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Finding is bounded to the pinned first-party operating surfaces.

### Absence scope

- Surfaces inspected: Task kernel, time budget/limit and failure recovery, ACP session cancellation and tool approvals.
- Plausible first-party paths checked: Current operating supervisor, model budget extension, operator decision on holding or cancelling tasks.
- Why no material first-party path remains: All examined returns alter the current task's admissible actions or terminal state. No whole-current intervention path is shipped.

## S3* — Complementary audit

- State: —
- Function: No complementary organizational audit function is established.
- Disturbance / variety regulated: A model may overstate completion or cite unsupported effects.
- Decisive decision or feedback right: No distinct function-specific decision or feedback right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Deterministic completion checks plus a separately configured decision model evaluating expected changes from the task record.
- Closure path: An unmet check requests more work or reports the missing user decision. Trace and ACP events expose the same recorded work.
- Why this is / is not agent-owned: The decision model is a meaningful separate task-quality check. It examines the active task ledger and returns to its own S1 completion gate. A complementary channel into independent operational evidence and organizational control was not found.
- Evidence: [loop/completion_changes.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/loop/completion_changes.go#L16-L69), [loop/completion_at_stop.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/loop/completion_at_stop.go#L11-L63), [cmd/bluecollar/repl.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/cmd/bluecollar/repl.go#L92-L104), [acpagent/ledger.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/acpagent/ledger.go#L60-L91), [DOCS.md](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/DOCS.md#L307-L319)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Finding is bounded to the pinned first-party operating surfaces.

### Absence scope

- Surfaces inspected: Completion checks, expected-change judgment, trace and ACP ledger forwarding, repository benchmark/eval material.
- Plausible first-party paths checked: Independent decision model, separate source observation, and possible corrective return beyond task completion.
- Why no material first-party path remains: Completion judgment uses in-band tool observations and governs acceptance of the current task. The runtime supplies no separate audit of a current organizational control claim.

## S4 — Outside-and-then intelligence

- State: —
- Function: No outside-and-then capability adaptation is established.
- Disturbance / variety regulated: Different task difficulty, host context and available instructions change what one task needs.
- Decisive decision or feedback right: No distinct function-specific decision or feedback right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Task-tier selection, context compaction and ACP host-supplied instruction/skill bundles.
- Closure path: Current task configuration and later inputs incorporate the chosen instructions and checkpoint or host context.
- Why this is / is not agent-owned: Dynamic instruction availability and tier selection tailor current work. They do not identify a future environmental shift, propose capabilities and return an adopted capability decision.
- Evidence: [loop/agent_kernel.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/loop/agent_kernel.go#L534-L554), [loop/agent_kernel.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/loop/agent_kernel.go#L844-L925), [acpagent/skills.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/acpagent/skills.go#L16-L55), [DOCS.md](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/DOCS.md#L375-L387)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Finding is bounded to the pinned first-party operating surfaces.

### Absence scope

- Surfaces inspected: Intake, task tiers, skill routing/loading, context compaction and benchmark surfaces.
- Plausible first-party paths checked: Autonomous or host-governed prospective adaptation, capability adoption and follow-on runtime implementation.
- Why no material first-party path remains: The shipped adjustments are request/host-driven context and budget choices. Development evaluations are outside the operating boundary.

## S5 — Policy and identity

- State: —
- Function: No policy and identity adjudication loop is supplied inside the assessed runtime.
- Disturbance / variety regulated: The host declares who the agent is, what tools it can run, and who can approve an effect.
- Decisive decision or feedback right: No distinct function-specific decision or feedback right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: AgentIdentity in the request, host-side tool authority and ACP instruction handoff.
- Closure path: The kernel consumes declared configuration and tool/approval constraints.
- Why this is / is not agent-owned: Host identity and permission declarations apply to operation. The declared dependency does not implement a first-party loop for settling ultimate identity or policy disputes.
- Evidence: [cmd/bluecollar/repl.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/cmd/bluecollar/repl.go#L70-L90), [acpagent/skills.go](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/acpagent/skills.go#L16-L55), [DOCS.md](https://github.com/yeomyeonggeori/bluecollar/blob/1aad1e6f77e7d81d9664df2e4461344aeac1a574/DOCS.md#L170-L205)
- Basis: Pinned first-party source inspection.
- Confidence: high
- Caveats: Finding is bounded to the pinned first-party operating surfaces.

### Absence scope

- Surfaces inspected: CLI launch parameters, ACP host instructions, request identity, and tool approval.
- Plausible first-party paths checked: Internal identity revision or explicit parent settlement with an attributable return route.
- Why no material first-party path remains: The runtime treats identity and authority as externally provided fields and enforcement policy. No shipped policy issue-to-decision loop was established.

## Recursion

The local task runtime is assessed at its own recursion. Optional children perform contained portions of the same job under host identity, and their results enter the parent turn. An embedding host's wider organization is outside scope.

## Variety and escalation

The loop handles malformed actions, rejected completion and stalled progress with bounded repair, asks for missing user information, and records terminal failure or cancellation as needed. No separate algedonic path was established.

## Evidence gaps

Pinned public source inspection only. No real provider or ACP sessions were run. Host-specific organizational arrangements and deployment claims are outside the established boundary.
