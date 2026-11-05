---
harness_id: harnessmm
project_name: HarnessMM
repository: https://github.com/YuhuaJiang2002/HarnessMM
review_ref: 8c4ff0f98332fab2dca5916dee63970d87c554e6
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: excluded-no-agentic-vsm
autonomy_s1: —
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# HarnessMM

**Canonical disposition: EXCLUDED — no independently closed first-party agentic S1.** This repository provides meaningful, source-backed *constructor* affordances around an external harness, but Methodology 0.3.7 does not admit an unassembled `S1=C` as an autonomous harness. An integrated Codex/DeepSeek host may be assessed at its own system boundary; importing its S1 ownership would conflate different repositories. The proposed review-stage `C / — / — / — / C / —` expressed the opt-in construction affordances, not an already operating S1 or a canonical ownership vector.

## Review boundary

- System in focus: The public HarnessMM decision-graph/callback-substitution library and opt-in training/selection constructor at its exact pinned repository revision, not the external Codex or DeepSeek host agent organization.
- Purpose and identity: Reuse recorded valid tool decisions in agent harness runs and select training-derived future execution instructions without taking over the native agent loop, tool executor, scoring or ultimate policy.
- Relevant environment: Developers integrating an existing slow reasoning actor, native tool dispatcher, observations and provider accounting; task histories, receipts, model endpoints, benchmark/task distributions and changing usage constraints.
- Standard-distribution boundary: Released Python `harnessmm` modules, JavaScript integration contracts, explicitly documented baseline and Codex/DeepSeek adapters; these are callback-based first-party constructors, not a self-hosted agent product that supplies its own model and tool host.
- Credited operating / distribution surfaces: [README](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/README.md), [integration contract](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/docs/INTEGRATION.md), [baseline decision boundary](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/integrations/baseline_harness/visual.py), [CHISEL controller](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/harnessmm/harness/codex_chisel.py), [DeepSeek SDK bridge](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/integrations/deepseek_harness/runner.py), [first-party integration example](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/examples/guarded_reuse.mjs).
- Adjacent first-party surfaces excluded from ownership: Training/reproduction scripts, benchmark native scorers, model-provider accounts and credentials, synthetic examples/tests, old PhiAgent compatibility paths, author/contributor project governance and source manifests. These corroborate library behavior but do not import the external host's S1/S3/S5 rights.
- First-party operating / deployment modes considered: Screenshot `VisualBaseline` with caller-provided metered actor; native graph/callback integration into an existing tool loop; opt-in Codex/DeepSeek CHISEL optimizer with caller-provided execute/optimize callbacks and explicit train/validation/freeze/test; synthetic local examples. The DeepSeek official SDK remains separately supplied and environment-specific.
- Recursion level: One integrated agent task/run and its optional future training-to-deployment harness configuration; distinct experimental trials and external host processes are not assumed to be autonomous S1 cells of a shared HarnessMM organization.
- Reviewed revision: `YuhuaJiang2002/HarnessMM@8c4ff0f98332fab2dca5916dee63970d87c554e6`.
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The package intercepts a native model-to-tool decision boundary. An external slow actor authors candidate literal actions and dependencies; graph eligibility/receipt guards determine when a recorded action may replace a further model callback. A native tool dispatcher remains the authority over execution, and the actual receipt returns through `observeTool`. Invalid, unsupported or exhausted graphs fall back to the original slow model path. `VisualBaseline` exposes model decision and action compilation using an injected `actor`, but leaves episode loops, native action dispatch, scoring and provider accounting with its host. Optional CHISEL controls training-only optimizer proposals, paired execution, split isolation, validation selection, source/policy freeze and test deployment; callbacks and model access are host supplied. [Integration](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/docs/INTEGRATION.md); [visual boundary](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/integrations/baseline_harness/visual.py); [optimizer](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/harnessmm/harness/codex_chisel.py).

## Operational model

The actual task-solving agent is the externally integrated model/host loop, which decides goals, native tool arguments and continuation. HarnessMM offers a specific constructor around that operational decision point, rather than an independently installed end-to-end S1. Its graph guard is deterministic and never acquires autonomous organizational discretion by suppressing a paid callback. Optional optimization affects *future* task runs by composing model-optimized residual instructions with guarded selection; the optimizer and executor are supplied by a developer or parent experiment runner. Training/validation/test isolation is experimental procedure, not a second product-level management organization.

## S1 — Operations

