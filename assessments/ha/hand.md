---
harness_id: hand
project_name: Hand
repository: https://github.com/sausheong/hand
review_ref: 201bda7bf531e8622d9f2a06f82237619371dbc0
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Hand

## Review boundary

- System in focus: the first-party Hand terminal coding agent at its shipped single-workspace, single-running-operation CLI, JSONL/RPC and embedded SDK boundary, including its model/tool loop, state, approvals, verification and optional integrations.
- Purpose and identity: perform open-ended coding and workspace investigation with a model-directed read/search/edit/command loop while retaining operator oversight, resumable evidence and bounded execution.
- Relevant environment: evolving source files, command errors, external web information, model and MCP availability, host/container trust boundaries, operator requests and permission decisions, and resource/cost limits.
- Standard-distribution boundary: pinned Hand Go source, shipped CLI and SDK, first-party app/agentio/config/permissions/verification/extension packages and documented installed modes; the external `github.com/sausheong/harness` library is credited only where Hand actually instantiates its runtime, not as a separate unconfigured agent organization.
- Credited operating / distribution surfaces: CLI one-shot/interactive agent loop, SDK/RPC access to the same bounded service, file/shell/web/search/tools, approved MCP and package extension tools, session branches/checkpoints, operator steering, goal-continuation hooks, verification profiles and workspace execution boundary.
- Adjacent first-party surfaces excluded from ownership: docs/superpowers planning and dogfood advice, developer implementation plans, acceptance ledgers and evidence bundles, examples, tests, release/CI governance, external provider and user-authored MCP/hook/extension agents not actually packaged into a standard multi-agent operating topology.
- First-party operating / deployment modes considered: local host tools and optional container tools, interactive and one-shot prompt execution, JSONL/RPC/SDK invocation, supervised approvals, session resume/fork and user-selected packages, optional local/remote MCP and hooks.
- Recursion level: one Hand application/service instance governing one current coding session and one autonomous model-backed work stream; session forks are alternative histories, not demonstrated simultaneously accountable operational units.
- Reviewed revision: `201bda7bf531e8622d9f2a06f82237619371dbc0` (batch #1013 row 7), observed 2026-10-24.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Hand is a native Go coding CLI built on the separate `sausheong/harness` library. The application constructs one model-backed runtime with a registered set of read/write/edit/bash/web/search/skill tools, wraps it in an application service, and exposes its operation via terminal, JSONL/RPC and SDK. The model chooses tool calls and next coding responses; runtime tools execute and return environmental observations. The service serializes one active goal operation, handles approval requests, user steering, cancellation and Stop-hook continuations. The single-operation busy guard is not evidence of coordination between independently operating S1 units.

The distribution includes durable named/forked/restorable sessions, bounded context/pins, model profiles and fallback, background shell processes, host or pinned-container tool execution, scoped/revocable permissions, trusted package installation and optional MCP/extension/hook integration. Hooks are *operator-configured external processes*: a `Stop` hook may inject a further prompt until a configured goal passes; it is not a bundled independent auditor or autonomous strategy decision-maker. First-party verification profiles execute a caller-authorized command, capture before/after workspace evidence, validate staleness and return a record, but do not supply an independent semantic assessor.

Primary frozen source: [README](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/README.md), [CLI runtime composition](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/cmd/hand/main.go), [first-party tools](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/agentio/registry.go), [application service](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/app/service.go), [hook runner](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/agentio/hooks.go), [verification](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/app/verification.go).

## Operational model

An operator supplies a coding objective and optionally authorizes workspace/tool effects. Hand builds a model runtime, returns actual read/search/shell/file results to the model and can run further model turns when a configured Stop validator requests goal continuation. A user can adjust current instructions, approve/deny tools or suspend activity. Session branches and background processes do not acquire independently accountable S1 mandates. The service/runtime implements safety and transaction integrity; its control mechanisms do not automatically constitute S2/S3/S3*/S4/S5 decision ownership. Assessment is source/static-script based: no live provider, LLM-agent or Browser benchmark was run.

## S1 — Operations

- State: A
- Function: produce requested code/investigative changes by adjusting workspace actions to repository evidence and tool feedback.
- Disturbance / variety regulated: unknown file organization, changed requirements, shell and compiler errors, external information, provider interruptions and incremental operator feedback.
- Decisive decision or feedback right: choose and revise concrete file reads/edits, shell actions, search queries and task response after model/tool observations.
- Decision owner: the model-backed Hand agent in the supported coding loop, bounded by operator permissions and configured runtime.
- Supporting / enforcement mechanisms: tool registry, model client, scoped approvals, host/container backends, session history, context trimming, budget caps, hook outputs and replay/restore.
- Closure path: prompt and workspace observations → model-selected tools and edits → first-party execution → result/error feedback in model context → revised actions or completion.
- Boundary reachability: normal CLI creates the registered tool-runtime and `app.NewHarness` service; the same first-party service is exposed through automation and SDK rather than requiring an external user-authored orchestration script.
- Why this is / is not agent-owned: the model chooses open-ended actions and revisions; deterministic file tools and limits cannot produce those judgments on their own.
- Evidence: [CLI runtime](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/cmd/hand/main.go), [tool registration](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/agentio/registry.go), [HarnessBackend](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/app/harness.go).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this establishes wired autonomous decision rights, not live model task quality; underlying generic Harness capabilities not instantiated by Hand are excluded.

## S2 — Coordination

- State: —
- Function: no first-party coordination relation between two concurrently accountable, separately deciding Hand operational units is established.
- Disturbance / variety regulated: potential overlap of session writes or background command effects is handled by one service/session ownership and resource admission, not shown as oscillation between distinct S1 agents.
- Distinct S1 units: the shipped normal Hand operation is one autonomous model loop; session forks are separate selectable histories and background commands are tools, not separate S1 agents with independent outcome commitments.
- Inter-S1 disturbance: no instantiated pair of S1 cells with a concrete mutual-interference path found.
- Attenuating coordination relation: application `ErrBusy` single-operation exclusion prevents overlapping service operations; it is not mutual adjustment among S1 units.
- Feedback into subsequent S1 behaviour: admission errors and command results affect the one active model/user, not multiple units adjusting to one another.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the observed serialization is a single-service ownership guard; no S2-specific multi-unit function is evidenced.
- Decisive decision or feedback right: no established inter-S1 negotiation or collision-response choice.
- Decision owner: no S2 owner identified; developer-written service admission and workspace locks enforce one operation at a time.
- Supporting / enforcement mechanisms: `ErrBusy`, session record/store ownership, background process tracking, RPC submit admission and checkpoints.
- Closure path: concurrent application commands are rejected/queued or serialized; no separate coordinated adjustment returned to multiple S1 agents.
- Why this is / is not agent-owned: the sole model's tool planning is operational S1, whereas the concurrency decision is fixed in code.
- Evidence: [service](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/app/service.go), [session management](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/sessionio/manager.go), [background processes](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/app/processes.go).
- Basis: structural bounded absence review.
- Confidence: medium-high.
- Caveats: separately configured MCP/extension systems may coordinate elsewhere; their agency/closed S2 is not built into this reviewed Hand instance.

### Absence scope

- Surfaces inspected: shipped CLI, registered tools, service operation reservation, session forks/catalogue, background processes, RPC/SDK and optional package/MCP integration documentation.
- Plausible first-party paths checked: session fork as another S1, background jobs as parallel agent cells, goal-loop iteration as orchestration, `ErrBusy` as coordination and MCP tools as multi-agent negotiation.
- Why no material first-party path remains: the reviewed default and supported optional modes demonstrate one deciding S1 and no first-party assembly of two S1 decision-makers with interference-damping feedback.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-current control authority over multiple independent operating commitments is established at the Hand application recursion.
- Disturbance / variety regulated: per-run budget, shell processes and current session status are managed for bounded execution of one task, not an organization of S1 commitments.
- Whole-system current view: the service publishes one session/run state and usage, and the operator can inspect tasks, process output and verification records; no cross-S1 operations/performance view exists.
- Current-control decision scope: user choices of budgets, permissions, model and cancellation plus fixed runtime admission; no distinct live resource bargaining or commitment reallocation across operational units.
- Decisive decision or feedback right: no evidenced separate whole-system resource/commitment control decision beyond operational task actions and operator configuration.
- Decision owner: model for task-level decisions, human for per-session policy/config; no autonomous or qualifying parent S3 loop at the assessed recursion.
- Supporting / enforcement mechanisms: token/cost/wall/run caps, goal-loop iteration cap, `ErrBusy`, process management, verification records and session/status reporting.
- Closure path: configured limits and user steering → one bounded run; whole-current portfolio observations → distinct authority → revised multi-unit commitments is absent.
- Why this is / is not agent-owned: safety limits constrain S1, while even an operator's steering of one coding task does not establish a parent current-control system over multiple independently accountable operations.
- Evidence: [service state and admission](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/app/service.go), [budget](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/app/token_budget.go), [CLI modes and caps](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/README.md).
- Basis: structural bounded absence review.
- Confidence: medium-high.
- Caveats: a separate client may build portfolio supervision using Hand SDK/RPC; this is not an instantiated first-party organizational loop.

### Absence scope

- Surfaces inspected: service state, resource budgets, process tool, goal continuation, CLI status/timing, session and SDK/RPC control methods.
- Plausible first-party paths checked: runtime budget monitors as S3 owner, operator steering as parent S3, single active-run tracker as whole-current management and scriptable SDK as S3 constructor.
- Why no material first-party path remains: no independently instantiated multi-unit operating portfolio plus function-specific current-control return exists; caps/admission enforce previously chosen constraints for one S1.

## S3* — Complementary audit

- State: —
- Function: no built-in sufficiently independent audit judgment and corrective feedback outside the ordinary coding/verification route is established.
- Disturbance / variety regulated: stale test evidence, changed files and false success claims are guarded by deterministic verification checks; they do not by themselves establish independent audit of the agent's operational account.
- Claim being audited: an agent's coding result or reported verification should reflect actual source state and command output.
- Ordinary reporting path: same runtime tool results and user/configured Stop-hook checks are reported within normal execution; verification commands run when explicitly authorized and their outputs/status are recorded.
- Complementary access path: checkpoint capture compares workspace digests before/after and validates saved command artifacts; it directly accesses files but implements ordinary requested verification, not a separate semantic audit authority.
- Independence boundary: no separately instantiated reviewer with authority to challenge agent claims independently of the user-authorized test profile; external hook authors could provide such a reviewer but are outside the credited standard distribution.
- Who acts on findings: the operator or coding Agent can react to failed command/check status; no separate first-party audit control owner.
- Decisive decision or feedback right: deterministic passed/failed/stale assessment of configured command evidence, with no complementary judgment of independently sampled operational reality.
- Decision owner: developer-configured verification logic/operator-provided command; no autonomous S3* audit owner in reviewed mode.
- Supporting / enforcement mechanisms: checkpoint digests, command/exit records, profile hash, artifact integrity checks and mandatory Stop-hook failure gates.
- Closure path: snapshot/command evidence → fixed status/gate → ordinary operator or model continuation; independently originated audit evidence → audit judgment → S3 correction is not shown.
- Why this is / is not agent-owned: the evaluator's correctness criterion is a preconfigured command, and the agent does not control an independent observer with complementary audit discretion.
- Evidence: [verification runner](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/verification/run.go), [authorization boundary](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/app/verification.go), [hook evaluation](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/agentio/hooks.go).
- Basis: structural bounded absence review.
- Confidence: medium-high.
- Caveats: snapshot-based verification is substantive and security relevant; this classification only denies a distinct independent S3* organizational audit function.

### Absence scope

- Surfaces inspected: verification profiles, record validation and recheck, context injection, Stop/PreTool hooks, session checkpoints and example verification extension.
- Plausible first-party paths checked: mandatory verification as S3*, raw snapshot capture as direct audit, Stop validators as separate auditor and external extension observers as an included audit loop.
- Why no material first-party path remains: verification is fixed current-task acceptance with caller-selected commands and no independent audit judgment/closure; optional custom code is not shipped as a connected independent reviewer.

## S4 — Outside-and-then intelligence

- State: —
- Function: no instantiated prospective environmental intelligence → strategic capability option → present capability adaptation loop is evidenced.
- Disturbance / variety regulated: provider availability, web search results and context limitations influence current coding execution; installed packages and model profiles are configured by humans.
- Decisive decision or feedback right: no organizational capability-adaptation option selection arising from a future/external model beyond current task and operator package/model choices.
- Decision owner: human operator/developer chooses model profiles, packages, upgrades and external integration; model responds to current task demands.
- Supporting / enforcement mechanisms: provider fallback/metadata catalogue, web search, learned session context, package import/review, SDK controls and configurable hooks.
- Closure path: external web/tool information → current code task decisions exists; prospective environment monitoring → tested capability alternative → adoption through S3 is absent.
- Why this is / is not agent-owned: changing model endpoint after failure or acquiring new web facts for a task does not amount to autonomous future-oriented adaptation.
- Evidence: [README packages and model configuration](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/README.md), [profile metadata](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/config/profiles.go), [package command](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/cmd/hand/packages.go).
- Basis: structural bounded absence review.
- Confidence: high.
- Caveats: human product-development plans in the repository are adjacent organization work and do not close a Hand runtime S4.

### Absence scope

- Surfaces inspected: built-in web tools, provider profiles/fallback, session context, package/skill management, hook examples, README and maintainer development plans.
- Plausible first-party paths checked: automatic provider fallback as adaptive strategy, user package import as parent S4, session memory as horizon model and web search as strategic scanning.
- Why no material first-party path remains: these are current-task tools, static selections or human maintenance; no shipped future-oriented strategic option assessment with return to present organizational capabilities is instantiated.

## S5 — Policy and identity

- State: —
- Function: no first-party runtime pathway for ultimate system identity or ethos controversies to receive legitimate adjudication and binding return.
- Disturbance / variety regulated: unsafe commands, unauthorized writes, untrusted packages and integrations are controlled as operational permission/trust issues, not identity-level policy decisions.
- Identity / ultimate-policy issue: Hand's declared role is a user-directed coding assistant; there is no supported institution/process deciding changes to that ultimate role, ethos or mission during operation.
- Ultimate authority in each claimed mode: no S5 mode claimed; user/developer authors configuration, selects tools, grants permissions and maintains code without a separate identity-level return loop at Hand recursion.
- Return-to-operation path: scoped allow/deny decisions and configuration change constrain individual tools or sessions; policy-identity issue → legitimate parent decision → governing return is not established.
- Decisive decision or feedback right: ordinary per-tool grant/deny and configuration rights, not ultimate-policy adjudication.
- Decision owner: human operator/developer for constraints and deployments; no autonomous S5 authority in the standard runtime.
- Supporting / enforcement mechanisms: permission grants/revocations, trust acknowledgement, immutable worker digest and package review/approval.
- Closure path: authorization request → user grant/deny → subsequent tool execution changes; no function-specific S5 identity-governance closure.
- Why this is / is not agent-owned: the model executes user tasks within configured limits but cannot legitimately amend the system's ultimate mission, nor does the UI establish a parent S5 adjudication channel.
- Evidence: [README approvals and config](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/README.md), [scoped permissions](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/permissions/scoped.go), [approval service](https://github.com/sausheong/hand/blob/201bda7bf531e8622d9f2a06f82237619371dbc0/internal/app/approval.go).
- Basis: structural bounded absence review.
- Confidence: high.
- Caveats: legitimate governance of the upstream OSS project is outside the installed Hand system-in-focus.

### Absence scope

- Surfaces inspected: global and workspace config, session approval modes, scopes, package and extension admissions, local/container execution trust boundaries and maintainer guidance.
- Plausible first-party paths checked: user tool approval as parent S5, persistent trust grants as constitutional decision, developer governance as product S5 and untrusted extension control as identity enforcement.
- Why no material first-party path remains: none exposes an ultimate-policy controversy and subsequent binding identity-level return; reviewed controls are permissions and fixed product settings.

## Distributed OSS parent arrangement

Hand can be installed independently by multiple people, but no shared organizational hierarchy among those installs is bundled. Upstream maintainers and developer project-management records are not borrowed as a Hand runtime parent S3/S4/S5 authority.

## Self-hosted and non-human modes

Local host and container execution, CLI and SDK all preserve operator-set limits and one model-backed operational work stream. Separate client applications may compose a richer organization, but no bundled autonomous metasystem or function-specific parent loop is established solely by exposing RPC/SDK controls.

## Recursion

The model/tool operation is an S1 cell with real source-code outcome responsibility. Session branches and spawned shell processes do not possess separate identities and metasystems sufficient to infer further viable-system recursion; the generic external Harness library is not automatically a nested Hand operating organization.

## Variety and escalation

Model decisions, broad workspace tooling and user-loaded skills expand S1 response variety. Permissions, tool execution isolation, snapshots, mandatory checks and spend/time bounds attenuate risk and cost. Errors, explicit approval requests, and failed Stop validations reach the operator or model continuation, but no evidence of a separate whole-current S3, future-facing S4 or policy-level S5 closure is supplied.

## Evidence gaps

- The upstream `sausheong/harness` dependency has additional generic primitives; only concrete wiring from the pinned Hand repository is considered. No inference is made from library marketing or unconfigured extensions.
- Operator-chosen verification profiles inspect direct artifacts but no distinct independent semantic audit owner is instantiated, so S3* is bounded absence rather than a claim that verification is ineffective.
- Supported RPC/SDK and packages could enable a separately built multi-agent organizational wrapper; the assessed source does not wire that wrapper into its standard distribution.
- No live LLM provider, executable agent quality experiment, or Browser evaluation was run; source-level claims and deterministic Index tests are the evidentiary scope.
