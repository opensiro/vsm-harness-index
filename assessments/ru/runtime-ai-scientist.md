---
harness_id: runtime-ai-scientist
project_name: Runtime AI Scientist
repository: https://github.com/systemind-team/Runtime-AI-Scientist
review_ref: 16dc9399b21ebe4deffac25e40129341cc1ecef1
reviewed_at: 2026-11-17
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: C
autonomy_s3_star: ?
autonomy_s4: —
autonomy_s5: —
---

# Runtime AI Scientist

## Review boundary

- System in focus: The published RAC runtime/integration layer and its first-party built-in bridges to supported ARK, Agent Laboratory and EvoScientist scientific-agent hosts at a pinned git revision.
- Purpose and identity: Run comparable science-agent episodes with runtime capability selection, scoped work contracts, usage accounting, result checks and benchmark attribution.
- Environment: Research question and workspace, external packaged host agent capabilities, API/LLM providers, artifacts, unresolved research issues, usage/lifecycle budgets and benchmark scorer.
- Standard-distribution boundary: The first-party `rac_ai_scientist` runner, SharedPolicy, host adapters, checkpoint schema, artifact transactions, R1–R3 SharedNet integration and native host launch wiring; externally installed host agent implementations/models are indispensable supported dependencies, not imported first-party policy owners.
- Credited operating / distribution surfaces: N0 native lifecycle adapter as comparison; R1–R3 shared episode runner and the shipped ARK/Agent Laboratory/EvoScientist bridges invoking actual model-backed host scientific agents. Selection and R3 checks are owned by shipped Python policy code, not by an LLM coordinator.
- Adjacent first-party surfaces excluded from ownership: Benchmark/Judge scoring after termination, isolated ResearchClawBench scorer, README graphs/paper claims, CI, experiments, tutorials and contributor governance.
- First-party operating / deployment modes considered: Host-integrated R1 messaging with fixed successor; R2 issue/tag-driven runtime selection; R3 optional scoped work contracts and advisory artifact verification; N0 externally owned host scheduling is not used to credit RAC with higher-level organization.
- Recursion level: One RAC-managed research episode with multiple underlying host agent role executions; external model providers and separate external host organizations are dependencies.
- Reviewed revision: `16dc9399b21ebe4deffac25e40129341cc1ecef1` (source main snapshot).
- Observation date: 2026-11-17.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

`EpisodeRunner` requests a live `HostBridge.checkpoint()` at every hop, selects current host capability via `SharedPolicy.decide`, executes `HostBridge.invoke`, records decision/result/usage in an append-only ledger and passes evaluations back through the bridge. Bridge implementations call model-backed ARK, Agent Laboratory or EvoScientist host capabilities; they are real supported agent operations, but the model and host agent source are external dependencies. R1 SharedNet adds a typed messaging context; R2 _select scores issue/capability tag matches deterministically and chooses a capability; R3 supplies scoped work contracts and checks before/after artifact fingerprints. R3 verdicts are expressly **advisory**: they are handed to the next agent but do not themselves trigger rollback, stop, retry or reroute. Native N0 execution and separate post-run benchmark score are controls for research reporting and not additional agent-owned governance.

Sources: [runner.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/runner.py), [policy.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/policy.py), [bridge.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/bridge.py), [ark.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/hosts/ark.py), [agent_laboratory.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/hosts/agent_laboratory.py), [evo_scientist.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/hosts/evo_scientist.py), [sharednet.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/sharednet.py), [architecture.md](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/docs/architecture.md).

