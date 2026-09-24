# Direct S3* benchmark coverage

Status: experimental, non-normative.

Initial issue: #392  
Primary-baseline follow-up: #430  
First canonical native observation: #502

Parent semantic map: `../vsm-benchmark-family-map/`

## Question

Can a reviewed direct S3* benchmark be linked to canonical Index systems without confusing an external audit wrapper, a generic review label, or ordinary task self-checking with the canonical system's own complementary-audit implementation?

Current answer:

```text
reviewed direct S3* benchmark families: 4
published direct observations at composed S3* boundaries: 3
canonical native direct-S3* observations: 1
S3* primary baseline: gap
```

The evidence state now has three layers:

```text
semantic gap: closed
  multiple direct families exercise complementary audit + corrective return

canonical linkage gap: partially closed
  AppliedScientist provides the first reviewed native canonical observation

matched-primary gap: open
  no common benchmark cell yet compares native S3* implementations across multiple canonical harnesses
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

For direct S3* evidence, the evaluated path must preserve all of the following:

1. an ordinary claim or operating artifact to challenge;
2. materially complementary evidence access;
3. sufficient audit independence for the addressed risk;
4. discrepancy/finding returned into current control;
5. correction or retry with possible re-verification.

For a canonical S3* observation, the path must additionally be native or defensibly adapter-preserved for the canonical harness being observed. A cross-harness primary baseline further requires a matched model/task/environment/evaluator cell.

This keeps function mapping separate from benchmark vocabulary and keeps ownership separate from capability measurement.

## Composed direct families

### TrueCall runtime verification

Reviewed TrueCall revision:

`3b1d8ce253ad6d9908936f844bf5e0255785e8b9`

The τ²-bench integration injects silent write-tool failures by undoing the database mutation while preserving a success-shaped tool response. The complementary post-condition path independently inspects world/database state, detects the discrepancy, replaces the false success with corrective feedback, and allows subsequent retry/re-verification.

Across the publisher's three paired run groups, `benchmark_observations.json` records:

- all injected silent failures detected;
- zero false positives in the reported runs;
- baseline mean task reward `0.362`;
- TrueCall mean task reward `0.384`;
- end-task recovery **not established**, because run-level reward deltas were inconsistent;
- retry uptake changing from `8%` (`n=25`) under soft correction wording to `64%` (`n=11`) under imperative wording.

The direct S3* result is the complementary detection/feedback path. It is not a claim that downstream S1 recovery is guaranteed.

### SWE-Review-Bench

SWE-Review-Bench closes a benchmark-defined generate → independent review → revise → re-verify loop. A separate reviewer explores the repository and candidate PR, returns structured approve/reject feedback, rejected work returns to the original generator, and the revised patch is independently re-evaluated through SWE-bench.

The published example for Qwen3-30B-A3B reports an initial resolve rate of `27.5%` and iterative resolve rate of `56.9%` (`+29.4` percentage points). Because the reviewer/revision organization is supplied by the benchmark, this remains composed direct S3* evidence rather than native evidence for an execution substrate or PR-generator harness.

### harness-bench adversarial review

harness-bench Pilot 4 directly instantiates a separate adversarial reviewer, returns `REQUEST_CHANGES` findings to the original executor session, performs one revision round, then reruns build, visible tests and held-out verification. The two published L2 FULL runs both requested changes, both revised, and both passed post-revision build/visible/holdout checks.

The benchmark authors describe this as a clean-room benchmark implementation of production patterns rather than production Telos code. The result therefore belongs to the benchmark-defined composed organization.

## First canonical native observation — AppliedScientist

Canonical anchor:

```text
harness_id: appliedscientist
catalog: 221
review_ref: 762824fd41598370e75588861b48991b0a9fd784
S3*=A
```

The standalone canonical assessment established the native S3* path independently from repository evidence: the Scientist submits the current manuscript to a separately deployed Reviewer, the Reviewer performs a fresh independent review with its own literature/methodology evidence access, findings return to the Scientist for corrective code/experiment/manuscript work, and the revised artifact is submitted for another fresh review.

The first-party publication then directly exercises that organization over 30 completed scientific-revision trajectories and five revision rounds. `canonical_observations.json` records the reported closure counts:

- execution-related weaknesses: `128 / 150` resolved (`85.3%`);
- idea-related weaknesses: `2 / 18` resolved (`11.1%`);
- revision conditions include human-initialized reviewer-guided revision, AI-initialized reviewer-guided revision, and autonomous fixed-prompt self-revision;
- saved human-initialized versions are separately scored by Stanford Reviewer as an external validation surface, not as the native S3* owner.

This is **first-party-reported**, not independently reproduced. The public repository at the canonical review ref implements the same Scientist → separate Reviewer → correction → fresh-review architecture described in the publication, but the fetched publication does not expose an explicit repository URL binding the reported experimental runs to that exact Git commit. The validator preserves this caveat mechanically.

This observation closes the previous `canonical_direct_observation_count = 0` evidence gap. It does **not** close the primary-baseline gap because it is one within-system result rather than a matched cross-harness comparison.

## Native proxy — SWE-agent

SWE-agent remains native benchmarked proxy evidence. Its first-party SWE-bench Lite configuration explicitly runs multiple attempts plus a separate chooser/reviewer model, but SWE-bench scores end-to-end software-task success rather than complementary-audit discrepancy and feedback. The evidence therefore remains `native-proxy`, not direct S3*.

## Negative controls

### PawBench `Self_Verification`

PawBench publishes a `Self_Verification` capability slice in the same fixed-model harness matrix used by the S1 baseline. The label does not establish a materially distinct reality path, audit independence, discrepancy detection, corrective return, or re-verification, so it remains `capability-label-not-s3star`.

### SilentProbe self-monitoring

SilentProbe exposes ordinary tool-using agents to production-API silent failures and reports low self-detection and no repair in its evaluated loop. This is useful negative evidence for same-agent self-monitoring, but it does not instantiate a materially distinct complementary evidence channel and remains non-direct scaffolded evidence.

## Canonical native paths without direct benchmark results

The absence of a direct benchmark is represented as missing evidence, not a low score.

- `codex` — `S3*=C`; Guardian/AutoReview supplies a first-party complementary review path, but no reviewed direct native result cell was recovered.
- `omnigent` — `S3*=A`; Polly supplies a separate cross-vendor reviewer and corrective fix-task loop, but no reviewer-specific direct result cell was recovered.
- `thclaws` — `S3*=A`; teammate completion can be challenged through workspace inspection and returned for correction, but no direct published benchmark was recovered.
- `reigen` — `S3*=C`; project-configured verification can inspect a completed child worktree before completion is accepted, but no direct published result was recovered.
- `redteam` — `S3*=A`; the default cross-provider adversarial reviewer returns requested changes into a fresh implementation/re-review loop, but the pinned repository exposes no committed real Phase-1 result set for direct admission.

These cases remain `candidate-native-no-direct-results`: the organizational path exists, but the direct capability observation does not.

## Existing proxy — AuditBench

AuditBench remains a strong S3* proxy. Its investigator can obtain alternative evidence about hidden target-model behavior, but the target is an external benchmark object and findings do not have to return into current control of the same operating organization.

## Representative canonical S3* systems inspected

The coverage layer currently checks mechanism-diverse canonical systems:

- `omnigent` — `S3*=A`;
- `thclaws` — `S3*=A`;
- `codex` — `S3*=C`;
- `swe-agent` — `S3*=C`;
- `reigen` — `S3*=C`;
- `redteam` — `S3*=A`;
- `appliedscientist` — `S3*=A`, first admitted canonical direct observation.

## What would close the primary gap

A selected primary baseline needs a matched cell where two or more canonical harnesses exercise their own complementary-audit paths under comparable disturbances and evaluation conditions.

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

End-task S1 success may be retained as downstream context, but it should not replace audit-specific measurement.

Until such a cell exists:

```text
S3* primary baseline = gap
```

That is an evidence state, not a zero capability score.

## Source of truth

- `benchmark_observations.json` — direct S3* observations at non-canonical composed boundaries;
- `canonical_observations.json` — direct native/adapter-preserved canonical harness observations; currently one AppliedScientist record;
- `coverage.json` — direct/proxy/negative-control/native-no-results cases and representative canonical cohort;
- `validate.py` — fail-closed checks for direct-family membership, composed/canonical observation separation, published metrics, provenance caveats and canonical assessment anchors;
- `../primary-baselines.json` — primary selection state; remains `gap` for S3*.

## Non-goals

This layer does not:

- infer canonical S3* ownership from external wrappers;
- credit TrueCall to Codex or Claude Code;
- treat every verifier, judge, test, `Self_Verification` label or retry loop as S3*;
- convert missing native benchmark results into zero scores;
- infer autonomy state from capability metrics;
- treat Stanford Reviewer as the native AppliedScientist S3* owner;
- claim the AppliedScientist result was independently reproduced at the pinned Git revision;
- combine S3* detection/closure with S1 task success into one score;
- select a primary baseline from one native observation;
- modify canonical assessments, Profile, Skills, catalog or derived rankings.
