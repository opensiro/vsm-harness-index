---
harness_id: hexagon
project_name: Hexagon
repository: https://github.com/NexusFox88/Hexagon
review_ref: 0998e49765d803fe4cd9b22f2b4c529190b975cc
reviewed_at: 2026-11-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: P
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# Hexagon

## Review boundary

- System in focus: self-managed Hexagon tenant fleet control plane plus standard deployed built-in Pi/OpenCode agent runtime.
- Purpose and identity: execute application-submitted model tasks in controlled cloud sandboxes, preserve sessions and results.
- Relevant environment: tenant/application, cloud sandbox and model providers, protected tools, paid compute and uncertain remote outcomes.
- Standard-distribution boundary: control-plane server, modules/execution, runtime, built-in pinned Pi/OpenCode installation adapters and tools, Console/SDK. External provider/model internals and business application excluded.
- Credited operating / distribution surfaces: built-in harness integrations actually registered in server, cloud execution worker, run/session lifecycle, fleet/resource control, evidence-bound tool reconciliation.
- Adjacent first-party surfaces excluded from ownership: testing/evidence and tooling acceptance/audits, development plans/release governance, examples as independent actors; arbitrary unconfigured OCI harnesses.
- First-party operating / deployment modes considered: configured built-in Pi or OpenCode in supported sandbox, continued native session, operator/API management, pause/resume and unknown-outcome reconciliation.
- Recursion level: one tenant fleet of separate operational sessions plus tenant management parent.
- Reviewed revision: 0998e49765d803fe4cd9b22f2b4c529190b975cc.
- Observation date: 2026-11-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

