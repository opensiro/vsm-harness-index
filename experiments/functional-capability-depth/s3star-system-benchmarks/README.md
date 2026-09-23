# Direct S3* benchmark coverage

Status: experimental, non-normative.

Issue: #392

Parent semantic map: `../vsm-benchmark-family-map/`

## Question

Can a reviewed direct S3* benchmark be linked to canonical Index systems without confusing an external audit wrapper with the canonical system's own complementary-audit implementation?

Current answer:

```text
reviewed direct S3* benchmark families: 1
published direct observations at a composed S3* boundary: 1 aggregate evidence record
canonical native/adapter-preserved direct-S3* observations: 0
```

The gap therefore has two layers:

```text
semantic gap: closed
  TrueCall directly exercises S3* at a composed audited-system boundary

canonical linkage gap: open
  no reviewed public direct-S3* observation yet exercises a canonical harness's own S3* path
```

## Direct family: TrueCall runtime verification

Reviewed TrueCall revision:

`3b1d8ce253ad6d9908936f844bf5e0255785e8b9`

The direct mapping is based on the actual audit path, not on verifier vocabulary:

```text
ordinary claim
  tool returns success
        ↓
complementary reality access
  deterministic post-condition inspects world/database state
        ↓
challenge
  expected state != actual state
        ↓
control feedback
  false success replaced by structured correction
        ↓
subsequent operation
  agent may retry and the effect is re-verified
```

The τ²-bench integration deliberately injects silent write-tool failures by undoing the database mutation while preserving a success-shaped tool response. Detection therefore cannot be obtained by trusting or re-parsing the ordinary report; it depends on the complementary state path.

## Why this is S3* and not generic QA

The current Profile explicitly rejects treating routine tests/checkers as S3* by name alone.

TrueCall crosses the threshold at the composed boundary because its post-condition observes materially different operational evidence from the claim being audited and the discrepancy can enter subsequent control.

A schema checker over the same returned payload would not satisfy this boundary argument.

## Published direct observation

`benchmark_observations.json` records the publisher's live τ²-bench retail experiment with Gemini 2.5 Flash.

Across three paired run groups the publisher reports:

- all injected silent failures detected;
- zero false positives in the reported runs;
- baseline mean task reward `0.362`;
- TrueCall mean task reward `0.384`;
- end-task recovery **not established**, because run-level reward deltas were inconsistent;
- retry uptake changed from `8%` (`n=25`) under soft correction wording to `64%` (`n=11`) under imperative wording.

The direct S3* result is the complementary detection/feedback path. It is **not** a claim that downstream S1 recovery is guaranteed.

## Canonical-system boundary

`canonical_observations.json` is intentionally empty.

TrueCall has adapters for Codex and Claude Code, but those adapters add an external audit layer. They do not make the wrapped product's canonical assessment own that layer.

A future observation may enter `canonical_observations.json` only when the direct benchmark actually exercises a canonical harness's first-party S3* path as either:

- `native-system`, or
- defensible `adapter-preserved` where the adapter preserves the native S3* mechanism rather than replacing it.

## Representative canonical S3* systems inspected

The first pass checks mechanism-diverse current canonical systems:

- `omnigent` — `S3*=A`, separate cross-vendor reviewer and corrective fix-task loop;
- `thclaws` — `S3*=A`, completion claim challenged through direct workspace inspection and corrective return;
- `codex` — `S3*=C`, optional Guardian AutoReview path;
- `swe-agent` — `S3*=C`, optional retry/chooser reviewer path;
- `reigen` — `S3*=C`, independent worktree verification constructor path.

No direct TrueCall-family observation currently exercises those native first-party paths.

## Native proxy: SWE-agent

SWE-agent is the strongest native benchmarked proxy found in this pass.

Its first-party SWE-bench Lite configuration explicitly runs:

- `agent.type: retry`;
- multiple operational attempts;
- a separate chooser/reviewer model (`o1` in the pinned config);
- reviewer selection among candidate patch submissions.

This is real benchmarked native S3* mechanism evidence, but SWE-bench is reviewed as a direct **S1** benchmark. Its score is end-to-end software task success, not a direct S3* discrepancy/challenge/feedback metric. The evidence is therefore preserved as `native-proxy`, not promoted into the direct registry.

## Existing proxy: AuditBench

AuditBench remains a strong S3* proxy. Its investigator can obtain alternative evidence about hidden target-model behavior, but the target is an external benchmark object and findings do not have to return into current control of the same operating organization.

## Source of truth

- `benchmark_observations.json` — direct S3* observations at non-canonical composed boundaries;
- `canonical_observations.json` — direct native/adapter-preserved canonical harness observations; currently `[]`;
- `coverage.json` — canonical linkage/proxy/boundary cases;
- `validate.py` — checks the reviewed direct family, observation separation and canonical assessment anchors.

## Non-goals

This layer does not:

- infer canonical S3* ownership from TrueCall results;
- credit an external audit plugin to Codex or Claude Code;
- treat every verifier, judge, test or retry loop as S3*;
- infer autonomy state from detection/retry/reward metrics;
- combine S3* detection with S1 recovery into one score;
- modify canonical assessments, Profile, Skills, catalog or derived rankings.
