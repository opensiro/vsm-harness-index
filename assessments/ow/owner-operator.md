---
harness_id: owner-operator
project_name: Owner Operator
repository: https://github.com/lhotwll217/owner-operator
review_ref: 430e152441af7e2d72fdd392feab627ab2a36f8d
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A(P)
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: P
---

# Owner Operator

## Review boundary

- System in focus: One Owner Operator installation on macOS and its managed parent-thread fleet.
- Purpose and identity: Support the owner by tracking ongoing coding work, finding relevant history and delegating or steering coding runs.
- Relevant environment: Owner, local coding harnesses and their transcripts, ACP adapters and externally provided model/account capabilities.
- Standard-distribution boundary: First-party agent, daemon, CLI, scheduler, state and widget. Only OO-issued child turns count as governed operations.
- Credited operating / distribution surfaces: [Agent](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/docs/agent.md) · [Daemon](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/docs/daemon.md) · [Delegated runs](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/docs/delegated-runs.md) · [Widget](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/docs/widget.md)
- Adjacent first-party surfaces excluded from ownership: Standalone downstream harness internals, unrelated observed sessions, evaluation rigs and repository maintainer workflow.
- First-party operating / deployment modes considered: Interactive and headless owner sessions, daemon-backed ACP delegation and scheduled sessions.
- Recursion level: One managed fleet from the parent conversation. Installation-wide settings delimit its ultimate authority.
- Reviewed revision: 430e152441af7e2d72fdd392feab627ab2a36f8d
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The Pi-backed Operator runs model sessions with a bounded tool configuration. A local daemon issues durable ACP runs, persists lineage and terminal results, and projects state to the CLI, parent conversation and widget. Owned session and run records are joined to observational transcript scans without conflating those identities. Separate schedules open fresh Pi sessions.

## Operational model

Operational units include the model-directed Operator turn and the externally backed coding tasks launched and tracked through the daemon. Within a managed parent fleet, Operator and owner modes can change dispositions of current runs. Adapter capabilities inform future delegated baselines, whose durable authorization stays with the owner.

## S1 — Operations

- State: A
- Function: Run a model-directed operational task and hand back tool or child results.
- Disturbance / variety regulated: Requests, tool outcomes and delayed delegated results vary across live work.
- Decisive decision or feedback right: Choose task actions or delegate a concrete unit of work and decide what to do with its result.
- Decision owner: Operator session model and task-local child models.
- Supporting / enforcement mechanisms: Pi tool path, permission guard, daemon lifecycle ledger and ACP execution.
- Closure path: Tool results return in the running session; delegated results enter the saved parent conversation with durable provenance.
- Why this is / is not agent-owned: The Operator selects task actions and the daemon executes authorized requests.
- Boundary reachability: The supported CLI and scheduled sessions construct the same first-party Operator session, whose tools can reach the daemon.
- Evidence: [Operator session](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent/agent.ts) · [Owned delegation](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/docs/delegated-runs.md) · [Execution](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent-runs/executor.ts)
- Basis: structural
- Confidence: high
- Caveats: Source evidence of reachable execution, with no new model or macOS runs.

## S2 — Coordination

- State: —
- Function: Attenuate interaction conflicts between peer S1 work units.
- Disturbance / variety regulated: Delegated runs can compete for execution slots and may share a workspace.
- Decisive decision or feedback right: No specific autonomous or composable work-conflict resolution path was established.
- Decision owner: The runtime owns slot admission; the parent selects delegation and workspace.
- Supporting / enforcement mechanisms: Global cap, transactional run claim, workspace resolution, event delivery and nested continuation.
- Closure path: Slots becoming available admit pending rows. The nearest parent gets terminal outcomes.
- Why this is / is not agent-owned: The reviewed slot cap and lifecycle sequencing supply generic admission, with no peer-work correction relation shown.
- Evidence: [Delegation controls](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/docs/delegated-runs.md) · [Nested continuation](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent-runs/nested-planner.ts) · [Worktree runtime](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent/worktree-runtime.ts)
- Basis: structural
- Confidence: medium
- Caveats: Peer overlap avoidance through external harness features is outside the declared authority boundary.

