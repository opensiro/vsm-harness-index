# Rejections and unresolved S1 candidates

Status: experimental.

This file records inspected candidates that were not admitted or not promoted into a stronger comparison class.

## Terminal-Bench 2.1 aggregate rows mentioning multiple agents

Public Harbor leaderboard rows were found under a job whose name includes `terminus-2-claude-code-codex-gemini-cli-3`, with row-level average rewards including 0.66, 0.70, 0.74, 0.78 and 0.83.

**Decision:** not admitted in the initial registry.

**Reason:** the retrieved row evidence did not expose a stable row→agent identity/version mapping. Inferring that one numeric row belongs to Gemini CLI, Codex or another named agent from job naming/order would violate the system-boundary gate.

## OpenHands + Claude 4 Sonnet vs SWE-agent + Claude 4 Sonnet

Both are admitted observations and form the strongest initial comparison group.

**Decision:** `partially-matched`, not `matched-model`.

**Reason:** benchmark, exact model ID and one-attempt setting align, but the historical harness/configuration provenance is asymmetric. OpenHands publishes an exact reproduction commit (`d839f3690fd16c1df0d9613982ac3235ff9a82bd`); SWE-agent identifies `SWE-agent 1.0` and a concrete config but not an exact repository revision. In addition, the SWE-agent submission README's internal 69.0% result differs from the current official leaderboard's 66.6%.

No causal harness-effect delta should be claimed from this pair until that discrepancy/configuration boundary is resolved.

## OpenHands official submission artifact completeness

The checked OpenHands submission publishes metadata, README, result summaries and log/trajectory locations. A later SWE-bench issue reported missing prediction files for several submissions including this one.

**Decision:** observation retained.

**Reason:** the official checked benchmark result, exact reproduction commit and result summary remain sufficient to establish the published observation. Missing prediction-file availability is a reproducibility/provenance limitation, not evidence that a different system was run. The limitation should be revisited before any deeper trajectory-level feature attribution.

## Aider Polyglot

Aider's project-maintained Polyglot benchmark exposes detailed model/edit-format results.

**Decision:** not admitted in this S1 layer yet.

**Reason:** the current reviewed function→benchmark map has not classified Aider Polyglot as a `direct` S1 benchmark family. Benchmark-family semantic admission must precede system observation admission.

## Scale SWE Atlas / DrugDiscoveryBench

These sources explicitly label native harnesses in several runs and may be excellent future S1 evidence.

**Decision:** deferred.

**Reason:** they are not yet reviewed as direct S1 families in the committed benchmark-family map. Add them only through a separate semantic-review change, then link system observations.

## FutureSim Codex runs

FutureSim publishes real Codex-harness evaluations and version metadata.

**Decision:** excluded from this S1 direct layer.

**Reason:** FutureSim is currently classified as an S4 `proxy`, not as a direct S1 benchmark family for this experiment. It belongs in a later S4-proxy system layer rather than being repurposed here simply because Codex executes tools.

## Generic leaderboard-name matches

Any result that merely names a model, provider, product family or `*-agent` string without sufficient evidence that the canonical harness's own operational loop ran is rejected.

Names do not establish system identity or organizational ownership.
