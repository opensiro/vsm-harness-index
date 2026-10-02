---
harness_id: sponsio
project_name: Sponsio
repository: https://github.com/SponsioLabs/Sponsio
review_ref: dfbdca2a224cdcdd56710283c60f48a45cdbbb17
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: proposed
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Sponsio

## Review boundary

- System in focus: the first-party Sponsio OSS contract-enforcement layer at frozen revision dfbdca2a224cdcdd56710283c60f48a45cdbbb17, including its deterministic contract compiler/evaluator, runtime monitor, framework adapters, session/action history, verdict strategies, CLI, observability and shipped contract library.
- Purpose and identity: inspect externally generated agent actions against declared contracts and return deterministic pass/block/warn/escalate/redirect outcomes, with trace and reporting support.
- Relevant environment: wrapped external agent/model loops, their tool calls and results, user-authored contracts, host framework state, optional human escalation callbacks, telemetry collectors and hosted rulebook workflows.
- Standard-distribution boundary: Sponsio's OSS monitor/evaluator/adapters and local control state are inside. Claude Code, OpenAI Agents, LangGraph/CrewAI/Google ADK/Vercel AI/OpenClaw and other wrapped reasoning/tool loops remain external. External model inference used by optional contract drafting/discovery is a dependency and is not the runtime enforcement owner.
- Credited operating / distribution surfaces: README.md; docs/concepts/architecture.md; docs/reference/oss-scope.md; sponsio/core.py; sponsio/runtime/monitor.py; sponsio/runtime/evaluators.py; sponsio/runtime/verifier.py; sponsio/runtime/strategies.py; sponsio/integrations/base.py; framework adapters; sponsio/generation/; sponsio/discovery/; session/trace/reporting surfaces.
- Adjacent first-party surfaces excluded from ownership: benchmark/eval harnesses and offline library-improvement work; CI/release/tests; hosted Cloud/Enterprise behavior not shipped in this OSS tree; maintainer review and repository governance.
- First-party operating / deployment modes considered: realtime integration-hook enforcement; post-hoc trace/reporting surfaces; CLI validation/check/report/eval; optional NL contract extraction; local plugins/adapters; hosted draft/publish/pull workflow only where documented by the OSS repository.
- Recursion level: one Sponsio enforcement/control layer around one or more external agents. Wrapped agents are environmental systems, not Sponsio S1 units.
- Reviewed revision: dfbdca2a224cdcdd56710283c60f48a45cdbbb17.
- Observation date: 2026-10-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Sponsio is intentionally a contract layer rather than an agent reasoning harness. Framework adapters intercept a wrapped agent's tool-call boundary, ground events into deterministic atoms, evaluate LTL/DFA contracts and return a verdict before or after the external action. The README and OSS-scope document explicitly state that the enforcement path makes no LLM call.

The decisive task-specific reasoning loop remains in the wrapped external agent. Sponsio can deny, warn, escalate or redirect an action selected elsewhere, and it can retain trace/history state needed for temporal contracts, but it does not itself interpret the user's open-ended objective, generate the next substantive operational action, observe that action's result and autonomously choose the next task action.

Optional natural-language extraction, discovery/scanning and benchmark-driven contract-library improvement exist outside the realtime enforcement owner. They can propose or compile constraints, but they do not turn the monitor into the autonomous operational agent whose actions are being governed.

Counterfactual owner test: remove the wrapped external agent while retaining Sponsio's monitor, contracts, adapters, trace state and verdict engine. The remaining system can evaluate supplied events and constraints, but it does not originate an open-ended operational trajectory. First-party autonomous S1 therefore does not close at the reviewed boundary.

Under Methodology 0.3.6, a repository without a first-party autonomous operational S1 is not retained in the autonomous-harness corpus by importing higher functions from the wrapped agent or by treating deterministic enforcement as agent ownership. This review therefore proposes the terminal disposition excluded-no-agentic-vsm for this frozen revision.

Primary evidence:

- [README.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/README.md) — Sponsio checks an agent's tool calls before execution and describes a deterministic, zero-LLM enforcement path.
- [docs/reference/oss-scope.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/docs/reference/oss-scope.md) — defines the shipped OSS engine as deterministic and states there is no LLM call on the enforcement path.
- [docs/concepts/architecture.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/docs/concepts/architecture.md) — integration hooks observe wrapped tool calls and can block them; the OTEL consumer path is described separately.
- [sponsio/core.py](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/sponsio/core.py) — public entry pattern wraps tools used by another agent rather than instantiating that agent's reasoning loop.

## Operational model

A wrapped agent chooses a tool call. Sponsio receives the event through an adapter, adds it to the monitored trace/context, evaluates configured formulas and produces an enforcement result. The adapter then blocks, warns, redirects, escalates or permits execution according to the selected strategy. Post-action evidence can be recorded and checked as well.

