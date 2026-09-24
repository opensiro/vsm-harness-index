# Direct S4 benchmark coverage

Status: experimental, non-normative.

Initial issue: #397  
Proxy system-observation follow-up: #401  
Primary-baseline follow-up: #432

Parent semantic map: `../vsm-benchmark-family-map/`

## Question

Can reviewed direct S4 benchmark families be linked to canonical Index systems without attributing a benchmark-hosted evolver to the task solver, and without mixing ordinary S4 adaptation with the separate experimental self-organizing `S` question?

Current result:

```text
reviewed direct S4 benchmark families/modes: 4
published direct evidence records at benchmark/composed boundaries: 4
canonical native/adapter-preserved direct-S4 observations: 2
published canonical-system S4-proxy observations: 5 across 3 systems
S4 primary baseline: gap
```

The semantic benchmark gap is closed. The canonical matched-harness linkage gap remains open.

## Rule — ordinary S4 baseline freezes the S4 regulator

An ordinary S4 capability benchmark measures the quality of the system's **current S4 repertoire**.

S4 is allowed to do its normal job: observe external/future distinctions, generate an adaptation option, and change some declared target capability that later operation uses.

It must not silently also improve the S4 mechanism that is performing that adaptation.

```text
ordinary S4 baseline
current S4 regulator is frozen
        ↓
external/future evidence
        ↓
S4 adapts declared target capability
        ↓
later operation measures transfer
```

If S4 changes its own decision/feedback repertoire, that run belongs to the separate self-organizing `S` evidence class:

```text
self-organizing S4 run
S4 changes the S4 regulator itself
        ↓
separate adaptive evidence
```

This is an application of the frozen-functional-repertoire rule in `../BASELINE.md`, not a redefinition of S4.

Ordinary S4 adaptation and experimental `S` therefore remain distinct:

- changing an S1 skill/tool/genome using a fixed S4 mechanism can be ordinary S4;
- changing the S4 mechanism that decides how adaptation is sensed/generated/integrated is the separate self-organizing question.

## Direct S4 families

### A-Evolve harness evolution

Reviewed implementation: `A-EVO-Lab/a-evolve@96ed93ba7ee0b9519fc55c963afb47a1975eb1ae`.

The first-party protocol converts execution evidence into persistent harness changes and measures later benefit. The original family review stored this at the benchmark/composed boundary because A-Evolve did not yet have a canonical standalone assessment. After #512/#515 independently established and admitted canonical `a-evolve` with `S4=A`, `canonical_observations.json` now links the published A-Evolve evolution run to that native S4 system as first-party-reported historical evidence. The reported release lineage and canonical review ref are divergent, so this is not claimed as a reproduction at the canonical commit.

### SkillEvolBench

Reviewed implementation: `AIoT-MLSys-Lab/SkillEvolBench@9e3daa339987c3cfa624121e1be442593a53d43c`.

Acquisition trajectories and verifier feedback feed a separate Skill Author that creates/revises persistent skills. The learned library is then frozen and tested under future context shift, adversarial variants and composition. The Skill Author belongs to the benchmark-defined organization.

### EvoHarnessBench self-evolving adaptation

Reviewed paper: arXiv `2609.04280`.

Only the self-evolving adaptation mode is direct S4. Deployment-only evaluation remains a retention/robustness control. The benchmark supplies the adaptation/evolution protocol rather than measuring a canonical harness's own S4 path.

### Evo-Bench

Reviewed implementation: `RUCAIBox/Evo-Bench@889e4fc8b197f426b444dbf8de217ea15b596fd2`.

Evo-Bench lets an evolver diagnose validation failures and persistently rewrite a minimal executable harness, then freezes the selected harness before a disjoint 448-task evaluation suite. This is direct S4 at the benchmark-defined harness-evolving boundary, not native evidence for an unrelated canonical harness.

## Canonical direct boundary

`canonical_observations.json` now contains two native direct observations: A-Evolve and KADATH. Their canonical assessments independently establish `S4=A`; capability evidence is linked only after that ownership decision.

A-Evolve preserves published harness-updating measurements without collapsing them into a scalar: the best-vs-worst evolver spread is at most 3.1 percentage points on any benchmark; Qwen3-235B reports +8.2 pp on SWE and +0.6 pp on MCP; on SkillsBench Qwen3.5-9B reports +3.8 pp versus Opus 4.6 +2.3 pp and Qwen3-235B +1.5 pp. These are first-party-reported historical results from a divergent release lineage, not reproduction at the canonical review commit.

