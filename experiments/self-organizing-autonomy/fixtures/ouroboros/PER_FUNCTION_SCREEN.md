# Ouroboros — required per-function `S` screen

**Status:** experimental review input; no judgment  
**Tracking:** `opensiro/vsm-harness-index#271`  
**Protocol revision:** `opensiro/vsm-harness-skills@ef7c029eae7ac86b90111f6d682563f1cc78593b`  
**Repository revision:** `razzant/ouroboros@86806ee123ce8e26cc063cc1a618f975eea64f26`

This worksheet closes an ambiguity in the initial frozen packet: the `S` hypothesis is **per VSM function**. A reviewer must explicitly screen every released positive function, not only list functions for which a promising witness was noticed.

This file adds no finding and changes no canonical state.

## Required screen

For each row, start from the canonical released baseline and ask whether primary evidence establishes a function-specific transition from the existing repertoire to a reconstructed/extended repertoire that closes previously unabsorbed material in-domain variety.

| Function | Released baseline | Function-specific `S` question |
| --- | --- | --- |
| S1 | `A` | When the existing operational process/tooling/local organization is insufficient, does Ouroboros itself recognize that insufficiency, reconstruct the operational repertoire, integrate it, and then use it to absorb the target operational variety? |
| S2 | `A` | When the existing coordination regime cannot attenuate material interference/oscillation among S1 units, does Ouroboros itself reconstruct the coordination regime and demonstrate closure into later S1 behavior? |
| S3 | `A` | When existing current-control/resource-allocation/accountability/escalation repertoire lacks requisite variety, does Ouroboros reconstruct that regulatory organization and demonstrate later inside-and-now closure? |
| S3* | `A` | When existing complementary audit repertoire is insufficient, does Ouroboros reconstruct audit strategy/probes/evidence access/auditor composition while preserving complementary independence and demonstrate corrective closure? |
| S4 | `A(P)` | When the existing adaptation repertoire is insufficient, does Ouroboros reconstruct how it senses/models/experiments/translates future or external variety, rather than merely use the existing evolution machinery to adapt S1/S2/S3/S3*/S5? |
| S5 | `A(P)` | When existing identity/ultimate-policy machinery is insufficient, does Ouroboros legitimately reconstruct the constitutional/policy machinery or rules for self-revision and demonstrate that later governance is actually closed through the reconstruction? |

## Required row result

Every function must receive exactly one screening result:

- `candidate-witness` — enough primary evidence exists to run the full candidate `S` test for this function;
- `no-candidate-witness` — inspected primary evidence positively keeps the behavior within the existing repertoire / otherwise establishes failure of a required `S` condition;
- `insufficient-evidence` — no qualifying transition can be reconstructed from the available pinned evidence.

`candidate-witness` is **not** `supports-S-hypothesis`. It only means the reviewer must complete the full test from `SPEC.md` for that function.

For each row record:

1. candidate disturbance / target variety, if any;
2. prior repertoire;
3. claimed reconstructed repertoire, if any;
4. evidence for insufficiency and endogenous recognition;
5. authority boundary;
6. integration and post-change closure evidence;
7. external-constructor check;
8. screening result;
9. primary evidence links and caveats.

Do not infer one function from another. In particular:

- self-modification used by S4 to change operational code does not automatically make `S4=S`;
- adding/spawning specialists does not automatically make `S2=S` or `S3=S`;
- changing reviewer configuration does not automatically make `S3*=S` unless complementary independence survives;
- changing `BIBLE.md`, `identity.md`, prompts or settings does not automatically make `S5=S` unless legitimate ultimate-policy reconstruction and later governance closure are established.

## Overall fixture result

After all six rows are screened, apply the full experimental finding vocabulary from the pinned Skills protocol:

- `supports-S-hypothesis`
- `does-not-support-S`
- `inconclusive`

The overall result must identify which per-function witness, if any, carries it. A positive per-function witness does not establish the strong recursive witness; evaluate that separately against `PACKET.md` and `SPEC.md`.
