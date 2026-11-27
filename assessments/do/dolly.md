---
harness_id: dolly
project_name: Dolly
repository: https://github.com/rozenmd/dolly
review_ref: d77ef9ff2eca1aa379ed3260eaf52a164be05d4d
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# Dolly

## Review boundary

- System in focus: The self-hosted Dolly Cloudflare deployment with owner web sessions, delegated children, a standing chief session, and optional pull request review.
- Purpose and identity: Conduct background coding work, report evidence and prepare pull requests for the owner.
- Relevant environment: Configured Cloudflare Workers, a model account, authorized GitHub workspaces and optional Slack or external MCP services.
- Standard-distribution boundary: Dolly's Worker, browser interface, durable session assembly, repository sandbox, coordination and automation code. Pi Durable supplies reusable runtime machinery.
- Credited operating / distribution surfaces: Dolly session and tool wiring, chief, child task routing, PR review handoff, and owner-gated connection registration.
- Adjacent first-party surfaces excluded from ownership: External provider internals, Cloudflare platform administration, external GitHub authority and model evaluation.
- First-party operating / deployment modes considered: Owner web work, delegated children, chief, optional GitHub intake and automatic read-only PR review; external integrations retain their authority boundaries.
- Recursion level: One owner-operated instance and its portfolio of active sessions and checkouts.
- Reviewed revision: d77ef9ff2eca1aa379ed3260eaf52a164be05d4d
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The Worker assembles a durable agent runtime with first-party repository and coordination tools. Sessions keep working after clients disconnect and answered turns checkpoint repository sandboxes. A standing chief sees the session portfolio and can spawn, redirect, or wait on children. Optional GitHub review launches separate pinned read-only sessions, whose verdict can restart bounded repair on the producing session.

## Operational model

A model uses Dolly's shipped workspace capabilities to inspect or change a checkout and respond. Child models own task briefs. The chief chooses how to partition and direct current commitments. Separate review agents obtain evidence directly from the pinned PR revision and return findings to the coding work.

## S1 — Operations

