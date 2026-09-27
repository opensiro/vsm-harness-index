# Self-organizing autonomy fixture corpus status

**Status:** experimental, non-normative  
**Tracking:** `opensiro/vsm-harness-index#732`  
**Snapshot:** `opensiro/vsm-harness-index@0ec71f3dddb16b5eb61d624a13420561a69a74da`  
**Current fixture contract:** `opensiro/vsm-harness-skills@8ab5fcbcb96e38eb02be4a6157c5d4a48cd39b23`

Machine-readable source: [`corpus-status.json`](corpus-status.json).

## Current conclusion

All **eight required fixture classes** named by the current experimental `FIXTURES.md` now have a frozen packet in the Index experiment directory.

That is only a **packet-class coverage** statement.

```text
required fixture classes represented: 8 / 8
packet-class coverage complete: yes
uniform current-protocol alignment: no
independent-review completion: no
reproducibility-grade corpus: no
stability gates complete: no
experiment stable: no
```

Do not collapse these stages.

## Required fixture-class coverage

| Required class | Frozen fixture | Packet stage | Review stage | Protocol alignment |
| --- | --- | --- | --- | --- |
| Clear `C` case | [`chief/`](fixtures/chief/) | frozen | independent reviews pending | older pinned protocol; current alignment not revalidated |
| Clear `A` case | [`trueforge/`](fixtures/trueforge/) | frozen | independent reviews pending | older pinned protocol; current alignment not revalidated |
| Self-modifying non-`S` case | [`harness-evolver/`](fixtures/harness-evolver/) | frozen | Review 1 withheld; Review 2 pending | older pinned protocol; current alignment not revalidated |
| Escalation-boundary-shift case | [`synthetic-s1-escalation-shift/`](fixtures/synthetic-s1-escalation-shift/) | frozen | independent reviews pending | older pinned protocol; current alignment not revalidated |
| Repertoire-change non-recursive case | [`scion/`](fixtures/scion/) | frozen | Review 1 withheld; Review 2 pending | older pinned protocol; current alignment not revalidated |
| Recursive realization case | [`megaagent/`](fixtures/megaagent/) | frozen | independent reviews pending | older pinned protocol; current alignment not revalidated |
| S3* counterexample | [`synthetic-s3star-independence-loss/`](fixtures/synthetic-s3star-independence-loss/) | frozen | independent reviews pending | current protocol |
| S5 counterexample | [`synthetic-s5-parent-authority/`](fixtures/synthetic-s5-parent-authority/) | frozen | independent reviews pending | current protocol |

[`ouroboros/`](fixtures/ouroboros/) remains an additional real-system candidate. It is not needed to fill one of the eight required class slots.

## Why current-protocol alignment is still open

Packet presence and protocol alignment are different questions.

The corpus was assembled over several experimental-methodology revisions:

- current S3*/S5 synthetic controls pin `8ab5fcbcb96e38eb02be4a6157c5d4a48cd39b23`;
- the synthetic S1 escalation fixture pins `96e16eba5882e98c6261b541521bc88862e00195`;
- Chief, TrueForge, Harness Evolver, Scion and MegaAgent pin `947b42e77551ed1a86456f8a812c72a96a36506a`;
- Ouroboros pins an earlier experimental revision.

Those frozen revisions remain valid provenance for their individual experiment runs. They must not be silently relabeled as if they had already been reviewed under the current Skills contract.

Before any corpus-level stability decision, protocol drift must be reconciled explicitly. Depending on the change, that may mean proving the old packet remains semantically compatible, refreezing a packet, or running a new review transaction under a later contract. Historical packets should not be rewritten in place merely to create apparent uniformity.

## Review gate remains open

A frozen packet is not a review finding.

For fixtures requiring two independent judgments:

1. both reviewers must receive the same frozen inputs;
2. Review 2 must not see Review 1 reasoning or finding before completing judgment;
3. withheld Review 1 records must stay undiscoverable until Review 2 exists;
4. both reviews and synthesis should be published together;
5. material disagreement must remain visible.

The current packet-design context is not an independent reviewer for fixtures it designed.

## Stability remains much stronger than coverage

The current Skills stability contract requires more than class representation. Among the still-open questions are:

- whether two independent reviewers can apply the distinction reproducibly;
- whether at least one real public harness provides a strong positive **per-function** self-improvement witness, or the experiment explicitly concludes that the proposed distinction is not empirically supported;
- whether self-modification and non-recursive repertoire-change controls behave as intended;
- whether S3* complementary independence and S5 legitimate authority survive the candidate test;
- whether `S` adds information not already captured by released autonomy, ownership, recursion, S4 and closure concepts;
- how parent-governed modes are composed or explicitly excluded;
- whether an adoption/migration plan exists if promotion is ever proposed.

Therefore:

```text
8 / 8 packet classes
```

must never be summarized as:

```text
experiment complete
experiment validated
S supported
S ready for Methodology adoption
```

## Canonical boundary

This status artifact does not alter:

- canonical assessments;
- released autonomy states;
- catalog/signatures;
- TLDR/rankings/Full-A;
- metrics;
- capability-depth observations;
- Profile or Skills semantics.

It is a workflow/provenance snapshot for `experiments/self-organizing-autonomy/` only.
