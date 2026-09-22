# S1 capability replication — Batch 02 design

Status: **non-normative replication design**

Issue: #351

This batch follows the Batch 01 result merged by `172edc9d8c44aaffe282754d8dc8f765164654f0`.
It does not change canonical VSM assessments, publication states, Profile semantics, Methodology semantics,
`TLDR.md`, `RANKINGS.md`, or `FULL_A.md`.

Batch 01 showed that systems sharing canonical `S1=A` can expose materially different S1 evidence,
but the evidence classes were heterogeneous. Batch 02 therefore changes the experimental question from:

```text
can evidence-backed S1 distinctions be reconstructed?
```

to:

```text
do useful S1 distinctions survive a substantially aligned task / model / environment protocol?
```

The comparison unit remains one function across systems:

```text
system A.S1 ↔ system B.S1
```

There is no harness-wide capability score.

## Design boundary

This file is the Batch 02 contract. Semantic execution MUST NOT begin until:

1. this design is merged into `main`;
2. the mechanical fixture/adaptor work tracked by #352 is complete and merged;
3. the resulting execution-readiness manifest passes all preflight gates below;
4. a separate execution issue is opened from then-current `main`;
5. execution begins in a fresh independent research context.

Batch 02 design, fixture construction, semantic execution, and independent review are separate tasks.

## Frozen runtime cohort

Reuse the Batch 01 upstream revisions so protocol change is not confounded with upstream evolution.

| System | Repository | Frozen review ref | Canonical S1 | Batch 02 role |
| --- | --- | --- | --- | --- |
| Pi | `earendil-works/pi` | `71dca871bc80b6bc97be37f0ca3189399d651fff` | `A` | directly runnable first-party runtime |
| oh-my-pi | `can1357/oh-my-pi` | `dbf3afad4894bde827d90f965e77b3fe1c5a95e5` | `A` | directly runnable first-party runtime |
| Ouroboros | `razzant/ouroboros` | `86806ee123ce8e26cc063cc1a618f975eea64f26` | `A` | directly runnable first-party runtime |
| thClaws | `thClaws/thClaws` | `cd700937a71a391f052438d139b7b1c5a6456755` | `A` | directly runnable first-party runtime |

`Headcount` and `Henterprise` are deliberately not in the primary execution matrix. Their Batch 01 value
was largely ownership-accounting over host-supplied execution. Mixing host-specific overlays into the same
direct-runtime matrix would weaken the matched-execution claim. A later overlay replication MAY compare
host baseline ↔ overlay under the same host, but it is a separate experiment.

Non-S1 canonical states are forbidden as priors. Full-A gives no S1 capability bonus.

## Common model substrate

All four frozen runtimes expose an OpenAI-compatible model route at the reviewed revisions. Batch 02 uses
one common endpoint and one frozen OSS model checkpoint.

Primary model:

```text
Qwen/Qwen3-Coder-30B-A3B-Instruct-FP8
revision: dcaee4d4dfc5ee71ad501f01f530e5652438fde0
```

Primary server contract:

```text
OpenAI Chat Completions compatible endpoint
vLLM: 0.18.2
model revision fixed to dcaee4d4dfc5ee71ad501f01f530e5652438fde0
max model context: 32768
Qwen3-Coder tool parser enabled
frozen model-provided chat template / tool parser preferred where required
```

The model server is a common external substrate and receives no first-party capability credit.

### Normalizing gateway

#352 MUST provide a thin experiment gateway in front of the model server. For every harness request it MUST:

- force the frozen primary model identity;
- force `temperature = 0`;
- force `top_p = 1`;
- cap per-response output at `8192` tokens;
- preserve user/system messages and tool schemas except for transport-normalization needed to reach the common endpoint;
- reject unsupported provider-specific request modes rather than silently translating them into a different semantic API;
- record request/response hashes, token usage, timestamps, HTTP failures, and model-call ordinal;
- expose a deterministic one-shot HTTP 503 injection used by the recovery protocol.

Harness-native system prompts, tool schemas, loop policy, edit strategy, session machinery, and completion policy
remain part of the harness and MUST NOT be normalized away.

If any frozen runtime cannot use this common Chat Completions path without a semantic adapter that changes
its agent behavior, Batch 02 is NOT READY until the cohort is narrowed explicitly.

## Common execution environment

#352 MUST freeze an execution image / environment lock satisfying:

- Linux container or equivalent isolated workspace;
- no public internet from the harness workspace;
- model access only through the Batch 02 gateway;
- fixed CPU and memory limits for every run;
- the same installed shell, Git, Python, test tooling, and filesystem layout for every harness;
- a fresh task workspace and fresh harness session for every primary run;
- controller/evaluator files not mounted inside the harness-visible working directory;
- controller-side acceptance executed only after harness termination;
- exact image digest or equivalent content-addressed environment identity recorded in the run manifest.