### Absence scope

- Surfaces inspected: Daemon run execution and slot controls, worktree selection, parent lineage and continuation delivery.
- Plausible first-party paths checked: Fixed global run cap, inherited workspace choice, overlapping child work and nested result delivery.
- Why no material first-party path remains: Those paths admit, place or resume runs. The supplied policy does not identify and return a specific sibling interaction correction to the affected operations.

## S3 — Inside-and-now control

- State: A(P)
- Function: Change current work commitments across the managed parent fleet.
- Disturbance / variety regulated: Parallel runs can fail, lose a process, finish out of order or need an altered commitment.
- Decisive decision or feedback right: Select a run to cancel, retry or resume and determine a subsequent work requirement after overall fleet outcomes.
- Decision owner: Parent Operator model in its own conversation or the owner using the installed run controls.
- Supporting / enforcement mechanisms: Durable fleet list, completion delivery, continuation eligibility, strict identity and deadline enforcement.
- Closure path: A selected disposition cancels the prior run or creates a durable successor associated with the same work and re-enters execution.
- Why this is / is not agent-owned: An operating model can interpret fleet evidence and choose the disposition. In the separate direct mode, the owner exercises that discretion.
- Boundary reachability: The daemon reports the entire parent-thread fleet, injects completions into Pi, and serves the same run mutation surface to owner CLI clients.
- Whole-system current view: The parent thread's complete durable managed run fleet plus terminal outcomes and child lineage.
- Current-control decision scope: Cross-run intervention in the current managed portfolio by cancel, retry or resume, with changed successor work where selected.
- Evidence: [Fleet and direct controls](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/docs/delegated-runs.md) · [Parent session](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent-runs/parent-run-session.ts) · [CLI controls](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/cli/operations/runs.ts) · [Continuation](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent-runs/continuation.ts)
- Basis: structural
- Confidence: medium
- Caveats: The claim is scoped to the managed parent fleet and excludes unrelated observed local sessions.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Parent Operator model | Fleet run outcome or active intervention request | Model-selected run control updates a commitment through the daemon. | [Delegated run execution](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/docs/delegated-runs.md) · [Parent session](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent-runs/parent-run-session.ts) |
| Parent (`P`) | Owner | Direct review of the current portfolio and its eligible controls | CLI selection changes run state or issues its validated successor. | [Run controls](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/cli/operations/runs.ts) · [Executor](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent-runs/executor.ts) |

## S3* — Complementary audit

- State: —
- Function: Independently challenge substantive claims about managed work.
- Disturbance / variety regulated: A child might report success despite a deficient task result.
- Decisive decision or feedback right: No independent task verifier with a return-to-correction relation was established.
- Decision owner: Managed child returns ordinary task outcome; daemon projects lifecycle and monitor classifies transcript state.
- Supporting / enforcement mechanisms: Run receipts, transcript scanner, summary enrichment and status reconciliation.
- Closure path: Ordinary results feed the parent. Transcript monitoring updates observed activity.
- Why this is / is not agent-owned: A separate status projection evidences session activity, while the inspected paths do not independently check a substantive delivered-work claim.
- Evidence: [Transcript monitor](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/session-monitor/monitor.ts) · [Enrichment](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent/enrichment.ts) · [Owned reporting contract](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/docs/delegated-runs.md)
- Basis: structural
- Confidence: medium
- Caveats: Capability probes apply to adapter selection and startup identity rather than independent checks of finished work.

### Absence scope

- Surfaces inspected: Run ledger and follow-up delivery, transcript monitor and status enrichment, product evaluation documentation.
- Plausible first-party paths checked: Raw transcript status versus run completion, and replay of child result evidence into the parent.
- Why no material first-party path remains: The transcript path informs activity status, and the ordinary parent receives the run evidence. No distinct auditor which challenges a work claim and sends its finding into managed corrective execution is wired here.