KADATH's pinned canonical README publishes a ten-epoch native run under one locked fitness benchmark: best fitness 18→91, top-five median 8→77, and the top-five floor 1→71. Each point may be a different leading organism, so this is a population-shift measurement rather than one individual trajectory.

The general system-linkage rule remains unchanged. A direct S4 benchmark can use a canonical harness as its S1 task solver while replacing S4 with a benchmark-owned evolver; that is evidence for the composed benchmark system, not for the task solver. SkillEvolBench's Codex integration remains the key negative control.

Two native observations still do **not** create a matched cross-harness primary. A-Evolve uses published task suites and a controlled harness-evolution protocol; KADATH generates and operator-approves a run-specific fitness benchmark. Their evaluation membranes are heterogeneous, so no shared comparison cell exists.

## Native S4 candidates without a general baseline

### KADATH — canonical native direct observation

Canonical KADATH has `S4=A`, and the same pinned revision publishes a ten-epoch native evolutionary proof under one locked fitness benchmark:

| Top-five measurement | Epoch 1 | Epoch 10 | Improvement |
| --- | ---: | ---: | ---: |
| Best fitness | 18 | 91 | +73 |
| Median fitness | 8 | 77 | +69 |
| Lowest fitness | 1 | 71 | +70 |

The repository states that each epoch point can be a different top-performing organism, so the observation measures an upward shift across the competitive population rather than a cherry-picked individual trajectory. The ordinary-S4 boundary is clean: organism genomes change only after grading, while the non-evolving kernel, locked benchmark, grading/evidence machinery and selection controls remain outside the evolvable genome.

This closes KADATH's native quantitative-observation gap, not the general matched-primary gap. The fitness benchmark is generated and operator-approved per run, and the published proof does not expose a common goal/model/population/configuration cell shared with A-Evolve or another canonical harness.

### super-agent — durable personal adaptation

Canonical `super-agent` has `S4=A`.

Its nightly Tone Mirror observes real user interaction, rewrites a durable user profile, and later normal turns inject that changed profile into their context.

The reviewed repository search did not recover published before/after measurements for later-turn benefit, retention/generalization, regression or adaptation cost. The path is native; the direct benchmark result is missing.

### BossConsole / Tool Evolver — live tool-capability adaptation

Canonical BossConsole has `S4=A(P)`.

Tool Evolver can turn a capability request into a changed plugin, build and hot-reload it into the running installation, probe/verify the new capability and iterate. The reviewed first-party repositories did not expose a standardized published adaptation-results corpus suitable for a matched canonical baseline.

### Exo — native S4 with an explicit freeze boundary

Canonical Exo has `S4=A(P)` and can create reusable tools/skills and edit mounted prompts/source before activation through its guardian path.

Because this reach can also touch machinery that participates in adaptation itself, a normal S4 benchmark must declare the adaptation target and freeze the S4 regulator. For example, measuring a new operational tool under a fixed self-maintenance policy can be ordinary S4; allowing the run to rewrite how Exo performs S4 adaptation itself belongs to the self-organizing `S` track.

The coverage record therefore marks Exo as `native-adaptation-boundary-needs-freeze`, not as a failed S4 system.

## Domain-specific S4 projections

S4 is functionally common but its application domain can be very different. A single software-harness-evolution benchmark should not silently become the universal S4 scale.

Two useful domain projections already emerge from canonical systems.

### `S4 / strategy`

`headcount` and `henterprise` both have `S4=A` through outside/future strategy paths:

```text
markets / competitors / regulation / technology / uncertainty
        ↓
scenarios, assumptions, early-warning distinctions
        ↓
strategic options
        ↓
executive / resource allocation
```

The reviewed repositories do not publish a matched strategy benchmark of those native paths. They remain domain benchmark candidates, not missing or zero capability.

### `S4 / research-science`

Canonical OmniScientist has `S4=A` through literature-grounded ideation: it senses prior scientific work, generates and screens candidate hypotheses for novelty/feasibility, persists the selected direction, and the later experiment stage consumes it.

The reviewed public evaluation surfaces do not provide a matched benchmark specifically measuring that S4 selection → future experiment closure across canonical harnesses.

This belongs naturally in a future `research-science` domain projection.

## FutureSim canonical S4-proxy observations

