---
harness_id: shob
project_name: Shob
repository: https://github.com/olovalabs/shob
review_ref: 381989bb4491d84e3053973df7ef97dbd67aed76
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: —
---

# Shob

## Review boundary

- System in focus: One installed Shob workspace with project panes and packaged native agent.
- Purpose and identity: Operate and supervise model-backed coding sessions across the user's projects.
- Relevant environment: Local repositories and worktrees, operator, model providers, external terminal agents and Shob release service.
- Standard-distribution boundary: Desktop GUI, terminal/agent panes, bundled embedded and RPC modes, shipped Git workspace and official-build updater paths.
- Credited operating / distribution surfaces: [Runtime architecture](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/ARCHITECTURE.md) · [Embedded runtime transport](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/agent_bridge.rs) · [Native runtime](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/agent/crates/embedded/src/lib.rs) · [Workspace view](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/main.rs)
- Adjacent first-party surfaces excluded from ownership: Upstream dependency development, contributor CI, benchmarks, and the decision internals of independently installed agents.
- First-party operating / deployment modes considered: Desktop embedded chat, bundled TUI and supported RPC baseline; status of attached terminal agents is visible at the host boundary.
- Recursion level: Workspace installation containing simultaneously active project conversations.
- Reviewed revision: 381989bb4491d84e3053973df7ef97dbd67aed76
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Shob combines local project panes, PTYs, a status bus, and persistent workspace state. Its vendored embedded library builds a model-backed session with its own tool loop, storage and provider configuration. A bundled RPC path and native TUI also expose the coding runtime. Terminal-hosted agents can contribute status events through hooks or screen detection. The desktop host keeps session state, attention badges, Git worktree choices and the official update interface.

## Operational model

An embedded pane can independently choose coding actions and produce repository changes. Multiple panes can hold distinct model sessions and working directories. The operator selects workspaces, sees project-level activity, and can stop or redirect sessions. External terminal agents contribute host-visible status only for the purposes of the first-party ownership mapping.

## S1 — Operations

- State: A
- Function: Perform coding work in a selected project or worktree through a native agent session.
- Disturbance / variety regulated: Different files, build results and task evidence require revised next actions.
- Decisive decision or feedback right: Choose the next permitted tool operation or task response as model and tool results arrive.
- Decision owner: The configured model in the native embedded or bundled coding session.
- Supporting / enforcement mechanisms: Embedded session builder, selected working directory, durable session storage and tool approval settings.
- Closure path: Agent tool results enter the session context and the agent continues, requests consent or hands back.
- Why this is / is not agent-owned: The native model determines the coding trajectory while desktop and PTY transport carry state and activity.
- Boundary reachability: The packaged desktop bridge instantiates EmbeddedSession and uses the vendored session builder; the packaged TUI starts the bundled coding loop.
- Evidence: [Desktop session bootstrap](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/agent_bridge.rs) · [Embedded session construction](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/agent/crates/embedded/src/lib.rs) · [Agent step execution](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/agent/crates/agent/src/agent_loop.rs) · [Shipped modes](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/README.md)
- Basis: structural
- Confidence: high
- Caveats: External CLI authorship is outside this ownership claim.

## S2 — Coordination

- State: C
- Function: Reduce workspace collisions between separately acting coding panes in one repository.
- Disturbance / variety regulated: Two live conversations can otherwise change the same checkout and branch state.
- Decisive decision or feedback right: Choose the destination worktree when assigning separate workspace scope to a pane.
- Decision owner: Operator through the workspace selector. No shipped agent-owned cross-pane isolation decision was established.
- Supporting / enforcement mechanisms: Git worktree creation, branch/worktree inspection, working-directory override and a guard against switching a busy pane.
- Closure path: Selecting or creating a worktree rebinds the pane workspace so subsequent model tools execute in that checkout.
- Why this is / is not agent-owned: Shob supplies the constructor that routes the next session to an isolated tree. The operator composes the relation across panes.
- Boundary reachability: Desktop pane workspace controls call create_and_switch_worktree or select_existing_worktree and apply the resulting directory before later agent turns.
- Distinct S1 units: Two separately prompted native agent conversations can act in the same repository via separate workspace panes.
- Inter-S1 disturbance: Simultaneous edits, branch checkouts or build artifacts in a shared checkout can alter another session's working state.
- Attenuating coordination relation: Assign disjoint Git worktrees and branches to the panes using the built-in switcher.
- Feedback into subsequent S1 behaviour: The selected folder becomes the next model session's tool working directory and the workspace state records the selection.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The constructor partitions mutable checkout state and checks active worktree placement, directly reducing concrete editing and checkout interference.
- Evidence: [Worktree creation and application](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/workspace_switcher.rs) · [Worktree and branch model](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/git_workspace.rs) · [Pane turn working directory](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/agent_composer.rs)
- Basis: structural
- Confidence: medium
- Caveats: Worktree isolation does not reconcile eventual merge conflicts or isolate all shared external state.

## S3 — Inside-and-now control

