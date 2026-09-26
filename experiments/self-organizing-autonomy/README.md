# Self-organizing autonomy experiment — Index execution layer

This directory stores **non-normative execution artifacts** for the self-organizing autonomy `S` experiment defined by `opensiro/vsm-harness-skills`.

It does not define VSM semantics, assessment states, or the experimental test itself.

## Source-of-truth boundary

```text
vsm-harness-profile
    VSM organizational semantics
        ↓
vsm-harness-skills
    experimental S classification protocol
        ↓
vsm-harness-index
    frozen real-system fixture packets and review records
```

The current protocol source is:

- `opensiro/vsm-harness-skills/experiments/self-organizing-autonomy/SPEC.md`
- `opensiro/vsm-harness-skills/experiments/self-organizing-autonomy/FIXTURES.md`
- `opensiro/vsm-harness-skills/experiments/self-organizing-autonomy/PROMOTION.md`

Every fixture packet MUST pin the exact Skills revision it uses.

Current packet-class coverage and remaining experiment gates are tracked in [`CORPUS-STATUS.md`](CORPUS-STATUS.md), backed by [`corpus-status.json`](corpus-status.json). Packet coverage is not equivalent to review completion or experiment stability.

## Separation from canonical assessments

Experimental findings are not canonical autonomy states.

A fixture may record only the experimental findings allowed by the pinned Skills protocol, such as:

- `supports-S-hypothesis`
- `does-not-support-S`
- `inconclusive`

These findings MUST NOT be written into `assessments/<harness_id>.md`, `data/catalog.psv`, `data/signatures.psv`, `TLDR.md`, `RANKINGS.md`, `FULL_A.md`, metrics, or other released-state projections unless `S` is later adopted by an explicit Methodology release and migration contract.

## Independent-review rule

For fixtures requiring independent reproducibility review:

1. merge a judgment-free frozen packet first;
2. give each reviewer the same packet and pinned protocol;
3. do not expose one reviewer's reasoning or finding to another reviewer before the latter completes judgment;
4. publish the independent review records together only after both exist;
5. synthesize disagreements explicitly rather than overwriting either review.

Review artifacts are experimental evidence about the candidate classification distinction. They do not rewrite the released assessment baseline.

## Current fixtures

Required-class packets:

- [`chief/`](fixtures/chief/) — clear `C` control; tracked by Index issue #302.
- [`trueforge/`](fixtures/trueforge/) — clear `A` control; tracked by Index issue #301.
- [`harness-evolver/`](fixtures/harness-evolver/) — self-modification boundary / non-`S` control; tracked by Index issue #292.
- [`synthetic-s1-escalation-shift/`](fixtures/synthetic-s1-escalation-shift/) — escalation-boundary-shift positive-control input for S1; tracked by Index issue #724/#311.
- [`scion/`](fixtures/scion/) — repertoire-change without assumed recursion candidate; tracked by Index issue #287.
- [`megaagent/`](fixtures/megaagent/) — strong recursive-realization candidate pinned to the older experimental protocol revision used by Index issue #306.
- [`synthetic-s3star-independence-loss/`](fixtures/synthetic-s3star-independence-loss/) — S3* counterexample where an apparently improved audit path loses complementary independence; packet merged from issue #727.
- [`synthetic-s5-parent-authority/`](fixtures/synthetic-s5-parent-authority/) — S5 counterexample where local policy generation remains parent-governed because higher-recursion constitutive authority is decisive; packet merged from issue #728.

Additional candidate:

- [`ouroboros/`](fixtures/ouroboros/) — first real-system multi-function candidate fixture; tracked by Index issue #271.

These packets were frozen across multiple experimental Skills revisions. See `CORPUS-STATUS.md` before making any corpus-level statement about current-protocol alignment or stability.

## Research notes

Research notes preserve candidate reasoning and evidence leads before a judgment-free fixture packet is frozen. They are not fixture findings and must not be used to alter canonical assessment state.

- [`browser-harness-s1-learning.md`](notes/browser-harness-s1-learning.md) — Browser Harness as a candidate learned S1 regulator / persistent operational repertoire case; focuses on `agent_helpers.py`, domain-skill reuse, the merged Expedia URL-first regulator, and the unresolved external-constructor/provenance test.
