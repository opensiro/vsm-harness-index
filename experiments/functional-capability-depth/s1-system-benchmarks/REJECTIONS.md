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

## SWE Atlas public scaffold rows

Reviewed benchmark repository: `scaleapi/SWE-Atlas@49e4af3b6c803dd54a1cd60ead703aac25de4e21`. The benchmark family itself is now admitted as direct Coding/SWE S1 evidence by #717 / #718.

The pinned repository publishes Harbor run configurations for Claude Code and mini-SWE-agent that recover benchmark component, model and substantial run configuration. For example, the Test Writing scripts use Claude Opus 4.6 with `reasoning_effort=high`; the Claude Code arm disables WebSearch/WebFetch and the mini-SWE-agent arm supplies the committed `mswea_tw_config.yaml` configuration.

**Decision:** public Claude Code / mini-SWE-agent rows are not admitted as S1 system observations in this transaction.

**Reason:** historical scaffold identity is not sufficiently recoverable. SWE Atlas documents Harbor `v0.18.0`, which resolves to `harbor-framework/harbor@527d50deb63a5d279e8c20593c18a2cbc7f61f9e`. At that exact Harbor revision, `BaseInstalledAgent` accepts a separate optional `version` field. `ClaudeCode.install()` checks/installs a specific Claude Code release only when that field is present; without it the installer accepts an existing binary or installs without a version pin. `MiniSweAgent.install()` likewise derives `version_spec = ==<version>` only when `_version` is set and otherwise executes `uv tool install mini-swe-agent` without a version constraint.

The reviewed SWE Atlas launch scripts pass `-a claude-code` or `-a mini-swe-agent` plus model/configuration arguments, but do not pass an agent package version. The committed mini-SWE-agent YAML fixes prompts, step limits, environment and model kwargs, not the mini-SWE-agent package version. In addition, SWE Atlas gitignores `results/`, and the reviewed revision contains no committed `results/` directory from which the actual installed agent version could be recovered from immutable run metadata or trajectories.

This is an observation-provenance failure, not a semantic rejection of SWE Atlas. Family-level direct-S1 admission remains valid, and the public rows may still be useful descriptive benchmark results; they are not bound tightly enough to a historical scaffold version/revision for this Index observation layer.

**Reopen when:** an immutable public artifact binds a reported SWE Atlas row to the actual executed Claude Code / mini-SWE-agent / other scaffold version or repository revision, or committed Harbor job/trajectory metadata records the actual agent version for the row. Do not substitute a current project version or infer identity from a leaderboard display label.

## DrugDiscoveryBench

DrugDiscoveryBench may provide useful future S1 evidence.

**Decision:** deferred.

**Reason:** it has not yet been reviewed as a `direct` S1 benchmark family in the committed function→benchmark map. Benchmark-family semantic admission must precede system observation admission.

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

## AgentBoardTT Harness-Bench result corpus

Reviewed repository: `AgentBoardTT/openharness` at `85c54682a209ca7c3fc8b1ab2e820b6724dc3028`. Reviewed result artifact: `eval-results/harness-bench-20260222-143334.json` / `.md`.

This first-party corpus contains real per-task public results for the same eight coding tasks across `harness`, `claude-code`, `opencode` and `pi-mono`. The pinned runner explicitly fixes `claude-opus-4-6` across all four agent labels and also fixes `gpt-5.2` across Harness/OpenCode/pi-mono. The report records 8/8 for Harness and 7/8 for Claude Code, OpenCode and pi-mono in the Opus cell; in the GPT-5.2 cell it records 2/8 for Harness, 7/8 for OpenCode and 8/8 for pi-mono.

**Decision:** unresolved result-bearing candidate; no S1 observation admitted and no primary change.

**Reason:** the benchmark runner launches the competitor binaries `claude`, `opencode` and `pi` from the operator PATH but the committed result records do not preserve the exact competitor harness versions or repository revisions used for those rows. Current canonical Index state also does not provide assessed system identities for AgentBoardTT OpenHarness, OpenCode or pi-mono; Claude Code is not an open canonical Index system. Names plus a matched model/task surface therefore do not satisfy the canonical-linkage/provenance gate. The rows must not be silently attached to similarly named current projects or versions.

The result corpus is useful evidence that the benchmark design executed, but it is not a PawBench primary challenger: PawBench's selected 150-task cell binds three canonical harness identities through version-known native adapters, whereas this eight-task corpus cannot yet establish the compared historical harness revisions.

**Reopen when:** public artifacts bind the executed competitor binaries to recoverable versions/revisions and at least two rows can be linked to canonical Index systems. A separate semantic-review/admission transaction may also consider non-canonical historical observations if the benchmark family is first admitted as direct S1 evidence.

## Generic leaderboard-name matches

Any result that merely names a model, provider, product family or `*-agent` string without sufficient evidence that the canonical harness's own operational loop ran is rejected.

Names do not establish system identity or organizational ownership.