FutureSim remains `proxy` for full S4. It directly exercises chronological external sensing, search, memory and forecast revision, but it closes on forecast/belief state rather than persistent organizational capability adaptation returned into later operation.

The published recommended/native-harness experiment nevertheless provides observation-specific behavioral evidence:

| Canonical system | Published harness version | Model | Final top-1 accuracy | Final Brier skill score |
| --- | --- | --- | ---: | ---: |
| Codex | `0.125.0` | GPT 5.5 | 25% | +0.05 |
| Claude Code | `2.1.132` | Claude Opus 4.6 | 20% | +0.02 |
| Claude Code | `2.1.132` | DeepSeek V4 Pro | 13% | -0.02 |
| Claude Code | `2.1.132` | GLM 5.1 | 10% | -0.01 |
| OpenCode | `1.4.11` | Qwen 3.6 Plus | 5% | -0.07 |

These rows stay `proxy` / `adapter-preserved` and share the comparability group `futuresim-v1-recommended-harness-cross-system-confounded`.

They are not a causal harness-effect comparison because model and prompt conditions differ. The current canonical assessments of Codex, Claude Code and OpenCode also remain `S4=—`, making these observations a useful negative control:

```text
adaptation-related benchmark behavior
        !=
canonical S4 function / ownership
```

## Other proxy controls

### SkillLearnBench

Skill generation/refinement from self or teacher feedback is strongly S4-relevant, but the family-level protocol is more tightly coupled to retry/refinement of the same task family and does not isolate frozen future transfer as cleanly as SkillEvolBench. It remains `proxy`.

### ClawArena

Staged external evidence and belief revision remain S4-relevant but do not by themselves establish organizational adaptation.

## What would close the general S4 primary gap

A usable primary comparison should provide at least one matched cell where:

1. two or more canonical systems independently establish S4;
2. each system's own native/adapter-preserved S4 path actually runs;
3. the model/configuration is matched where model-driven S4 is involved;
4. the external/future disturbance stream, budget, environment and evaluator are comparable;
5. the persistent adaptation target is explicit;
6. the S4 regulator itself remains frozen for the ordinary baseline;
7. later deployment measures whether the changed capability transfers;
8. retention, regression and adaptation cost are recorded separately where possible.

A narrower benchmark can still become a domain primary if it is labeled honestly, for example `strategy` or `research-science`.

Until a matched canonical cell exists:

```text
S4 primary baseline = gap
```

That is an evidence state, not a zero score.

## Representative canonical S4 cohort

The coverage layer continues to validate several ownership arrangements:

- `a-evolve` — `A`;
- `headcount` — `A`;
- `henterprise` — `A`;
- `kadath` — `A`;
- `omniscientist` — `A`;
- `super-agent` — `A`;
- `bossconsole` — `A(P)`;
- `exo` — `A(P)`;
- `agentyou` — `C`.

These states come from canonical assessments, not benchmark scores.

## Evidence channels

Keep these questions separate:

```text
canonical assessment
  does this harness implement S4 and who owns it?

benchmark semantic review
  does this benchmark directly exercise S4 at its own boundary?

system linkage
  did the benchmark exercise this canonical harness's own S4 path?

ordinary-vs-self-organizing boundary
  was the S4 regulator frozen, or did S4 improve itself?
```

## Source of truth

- `benchmark_observations.json` — direct evidence records at benchmark/composed boundaries;
- `canonical_observations.json` — direct canonical native/adapter-preserved observations; currently 2 (`a-evolve`, `kadath`);
- `proxy_observations.json` — observation-specific canonical-system proxy evidence such as FutureSim;
- `coverage.json` — boundary/proxy/native-no-results/domain/freeze cases and canonical anchors;
- `validate.py` — validates direct-family map, direct/proxy separation, required cases, frozen-regulator guard and current canonical states.

## Non-goals

This layer does not:

- infer S4 autonomy from benchmark performance;
- equate generic memory/learning/self-improvement with S4;
- credit a benchmark-hosted evolver to a task solver;
- convert FutureSim proxy scores into canonical S4 evidence;
- claim a causal cross-harness winner from confounded rows;
- treat native systems without published benchmarks as zero capability;
- infer experimental self-organizing `S` merely because a system performs persistent adaptation;
- combine ordinary S4 and self-organizing S4 runs into one baseline;
- modify canonical assessments, Profile, Skills, catalog or generated rankings.
