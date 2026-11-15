---
harness_id: mu
project_name: mu
repository: https://github.com/qybaihe/mu
review_ref: ba0aeb2d2a6f6caa5809f7bb314642827bc11a96
reviewed_at: 2026-11-15
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: P
---

# mu

## Review boundary

- System in focus: One local mu coding-agent session or goal, with its shipped decision kernel and any first-party hive/worker sessions spawned to serve it.
- Purpose and identity: Deliver an operator-defined coding or investigative result, with optional multiple workers and reviewable limits on delegated actions.
- Relevant environment: Task owner and workspace, files and version-control state, local commands, model providers, external documentation, checks and tools.
- Standard-distribution boundary: mu CLI and desktop distribution, packaged Pi-based agent engine, bundled judgment extension, first-party workers, persisted decisions and supported operator controls.
- Credited operating / distribution surfaces: CLI launcher, packaged coding agent and agent loop, judgment extension, Hive/Swarm, goal controller, approval modes, procedure drafting and skill refresh.
- Adjacent first-party surfaces excluded from ownership: Project maintenance and CI, product development, benchmark harnesses, evaluation datasets, static screenshots and unrelated outside agents or provider organizations.
- First-party operating / deployment modes considered: Standard CLI/desktop coding session; supported Hive and goal modes; operator-governed interactive session and local project. Print/JSON has fewer intervention and learning options.
- Recursion level: One coding work cell with worker sessions where invoked. The outer product organization and arbitrary teams of local installations are outside this boundary.
- Reviewed revision: ba0aeb2d2a6f6caa5809f7bb314642827bc11a96.
- Observation date: 2026-11-15.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The launcher starts the packaged Pi-derived coding session with mu’s judgment extension. The main agent loops over model responses, tools and steering. Model-backed decision points classify bounded questions, with active, shadow and fallback behavior. The extension persists turn and decision records, runs fresh workers and Hive investigators, and supplies the goal checker, worker status and control surfaces. A separate operator path covers steering, acceptance of reusable skills and policy settings. Models supply inference through configured providers, while the distribution owns role invocation, context, tool execution and consequences.

