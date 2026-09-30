---
harness_id: archon
project_name: Archon
repository: https://github.com/coleam00/Archon
review_ref: e237584d9c332fc492125bf9e0cb4756895f4da2
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Archon

## Review boundary

- System in focus: the first-party `coleam00/Archon` workflow/runtime organization at frozen revision `e237584d9c332fc492125bf9e0cb4756895f4da2`, including the shipped DAG workflow executor, Archon-authored prompt/command contracts, provider-neutral AI-node interface and built-in provider adapters, run/session state, worktree isolation, project-scoped run-management surface, approval gates, and bundled review/fix workflows where they bear on organizational function.
- Purpose and identity: convert software-development intent into reproducible agentic workflow runs whose structure, isolation, state transitions, review gates and corrective stages are owned by Archon while model-backed actors perform context-sensitive coding/review decisions inside that structure.
- Relevant environment: target Git repositories and PRs, user development intent, current source/worktree state, model/provider responses, tests/builds, GitHub state, concurrent Archon workflow runs, run failures/pauses, and human decisions at explicit approval/control boundaries.
- Standard-distribution boundary: Archon's shipped CLI/server/runtime, default workflows and commands, workflow executor, provider contract/adapters, worktree/isolation providers, durable run state, orchestrator chat/run-management paths and default review block are inside. Claude Code, Codex, Pi, OpenCode/Copilot and their independent upstream reasoning/runtime implementations are external execution/model dependencies; their organizational functions are not inherited merely because Archon can invoke them.
- Credited operating / distribution surfaces: `README.md`; `packages/workflows/src/{executor,dag-executor}.ts`; `packages/providers/src/types.ts`; built-in provider adapters including `packages/providers/src/claude/provider.ts`; `packages/isolation/src/providers/worktree.ts`; `packages/core/src/orchestrator/{orchestrator-agent,prompt-builder,manage-run-tool}.ts`; bundled `.archon/workflows/defaults/legacy/archon-review-block.yaml`; bundled review/synthesis/fix command contracts under `.archon/commands/defaults/`.
- Adjacent first-party surfaces excluded from ownership: repository-development CI/tests/fixtures; maintainer/contributor governance; documentation-only architecture notes not wired into the frozen runtime; project self-dogfood artifacts; future/current-default-branch features absent at the frozen revision; and the organizational autonomy internal to external coding-agent providers.
- First-party operating / deployment modes considered: CLI/server workflow execution; bundled default workflows; AI/prompt/command DAG nodes; loop/gate/wait/fan-out and deterministic exec nodes; concurrent workflow runs with worktree isolation; project-scoped orchestrator chat with `manage_run` or equivalent CLI run management; human approval/rejection/respond gates; bundled multi-agent PR review followed by synthesis and corrective implementation.
- Recursion level: one Archon-managed project/workspace as the focal organization. A materially independent workflow run that transforms the target repository is an operational S1 unit at this recursion. AI node turns, tool calls and provider subagents are lower-level operations inside a run unless separately evidenced as viable same-recursion units. Parallel review actors belong to the complementary audit path over produced repository changes, not to S2 merely because they are numerous.
- Reviewed revision: `e237584d9c332fc492125bf9e0cb4756895f4da2`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Archon is not only a launcher around an external coding-agent CLI. The frozen distribution owns a workflow execution contract: DAG nodes are ordered topologically, independent nodes may run concurrently, loop/gate/wait/fan-out semantics are first-party, run state is durable, and AI nodes are dispatched through Archon's provider-neutral `IAgentProvider.sendQuery(prompt, cwd, session, options)` boundary. Node configuration carries Archon-declared tool restrictions, skills, inline agents, budgets, system prompts, MCP configuration, execution context and other controls.

The built-in Claude adapter demonstrates the boundary concretely. Archon translates its own node configuration into SDK options, narrows declared skills/tools, supplies hooks and native Archon tools, chooses system/model/budget/session settings, starts the query and normalizes tool/result/task events back into Archon state. Claude Code performs the model/tool reasoning internally, but the operational role, workflow prompt, declared capability envelope and feedback path are reachable through first-party Archon surfaces rather than borrowed wholesale from an unrelated external organization.

