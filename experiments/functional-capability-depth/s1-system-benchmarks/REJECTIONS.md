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

## HarnessBench-Lite

Reviewed repository: `reacher-z/HarnessBench` at `d7ff1255d623177b10b59f858a95f48b7bd070e5`.

HarnessBench-Lite is structurally promising for S1 comparison. It reuses a fixed 20-task ClawBench subset, exposes harness-specific adapters over one shared benchmark stack, and documents a fixed-model matrix workflow whose examples include OpenClaw, Hermes and browser-use. The README identifies `claude-sonnet-4-6` as the model intended for published comparisons.

**Decision:** unresolved candidate; no observation admitted and no S1 primary change.

**Reason:** the reviewed immutable repository exposes fixtures, adapters, matrix/run commands and a leaderboard renderer, but no committed multi-harness result corpus or immutable published leaderboard rows for the advertised HarnessBench-Lite matrix. A runnable matched design is not itself a capability observation. Without recoverable result rows, exact executed harness/configuration provenance and observed scores cannot be bound to canonical systems.

**Reopen when:** the project publishes recoverable multi-harness result artifacts under one fixed task/model configuration, with enough harness/version provenance to establish the executed system identities. At that point it can be reviewed as secondary S1 evidence or, only if it is materially stronger under the existing selection gate, as a PawBench primary challenger.

## Generic leaderboard-name matches

Any result that merely names a model, provider, product family or `*-agent` string without sufficient evidence that the canonical harness's own operational loop ran is rejected.

Names do not establish system identity or organizational ownership.
