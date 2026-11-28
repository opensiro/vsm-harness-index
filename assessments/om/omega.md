---
harness_id: omega
project_name: OMega
repository: https://github.com/code10/OMega
review_ref: d9189cea97eff90d0b5d2563e082081491e5d8f8
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# OMega

## Review boundary

- System in focus: One running OMega installation, including the optional gateway and daemon shipped with the same package.
- Purpose and identity: Operate workspace tasks and configured background automations through model-directed tools.
- Relevant environment: Operator workspaces, configured providers, optional execution backends and external services.
- Standard-distribution boundary: Shipped CLI, gateway, daemon, worker, provider, tool, memory and verification code.
- Credited operating / distribution surfaces: Interactive and headless execution, supported gateway operator controls, persistent and detached workers, daemon automation.
- Adjacent first-party surfaces excluded from ownership: Development benchmarks, external provider internals, third-party plugins and external project maintainers.
- First-party operating / deployment modes considered: Interactive CLI, one-shot CLI, gateway with local or multiuser operation, and the daemon as foreground or native service.
- Recursion level: One installation and its operational commitments. Each independently executing worker is a nested operational cell.
- Reviewed revision: d9189cea97eff90d0b5d2563e082081491e5d8f8
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

OMega packages a TypeScript agent with a provider router, tool registry, execution backends, memory and checkpointing. The same distribution ships gateway operator controls, detached workers and scheduled automation. Provider fallback and execution backends are runtime mechanisms. The verification gate reads actual command results before the agent can complete qualifying edit runs.

## Operational model

The model selects task actions and revises them from tool observations. Detached workers have their own prompts and checkpoints. Gateway operators can see runs and intervene in active commitments. Worktrees, timers and budgets enforce selected constraints.

## S1 — Operations

