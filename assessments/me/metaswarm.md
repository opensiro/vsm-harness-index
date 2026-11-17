---
harness_id: metaswarm
project_name: metaswarm
repository: https://github.com/dsifry/metaswarm
review_ref: 4bbb10abd301b9ec9d63371e296049cbc6043baa
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: A
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: P
autonomy_s5: —
---

# metaswarm

## Review boundary

- System in focus: One installed metaswarm command/skill/agent plugin in a host coding-agent CLI (Claude Code, Codex, Gemini or comparable supported mode) operating within a project and its worktrees, issues and project-local knowledge base, not the entire generic host CLI.
- Purpose and identity: Coordinate an agentic software development workflow from issue through planning, reviewed parallel work units, PR shepherding, merge and retained learning.
- Relevant environment: GitHub issue/PR comments, human approval, filesystem/worktrees, tests and CI, BEADS task status, external coding-agent host APIs, independent reviewers and project knowledge.
- Standard-distribution boundary: Shipped installable metaswarm commands, role definitions, skills, governance instructions, CLI setup, review rubrics and small shell/JS helpers. Host `Task`/`TeamCreate`/LLM provider and OS/Git/BEADS tools are execution dependencies. Their generalized intelligence is not credited beyond following metaswarm's supplied specific orchestration instructions.
- Credited operating / distribution surfaces: [cli/metaswarm.js](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/cli/metaswarm.js), [skills/start/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/start/SKILL.md), [skills/orchestrated-execution/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/orchestrated-execution/SKILL.md), [agents/swarm-coordinator-agent.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/agents/swarm-coordinator-agent.md), [agents/issue-orchestrator.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/agents/issue-orchestrator.md), [commands/self-reflect.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/commands/self-reflect.md), [commands/prime.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/commands/prime.md), [skills/orchestrated-execution/guides/agent-coordination.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/orchestrated-execution/guides/agent-coordination.md) in installed plugin/task mode.
- Adjacent first-party surfaces excluded from ownership: `tests/`, `evals/`, examples/templates not yet installed, repository's own CI and release tooling, dogfood assertions and maintainer policies. Evidence from these surfaces informs plausible reachability but does not by itself close a deployed organization function.
- First-party operating / deployment modes considered: Plugin installed into a configured host; default Task-mode fresh subagent spawning; Team mode only where host exposes TeamCreate/SendMessage; parallel worktree/Issue orchestrator mode; human approval/clarification checkpoints; project knowledge-base self-reflection and priming.
- Recursion level: A project-level orchestration cell with multiple independent implementer/task agents and a meta-orchestrator spanning issues/worktrees. An unrelated repository's governance, coding host platform and the broader metaswarm maintainer organization are not collapsed into this cell.
- Reviewed revision: `4bbb10abd301b9ec9d63371e296049cbc6043baa`, frozen original public main; no repin.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

metaswarm is primarily an installable **agent workflow contract**, not a bespoke LLM inference server. Its Node CLI installs plugin/skills for supported coding hosts, and its source-shipped `skills/start`, `skills/orchestrated-execution`, role files and review rubrics instruct the host model and its subagents to complete issue-level work. The documented flow has planned work units, independent implementation branches/worktrees, plan and design review, validation by the orchestrator, fresh adversarial reviewers, bounded retries, merges and human pause/escalation. `.beads` retains work plans, review history and knowledge; commands self-reflect and prime act on project-owned JSONL knowledge entries. Host APIs and external review providers are required at runtime but the precise role-specific organizational decision paths are authored in metaswarm. Source: [README.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/README.md), [cli/metaswarm.js](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/cli/metaswarm.js), [skills/start/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/start/SKILL.md), [skills/orchestrated-execution/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/orchestrated-execution/SKILL.md), [skills/plan-review-gate/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/plan-review-gate/SKILL.md), [skills/orchestrated-execution/guides/agent-coordination.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/orchestrated-execution/guides/agent-coordination.md).

## Operational model

