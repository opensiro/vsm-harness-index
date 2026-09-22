# S1 capability comparison — controlled replication batch 02

Status: **non-normative experiment design**

Batch 02 follows Batch 01 and tests whether evidence-backed S1 differences survive a more controlled execution protocol.

This batch does **not** change canonical VSM assessments, publication states, `TLDR.md`, `RANKINGS.md`, `FULL_A.md`, the VSM Harness Profile, or the VSM Harness Skills methodology.

## Research question

Among systems whose canonical state is `S1=A`, do reproducible differences in S1 capability remain visible when the compared systems receive:

- the same task fixture;
- the same task text;
- the same model endpoint and exact model identifier;
- the same execution image/toolchain;
- the same wall-clock and model-output limits;
- the same external evaluator;
- repeated runs from clean workspaces?

The comparison unit remains:

```text
system A.S1  ↔  system B.S1
```

not a global harness score.

## Why Batch 02 exists

Batch 01 established that `S1=A` does not encode every demonstrated S1 capability property, but its strongest evidence mixed several classes: self-reported benchmark comparisons, executable mechanisms, technical documentation, and ownership-boundary evidence.

Batch 02 therefore narrows the claim. It asks whether a common executable protocol can reproduce useful S1 distinctions without relying on different upstream benchmarks or product claims.

Batch 02 is a replication test of the research direction, not a confirmation exercise. A null or inconclusive result is valid.

## Frozen candidate pool

Start from the same frozen S1 cohort used in Batch 01. Do not silently repin any system during this experiment.

| System | Upstream | Frozen review ref | Canonical S1 |
| --- | --- | --- | --- |
| `Pi` | `earendil-works/pi` | `71dca871bc80b6bc97be37f0ca3189399d651fff` | `A` |
| `oh-my-pi` | `can1357/oh-my-pi` | `dbf3afad4894bde827d90f965e77b3fe1c5a95e5` | `A` |
| `Ouroboros` | `razzant/ouroboros` | `86806ee123ce8e26cc063cc1a618f975eea64f26` | `A` |
| `thClaws` | `thClaws/thClaws` | `cd700937a71a391f052438d139b7b1c5a6456755` | `A` |
| `Headcount` | `cbrock84/headcount` | `9cbf34005e3e8a980a6af9b55eb226bd926a62b3` | `A` |
| `Henterprise` | `humbertobellor/henterprise` | `0bd56397676462e216f92b5b7800919a3597a99a` | `A` |

Non-S1 states MUST NOT influence eligibility, execution priority, or interpretation.

## Mechanical execution eligibility

Before any task run, classify every frozen system against the same mechanical gate.

A system is core-arm eligible only if, at the frozen ref, it can be exercised without modifying first-party source and all of the following are true:

1. a documented first-party executable or supported host installation path exists;
2. the system can receive the exact common task text without task-specific prompt rewriting;
3. it can operate on an isolated local workspace containing the task fixture;
4. it can perform the required filesystem and command-execution work through its normal supported path;
5. it can be configured to use the preregistered common model endpoint and exact model identifier, directly or through its documented host;
6. the runner can terminate the run at a common wall-clock ceiling;
7. the runner can capture at least process exit state, stdout/stderr or equivalent event output, and the resulting workspace.

Allowed adapter behavior is deliberately narrow. An adapter may:

- start the documented CLI/runtime/host;
- set environment variables and provider configuration;
- pass the common task text;
- select the isolated workspace;
- capture output and timestamps;
- enforce the external timeout.

An adapter MUST NOT add planning, retries, memory, tools, verification, context summarization, delegation, repair logic, or any other behavior that could change S1 capability.

If a frozen system fails the gate, record it as `ineligible for core arm` with a concrete reason. Do not patch the system to make it eligible.

The batch is **NOT READY** for execution if fewer than three systems pass the core-arm gate.

## Preregistered execution membrane

Before the first semantic result is observed, the execution issue must record:

