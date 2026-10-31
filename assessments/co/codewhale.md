---
harness_id: codewhale
project_name: Codewhale
repository: https://github.com/codewhale-hq/Codewhale
review_ref: 327c15df976601ca3114ea40ac3dc88cea9f152a
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Codewhale

## Review boundary

- System in focus: the local Codewhale CLI/Runtime workspace with its native agent/tool loop, optional named fleet/workflow coordinator and goal continuation, not a hosted commercial Codewhale product or repository maintainers.
- Purpose and identity: perform user-defined coding/workspace tasks, coordinate bounded subordinate workers, verify progress and return artifacts while enforcing local policy.
- Relevant environment: repository files/tests/CLI results, provider responses, parallel worker edits, failed jobs, stale reviewer artifacts, limits, user goals and permissions.
- Standard-distribution boundary: Rust `crates/tui` engine, tools, Runtime, fleet manager and ledger; `crates/workflow` and `workflow-js` compiled workflow/gate/review-repair contracts; shipped CLI/TUI/Web client mode descriptions and bundled fleet-manager skill.
- Credited operating / distribution surfaces: `codewhale exec`/work mode model/tool engine, `agent` delegation, parallel write-scope claims and worktree isolation, durable fleet/Workflow manager, `create_goal`/`update_goal` continuation, explicit reviewer/verifier gate and return paths.
- Adjacent first-party surfaces excluded from ownership: private GPUI roadmaps, landing/site/payment product, CI/build scripts, tests and demo-only workflows, optional third-party VS Code extension and upstream repository contributor governance. External LLM/model APIs and user-installed MCP services remain providers, not independent Codewhale-owned organs.
- Modes considered: terminal interactive/`exec`, Plan vs Work/Operate permissions, optional spawned agents and fleet workflows, manager-authored Workflow, review/verify gate with bounded repair, persisted goal continuation, manual approvals; the documented variants are not all enabled in every run.
- Recursion level: one workspace-level coordinated coding mission with subordinate role agents/workers. Independent installations and the OSS organization are outside.
- Reviewed revision: `codewhale-hq/Codewhale@327c15df976601ca3114ea40ac3dc88cea9f152a`, GitHub repo ID 1137711311, formerly `Hmbown/Codewhale`, immutable intake #2501/controller #2502 row 4.
- Observation date: 2026-10-31; active Profile 0.2.4 / released Methodology 0.3.7. Source/static review, not a paid-provider E2E task.

## Repository architecture

The pinned [README](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/README.md) describes a source-distributed model-directed agent that reads, edits, runs commands, checks results and persists goals. [Fleet](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/FLEET.md) is a roster/identity selector, not the execution owner; a delegated Runtime coordinator launches actual `codewhale exec` workers and records leases, heartbeats, receipts and failure recovery. [Subagent guidance](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/SUBAGENTS.md) separates worktree isolation from file-write claims and refuses overlapping active claims before mutation. [Workflow write-scope validator](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/workflow/src/lib.rs) explicitly rejects parallel write tasks with overlapping file scopes. [Workflow gates](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/workflow/src/gates.rs) and [review-repair contract](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/workflow/src/review_repair.rs) distinguish reviewer/verifier role verdicts, exact artifact digest, bounded repair, fail-closed inconclusive results and optional explicit user ratification. [Goals](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/tui/src/tools/goal.rs) allow the model agent to record evidence-backed continuation rather than silently treating an incomplete goal as done.

## Operational model

An operator sets a task and authority envelope; the Codewhale agent interprets file/tool feedback and selects next steps. For a complex job, an agent-authored Workflow and manager coordinate child workers; Runtime enforces leases and file isolation but does not itself make coding judgments. Review/verify gates become a function-specific complementary constructor when separately routed roles supply substantive findings and a returned rework loop. Durable goal completion/repair is inside-and-now mission control, not necessarily future-looking S4. Approval postures and user prompts are constraints, not S5 identity policy.

## S1 — Operations

