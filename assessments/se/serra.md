---
harness_id: serra
project_name: Serra
repository: https://github.com/isacssw/serra
review_ref: fb356389548b8691685a552c527b4a3ef19091d5
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: P
---

# Serra

## Review boundary

- System in focus: A local Serra profile with its shipped daemon, macOS owner app and configured T3 or supported ACP worker.
- Purpose and identity: Turn approved chat and app requests into delegated work, return results, and maintain the profile knowledge used in future jobs.
- Relevant environment: Slack thread audiences, local Git repositories and a signed-in agent runtime. Knowledge evidence includes owner responses and work conversations.
- Standard-distribution boundary: The bot's intake, job lifecycle, worktree and agent adapters, brief/knowledge services and owner interfaces.
- Credited operating / distribution surfaces: Configured Slack and app work, first-party knowledge interview and weekly review, approved-policy management.
- Adjacent first-party surfaces excluded from ownership: Unrelated sessions opened directly in T3 or an ACP client, provider policy, development evaluation and external GitHub authority.
- First-party operating / deployment modes considered: Slack job and follow-up, app job, T3 and supported ACP, periodic knowledge review and owner interview.
- Recursion level: One configured local bot profile, with its worktree jobs as operational units.
- Reviewed revision: fb356389548b8691685a552c527b4a3ef19091d5
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

Serra renders a job-specific brief, prepares worktree scope, starts a supported worker, tracks the run and returns its result to the originating thread. Its ACP client constructs the session, forwards prompt turns, receives updates and queues follow-ups. The first-party knowledge flow has separate permitted snapshots, proposals, review and approval. An owner-controlled policy file governs subsequent jobs.

## Operational model

The configured worker decides how to investigate a request or change its workspace in the supported job. Serra assigns the task scope and routes the result. For advice about the profile itself, Serra starts a separate interview or knowledge-review role with purpose-specific instructions. The owner can decide which evidence, policies and knowledge enter subsequent work.

## S1 — Operations