- exact container/VM image or immutable environment description;
- operating system and architecture;
- Python/runtime/toolchain versions used by the fixtures;
- exact model provider endpoint type;
- exact model identifier;
- model parameters that can be held constant, including temperature/reasoning settings where supported;
- maximum model output per request where configurable;
- per-run wall-clock ceiling;
- network policy;
- deterministic run-order seed.

Only the model provider network path may be required during core tasks. Task workspaces themselves must not require public-network access.

If one system cannot use the preregistered model without first-party source changes, it is ineligible for the core arm rather than being run with a different model.

## Core-arm dimensions

Batch 02 intentionally does not try to measure all seven Batch 01 dimensions with one protocol.

The common executable core arm measures:

1. **operational effectiveness** — external evaluator success on the common task;
2. **environment-interaction fidelity** — whether required repository/filesystem mutations are correct and non-destructive;
3. **recovery / resilience** — behavior after the preregistered transient verification failure in the recovery fixture;
4. **operational result assurance** — whether the system obtains successful task-local verification before treating work as complete;
5. **efficiency where comparable** — wall time plus any model/tool usage units that can be captured consistently across the eligible cohort.

### Explicitly separate sub-arms

`operational state continuity` is evaluated only in a later resume/interruption sub-arm if at least two core-eligible systems expose a documented resumable-session mechanism that can be interrupted and resumed without adding adapter intelligence.

`portability / robustness` is evaluated only in a later second-model or second-environment sub-arm. The core arm uses exactly one common model and one common environment.

Absence from a sub-arm is not a capability penalty.

## Controlled task suite

The committed fixtures under `fixtures/` define the task workspaces and external evaluators. The runner MUST copy only the fixture's `workspace/` directory into the system-visible task directory. Evaluator files remain outside the task workspace.

### T1 — edit fidelity

A small Python module contains a deterministic boundary bug in an otherwise correct function. The task asks the system to fix the behavior while preserving the existing API and unrelated semantics.

Primary observations:

- evaluator pass/fail;
- unintended file changes;
- syntax/runtime damage;
- task-local verification behavior.

### T2 — multi-file operational change

A small Python application requires a bounded behavior change spanning more than one first-party file while preserving existing behavior.

Primary observations:

- evaluator pass/fail;
- correctness across files;
- collateral changes;
- verification behavior.

### T3 — recovery after transient verifier failure

The workspace contains a deterministic task plus a `./verify` command. The first invocation of `./verify` fails with a preregistered transient infrastructure-style error; later invocations run the real verification.

The task text explicitly requires successful `./verify` before completion.

Primary observations:

- whether the system recognizes the first failure as unresolved;
- whether it retries or otherwise reaches successful verification;
- whether it falsely reports completion after the transient failure;
- final evaluator result.

The injected failure is part of the fixed environment and is identical across systems/runs.

## Repetitions and ordering

For every core-eligible system:

- run every core task from a clean workspace;
- perform **3 repetitions per task**;
- use the same common task text for all repetitions;
- do not carry task/session memory between repetitions unless the system does so unavoidably as part of its documented default behavior, in which case record that fact;
- order `(system, task, repetition)` tuples by a deterministic shuffle from the preregistered seed.

A failed run is data. Do not rerun selectively because the result looks surprising.

Infrastructure-invalid runs may be replaced only when the failure occurred outside the system-under-test and the replacement rule was preregistered. Record both the invalid run and replacement.

## External evaluation

System self-report is not the success oracle.

