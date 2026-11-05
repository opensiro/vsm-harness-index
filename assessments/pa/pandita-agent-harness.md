---
harness_id: pandita-agent-harness
project_name: Pandita Agent Harness
repository: https://github.com/bhandiwad/agent-harness
review_ref: 0827a48d5131537216e74cabd2acf78f0138686b
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Pandita Agent Harness

## Review boundary

- System in focus: The first-party Pandita generic agent service, its configured assistant and durable worker, not the surrounding AgentFabric application or a tenant's wider human organization.
- Purpose and identity: Turn a user's conversation request into a bounded, model-selected sequence of local or connected tool actions, preserve state and return accountable results or pauses.
- Relevant environment: User requirements, tenant/workspace permissions, model endpoint, local files and external tool responses, concurrent sessions, identity issuer, independent action approver and runtime failures.
- Standard-distribution boundary: The installable Python `pandita_agent` service and worker; the documented single-assistant configuration and explicitly supported optional specialist team/delegation mode. Real endpoints and credentials are operator-supplied.
- Credited operating / distribution surfaces: [runner and model/tool feedback](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py), [specialist handoff](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/teams.py), [session storage](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/storage.py), [agent contract](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/contracts.py) and [installed example config](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/config/agent.json).
- Adjacent first-party surfaces excluded from ownership: Optional maintenance-agent/demo and authoring examples, test stubs, CI validation and upstream/provider tool internals; their specific claims cannot be donated to an unconfigured service instance.
- First-party operating / deployment modes considered: One configured assistant with local tools; a developer-configured specialist team/delegate chain; external tool connections with separate approval and reconciliation; code-agent mode, session resume and completion checks. No live provider-backed tenant deployment is attested.
- Recursion level: One user-facing assistant as S1, potentially using bounded specialist steps inside the same session; no established autonomous federation of viable organizations.
- Reviewed revision: `bhandiwad/agent-harness@0827a48d5131537216e74cabd2acf78f0138686b` (Apache-2.0).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

