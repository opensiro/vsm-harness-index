---
harness_id: devspace
project_name: DevSpace
repository: https://github.com/Waishnav/devspace
review_ref: 559781284677e5b128aa44a2c95f8bdb0c72b7c0
reviewed_at: 2026-11-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# DevSpace

## Review boundary

- System in focus: One local DevSpace coding workspace and its managed worker/workflow cell, in the published npm mode that reaches the packaged Pi dependency and DevSpace tool extension.
- Purpose and identity: Run user- or host-requested coding and review work in owner-authorized workspace environments and keep managed worker outcomes inspectable.
- Relevant environment: Local owner, project checkout and worktrees, model inference accounts, file/command outcomes and optional external caller agents.
- Standard-distribution boundary: DevSpace CLI and daemon, distributed Pi execution dependency, first-party adapter/tool extension, worktrees, review checkpoints and opt-in workflow controls. Independent MCP host and separately installed CLI modes are adjacent.
- Credited operating / distribution surfaces: DevSpace Pi driver, workspace-bound tools, managed workers, workflow group controls, checkpoints and included profile/Skill construction material.
- Adjacent first-party surfaces excluded from ownership: Provider organizations, separate external MCP orchestrator, user-installed agents, developer-only QA/replays as operating actors and repository/website maintenance.
- First-party operating / deployment modes considered: Local direct CLI with the supplied Pi fallback and configured model; parallel writer worktrees; experimental managed workflow mode with owner controls; separately composed read-only review mode.
- Recursion level: One managed workspace coding cell with directly managed worker turns and optionally one bounded workflow group. No claim over unrelated workspaces or the external host’s own operations.
- Reviewed revision: 559781284677e5b128aa44a2c95f8bdb0c72b7c0.
- Observation date: 2026-11-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

DevSpace supplies a local daemon and MCP/CLI interfaces, records provider sessions and scoped turns, and manages isolated worktrees and review snapshots. One supported local adapter resolves a configured Pi override or a system binary, then explicitly falls back to the Pi package installed as a production dependency. It starts that executable as a managed RPC child with the first-party workspace tool extension in restricted modes. DevSpace submits the brief, retains session identity and returns the model/tool result. The experimental workflow runner executes caller-authored composition and keeps call records, cancellation ownership and bounded replay state. External host and externally installed providers remain separate deployment variants.

Evidence: [README.md](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/README.md), [package.json](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/package.json), [local-agent-pi.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-pi.ts), [local-agent-pi-rpc.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-pi-rpc.ts), [local-agent-pi-sandbox.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-pi-sandbox.ts), [local-agent-manager.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-manager.ts), [workflow-manager.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/workflow-manager.ts).

## Operational model

A commissioned bundled Pi worker is the autonomous operating actor in the credited mode. The supplied workspace extension participates in file/tool closure, and DevSpace owns admission and result transport. Multiple writers can use isolated branches and return branch/checkout identity. Owner-defined workflow composition or an external caller can decide how to integrate work and how to respond to review reports.

## S1 — Operations

- State: A
- Function: Produce a coding, investigation or review result with the packaged Pi worker under DevSpace’s scoped workspace mode.
- Disturbance / variety regulated: A code/task brief and changing tool results require model decisions about source inquiry and work outputs.
- Decisive decision or feedback right: Choose the next project read, edit, command or response based on the requested outcome and previous results.
- Decision owner: Pi model-backed actor in the explicitly wired, dependency-bundled DevSpace operating mode.
- Supporting / enforcement mechanisms: Daemon turn and session state, Pi RPC, provider transport, local project tool extension and permission mode.
- Closure path: DevSpace submits the task to the packaged actor, Pi executes the model/tool turns through the scoped environment, and the daemon captures and returns the result and retains session identity.
- Boundary reachability: The package directly declares Pi, resolves its cli.js when a separate executable is absent, launches it with the first-party extension and invokes its model loop. No external autonomous host is required for this local CLI entry point.
- Why this is / is not agent-owned: The installed code packages an operating actor with a concrete action/result loop. An independently connected MCP host contributes no ownership to this claim.
- Evidence: [package.json](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/package.json), [local-agent-pi.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-pi.ts), [local-agent-pi-rpc.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-pi-rpc.ts), [local-agent-pi-sandbox.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-pi-sandbox.ts), [local-agent-manager.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-manager.ts), [package-install-smoke.test.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/test/package-install-smoke.test.ts).
- Basis: structural
- Confidence: high
- Caveats: This judgment is specific to the dependency-bundled path. Adapters to separately installed CLIs and the bare MCP host mode do not independently establish the same S1 boundary.

## S2 — Coordination

