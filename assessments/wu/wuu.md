---
harness_id: wuu
project_name: Wuu
repository: https://github.com/blueberrycongee/wuu
review_ref: 5ef7adcb8a967346ec98d2da693b92d8a4200fc9
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: P
---

# Wuu

## Review boundary

- System in focus: Wuu's packaged Coding runtime, workspace controls, and supported bundled extensions.
- Purpose and identity: Run and oversee tool-using model agents in developers' workspaces and maintain the installed extensions that shape future work.
- Relevant environment: Local projects, Git checkouts, user, selected model providers and optionally external execution engines.
- Standard-distribution boundary: Desktop installed core and Go CLI-native model loop, with bundled optional Subagent, Memory, Dream and built-in skill authoring modes.
- Credited operating / distribution surfaces: Go model/tool runtime, workspace checkout and session router, Subagent lifecycle services, Dream and Memory, skill discovery, and owner-bound plugin trust management.
- Adjacent first-party surfaces excluded from ownership: External agent engines' internal implementation, legacy mobile paths, hosted deployment governance, contributor workflows and benchmark harnesses.
- First-party operating / deployment modes considered: Native model-backed Coding sessions, workspace worktree delegation, optional Dream + Memory, operator-directed skill authoring and extension control.
- Recursion level: One deployed Wuu Coding workspace and its managed conversation family. Installation-level trust acts as the parent authority boundary shared by its workspaces.
- Reviewed revision: `5ef7adcb8a967346ec98d2da693b92d8a4200fc9`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The desktop/CLI frontend uses a Go agent engine that streams LLM choices and executes tools with persistent session state. A workspace dispatches child sessions through a bundled plugin and can allocate separate Git worktrees. Bundled model workflows can inspect raw memory sources and update projected workspace knowledge. The owner manages future tools/skills and source-based plugin trust through the same supported distribution. [`README.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/README.md), [`internal/agent/loop.go`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/agent/loop.go#L78-L137), [`docs/en/customize/plugin-system.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/docs/en/customize/plugin-system.md), [`docs/en/desktop/subagents.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/docs/en/desktop/subagents.md), [`docs/en/customize/dream.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/docs/en/customize/dream.md), [`docs/en/customize/plugins.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/docs/en/customize/plugins.md).

## Operational model

Coding conversations make tool-backed project changes. Delegated child sessions have their own context, model requests, and scoped work. The root model can select worktree isolation and intervene on child commitments. A separate optional Dream model checks durable claims used by later workspace sessions. The owner settles what operating procedures and plugin sources the deployment may adopt.

## S1 — Operations

- State: A
- Function: Perform tool-backed work in the local project and return its artifact or answer.
- Disturbance / variety regulated: Changing user intent, tool findings, code and execution errors across model turns.
- Decisive decision or feedback right: Choose and revise task-local actions, tool arguments, and the terminal response.
- Decision owner: The model in the first-party Wuu agent loop.
- Supporting / enforcement mechanisms: Provider adapters, `RunToolLoop`, tool dispatcher, execution context, saved history, and desktop/CLI controls.
- Closure path: The engine executes returned tool calls, records results and feeds them into further model steps; a response without a tool call completes the loop.
- Why this is / is not agent-owned: Removing the model leaves runtime dispatch and permissions but no responsive tool selection.
- Evidence: [`internal/agent/loop.go`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/agent/loop.go#L78-L137), [`internal/agent/loop.go`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/agent/loop.go#L1249-L1325), [`docs/en/automation/exec.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/docs/en/automation/exec.md), [`README.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/README.md)
- Basis: explicit
- Confidence: High
- Caveats: Native execution is credited. The assessment does not need to attribute third-party engines' own model decisions to Wuu.
- Boundary reachability: The installed core and native CLI execute the package's model/tool loop when a supported provider is configured.

## S2 — Coordination

- State: A
- Function: Prevent parallel writing child agents from colliding in a shared workspace.
- Disturbance / variety regulated: Several separately acting workers can overwrite the same working files when default shared mode is used for parallel edits.
- Decisive decision or feedback right: Choose separate write scopes and ask the host for dedicated worktrees for conflicting child work.
- Decision owner: The initiating model using the bundled Subagent plugin.
- Supporting / enforcement mechanisms: `spawn_agent` isolation choice, binding of child session to a worktree, and returned child status/result.
- Closure path: A child runs with its assigned checkout and returns its result or completion to the initiating model. Each isolated child's edits occur in a separate checkout, enabling scoped parallel work and later selection for integration.
- Why this is / is not agent-owned: The model selects the conflict response on dispatch. The plugin and Git enforce the chosen separation.
- Evidence: [`docs/en/desktop/subagents.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/docs/en/desktop/subagents.md), [`internal/plugin/bundled/subagent/runtime.mjs`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/plugin/bundled/subagent/runtime.mjs#L876-L891), [`internal/plugin/bundled/subagent/runtime.mjs`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/plugin/bundled/subagent/runtime.mjs#L967-L1005), [`docs/en/reference/agent-command-system.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/docs/en/reference/agent-command-system.md#L72-L83)
- Basis: structural
- Confidence: High
- Caveats: The claim applies when the optional bundled Subagent mode is enabled and the caller uses a supported local Git workspace. Applying or merging worker patches remains a separate choice.
- Boundary reachability: `spawn_agent` exposes `isolation: worktree` directly to the root model in the optional bundled Subagent mode.
- Distinct S1 units: Separate model-backed working sessions undertaking assigned local implementation tasks within the same workspace effort.
- Inter-S1 disturbance: Parallel edits in the shared workspace can touch the same files, causing contradictory writes or integration confusion.
- Attenuating coordination relation: The parent can choose separate file ownership and opt into an actual Git checkout per parallel child.
- Feedback into subsequent S1 behaviour: After the model's selection children execute against the resulting isolated worktrees and report their own changes to the parent.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The worktree choice directly changes which writable checkout competing agents can affect, constraining the shared resource conflict identified in the source guide.

## S3 — Inside-and-now control

- State: A
- Function: Regulate current commitments across a root conversation's children while work is active.
- Disturbance / variety regulated: Children may overlap, return a blocker or result that invalidates remaining delegated work, or continue after a parent priority changes.
- Decisive decision or feedback right: Choose whether to keep, redirect or cancel a particular ongoing child commitment from the root.
- Decision owner: The root model in the managed conversation family.
- Supporting / enforcement mechanisms: Bound task identities, host session control and inspection, progress/terminal delivery and retained receipts.
- Closure path: A root tool sends a follow-up to the existing child or requests cancel on that owned child turn. The host applies the resulting lifecycle change and returns its status. Terminal feedback reaches the root, where it can change remaining work.
- Why this is / is not agent-owned: The root can exercise named live commitments after dispatch. The runtime enforces its chosen follow-up or termination.
- Evidence: [`docs/en/desktop/subagents.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/docs/en/desktop/subagents.md), [`internal/plugin/bundled/subagent/runtime.mjs`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/plugin/bundled/subagent/runtime.mjs#L895-L913), [`internal/plugin/bundled/subagent/runtime.mjs`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/plugin/bundled/subagent/runtime.mjs#L1066-L1114), [`internal/plugin/bundled/subagent/runtime.mjs`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/plugin/bundled/subagent/runtime.mjs#L1129-L1172)
- Basis: structural
- Confidence: Medium
- Caveats: This is the root's own worker portfolio. Human steering normally enters the root conversation and does not establish a separate whole-family parent execution surface in this assessment.
- Boundary reachability: When Subagent is enabled, the root holds first-party follow-up and cancel tools for its created children and receives their completion events.
- Whole-system current view: At the declared conversation-family recursion, the root receives admission receipts and result/failure feedback for the children it owns. Host state and client status cover the family; the model view is mediated by its task history and delivered events.
- Current-control decision scope: Change an already accepted child commitment by directing its existing session to do different work, stopping it or switching the root's remaining task portfolio in response to returned results.

## S3* — Complementary audit

- State: A
- Function: Challenge material durability claims in workspace memory against original evidence.
- Disturbance / variety regulated: Wrong or outdated memory entries can be recalled by future agents as established facts.
- Decisive decision or feedback right: Judge which existing claims to verify, keep, correct or remove after direct evidence access.
- Decision owner: The separately invoked Dream model in optional Coding Dream plus Memory mode.
- Supporting / enforcement mechanisms: Workspace memory snapshot, original histories, repository read tools, private background session, interval/candidate selection and durable memory write tools.
- Closure path: Dream compares original transcript evidence and current repository state with the stored claim, changes or removes unsupported entries, and leaves the revised memory projection for later ordinary sessions.
- Why this is / is not agent-owned: The Dream model owns evidence judgment and corrective selection. Timer and memory writes carry out the model's choices.
- Evidence: [`docs/en/customize/dream.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/docs/en/customize/dream.md), [`internal/plugin/bundled/dream/runtime.mjs`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/plugin/bundled/dream/runtime.mjs#L870-L876), [`internal/plugin/bundled/dream/runtime.mjs`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/plugin/bundled/dream/runtime.mjs#L919-L982), [`docs/en/customize/memory.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/docs/en/customize/memory.md#L15-L25)
- Basis: structural
- Confidence: High
- Caveats: The audited claims are durable workspace memories. This does not establish that Wuu dispatches an independent code-review gate in every coding run.
- Boundary reachability: The bundled Dream plugin creates a private model session with the normal Coding tools when enabled with the Memory service and fed eligible completed sessions.
- Claim being audited: A durable workspace or notebook entry accurately reflects earlier decisions or current repository facts.
- Ordinary reporting path: Ordinary agents write memory entries and later agents receive the stored index and details.
- Complementary access path: Dream can inspect multiple original conversation histories and the current repository, rather than relying on the existing memory entry.
- Independence boundary: The verifier runs in a separately scheduled private session. It can inherit one candidate's context, so its independence is grounded in separate judgment plus access to independent primary artifacts and multiple histories, rather than a blind model identity.
- Who acts on findings: The Dream agent corrects or removes the verified record through memory tools; subsequent workspace sessions read the changed state.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adopt future operating procedures in response to newly understood or repeated workflow needs.
- Disturbance / variety regulated: External tools, project-specific workflow requirements and constraints vary beyond a current task run.
- Decisive decision or feedback right: Accept a reusable future procedure grounded in concrete task examples and choose its deployment scope.
- Decision owner: The workspace user initiates and directs skill adoption. The native agent drafts, checks and refines the prospective option.
- Supporting / enforcement mechanisms: Bundled skill-creator instructions, lint, optional separate-context forward-test, repo/user skill files and live discovery.
- Closure path: An agreed skill is written to an admitted source, linted against discovery rules, appears in the runtime catalog, then loads in later eligible tasks. Real uses can return revisions to the same skill.
- Why this is / is not agent-owned: The Wuu model does the authoring and test work under a user-selected requirement and destination, with subsequent invocation governed by the approved catalog.
- Evidence: [`internal/skills/bundled/skill-creator/SKILL.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/skills/bundled/skill-creator/SKILL.md#L125-L194), [`internal/skills/materialize_test.go`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/skills/materialize_test.go#L85-L108), [`docs/en/customize/skills.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/docs/en/customize/skills.md#L1-L44)
- Basis: structural
- Confidence: Medium
- Caveats: Credited only for the user-directed capability-adaptation workflow. Dream memory consolidation alone and scheduled work do not supply this S4 claim.
- Boundary reachability: Skill Creator is packaged and the documented workspace/user skill directories are discovered by the installed agent loop.
- External distinction: The creator works from target project workflows and external tooling requirements or recurring outside inputs supplied by the user and checked on sample inputs.
- Future / prospective distinction: The purpose is to make future task executions reliable through a reusable capability rather than finish a single example.
- Adaptation option generated: The agent proposes instructions or scripts, references and assets derived from examples, then tests how a fresh session would use them.
- Path back into current capability / S3: The owner-selected scope receives the skill file, which is admitted by runtime discovery and becomes selectable or model-loadable for future work.

## S5 — Policy and identity

- State: P
- Function: Set which external executable sources may participate in the deployed agent runtime on an ongoing basis.
- Disturbance / variety regulated: A replacement extension from a different source would change the source of code and authority entering future runtime generations.
- Decisive decision or feedback right: Approve or reject an enduring change in the accepted executable plugin source for the deployment.
- Decision owner: The local deployment owner operating the supported plugin management surface.
- Supporting / enforcement mechanisms: Source-bound trust records, staged update and fingerprint checks, activation generation and durable configuration.
- Closure path: A source change is staged while the old trusted generation remains active. An explicit owner decision applies the pending package and trusted source, or rejects it. Subsequent plugin activation and tool exposure honor that policy.
- Why this is / is not agent-owned: The runtime cannot auto-approve a changed authority origin; it applies the owner's accepted source policy across later invocations.
- Evidence: [`docs/en/customize/plugins.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/docs/en/customize/plugins.md#L5-L36), [`internal/appserver/plugin_package_handlers.go`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/appserver/plugin_package_handlers.go#L520-L612), [`internal/plugin/update_test.go`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/internal/plugin/update_test.go), [`docs/en/customize/plugin-system.md`](https://github.com/blueberrycongee/wuu/blob/5ef7adcb8a967346ec98d2da693b92d8a4200fc9/docs/en/customize/plugin-system.md)
- Basis: structural
- Confidence: High
- Caveats: Credited for durable source authority across runtime generations. Individual shell, tool, or action approvals are outside this policy claim.
- Boundary reachability: The first-party desktop plugin detail page and CLI support source-changing update approval in deployed Wuu.
- Identity / ultimate-policy issue: Whether code from a previously untrusted origin may become an ongoing, user-authority-bearing constituent of the Wuu installation.
- Ultimate authority in each claimed mode: The owner decides whether the new source becomes trusted. Settings and runtime lifecycle apply the choice.
- Return-to-operation path: Approval promotes the pending source into the trusted active generation; rejection preserves the prior source boundary. Later execution can only use the resulting activation policy.

## Recursion

A root coding conversation and its separately model-driven workers form a bounded workspace operating family. The plugin source authority belongs to the surrounding deployment owner. No viability grade is assigned solely because a child session is created.

## Variety and escalation

Worktree choice separates conflicting edits. Tool results and terminal receipts return to model supervision. Optional independent memory checks modify future operational recall. The reviewed release instructions distinguish ordinary current steering from deployment-wide trust decisions.

## Evidence gaps

This is a pinned source and test-code review. No live macOS or external provider run was performed. Personal, mobile and external engine internals were not used to supply positive states. Control and audit claims are scoped to the explicit modes and claims above.

