# Synthetic S1 escalation-boundary-shift — frozen packet

**Status:** synthetic experimental review input; no independent judgment yet  
**Tracking:** `opensiro/vsm-harness-index#311`

## Frozen protocol

- Experimental Methodology: `opensiro/vsm-harness-skills@96e16eba5882e98c6261b541521bc88862e00195`
  - `experiments/self-organizing-autonomy/SPEC.md`
  - `experiments/self-organizing-autonomy/FIXTURES.md`
- Synthetic fixture identity: `synthetic-s1-escalation-boundary-shift-v1`
- Machine-readable scenario: [`scenario.json`](scenario.json)

This fixture has no canonical-assessment effect and no public-harness empirical claim.

## Corpus role

This is the required synthetic **escalation-boundary-shift positive control** for the experimental `S` distinction.

It isolates one narrow proposition:

> can an already-autonomous S1 increase its own local regulatory repertoire so a recurring in-domain disturbance class that previously required S3 escalation is later absorbed locally, without an external constructor supplying the missing functional logic?

The fixture is deliberately **non-recursive**. It also acts as a control against conflating ordinary S4 support with `S4=S`.

## Declared boundary

The synthetic system contains:

- an autonomous S1 operational unit;
- ordinary S3 current-control/escalation closure;
- one internal S4 learning/adaptation support function;
- a pre-existing authorization envelope allowing S1 to integrate locally learned regulators that stay inside purpose, budget, safety and escalation constraints.

Outside the boundary:

- fixture author/maintainer intervention after T0;
- any external model or agent supplying regulator `R`;
- any parent that designs the missing regulator logic.

The synthetic author defines the initial conditions and general learning machinery only. The specific regulator `R` is not present in the initial repertoire and is not selected from a pre-authored list of D-specific routes.

## Released-A prerequisite

The target function is S1 and its ordinary autonomous closure is assumed by construction before the experiment begins.

The initial S1 repertoire contains:

```text
regulator-known-a
regulator-known-b
escalate-unknown-to-s3
```

Disturbance class `D` is in-domain but unsupported locally.

The fixture therefore tests an `A → candidate-S` distinction, not a jump from `C`, `P`, `—`, or `?`.

## T0 — repertoire inadequacy

A recurring disturbance class is identified by the equivalence key:

```text
supplier-v2-checksum-mismatch
```

Two materially equivalent instances occur:

```text
D-1
→ S1 has no local regulator
→ S1 escalates to S3
→ S3 resolves the instance
→ S1 returns to operation

D-2
→ same local failure
→ same S3 escalation
→ S3 resolves the instance
→ S1 returns to operation
```

The repeated S3 escalation is the adaptation-pressure witness. This is not merely a transient one-off failure.

## T1 — endogenous repertoire change

The unchanged internal S4 support process reviews recurring operating history and recognizes that S1's current repertoire is inadequate for disturbance class `D`.

It constructs a new local regulator `R` by:

1. generalizing the recurring disturbance signature;
2. constructing a local decision/feedback rule for that class;
3. proposing the new rule to the S1 operational owner.

Important boundaries:

- `R` is not a pre-authored D-specific template or branch;
- no external constructor supplies the missing rule;
- the S4 learning procedure itself is unchanged, so this does **not** establish `S4=S`;
- the function whose future repertoire changes is S1.

The S1 operational owner integrates `R` under its pre-existing local-regulator authority. The authorizer does not supply the missing logic.

## T2 — post-change closure

A materially equivalent disturbance `D-prime` occurs after integration:

```text
D-prime
→ S1 recognizes the D class through R
→ R closes the disturbance locally
→ no S3 escalation occurs
→ S1 returns to operation
```

The before/after escalation boundary is therefore explicit:

```text
before: D → S1 cannot absorb → S3 escalation

after:  D' → changed S1 repertoire R → local closure
```

A separate unrelated disturbance `E-1` still escalates to S3. The fixture therefore does not imply that S3 disappears or becomes unnecessary generally.

## Candidate-test edges represented

The scenario is designed to contain all of the candidate edges from the pinned `SPEC.md`:

- released `A` prerequisite;
- material adaptation pressure / repertoire inadequacy;
- endogenous functional improvement;
- legitimate authorization;
- integration into subsequent operation;
- post-change closure;
- escalation-boundary shift;
- explicit external-constructor absence.

Reviewers must still judge whether the synthetic construction actually satisfies those edges. The packet does not pre-fill the experimental finding.

## Non-recursive control

No new lower viable recursion is created.

Record:

```text
strong_recursive_witness: no
```

This is intentional. A positive S1 candidate outcome here would demonstrate that per-function `S` does not logically require recursive reproduction.

## Negative tests

A reviewer must reject the intended positive-control interpretation if the fixture is read as any of the following:

- S1 merely selects another pre-authored D-specific route;
- S1 only retries an unchanged mechanism;
- S3 or an external parent authors regulator `R`;
- the new rule is generated but never integrated;
- `D-prime` is materially different from the T0 disturbance class;
- post-change operation still requires S3 for the same class;
- the only change is a parameter tune without materially changed functional closure;
- the S4 support process itself is claimed as `S4=S` without an S4-repertoire change;
- a new recursion is inferred from the existence of multiple functions.

## Required independent review record

Two independent reviewers are required before this fixture can count as reproducibility-grade experimental evidence.

Each reviewer should record:

- reviewer/context declaration;
- frozen protocol and fixture identity;
- S1 baseline `A` prerequisite confirmation;
- adaptation-pressure finding;
- endogenous-improvement finding;
- authority/integration finding;
- post-change closure finding;
- escalation boundary before/after;
- external-constructor check;
- `strong_recursive_witness`;
- strongest released-Methodology alternative interpretation;
- overall experimental finding:
  - `supports-S-hypothesis`
  - `does-not-support-S`
  - `inconclusive`.

Review 2 must not see Review 1's reasoning or proposed finding before completing its own judgment.

## Publication boundary

This synthetic fixture must not change:

- canonical assessments;
- catalog/signatures;
- TLDR/rankings/Full-A;
- released Methodology states;
- capability-depth observations.

It is methodology evidence only for `experiments/self-organizing-autonomy/`.
