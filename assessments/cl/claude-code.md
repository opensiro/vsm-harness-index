---
harness_id: claude-code
project_name: Claude Code
repository: https://github.com/anthropics/claude-code
review_ref: 7dd06361110d4417f3edefaf075f41923f0e04c5
reviewed_at: 2026-09-17
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-17
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Claude Code

## Review boundary
Pinned public first-party Claude Code repository at `7dd06361110d4417f3edefaf075f41923f0e04c5`, treating the shipped coding-agent product boundary evidenced by the repository's README, release/change feed and first-party customization surfaces as the system-in-focus. Agent Teams, subagents/background agents and cross-session messaging are included; separately operated Claude Code cloud review services are not credited without a repository-local closure path.

Observation date: 2026-09-17. Generated/current contract: Profile `0.2.2`, Methodology `0.3.1`.

## Primary evidence
- [`README.md`](https://github.com/anthropics/claude-code/blob/7dd06361110d4417f3edefaf075f41923f0e04c5/README.md) — first-party coding-agent product boundary.
- [`CHANGELOG.md`](https://github.com/anthropics/claude-code/blob/7dd06361110d4417f3edefaf075f41923f0e04c5/CHANGELOG.md) — shipped subagents/background agents, Agent Teams, agent listings, SendMessage, scheduled tasks, worktree/session behavior, teammate permissions and shutdown lifecycle.
- [`feed.xml`](https://github.com/anthropics/claude-code/blob/7dd06361110d4417f3edefaf075f41923f0e04c5/feed.xml) — same pinned first-party release evidence in structured form, including teammate-to-team-lead completion delivery and current team/session lifecycle fixes.

## Repository architecture
The public repository is not a complete source dump of every shipped Claude Code runtime component, so this assessment is intentionally limited to functions reconstructable from first-party pinned repository evidence. That evidence establishes an autonomous coding-agent loop plus subagents/background sessions, Agent Teams with a team lead and teammates, agent/session listing, inter-agent SendMessage, teammate permission handling, shutdown lifecycle, worktree/session isolation and scheduled/background execution.

## Operational model
Claude Code agents autonomously perform coding work. In Agent Teams mode, multiple teammate S1s operate concurrently while a lead agent receives teammate completion state, can observe team/session state and participates in permission/shutdown/current-work control. Supporting session/process machinery executes those decisions.

## S1 — Operations
`A`. Claude Code autonomously performs coding tasks through a model-driven tool loop; subagents and teammates are likewise agent actors that execute assigned work. Confidence: high.

## S2 — Coordination
`—`. The pin establishes parallel subagents/teammates, messaging, worktrees and team/session state, but the public evidence reviewed does not reconstruct a specific inter-S1 interference/conflict/oscillation together with an S2-specific attenuation decision and feedback loop. Generic messaging, parallelism and workspace/session separation are therefore not promoted to S2. Confidence: medium-high.

## S3 — Inside-and-now control
`A`. In Agent Teams mode the main/team-lead agent participates in a current-control relation over the live teammate system: teammate completion is returned to the team lead, live agents are represented in the agent list/panel, teammate permission requests are routed through the leader path, and teammate shutdown is a first-party lifecycle operation. These surfaces give the lead a current view plus discretionary intervention/continuation authority over active subordinate work; process/session machinery is supporting enforcement. Confidence: medium.

## S3* — Complementary audit
`—`. The repository contains code-review/product surfaces, but the pinned public evidence does not establish a sufficiently independent audit actor and a repository-local corrective closure path back into the same running Claude Code organization. Ordinary review/test use is not enough. Confidence: medium-high.

## S4 — Outside-and-then intelligence
`—`. Memory, compaction, scheduling, session resume and model/tool configuration support current/future execution but do not establish an external-and-prospective organizational intelligence loop that generates adaptation options and returns them into present capability. Confidence: high.

## S5 — Policy and identity
`—`. Managed settings, permission policies, user approval and organization configuration are constraints/authority surfaces, not evidence by themselves of a runtime identity or ultimate-policy tension-resolution loop. No qualifying S5 closure was established. Confidence: high.

## Recursion, variety, and escalation
Subagents, background agents and Agent Teams amplify operational variety; session/worktree isolation and permissions attenuate execution risk. Team-lead current control provides escalation from teammate work, but nesting/spawning alone is not VSM recursion. The incomplete public-source boundary is treated as an evidence limit rather than filled by inference.

## Admission conclusion
Canonical vector: `A — A — — —`.

The positive S3 is intentionally narrower than a claim that every Agent Teams mechanism is metasystemic: it rests on evidenced lead-owned current supervision/intervention, while S2 remains uncredited because disturbance-specific coordination closure was not established from the public pin.