The standard runtime also creates independent git worktrees/branches for runs. This is an explicit isolation mechanism for the structural interference that would otherwise occur when multiple software-development runs modify the same checkout/branch concurrently. The mechanism is deterministic: it creates/adopts/verifies worktrees and branches; no autonomous S2 actor chooses the coordination policy.

Project-scoped chat exposes a current-run control surface. The orchestrator can list/get/start workflow runs and exposes resume/cancel/abandon/approve/reject/respond semantics through the native `manage_run` tool or equivalent first-party CLI instructions. The decisive destructive/current-control actions are deliberately parent-governed: they require human confirmation, and human-gate decisions are to preserve the user's own words rather than be invented by the model. This supplies a real whole-project current-control path but not an autonomous S3 owner.

The bundled review block provides a distinct audit organization over produced code. After scope/sync it launches five fresh-context specialized reviewers in parallel, each reads repository/PR evidence and writes its own finding artifact. A separate synthesis role aggregates, deduplicates and prioritizes those findings, and `archon-implement-review-fixes` reads the consolidated review, applies CRITICAL/HIGH fixes, adds/executes tests, commits and pushes the corrected PR branch. This closes a complementary challenge → corrective return loop rather than stopping at observability.

Primary evidence:

- [`README.md`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/README.md)
- [`packages/workflows/src/executor.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/workflows/src/executor.ts)
- [`packages/workflows/src/dag-executor.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/workflows/src/dag-executor.ts)
- [`packages/providers/src/types.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/providers/src/types.ts)
- [`packages/providers/src/claude/provider.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/providers/src/claude/provider.ts)
- [`packages/isolation/src/providers/worktree.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/isolation/src/providers/worktree.ts)
- [`packages/core/src/orchestrator/orchestrator-agent.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/core/src/orchestrator/orchestrator-agent.ts)
- [`packages/core/src/orchestrator/prompt-builder.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/core/src/orchestrator/prompt-builder.ts)
- [`packages/core/src/orchestrator/manage-run-tool.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/core/src/orchestrator/manage-run-tool.ts)
- [`.archon/workflows/defaults/legacy/archon-review-block.yaml`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/.archon/workflows/defaults/legacy/archon-review-block.yaml)
- [`.archon/commands/defaults/archon-code-review-agent.md`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/.archon/commands/defaults/archon-code-review-agent.md)
- [`.archon/commands/defaults/archon-synthesize-review.md`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/.archon/commands/defaults/archon-synthesize-review.md)
- [`.archon/commands/defaults/archon-implement-review-fixes.md`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/.archon/commands/defaults/archon-implement-review-fixes.md)

## Operational model

A standard Archon run combines deterministic workflow structure with model-backed local judgment. Workflow YAML/command prompts declare what a node is trying to accomplish and what capabilities/context it receives; the first-party executor invokes the selected provider and records/threads its result into subsequent DAG state. The external provider supplies inference and its own lower-level tool loop, but Archon owns the run-level operational contract, prompt role, workflow transitions, isolation and returned output usage.

Several runs can coexist for one project. Rather than sharing one mutable checkout, first-party isolation creates separate worktrees/branches and routes each run to its own working path. Project-scoped run management then exposes current run status and intervention controls to a legitimate parent user/operator. Separately, bundled review workflows can challenge produced changes through fresh-context reviewer invocations and route accepted findings into actual corrective code changes.

## S1 — Operations