- State: A
- Function: inspect, modify and validate a user's codebase or workspace through a model-directed tool/action loop.
- Disturbance / variety regulated: arbitrary coding tasks, changing repository content, tool errors, test feedback and model output variation.
- Decisive decision or feedback right: the instantiated Codewhale agent chooses file edits, commands and corrective steps from observed results.
- Decision owner: first-party model/tool loop in the CLI/Runtime; hosted/local inference endpoints generate replies but are not owners of Codewhale's tool authorization or run lifecycle.
- Supporting / enforcement mechanisms: tool registry, permission/sandbox checks, file revisions, transcript/session memory and provider transport.
- Closure path: task prompt → model/tool decision → read/edit/command execution → observed diff/test result → next agent action or final validated artifact.
- Boundary reachability: `codewhale exec` and interactive Work mode are documented everyday product entry points with a shipped Rust engine and tool set.
- Why this is / is not agent-owned: without the model-driven actor the CLI could still enforce permissions or run commands manually, but would not autonomously select coding work and repair steps.
- Evidence: [README](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/README.md); [MODES](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/MODES.md); [engine](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/tui/src/core/engine.rs); [agent tool](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/tui/src/tools/subagent/mod.rs).
- Basis: structural
- Confidence: medium
- Caveats: no live code task/provider E2E was run; model/tool actor is source-evidenced, not claimed empirically successful.

## S2 — Coordination

- State: C
- Function: attenuate simultaneous child editors' interference in shared workspace files and declared coordination resources.
- Distinct S1 units: separate model-driven child workers/fleet roles executing parallel coding tasks, each with a possible write envelope.
- Inter-S1 disturbance: overlapping parallel write scopes, conflicting edits on the same file/contract, stale shared checkout state and duplicate incompatible ownership claims.
- Attenuating coordination relation: Runtime requires declared exact files/write roots or coordination contracts, checks active overlaps before mutation, or launches truly isolated worktrees. Workflow validation rejects parallel writable tasks with intersecting scopes, while manager/worker receipts permit later non-conflicting merge/handoff.
- Feedback into subsequent S1 behaviour: an overlapping claim is refused instead of permitting simultaneous conflicting writes; a selected isolated worktree executes separately and returns branch/artifact identity for manager-mediated integration.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: a concrete same-file/contract contention witness is checked by a specific overlap/exclusion relation that directly changes whether independently active S1 workers can proceed.
- Disturbance / variety regulated: write contention and destructive workspace interference among parallel S1 units.
- Decisive decision or feedback right: validate/admit or block conflicting writer claims and return separation into later work.
- Decision owner: first-party deterministic write-scope/worktree coordination constructor with operator/manager-provided scope; broader autonomous conflict trade-off remains to be composed.
- Supporting / enforcement mechanisms: live claim registry, path normalization, authorization ceilings, git worktrees, task/role status and ledger receipts.
- Closure path: parallel work claim → active/shared scope comparison → reject or isolated admission → permitted edits/worker result → coordinator selects a safe follow-on handoff.
- Boundary reachability: [SUBAGENTS](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/SUBAGENTS.md), [Workflow overlap check](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/workflow/src/lib.rs) and source [subagent tools](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/tui/src/tools/subagent/mod.rs) are first-party standard multiworker paths.
- Why this is / is not agent-owned: overlap exclusion is specific S2 capacity but its decisive arbitration is fixed policy plus caller claims, not a mandatory model-owned negotiation/repair owner; hence `C`, not `A`.
- Evidence: [SUBAGENTS](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/SUBAGENTS.md); [Workflow lib](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/workflow/src/lib.rs); [fleet/Runtime](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/FLEET.md).
- Basis: structural
- Confidence: medium
- Caveats: applies to declared write-resource collisions, not automatic model-led balancing of all competing worker goals.

## S3 — Inside-and-now control

