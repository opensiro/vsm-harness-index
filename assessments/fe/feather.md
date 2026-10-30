---
harness_id: feather
project_name: Feather
repository: https://github.com/paper-instruments/feather-train
review_ref: cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Feather

## Review boundary

- System in focus: the independently installable Feather Harness knowledge-work runtime, including its supported optional production subagent team, at one local task/team recursion.
- Purpose and identity: produce document, spreadsheet, presentation, PDF and other knowledge-work deliverables with model-selected tools.
- Relevant environment: user requests, shared workspace files, shell processes, MCP services, optional web sources and an OpenAI-compatible model provider.
- Standard-distribution boundary: `feather-harness` library and local CLI, built-in `prod` and `train` profiles; `prod` with explicitly configured subagents is the credited multi-agent mode.
- Credited operating / distribution surfaces: `core/runner.py`, `local/__init__.py`, `cli.py`, `subagents.py`, `tools/agents.py`, file/process/MCP tools and packaged production guidance.
- Adjacent first-party surfaces excluded from ownership: independently packaged Feather Train rollout/grading/Tinker training and Feather Eval Harbor/ATIF adapters, repository CI, tests and contributor governance. Their evaluators do not become the installed knowledge-work team's auditor or adaptation owner.
- First-party operating / deployment modes considered: noninteractive local CLI, direct library embedding, production single agent and production subagent team, minimal training profile. Generic application-host extensions are not credited as installed actors.
- Recursion level: one user-task team; its parent model and child model sessions are operational actors, not the human/organization parent denoted by publication `P`.
- Reviewed revision: `cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The [root package map](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/README.md) separates Harness, Train and Eval. Harness's [CLI](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/cli.py#L28-L92) creates the model and local runtime. The [agent loop](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/core/runner.py#L297-L370) repeatedly feeds model-selected tool results back into context until an answer or a turn/error limit. Compaction preserves separate execution/summary segments; traces, shell logs and child results are saved locally.

The [supported subagent mode](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/docs/subagents.md) is opt-in and production-only. The parent receives assignment, status, wait, follow-up and stop tools. Children retain their own conversation, todo, read revisions, shell/MCP resources and transcripts while sharing the filesystem. Children cannot delegate. The standard local runner constructs these sessions and injects the parent/child guidance; callers do not have to write an organizational controller.

Human involvement sets the task, endpoint, workspace, profile and upper bounds. The CLI runs one noninteractive task and returns a result; generic host embedding and additional instructions are configurable, not evidence of a function-specific supervisory or ultimate-policy conversation. OSS maintainer decisions and releases belong to the repository-development organization.

## Operational model

The parent and each activated child transform assigned knowledge work into findings or files, selecting tools and handling local failures. The parent also controls current team commitments and shared-file division of work. Runtime limits, status persistence and cancellation implement those choices but do not own the parent's discretionary allocation or revision decisions. Single-agent/train modes need not exercise the optional S2/S3 team paths.

## S1 — Operations

- State: A
- Function: execute user knowledge work and child assignments into deliverables.
- Disturbance / variety regulated: changing file contents, incomplete sources, tool errors, model-response interruptions and task-specific analysis.
- Decisive decision or feedback right: select the next tool/action and decide how returned evidence changes the work or final answer.
- Decision owner: parent/child model agent within its assigned task.
- Supporting / enforcement mechanisms: tool schema validation, local file/shell/MCP transport, turn caps, retries, compaction and saved traces.
- Closure path: model action → tool invocation → ToolMessage → next model decision → deliverable/final answer.
- Boundary reachability: CLI `run` calls `run_local`; the packaged local runner constructs `FeatherAgent` for parent and children. No developer-only dogfood actor is borrowed.
- Why this is / is not agent-owned: removing the model leaves transport and caps but no task-specific discretionary next action.
- Evidence: [runner](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/core/runner.py#L305-L370), [local wiring](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/local/__init__.py#L107-L138).
- Basis: structural.
- Confidence: high.
- Caveats: source-backed availability, not an empirical claim of deliverable quality or long-run viability.

## S2 — Coordination

- State: A
- Function: prevent the operational team from overwriting shared deliverables or duplicating one another's work.
- Distinct S1 units: parent and independently executing child assignments, including multiple concurrent children.
- Inter-S1 disturbance: agents with separate histories/read revisions can edit the same shared file from incompatible prior versions; duplicated assignments can also consume effort on the same work.
- Attenuating coordination relation: injected parent guidance assigns allowed files and one assembling writer for a shared workbook/document/deck; child guidance preserves others' edits and prohibits writing files another agent is changing. The parent chooses these scopes and revises work through follow-ups/stop.
- Feedback into subsequent S1 behaviour: statuses/reports enter the parent's next model turn; follow-up assignments specify revised work. File tools return stale-read rejection into the offending agent's next turn.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the shipped guidance specifically addresses concurrent same-file interference, chooses exclusive assembly responsibilities and prohibits overlapping writes; this is additional to generic spawn/wait.
- Disturbance / variety regulated: shared-file ownership and stale views across distinct operational agents.
- Decisive decision or feedback right: choose who may write which deliverable and reconcile overlapping work before further changes.
- Decision owner: the autonomous parent agent; children apply their scoped instructions locally.
- Supporting / enforcement mechanisms: assignment/report tools, separate revision maps, stale-read checks. Guidance is not an atomic lock and shell writes can bypass file-tool checks.
- Closure path: assignment with allowed paths → child action/report → parent reconciliation/follow-up → subsequent scoped work; stale file-tool edits return an error requiring current evidence.
- Boundary reachability: `run_local` appends `PARENT_GUIDANCE`, supplies `CHILD_GUIDANCE` through `Subagents`, and exposes team tools in the supported production mode.
- Why this is / is not agent-owned: the model chooses the actual partition and corrective instruction; deterministic revision checking only rejects a preselected invalid write.
- Evidence: [coordination guidance](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/subagents.py#L20-L72), [parent wiring](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/local/__init__.py#L83-L90), [file-tool revision feedback](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/tools/files.py#L180-L227), [scripted shared-file test](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/tests/local/test_subagents.py#L200-L280).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a supported behavioral regulation path, not proof that every model follows it or that simultaneous shell writes are impossible. Single-agent mode has no inter-unit coordination demand.

## S3 — Inside-and-now control

- State: A
- Function: regulate current commitments of the task team and intervene when a child is unnecessary, incomplete or no longer useful to the whole deliverable.
- Whole-system current view: parent context plus `list_agents` statuses, selected `wait_agent` reports, failed/exhausted partial-work diagnostics and compacted team-state reminders.
- Current-control decision scope: decide active assignments, restrict scope/side effects, follow up on gaps, stop owned children and decide which completed work supports the overall result.
- Disturbance / variety regulated: incomplete/failed children, conflicting findings and currently active commitments competing for bounded concurrency.
- Decisive decision or feedback right: revise commitments and terminate a selected child after reviewing present team state; this goes beyond initial task decomposition.
- Decision owner: autonomous parent model.
- Supporting / enforcement mechanisms: configured max-concurrent/total/turn limits, status registry, cancellation and awaited resource cleanup. The host owns fixed ceilings; these are not themselves autonomous resource bargaining.
- Closure path: current reports/status → model selects follow-up/stop/new work → manager changes child lifecycle → results/status feed the next parent decision.
- Boundary reachability: standard production team exposes all five team tools to the parent and constructs children; [local runner](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/local/__init__.py#L130-L165) owns the manager lifetime.
- Why this is / is not agent-owned: removing parent discretion leaves fixed caps and automatic teardown, but no evidence-dependent choice of which commitment to revise or stop.
- Evidence: [model-facing team tools](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/tools/agents.py#L42-L90), [status/follow-up](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/subagents.py#L169-L225), [stop/cleanup](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/subagents.py#L244-L260), [parent responsibility](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/subagents.py#L29-L47).
- Basis: structural.
- Confidence: medium-high.
- Caveats: one local task team's current control, not organization-wide portfolio control or authority to change host ceilings. The noninteractive CLI and general embedding API supply no distinct function-specific human-parent mode.

## S3* — Complementary audit

- State: —
- Function: no material independent complementary audit path in the assessed task-team distribution.
- Disturbance / variety regulated: erroneous operational claims are handled by ordinary checks and parent result reconciliation.
- Decisive decision or feedback right: no separate audit judgment/feedback owner established.
- Decision owner: ordinary producing agents and parent remain responsible for QA.
- Supporting / enforcement mechanisms: execution traces, artifact reads and test tools provide observability.
- Closure path: routine checking stays in production; no independent audit-to-control loop is supplied.
- Why this is / is not agent-owned: a child can be asked to check work, but the generic assignment API supplies no specifically independent auditor role or complementary audit contract.
- Evidence: [subagent responsibility and reporting](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/docs/subagents.md), [adjacent grading](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-train/README.md), [external Harbor adapter](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-eval/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: a host can construct a different audited system.

### Absence scope

- Surfaces inspected: Harness loop/local/team tools and guidance, trace/result persistence, package map and Train/Eval documentation.
- Plausible first-party paths checked: parent reconciliation, separate child histories/raw-file reads, saved traces, isolated task graders and Harbor results.
- Why no material first-party path remains: runtime children are ordinary parent-owned assignments without a complementary audit-specific independence path; training/evaluation belongs to separately installed experiment systems and does not return independent audit judgment to this installed team's control.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped external-and-prospective adaptation loop at the local team boundary.
- Disturbance / variety regulated: web/source information and model/context issues are processed as current task work.
- Decisive decision or feedback right: no adaptation-options-to-current-capability decision path established.
- Decision owner: host selects configuration; producing model handles tasks.
- Supporting / enforcement mechanisms: optional web search/fetch, skills, compaction and separate training recipe.
- Closure path: source retrieval enters task context; no distinct prospective capability-regulation conversation is supplied.
- Why this is / is not agent-owned: generic research or model training alone does not establish S4.
- Evidence: [supported runtime composition](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/local/__init__.py), [Train's external recipe](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-train/README.md), [package separation](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/README.md).
- Basis: structural.
- Confidence: high.
- Caveats: future custom research assignments are not bounded absence counterexamples.

### Absence scope

- Surfaces inspected: CLI/local configuration, production/train modes, web tooling, compaction, subagent guidance and training/eval package interfaces.
- Plausible first-party paths checked: external research tools, skill selection, compaction summaries, Tinker rollout/grading/weight training and operator configuration.
- Why no material first-party path remains: task sensing and context preservation do not develop prospective organizational adaptation options; the separate externally launched training recipe does not close an S4-to-current-team loop, and no function-specific parent adaptation mode is wired into Harness.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy resolution loop established.
- Disturbance / variety regulated: task scope, source trust and host constraints are applied as preselected guidance.
- Decisive decision or feedback right: no identity-level case → legitimate ultimate authority → returned policy path supplied.
- Decision owner: host/user sets task and instructions; ordinary parent model controls current task work.
- Supporting / enforcement mechanisms: system guidance, profile validation, filesystem boundaries and configured limits.
- Closure path: constraints govern tools; no distinct ultimate-policy decision-return loop.
- Why this is / is not agent-owned: being the root task agent or accepting host instructions does not grant ultimate-policy authority.
- Evidence: [production guidance](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/production_prompt.md), [CLI config/run](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/src/feather_harness/cli.py#L28-L92), [supported embedding limits](https://github.com/paper-instruments/feather-train/blob/cdb5f34bad11c0c75ca4124b25a3e5da86bb62e2/feather-harness/docs/subagents.md).
- Basis: structural.
- Confidence: high.
- Caveats: an operator's ability to replace instructions is not itself function-specific parent governance.

### Absence scope

- Surfaces inspected: profiles/prompts, CLI/local/team composition, additional-instruction support and contributor/deployment documentation.
- Plausible first-party paths checked: task clarification, host guidance, team-parent authority, custom application hosting and maintainer release decisions.
- Why no material first-party path remains: all are task/configuration or adjacent development decisions; no supported identity/policy case routing and authoritative returned policy closure is shipped at this task-team recursion.

## Distributed OSS parent arrangement

The MIT repository's contributors maintain packages. No project-wide parent arrangement is imported into independently installed local teams. Parent in the subagent API means the producing model agent; it does not automatically imply a publication `P` mode.

## Self-hosted and non-human modes

The local CLI is a supported operator-configured mode. Human configuration supplies ceilings and credentials but no distinct closed S3/S4/S5 parent process. Generic host embeddings may create other systems and are not assigned ownership here.

## Recursion

Children have local task discretion and separate contexts but no complete local metasystem is established. Spawning alone does not establish recursive VSM viability.

## Variety and escalation

Tool feedback, bounded provider recovery, compaction and child partial reports preserve some operational distinctions. Parent assignments attenuate write conflicts and scope overlap. Turn/concurrency caps and automatic teardown enforce preselected limits; child failure need not cancel siblings. No distinct algedonic channel is established merely by failed/exhausted statuses.

## Evidence gaps

Source inspection establishes available first-party paths, not empirical reliability. No live provider, E2B, Tinker, Harbor or model-backed task was executed. Upstream deterministic tests and Index contract validation are reported in the owning batch receipt; tests use scripted responses and are not independent semantic assessment. The fixed source boundary is preserved.
