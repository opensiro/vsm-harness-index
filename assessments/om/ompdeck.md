---
harness_id: ompdeck
project_name: OmpDeck
repository: https://github.com/lavinhoque33/omp-deck
review_ref: 792cbff3d8c2ab041e03dcc33c5583fba38b4694
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: —
---

# OmpDeck

## Review boundary

- System in focus: One OmpDeck installation, its gateway, and the required omp session fleet as operated through first-party extensions.
- Purpose and identity: Run, coordinate and supervise parallel coding work while preserving working directories, sessions and artifacts.
- Relevant environment: Operator, local projects and worktrees, separate omp distribution and providers, release feed, and optional paired phone.
- Standard-distribution boundary: Desktop, gateway, native session host or dedicated tmux backend, bundled omp extension, and paired remote control when enabled.
- Credited operating / distribution surfaces: [Distribution and operating features](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/README.md) · [Bundled agent extension](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-core/assets/ompdeck-ctl.ts) · [Gateway tool dispatch](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-service/src/gateway/engine/agent_tools.rs)
- Adjacent first-party surfaces excluded from ownership: Upstream omp features beyond the integrated paths, provider internals, GitHub repository governance, development recordings and tests.
- First-party operating / deployment modes considered: Desktop with live control and enabled tool roster, legacy terminal sessions, and optional paired companion with the same gateway.
- Recursion level: Installation across desktop and gateway sessions, with separate worktree-owned operations.
- Reviewed revision: 792cbff3d8c2ab041e03dcc33c5583fba38b4694
- Observation date: 2026-11-20
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The installed application finds or helps install omp. The local gateway and host manage terminal processes that survive detachment. The shipped extension plugs platform-specific tools into live omp sessions, dispatches model requests to the gateway, and returns results. Session journals and process activity feed a fleet view. The changes pane reads Git state separately from the ordinary chat stream.

## Operational model

Each live omp session can act on a coding task in its checkout. In the enabled first-party tool mode a model can create and steer individually operating child sessions through OmpDeck, so operational agency reaches the product through a supported assembly. The desktop operator can view and interrupt work. Unsupported omp internals are outside the credited boundary.

## S1 — Operations

- State: A
- Function: Perform model-directed work across coding sessions and produce workspace outcomes.
- Disturbance / variety regulated: Work needs different tools, project scopes or parallel investigations depending on intermediate results.
- Decisive decision or feedback right: Choose the next action, including whether to create, prompt, wait for or steer operational sessions through the installed tool surface.
- Decision owner: The configured model inside the required omp operation cell.
- Supporting / enforcement mechanisms: OmpDeck's bundled extension, gateway dispatch, child handles and persistent terminal host.
- Closure path: Workspace evidence and first-party child tool results return to the same or originating model session.
- Why this is / is not agent-owned: The model determines what to work on next and selects platform operations. The host supplies lifecycle, routing and tool enforcement.
- Boundary reachability: The shipped extension registers OmpDeck operations in supported live-control sessions. The native gateway starts and governs the corresponding omp processes when the operator enables those tools.
- Evidence: [Required session runtime](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/README.md) · [Registered tool choices](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-core/assets/ompdeck-ctl.ts) · [Native tool dispatch and closure](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-service/src/gateway/engine/agent_tools.rs)
- Basis: structural
- Confidence: high
- Caveats: The coding brain is a separately installed dependency. The claim credits its wired participation, without importing its unrelated standalone capabilities.

## S2 — Coordination