- State: A
- Function: supervise the current user coding mission and subordinate worker commitments/results until completion, correction, or explicit blocked return.
- Whole-system current view: at the declared workspace mission boundary, the manager receives child status, task/receipt/validation outcomes, durable goal state and work artifacts, not every unrelated local process.
- Current-control decision scope: when to delegate/fan-in, retry, inspect/verify, continue after a failed attempt, stop/escalate or report terminal goal status.
- Disturbance / variety regulated: task failure, stale child result, incomplete verification, workflow dependency blockage and partial goal progress.
- Decisive decision or feedback right: the model-driven manager/goal agent chooses corrective child actions and marks evidence-backed `not_achieved`, `complete` or `blocked` states; Runtime and bounded ledger enforce those choices.
- Decision owner: first-party main model agent/manager in the agent-authored Workflow or persistent goal continuation mode; not the deterministic worker scheduler.
- Supporting / enforcement mechanisms: fleet task ledger and leases, workflow plan/role gates, status/heartbeat, terminal receipts, `create_goal`/`update_goal` tools and bounded retry budgets.
- Closure path: manager plan/current goal → child tasks and tools → wait/receipt/evidence → agent-selected retry/rework/continuation → updated goal/status and later work or terminal result.
- Boundary reachability: [FLEET manager-owned fan-in](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/FLEET.md), source-distributed [goal tools](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/tui/src/tools/goal.rs), [fleet manager](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/tui/src/fleet/manager.rs) and [runtime threads](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/tui/src/runtime_threads.rs) close configured supported paths.
- Why this is / is not agent-owned: the model interprets varied child/goal evidence and chooses next mission interventions; removing it leaves queueing and receipt bookkeeping, not comparable discretionary mission supervision.
- Evidence: [FLEET](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/FLEET.md); [goal.rs](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/tui/src/tools/goal.rs); [fleet manager](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/tui/src/fleet/manager.rs).
- Basis: structural
- Confidence: medium
- Caveats: S3 is at one manager-owned mission recursion, not all repositories or installed Codewhale sessions. A scheduled task alone is not S3 ownership.

## S3* — Complementary audit

- State: C
- Function: challenge a producer's output using separately routed reviewer/verifier roles and gate consequential rework before downstream progression.
- Claim being audited: an implementation artifact/diff is correct, validated and ready for the next role or final completion.
- Ordinary reporting path: implementer/child produces diff, artifacts, logs, model self-report and terminal task receipt.
- Complementary access path: Workflow `Review` and `Verify` gates accept explicit findings/verdicts from separately configured reviewer/verifier role routes; the pinned digest/route receipts and lane-scoped handoff distinguish the review artifact from the implementer's final prose.
- Independence boundary: reviewer and verifier may be distinct fleet agents/models with frozen exact route receipts, but independence is composition-dependent. A bare `ReviewRepairLoop` data structure alone is not an automatically spawned auditor.
- Who acts on findings: gate evaluation blocks the downstream role or triggers bounded upstream retry/escalation; a manager/developer must wire the reviewer actor and corrective return, with optional parent ratification.
- Disturbance / variety regulated: false completion, unreviewed diffs, stale review against moved artifacts, missing/verifier receipts and unsupported pass claims.
- Decisive decision or feedback right: reviewer can issue substantive `RepairsNeeded`/failed/inconclusive judgment and withhold advancement; the gate consumes it to request rework or escalation.
- Decision owner: a separately configured model-driven reviewer/verifier and first-party lane gate/ReviewRepairLoop; assembling a truly independent reviewer and correction loop is not universal/default.
- Supporting / enforcement mechanisms: exact provider/model route receipts, input digest, bounded iterations/time/tools, explicit verdict and fail-closed status, optional human ratification.
- Closure path: producer artifact → separately routed reviewer/verifier evidence → gate verdict → retry/block/escalate to producer/manager → changed artifact/digest and subsequent verification → accepted downstream release or honest blocked status.
- Boundary reachability: [Workflow gates](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/workflow/src/gates.rs), [review_repair.rs](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/workflow/src/review_repair.rs), documented [FLEET/Workflow roles](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/FLEET.md) are source-distributed enabled compositions.
- Why this is / is not agent-owned: reviewer judgment can be a distinct model decision; the controller does not itself supply that independent actor unconditionally, so `C` rather than unconditional `A`.
- Evidence: [gates.rs](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/workflow/src/gates.rs); [review_repair.rs](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/workflow/src/review_repair.rs); [FLEET](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/FLEET.md).
- Basis: structural
- Confidence: medium-low
- Caveats: role and digest records strengthen provenance but do not prove independent reviewer execution in every run. Tests exercised the IR semantics, not a live provider reviewer in this assessment.

## S4 — Outside-and-then intelligence

