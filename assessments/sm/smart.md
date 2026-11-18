---
harness_id: smart
project_name: SMART
repository: https://github.com/awslabs/social-messaging-agent-runtime-toolkit
review_ref: 2068968416fffc891d6d7ea42c641ff636c90f64
reviewed_at: 2026-11-18
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# SMART

## Review boundary

- System in focus: A SMART WhatsApp deployment with the first-party personal-assistant blueprint, the channel control layer, agent-side helpers and the optional integrated administration console.
- Purpose and identity: Answer users through WhatsApp and provide tool-backed messaging, per-user state and scheduled actions on AWS.
- Relevant environment: WhatsApp users and messaging provider, AWS account and Bedrock model, AgentCore hosting and memory, and authenticated stack operators.
- Standard-distribution boundary: Published CLI and SDK, deployable blueprints copied by the CLI, runtime helper package, channel Lambdas, Terraform and documented first-party console.
- Credited operating / distribution surfaces: Personal-assistant and appointment-scheduler tool-backed entrypoints, CLI scaffold and deploy path, webhook and notification delivery, scheduler and console operator controls.
- Adjacent first-party surfaces excluded from ownership: Repository CI and maintainers, local test fixtures, wholly user-supplied agent logic, and independent AWS platform governance. The default minimal blueprint's echo implementation supplies no model discretion.
- First-party operating / deployment modes considered: Minimal echo; shipped model-backed personal-assistant and appointment-scheduler blueprints; configured stack deployment with optional role-scoped admin console.
- Recursion level: One deployed SMART stack with user-scoped operational sessions and a separate authorized stack operator.
- Reviewed revision: 2068968416fffc891d6d7ea42c641ff636c90f64.
- Observation date: 2026-11-18.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The webhook layer normalizes a user message, resolves its session and invokes the deployed AgentCore runtime. The model-backed blueprints instantiate Strands with the supplied session manager and registered tools and return selected tool-produced messages plus a final response. SMART's control layer sends the result through the messaging service. The runtime helpers expose per-user state, notifications and scheduler operations. EventBridge and external events call separately configured handlers. With the optional admin console, a role-scoped operator can see stack health, conversations, schedules and deployment state and restart stack resources.

## Operational model

In model-backed blueprint mode a Strands agent chooses tool calls and responses for a user's conversation. The provider executes model requests, AgentCore hosts the configured agent, and SMART sends and schedules operational results. The default minimal blueprint only echoes. Operators can independently decide live actions on a deployed stack, while most channel controls are deterministic.

## S1 — Operations