- State: C
- Function: Attenuate interference between simultaneous writers performing autonomous subtasks in a common project.
- Disturbance / variety regulated: Distinct writers can target overlapping paths and overwrite each other when they act on one checkout.
- Decisive decision or feedback right: Select separate execution placement for competing writers and choose how to reconcile their returned candidate changes.
- Decision owner: Local project operator or an explicitly composed coordinating caller decides isolation and integration. The first-party worktree path executes it.
- Supporting / enforcement mechanisms: Git worktree/branch creation, source revision, per-worker scope, durable branch identity and review/diff support.
- Closure path: Workers write isolated states. The wait/result includes checkout and branch; the caller inspects and incorporates selected changes before operating on the shared target again.
- Boundary reachability: The normal worker path provides worktree mode, per-call workspace binding and returned branch metadata. The supplied Skill specifies when parallel writers use it and how results return.
- Why this is / is not agent-owned: The first-party path is specifically aimed at concurrent writer interference; composing an autonomous coordinator and integration choice remains necessary.
- Distinct S1 units: Independently running Pi-backed worker turns on related implementation subtasks.
- Inter-S1 disturbance: Concurrent writers operating in one checkout can overwrite changes from another writer.
- Attenuating coordination relation: The distributed worker placement option puts each writer on its own branch and checkout based on one project revision.
- Feedback into subsequent S1 behaviour: Returned branch and path identify the candidate to review and merge. Further work can be based on the reconciled workspace.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The supplied path contains interfering writes and carries the distinct candidate states into the follow-on coordination decision, beyond delegating or waiting for tasks.
- Evidence: [SKILL.md](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/skills/subagents/SKILL.md), [local-agent-worktree.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-worktree.ts), [local-agent-manager.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-manager.ts), [workflow-workspaces.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/workflow-workspaces.ts).
- Basis: structural
- Confidence: medium
- Caveats: Isolation protects parallel working state but does not automatically reconcile Git changes or assign semantic priority.

## S3 — Inside-and-now control

- State: P
- Function: Regulate the current committed group of worker calls in an enabled DevSpace workflow run.
- Disturbance / variety regulated: A workflow with multiple running or queued calls may need interruption, cancellation or explicit recovery after a failed or obsolete commitment.
- Decisive decision or feedback right: Inspect the whole owned workflow and decide whether to cancel its active commitments, wait or explicitly resume from durable state.
- Decision owner: Authorized local workspace operator or commissioning owner in the direct CLI mode.
- Supporting / enforcement mechanisms: Workflow snapshot and calls/events, explicit cancellation intent, stop propagation, child-turn ownership checks, retained history and replay rules.
- Closure path: Cancellation closes admission and settles owned child calls; explicit resume creates a new run term based on recorded results under reuse rules.
- Boundary reachability: The opt-in workflow CLI and manager directly expose owned-run reads and cancellation/resume paths. Human command entry is supported without composing a new controller.
- Why this is / is not agent-owned: The operator makes the supervisory decision after inspecting the whole run. Deterministic cancellation and replay rules execute it.
- Whole-system current view: Snapshot plus calls and events cover the group of queued/running/settled worker calls owned by the assessed workflow.
- Current-control decision scope: Cancel the whole current workflow and settle subordinate turns, or explicitly resume from the captured prior work.
- Evidence: [workflow-manager.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/workflow-manager.ts), [workflow-cli.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/workflow-cli.ts), [workflow-store.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/workflow-store.ts), [README.md](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/README.md).
- Basis: structural
- Confidence: medium
- Caveats: This P is scoped to an active managed workflow group. It does not assign whole-system current control to an ordinary tool host or imply that every workspace is one governed workflow.

## S3* — Complementary audit

- State: C
- Function: Provide a reconstructable independent source review of a managed workspace result.
- Disturbance / variety regulated: A producer can report a change as complete while the candidate diff or source behavior contradicts that account.
- Decisive decision or feedback right: Assess source and changed lines independently, return evidence-based findings and let the commissioning owner use them to resolve acceptance or repair.
- Decision owner: Scoped read-only reviewer actor composed from the shipped profile and a separate worker; the commissioning caller selects the audit target and owns corrective action.
- Supporting / enforcement mechanisms: Read-only provider mode and separate session, packaged targeted reviewer profile, source/diff checkpoints, persisted findings and wait result.
- Closure path: Caller supplies actual target/baseline, obtains findings that cite directly read source instead of relying on the worker's summary, and can return a specific corrective instruction or hold integration.
- Boundary reachability: Published npm files include the targeted read-only reviewer example and installed subagent Skill; the packaged Pi driver can run the separately provisioned reviewer scope. The caller still composes the claim and return decision.
- Why this is / is not agent-owned: The supplied targeted profile and independent inspection channel support construction. Standard execution does not automatically install a binding audit step for every writer.
- Claim being audited: A managed writer says its candidate changes satisfy the commissioned requirements.
- Ordinary reporting path: Producer turn/result and implementation summary are the ordinary reporting path.
- Complementary access path: Separate read-only worker can inspect actual source or diff. Review checkpoints provide evidence independent of the report.
- Independence boundary: A new worker sees its own bounded brief with source access, rather than inheriting the producer's conversation. Independent outcome adjudication must be arranged by the caller.
- Who acts on findings: The caller checks findings, conditions acceptance, or sends a bounded repair/follow-up.
- Evidence: [pi-reviewer.md](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/examples/agents/pi-reviewer.md), [SKILL.md](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/skills/subagents/SKILL.md), [review-checkpoints.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/review-checkpoints.ts), [local-agent-pi.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-pi.ts), [package.json](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/package.json).
- Basis: structural
- Confidence: medium
- Caveats: The profile is an explicit packaged construction example, not evidence that an audit automatically runs or that an arbitrary subagent is an auditor.

