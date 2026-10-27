---
harness_id: taurus-ai-shell
project_name: Taurus AI Shell
repository: https://github.com/Lukeus/taurus
review_ref: b643754200a241299bb6c3bac7e9dd8237e1da8d
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Taurus AI Shell

## Review boundary

- System in focus: one Taurus workspace conversation, its built-in delegates and supported on-demand turn-review mode.
- Purpose and identity: produce coding/workspace outcomes with a provider-backed tool agent and recoverable changes.
- Relevant environment: workspace/files, OS commands, configured local/hosted model providers, user permissions and conversations.
- Standard-distribution boundary: Rust agent/core/host/tools/agents/skills plus first-party Tauri desktop and CLI; installed plugins/user agents are not assumed to supply extra owners.
- Credited operating / distribution surfaces: [README.md](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/README.md), [crates/taurus-core/src/agent.rs](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-core/src/agent.rs), [crates/taurus-core/src/subagent.rs](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-core/src/subagent.rs), [crates/taurus-agents/src/builtin.rs](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-agents/src/builtin.rs), [crates/taurus-host/src/review.rs](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-host/src/review.rs), [src/components/ChangesDrawer.tsx](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/src/components/ChangesDrawer.tsx), [docs/safety.md](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/docs/safety.md)
- Adjacent first-party surfaces excluded from ownership: repository development/CI, screenshot fixtures, benchmarks and standalone examples are not deployed owners. Built-in review is a real host/UI/CLI path, unlike contributor PR review.
- First-party operating / deployment modes considered: desktop and CLI run/repl; local/hosted providers; foreground coder/worker and optional read-only background explorer; user-invoked Review this turn / taurus review and Fork with this.
- Recursion level: a workspace coding conversation and its scoped delegates, not the entire user's machine or upstream maintainer organization.
- Reviewed revision: b643754200a241299bb6c3bac7e9dd8237e1da8d
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

A shared Rust core drives provider responses, tool execution, session state, retries/stall detection and optional verification nudges. Host/frontends provide permissions, checkpoints/diffs, fork/rewind, tools/MCP, notes, skills and agent proposals. Built-in explorer, worker and coder delegates get fresh contexts, restricted tools, iteration limits and structured finish reports. Read-only delegates may run in the background; mutable delegates run alone, with a shared per-message concurrency bound. Turn review is a separate host verb: it constructs a fresh read-only agent from a bounded diff plus closing claims and recorded command/delegate evidence, permits surrounding source reads, and returns a persistent/fingerprinted report to the drawer or CLI. A selected finding can populate a forked retry. It is not inserted into every future context automatically.

## Operational model

The coding model owns local strategy and tool selection; delegates have scoped operational discretion, including a coder instructed to choose code-consistent options and verify. The runtime decides scheduling/safety enforcement from declared effects. Human users choose ordinary goals, tool approvals, review triggers and whether to act on a finding. The review model owns its evidential judgment; user triggering/correction selection does not turn that judgment into a human audit verdict.

## S1 — Operations