This is a meaningful first-party control function over an external operation, but it is not an autonomous S1 operation owned by Sponsio. The decisive open-ended action selection remains outside the assessed system. Because S1 admission fails, higher-function mechanisms are documented below as control/audit/adaptation candidates but are not published as positive autonomous-harness ownership states.

## S1 — Operations

- State: —
- Function: no first-party autonomous environment-facing agent operation is established.
- Disturbance / variety regulated: Sponsio regulates policy violations in actions proposed by an external agent, but it does not regulate open-ended task variety by selecting substantive operational actions itself.
- Decisive decision or feedback right: interpret an open-ended objective, choose the next substantive action/tool use, observe the result and choose what follows.
- Decision owner: the wrapped external agent/model loop, outside the Sponsio boundary.
- Supporting / enforcement mechanisms: contract compiler/evaluator, monitor state, integration hooks, verdict strategies, trace/session logs and adapters.
- Closure path: no first-party objective → agent decision → action → observation → next-agent-decision loop exists inside Sponsio; the first decision is supplied by the wrapped agent.
- Boundary reachability: shipped integrations require an existing external tool-calling loop and wrap/intercept its action boundary rather than replacing its reasoning owner.
- Why this is / is not agent-owned: removing the external agent leaves a deterministic event/contract monitor that can evaluate supplied calls but cannot originate an open-ended task trajectory.
- Evidence: [README.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/README.md); [docs/reference/oss-scope.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/docs/reference/oss-scope.md); [docs/concepts/architecture.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/docs/concepts/architecture.md); [sponsio/core.py](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/sponsio/core.py).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: deterministic blocking can materially change an external agent's behavior; that enforcement strength does not transfer the external agent's S1 decision ownership into Sponsio.

### Absence scope

- Surfaces inspected: runtime monitor/evaluators/verifier/strategies; framework adapters; contract/generation/discovery paths; CLI modes; trace/session/reporting; README and architecture/OSS-scope docs.
- Plausible first-party paths checked: verdict engine as autonomous S1; redirect strategy as task-action selection; optional NL contract generation as agent loop; discovery scanner as operational actor; daemon/CLI as autonomous execution owner.
- Why no material first-party path remains: each candidate either evaluates/rewrites caller-supplied constraints or regulates an action proposed elsewhere; none closes an open-ended first-party operational decision/action/feedback loop.

## S2 — Coordination

