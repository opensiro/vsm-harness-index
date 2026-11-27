---
harness_id: penelope
project_name: Penelope
repository: https://github.com/LaertesAI/Penelope
review_ref: 99ffa8fb41a4dfc944efb995a0264956f2d983d7
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# Penelope

## Review boundary

- System in focus: The installed Penelope CLI/TUI and its native agent and cluster runtimes.
- Purpose and identity: Run local coding and research tasks while making model choice, work, checks and costs visible.
- Relevant environment: A user's repository and local profile, optionally backed by model APIs or the Claude CLI.
- Standard-distribution boundary: Shipped Penelope CLI/TUI, model integration, local tool dispatch, and supplied cluster machinery configured with inference providers.
- Credited operating / distribution surfaces: Native API tool loop, crew and cluster workers, cluster validator and control tools, persistent tool forge.
- Adjacent first-party surfaces excluded from ownership: Model services, Claude CLI internals, development benchmarks, external MCP servers and application integrations.
- First-party operating / deployment modes considered: Interactive native API and Claude CLI sessions, named agents, and optional profile-driven clusters.
- Recursion level: One Penelope workspace. Cluster workers and independent quorum runs are subordinate activity units.
- Reviewed revision: 99ffa8fb41a4dfc944efb995a0264956f2d983d7
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The native model path builds tool schemas from role-specific capabilities and runs local tool feedback. Configured cluster profiles assemble worker waves with dependencies, separate verification, quotas and optional worktree return. A separate recorded cluster state exposes commitments and control operations. Persistent tools and cluster profiles can modify what subsequent runs have available.

## Operational model

The lead produces a coding or research result by choosing tools and using observations. Cluster workers act within their assigned focus. A second quorum run may independently answer the same work, after which a decider resolves disagreement. Cluster validation runs its own checks and decides whether feedback or acceptance follows.

## S1 — Operations

