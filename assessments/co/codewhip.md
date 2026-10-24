---
harness_id: codewhip
project_name: CodeWhip
repository: https://github.com/hasitpbhatt/codewhip
review_ref: be51da68db85096e9fa0455777e3ed89985df756
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# CodeWhip

## Review boundary

- System in focus: the local-first CodeWhip coding-agent CLI/SDK run and its first-party main model/tool loop, optional bounded read-only subagents, controlled repository tools, permission and budget paths, checkpoints, sessions, outcomes and audit trail.
- Purpose and identity: perform repository coding and inspection under operator-configured safety/cost limits, retain reproducible run evidence and support controlled follow-up work.
- Relevant environment: changing source tree and tests, model/provider responses and failures, operator approvals, shared child token budgets, local process work, repository policy and permitted external fetches.
- Standard-distribution boundary: executable TypeScript paths wired through src/index.ts, src/loop.ts, src/tools, src/subagents.ts, src/policy.ts, src/budget.ts, session/outcome/permission and audit modules.
- Credited operating / distribution surfaces: ordinary codewhip run / SDK query mode; native coding and tool feedback loop; opt-in delegate and delegate_many with shipped built-in read-only review/explore/plan agents; code review returned to the main thread; budget-sharing gate; supported tool/audit/checkpoint and optional background process modes.
- Adjacent first-party surfaces excluded from ownership: benchmark tasks, src/bench, src/immunity adversarial/evaluation suites, development CI, governance essays, contributor organization, future roadmap H2 designs, provider-internal reasoning and user-authored agent or hook scripts.
- First-party modes checked: main terminal/model/tool run; allowed/denied/approval and remember-policy modes; delegated single child and concurrent child fan-out; read-only adversarial review; background shell-process tools; separate offline audit verification, rollback and operator verdict commands.
- Recursion level: one installed workspace-level CodeWhip operating organization. The main coding Agent and optional independent model-backed research/review subagents enact work within one parent run; the developer/maintainer organization is outside the assessed product.
- Reviewed revision: be51da68db85096e9fa0455777e3ed89985df756 (batch #1013 row 2). Observation date: 2026-10-24. MIT license.

## Repository architecture

The native agentLoop in src/loop.ts cycles through model responses, validates tool calls, applies first-party permission policy, dispatches repository tools, records result/audit entries, checks budgets and feeds observations back to the model. The CLI src/index.ts and SDK src/sdk.ts expose this shipped loop; these are executable rather than a prompt-only wrapper. File edits/writes are checkpointed for rollback; sessions and outcomes preserve context and run receipts. The jail, deny rules, human asks, promoted tool denies, hash-chained audit and cost ceilings constrain operations without owning the model's code-choice discretion.

The optional delegate and delegate_many tools instantiate bounded child agentLoop runs through src/subagents.ts with separate prompts/context, read/search-only authority, distinct run IDs and returned summaries. The built-in review agent explicitly challenges correctness/security of real file content and reports file:line findings. The main model receives those reports as tool results and may use them to revise coding actions. This is the product's complementary audit mode; the signed audit log itself is a provenance mechanism, not a substitute for the reviewer's risk judgment.

For concurrent delegation, delegate_many runs up to four separately progressing children. When a parent token ceiling exists, allocateChildBudgets divides the shared remaining budget into fixed child quotas while reserving a portion for parent convergence; each child receives an enforceable tokenBudget and returns usage/failure/report feedback. That is a concrete inter-child shared-budget contention attenuator, but the 85/15 allocation and equal child shares are chosen by deterministic source code rather than an autonomous coordination agent.

Source anchors: [run loop](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/loop.ts), [subagents](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/subagents.ts), [fan-out](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/tools/delegate_many.ts), [budget](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/budget.ts), [audit](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/audit.ts), [policy](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/policy.ts).

## Operational model

A normal run has one main model-backed coding actor. Its tools perform and report workspace actions, while permissions, host asks, token/cost limits and audit records enforce externally chosen constraints. In optional delegated mode the parent model chooses a specialist and supplies a task; the child models use separate read-only loops and return short findings. Concurrent children cannot write to each other's workspace, but compete for one finite parent token budget, which CodeWhip splits and enforces before convergence. No live model/provider execution was used for this source assessment.

## S1 — Operations

- State: A
- Function: transform coding objectives into repository inspection, edits, commands and validated responses through an agent-controlled model/tool feedback loop.
- Disturbance / variety regulated: varying source files, implementation alternatives, failed commands, provider/tool errors, returned observations and task-specific user needs.
- Decisive decision or feedback right: select and revise task-specific tool calls, code changes and next actions from observations.
- Decision owner: the main model-backed CodeWhip Agent; optional child investigators separately choose their read/search steps.
- Supporting / enforcement mechanisms: CLI and SDK adapters, tool registry, path jail, policy ladder, denied action list, token/cost caps, checkpoint/rollback, sessions, hooks, outcomes and hash-chain.
- Closure path: user prompt and source context → model-selected tool call → permission-gated tool execution or refusal → tool result entered into model transcript → subsequent revised action or final answer.
- Boundary reachability: src/index.ts invokes the native agentLoop from src/loop.ts; shipped read/edit/write/bash/search tools are wired into the normal local run, not merely example scripts.
- Why this is / is not agent-owned: removing the model leaves rules and deterministic tool executors, but no open-ended choice of coding modifications or revision from feedback; tool policy only constrains that choice.
- Evidence: [src/loop.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/loop.ts), [src/index.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/index.ts), [tools](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/tools/registry.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model-provider quality and actual coding effectiveness are not tested; human approvals and deterministic stop rules limit reachable actions.

## S2 — Coordination

- State: C
- Function: attenuate shared token-budget exhaustion and parent-convergence starvation among independently running delegated S1 investigators in the supported concurrent fan-out mode.
- Disturbance / variety regulated: up to four simultaneous read-only child model loops can consume the same finite parent token allowance and prevent sibling work or the parent's final result.
- Distinct S1 units: concurrently running delegated child model/tool loops, each with its own task, transcript, model decisions, timeout and returned output; parent coding loop is another operational actor.
- Inter-S1 disturbance: unbounded sibling token consumption would deplete the parent quota needed for other children and the parent convergence step.
- Attenuating coordination relation: delegate_many invokes allocateChildBudgets, divides the available budget into child quotas and reserves a separate coordination share, then passes enforceable ceilings to individual child loops.
- Feedback into subsequent S1 behaviour: a child's token ceiling stops or bounds its continuation; completed/failed child reports and metered usage return to the parent model, which continues with that constrained result rather than unknowingly spending the entire shared budget.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism is explicitly tied to shared resource interference among simultaneous operational children, not merely their order or message transport.
- Decisive decision or feedback right: decide the concrete shared-budget attenuation policy (85% child pool, 15% parent reserve, equal child shares); the shipped code enforces the selected policy and reports outcomes.
- Decision owner: CodeWhip developers/configured deterministic allocator for the budget-split policy; no first-party autonomous S2 actor selects or revises the quota policy from conflict feedback.
- Supporting / enforcement mechanisms: Promise.all child scheduling, tokenBudget caps in child agentLoop, per-child deadlines, usage folding, ordered report collection and the parent's model-selected delegate_many task set.
- Closure path: finite parent budget and multiple children → first-party allocation → enforced per-child ceilings → bounded child work and result/usage feedback → parent continues with reserved capacity.
- Boundary reachability: delegate_many is an advertised first-party model tool in the normal loop, and the allocator and child caps run when this optional standard mode is chosen with a configured token budget.
- Why this is / is not agent-owned: the parent model chooses to fan out tasks but does not decide the concrete equal-share allocation or dynamically renegotiate exhausted quotas; its choice of delegates does not transfer ownership of the coordination response.
- Evidence: [src/tools/delegate_many.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/tools/delegate_many.ts), [src/budget.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/budget.ts), [src/subagents.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/subagents.ts).
- Basis: structural.
- Confidence: medium.
- Caveats: the budget mechanism is inactive when no parent token budget is configured; children are read-only and thus do not create a qualifying shared-file write conflict. No generalized coordination beyond bounded token contention is claimed.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-current resource/commitment management over a population of independently accountable operational units is established.
- Disturbance / variety regulated: not established for an S3-specific whole-current function.
- Whole-system current view: the current run tracks tool/child usage and process-scoped background command status, not an enduring portfolio of S1 commitments under a separate manager.
- Current-control decision scope: the main Agent delegates task fragments, handles tool feedback and can stop background shell processes; these are local operational choices, not a whole-system current resource bargain or intervention authority.
- Decisive decision or feedback right: no material S3-specific right established.
- Decision owner: no S3 owner established; configured caps belong to the operator/developer and routine task choices to S1.
- Supporting / enforcement mechanisms: budget counters, todo state, concurrency ceilings, background process map/status, timeouts, token limits and permission gates.
- Closure path: no whole-current performance/resource regulation returned across an enduring S1 portfolio; deterministic limits simply bound the selected run and its child operations.
- Why this is / is not agent-owned: model-selected delegation and fixed resource enforcement do not constitute autonomous S3 current control; similarly a human set ceiling is not a complete parent S3 mode.
- Evidence: [src/loop.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/loop.ts), [background tasks](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/tools/background-tasks.ts), [src/budget.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/budget.ts).
- Basis: structural bounded absence review.
- Confidence: medium-high.
- Caveats: the TUI exposes process-local task status and operator stopping controls; they are not credited as a whole-current governance regime over autonomous S1 commitments.

### Absence scope

- Surfaces inspected: main loop, child fan-out, budget allocator, background task manager/status, CLI run controls, policy and outcome recording.
- Plausible first-party paths checked: parent model as manager, shared child budgets as S3, process-scoped job list, policy ceilings, multi-run commitments and operator current-control mode.
- Why no material first-party path remains: the supported paths coordinate or limit one operating task and its dependent children/processes, with no distinct whole-current authority/feedback over independent operational commitments.

## S3* — Complementary audit

- State: A
- Function: independently challenge a coding result through a first-party adversarial code-review specialist with direct source evidence and returned findings.
- Disturbance / variety regulated: defects and risky assumptions missed by the main coding actor's own reasoning or self-report.
- Claim being audited: the correctness/security and failure behavior of a proposed repository change.
- Ordinary reporting path: the main coding Agent's own tool observations, implementation summary, and regular command/test feedback.
- Complementary access path: the built-in review subagent receives a fresh transcript, specialist adversarial prompt and read/search tools to inspect actual workspace files, then reports grounded file:line issues.
- Independence boundary: a distinct read-only child model loop cannot edit the reviewed repository, sees no parent transcript, and applies a separate risk-focused prompt; it is product-internal complementary independence, not an external third-party review.
- Audit judgment / decisive feedback right: select concrete correctness/security findings and their severity from direct code evidence rather than accepting the parent Agent's report.
- Decisive decision or feedback right: the reviewer model's source-grounded risk judgment and corrective feedback returned to the parent.
- Decision owner: the built-in review subagent model in the opted-in delegated-review mode.
- Supporting / enforcement mechanisms: agent definitions, read-only plan-mode, no-network/delegation child caps, path jail, timeout, summary return, audit chain and per-child usage accounting.
- How findings enter subsequent control: the delegate tool returns the specialist's findings as a parent tool result in the main model transcript, making them actionable in its next coding steps.
- Who acts on findings: the main coding Agent decides whether and how to implement corrections from the returned review; optional human permission gates still govern protected edits.
- Closure path: primary code artifact → separate read-only reviewer inspects files → independent risk report with file:line findings → main Agent receives report and can correct/test subsequent work.
- Boundary reachability: review is one of the built-in shipped agents in src/subagents.ts and is reachable via advertised delegate/delegate_many model tools, with runtime read-only enforcement.
- Why this is / is not agent-owned: removing the review model leaves the deterministic audit log and tool filters, but not the independent semantic risk assessment; the model owns that audit judgment in the supported optional mode.
- Evidence: [src/subagents.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/subagents.ts), [src/tools/delegate.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/tools/delegate.ts), [src/tools/child-run.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/tools/child-run.ts).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: review is opt-in rather than a mandatory gate, findings are plain returned text rather than a dedicated persistent review database, and the main model may disregard them; no independently demonstrated effectiveness is claimed.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supported external-and-prospective capability adaptation loop is established within the installed coding runtime.
- Disturbance / variety regulated: not established for an S4-specific future environmental adaptation function.
- Decisive decision or feedback right: no established prospective adaptation selection and return.
- Decision owner: not established in the assessed runtime.
- Supporting / enforcement mechanisms: model/provider routing and failover, session memory, remembered approvals, outcome metrics, operator verdicts, benchmark/immunity analysis and roadmap papers.
- Closure path: no product-run environmental sensing → future options → changed current capability/control cycle was found.
- Why this is / is not agent-owned: model changes during execution address current provider failures; developer benchmark and immunity suites are adjacent evaluation, not a live strategic S4 owner.
- Evidence: [src/loop.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/loop.ts), [src/remember.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/remember.ts), [src/verdict.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/verdict.ts).
- Basis: structural bounded absence review.
- Confidence: medium-high.
- Caveats: outcomes and retrospective verdicts could inform a future learning system but do not by themselves constitute a product-wired prospective adaptation decision.

### Absence scope

- Surfaces inspected: provider selection/failover, memory/grant promotion, outcome/verdict records, loop feedback, first-party benchmark/immunity directories and roadmap.
- Plausible first-party paths checked: observed model failure → future provider capability choice, verdict-driven learning, automatic policy or tool evolution, external threat scouting and adaptation option return.
- Why no material first-party path remains: the shipped operational paths react to current work or persist prior operator choices; experimental evaluation and prospective product proposals remain adjacent development, with no in-boundary S4 closure.

## S5 — Policy and identity

- State: —
- Function: no first-party ultimate identity/constitutional policy authority and returned decision path are established at the installed harness recursion.
- Disturbance / variety regulated: tool permissions, risky commands, private-route selection and remembered/promoted denies are operational constraints, not an identity-level controversy.
- Decisive decision or feedback right: no identity/ultimate-policy decision right established.
- Decision owner: developer and operator choose configuration/permission rules outside a qualifying S5 product loop.
- Supporting / enforcement mechanisms: non-overridable denylist, policy file, manual approvals, session grants, remembered shapes, promoted denies, audit signatures and local trust commands.
- Closure path: external permissions/configuration → deterministic policy check → tool allow/ask/deny is present; identity-level matter → legitimate authority decision → authoritative return governing the organization is not.
- Why this is / is not agent-owned: neither fixed policy enforcement nor an operator's approval of an ordinary file/bash command establishes ultimate identity/policy governance by a first-party actor.
- Evidence: [src/policy.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/policy.ts), [src/policy-store.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/policy-store.ts), [src/audit.ts](https://github.com/hasitpbhatt/codewhip/blob/be51da68db85096e9fa0455777e3ed89985df756/src/audit.ts).
- Basis: structural bounded absence review.
- Confidence: high.
- Caveats: a human can approve persistent tool-denial promotion, but that is task/tool risk policy without a demonstrable system identity/ultimate-policy adjudication return.

### Absence scope

- Surfaces inspected: policy checking, remembered permission rules, promote-deny CLI, signed audit, trust verdicts, configuration and operator approval modes.
- Plausible first-party paths checked: identity-level issue escalation, constitutional rule revision by an autonomous or legitimate parent S5 owner, policy-adoption feedback into the installed product.
- Why no material first-party path remains: observed decisions approve or refuse tool patterns and current work; the product has no first-party ultimate-identity decision forum and closure path at this recursion.

## Recursion

The main agent and read-only child investigators are distinct bounded operational units for delegated tasks, but the child nodes have no independent full metasystem or authority to reproduce the entire harness. Their fresh context does not itself demonstrate autonomous viable-system recursion. Maintainers, benchmarks and surrounding cloud model providers are outside this product recursion.

## Variety and escalation

CodeWhip attenuates tool-action variety through path checks, immutable denies, approval prompts and cost limits; parallel children receive separate token envelopes to prevent one from exhausting all parent capacity. It amplifies operational variety through model-selected code tools and specialist read-only investigations. Denied actions may ask the legitimate operator within ordinary task scope. Audit evidence and optional review findings are separate; only the model-based review gives complementary semantic risk judgment in the credited S3* mode.

## Evidence gaps

- S2=C is bounded to optional concurrent read-only child runs with an explicit finite parent token budget. Its static quota policy is not an autonomous coordinator, and no live token-contention test was executed.
- The shipped review subagent is sufficiently separated by prompt/context/authority for an optional product-internal complementary audit, but no model-backed empirical review-quality outcome was measured.
- No whole-current S3, future-facing S4 or ultimate-policy S5 path is inferred from budgets, process tasks, provider routing, CLI policy or adjacent development research.
- All judgments are source-relative to the frozen commit. No live LLM-agent, model-provider or Browser quality test was performed.
