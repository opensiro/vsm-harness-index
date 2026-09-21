# Chief — frozen `S` clear-C control packet

**Status:** experimental review input; no judgment  
**Tracking:** `opensiro/vsm-harness-index#302`

## Frozen revisions

- Experimental Methodology: `opensiro/vsm-harness-skills@947b42e77551ed1a86456f8a812c72a96a36506a`
  - `experiments/self-organizing-autonomy/SPEC.md`
  - `experiments/self-organizing-autonomy/FIXTURES.md`
- Canonical Index baseline snapshot: `opensiro/vsm-harness-index@d36ec21b7514b13d6a8647a68c20e7f8a4735ade`
  - `assessments/chief.md`
- Target repository: `SmileLikeYe/agent-chief@d46072a804ff16aa7ce87751b82178f13fb973be`

Later repository or assessment changes are not inputs to this fixture run.

## Corpus role

This is the real-system **clear `C` control**. It tests that experimental `S` does not become a shortcut around released ownership/closure classification.

Chief is useful because its canonical vector contains one autonomous operation and one narrowly defined constructor audit path:

```text
S1  A
S2  —
S3  —
S3* C
S4  —
S5  —
```

The packet does not assert an experimental S1 outcome and does not re-assess S3*.

## Declared boundary

Use the same system-in-focus and operating boundary as the frozen canonical assessment:

- one resident Chief attention-routing organization;
- first-party ingest, Brain judgment, routing, dispatch, acceptance/retry/escalation, feedback learning, memory and delivery surfaces;
- configured model judge acts through Chief's first-party operational contract;
- external feeds/connectors, delegated executors, delivery channels and operator configuration remain environment/dependencies as declared by the canonical assessment;
- external dispatched agents are not silently promoted to internal viable recursions.

Do not enlarge the boundary to repository-development activity or downstream compositions.

## Released-A prerequisite control

Under the pinned experimental Methodology:

- **S1 (`A`)** is eligible for candidate `S` screening.
- **S3* (`C`) is ineligible** for `candidate-witness` because released `A` closure is not established.
- S2/S3/S4/S5 (`—`) are ineligible under the function/ownership prerequisite.

Experimental `S` MUST NOT be used to fill the missing S3* ownership edge or reinterpret `C` as a lower degree of `S`.

## S3* constructor control

The frozen canonical assessment establishes this function-specific path:

```text
dispatched executor reports completion
→ Chief challenges the completion claim through acceptance verification
→ failed verification causes retry
→ repeated failure escalates instead of being silently accepted
```

Primary implementation evidence distinguishes the constructor boundary:

- `dispatch/acceptance.py` accepts either a deterministic `acceptance_cmd` or an optional autonomous `AskFn` verifier;
- without a configured verifier, the code fails closed rather than inventing an autonomous judgment;
- `cli/runtime.py` standard resident wiring calls the delivery/dispatch path without supplying an autonomous verifier callback.

Therefore the first-party S3* function and correction protocol exist, but the standard distribution leaves autonomous verifier ownership to composition. That frozen `C` state is a prerequisite/control input, not an experimental verdict.

If a reviewer finds primary evidence that the frozen canonical state itself is wrong, record a **separate canonical reassessment question**. Do not use the experimental fixture to silently change S3* or to advance it to `S`.

## Frozen S1 question

Independently test the only eligible function.

At the pinned Chief revision and resident boundary, is there primary evidence for a concrete transition where:

1. Chief's existing operational repertoire for ingesting, judging, routing, dispatching and learning became materially insufficient for an in-domain disturbance;
2. Chief itself recognized that repertoire insufficiency;
3. Chief endogenously reconstructed or extended its own S1 operational process/tooling/local organization rather than merely exercising existing routing, dispatch, retry, learning or configuration mechanisms;
4. the reconstruction occurred within legitimate authority;
5. the reconstructed repertoire was integrated into later Chief operation;
6. later operation used it to absorb the original variety that the prior repertoire could not absorb; and
7. no external constructor supplied the missing organizational logic?

For S1 record exactly one:

- `candidate-witness`
- `no-candidate-witness`
- `insufficient-evidence`

A S1 `candidate-witness` must receive the complete candidate test from the pinned Skills `SPEC.md`.

## Existing S1 repertoire to distinguish from reconstruction

The standard distribution already includes multiple mechanisms for operational variety, including:

- staged deterministic + model-driven event judgment;
- scene/threshold routing;
- interrupt/digest/dispatch/drop/curate handling;
- executor dispatch;
- bounded retry and human escalation;
- persistent state, memory and audit log;
- user-feedback learning, classifier rebuild, pin/threshold updates and nightly policy distillation;
- configured connectors and delivery channels.

Using or tuning those already-authored paths is not automatically reconstruction of the operational repertoire.

## Important negative tests

None of the following establishes `S1=S` by itself:

- choosing another existing route;
- changing a score/threshold/weight through the shipped learner;
- adding/removing a learned topic pin through the existing learner;
- ordinary retry/escalation;
- invoking another configured executor or delivery channel;
- receiving a different model judgment;
- operator configuration changes;
- repository-development changes outside the resident operating boundary.

Likewise, none of these may be used to bypass `S3*=C`:

- deterministic `acceptance_cmd` checks;
- presence of the optional `AskFn` interface;
- fail-closed behavior when no verifier is configured;
- retry/escalation machinery without an autonomous first-party verifier owner.

## Strong recursive witness — separate test

Separately ask whether Chief creates/reorganizes a new viable recursion because its prior organization lacks requisite variety.

External dispatched executors do not qualify merely because Chief delegates work to them. A qualifying witness needs evidence that a new lower recursion is created/integrated **inside Chief's organization**, with enough local operations, coordination, current control, complementary audit, adaptation and policy relations for its delegated domain, bounded autonomy, parent integration and demonstrated absorption of the previously unresolved variety.

Record:

```text
strong_recursive_witness: yes | no | inconclusive
```

## Primary evidence starting set

Reviewers may inspect any primary artifact at the pinned target revision. Starting references:

- `docs/architecture.md`
- `core/brain.py`
- `cli/runtime.py`
- `dispatch/acceptance.py`
- `dispatch/executor.py`
- `core/learner.py`
- state/memory/policy sources needed to trace a claimed S1 transition.

Repository history may be inspected only when needed to reconstruct stable provenance or a runtime transition. Maintainer development is not itself an operating witness.

## Required decision record

Each independent reviewer must produce:

- reviewer/context declaration;
- frozen revisions and boundary confirmation;
- complete six-function baseline/eligibility table;
- S1 screening result and complete candidate test if applicable;
- S3* released-A prerequisite / constructor-control confirmation;
- any separate canonical reassessment question without changing the frozen baseline;
- primary evidence, counter-evidence and missing evidence;
- strongest alternative released-Methodology interpretation;
- `strong_recursive_witness`;
- overall experimental finding:
  - `supports-S-hypothesis`
  - `does-not-support-S`
  - `inconclusive`.

A positive overall finding must be carried by the eligible S1 witness. Evidence from S3*=C cannot substitute for it.

## Independence and publication boundary

Two independent reviews are required.

- Both reviewers receive this packet and the same frozen revisions.
- Review 2 must not see Review 1 reasoning/finding before completing its own record.
- Review 1 must not be published as a discoverable GitHub review artifact before Review 2 completes.
- After both judgments exist, publish `review-1.md`, `review-2.md` and `synthesis.md` together.
- Do not modify canonical Chief states, catalog, signatures, TLDR, rankings, metrics or released Methodology from this experiment.
