# Direct S4 benchmark coverage

Status: experimental, non-normative.

Issue: #397  
Proxy system-observation follow-up: #401

Parent semantic map: `../vsm-benchmark-family-map/`

## Question

Can reviewed direct S4 benchmark families be linked to canonical Index systems without attributing a benchmark-hosted evolver, Skill Author or persistent adaptation store to the task-solving harness that happens to run inside the benchmark?

Current result:

```text
reviewed direct S4 benchmark families/modes: 3
published direct evidence records at benchmark/composed boundaries: 3
canonical native/adapter-preserved direct-S4 observations: 0
published canonical-system S4-proxy observations: 5 across 3 systems
```

The semantic benchmark gap is therefore closed, but the canonical direct-linkage gap remains open. Proxy observations are stored separately and must not be promoted into direct S4 evidence.

## Direct S4 families

### A-Evolve harness evolution

Reviewed implementation: `A-EVO-Lab/a-evolve@96ed93ba7ee0b9519fc55c963afb47a1975eb1ae`.

The benchmark-defined organization converts execution evidence from external task streams into persistent harness changes and then measures whether later agents benefit from the changed harness.

Its experiment design deliberately separates the evolver's ability to update the harness from the later agent's ability to use it.

### SkillEvolBench

Reviewed implementation: `AIoT-MLSys-Lab/SkillEvolBench@9e3daa339987c3cfa624121e1be442593a53d43c`.

Acquisition tasks produce trajectories/verifier feedback; a separate Skill Author induces/revises persistent skills; the skill library is then frozen and tested on context-shift, adversarial and composition deployment tasks.

This directly distinguishes durable procedural adaptation from current-episode retry or raw trajectory reuse.

### EvoHarnessBench self-evolving adaptation

Reviewed paper: arXiv `2609.04280`, v2 dated 2026-09-10.

The benchmark externally evolves tools/skills/specialist agents across stages. Its `self-evolving adaptation` setting additionally lets the evaluated system update persistent inner adaptation state from accumulated experience and carry it across later harness versions.

Only that setting is direct S4. The deployment-only setting is a retention/robustness control and does not itself close S4.

No unambiguous official GitHub code repository was recovered during this review. The record is intentionally pinned to the paper/project protocol rather than an unrelated repository with a similar name.

## Canonical direct boundary

`canonical_observations.json` is intentionally empty.

A direct S4 benchmark can run a canonical S1 harness while replacing S4 with a benchmark-owned evolver. That is still direct S4 evidence for the **composed benchmark system**, not for the canonical task solver.

Examples:

- SkillEvolBench can run Codex CLI or Claude Code, but its Skill Author is benchmark-hosted;
- A-Evolve supplies the evolution engine around the solver;
- EvoHarnessBench supplies the harness-evolution/adaptation protocol.

No result from those configurations is promoted into canonical S4 evidence merely by task-solver identity.

## FutureSim canonical S4-proxy observations

FutureSim is still `proxy` for full S4: it directly exercises chronological external sensing, search, memory and forecast revision as dated information arrives, but it closes on forecast/belief state rather than persistent organizational capability adaptation returned into present capability/S3.

Its published recommended/native-harness experiment is nevertheless useful system-level behavioral evidence because it executes recoverable CLI harnesses rather than collapsing every system into one common agent loop.

The paper reports the following final Figure 1 values over 330 replayed forecasting questions, three seeds and maximum reasoning effort:

| Canonical system | Published harness version | Model | Final top-1 accuracy | Final Brier skill score |
| --- | --- | --- | ---: | ---: |
| Codex | `0.125.0` | GPT 5.5 | 25% | +0.05 |
| Claude Code | `2.1.132` | Claude Opus 4.6 | 20% | +0.02 |
| Claude Code | `2.1.132` | DeepSeek V4 Pro | 13% | -0.02 |
| Claude Code | `2.1.132` | GLM 5.1 | 10% | -0.01 |
| OpenCode | `1.4.11` | Qwen 3.6 Plus | 5% | -0.07 |

These rows are recorded in `proxy_observations.json` as:

```text
benchmark_fit: proxy
system_compatibility: adapter-preserved
comparability_group: futuresim-v1-recommended-harness-cross-system-confounded
```

### What can be compared

The rows can be compared descriptively as observed `(harness, model, prompt condition, benchmark)` configurations under one benchmark protocol.

### What cannot be inferred

They are **not** a causal harness-effect comparison:

- the model differs across the three harnesses;
- Claude Code appears with three different models;
- DeepSeek V4 Pro and Qwen 3.6 Plus received extra prompting intended to encourage prediction updates;
- FutureSim supplies the chronological environment, search/forecast interface and sandbox restrictions.

Therefore do not summarize these values as “Codex beats Claude Code/OpenCode”. A matched-model or otherwise controlled experiment would be needed to isolate a harness effect.

## Negative-control value

The current canonical Index assessments of the three FutureSim-linked products all have:

```text
codex       S4=—
claude-code S4=—
opencode    S4=—
```

They nevertheless show measurable behavior on an S4-proxy benchmark. This is a useful negative control for the entire program:

```text
adaptation-related benchmark behavior
        ≠
canonical S4 function / ownership
```

Benchmark behavior and repository-grounded function/ownership evidence remain independent channels.

## Representative canonical S4 cohort

The direct-S4 coverage pass separately validates several current ownership arrangements:

- `headcount` — `A`;
- `henterprise` — `A`;
- `kadath` — `A`;
- `omniscientist` — `A`;
- `super-agent` — `A`;
- `bossconsole` — `A(P)`;
- `exo` — `A(P)`;
- `agentyou` — `C`.

These states come from canonical repository assessments, not benchmark scores.

## Other proxy controls

### SkillLearnBench

Skill generation/refinement from self or teacher feedback is strongly S4-relevant, but the family-level protocol is more tightly coupled to retry/refinement of the same task family and does not isolate frozen future transfer as cleanly as SkillEvolBench. It remains `proxy`.

### ClawArena

Staged external evidence and belief revision remain S4-relevant but do not by themselves establish organizational adaptation.

## Evidence channels

Keep three questions separate:

```text
canonical assessment
  does this harness implement S4 and who owns it?

benchmark semantic review
  does this benchmark directly exercise S4 at its own boundary?

system linkage
  did the benchmark exercise this canonical harness's own S4 path,
  or only an S4-adjacent capability?
```

A positive behavioral observation does not imply a positive canonical S4 mapping.

## Source of truth

- `benchmark_observations.json` — reviewed direct evidence records at benchmark/composed boundaries;
- `canonical_observations.json` — direct canonical native/adapter-preserved observations; currently `[]`;
- `proxy_observations.json` — observation-specific canonical-system proxy evidence such as the FutureSim CLI runs;
- `coverage.json` — boundary/proxy/linkage cases and canonical anchors;
- `validate.py` — validates direct-family map, direct/proxy evidence separation and current canonical assessment states.

## Non-goals

This layer does not:

- infer S4 autonomy from benchmark performance;
- equate generic memory/learning/self-improvement with S4;
- credit a benchmark-hosted evolver to Codex, Claude Code or another task solver;
- convert FutureSim proxy scores into canonical S4 evidence;
- claim a causal cross-harness winner from model/prompt-confounded rows;
- collapse `A`, `A(P)`, `C`, `—` or other ownership forms into a maturity order;
- modify canonical assessments, Profile, Skills, catalog or generated rankings.
