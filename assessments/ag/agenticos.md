---
harness_id: agenticos
project_name: AgenticOS
repository: https://github.com/patil-shubham-dev/AgenticOS
review_ref: d9c91c66cc3d32f78074ffc96cfd365f6368a80b
reviewed_at: 2026-11-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: ?
---

# AgenticOS

## Review boundary

- System in focus: The source-distributed AgenticOS DeepSeek application core and a configured project workflow running through its maintained app-server protocol.
- Purpose and identity: Run a provider-backed workspace coding loop with operator control of multi-agent workflows and code review.
- Relevant environment: A project working directory, core profile, configured model and operator acting through the core's client protocol.
- Standard-distribution boundary: The committed core launcher, profile and bridge source plus pinned dependency packages used at runtime. The engine can be entered through its stdio app-server without the desktop interface.
- Credited operating / distribution surfaces: DeepSeek core bundle, bridge-owned thread lifecycle, workflow engine binding, named worktree isolation option, workflow observability and control, and the dedicated review turn.
- Adjacent first-party surfaces excluded from ownership: Desktop renderer and its extracted reference assets, parity fixtures, historical audit reports, alternate vendor core internals and release packaging. Their behavior supplies no required ownership witness.
- First-party operating / deployment modes considered: Headless core coding, model- and caller-initiated workflows through the core, and a caller-invoked review turn.
- Recursion level: One project coding operation and its active workflow campaign. Separate child sessions are operational units in the configured workflow.
- Reviewed revision: d9c91c66cc3d32f78074ffc96cfd365f6368a80b
- Observation date: 2026-11-15
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The core starts a DeepSeek Harness profile and exposes a stdio JSON-RPC application server. The committed bridge creates and resumes model-backed sessions, binds workspace tools, and projects parent and child turn events. The workflow entrypoints wrap the same pinned engine for a model-authored script or a caller-started workflow. AgenticOS traces its source lineage to OpenClaude Desktop. Its root license and notice distinguish that lineage from separately licensed dependencies and assets. The assessed core has its own launcher and package manifest. The documented desktop build has additional reference assets outside the checkout. [Core launcher][launch] · [Dependencies][package] · [Lineage and third-party notice][notice] · [Desktop build inputs][audit]

## Operational model

The connected model chooses successive workspace tool actions and reviews their returned results. Workflow scripts can create separate children, collect their work and apply a worktree boundary to concurrent writers. The supervising caller can vary a live campaign using per-member controls. A separate review session can inspect a selected change through the purpose-built review entrypoint.

## S1 — Operations

- State: A
- Function: Perform a coding or investigation assignment in the configured workspace.
- Disturbance / variety regulated: Changing source and tool results during a task, and differences in the model route.
- Decisive decision or feedback right: Choose workspace actions and react to outcome evidence until returning the task result.
- Decision owner: The model-backed agent in the installed DeepSeek core.
- Supporting / enforcement mechanisms: Application-server thread creation, model routing, profile and tool binding, persistent session and event projection.
- Closure path: A caller starts a turn; the core presents the workspace task to the agent, records tool and model events and returns the result to the caller.
- Boundary reachability: The core's documented package entrypoint launches the installed profile. The owned bridge binds a working-directory-specific agent to its available tools with each supported new session.
- Why this is / is not agent-owned: The model chooses the next action from the current task and tool feedback. The bridge manages the surrounding lifecycle.
- Evidence: [Runtime launcher][launch] · [Model and workspace binding][thread] · [Core turn route][turn]
- Basis: Pinned source including the runtime package manifest.
- Confidence: High.
- Caveats: Operation requires installed dependencies and a configured model provider.

## S2 — Coordination

