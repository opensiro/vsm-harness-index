---
harness_id: miniharness
project_name: miniharness
repository: https://github.com/ZeleMate/miniharness
review_ref: 2eb01d8eda873bcf9087d329540e808298587cf0
reviewed_at: 2026-11-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-11-03
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# miniharness

## Review boundary

- System in focus: The installable Python model/tool agent harness and its first-party optional `Team` reviewer composition, not a user-created multi-agent company.
- Purpose and identity: Run bounded model-chosen tools against tasks with provider adapters, permissions, budgets, checkpoint/rewind and optional independent peer review.
- Relevant environment: User task/workspace, local files, model APIs, tool failures and permissions; developer-supplied team roles and routing.
- Standard-distribution boundary: Python package `miniharness`, usable `Harness` facade, `Agent` lifecycle, `Team` mediator and documented optional `examples/team.py` construction. An application must compose actual team agents/roles; examples are construction evidence, not a default always-on reviewer.
- Credited operating / distribution surfaces: [agent.py](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/agent.py), [harness.py](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/harness.py), [team.py](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/team.py), [agent_types.py](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/agent_types.py), [tools/policy.py](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/tools/policy.py).
- Adjacent first-party surfaces excluded from ownership: Mock scripted provider, tests, educational pattern/book writing, CI, externally hosted inference, developer-authored reviewer prompt and workspace permissions; `ReviewerAgent`'s same-conversation self-check is not an independent S3* actor.
- First-party operating / deployment modes considered: Single `Harness.run()` model/tool agent; `PlannerAgent` and `ReviewerAgent` subclasses; opt-in child `AgentTool`; composed `Team` writer→reviewer→revision/approval; mock-provider offline tests.
- Recursion level: One task-producing agent run; optional team is a separate composed two-agent operating mode. Tool calls, nesting and message count alone are not recursive viable systems.
- Reviewed revision: `2eb01d8eda873bcf9087d329540e808298587cf0`.
- Observation date: 2026-11-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

`Agent` owns the repeated model→tool→observation→next-decision path and supports follow-up, checkpoints, forks and streaming events. `Harness` constructs the provider stack, usage budget, toolbox, default side-effect approval, trace and optional helper agent; hard guards execute selected constraints rather than choosing task direction. `PlannerAgent` adds an initial within-task plan; `ReviewerAgent` re-prompts the *same* agent to check its own answer. Separately, `Team` supplies routed peer messages and a finisher-only `approve` tool. The shipped writer/reviewer construction gives the reviewer the original requirements and the writer's actual draft, lets it send corrective feedback, and publishes only a draft the designated finisher approves. This review arrangement requires application configuration and may use the same provider; no default independent source/host auditor exists. [README](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/README.md), [team.py#L93-L195](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/team.py#L93-L195), [examples/team.py](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/examples/team.py).

## Operational model

The principal S1 model selects task and tool actions, with policy/budget/retry and checkpoints as support. In opt-in `Team`, writer and reviewer are separate model sessions at the same operational composition, but review is a complementary check on the writer's actual produced text rather than proof of ordinary S2 collision regulation. The reviewer can reject by returning corrections and is the only finisher that can call `approve`; the developer must install the reviewer identity, route and risk-appropriate access. No independent organization-level S3/S4/S5 decision owner is shipped.

## S1 — Operations