The installed orchestration skill has a planner and one or more coding subagents turn an issue into independent work units, demand validation and adversarial review, feed failure reports back into subsequent implementation attempts, and constrain merge progression. A swarm coordinator can track active issues, worktrees, conflicting file scopes and blocked agents; it assigns or rebalances work based on priority and available capacity. The first-party instructions include explicit human stop points and escalation, distinct from agent-owned decisions in routine work. Model judgment happens in host-executed agents **using first-party packaged role/skill contracts**; generic host tooling itself is not donated as S2/S3/S4 ownership. Knowledge reflection is human-selected and written to project files, then selectively loaded at the beginning of subsequent tasks.


## S1 — Operations
- State: A
- Function: Execute model-mediated research, coding, tests, review responses and PR delivery for project work units.
- Disturbance / variety regulated: Evolving source code and tests, issue requirements, review feedback, setup errors and implementation uncertainties.
- Decisive decision or feedback right: A coder/model agent chooses implementation changes and tool calls to meet the specific work unit definition and revises them in response to validator/reviewer feedback.
- Decision owner: Installed host model-backed coder/issue agent executing the published metaswarm role/skill instructions, not the installer or static shell scripts.
- Supporting / enforcement mechanisms: Work-unit plan, BEADS records, Git worktrees, subprocess tooling, run state, tests and CLI integration.
- Closure path: Agent changes code, receives independent validation/review, iterates or escalates, and commits an accepted implementation/PR.
- Boundary reachability: The installed `start` and orchestrated-execution skill explicitly binds an issue workflow to coding `Task()` roles and host tool calls; agent role payloads are part of the distributed plugin.
- Why this is / is not agent-owned: Operational code-writing decisions are made by model-backed workers following source-shipped role requirements; ordinary Git and host API execution support their choices.
- Evidence: [skills/start/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/start/SKILL.md), [skills/orchestrated-execution/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/orchestrated-execution/SKILL.md), [agents/coder.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/agents/coder.md), [cli/metaswarm.js](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/cli/metaswarm.js), [skills/start/references/codex-tools.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/start/references/codex-tools.md)
- Basis: structural first-party shipped workflow and role contracts
- Confidence: medium-high for configured installed mode
- Caveats: No actual host model session or external CLI execution in this source-only assessment.


## S2 — Coordination
- State: A
- Function: Attenuate identifiable write-surface and dependency interference between distinct parallel agent work units.
- Disturbance / variety regulated: Two independent agents can modify overlapping files/migrations, spawn conflicting branches, depend on unmerged work or overload shared worktree capacity.
- Decisive decision or feedback right: Swarm/issue coordinator judges file-scope and dependency conflicts, chooses to move, rebalance, serialize, pause or re-plan work, and transmits the resulting instructions/priority to affected agents.
- Decision owner: Model-backed swarm coordinator in the shipped role and issue-orchestrator process; deterministic Git/BEADS tools persist the selected changes and validation gates.
- Supporting / enforcement mechanisms: Per-worktree assignments/conflict registry, `Task`/Team messaging and work-unit dependencies, plan review gate, branch collision tests and integration validation.
- Closure path: Coordinator detects competing file/schema scope or unmet dependency, instructs subagents/revises the plan and allows dependent work only when prerequisites are complete; later work units obey revised ownership/sequence.
- Boundary reachability: The plugin exposes swarm-coordinator agent role and shipped `start`/orchestrated execution skills in standard host task mode; prompts specify exact task assignment, conflict detection and returned operational commands.
- Why this is / is not agent-owned: The credited witness is role-directed conflict judgment and redistribution, not mere parallel spawning or message passing.
- Evidence: [agents/swarm-coordinator-agent.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/agents/swarm-coordinator-agent.md), [agents/issue-orchestrator.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/agents/issue-orchestrator.md), [skills/orchestrated-execution/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/orchestrated-execution/SKILL.md), [skills/orchestrated-execution/guides/agent-coordination.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/orchestrated-execution/guides/agent-coordination.md), [skills/plan-review-gate/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/plan-review-gate/SKILL.md)
- Basis: explicit first-party role decision authority and conflict-specific workflow path
- Confidence: medium
- Caveats: Depends on configured host Task/Team tools and project-level worktree tracking; the docs are an operational contract rather than an independently observed concurrent run.
- Distinct S1 units: Two or more coding subagents working on separate PR slices/issues in different worktrees under the same project orchestrator.
- Inter-S1 disturbance: Overlapping file edits, schema changes or missing cross-branch dependency create merge/integration conflicts or block a sibling agent.
- Attenuating coordination relation: First-party coordinator detects file/dependency overlaps; it may serialize, reassign worktree ownership, pause lower-priority work or broadcast conflicts; the plan gate rejects unsafe concurrent scopes.
- Feedback into subsequent S1 behaviour: Remediation is sent to affected issue orchestrators/coders and changes subsequent assignment, worktree or wave execution before integration.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Specific structurally modeled cross-agent source/migration collisions and corrective work redistribution exist, not only message envelopes.