## S4 — Outside-and-then intelligence

- State: P
- Function: Choose a durable default for future delegation using current externally advertised capabilities.
- Disturbance / variety regulated: Adapter model and effort options or allowance can differ from the existing baseline.
- Decisive decision or feedback right: Approve a proposed harness/model/effort baseline after observing real adapter options.
- Decision owner: Owner decides the lasting baseline; the agent can request observation and present the candidate.
- Supporting / enforcement mechanisms: Disposable ACP inspection, explicit consent, atomic baseline file, launch-time resolution.
- Closure path: Owner's decision persists the accepted baseline. A later missing-field launch applies it after checking capability evidence.
- Why this is / is not agent-owned: The launch path applies the stored owner-approved choice, with the agent allowed to present and propose options.
- Boundary reachability: First-party harness details/propose/approve routes and launch configuration are available in the normal app and delegation CLI.
- External distinction: The active ACP adapter's current model/effort options, contrasted with an existing or absent approved baseline.
- Future / prospective distinction: A baseline changes which execution identity can be used by future unpinned delegated runs.
- Adaptation option generated: A live unpinned capability probe yields an exact candidate harness, model and effort for owner review.
- Path back into current capability / S3: Accepted baseline is stored and supplies future launch defaults through the managed executor.
- Evidence: [Observation and approval](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/docs/delegated-runs.md) · [Probe](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent-runs/harness-details.ts) · [Consent workflow](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent/skills/select-harness-for-delegation/SKILL.md) · [Launch resolution](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent-runs/launch-config.ts)
- Basis: structural
- Confidence: medium
- Caveats: This is an on-demand, owner-approved adaptation route. Automatic forecasting and unattended rewriting of defaults remain outside the claim.

## S5 — Policy and identity

- State: P
- Function: Set the enduring data and tool authority of a local installation.
- Disturbance / variety regulated: New transcript sources and operational use raise questions about whether the Operator may observe or change local resources.
- Decisive decision or feedback right: Decide which transcript source classes are in scope and choose the installation-wide permission posture.
- Decision owner: Installation owner in the interactive review and permission commands.
- Supporting / enforcement mechanisms: Catalog review, settings persistence, prompt reload and permission enforcement.
- Closure path: Saved selections constrain session discovery and subsequent tool behavior; reloading applies the updated tool posture.
- Why this is / is not agent-owned: The first-party permission interaction and source review return durable human selections to the runtime.
- Boundary reachability: Interactive onboarding and the installed permission command operate on the same home/settings read by the live Agent and scanner.
- Identity / ultimate-policy issue: Whether the installation can inspect particular local transcript domains and act against local resources under a standing posture.
- Ultimate authority in each claimed mode: The owner decides the permitted scope. The model exercises delegated rights within it.
- Return-to-operation path: Review selections and permission mode are persisted, consumed by the monitor and reapplied by the agent reload.
- Evidence: [Onboarding](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent/onboarding.ts) · [Permission choice](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent/permission-settings.ts) · [Agent binding](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/src/agent/agent.ts) · [Local session sources](https://github.com/lhotwll217/owner-operator/blob/430e152441af7e2d72fdd392feab627ab2a36f8d/docs/sessions.md)
- Basis: structural
- Confidence: medium
- Caveats: The standing installation scope supports the claim. Individual command approvals alone do not establish ultimate policy.

## Recursion

An installation contains managed parent-thread fleets and child sessions. Observed sessions outside the owned lineage supply environment data, not governed child operations.

## Variety and escalation

Terminal events feed the parent. Owner intervention changes selected current runs, while absent or stale delegated baselines can reach the owner for a lasting decision.

## Evidence gaps

No fresh live macOS or provider execution was performed. Individual harness/provider continuation capabilities vary. The assessment concerns the shipped grounding and boundaries of the OO-owned paths.
