---
harness_id: emrg
project_name: EMRG
repository: https://github.com/argszero/emrg
review_ref: cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8
reviewed_at: 2026-11-19
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: P
autonomy_s5: ?
---

# EMRG

## Review boundary

- System in focus: One installed EMRG personal-agent service with supported scheduled self-evolution, host task controls and released-capability upgrade mode.
- Purpose and identity: Perform user coding/work tasks and improve the reusable agent capability under host authority and published release boundaries.
- Relevant environment: User projects and feedback, competing tools/community changes, source/release repositories, model/tool failures, host resources and installation state.
- Standard-distribution boundary: Installed daemon, client protocol, model/tool/session loop, scheduled evolution template and exact-head review instruments, host task controls, UpgradeManager and upgrade-agent template. The separate public developer organization is not automatically included.
- Credited operating / distribution surfaces: Packaged interactive/headless tool loop, task scheduler and evolution workspace registration, shipped evolution prompt and review-specific scripts, task list/update/trigger controls, released-version sensing and agent-driven local installation.
- Adjacent first-party surfaces excluded from ownership: Standalone repository CI/build execution and historical cycle/rant anecdotes cannot donate runtime owners. The source checkout is credited only through the installed self-evolution task and upgrade bindings. External contributors/reviewers, GitHub permissions, model providers and release publishing authority remain separately bounded.
- First-party operating / deployment modes considered: Interactive Ask/Auto and sandbox tiers; supported enabled scheduled evolution on the registered emrg workspace, contributor versus committer GitHub rights; host task configuration and released-upgrade mode (enabled/delay configurable). Fresh installs seed an evolution task; deleting an existing task is respected.
- Recursion level: One deployed harness instance; nested execution is not presumed recursively viable.
- Reviewed revision: cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8
- Observation date: 2026-11-19
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The daemon streams model/tool turns with persisted sessions and context; tools return results until the model finishes or limits/cancellation intervene. Scheduled tasks render packaged templates and invoke that same daemon loop. The self-evolution template reads user rants, community/source/competitor evidence, develops changes, verifies them and submits/reviews source PRs within actual GitHub rights. Exact-head vote and merge instruments make source review reconstructable. Tasks are independent handlers whose live records are read at wake boundaries. A distinct UpgradeManager senses eligible published releases and starts an upgrade agent, which chooses installation/dependency actions and verification/rollback for the live product. Source proposal, release acceptance and installed effect are distinct stages.

## Operational model

Interactive tool-using agents and scheduled task cells produce outcomes. Host task controls regulate current service commitments. Dedicated evolution review instruments are audit-specific constructors, but cycle-tag distinctness is not claimed as independent judgment: a task uses a fixed persisted session. Future capability options from external evidence are proposed by evolution; the supported released-upgrade chain leaves publication/adoption authority with the legitimate human/release parent.

## S1 — Operations

- State: A
- Function: Execute user and scheduled work through discretionary model-selected tools.
- Disturbance / variety regulated: Unknown project state, tool/provider errors and multi-step coding/research tasks.
- Decisive decision or feedback right: Choose tool calls and revisions from observations; finish or continue a task.
- Decision owner: Configured model actor in the first-party daemon tool loop.
- Supporting / enforcement mechanisms: Tool registry, persisted Session, streaming provider interface, sandbox roots/tiers, bounded rounds and cancellation.
- Closure path: Daemon sends history/tools to the model, executes requested tools, stores results and repeats; scheduled evolution invokes this same loop through the task protocol.
- Why this is / is not agent-owned: Tool selection and work changes are model-discretionary; storage, sandbox and transport alone cannot produce the task solution.
- Evidence: [README.md](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/README.md); [emrg/server/daemon.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/daemon.py); [emrg/server/scheduler.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/scheduler.py); [emrg/session.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/session.py); [emrg/tools/registry.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/tools/registry.py); [emrg/tools/subagent_tool.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/tools/subagent_tool.py)
- Basis: structural
- Confidence: high
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.
- Boundary reachability: Interactive task requests and TaskHandler._run_evolution_cycle both enter the installed daemon; the loop is implemented in _run_tool_loop, not borrowed from another harness.

