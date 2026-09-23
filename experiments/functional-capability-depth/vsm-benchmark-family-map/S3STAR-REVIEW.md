# Follow-up semantic review: S3* direct benchmark candidate

Status: experimental, non-normative.

Issue: #392

Reviewed Profile: `vsm-harness-profile` `0.2.4`.

Reviewed TrueCall revision: `3b1d8ce253ad6d9908936f844bf5e0255785e8b9`.

`map.json` remains the machine-readable source of truth. This note records the function-first argument for adding `truecall-runtime-verification` as a `direct` S3* benchmark family at a composed system boundary.

## Decision

`TrueCall silent-failure runtime verification` is reviewed as:

```text
function: S3*
fit: direct
boundary: composed tool-using agent + TrueCall audit path
canonical harness attribution: observation-specific; not native by adapter association
```

`AuditBench` remains `proxy`.

## Why TrueCall crosses the direct S3* threshold

The Profile requires more than a component named verifier or reviewer. A positive S3* mapping needs an operational claim, an ordinary reporting path, materially different access to operational reality, an audit finding, and a path by which that finding changes subsequent control.

At the pinned TrueCall revision the live τ²-bench integration instantiates that structure directly:

```text
ordinary claim
  tool returns a success-shaped response
        ↓
complementary access
  post-condition inspects the resulting environment/database state
        ↓
audit finding
  expected state differs from actual state
        ↓
control feedback
  false success is replaced by a structured in-flight correction/error
        ↓
subsequent operation
  the agent can retry; the same post-condition is applied again
```

The complementary access is not a second reading of the tool's response. The τ² seam snapshots the environment state before/after the tool call and verifies the actual state transition. Injected silent failures deliberately preserve the success-shaped ordinary report while undoing the state mutation, so detection depends on the alternative reality-access path.

The first-party core also exposes `verifyWithRetry`: each failed post-condition becomes a correction signal passed into the next attempt, and the post-condition is re-run after that attempt. This closes audit finding → corrective operation → renewed audit rather than stopping at offline scoring.

## Why inline placement does not collapse it into ordinary QA

The Profile says a routine checker or mandatory QA stage in the same operational path is not automatically S3*. The decisive distinction here is the evidence path, not process placement.

TrueCall qualifies at the composed boundary because:

- the ordinary claim is the tool result;
- the audit does not trust that result;
- the audit reads materially different state evidence;
- a discrepancy can block the ordinary success claim;
- the discrepancy is returned to subsequent control.

A wrapper that merely schema-checks the returned payload would not satisfy this argument.

## Published benchmark evidence

The pinned repository publishes a live τ²-bench retail integration using Gemini 2.5 Flash with injected write-tool faults.

Three paired run groups are reported:

| Run | fault p | seed | tasks × trials | baseline reward | TrueCall reward |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 0.3 | 12345 | 10 × 2 | 0.375 | 0.353 |
| 2 | 0.4 | 777 | 16 × 2 | 0.321 | 0.467 |
| 3 | 0.4 | 2024 | 20 × 2 | 0.389 | 0.333 |

The publisher reports that all injected silent failures in those runs were detected and that no false positives were observed. End-task reward recovery did not replicate consistently across the three runs; the reported mean moved only from `0.362` to `0.384` and is explicitly described as within run-to-run noise.

Trajectory analysis separates detection from corrective uptake:

- soft correction wording: retry the failed tool in 8% of 25 corrections;
- imperative wording: retry in 64% of 11 corrections.

This distinction matters for VSM interpretation. The direct S3* claim is about complementary audit capability and closed feedback availability, not a claim that the downstream S1 always recovers successfully.

## Boundary provenance

The benchmarked system is not canonical Codex or canonical Claude Code merely because TrueCall ships adapters for those harnesses.

For this review the direct boundary is:

```text
operational agent / tool loop
        +
TrueCall post-condition audit layer
        +
correction return path
```

Therefore:

- a TrueCall-wrapped Codex run is a composed system unless a separate assessment declares that composition as the system-in-focus;
- the external layer must not be credited to `codex` canonical S3* ownership;
- likewise, Claude Code adapter support does not create a canonical Claude Code S3* result.

## Existing canonical S3* evidence remains separate

Current canonical assessments already establish first-party S3* paths for systems including:

- `omnigent` — `A`;
- `thclaws` — `A`;
- `codex` — `C`;
- `swe-agent` — `C`;
- `reigen` — `C`.

That repository evidence answers whether the system implements complementary audit. It does not mean TrueCall's benchmark exercised those native paths.

A particularly useful native proxy exists in SWE-agent: its published SWE-bench Lite configuration uses first-party `RetryAgent` plus a distinct chooser/reviewer over multiple attempts. That is real benchmarked native S3* mechanism evidence, but SWE-bench scores end-to-end software-task success and does not directly target complementary audit discrepancy/feedback. It therefore remains proxy evidence for S3* rather than a direct S3* observation.

## AuditBench remains proxy

AuditBench gives an investigator alternative access to hidden target-model behaviour, but the target is an external benchmark object and findings are not required to return into current control of the same operating organization.

It remains valuable audit-capability evidence without crossing the same-system closure threshold.

## Resulting coverage statement

After this follow-up review:

```text
reviewed direct S3* benchmark families: 1
published direct S3* observations at composed boundary: yes
canonical native/adapter-preserved direct-S3* observations: 0
```

The gap has therefore narrowed from “no direct benchmark family” to “direct family exists, but canonical harness linkage is still missing.”

## Primary sources

- Profile S3* semantics: https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md
- TrueCall repository at reviewed revision: https://github.com/abhid1234/truecall/tree/3b1d8ce253ad6d9908936f844bf5e0255785e8b9
- Core verifier: https://github.com/abhid1234/truecall/blob/3b1d8ce253ad6d9908936f844bf5e0255785e8b9/packages/core/src/verify.ts
- Retry closure: https://github.com/abhid1234/truecall/blob/3b1d8ce253ad6d9908936f844bf5e0255785e8b9/packages/core/src/retry.ts
- τ² integration seam: https://github.com/abhid1234/truecall/blob/3b1d8ce253ad6d9908936f844bf5e0255785e8b9/bench/tau2/seam.py
- Published live results: https://github.com/abhid1234/truecall/blob/3b1d8ce253ad6d9908936f844bf5e0255785e8b9/bench/tau2/RESULTS.md
- SWE-agent native retry/chooser benchmark config: https://github.com/SWE-agent/SWE-agent/blob/3ea751c087f32b16e039a2233dd6eefecef325d5/config/benchmarks/250212_sweagent_heavy_sbl.yaml