- State: C
- Function: Reduce cross-worker interference from parallel edits to the same checkout.
- Disturbance / variety regulated: Multiple independent workflow children can write overlapping files in the same project.
- Decisive decision or feedback right: Choose which concurrent assignments get isolated worktrees and reconcile their returned results.
- Decision owner: The workflow composer or an explicitly authored agent role. The default constructor provides the isolation and result path.
- Supporting / enforcement mechanisms: Pinned workflow engine, explicit worktree isolation in the local spawn provider, phase result handling and child lifecycle.
- Closure path: A composed workflow requests isolated children, receives their results after settlement and determines the next merge or corrective phase. Workspace separation prevents one child's edits from overwriting another's shared checkout.
- Boundary reachability: The core's workflow launcher uses the pinned local engine and publishes model-initiated and caller-initiated runs to the supported protocol.
- Distinct S1 units: Separate local workflow children with their own agent sessions.
- Inter-S1 disturbance: Concurrent writes and resulting overlap among child jobs.
- Attenuating coordination relation: Per-child Git worktree isolation carries disjoint writable views through the parallel work.
- Feedback into subsequent S1 behaviour: The composing workflow consumes returned child outcomes before assigning or integrating dependent work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The constructor expressly changes each writer's checkout to avoid cross-child mutation. Pure phase grouping would leave that worktree interference intact.
- Why this is / is not agent-owned: The installed mechanism gives an explicit collision-attenuation path. Choosing and reconciling overlap beyond it depends on a composed workflow.
- Evidence: [Pinned local workflow and spawn packages][package] · [Explicit isolation and result boundary in vendor patch](https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/new-2.42304.0/harness/patches/workflow-cli-merge.patch#L56640-L56667) · [Run and result binding][run]
- Basis: Bridge and local workflow package at the reviewed ref.
- Confidence: Medium.
- Caveats: Worktree setup applies only to an isolation-capable spawn provider and opts into it.

## S3 — Inside-and-now control

- State: P
- Function: Supervise and redirect current commitments across one active multi-agent workflow.
- Disturbance / variety regulated: Stalled or failed members, unwanted resource use and changing operator priorities during the run.
- Decisive decision or feedback right: Decide whether to stop the campaign or skip, retry or resume the affected work.
- Decision owner: The supervising caller operating the workflow through its client protocol.
- Supporting / enforcement mechanisms: Attempt-bound phase and member events, active-run membership checks, skip/retry and stop/resume routes.
- Closure path: The live phase, admission and termination views expose current work. An operator decision changes the run's active member or attempt state and that state is returned by the engine.
- Boundary reachability: Both progress and intervention paths are native stdio methods. The workflow execution binding relays the choice directly to the same engine that owns the run.
- Whole-system current view: Active phases, member admissions, progress and results across the assessed run.
- Current-control decision scope: Withdraw or retry a current activity, stop the overall run, or resume an interrupted campaign.
- Why this is / is not agent-owned: The caller selects the substantive intervention over the running campaign. The inspected agent-authored work selection operates through workflow scripts and their results.
- Evidence: [Run-wide progress and member control][run] · [Live stop, skip and retry routes][control] · [Attempt isolation test definition][run-test]
- Basis: First-party runtime and protocol source.
- Confidence: Medium.
- Caveats: Scope is one current workflow. The test definition covers runtime events and attempt identity.

## S3* — Complementary audit

- State: C
- Function: Inspect the actual work behind a code change and return independent findings when configured in a separate review session.
- Disturbance / variety regulated: The implementation conversation can overstate the completeness of its actual diff.
- Decisive decision or feedback right: Decide what the actual reviewed source and diff show and return concrete findings.
- Decision owner: The composed reviewer agent. The caller is responsible for making a fresh review thread and routing findings to the work owner.
- Supporting / enforcement mechanisms: Purpose-built commit, branch or worktree targets; read-only review turn; structured output and event projection.
- Closure path: A caller opens a fresh thread against the same checkout and requests a pinned-target review. The reviewer inspects the change directly. Findings return through the review event so the caller can initiate correction.
- Boundary reachability: A new core thread and review start are both supported protocol paths and can be composed without desktop reference assets.
- Claim being audited: Whether the identified implementation change meets its expected behavior without material errors.
- Ordinary reporting path: The implementing agent's completion message and history.
- Complementary access path: Review prompt reads the actual named commit or diff in the workspace.
- Independence boundary: A fresh thread can carry a separate actor and context. The standard inline review in the producing thread shares its history.
- Who acts on findings: The supervising caller or lead consuming the returned review result.
- Why this is / is not agent-owned: The evaluator chooses the findings. A caller must compose the distinct reviewer and correction handoff to establish independence.
- Evidence: [Review target and findings contract][review] · [Read-only inline entrypoint][review-start] · [Fresh thread construction][thread] · [Review result projection test][review-test]
- Basis: Pinned review path and caller-composed independence.
- Confidence: Medium.
- Caveats: Inline review by itself provides direct evidence access within the current session.

## S4 — Outside-and-then intelligence

- State: —
- Function: Turn future-relevant external change into a change in reusable workspace capability.
- Disturbance / variety regulated: New requirements, provider or tool changes and future operating constraints.
- Decisive decision or feedback right: Select a prospective adaptation grounded in the changing external environment and return it into future operating capability.
- Decision owner: No supplied adaptation owner in the assessed core.
- Supporting / enforcement mechanisms: Configured providers, profiles, workflow scripts, reusable plugin and routine hooks.
- Closure path: No material first-party external-sensing and capability-adoption loop is implemented within the assessed core modes.
- Why this is / is not agent-owned: A caller can author an adaptive workflow using the generic facilities.
- Evidence: [Core profile loading][launch] · [Workflow control and settings routes][control] · [Provider configuration and feature boundary][package]
- Basis: Bounded inspection of installed-profile, workflow and runtime settings paths.
- Confidence: Medium.
- Caveats: The scope excludes plans for other versions and externally implemented plugins.

### Absence scope

- Surfaces inspected: Model and plugin/profile settings, core workflow and scheduled behavior, available review and result channels.
- Plausible first-party paths checked: Provider switching, reusable jobs and skills, review findings, and profile updates.
- Why no material first-party path remains: Provider and profile changes follow configured inputs. Workflows execute supplied tasks. The inspected paths supply no standing external-and-prospective judgment linked to adaptation of the core or workspace's capabilities.

## S5 — Policy and identity

- State: ?
- Function: Set and return enduring policy for the project coding operation.
- Disturbance / variety regulated: Changes in delegated authority or the operating purpose of recurrent project work.
- Decisive decision or feedback right: Resolve an ultimate-policy choice and bind it to subsequent operation.
- Decision owner: Unresolved at the assessed core boundary.
- Supporting / enforcement mechanisms: Operator-specified profile overlays, persistent developer instructions, workflow gates and per-turn permission policy.
- Closure path: The core reapplies saved instructions on resume. Evidence for an identity-level issue reaching an authorized owner and returning as policy across the operation remains incomplete.
- Why this is / is not agent-owned: The core accepts the caller's operating configuration. Per-turn permissions and stored instructions evidence configured authority boundaries, with the identity-level decision path unresolved.
- Evidence: [Operator-supplied profile overlays][launch] · [Instruction storage on create][thread] · [Instruction rebinding on resume](https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/new-2.42304.0/harness/packages/codex-app-server/src/index.js#L1272-L1306)
- Basis: Pinned runtime and profile boundary.
- Confidence: Medium.
- Caveats: Desktop-wide instructions and the caller's governance process were outside the graded core boundary.

## Recursion

A project workflow contains separately acting child sessions. The core exposes group progress and member interventions to a supervising operator. The app-server boundary leaves the surrounding organization and alternate vendor runtimes outside the assessment.

## Variety and escalation

Admission and result events carry changing run state to the supervising caller. Its intervention changes the active campaign; explicit review paths give the caller task evidence independently of ordinary completion when composed in a fresh thread.

## Evidence gaps

The review establishes behavior from pinned core source, dependency records and test definitions. Desktop packaging requires external reference assets and was outside the credited boundary. No provider-backed execution or independent replay was used.

[launch]: https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/new-2.42304.0/harness/bin/codex-app-server.mjs
[package]: https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/new-2.42304.0/harness/package.json
[notice]: https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/NOTICE.md
[audit]: https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/AUDIT.md#L60-L73
[thread]: https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/new-2.42304.0/harness/packages/codex-app-server/src/index.js#L1212-L1258
[turn]: https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/new-2.42304.0/harness/packages/codex-app-server/src/index.js#L2143-L2212
[run]: https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/new-2.42304.0/harness/packages/codex-app-server/src/workflow-execution.js#L9-L58
[control]: https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/new-2.42304.0/harness/packages/codex-app-server/src/index.js#L2320-L2346
[run-test]: https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/new-2.42304.0/harness/tests/workflow-executions.test.mjs
[review]: https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/new-2.42304.0/harness/packages/codex-app-server/src/review.js#L36-L69
[review-start]: https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/new-2.42304.0/harness/packages/codex-app-server/src/index.js#L1368-L1407
[review-test]: https://github.com/patil-shubham-dev/AgenticOS/blob/d9c91c66cc3d32f78074ffc96cfd365f6368a80b/new-2.42304.0/harness/tests/review-rewind.test.mjs#L30-L84