## S1 — Operations
- State: A
- Function: Execute research work with multi-step host scientific agents using models and tools, under RAC's first-party supported integration mode.
- Disturbance / variety regulated: Research requests, literature/experiment/writing outputs and unexpected host-tool results.
- Decisive decision or feedback right: A currently invoked model-backed researcher/experimenter/writer/reviewer chooses task content and tool actions.
- Decision owner: Model-backed scientific agent invoked by the shipped ARK/Agent Laboratory/EvoScientist bridges; the deterministic RAC runner selects who runs next.
- Supporting / enforcement mechanisms: HostBridge.invoke dispatch to host capability, work contracts, provider call, terminal result and artifact snapshots.
- Closure path: Agent creates/modifies research workspace artifacts or outputs; the next checkpoint sees resulting outputs and issues for follow-on work.
- Boundary reachability: Operational S1 depends on installed native host agents/models; pure offline policy tests are not themselves autonomous agents.
- Why this is / is not agent-owned: All three supported adapters implement `HostBridge.invoke` and run native agent role calls; R1–R3 EpisodeRunner dispatches those first-party supported operating modes. External host code is not credited with RAC-owned S2–S5 decisions.
- Evidence: Operational choices are made by model-backed host agents in the supported integrated mode, not solely by the deterministic role selector.
- Basis: [ark.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/hosts/ark.py), [agent_laboratory.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/hosts/agent_laboratory.py), [evo_scientist.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/hosts/evo_scientist.py), [runner.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/runner.py), [bridge.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/bridge.py)
- Confidence: source and integration/test contracts
- Caveats: medium-high


## S2 — Coordination
- State: —
- Function: No function-specific attenuation of concrete concurrent or competing S1 interference is established in RAC's controlled episode mode.
- Disturbance / variety regulated: Different research roles may communicate, hand off artifacts or receive scoped work, but no concrete competing execution collision is resolved by a first-party inter-S1 relation.
- Decisive decision or feedback right: Would require conflict/arbitration/oscillation control between distinct simultaneous or competing role units with subsequent corrective feedback.
- Decision owner: No independently identified S2-specific decision owner in the inspected R1–R3 flow.
- Supporting / enforcement mechanisms: SharedNet messages, serial turn/hop ordering, deterministic role selection and per-hop work contract.
- Closure path: RAC passes current output/context to the next selected role but does not exhibit specific inter-agent conflict adjudication in the supported source inspected.
- Why this is / is not agent-owned: Messaging, handoffs, resource caps and per-role path scopes do not alone establish S2.
- Evidence: [runner.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/runner.py), [sharednet.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/sharednet.py), [policy.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/policy.py), [bridge.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/bridge.py), [architecture.md](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/docs/architecture.md)
- Basis: bounded source absence
- Confidence: medium-high
- Caveats: If an actual first-party inter-agent interference resolver is shown at this frozen ref, request a source-pinned correction.

### Absence scope
- Surfaces inspected: EpisodeRunner sequential hops, R1 SharedNet typed requests/results, R2 deterministic role selector, R3 work contracts and transaction handling.
- Plausible first-party paths checked: Potential simultaneous conflicting edits, duplicate competing commitments, arbitration across distinct S1 agents and feedback into their subsequent behavior.
- Why no material first-party path remains: No shipped function-specific path was found beyond serial sequencing, typed communication and admission of the next capability; the required inter-S1 disturbance and its closed attenuation are not evidenced.