- State: A
- Function: Partition parallel coding runs to reduce checkout and branch interference.
- Disturbance / variety regulated: Two workers launched against the same repository can otherwise edit the same checkout or change its branch state.
- Decisive decision or feedback right: Choose the fan-out task partition and use or change the supplied per-child worktree arrangement.
- Decision owner: Originating model using the enabled fan-out tool.
- Supporting / enforcement mechanisms: Gateway fan-out state, default worktree isolation, Git branch support, and combined result delivery.
- Closure path: Worker prompts execute in distinct worktrees. Returned handles and results let the originating model adjust subsequent work or select a finish path.
- Why this is / is not agent-owned: The caller model chooses whether and how to partition the work and may select branches. The runtime creates and tracks the chosen isolation.
- Boundary reachability: The bundled extension registers fan-out and the gateway invokes the group execution path with worktrees enabled by default.
- Distinct S1 units: Parallel child omp sessions each execute an initial task in its own persistent process and can choose task actions.
- Inter-S1 disturbance: Parallel writes and branch operations would alter each other's working tree when those sessions share the same checkout.
- Attenuating coordination relation: The model selects a multi-task fan-out with separate Git worktrees and branch options; the gateway binds each child before its prompt runs.
- Feedback into subsequent S1 behaviour: Children operate from the selected paths and the opener obtains structured outcomes and can send a follow-up or initiate finish.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Separate mutable Git trees prevent a specific shared-checkout conflict. Session messaging alone supplies no such attenuation.
- Evidence: [Fan-out tool and defaults](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-core/assets/ompdeck-ctl.ts) · [Group lifecycle and returned result](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-service/src/gateway/engine/agent_tools/children/fanout.rs) · [Worktree creation](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-core/src/worktree.rs)
- Basis: structural
- Confidence: medium
- Caveats: Isolation does not guarantee compatibility of the final changes when merged.

## S3 — Inside-and-now control

- State: P
- Function: Regulate current commitments and process use across the installation's active fleet.
- Disturbance / variety regulated: Work can remain active while detached and retain memory or continue an unneeded commitment.
- Decisive decision or feedback right: Choose which independently running sessions to stop or restart from the shared current state.
- Decision owner: Installation operator.
- Supporting / enforcement mechanisms: Workspace running dock, session status and resource view, process controls, and optional idle parking.
- Closure path: Chosen process stops or restarts while the workstation retains other sessions and their work.
- Why this is / is not agent-owned: Default idle parking enforces a configured policy. A model can manage owned child work but no equivalent installed fleet-wide mandate was established.
- Boundary reachability: The packaged live fleet view exposes every tracked running session and permits targeted stop from the session manager or backend.
- Whole-system current view: Running dock and session manager enumerate open and detached running sessions, with state and process-tree memory.
- Current-control decision scope: Operator can retire selected current process commitments independently of mere tab visibility and keep the other sessions running.
- Evidence: [Running views, controls and scope](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/README.md) · [Fleet sensing](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-core/src/fleet.rs) · [Scoped model intervention](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-service/src/gateway/engine/agent_tools.rs)
- Basis: structural
- Confidence: medium
- Caveats: Agent-side cross-session messaging can ask an independent session to act but does not convey the operator's fleet-wide termination authority.

## S3* — Complementary audit