- State: A
- Function: transform a software-development intent into repository/PR outcomes through first-party workflow roles that invoke model-backed judgment, act on the target codebase and feed results into subsequent workflow state.
- Disturbance / variety regulated: heterogeneous coding tasks, repository structure and constraints, changing source state, model/tool results, implementation choices, validation failures and review feedback that require contextual decisions rather than a fixed command sequence.
- Decisive decision or feedback right: within shipped AI/command nodes, interpret the Archon-authored role prompt against live repository evidence, choose code/review actions through the provider tool loop, and return a result that determines subsequent DAG/loop state and ultimately repository changes.
- Decision owner: the model-backed operational actor invoked through Archon's first-party AI-node/provider path. Archon owns the role/prompt/capability envelope and run closure; the configured Claude/Codex/Pi/etc. runtime supplies external inference/tool execution rather than being credited for unrelated higher-level organizational functions.
- Supporting / enforcement mechanisms: DAG executor; workflow schemas; prompt/command contracts; `IAgentProvider`; provider adapters; node tool/skill/MCP restrictions; sessions; durable run state; bash/test nodes; loops/gates; isolation; Git/GitHub operations.
- Closure path: user/application intent selects/starts a shipped workflow → Archon creates run/isolation state and dispatches an Archon-defined AI role through its provider contract → the model-backed actor reads/changes the repository or produces a finding/plan → Archon records the result and advances/replans/loops according to workflow semantics → later nodes consume that result and the run produces repository/PR outcomes.
- Boundary reachability: standard bundled workflows contain AI/command nodes whose prompts live in Archon's shipped distribution and are directly executed by the first-party DAG executor through built-in provider adapters. No downstream application author must create the operational agent loop or manually shuttle its result back into workflow state.
- Why this is / is not agent-owned: if the model-backed actor is removed while keeping the DAG scheduler, worktree state and deterministic nodes, Archon can still sequence commands but loses the contextual coding/review decisions that realize its primary software-development transformation. The organizational discretion at those operational nodes is therefore model-owned even though provider internals remain external dependencies.
- Evidence: [`README.md`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/README.md); [`packages/workflows/src/dag-executor.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/workflows/src/dag-executor.ts); [`packages/providers/src/types.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/providers/src/types.ts); [`packages/providers/src/claude/provider.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/providers/src/claude/provider.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Archon does not receive credit for autonomous functions internal to Claude Code/Codex/Pi merely because their SDKs may contain subagents/planners. S1 is credited only for the first-party Archon role → provider invocation → run-state/repository closure that is operationally present at the frozen revision.

## S2 — Coordination

- State: C
- Function: attenuate destructive filesystem/branch interference among concurrent Archon S1 workflow runs operating on the same project repository.
- Disturbance / variety regulated: concurrent implementation/review runs would otherwise modify one checkout/branch, overwrite or observe one another's in-progress files, and entangle run-specific commits/state.
- Decisive decision or feedback right: assign/adopt a run-specific git worktree and branch/working path before that run acts on repository state, preserving separation until its changes are deliberately integrated.
- Decision owner: first-party deterministic isolation policy in `WorktreeProvider`; no autonomous coordination actor chooses or revises the inter-run coordination response in the reviewed standard mode.
- Supporting / enforcement mechanisms: generated branch names and worktree paths; existing-worktree detection/adoption; `git worktree add/remove`; ownership verification; per-run working paths; cleanup/branch handling; run metadata tying execution to isolation.
- Closure path: a new/concurrent workflow run is admitted for a project → Archon's isolation layer resolves a distinct/adopted worktree/branch → the S1 run executes against that isolated working path instead of the shared checkout → its subsequent reads/writes/commits remain separated from other active runs until explicit integration/cleanup.
- Boundary reachability: worktree isolation is the shipped default `IIsolationProvider` path used by Archon workflow execution and is presented by the product as the mechanism enabling concurrent isolated runs; downstream developers do not have to invent the isolation protocol.
- Why this is / is not agent-owned: the S2 function is real and specific to cross-run interference, but its decisive response is encoded in deterministic worktree/branch policy. A first-party autonomous coordinator is not present, so the published state is constructor/control `C`, not `A`.
- Evidence: [`README.md`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/README.md); [`packages/isolation/src/providers/worktree.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/isolation/src/providers/worktree.ts); [`packages/workflows/src/executor.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/workflows/src/executor.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: generic DAG edges, sequencing, provider routing and parallel review roles are not counted as S2. The witness is specifically the concrete shared-repository collision mode and the shipped run-isolation response.
- Distinct S1 units: separate Archon workflow runs for the same project, each capable of independently producing repository/PR changes.
- Inter-S1 disturbance: without isolation, simultaneously active runs can read/write the same checkout/branch and destructively interfere through overlapping files, commits and transient worktree state.
- Attenuating coordination relation: Archon assigns/adopts distinct git worktrees and branches/working paths per run and enforces execution in those paths.
- Feedback into subsequent S1 behaviour: the isolation decision changes the cwd/branch against which each run subsequently reads, writes and commits, preventing the other active run's unintegrated state from becoming its live working state.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism exists to separate simultaneously active repository-transforming runs and directly attenuates a concrete cross-S1 state collision; it is not merely a workflow edge or task router.

## S3 — Inside-and-now control

- State: P
- Function: provide project-wide current visibility and intervention over active/recent workflow commitments so a legitimate parent operator can start, inspect, continue, cancel/abandon, or resolve gates on current work.
- Disturbance / variety regulated: multiple current workflow commitments can be running, paused, failed, blocked on human response, orphaned or no longer desired; the project needs a current view plus authority to change those commitments rather than treating each run as an isolated opaque process.
- Decisive decision or feedback right: decide whether current project work should be started, cancelled/abandoned, resumed/continued, approved/rejected/responded at a gate, or left untouched after inspecting current run state.
- Decision owner: the legitimate parent user/operator in the evidenced parent-governed mode. The orchestrator model can expose state, preview actions and translate unambiguous user language into the run-management verb, but destructive actions and human-gate decisions require explicit human confirmation/decision; deterministic workflow operations enforce the returned choice.
- Supporting / enforcement mechanisms: `manage_run` list/get/start/resume/cancel/abandon/approve/reject/respond interface; project-scoped run queries; run status/attention state; orchestrator system prompt; confirmation gate for destructive actions; core workflow-operation functions; live-owner/continuation plumbing.
- Closure path: current project runs/statuses become visible through `manage_run`/CLI → parent user/operator reviews the relevant commitment or gate and makes the current-control decision → Archon's first-party operation validates/persists/enforces it → the affected workflow is started, continued, cancelled/abandoned, reworked or kept paused, changing subsequent current operation.
- Boundary reachability: project-scoped Archon chat directly exposes the native `manage_run` tool on capable providers and ships equivalent CLI run-management instructions on other supported providers; the parent does not need to write a custom supervisor around the runtime.
- Why this is / is not agent-owned: the autonomous chat/orchestrator can route work and operate the tool surface, but the decisive destructive/current-control authority is intentionally retained by the human parent. Removing the model still leaves the same parent decisions reachable through the first-party CLI/control operations; removing the parent confirmation removes the decisive authority for those governed interventions. No separate autonomous S3 mode with equivalent whole-project authority was established.
- Evidence: [`packages/core/src/orchestrator/manage-run-tool.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/core/src/orchestrator/manage-run-tool.ts); [`packages/core/src/orchestrator/prompt-builder.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/core/src/orchestrator/prompt-builder.ts); [`packages/core/src/orchestrator/orchestrator-agent.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/core/src/orchestrator/orchestrator-agent.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: individual approval gates alone would not establish S3. The mapping depends on the broader project-scoped current-run surface (`list/get/status/start/resume/cancel/abandon` plus gate intervention) and its return into run lifecycle. `P` describes that supported parent-governed current-control mode, not every Archon interaction.
- Whole-system current view: `manage_run list`/project-scoped workflow status exposes recent/current runs for the project with workflow, status, authored outcome and active nodes; per-run `get` supplies current detail and gate state.
- Current-control decision scope: project workflow commitments and interventions — launching new work, stopping/abandoning current work, continuing eligible work, and resolving current human-gated commitments so the workflow either proceeds/reworks or terminates.

## S3* — Complementary audit

- State: A
- Function: independently challenge produced PR/code changes through fresh-context specialized reviewers, reconcile their findings, and return high-severity audit results into corrective implementation.
- Disturbance / variety regulated: implementation bugs, error-handling gaps, missing test coverage, misleading comments, documentation impact and violations of repository-specific coding rules that the ordinary implementation path may miss or misreport.
- Decisive decision or feedback right: each reviewer independently judges its assigned quality/risk dimension from the PR diff and repository evidence; the synthesis actor resolves overlap/conflicting recommendations and prioritizes findings; the corrective actor decides/applies fixes for the consolidated CRITICAL/HIGH set within the shipped review contract.
- Decision owner: model-backed fresh-context review/synthesis/fix actors invoked as distinct first-party Archon workflow roles.
- Supporting / enforcement mechanisms: review-scope artifact; five parallel fresh-context reviewer nodes; separate finding artifacts; synthesis prompt; severity/deduplication rules; `implement-fixes`; type-check/lint/test/build validation; commit/push and PR-comment paths.
- Closure path: ordinary implementation produces/synchronizes a PR → five fresh-context reviewers separately inspect PR/repository evidence and produce findings → synthesis aggregates/deduplicates/prioritizes the independent artifacts → fix role reads the consolidated audit and edits/tests/commits/pushes required CRITICAL/HIGH corrections → subsequent PR state reflects the audit result.
- Boundary reachability: `archon-review-block` is shipped in the default distribution and included by standard end-to-end workflows; all reviewer, synthesis and fix role contracts are first-party command artifacts executed by the ordinary workflow engine. No application-authored evaluator wiring is required.
- Why this is / is not agent-owned: the substantive finding/verdict/reconciliation/fix judgments are made by distinct model-backed roles; deterministic DAG edges merely ensure that separate evidence artifacts are gathered before synthesis and that correction follows it. Removing those model-backed audit actors leaves orchestration but not materially the same complementary judgment.
- Evidence: [`.archon/workflows/defaults/legacy/archon-review-block.yaml`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/.archon/workflows/defaults/legacy/archon-review-block.yaml); [`.archon/commands/defaults/archon-code-review-agent.md`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/.archon/commands/defaults/archon-code-review-agent.md); [`.archon/commands/defaults/archon-synthesize-review.md`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/.archon/commands/defaults/archon-synthesize-review.md); [`.archon/commands/defaults/archon-implement-review-fixes.md`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/.archon/commands/defaults/archon-implement-review-fixes.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: reviewers may use the same configured provider/model family as implementation, so independence is not provider/institutional independence. It is operational/contextual independence: distinct fresh-context invocations with specialized challenge roles, direct access to PR diff/codebase evidence, separate artifacts, and a returned corrective path.
- Claim being audited: that the implementation/PR produced by the ordinary development workflow is sufficiently correct, robust, tested, understandable and documented for its intended scope.
- Ordinary reporting path: implementation/validation nodes produce repository changes, test/build outcomes and PR state in the normal production workflow.
- Complementary access path: after sync, five dedicated reviewers start with `context: fresh` and independently inspect the actual PR diff plus repository rules/code patterns from specialized perspectives, writing separate artifacts rather than relying on the implementation actor's narrative.
- Independence boundary: the audit roles are separate workflow invocations with fresh contexts and direct repository/PR evidence; they neither inherit the implementation conversation nor depend solely on its self-report. Their outputs remain separate until the later synthesis node.
- Who acts on findings: the first-party synthesis role consolidates/prioritizes findings and the subsequent `archon-implement-review-fixes` role applies/tests/commits/pushes CRITICAL/HIGH corrections; remaining findings are surfaced for parent/user decision.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material first-party external-and-prospective intelligence/adaptation loop was established at the assessed project-runtime boundary.
- Disturbance / variety regulated: Archon senses current user intent, current repository/PR state, provider/tool results and current run failures, but no shipped path was found that models future/external developments and develops adaptation options for the Archon organization on that basis.
- Decisive decision or feedback right: not established at S4. Workflow selection, implementation planning, retries, repository review and current provider/model selection respond to present task/runtime conditions.
- Decision owner: not established at S4.
- Supporting / enforcement mechanisms: workflow discovery/routing; project/repository context; persisted sessions/runs; model/provider abstraction; review findings; current failure/retry/approval paths.
- Closure path: not applicable at S4; reviewed adaptation paths remain present-task/repository regulation rather than prospective environment → adaptation option → present-capability return.
- Why this is / is not agent-owned: Archon's models can plan software work and react to current evidence, but the required outside-and-then organizational function itself is not established. No actor can own an absent S4 loop merely by planning ahead within one coding task.
- Evidence: [`README.md`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/README.md); [`packages/core/src/orchestrator/orchestrator-agent.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/core/src/orchestrator/orchestrator-agent.ts); [`packages/workflows/src/dag-executor.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/workflows/src/dag-executor.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: external integrations (GitHub/provider APIs) are environmental inputs, not by themselves prospective intelligence.

### Absence scope

- Surfaces inspected: orchestrator routing/project/workflow context; workflow DAG/loop/gate semantics; run/session persistence; provider/model selection; review/validation workflows; current run-attention/recovery paths; bundled default workflows/commands; repository architecture and supported operating modes.
- Plausible first-party paths checked: planning workflows; persisted history/session resume; provider capability/model selection; GitHub PR/review inputs; review findings and follow-up suggestions; retries/fallback models; workflow discovery and current project routing.
- Why no material first-party path remains: all located model-backed adaptation is coupled to a current coding/review/run objective. No first-party path was found that distinguishes future/external environmental change, develops organizational adaptation options from it and returns a selected option into Archon's present capability/current-control layer.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure was established for the assessed Archon project organization.
- Disturbance / variety regulated: workflow YAML, tool restrictions, budgets, provider/model choices, approval gates, project registration and user control constrain operation, but they do not constitute a runtime decision over what the organization ultimately is or which supreme policy should govern it.
- Decisive decision or feedback right: not established at S5. Ultimate purpose and policy remain outside the runtime in operator/developer choices; the parent user approves/rejects ordinary run/gate decisions rather than adjudicating an evidenced identity-level issue through a dedicated S5 path.
- Decision owner: not established as a first-party S5 owner.
- Supporting / enforcement mechanisms: workflow/config files; system prompts; tool restrictions; guard/gate semantics; user confirmations; provider/project settings; run-management controls.
- Closure path: not applicable at S5; no identity/ultimate-policy issue → legitimate authority → authoritative decision → returned governance loop was found.
- Why this is / is not agent-owned: Archon agents may choose workflows/actions and humans may control current runs, but neither path grants a first-party actor ultimate identity/policy authority. Current-run approval remains S3/current-operation governance rather than S5.
- Evidence: [`README.md`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/README.md); [`packages/core/src/orchestrator/prompt-builder.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/core/src/orchestrator/prompt-builder.ts); [`packages/core/src/orchestrator/manage-run-tool.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/core/src/orchestrator/manage-run-tool.ts); [`packages/providers/src/types.ts`](https://github.com/coleam00/Archon/blob/e237584d9c332fc492125bf9e0cb4756895f4da2/packages/providers/src/types.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: operator/developer control over configuration and repository governance can be institutionally important without being a shipped S5 closure at this runtime boundary.

### Absence scope

- Surfaces inspected: orchestrator system/routing prompts; project/workflow registration; workflow YAML and command prompts; provider/tool/model restrictions; approval gates; parent run-management controls; configuration; review/fix workflows; repository governance adjacent to runtime.
- Plausible first-party paths checked: human approve/reject/respond; destructive-action confirmations; project registration/removal; workflow/provider configuration; system prompts; guard/gate policy; maintainer/repository policy outside the operating runtime.
- Why no material first-party path remains: located authority either defines configuration before execution or makes ordinary current-task/run decisions. No shipped path elevates an identity/ultimate-policy dispute to a legitimate S5 authority and returns that decision as governing policy for subsequent Archon operation.

## Recursion

The focal recursion is one Archon-managed project/workspace with multiple independently active workflow runs. Each qualifying run is an operational S1 because it directly transforms the project's repository/PR environment and carries local model-backed discretion inside Archon's workflow contract. AI node turns, provider subagents and tool calls are lower-recursion operations. The five review roles are complementary audit access over S1-produced code; their parallelism does not make them a separate S2 witness.

## Variety and escalation

Archon amplifies operational variety through model-backed coding/review roles and a portable provider interface while attenuating execution variety with deterministic DAG, loop, gate and run-state semantics. Worktree isolation attenuates cross-run repository collisions. Parent run-management exposes current commitments and intervention rights without silently giving destructive authority to the model. Review workflows add a complementary challenge channel whose findings return to corrected code. Failed/paused/gated conditions can surface for intervention, but no prospective S4 or identity-level S5 closure was found.

## Evidence gaps

No evidence gap requires `?` at the frozen revision. The main interpretive boundary is deliberate: external coding-agent internals are not inherited, while first-party Archon prompt roles/provider invocation/run closure are credited where they operationally own the role and feedback path. S3 is published as `P`, not `A`, because the strongest evidenced whole-project current-control decisions remain explicitly parent-confirmed; ordinary autonomous workflow routing is insufficient to upgrade that right.