- State: A
- Function: agentic workspace/coding transformation
- Disturbance / variety regulated: unknown source, tool results, command failures and delegated findings
- Decisive decision or feedback right: choose actions/arguments and adapt the solution from returned evidence
- Decision owner: root model and scoped delegate models
- Supporting / enforcement mechanisms: shared core loop, provider adapters, permissions, tool registry, checkpoints/session recording and structured delegate finish
- Closure path: model tool choice → execution results and background reports → updated model input → subsequent action or final answer
- Why this is / is not agent-owned: Deterministic tools and verification nudges support rather than choose the coding solution.
- Evidence: [crates/taurus-core/src/agent.rs#L500-L509](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-core/src/agent.rs#L500-L509), [crates/taurus-core/src/agent.rs#L975-L984](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-core/src/agent.rs#L975-L984), [crates/taurus-core/src/subagent.rs#L274-L338](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-core/src/subagent.rs#L274-L338), [crates/taurus-agents/src/builtin.rs#L125-L155](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-agents/src/builtin.rs#L125-L155)
- Basis: structural
- Confidence: medium-high
- Caveats: Pinned source establishes a supported path, not observed effectiveness or universal deployment.
- Boundary reachability: Desktop and CLI share the first-party core; built-in delegate definitions/launch are supplied without custom agent implementation.

## S2 — Coordination

- State: C
- Function: prevent concurrent mutable delegate/parent work from overwriting shared files
- Disturbance / variety regulated: two agents writing one working tree can edit over each other's intermediate state
- Decisive decision or feedback right: allow only read-only concurrent/background delegates; serialize mutating calls and reject an invalid background writer
- Decision owner: first-party effect/scope scheduler; autonomous team coordination policy is not separately composed
- Supporting / enforcement mechanisms: runs_concurrently/read-only scope checks, serialization, per-message semaphore and explicit rejection feedback
- Closure path: proposed mutable background delegate → refusal explaining write collision → parent selects foreground writer or read-only background explorer; serial mutable calls finish before the next
- Why this is / is not agent-owned: A concrete interference-specific constructor is supplied. Static scope classification and execution order do not themselves own agentic coordination discretion.
- Evidence: [crates/taurus-core/src/subagent.rs#L247-L301](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-core/src/subagent.rs#L247-L301), [crates/taurus-core/src/subagent.rs#L355-L369](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-core/src/subagent.rs#L355-L369), [crates/taurus-core/src/agent.rs#L1423-L1478](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-core/src/agent.rs#L1423-L1478), [docs/capabilities.md#L445-L493](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/docs/capabilities.md#L445-L493)
- Basis: structural
- Confidence: medium-high
- Caveats: Per-turn mechanism, not global isolation: different conversations and external processes may still write concurrently.
- Boundary reachability: The built-in spawn tool and core call scheduler enforce this relation in supported desktop/CLI execution.
- Distinct S1 units: parent coding agent and built-in/custom scoped delegate agents.
- Inter-S1 disturbance: mutable child running alongside parent/peer can overwrite shared working-tree changes.
- Attenuating coordination relation: background readers only; mutable delegates/calls execute alone based on actual tool effects.
- Feedback into subsequent S1 behaviour: rejected writer request explicitly tells the parent to choose foreground execution or explorer; returned reports then enter the parent turn.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: serialization and refusal are explicitly tied to destructive inter-writer interference.

## S3 — Inside-and-now control

- State: —
- Function: whole-current operational cohesion
- Disturbance / variety regulated: Delegate choice and result aggregation are local task decomposition; fixed slot/iteration ceilings do not establish current-control discretion.
- Decisive decision or feedback right: No function-specific decisive path established.
- Decision owner: None established for this function in the assessed mode.
- Supporting / enforcement mechanisms: spawn/finish/background delivery, max_concurrent_agents, activity inspector, Stop, turn budgets, agent definitions and model overrides
- Closure path: No qualifying function-specific return into operations.
- Why this is / is not agent-owned: The shipped parent chooses a scoped delegate and receives its result, but no distinct ongoing portfolio status/steer/reallocate current-control loop is established. Agent activity is observation, settings apply to a subsequent message, and generic Stop is not a complete parent current-control arrangement. No S3-specific constructor is credited from these general mechanisms.
- Evidence: [crates/taurus-core/src/subagent.rs](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-core/src/subagent.rs), [docs/capabilities.md#L482-L535](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/docs/capabilities.md#L482-L535), [docs/known-gaps.md#L100-L117](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/docs/known-gaps.md#L100-L117)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded absence at the frozen first-party distribution; arbitrary surrounding organizations and user extensions are not assessed.

### Absence scope

- Surfaces inspected: spawn/finish/background delivery, max_concurrent_agents, activity inspector, Stop, turn budgets, agent definitions and model overrides
- Plausible first-party paths checked: whether the model has a whole-current portfolio view plus authority to revise ongoing commitments/resources, or the human inspector closes a qualified parent mode
- Why no material first-party path remains: The shipped parent chooses a scoped delegate and receives its result, but no distinct ongoing portfolio status/steer/reallocate current-control loop is established. Agent activity is observation, settings apply to a subsequent message, and generic Stop is not a complete parent current-control arrangement. No S3-specific constructor is credited from these general mechanisms.

## S3* — Complementary audit

- State: A
- Function: complementary audit of a coding turn's claims against independent source/diff evidence
- Disturbance / variety regulated: the coder can claim success despite contradictory command results or defective source changes
- Decisive decision or feedback right: judge claims as supported/contradicted/uncertain and identify actionable defects through fresh surrounding-code inspection
- Decision owner: separate review agent/model context; human selects invocation and subsequent correction, not the audit verdict
- Supporting / enforcement mechanisms: host review constructor, explorer-only registry, diff/checkpoint and recorded-result extraction, fingerprint/cache and finding-to-fork UI
- Closure path: user selects changed turn → fresh review inspects diff/files and recorded claims/results → evidence-bearing report returns → selected finding enters a forked retry draft → user submission starts changed coding attempt
- Why this is / is not agent-owned: The reviewer independently chooses source checks and evidential verdicts; the runtime supplies/filter evidence and transports findings. Triggering an audit manually does not make its discretionary judgment human-owned.
- Evidence: [crates/taurus-host/src/review.rs#L1-L55](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-host/src/review.rs#L1-L55), [crates/taurus-host/src/review.rs#L139-L203](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-host/src/review.rs#L139-L203), [crates/taurus-host/src/review.rs#L233-L260](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-host/src/review.rs#L233-L260), [crates/taurus-host/src/review.rs#L377-L443](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-host/src/review.rs#L377-L443), [src/components/ChangesDrawer.tsx#L70-L79](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/src/components/ChangesDrawer.tsx#L70-L79), [src/components/ChangesDrawer.tsx#L385-L388](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/src/components/ChangesDrawer.tsx#L385-L388), [docs/safety.md#L955-L984](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/docs/safety.md#L955-L984)
- Basis: structural
- Confidence: medium-high
- Caveats: On-demand, not autonomous audit scheduling. It cannot run tests; diff/evidence are bounded and omitted coverage is named. Review stays outside normal transcript until explicitly returned through a retry. No live defect-detection effectiveness is claimed.
- Boundary reachability: Built-in host run constructs a fresh Session and read-only Agent. Changes drawer and taurus review invoke it; Fork with this carries actual findings into the next attempt without custom auditor wiring.
- Claim being audited: changed turn's final success/blocker assertions and its source transformation.
- Ordinary reporting path: coder's final message and delegated summaries.
- Complementary access path: fresh read-only reviewer examines diff and surrounding files, comparing claims with recorded command/delegate outcomes.
- Independence boundary: review has no producing conversation/request/plan and no write/shell/delegation ability; it may use the same model/provider. Context independence does not guarantee freedom from source injection.
- Who acts on findings: user accepts/selects a finding through native fork UI; the subsequent coding agent receives the finding in the retry request.

## S4 — Outside-and-then intelligence

- State: —
- Function: external prospective adaptation
- Disturbance / variety regulated: Notes, proposed skills/agents, search and model configuration can improve future convenience without constituting S4.
- Decisive decision or feedback right: No function-specific decisive path established.
- Decision owner: None established for this function in the assessed mode.
- Supporting / enforcement mechanisms: notes/skills/agent proposal catalogs, user approval/save paths, provider selection, web tools and context relay
- Closure path: No qualifying function-specific return into operations.
- Why this is / is not agent-owned: Skill/agent proposals capture learned procedures or requested capabilities; user approval saves them, but no shipped externally/prospectively oriented adaptation decision loop is established. Internal learning and generic tool extensibility do not alone establish S4 or a parent modifier.
- Evidence: [crates/taurus-skills/src/proposal.rs](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-skills/src/proposal.rs), [crates/taurus-agents/src/proposal.rs](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-agents/src/proposal.rs), [docs/capabilities.md](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/docs/capabilities.md), [docs/working-with-it.md](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/docs/working-with-it.md)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded absence at the frozen first-party distribution; arbitrary surrounding organizations and user extensions are not assessed.

### Absence scope

- Surfaces inspected: notes/skills/agent proposal catalogs, user approval/save paths, provider selection, web tools and context relay
- Plausible first-party paths checked: whether externally sensed future distinctions generate adaptation options and return through a function-specific current-capability negotiation loop
- Why no material first-party path remains: Skill/agent proposals capture learned procedures or requested capabilities; user approval saves them, but no shipped externally/prospectively oriented adaptation decision loop is established. Internal learning and generic tool extensibility do not alone establish S4 or a parent modifier.

## S5 — Policy and identity

- State: —
- Function: ultimate identity/policy closure
- Disturbance / variety regulated: tool allowlists, hooks, user skill acceptance and agent prompts constrain operations.
- Decisive decision or feedback right: No function-specific decisive path established.
- Decision owner: None established for this function in the assessed mode.
- Supporting / enforcement mechanisms: permissions/safety, per-project settings, agent editor/proposals, hooks and ordinary user questions
- Closure path: No qualifying function-specific return into operations.
- Why this is / is not agent-owned: No function-specific identity/ultimate-policy issue/decision/return constructor is supplied by approval and configuration editing alone; maintainer governance remains outside this workspace conversation.
- Evidence: [docs/safety.md](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/docs/safety.md), [docs/configuration.md](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/docs/configuration.md), [crates/taurus-agents/src/proposal.rs](https://github.com/Lukeus/taurus/blob/b643754200a241299bb6c3bac7e9dd8237e1da8d/crates/taurus-agents/src/proposal.rs)
- Basis: structural
- Confidence: medium-high
- Caveats: Bounded absence at the frozen first-party distribution; arbitrary surrounding organizations and user extensions are not assessed.

### Absence scope

- Surfaces inspected: permissions/safety, per-project settings, agent editor/proposals, hooks and ordinary user questions
- Plausible first-party paths checked: whether identity-policy matters are escalated to legitimate ultimate authority and returned into future operation
- Why no material first-party path remains: No function-specific identity/ultimate-policy issue/decision/return constructor is supplied by approval and configuration editing alone; maintainer governance remains outside this workspace conversation.

## Distributed OSS parent arrangement

Local users own goals, permissions and the decision to invoke/act on review. These are not automatically parent S3/S4/S5 loops or an organization-wide governance arrangement. Maintainer development decisions are outside.

## Self-hosted and non-human modes

Local and hosted model choices retain the same loop. Review's read-only independent-context mode is built in and user-invoked. Self-hosting and custom-agent model overrides do not by themselves add a parent policy/adaptation mode.

## Recursion

Scoped delegates and separate transcripts demonstrate decomposition, not complete viable recursive organizations; child spawning is structurally removed from delegates.

## Variety and escalation

Structured finish distinguishes done/blocked/failed and preserves required action fields. Read-only background policy attenuates write collisions; summaries still compress observations. Review adds source/recorded-evidence access and a native corrective fork, with explicit coverage limits.

## Evidence gaps

Static frozen-source review only. Cargo absent, so no native compilation/tests or provider-backed tasks. Review cannot execute tests, may share the producer's model/provider and omits bounded diff/results; same context separation is not proof of statistical audit efficacy. Concurrent independent conversations and external writers remain outside per-turn coordination.

## Index execution provenance

Frozen intake #2176, serial controller #2177, row 5. Source assessment is the executing Index S1 actor's work; GitHub, deterministic checks and CI are supporting machinery. No independent semantic review or autonomy grade is claimed. Proposed publication precedes a separate canonical transaction.