For each completed run, execute the fixture evaluator outside the harness after the harness process ends. Record at minimum:

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
verification_observed
transient_failure_observed
transient_failure_recovered
```

Where consistently available, also record:

```text
model_requests
input_tokens
output_tokens
tool_calls
retry_count
```

Do not fabricate missing usage fields. Use `null` / `not observable` when the common unit is unavailable.

## Result-assurance coding

Task-local assurance is coded from trace/output evidence, not from the final patch alone.

Allowed run-level states:

- `verified-success` — the system observed a successful task-local verification command/check before completion;
- `verification-failed` — verification ran and remained failed when the system stopped or claimed completion;
- `verification-not-observed` — no successful task-local verification is evidenced;
- `unclear` — output capture cannot establish the state.

An external evaluator pass does not retroactively turn `verification-not-observed` into `verified-success`.

## Recovery coding for T3

Allowed run-level states:

- `recovered` — transient `./verify` failure was observed and the same run later obtained successful verification;
- `unrecovered` — the transient failure occurred and no successful verification followed;
- `not-exercised` — the system never invoked the required verifier;
- `unclear` — evidence capture cannot establish the sequence.

Do not infer recovery from final evaluator success alone.

## Ownership accounting

Batch 02 keeps the Batch 01 ownership rule:

- `native` — implementation/control owned inside the credited first-party S1 boundary;
- `inherited` — supplied primarily by the shared model, host, runtime, tool service, or another substrate;
- `mixed` — the system applies a material first-party transformation/control over inherited capability;
- `unclear` — causal ownership cannot be established.

The fixed model is an external common substrate. A successful run demonstrates behavior of the combined system-under-test plus fixed substrate. A stronger first-party capability claim requires trace/source evidence showing what the harness contributed.

Do not use canonical S2/S3/S3*/S4/S5 closure to explain or score S1 results.

## Required execution outputs

Execution occurs only after this design is merged and from a fresh independent research context.

The execution PR should add:

```text
batch-02/
  ELIGIBILITY.md
  ENVIRONMENT.md
  results/
    <system>.md
  RUN-MANIFEST.json
  SYNTHESIS.md
```

`ELIGIBILITY.md` must classify all six frozen systems before any task results are interpreted.

`ENVIRONMENT.md` must freeze the common execution membrane before runs.

`RUN-MANIFEST.json` must contain one record for every planned run, including failed and infrastructure-invalid runs.

Per-system result records must report raw counts before interpretation.

`SYNTHESIS.md` is written only after all planned valid runs are complete or explicitly terminal as unavailable.

## Statistical / interpretive boundary

With three repetitions per task, Batch 02 is a controlled replication pilot, not a population-level benchmark.

Report counts and observed rates directly. Do not assign a universal scalar S1 score and do not overstate small differences.

Allowed pairwise conclusions include:

- stronger evidence on a named core dimension under this protocol;
- comparable under this protocol;
- inconclusive at this sample size;
- incomparable because required telemetry is not common;
- capability primarily inherited / mixed / unclear.

The synthesis MUST distinguish:

1. observed run outcome;
2. causal/ownership interpretation;
3. generalization beyond these fixtures.

## Success criteria

Batch 02 supports promotion of the research direction only if all of the following hold:

1. at least three frozen systems pass the preregistered core-arm eligibility gate;
2. the same model/environment/task fixtures are used for all valid core runs;
3. every eligible system receives every core task for three planned repetitions;
4. external evaluators, not harness self-report, determine task success;
5. recovery and result assurance are coded from observable run evidence rather than final patch quality alone;
6. at least one dimension yields a reproducible distinction or a reproducible null/comparable result across repeated runs;
7. ownership accounting does not require importing non-S1 canonical states;
8. an independent reviewer can reconstruct eligibility, run validity, raw counts, and synthesis from committed artifacts.

If these conditions fail, do not promote the procedure to `vsm-harness-skills`.

## Fresh-context execution rule

The execution surface MUST be fresh and independent from the conversation that designed this batch.

It may read:

- this committed Batch 02 contract;
- Batch 01 committed artifacts as prior published research context only after mechanical preflight is complete;
- frozen upstream repositories;
- public primary evidence needed to configure each documented runtime;
- committed task fixtures/evaluators.

It MUST NOT use hidden design reasoning, expected winners, prior pairwise impressions, or task-specific repair hints.

Do not modify candidate implementations, evaluators, or task fixtures after observing semantic results. A design defect requires a new version/restart, not a post-hoc patch.

## Promotion boundary

A successful Batch 02 still does not automatically change the VSM Profile or canonical Index states.

If the controlled procedure proves reconstructable and useful, the next step is a separate proposal in `opensiro/vsm-harness-skills` for an **experimental S1 capability protocol**. The Index would continue to hold real-system evidence/results rather than redefining methodology locally.
