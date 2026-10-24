---
harness_id: reins
project_name: Reins
repository: https://github.com/shamspias/reins
review_ref: 69d5ae7e3f2336366e7567b7a476e7c71608f226
reviewed_at: 2026-10-20
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

# Reins

## Review boundary

- System in focus: Open-source Reins agent harness acting on one embedding application's registered capabilities to pursue a caller goal, under the shipped model/tool and admission/gate/record interfaces.
- Purpose and identity: A multi-language app-native LLM operational agent that selects registered verbs, observes results and returns a task answer; not a multi-department managerial organization by default.
- Relevant environment: Python 3.11+ package with Anthropic/OpenAI-compatible provider adapters, TypeScript and Go packages, application-defined callable registry or ORM binding, user-provided principal, configured provider and optional terminal approval or injected handler/sandbox.
- Standard-distribution boundary: Shipped Python `Agent.ask` / `Agent.run` and `run_loop` with external configured model; corresponding TypeScript/Go model/loop/registry/policy code where implemented. No application-specific business organization, hosted provider internal strategy, benchmark fixtures or future roadmap is treated as first-party metasystem.
- Credited operating / distribution surfaces: [packages/python/src/reins/loop.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/loop.py); [packages/python/src/reins/model.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/model.py); [packages/python/src/reins/registry.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/registry.py); [packages/python/src/reins/policy.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/policy.py); [packages/python/src/reins/approval.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/approval.py); [packages/python/src/reins/audit.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/audit.py); [packages/js/src/loop.ts](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/js/src/loop.ts); [packages/go/loop.go](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/go/loop.go). Python agent-run and read-only ask modes; JS/Go published model/tool feedback; optional Python sandbox execution uses bridged capability calls through the same authorization gate.
- Adjacent first-party surfaces excluded from ownership: [packages/python/tests/test_approval.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/tests/test_approval.py) and separate conformance/testing, example/demo application, project contributor administration/CI, README marketing/roadmap/benchmarks, external Anthropic/OpenAI providers, downstream ORM/application user data/permissions, and optional consumer-supplied policy, sandbox or audit sinks as external organizational owners. Their independent decisions cannot be inherited by Reins.
- First-party operating / deployment modes considered: Python read-only `ask`, approval-gated `run`, explicit trusted/restricted write configurations, directly invoked registered operations and optional sandboxed Python code-mode; TypeScript/Go corresponding supported model/tool runner and read/write policies, with nonidentical feature sets. FakeModel tests are not credited as independent agent judgment.
- Recursion level: One task-operating agent at the boundary of a configured embedding application; tools are not independent viable organizational departments. End-application employees, departments and governance are outside the Reins boundary.
- Reviewed revision: `shamspias/reins@69d5ae7e3f2336366e7567b7a476e7c71608f226`; GitHub stable repository ID `625567062`; Git tree `a6f633c6950b35f2d8ce27423e71d724d23172fe`; MIT; source-first pinned review 2026-10-20.
- Observation date: 2026-10-20.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

Reins bundles three language implementations of a model/tool feedback loop. Python `run_loop` collects the user goal and a system instruction; external Model.complete receives messages and exposed tool definitions; calls dispatch through the capability registry; any structured result is appended to the same transcript and the model reconsiders until final answer or budget stop. TypeScript and Go ship analogous Reins-owned loop/protocol classes; they are not necessarily feature-identical. [packages/python/src/reins/loop.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/loop.py); [packages/js/src/loop.ts](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/js/src/loop.ts); [packages/go/loop.go](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/go/loop.go); [packages/python/src/reins/model.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/model.py).

