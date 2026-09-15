---
harness_id: gemini-cli
project_name: Gemini CLI
repository: https://github.com/google-gemini/gemini-cli
review_ref: 9c1b0a610534d6f8120964cf2672c07807d8fc90
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Gemini CLI

## Review boundary
Deep review of the pinned Gemini CLI subagent model and terminal-agent runtime. Specialist delegation is kept separate from VSM S2 coordination.

## Repository architecture
Gemini CLI is an autonomous terminal/coding agent with built-in and MCP tools. Its subagent mechanism creates specialized, isolated delegated workers with scoped prompts/tools and returns their results to the caller. The reviewed path does not supply a distinct peer-coordination or whole-system control function.

## Primary evidence
- `docs/core/subagents.md`: describes isolated specialist subagents invoked for delegated work and returning a result to the parent context.
- Subagent definitions constrain role/tool/context boundaries; they do not establish an interference-regulation channel among multiple autonomous S1 units.

## Operational model
The main agent performs tool-using development work and may offload bounded subtasks to configured specialists before continuing from their returned output.

## S1 — Operations
`A`: the terminal agent autonomously selects tools/actions and iterates from workspace/tool feedback. Confidence: high.

## S2 — Coordination
`—`: subagent invocation is delegation and result return. No mechanism was found for regulating conflicts, oscillation or shared constraints between autonomous operational units.

## S3 — Inside-and-now control
`—`: parent-child task ownership does not amount to whole-system current resource/capacity/commitment authority.

## S3* — Complementary audit
`—`: no organizationally separate complementary audit channel was established.

## S4 — Outside-and-then intelligence
`—`: specialist selection and task reasoning concern current execution, not prospective environment intelligence and organizational adaptation.

## S5 — Policy and identity
`—`: subagent definitions, permissions, prompts and tools remain developer/user supplied.

## Recursion, variety, escalation
Subagents add specialized operational variety and hierarchy, but no reviewed metasystem function is closed.