- State: —
- Function: No standalone first-party autonomous operational S1 loop is supplied by the published HarnessMM package; the decision-boundary constructor is not an included operational cell.
- Disturbance / variety regulated: New screenshot/tool outcomes, tool argument uncertainty, unexpected receipts and exhaustion of stored eligible actions.
- Decisive decision or feedback right: A model-backed *external host actor* chooses literal actions; `VisualBaseline.decide` requests and parses it, while the graph contract can reuse previously authored actions only when the current receipt justifies them.
- Decision owner: The host-injected reasoning actor owns discretionary task action selection; HarnessMM supplies the first-party specific callback interfaces and guard/reuse path but no autonomous actor/native dispatcher as a standalone default.
- Supporting / enforcement mechanisms: Action schema validation, guarded-decision graph, native receipt checking, callback substitution certificates, fallback and metered event log.
- Closure path: Host observation/current screenshot → supplied model decision or receipt-supported saved decision → host native tool dispatch → native receipt returned to next guarded boundary/slow actor.
- Boundary reachability: The documented `VisualBaseline(actor=..., audit=...)` and `ExecutableSubdag(...).observeTool(...)` APIs are shipped and exercised through local examples; completing an autonomous task requires an explicit host provider, native executor and episode loop, so these constructor affordances are not an installed first-party S1.
- Why this is / is not agent-owned: An integrated model actor can own S1 choices, but neither the deterministic reuse guard nor a host-supplied callback automatically makes that agent a first-party owned and wired HarnessMM standard-distribution S1.
- Evidence: [Baseline readme](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/integrations/baseline_harness/README.md), [visual adapter](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/integrations/baseline_harness/visual.py), [integration guide](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/docs/INTEGRATION.md).
- Basis: Bounded exclusion after explicit review of first-party construction and the missing autonomous deployment witness.
- Confidence: High for constructor boundary; medium on whether a narrower integrated-host framing could be admitted as autonomous S1.
- Caveats: Codex and DeepSeek's separate native loops cannot be donated to HarnessMM without changing the declared boundary; no provider-backed E2E run conducted. The noncanonical proposal recorded S1 constructor C, but the accepted inclusion gate requires actual S1 A.

### Absence scope

- Surfaces inspected: Released baseline adapter, callback/graph integration, native Codex/DeepSeek adapters, CHISEL runner contracts, synthetic examples and first-party tests.
- Plausible first-party paths checked: `VisualBaseline.decide` as task loop, callback substitution as autonomous action, CHISEL's execute/optimize hooks as in-repository agent, DeepSeek SDK runner as packaged agent.
- Why no material first-party path remains: These all require the external slow actor, host SDK/runtime, native tool dispatcher, task episode owner or experiment callbacks to complete S1; none is shipped as a self-contained HarnessMM task-operating agent loop at the declared boundary.

## S2 — Coordination

- State: —
- Function: No demonstrated coordination of distinct viable S1 operating units at this HarnessMM run boundary.
- Disturbance / variety regulated: Independent optimizer trial collisions or shared execution resources are possible in an external campaign, but not an established in-boundary inter-S1 disturbance.
- Decisive decision or feedback right: CHISEL executor-worker limits and isolated workspaces order independent evaluations; no inter-S1 negotiation or conflict response is supplied.
- Decision owner: Static developer/runner config and deterministic execution scheduler.
- Supporting / enforcement mechanisms: Worker bounds, pair ordering, source/test seals, isolated run directories.
- Closure path: Scheduling and test records return to experiment selection, not a feedback relation regulating two concurrent autonomous S1 cells.
- Why this is / is not agent-owned: Technical parallel tasks and trial reservations are not proof of inter-S1 organizational coordination.
- Evidence: [CHISEL controller](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/harnessmm/harness/codex_chisel.py), [integration guide](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/docs/INTEGRATION.md).
- Basis: Structural bounded negative.
- Confidence: Medium-high.
- Caveats: External native host platforms may coordinate their own agents.

### Absence scope

- Surfaces inspected: Public integration modes, runner/CHISEL concurrency and selection interfaces, baseline adapter and native decision-graph examples.
- Plausible first-party paths checked: Trial worker pool as S2, graph dependency edges as S2, host tool bridge as inter-agent channel.
- Why no material first-party path remains: Each concerns one callback/independent trial; no two separate S1 work cells, specific interference, attenuating decision and returned inter-S1 coordination are shipped together.

## S3 — Inside-and-now control