## S3 — Inside-and-now control
- State: C
- Function: Use a whole-current research episode checkpoint and shared resources to select the next authorized role and stop unsafe over-budget work.
- Disturbance / variety regulated: Research stages compete for limited remaining agent calls, tokens, time and permitted capabilities; current unresolved issues change priorities across roles.
- Decisive decision or feedback right: Select eligible capability, stop/escalate when no suitable role or budget remains, apply repeat/recovery decisions after errors.
- Decision owner: First-party deterministic SharedPolicy and EpisodeRunner, configured by application/researcher; no autonomous manager agent owns the shared-current decision.
- Supporting / enforcement mechanisms: Checkpoint of current artifacts/issues/remaining budget/role availability, _select tag scoring, provider budget checks, action STOP/ESCALATE/RETRY/RECOVER and ledger.
- Closure path: After each host invocation, the next bridge checkpoint updates issues/usage/artifacts; the policy chooses later role or terminates and the runner enforces the decision; error evaluation can rollback or recover according to configured rules.
- Boundary reachability: R2 algorithm chooses by issue tags and availability, *not* by model-discretionary agent selection despite colloquial README. Hard ceilings alone are not credited as S3.
- Why this is / is not agent-owned: In shipped R2/R3 mode, EpisodeRunner calls SharedPolicy.decide/_select on fresh global checkpoint and executes selected capability via HostBridge; this is more than a raw budget counter because role admission depends on whole episode issue state.
- Evidence: The runtime policy closes shared-current task-capability choice, but its tag/score logic is deterministic and config-owned, so C rather than A.
- Basis: [runner.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/runner.py), [policy.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/policy.py), [bridge.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/bridge.py), [ark.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/hosts/ark.py), [budget.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/budget.py), [test_runner.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/tests/test_runner.py), [test_policy.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/tests/test_policy.py)
- Confidence: explicit implementation, source tests
- Caveats: high for C, not A
- Whole-system current view: The per-hop checkpoint contains admitted capability cards, active unresolved research issues, artifacts, native stage and remaining lifecycle budget across the single research episode.
- Current-control decision scope: Deterministic controller chooses which role receives shared research work next, whether to escalate and when to stop/rollback, with downstream host execution honoring the selection.

## S3* — Complementary audit
- State: ?
- Function: A distinct artifact-grounded verification access path plausibly challenges agent-produced outputs, but evidence does not resolve independence and corrective return to the S3 whole-current controller.
- Disturbance / variety regulated: Agent output can claim completion when required artifacts were not actually produced, or can write outside scoped paths.
- Decisive decision or feedback right: A sufficiently independent auditing actor would need to inspect complementary reality, issue a substantive finding and feed it back into subsequent controlling decisions.
- Decision owner: SharedPolicy.verify_result performs deterministic filesystem-snapshot checks on invocation artifacts; the same RAC policy/runner owns ordinary runtime flow. Sufficiency of independent witness and corrective owner unresolved.
- Supporting / enforcement mechanisms: WorkContract required evidence, before/after workspace fingerprints, advisory SUPPORTED/REFUTED/INCONCLUSIVE verdict, SharedNet verification message and ledger.
- Closure path: R3 verification verdict is passed into the next role's context; however, documented and implemented R3 paths explicitly do not stop, retry, reroute or rollback based on verdict, leaving whether this qualifies as complementary audit to S3 unproven.
- Why this is / is not agent-owned: A fixed artifact checker can provide extra evidence distinct from model self-report, yet mere routine verification and advisory status are not automatically an independent complementary audit.
- Evidence: [policy.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/policy.py), [runner.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/runner.py), [sharednet.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/sharednet.py), [artifacts.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/artifacts.py), [architecture.md](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/docs/architecture.md)
- Basis: specific in-boundary plausible but unresolved audit path
- Confidence: medium
- Caveats: Not the separate ResearchClawBench scorer: post-episode benchmark judging is outside this operational recurrence. Follow-up should prove actual independent corrective governance or resolve to bounded absence.


## S4 — Outside-and-then intelligence
- State: —
- Function: No prospective external-environment sensing and adaptation of the future agent organization is established in this RAC research episode.
- Disturbance / variety regulated: New future scientific requirements or environmental changes could require changing role capabilities or policy.
- Decisive decision or feedback right: A mechanism would have to evaluate external future conditions, generate organizational adaptation options and return accepted ones into active role capability.
- Decision owner: No first-party future-capability adaptation owner identified; the researcher configures supported roles/budgets outside the run.
- Supporting / enforcement mechanisms: Issue-triggered current role selection, experiment objectives, work contracts and benchmark paper results.
- Closure path: Unresolved issues lead to *current* choice among already admitted role cards; there is no shipped organizational future adaptation decision and apply path.
- Why this is / is not agent-owned: Research future hypotheses and repeated experiments are S1 work content, not S4 capability planning at this recursion.
- Evidence: [policy.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/policy.py), [runner.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/runner.py), [ark.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/hosts/ark.py), [architecture.md](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/docs/architecture.md)
- Basis: bounded negative source adjudication
- Confidence: medium
- Caveats: A downstream scientist agent may study future scientific results, not the same as harness governance.

