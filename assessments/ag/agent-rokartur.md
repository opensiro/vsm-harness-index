---
harness_id: agent-rokartur
project_name: agent (rokartur)
repository: https://github.com/rokartur/agent
review_ref: f02a473edd8a08368876e45a641f8ed8c2a4c85d
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# agent (rokartur)

## Review boundary

- System in focus: a root coding session and its first-party child-agent task team.
- Purpose and identity: complete coding requests with model-selected tools, optional delegated work and durable sessions.
- Relevant environment: workspace files, shell processes, model accounts, peer sessions and user permissions.
- Standard-distribution boundary: released/source-built Rust binary, session server and bundled tools/prompts/workflows; externally installed plugins/skills are not credited as built-in owners.
- Credited operating / distribution surfaces: [source/src/agent/mod.rs](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/mod.rs), [source/src/agent/subagent.rs](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/subagent.rs), [source/src/agent/swarm-prompt.md](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/swarm-prompt.md), [source/src/tools/tools.json](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/tools/tools.json), [source/src/tools/hashline.rs](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/tools/hashline.rs), [source/docs/run-modes.md](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/docs/run-modes.md)
- Adjacent first-party surfaces excluded from ownership: repository contributor/triage agents, CI/release, benchmark claims, and usagefleet plugin development are outside this task-team ownership boundary. Tests corroborate implementation without donating audit ownership.
- First-party operating / deployment modes considered: interactive session server, print/JSON/headless/ACP, supervised Ask, Auto reviewer and FullAccess; child processes, bundled workflows, trusted project instructions and remote Tailscale attachment.
- Recursion level: one root task team; unrelated peer sessions remain adjacent unless explicitly participating.
- Reviewed revision: f02a473edd8a08368876e45a641f8ed8c2a4c85d
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

One Rust binary supplies synchronous provider requests, threads/channels, a persistent JSONL session and socket-based terminal attachment. Agent::run_turns selects model tools, executes them with permissions/snapshots, appends results and re-enters the model. Root-only child spawning launches the same binary in fresh headless contexts with bounded tools; background results queue into the root's next turn, and messages can steer or resume a child. The root can see child states, select model/effort/cwd and stop work. Hashline anchors reject edits when a read version is stale; worktrees and Git conflict hints are additional tools. Auto permissions use a separate model's allow/deny response on the proposed call. LSP/edit hooks are routine coding feedback. Bundled deep-research performs source checking as part of its production workflow; model accounts/failover, skills, cron, compaction, snapshots and updates support operations.

## Operational model

The root and delegated model-backed coding children are S1 units; transport threads and background shell tasks are not automatically additional S1s. A root tasked with a team outcome retains the current roster/results and may revise scope, model effort and continued commitments using messages and TaskStop. The specific S2 claim below is the conflict-safe edit constructor, not generic messaging or task splitting. Audit ownership is limited to the built-in root instruction to independently verify child claims before relying on them; an arbitrary 'reviewer' persona, Auto permission approval and routine edit hooks are not the credited audit.

## S1 — Operations

