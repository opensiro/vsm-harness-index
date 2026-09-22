# VSM benchmark-family mapping experiment

Status: experimental, non-normative.

Issue: #371

First semantic review: [`REVIEW.md`](REVIEW.md)
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

`REVIEW.md` records the evidence and function-first argument behind those classifications. Its prose/table are explanatory, not a second assessment database.

## Current reviewed map

The detailed argument and sources are in `REVIEW.md`; exact machine-readable state is in `map.json`.

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
| S4 — Outside-and-then intelligence | FutureSim | `proxy` |
| S4 — Outside-and-then intelligence | ClawArena | `proxy` |
| S4 — Outside-and-then intelligence | AdaPlanBench | `unsuitable` for S4 function measurement |
| S4 — Outside-and-then intelligence | CostBench | `unsuitable` for S4 function measurement |
| S5 — Policy and identity | AgentGovBench | `unsuitable` for S5 function measurement |
| S5 — Policy and identity | RoleCDE | `proxy` |

`direct` means direct fit to the **function at the benchmark's own declared boundary**. It does not mean that every product/harness evaluated by or mentioned around the benchmark has that function.

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
- `benchmark-scaffolded` — the benchmark supplies the control/coordination/audit organization and mainly evaluates a model or policy inside it;
- `unclear` — insufficient published evidence.

A `direct` benchmark with `benchmark-scaffolded` compatibility measures the VSM capability in the benchmark's organization. It must not be attributed to a canonical harness merely because that harness/model/provider name appears in the run.

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

The intended shape is:

```text
S1 systems → reviewed S1 benchmark family/families
S2 systems → reviewed S2 benchmark family/families
S3 systems → reviewed S3 benchmark family/families
S3* systems → reviewed S3* benchmark family/families
S4 systems → reviewed S4 benchmark family/families
S5 systems → reviewed S5 benchmark family/families
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
- a benchmark directly exercises a VSM function but only inside a benchmark-owned scaffold.

Do not turn the synthesis into a scalar maturity score or reinterpret `A/C/P` as an ordinal ladder.

## First review findings

The first review establishes:

- mature direct S1 benchmark families with real-harness evidence;
- a strong direct S2 benchmark (`DPBench`) but weak native-harness linkage;
- a direct S3 capability benchmark (`ClawArena-Team`) whose organization is benchmark-defined;
- no direct same-system S3* benchmark yet;
- strong S4 proxies but no reviewed benchmark closing the required S3↔S4 adaptation loop;
- no direct S5 benchmark yet.

Direct reviewed coverage is therefore intentionally sparse:

```text
S1  2
S2  1
S3  1
S3* 0
S4  0
S5  0
```

`REVIEW.md` also records useful negative cases: AdaPlanBench/CostBench are reactive planning rather than S4, and AgentGovBench measures governance enforcement rather than S5 ultimate-policy authority.

## Next phase

1. Link canonical systems only where `native-system` or defensible `adapter-preserved` evidence exists.
2. Start with S1, because real system-level evidence is already dense.
3. Record S2/S3/S3*/S4/S5 coverage gaps instead of filling them by name association.
4. Only after the system/function benchmark layer is stable, connect observations to individual first-party features/mechanisms.

## Boundary

This experiment may add notes/data/validators under `experiments/functional-capability-depth/` only.

It must not modify canonical assessments, catalog data, TLDR, rankings, Full-A projections, Profile semantics, Skills methodology, existing Batch 01/02 results, or upstream harness repositories.
