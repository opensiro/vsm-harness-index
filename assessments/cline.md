---
harness_id: cline
project_name: Cline
repository: https://github.com/cline/cline
review_ref: cfe9cadab99617d5013bf89f07b079d105057791
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: ?
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Cline

## Review boundary
Cline at the pinned revision across the shared agent engine used by CLI/desktop/IDE surfaces and its SDK. Human approval remains parent authority unless auto-approval is enabled.

## Repository architecture
Cline edits code, runs commands, observes compiler/test/server feedback, browses and uses tools. The SDK exposes custom tools, multi-agent teams, connectors and schedules; rules/plugins/hooks can add policy/auditing behavior.

## Primary evidence
- `README.md`: shared coding-agent engine; Plan/Act loop; automatic reaction to linter/test/server output; SDK multi-agent teams; plugins/hooks; human approval/auto-approve.

## Operational model
Coding agents are S1 units. Teams exist as a first-party SDK surface, but their organizational relation is not specified strongly enough to infer S2.

## S1 — Operations
`A`: agents autonomously edit/run/browse and react to execution feedback. Confidence: high.

## S2 — Coordination
`?`: multi-agent teams are first-party, but no concrete interference-dampening decision right is established by the reviewed evidence.

## S3 — Inside-and-now control
`?`: lifecycle hooks/schedules do not prove autonomous whole-system regulation.

## S3* — Complementary audit
`?`: plugins can add auditing and tests feed the normal loop; neither establishes a sufficiently independent first-party audit role out of the box.

## S4 — Outside-and-then intelligence
`?`: Plan mode and environment feedback remain current-task behavior.

## S5 — Policy and identity
`?`: rules, approvals and permissions are user/developer-controlled.

## Recursion, variety, escalation
Team/subagent composition and multiple clients do not by themselves establish recursive viability.