- State: A
- Function: Complete coding work or investigation asynchronously in a delegated or owner session.
- Disturbance / variety regulated: Changing objectives, tool errors, model backend failure and checkout state.
- Decisive decision or feedback right: Choose workspace operations, observe results, and decide the next action or final response.
- Decision owner: The provider-backed session model in the bundled Dolly product.
- Supporting / enforcement mechanisms: Pi Durable for loop and durable task mechanics, Dolly tools and workspace isolation, end-of-run checkpoints and optional model fallback.
- Closure path: First-party tool results flow into generation. Completed answers persist and trigger workspace checkpoints, and a failed child can report back to its parent.
- Boundary reachability: The shipped Worker opens the runtime with Dolly's installed extension, registry and tools. Operators configure a model account, without composing their own agent.
- Why this is / is not agent-owned: Pi Durable and the tools execute and persist decisions. The configured model closes what work to perform and how to respond.
- Evidence: [src/agent.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/agent.ts#L1120-L1144), [src/agent.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/agent.ts#L1174-L1215), [src/agent.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/agent.ts#L1280-L1314), [README.md](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/README.md#L5-L19)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Opening or preparing a PR can be part of the task. Default-branch merge authority is external.

## S2 — Coordination

- State: A
- Function: Coordinate independent working sessions so they do not accidentally take over the same checkout or duplicate a commitment.
- Disturbance / variety regulated: Separate agents can change overlapping files or start duplicate tasks on work already owned by another branch or session.
- Decisive decision or feedback right: Choose shared versus isolated checkout and route new information to the session that already owns work.
- Decision owner: The chief or authorized parent model exercising task coordination tools.
- Supporting / enforcement mechanisms: Session inventory, child IDs, optional isolated branch allocation and bounded reports with runtime evidence.
- Closure path: The model assigns scopes or steers an existing owner. Child status, failure or completion returns by wait or report, and can lead to adjusted assignment.
- Boundary reachability: The deployed chief prompt and the default coordination extension wire status, task creation, messaging and reports.
- Why this is / is not agent-owned: The checkout machinery enforces selected isolation. The model decides whether to share, isolate or reuse a particular task owner.
- Distinct S1 units: Separate worker sessions with task-specific briefs, active model turns, and distinct or shared checkout state.
- Inter-S1 disturbance: Duplicate work and overlapping mutation of a shared checkout by independently acting units.
- Attenuating coordination relation: Allocate a distinct branch where appropriate and redirect follow-up to the existing session owner.
- Feedback into subsequent S1 behaviour: Live status, wake and outcome reporting feed the next decision about which agent continues and where it works.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: It mediates a specific conflict over task ownership and branch state. Launching separate sessions alone does not settle the conflict.
- Evidence: [src/chief.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/chief.ts#L48-L59), [src/coordination.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/coordination.ts#L979-L1026), [src/coordination.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/coordination.ts#L1121-L1190), [src/child-report-message.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/child-report-message.ts#L30-L52)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Shared checkout is supported, so isolation depends on the chosen operating mode.

## S3 — Inside-and-now control

- State: A
- Function: Manage the current portfolio of commitments, including delegated work that needs redirection or cancellation.
- Disturbance / variety regulated: Multiple ongoing sessions can stall, hold a commitment, or continue work that needs to be redirected.
- Decisive decision or feedback right: Choose whether to assign, steer, wait, or cancel a particular live commitment.
- Decision owner: The standing chief model and model parents over their own children.
- Supporting / enforcement mechanisms: Current state and parent/PR metadata, limits, task lineage and cancellation enforcement.
- Closure path: Tool actions update live responsibility or abort a selected child and its descendants. Status and reports allow the model to reconcile the resulting portfolio.
- Boundary reachability: The first-party standing chief identity is wired to the session repository and task controls. Parent models can manage their own spawned children.
- Why this is / is not agent-owned: Limits and abort execute policy mechanically. A model chooses the specific operational commitment to intervene in.
- Whole-system current view: Portfolio status and session summaries, including running state, task links and PR ownership, with child-level evidence.
- Current-control decision scope: Assigning, steering, stopping or continuing live commitments. Cancellation is scoped to the model's own children.
- Evidence: [src/chief.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/chief.ts#L4-L16), [src/chief.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/chief.ts#L48-L59), [src/agent.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/agent.ts#L1247-L1253), [src/coordination.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/coordination.ts#L874-L914), [src/self-query.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/self-query.ts#L331-L348)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: The deployed owner retains direct intervention rights over arbitrary sessions. The model path shown here concerns delegated control.

## S3* — Complementary audit

- State: A
- Function: Audit whether a working session's pull request is ready by examining its actual change set independently.
- Disturbance / variety regulated: An author may claim readiness although its implementation misses stated requirements or introduces defects.
- Decisive decision or feedback right: Adjudicate evidence from the pinned diff and files, then publish a verdict and actionable findings.
- Decision owner: The separate automatic review model in the read-only session.
- Supporting / enforcement mechanisms: Event intake, independent checkout, read-only role scope, stale-head protection and durable routing.
- Closure path: Current-head review feedback is queued to the originating session, which may repair and push under a bounded loop. Further pushes get a fresh review.
- Boundary reachability: The installed optional PR-review automation configures a distinct review session and returns qualifying findings to the originating work.
- Why this is / is not agent-owned: The reviewer determines the findings and verdict using direct access to the revision, while intake and handoff enforce eligibility and return.
- Claim being audited: The coding session's claim that its pull request is ready for owner acceptance.
- Ordinary reporting path: The working session's PR description, status and readiness summary.
- Complementary access path: A fresh read-only reviewer inspects the actual PR diff and checkout at the current event commit.
- Independence boundary: Separate session and pinned source. The reviewer may consult the PR description and conversation but does not depend on them for evidence.
- Who acts on findings: The original coding session receives the distinct review finding and can repair and submit a new revision.
- Evidence: [docs/setup.md](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/docs/setup.md#L150-L166), [src/github-inbox.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/github-inbox.ts#L140-L180), [src/github-inbox.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/github-inbox.ts#L475-L518), [src/github-inbox.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/github-inbox.ts#L589-L635), [src/review-handoff.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/review-handoff.ts#L360-L382)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: The automatic audit must be configured and the return path is bounded to qualifying Dolly-owned work.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adopt an external operational capability for later owner sessions when work requires a new service integration.
- Disturbance / variety regulated: A needed service remains outside the available tool repertoire until the owner selects a new endpoint and grants access.
- Decisive decision or feedback right: Choose the specific external service to adopt and, when needed, complete its authorization.
- Decision owner: The legitimate deployment owner. The model assists in filling the connection registry.
- Supporting / enforcement mechanisms: Authorization context, owner-authored endpoint gate, connection state, optional owner sign-in and subsequent MCP discovery.
- Closure path: The owner supplies the selected endpoint directly in an eligible turn or Settings. After installation and any owner sign-in, future eligible turns discover the new operational tools.
- Boundary reachability: The standard owner web session and Connections settings wire service selection, authorization and reuse. An automation or review turn cannot acquire that authority.
- Why this is / is not agent-owned: A model cannot pick an endpoint from tool output and adopt it. The evidence supports parent-owned attachment and a runtime return path.
- External distinction: An external MCP service whose tools can expand the work the deployment can perform.
- Future / prospective distinction: A capability requirement for later sessions, with integration chosen by the owner.
- Adaptation option generated: Register and if needed authorize a new remote tool source.
- Path back into current capability / S3: The persistent connection is loaded into qualifying next-turn tool discovery.
- Evidence: [src/connections-tool.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/connections-tool.ts#L4-L32), [src/connections-tool.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/connections-tool.ts#L34-L45), [src/connections-tool.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/connections-tool.ts#L59-L79), [src/agent.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/agent.ts#L3655-L3666), [src/agent.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/agent.ts#L1258-L1275)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Limited to the supported owner-directed adoption loop. Provider failover handles current resource disruption and is distinct.

## S5 — Policy and identity

- State: —
- Function: No distinct ultimate-policy or identity adjudication loop was established.
- Disturbance / variety regulated: The owner can choose which users, repositories or integrations participate and can change review instructions.
- Decisive decision or feedback right: No distinct decision right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Initial owner assignment, instance access rules, review recipe and role-scoped mechanisms.
- Closure path: Settings are enforced on subsequent sessions within the fixed governance model.
- Why this is / is not agent-owned: The inspected boundary has a fixed owner and fixed authority classes. Changes to repository scope, tool permissions or review criteria apply that policy rather than resolving a new ultimate authority or mission.
- Evidence: [README.md](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/README.md#L27-L35), [README.md](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/README.md#L59-L63), [docs/setup.md](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/docs/setup.md#L150-L166), [src/agent.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/agent.ts#L962-L988), [src/chief.ts](https://github.com/rozenmd/dolly/blob/d77ef9ff2eca1aa379ed3260eaf52a164be05d4d/src/chief.ts#L4-L16)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: External GitHub organization and branch policy is outside the deployment boundary.

### Absence scope

- Surfaces inspected: Owner access, allowed actions and restriction of automation, child, review and web contexts.
- Plausible first-party paths checked: A supported loop that resolves an organizational identity or ultimate authority dispute and returns the settlement.
- Why no material first-party path remains: Observed permissions and workflow settings operate inside the declared one-owner model. A named chief is an assigned role with a configurable display name.

## Recursion

The owner-operated Dolly instance is the focal recursion. Coding, delegation and review sessions are subunits. GitHub and hosted model providers are environmental actors.

## Variety and escalation

Turn state, reports, read-only gates, bounded review cycles and cancellation attenuate runtime variety. A model provider error may trigger configured fallback or a report to the parent.

## Evidence gaps

This assessment uses pinned product source and deployment documentation. No provider-backed sessions, external PR actions, or deployed trials were executed.