- State: —
- Function: No separately established whole-system current operations manager over multiple agent work commitments.
- Disturbance / variety regulated: Token cost, execution errors, trial concurrency and task completion uncertainty are monitored locally.
- Decisive decision or feedback right: The host controls native episode, model budget, dispatch, scoring and stopping; CHISEL selection changes future policy configuration, not present whole-system resource commitments between viable S1 units.
- Decision owner: External host/operator for current commitments; deterministic guards for immediate callback validity.
- Supporting / enforcement mechanisms: Receipt checks, usage ledgers, frozen experimental partitions and safe fallback.
- Closure path: Invalid action returns to the same slow actor; no shipped HarnessMM S3 manager decides and returns a current multi-operation intervention.
- Why this is / is not agent-owned: Blocking a callback on a deterministic receipt condition is enforcement, not ownership of resource or priority authority.
- Evidence: [Integration](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/docs/INTEGRATION.md), [CHISEL](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/harnessmm/harness/codex_chisel.py).
- Basis: Bounded structural negative.
- Confidence: Medium-high.
- Caveats: A parent experiment campaign can exercise current control outside this constructor.

### Absence scope

- Surfaces inspected: Callback/graph runtime, host contract, training/validation worker limits, source/policy freeze and operational example.
- Plausible first-party paths checked: Cost ledger as S3 executive, guard rejection as S3 intervention, optimizer candidate selection as S3 priority allocation.
- Why no material first-party path remains: These are per-boundary controls or future policy selection; a distinct whole-current-system view and discretionary shared commitment authority are not wired into the released library.

## S3* — Complementary audit

- State: —
- Function: No first-party complementary organizational reality-audit channel from distinct evidence into a controlling S3.
- Disturbance / variety regulated: False tool receipts, malformed actions, benchmark score error or optimizer overfitting.
- Decisive decision or feedback right: Guards validate reported receipts and validation holds out training data; neither establishes an independent audit judge challenging routine S1/S3 performance claims with corrective return into S3.
- Decision owner: Deterministic local code/host native scorer; no independently authorized in-boundary auditor.
- Supporting / enforcement mechanisms: Receipt certificates, source seals, validation split, unit tests and benchmark accounting.
- Closure path: Invalid receipt → fallback/abstain or experiment selection; no independent finding → separate whole-current manager correction path.
- Why this is / is not agent-owned: Source verification and held-out performance evaluation are meaningful quality checks but do not acquire an organizational S3* mandate or independent judgment merely by being different code.
- Evidence: [README](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/README.md), [CHISEL](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/harnessmm/harness/codex_chisel.py), [integration](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/docs/INTEGRATION.md).
- Basis: Bounded negative against concrete audit candidates.
- Confidence: Medium-high.
- Caveats: The frozen-run auditor and external benchmark scorer are adjacent experiment/QA paths; a separate host may supply audit authority.

### Absence scope

- Surfaces inspected: Receipt guard/certificates, frozen rollout and evidence validation modules, CHISEL partitions, first-party integration docs.
- Plausible first-party paths checked: Native tool-receipt corroboration, held-out validation as independent audit, experimental frozen-run auditor as S3*.
- Why no material first-party path remains: No materially distinct independent auditor with a S3 organizational reporting claim and actionable corrective return is established inside the supported integrated-task boundary.

## S4 — Outside-and-then intelligence

- State: —
- Function: No installed HarnessMM-owned strategic S4 loop jointly regulating current task operations; the opt-in CHISEL train/validation/freeze constructor belongs to external host/experiment composition.
- Disturbance / variety regulated: Changing future task mix, inefficient repeated model callbacks and performance/cost tradeoffs beyond the current task.
- Decisive decision or feedback right: An injected optimizer proposes reusable residual instructions from TRAIN evidence; held-out VALIDATION selects eligible improvement and freezes a policy before a later TEST/deployment run.
- Decision owner: Developer-provided optimizer actor and executor callbacks own the decisive behavioral proposal and external host owns deployment; first-party CHISEL provides partition-safe selection/freeze machinery without its own S3–S4 closure.
- Supporting / enforcement mechanisms: Split seals, cross-fit residual routing, score/usage ledgers, source/policy hashes and no-validation-leak guards.
- Closure path: Prior native execution and task feedback → optimizer proposes future behavior option → independent validation selects or abstains → source/policy freeze → subsequent executor receives selected instruction in native task prompt/AGENTS.md.
- Boundary reachability: Public `CodexChiselController(train, select_validation, freeze, evaluate_test)` is shipped, but explicit externally supplied `execute` and `optimize` callbacks and host policy are indispensable; this is a research adaptation constructor, not installed autonomous S4 of the assessed standalone package.
- Why this is / is not agent-owned: The potential optimization candidate is model-authored by a supplied optimizer, but the published package does not itself own the external actor or operational S3 which would adopt a future strategy.
- Evidence: [CHISEL docstring and implementation](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/harnessmm/harness/codex_chisel.py), [README future-configuration description](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/README.md), [integration contract](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/docs/INTEGRATION.md).
- External distinction: Native task feedback and out-of-sample task distribution distinguish behavioral weaknesses not visible in one callback.
- Future / prospective distinction: Trained residual options are selected and frozen *before* future holdout/deployment tasks; validation/test evidence must not return to the optimizer.
- Adaptation option generated: A bounded residual task instruction/router configuration chosen against actual quality and token cost.
- Path back into current capability / S3: The selected frozen instruction is injected into the next run's native agent prompt/AGENTS.md, preserving the host's current tool loop and scoring contract; external host operational control remains separately owned.
- Basis: Bounded negative for standalone organizational S4, while preserving the concrete first-party prospective constructor witness.
- Confidence: Medium: evidence supports future adaptation constructor, while whether a deployed host would establish a fully separated S3–S4 organizational conversation depends on composition.
- Caveats: Experimental optimization of a fixed benchmark alone must not be misreported as autonomous external sensing or current-product S4; a separately composed host may create that organization.