- State: P
- Function: Intervene in current work across the visible workspace sessions.
- Disturbance / variety regulated: Follow-up queues and running tasks can continue consuming attention or resources after priorities change.
- Decisive decision or feedback right: Select an active conversation from the current view and cancel its running turn and queued requests as a current commitment decision.
- Decision owner: Workspace operator.
- Supporting / enforcement mechanisms: Status bus, cross-pane attention state, session selection, stop button and bridge cancellation.
- Closure path: The selected session clears queued follow-ups and pauses them; cancellation returns into its bridge and runtime.
- Why this is / is not agent-owned: The app tracks status and applies a chosen stop. The operator decides which current commitment to interrupt.
- Boundary reachability: The desktop app loops over tracked panes to surface work status, and the native chat composer exposes cancellation for selected embedded work.
- Whole-system current view: The desktop attention pass tracks the workspace's panes and exposes blocked, running and completed work across projects.
- Current-control decision scope: The operator can discontinue a selected running native turn and remove its queued follow-up work while other panes continue.
- Evidence: [Workspace-wide attention pass](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/main.rs#L6631-L6709) · [Attention state model](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/attention.rs) · [Stop and queue effect](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/agent_composer.rs#L931-L945) · [Session bridge](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/agent_bridge.rs)
- Basis: structural
- Confidence: medium
- Caveats: This parent mode governs current work within one Shob installation. No autonomous resource allocator is established.

## S3* — Complementary audit

- State: —
- Function: Independently challenge an operational claim and return a finding into corrective regulation.
- Disturbance / variety regulated: An agent's reported edits or completion can differ from the actual worktree.
- Decisive decision or feedback right: No installed claim-specific audit decision and corrective return construction was established.
- Decision owner: Operator can inspect a worktree, while ordinary coding reports are supplied by the agent.
- Supporting / enforcement mechanisms: Git project diff, transcript display and terminal status detection.
- Closure path: The diff reaches an inspection pane. Further review and a corrective task are chosen separately.
- Why this is / is not agent-owned: The host exposes raw repository changes and ordinary status signals. Neither path adjudicates a run claim or binds a finding to correction.
- Evidence: [Project change viewer](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/main.rs#L7576-L7605) · [Independent source diff](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/project_diff.rs) · [Terminal reporting signals](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/status_bus.rs) · [Comparison with native loop](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/agent/crates/agent/src/agent_loop.rs)
- Basis: structural
- Confidence: medium
- Caveats: The operator could compose a separate external review using the displayed diff.

### Absence scope

- Surfaces inspected: Project changes viewer, embedded coding loop, session reporting, status bus and bundled child/extension integration.
- Plausible first-party paths checked: Raw Git changes versus ordinary reports, review work assigned to separate children, and change acceptance feedback.
- Why no material first-party path remains: The Git diff is a general repository view. Status and child reporting feed supervision without a supplied audit trigger, claim judgement and corrective return path.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adopt an externally published future version of the installed Shob capability.
- Disturbance / variety regulated: Upstream releases can add capability or change behavior relative to the installed version.
- Decisive decision or feedback right: Decide whether to install a surfaced stable update for a supported installation type.
- Decision owner: Installation operator.
- Supporting / enforcement mechanisms: Stable release lookup, platform filtering, delta or full asset validation and update application.
- Closure path: The operator authorizes the upgrade and subsequent runs load the replacement build.
- Why this is / is not agent-owned: The official-build check senses and offers the release; the operator owns adoption.
- Boundary reachability: The supported official builds expose startup availability and installation via the packaged updater or desktop Settings.
- External distinction: The updater consults the Shob GitHub stable release endpoint.
- Future / prospective distinction: Adoption changes the executable used on subsequent sessions.
- Adaptation option generated: The product compares installed and external stable releases and offers an eligible platform update.
- Path back into current capability / S3: The selected delta or full replacement updates the installed runtime.
- Evidence: [Release selection and installation](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/updater.rs) · [Supported update routes](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/README.md#L94-L102)
- Basis: structural
- Confidence: medium
- Caveats: The positive mode is bounded to shipped update-capable builds; some distribution formats use separate package managers.

## S5 — Policy and identity

- State: —
- Function: Resolve ultimate identity, mission, or policy tensions at workspace level.
- Disturbance / variety regulated: Permissions and provider choices can affect what operator-directed work the workspace carries out.
- Decisive decision or feedback right: No ultimate-policy decision and governance return path was established.
- Decision owner: The operator controls scoped permissions, provider credentials and workspace choices.
- Supporting / enforcement mechanisms: Persisted approval selection and project/user configuration.
- Closure path: Subsequent tool and session activity follows the saved local configuration.
- Why this is / is not agent-owned: These settings close scoped operational choices, without a separate installation identity decision or S3–S4 policy resolution.
- Evidence: [Permission and provider operation](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/README.md) · [Host architecture and configuration](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/ARCHITECTURE.md) · [Agent authentication](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/agent_auth.rs) · [Composer controls](https://github.com/olovalabs/shob/blob/381989bb4491d84e3053973df7ef97dbd67aed76/src/agent_composer.rs)
- Basis: structural
- Confidence: medium
- Caveats: Repository maintainers and model-provider policy act at different recursion levels.

### Absence scope

- Surfaces inspected: Native permissions, host settings, workspace state, provider auth and update controls.
- Plausible first-party paths checked: Operator mission or authority changes, adaptive-update conflicts returned to an ultimate decision, and scope of saved permissions.
- Why no material first-party path remains: Shob supplies task access and capability choices. The reviewed paths do not expose an ultimate-policy issue and returned governing decision.

## Recursion

The installation has independent operation cells in project panes; an externally attached agent can itself have separate internal recursion. Child status labels do not establish an additional viable system.

## Variety and escalation

Attention rules promote blocked and completed states to the user who can redirect native work; Git checkout isolation reduces file and branch interference; remote publisher updates enter the operator's future capability decision.

## Evidence gaps

No GUI, provider, or updater was run. Attention-to-stop, workspace binding and updates were traced in the pinned source. No independent complementary audit loop was established.