The Python capability registry validates arguments, injects the caller's context/principal, rejects missing/invalid names, and returns exceptions as data. `ask` cannot write. `run` applies caller-selectable policy levels before potentially asking a terminal human handler to approve exact write actions; every write attempt is audited before execution and audit failure denies the effect. The same boundary is retained for Python sandbox code-mode via an execution bridge. These are execution admission and safety mechanisms, not independently authored organizational policy or supervisory autonomy. [packages/python/src/reins/registry.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/registry.py); [packages/python/src/reins/loop.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/loop.py); [packages/python/src/reins/policy.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/policy.py); [packages/python/src/reins/approval.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/approval.py); [packages/python/src/reins/audit.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/audit.py).

Per-run budgets, token/cost/elapsed constraints, deterministic context compaction, progressive capability/schema disclosure, optional provider adapters, ORM-derived registered verbs, in-memory or injected audit sink and stop conditions shape the local operating loop. Neither the shell approvals nor named audit events independently instantiate a current-management S3 unit, a complementary S3* operational-reality auditor, future capability strategy S4, or policy/identity S5. Existing unit/conformance tests and the README are corroborative rather than direct evidence of those separate functions. [packages/python/src/reins/budget.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/budget.py); [packages/python/src/reins/conversation.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/conversation.py); [packages/python/src/reins/disclosure.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/disclosure.py); [README.md](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/README.md).

## Operational model

One app/user supplies a goal and a fixed set of safe application capabilities; a configured provider model chooses operations in context, whose result or error is fed to the same decision-maker. Actions with write effects are constrained by host policy, operator approvals, principal scoping and recording; completion stops on a result or guard. This is one operating S1 recursion and an externally governed capability-execution boundary, not a demonstrated departmental viable metasystem. Human-gated single-action execution is not, without a whole-system management mandate and returned decision, `S3=P`; configured risk levels do not demonstrate policy-identity S5.

## S1 — Operations

- State: A
- Function: Model-selected operations through an application-capability interface, returning observations to the same goal-facing operating agent.
- Disturbance / variety regulated: New user goals, varying application data/tool results, access restrictions, incompatible schemas, operation failures, token/turn/time budget exhaustion and write-approval outcomes.
- Decisive decision or feedback right: Configured model chooses which exposed capability to call or program to submit and when to answer; the first-party loop executes qualified calls and returns errors/results on the next model turn.
- Decision owner: External configured model owns contextual task-next-action discretion in a shipped Reins Python/TS/Go composition. The caller owns the top-level goal, callable app operations and risk policy; the runtime gates effects.
- Supporting / enforcement mechanisms: CapabilityRegistry registration/schema checks; `ask()` read-only bound; `run()` policy–human-approval–audit–execution chain; sandbox/code-mode bridge; progressive disclosure; conversation compaction; budgets/stop conditions.
- Closure path: User goal → `model.complete(messages, tools, params)` → tool/program request → registered tool admission and dispatch → tool result into conversation → next model choice or goal-completed answer. A disallowed operation is refused/denied/audited without an unauthorized write.
- Boundary reachability: Python `Agent.ask()` / `Agent.run()` invoke first-party `run_loop`, which instantiates a policy, approval gate and registry; provider/model via `Model.complete` and `CapabilityRegistry.call` have real shipped interfaces. JS `loop.ts` and Go `RunWith` expose comparable configured model/tool paths. The optional fake model is a test stand-in only.
- Why this is / is not agent-owned: Removing the provider model leaves deterministic admission, audit and replayable test scripts, not flexible selection of an action path from new application feedback. The meaningful task-deciding model is externally configured but connected through a concrete first-party operating loop, warranting S1=A.
- Evidence: [packages/python/src/reins/loop.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/loop.py); [packages/python/src/reins/model.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/model.py); [packages/python/src/reins/registry.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/registry.py); [packages/js/src/loop.ts](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/js/src/loop.ts); [packages/go/loop.go](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/go/loop.go); [packages/python/src/reins/policy.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/policy.py).
- Basis: Explicit reachable source-wiring across supported modes; test source corroborates safety patterns.
- Confidence: High for published model/tool integration; real-provider task effectiveness not measured.
- Caveats: Policy enforcement is not itself autonomous governance. Go code-mode support is narrower than Python; the vector relies on shared first-party model/tool loop, not identical feature parity.