- State: A
- Function: Produce a requested workspace result in the installed agent loop.
- Disturbance / variety regulated: Changing workspace state, incomplete task representations and failed tool calls.
- Decisive decision or feedback right: Choose the next workspace action from model output and determine when to propose completion.
- Decision owner: The configured model acting through the first-party OMega loop.
- Supporting / enforcement mechanisms: Provider and execution adapters, tool handlers, approval hooks and budget enforcement.
- Closure path: Tool results become messages in the same loop. A no-tool response enters synthesis and any applicable verification gate.
- Boundary reachability: The documented CLI and gateway entry points instantiate the bundled loop. Configuring a model backend does not require composing a task controller.
- Why this is / is not agent-owned: Removing the model leaves routing, tools and enforcement, but removes the discretionary workspace actions.
- Evidence: [README.md](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/README.md#L38-L58), [src/agent/runner.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/agent/runner.ts#L480-L495), [src/agent/runner.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/agent/runner.ts#L566-L591), [src/agent/runner.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/agent/runner.ts#L795-L836)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: The default offline provider and external provider capabilities vary. The claim is about the supplied model-driven path.

## S2 — Coordination

- State: —
- Function: Cross-worker interference regulation was sought among the detached and child work units.
- Disturbance / variety regulated: Concurrent writes and overlapping subtasks can affect a shared workspace.
- Decisive decision or feedback right: No closed inter-worker adjustment rule was found.
- Decision owner: The caller configures tasks and workspace isolation. Individual model loops own their own tasks.
- Supporting / enforcement mechanisms: Worktree partitioning, swarm identifiers, status and checkpoint storage.
- Closure path: The launch plan partitions workspaces before execution. Worker results do not feed a supplied inter-worker interference response.
- Why this is / is not agent-owned: Batch launch, isolation and status aggregation do not return conflict evidence to change the next choices of distinct workers.
- Evidence: [src/agent/detachedSwarm.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/agent/detachedSwarm.ts#L85-L109), [src/agent/detachedSwarm.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/agent/detachedSwarm.ts#L252-L278), [src/gateway/routes/agents.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/gateway/routes/agents.ts#L235-L281), [src/skills/subagent.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/skills/subagent.ts#L38-L64)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: An operator can avoid overlap by choosing separate worktrees.

### Absence scope

- Surfaces inspected: Detached swarm launch, child delegation, workspace isolation and gateway checkpoint status.
- Plausible first-party paths checked: Ownership conflict detection, shared resource negotiation, branch reconciliation and return of conflict findings to workers.
- Why no material first-party path remains: The supplied swarm routes launch and observe independent sessions. Worktree selection is an initial partition, with no supplied conflict-responsive coordination loop.

## S3 — Inside-and-now control

- State: P
- Function: Control the current portfolio of gateway commitments and whether an automated change enters the operational workspace.
- Disturbance / variety regulated: Active work can cease to be worthwhile, and isolated outputs can conflict with the current workspace.
- Decisive decision or feedback right: Select an active commitment to interrupt or choose whether a daemon run's workspace change is incorporated or discarded.
- Decision owner: Authorized gateway operator or administrator.
- Supporting / enforcement mechanisms: Run view, run controller, abort signal and isolated worktrees.
- Closure path: The chosen abort stops the addressed run. The daemon merge or discard action changes the destination workspace or removes the isolated result.
- Boundary reachability: The installed gateway exposes state, abort, worktree diff, merge and discard over first-party routes.
- Why this is / is not agent-owned: Runtime constructors enforce the operator's selection. They do not independently choose which active obligation to stop or which worktree outcome to accept.
- Whole-system current view: Gateway run state joins active and recent agent commitments. Daemon status and per-run diff expose the outputs subject to intervention.
- Current-control decision scope: Stop a selected active run and control whether the daemon's worktree changes enter the current workspace.
- Evidence: [src/gateway/routes/agents.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/gateway/routes/agents.ts#L14-L26), [src/gateway/routes/agents.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/gateway/routes/agents.ts#L65-L88), [src/gateway/agentManager.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/gateway/agentManager.ts#L525-L551), [src/gateway/agentManager.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/gateway/agentManager.ts#L1017-L1034), [src/gateway/routes/daemon.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/gateway/routes/daemon.ts#L154-L197)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: The documented headless mode by itself does not establish this parent-owned portfolio decision.

## S3* — Complementary audit

- State: C
- Function: Directly verify claims of completed work after an edit and return failed checks to the producer.
- Disturbance / variety regulated: A model can propose completion while the edited workspace still fails configured checks.
- Decisive decision or feedback right: Select the independent verification scope and what to require before accepting the edit.
- Decision owner: Operator or developer supplies the commands. The bundled verification gate executes them and returns actionable findings.
- Supporting / enforcement mechanisms: Mutated-file tracking, workspace command execution, result events and bounded retries.
- Closure path: A failed check inserts independent output into model context and resumes the edit loop while retries remain.
- Boundary reachability: The shipped task loop enables this path when post-edit verification commands are configured.
- Why this is / is not agent-owned: The producer proposes finalization and chooses repairs. The check gives complementary evidence but the shipped gate uses a preselected audit scope.
- Claim being audited: The edited workspace satisfies the checks imposed before task completion.
- Ordinary reporting path: The producing model returns its final response with no further tool calls.
- Complementary access path: Configured commands run against the edited workspace and return their own exit status and output.
- Independence boundary: The producing model cannot make a failing check pass by modifying its completion message. The auditor is a configured deterministic check.
- Who acts on findings: The runtime passes findings to the producing model for another edit attempt.
- Evidence: [src/agent/runner.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/agent/runner.ts#L101-L117), [src/agent/runner.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/agent/runner.ts#L480-L549)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: The retry limit and configured coverage bound assurance. The audit ledger alone does not qualify as this function.

## S4 — Outside-and-then intelligence

- State: —
- Function: Prospective capability adaptation was sought across the agent, daemon and evaluation surfaces.
- Disturbance / variety regulated: Provider and workload conditions can change beyond the current run.
- Decisive decision or feedback right: No supplied owner was found that selects and returns a prospective change from external evidence.
- Decision owner: Operators configure models and automation. The distiller runs its configured extraction and retention logic.
- Supporting / enforcement mechanisms: Configuration, provider routing, replay/eval and memory distillation.
- Closure path: Memory is compressed or retained for recall. Comparison findings do not feed a supplied prospective decision and enactment loop.
- Why this is / is not agent-owned: Tool repair and provider fallback respond to current failures. Distillation and offline eval do not by themselves choose a future operating configuration.
- Evidence: [src/daemon.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/daemon.ts#L272-L318), [src/selfImprove.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/selfImprove.ts#L12-L48), [src/eval.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/eval.ts#L60-L97), [src/gateway/routes/config.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/gateway/routes/config.ts#L21-L59)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: Memory can affect later prompts and operators can independently configure future runs.

### Absence scope

- Surfaces inspected: Daemon distillation, workflow promotion, provider configuration and replay/baseline evaluation.
- Plausible first-party paths checked: An outside trend or evaluation result selecting a future capability change and returning it through an autonomous or governed deployment path.
- Why no material first-party path remains: The distiller has a scheduled retention path. Promotion is a helper given a workflow and the evaluation surface supplies comparison evidence without a shipped adaptation decision and return.

## S5 — Policy and identity

- State: —
- Function: An ultimate identity or policy decision loop was sought within the installed runtime.
- Disturbance / variety regulated: Operational objectives or constraints can conflict.
- Decisive decision or feedback right: No supplied route elevates conflicting identity/policy matters to a legitimate policy decision and returns it to operations.
- Decision owner: The installer or administrator sets configuration and can choose a system prompt.
- Supporting / enforcement mechanisms: Static configuration, prompt injection at run setup and gateway authorization.
- Closure path: Settings govern subsequent calls, with no runtime identity-issue intake and resolution loop shown.
- Why this is / is not agent-owned: The model works under supplied objectives and policy. A configuration editor can apply a supplied setting without constituting policy judgment.
- Evidence: [README.md](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/README.md#L61-L75), [src/gateway/routes/config.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/gateway/routes/config.ts#L19-L72), [src/agent/runner.ts](https://github.com/code10/OMega/blob/d9189cea97eff90d0b5d2563e082081491e5d8f8/src/agent/runner.ts#L38-L61)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: Project-maintainer decisions are external to an installation.

### Absence scope

- Surfaces inspected: Gateway configuration, prompt initialization, operator permissions and agent/daemon run controls.
- Plausible first-party paths checked: Internal policy conflict judgment and a first-party parent identity issue with authoritative feedback.
- Why no material first-party path remains: Shipped endpoints set configured behavior and operate runs. They do not admit and return ultimate-policy decisions generated by the operating system under review.

## Recursion

A detached or child agent supplies a nested operational loop. The installation-level claims above cover the local gateway's current commitments; they do not extend to the business or OSS organization using the installation.

## Variety and escalation

Separate workspaces, limits, role checks, approval prompts and error recovery attenuate execution variety. Verification failures return to the producer. The evidence establishes ordinary operational intervention without an exceptional channel to an organizational parent.

## Evidence gaps

Static source review. No provider session, worker concurrency test, audit resistance test or live gateway intervention was executed. The configured checks and host access define the validity of each verification result.
