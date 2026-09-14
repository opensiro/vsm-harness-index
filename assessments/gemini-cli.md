---
harness_id: gemini-cli
project_name: Gemini CLI
repository: https://github.com/google-gemini/gemini-cli
review_ref: 9c1b0a610534d6f8120964cf2672c07807d8fc90
reviewed_at: 2026-09-14
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: ?
autonomy_s3_star: ?
autonomy_s4: ?
autonomy_s5: ?
---

# Gemini CLI

## Review boundary
Gemini CLI at the pinned revision as a terminal agent with built-in tools and automation integrations.

## Repository architecture
Gemini CLI edits/query codebases, uses shell/files/web/Search/MCP tools, checkpoints sessions and runs non-interactively. GitHub Actions can invoke the same agent for PR review, issue triage and automated workflows.

## Primary evidence
- `README.md`: terminal agent, built-in tools, automation, checkpointing, context files and GitHub workflows.

## Operational model
One Gemini CLI agent is S1. GitHub workflow invocations are separate runs, not an autonomous multi-S1 organization.

## S1 — Operations
`A`: the agent autonomously selects tools/actions toward coding and operational tasks. Confidence: high.

## S2 — Coordination
`—`: no material multi-S1 anti-oscillation function is established.

## S3 — Inside-and-now control
`?`: checkpoint/runtime controls do not establish autonomous whole-system regulation.

## S3* — Complementary audit
`?`: PR-review workflows are application tasks and not a standard independent audit channel over another S1 organization.

## S4 — Outside-and-then intelligence
`?`: Search/web access is current-task sensing, not prospective adaptation.

## S5 — Policy and identity
`?`: GEMINI.md and workflow configuration remain parent-authored.

## Recursion, variety, escalation
Tool/MCP integrations amplify one S1's variety; no recursion is established.