---
harness_id: pydantic-deep
project_name: Pydantic Deep
repository: https://github.com/vstorm-co/pydantic-deepagents
review_ref: 650b592b6accd7dc994226abbaa0cf717527e457
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# Pydantic Deep

## Review boundary

- System in focus: One Pydantic Deep coding session and its optional live-fork branch organization on a configured workspace.
- Purpose and identity: Carry out coding/tool tasks and incorporate selected operating knowledge into future sessions.
- Relevant environment: User requests, project worktree and toolchain, model providers, and available workspace/tool backends.
- Standard-distribution boundary: Installed Pydantic Deep CLI/TUI and shipped agent construction/capabilities at this commit.
- Credited operating / distribution surfaces: Headless and interactive CLI, packaged model/tool loop, opt-in live fork and teams, branch judge, and TUI improvement review.
- Adjacent first-party surfaces excluded from ownership: Development and benchmark jobs, demonstrations, repository governance and CI, and optional customer compositions outside the shipped path.
- First-party operating / deployment modes considered: Headless single task, interactive local workspace, optional SDK capabilities, model-driven and operator-driven fork control. The adaptation witness uses the local workspace TUI.
- Recursion level: One lead session and its subordinate task/branch S1 units, including the bounded current fork when active.
- Reviewed revision: `650b592b6accd7dc994226abbaa0cf717527e457`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The package installs a CLI and builds a model-backed agent with workspace tools and run-level state. The TUI adds check-pointed live forks, per-branch isolation, operator intervention, model judges and a session-based improvement analyzer. Hosted model inference and workspace backends execute or support decisions in the assessed assembly. [`pyproject.toml`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pyproject.toml#L120-L130), [`apps/cli/run.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/run.py#L85-L142), [`apps/cli/agent.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/agent.py#L493-L527), [`pydantic_deep/features/forking/coordinator.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/coordinator.py#L519-L599), [`apps/cli/commands.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/commands.py#L677-L715).

## Operational model

The ordinary unit produces a coding or workspace outcome through its own model-led tool loop. A fork can give distinct live branches separate local instructions, state and tool feedback. Fork coordination maintains isolation and an admitted common workspace. The lead or operator can regulate ongoing commitments. A distinct judge may check the artifacts behind a branch's report before selection. The operator is the deciding authority for the evidenced cross-session adaptation loop. [`pydantic_deep/features/forking/coordinator.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/coordinator.py#L541-L599), [`pydantic_deep/features/forking/coordinator.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/coordinator.py#L980-L1024), [`pydantic_deep/features/forking/__init__.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/__init__.py#L171-L241), [`pydantic_deep/features/forking/coordinator.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/coordinator.py#L1327-L1377), [`apps/cli/commands.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/commands.py#L677-L715).

## S1 — Operations

- State: A
- Function: Complete coding and workspace tasks through model-selected tool action.
- Disturbance / variety regulated: Uncertain requirements, changing workspace observations and tool results.
- Decisive decision or feedback right: Choose what to inspect, edit or execute and choose subsequent actions from tool feedback.
- Decision owner: The configured model-backed Pydantic Deep agent.
- Supporting / enforcement mechanisms: Pydantic AI execution, installed CLI, workspace, toolsets and usage limits.
- Closure path: The CLI passes the task to the constructed agent run and returns the resulting answer. During the run, tool responses inform the next action.
- Boundary reachability: The package exposes the CLI and its headless entry calls the shipped agent factory and run directly.
- Why this is / is not agent-owned: Removing the model leaves configured capabilities and limits but removes discretionary task action.
- Evidence: [`pyproject.toml`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pyproject.toml#L120-L130); [`apps/cli/run.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/run.py#L85-L142); [`apps/cli/agent.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/agent.py#L493-L527); [`pydantic_deep/agent.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/agent.py#L1489-L1544)
- Basis: structural
- Confidence: High for source reachability.
- Caveats: Requires a configured compatible model and operating workspace.

## S2 — Coordination

- State: A
- Function: Prevent simultaneously executing alternate coding branches from contaminating each other's workspace state during exploration and reconvergence.
- Disturbance / variety regulated: Competing branches may independently edit the same destination path, with incompatible results or a write that can distort another running branch's fallback read.
- Decisive decision or feedback right: Inspect the active fork and choose which branch's changes may become shared state, or discard the fork.
- Decision owner: The model-backed parent-run agent in the agent-driven mode. Deterministic workspace isolation maintains separation during exploration.
- Supporting / enforcement mechanisms: Per-branch overlays, changed-path comparison, merge lock, and cancellation before shared writes.
- Closure path: Branch-local writes feed subsequent branch-local reads. At convergence the chosen overlay is flushed, competitors are quiesced before they can observe that flush, and the surviving context governs continued work.
- Boundary reachability: Interactive CLI enables forking by default and registers shipped fork, diff, inspect and resolve tools. SDK provides the same opt-in capability.
- Why this is / is not agent-owned: The branch views and quiescence rule are deterministic. Choice of the mutually exclusive active path is delegated to the model-backed parent agent in the claimed mode.
- Distinct S1 units: Two or more separately tasked branches, each running a model loop in its own cloned dependencies and workspace.
- Inter-S1 disturbance: Incompatible writes to the same relative path and visibility of an adopted version to another still-running branch.
- Attenuating coordination relation: Local overlay containment, cross-branch diff and exactly one admitted overlay with other branches cancelled.
- Feedback into subsequent S1 behaviour: Each branch reads its own state while running. At convergence the selected workspace becomes the continuation baseline and competing writers stop.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The implemented relation addresses an identified shared-file interference path and changes which state can enter an active work unit.
- Evidence: [`pydantic_deep/features/forking/coordinator.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/coordinator.py#L541-L599); [`pydantic_deep/features/forking/isolation.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/isolation.py#L315-L340); [`pydantic_deep/features/forking/diff.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/diff.py#L122-L154); [`pydantic_deep/features/forking/__init__.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/__init__.py#L207-L241); [`pydantic_deep/features/forking/coordinator.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/coordinator.py#L980-L1024); [`apps/cli/commands.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/commands.py#L981-L1007)
- Basis: structural
- Confidence: Moderate to high in live workspace-fork mode.
- Caveats: Shared TODO state and team messaging are additional surfaces; they are not the S2 witness used here.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate the current fork's active commitments across its model-driven work branches.
- Disturbance / variety regulated: Running, failed or cost-exhausted branches competing to continue a single active job.
- Decisive decision or feedback right: Use the current fork-wide status and cost view to terminate branches or abort, leaving a changed portfolio of ongoing commitments.
- Decision owner: Model-backed lead in the agent-tool mode, and session operator in the separate TUI mode.
- Supporting / enforcement mechanisms: Fork summary, branch status and cost tracking, stop/merge tools and preconfigured budget caps.
- Closure path: Cancellation updates the branch lifecycle and removes its consumption. An abort releases the fork or a picked branch returns a selected history and workspace to the parent run.
- Boundary reachability: The shipped agent and TUI expose the same fork runtime and explicit intervention controls.
- Why this is / is not agent-owned: In agent mode the agent can decide whether and when to terminate or abandon existing work; automatic caps merely enforce their presets. The TUI supplies a separate operator-owned path.
- Whole-system current view: At declared fork-session recursion, inspection spans every active branch and the fork cost view aggregates the branches.
- Current-control decision scope: Intervene in running branch commitments, abandon the fork or authorize the surviving commitment.
- Evidence: [`pydantic_deep/features/forking/__init__.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/__init__.py#L171-L205); [`pydantic_deep/features/forking/__init__.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/__init__.py#L241-L275); [`pydantic_deep/features/forking/__init__.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/__init__.py#L353-L368); [`pydantic_deep/features/forking/coordinator.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/coordinator.py#L805-L851); [`apps/cli/forking.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/forking.py#L101-L171); [`apps/cli/commands.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/commands.py#L967-L1012)
- Basis: structural
- Confidence: Moderate to high at session recursion.
- Caveats: No cross-tenant or multi-project resource authority is inferred.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Lead model agent | Inspect an active fork and decide a branch or fork should cease | Terminate or abort the corresponding running work and continue at the returned baseline | [`pydantic_deep/features/forking/__init__.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/__init__.py#L171-L205), [`pydantic_deep/features/forking/__init__.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/__init__.py#L241-L275), [`pydantic_deep/features/forking/__init__.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/__init__.py#L353-L368) |
| Parent (`P`) | Authorized interactive session operator | Review current active fork and decide which commitment to keep or stop | The TUI invokes the coordinator, commits the selected workspace/history and clears the fork | [`apps/cli/forking.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/forking.py#L140-L171), [`apps/cli/commands.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/commands.py#L967-L1012) |

## S3* — Complementary audit

- State: A
- Function: Corroborate branch claims against materialized changes and optional separate test execution before controlling fork resolution.
- Disturbance / variety regulated: A branch's textual report may overstate task completion or disagree with the edited artifacts or measured outcomes.
- Decisive decision or feedback right: A separately instantiated judge assesses the actual branch evidence and selects the supported winning branch in auto/vote mode.
- Decision owner: First-party model-backed judge, or the model panel in vote mode with deterministic aggregation.
- Supporting / enforcement mechanisms: Structured outcomes, independent diff collection, optional coordinator-run branch tests, structured verdict and merge dispatcher.
- Closure path: The judge verdict selects the branch to adopt in auto/vote mode, causing application of its overlay and cancellation of competitors. CLI replays the selected history.
- Boundary reachability: The shipped CLI exposes the automated merge strategies and routes the coordinator's committed result into session state.
- Why this is / is not agent-owned: The judge owns the evaluative selection. Test execution, diff computation and application of the verdict are supporting machinery.
- Claim being audited: Whether a branch actually fulfilled its assigned task.
- Ordinary reporting path: The branch's own final assistant message and run counters.
- Complementary access path: The coordinator assembles changed-file diffs directly from workspace state and, where configured, runs a separate test command against the branch snapshot.
- Independence boundary: A new judge request receives the branch goal, bounded reports and complementary evidence rather than participating in the coding turn or relying on the branch narrative alone.
- Who acts on findings: The coordinator commits the selected outcome in auto/vote mode, and the session continues on the adopted state.
- Evidence: [`pydantic_deep/features/forking/coordinator.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/coordinator.py#L1070-L1120); [`pydantic_deep/features/forking/coordinator.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/coordinator.py#L1163-L1220); [`pydantic_deep/features/forking/coordinator.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/coordinator.py#L1327-L1377); [`pydantic_deep/features/forking/judge.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/judge.py#L144-L166); [`pydantic_deep/features/forking/judge.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/forking/judge.py#L283-L322); [`apps/cli/commands.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/commands.py#L1057-L1075); [`apps/cli/commands.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/commands.py#L1106-L1121)
- Basis: structural
- Confidence: Moderate to high for the source path.
- Caveats: Optional live fork audit. Local test execution requires a compatible workspace and detected or configured test command. Manual branch selection does not exercise this automated audit.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adapt future coding behavior from actual encounters with the project's environment, build commands and toolchain.
- Disturbance / variety regulated: Project-specific workflow and environment differences encountered across sessions which would otherwise cause repeated ineffective approaches.
- Decisive decision or feedback right: Select the proposed durable adaptation to admit into project guidance after reviewing the synthesis report.
- Decision owner: The project session operator. Extraction and synthesis agents propose the options.
- Supporting / enforcement mechanisms: Session archive, raw tool traces, extraction and synthesis models, review modal and context file loading.
- Closure path: The operator selects the proposed guidance, the CLI writes selected changes to project context, and the supported local-workspace mode reloads context for subsequent agent work.
- Boundary reachability: The installed TUI includes `/improve`, admission by selection and the first-party context reader.
- Why this is / is not agent-owned: The analyzer can choose what to propose. Its installed automatic-analysis path does not own the persistence decision in the evidenced loop.
- External distinction: Workspaces, build/test commands, project tools and dependencies encountered outside the harness, captured in tool outcomes.
- Future / prospective distinction: The prompt explicitly identifies reusable strategies for later sessions and recurring project situations.
- Adaptation option generated: For example a proposed reusable build/test practice in AGENTS.md based on observed first-party session traces.
- Path back into current capability / S3: Operator review selects applicable proposals, the analyzer changes the project instructions, and the agent incorporates the changed context during subsequent work.
- Evidence: [`pydantic_deep/features/improve/prompts.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/improve/prompts.py#L27-L36); [`pydantic_deep/features/improve/prompts.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/improve/prompts.py#L93-L127); [`pydantic_deep/features/improve/analyzer.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/improve/analyzer.py#L193-L215); [`apps/cli/commands.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/commands.py#L677-L715); [`pydantic_deep/features/improve/analyzer.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/improve/analyzer.py#L288-L320); [`pydantic_deep/features/context/capability.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/context/capability.py#L48-L68); [`apps/cli/agent.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/agent.py#L513-L526)
- Basis: structural
- Confidence: Moderate for the local CLI project-guidance mode.
- Caveats: Assessment does not infer closed adaptation from memory persistence alone or claim the configured SDK always enables improvement.

## S5 — Policy and identity

- State: —
- Function: No supported ultimate-policy adjudication is evidenced at the assessed session/workspace level.
- Disturbance / variety regulated: Project style, task permissions and fork conflicts pass through lower-level configuration, approvals and control decisions.
- Decisive decision or feedback right: No shipped escalation from a conflict over the harness's ultimate purpose or risk policy into a binding adjudication was identified.
- Decision owner: No qualifying owner is established inside the reviewed runtime boundary.
- Supporting / enforcement mechanisms: Configurable instructions, approvals, instruction discovery and apply-selected context changes.
- Closure path: Their returned decisions govern the project task, future techniques or style. The shipped paths do not adjudicate the harness's ultimate identity/authority.
- Why this is / is not agent-owned: The available agent and parent paths are scoped to operations, branch control and prospective project guidance.
- Evidence: [`pydantic_deep/features/improve/prompts.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/improve/prompts.py#L108-L127); [`pydantic_deep/features/context/service.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/pydantic_deep/features/context/service.py#L19-L51); [`apps/cli/config.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/config.py#L132-L174); [`apps/cli/commands.py`](https://github.com/vstorm-co/pydantic-deepagents/blob/650b592b6accd7dc994226abbaa0cf717527e457/apps/cli/commands.py#L699-L715)
- Basis: structural
- Confidence: Moderate within the examined distribution.
- Caveats: Repository maintainers and host application owners are outside this session recursion.

### Absence scope

- Surfaces inspected: Agent instructions, TUI settings and approvals, fork control and improvement targets, project context loader, repository governance boundary.
- Plausible first-party paths checked: Model instruction changes, SOUL.md updates, choice of active branch, manual permissions and OSS parent involvement.
- Why no material first-party path remains: SOUL update prompts address behavior preferences, and intervention controls concern an active job or settings. None establishes an ultimate-policy matter reaching an authority for adjudication and subsequent binding return at this recursion.

## Distributed OSS parent arrangement

The local workspace operator is the parent in the supported supervisory and adaptation modes. The source repository's maintainer governance is outside the assessed runtime.

## Self-hosted and non-human modes

The packaged SDK can be embedded with configured models/workspaces. The interactive runtime can use an operator, while headless mode runs individual tasks. No organization-level authority is inferred from deployment topology.

## Recursion

The session is the assessed whole. Fork branches are locally agentic work units inside the active fork. External providers and shared hosting organizations remain outside.

## Variety and escalation

Tool feedback, branch-local workspace isolation, status views, bounded usage, stop controls and operator review absorb different disturbances. A normal tool approval or branch status does not by itself establish an algedonic channel.

## Evidence gaps

Source inspection at the exact revision. No end-to-end provider run was conducted. The analysis does not establish generalized team resource allocation, complete rewind semantics, or continuous independent audit beyond the stated fork paths.