## S3 — Inside-and-now control
- State: A
- Function: Manage current multi-issue fleet commitments, worktree capacity, priorities, active failures and escalation across the project.
- Disturbance / variety regulated: Worktree saturation, active agent failure, urgent P0/P1 issues displacing lower-priority work, unresolvable conflicts and delayed delivery.
- Decisive decision or feedback right: Swarm coordinator can assign issues/worktrees, rebalance work, pause lower-priority work, spawn issue orchestrators and escalate problems beyond its authority.
- Decision owner: Model-backed deployed swarm coordinator role under metaswarm instruction/host tooling, in its supported multi-issue orchestration mode; not a mere deterministic status counter.
- Supporting / enforcement mechanisms: Active assignments registry, worktree status, conflict registry, BEADS task status, agent heartbeats and host task orchestration.
- Closure path: Coordinator reads present fleet state, chooses intervention and sends commands/revised task assignments to issue orchestrators; subsequent active agent work changes or waits for parent.
- Boundary reachability: The shipped plugin role is installed and exposed through host-model invocation; the role's Decision Authority and Task/Team coordination mode supply the current-control return path for the project cell.
- Why this is / is not agent-owned: Coordinator is explicitly granted discretionary resource/priority decisions; monitoring registries only report current facts and do not own these choices.
- Evidence: [agents/swarm-coordinator-agent.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/agents/swarm-coordinator-agent.md), [skills/start/agents/swarm-coordinator-agent.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/start/agents/swarm-coordinator-agent.md), [skills/start/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/start/SKILL.md), [skills/orchestrated-execution/guides/agent-coordination.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/orchestrated-execution/guides/agent-coordination.md)
- Basis: explicit first-party role authority and operational workflow
- Confidence: medium
- Caveats: Conditional role activation in configured multi-issue mode; no live whole-project run observed. Human checkpoints are specific task gates and are not independently credited as a whole-system S3 parent mode.
- Whole-system current view: Active GitHub Issues/BEADS epics, worktree utilization/assignments, conflict registry, heartbeats and blocked/failing agent state are specified coordinator inputs.
- Current-control decision scope: Assignment, shared capacity, prioritization, pausing and rebalancing live work, with return via Task/Team messages and tracked worktree files.


