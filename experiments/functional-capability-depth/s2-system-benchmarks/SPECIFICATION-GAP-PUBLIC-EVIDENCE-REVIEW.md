# The Specification Gap — S2 public-evidence review

Status: **admitted direct non-canonical observation**

Tracking issue: #629  
Repository: `camilochs/the_specification_gap`  
Reviewed revision: `b64059f3ee5cab9b71b834c7b5acc597791880d5`  
Paper: `arXiv:2603.24284`

## Decision

The conflict-recovery experiment is **direct S2 evidence at a benchmark-defined organization boundary**.

The organization contains two coding-worker S1-like units that independently implement disjoint methods under intentionally opposing list-versus-dictionary structural priors. Their outputs can be individually plausible yet carry incompatible assumptions about shared class state. The recovery stage then varies the information membrane presented to the merger while reusing the same split-worker outputs.

The direct functional chain is:

```text
independent workers
→ incompatible hidden representation assumptions
→ integration disturbance
→ shared specification supplied to merger
→ attenuation of representation mismatch
→ changed composed test outcome
```

This qualifies as S2 because the measured variety is interaction-specific: the failure arises from the relation between otherwise separate worker outputs, and the recovery condition attenuates that relational disturbance before return to composed operation.

## Public result

The repository commits the experiment implementation and per-task result corpus in `data/conflict_results/`. The paper reports the 53-task recovery cell:

| Condition | Shared specification | Conflict report | Pass rate |
| --- | --- | --- | ---: |
| Blind | L3 | no | 52.7% |
| Guided | L3 | yes | 52.7% |
| Spec-Only | L0 | no | 88.9% |
| Resolve | L0 | yes | 82.3% |

The single-agent L0 ceiling is 88.3%.

The cleanest attenuation contrast is Blind versus Spec-Only: supplying the full shared specification raises the recovery pass rate by **36.2 percentage points** while operating on the same pair of split-worker outputs. Conflict metadata alone does not improve the L3 recovery cell.

## Boundary

This result is **not** attributed to a canonical harness.

- `canonical_harness_id = null`;
- `system_compatibility = benchmark-scaffolded`;
- evidence source is `first-party-reported`;
- the benchmark-defined worker/merger organization owns the measured S2 relation.

The observation therefore increases direct S2 evidence depth but cannot select a canonical primary baseline. The S2 primary remains `gap` until public evidence supplies a canonical native/adapter-preserved direct observation and a materially matched cross-harness cell.

## Non-claims

- no canonical S2 ownership is inferred from the benchmark;
- no external model or harness inherits S2 from participating in the experiment;
- no autonomy state changes;
- no Opensiro-operated reproduction was performed;
- no universal scalar S2 score is created.
