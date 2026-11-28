---
harness_id: vieforge
project_name: VieForge
repository: https://github.com/vieforge/vieforge
review_ref: 9a4b7665326909f6ffd8e0e89dbf16505d0ad373
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# VieForge

## Review boundary

- System in focus: A workstation installation of VieForge with the first-party orchestration skill loaded in a supported model host and with its local MCP worker.
- Purpose and identity: Complete batch or workspace jobs while moving repetitive work to lower-cost local execution and recovering from bounded failures.
- Relevant environment: A compatible coding-agent host and provider, local workspaces, SQLite and optional Ollama and GPU services.
- Standard-distribution boundary: The packaged Python distribution, documented skill and MCP installation, and first-party worker and support code.
- Credited operating / distribution surfaces: Installed orchestration skill, local MCP tools, batch input and result contracts, cross-process coordination primitives and repair CLI.
- Adjacent first-party surfaces excluded from ownership: Benchmark and repository QA, third-party model and host internals, external browser provider, optional companion programs and maintainer governance.
- First-party operating / deployment modes considered: Skill with MCP worker in a compatible host. Standalone worker/CLI and manual architect handoff were inspected as separate configurations.
- Recursion level: Installed workflow over individual jobs. Independent project installations can interact at the shared workstation-resource boundary.
- Reviewed revision: 9a4b7665326909f6ffd8e0e89dbf16505d0ad373
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The wheel bundles the skill, instructions and worker. The installer registers a skill in the selected host's supported directory and emits client-native MCP configuration. The installed model follows the staged routing workflow. The MCP worker checks the environment, invokes an isolated command or local batch, returns compact summaries, and stores item outcomes and costs. The CLI also provides separate diagnostic and approval-gated repair operations.

## Operational model

In the supported integrated path, the active model chooses how to carry out an assigned job with the supplied tier and exception rules. Local model extraction, subprocesses and SQLite checkpoints support that operation. The standalone CLI and batch operation execute one requested tool or transformation. A human retains any required approval for spending and explicit repair application.

## S1 — Operations