- State: —
- Function: no qualifying first-party inter-S1 coordination function is published at the reviewed Sponsio recursion.
- Disturbance / variety regulated: contracts can express permissions, segregation of duty, rate limits, data-flow or subagent constraints over external actors, but those actors are not first-party Sponsio S1 units.
- Distinct S1 units: not established inside the Sponsio boundary.
- Inter-S1 disturbance: not established between first-party Sponsio operational units.
- Attenuating coordination relation: configurable contracts can regulate externally supplied interactions, but this does not establish a first-party Sponsio S2 population.
- Feedback into subsequent S1 behaviour: verdicts return to wrapped external agents/frameworks, not to first-party Sponsio S1 units.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the shipped primitives are policy/enforcement over external events; no internal autonomous operational population is coordinated.
- Decisive decision or feedback right: not established for first-party S2 ownership.
- Decision owner: not established.
- Supporting / enforcement mechanisms: temporal contracts, permissions, segregation-of-duty/data-flow patterns, per-run context and enforcement strategies.
- Closure path: not applicable for an internal S2 finding.
- Boundary reachability: contracts are reachable in ordinary deployments, but their regulated S1 actors remain outside the assessed Sponsio system.
- Why this is / is not agent-owned: deterministic enforcement of user-selected coordination constraints does not supply an autonomous coordination actor or internal S1 population.
- Evidence: [docs/concepts/architecture.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/docs/concepts/architecture.md); [docs/reference/oss-scope.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/docs/reference/oss-scope.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: Sponsio can be a useful coordination-enforcement substrate for another organization; that constructor use does not import the other organization's S1/S2 ownership into this repository-relative assessment.

### Absence scope

- Surfaces inspected: multi-agent permission/data-flow patterns, subagent contracts, monitor context, adapters and enforcement strategies.
- Plausible first-party paths checked: segregation-of-duty as S2; subagent-depth limits; rate/loop controls; shared trace context as coordination.
- Why no material first-party path remains: the regulated agents are external, and no first-party Sponsio autonomous S1 units plus disturbance/attenuation/feedback witness are instantiated.

## S3 — Inside-and-now control

- State: —
- Function: no first-party whole-organization current-control loop over Sponsio-owned S1 commitments is established.
- Disturbance / variety regulated: monitor state and verdicts regulate each intercepted external action against preselected contracts.
- Whole-system current view: action history/context and traces expose monitored event state, not a live whole-system view of Sponsio-owned operational commitments/resources.
- Current-control decision scope: block/warn/escalate/redirect follows configured contract outcomes; no autonomous current allocation/prioritization/intervention across an internal S1 population is established.
- Decisive decision or feedback right: not established for S3.
- Decision owner: not established.
- Supporting / enforcement mechanisms: trace/history state, runtime monitor, verdict strategies, reporting and hosted visibility.
- Closure path: not applicable for a first-party S3 function.
- Boundary reachability: enforcement is shipped, but the regulated current operation belongs to wrapped external agents.
- Why this is / is not agent-owned: deterministic enforcement applies previously selected policy; it does not own whole-system current organizational discretion for Sponsio.
- Evidence: [README.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/README.md); [docs/concepts/architecture.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/docs/concepts/architecture.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: human escalation or hosted console supervision may regulate an external deployment, but no qualifying internal S3 loop is credited here.

### Absence scope

- Surfaces inspected: runtime monitor/history, verdict strategies, escalation callbacks, audit/trace/reporting and hosted-console documentation.
- Plausible first-party paths checked: monitor as S3 controller; escalation as parent S3; hosted run visibility; redirect as current-control decision.
- Why no material first-party path remains: the mechanisms enforce selected contracts against external actions and lack both an internal S1 population and a distinct whole-system current-control owner.

## S3* — Complementary audit

- State: —
- Function: no positive S3* ownership state is retained for the autonomous-harness corpus after first-party S1 admission fails.
- Disturbance / variety regulated: Sponsio provides strong independent policy checking and audit trails over external agent actions.
- Claim being audited: whether an external agent's actions conform to declared runtime contracts.
- Ordinary reporting path: the wrapped agent/framework supplies proposed actions and results through integration hooks.
- Complementary access path: Sponsio directly intercepts tool-call events and independently evaluates them against deterministic formulas.
- Independence boundary: the checker is first-party Sponsio and can be structurally separate from the wrapped external agent.
- Who acts on findings: the adapter/runtime can block/warn/redirect or invoke a human escalation callback; subsequent open-ended action remains owned externally.
- Decisive decision or feedback right: contract-conformance verdict over external actions.
- Decision owner: deterministic Sponsio evaluator under user/configured contracts rather than an autonomous audit agent.
- Supporting / enforcement mechanisms: formula evaluator, monitor, strategies, audit/session log and adapters.
- Closure path: external proposed action → Sponsio independent contract check → verdict → external framework/agent execution path changes.
- Boundary reachability: the audit/enforcement checker is shipped and directly wired by first-party adapters.
- Why this is / is not agent-owned: the checker is deterministic enforcement machinery, and the operational subject being audited is external to Sponsio; without first-party S1 admission this is not published as an autonomous-harness S3* state.
- Evidence: [docs/concepts/architecture.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/docs/concepts/architecture.md); [docs/reference/oss-scope.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/docs/reference/oss-scope.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: this negative publication state should not be read as denying Sponsio's practical audit/enforcement capability over other agent systems; it reflects the selected repository-relative autonomous-harness boundary.

### Absence scope

- Surfaces inspected: monitor/evaluator/verifier, integration hooks, audit/session logs, escalation/redirect strategies and reporting.
- Plausible first-party paths checked: deterministic verifier as S3*; audit trail as complementary access; hosted/OTEL reporting as independent audit.
- Why no material first-party path remains: the audit subject is an external agent and the decisive semantic judgment is deterministic contract evaluation; no first-party autonomous operational organization plus agent-owned complementary audit closure is established.

## S4 — Outside-and-then intelligence

- State: —
- Function: no first-party runtime prospective adaptation loop is established at the assessed boundary.
- Disturbance / variety regulated: discovery, scans, benchmark analysis and library iteration can inform future contracts, but the realtime OSS monitor applies the currently selected rule set.
- External distinction: benchmark threats, incident/CVE patterns and observed traces can supply external evidence.
- Future / prospective distinction: maintainers/users may use that evidence to revise future contract libraries.
- Adaptation option generated: scanners/optional extraction can propose contracts, but the decisive adoption/revision loop is not autonomously closed by the runtime.
- Path back into current capability / S3: contract/library changes require user/maintainer selection or external workflow before later enforcement.
- Decisive decision or feedback right: not established as autonomous runtime adaptation.
- Decision owner: user/maintainer/external workflow for the reviewed paths.
- Supporting / enforcement mechanisms: discovery extractors, optional NL extraction, eval replay, versioned contract library and hosted draft/publish workflow.
- Closure path: no standard-distribution autonomous sense → model future → choose adaptation → reinject capability loop is established.
- Boundary reachability: discovery/eval tools are shipped, but autonomous adoption authority is not.
- Why this is / is not agent-owned: tooling can generate evidence/proposals; it does not own the prospective organizational adaptation decision.
- Evidence: [docs/reference/benchmarks.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/docs/reference/benchmarks.md); [docs/reference/oss-scope.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/docs/reference/oss-scope.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: historical library self-improvement demonstrates a development process, not a shipped autonomous S4 owner.

### Absence scope

- Surfaces inspected: discovery, generation, eval/benchmark docs, library versioning, hosted draft/publish flow and runtime enforcement path.
- Plausible first-party paths checked: benchmark self-improvement as S4; scan-generated contracts; NL extraction; incident-library updates; hosted rulebook publication.
- Why no material first-party path remains: prospective evidence and proposal generation exist, but authoritative adaptation selection and reinjection depend on humans/external workflows rather than a first-party autonomous runtime loop.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime identity/ultimate-policy authority loop is established for Sponsio as an autonomous organization.
- Disturbance / variety regulated: contracts and rulebooks encode operational policy for external agents, including permissions, forbidden actions and escalation behavior.
- Identity / ultimate-policy issue: not established at Sponsio's own organizational identity recursion; configured contracts specify external operational constraints rather than resolving Sponsio's identity/ultimate policy.
- Ultimate authority in each claimed mode: users/project owners author/review/publish rulebooks; Sponsio enforces the resulting configuration.
- Return-to-operation path: selected contracts are loaded into the monitor and govern later external agent actions, but this is operational policy configuration rather than an evidenced S5 identity-resolution loop for Sponsio.
- Decisive decision or feedback right: not established for Sponsio identity/ultimate policy.
- Decision owner: no qualifying S5 owner is established.
- Supporting / enforcement mechanisms: YAML contracts, CLI config, hosted draft/publish/pull, runtime strategies and adapters.
- Closure path: not applicable for a positive S5 claim.
- Boundary reachability: policy enforcement is shipped; identity/ultimate-policy resolution is not.
- Why this is / is not agent-owned: strong configured guardrails and human publication authority do not become S5 merely because they constrain action; the function-first identity/ultimate-policy threshold is not met.
- Evidence: [README.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/README.md); [docs/reference/oss-scope.md](https://github.com/SponsioLabs/Sponsio/blob/dfbdca2a224cdcdd56710283c60f48a45cdbbb17/docs/reference/oss-scope.md).
- Basis: explicit + structural negative review.
- Confidence: high.
- Caveats: parent humans clearly own rulebook publication in the hosted mode, but ordinary policy configuration is not sufficient to establish Profile S5.

### Absence scope

- Surfaces inspected: rulebook/config model, hosted draft/publish/pull workflow, enforcement strategies, escalation paths and project/runtime documentation.
- Plausible first-party paths checked: rulebook publisher as parent S5; contract hierarchy as identity policy; escalation-to-human as S5; permissions as S5.
- Why no material first-party path remains: inspected paths set or enforce operational constraints for external agents without an identity/ultimate-policy tension-and-resolution loop at Sponsio's own recursion.

## Recursion

Sponsio is assessed as a control layer around external agent organizations. Its adapters can sit inside many host stacks, but the wrapped agents' reasoning loops remain separate systems. This prevents external S1/S2/S3/S3*/S4/S5 capabilities from being inherited merely because Sponsio can observe or constrain their actions.

## Variety and escalation

Sponsio attenuates action variety through contracts, temporal formulas, permissions, rate/loop bounds, block/warn/redirect strategies and escalation callbacks. It preserves action history and audit evidence. These are substantive control capabilities, but the autonomous-harness Index requires first-party autonomous S1 ownership before retaining the repository as an included harness.

## Evidence gaps

- Hosted Cloud/Enterprise internals are not part of the public OSS frozen boundary and are not used for ownership claims.
- Optional external LLM extraction can assist contract drafting, but no standard-distribution autonomous operational loop was found around it.
- The repository describes historical benchmark/library improvement cycles; those are development/evaluation evidence rather than runtime S4 closure.
- The exclusion is frozen-ref-specific and does not claim Sponsio lacks practical value as a guardrail/control product.

## Assessment summary

At frozen revision dfbdca2a224cdcdd56710283c60f48a45cdbbb17, Sponsio is a deterministic first-party contract enforcement and audit layer around external agent loops. It materially changes those agents' permitted actions, but the open-ended operational S1 decision/action/feedback loop remains outside the Sponsio boundary. Under Methodology 0.3.6, the canonical terminal disposition should therefore be excluded-no-agentic-vsm for this frozen ref.

**Vector:** — · — · — · — · — · —