PostgreSQL owns run/session and event state; a leased worker provisions a sandbox and installs the registered harness, launches it with scoped model/tool connections and records results. Built-in versioned Pi and OpenCode adapters provide actual model-directed execution, not just API contracts. Console and SDK manage current fleet and resources. Unknown remote operations have explicit evidence-based resolution paths. See [README.md](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/README.md), [modules/execution/worker.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/worker.ts#L58-L189), [apps/control-plane/server.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/apps/control-plane/server.ts).

## Operational model

One session is an operating cell with native model context, task tools and outcome. The built-in model owns action choice; runtime enforces connection/lifecycle constraints. Tenant management owns current fleet interventions. No arbitrary custom harness or external app autonomy is imported.

## S1 — Operations

- State: A
- Function: Execute user/application-submitted model-directed tasks in a cloud workspace and deliver results/artifacts.
- Disturbance / variety regulated: Uncertain task environment, model/tool outcomes, connection availability.
- Decisive decision or feedback right: Select and revise actions using model feedback and return task result.
- Decision owner: Model-backed Pi or OpenCode operational agent in built-in supported combination.
- Supporting / enforcement mechanisms: Versioned adapter, sandbox, worker/runtime process, broker, events, credentials and artifacts.
- Closure path: Worker launches native harness, brokers model-selected tool requests/results, captures exit and artifacts; native session can continue.
- Boundary reachability: Built-in registry wires Pi/OpenCode; worker installs exact version and starts configured native agent, not merely a hypothetical external integration.
- Why this is / is not agent-owned: Without model, orchestration can provision and transport but cannot choose task action. Agent engine is pinned packaged dependency; no generic custom OCI autonomy assumed.
- Evidence: [apps/control-plane/main.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/apps/control-plane/main.ts#L17-L54), [integrations/harnesses/pi.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/integrations/harnesses/pi.ts#L11-L65), [integrations/harnesses/opencode.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/integrations/harnesses/opencode.ts#L33-L79), [modules/execution/worker.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/worker.ts#L125-L189), [modules/execution/worker.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/worker.ts#L231-L253)
- Basis: explicit
- Confidence: high
- Caveats: Developer preview; only supported configured combinations; not proof all adapters run.

## S2 — Coordination

- State: —
- Function: No demonstrated inter-S1 discretionary coordination relation across fleet sessions.
- Disturbance / variety regulated: Potential interference of distinct agents on shared external resources.
- Decisive decision or feedback right: No function-specific inter-S1 decision/feedback path established.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Separate sandbox sessions, row locks, per-run worker leases, tool request idempotency and connection gates.
- Closure path: Per-session busy rejection and duplicate worker/tool fencing regulate one session/run, not mutual adjustment between distinct agents.
- Why this is / is not agent-owned: Sandbox separation is per-session topology; no shipped agent-to-agent conflict response or coordination constructor for shared external tools established.
- Evidence: [modules/execution/runs.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/runs.ts#L24-L63), [modules/execution/runs.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/runs.ts#L79-L105), [modules/execution/sessions.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/sessions.ts#L123-L180), [modules/execution/worker.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/worker.ts#L58-L85), [modules/tools/reconciliation.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/tools/reconciliation.ts#L43-L68)
- Basis: structural
- Confidence: medium
- Caveats: Multiple sessions share a tenant but no distinct inter-S1 collision witness beyond potential generic competition.

### Absence scope

- Surfaces inspected: Session/run and worker admission, sandbox isolation, tool broker/reconciliation, fleet and connection binding docs.
- Plausible first-party paths checked: Same-session busy gate, worker leases, stable connection locks, per-call replay protection, independent sandbox provisioning.
- Why no material first-party path remains: These ensure consistency of one operation or deterministic tenancy isolation; no material inter-S1-specific feedback/decision path shown.

## S3 — Inside-and-now control

- State: P
- Function: Tenant management identity regulates current agent commitments and shared paid execution resources.
- Disturbance / variety regulated: Concurrent sessions, active runs, idle/uncertain cloud resources and competing priorities.
- Decisive decision or feedback right: Choose which run to cancel, which session/sandbox to pause, resume or close, and whether to reconcile resources.
- Decision owner: Legitimate tenant operator/application management authority.
- Supporting / enforcement mechanisms: Fleet projection, lifecycle and run endpoints, provider inspection, cancel intent, fenced worker and cleanup.
- Closure path: Selected cancel reaches runtime; session pause/resume/close changes current compute and admissible execution with state/event readback.
- Boundary reachability: First-party fleet API and Console expose current sessions, runs and resources; owner commands invoke run/lifecycle methods directly.
- Why this is / is not agent-owned: No shipped agent with whole-fleet view and decision authority; deterministic idle/expiry cleanup enforces predefined constraints; general management APIs do not establish autonomous controller composition.
- Evidence: [modules/execution/sessions.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/sessions.ts#L202-L214), [apps/control-plane/server.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/apps/control-plane/server.ts#L122-L150), [apps/control-plane/server.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/apps/control-plane/server.ts#L242-L247), [modules/execution/worker.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/worker.ts#L155-L189), [modules/sandboxes/lifecycle.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/sandboxes/lifecycle.ts#L135-L190), [modules/sandboxes/lifecycle.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/sandboxes/lifecycle.ts#L212-L275)
- Basis: explicit/structural
- Confidence: high
- Caveats: Fleet projection bounded to latest 200; scope tenant resources/commitments, not cloud provider or business policy. Pause may be logical, not zero billing.

- Whole-system current view: tenant fleet lists sessions with latest run, runtime and resource operations; complete session listing and detailed resource records support inspection.
- Current-control decision scope: tenant management identity selects cancellation, pause/resume/close or resource reconciliation on behalf of current fleet operation.

## S3* — Complementary audit

- State: C
- Function: Enable external reality check of uncertain tool effects and return evidence-bound resolution rather than trusting missing/ambiguous ordinary receipt.
- Disturbance / variety regulated: Remote side effect may complete while its response is lost; blind retry can duplicate action.
- Decisive decision or feedback right: Independently determine actual outcome and provide request-bound evidence to resolve uncertainty.
- Decision owner: Management caller/externally composed independent reviewer; not shipped autonomous auditor.
- Supporting / enforcement mechanisms: Unknown-outcome gate, typed resolution evidence, request hash and advisory lock, runtime tool-results delivery.
- Closure path: Caller verifies external effect and submits completed/failed result with evidence; broker then returns completed result to active runtime; no automatic unsafe retry.
- Boundary reachability: First-party tool reconciliation API and operator documentation explicitly expose evidence-based outcome resolution; separately queried provider-resource reconciliation is adjacent corroborating operational check.
- Why this is / is not agent-owned: Removing reviewer leaves unknown outcome blocked; runtime records/delivers verdict but does not own independent judgment.
- Evidence: [modules/tools/reconciliation.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/tools/reconciliation.ts#L6-L14), [modules/tools/reconciliation.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/tools/reconciliation.ts#L39-L68), [modules/execution/worker.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/worker.ts#L158-L168), [modules/sandboxes/operations.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/sandboxes/operations.ts#L23-L38), [docs/product/en/operate/reconciliation.md](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/docs/product/en/operate/reconciliation.md)
- Basis: explicit/structural
- Confidence: medium
- Caveats: Restricted to exceptional outcome reconciliation, not general product quality audit. Caller must independently obtain evidence; code does not verify truth of arbitrary evidence text; no A claim.

- Claim being audited: actual completion/failure of an uncertain external tool invocation identified by request hash.
- Ordinary reporting path: tool broker response and runtime events/results; remote lost response leaves unknown.
- Complementary access path: caller-verified external application/provider effect, outside the ordinary call receipt, then typed resolution carrying evidence.
- Independence boundary: management caller obtains external evidence separately; hash/lock fences exact invocation; independent actor and access must be composed.
- Who acts on findings: caller submits resolution and runtime receives recorded result; no shipped autonomous audit actor.

## S4 — Outside-and-then intelligence

- State: —
- Function: No first-party prospective external adaptation decision loop at tenant fleet boundary.
- Disturbance / variety regulated: Future external provider capabilities, changing environment and opportunities.
- Decisive decision or feedback right: No externally informed future-option judgment returning into capability.
- Decision owner: None established.
- Supporting / enforcement mechanisms: Harness/model registry and compatibility check, versioned agent config, provider lifecycle sensing, test matrix.
- Closure path: Operator chooses supported combination or new config; runtime applies fixed contracts, not a prospective feedback loop.
- Why this is / is not agent-owned: Compatibility catalog, recovery and release/testing plans do not establish future adaptation; external model performing user's current research is S1.
- Evidence: [modules/execution/sessions.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/sessions.ts#L49-L103), [modules/execution/sessions.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/sessions.ts#L152-L175), [modules/execution/worker.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/worker.ts#L219-L230), [README.md](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/README.md)
- Basis: structural
- Confidence: medium
- Caveats: Provider adapters and custom OCI are extensibility, not demonstrated S4.

### Absence scope

- Surfaces inspected: Registry, sessions/agent revision and compatibility path, lifecycle, README and release/test docs.
- Plausible first-party paths checked: Provider capability checks, custom version registration, future configs, compatibility evidence, idle recovery.
- Why no material first-party path remains: No shipped prospective environmental model generating adaptation options and returning selected capability changes, including parent mode.

## S5 — Policy and identity

- State: —
- Function: No runtime identity/ultimate-policy issue resolution at tenant fleet boundary.
- Disturbance / variety regulated: Potential tensions between present operations and future identity.
- Decisive decision or feedback right: No ultimate policy decision loop established.
- Decision owner: External application owns business identity; management configures agent definitions.
- Supporting / enforcement mechanisms: Agent identity/instructions, revision history, pinned session initialization, access policy and approvals.
- Closure path: New sessions may pin revised configuration, but no runtime identity-level issue routed to legitimate authority and returned.
- Why this is / is not agent-owned: Identity strings and versioned configuration do not establish a runtime S5 decision channel; ordinary per-tool approval is not identity arbitration.
- Evidence: [modules/execution/sessions.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/sessions.ts#L17-L45), [modules/execution/sessions.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/sessions.ts#L72-L103), [modules/execution/sessions.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/sessions.ts#L123-L180), [modules/execution/runs.ts](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/modules/execution/runs.ts#L181-L200), [README.md](https://github.com/NexusFox88/Hexagon/blob/0998e49765d803fe4cd9b22f2b4c529190b975cc/README.md)
- Basis: structural
- Confidence: medium
- Caveats: No credit for external application governance outside assessed product.

### Absence scope

- Surfaces inspected: Agent revision/session pinning, approvals, access policy, fleet API, README boundary.
- Plausible first-party paths checked: Owner revision of identity/instructions, approval/revocation, management controls, application responsibility.
- Why no material first-party path remains: Static/revised configuration and operation approvals do not show identity issue reaching ultimate authority and returning as governance at chosen recursion.

## Recursion

Separate sessions are operational cells; no complete child viable-system structure inferred.

## Variety and escalation

Fenced leases, runtime events, scoped credentials, pause/cancel and unresolved remote outcome review preserve operational distinctions; no independent algedonic channel claimed.

## Evidence gaps

Static source review only, exact frozen commit restored after an initial incomplete clone. No cloud or model run, independent semantic audit or blanket compatibility claim. S3* is limited to caller-verified uncertain effects. External business identity and provider operation are outside this boundary.
