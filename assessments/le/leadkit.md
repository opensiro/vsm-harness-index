---
harness_id: leadkit
project_name: Leadkit
repository: https://github.com/MattGrundy/leadkit
review_ref: 3efcde576a5f687b0013fad902fe9cff8be11766
reviewed_at: 2026-11-01
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: C(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: P
---

# Leadkit

## Review boundary

- System in focus: the adopted Leadkit operating model for a project team of Claude Code Agents, comprising shipped role definitions, persistent disk task store/queue, CLI/daemons, hooks, review gate and project owner authority profile.
- Purpose and identity: keep multi-agent coding work coherent across long-running projects with scoped task ownership, independent code review, resource awareness and human-direct permission grants.
- Relevant environment: Claude Code with Agent Teams explicitly enabled, project files/git remotes, repo owner, project teams/agents, Claude account usage telemetry and external forge rules.
- Standard-distribution boundary: the documented installed mode after leadkit init/team install and leadkit-adopt with configured profile and active Agent Teams. The Claude Code host supplies the model/tool execution engine; Leadkit ships the identities, role permissions, durable coordination/decision protocol, executable guards and reconciliation interfaces. The bare Go binary or an unwired hook alone is not a free-standing LLM agent.
- Credited operating / distribution surfaces: [internal/starter/agents/lead.md#L1-L42](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/agents/lead.md#L1-L42), [internal/starter/agents/developer.md#L1-L40](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/agents/developer.md#L1-L40), [internal/starter/agents/orchestrator.md#L1-L28](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/agents/orchestrator.md#L1-L28), [internal/starter/agents/code-review-agent.md#L1-L65](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/agents/code-review-agent.md#L1-L65), [internal/starter/agents/critique-agent.md#L1-L80](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/agents/critique-agent.md#L1-L80), [internal/starter/team-protocol.md#L1-L100](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/team-protocol.md#L1-L100), [internal/orchestrate/plan.go#L1-L130](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/orchestrate/plan.go#L1-L130), [internal/gate/chain.go#L1-L140](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/gate/chain.go#L1-L140), [docs/ADOPTING-LEADKIT.md#L1-L105](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/docs/ADOPTING-LEADKIT.md#L1-L105).
- Adjacent first-party surfaces excluded from ownership: read-only viewer, code-generation tests, contributor CI/release pipeline, unbuilt container sandbox and future design-only controls. Claude Code's proprietary model loop is external execution machinery, not evidence that the Go CLI alone implements autonomous judgment.
- First-party operating / deployment modes considered: adopted enabled Claude Code Teams with lead/developer/reviewer/orchestrator roles, on-disk role lanes and guards; human repo-owner authority grant mode; account burn monitor and optional project-level daemon; plain CLI-only mode as a negative counterfactual.
- Recursion level: one adopted project team, where named Claude Code role agents are operational S1s and the lead/orchestrator operate at their project collective level. The overarching-lead cross-project role is noted but not automatically merged into this project's internal recursion.
- Reviewed revision: 3efcde576a5f687b0013fad902fe9cff8be11766; exact source checkout.
- Observation date: 2026-11-01.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Go CLI has no model adapter or in-process agent loop. It writes Claude Code agent definitions, skills, hooks, a project profile and queue daemons. The shipped role definitions are the intentional model-bound operating program: lead decomposes/spawns/supervises, developers implement within owned paths, orchestrator watches/requeues, reviewers separately judge correctness and goal-fit, and finalise delivers after gate approval. Claude Code runs the actual model/tool sessions; Agent Teams must be enabled, else the arrangement does not operate ([README.md#L1-L75](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/README.md#L1-L75), [internal/starter/starter.go#L1-L85](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/starter.go#L1-L85), [docs/ADOPTING-LEADKIT.md#L1-L105](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/docs/ADOPTING-LEADKIT.md#L1-L105)).

The queue is a disk-backed source of task truth, with one role-keyed lane and authoritative status/owner/priority/dependencies per task. A deterministic orchestration planner computes route, requeue, capacity/hold and escalation signals from disk plus an Agent-captured live roster; an apply verb acts only on selected route/requeue steps with explicit --apply --confirm. It cannot spawn agents itself or make model-level decisions ([internal/orchestrate/plan.go#L1-L125](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/orchestrate/plan.go#L1-L125), [internal/orchestrate/apply.go#L1-L80](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/orchestrate/apply.go#L1-L80), [cmd/leadkit/cmd_orchestrate.go#L1-L110](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/cmd/leadkit/cmd_orchestrate.go#L1-L110)).

Code-review and critique model agents ask independent questions and record verdicts on an exact commit/range. The gate demands ordered layers, different role identity and a current SHA; push hooks/forge protection connect the verdicts to consequential changes. Identity claims can be caller-injected if the host does not bind them, and client hooks are bypassable if not installed, so independence is operational and role-bounded rather than cryptographic ([internal/starter/team-protocol.md#L35-L100](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/team-protocol.md#L35-L100), [internal/gate/chain.go#L1-L140](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/gate/chain.go#L1-L140), [docs/design/agent-sandboxing-and-enforcement.md#L1-L95](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/docs/design/agent-sandboxing-and-enforcement.md#L1-L95)).

The project owner directly grants standing repository authority in profile entries. Agent roles may request or escalate but may not self-grant. The same profile drives guards and PR/push checks, while forge protection can be verified server-side. Budget burn data and pause-lock hysteresis govern concurrency execution mechanically but do not themselves make a free agentic S3 decision ([docs/ADOPTING-LEADKIT.md#L35-L105](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/docs/ADOPTING-LEADKIT.md#L35-L105), [internal/burn/burn.go#L1-L110](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/burn/burn.go#L1-L110), [internal/burn/throttle.go#L1-L70](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/burn/throttle.go#L1-L70)).

## Operational model

The credited S1 choice occurs in an installed Claude Code role agent, not in Leadkit's Go functions. Lead agent coordination is autonomous in the normal enabled team mode because it allocates path owners, sequences reviewers and reacts to their returned findings, with a deterministic guard at the effect boundary. The whole-team current view/priority/budget contracts are S3-specific constructors, but no built-in autonomous agent owns all current-resource choices out of the box; a distinct repo-owner/operator mode can close priority/parallelism decisions through profiles and queue commands. Independent reviewers close S3* with bounded audit rather than verifying every external effect. Human-direct authority to grant standing repo rights forms a narrow S5 parent-governed path; ordinary merge approvals are not independently counted as constitutional governance.

## S1 — Operations

- State: A
- Function: implement project-scoped coding and verification tasks through agent-selected reading, editing, testing and tool use.
- Disturbance / variety regulated: variable code requests, test outcomes, repository content and task-specific errors.
- Decisive decision or feedback right: the installed developer/specialist Claude Code Agent decides how to perform its assigned task and reacts to tool observations and reviewer feedback.
- Decision owner: active model-driven role Agent in Claude Code Teams, configured by Leadkit's shipped first-party role definitions.
- Supporting / enforcement mechanisms: Claude Code model/tool host, installed role allowlist, task files, path guard, queue/status verbs and project profile.
- Closure path: tools return output to the active agent; it changes/tests code, records evidence and returns its result to task/reviewer queue.
- Boundary reachability: standard adoption installs the role definitions and wires hooks; the deployed Host Agent Teams directly consumes these, whereas bare leadkit CLI-only execution is explicitly not claimed to be autonomous.
- Why this is / is not agent-owned: the role agent chooses substantive code edits and validation steps; CLI/guards enforce boundaries and do not generate the operational choices.
- Evidence: [internal/starter/agents/developer.md#L1-L40](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/agents/developer.md#L1-L40); [internal/starter/agents/lead.md#L1-L42](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/agents/lead.md#L1-L42); [internal/starter/starter.go#L1-L85](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/starter.go#L1-L85); [docs/ADOPTING-LEADKIT.md#L1-L105](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/docs/ADOPTING-LEADKIT.md#L1-L105).
- Basis: explicit / structural within adopted supported mode.
- Confidence: medium-high.
- Caveats: model execution belongs to external Claude Code; no live paid Claude Code Teams E2E was performed, and disabled Teams yields no autonomous team.

## S2 — Coordination

- State: A
- Distinct S1 units: lead-assigned developer and specialist Agents working potentially overlapping git paths and successive reviews, each with its own task/owner identity.
- Inter-S1 disturbance: concurrent edits to the same path can silently undo peer work; premature parallel critique can review a SHA invalidated by prior code-review fixes; orphaned task ownership can stall delivery.
- Attenuating coordination relation: lead Agent deliberately assigns path ownership, sequences the code-review and critique sessions, returns failures to original owner, and orchestrator Agent resolves stale/idle queue handoffs. Path/queue and gate checks enforce these decisions.
- Feedback into subsequent S1 behaviour: reviewer findings change the owner's next implementation, a changed commit invalidates old approval, and queue/orphan status causes reassignment or escalation rather than duplicate work.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: these mechanisms target concrete shared-path collision, stale-SHA review race and lost-ownership hazards and return corrective outcomes to specific work units.
- Function: attenuate interference among parallel project Agents so ownership and review outcomes remain consistent.
- Disturbance / variety regulated: shared-file contention, role drift, stale review race, lost work and duplicate ownership.
- Decisive decision or feedback right: Lead chooses paths and reviewer order; the orchestrator chooses how to handle queue stalls within documented roles; deterministic planner provides constraints and signals.
- Decision owner: model-driven Lead/Orchestrator Agents in the shipped enabled-team operating mode, not the Go planner or filesystem alone.
- Supporting / enforcement mechanisms: ownership guard, role lanes, task IDs, deterministic plan, reviewer chain SHA binding and distinct identities.
- Closure path: owner assignment enters task store/queue, agents act within scoped paths, review findings return to builder, and next verified SHA advances review/ship stages.
- Boundary reachability: these roles and paths are installed through the public adoption workflow and use active Claude Code Teams Agent/SendMessage capabilities, not only project maintainer dogfood.
- Why this is / is not agent-owned: the meaningful assignment and remediation selection belongs to autonomous role Agents; guards deny inconsistent actions but do not choose the route.
- Evidence: [internal/starter/agents/lead.md#L1-L42](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/agents/lead.md#L1-L42); [internal/starter/agents/orchestrator.md#L1-L28](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/agents/orchestrator.md#L1-L28); [internal/starter/team-protocol.md#L1-L100](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/team-protocol.md#L1-L100); [internal/orchestrate/plan.go#L1-L130](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/orchestrate/plan.go#L1-L130); [internal/gate/chain.go#L65-L140](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/gate/chain.go#L65-L140).
- Basis: explicit / structural.
- Confidence: medium-high for standard deployed role protocol.
- Caveats: coordination relies on following first-party role instructions; the Go CLI does not itself launch or monitor a proprietary model session.

## S3 — Inside-and-now control

- State: C(P)
- Whole-system current view: project queue/status/owner/priority/dependency records plus live roster passed in from Agent Teams; account burn telemetry, workstream count, budget reserve and pause-lock status.
- Current-control decision scope: choose active team workload and concurrency, defer dispatch when budget is stressed, prioritize critical tasks, requeue orphaned work or grant owner-directed staffing/priority changes.
- Function: maintain present project-team commitments, workload and throughput within user resource and authority bounds.
- Disturbance / variety regulated: misallocated role capacity, budget burn, stuck tasks and competing current priorities.
- Decisive decision or feedback right: first-party planner exposes S3-specific route/requeue/hold/triage choices, while the installed autonomous actor must assemble a live roster and act on higher-level capacity/priority reports; in the parent mode the human selects the active roster/priority/parallelism and authorizes changes.
- Decision owner: C constructor has deterministic CLI and Agent-facing role protocol but lacks a self-contained autonomous S3 governor with all decisive rights; P mode is the legitimate project operator who decides and applies current resource/priority constraints.
- Supporting / enforcement mechanisms: leadkit status, burn/priority planner, usage history, account pause lock, role roster, task queue, apply confirmation, waker/sweep daemons.
- Closure path: computed route/hold/escalation is returned to orchestrator or human; accepted priority/roster/budget decisions alter task status or available consumers, and subsequent queue/burn samples expose the result.
- Boundary reachability: CLI+roles+hooks/daemons are standard installed interfaces, including explicit owner changes, not private governance; C still needs external Agent Teams and operator adoption, P needs actual human choice.
- Why this is / is not agent-owned: consuming a deterministic burn verdict and routing plan does not by itself make the autonomous Lead own a whole-system capacity tradeoff. Parent control is a distinct explicit operating mode rather than a decoration on an approval button.
- Evidence: [internal/orchestrate/plan.go#L1-L130](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/orchestrate/plan.go#L1-L130); [internal/orchestrate/apply.go#L1-L80](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/orchestrate/apply.go#L1-L80); [cmd/leadkit/cmd_orchestrate.go#L1-L110](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/cmd/leadkit/cmd_orchestrate.go#L1-L110); [internal/burn/burn.go#L1-L115](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/burn/burn.go#L1-L115); [internal/burn/throttle.go#L1-L70](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/burn/throttle.go#L1-L70); [docs/ADOPTING-LEADKIT.md#L20-L105](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/docs/ADOPTING-LEADKIT.md#L20-L105).
- Basis: explicit / structural.
- Confidence: medium; project-specific actual authorization and agent roster are deployment-specific.
- Caveats: automatic pause/resume is deterministic enforcement; the C notation is restricted to S3-specific live-resource decision paths, not arbitrary queue commands. Parent mode presumes a real operator uses reports to revise priority/roster rather than merely installing a static config.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`C`) | S3-specific deterministic plan and installed Agent-role construction path; developer supplies ultimate autonomous governor | Queue/roster/burn changes | Route/requeue/hold signals and guarded apply affect later dispatch, but fully agent-owned discretion is not supplied | [internal/orchestrate/plan.go#L1-L130](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/orchestrate/plan.go#L1-L130) |
| Parent (`P`) | Human operator chooses active roster, priority and burn limits | Work/status/budget report | Profile/queue settings and subsequent waker/plan ticks change live workload | [docs/ADOPTING-LEADKIT.md#L20-L105](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/docs/ADOPTING-LEADKIT.md#L20-L105) |

## S3* — Complementary audit

- State: A
- Claim being audited: a code diff at a pinned SHA is correct/safe and actually serves the ticket's intended goal.
- Ordinary reporting path: builder Agent's completion claim, code changes and test logs.
- Complementary access path: separate read-only code-review and critique Agents inspect diff, task and surrounding code under different questions and record own SHA-bound verdicts/evidence.
- Independence boundary: distinct installed roles/tools (reviewers lack Edit/Write/SendMessage), order and different-role gate checks; reviewers are not the builder and may not file the other layer's verdict.
- Who acts on findings: original builder/lead receives changes-needed; gate blocks push/PR path until matching independent ready layers, then finalise/human may proceed.
- Function: complementary audit of operational output and purpose before a consequential code shipment.
- Disturbance / variety regulated: self-certified implementation errors, wrong goal, stale-SHA approval, and review-role collusion/impersonation accidents.
- Decisive decision or feedback right: separate model-driven reviewer Agents make substantive correctness and goal-fit judgments, each recorded on observed commit evidence.
- Decision owner: reviewer Agents own their respective judgments, while Go gate and forge enforcement decide only whether required current, role-separated records exist.
- Supporting / enforcement mechanisms: reviewer read-only grants, mutation-evidence notes, chain/order, SHA stamps, status/queue, push hooks and optional verified server protection.
- Closure path: changes-needed returns work to developer, revised SHA invalidates old approvals, both ready verdicts permit finalise/push within granted authority.
- Boundary reachability: reviewer roles and gate are shipped/installable first-party components in the normal team setup, not merely CI tests; the external Claude Code host executes reviewers.
- Why this is / is not agent-owned: semantic findings belong to independent review Agents; checking SHA/order/identity and command gating is deterministic enforcement.
- Evidence: [internal/starter/agents/code-review-agent.md#L1-L65](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/agents/code-review-agent.md#L1-L65); [internal/starter/agents/critique-agent.md#L1-L85](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/agents/critique-agent.md#L1-L85); [internal/gate/chain.go#L1-L140](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/gate/chain.go#L1-L140); [internal/starter/team-protocol.md#L35-L100](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/team-protocol.md#L35-L100); [cmd/leadkit/cmd_gate.go#L1-L95](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/cmd/leadkit/cmd_gate.go#L1-L95).
- Basis: explicit / structural.
- Confidence: medium-high for first-party role separation and gate.
- Caveats: recorded --by identity may be self-asserted when host does not bind CLAUDE_AGENT_NAME; local hooks are bypassable without forge protection. Multiple reviewers may share provider/model family; independence is role/evidence separation, not externally certified audit.

## S4 — Outside-and-then intelligence

- State: —
- Function: no evidenced external-future sensing, adaptation-option judgment and return into current project capability at the assessed boundary.
- Disturbance / variety regulated: emerging technology/organizational threats or future opportunities are not a first-party recurrent object of control.
- Decisive decision or feedback right: no first-party S4 actor chooses strategic redesign from external signals and deploys it.
- Decision owner: not established; humans may modify roles or open issues; normal Lead coordination operates on present tasks.
- Supporting / enforcement mechanisms: feedback-as-issues in overarching-lead protocol, role capture, postmortems, repo governance and backlog.
- Closure path: issues preserve potential improvements but no closed strategic adoption loop into team capabilities is wired.
- Why this is / is not agent-owned: planning future tasks and capturing lessons is not necessarily outside-and-then adaptation.
- Evidence: [internal/starter/agents/overarching-lead.md#L1-L110](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/agents/overarching-lead.md#L1-L110); [internal/starter/starter.go#L1-L100](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/starter.go#L1-L100); [README.md#L75-L145](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/README.md#L75-L145).
- Basis: structural bounded absence.
- Confidence: medium-high.
- Caveats: the user can commission tool upgrades; they remain discretionary external work, not a shipped S4 mode.
### Absence scope

- Surfaces inspected: overarching-lead protocol, queue/feedback, team role templates, burn monitoring, publishing and configuration.
- Plausible first-party paths checked: feedback capture to issues, role-definition versioning, strategic decisions to changed team capability.
- Why no material first-party path remains: no first-party mechanism senses prospective external distinctions, weighs adaptation options and returns an adopted strategic choice to current execution.

## S5 — Policy and identity

- State: P
- Identity / ultimate-policy issue: whether a project team may grant itself standing rights to push, create PRs, merge or modify protected repository policy, versus retaining those fundamental authorization rights at the repository owner.
- Ultimate authority in each claimed mode: direct project/repository owner alone; peer lead and overarching coordinator cannot grant or relay authority in lieu of the owner.
- Return-to-operation path: owner-approved authority.<repo> entry in the project profile changes guards and governed PR/push commands; protected-branch rules can be installed and read back, and subsequent operations are permitted/blocked by the returned grant.
- Function: reserve ultimate scope of consequential agent action to direct human owner authority and apply it as a durable team constitution.
- Disturbance / variety regulated: agent self-grant, laundering authority through a peer coordinator, unreviewed merges/pushes and inconsistent rights across repositories.
- Decisive decision or feedback right: grant or deny standing repository mutation/merge authority, and amend protected-branch policy under owner mandate.
- Decision owner: legitimate human project/repository owner in the shipped parent-governed setup, not the autonomous Lead or other session.
- Supporting / enforcement mechanisms: per-repo authority profile, adoption stop point, PR/push guard, default-deny allowlists, forge protection verification and doctor.
- Closure path: team must request direct owner grant; owner decision is written to profile/forge policy; subsequent hook/CLI operations consume it, permit only granted action and report denials. Denial leaves default-deny intact.
- Boundary reachability: authority-grant step and policy guards are part of normal adoption flow and CLI; code explicitly reads named per-repo authority, so the mode is real without relying on GitHub contributors as a metasystem.
- Why this is / is not agent-owned: agents cannot legitimately establish their own standing constitutional authority merely by relaying a request; the owner remains the sole source of grants, while Go enforces the returned decision.
- Evidence: [docs/ADOPTING-LEADKIT.md#L20-L105](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/docs/ADOPTING-LEADKIT.md#L20-L105); [internal/starter/agents/overarching-lead.md#L1-L110](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/internal/starter/agents/overarching-lead.md#L1-L110); [README.md#L75-L145](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/README.md#L75-L145); [docs/design/agent-sandboxing-and-enforcement.md#L1-L95](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/docs/design/agent-sandboxing-and-enforcement.md#L1-L95); [cmd/leadkit/cmd_gate.go#L1-L95](https://github.com/MattGrundy/leadkit/blob/3efcde576a5f687b0013fad902fe9cff8be11766/cmd/leadkit/cmd_gate.go#L1-L95).
- Basis: explicit / structural parent-governed closure.
- Confidence: medium-high for first-party policy path, not for an unseen specific live owner decision.
- Caveats: ordinary per-PR human review is not counted as S5; standing authority is the constitutional object. Client-side hooks alone are bypassable; host/forge enforcement and real owner-supplied profile must be configured.

## Distributed OSS parent arrangement

Public Leadkit contributors are not assumed to govern any adopter's live team. The legitimate parent in S3/S5 modes is the project's own human operator/repo owner, with per-repo direct grants; a cross-project overarching-lead is a coordination role and explicitly not an authority issuer.

## Self-hosted and non-human modes

Leadkit is self-hosted as a Go CLI and Claude Code Teams configuration; it has no standalone model provider or LLM API loop. The S1/S2/S3* autonomies require the supported external Claude Code runtime with first-party installed roles, not merely running leadkit doctor. The parent-governed S3/S5 modes require actual operator choices and configured authority records. Disabling Teams or omitting hooks is materially different and does not inherit the positive claims.

## Recursion

A project Lead and agents form one bounded coding-team collective. Optional overarching-lead coordinates multiple project Leads but does not automatically create an independently evidenced higher parent S3/S4/S5 in any private deployment. Agent spawning is a role implementation mechanism, not sufficient evidence of VSM recursion without the team ownership/feedback relations traced here.

## Variety and escalation

Model Agents react to task/test/review variety; queue and ownership guard prevent conflict; burn/lock reacts to usage; policy requests escalate human-direct. Tool denials, ordinary tasks stuck in a queue and status dashboards are not by themselves algedonic whole-system exceptional signals. The system's enforcement paths should not be mistaken for independent human/agent discretion.

## Evidence gaps

No live Claude Code model/team E2E was run. Deployed leadkit requires explicit CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1, correct agent installation and owner config; negative outcomes of incomplete adoption are not hidden. S3 C(P) is intentionally bounded because deterministic burn/route plan does not establish an autonomous whole-system controller; reviewer independent identity is best-effort under a self-asserted role variable, not cryptographic proof.