Hardware differences MUST NOT be interpreted as harness capability. Wall-clock latency is supporting evidence
only unless the same server and scheduling conditions are demonstrated.

## Common task corpus

#352 MUST implement the following task families as small deterministic Coding/SWE fixtures. Exact fixture
commits/hashes and prompt text MUST be frozen before semantic execution.

### T1 — exact local mutation

A small repository requires one behavior change with an externally checked exact contract.

Purpose:

- baseline operational effectiveness;
- basic environment-interaction fidelity;
- resource-use baseline.

### T2 — multi-file consistency change

A public interface or data contract changes across multiple files. A partial edit can satisfy a visible local
check while failing the controller-side acceptance oracle.

Purpose:

- whole-task effectiveness;
- cross-file state continuity;
- result-assurance evidence without relying on the harness's own completion claim.

### T3 — seeded regression diagnosis

The repository starts with a deterministic failing test whose visible symptom is downstream from the seeded
root cause. The task asks for repair, not merely suppression of the failing assertion.

Purpose:

- diagnosis / repair effectiveness;
- tool/environment fidelity;
- retry and correction behavior.

### T4 — bounded integration change

A small local service/library contract must be implemented and exercised using only the fixture environment.
No network lookup is needed.

Purpose:

- repeated tool use;
- current-task state continuity;
- effectiveness under a slightly longer trajectory.

The task prompts MUST be identical across systems. Harness-specific invocation wrappers may inject only the
minimum provider/session configuration required to start the frozen runtime.

## Perturbation protocol

Perturbations are separate runs over frozen task fixtures. Do not mix them into the baseline result silently.

### F1 — common model-transport failure

For a precommitted task and run ordinal, the common gateway returns exactly one HTTP 503 on model-call ordinal 2,
then resumes normal service.

Measure:

- whether the harness retries / recovers / terminalizes;
- whether useful work survives the failure;
- additional model calls / tokens / elapsed work caused by recovery.

This is evidence for `recovery / resilience`, not S3 current control.

### F2 — forced process interruption / resume

For runtimes with a first-party resumable session path, the controller terminates the harness process after the
first observed workspace mutation, then restarts through the frozen runtime's native resume surface.

Measure:

- whether the same operational trajectory can continue;
- retained state/artifacts;
- duplicated or lost work;
- final task acceptance.

If a runtime lacks an exposed first-party resumable path at the frozen ref, record `not tested`; do not emulate
resume by replaying the entire transcript externally.

## Run policy

Primary matrix:

```text
4 systems × 4 baseline tasks × 3 repetitions = 48 baseline runs
```

F1 and F2 are additional perturbation runs defined by the execution-readiness manifest.

Every repetition starts from:

- the same task fixture commit;
- a clean workspace;
- a fresh harness session unless the perturbation explicitly tests resume;
- the same gateway/model configuration;
- the same run limits.

Run order MUST be deterministic but shuffled from a seed derived from the merged design commit and frozen run
manifest. Do not choose run order after seeing outcomes.

Invalid runs may be excluded only for precommitted infrastructure failures outside the harness boundary, such as
controller crash or model server unavailability beyond the intentional F1 injection. Harness crashes, malformed
requests, timeouts, and failure to complete are results, not invalid-run excuses.

## Common run limits

#352 MUST encode the same limits for all systems:

- wall-clock timeout: 20 minutes per run;
- maximum model requests: 64;
- maximum cumulative model output: 80000 tokens;
- no human intervention after run start;
- no external web/network tools;
- no third-party skills/plugins/extensions beyond what is required to connect the common model endpoint.

A harness that reaches a limit is terminalized as such. Limits MUST NOT be raised selectively after seeing a result.

## Controller evidence schema

Every run MUST yield a machine-readable record containing at least:

```text
run_id
system
system_ref
task_id
task_fixture_hash
repetition
perturbation
execution_image_digest
model_repo
model_revision
gateway_version
start_time
end_time
terminal_state
acceptance_pass
model_request_count
input_tokens
output_tokens
tool_call_count_if_observable
tool_error_count_if_observable
retry_count_if_observable
workspace_diff_hash
controller_log_hash
harness_trace_hash_or_null
```

Missing telemetry stays missing. Do not infer unavailable counts from prose.

Raw traces/artifacts MUST be retained so an independent reviewer can reconstruct every derived observation.

## S1 dimension mapping

Batch 02 does not force all seven Batch 01 dimensions into one experiment.