- State: A
- Function: Produce user task outcomes through adaptive model-driven tools.
- Disturbance / variety regulated: Unknown task steps, tool errors, differing provider responses and workspace side effects.
- Decisive decision or feedback right: Select/sequence tools, interpret results, retry or revise the answer and finish a model turn.
- Decision owner: Model acting through `Agent`'s first-party state transitions, in the default `Harness` and optionally a team member.
- Supporting / enforcement mechanisms: Provider adapters, `Toolbox`, approval chain, budget guard, retry/circuit breaker, events and checkpoints.
- Closure path: Task → model choice → validated tool call → tool result/error in messages → renewed model judgment or final answer.
- Boundary reachability: Standard `Harness` instantiates an `Agent` and exposes `run()` with configurable provider; optional real provider requires a key, but mock tests exercise the same loop.
- Why this is / is not agent-owned: A model has substantive next-action discretion; deterministic permissions and retries do not themselves choose the work.
- Evidence: [agent.py#L67-L147](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/agent.py#L67-L147), [harness.py#L52-L148](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/harness.py#L52-L148), [lifecycle.py](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/lifecycle.py).
- Basis: explicit + structural
- Confidence: high for library loop wiring; actual model task effectiveness unmeasured.
- Caveats: Real LLM endpoints and side-effect permissions depend on operator setup; `MockProvider` tests verify structure, not real reasoning quality.

## S2 — Coordination

- State: —
- Function: No evidenced first-party coordination decision that attenuates a specific interference/oscillation among different S1 operations.
- Disturbance / variety regulated: Team feedback can correct a writer's artifact; shared provider budget and serial message delivery prevent technical overlap but do not govern competing S1 commitments.
- Decisive decision or feedback right: Resolve destructive cross-unit resource or work conflicts and return mutual constraints to operating agents; not instantiated.
- Decision owner: Team members choose messages; `Team` deterministically applies developer-authored routes and turn limits.
- Supporting / enforcement mechanisms: `send_message`, route whitelist, `max_turns`, shared budget, read-only tool concurrency.
- Closure path: A reviewer message may return to the writer for artifact correction, but no specified inter-S1 interference is detected and attenuated as S2.
- Why this is / is not agent-owned: Peer messaging and reviewer disagreement are not by themselves the Profile's distinct-S1/conflict/attenuation/feedback S2 witness.
- Evidence: [team.py#L49-L90](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/team.py#L49-L90), [team.py#L146-L179](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/team.py#L146-L179), [tools/agent_tool.py](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/tools/agent_tool.py).
- Basis: structural
- Confidence: medium-high.
- Caveats: Applications can compose conflict-aware teams, but generic routes and a reviewer finisher do not evidence that shipped function.

### Absence scope

- Surfaces inspected: `Team` routing/finishing, `AgentTool` delegation, read-only concurrent tool execution, providers and team tests.
- Plausible first-party paths checked: Multiple team agents, shared-budget stop, message delivery and parallel tool calls.
- Why no material first-party path remains: None supplies a specific cross-S1 collision/oscillation regulator that changes subsequent peer operations; reviewed team correction is task-artifact assurance instead.

## S3 — Inside-and-now control

- State: —
- Function: No autonomous or parent-composed whole-current organization control across operating units.
- Disturbance / variety regulated: Per-agent call budgets, tool approvals, excessive turns and failures stay local to current tasks.
- Decisive decision or feedback right: Choose multi-agent current priorities, resource commitments and intervention from a whole-system operational view; not implemented.
- Decision owner: Caller configures budgets/roles/routes; static runtime enforces them. Team reviewer chooses whether a specific artifact passes its review, not whole-system resource allocation.
- Supporting / enforcement mechanisms: `UsageTracker`, budget guard, `max_turns`, per-agent step limits, toolbox policy.
- Closure path: A hard limit stops an operation or approval gates a tool; no separate S3 decision returns to multiple S1 units as revised commitments.
- Why this is / is not agent-owned: Configurable hard guards and reviewer approval lack whole-current control rights.
- Evidence: [harness.py#L52-L138](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/harness.py#L52-L138), [team.py#L93-L110](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/team.py#L93-L110), [tools/policy.py](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/tools/policy.py).
- Basis: structural
- Confidence: high for exposed modes.
- Caveats: An application could implement its own manager; library expressiveness is not a constructor S3 function.

### Absence scope

- Surfaces inspected: Harness constructor, agent lifecycle, Team mediation, provider budgets, tool policy and tests.
- Plausible first-party paths checked: Shared budget stop, team finisher, agent type `PlannerAgent`, developer control of routes/roles and multi-agent helper composition.
- Why no material first-party path remains: No whole-current status view drives discretionary cross-task commitments or operating-unit corrective allocation.

## S3* — Complementary audit

- State: C
- Claim being audited: A writer's produced draft satisfies the original user requirements.
- Ordinary reporting path: Writer sends its drafted text as a routed message and may claim that it is ready.
- Complementary access path: Separate configured reviewer receives the actual draft plus the original task brief, may challenge requirements and optionally use its own tools, returns a correction to writer or calls the reserved `approve` gate.
- Independence boundary: Peer `Agent` conversations and tools are separately held; reviewer is not the writer's self-review pass. However reviewer role, prompt, route and any external/source-ground-truth tools must be deliberately composed by the application; there is no unconditional independent audit in a plain `Harness`.
- Who acts on findings: The writer gets a routed correction and revises; the designated reviewer alone approves the last received draft, which becomes `Team.run()`'s result.
- Function: Optional function-specific complementary check of the operational draft against separately delivered original requirements.
- Disturbance / variety regulated: Writer omissions or false completeness claims can be challenged before publication of a team result.
- Decisive decision or feedback right: Review independent draft-vs-brief evidence, demand a correction or approve for final release.
- Decision owner: A developer-composed separate reviewer model owns the judgment when the provided `Team` pattern is instantiated; `Team._approve` only enforces a configured finisher's decision.
- Supporting / enforcement mechanisms: Team membership and recipient routes, original-brief injection, designated finisher `approve` tool and mediated run/return loop.
- Closure path: Writer draft → reviewer sees original brief and submitted artifact → reviewer sends flaw → writer revision → reviewer `approve` → team output; tests exercise this correction and gate sequence.
- Boundary reachability: `Team`, agent roles and the finish tool are shipped public library code, with a complete executable `examples/team.py` and mock-provider lifecycle tests. This justifies a **constructor C**, not `A` in the default facade, nor any claim of independent filesystem/runtime audit without configured access.
- Why this is / is not agent-owned: The review choice belongs to a separate configured model; the library cannot guarantee reviewer composition, independence or audit coverage. `ReviewerAgent` checking its own answer is explicitly not this credited pathway.
- Evidence: [team.py#L93-L195](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/team.py#L93-L195), [examples/team.py#L35-L70](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/examples/team.py#L35-L70), [tests/test_team.py#L87-L119](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/tests/test_team.py#L87-L119), [agent_types.py#L56-L75](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/agent_types.py#L56-L75).
- Basis: explicit + structural
- Confidence: medium for limited draft-assurance constructor; not a generalized audit of arbitrary tools or real-world truth.
- Caveats: The example uses no independent file/search tools and both agent instances can use the same model/provider. An application must configure genuinely complementary access appropriate to its audit claim; absent that, S3* may remain unclosed in that deployment.

## S4 — Outside-and-then intelligence

- State: —
- Function: No independent prospective environmental scanning and capability-adaptation closure.
- Disturbance / variety regulated: New user tasks or model-provider outages are current operational inputs, not a future strategy model.
- Decisive decision or feedback right: Turn external/future distinctions into durable capability changes and return a chosen adaptation to current operations.
- Decision owner: Application developer chooses providers/prompts/tools; `PlannerAgent` produces only a plan for the present task.
- Supporting / enforcement mechanisms: Provider fallback, history checkpoint/fork, planner prompt and learning workbook.
- Closure path: Local task plan/tool iteration or developer edits; no agent/parent prospective option authorization and capability update.
- Why this is / is not agent-owned: Planning a task, self-reviewing its answer or switching on provider failure is not the Profile's S4 two-way adaptation loop.
- Evidence: [agent_types.py#L20-L75](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/agent_types.py#L20-L75), [harness.py](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/harness.py), [README](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/README.md).
- Basis: structural
- Confidence: high for exposed modes.
- Caveats: Source evolution by a developer is not part of runtime S4.

### Absence scope

- Surfaces inspected: Agent types, provider wrappers, retry/fallback, checkpoint/fork, examples, team and README roadmap.
- Plausible first-party paths checked: Planner, reviewer, provider change, history snapshot/fork and optional helper agents.
- Why no material first-party path remains: Those mechanisms plan/repair the present task or support manual extension; none integrates prospective external choices into enduring present capability under a separate S4 decision.

## S5 — Policy and identity

- State: —
- Function: No first-party ultimate identity/policy decision and returned constitutional governance at harness recursion.
- Disturbance / variety regulated: Unauthorized files, risky side effects and cost limits are treated as ordinary capability/permission constraints.
- Decisive decision or feedback right: Decide a disputed binding purpose/ultimate policy and return a changed organizational rule; not shipped.
- Decision owner: Caller selects prompts and policy handlers; approval callback/human user accepts or rejects individual tool actions.
- Supporting / enforcement mechanisms: Policy chain, read-only views, workspace confinement, side-effect approval and developer-authored role prompts.
- Closure path: Existing permissions allow/deny a tool; no identity matter reaches a legitimate parent authority and returns as an updated binding mission/policy.
- Why this is / is not agent-owned: Reviewer approval and user tool permissions are local operational controls, not runtime S5 governance.
- Evidence: [harness.py#L49-L90](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/harness.py#L49-L90), [tools/policy.py](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/tools/policy.py), [team.py#L64-L90](https://github.com/ZeleMate/miniharness/blob/2eb01d8eda873bcf9087d329540e808298587cf0/src/miniharness/team.py#L64-L90).
- Basis: structural
- Confidence: high at library boundary.
- Caveats: An application can implement human governance on top; library alone does not provide the specific return/closure path.

### Absence scope

- Surfaces inspected: Default policy chain, Harness configuration, team finisher, agent prompts and external-provider settings.
- Plausible first-party paths checked: Human approval callback, reviewer `approve`, system-prompt configuration, tool budget and read-only mode.
- Why no material first-party path remains: None handles identity/ultimate-policy disputes with a legitimate authority and binding returned decision; they enforce preselected task-level constraints.

## Distributed OSS parent arrangement

The developer of a composed team or an operator approving a tool is not evidenced as an organization-level parent S3/S4/S5 decision owner. Local developer intent cannot be projected to all deployments.

## Self-hosted and non-human modes

Providers can be swapped or injected and agents may be composed into a peer team; this changes execution plumbing, not a demonstrated autonomous non-human metasystem. In the configured reviewer constructor, the reviewer judgment remains distinct from deterministic team gating.

## Recursion

`AgentTool` can nest agents and `Team` can route among peers, but nesting alone lacks demonstrated durable distinct environments and complete local metasystems. No further recursive viability claim follows.

## Variety and escalation

Tools and providers amplify local task variety; permission checks, budget and rollback attenuate unsafe side effects. A reviewer correction is a potential complementary assurance signal into another S1's revision; general team message delivery is not a separate S2 conflict regulator. Ordinary budget exhaustion or event logs are not S3/S5/algedonic evidence.

## Evidence gaps

- No external provider-backed session or independent ground-truth tool audit was run; confidence for S3* is restricted to the constructor path, not efficacy on real software artifacts.
- The example's reviewer has no direct filesystem tool, so stronger source reality claims require explicit reviewer-tool composition and cannot be inferred from `approve` alone.