## S3* — Complementary audit
- State: A
- Function: Independently falsify implementer assertions using actual diffs, tests and independent assessment of each work-unit specification.
- Disturbance / variety regulated: Implementer hallucination, self-certification, incomplete or defective code, and review anchoring across retries.
- Decisive decision or feedback right: Fresh independent adversarial-review agent judges PASS/FAIL against work-unit spec and code evidence; orchestrator performs separate validation and adjudicates bounded retry/escalation.
- Decision owner: New model-backed `adversarial-reviewer` per work unit/round; not implementer and not deterministic test runner.
- Supporting / enforcement mechanisms: Spec/DoD, direct Git diff and tests, review rubric, attempt history, forced fresh-instance rule, gated commit.
- Closure path: Reviewer FAIL produces actionable findings, implementation is revised and re-validated, and a *new* reviewer tests again; PASS permits commit while unresolved blockers force human escalation/stop.
- Boundary reachability: `orchestrated-execution` and `start` shipped skill contracts mandate fresh host Task reviewer roles at concrete phase boundaries and route findings into the next implementation/review round.
- Why this is / is not agent-owned: Reviewer independently judges the implementation's actual code/DoD, rather than only displaying the implementing agent's own success report.
- Evidence: [skills/orchestrated-execution/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/orchestrated-execution/SKILL.md), [agents/adversarial-reviewer.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/agents/adversarial-reviewer.md), [skills/orchestrated-execution/rubrics/adversarial-review-rubric.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/orchestrated-execution/rubrics/adversarial-review-rubric.md), [skills/start/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/start/SKILL.md), [skills/plan-review-gate/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/plan-review-gate/SKILL.md)
- Basis: first-party review role and explicit feedback/gate requirements
- Confidence: medium-high for structurally required path
- Caveats: No live audit of review independence beyond the source-defined fresh-Task separation; this is source-side S3* classification, not an independent OpenSiro second human audit.
- Claim being audited: A coding subagent delivered a work unit fully and correctly under written spec/DoD.
- Ordinary reporting path: Coder status, implementation output and self-described tests.
- Complementary access path: Fresh separate reviewer reads actual diff/work-unit files and specification; orchestrator independently executes validation rather than believing coder self-report.
- Independence boundary: Fresh Task instance on each review, not resumed teammate or implementing subagent, with prior findings deliberately withheld to avoid anchoring.
- Who acts on findings: Implementing agent fixes FAILs, orchestrator revalidates and respawns reviewer; persistent blockers are escalated to the human.


## S4 — Outside-and-then intelligence
- State: P
- Function: Translate changing project/external tool feedback into accepted, persistent development knowledge that modifies the next agent's strategy.
- Disturbance / variety regulated: Repeated errors in GitHub review, CodeRabbit external feedback, third-party API quirks, changed build/test conventions and misunderstood user needs.
- Decisive decision or feedback right: Model-assisted self-reflect proposes reusable lessons and ranks them; the project user explicitly selects which to accept or resolve against previous knowledge, retaining final prospective adaptation ownership.
- Decision owner: Legitimate project operator for adopted knowledge choices; agent is the evidence-gathering/option-generating support, not an independent ultimate authority.
- Supporting / enforcement mechanisms: `/self-reflect` structured review/comment extraction, JSONL .beads knowledge writes, dedup/supersession, `/prime` selective lookup and subsequent planner/coder prompt consumption.
- Closure path: External PR review/API experience → proposed lesson → **human selection** → committed project-local knowledge fact → `/prime` loads relevant rule into a later planning/coding session, changing how work is done.
- Boundary reachability: The installable plugin ships both self-reflect and prime commands; orchestrated-execution requires knowledge capture before PR, and recovery/next-task instructions load relevant facts from the project knowledge base.
- Why this is / is not agent-owned: The decisive acceptance/supersession of future policy-for-work belongs to the project human; automatic learning without approval is not asserted.
- Evidence: [commands/self-reflect.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/commands/self-reflect.md), [commands/prime.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/commands/prime.md), [skills/orchestrated-execution/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/orchestrated-execution/SKILL.md), [skills/start/guides/delivery-scope.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/start/guides/delivery-scope.md), [README.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/README.md)
- Basis: explicit end-to-end source-specified project mode and parent decision
- Confidence: medium
- Caveats: Source-level closed human decision and future priming route are shown, not observed behavior improvement on a live independent task. The curated knowledge affects project work practices, not proof of a self-governing S5 constitution.
- External distinction: GitHub/CodeRabbit review feedback, external API behavior and user corrections are inputs distinct from the agent's ordinary transcript self-report.
- Future / prospective distinction: Retained lessons explicitly target the next project task and future error prevention, not only a single-run memory summarization.
- Adaptation option generated: Add/supersede a project-wide reusable rule or workaround, reject low-value patterns, or propose a separately approved metaswarm core issue.
- Path back into current capability / S3: Once user-approved fact is written to .beads/knowledge, `/prime` reads it before subsequent planning/implementation and recovery, conditioning later agent behavior.


