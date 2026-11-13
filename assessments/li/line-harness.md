---
harness_id: line-harness
project_name: Line Harness
repository: https://github.com/LineLuLan/line-harness
review_ref: 63c98c60b18cfe603381890e104a043627b35ccf
reviewed_at: 2026-11-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Line Harness

## Review boundary

- System in focus: The shipped Line Harness operational harness with its documented external agent integration.
- Purpose and identity: Turn a user request into verified changes through a Claude Code supervisor and bounded Codex workers.
- Relevant environment: Windows development workspaces, shared files, concurrent workers, provider or sandbox failures, and human-controlled publication.
- Standard-distribution boundary: The restored Windows Claude Code/Codex configuration, shipped supervisor and worker instructions, PowerShell dispatch and review helpers, hooks and local job state.
- Credited operating / distribution surfaces: Supervisor rules, task packet workflow, path partition and dispatch lock, durable run status, independent diff review and bounded rework.
- Adjacent first-party surfaces excluded from ownership: Claude Code, Codex CLI and hosted inference are external agent implementations in the supported assembly. The optional marketplace rescue plugin, unrelated projects' CI and deployments, and external skill-bank source are outside the credited boundary.
- First-party operating / deployment modes considered: Documented installed Windows supervisor/worker mode using the bundled PowerShell helpers. Higher-risk work reaches the human approval boundary.
- Recursion level: The task team for one user-requested change, with worker cells operating on distinct packets and a supervisor regulating the shared delivery.
- Reviewed revision: `63c98c60b18cfe603381890e104a043627b35ccf`.
- Observation date: 2026-11-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The restore script copies supervisor and worker instructions and helper programs. The supervisor sends an outcome packet with scope and acceptance criteria. The dispatch helper invokes Codex with workspace controls and records run/session status, supports reconnect/cancel, and returns the worker's result. The review helper collects the current Git diff directly and can invoke a fresh reviewer after deterministic checks.

## Operational model

Codex worker sessions select and execute changes within their packets. The Claude supervisor chooses partitions, monitors jobs, combines results and directs remediation. The model review and supervisor validation can inspect the underlying diff and return actionable findings before the user-facing handoff.

## S1 — Operations

