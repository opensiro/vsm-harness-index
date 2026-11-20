---
harness_id: marius-agent-harness
project_name: agent-harness (Marius-Juston)
repository: https://github.com/Marius-Juston/agent-harness
review_ref: 2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c
reviewed_at: 2026-11-20
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A(P)
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# agent-harness (Marius-Juston)

## Review boundary

- System in focus: the installed reusable agent-harness distribution for a multi-worker GitHub project, comprising Python devkit, Claude Code harness-ops plugin and Copier project template, NOT the other indexed `0xenzyme/agent-harness` (#534).
- Purpose and identity: maintain one measurable GitHub issue and PR ledger for model-backed leads and isolated worker subagents across machines, with separate source-aware code/research audit and exact-merge-tree acceptance.
- Relevant environment: changing source and CI, concurrent workers on GitHub, external model runtime, owner/project policies, issue and PR comments, quotas and source literature retrieved for tasks.
- Standard-distribution boundary: version-pinned `devkit/`, `plugins/harness-ops/`, `template/`; Claude Code CLI/model, GitHub service, optional literature APIs and downstream project logic are dependencies, not automatically the harness's own authority.
- Credited operating / distribution surfaces: `devkit/board.py`, `devkit/workflow.py`, `devkit/autopilot.py`, `plugins/harness-ops/skills/lead/SKILL.md`, `plugins/harness-ops/agents/{builder,tester,reviewer,research-auditor}.md`, `docs/specs/multi-agent.md`, template rules and pinned install scripts.
- Adjacent first-party surfaces excluded from ownership: original source repository's dogfood CI, experimental research scripts under `docs/research/_scratch/`, maintainer/release governance, illustrations, benchmark claims, and plugin-only configurations lacking required devkit integration.
- First-party operating / deployment modes considered: Claude lead+builder/tester/researcher worktree issue/PR loop; independently tasked reviewer and evidence auditor; separate machine leads sharing GitHub; owner budget/blocked-issue mode and optional trusted-review autopilot.
- Recursion level: one installed project team comprising several operational agent cells and an owner parent; no assumption of shared higher policy across unrelated installations.
- Reviewed revision: `2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c`.
- Observation date: 2026-11-20.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

`README.md` defines a three-part install: pinned Python `uv run dev` command, `harness-ops` plugin agents/skills/guards, and Copier template with project rules, CI and constraints. The lead is a model-backed Claude Code session; separate builder/tester/researcher/reviewer subagents execute one GitHub issue apiece in worktrees. Multi-machine coordination is exclusively shared GitHub issue/claim/PR state. `board next/wave` prioritizes unblocked issues with disjoint `Owns`; claims have an earliest-live-winner rule and stale recovery. The lead asks workers to implement, then `dev integrate` re-gates a merged tree against current main and routes failure to a worker. `harness-ops:reviewer` independently reads PR diff, issue DONE WHEN and test source, posting a SHA-bound verdict. `harness-ops:research-auditor` re-fetches sources rather than taking the researcher's summary on trust. Project owner sets objectives, priority and quota and handles explicit `needs owner` conditions. The runtime is the configured external Claude Code CLI, not a first-party model server.

Primary evidence: [README.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/README.md), [docs/specs/multi-agent.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/docs/specs/multi-agent.md), [devkit/board.py](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/devkit/board.py), [devkit/workflow.py](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/devkit/workflow.py), [plugins/harness-ops/skills/lead/SKILL.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/plugins/harness-ops/skills/lead/SKILL.md).

## Operational model

Model-backed workers own substantive code/research decisions (S1). The deterministic GitHub board and exclusive `Owns`+claims attenuate inter-worker interference (S2 constructor). A model lead chooses project-wide current work, dispatch, retries, integration, and human parent can decide whole-project budget and blocked interventions (S3 A(P)). A distinctly tasked read-only reviewer and independent research auditor challenge actual output with their own source inputs (S3* A). Source-retrieved papers are task input, not a continuous future intelligence function. Owner priority and tool permissions do not establish a resolved ultimate-policy issue for S5.

## S1 — Operations

- State: A
- Function: Execute one assigned code, test or literature research issue and return tangible source artifacts.
- Disturbance / variety regulated: Changing project APIs, failing tests, unexpected tool outputs and research findings.
- Decisive decision or feedback right: Model-backed worker chooses edits, tools, test hypotheses, research sources and response to specific review findings.
- Decision owner: Configured Claude Code builder, tester or researcher subagent executing the installed plugin prompt; the third-party model provides inference only.
- Supporting / enforcement mechanisms: Per-issue worktree, task brief, tool/secret guards, `dev test --affected`, `dev check`, PR check.
- Closure path: Worker commits, gates and creates an issue-linked PR; review/merge failure returns source-bound correction into the same issue/worker cycle.
- Boundary reachability: Template `dev setup` installs tagged devkit and plugin; lead calls supplied named subagents, requiring an authenticated external Claude Code install.
- Why this is / is not agent-owned: Static gates do not choose implementation/research actions, while model-backed installed worker does; no model-provider internals are credited.
- Evidence: [plugins/harness-ops/agents/builder.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/plugins/harness-ops/agents/builder.md); [devkit/board.py](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/devkit/board.py); [docs/specs/multi-agent.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/docs/specs/multi-agent.md); [README.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/README.md).
- Basis: structural
- Confidence: high for installed composition
- Caveats: Source-only; no live Claude model or downstream multi-machine execution verified.


## S2 — Coordination

- State: C
- Function: Attenuate simultaneous worker interference and competing issue claims across worktrees and machine-local leads.
- Disturbance / variety regulated: Two workers write overlapping `Owns` files, claim the same issue, or merge against a stale main.
- Decisive decision or feedback right: Admit a disjoint wave, reject duplicate claims and withhold/conflict-return work before integration.
- Decision owner: First-party deterministic devkit board/claim/wave and Git conflict logic; leads create scopes but do not autonomously change the anti-conflict policy.
- Supporting / enforcement mechanisms: GitHub claim comments, issue dependencies, path Owns checks, individual worktrees and merge conflict gates.
- Closure path: Conflicting tasks wait or withdrawn claims return to pool; completed/merged tasks release dependencies and rejected conflicting PRs return concrete repair directions.
- Boundary reachability: `dev board next/wave/claim` and `dev integrate` are shipped, invoked by standard lead skill on every project using all three distribution parts.
- Why this is / is not agent-owned: Inter-worker regulation is source-native but rules are deterministic rather than owned by an adapting S2-specific autonomous actor.
- Evidence: [devkit/board.py](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/devkit/board.py); [docs/specs/multi-agent.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/docs/specs/multi-agent.md); [devkit/workflow.py](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/devkit/workflow.py).
- Basis: structural
- Confidence: medium-high
- Caveats: `Owns` approximations do not mediate every resource; GitHub availability is external.
- Distinct S1 units: Separate builder/tester/researcher sessions and their independently claimed issues, including workers running on different machines.
- Inter-S1 disturbance: Simultaneous writes to shared repository paths and conflicting issue claims disrupt each other's delivery.
- Attenuating coordination relation: `board wave` excludes overlapping Owns against other in-progress/review work; earliest-live-claim ordering and merge-time checks prevent collisions.
- Feedback into subsequent S1 behaviour: Withheld workers are only dispatched once conflict/dependency clears; losing claims withdraw and incompatible PR heads receive worker-specific return notes.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: The decision suppresses actual cross-cell write/claim contention, rather than simply sequencing a workflow message.


## S3 — Inside-and-now control

- State: A(P)
- Function: Regulate the whole current project's backlog, agent allocation, review, integration and blocked/failed commitments.
- Disturbance / variety regulated: Concurrent priorities, stalled workers, failed CI, owner-required blockers, budget and quota exhaustion.
- Decisive decision or feedback right: Choose what to dispatch, return/re-review, pause, integrate, reprioritize or escalate across many issues.
- Decision owner: Model-backed project lead in base mode; legitimate human owner when resolving project-wide priorities/budget and blocked work in parent mode.
- Supporting / enforcement mechanisms: `dev status`, `dev orient`, `board next`, PR state, `dev autopilot`, HEAD-aware integrate, HANDOFF and quota cap.
- Closure path: Worker/reviewer state returns to lead, whose dispatch, rework, integrate and stop decisions modify board/PR/main; parent owner budget/priority resolutions change subsequent lead resource/commitment choices.
- Boundary reachability: Installed `/harness-ops:lead`, `continue` and `uv run dev` supply the operating loop and owner-blocker path without downstream custom control code.
- Why this is / is not agent-owned: Lead discretion concerns whole current commitments, not deterministic scheduling; parent mode has distinct owner authority over project-wide resource constraints, not generic tool approval.
- Evidence: [plugins/harness-ops/skills/lead/SKILL.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/plugins/harness-ops/skills/lead/SKILL.md); [docs/specs/multi-agent.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/docs/specs/multi-agent.md); [devkit/board.py](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/devkit/board.py); [devkit/workflow.py](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/devkit/workflow.py).
- Basis: structural; explicit protocol
- Confidence: medium
- Caveats: Human tool permission alone does not establish parent S3; only binding project-wide owner decisions considered.
- Whole-system current view: Lead reads open/current review issues, ranked ready work, live claims, quota budget and handoff across all project workers.
- Current-control decision scope: Lead can reorganize issue priority, worker assignments, integration and return of failed work across the project.
| Mode | Decisive owner | Trigger | Closure | Evidence |
| --- | --- | --- | --- | --- |
| Base (`A`) | Model lead | New ready/blocked/review issues | Dispatch, return, integrate, change next work across project | `skills/lead/SKILL.md` |
| Parent (`P`) | Human project owner | Project-wide budget, priority conflict or `needs owner` | Owner updates governing budget/commitment and lead resumes or stops | `docs/specs/multi-agent.md` |

## S3* — Complementary audit

- State: A
- Function: Challenge worker claims against independently inspected Git diff/issue evidence or research sources before integration.
- Disturbance / variety regulated: Plausible but faulty worker patch, missed DONE WHEN requirement, unsubstantiated note claim or weakened test.
- Decisive decision or feedback right: Substantively accept/reject source or research evidence and issue specific blocking findings with a commit-bound verdict.
- Decision owner: Distinct installed model-backed read-only reviewer and research-auditor subagents rather than worker or deterministic gate.
- Supporting / enforcement mechanisms: Diff/commit SHA, quoted review verdict, own issue DONE WHEN, authoritative source retrieval, first-line trusted verdict, bounded rework rounds.
- Closure path: Reviewer findings enter PR/lead review; Blocking returns worker for fix and new SHA, success plus gate allows integrate; after repeated failures owner gets blocker.
- Boundary reachability: Standard plugin installs both specialized review roles and lead invokes them for user-facing/risky PRs and decision-driving research.
- Why this is / is not agent-owned: Audit actor separately reads raw source/evidence and decides substantive defects; CI and gate alone only check predefined commands.
- Evidence: [plugins/harness-ops/agents/reviewer.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/plugins/harness-ops/agents/reviewer.md); [plugins/harness-ops/agents/research-auditor.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/plugins/harness-ops/agents/research-auditor.md); [plugins/harness-ops/skills/lead/SKILL.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/plugins/harness-ops/skills/lead/SKILL.md); [devkit/workflow.py](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/devkit/workflow.py).
- Basis: structural
- Confidence: medium-high
- Caveats: Reviewer is conditional, no independent empirical quality benchmark, model family can match builder.
- Claim being audited: Issue-linked worker claims completed implementation/research is correct, safe and merge-ready.
- Ordinary reporting path: Worker `dev pr` summary, `dev check` gate and GitHub issue task status.
- Complementary access path: Reviewer reads actual `gh pr diff` and issue + tests, research-auditor re-fetches cited sources and actively seeks contradictory material.
- Independence boundary: Dedicated read-only actor cannot edit worker artifact, reviewers are separately tasked and SHA-bound, not a self-reported worker conclusion.
- Who acts on findings: Lead and `dev integrate` return Blocking findings to worker with exact PR feedback, or allow reviewed PR after all checks.


## S4 — Outside-and-then intelligence

- State: —
- Function: No distinct installed prospective external intelligence process for adapting the organization to future environment was established.
- Disturbance / variety regulated: Future external scientific, provider, market or operational changes demanding changes to current team capability.
- Decisive decision or feedback right: Would require choosing a future-oriented adaptation from external signals and returning it into current control; no such first-party right is shown.
- Decision owner: No dedicated in-boundary S4 owner; research workers own task-level literature retrieval, architect checks internal code architecture.
- Supporting / enforcement mechanisms: Literature tools, indexed notes and internal consolidation supply task evidence or internal improvement rather than horizon management.
- Closure path: No externally sensed future possibility → proactive choice → present capability adaptation feedback is evidenced.
- Why this is / is not agent-owned: Web-enabled task research is S1; codebase consolidation evaluates current internal structure and lacks future-environment return.
- Evidence: [docs/specs/multi-agent.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/docs/specs/multi-agent.md); [plugins/harness-ops/skills/research/SKILL.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/plugins/harness-ops/skills/research/SKILL.md); [devkit/consolidation.py](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/devkit/consolidation.py).
- Basis: bounded source absence
- Confidence: medium
- Caveats: A user could author future-oriented research issues, but that does not install an ongoing S4 loop.
### Absence scope

- Surfaces inspected: installed lead, researcher, auditor, architect, research and consolidation commands and project policy/template.
- Plausible first-party paths checked: scholarly literature retrieval, adversarial note audit, architecture consolidation and user-created research tasks.
- Why no material first-party path remains: each selected path is present task evidence or internal audit, not externally driven future adaptation with organizational feedback.


## S5 — Policy and identity

- State: —
- Function: No source-native ultimate organizational identity/policy issue resolution and binding return was demonstrated at local project-team recursion.
- Disturbance / variety regulated: Identity/purpose conflict between current delivery and future direction, beyond an issue's scope or immediate resource quota.
- Decisive decision or feedback right: Would determine ultimate purpose/policy in response to an identity-level issue and govern later S3/S4.
- Decision owner: Human user sets project brief and quotas, but no first-party S5 issue and ultimate-authority transaction is supplied.
- Supporting / enforcement mechanisms: CLAUDE/project rules, decisions files, board owner blockers and permission guards regulate present tasks.
- Closure path: No distinct identity/policy issue → final authority ruling → binding updated team mission feedback is evidenced.
- Why this is / is not agent-owned: Tool permissions, PR merge approval or human-set budget do not constitute an ultimate-policy loop.
- Evidence: [docs/specs/multi-agent.md](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/docs/specs/multi-agent.md); [template/.devkit/HARNESS.md.jinja](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/template/.devkit/HARNESS.md.jinja); [devkit/rules.py](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/devkit/rules.py); [devkit/board.py](https://github.com/Marius-Juston/agent-harness/blob/2c07a9c07da73bc8c981680a5c08fe9d8ed25f8c/devkit/board.py).
- Basis: bounded source absence
- Confidence: medium
- Caveats: An adopting enterprise may independently implement S5; its governance cannot be credited to this generic installation.
### Absence scope

- Surfaces inspected: owner roles, issue priorities, quota cap, project/Claude policies, review and merge permissions and adjacent OSS governance.
- Plausible first-party paths checked: `needs owner` issue escalation, owner brief, budget override, rule/decision files and GitHub review.
- Why no material first-party path remains: none performs a triggered identity-policy ultimate ruling with binding return to current and prospective system functions.


## Distributed OSS parent arrangement

The parent is the local adopting project owner, not the GitHub maintainer collective. Separate installations share no policy state or S5 authority by default.

## Self-hosted and non-human modes

The template may run cross-machine leads sharing GitHub and unattended worker/PR loops via external Claude Code. Parent budget/priority decisions are S3-specific; plugin-only use lacks all standard devkit controls.

## Recursion

The installed team has worker S1 units, anti-conflict S2, lead and owner current S3, complementary diff and research S3*; no confirmed S4/S5 at this recursion.

## Variety and escalation

Source ambiguity goes to workers; issue/Owns contention to board policy; current workload and failed gates to lead; findings to separate auditors and fix loops; budget/reconsider to owner.

## Evidence gaps

Pinned source and bundled protocol only: no provider execution, authenticated GH account, independent model-provider audit or multi-machine race test. This project is distinct from the existing `0xenzyme/agent-harness` canonical entry. Negative claims are scoped to installed generic distribution, not hypothetical external extensions.
