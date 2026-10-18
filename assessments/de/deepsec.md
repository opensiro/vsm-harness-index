---
harness_id: deepsec
project_name: deepsec
repository: https://github.com/vercel-labs/deepsec
review_ref: 42ed66efd3fc039767312e1b3aa66db6e173c850
reviewed_at: 2026-09-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-30
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# deepsec

## Review boundary

- System in focus: the first-party `vercel-labs/deepsec` security-scanning harness at frozen revision `42ed66efd3fc039767312e1b3aa66db6e173c850`, including its deterministic scanner, AI `process` workers, durable FileRecord/run state, claim/reclaim machinery, optional autonomous `revalidate` pass, reporting path, and repository-specific setup/coverage workflow where they bear on organizational function.
- Purpose and identity: inspect a target source repository for security vulnerabilities, use model-backed investigation to turn deterministic candidates into reasoned findings, support parallel/distributed execution without corrupting shared scan state, and optionally subject findings to a separate AI revalidation pass before they are consumed in reports.
- Relevant environment: target repository files and imports, git history, scanner candidates and detected technology, model/provider availability and quota, process cost/duration limits, sandbox/host process state, and the operator's configured project/model boundary.
- Standard-distribution boundary: the shipped Deepsec CLI plus `@deepsec/core`, `@deepsec/scanner`, `@deepsec/processor`, bundled agent adapters/prompts, setup workflow, durable `.deepsec`/data state and report/export commands are inside. OpenAI/Anthropic model inference, the external Codex/Claude/Pi SDK/runtime implementations, Vercel Sandbox infrastructure, and the scanned target repository are dependencies/environment rather than Deepsec organizational decision owners.
- Credited operating / distribution surfaces: `README.md`; `docs/architecture.md`; `packages/processor/src/index.ts`; `packages/processor/src/agents/{shared,codex-sdk,claude-agent-sdk,pi-sdk}.ts`; `packages/deepsec/src/commands/{process,revalidate,report}.ts`; `packages/deepsec/src/setup/coordinator.ts`; first-party core run/FileRecord state and lock primitives reached by those commands.
- Adjacent first-party surfaces excluded from ownership: repository tests/fixtures and CI; website/documentation generation; project-development self-scan or benchmark artifacts; release/install maintenance except where it establishes runtime reachability; contributor governance; external provider/SDK internals; target-project policy and remediation decisions made after Deepsec reports findings.
- First-party operating / deployment modes considered: local `scan` → `process`; concurrent `process` batches; distributed sandbox processing; resumable/reinvestigate paths; optional `revalidate`; `report`/export consumption; and `init`/setup through repository analysis, coverage evaluation, generated matcher attempts, final scan and processing.
- Recursion level: one Deepsec scanning organization around one target project. Concurrent model-backed investigation batches are operational S1 units over claimed file batches; deterministic shared-state machinery coordinates collisions between them. Revalidation is a separate complementary audit pass over produced findings, not another production S1 merely because it invokes a model.
- Reviewed revision: `42ed66efd3fc039767312e1b3aa66db6e173c850`.
- Observation date: 2026-09-30.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

Deepsec combines a deterministic candidate scanner with a model-backed processor. The scanner writes per-file records; `process()` selects eligible records, batches them, invokes a configured first-party agent adapter, persists findings/history and supports multiple batches concurrently. The default registry ships adapters for Claude Agent SDK, Codex SDK and Pi, while the actual model/provider remains external.

Concurrency is explicitly protected as a shared-state correctness problem. Before work begins, the processor atomically claims fresh FileRecords under a short process mutex and records `lockedByRunId`. Its own source describes the failure mode: two invocations can otherwise see the same pending record and later clobber findings/history. Locks are reclaimable only under explicit run-state/PID/staleness rules, so disjoint workers remain parallel while conflicting ownership is attenuated deterministically.

`revalidate` is a separate model-backed pass over existing findings. Its prompt requires the reviewer to read the full target file and relevant imports, trace data flow, construct an attack scenario, check framework protections, compare current code and git history, and return a verdict such as true-positive, false-positive, fixed or uncertain. Reconciliation persists that verdict and may adjust severity. The standard report path then uses revalidation state: its actionable stdout omits false-positive, fixed and duplicate findings and exposes revalidation reasoning in report output.

