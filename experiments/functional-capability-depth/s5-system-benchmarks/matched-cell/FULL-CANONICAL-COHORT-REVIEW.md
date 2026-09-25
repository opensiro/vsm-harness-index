# Full canonical S5 cohort review

Status: experimental, non-normative.  
Tracking issue: #621  
Reviewed: 2026-09-25  
Index revision: `38538480d2fdc0a1ea056d813b9bef5bf3736a5f`

## Scope

This review reconciles the S5 public-evidence search against **every included canonical system with a positive S5 state** at the reviewed Index revision.

Positive states are `A`, `P`, `A(P)` and `C(P)`. `?` is not treated as positive.

The review uses public upstream/third-party evidence only. No harness was run or reproduced by Opensiro.

## Direct-result gate

A canonical direct S5 observation must show the full chain:

```text
identity / ultimate-policy issue
        ↓
legitimate authority at declared recursion
        ↓
actual adjudication / ratification / amendment
        ↓
ownership / enforcement provenance
        ↓
persisted policy or identity change
        ↓
subsequent operation under the changed state
```

A structural S5 mechanism or ownership path is not itself a capability observation.

## Current cohort

| Harness | S5 | Public-evidence disposition | Blocking gate / note |
| --- | --- | --- | --- |
| Ouroboros | `A(P)` | **direct observation** | Existing descriptive parent-governed PR #855 witness; still the only canonical direct observation. |
| Headcount | `A` | no direct public result | actual execution result |
| Henterprise | `A` | no direct public result | actual execution result |
| Argus | `P` | no direct public result | operator identity / standing-objective enactment result |
| LoopX | `P` | no direct public result | Goal-owner policy-change result |
| thClaws | `P` | no direct public result | legitimate deployment-parent signed-policy result |
| Marveen | `P` | no direct public result | owner self-rename / identity runtime result |
| Paperclip | `P` | no direct public result | board strategy enactment result |
| Squad | `P` | no direct public result | user roster/directive enactment result |
| KADATH | `P` | no direct public result | operator-approved run-wide benchmark/fitness-policy result |
| Exo | `A(P)` | no direct public result | runtime Agent/parent identity-policy enactment result |
| omniHarness | `P` | no direct public result | user SOUL/config refinement runtime result |
| AgentOS | `P` | no direct public result | parent SOUL change runtime result |
| CowAgent | `A(P)` | no direct public result | runtime Self-Evolution or parent identity enactment result |
| pibot | `P` | no direct public result | owner persona enactment result |
| WASP | `C(P)` | no direct public result | operator identity enactment result |
| QwenPaw | `P` | no direct public result | persona enactment result |
| Masters of AI Harness | `C(P)` | no direct public result | accepted parent identity-change result |
| Tevarn | `P` | no direct public result | owner strategic-clarification result |
| Shep | `P` | no direct public result | authority-regime enactment result |

Machine-readable per-system findings, pinned refs and reopen conditions live in [`full-canonical-cohort-review.json`](full-canonical-cohort-review.json).

## Near hits

Several systems expose unusually strong mechanisms without a public direct result:

- **KADATH** — operator approval locks the run-wide benchmark/fitness/evidence policy and later epochs are governed by its hash, but no reviewed immutable completed run binds an actual approval to later epochs.
- **Exo** — the Agent and parent can alter durable identity/basic-harness policy and activate it, but public product-development commits are not runtime S5 decisions by the assessed organization.
- **CowAgent** — Self-Evolution can make a rare `AGENT.md` identity revision and the parent can override identity files, but implementation commits do not supply a runtime signal → identity judgment → persisted change → later-operation trace.
- **thClaws** — signed enterprise policy is a strong parent-governed mechanism, but software-maintainer history is not the credited deployment organization's signing authority.

These remain mechanism evidence, not capability observations.

## Result

```text
canonical S5-positive systems reviewed   20
canonical direct observations             1 — Ouroboros
no-direct-public-result dispositions      19
unresolved dispositions                    0
matched multi-canonical S5 primary         no
S5 primary baseline                        gap
```

The full current canonical cohort therefore does **not** supply the materially comparable second canonical direct observation required to reopen primary selection.

## Reopen rule

A system-specific row reopens when new public evidence satisfies its machine-readable `reopen_when` condition. The primary decision reopens when a second canonical native/adapter-preserved direct S5 observation is materially comparable to the existing anchor, or when a matched public benchmark supplies multiple canonical-linkable S5 rows under one authority/change/subsequent-operation protocol.

## Non-claim

`no-direct-public-result` is temporal. It does not mean the harness has zero S5 capability, and it does not alter its canonical autonomy state. The canonical assessment establishes organizational function/ownership; this experiment separately records what public evidence says about observed capability.