- State: A
- Function: Deliver a user-directed coding or research turn.
- Disturbance / variety regulated: Diverse requests, tool failures and missing workspace evidence.
- Decisive decision or feedback right: Select tools and interpret results before returning an answer.
- Decision owner: The configured lead model operating through Penelope's native loop.
- Supporting / enforcement mechanisms: Role-based tool policy, local dispatch, history, model adapters and turn bounds.
- Closure path: Tool observations return to the model and the loop renders an answer or reports failure.
- Boundary reachability: The installed API mode wires the backend to Penelope's own tool loop. It needs provider configuration without a user-authored actor.
- Why this is / is not agent-owned: The shell, files and checks are supporting surfaces. The model makes the task-level choices.
- Evidence: [cli/src/backend.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/backend.rs#L350-L379), [cli/src/llm.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/llm.rs#L347-L420), [README.md](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/README.md#L420-L428)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Individual edit and command policies can require authorization.

## S2 — Coordination

- State: A
- Function: Resolve interference between independently produced answers before cluster work consumes them.
- Disturbance / variety regulated: Two model runs on the same cluster task may return incompatible answers.
- Decisive decision or feedback right: Choose or synthesize the operative answer when the two runs disagree.
- Decision owner: The profile-selected quorum decider model.
- Supporting / enforcement mechanisms: Blind second answer, comparison, role-aware routing and hard budgets.
- Closure path: The selected result replaces the disputed worker output in the persisted note supplied to later cluster activity.
- Boundary reachability: Optional quorum config activates the shipped paired-run and decider path.
- Why this is / is not agent-owned: Quorum's text comparator detects disagreement. The decider chooses the accepted output.
- Distinct S1 units: The primary part run and a distinct second model run with a separately computed result.
- Inter-S1 disturbance: Incompatible answers to one focus would otherwise compete as evidence for the remaining cluster.
- Attenuating coordination relation: Detect disagreement, invoke a dedicated decider and persist one replacement result.
- Feedback into subsequent S1 behaviour: Downstream worker or validator reads the persisted result with the decision recorded in cluster memory.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: It reconciles inconsistent outputs before later work consumes them. Basic dependency scheduling does not perform this judgment.
- Evidence: [cli/src/clusters.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/clusters.rs#L1805-L1828), [cli/src/clusters.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/clusters.rs#L1979-L1999), [cli/src/clusters.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/clusters.rs#L2019-L2047)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: The second actor uses the prepared task context without tools. Quorum is configurable.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate live cluster commitments within the local workspace.
- Disturbance / variety regulated: A stale or stalled cluster may consume budget or retain a commitment that should be cancelled or restarted.
- Decisive decision or feedback right: Select a named run to stop, dump or respawn using its persisted current state.
- Decision owner: The lead model on its tool surface and the legitimate workspace operator in the CLI/TUI supervision mode.
- Supporting / enforcement mechanisms: Cluster state/report projection, cancellation flag, cleanup and bounded retries.
- Closure path: The chosen control action changes the persisted cluster state and interrupts or restarts its operative work.
- Boundary reachability: The MCP dispatch exposes clustered current status and control to the lead, while direct CLI/TUI commands provide the operator path.
- Why this is / is not agent-owned: Watchdog limits enforce local constraints. The discretionary choice of which live commitment to intervene in belongs to the actor requesting the intervention.
- Whole-system current view: Workspace-wide cluster inventory with task and state plus per-cluster part, evidence and progress projection.
- Current-control decision scope: Intervention in identified live cluster commitments through status, cancellation and restart.
- Evidence: [cli/src/mcp.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/mcp.rs#L159-L170), [cli/src/clusters.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/clusters.rs#L3129-L3168), [cli/src/clusters.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/clusters.rs#L3306-L3324), [cli/src/main.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/main.rs#L308-L331), [cli/src/tui/mod.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/tui/mod.rs#L1555-L1580)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Conditional on the deployed cluster model and the workspace tool mode.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Workspace lead model | Cluster status shows a failed or obsolete commitment | Lead invokes the stop or restart tool and persisted live state changes. | [cli/src/mcp.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/mcp.rs#L159-L170) |
| Parent (`P`) | Workspace operator | Current cluster board and evidence reveal a commitment needing intervention | Operator issues the CLI/TUI command and the cluster stops or restarts. | [cli/src/main.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/main.rs#L308-L331) |

## S3* — Complementary audit

- State: A
- Function: Independently verify a cluster's claim of completed work.
- Disturbance / variety regulated: Worker notes and a plausible reported result may overstate successful completion.
- Decisive decision or feedback right: Choose PASS or FAIL after acquiring direct project evidence.
- Decision owner: The configured validator model in a separate role.
- Supporting / enforcement mechanisms: Validator-specific tool calls, evidence capture, passing-check constraint and proof requirement.
- Closure path: Accepted notes become confirmed. A FAIL stales them and returns concrete feedback into bounded worker retries. Worktree application requires validation.
- Boundary reachability: The runtime constructs a separate validator run from the supplied cluster-profile slot and feeds the verdict into its acceptance loop.
- Why this is / is not agent-owned: The validator directly inspects the work and adjudicates. The proof check enforces its evidence standard.
- Claim being audited: Worker claims that the cluster task is complete.
- Ordinary reporting path: Worker output and persisted part notes.
- Complementary access path: Separate model-run validator reads project files or runs checks independently of the worker report.
- Independence boundary: Distinct validator role and recorded direct check, with model identity permitted to be shared.
- Who acts on findings: The cluster orchestrator consumes it in the worker retry or acceptance path.
- Evidence: [cli/src/clusters.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/clusters.rs#L1737-L1746), [cli/src/clusters.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/clusters.rs#L2107-L2166), [cli/src/clusters.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/clusters.rs#L2371-L2429)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Applies to a validator-enabled profile and not to the answer-only quorum comparison.

## S4 — Outside-and-then intelligence

- State: A
- Function: Adapt the workspace's reusable capabilities after observing repeated external command work.
- Disturbance / variety regulated: Recurrent project or environment interactions expose operations the installed tool set handles inefficiently.
- Decisive decision or feedback right: Decide whether a discovered repeating command warrants a new persistent tool, then supply and register its schema.
- Decision owner: The workspace lead model.
- Supporting / enforcement mechanisms: Forge schema validation, tool configuration storage, reload on tool enumeration and ordinary execution policy.
- Closure path: The generated tool persists and is discoverable by later lead and worker turns. Its calls retain ordinary authorization policy.
- Boundary reachability: A shipped lead prompt directs reusable tool creation. The standard dispatcher and tool enumeration wire the new definition back into operation.
- Why this is / is not agent-owned: The model decides which capability to add from observed work. The registry validates and makes it accessible.
- External distinction: Repeated commands discovered in the external project or workspace environment.
- Future / prospective distinction: Whether later work will need the same operation and could use a stable interface.
- Adaptation option generated: A new persistent tool contract for future sessions.
- Path back into current capability / S3: Tool enumeration reads the saved contract and the dispatch checks it as a lead or worker tool.
- Evidence: [cli/src/backend.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/backend.rs#L101-L118), [cli/src/mcp.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/mcp.rs#L29-L45), [cli/src/mcp.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/mcp.rs#L140-L147), [cli/src/forge.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/forge.rs#L101-L141), [cli/src/tui/mod.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/tui/mod.rs#L1955-L1959)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Scope is tool capability adaptation. Shadow measurements and operator-applied model advice serve distinct purposes.

## S5 — Policy and identity

- State: —
- Function: No distinct ultimate identity or policy settlement was established.
- Disturbance / variety regulated: Users can choose permission presets and add instruction notes.
- Decisive decision or feedback right: No distinct decision right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Modes, tool policy and persistent rule notes.
- Closure path: Mode selection rewrites the fixed settings and later calls observe the corresponding gates.
- Why this is / is not agent-owned: The checked paths change configured parameters and instructions within the installed workspace's existing authority scheme.
- Evidence: [cli/src/mode.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/mode.rs#L28-L55), [cli/src/route.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/route.rs#L198-L214), [cli/src/tui/mod.rs](https://github.com/LaertesAI/Penelope/blob/99ffa8fb41a4dfc944efb995a0264956f2d983d7/cli/src/tui/mod.rs#L1539-L1552)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: The finding is bounded to the installed local workspace.

### Absence scope

- Surfaces inspected: Permission modes, global/session rule writing and lead tool authority.
- Plausible first-party paths checked: A workflow to resolve disputed organizational identity or determine who has final authority and return that settlement.
- Why no material first-party path remains: The supported settings and notes carry user preferences and fixed profile choices. No first-party identity or ultimate-purpose adjudication was found.

## Recursion

The instance is the workspace. Cluster profiles, runs and validators are internal roles. An external model provider or an MCP server has its own operational recursion.

## Variety and escalation

Missing role models, budget limits, stuck workers, worktree conflicts and incomplete checks yield distinct failure or retry outcomes. The operator can inspect persisted running and terminal states.

## Evidence gaps

Pinned-source assessment. No model provider, private workspace, browser or execution traces were used to assign grades.