`Runner` loads configured agents/models/connections, authorizes the session owner, and persists revision-checked state in PostgreSQL. `tick` advances a queued run through model or code steps, then external or native tools, accumulating tool receipts and preserving cancelled/interrupted/uncertain outcomes. `model_step` sends instructions/history/available tool schemas to the configured provider; a model-chosen call becomes pending, and `execute_tool` validates permissions, arguments, possible independent human approval and a confirmed receipt before feeding the result back to the model. The basic distribution has one `assistant`, a placeholder model endpoint, native file/calculation tools and no connected external adapters. Optional `team` members run sequentially in the same parent session, or a configured delegate can be called within a bounded frame depth. Completed answers may undergo developer-installed schema/acceptance callbacks, which are not automatically independent audits. See [runner](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py#L486-L572), [model step](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py#L572-L740), [tool dispatch](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py#L980-L1139), and [team transitions](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/teams.py).

## Operational model

The configured assistant selects substantive responses or permissible tools from live model feedback and session evidence. The runtime enforces a configured authorization/budget/dependency envelope but does not choose the task goal or the agent's discretionary next action. A specialist frame is a bounded operation within the same request, not an independently governed S1 merely because it has a role. Runtime permission/approval, completion check, audit trail and replay are kept separate from VSM metasystem ownership.

## S1 — Operations

- State: A
- Function: Model-directed task execution and conversational/file/tool work with successive observations.
- Disturbance / variety regulated: User changes, variable model output, local file contents, tool errors, context and permission limits.
- Decisive decision or feedback right: The model chooses a tool name/arguments, delegates to an allowed specialist or returns a final answer; subsequent tool receipts can alter its next choice.
- Decision owner: The configured assistant model, within operator-set tool schemas and permission bounds.
- Supporting / enforcement mechanisms: Durable session/turn history, PostgreSQL writer lock, budgets, installed adapters, native tools, separate approver and receipt validation.
- Closure path: User turn → model generation → selected tool or final response → verified tool result/feedback appended → next agent model step or terminal answer.
- Boundary reachability: The shipped `Runner.tick` and `model_step` are wired from the installable worker and current `config/agent.json` gives the assistant selectable native file tools; a real provider endpoint must be configured by the operator.
- Why this is / is not agent-owned: Removing the model leaves authorization and state transitions, but no discretionary interpretation of the user task or choice among tools; hence S1 choice is agent-owned.
- Evidence: [installed config](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/config/agent.json), [model/tool loop](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py#L572-L740), [dispatch](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py#L980-L1139).
- Basis: structural.
- Confidence: High for first-party wiring, not for untested live model behavior.
- Caveats: Endpoint/keys and tenant authorization need real deployment; API limits and approval are external constraints, not autonomous owner rights.

## S2 — Coordination

- State: —
- Function: No shipped closed attenuation relation between distinct concurrently operating S1 organizations is demonstrated.
- Disturbance / variety regulated: Potential conflicting specialist work or concurrent session writes; team handoff data and writer locking address different local hazards.
- Decisive decision or feedback right: No distinct inter-S1 coordination actor decides a response to concrete peer conflict; fixed team order and single-session concurrency prevent local overlap.
- Decision owner: Root S1 chooses permitted delegation; deterministic session code serializes handoffs.
- Supporting / enforcement mechanisms: Specialist `team` sequence, parent frames, Postgres writer lock and configured active-session capacity.
- Closure path: Root task → specialist result → root context; no peer-interference observation → coordination judgment → revised independent S1 commitments loop.
- Why this is / is not agent-owned: Sequencing a hierarchy and blocking concurrent writes do not by themselves establish independent S1-unit oscillation regulation.
- Evidence: [team handoff/return](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/teams.py), [session ownership](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py#L192-L301), [storage](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/storage.py).
- Basis: structural bounded absence.
- Confidence: Medium-high.
- Caveats: A tenant could build a fleet with external coordination; no S2-specific packaged correction relation was established here.

### Absence scope

- Surfaces inspected: Installed config, specialist `teams.py`, delegate frames and session/storage locking.
- Plausible first-party paths checked: Delegated specialist conflict, multiple sessions sharing a workspace, serial team handoff and writer contention.
- Why no material first-party path remains: They serialize local execution or return task outputs but provide no identified peer S1 interference, discretionary attenuation relation and subsequent peer-behavior feedback in the reviewed standard modes.

## S3 — Inside-and-now control

- State: —
- Function: No separately owned whole-system current-control function over a portfolio of autonomous operations is established.
- Disturbance / variety regulated: Session concurrency, budget exhaustion, cancellation, uncertain external writes and approval delays.
- Decisive decision or feedback right: Configuration/tenant owner sets limits and agent roster; runtime enforces caps and halts risky states, rather than autonomously revising whole-system resource/commitment priorities.
- Decision owner: Operator/developer for configuration and human approver for action permission; model for its own S1 task steps.
- Supporting / enforcement mechanisms: `max_steps`/tokens/time, session locks, access-control checks, approval digest and reconciliation guard.
- Closure path: Fixed limit violation → fail/pause/deny/reconcile; no evidenced autonomous or legitimate parent current-control bargaining and returned cross-unit decisions.
- Why this is / is not agent-owned: Removing the model leaves static limit enforcement, not a discretionary portfolio-control decision. Team delegation is task decomposition, not S3 by name.
- Evidence: [config and capacities](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/config/agent.json), [run limits/recovery](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py#L486-L572), [approval/receipt enforcement](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py#L1009-L1119).
- Basis: structural bounded absence.
- Confidence: Medium-high.
- Caveats: A broader tenancy operation may have S3 outside this agent-service boundary.

### Absence scope

- Surfaces inspected: Agent/settings contracts, default assistant config, worker loop, session/capacity protection, optional team control and independent approval.
- Plausible first-party paths checked: Root team orchestration as whole-system manager, workspace capacity as resource allocation, separate approver as parent S3, recovery as intervention.
- Why no material first-party path remains: Each is a fixed constraint or local task/permission gate without an authority with whole-system current view that revises operational commitments in the selected distribution.

## S3* — Complementary audit

- State: —
- Function: No default complementary, sufficiently independent audit of operational claims is wired into a corrective governance path.
- Disturbance / variety regulated: Incorrect answers, unconfirmed tool side effects and fabricated completion.
- Decisive decision or feedback right: The optional `completion_check` callback can reject format/content against a developer-supplied checker; tool receipts confirm transport outcomes, but no first-party separate reality-inspecting auditor makes an independent judgment.
- Decision owner: Configured callback/adapter and deterministic runtime for validation; no S3* audit owner established.
- Supporting / enforcement mechanisms: Tool result schema checks, write receipts, completion schema/check callbacks, test suite and event log.
- Closure path: Model answer → optional direct callback → retry/fail, or tool invocation → receipt → model; this is routine completion/tool validation, not complementary audit access to independent operational reality.
- Why this is / is not agent-owned: An injected callback can be implemented by an external evaluator, but no shipped audit-specific independent actor/path is present or owned by a first-party standard mode.
- Evidence: [completion check and rejection](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py#L700-L810), [tool receipt validation](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py#L1031-L1139).
- Basis: structural bounded absence.
- Confidence: Medium-high.
- Caveats: An application can install an independent checker, but generic callback extensibility alone does not supply a first-party S3* mode.

### Absence scope

- Surfaces inspected: Completion check registration and return, tool outcome reconciliation, first-party team/approval interfaces and shipped tests/configuration.
- Plausible first-party paths checked: Completion checker as independent verifier, receipt checks as raw-artifact audit, specialist QA as separate audit, event history as complementary evidence.
- Why no material first-party path remains: The standard service has no separately reached, independent reality-accessing audit judgment returned to whole-system control; validation and logging are in the ordinary execution/acceptance path.

## S4 — Outside-and-then intelligence

- State: —
- Function: No closed external-and-prospective adaptation cycle for future harness capability is installed.
- Disturbance / variety regulated: Changing model providers, tools, user needs and knowledge; context windows and new requirements.
- Decisive decision or feedback right: User/developer changes the model/tool configuration and prompts, while agent research occurs only within the current request.
- Decision owner: Operator/developer for future capacity; same S1 model for present task response.
- Supporting / enforcement mechanisms: Configured model aliases, skills, context history/archive, provider protocol adapter and optional specialist handoff.
- Closure path: Manual config changes can affect later execution; no product-owned future-environment sensing → adaptation option judgment → feedback into present S3/capability.
- Why this is / is not agent-owned: Context/history retention and task planning optimize current work; they do not authorize an agent to revise its organizational future capability.
- Evidence: [settings and agent contracts](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/contracts.py), [context construction](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py#L423-L475), [installed config](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/config/agent.json).
- Basis: structural bounded absence.
- Confidence: High.
- Caveats: Separate maintenance-agent examples do not automatically wire future adaptation into the deployed generic assistant.

### Absence scope

- Surfaces inspected: Generic runtime, configuration and model selection, context/history/skills and separately packaged development/demo examples.
- Plausible first-party paths checked: Long-term conversation history as learning, model selection as adaptation, optional specialist as environment scanner and maintenance demo as self-improvement.
- Why no material first-party path remains: No supported generic-mode strategic environmental model and consequential prospective adaptation return is wired; external modifications are operator choices.

## S5 — Policy and identity

- State: —
- Function: No first-party identity/ultimate-policy dispute resolution loop at the assessed agent-service recursion.
- Disturbance / variety regulated: Access violations, disallowed tools, untrusted input and action approval.
- Decisive decision or feedback right: Tenant operator and external identity authority supply authorizations and policy; independent actor approves a particular write action, not ultimate organizational identity.
- Decision owner: External operator/IdP/approver for fixed permissions; none for a packaged S5 function.
- Supporting / enforcement mechanisms: RS256 identity verification, role permissions, immutable configuration digest, approval digest and untrusted-input isolation.
- Closure path: Token/policy match → permitted/denied session/tool; action approval returns one tool gate, not an identity-level dispute → legitimate authority decision → enduring operating-policy return.
- Why this is / is not agent-owned: Agent instructions explicitly treat tool output as data and cannot change policy authority. Human approval is narrow execution consent, not S5.
- Evidence: [authorization and config digest](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py#L185-L220), [approval logic](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/src/pandita_agent/agent/runner.py#L336-L355), [policy/identity config](https://github.com/bhandiwad/agent-harness/blob/0827a48d5131537216e74cabd2acf78f0138686b/config/agent.json).
- Basis: structural bounded absence.
- Confidence: High.
- Caveats: A separate operating institution may exercise S5 outside the declared product boundary.

### Absence scope

- Surfaces inspected: Role/policy and identity configuration, authorization code, agent system instructions, action approval, and README operating boundary.
- Plausible first-party paths checked: External IdP as S5 parent, write approver as policy authority, static instructions as constitution, tenant config as ultimate-policy feedback.
- Why no material first-party path remains: These enforce preselected permissions or decide individual actions; no first-party reachable path adjudicates an identity/ultimate-policy question and returns a new binding organizational mandate.

## Recursion

The service can compose specialists and nested delegated frames, but their bounded role handoffs do not establish independently viable S1 units with own metasystems. No additional organizational recursion is asserted.

## Variety and escalation

The model and bounded tool connections amplify operational response variety. Capability filtering, authorization, budgets, session locking, tool-schema checks and approval attenuate risky or expensive paths. A specific write can reach a distinct approver; cancellations and unknown outcomes are halted for reconciliation. These are operational protection/escalation, not evidence of separate S3/S4/S5 ownership or an algedonic channel.

## Evidence gaps

- Source-traced pinned first-party paths and shipped configuration were inspected; no live tenant, PostgreSQL, provider API or external write endpoint was executed. Actual reliability and model decision quality are not claimed.
- Optional customer-installed completion checks, connector backends and wider tenant organization may realize functions outside the credited standard mode; the checked generic extension interfaces alone do not establish those functions.
- The bounded negative findings apply to this distribution, not to every possible developer composition.