Evidence: [launcher](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/kyrn/bin/mu.mjs#L1-L31), [architecture](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/docs/architecture.md), [feature registration](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/extension/kyrn-judge.ts#L255-L333), [agent loop](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/agent/src/agent-loop.ts#L172-L300).

## Operational model

The main coding agent chooses operational actions and synthesizes a delivered result. Spawned worker sessions independently execute scoped implementation or investigation tasks. In Hive, distinct investigators generate source findings, receive qualified corrections and share them with the main agent. The goal mode regulates continuation of the whole coding-cell commitment, while a user can inspect and redirect the active session. The local owner decides which prospective skills are installed and the standing discretion under which future sessions operate.

## S1 — Operations

- State: A
- Function: Investigate, implement and check the assigned coding task through a model-directed tool loop.
- Disturbance / variety regulated: Changing source state, failing checks and incomplete task evidence require choices about subsequent reads, edits and verification.
- Decisive decision or feedback right: Choose the next tool action or response from task context and returned operational results.
- Decision owner: Main agent running inside the packaged coding runtime; workers own bounded delegated operational choices when spawned.
- Supporting / enforcement mechanisms: Model transport, typed tool executor, session log, workspace and permission checks.
- Closure path: Tools return observations and edits to the model context, which informs the next action and final work report.
- Boundary reachability: The packaged CLI directly starts this coding loop with its bundled tools and kernel. A configured inference provider supplies responses without serving as a separate orchestration host.
- Why this is / is not agent-owned: Removing the agent’s semantic next-action choice leaves the tools and permissions available without an actor choosing a coding outcome.
- Evidence: [coding session](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/coding-agent/src/core/agent-session.ts#L2000-L2020), [agent loop](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/agent/src/agent-loop.ts#L172-L300), [launcher](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/kyrn/bin/mu.mjs#L1-L31).
- Basis: structural
- Confidence: high
- Caveats: Operator checkpoints may limit particular actions. Native model quality and output success are outside the grade.

## S2 — Coordination

- State: A
- Function: Attenuate interference between simultaneously active Hive investigations about the same operational question.
- Disturbance / variety regulated: Independently derived, stale or contradictory conclusions would otherwise continue to guide peers’ subsequent searches.
- Decisive decision or feedback right: Judge whether a finding materially supersedes, contradicts or supports an earlier finding and route relevant material between active investigators.
- Decision owner: Bundled model-backed relation and delivery decisions in active Hive mode. Investigators own their subsequent inquiry.
- Supporting / enforcement mechanisms: Append-only note and relation store, score/policy interpretation, delivery caps, receiver history and steering messages.
- Closure path: A correction or dispute reaches investigators who received the previous finding, updates their context during operation, and is reflected in the main agent’s result.
- Boundary reachability: The installed extension registers Hive and supplies the decision and feedback protocol when invoked.
- Why this is / is not agent-owned: The runtime transports corrections, while a configured judge chooses semantic relations from case evidence and thus which corrections enter peer contexts.
- Distinct S1 units: Two or more first-party investigator sessions independently read source, run checks and report findings under assigned scopes.
- Inter-S1 disturbance: Evidence collected by one peer can invalidate a finding another peer is already working from.
- Attenuating coordination relation: A later report is classified against prior notes, and the relation determines whether the earlier claim should be corrected or treated as disputed.
- Feedback into subsequent S1 behaviour: The receiving bee gets a steering message about a contradiction or replacement before further inquiry.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The algorithm recognizes semantically interfering findings and targets corrective feedback to recipients already depending on them.
- Evidence: [relation decision](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/decisions/hive.ts), [correction and peer steering](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/extension/features/hive.ts#L221-L343), [relation folding](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/hive/board.ts#L193-L230).
- Basis: structural
- Confidence: high
- Caveats: Shadow, unavailable-judge and non-Hive runs need not supply the same ownership path.

## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate the active coding cell’s current commitment when a completed turn fails to settle the goal, a blocker appears, or the work stalls.
- Disturbance / variety regulated: Multiple turns and delegated steps can consume effort while a goal remains unmet or progress stalls.
- Decisive decision or feedback right: Evaluate accumulated current-work evidence against the active commitment and decide whether to continue with a next step, pause for intervention, or settle the goal. An interactive owner can inspect progress and redirect or terminate the current commitment.
- Decision owner: Model-based goal checker in the supported goal mode; legitimate session owner in the interactive supervisory path.
- Supporting / enforcement mechanisms: Goal state, hard continuation/time caps, stop and steering integration, Board/worker status, session event persistence.
- Closure path: Goal verdict changes the cell’s status or enqueues a specific next instruction. Owner interruption pauses the goal and a returned user direction can replace or resume the active work.
- Boundary reachability: The installed judge registers goal evaluation and both terminal and interactive controls. These operate on the same live session and goal.
- Why this is / is not agent-owned: The checker’s judgment about work remaining contributes discretion beyond fixed budget enforcement. The owner independently decides whether the cell should continue its present assignment.
- Whole-system current view: For this one work cell, the current goal checker receives the session goal and material recent execution evidence. The operator can inspect the live task board, goal, latest events and workers.
- Current-control decision scope: Continue, change next work, pause or stop the present cell commitment. No broader inter-project resource control is inferred.
- Evidence: [goal implementation](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/extension/features/goal.ts#L346-L505), [goal state and resume](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/extension/features/goal.ts#L212-L282), [operator mid-run controls](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/kyrn/docs/features/mid-run-messages.md), [Board](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/kyrn/docs/features/plain-language-board.md).
- Basis: structural
- Confidence: medium
- Caveats: This assessment treats the finite goal as the whole work cell. A routine single-turn completion check alone does not establish this current-control function.

| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Built-in model-based goal checker | End of turn with a live goal and evidence of progress or failure | Model judgment is translated into renewed work, pause or completion by the goal controller | [goal control](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/extension/features/goal.ts#L346-L505) |
| Parent (`P`) | User who commissioned and controls the local cell | Live progress view, blocker or changed present priority | Interruption or steering changes the active session, goal state and subsequent work | [interruption and resume](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/extension/features/goal.ts#L235-L282), [operator steering](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/kyrn/docs/features/mid-run-messages.md) |

## S3* — Complementary audit

- State: A
- Function: Independently check conflicting primary-source claims reported by existing Hive investigators when ordinary coordination leaves the dispute unresolved.
- Disturbance / variety regulated: Contradictory reports could leave the main agent relying on a flawed operating account.
- Decisive decision or feedback right: Determine whether either disputed source claim holds, or both hold under different conditions, by checking underlying evidence and reporting the result.
- Decision owner: Fresh, separately spawned verifier agent. The judge classifies the relation of its published findings, while the verifier does the evidence check.
- Supporting / enforcement mechanisms: Timed unresolved-dispute detection, fresh worker session, bounded verifier count, source-reading and checking tools, and the Hive board.
- Closure path: A verifier finding reaches peers through correction and dispute routing and appears in the board and reports returned to the main agent. Unresolved disputes remain visible.
- Boundary reachability: The registered Hive implementation automatically adds a targeted verifier in the supported mode when a dispute persists.
- Why this is / is not agent-owned: A timeout only starts the additional inquiry. The fresh verifier decides what evidence to inspect and what conclusion the evidence supports.
- Claim being audited: Competing reports about the same operational source or check produced by existing investigators.
- Ordinary reporting path: Original investigators report through their own notes and terminal reports.
- Complementary access path: The new verifier is tasked to find the underlying command, file and line and can inspect the workspace directly.
- Independence boundary: Fresh agent session distinct from the original reporters, with the conflicting statements supplied as hypotheses. The source does not establish provider diversity or an external auditor.
- Who acts on findings: Corrective messages reach investigators and the main agent uses the evidence in its response.
- Evidence: [independent dispute verifier](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/extension/features/hive.ts#L555-L615), [report return](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/extension/features/hive.ts#L622-L692), [correction routing](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/extension/features/hive.ts#L221-L245), [main-agent request](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/hive/request.ts#L38-L47).
- Basis: structural
- Confidence: medium
- Caveats: This is a narrow audit of disputed Hive evidence. Verifier absence after a short or unavailable run remains possible, and the patch metadata judgment is not credited as a separate audit.

## S4 — Outside-and-then intelligence

- State: P
- Function: Convert evidence about recurring user/project demands or environment constraints into reusable capability for future coding tasks.
- Disturbance / variety regulated: Interactive runs repeatedly encounter the same project procedures or need capabilities adapted to workspace-specific conditions.
- Decisive decision or feedback right: Select which evidenced procedure becomes an installed reusable skill and when a project-specific adaptation can take effect.
- Decision owner: Local user with authority over installed task capabilities.
- Supporting / enforcement mechanisms: Model-based procedure detection/writing, draft store, accept/reject commands, skill refresh and later session discovery.
- Closure path: An accepted draft becomes a project or local skill and is advertised to the model in later interaction or session initialization. The evolve path also feeds selected workspace permission adaptations into later use.
- Boundary reachability: The standard interactive extension registers procedure drafts and installs accepted skills through its own commands.
- Why this is / is not agent-owned: The runtime detects and proposes options. The owner makes the binding decision to install a draft. Observing a command substitution or recalling a stored note is narrower evidence than autonomous ownership of this general adaptation right.
- External distinction: The user’s actual recurring tasks and workspace-specific procedures, including observed environment requirements.
- Future / prospective distinction: A repeatable procedure is selected for later work beyond the completed example that produced it.
- Adaptation option generated: Install, reject or retain a proposed reusable skill, optionally scoped to the current project.
- Path back into current capability / S3: Accepted skill is persisted and discovered by later model instructions. The agent’s available procedures therefore change.
- Evidence: [procedure generation](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/extension/features/procedures.ts#L104-L145), [operator acceptance](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/extension/features/procedures.ts#L210-L280), [capability refresh](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/kyrn/docs/features/skill-refresh.md), [environment feedback and adaptations](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/kyrn/docs/features/self-evolution.md).
- Basis: structural
- Confidence: medium
- Caveats: The source establishes a feature-level adaptation loop with owner acceptance. It does not establish autonomous prospective product redesign or measured recurrent benefit.

## S5 — Policy and identity

- State: P
- Function: Resolve the standing policy about what the local coding cell may do autonomously and when it must return authority to its owner.
- Disturbance / variety regulated: The drive to complete a coding task can conflict with the local owner’s standing limits on delegated operation.
- Decisive decision or feedback right: Choose and revise the durable permission mode governing future local sessions, including whether delegated approval decisions go to a judge or remain with the user.
- Decision owner: Legitimate local workspace/session owner in the interactive permission settings path.
- Supporting / enforcement mechanisms: Owner-facing mode setting, saved defaults, session binding and permission enforcement. Child sessions can receive the parent session’s current mode.
- Closure path: The owner’s selected durable mode is read into new sessions and determines their future approval ownership and action boundary.
- Boundary reachability: The permission modes and persistent operator path ship and are registered by default in the assessed distribution.
- Why this is / is not agent-owned: Per-action tool decisions operate inside the standing mode. The mode choice remains an operator decision and affects subsequent tasks.
- Identity / ultimate-policy issue: Whether the local harness is constituted as an ask-first or judge-delegated coding cell and which powers that choice leaves with the workspace owner.
- Ultimate authority in each claimed mode: Local owner commissions the cell and selects its enduring authority configuration.
- Return-to-operation path: Owner command or desktop setting → persistent mode and current session binding → approval disposition in future work and inherited worker modes.
- Evidence: [standing mode and inheritance](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/kyrn/docs/features/permissions.md#L93-L120), [operator command implementation](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/extension/features/permissions.ts#L854-L923), [subagent inheritance](https://github.com/qybaihe/mu/blob/ba0aeb2d2a6f6caa5809f7bb314642827bc11a96/packages/kyrn-judge/src/extension/features/swarm.ts#L199-L209).
- Basis: structural
- Confidence: medium
- Caveats: Scope is the local work cell’s enduring delegation policy. Individual approvals and the upstream project's governance are outside this S5 claim.

## Distributed OSS parent arrangement

The operator of the local work cell is the parent for the claimed modes. The repository’s maintainers and contributors do not receive authority over an arbitrary installation’s live goal, adaptations or operating limits.

## Self-hosted and non-human modes

Terminal and desktop sessions share the shipped agent and judgment runtime. Goal and Hive exercise built-in autonomous paths when activated and adequately configured. The supported interactive host supplies the parent decisions. Unattended modes are not assumed to offer interactive acceptance, steering or observation of new adaptation evidence.

## Recursion

The assessment treats the commissioned main coding cell as one recursion. Worker sessions are operational units at this boundary, without a claim that each child implements its own complete viable system. The local workspace owner is the external parent.

## Variety and escalation

The judgment layer transforms runtime evidence into targeted corrections or next steps. The user can intervene when the goal cannot progress, a policy calls for approval, or a workflow proposes changes to future capabilities. Routine permission prompts constitute bounded escalation at this scope.

## Evidence gaps

This is a primary-source structural review. No live model, tool execution or provider benchmark was reproduced. Hive verification depends on an unresolved dispute, available verifier budget and successful launch. Goal control is scoped to one active coding cell. The strength of verifier independence and the effectiveness of installed adaptations remain unmeasured here.