### Absence scope

- Surfaces inspected: CHISEL train/validation/freeze/test contract, integration/README docs, configured native host/optimizer boundaries and baseline callback mode.
- Plausible first-party paths checked: Residual optimizer as future strategic agent, validation-selected instruction as capability policy, experiment `freeze` as return to S3, paper's recursive self-improvement claims.
- Why no material first-party path remains: Future-policy selection is available only through externally supplied optimizer/executor and benchmark/host ownership; no packaged own S3 operations and externally prospective S4 actor exchanging options and closing them in subsequent HarnessMM-owned operations.

## S5 — Policy and identity

- State: —
- Function: No shipped ultimate identity/ethos/policy decision-return loop at the assessed harness recursion.
- Disturbance / variety regulated: Model/tool constraints, source contamination, train/test integrity and developer policy concerns.
- Decisive decision or feedback right: Static policies and provenance freezes constrain execution; human developers choose the benchmark/project purpose and any exceptional rule changes outside the run.
- Decision owner: External developer/host for normative choices; guard code enforces a preselected policy.
- Supporting / enforcement mechanisms: Frozen config, source hashes, callback schemas, restricted evaluation access and tools.
- Closure path: Developer updates to library/config are external production changes, not a shipped runtime identity dispute → legitimate parent decision → returned operation path.
- Why this is / is not agent-owned: No agent or bounded parent mode closes the system's identity-level decisions; prompt instructions and safety checks do not establish S5.
- Evidence: [CHISEL configuration](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/harnessmm/harness/codex_chisel.py), [integration contract](https://github.com/YuhuaJiang2002/HarnessMM/blob/8c4ff0f98332fab2dca5916dee63970d87c554e6/docs/INTEGRATION.md).
- Basis: Bounded negative.
- Confidence: Medium-high.
- Caveats: The external host or contributing laboratory may have separate human ultimate authority.

### Absence scope

- Surfaces inspected: Public package/integration docs, source/policy frozen config paths, provider and developer boundaries, callback APIs.
- Plausible first-party paths checked: Trial admission/freeze as identity governance, host permission constraints, project/research optimization policy as S5.
- Why no material first-party path remains: All are fixed safeguards or developer decisions outside runtime; no first-party identity/policy matter is routed to a legitimate authoritative owner and returned as changed subsequent operating policy.

## Recursion

Native host tasks may contain many subcalls, but guard graph nodes, optimizer trials and benchmark repetitions do not thereby become autonomous viable S1 units. HarnessMM primarily supplies a composable local agent-decision boundary and an optional future configuration selection loop; external host ownership is not promoted into an independent nested metasystem.

## Variety and escalation

Eligibility predicates attenuate action variety by reusing only current-receipt-compatible recorded calls; invalid/unsupported evidence yields safe abstention to the original slow actor. Cost/quality evidence broadens the optimizer's future option set while partition/source seals guard against overfitting. Real tool faults, missing external provider, source/score disputes and ultimate policy exceptions return to the host/developer. Ordinary callback abstention is not an algedonic S5 channel.

## Evidence gaps

- The first-party distribution provides no one-command, credential-free full native Codex/DeepSeek episode; synthetic tests establish interface behavior rather than deployed autonomous S1 ownership.
- S1/S4 constructor affordances were explicitly considered at the proposal stage; canonical exclusion does not claim they are useless. A later host-integrated source-first review may move the boundary but cannot silently borrow external host functions here.
- No live paid-model benchmark run was attempted; published paper outcome and cost numbers were not used as proof of VSM ownership.
