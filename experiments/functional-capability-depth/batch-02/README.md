# S1 capability comparison — controlled replication batch 02

Status: **non-normative experiment design**

Batch 02 follows Batch 01 and tests whether evidence-backed S1 differences survive a common executable protocol. It does **not** change canonical assessments, VSM publication states, `TLDR.md`, `RANKINGS.md`, `FULL_A.md`, the VSM Harness Profile, or the VSM Harness Skills methodology.

## Research question

Among systems whose canonical state is `S1=A`, do reproducible differences in S1 capability remain visible when eligible systems receive the same:

- task fixture and task text;
- model endpoint and exact model identifier;
- execution image/toolchain;
- wall-clock/model-output limits;
- external evaluator;
- clean-workspace repetition protocol?

The unit remains `system A.S1 ↔ system B.S1`, never a global harness score.

## Why Batch 02 exists

Batch 01 showed that `S1=A` does not encode every demonstrated S1 capability property, but its strongest evidence mixed self-reported benchmarks, public artifacts, executable mechanisms, documentation, and ownership-boundary evidence.

Batch 02 narrows the claim: can a common execution membrane reproduce useful S1 distinctions without depending on different upstream benchmarks or product claims?

A null or inconclusive result is valid. This is replication, not confirmation.

## Frozen candidate pool

Use the same frozen S1 cohort as Batch 01. Do not silently repin.

| System | Upstream | Frozen review ref | Canonical S1 |
| --- | --- | --- | --- |
| `Pi` | `earendil-works/pi` | `71dca871bc80b6bc97be37f0ca3189399d651fff` | `A` |
| `oh-my-pi` | `can1357/oh-my-pi` | `dbf3afad4894bde827d90f965e77b3fe1c5a95e5` | `A` |
| `Ouroboros` | `razzant/ouroboros` | `86806ee123ce8e26cc063cc1a618f975eea64f26` | `A` |
| `thClaws` | `thClaws/thClaws` | `cd700937a71a391f052438d139b7b1c5a6456755` | `A` |
| `Headcount` | `cbrock84/headcount` | `9cbf34005e3e8a980a6af9b55eb226bd926a62b3` | `A` |
| `Henterprise` | `humbertobellor/henterprise` | `0bd56397676462e216f92b5b7800919a3597a99a` | `A` |

Non-S1 states MUST NOT affect eligibility, execution priority, or interpretation.

## Mechanical core-arm eligibility

Before observing any task result, classify all six frozen systems against the same gate.

A system is core-arm eligible only if, without modifying first-party source:

1. a documented first-party executable or supported host-installation path exists;
2. it can receive the exact common task text without task-specific prompt rewriting;
3. it can operate on an isolated local copy of the fixture workspace;
4. it can perform filesystem mutation and command execution through its normal supported path;
5. it can use the preregistered common model endpoint and exact model identifier, directly or through its documented host;
6. an external runner can impose the same wall-clock ceiling;
7. the runner can capture process/terminal state or equivalent events plus the resulting workspace.

Allowed adapter behavior is limited to launching the documented runtime/host, setting provider/environment configuration, passing the task text, selecting the workspace, capturing output/timestamps, and enforcing timeout.

Adapters MUST NOT add planning, retries, memory, tools, verification, summarization, delegation, repair logic, or any other S1 behavior.

Failures of this gate are recorded as `ineligible for core arm` with a concrete reason. Do not patch a system to make it eligible.

The batch is **NOT READY** if fewer than three systems pass.

## Preregistered execution membrane

Before the first semantic run, commit `ENVIRONMENT.md` containing:

- immutable container/VM image or equivalent environment digest;
- OS and architecture;
- fixture runtime/toolchain versions;
- provider endpoint type and exact model identifier;
- held-constant model parameters where supported;
- model-output limit where configurable;
- per-run wall-clock ceiling;
- network policy;
- deterministic run-order seed.

Core task workspaces require no public network. The model-provider path may remain available.

A system that cannot use the preregistered model without source modification is ineligible rather than run with a different model.

## Dimensions measured in the common core arm

1. **operational effectiveness** — external evaluator success;
2. **environment-interaction fidelity** — correct, non-destructive workspace mutation;
3. **recovery / resilience** — response to the fixed transient verifier failure in T3;
4. **operational result assurance** — whether successful task-local verification is observed before completion;
5. **efficiency where comparable** — wall time and only those model/tool usage units available in a common form.

Two Batch 01 dimensions are deliberately separate:

- **operational state continuity**: later interruption/resume sub-arm only if at least two core-eligible systems expose a documented resumable-session path without adapter intelligence;
- **portability / robustness**: later second-model/environment sub-arm; the core arm uses one model and one environment.

Absence from a sub-arm is not a capability penalty.

## Frozen task suite

Fixtures live under `fixtures/`. The runner copies only each fixture's `workspace/` directory into the system-visible task directory. `task.md` supplies the exact task text. `evaluator.py` remains outside the system-visible workspace and is run only after the harness exits.

### T1 — edit fidelity

A deterministic boundary bug in a small Python function. The required change preserves API and unrelated behavior.

Observe evaluator outcome, collateral file changes, runtime/syntax damage, and visible verification behavior.

### T2 — multi-file operational change

A bounded retry-policy change spans two application files while preserving the existing return contract.

Observe evaluator outcome, cross-file correctness, collateral changes, and verification behavior.

### T3 — recovery after transient verification failure

