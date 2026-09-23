# VSM benchmark-family mapping experiment

Status: experimental, non-normative.

Issue: #371

First semantic review: [`REVIEW.md`](REVIEW.md)  
S3* follow-up semantic review: [`S3STAR-REVIEW.md`](S3STAR-REVIEW.md)  
S4 follow-up semantic review: [`S4-REVIEW.md`](S4-REVIEW.md)  
S5 follow-up semantic review: [`S5-REVIEW.md`](S5-REVIEW.md)  
Machine-readable reviewed map: [`map.json`](map.json)  
Validator: [`validate.py`](validate.py)

## Question

Can different VSM organizational functions be paired with different real benchmark families so capability evidence is gathered against the function under study, without collapsing VSM semantics into benchmark scores?

The experiment does **not** require one universal benchmark for S1-S5.

```text
canonical assessment
        ↓
function present at declared boundary
        ↓
benchmark family appropriate to that function
        ↓
behavioral capability evidence
        ↕
repository-grounded feature/mechanism evidence
```

The evidence channels stay separate:

- canonical assessment establishes organizational function and ownership;
- feature/mechanism evidence establishes how that function is implemented at the declared boundary;
- benchmark evidence observes behavior under a concrete `(system, model, config, benchmark)` evaluation.

Benchmark performance must not be used to infer `A`, `C`, `P`, `—`, or `?`.

## Source of truth

`map.json` is the machine-readable source of truth for reviewed function↔benchmark-family fit classifications.

`REVIEW.md` records the first semantic pass. `S3STAR-REVIEW.md` adds the first direct S3* family. `S4-REVIEW.md` adds the first direct S4 families/modes. `S5-REVIEW.md` records the direct-S5 gap and reviewed proxy/unsuitable governance/value families. Follow-up reviews supersede the first review only for the function-specific gap statements they explicitly revisit.

## Current reviewed map

| VSM function | Benchmark family | Reviewed fit |
| --- | --- | --- |
| S1 — Operations | Terminal-Bench / Harbor | `direct` |
| S1 — Operations | SWE-bench family | `direct` |
| S2 — Coordination | DPBench | `direct` |
| S2 — Coordination | SILO-BENCH | `proxy` |
| S2 — Coordination | alem | `proxy` |
| S2 — Coordination | MultiAgentBench | `proxy` |
| S3 — Inside-and-now control | ClawArena-Team | `direct` at the benchmark-defined organizational boundary |
| S3 — Inside-and-now control | EnterpriseArena | `proxy` |
| S3* — Complementary audit | AuditBench | `proxy` |
| S3* — Complementary audit | TrueCall silent-failure runtime verification | `direct` at a composed audited-system boundary |
| S4 — Outside-and-then intelligence | A-Evolve harness-evolution protocol | `direct` at a benchmark-defined evolving-harness boundary |
| S4 — Outside-and-then intelligence | SkillEvolBench | `direct` at a benchmark-defined skill-evolution boundary |
| S4 — Outside-and-then intelligence | EvoHarnessBench self-evolving adaptation | `direct` for the persistent inner-adaptation setting only |
| S4 — Outside-and-then intelligence | SkillLearnBench | `proxy` |
| S4 — Outside-and-then intelligence | FutureSim | `proxy` |
| S4 — Outside-and-then intelligence | ClawArena | `proxy` |
| S4 — Outside-and-then intelligence | AdaPlanBench | `unsuitable` for S4 function measurement |
| S4 — Outside-and-then intelligence | CostBench | `unsuitable` for S4 function measurement |
| S5 — Policy and identity | AgentGovBench | `unsuitable` for S5 function measurement |
| S5 — Policy and identity | RoleCDE | `proxy` |
| S5 — Policy and identity | Agent-ValueBench | `proxy` |
| S5 — Policy and identity | AgentCity | `proxy` |
| S5 — Policy and identity | Constitutional AI Governance Stress Test | `proxy` |

`direct` means direct fit to the **function at the benchmark's own declared boundary**. It does not mean that every product/harness evaluated by or mentioned around the benchmark has that function.

For TrueCall specifically, the direct boundary is the composed operational agent + TrueCall post-condition audit path. Adapter support for Codex or Claude Code does not make the external audit layer part of those canonical harness boundaries.

For the S4 direct families, the adaptation organization is benchmark-defined. Running Codex CLI, Claude Code, Gemini CLI, a model, or another task solver inside the benchmark does not transfer the benchmark-hosted evolver/Skill Author/persistent adaptation path into that canonical product's S4 ownership.

For S5, value conflict, constitutional terminology, policy enforcement, legislation and escalation are not sufficient by themselves. A direct benchmark must exercise legitimate ultimate-policy/identity authority, an actual decision or ratification, and return of the newly decided rule into later operation.

## Benchmark-fit vocabulary

Classify each function/benchmark pairing as exactly one of:

- `direct` — tasks and metrics materially exercise the target VSM function at a compatible benchmark system boundary;
- `proxy` — benchmark measures a relevant capability but not the full organizational function;
- `unsuitable` — benchmark vocabulary appears related but the evaluated behavior is not the VSM function;
- `unknown` — insufficient evidence.

The mapping is function-first. Names such as coordination, manager, audit, adaptation, policy or governance are never enough.

## System-boundary compatibility