- State: —
- Function: no distinct first-party prospective organizational adaptation control/return loop established beyond current coding task goals and configurable runtime options.
- Disturbance / variety regulated: evolving providers, future repository requirements, model quality/cost and role fit were checked as candidates.
- Decisive decision or feedback right: no owner evidenced selecting future mission capability/policy changes from environmental trends and closing them into later system operation as a separate organizational function.
- Decision owner: user configures fleet/model routes/goals, and main agent repairs current task; those choices are not a distinct S4 organ at the reviewed recursion.
- Supporting / enforcement mechanisms: model catalog, Reasoning Router, role profiles, durable sessions, goals and workflow plans.
- Closure path: goal updates/rework improve current mission outcome; there is no source-backed external future distinctions → adaptation alternatives → selected capability change → later effectiveness feedback circuit.
- Why this is / is not agent-owned: durable memory, dynamic model selection and iterative verification can serve S1/S3 without establishing outside-and-then adaptation.
- Evidence: [FLEET](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/FLEET.md); [MODES](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/MODES.md); [goal.rs](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/crates/tui/src/tools/goal.rs).
- Basis: structural
- Confidence: medium-low
- Caveats: source-reviewed standard modes only; an agent-authored custom workflow could implement such a function, but no first-party S4-specific constructor was found.

### Absence scope — S4

- Surfaces inspected: model/fleet routing, workflow manager and gates, persisted goal continuation, config and role profiles, README/MODES and Runtime policy.
- Plausible first-party paths checked: Reasoning Router, model switching, goal updates, review-repair learning, fleet profile editing, external model trends and workflow evolution.
- Why no material first-party path remains: route choice and task-goal correction optimize a current run under user settings, not a distinct prospective environmental intelligence/adaptation owner with return to future S3 capability.

## S5 — Policy and identity

- State: —
- Function: no independent legitimate ultimate-identity/policy adjudication and return loop evidenced within a workspace run.
- Disturbance / variety regulated: conflicting permissions, safety policy, user role settings and approval requests are already governed by configured authority ceilings.
- Decisive decision or feedback right: no agent/runtime right to redefine the organization's ultimate purpose/identity beyond ordinary user-specified coding goals and policy constraints.
- Decision owner: user/administrator chooses policy stack and project/workspace trust; Runtime enforces non-escalating delegated authority.
- Supporting / enforcement mechanisms: permission postures, sandbox, tool ACLs, worktree claims, delegated scope intersection and explicit approvals.
- Closure path: approve/deny or config changes constrain later tasks, but are not an unresolved identity/policy conflict → authoritative deliberation → returned S5 governance loop.
- Why this is / is not agent-owned: personal skill/persona profiles and user authorization are not ultimate-policy S5 decisions for the coding organization.
- Evidence: [AUTHORIZATION_ORDER](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/AUTHORIZATION_ORDER.md); [MODES](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/MODES.md); [SUBAGENTS](https://github.com/codewhale-hq/Codewhale/blob/327c15df976601ca3114ea40ac3dc88cea9f152a/docs/SUBAGENTS.md).
- Basis: structural
- Confidence: medium-low
- Caveats: bounded absence at one workspace mission, not a judgment about upstream OSS governance.

### Absence scope — S5

- Surfaces inspected: authorization hierarchy, permission modes, workspace trust, fleet identity vs authority, goal role profiles and contributor/public project governance.
- Plausible first-party paths checked: agent profile/identity, project trust, user approval, policy changes, managed tool constraints, team ownership and upstream maintainer decisions.
- Why no material first-party path remains: these are preselected boundaries, operational approvals or adjacent institutions, none an identity-level conflict resolved by a distinct runtime governance owner and returned to later operation.

## Distributed OSS parent arrangement

Multiple Codewhale contributors, remote model providers and fleet roles are not a unified parent S5. A user's ratification of a clean review is a task-release approval, not S5 or independent S4 adaptation.

## Self-hosted and non-human modes

The CLI/Runtime is local/self-hosted, with an operator-selected model. The autonomous agent may drive coding and mission supervision within policy; Runtime enforces tool access, sandbox/permissions, scope reservations and receipts. No vendor-hosted supervisory organ is borrowed.

## Recursion

The workspace mission is the declared whole. Subordinate independent workers form S1 units; conflict protection and manager fan-in operate at that recursion. A named fleet roster or nested profile alone is not a viable recursive system.

## Variety and escalation

Tool errors, bounded retries, receipt validity, stale-artifact checks, write-claim denials and human-ratification gates channel operational variety. A blocked gate/escalation is a returned exception, not a proof of S5 identity choice or future S4.

## Evidence gaps

No live Rust build/provider-backed run or actual external reviewer was executed; source and relevant tests/first-party documentation were inspected. The S2 witness is specific simultaneous write contention, and S3 supervision is mission-local. S3* is an explicitly composable independent review constructor, not an automatic review on every local session. Goal persistence/restart does not, without distinct environmental future adaptation, warrant S4.