- State: A
- Function: coding transformation by root and child agent loops
- Disturbance / variety regulated: unknown source, tool failures, changing files and delegated findings
- Decisive decision or feedback right: select tool/action/arguments and revise the approach from results
- Decision owner: root/child models within their assigned scopes
- Supporting / enforcement mechanisms: provider adapters, permissions, tool dispatcher, JSONL persistence, snapshots and channels
- Closure path: model tool choice → execution result → next model input; child answer/follow-up → root continuation
- Why this is / is not agent-owned: Removing the model leaves execution support but no discretionary solution.
- Evidence: [source/src/agent/mod.rs#L539-L670](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/mod.rs#L539-L670), [source/src/agent/subagent.rs#L188-L215](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/subagent.rs#L188-L215), [source/src/agent/subagent.rs#L263-L323](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/subagent.rs#L263-L323)
- Basis: structural
- Confidence: medium-high
- Caveats: Pinned source establishes a supported path, not observed effectiveness or universal deployment.
- Boundary reachability: Agent::run_turns is called by supported CLI/server modes; child launch uses the current installed executable.

## S2 — Coordination

- State: C
- Function: prevent stale writes from overwriting another operational writer's changes
- Disturbance / variety regulated: root/parallel children can act on the same cwd after reading different file versions
- Decisive decision or feedback right: reject stale anchored edits and return fresh-read feedback; broader coordination discretion still needs composition
- Decision owner: first-party anchor controller enforces the rule; no separately assigned autonomous cross-writer coordination owner
- Supporting / enforcement mechanisms: session-specific anchors, reread/sync before edit, model-visible error and common child cwd
- Closure path: another writer changes file → stale anchor rejected → caller receives E_STALE_ANCHOR and must reread before a valid subsequent edit
- Why this is / is not agent-owned: A concrete collision-specific path exists; deterministic rejection does not itself own autonomous coordination judgment. C credits this narrow supplied path, not the ability to program any coordinator.
- Evidence: [source/src/tools/hashline.rs#L308-L329](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/tools/hashline.rs#L308-L329), [source/src/tools/hashline.rs#L654-L659](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/tools/hashline.rs#L654-L659), [source/src/agent/mod.rs#L975-L1004](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/mod.rs#L975-L1004), [source/src/agent/mod.rs#L640-L666](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/mod.rs#L640-L666)
- Basis: structural
- Confidence: medium-high
- Caveats: Pinned source establishes a supported path, not observed effectiveness or universal deployment.
- Boundary reachability: Hashline-backed tools are installed for the coding agents and child launch defaults to the root cwd.
- Distinct S1 units: root coding agent and parallel child coding agents.
- Inter-S1 disturbance: stale read-modify-write on shared files after a different writer edits them.
- Attenuating coordination relation: anchor ownership plus reread/sync rejects stale range rather than silently overwriting.
- Feedback into subsequent S1 behaviour: caller receives explicit fresh-read instruction in tool result, then chooses its next action.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the credited path is version-sensitive writer-conflict rejection, not child spawning, work ordering or a mailbox.

## S3 — Inside-and-now control

- State: A
- Function: current cohesion and accountability of the bounded child task team
- Disturbance / variety regulated: different child states, failed/superseded work and model/effort commitments
- Decisive decision or feedback right: inspect team roster/results, change active child scope, stop and resume commitments, select model/effort for replacement work
- Decision owner: root model for its current team
- Supporting / enforcement mechanisms: ListAgents, SendMessage, TaskStop, subagent state and follow-up queues; static concurrency cap is enforcement
- Closure path: team status/result → root current judgment → steering/stop/resume/new scoped resource choice → changed child operations → later state/result
- Why this is / is not agent-owned: This is narrower than global fleet governance and exceeds initial decomposition: a running child can be steered, stopped and resumed after accountability feedback.
- Evidence: [source/src/agent/mod.rs#L892-L1029](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/mod.rs#L892-L1029), [source/src/agent/subagent.rs#L92-L108](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/subagent.rs#L92-L108), [source/src/tools/tools.json](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/tools/tools.json), [source/src/agent/swarm-prompt.md#L18-L35](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/swarm-prompt.md#L18-L35)
- Basis: structural
- Confidence: medium-high
- Caveats: Task-team scope only. Generic human plan approval, session interruption and permission-mode edits are not credited as a separate parent S3 mode.
- Boundary reachability: Root's shipped tool set exposes status and intervention; follow-ups enter its continuing run loop. No custom control-plane code is required.
- Whole-system current view: root's roster of its child tasks/status plus returned answers, within the task-team recursion.
- Current-control decision scope: ongoing team commitments, task scope, model/effort resources and intervention; not provider infrastructure or unrelated sessions.

## S3* — Complementary audit

- State: A
- Function: challenge delegated outcome claims with complementary primary-artifact access
- Disturbance / variety regulated: a child answer can be mistaken despite appearing complete
- Decisive decision or feedback right: independently open cited source or rerun the decisive command before relying on the child's claim
- Decision owner: root agent as a decision holder distinct from the child producer
- Supporting / enforcement mechanisms: built-in swarm guidance embedded in Agent tool description, root Read/Bash, returned child claim and root continuation
- Closure path: child answer → root selects checks on depended-on claims → raw artifact/command evidence → root revises or withholds next work and can steer/resume the child
- Why this is / is not agent-owned: The shipped instruction explicitly treats the answer as a claim and names an alternate evidence path; judgment resides with the root, not a deterministic hook. This does not rely on naming an arbitrary spawned child 'auditor'.
- Evidence: [source/src/agent/swarm-prompt.md#L18-L27](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/swarm-prompt.md#L18-L27), [source/src/tools/mod.rs#L38-L43](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/tools/mod.rs#L38-L43), [source/src/agent/mod.rs#L1022-L1029](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/mod.rs#L1022-L1029), [source/src/agent/mod.rs#L892-L920](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/mod.rs#L892-L920)
- Basis: structural
- Confidence: medium-high
- Caveats: Prompt-guided supported audit mode, not evidence that every run performs it. Auto permission reviewer and deep-research's mandatory verify phase are not used to establish complementary audit.
- Boundary reachability: The default bundled swarm prompt is injected into the root's Agent tool description; root already has source/command tools and consumes child results in supported modes.
- Claim being audited: child's completion/finding claims on which the root's next step depends.
- Ordinary reporting path: child final answer or queued background follow-up.
- Complementary access path: root independently reads cited path:line or reruns decisive command against workspace reality.
- Independence boundary: root context/judgment is separate from the child production context; model provider may be shared, so this is workflow/claim independence, not model-diversity assurance.
- Who acts on findings: root changes its own next step or sends corrective child instructions.

## S4 — Outside-and-then intelligence

- State: —
- Function: outside-and-then adaptation of the harness/team capability
- Disturbance / variety regulated: Web research, long-term goals and self-update are not by themselves prospective system adaptation.
- Decisive decision or feedback right: No function-specific decisive path established.
- Decision owner: None established for this function in the assessed mode.
- Supporting / enforcement mechanisms: bundled deep-research/workflows, goal/todo/cron, model routing, compaction, update and skills
- Closure path: No qualifying function-specific return into operations.
- Why this is / is not agent-owned: Deep-research produces the requested research report; updates follow published versions. No shipped loop turns external prospective distinctions into adaptation options and a current-capability regulatory return; parent adaptation was not established.
- Evidence: [source/src/agent/deep-research.js](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/deep-research.js), [source/src/update.rs](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/update.rs), [source/src/tools/goal.rs](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/tools/goal.rs), [source/src/agent/workflow.rs](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/workflow.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded absence at the frozen first-party distribution; arbitrary surrounding organizations and user extensions are not assessed.

### Absence scope

- Surfaces inspected: bundled deep-research/workflows, goal/todo/cron, model routing, compaction, update and skills
- Plausible first-party paths checked: external searches, verification, reusable workflow scripts and software update paths
- Why no material first-party path remains: Deep-research produces the requested research report; updates follow published versions. No shipped loop turns external prospective distinctions into adaptation options and a current-capability regulatory return; parent adaptation was not established.

## S5 — Policy and identity

- State: —
- Function: identity / ultimate-policy closure
- Disturbance / variety regulated: Ask/Auto/FullAccess permissions, trust and prompt policy bound ordinary tool actions.
- Decisive decision or feedback right: No function-specific decisive path established.
- Decision owner: None established for this function in the assessed mode.
- Supporting / enforcement mechanisms: permission reviewer, trusted project instructions, plan approval, settings, root swarm constraints and session UI
- Closure path: No qualifying function-specific return into operations.
- Why this is / is not agent-owned: The review judges an individual proposed action against the existing request; it neither resolves identity-policy tension nor constructs an authoritative policy-return loop. Mutable prompts and contributor governance do not close S5 for the deployed task team.
- Evidence: [source/src/agent/permissions.rs#L178-L229](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/permissions.rs#L178-L229), [source/src/agent/mod.rs#L1106-L1141](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/mod.rs#L1106-L1141), [source/src/agent/prompt.rs](https://github.com/rokartur/agent/blob/f02a473edd8a08368876e45a641f8ed8c2a4c85d/source/src/agent/prompt.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded absence at the frozen first-party distribution; arbitrary surrounding organizations and user extensions are not assessed.

### Absence scope

- Surfaces inspected: permission reviewer, trusted project instructions, plan approval, settings, root swarm constraints and session UI
- Plausible first-party paths checked: whether permission/plan decisions constitute identity matters and whether a legitimate parent policy return is wired
- Why no material first-party path remains: The review judges an individual proposed action against the existing request; it neither resolves identity-policy tension nor constructs an authoritative policy-return loop. Mutable prompts and contributor governance do not close S5 for the deployed task team.

## Distributed OSS parent arrangement

Human maintainers own the repository; local users supply goals and permissions. Repository triage/development agents and contributor decisions are not part of this deployed team. No organization-level parent governance is inferred.

## Self-hosted and non-human modes

All provider/local/remote-terminal modes share the root/child runtime. Ask and Auto change ordinary permission ownership; they do not by themselves add a qualified S3/S4/S5 parent loop.

## Recursion

Root/child decomposition is not evidence that every child is a viable recursive organization; child tools are deliberately restricted and spawning is root-only.

## Variety and escalation

Per-child contexts attenuate root input; completion messages restore selected findings. Raw claim checks counter lossy child reporting. Concurrency, permissions and context budgets enforce selected limits; they do not inherit the root's current-control judgment.

## Evidence gaps

Static source review; cargo absent so Rust tests/compilation were not run. No live provider-backed agent task, performance comparison or empirical audit-effect claim. User-overridden swarm prompts, installed extensions and unknown deployments may change ownership.

## Index execution provenance

Frozen intake #2176, serial controller #2177, row 2. Source assessment is the executing Index S1 actor's work; GitHub, deterministic checks and CI are supporting machinery. No independent semantic review or autonomy grade is claimed. Proposed publication precedes a separate canonical transaction.