### Absence scope
- Surfaces inspected: Supported episode policy/runner/host bridges, checkpoint issue tags, work contracts, benchmark reports and setup manifests.
- Plausible first-party paths checked: External future-signal acquisition, new role/tool policy option proposals and accepted return into future episode capacity.
- Why no material first-party path remains: All inspected decisions route existing supported role cards or report completed benchmark results; no first-party outside-and-then organizational adaptation loop identified.

## S5 — Policy and identity
- State: —
- Function: No operating identity or ultimate-policy governance decision and returned higher-level authority was established inside RAC.
- Disturbance / variety regulated: Changes to episode authorization or scientific objective may require legitimate policy authority.
- Decisive decision or feedback right: A supreme-policy actor would have to decide the research-organization charter and make that decision operative to subsequent work.
- Decision owner: Researcher controls manifests/budget and choice of comparison condition; RAC itself has no evidenced S5 governance decision loop.
- Supporting / enforcement mechanisms: Static admitted capability cards, config, fixed condition N0–R3, per-hop work contract and budget guard.
- Closure path: Permission and contract bounds are preselected and enforced; work contract checks explicitly warn on out-of-scope writes but do not establish ultimate organizational-policy acceptance or a separate human-authorized return path.
- Why this is / is not agent-owned: Neither static condition choice nor capability filter is S5 by itself.
- Evidence: [policy.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/policy.py), [bridge.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/bridge.py), [runner.py](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/src/rac_ai_scientist/runner.py), [architecture.md](https://github.com/systemind-team/Runtime-AI-Scientist/blob/16dc9399b21ebe4deffac25e40129341cc1ecef1/docs/architecture.md)
- Basis: bounded negative source inspection
- Confidence: medium
- Caveats: A parent research organization may impose ethics/identity policy outside the distribution.

### Absence scope
- Surfaces inspected: Policy constructor, host manifests, eligibility cards, contract/write warnings, benchmark preparation and CLI/configured condition.
- Plausible first-party paths checked: Ultimate organizational identity decision, authorized parent approval and feedback changing subsequent runtime identity/policy.
- Why no material first-party path remains: Only externally configured execution/benchmark rules and current operational gating are shown, without a first-party ultimate-policy decision cycle.

## Recursion

The selected research host's distinct scientist roles are the operational units invoked by RAC. The RAC episode supplies a shared current coordination/control level but not evidence of independent policy and adaptation across a higher organizational recursion. Benchmark scoring and maintainer governance sit outside the live episode.

## Variety and escalation

Varying research issues and artifacts feed operational host agents; the R2 shared policy uses their changing checkpoint to select the next admitted specialist with a fixed decision rule. Budget exhaustion, missing role availability and fatal transport errors lead to stop/escalation, with ledger and optional SharedNet notes. R3 advisory checks may inform later role output but do not constitute a mandatory control override.

## Evidence gaps

- Source inspection only at frozen upstream commit; no live external host/model episodes or benchmark run, no independent semantic auditor claim.
- S3*=?: concrete R3 filesystem evidence checks are not automatically credited as independent S3*; their actual relation to a separately authoritative controller needs source-specific verification. Do not confuse ResearchClawBench post-run score with runtime complementary audit.
- S2=— is bounded to shipped sequential role-selection/SharedNet paths. If a real conflict-resolution relation across distinct agents is discovered, open a same-ref correction.
- S3=C credits current shared-control role selection and feedback, not purported discretionary LLM coordination, and S4/S5 remain unestablished at the declared operating boundary.
