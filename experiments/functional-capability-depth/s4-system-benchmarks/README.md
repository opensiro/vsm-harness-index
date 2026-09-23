# Direct S4 benchmark coverage

Status: experimental, non-normative.

Issue: #397

Parent semantic map: `../vsm-benchmark-family-map/`

## Question

Can reviewed direct S4 benchmark families be linked to canonical Index systems without attributing a benchmark-hosted evolver, Skill Author or persistent adaptation store to the task-solving harness that happens to run inside the benchmark?

Current result:

```text
reviewed direct S4 benchmark families/modes: 3
published direct evidence records at benchmark/composed boundaries: 3
canonical native/adapter-preserved direct-S4 observations: 0
```

The semantic benchmark gap is therefore closed, but the canonical linkage gap remains open.

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

## Canonical boundary

`canonical_observations.json` is intentionally empty.

A direct S4 benchmark can run a canonical S1 harness while replacing S4 with a benchmark-owned evolver. That is still direct S4 evidence for the **composed benchmark system**, not for the canonical task solver.

Examples:

- SkillEvolBench can run Codex CLI or Claude Code, but its Skill Author is benchmark-hosted;
- A-Evolve supplies the evolution engine around the solver;
- EvoHarnessBench supplies the harness-evolution/adaptation protocol.

No result from those configurations is promoted into canonical S4 evidence merely by task-solver identity.

## Representative canonical S4 cohort

The first pass validates several current ownership arrangements:

- `headcount` — `A`;
- `henterprise` — `A`;
- `kadath` — `A`;
- `omniscientist` — `A`;
- `super-agent` — `A`;
- `bossconsole` — `A(P)`;
- `exo` — `A(P)`;
- `agentyou` — `C`.

These states come from canonical repository assessments, not benchmark scores.

## Proxy controls

### SkillLearnBench

Skill generation/refinement from self or teacher feedback is strongly S4-relevant, but the family-level protocol is more tightly coupled to retry/refinement of the same task family and does not isolate frozen future transfer as cleanly as SkillEvolBench. It remains `proxy`.

### FutureSim

Chronological external sensing and forecast revision are valuable S4 ingredients, but the closed loop is belief/forecast state rather than persistent operational capability change.

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
  did the benchmark exercise this canonical harness's own S4 path?
```

A positive answer to the second question does not imply a positive answer to the third.

## Source of truth

- `benchmark_observations.json` — reviewed direct evidence records at benchmark/composed boundaries;
- `canonical_observations.json` — direct canonical native/adapter-preserved observations; currently `[]`;
- `coverage.json` — boundary/proxy/linkage cases and canonical anchors;
- `validate.py` — validates direct-family map, evidence separation and current S4 assessment states.

## Non-goals

This layer does not:

- infer S4 autonomy from benchmark performance;
- equate generic memory/learning/self-improvement with S4;
- credit a benchmark-hosted evolver to Codex, Claude Code or another task solver;
- collapse `A`, `A(P)`, `C` or other ownership forms into a maturity order;
- modify canonical assessments, Profile, Skills, catalog or generated rankings.