- State: A
- Function: Respond to WhatsApp messages and execute selected tool-backed actions, such as persisting a preference, producing a rich reply or scheduling a reminder.
- Disturbance / variety regulated: Different messages, earlier conversation context, tool results and timing requests require different operational actions.
- Decisive decision or feedback right: Select which registered tools to invoke, their arguments and the response based on the available observations.
- Decision owner: The configured Bedrock model inside the first-party Strands deployment.
- Supporting / enforcement mechanisms: CLI blueprint copier, Bedrock AgentCore entrypoint, Strands session manager, outbound context, webhook and delivery provider.
- Closure path: Inbound messages reach the deployed blueprint. Tool effects change state, outbound messages or scheduled work; the tool result returns to the model and response is delivered to the user.
- Boundary reachability: The normal init command ships and copies the full first-party agent code and registered tools for the selected personal-assistant blueprint into the deployed project.
- Why this is / is not agent-owned: The model decides the next task step. The AWS transport and runtime helpers deliver and enforce the selected action.
- Evidence: [scaffold path](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/src/socialagent/cli/init.py#L100-L154), [model-backed entrypoint](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/blueprints/personal-assistant/agent.py#L75-L97), [tools and scheduler calls](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/blueprints/personal-assistant/src/tools/__init__.py), [webhook runtime call](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/src/socialagent/handlers/webhook.py), [default echo](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/blueprints/minimal/agent.py)
- Basis: structural
- Confidence: High
- Caveats: The minimum echo scaffold and generic channel are not the basis for this grade. Real model configuration and deployed services are needed.

## S2 — Coordination

- State: —
- Function: Attenuate disturbances between distinct operational agents or sessions that can interfere with each other.
- Disturbance / variety regulated: Multiple delivery attempts, short bursts of inputs and similar scheduled firings can coincide; user sessions can also possess overlapping context.
- Decisive decision or feedback right: No packaged relationship resolves conflict between independent operational agents' choices.
- Decision owner: Operator or downstream application owns any cross-session task conflict policy.
- Supporting / enforcement mechanisms: Message debounce and generation tokens, deterministic firing claims, user keys and atomic state primitives.
- Closure path: The same user's input gets debounced and duplicate firings can be suppressed. These paths protect the transport and one unit's event delivery, with no agent-level conflict feedback.
- Why this is / is not agent-owned: Deterministic deduplication and scoped keys address messaging consistency. They do not assign mutual adjustment among distinct operational units.
- Evidence: [message buffering](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/docs/message-buffering.md), [scheduled firing semantics](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/docs/events-scheduling.md#handling-scheduled-events), [per-user atomic state](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/docs/state.md)
- Basis: structural
- Confidence: High
- Caveats: Distinct task or user sessions are possible. No first-party shared-work interference contract was established.

### Absence scope

- Surfaces inspected: Webhook buffering and input generation, event and scheduler paths, user-scoped state and blueprint interaction rules.
- Plausible first-party paths checked: Same-user overlapping message batches, repeated scheduler firings, and two units contending for a shared task responsibility.
- Why no material first-party path remains: Found delivery coalescing, duplicate suppression and atomics. There is no shipped conflict-specific inter-agent coordination and corrective return.

## S3 — Inside-and-now control

- State: P
- Function: Intervene in current service operation based on health and commitments across the deployed SMART stack.
- Disturbance / variety regulated: Degraded channel functions, stuck runtime capacity or inconsistent scheduled/user workload can require an operator decision.
- Decisive decision or feedback right: Choose which stack component or ongoing schedule to intervene on, or initiate coordinated recovery across stack components under the appropriate role.
- Decision owner: The authorized stack operator or admin in the console deployment. SMART's API enforces role and dispatches the change.
- Supporting / enforcement mechanisms: Resource registry, observable per-stack health and alarms, error logs, schedules, role enforcement, restart routes and AWS control APIs.
- Closure path: Operator selects and issues a live intervention based on the current stack view. The backend applies it to the governing deployment resources, affecting subsequent invocations, schedules or service recovery.
- Boundary reachability: The optional first-party console links the registered stack to current metrics and state and exposes role-checked operations against the same runtime and Lambdas.
- Why this is / is not agent-owned: The human chooses the response to a real stack disturbance. The agent-facing reminders and deterministic processors do not set whole-stack commitments.
- Evidence: [console stack detail](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/docs/admin-console.md#stack-detail-tabs), [authority and role scope](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/docs/admin-console.md#authorization-roles-and-permissions), [runtime and Lambda operation](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/socialagent-admin-console/backend/routes/ops.py)
- Basis: structural
- Confidence: High
- Caveats: At the assessed stack recursion, this is an opt-in operator mode. It does not imply the operator owns model task decisions.
- Whole-system current view: Registered deployment status spans webhook, notification, event and scheduler functions, AgentCore runtime, error and metric signals and active schedules.
- Current-control decision scope: Role-scoped live restart of runtime and Lambda resources and the authorized intervention over active schedules or a degraded stack.

## S3* — Complementary audit

- State: —
- Function: Complement ongoing stack reporting with independent operational judgment and return corrective findings.
- Disturbance / variety regulated: Normal message and health reports may mask undelivered output or an incorrect model or tool result.
- Decisive decision or feedback right: No first-party audit actor or function-specific independent verdict-and-return constructor was identified.
- Decision owner: A console operator can inspect evidence and choose repairs under S3. No separate deployed review role or audit judgment pipeline was found.
- Supporting / enforcement mechanisms: AgentCore traces, delivery and CloudWatch records, conversation and usage views, and logs.
- Closure path: The console reports health and material operational records. The runtime supplies no distinct corroborating audit verdict with a specified corrective feedback path.
- Why this is / is not agent-owned: Observability and ordinary operator inspection expose evidence without assigning a separate complementary audit function.
- Evidence: [conversation and error views](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/docs/admin-console.md#stack-detail-tabs), [conversation operator backend](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/socialagent-admin-console/backend/routes/conversations.py), [delivery log semantics](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/docs/notifications.md)
- Basis: structural
- Confidence: Medium
- Caveats: Product CI and independent assurance a deployment may add are separate boundaries.

### Absence scope

- Surfaces inspected: Live logs, event observations, per-conversation memory and runtime tracing, role-scoped health and operation paths.
- Plausible first-party paths checked: Direct delivery evidence versus message results, memory-backed review of agent outcomes and corrective session or stack action.
- Why no material first-party path remains: The console exposes sources and ordinary monitoring. A deployed function making independent operational judgments and routing findings back is not specified.

## S4 — Outside-and-then intelligence

- State: —
- Function: Develop a future capability adaptation from external intelligence and apply it to the deployed service.
- Disturbance / variety regulated: External applications and WhatsApp provider conditions can alter future service needs.
- Decisive decision or feedback right: No packaged actor or specific parent path develops and selects adaptation options from outside-and-then information.
- Decision owner: Project developers determine what to change and deploy. Handlers act under rules for current events.
- Supporting / enforcement mechanisms: External event triggers, scheduled invocation, operator templates and deployment configuration.
- Closure path: The first-party context handles an incoming event or future scheduled task. It does not use that result to select how the organization's future capability will change.
- Why this is / is not agent-owned: Handling a future appointment or an external event is task execution. Updating the implementation is a separate deployment action.
- Evidence: [external events and schedules](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/docs/events-scheduling.md), [templates and routing](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/docs/templates.md), [appointment agent](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/blueprints/appointment-scheduler/agent.py), [deployment and model settings](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/docs/configuration.md)
- Basis: structural
- Confidence: High
- Caveats: No credit is assigned to future options described in the project roadmap.

### Absence scope

- Surfaces inspected: Event and scheduler entrypoints, blueprint tool loops, template synchronization and operator configuration.
- Plausible first-party paths checked: Event-triggered activity, remembered user state, provider classification alerts and new deployment settings.
- Why no material first-party path remains: These paths react, remember or execute selected changes. No bundled prospective model or parent feedback loop developing capability options was established.

## S5 — Policy and identity

- State: —
- Function: Route a standing identity or ultimate-policy dispute to a legitimate authority and apply the decision to service operation.
- Disturbance / variety regulated: Deployed agent purpose, policy and credentials may need authoritatively approved revision.
- Decisive decision or feedback right: No installed identity-policy escalation and authoritative decision flow was identified.
- Decision owner: Project owners author deployment policy and role settings outside the agent loop. Runtime and console enforce those chosen constraints.
- Supporting / enforcement mechanisms: Stack role membership, versioned Bedrock guardrails, deployment settings, channel constraints and fixed blueprint instructions.
- Closure path: Redeploying specified configuration can change which guardrail or prompt applies. Runtime checks implement the configured version and do not adjudicate an ultimate-policy matter.
- Why this is / is not agent-owned: Permission gates, provider templates and changeable guardrails do not themselves establish decision ownership over a routed identity or governing-policy issue.
- Evidence: [guardrail selection and versions](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/docs/configuration.md#guardrails), [console authorization](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/docs/admin-console.md#authorization-roles-and-permissions), [architecture authority boundary](https://github.com/awslabs/social-messaging-agent-runtime-toolkit/blob/2068968416fffc891d6d7ea42c641ff636c90f64/docs/adr/0001-two-runtime-layers.md)
- Basis: structural
- Confidence: Medium
- Caveats: A particular deployment can add a legitimate policy-governance process outside the assessed standard setup.

### Absence scope

- Surfaces inspected: Blueprint identity instructions, account role assignment, guardrail version propagation and console action approvals.
- Plausible first-party paths checked: Change guardrails, change permissions or user scope, escalate semantic disagreement to a parent and return an authoritative choice.
- Why no material first-party path remains: Reviewed tools apply supplied changes and defaults. They do not implement that policy matter, authorized adjudication and governing return as a packaged operating function.

## Recursion

A deployment is the system in focus. A user-scoped invocation is an operational session. AWS service hosting and the product maintainers' organization are outside this recursion.

## Variety and escalation

Typed channel inputs, session state, fixed scheduling and role checks constrain workload variety. The model decides within the tool set. An authorized operator can intervene against the active deployment using its own current view.

## Evidence gaps

Pinned source review only. No AWS resources were provisioned, no real account or model was used, and no separate semantic review or Index audit was performed.