- State: A
- Function: Carry out a project task and return a workspace artifact or supported response to the initiating job.
- Disturbance / variety regulated: Changing chat requests, repository state, tool results and follow-up inputs.
- Decisive decision or feedback right: Choose task actions within the brief and workspace, respond to feedback and produce work and a result.
- Decision owner: The configured T3 or ACP model-backed Serra job worker.
- Supporting / enforcement mechanisms: Audience-filtered brief, agent adapter, job-specific workspace, run tracking and reply delivery.
- Closure path: Serra briefs and starts the model worker, follows the result, and can return follow-up information into the same job. The model's chosen actions produce the artifacts and reply.
- Boundary reachability: Supported default/optional agent backends are deliberately integrated into the packaged job lifecycle. The owner supplies the backend and sign-in while Serra supplies the operational setup, dispatch and return.
- Why this is / is not agent-owned: If the backend worker is removed, the first-party transport can still observe or relay but no one decides what work to carry out. Ownership belongs to the active worker as bound into the supplied Serra job.
- Evidence: [README.md](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/README.md#L21-L36), [src/bot.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/bot.ts#L342-L385), [src/agent/acp.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/agent/acp.ts#L628-L657), [src/bot.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/bot.ts#L987-L1000)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: No claim is made about arbitrary external coding sessions or the autonomous internals of every ACP provider.

## S2 — Coordination

- State: C
- Function: Regulate direct write interference between jobs against the same repository.
- Disturbance / variety regulated: Overlapping agent edits and checkout changes can interfere if independent jobs share a working tree.
- Decisive decision or feedback right: Decide or revise job workspace isolation in response to concurrent work.
- Decision owner: Serra supplies job-specific branch/worktree isolation. An autonomous coordination decision owner would require composition.
- Supporting / enforcement mechanisms: Git worktrees and distinct per-job branches, with first-party creation or T3 workspace assembly.
- Closure path: Each agent executes in the allocated branch/worktree, limiting collisions at the working-copy level.
- Boundary reachability: The ordinary worktree job route passes workspace identity at launch. Serra makes ACP worktrees for the applicable mode and requests T3 worktrees through its backend.
- Why this is / is not agent-owned: The allocation rule is predefined. The isolated workers own task actions, not arbitration of competing workspace commitments.
- Distinct S1 units: Separate job-bound worker agents using the same underlying project repository.
- Inter-S1 disturbance: Concurrent jobs could edit the same files and checkout state when run in a single project directory.
- Attenuating coordination relation: One branch and working tree per job in the standard worktree-backed mode.
- Feedback into subsequent S1 behaviour: The workspace boundary directs subsequent file actions to the isolated checkout.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Distinct Git working directories specifically attenuate direct cross-job write interference.
- Evidence: [README.md](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/README.md#L21-L28), [src/agent/worktree.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/agent/worktree.ts#L1-L18), [src/agent/acp.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/agent/acp.ts#L628-L644)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: Folder-bound ACP agents use their own folder, and worktree separation does not settle conflicts at integration.

## S3 — Inside-and-now control

- State: P
- Function: Regulate currently active jobs after the owner restricts knowledge available to their audience.
- Disturbance / variety regulated: An existing job may retain evidence whose allowed audience or approval changes while that job is active.
- Decisive decision or feedback right: Decide to restrict or retire the in-force knowledge across affected jobs.
- Decision owner: Local profile owner through the approved knowledge and audience controls.
- Supporting / enforcement mechanisms: Current job list, audience checks against knowledge snapshots, held replies and rebriefing in a new worker.
- Closure path: Owner retirement or narrowed scope changes the approved knowledge. The active-delivery gate can withhold affected replies and the next turn starts a worker with the revised brief and retained task branch.
- Boundary reachability: The owner app exposes jobs and page controls, and the active daemon consults the resulting profile for its live current governance checks.
- Why this is / is not agent-owned: The owner decides the shared information constraint. The daemon enforces the returned decision and no autonomous actor owns revocation.
- Whole-system current view: The owner-facing Jobs state tracks running and blocked work across the profile. The runtime checks active job audience and which approval snapshot it received.
- Current-control decision scope: Change in-force constraints on current worker evidence, affecting existing runs with formerly allowed knowledge.
- Evidence: [src/jobs.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/jobs.ts#L169-L218), [app/main/ipc/proposals.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/app/main/ipc/proposals.ts#L40-L63), [src/bot.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/bot.ts#L505-L520), [src/bot.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/bot.ts#L911-L933), [src/bot.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/bot.ts#L944-L970)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: The finding is limited to current knowledge constraints that trigger intervention. Routine card approvals or deterministic backend selection alone do not establish S3.

## S3* — Complementary audit

- State: A
- Function: Sample whether the knowledge used by jobs actually supports answers, and surface conflicting or stale rules to the profile owner.
- Disturbance / variety regulated: Ordinary worker citation and completeness reports can overstate the value or current validity of a page.
- Decisive decision or feedback right: Judge contradictory or unsupported guidance and propose corrective evidence from a separate review role.
- Decision owner: The read-only model reviewer in the supported weekly flow, with owner authority over applying changes.
- Supporting / enforcement mechanisms: Periodic scheduler, approved snapshot reader, journal of request/reply/page usage, controlled re-answer comparisons and proposal validation.
- Closure path: The model receives historical material and page texts, writes a review or rewrite proposal, and the owner can accept actionable findings into the profile that governs later work.
- Boundary reachability: The live daemon schedules the first-party weekly review and supplies a configured read-only model run.
- Why this is / is not agent-owned: The reviewer makes fresh, task-independent judgments over evidence. Owner approval governs the response to the findings.
- Claim being audited: The pages cited and carried in real worker answers are current, useful and internally consistent.
- Ordinary reporting path: Worker replies, knowledge use/citation and per-job status.
- Complementary access path: Read the approved pages independently, inspect actual sampled requests/replies, and compare re-answers with and without a cited page.
- Independence boundary: Separate review turns have their own supplied context and no need for a different provider. The evidence is bounded to the stored samples and pages.
- Who acts on findings: The owner sees the digest and may accept corrective knowledge proposals or retire pages.
- Evidence: [src/daemon.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/daemon.ts#L368-L380), [src/knowledge-review.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/knowledge-review.ts#L129-L154), [src/knowledge-review.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/knowledge-review.ts#L204-L220), [src/knowledge-review.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/knowledge-review.ts#L253-L283), [app/main/ipc/proposals.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/app/main/ipc/proposals.ts#L38-L63)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: This audit concerns the knowledge-to-reply function. A PR review request is a separate external handoff.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adapt the profile's future job knowledge to changes in external project and user practices.
- Disturbance / variety regulated: New human decisions, changed project context and repeated unanswered questions can make the current knowledge obsolete.
- Decisive decision or feedback right: Decide which new or revised facts and procedures become approved future capability.
- Decision owner: The profile owner reviewing proposed additions, rewrites, merges and retirements.
- Supporting / enforcement mechanisms: Interview, weekly knowledge review, provenance, approval UI and audience-filtered brief assembly.
- Closure path: New evidence is turned into a concrete proposal. Owner accept/merge decides its applicability, and subsequent worker briefs consume the approved copy.
- Boundary reachability: The supplied app and daemon implement proposal construction, human acceptance and reads from approved knowledge.
- Why this is / is not agent-owned: Model workflows produce candidate changes. The owner controls whether they enter subsequent operation.
- External distinction: New owner information, changing working practices and project evidence surfaced by actual chat or review.
- Future / prospective distinction: Determine what later jobs need to know across requests.
- Adaptation option generated: New or revised knowledge page, with scope and recorded decision source.
- Path back into current capability / S3: Promoted or merged pages feed the approved snapshot and hence subsequent job briefs.
- Evidence: [README.md](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/README.md#L123-L133), [templates/interview.md](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/templates/interview.md#L38-L49), [src/knowledge-review.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/knowledge-review.ts#L204-L220), [app/main/ipc/proposals.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/app/main/ipc/proposals.ts#L38-L63), [src/brief.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/brief.ts#L56-L86)
- Basis: Structural evidence from pinned first-party source.
- Confidence: high
- Caveats: The evidence concerns reusable knowledge and working procedures rather than automatic policy escalation.

## S5 — Policy and identity

- State: P
- Function: Define the installed engineering assistant's persistent operating mandate and authority limits.
- Disturbance / variety regulated: Different people and requests can conflict about who may decide, what the assistant represents, and off-limits work.
- Decisive decision or feedback right: Set what the bot may do independently, who has permission to authorize work and which subjects are outside its mandate.
- Decision owner: Legitimate local profile owner.
- Supporting / enforcement mechanisms: First-party mandate interview, owner preview and apply, persistent policy and repeat brief assembly.
- Closure path: The interview explicitly returns unresolved policy matters for owner decision. The owner can save or apply reviewed policy wording, and workers read it in later jobs.
- Boundary reachability: The app exposes the interview and the policy service, and the default brief supplies the active policy reference to each worker.
- Why this is / is not agent-owned: The model elicits matters and proposes wording. Only the owner can set the enduring mandate and grant a wider permission where allowed.
- Identity / ultimate-policy issue: Which tasks the assistant is authorized to take, what it may disclose or promise, and who may widen its permission.
- Ultimate authority in each claimed mode: The owner who defines and operates the profile. The interview cannot widen its own brief.
- Return-to-operation path: Owner decides and saves or applies policy. The supplied brief makes that policy operative for later jobs, with widening reserved to explicit owner authority.
- Evidence: [templates/interview.md](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/templates/interview.md#L17-L30), [templates/interview.md](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/templates/interview.md#L47-L51), [templates/brief.md](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/templates/brief.md#L79-L95), [src/brief.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/brief.ts#L185-L189), [src/brief.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/src/brief.ts#L241-L262), [app/main/ipc/brief.ts](https://github.com/isacssw/serra/blob/fb356389548b8691685a552c527b4a3ef19091d5/app/main/ipc/brief.ts#L26-L45)
- Basis: Structural evidence from pinned first-party source.
- Confidence: medium
- Caveats: The finding is limited to the mandate and enduring authority limits. Ordinary workflow preferences are not treated as S5.

## Recursion

The installed owner profile coordinates multiple jobs. A worktree task executes inside one worker's own context. The sealed policy, knowledge decisions and weekly review apply at the profile boundary.

## Variety and escalation

Per-job worktrees, approved knowledge views and explicit response routing attenuate interference and varying audience constraints. Backend failure or access questions can return to the operator through supported job and chat surfaces.

## Evidence gaps

Static evidence from the pinned distribution. No Slack, T3, ACP, provider sessions or GitHub jobs were executed. The user and backend may choose configurations with fewer of the documented paths.