A deterministic text-normalization task includes `python verify.py`. Its **first invocation always exits 75** with a fixed temporary-verifier error and records that the transient failure occurred. Later invocations execute the real verification.

The exact task text requires successful `python verify.py` before completion.

Observe whether the system:

- recognizes the first failure as unresolved;
- retries or otherwise reaches successful verification;
- falsely treats the transient failure as completion;
- ultimately passes the external evaluator.

The injected failure is identical across systems and repetitions.

## Repetitions and ordering

For every core-eligible system:

- run all three core tasks from clean workspace copies;
- perform **3 repetitions per task**;
- use identical task text across systems/repetitions;
- do not carry session/task memory between repetitions unless unavoidable default behavior is documented and recorded;
- deterministically shuffle `(system, task, repetition)` tuples using the preregistered seed.

A failed run is data. Do not selectively rerun surprising results.

An infrastructure-invalid run may be replaced only under a preregistered rule when failure occurred outside the system-under-test. Preserve both the invalid run and replacement in the manifest.

## External evaluation and run manifest

Harness self-report is not the success oracle. After each harness exits, run the fixture evaluator outside the harness.

Every planned run must appear in `RUN-MANIFEST.json` with at least:

```text
system
frozen_ref
adapter_version_or_digest
task
repetition
model_identifier
environment_digest
start_time
end_time
exit_state
evaluator_pass
changed_paths
verification_state
transient_failure_observed
recovery_state
```

Where consistently observable, also record:

```text
model_requests
input_tokens
output_tokens
tool_calls
retry_count
```

Missing telemetry remains `null` / `not observable`; do not infer it.

## Result-assurance coding

Code task-local assurance from captured run evidence, not final patch quality:

- `verified-success` — successful task-local verification is observed before completion;
- `verification-failed` — verification remained failed when the run stopped/claimed completion;
- `verification-not-observed` — no successful task-local verification is evidenced;
- `unclear` — capture cannot establish the state.

External evaluator success does not retroactively convert `verification-not-observed` to `verified-success`.

## T3 recovery coding

- `recovered` — the transient `python verify.py` failure is observed and the same run later obtains successful verification;
- `unrecovered` — transient failure occurred and no successful verification followed;
- `not-exercised` — the system never invoked the required verifier;
- `unclear` — capture cannot establish the sequence.

Do not infer recovery from final patch success alone.

## Ownership accounting

Keep the Batch 01 ownership labels:

- `native` — owned inside the credited first-party S1 boundary;
- `inherited` — supplied primarily by shared model/host/runtime/tool substrate;
- `mixed` — material first-party control/transformation over inherited capability;
- `unclear` — causal ownership unsupported.

The fixed model is a shared external substrate. A successful run establishes behavior of system-under-test + fixed substrate. A stronger first-party claim additionally requires source/trace evidence showing the harness contribution.

Do not import S2/S3/S3*/S4/S5 closure into S1 interpretation.

## Required execution artifacts

Execution occurs only after this design is merged and from a fresh independent context.

Add, in order:

```text
batch-02/
  ELIGIBILITY.md
  ENVIRONMENT.md
  results/
    <system>.md
  RUN-MANIFEST.json
  SYNTHESIS.md
```

`ELIGIBILITY.md` classifies all six systems before task results are interpreted.

`ENVIRONMENT.md` freezes the common membrane before runs.

Per-system records report raw counts before interpretation.

`SYNTHESIS.md` is written only after all planned valid runs are complete or terminally unavailable.

## Interpretation boundary

Three repetitions per task make this a controlled replication pilot, not a population benchmark.

Report counts and observed rates directly. No universal scalar S1 score is allowed.

Allowed pairwise conclusions:

- stronger evidence on a named core dimension under this protocol;
- comparable under this protocol;
- inconclusive at this sample size;
- incomparable because telemetry is not common;
- capability primarily inherited / mixed / unclear.

Every synthesis statement must separate:

1. observed run outcome;
2. causal/ownership interpretation;
3. generalization beyond these fixtures.

## Success criteria

Batch 02 supports methodological promotion only if:

1. at least three frozen systems pass the preregistered core eligibility gate;
2. all valid core runs share the same model/environment/task fixtures;
3. every eligible system receives every task for three planned repetitions;
4. external evaluators determine task success;
5. recovery and result assurance are coded from observable trace/output evidence;
6. at least one dimension yields a reproducible distinction **or reproducible null/comparable result** across repetitions;
7. ownership accounting does not require non-S1 canonical states;
8. an independent reviewer can reconstruct eligibility, validity, raw counts, and synthesis from committed artifacts.

If these conditions fail, do not promote the procedure to `vsm-harness-skills`.

## Fresh-context rule

Execution MUST occur in a fresh independent research context.

The execution surface may read this committed contract, the frozen upstream repositories, public primary evidence needed to configure their documented runtimes, and the committed fixtures/evaluators. Batch 01 is prior published context, but its pairwise conclusions must not be used as expected outcomes or run-selection priors.

Do not use hidden design reasoning, expected winners, task-specific repair hints, or post-hoc criteria.

Do not modify candidate implementations, task text, evaluator logic, or fixture starting state after semantic results are observed. A design defect requires a new version/restart.

## Promotion boundary

Even a successful Batch 02 does not modify the VSM Profile or canonical Index states.

If the controlled procedure proves useful and reconstructable, open a separate proposal in `opensiro/vsm-harness-skills` for an **experimental S1 capability protocol**. The Index remains the evidence/results corpus rather than a parallel methodology owner.