- State: A
- Function: Execute bounded coding or analysis tasks and deliver the resulting changes and evidence.
- Disturbance / variety regulated: Changing repository state, tool results, implementation errors, requirements and review feedback.
- Decisive decision or feedback right: Choose task-local tool actions, implementation and corrections within the packet.
- Decision owner: Codex worker in the shipped Claude supervisor/Codex worker assembly.
- Supporting / enforcement mechanisms: Task packet, dispatch helper, scoped directory, sandbox, session/exit records.
- Closure path: Supervisor dispatch → Codex selects actions and edits or analyzes → worker outputs and diff return → corrections can be sent in the existing worker session.
- Boundary reachability: Restore installs the supervisor/worker rules and helper. The documented standard path invokes Codex and makes its local output available to Claude.
- Why this is / is not agent-owned: The worker owns implementation discretion, while the shell and sandbox execute and constrain it.
- Evidence: [readme](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/README.md#how-it-works), [restore](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/restore.ps1#L7-L34), [role](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/codex/AGENTS.md#L7-L25), [dispatch](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/bin/codex-do.ps1), [supervisor](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/CLAUDE.md#L20-L38).
- Basis: explicit and structural
- Confidence: High for the composed source path.
- Caveats: The native agent loop is external. The finding is limited to the supported composition.

## S2 — Coordination

- State: A
- Distinct S1 units: Separate Codex worker sessions assigned distinct task packets, each responsible for its own repository changes.
- Inter-S1 disturbance: Concurrent edits to the same path in shared development work can destroy or overwrite each worker's work.
- Attenuating coordination relation: The supervisor partitions disjoint paths for parallel work and bundles conflicting scopes into a single worker. A directory lock rejects overlapping live helper dispatches.
- Feedback into subsequent S1 behaviour: The resulting scope and worker assignment are returned as new task packets. A refused dispatch exposes the active run for supervisor follow-up.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The coordination rule is tied to a named cross-worker interference and changes where or when the next worker acts.
- Function: Coordinate separately dispatched worker cells to prevent concurrent write interference on shared files.
- Disturbance / variety regulated: Two packets can target overlapping file paths and overwrite each other's edits. The shipped operating protocol names this concrete failure mode.
- Decisive decision or feedback right: Partition candidate packets by file ownership, allow parallel work when disjoint, and bundle overlapping work into one worker.
- Decision owner: Claude supervisor supplied by the installed agent mode.
- Supporting / enforcement mechanisms: Worker packet scope, dispatch directory lock, active-run record and supervisor visibility of workers.
- Closure path: Supervisor compares packet scopes → partitions or combines overlapping work → dispatches compatible packets → outcomes and blocked or live run information inform the next dispatch.
- Boundary reachability: Installed supervisor rules reference the shared delegation protocol and invoke the shipped dispatch helpers. The path-partition choice is given to the agent in normal delegation.
- Why this is / is not agent-owned: The supervisor makes the cross-worker assignment choice. The directory lock enforces a coarser runtime backstop.
- Evidence: [delegation](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/codex/AGENTS.md#L44-L65), [supervisor](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/CLAUDE.md#L20-L38), [dispatch](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/bin/codex-do.ps1), [lock](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/bin/codex-do.ps1#L874-L953).
- Basis: explicit operating protocol supported by executable lock and dispatch
- Confidence: Medium-high for the documented mode.
- Caveats: The lock is per directory. Path-level scope decisions depend on the supervisor, with no separate universal path-conflict oracle.

## S3 — Inside-and-now control

- State: A
- Whole-system current view: For the task team, the supervisor holds all outstanding packet obligations and receives the worker run inventory, current outcome and review status.
- Current-control decision scope: Decide which outstanding work is active, whether an attempt is stopped or reconnected, which failed packet is resumed or reissued, and when bounded rework escalates.
- Function: Regulate current commitments of the bounded task team by assigning work and intervening in stalled or rejected attempts.
- Disturbance / variety regulated: Concurrent outstanding packets, stale or failed runs, blocked work, invalid diffs and a bounded rework budget.
- Decisive decision or feedback right: Use current run state and outstanding packet obligations to continue, reconnect, cancel, revise a packet, or stop and escalate repeated failure.
- Decision owner: Claude supervisor acting on the task team as a whole.
- Supporting / enforcement mechanisms: Run status table, attach/cancel/resume commands, exit codes, review verdicts and human approval boundary for listed actions.
- Closure path: Current run states and review evidence reach the supervisor → supervisor selects a continue, cancel, corrective resume or escalation action → helper changes the live or next worker commitment.
- Boundary reachability: The installed supervisor instructions wire the helper commands, job statuses and remediation rules into the normal task-team procedure.
- Why this is / is not agent-owned: Job instrumentation reports state and executes intervention. The supervisor decides which commitment or attempt changes.
- Evidence: [role](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/codex/AGENTS.md#L7-L25), [delegation](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/codex/AGENTS.md#L44-L65), [supervisor](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/CLAUDE.md#L20-L38), [status](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/bin/codex-do.ps1#L793-L845), [dispatch](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/bin/codex-do.ps1), [review](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/CLAUDE.md#L69-L88).
- Basis: explicit operating role plus source-level intervention path
- Confidence: Medium-high for the bounded task team.
- Caveats: This finding does not extend to all projects or to authorizing publication, and assumes normal model adherence to the installed workflow.

## S3* — Complementary audit

- State: A
- Claim being audited: The worker delivered a change that meets the packet's acceptance criteria.
- Ordinary reporting path: The worker returns its completion report and dispatch output to the supervisor.
- Complementary access path: The helper reads the actual tracked and untracked Git diff independently of the worker report and supplies that evidence with the packet criteria.
- Independence boundary: Fresh reviewer session separate from the implementer transcript; the supervisor independently validates the actual result before handoff.
- Who acts on findings: The supervisor returns material findings to the worker for correction or escalates repeated failure. A later review starts fresh.
- Function: Inspect a worker's actual change independently of the worker's completion report and return corrective findings to the task team.
- Disturbance / variety regulated: A worker may claim completion despite a deficient diff or unmet acceptance criterion.
- Decisive decision or feedback right: Judge the underlying diff against acceptance criteria and, through the supervisor, decide whether rework is needed.
- Decision owner: Fresh review model for the supported review tier. The Claude supervisor separately owns the decision to accept or direct remediation.
- Supporting / enforcement mechanisms: Git diff captured by the helper, criteria extracted from the packet, fresh review context, separate supervisor validation and bounded retry.
- Closure path: Worker returns outcome → helper obtains independent diff evidence → fresh reviewer issues findings and verdict → supervisor checks the underlying change and routes failure into worker correction or escalation.
- Boundary reachability: The review helper is installed by restore and explicitly required for Important-tier work. The packaged supervisor protocol connects a failed review to fresh re-review after correction.
- Why this is / is not agent-owned: Review model owns the evidence judgment. The helper assembles evidence and parses the result, and the supervisor exercises current-control authority over the return.
- Evidence: [restore](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/restore.ps1#L7-L34), [review](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/CLAUDE.md#L69-L88), [diff](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/bin/codex-review.ps1#L254-L269), [verdict](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/bin/codex-review.ps1#L350-L442), [supervisor](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/CLAUDE.md#L20-L38).
- Basis: explicit review contract and source-level artifact access
- Confidence: Medium-high for the supported tier.
- Caveats: A fresh context can use the same model family. The first-party mode also documents supervisor verification. Lower tiers can omit the fresh model review.

## S4 — Outside-and-then intelligence

- State: —
- Function: No material prospective intelligence and capability decision loop is supplied for the task team.
- Disturbance / variety regulated: Tool/library updates, available models, quota and prior review defect rates can affect the team.
- Decisive decision or feedback right: Supervisors consult external documentation for current tasks. The weekly helper updates configured packages under a fixed rule, and the owner can revise review-tier policy after a ledger report.
- Decision owner: Task agent for current choices, deterministic updater for routine maintenance and human for external changes to operating rules.
- Supporting / enforcement mechanisms: Version lookup, config inventory validation and rollback, review ledger, model-selection rules.
- Closure path: Docs inform the current packet and version updates keep configured packages current. The review ledger counts internal defects; the inspected paths do not synthesize prospective external options for the team's capability.
- Why this is / is not agent-owned: Dependency refresh and internal quality statistics are distinct from future capability judgment at this recursion.
- Evidence: [updater](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/bin/mcp-weekly-update.ps1#L178-L215), [supervisor](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/CLAUDE.md#L20-L38), [review](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/CLAUDE.md#L69-L88), [restore](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/restore.ps1#L7-L34).
- Basis: bounded source review
- Confidence: Medium.
- Caveats: Weekly updates are documented as machine configuration and the restore script copies the helper. The code shows deterministic maintenance under a preset selection rule.

### Absence scope

- Surfaces inspected: Supervisor instructions, model routing, review ledger and weekly dependency updater.
- Plausible first-party paths checked: Registry version tracking, documentation retrieval, quota routing and defect-rate feedback into tier settings.
- Why no material first-party path remains: The first two serve maintenance or immediate tasks; ledger feedback evaluates internal review yield. No supplied path links external prospective sensing to an adaptation decision about the team's capability.

## S5 — Policy and identity

- State: —
- Function: No operational path adjudicates and returns a change to the task team's ultimate identity or policy.
- Disturbance / variety regulated: Some actions exceed delegated scope and require a human decision.
- Decisive decision or feedback right: The user authorizes a protected action while installed rules define the ordinary supervisor and worker mandates.
- Decision owner: Human for protected actions and configuration authors for standing policy.
- Supporting / enforcement mechanisms: Permission checks, scope instructions, protected-action gates and manual configuration.
- Closure path: A human can permit a specific action, while subsequent tasks continue under the existing standing policy.
- Why this is / is not agent-owned: The rules define and enforce a mandate; the protected-action response resolves a request within it.
- Evidence: [gates](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/codex/AGENTS.md#L117-L148), [role](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/codex/AGENTS.md#L7-L25), [restore](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/restore.ps1#L7-L34), [settings](https://github.com/LineLuLan/line-harness/blob/63c98c60b18cfe603381890e104a043627b35ccf/claude/settings.json).
- Basis: bounded source review
- Confidence: Medium-high.
- Caveats: The human can edit the installed policy externally. No ultimate-policy escalation/return procedure is evidenced in this assessed task-team mode.

### Absence scope

- Surfaces inspected: Restored policy files, role definitions, hooks and written-approval gates.
- Plausible first-party paths checked: User approval, deployment controls, role rules and policy configuration changes.
- Why no material first-party path remains: The inspected shipped paths settle permission for an action and apply authored policy without an identity-level issue-to-decision-to-operation loop.

## Distributed OSS parent arrangement

The human owner sets the authorization envelope and retains decisions about protected or outward-facing actions. The assessed team still performs ordinary local allocation, cancellation and rework through its supervisor. The protected-action gate does not supply an ultimate-policy decision loop.

## Self-hosted and non-human modes

The restored local configuration depends on installed CLIs, authenticated model access, Windows PowerShell and Git. Ordinary changes can be delegated and reviewed in the shipped assembly; publication and listed high-risk actions retain a human gate.

## Recursion

Separate worker and reviewer contexts serve one task team. The source does not show the worker sessions operating as independently governed viable organizations.

## Variety and escalation

Scope rules and local locks reduce conflicts, runtime receipts identify each attempt, and the supervisor can reconnect, cancel, resume or re-delegate. Repeated review failure returns to the human owner.

## Evidence gaps

The pinned scripts and installed instructions were examined statically. Windows dispatch, paid model calls and live review were not run. The positive S2/S3 results rely on the packaged supervisor operating protocol plus executable feedback and intervention paths; they are not guarantees that every model run follows the protocol.