The setup workflow analyzes the current repository, evaluates current scan coverage and, while coverage fails, may ask an agent to propose bounded declarative matchers before re-scanning. This is useful adaptive setup for the present target, but the reviewed path does not establish a prospective environment model or future-facing adaptation authority. Runtime quota, cost, duration, concurrency and retry handling are likewise deterministic operating controls rather than an agent-owned S3 regulator.

Primary evidence:

- [`README.md`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/README.md)
- [`docs/architecture.md`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/docs/architecture.md)
- [`packages/processor/src/index.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/processor/src/index.ts)
- [`packages/processor/src/agents/shared.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/processor/src/agents/shared.ts)
- [`packages/deepsec/src/commands/revalidate.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/deepsec/src/commands/revalidate.ts)
- [`packages/deepsec/src/commands/report.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/deepsec/src/commands/report.ts)
- [`packages/deepsec/src/setup/coordinator.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/deepsec/src/setup/coordinator.ts)

## Operational model

A supported run first obtains deterministic candidate/state records, then model-backed investigation workers receive bounded file batches plus repository/project context and independently inspect source to decide whether concrete vulnerabilities exist. Their findings are persisted per file. Multiple workers can be active concurrently, but file ownership is mediated by first-party atomic claims and reclaim rules. An optional later revalidation run gives a model a distinct review task and additional evidence-gathering instructions; its verdict is persisted back onto the finding and affects the actionable reporting surface.

Agentic judgment is therefore credited at the investigation and revalidation layers. Claim ownership, stale-lock recovery, batch scheduling, cost/quota cancellation, setup phase gates and coverage-attempt limits are credited as deterministic runtime mechanisms unless a separate model-owned decision right is established.

## S1 — Operations

- State: A
- Function: perform environment-facing security investigation of candidate source files and produce reasoned vulnerability findings for the target repository.
- Disturbance / variety regulated: heterogeneous source code, framework-specific behavior, candidate vulnerability classes, data-flow/context ambiguity and repository evidence that determines whether a suspected issue is exploitable.
- Decisive decision or feedback right: choose what repository evidence to inspect and judge whether a candidate represents a concrete vulnerability, including title/severity/confidence/description/recommendation output within the assigned batch.
- Decision owner: the model-backed investigation actor invoked through Deepsec's shipped agent-plugin interface (`ClaudeAgentSdkPlugin`, `CodexAgentSdkPlugin`, `PiAgentPlugin`, or a registered compatible plugin).
- Supporting / enforcement mechanisms: deterministic scanner candidates; batch selection; repository/project context; prompt assembly; tool/shell/file access supplied by the chosen agent backend; FileRecord persistence; retry/parsing/reconciliation machinery.
- Closure path: scanner/state exposes candidate files → Deepsec invokes a model-backed investigation worker → worker inspects source/context and returns findings → processor validates/parses and persists findings/history → persisted output feeds report/revalidation and subsequent security handling.
- Boundary reachability: `deepsec process` and the documented init/setup path directly instantiate the shipped processor and default first-party agent registry; no separate application-authored orchestration layer is needed to reach the model-backed investigation actor.
- Why this is / is not agent-owned: removing the model-backed investigation actor leaves deterministic candidate/state machinery but removes the open-ended source interpretation and vulnerability judgment that turns candidates into findings.
- Evidence: [`README.md`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/README.md); [`docs/architecture.md`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/docs/architecture.md); [`packages/processor/src/index.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/processor/src/index.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: model inference and upstream coding-agent SDKs are external dependencies; Deepsec is credited for the shipped role/prompt/adapter/runtime path that operationally invokes them, not for provider internals.

## S2 — Coordination

- State: C
- Function: attenuate destructive interference among concurrent Deepsec S1 workers competing for the same pending FileRecords.
- Disturbance / variety regulated: duplicate claiming of the same file, concurrent processing of the same pending state, and resulting overwrite/clobber races in persisted findings/history.
- Decisive decision or feedback right: decide whether a file can be claimed by the current run or must remain owned by another run, including whether an existing ownership lock is reclaimable after completion/error, local-process death or staleness.
- Decision owner: constructor/runtime policy in Deepsec's deterministic process-lock and `lockedByRunId` claim/reclaim machinery; no autonomous S2 agent owns this right in the reviewed distribution.
- Supporting / enforcement mechanisms: project process mutex; fresh FileRecord re-read before claim; `lockedByRunId`/timestamp state; RunMeta phase; hostname/PID liveness; stale-lock threshold; atomic persistence; disjoint-batch concurrency.
- Closure path: concurrent runs expose a shared pending record → first-party claim/reclaim policy resolves ownership → the record is atomically marked for one run or withheld from another → only the owner proceeds with investigation/writeback → later run state or completion makes ownership releasable/reclaimable.
- Boundary reachability: the S2-specific claim path is embedded directly in the standard `process()` execution reached by `deepsec process` and distributed processing; an application author does not have to invent collision detection or shared-file claiming.
- Why this is / is not agent-owned: the S2 function and returned coordination effect are real, but the materially decisive ownership/reclaim rules are hard-coded runtime policy. An autonomous coordination actor/authority would still have to be composed to upgrade this path to `A`.
- Evidence: [`packages/processor/src/index.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/processor/src/index.ts); [`docs/architecture.md`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/docs/architecture.md).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: ordinary batching/concurrency alone is not the witness; the mapping depends on Deepsec's explicit same-record clobber race and its claim/reclaim feedback loop.
- Distinct S1 units: simultaneously active model-backed investigation batches/runs, each operating over file records it has claimed.
- Inter-S1 disturbance: without atomic claiming, two process invocations can observe the same pending FileRecord, both investigate it and overwrite/clobber findings/history.
- Attenuating coordination relation: the short project process mutex plus per-record `lockedByRunId` ownership and reclaim rules serialize the ownership decision while allowing disjoint work to remain concurrent.
- Feedback into subsequent S1 behaviour: a run that loses the claim does not investigate/write that FileRecord; a later run can only take it after the owner becomes terminal/dead/stale under the shipped rules.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the mechanism exists specifically to prevent a documented cross-worker shared-record collision and directly changes which S1 may act on the contested work.

## S3 — Inside-and-now control

- State: —
- Function: no material first-party agent/constructor/parent path was established for whole-organization current regulation distinct from deterministic run scheduling and limits.
- Disturbance / variety regulated: not established at S3 ownership level; the runtime handles batch completion/failure, quota exhaustion, cost/duration limits, stale locks and cancellation mechanically.
- Decisive decision or feedback right: not established. Operator-supplied limits and hard-coded retry/cancel/reclaim rules are enforced, but no first-party actor is given a whole-system current view and a substantive right to revise shared priorities, commitments, resources or constraints as an organizational judgment.
- Decision owner: not established.
- Supporting / enforcement mechanisms: batch counters, run metadata, AbortSignal, quota cancellation, `maxCostUsd`, setup duration limits, deterministic retry/error handling, claim/reclaim state and progress reporting.
- Closure path: not applicable; observed paths enforce preconfigured/runtime policy rather than closing a distinct S3 decision loop.
- Why this is / is not agent-owned: the model-backed workers perform investigation or revalidation; they are not shown owning the global batch/resource/commitment controller. The runtime can stop or reclaim work, but those decisions are encoded mechanically.
- Evidence: [`packages/processor/src/index.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/processor/src/index.ts); [`packages/deepsec/src/setup/coordinator.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/deepsec/src/setup/coordinator.ts); [`docs/architecture.md`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/docs/architecture.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: this does not deny that an operator can stop/restart/configure a scan; generic operational control does not itself satisfy the S3 ownership threshold.

### Absence scope

- Surfaces inspected: processor run lifecycle and batch scheduler; quota/cost/cancellation handling; FileRecord/RunMeta ownership state; setup coordinator/checkpoints; CLI process/revalidate/report paths; architecture documentation and supported sandbox/concurrency modes.
- Plausible first-party paths checked: whole-run progress/status; stale-worker recovery; error/retry handling; cost/quota/duration gates; setup coverage gates; concurrent/distributed worker management; operator configuration and resume paths.
- Why no material first-party path remains: every located whole-run intervention is either deterministic enforcement of a preset condition or operator configuration. No shipped model/constructor decision surface was found that owns current organization-wide allocation/commitment/prioritization judgment and returns a revised decision into ongoing S1 work.

## S3* — Complementary audit

- State: A
- Function: independently challenge produced vulnerability findings through a separate model-backed revalidation pass that gathers fresh repository/context evidence and assigns an audit verdict.
- Disturbance / variety regulated: false-positive findings, findings invalidated by code changes, duplicates, overstated severity, missing framework protections and unsupported exploitability claims from the ordinary investigation pass.
- Decisive decision or feedback right: judge an existing finding as true-positive, false-positive, fixed, duplicate or uncertain, supply reasoning and optionally adjusted severity after independently re-inspecting the relevant code/context.
- Decision owner: the model-backed actor invoked through the shipped `revalidate` agent-plugin path.
- Supporting / enforcement mechanisms: a distinct revalidation prompt; full-file/import/data-flow review instructions; recent git-history context; verdict parsing/reconciliation; stable finding IDs; persisted `finding.revalidation`; severity adjustment; report filtering/rendering.
- Closure path: ordinary `process` persists a finding → optional standard `revalidate` selects that existing claim → a model-backed reviewer re-reads code/context/history and returns a verdict → processor reconciles and persists the audit decision → report output exposes the verdict/reasoning and suppresses false-positive/fixed/duplicate items from actionable stdout.
- Boundary reachability: `deepsec revalidate` is a shipped first-party CLI command directly wired to the processor's agent `revalidate()` interface and default agent registry; it does not require a user-authored reviewer workflow.
- Why this is / is not agent-owned: deterministic reconciliation persists and applies the result, but the substantive audit verdict and reasoning are produced by the separate model-backed revalidation actor. Removing that actor removes the complementary judgment rather than merely its enforcement.
- Evidence: [`packages/deepsec/src/commands/revalidate.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/deepsec/src/commands/revalidate.ts); [`packages/processor/src/index.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/processor/src/index.ts); [`packages/processor/src/agents/shared.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/processor/src/agents/shared.ts); [`packages/deepsec/src/commands/report.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/deepsec/src/commands/report.ts).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: revalidation is optional and may use the same model family/provider as investigation; independence here is operational/contextual separation with a fresh review task and materially different evidence instructions, not organizational or provider independence.
- Claim being audited: an existing vulnerability finding emitted by the ordinary model-backed `process` investigation path.
- Ordinary reporting path: `process` parses and persists investigation findings on FileRecords, which are then available to normal report/export consumers.
- Complementary access path: `revalidate` creates a fresh agent invocation instructed to read the complete target file, relevant imports, end-to-end data flow, framework protections, current code and recent git history before judging exploitability/status.
- Independence boundary: revalidation is a separate invocation and role contract over already-persisted findings rather than the original producer merely self-labeling its own response in the same pass; its prompt/context includes audit-specific evidence and verdict semantics.
- Who acts on findings: first-party processor/report machinery persists the verdict, applies adjusted severity where supplied and changes the actionable reporting surface; downstream operators/remediation systems consume the returned audited state.

## S4 — Outside-and-then intelligence

- State: —
- Function: no material prospective environment-facing intelligence/adaptation loop was established beyond present-target scanning and setup adaptation.
- Disturbance / variety regulated: current repository technology, attack surface and scanner-coverage gaps are observed, but no future/prospective organizational adaptation disturbance is established.
- Decisive decision or feedback right: not established for S4. Setup can ask a model to propose declarative matchers when current coverage fails, but this responds to the presently scanned repository rather than judging future environmental developments or strategic adaptation options.
- Decision owner: not established at S4.
- Supporting / enforcement mechanisms: repository analysis; technology/surface inventory; coverage evaluation; bounded generated-matcher proposals; final rescan; persisted setup checkpoints.
- Closure path: not applicable at S4; the observed matcher loop is current-configuration adaptation inside setup.
- Why this is / is not agent-owned: a model can generate current-target matcher candidates, but the missing element is the S4 function itself: no distinct future/prospective environment model and return path into organization capability was found.
- Evidence: [`packages/deepsec/src/setup/coordinator.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/deepsec/src/setup/coordinator.ts); [`docs/architecture.md`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/docs/architecture.md); [`README.md`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/README.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: repository-specific generated matchers are meaningful adaptation, but Methodology requires the outside-and-then / prospective distinction rather than treating any learning/configuration change as S4.

### Absence scope

- Surfaces inspected: init/setup repository analysis, surface inventory, coverage evaluator, generated matcher loop, scanner technology detection, repeated process/revalidate/history paths, README/architecture descriptions and runtime configuration.
- Plausible first-party paths checked: current target technology sensing; coverage-driven matcher generation; repeated scans/reinvestigation; git-history use in revalidation; plugin/model configuration; persisted analysis history.
- Why no material first-party path remains: located adaptation responds to the current target or past/current finding evidence. No shipped path separates a prospective external/future model, generates adaptation options on that basis and returns a selected adaptation into present organizational capability as S4.

## S5 — Policy and identity

- State: —
- Function: no material first-party identity/ultimate-policy closure was established.
- Disturbance / variety regulated: model/provider selection, scan scope, limits, accepted-risk markers and output/remediation choices exist, but they are configuration/operational policy rather than an internally closed identity constitution.
- Decisive decision or feedback right: ultimate purpose, risk appetite, legitimate scan/remediation policy and authority remain with the operator/project boundary; no Deepsec agent is shown deciding what the organization ultimately is or which supreme policy should govern it.
- Decision owner: not established as a first-party S5 owner.
- Supporting / enforcement mechanisms: CLI/config options, model routing, preflight/auth checks, project state, manual accepted-risk preservation, report/export surfaces.
- Closure path: not applicable; no identity/policy issue → legitimate S5 authority → authoritative decision → returned governance loop was found inside the assessed distribution.
- Why this is / is not agent-owned: Deepsec agents investigate or audit security findings under supplied prompts/configuration; they do not possess ultimate-policy authority over the scanning organization's identity or mandate.
- Evidence: [`README.md`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/README.md); [`packages/processor/src/index.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/processor/src/index.ts); [`packages/deepsec/src/setup/coordinator.ts`](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/deepsec/src/setup/coordinator.ts).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: preserving an operator-authored accepted-risk marker is enforcement of external policy, not evidence that Deepsec owns S5.

### Absence scope

- Surfaces inspected: CLI/init/setup configuration; auth/model routing; process/revalidate state; accepted-risk handling; report/export surfaces; architecture/runtime documentation; plugin and operator controls.
- Plausible first-party paths checked: model/provider choice; risk/severity policy; accepted-risk state; scan scope; cost/duration constraints; project setup; plugin extensibility; operator review/remediation decisions.
- Why no material first-party path remains: these surfaces either execute operator/developer policy or expose operational configuration. No first-party agent, constructor-specific S5 decision surface or qualifying parent loop closes ultimate identity/policy authority and returns that authoritative decision into subsequent operation.

## Recursion

The assessed recursion is one Deepsec scan organization around one target repository. Investigation batches are parallel operational S1 units; the target application's own teams/processes and upstream model/provider organizations are outside this recursion. The optional revalidator audits S1-produced security claims at this recursion rather than constituting a separate viable organization.

## Variety and escalation

Deepsec amplifies operational variety through model-backed source investigation and parallel batches. Deterministic candidate generation narrows the search space; S2-specific claims prevent duplicate concurrent mutation of shared FileRecords; quota/cost/cancellation/retry mechanisms bound execution. Revalidation adds a separate autonomous challenge channel whose verdicts return to persisted findings and actionable reporting. Escalation beyond those shipped mechanisms remains operator-owned.

## Evidence gaps

No material evidence gap changes the published vector at the frozen revision. Provider/model internals are intentionally outside the ownership boundary. S3 and S4 were specifically checked against the tempting scheduler/coverage-generation paths and remain negative because their required organizational functions/owners are not closed by those mechanisms.