## S4 — Outside-and-then intelligence

- State: —
- Function: Check for prospective selection and installation of a new operational capability from sensed changes.
- Disturbance / variety regulated: Future tasks, providers and codebases may demand different workers or methods.
- Decisive decision or feedback right: Use evidence about future conditions to choose and adopt a capability change into later operation.
- Decision owner: No first-party adaptation controller established. Local users or external callers author profiles and scripts.
- Supporting / enforcement mechanisms: Profile files, provider inventory, stored results, workflow replay and launch flags.
- Closure path: Roles and scripts configured by the caller affect execution. Retained run outputs support resumption, without a shipped outside-and-then adoption loop.
- Why this is / is not agent-owned: The inspected paths recover or reconfigure a given workflow; they do not generate and settle prospective capability changes from observed evidence.
- Evidence: [README.md](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/README.md), [local-agent-profiles.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-profiles.ts), [workflow-manager.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/workflow-manager.ts), [local-agent-availability.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-availability.ts).
- Basis: structural
- Confidence: medium
- Caveats: User-authored scripts may perform further analysis, which is outside this package-owned boundary.

### Absence scope

- Surfaces inspected: Profiles and provider queries, managed scripts, event storage, output reuse and replay.
- Plausible first-party paths checked: Future experiments, autonomous revision of worker definitions and durable updates to how future work is delivered.
- Why no material first-party path remains: Runtime checks availability and replays authored work. No first-party prospective sensing/choice/adoption path controls subsequent capability in the reviewed distribution.

## S5 — Policy and identity

- State: —
- Function: Check for a governance path that decides the local cell’s ultimate work identity or standing mandate.
- Disturbance / variety regulated: External caller requests or changes of provider can vary day-to-day work under owner-set workspace constraints.
- Decisive decision or feedback right: Legitimately choose or change the work cell’s ultimate purpose and return that policy into the actors’ behavior.
- Decision owner: No first-party constitutive mandate chooser or explicit in-boundary ultimate-policy loop was evidenced.
- Supporting / enforcement mechanisms: Allowed roots, local runtime/profiles config, connector authorization and per-turn permission selection.
- Closure path: Configuration persists paths and scope. It does not provide a supported decision loop for governing changes of ultimate purpose across the work cell.
- Why this is / is not agent-owned: Auth and write-mode gates enforce chosen access; the operator- or caller-authored task remains ordinary assignment.
- Evidence: [README.md](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/README.md), [config-schema.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/config-schema.ts), [SKILL.md](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/skills/subagents/SKILL.md), [local-agent-profiles.ts](https://github.com/Waishnav/devspace/blob/559781284677e5b128aa44a2c95f8bdb0c72b7c0/src/local-agent-profiles.ts).
- Basis: structural
- Confidence: medium
- Caveats: Workspace security authority and repo maintainers’ release policy are distinct from the operating cell’s ultimate-policy function.

### Absence scope

- Surfaces inspected: Local config, workspace ownership and authentication, profiles, workflow source and execution controls.
- Plausible first-party paths checked: Durable identity or policy review, authority to choose governing purpose, and binding return to subsequent operation.
- Why no material first-party path remains: Reviewed paths select permitted resources and define tasks/profiles. They provide no specific first-party ultimate-policy adjudication/return arrangement.

## Distributed OSS parent arrangement

The user owning the local workspace is the parent for the supported current-control path. Repository maintainers and third-party providers do not hold that runtime right.

## Self-hosted and non-human modes

The package supports the local bundled Pi fallback, separate system/external provider paths and optional authored workflow composition. The restricted tool extension is credited only where the adapter installs it; the capability claims do not imply full-access mode has the same policy.

## Recursion

The managed workflow group and its coding workers use local project-scoped coordination. External MCP callers may control a larger system, which is outside this assessment.

## Variety and escalation

Different task and tool outcomes are handled inside the operating Pi loop. Local workspaces and workflow scope bound external callers, and the owner can inspect and intervene on currently owned turns.

## Evidence gaps

Pinned source review only. No live provider, authorization test, deployment or independent audit was executed. The package’s fallback and supplied extension establish source-level operational reachability; external-driver paths and model access remain deployment-dependent.