## S2 — Coordination

- State: —
- Function: No first-party function separately regulates real mutual interference among two or more independently viable S1 operational departments.
- Disturbance / variety regulated: Multiple capability calls and application data access may conflict, and one user-facing goal can contain multiple operations; they remain tool substeps of one task.
- Decisive decision or feedback right: No separately authorized inter-S1 conflict-damping decision changes mutual commitments of independent task departments.
- Decision owner: One task model and caller-specified policies; code-level action batching and admission are not inter-division regulators.
- Supporting / enforcement mechanisms: Per-turn pending calls, capability registry, group policy verdicts, bulk confirmations and the sandbox capability bridge.
- Closure path: Multiple call effects and results return to the same task loop or are refused, not to distinct ongoing viable S1 units under reciprocal coordination.
- Why this is / is not agent-owned: No separately viable departmental plurality or S2-specific owner/feedback path is defined in the supported Reins distribution.
- Evidence: [packages/python/src/reins/loop.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/loop.py); [packages/python/src/reins/registry.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/registry.py); [packages/python/src/reins/policy.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/policy.py); [packages/python/src/reins/disclosure.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/disclosure.py); [packages/go/loop.go](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/go/loop.go).
- Basis: Bounded absence at the published app-operating agent recursion.
- Confidence: High.
- Caveats: Independent host applications could compose multi-agent departments externally, but that composite organization is not assessed.

### Absence scope

- Surfaces inspected: Python `loop.py`, registry and batch policy, TypeScript and Go run loops, capability disclosure and code-mode bridging.
- Plausible first-party paths checked: Simultaneous/multiple tool calls, shared application records, action batch sequencing and bulk-write confirmation as possible inter-operation conflict routes.
- Why no material first-party path remains: These regulate tool side effects of one agent goal, not independently viable S1 departmental units with a separately decisive cross-S1 stabilization loop.

## S3 — Inside-and-now control

- State: —
- Function: No first-party current whole-system executive owns discretionary resource/obligation/priority decisions across independently viable S1 departments.
- Disturbance / variety regulated: Risky writes, budget overruns, many app capabilities, missing principal and failed actions are current-task disturbances.
- Decisive decision or feedback right: DefaultPolicy deterministically allows/denies/requests approval under host-set risk modes; terminal human approves individual write requests, not a whole-current portfolio allocation.
- Decision owner: Host/application owner establishes permissions and available capabilities; per-write human approver gates execution; runtime enforces rather than owns a distinct S3 mandate.
- Supporting / enforcement mechanisms: AutonomyLevel read-only/draft/approved/trusted settings, per-run budgets and principal scoping, terminal approval prompt, audit.
- Closure path: Task write proposal → policy/gate → current action executed or stopped; no cross-S1 whole-current managerial picture, decision and returned binding reallocation.
- Why this is / is not agent-owned: `AutonomyLevel` labels adjust task permissions and are not VSM autonomy vectors. An individual user approval does not constitute a parent-held system-wide current management loop at the assessed recursion.
- Evidence: [packages/python/src/reins/policy.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/policy.py); [packages/python/src/reins/approval.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/approval.py); [packages/python/src/reins/loop.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/loop.py); [packages/python/src/reins/budget.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/budget.py); [packages/js/src/loop.ts](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/js/src/loop.ts); [packages/go/loop.go](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/go/loop.go).
- Basis: Bounded absence after specific inspection of shipped approval/policy and control surfaces.
- Confidence: High.
- Caveats: Separate human-operated business management could use Reins as a tool; its own S3 is outside the first-party harness.

### Absence scope

- Surfaces inspected: Agent run/ask, default authorization ladder, terminal approval, budget/stop conditions, row/principal-scoping and language mirrors.
- Plausible first-party paths checked: Host risk profiles, write permission/approval, bulk operation admission, stop/limit controls and audit exceptions as potential current-control owners.
- Why no material first-party path remains: No first-party whole-system current management of multiple viable S1s, discretionary resource/obligation choice and returned departmental adjustment. Single-action human approval does not establish that parent mode.

