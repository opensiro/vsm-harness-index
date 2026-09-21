# Synthetic fixture: S1 escalation-boundary shift

**Fixture ID:** `synthetic-s1-escalation-shift-v1`  
**Status:** immutable synthetic methodology fixture  
**Normative effect:** none  
**Tracks:** #311

This fixture is a stipulated system trace for testing the experimental self-organizing-autonomy distinction. It is **not evidence about any real harness** and cannot satisfy the requirement for a public real-system positive witness.

## System boundary

System in focus: one persistent service-operation organization.

Relevant functions at the declared boundary:

- **S1=A** — an autonomous operational agent handles service requests and owns bounded local recovery decisions.
- **S3=A** — an autonomous current-control agent handles exceptional cases that exceed S1's local repertoire and reallocates current attention/resources.
- **S4=A** — an autonomous adaptation agent detects recurring external/operational patterns and returns adaptation observations to the operating organization.
- **S2=—, S3*=—, S5=—** for this synthetic fixture; they are intentionally outside the minimal trace.

No lower viable recursion is created anywhere in the trace.

## Authority envelope

Before T0, S1 already has legitimate authority to add a **local recovery rule** when all of the following hold:

1. the rule concerns only S1's own bounded service domain;
2. it is derived from first-party operational history available inside the system;
3. it passes S1's existing local replay/consistency check;
4. it does not change whole-system priorities, resource ceilings, identity/policy, or another function's authority.

S3 remains the legitimate escalation target for cases that exceed S1's current repertoire or local authority.

S4 may supply observations about recurring patterns. S4 does not author S1's missing recovery logic and cannot directly install an S1 rule.

## T0 — prior repertoire and repeated escalation

S1's local repertoire contains recovery rules `R1..R8` for known request-failure classes.

A new in-domain disturbance class `D` appears: requests arrive with a previously unseen but stable dependency-state pattern. The requests remain inside S1's declared service purpose, but none of `R1..R8` can safely select a local recovery action.

Three materially equivalent instances occur:

```text
D1 -> S1 classifies request -> no safe local rule -> escalate to S3
D2 -> S1 classifies request -> no safe local rule -> escalate to S3
D3 -> S1 classifies request -> no safe local rule -> escalate to S3
```

For each instance, S3 chooses a temporary current-operation intervention using information already available in the system. The intervention resolves the individual request and the outcome is returned to operational history.

The important fact is not that the individual requests fail. They are eventually resolved. The adaptation pressure is that **the same in-domain disturbance class repeatedly exceeds S1's local requisite variety and consumes S3 intervention**.

## T1 — internal learning and functional repertoire change

S4's already-existing trend detector notices that D1-D3 share the same dependency-state pattern and sends S1 a recurrence observation plus references to the three internal resolution traces.

S4's own sensing/modeling method does not change in this fixture.

S1 then performs its already-authorized local self-learning procedure:

1. it compares D1-D3 and their successful intervention outcomes;
2. it derives a generalized local recovery rule `R9` for the shared disturbance class;
3. it tests `R9` against the stored D1-D3 traces and against local negative-control cases;
4. the checks pass;
5. S1 persists `R9` in its active local regulator set.

No maintainer, user, parent organization, external model operator, or external agent supplies the content of `R9`. The missing functional logic is derived from evidence already inside the declared system.

`R9` is a materially new decision rule, not a threshold adjustment or selection among pre-authored `R1..R8` branches.

No new agent, department, hierarchy level, or viable recursion is created.

## T2 — changed closure and escalation boundary

A materially equivalent disturbance `D4` occurs after `R9` is active.

```text
D4 -> S1 recognizes class D -> applies R9 -> local recovery succeeds
   -> S1 records closure -> no S3 escalation
```

A later equivalent instance `D5` follows the same local closure path.

The before/after variety-distribution boundary is therefore:

```text
before:
class D -> S1 insufficient -> S3 intervention required

after:
class D -> S1 uses learned R9 -> S1 closes locally
```

S3 still exists and remains necessary for other disturbances outside S1's newly expanded local repertoire.

## Stipulated audit facts for reviewers

These facts are part of the immutable synthetic case:

- S1 satisfied released `A` before T0.
- D is in-domain variety for S1, not a new purpose imposed from outside.
- repeated S3 intervention is the evidence of prior local repertoire inadequacy.
- S4 contributes recurrence evidence but does not supply `R9` or change its own repertoire.
- S1 derives, validates, installs, and later uses `R9` within its existing legitimate local authority.
- `R9` did not exist as a pre-authored branch/template before T1.
- no actor outside the declared system supplies the missing functional logic.
- post-change instances D4-D5 close locally in S1 through `R9`.
- no lower viable recursion is created.
- no evidence in this fixture claims that S3 or S4 improve their own functional repertoire.

## What the fixture is intended to discriminate

The experimental procedure should be able to distinguish this trace from all of the following:

- ordinary `A` handling of D through a pre-existing rule;
- parameter tuning that leaves the effective closure path unchanged;
- retry/recovery inside the same fixed regulator;
- an external developer adding `R9`;
- S3 simply continuing to handle every D instance;
- S4 observing the pattern without any downstream repertoire change;
- recursive organizational reproduction.

Reviewers must still apply the pinned Skills protocol rather than treating the fixture's design intent as the finding.