## S5 — Policy and identity
- State: —
- Function: No accepted first-party organizational identity/ultimate-policy decision-and-return loop is established at the installed project-cell recursion.
- Disturbance / variety regulated: Constitutional change of ultimate purpose, legitimate organizational rule-set and final identity authority.
- Decisive decision or feedback right: No shipped agent or parent constitutional policy procedure identified beyond project user checkpoints and fixed playbook guards.
- Decision owner: None established for S5; project human decides checkpoints and S4 knowledge adoption but this does not create ultimate policy governance.
- Supporting / enforcement mechanisms: Reviewer/plan gates, human approvals, severity retry bounds, plugin role instructions and project knowledge rules.
- Closure path: No distinct ultimate-policy change with authoritative return to the deployed project organization's constitution was traced.
- Why this is / is not agent-owned: Mandatory local workflow guidelines and user-approved lessons are operational/adaptive constraints; they do not constitute a decision mechanism for the project organization's identity.
- Evidence: [skills/start/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/start/SKILL.md), [skills/orchestrated-execution/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/orchestrated-execution/SKILL.md), [commands/self-reflect.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/commands/self-reflect.md), [cli/metaswarm.js](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/cli/metaswarm.js), [agents/swarm-coordinator-agent.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/agents/swarm-coordinator-agent.md)
- Basis: bounded inspected packaged workflow surfaces
- Confidence: medium
- Caveats: The target project/human team may maintain a separate S5 governance system, which is not metaswarm's first-party authored loop.

### Absence scope

- Surfaces inspected: [skills/start/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/start/SKILL.md), [skills/orchestrated-execution/SKILL.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/skills/orchestrated-execution/SKILL.md), [agents/swarm-coordinator-agent.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/agents/swarm-coordinator-agent.md), [commands/self-reflect.md](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/commands/self-reflect.md), [cli/metaswarm.js](https://github.com/dsifry/metaswarm/blob/4bbb10abd301b9ec9d63371e296049cbc6043baa/cli/metaswarm.js)
- Plausible first-party paths checked: Fixed mandatory approval/review rules, model role authorization, knowledge supersession and operator checkpoints were assessed as candidate ultimate-policy gates.
- Why no material first-party path remains: All observed decisions concern current workflow, conflict control or reuse of engineering lessons; none changes a legitimate overarching identity/constitutional authority with an operational return path in the installed distribution.

## Recursion

The installed project orchestration contains issue/work-unit S1 agents, a cross-worktree model-backed coordinator and fresh independent reviewers. This is a bounded project cell; external host Claude/Codex/Gemini, GitHub institution and metaswarm maintainers are not grouped into an unobserved higher-recursion viable organization.

## Variety and escalation

The orchestration attenuates parallel edit collisions through task scopes/dependencies, checks work-unit integrity independently and enforces fresh reviewers. Stuck/failed units, exhausted review retries or capacity/priority disputes escalate to the project operator. Human checkpoints explicitly stop continuation until a decision, without transferring S5 authority.

## Evidence gaps

- No live deployed host-model episodes or third-party end-to-end reliability measurements were run; instructions, role exposure and installation are judged as structural first-party paths, not as observed execution traces.
- In Task mode no cross-agent persistent messaging is assumed; agent-specific returned task outputs/approved plans carry the evidenced feedback. Team mode is conditional on host `TeamCreate`/`SendMessage`.
- The project-local S4 parent mode depends on a real operator selecting lesson candidates and a subsequent agent invoking `/prime`; no unapproved background adaptation is claimed.
- This source-only S3* determination does not constitute an independent OpenSiro secondary audit or proof of independent model-provider identities. S5 negative is scoped to the installed plugin/project cell, not to the full human organization.