## S3* — Complementary audit

- State: —
- Function: No independent complementary operating-reality auditor with a separate mandate that corrects reporting to an S3 current-management owner.
- Disturbance / variety regulated: Unattributed/unauthorized writes, leaked private arguments and action failure must be recorded or rejected.
- Decisive decision or feedback right: AuditSink records each write attempt and decision on the same policy/gate execution path, defaulting to MemoryAuditSink. Tests check compliance but no independent S3 corrective challenge follows.
- Decision owner: Run-loop instrumentation and caller-provided sink; no distinct S3* actor/authority.
- Supporting / enforcement mechanisms: AuditRecord with trace_id, PII-redacted arguments, decision, principal; fail-closed no-audit-no-write; safety/conformance tests.
- Closure path: Attempt → synchronous audit record → action allowed/denied in current task. No independent reality inspection → challenged S3 managerial report → corrective current-control feedback loop.
- Why this is / is not agent-owned: Recording an audit trail is useful evidence infrastructure but cannot establish an independent function-specific auditor. A distinct S3 manager receiving and acting on challenged claims is also absent.
- Evidence: [packages/python/src/reins/audit.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/audit.py); [packages/python/src/reins/loop.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/loop.py); [packages/python/src/reins/registry.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/registry.py); [packages/python/tests/test_approval.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/tests/test_approval.py); [packages/go/loop.go](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/go/loop.go).
- Basis: Bounded absence despite named first-party audit component.
- Confidence: High.
- Caveats: Downstream business audit teams or integrations could consume emitted records, not an included S3* mode.

### Absence scope

- Surfaces inspected: Structured audit records/sinks, in-run traces, fail-closed write gate, policy, independent test source and Go/JS mirrors.
- Plausible first-party paths checked: Direct action logs, audit durability, test/compliance checks and per-call human approval as candidate S3* reality audits.
- Why no material first-party path remains: Logs arise inside the ordinary action admission channel and do not show an independent source inspecting claims and returning corrective findings to a distinct S3 owner.

## S4 — Outside-and-then intelligence

- State: —
- Function: No implemented outside-and-then sensing/prospective strategy-authoring and accepted change of future Reins operating capability.
- Disturbance / variety regulated: Future application needs may require new capability definitions, provider changes, policy rules or context handling.
- Decisive decision or feedback right: Configured model makes present goal-directed calls; deterministic context compaction and capability discovery modify current context exposure, not future organizational strategy.
- Decision owner: External developer/operator chooses tool exposure/provider/policy and future versions; shipped code does not entrust prospective adaptation choices and durable return to an S4 agent or legitimate operational parent.
- Supporting / enforcement mechanisms: Capability search/schema disclosure, conversation compaction, provider configuration, examples and test suites.
- Closure path: Current query → capability search/tool feedback → current task completion; no external-change observation → future option → decision owner → changed subsequent distribution/strategy.
- Why this is / is not agent-owned: Code-mode may generate temporary programs for the *current* goal; it does not persist a newly adopted platform strategy. Tests and GitHub development are adjacent rather than first-party S4.
- Evidence: [packages/python/src/reins/loop.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/loop.py); [packages/python/src/reins/conversation.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/conversation.py); [packages/python/src/reins/disclosure.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/disclosure.py); [packages/python/src/reins/model.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/model.py); [README.md](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/README.md).
- Basis: Bounded negative after reviewing the supported run modes and contextual features.
- Confidence: Medium-high.
- Caveats: Source release could grow S4 later; a new ref would need a distinct reassessment.

### Absence scope