- State: A
- Function: Carry out an input job by choosing local tools, interpreting responses and resuming after correction.
- Disturbance / variety regulated: Variable job shape, model failures, different item results and interrupted work.
- Decisive decision or feedback right: Select a tier and executable tool path, decide what failed, adjust execution and continue from accepted checkpoints.
- Decision owner: The active model running the installed first-party orchestration skill.
- Supporting / enforcement mechanisms: Host inference and tool transport, skill routing and recovery rules, the registered MCP worker and durable per-item state.
- Closure path: The worker returns item status and cost evidence to the active model. The installed procedure guides the model to inspect failed items, choose a correction and resume from checkpoints until the work is reported.
- Why this is / is not agent-owned: The first-party distribution supplies the operational procedure, tool endpoints, feedback schema and corrective return. The host supplies the standard model and tool execution substrate.
- Boundary reachability: The documented installation loads the project-owned procedure and exposes the project-owned worker methods to the same model turn. No developer-authored orchestration glue is needed for the supported skill/MCP mode.
- Evidence: [pyproject.toml](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/pyproject.toml#L50-L72), [scripts/install_skill.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/scripts/install_skill.py#L146-L159), [scripts/install_skill.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/scripts/install_skill.py#L195-L213), [AGENT_INSTALL.md](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/AGENT_INSTALL.md#L7-L29), [skills/three-tier-orchestrator/SKILL.md](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/skills/three-tier-orchestrator/SKILL.md#L10-L30), [scripts/mcp_server.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/scripts/mcp_server.py#L248-L299), [scripts/mcp_server.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/scripts/mcp_server.py#L466-L473)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: The state is scoped to the installed orchestration skill and bound MCP tools in a supported agent host. The standalone batch script has no general task-control loop.

## S2 — Coordination

- State: C
- Function: Attenuate interference between independently run projects competing for one workstation's GPU.
- Disturbance / variety regulated: Two active operational workflows can start heavy GPU work against the same device and exhaust memory or contend for capacity.
- Decisive decision or feedback right: Select the exclusive GPU launch path and coordinate which operations share the same machine lock.
- Decision owner: The integrating caller composes the competing workflows and chooses the execution flag.
- Supporting / enforcement mechanisms: An OS-level shared lock exists for heavy child runs. The optional GPU flag holds it from launch until completion and returns a normal subprocess result. The supplied local batch also leases a shared model across active work.
- Closure path: A second exclusive GPU operation waits for the first to release the lock. Result or timeout returns to its caller, which can proceed, defer or choose a different tier.
- Why this is / is not agent-owned: The supplied device-contention path is specific to the disturbance. The integrating caller supplies an autonomous cross-project actor and chooses where to apply it.
- Boundary reachability: The wheel ships the GPU-serialized subprocess path, and the first-party operating instructions specify its use for co-resident heavy workloads.
- Distinct S1 units: Two independent project-level installed agent workflows sharing the local GPU.
- Inter-S1 disturbance: Concurrent heavy subprocesses can compete for memory on one device.
- Attenuating coordination relation: The shared GPU file lock delays a competing opted-in workload until the active subprocess releases it.
- Feedback into subsequent S1 behaviour: The subprocess result or acquisition failure returns to its caller. Starting the next workload is controlled by the lock's release.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The named device-wide coordination scope, specific exclusion condition and runtime return target GPU contention across independent projects.
- Evidence: [README.md](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/README.md#L142-L149), [AGENTS.md](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/AGENTS.md#L5-L14), [core/concurrency.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/core/concurrency.py#L129-L189), [core/subprocess_runner.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/core/subprocess_runner.py#L104-L120), [core/subprocess_runner.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/core/subprocess_runner.py#L203-L217), [scripts/mcp_server.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/scripts/mcp_server.py#L61-L81)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: The standard generic MCP command wrapper does not set the explicit exclusive GPU option. The reference-counted Ollama lease witness adds no guarantee of all device use being serialized.

## S3 — Inside-and-now control

- State: —
- Function: Whole-current control across live active projects or agent commitments was sought.
- Disturbance / variety regulated: Independent jobs can run short of shared capacity or call for changed priorities.
- Decisive decision or feedback right: No shipped actor uses a whole-current view to change resource allocations or commitments across the installation.
- Decision owner: Each host agent handles its own job. An operator decides scoped spend or patch approvals.
- Supporting / enforcement mechanisms: Job summaries, checkpointing, daily spend ledger, estimates, approval gates and snapshots.
- Closure path: A guard decides whether another item or isolated action is permitted. The workflow can patch and resume its current job.
- Why this is / is not agent-owned: A spend counter or a local approval changes one job under preselected limits. A whole-current reprioritization feedback loop was not found.
- Evidence: [README.md](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/README.md#L43-L58), [skills/three-tier-orchestrator/SKILL.md](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/skills/three-tier-orchestrator/SKILL.md#L17-L30), [scripts/mcp_server.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/scripts/mcp_server.py#L84-L98), [scripts/mcp_server.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/scripts/mcp_server.py#L248-L299), [core/pipeline_runner.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/core/pipeline_runner.py#L30-L68), [core/repair_loop.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/core/repair_loop.py#L253-L281)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: No independent workspace portfolio control was demonstrated.

### Absence scope

- Surfaces inspected: Tier selection, local and per-job state, shared spend and capacity enforcement, repair and spend approval.
- Plausible first-party paths checked: A model or authorized parent uses a whole-current view to redistribute active capacity or adjust standing commitments.
- Why no material first-party path remains: Study of the supplied controls found decisions local to inputs, jobs or patch authorizations. Shared enforcement and monitoring do not supply whole-current authority and return.

## S3* — Complementary audit

- State: —
- Function: Complementary audit of a current workflow's performance claim was sought.
- Disturbance / variety regulated: A worker's compact report can omit context or claim successful operation that is not justified.
- Decisive decision or feedback right: No first-party complementary audit loop selects or challenges the operational claim and returns findings to a governing controller.
- Decision owner: The worker produces results. Operators can request patch verification or run separate QA.
- Supporting / enforcement mechanisms: Workspace snapshots, read-only diff views, verification and rollback after an applied patch, and an exported evaluation prompt.
- Closure path: Ordinary verification reports a code and may roll back the scoped patch. The project auditor exports evidence usable by another process.
- Why this is / is not agent-owned: The verifier checks the same patch in its normal repair path. Generic diff access and exported review prompts do not instantiate a complementary audit role and return.
- Evidence: [scripts/mcp_server.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/scripts/mcp_server.py#L354-L392), [core/repair_loop.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/core/repair_loop.py#L291-L360), [core/step_auditor.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/core/step_auditor.py#L500-L535), [README.md](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/README.md#L183-L203)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: The project can be audited independently using the exposed artifacts.

### Absence scope

- Surfaces inspected: Repair verify/rollback, workspace evidence and impact views, project audits and manual architect handoff.
- Plausible first-party paths checked: A separate supplied inspection of a named current job claim with a binding corrective result to the installation's control.
- Why no material first-party path remains: The repair verifier is a regular safety step, and the exported evaluator requires a separate process whose judgments are not wired back to operational control.

## S4 — Outside-and-then intelligence

- State: —
- Function: Select and adopt a future operational capability in response to external variation.
- Disturbance / variety regulated: Different projects can repeat verified failures and the workspace environment can change.
- Decisive decision or feedback right: No supplied mechanism admits a selected playbook or prospective change back into the installed operator workflow.
- Decision owner: The current model retrieves prior repair evidence. An operator may manually generate or edit a playbook.
- Supporting / enforcement mechanisms: Persistent incident memory, cross-project lesson harvest, optional Markdown export and static skill loading.
- Closure path: The repair tools retrieve stored fixes when diagnosing another incident. The export provides a file for possible external use.
- Why this is / is not agent-owned: The supplied playbook generation creates options without a governing or operational return into the installed skill.
- Evidence: [core/repair_loop.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/core/repair_loop.py#L173-L183), [core/repair_loop.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/core/repair_loop.py#L328-L340), [scripts/mcp_server.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/scripts/mcp_server.py#L312-L350), [scripts/eval_repair.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/scripts/eval_repair.py#L35-L69), [core/repair_eval.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/core/repair_eval.py#L467-L492), [scripts/install_skill.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/scripts/install_skill.py#L146-L159)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: A model can reuse evidence when an error recurs. Durable adoption of updated future operating rules is a separate capability.

### Absence scope

- Surfaces inspected: Repair memory, documented cross-project harvest and playbook export, and the installed skill's load path.
- Plausible first-party paths checked: A supported autonomous or parent-guided decision that selects the external lesson and binds a changed policy or capability for upcoming tasks.
- Why no material first-party path remains: The playbook is emitted as a report, and ordinary skill installation copies packaged source instructions. No supplied adapter feeds a selected learned rule into that installation.

## S5 — Policy and identity

- State: —
- Function: Resolve an identity or ultimate-policy choice for the operating installation.
- Disturbance / variety regulated: A task can conflict with local-first constraints or an operator's action policy.
- Decisive decision or feedback right: No issue-to-governing-authority loop adjudicates a proposed change to those constraints and returns it to the installation.
- Decision owner: The distributed skill sets default guardrails. The user supplies local action parameters and authorizations.
- Supporting / enforcement mechanisms: Static routing rules, role action allowlists, policy logs, budget settings and optional external callbacks.
- Closure path: The configured policy guard accepts or rejects an action or records its decision.
- Why this is / is not agent-owned: Command permission and optional extension points apply existing policy. No native authority arbitrates an identity-level case.
- Evidence: [skills/three-tier-orchestrator/SKILL.md](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/skills/three-tier-orchestrator/SKILL.md#L17-L30), [core/policy_guard.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/core/policy_guard.py#L63-L89), [core/policy_guard.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/core/policy_guard.py#L91-L116), [core/pipeline_runner.py](https://github.com/vieforge/vieforge/blob/9a4b7665326909f6ffd8e0e89dbf16505d0ad373/core/pipeline_runner.py#L58-L68)
- Basis: Static inspection of pinned first-party source.
- Confidence: medium
- Caveats: External enterprise policy integration and project governance are outside the shipped operating boundary.

### Absence scope

- Surfaces inspected: First-party skill guardrails, role authorization and policy logs, approval gates, external callback interfaces.
- Plausible first-party paths checked: A supported parent or autonomous route for a governing policy dispute and return of its decision to subsequent operations.
- Why no material first-party path remains: Every observed authority path sets configuration or applies it to a single action. No first-party identity-policy adjudication loop was established.

## Recursion

The installed host agent operates each job. Local inference and subprocesses are execution supports. Separate project-level agents remain distinct units where they contend for shared workstation resources.

## Variety and escalation

Typed result fields, item checkpoints, process locks and budget gates attenuate task variety. The repair loop can stop at repeat failure and request review. The observed paths escalate job-level exceptions.

## Evidence gaps

Source inspection only. No model, agent host, MCP server, GPU, repair or payment path was executed. Positive ownership is specific to the declared installed distribution. The CLI and optional manual handoff are distinct modes.