| S1 dimension | Batch 02 status | Primary evidence |
| --- | --- | --- |
| operational effectiveness | primary | controller-side acceptance rate / terminal outcome |
| environment-interaction fidelity | primary where observable | tool errors, failed actions, incorrect mutations, acceptance artifacts |
| operational state continuity | primary in F2 / trajectory evidence | interruption/resume outcome, retained work |
| recovery / resilience | primary in F1 plus task recovery traces | injected 503 recovery, retries, retained work |
| operational result assurance | secondary | relationship between harness completion behavior and external acceptance; first-party verification evidence where traceable |
| efficiency | primary conditional on comparable work | model calls, tokens, retries; wall time is supporting only |
| portability / robustness | **not tested by the primary model matrix** | requires a separately frozen second substrate; no portability claim from Batch 02 primary results |

`not tested` is not a low score.

## Ownership accounting

Every positive capability observation MUST still be labeled:

- `native`;
- `inherited`;
- `mixed`;
- `unclear`.

The common model, vLLM server, gateway, Linux container, shell, Git, interpreter, and controller-side evaluator are
external substrates. Their capability is not credited as first-party S1 capability merely because a harness uses them.

## Pairwise interpretation

Pairwise analysis is allowed only after all admitted systems have completed the frozen matrix or have a terminal
precommitted reason they could not.

Allowed dimension-level outcomes:

- stronger evidence for A;
- stronger evidence for B;
- comparable under available evidence;
- incomparable;
- insufficient evidence;
- capability primarily inherited rather than first-party;
- not tested.

Do not collapse dimensions into a weighted total.

A difference in acceptance rate, recovery rate, or resource use MAY support a pairwise relation only when the
underlying runs share the frozen model, task, environment, and limits and the difference is not explained by a
recorded substrate failure.

No significance language should be used unless the sample size and statistical test were committed before analysis.
With three repetitions, report the observed counts and dispersion directly rather than implying population-level
certainty.

## Protocol success vs hypothesis result

These are separate.

### Protocol success

The protocol succeeds if:

1. at least three of the four frozen runtimes complete the common-provider preflight;
2. the same frozen model endpoint is used for every admitted system;
3. all baseline task fixtures and external acceptance oracles are frozen before execution;
4. raw run artifacts allow independent reconstruction;
5. at least operational effectiveness plus one of fidelity/recovery/continuity/efficiency is aligned across at least one pair;
6. unsupported dimensions remain honestly `not tested`, `incomparable`, or `insufficient evidence`.

A protocol can succeed even if no capability distinction survives.

### Hypothesis support

Batch 02 supports the capability-depth hypothesis only if the aligned evidence demonstrates at least one reproducible
S1 distinction between systems sharing `S1=A` that cannot be reduced to model choice, task mismatch, environment
mismatch, non-S1 VSM coverage, or an inherited external substrate.

A null result, reversal, or disappearance of a Batch 01 distinction is valid research output and MUST NOT trigger
post-hoc fixture, model, cohort, or metric changes.

## NOT READY / STOP conditions

Do not open semantic execution if any of these hold:

- the frozen Batch 01 merge is absent from current `main` history;
- the task corpus or acceptance oracle is mutable / not content-addressed;
- the common model revision is not pinned;
- the execution environment is not content-addressed;
- fewer than three cohort systems can reach the same gateway/model API without semantic provider translation;
- harness-specific prompts differ beyond mechanically required invocation wrappers;
- evaluator artifacts are visible inside the task workspace;
- run limits or invalid-run rules are not frozen;
- #352 has not completed the execution-readiness manifest.

Return `NOT READY` rather than weakening the controls after seeing compatibility problems.

## Fresh independent execution

The later Batch 02 execution issue MUST require a fresh research context.

That context may use:

- this committed design;
- the merged #352 fixtures/adapters/manifest;
- frozen upstream repositories;
- raw execution artifacts produced by the protocol.

It MUST NOT import expected winners, prior pairwise semantic conclusions, or coordinator hints from Batch 01.
Batch 01 is prior motivation and protocol history, not a source of Batch 02 outcome labels.

## Independent review

After execution, a separate reviewer MUST reconstruct:

- the execution boundary;
- admitted cohort;
- model/environment identity;
- run completeness;
- invalid-run handling;
- per-dimension evidence;
- pairwise claims;
- ownership labels;
- all `incomparable` / `insufficient evidence` / `not tested` outcomes.

Execution and review are separate surfaces.

## Promotion boundary

Batch 02 remains Index-local experimental research.

Do not create an S1 capability protocol in `opensiro/vsm-harness-skills` merely because Batch 01 produced useful
observations. A later Skills proposal requires, at minimum:

```text
Batch 01 exploratory evidence
→ Batch 02 controlled replication
→ independent Batch 02 review
→ evidence that the comparison procedure is stable enough to reuse
```

Any Skills proposal must remain S1-specific. S2/S3/S3*/S4/S5 require their own function-specific experiments and
must not inherit these S1 dimensions mechanically.
