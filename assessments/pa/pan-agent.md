---
harness_id: pan-agent
project_name: Pan Agent
repository: https://github.com/pym96/Pan-agent
review_ref: 6040fcadde20e2628ba18550848f3bb2c725e68e
reviewed_at: 2026-10-27
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

# Pan Agent

## Review boundary

- System in focus: the Pan Agent native TypeScript terminal model/tool harness, not all experiments and companion services in the repository.
- Purpose and identity: fulfill a user's local file/shell tasks through iterative model-selected tool use under operator authority.
- Relevant environment: user prompts, provider responses, workspace files and shell, permission decisions, cancellation, and run archives.
- Standard-distribution boundary: documented installed TUI v0.1.6 and supported source-build native kernel (source candidate v0.1.7); optional retrieval is source-build only, not attributed to the published v0.1.6 asset.
- Credited operating / distribution surfaces: `typescript/src/runtime/{native-kernel,session,authorization}.ts`, packaged native TUI/tools and run archive, with the first-party source-build option documented in `README.md`.
- Adjacent first-party surfaces excluded from ownership: historical Python agent implementation, ReAct and protocol experiments, benchmark/proof packs, development/test fixtures, and separate `apps/evidence-web` service; the repository expressly distinguishes product and reference surfaces [README lines 114–126](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/README.md#L114-L126).
- First-party operating / deployment modes considered: real provider-backed native TUI, offline scripted-model demonstration (not evidence of model discretion), source-build native session, protected-file/shell operator approvals, run replay and optional source-build retrieval.
- Recursion level: one local Pan terminal task session and its agent loop; operator and provider are environment/parent, not a multi-agent metasystem by default.
- Reviewed revision: `6040fcadde20e2628ba18550848f3bb2c725e68e`.
- Observation date: 2026-10-27.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The installed product is a terminal application, configured for Kimi/DeepSeek and a native TypeScript kernel, with model-selected filesystem and shell tool calls. The session creates and seals a run archive and binds a runbook to the task; authorization can request operator consent for protected/outside-workspace paths and shell use. A model response with tool calls returns their results to subsequent model context until the assistant ends or cancellation/limits/failure stop the run. A trusted kernel adapter, limits, archive, protocol validation and terminal UI surround that loop, but do not independently choose its ordinary task steps. A replay displays settled history without rerunning tools or making a model call. The source-built retrieval option draws from explicitly operator-selected material and requires permission; it is not a prospective strategy authority [README lines 43–71](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/README.md#L43-L71), [session lines 155–203](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/typescript/src/runtime/session.ts#L155-L203), [native kernel lines 173–264](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/typescript/src/runtime/native-kernel.ts#L173-L264).

## Operational model

The primary S1 unit is the agent-led terminal task loop operating on local files/commands. The model has bounded discretion to choose calls and respond to their outcomes; the human supplies the task, provider credentials and exceptional tool permissions. Turn/step limits, path-scoped authorization, checkpoint settlement and immutable replay records enforce or observe those choices. They do not form additional autonomous S1 units or, without a further first-party control loop, a whole-system S3/S4/S5 decision owner.

## S1 — Operations

- State: A
- Function: execute a user task through a continuing local agent/tool transformation.
- Disturbance / variety regulated: unpredictable user-request details, file contents, command outputs and recoverable tool errors.
- Decisive decision or feedback right: select the next model-specified tool call or conclude based on the updated context.
- Decision owner: provider-backed agent within the native kernel; user approvals bound effects but do not select the ordinary next model action.
- Supporting / enforcement mechanisms: tool schema validation, authorization, filesystem/shell executors, maximum-turn/step guards, archive and checkpoint.
- Closure path: model output → validated calls → executed/denied tool results → appended messages → next model exchange or terminal answer.
- Boundary reachability: the documented native TUI runs this exact first-party loop in the supported real-provider mode, not only in a test or reference module.
- Why this is / is not agent-owned: the kernel runs an iterative exchange but the model chooses task-relevant calls from context; deterministic limit and permission gates merely constrain or stop them.
- Evidence: [native loop lines 173–264](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/typescript/src/runtime/native-kernel.ts#L173-L264), [tool execution lines 287–306](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/typescript/src/runtime/native-kernel.ts#L287-L306), [documented native invocation](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/README.md#L43-L61).
- Basis: structural.
- Confidence: high for shipped source loop; no live provider run performed in this review.
- Caveats: source and published package versions differ for optional retrieval; the offline scripted demo does not itself demonstrate autonomous model choice.

## S2 — Coordination

- State: —
- Function: no inter-S1 oscillation attenuation established at this single-session recursion.
- Disturbance / variety regulated: concurrency between independent S1 operations would be relevant if such units were supplied; only one agent task is admitted per native session.
- Decisive decision or feedback right: no S2-specific mutual adjustment right is exposed.
- Decision owner: none evidenced at this boundary; single-session busy rejection is runtime protection.
- Supporting / enforcement mechanisms: `GeneralAgentSession` busy/admission guard and serial conversation state.
- Closure path: no cross-unit coordination feedback path; one task's tool results feed its own loop.
- Why this is / is not agent-owned: sequencing calls within one S1 and refusing a second concurrent task is not regulating interference among distinct S1s.
- Evidence: [session lines 148–161](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/typescript/src/runtime/session.ts#L148-L161), [kernel lines 129–176](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/typescript/src/runtime/native-kernel.ts#L129-L176).
- Basis: structural.
- Confidence: high within the documented native TUI boundary.
- Caveats: multiple externally run Pan processes are not first-party inter-S1 coordination in one assessed Pan organization.

### Absence scope

- Surfaces inspected: native kernel, session, TUI invocation, tools, authorization, README product/reference split.
- Plausible first-party paths checked: parallel tool invocation, multiple sessions, task admission and handoff; no distinct S1-unit conflict witness plus responsive S2-specific coordination closure is supplied.
- Why no material first-party path remains: the shipped standard agent loop is a single S1 with local task guards; generic sequencing/concurrency prevention lacks the required inter-S1 disturbance and mutual feedback.

## S3 — Inside-and-now control

- State: —
- Function: no whole-system discretionary regulation of multiple current S1 commitments is established.
- Disturbance / variety regulated: local turn/tool overrun and unsafe filesystem or shell effects are bounded, not whole-system resource bargaining.
- Decisive decision or feedback right: no reachable agent-held whole-system resource/commitment priority or intervention right at this recursion.
- Decision owner: operator sets authorization, runtime enforces configured limits; the model owns S1 tool choices.
- Supporting / enforcement mechanisms: turn/step limits, abort, authorization channel, archive/checkpoint.
- Closure path: deterministic stop/deny of local effects, not a returned whole-system S3 policy choice.
- Why this is / is not agent-owned: a hard limiter and an operator approval decision do not give an agent S3 discretion.
- Evidence: [native limits lines 173–176 and 249–255](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/typescript/src/runtime/native-kernel.ts#L173-L255), [approval decisions lines 154–183](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/typescript/src/runtime/authorization.ts#L154-L183).
- Basis: structural.
- Confidence: high for assessed single-session mode.
- Caveats: a parent operator can stop or permit effects, but those local approvals are not evidence of parent whole-system S3 closure.

### Absence scope

- Surfaces inspected: product README, session/kernel limits and cancellation, authorization and TUI commands.
- Plausible first-party paths checked: native task admission, resource limits, cancellation, approval/trust path and archive-based monitoring; no whole-system current view coupled to a discretionary resource/commitment decision returns to S1.
- Why no material first-party path remains: available mechanisms enforce predefined single-task constraints rather than provide S3 regulatory authority over the whole.

## S3* — Complementary audit

- State: —
- Function: no separately owned, complementary audit of ordinary agent claims is included in the assessed product path.
- Disturbance / variety regulated: a wrong success report could warrant independent raw-artifact scrutiny, but available replay/observation does not install an independent audit judgment and control return.
- Decisive decision or feedback right: no first-party independent audit selection/verdict and corrective closure evidenced.
- Decision owner: ordinary agent and human viewing archives; independent reviewer not packaged as a required or selectable audited owner.
- Supporting / enforcement mechanisms: run archive, deterministic protocol validation, UI replay and adjacent evidence web/tests.
- Closure path: replay informs a human observer; no S3* findings feed autonomous corrective control in the native loop.
- Why this is / is not agent-owned: retaining and replaying the same run is observability; adjacent test/evidence infrastructure is outside the product boundary.
- Evidence: [README replay and offline demo](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/README.md#L63-L88), [session terminal archive settlement](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/typescript/src/runtime/session.ts#L194-L203), [product versus evaluator split](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/README.md#L114-L126).
- Basis: structural.
- Confidence: medium-high for native product; not a claim about independent human review outside Pan.
- Caveats: operator inspection can be useful but is not evidence of a first-party complementary feedback loop.

### Absence scope

- Surfaces inspected: archive, replay/TUI documentation, session observations, test/evaluation reference boundary.
- Plausible first-party paths checked: archived raw run inspection, protocol validation, simulated evaluation and evidence-web adjunct; none supplies independent audit ownership with returned corrective authority in native standard mode.
- Why no material first-party path remains: the shipped Pan agent runs and records actions but does not incorporate a qualifying independent S3* loop.

## S4 — Outside-and-then intelligence

- State: —
- Function: no future-oriented external sensing → adaptation option → current-capability closure established.
- Disturbance / variety regulated: incoming user tasks and selected retrieval sources change S1 context, not a planned future capability portfolio.
- Decisive decision or feedback right: no autonomous or parent-returned strategic adaptation right in the packaged native session.
- Decision owner: operator selects retrieval corpus/runbook; model uses evidence to answer local tasks.
- Supporting / enforcement mechanisms: runbook context, opt-in retrieval, archives and task-level model planning.
- Closure path: sources enter S1 context, but no first-party feedback modifies durable present capability on prospective external analysis.
- Why this is / is not agent-owned: task planning and document/history retrieval do not alone realize S4's external-and-prospective loop.
- Evidence: [runbook injection lines 164–188](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/typescript/src/runtime/session.ts#L164-L188), [retrieval boundary lines 142–160](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/README.md#L142-L160).
- Basis: structural.
- Confidence: medium-high for supported native/product and source-built retrieval modes.
- Caveats: user may manually develop future plans using Pan, but that does not transfer strategic adaptation authority to the harness.

### Absence scope

- Surfaces inspected: source-build retrieval, archived history, runbook, native loop and README operating modes.
- Plausible first-party paths checked: retrieval, runbook revision, provider choice and historical improvement/dogfood experiments; no supported external prospective assessment producing returned capability decisions is wired into the assessed Pan runtime.
- Why no material first-party path remains: optional context enrichment and task execution stop at S1; no S4-specific first-party adaptation loop closes.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy dispute and legitimate authority/return loop established.
- Disturbance / variety regulated: file/path/shell risk and credential preferences are ordinary operational constraints, not identity-policy tensions with S3/S4.
- Decisive decision or feedback right: no identity-level charter revision decision is exposed to an autonomous/parent authority and returned to later operation.
- Decision owner: human operator selects task, configuration and permissions; authorization engine checks each scoped request.
- Supporting / enforcement mechanisms: base system prompt, runbook, key settings, path-classification and allow/deny channel.
- Closure path: ordinary approval/denial returns to the tool call, not an identity-policy outcome governing future system purpose.
- Why this is / is not agent-owned: operator control of dangerous effects or static instructions is not S5 merely because human approval can be final.
- Evidence: [authorization and trust lines 116–183](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/typescript/src/runtime/authorization.ts#L116-L183), [session prompt/runbook](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/typescript/src/runtime/session.ts#L164-L188), [operator control](https://github.com/pym96/Pan-agent/blob/6040fcadde20e2628ba18550848f3bb2c725e68e/README.md#L53-L61).
- Basis: structural.
- Confidence: high within declared runtime and documented operator modes.
- Caveats: OSS maintainer/release governance is adjacent; no organization-level parent S5 loop is borrowed from it.

### Absence scope

- Surfaces inspected: configuration, kernel/system prompt/runbook, approval/revocation, terminal supported modes and repository development boundary.
- Plausible first-party paths checked: ordinary operator permission and trust, local prompt revisions, user stop, maintained project policy; no identity/ultimate-policy matter and governing return-to-operation mechanism appears in the native distribution.
- Why no material first-party path remains: constraints and approvals regulate tool effects while the purpose/identity is supplied outside the assessed runtime; they do not decide that purpose.

## Recursion

The local native agent session is the S1 operating boundary assessed here; individual tool calls and the historical Python reference are not separately viable child organizations. Multiple independently launched sessions are not evidence of packaged cross-session VSM recursion.

## Variety and escalation

Model choice absorbs task-level environmental variety. Invalid provider output, missing credentials, cancellation and tool-step limits close as error/incomplete/cancelled terminal statuses. Exceptional shell/protected path effects reach an operator approval channel, but this is local authority over tool effects, not an independent S3/S5 function. The source-built retrieval feature preserves selected-material authorization rather than providing strategic governance.

## Evidence gaps

No live model-provider E2E was run; code, README and shipped/source-build mode wiring are primary evidence. Source-build retrieval is not claimed for published v0.1.6. No independent reviewer or observed organizational viability is inferred from deterministic tests, demos or archive replay.