## S2 — Coordination

- State: —
- Function: No concrete inter-S1 disturbance-specific coordination loop established at the installation boundary.
- Disturbance / variety regulated: Potential interference among independent task cells sharing host or source resources.
- Decisive decision or feedback right: No function-specific decisive organizational right is established in the inspected supported modes.
- Decision owner: No qualifying owner for this function; narrower runtime/developer/operator decisions remain with their actual actors.
- Supporting / enforcement mechanisms: Independent task handlers, per-session queuing, child-session slots, serialized child delegation and dirty-tree recovery.
- Closure path: No function-specific returned decision changing subsequent regulation is established.
- Why this is / is not agent-owned: Session/slot lifecycle prevents local execution/state errors; generic scheduling or one-child-at-a-time delegation does not establish a specific inter-unit mutual coordination decision. Dirty-tree recovery preserves data but does not identify another S1 owner and negotiate conflicting work.
- Evidence: [README.md](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/README.md); [emrg/server/daemon.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/daemon.py); [emrg/server/scheduler.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/scheduler.py); [emrg/tools/subagent_tool.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/tools/subagent_tool.py); [emrg/server/atomic.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/atomic.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.

### Absence scope

- Surfaces inspected: [README.md](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/README.md); [emrg/server/daemon.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/daemon.py); [emrg/server/scheduler.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/scheduler.py); [emrg/tools/subagent_tool.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/tools/subagent_tool.py); [emrg/server/atomic.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/atomic.py); supported-mode documentation and relevant configuration/test wiring.
- Plausible first-party paths checked: Independent scheduler handlers, task/source registration, per-session queuing, child slots, dirty-tree convergence and PR merge-race guidance.
- Why no material first-party path remains: No shipped relation ties an identified inter-S1 collision/oscillation to a function-specific coordination choice and feedback. Arbitrary future source locks or prompt-authored coordination cannot donate C; community PR review remains the separately analyzed audit/adaptation interface.

## S3 — Inside-and-now control

- State: P
- Function: Regulate the installation current scheduled/interactive work commitments and operating cadence.
- Disturbance / variety regulated: Multiple active sessions/tasks compete for host attention and model/tool resources; work can be stale, overactive or no longer wanted.
- Decisive decision or feedback right: Inspect the whole task/session portfolio, enable/disable or retime work, trigger selected work and interrupt current activity.
- Decision owner: The legitimate local human host through the shipped client/daemon control protocol.
- Supporting / enforcement mechanisms: list_tasks/list_all_sessions, task_update/create/delete/trigger, task status/runs, usage records, scheduler reconcile and boundary refresh.
- Closure path: The daemon persists host task edits; handlers read their live records at wake boundaries and reconciliation starts missing enabled handlers without rewriting active cycles. User cancellation interrupts actual sessions.
- Why this is / is not agent-owned: The host chooses current portfolio/cadence interventions; deterministic handlers only implement those choices. The evolution prompt reserves tasks.yml to the host, so autonomous schedule control is not inferred.
- Evidence: [README.md](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/README.md); [emrg/server/daemon.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/daemon.py); [emrg/server/scheduler.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/scheduler.py); [emrg/server/usage_ledger.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/usage_ledger.py); [emrg/server/evolution_prompt.md](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/evolution_prompt.md)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.
- Whole-system current view: Installation-wide task status/run summaries and all sessions, with activity/usage information; this is broader than one agent child-task list.
- Current-control decision scope: Current work commitments, enabled task portfolio, schedule/interval and manual intervention on behalf of the installation.
- Boundary reachability: The deployed daemon exposes task-list/update/trigger and all-session protocol handlers used by the client; the same TaskScheduler owns current handlers and effective records.

## S3* — Complementary audit

- State: C
- Function: Construct complementary source review that can challenge evolution PR readiness and block acceptance.
- Disturbance / variety regulated: A producer success claim/green local tests can conceal a defect or mismatch between reviewed head and prospective merge tree.
- Decisive decision or feedback right: Supply sufficiently independent reviewer judgment from raw code, causal tests and actual merge-tree/head evidence, then bind findings to acceptance.
- Decision owner: Reviewer actors/independence and lawful committer authority must be composed; scripts count/enforce evidence and do not own audit judgment.
- Supporting / enforcement mechanisms: Evolution review/abstention procedure, review-queue, exact-head vote counting, merge freshness and merge-plan suite checks.
- Closure path: Reviewer findings/veto reset the acceptance streak; head changes void earlier votes; qualified acceptance or demanded fixes affect subsequent source work. Installation/release effects remain a separate chain.
- Why this is / is not agent-owned: The repository exposes an audit-specific raw-evidence/judgment/return protocol. A different cycle ID in the fixed retained task session is insufficient to assert installed independent A ownership; a genuine independent reviewer/authority remains a composition requirement.
- Evidence: [emrg/server/evolution_prompt.md](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/evolution_prompt.md); [emrg/server/scheduler.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/scheduler.py); [scripts/review-queue.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/scripts/review-queue.py); [scripts/check-vote-count.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/scripts/check-vote-count.py); [scripts/check-merge-freshness.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/scripts/check-merge-freshness.py); [scripts/check-merge-plan-suite.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/scripts/check-merge-plan-suite.py)
- Basis: structural
- Confidence: medium
- Caveats: Bounded source inspection at the exact revision; no provider-backed runtime experiment or independent secondary semantic review was performed.
- Claim being audited: An evolution PR is substantively sound and its actual accepted head/merge tree meets the intended change.
- Ordinary reporting path: Producing cycle completion summary and its routine local checks/PR report.
- Complementary access path: Reviewer checks out actual source and prospective merge tree, reads discussions and probes tests/causes, rather than voting on the producer summary alone.
- Independence boundary: Must be supplied beyond cycle identifiers: the default task has a fixed persisted session, and later cycles can revisit prior authored PRs. No independent live reviewer is claimed here.
- Who acts on findings: Lawful committer/evolution acceptance path; veto demands changes and prevents eligible merge until resolved.
- Boundary reachability: The packaged scheduler renders evolution_prompt, which directs use of these supplied review-specific scripts and source checkout in the self-evolution workspace. C is conditional on actual independent reviewers and GitHub rights, not every default cycle.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adapt reusable EMRG capability from external user/community/competitor distinctions through a parent-governed source-release-install chain.
- Disturbance / variety regulated: Changing user needs and alternative-tool capabilities can make current agent capability inadequate for future work.
- Decisive decision or feedback right: Develop/select reusable capability options and lawfully accept a released option for installation; final release/adoption authority is retained at the human/release parent.
- Decision owner: Parent-governed arrangement: evolution model develops options; legitimate release/host authority accepts publication/adoption; the upgrade agent implements and verifies the returned released target.
- Supporting / enforcement mechanisms: Rant/issue/competitor sensing in evolution template, source changes and tests/reviews, release boundary, configured update eligibility/delay, UpgradeManager and isolated upgrade-agent workspace.
- Closure path: External distinctions become capability proposals/source changes; lawful release acceptance returns as a published eligible target. UpgradeManager starts the configured upgrade actor, which reads the target source, updates the live installation and verifies or rolls back. Unmerged/unreleased source work alone does not close the installed effect.
- Why this is / is not agent-owned: The model has real option-generation and installation discretion, but no autonomous release authority is inferred. The credited end-to-end installed adaptation mode retains a legitimate parent release/adoption decision; no A/C base is claimed merely from self-improvement naming.
- Evidence: [README.md](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/README.md); [emrg/server/daemon.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/daemon.py); [emrg/server/scheduler.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/scheduler.py); [Agent.md](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/Agent.md); [emrg/server/evolution_prompt.md](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/evolution_prompt.md); [emrg/server/rants.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/rants.py); [emrg/server/upgrade.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/upgrade.py); [emrg/server/prompts/upgrade_prompt.j2](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/prompts/upgrade_prompt.j2); [emrg/config.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/config.py)
- Basis: structural
- Confidence: medium
- Caveats: This is a source-traced supported parent-governed capability, not evidence that any particular release was produced or installed by this assessment. Contributor-only source proposals and disabled updates do not establish the full loop.
- External distinction: Host dissatisfaction across user projects, community issues and changing competitor releases/features inform capability gaps.
- Future / prospective distinction: Evolution considers reusable methods/tools/features missing from EMRG, beyond solving the triggering task once.
- Adaptation option generated: Proposed changes to agent tools, prompts or reusable implementation, reviewed as source changes and accepted through the released-target boundary.
- Path back into current capability / S3: Published accepted target → configured update eligibility → upgrade-agent session → live installation/dependencies and verification/rollback; host task/installation operation then uses that capability.
- Boundary reachability: TaskScheduler seeds/registers the emrg evolution workspace and runs the packaged external-sensing template; the daemon separately wires UpgradeManager to _run_upgrade_session and the live install. This is supported self-evolution/upgrade mode, not solely development dogfood.

## S5 — Policy and identity

- State: ?
- Function: Potential host closure of identity/lineage and ultimate-policy matters remains unresolved.
- Disturbance / variety regulated: Manifesto-described major lineage divergence or policy tensions between service and self-evolution.
- Decisive decision or feedback right: Unresolved runtime routing and authoritative return of a host identity/policy decision in scheduled evolution mode.
- Decision owner: Manifesto assigns legitimate human host/community authority, but effective function-specific runtime closure is not established by the inspected source.
- Supporting / enforcement mechanisms: Manifesto/embedded service principles, host attribution rules, ordinary client conversations and per-call sandbox approval future.
- Closure path: Tool-level approval demonstrably widens only one call. The source did not establish that a lineage/policy proposal reaches host authority and returns as binding subsequent evolution policy.
- Why this is / is not agent-owned: A constitution, human-reserved rights and generic approval channel do not alone prove S5=P; the explicit lineage/policy candidate prevents a defensible absence conclusion without resolving its return path.
- Evidence: [MANIFESTO.md](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/MANIFESTO.md); [emrg/server/prompts/system.j2](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/prompts/system.j2); [emrg/server/evolution_prompt.md](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/evolution_prompt.md); [emrg/server/daemon.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/server/daemon.py); [emrg/sandbox/escalation.py](https://github.com/argszero/emrg/blob/cd30b38e33c0b12765df5d1bf5e0ec5228d1d9b8/emrg/sandbox/escalation.py)
- Basis: structural
- Confidence: low
- Caveats: Specific unresolved S5 candidate, not a positive grade or an invitation to infer P from sandbox permission. Scheduled headless sessions may lack a subscribed host.

## Distributed OSS parent arrangement

The local self-evolution installation is the assessed recursion. Public repository maintenance is adjacent except for the explicitly packaged source-review/release-input interfaces. Three cycle votes do not prove three independent actors or organization-level autonomy; actual GitHub and release authority must be supplied.

## Self-hosted and non-human modes

A host can inspect all sessions/tasks, change enabled work and cadence, trigger work and interrupt activity. Contributor/committer permissions are material: an installation cannot assume source merge or release rights. The supported parent-governed adaptation mode requires lawful release acceptance followed by the configured local upgrade path, rather than treating an unmerged PR as changed installed capability.

## Recursion

No claim of recursively complete VSM units is made. Execution phases, provider instances and nested calls do not establish recursive viability.

## Variety and escalation

Tool results and errors regulate local action; task status and usage expose current load to the host. Scheduled workers can park pending CI and return next cycle. Tool sandbox escalation uses a real subscriber approval future and fails closed when nobody answers, but it is a per-call permission decision, not automatically S5. Upgrade failure can return to backup/retry within its released-version target.

## Evidence gaps

No live model, GitHub publication, release, install/upgrade or host-policy experiment was run. A source PR or changed evolution checkout is not a verified change to the running installation. S3* is C because independent reviewer judgment/context and authority still need composition beyond cycle IDs. S5 remains ? specifically because the manifesto describes host-confirmed lineage/policy decisions but source tracing does not establish a function-specific returned authority loop in the headless scheduled mode; the wired sandbox approval path decides only a tool call.
