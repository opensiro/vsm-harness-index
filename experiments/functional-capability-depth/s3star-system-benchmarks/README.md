# Direct S3* benchmark coverage

Status: experimental, non-normative.

Initial issue: #392  
Primary-baseline follow-up: #430

Parent semantic map: `../vsm-benchmark-family-map/`

## Question

Can a reviewed direct S3* benchmark be linked to canonical Index systems without confusing an external audit wrapper, a generic review label, or ordinary task self-checking with the canonical system's own complementary-audit implementation?

Current answer:

```text
reviewed direct S3* benchmark families: 1
published direct observations at a composed S3* boundary: 1 aggregate evidence record
canonical native/adapter-preserved direct-S3* observations: 0
S3* primary baseline: gap
```

The gap therefore has two layers:

```text
semantic gap: closed
  TrueCall directly exercises S3* at a composed audited-system boundary

canonical linkage gap: open
  no reviewed public direct-S3* observation yet exercises a canonical harness's own S3* path
```

## Rule — a direct S3* benchmark must preserve the complementary audit path

A benchmark is not S3* merely because it contains:

- `review`;
- `verification`;
- `Self_Verification`;
- tests;
- a judge;
- retries;
- a second model.

For a canonical S3* baseline, the evaluated path must preserve all of the following:

1. an ordinary claim or operating report to challenge;
2. materially complementary evidence access;
3. sufficient audit independence for the addressed risk;
4. discrepancy/finding returned into current control;
5. correction or retry with possible re-verification;
6. native or adapter-preserved ownership of that path by the canonical harness being scored;
7. matched model/task/environment/evaluator where cross-harness comparison is claimed.

This keeps function mapping separate from benchmark vocabulary.

## Direct family: TrueCall runtime verification

Reviewed TrueCall revision:

`3b1d8ce253ad6d9908936f844bf5e0255785e8b9`

The direct mapping is based on the actual audit path:

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

## Native proxy: SWE-agent

SWE-agent remains the strongest native benchmarked proxy found so far.

Its first-party SWE-bench Lite configuration explicitly runs:

- `agent.type: retry`;
- multiple operational attempts;
- a separate chooser/reviewer model;
- reviewer selection among candidate patch submissions.

This is real benchmarked native S3* mechanism evidence, but SWE-bench is reviewed as a direct **S1** benchmark. Its score is end-to-end software task success, not a direct S3* discrepancy/challenge/feedback metric. The evidence therefore remains `native-proxy`.

## Negative control: PawBench `Self_Verification`

PawBench publishes a `Self_Verification` capability slice in the same fixed-model harness matrix used by the S1 baseline.

That label must not be translated into S3*.

The slice remains task-performance evidence and does not by itself establish:

- an ordinary claim versus a distinct reality path;
- audit independence;
- discrepancy detection;
- corrective return into S3;
- re-verification.

This case is retained explicitly as `capability-label-not-s3star` so future domain/capability views cannot silently equate benchmark vocabulary with VSM organizational functions.

## Canonical native paths without direct benchmark results

The absence of a direct benchmark is represented as missing evidence, not a low score.

### Codex Guardian / AutoReview

Canonical Codex has `S3*=C`. Its optional Guardian/AutoReview path runs a distinct reviewer over a captured proposed action, can gather read-only context, and returns a structured allow/deny result into execution.

The reviewed public search did not recover a first-party published benchmark cell that directly measures this native complementary-audit path and supports a matched canonical-harness comparison. TrueCall-wrapped Codex remains an external composed system, not Codex Guardian evidence.

### Omnigent Polly reviewer

Canonical Omnigent has `S3*=A`. The bundled Polly organization uses a separate cross-vendor reviewer; blocking findings become corrective fix tasks.

The repository has broader release/performance benchmark infrastructure, but the reviewed benchmark surfaces did not publish reviewer-specific discrepancy, corrective-return and re-verification measurements under a matched canonical-harness design. Generic regression/performance benchmarks are not promoted to S3*.

### thClaws Team audit path

Canonical thClaws has `S3*=A`. A teammate completion claim can be challenged through direct lead inspection of workspace reality; inadequate work can be returned to the responsible teammate before acceptance/integration.

No reviewed published benchmark was recovered for this exact claim → complementary inspection → corrective return path.

### Reigen verification constructor

Canonical Reigen has `S3*=C`. A configured project verification command can inspect a finished child's worktree before the manager consumes the child-completion event, and the verdict returns into current control.

No reviewed published direct benchmark was recovered for that constructor path.

These cases are recorded as `candidate-native-no-direct-results`: the organizational path exists, but the benchmark observation does not.

## Existing proxy: AuditBench

AuditBench remains a strong S3* proxy. Its investigator can obtain alternative evidence about hidden target-model behavior, but the target is an external benchmark object and findings do not have to return into current control of the same operating organization.

## Representative canonical S3* systems inspected

The coverage layer checks mechanism-diverse current canonical systems:

- `omnigent` — `S3*=A`, separate cross-vendor reviewer and corrective fix-task loop;
- `thclaws` — `S3*=A`, completion claim challenged through direct workspace inspection and corrective return;
- `codex` — `S3*=C`, optional Guardian AutoReview path;
- `swe-agent` — `S3*=C`, optional retry/chooser reviewer path;
- `reigen` — `S3*=C`, independent worktree verification constructor path.

## What would close the primary gap

A usable primary baseline needs at least one matched cell where two or more canonical harnesses exercise their own complementary-audit paths under comparable disturbances.

A suitable benchmark would preferably report S3*-specific observables such as:

```text
injected / naturally occurring audit-relevant failures
        ↓
discrepancy detection rate
false-positive rate
corrective-return rate
successful re-verification rate
        +
audit cost / latency
```

End-task S1 success may be retained as downstream context, but it should not replace the audit-specific measurement.

Until such a cell exists:

```text
S3* primary baseline = gap
```

That is an evidence state, not a zero capability score.

## Source of truth

- `benchmark_observations.json` — direct S3* observations at non-canonical composed boundaries;
- `canonical_observations.json` — direct native/adapter-preserved canonical harness observations; currently `[]`;
- `coverage.json` — direct/proxy/negative-control/native-no-results cases;
- `validate.py` — checks the reviewed direct family, observation separation, required search cases and canonical assessment anchors.

## Non-goals

This layer does not:

- infer canonical S3* ownership from TrueCall results;
- credit an external audit plugin to Codex or Claude Code;
- treat every verifier, judge, test, `Self_Verification` label or retry loop as S3*;
- convert missing native benchmark results into zero scores;
- infer autonomy state from detection/retry/reward metrics;
- combine S3* detection with S1 recovery into one score;
- modify canonical assessments, Profile, Skills, catalog or derived rankings.
