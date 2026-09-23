# S1 Capability Baseline

Generated experimental projection from `primary-baselines.json`, canonical assessments, and `s1-system-benchmarks/observations.jsonl`.

This is not a global harness ranking. Canonical VSM ownership and benchmark performance remain separate evidence layers. Rows are ordered by harness ID, never by score.

## Function baseline availability

| Function | Status | Primary family | Reference model |
| --- | --- | --- | --- |
| S1 | `selected` | PawBench v1.0 | qwen3.6-35b-a3b |
| S2 | `gap` | — | — |
| S3 | `gap` | — | — |
| S3* | `gap` | — | — |
| S4 | `gap` | — | — |
| S5 | `gap` | — | — |

A `gap` means no primary matched canonical-harness baseline has been selected for that function yet. It is not a zero score and does not mean the function has no benchmark evidence.

## S1 general primary

**PawBench v1.0** · model `qwen3.6-35b-a3b` · scope `general-baseline`

| Harness | Canonical S1 | Historical benchmark identity | Result | Compatibility |
| --- | --- | --- | ---: | --- |
| Hermes Agent (`hermes-agent`) | `A` | `2026.4.23` · version-known | `0.5674` | `adapter-preserved` |
| OpenClaw (`openclaw`) | `A` | `2026.4.24` · version-known | `0.6779` | `adapter-preserved` |
| QwenPaw (`qwenpaw`) | `A` | `1.1.3` · version-known | `0.6828` | `adapter-preserved` |

Only this selected family/cell is the current general S1 baseline. Other S1 observations remain secondary or domain evidence.

## S1 / Coding-SWE domain primary

**Claw-SWE-Bench** · model `Qwen 3.6-flash` · scope `coding-swe`

| Harness | Canonical S1 | Historical benchmark identity | Result | Compatibility |
| --- | --- | --- | ---: | --- |
| Hermes Agent (`hermes-agent`) | `A` | N/A · unknown | `62.6%` | `adapter-preserved` |
| OpenClaw (`openclaw`) | `A` | N/A · unknown | `66.0%` | `adapter-preserved` |

This table is a Coding/SWE projection of S1 capability. It must not be promoted to universal S1 capability.

## Additional Coding-SWE evidence

**FrontierHarness Eval v1.0** · model `Kimi K3` · scope `coding-swe`

| Harness | Canonical S1 | Historical benchmark identity | Result | Compatibility |
| --- | --- | --- | ---: | --- |
| Claude Code (`claude-code`) | `A` | `2.1.237` · version-known | `19/30` (63.3%) | `adapter-preserved` |
| Codex (`codex`) | `A` | `0.148.0` · version-known | `20/30` (66.7%) | `adapter-preserved` |
| Hermes Agent (`hermes-agent`) | `A` | `0.20.4` @ `044acf2bf700` · exact-historical | `15/30` (50.0%) | `adapter-preserved` |
| oh-my-pi (`oh-my-pi`) | `A` | `17.4.0` · version-known | `17/30` (56.7%) | `adapter-preserved` |
| OpenCode (`opencode`) | `A` | `1.18.19` · version-known | `15/30` (50.0%) | `adapter-preserved` |
| Pi (`pi`) | `A` | `0.84.2` · version-known | `18/30` (60.0%) | `adapter-preserved` |

This is additional matched evidence, not another primary and not an input to a composite score.

## Reading rule

```text
canonical VSM state
        ↓
selected function/domain baseline
        ↓
additional benchmark evidence

separate track:
self-organizing adaptation evidence
```

Ordinary baseline observations use the frozen-repertoire rule. Adaptive/self-organizing runs belong to a separate evidence class and are not mixed into these cells.

Do not average PawBench, Claw-SWE-Bench, FrontierHarness, or other benchmark families into one S1 or overall harness score.