- State: C
- Function: Challenge a session's change report using the actual Git changes and feed human findings back to coding work.
- Disturbance / variety regulated: A worktree may contain unintended edits, incomplete changes or discrepancies that the session transcript does not expose.
- Decisive decision or feedback right: The reviewer chooses which actual diff findings to return to the originating session.
- Decision owner: Independent human reviewer. The shipped assessment-specific path constructs access and corrective return.
- Supporting / enforcement mechanisms: Changes panel, raw Git changes, review request and path highlighting, line-anchored prompt builder, gateway reply.
- Closure path: Reviewer comments return through the waiting request or are submitted to the originating omp session for revision.
- Why this is / is not agent-owned: The agent can request review but cannot supply the independent reviewer judgment through its own completion summary.
- Boundary reachability: The shipped extension exposes request_review, which opens the gateway review path and waits for a reviewer response from the author-independent changes pane.
- Claim being audited: Whether the session's reported repository changes correspond to acceptable worktree changes.
- Ordinary reporting path: The prompted coding session reports in its transcript and status or completion reply.
- Complementary access path: The Changes panel reads Git worktree and index diffs and gives the reviewer independent line-level visibility.
- Independence boundary: The reviewer inspects Git data read by the host and composes the finding separately from the session narrative.
- Who acts on findings: The named coding session receives the review comments and can act on them in a corrective turn.
- Evidence: [Review request and response](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-service/src/gateway/engine/agent_tools.rs) · [Direct Git evidence](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-core/src/changes.rs) · [Line-anchored feedback](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-service/src/review.rs) · [Operator workflow](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/README.md)
- Basis: structural
- Confidence: medium
- Caveats: Human review is optional and a dismissed or empty review produces no corrective finding. C credits the supplied complementary evidence and return construction.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adopt a newly released installation capability while preserving access to active sessions.
- Disturbance / variety regulated: External releases can improve or alter the desktop and gateway capability.
- Decisive decision or feedback right: Choose whether to apply an eligible surfaced OmpDeck update.
- Decision owner: Installation operator.
- Supporting / enforcement mechanisms: Release fetch and comparison, matching asset, verification, update and reopen path.
- Closure path: The installed app restarts on the selected release and reattaches saved tabs.
- Why this is / is not agent-owned: The release monitor discovers options; the user decides adoption.
- Boundary reachability: Supported packaged installs expose the shipped update check and operator-triggered update and restart.
- External distinction: Externally published release metadata and assets provide the candidate version.
- Future / prospective distinction: The replacement will change subsequent operation while existing sessions can be reattached.
- Adaptation option generated: Detect a newer eligible version for the observed installation type.
- Path back into current capability / S3: The selected update replaces the installed desktop binary and restarts into the upgraded operating path.
- Evidence: [Update workflow](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/README.md) · [Release comparison and application](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-core/src/selfupdate.rs)
- Basis: structural
- Confidence: medium
- Caveats: The claim covers eligible OmpDeck package modes and does not require autonomous provider adaptation.

## S5 — Policy and identity

- State: —
- Function: Close an installation-level identity or ultimate-policy decision.
- Disturbance / variety regulated: The operator can enable different agent tools, choose providers and set scoped workspace policies.
- Decisive decision or feedback right: No path resolving an identity or ultimate-policy matter and returning it to operation was established.
- Decision owner: The operator chooses scoped tool exposure, permissions and settings.
- Supporting / enforcement mechanisms: Opt-in tool roster, approval categories, project conventions, settings and agent definitions.
- Closure path: Future session tools operate under the selected configuration and scoped approval.
- Why this is / is not agent-owned: Tool grants and workspace policies constrain ordinary operations. No credited owner resolves S3–S4 policy tensions or installation identity.
- Evidence: [Scoped tool enablement](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-core/assets/ompdeck-ctl.ts) · [Session authority dispatch](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/crates/deck-service/src/gateway/engine/agent_tools.rs) · [Settings and user modes](https://github.com/lavinhoque33/omp-deck/blob/792cbff3d8c2ab041e03dcc33c5583fba38b4694/README.md)
- Basis: structural
- Confidence: medium
- Caveats: Repository and provider governance are separate recursion levels.

### Absence scope

- Surfaces inspected: Packaged settings, gateway authority model, review/operator controls and external advisor configuration.
- Plausible first-party paths checked: Delegated session authority, project-level advisor policy and control over adoption of future capabilities.
- Why no material first-party path remains: The controls resolve workspace, capability and tool decisions separately without a shipped identity-level decision and operative return.

## Recursion

The installation contains persistent coding sessions, some in their own worktrees. The fleet is the declared recursion for current control. Parent–child handles express operating relationships; they do not alone establish another VSM recursion.

## Variety and escalation

Child attention, isolated checkout outcomes, session statuses, independent change review and upgrade notices travel through distinct channels. The receiving model, reviewer or operator decides according to the specific path.

## Evidence gaps

Live desktop, provider and relay runs were outside this pinned source review. The autonomous coordination claim is bounded to configured live-control sessions with the shipped fan-out tool available.