- Surfaces inspected: Capability registry/progressive disclosure, context compaction, provider interfaces, runtime output, tests, README/EXTENDING integration.
- Plausible first-party paths checked: Tool discovery as future capability search, context compression as adaptive strategy, temporary code programs, human provider changes and proposed extensions.
- Why no material first-party path remains: All shipped routes configure or adjust current-task execution; no first-party environmental intelligence decides/returns accepted prospective changes to the later operating system.

## S5 — Policy and identity

- State: —
- Function: No first-party agent or reconstructable legitimate parent loop decides ultimate mission, organizational identity or constitutional policy, then returns binding policy to subsequent operation.
- Disturbance / variety regulated: The supported instance must respect identity/principal scoping, read/write boundaries and operator intent.
- Decisive decision or feedback right: Host app sets the goal, registered capabilities, principal and allowed autonomy mode; deterministic policy applies those supplied rules, with isolated per-write approval.
- Decision owner: Application owner/user or downstream institution outside the harness chooses constitutional purpose; no explicit first-party ultimate-policy decision/return channel is shipped.
- Supporting / enforcement mechanisms: Policy classes, principal/row scoping, approval request, audit sink, capability metadata and public repository governance.
- Closure path: Host user input/configuration → bounded agent task. No first-party identity-policy matter → legitimate parent authority judgment → authoritative change to future organizational operating rules.
- Why this is / is not agent-owned: Names such as autonomy ladder, policy engine and audit represent permissions/execution enforcement, not a substantive VSM S5 identity/ultimate-purpose authority. A user clicking yes for one write does not form an S5 parent loop.
- Evidence: [packages/python/src/reins/policy.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/policy.py); [packages/python/src/reins/approval.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/approval.py); [packages/python/src/reins/loop.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/loop.py); [packages/python/src/reins/registry.py](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/packages/python/src/reins/registry.py); [README.md](https://github.com/shamspias/reins/blob/69d5ae7e3f2336366e7567b7a476e7c71608f226/README.md).
- Basis: Bounded negative after inspection of caller policy and all three first-party loop families.
- Confidence: High for the stated packaged recursion.
- Caveats: Project maintainers set external software policy, but there is no corresponding packaged constitution-level return in a first-party agent organization.

### Absence scope

- Surfaces inspected: DefaultPolicy, AutonomyLevel, context/principal checks, approvals, Reins RunOptions, project docs and multi-language loops.
- Plausible first-party paths checked: Human approvals, developer-configured safety policy, autonomy ladder and application identity as possible ultimate-purpose governance paths.
- Why no material first-party path remains: No function-specific constitutional decision mandate or legitimate parent policy return to Reins organizational identity. App user consent is an action admission mechanism, not S5.


## Recursion

At the assessed boundary the model/tool closed loop forms one goal-facing S1. Application functions, approval handlers, registry, sandbox and audit are supporting capability-operation controls. Different languages are three implementations of a framework, not three distinct viable S1 departments. External app org, human owner and model vendor remain out of scope. A broader S3/S4/S5 may exist *in a downstream organization*, not established by this repository.

## Variety and escalation

Tool/goal variety is addressed by model choices; invalid schema, restricted writes, missing authorization, and budget exhaustion are handled by deterministic guards or operator approval. Audit records and traces are action evidence, not an independent algedonic signal or managerial corrective loop. A denied request returns a local task refusal rather than escalating a verified cross-S1 governance issue. This source-first analysis does not claim superior autonomy or task quality merely because Reins implements safeguards.

## Evidence gaps

- The public source supports external model integration but no live provider measurement or benchmark performance was reproduced in this assessment.
- The three language implementations are not feature-identical; the positive S1 witness relies on their model/tool runtime, whereas code-mode parity is not assumed for Go.
- Distinguishing actual human organizational supervision from a one-call approval prompt would require downstream deployment evidence at a larger recursion; do not grant parent-mode S3/S5 based on an abstract possibility.
- Any future explicit environmental model/policy learning or independent audit oversight would require a new-ref source-backed re-review, not inferred from the current single-task implementation.