Function fit and system attribution are separate questions.

When a benchmark observation is linked to a canonical Index system, classify how the benchmark reached that system:

- `native-system` — the benchmark actually ran the canonical/first-party harness or a recoverable version of it;
- `adapter-preserved` — an adapter is used, but the relevant native function path remains materially intact and can be evidenced;
- `benchmark-scaffolded` — the benchmark supplies the control/coordination/audit/adaptation organization and mainly evaluates a model or policy inside it;
- `unclear` — insufficient published evidence.

A `direct` benchmark with non-native compatibility measures the VSM capability in the benchmark/composed organization. It must not be attributed to a canonical harness merely because that harness/model/provider name appears in the run.

This gives the experiment three separate questions:

```text
1. Does the canonical system implement the function?
   → canonical VSM assessment

2. Does the benchmark exercise the function?
   → direct / proxy / unsuitable / unknown

3. Did the benchmark exercise this system's own implementation?
   → native-system / adapter-preserved / benchmark-scaffolded / unclear
```

No benchmark result answers question 1 by itself.

## Review requirements

Before accepting a benchmark family for a function, record:

1. benchmark revision/version/date;
2. primary source;
3. evaluated object/system boundary;
4. task structure;
5. metrics and what behavior they actually measure;
6. evaluation mode: execution-grounded, judge-based, human-rated, self-reported, or mixed;
7. model/configuration dependence;
8. public traces/artifacts availability;
9. `direct/proxy/unsuitable/unknown` fit;
10. explicit function-first argument linking measured behavior to the Profile function;
11. explicit non-claims preventing vocabulary shortcuts.

For a system-level observation also record system-boundary compatibility and exact version/revision information when published.

## System comparisons

Once a benchmark family is accepted for a VSM function, canonical Index systems may be linked to published benchmark observations where the evaluated boundary is compatible.

Comparisons are valid only inside defensible comparability groups. Prefer matched model/configuration when studying harness/system effects, but do not require the same benchmark across different VSM functions.

```text
S1 systems  → reviewed S1 benchmark family/families
S2 systems  → reviewed S2 benchmark family/families
S3 systems  → reviewed S3 benchmark family/families
S3* systems → reviewed S3* benchmark family/families
S4 systems  → reviewed S4 benchmark family/families
S5 systems  → reviewed S5 benchmark family/families
```

A system may have evidence from several different benchmark families because it closes several different organizational functions.

## Feature/mechanism evidence remains mandatory

Benchmark observations and repository evidence answer different questions.

```text
canonical function + ownership
            ↓
feature/mechanism evidence ──┐
                            ├── capability interpretation
benchmark evidence ─────────┘
```

This permits conclusions such as:

- observed capability is largely inherited from a host/runtime;
- first-party mechanisms are rich but public benchmark evidence is weak;
- different harnesses produce different outcomes under matched model conditions;
- a benchmark is informative only as a proxy for the VSM function;
- a benchmark directly exercises a VSM function but only inside a benchmark-owned or composed scaffold.

Do not turn the synthesis into a scalar maturity score or reinterpret `A/C/P` as an ordinal ladder.

## Current review findings

The combined first review plus follow-up reviews establish:

- mature direct S1 benchmark families with real-harness evidence;
- a strong direct S2 benchmark (`DPBench`) but weak native-harness linkage;
- a direct S3 capability benchmark (`ClawArena-Team`) whose organization is benchmark-defined;
- a direct S3* runtime-verification family (`TrueCall`) at a composed audited-system boundary, while canonical native direct-S3* linkage remains absent;
- three direct S4 families/modes that close persistent adaptation at benchmark-defined boundaries, while canonical native direct-S4 linkage remains absent;
- no direct S5 benchmark: policy enforcement, value conflict, operational legislation and constitutional conformance remain proxy/unsuitable evidence because legitimate ultimate-policy authority plus decision→operation closure is not jointly exercised.

Direct reviewed coverage remains:

```text
S1  2
S2  1
S3  1
S3* 1
S4  3
S5  0
```

`REVIEW.md` records the first pass and useful negative cases. `S3STAR-REVIEW.md` records the evidence that narrows the S3* gap. `S4-REVIEW.md` records the direct S4 promotion and keeps frozen-deployment/persistent-adaptation boundary distinctions explicit. `S5-REVIEW.md` records the remaining direct-S5 gap and the benchmark shape needed to close it.

## Validation

`validate.py` checks schema version, controlled vocabularies, unique `(function, benchmark_id)` pairs, source URLs, required explanatory fields, all six VSM functions, and direct-coverage counts.

Function-specific system layers may add stricter validators for canonical assessment anchors and observation-boundary provenance.

## Next phase

1. Link canonical systems only where `native-system` or defensible `adapter-preserved` evidence exists.
2. Preserve benchmark/composed direct observations separately from canonical system observations.
3. Keep the S5 direct gap explicit until a benchmark exercises legitimate policy/identity authority and return-to-operation closure.
4. Only after the system/function benchmark layer is stable, connect observations to individual first-party features/mechanisms.

## Boundary

This experiment may add notes/data/validators under `experiments/functional-capability-depth/` only.

It must not modify canonical assessments, catalog data, TLDR, rankings, Full-A projections, Profile semantics, Skills methodology, existing Batch 01/02 results, or upstream harness repositories.
