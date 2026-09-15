---
harness_id: goose
project_name: Goose
repository: https://github.com/aaif-goose/goose
review_ref: 50666ae0b9a51e260b52b7efbab2e4e020346e94
reviewed_at: 2026-09-15
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Goose

## Review boundary
Deep review of Goose at the pinned revision, centered on the first-party agent engine and repository structure rather than feature naming alone.

## Repository architecture
Goose is an autonomous tool-using agent harness. Its core agent owns the model/tool turn loop, extension access, state and execution feedback. The repository also contains subagent/session-forking concepts, but those extend operational decomposition; they do not by themselves establish a metasystem that regulates multiple autonomous S1 units.

## Primary evidence
- `crates/goose/src/agents/agent.rs`: defines the operational agent, provider/tool iteration, extension access, retries/compaction and agent configuration, including subagent state.
- `crates/goose/src/agents/extension_manager.rs`: extension/tool capability is supplied to the operational agent runtime.
- `crates/goose-cli/src/recipes/sub_recipe.rs` and session-forking paths in the pinned tree show decomposition/forking support without evidence of an S2 interference-regulation function.

## Operational model
A Goose agent receives a task, invokes the model, executes requested tools/extensions and continues from execution feedback. Forked or subordinate work remains task decomposition around that operational loop.

## S1 — Operations
`A`: the standard runtime autonomously selects and executes actions/tools within configured bounds and iterates from results. Confidence: high.

## S2 — Coordination
`—`: no first-party mechanism was found whose function is regulating interference, oscillation or shared constraints among multiple autonomous S1 units. Subagent/fork support is delegation, not sufficient S2 evidence.

## S3 — Inside-and-now control
`—`: the reviewed runtime does not expose a whole-system current-control authority that allocates shared resources or regulates commitments across multiple S1 units. Agent/session management is operational runtime management.

## S3* — Complementary audit
`—`: no independent or complementary audit channel with access distinct from routine operational reporting was established.

## S4 — Outside-and-then intelligence
`—`: context management, retries and task reasoning concern current execution; no distinct prospective environment-intelligence function that adapts the viable system was found.

## S5 — Policy and identity
`—`: system prompts, permissions, extensions and runtime configuration remain developer/user supplied rather than an autonomous legitimate policy/identity authority.

## Recursion, variety, escalation
Subagents and session forks increase operational variety and recursion depth, but the reviewed distribution does not close the S2–S5 metasystem functions around them.