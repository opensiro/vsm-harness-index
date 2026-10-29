---
harness_id: chainreactors-cyber-harness
project_name: chainreactors/cyber-harness
repository: https://github.com/chainreactors/cyber-harness
review_ref: 89f8af5ea2f478bf96eedc8f1b6ba8401ce28853
reviewed_at: 2026-10-29
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# chainreactors/cyber-harness

## Review boundary

- System in focus: one first-party cyber-harness `aiscan` agent/task runtime, including the explicitly supported optional `jev.mode=auto`/`learning=auto` adaptation mode and its separate semantic reviewer; not all scanners, standalone audits, independent Web Hub nodes or the external cybersecurity organization.
- Purpose and identity: provide a model-driven general cyber-task agent with configurable tools, sessions and observations; optionally learn reusable executable Reflex capabilities from actual task traces under native/replay/semantic validation.
- Relevant environment: task/tool feedback, provider errors, actual native execution traces, unknown selectors and effect identities, candidate-program defects, changing user task values, parallel subagent messages and operator permissions.
- Standard-distribution boundary: shipped `cmd/aiscan` Profile, Go `agent` loop/session/tool stack and `exts/jev` opt-in extension, including first-party compiler/replay/semantic reviewer/library. Full, minimal and `cyber-audit` binaries are distinct assemblies; isolated scanners and Web UI are not assumed to have JEV enabled.
- Credited operating / distribution surfaces: `cmd/aiscan/profile.go`, `agent/loop.go`, `agent/session/`, `exts/jev/extension.go`, `compile.go`, `compiler_agent.go`, `store.go`, replay and typed-claim provider client; only the explicit opt-in mode with real model and TypeSafe JEV credentials supplies the S3*/S4 actors.
- Adjacent first-party surfaces excluded from ownership: separate `cmd/audit` agent as an independent product, `cyber-web` Hub, Playwright acceptance and demo benchmarks, `examples/`, first-party CI/tests and developer documentation, third-party scanner/IOA providers and any user-defined external governance.
- First-party operating / deployment modes considered: `aiscan agent` model/tool loop with sessions, `aiscan-full` Web/browser/scan profiles, local subagent/IOA messaging, optional `guardrail.provider=jev`, and `jev.mode=auto` with automatic Claim generation/Reflex compilation or explicitly invoked `jev compile`. The off-by-default mode is an essential positive-state caveat.
- Recursion level: one task-bearing agent plus its optional first-party adaptation/audit extensions as a supported installed operating cell; JEV's background compiler is a distinct function-specific actor, not a second independent pentest S1.
- Reviewed revision: `chainreactors/cyber-harness@89f8af5ea2f478bf96eedc8f1b6ba8401ce28853`.
- Observation date: 2026-10-29.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The Go host assembles resource/extension lifecycle, model request hooks, tools, sessions, subagents, scan and Web modes. In `aiscan agent`, `StandardLoop` lets a configured model select tool calls and consume actual results; IOA and subagent messages return to a bounded session Inbox. The opt-in JEV extension hooks model/utility events, creates typed Claims from actual evidence, asynchronously compiles executable `Reflex` programs via a separate compiler agent, validates native argument contracts and recorded-result replay, then asks a separate JEV semantic reviewer to judge original user constraints, current native results, effect/read freshness and completion. Successful Reflexes publish atomically in a bounded persistent library and can replace repeated planning on later qualifying tasks; rejection returns diagnostics for repair. [Product modes](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/README.md#L18-L88), [Profile opt-in composition](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/cmd/aiscan/profile.go#L140-L185), [JEV runtime hooks](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/exts/jev/extension.go#L56-L135), [JEV lifecycle](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/docs/jev.md#L8-L98).

## Operational model

The user supplies a task, model credentials and permitted tools. The main Agent executes model-selected actions and supplies actual traces. In opt-in JEV auto-learning, a background compiler agent proposes future executable reuse, while separate typed semantic judgments have their own accept/reject right against the original constraints and actual recorded evidence. Publication and later reuse close an S4 adaptation path. The semantic gate is credited only to the compilation/reflex mode, not as an independent auditor of every ordinary S1 task. Neither user approval nor a tool-inbox queue is promoted to S3/S5.

## S1 — Operations

- State: A
- Function: perform a user-initiated agent task using model-selected tools and feedback, including authorized local cyber workflows.
- Disturbance / variety regulated: changing task outputs, file/browser/native results, model/tool errors, user follow-ups and observed system state.
- Decisive decision or feedback right: configured model in `StandardLoop` chooses task-specific tool calls, response and continuation.
- Decision owner: native first-party agent loop's active LLM reasoning actor; optional JEV Reflex may replace a qualified repeated subworkflow but does not make the ordinary scanner itself autonomous.
- Supporting / enforcement mechanisms: executable tool registry, session, bounded inbox, hook/event stream, provider adapters, extension lifecycle and configured permissions.
- Closure path: user/task input → model chooses tool → native executor records actual result → model consumes observation/continues → session result/event stream.
- Boundary reachability: documented `aiscan agent` and minimal `cmd/agent` compose real `StandardLoop` with model/provider; source code has a standard executable path, not only an example fixture or deterministic scan mode.
- Why this is / is not agent-owned: model-selected tool execution and subsequent choices provide the task-specific decision, distinct from rule-only scanning or host wiring.
- Evidence: [agent runtime entry](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/cmd/aiscan/modes.go#L49-L79), [minimal agent](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/README.md#L115-L160), [runtime assembly](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/cmd/aiscan/profile.go#L135-L185).
- Basis: structural supported executable-mode review; no live LLM/targets.
- Confidence: high for a wired agentic path, not for task completion accuracy or safety of real-world scans.
- Caveats: no autonomy claim is made about the `scan --verify=off` deterministic path, empty model/tool host, or unconfigured provider.

## S2 — Coordination

- State: —
- Function: no first-party S2-specific interference-attenuation loop between separately viable S1 agent units is established at the selected task-runtime recursion.
- Disturbance / variety regulated: simultaneous subagent/IOA events can enter a bounded Inbox, but this is messaging/backpressure rather than shown inter-S1 disturbance negotiation.
- Decisive decision or feedback right: event bus/inbox routes prioritized task messages; parent agent delegates and receives child reports.
- Decision owner: deterministic queue/resource limits and the parent task agent, not a separately evidenced coordination regulator.
- Supporting / enforcement mechanisms: bounded Inbox, async subagent results, IOA messaging, host node connection management.
- Closure path: messages arrive or are rejected, then agent handles next task turn; no independently operating S1 peers' actions are altered in response to a concrete shared collision.
- Why this is / is not agent-owned: routing and queue priorities are not sufficient without an inter-unit interference witness and returned S2-specific regulation.
- Evidence: [architecture: inbox and subagents](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/docs/architecture.md#L54-L71), [scanner mode separation](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/README.md#L18-L43).
- Basis: structural.
- Confidence: medium, bounded to default and explicitly supported variants inspected.
- Caveats: a multi-node application using IOA may implement its own inter-unit resource conflict governance externally.

### Absence scope

- Surfaces inspected: Subagent, IOA messaging, Inbox priority/drop, event bus, scanner verification modes and Web node state.
- Plausible first-party paths checked: child/peer messages, async reports, PID locks, bounded inbox and node connections.
- Why no material first-party path remains: observed channels manage delivery and resource safety, not an identifiable inter-S1 disturbance with a specific attenuating decision and feedback to another S1 unit.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system current resource/commitment regulator with distinct decision ownership is established for this single task cell.
- Disturbance / variety regulated: tool errors, scanner events, guardrail prompts, session requests and JEV qualification failures.
- Decisive decision or feedback right: user configures permissions and may intervene; deterministic tool hooks enforce rules; model chooses its own task work.
- Decision owner: external user for local settings, task model for work, static controls for safety; not a shared S3 manager over plural operations.
- Supporting / enforcement mechanisms: `guardrail` tool admission (default `provider:none`), session inbox, runtime config, effect journaling.
- Closure path: a particular tool may be allowed/denied and a task adjusted, but no whole-system current resource bargain or returned portfolio regulation is demonstrated.
- Why this is / is not agent-owned: policy screening and retry/error gates do not themselves choose common current commitments.
- Evidence: [guardrail default and hook](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/exts/guardrail/extension.go#L12-L89), [Profile assembly](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/cmd/aiscan/profile.go#L140-L185).
- Basis: structural.
- Confidence: medium-high for assessed one-cell recursion.
- Caveats: a separately configured multi-node portfolio could be reassessed at a higher recursion.

### Absence scope

- Surfaces inspected: `aiscan` Profile, session control, scanner/event scheduling, guardrail modes and JEV controller admission.
- Plausible first-party paths checked: tool admission, human approval, model budget, Web node management, Reflex effect journal and provider failover.
- Why no material first-party path remains: these are task/transport/qualification constraints, not a current whole-system regulatory owner setting shared operating resources or commitments.

## S3* — Complementary audit

- State: A
- Function: independently test proposed reusable Reflex capability claims against original user task constraints and recorded native execution evidence before allowing publication.
- Disturbance / variety regulated: compiler-generated source may misstate result fields, native argument provenance, read/effect freshness, missing required work or task completion.
- Claim being audited: that a compiler-generated Reflex program is safe and semantically faithful enough to reuse for an observed task capability; not that every ordinary pentest conclusion is independently correct.
- Ordinary reporting path: foreground agent native-tool results and compiler draft/mechanism replay proof; compiler itself proposes the program.
- Complementary access path: separate JEV semantic `exchange` reads original task constraints, full actual trajectory, native binding witnesses and candidate program without relying solely on compiler's summary.
- Independence boundary: the JEV reviewer receives its own typed Claim request with independent access to actual/native evidence, not the compiler's self-attestation; the compiler can only repair and resubmit after a rejection, not mark itself qualified.
- Decisive decision or feedback right: typed independent reviewer returns accept/reject (`compile`/`defer` and concrete coverage checks); rejection prevents publication and enters compiler repair diagnostics.
- Decision owner: separately invoked JEV semantic reviewer in opt-in `jev.mode=auto` compile path; native validators independently reject invalid contracts/replay.
- Supporting / enforcement mechanisms: `reviewReflex` evidence projection, native replay witnesses, bounded 64 KiB review input, typed claims, `validate_reflex` no-real-user-tool validation, fail-closed qualification.
- Closure path: compiler draft → native validation and actual-trace replay → independent JEV semantic judgment → accepted qualification/publish or explicit failed diagnostic → compiler repair/resubmission.
- Who acts on findings: the compiler agent repairs rejected programs from concrete diagnostics; qualification/persistence blocks publication until the distinct reviewer and native gates accept.
- Boundary reachability: `cmd/aiscan` explicitly installs `jevext.New` when enabled with credentials, worker runs compiler, `validate_reflex` directly invokes `reviewReflex` before `accepted` and library publication; not test-only review scripts.
- Why this is / is not agent-owned: a separate semantic model makes the judgment from complementary actual evidence; the draft-producing compiler cannot self-certify or bypass the gate.
- Evidence: [compiler gate and repair](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/exts/jev/compiler_agent.go#L109-L221), [independent semantics and concrete failure return](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/exts/jev/compile.go#L319-L426), [mode installation](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/cmd/aiscan/profile.go#L161-L185).
- Basis: direct source contract and verified native/reviewer path, no independent live model audit executed here.
- Confidence: medium-high for distinct code path and approval authority; semantic accuracy of a given reviewer verdict remains unmeasured.
- Caveats: JEV is off by default; configured TypeSafe credentials and learning mode are required. This audits *generated Reflex capability*, not all S1 task or scan claims, nor OpenSiro independent S3* validation.

## S4 — Outside-and-then intelligence

- State: A
- Function: autonomously develop and validate reusable future task capability from real execution evidence, and return a qualified program to later operations.
- Disturbance / variety regulated: repeated task variety, variable handles/arguments, missing native bindings, degraded or failing candidate programs and new user inputs.
- External distinction: real user tasks, changed native tool outcomes and fresh evidence challenge reusable capability; this is outside the compiler's draft and not simply re-reading the model's own plan.
- Future / prospective distinction: learning turns observed executions into tested programs intended for *later* qualifying task instances, beyond choosing the next action of the current S1 turn.
- Adaptation option generated: an executable Reflex with entry applicability, parameter schema, native contracts, evidence-aware logic and reusable persistent ID; rejected versions are repaired or retired.
- Decisive decision or feedback right: background compiler agent generates executable candidate and repairs from feedback; typed criteria and native validators decide admissibility; accepted Reflex is published into runtime selection.
- Decision owner: first-party JEV background compiler agent for adaptation proposals, with autonomous model-driven generation; independent semantic gate remains a distinct S3* reviewer, not identical S4 ownership.
- Supporting / enforcement mechanisms: Claim generation, tool-trace capture, bounded persistent Claim/Reflex store, compiler agent, replay, semantic reviewer and atomic publication/retirement.
- Closure path: observed task → generated Claim → compiler proposes/repairs executable Reflex → native/replay/independent qualification → library persist → subsequent matching tasks run validated program with current parameters/results instead of re-planning.
- Path back into current capability / S3: the qualified Reflex is atomically published to the runtime library and the JEV tool hooks may execute it in subsequent ordinary Agent turns; current-operation tool admission/replay still enforces native contracts and journaled effects. No separate S3 owner is inferred from this return path.
- Boundary reachability: optional `jev.mode=auto`/`learning=auto` is registered into the actual `aiscan` Profile; `extension.Load` subscribes model/tool hooks and starts background `work` when configured, so loop is shipped not a proposal or isolated experiment.
- Why this is / is not agent-owned: a separately driven model compiler develops executable options and repairs from external evidence, unlike static caches, installed skills or user-authored scripts.
- Evidence: [JEV lifecycle and learning](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/docs/jev.md#L22-L89), [extension runtime hook/work](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/exts/jev/extension.go#L72-L147), [compiler validation path](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/exts/jev/compiler_agent.go#L106-L219), [persistent publish](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/exts/jev/store.go#L150-L228).
- Basis: structural operational path plus first-party documented real/replay tests, not reproduction of paid JEV/LLM services.
- Confidence: medium-high for a shipped adaptation loop, lower for generalization/per-task savings.
- Caveats: `mode:off` is default; `learning:frozen` only reuses approved Reflexes and does not exercise the S4 development mode. Failures leave old definitions intact and genuine completion is not assumed from replay alone.

## S5 — Policy and identity

- State: —
- Function: no ultimate constitutional identity/policy issue reaches a legitimate decision owner and returns to govern the running agent's viability.
- Disturbance / variety regulated: user authorization, target selection, tool allow/deny, API credentials and optional JEV learning choice.
- Decisive decision or feedback right: user/operator chooses tool, model and opt-in modes; deterministic host/guardrail enforces configured boundaries.
- Decision owner: external operator for authorized cyber task and software maintainers for release policy; no first-party S5 authority within one session.
- Supporting / enforcement mechanisms: configuration, disclaimers, guardrail, effect journal and approval controls.
- Closure path: per-tool/per-mode settings constrain task execution, not identity-level S3–S4 tension resolution with returned legitimate ultimate policy.
- Why this is / is not agent-owned: safety screening or consent is ordinary operating constraint, and a security-workflow label cannot become S5 by convention.
- Evidence: [disclaimer and operator scope](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/README.md#L196-L214), [guardrail configuration](https://github.com/chainreactors/cyber-harness/blob/89f8af5ea2f478bf96eedc8f1b6ba8401ce28853/exts/guardrail/extension.go#L18-L64).
- Basis: structural.
- Confidence: medium-high.
- Caveats: an external institution may supply S5 at a different, explicitly declared recursion level.

### Absence scope

- Surfaces inspected: Profile configuration, JEV optional policy/mode, guardrail, operator disclaimers, tool permissions and Web session administration.
- Plausible first-party paths checked: target authorization, human approval, Reflex publication, policy Claim evaluation and provider credentials.
- Why no material first-party path remains: JEV/guardrail judge task/tool/reflex correctness, not legitimate ultimate organizational identity; external operator chooses purpose and constraints.

## Distributed OSS parent arrangement

Maintainers control source releases, standalone cyber-audit modules and optional modes, but their governance is not a live first-party S5 of an installed user's task. Institution-level authorization and target scope belong to external human authority.

## Self-hosted and non-human modes

Local model endpoints and standalone host composition are supported. Positive S3*/S4 only applies when installed `aiscan` Profile explicitly activates JEV with an actual TypeSafe key and learning enabled; other editions and default `jev.mode=off` do not inherit these states automatically.

## Recursion

One root task agent is S1. The JEV compiler/reviewer and durable Reflex library form function-specific complementary and future-intelligence loops supporting this cell, not extra pentest S1 units. IOA peers and external Web node fleets require separate higher-recursion assessment to claim coordination or management.

## Variety and escalation

Tool hooks, bounded Inbox and guardrail attenuate immediate variety. JEV failures keep the current library unchanged, publish explicit diagnostics and preserve prior code; this is a returned adaptation/audit signal, not an identity-policy escalation. A `BLOCKED` status alone would be insufficient as evidence of an algedonic governing channel.

## Evidence gaps

- No live model, JEV paid endpoint, scanner, target exploitation or browser task was executed; source-first positive S3*/S4 states concern the shipped conditional mode and actual code paths, not independently measured quality.
- JEV is explicitly off by default. `learning=frozen` or missing credentials precludes active self-development; higher-function claims cannot be projected onto the minimal agent binary, bare scanner or a plain Web Hub.
- Runtime JEV reviewer is independent of candidate generation and reads actual tool evidence, but it audits Reflex publications only; it is not an OpenSiro independently commissioned semantic reassessment and not a general pentest finding certification.
