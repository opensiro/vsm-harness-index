# Public PolyBench matched-S4 preflight — canonical Continual Harness linkage

Status: experimental, non-normative.

Tracking issue: #547.

This is an additive refinement of the completed #534 and #538 preflights. It does **not** rewrite those historical artifacts.

## What changed

Continual Harness is now independently canonical in the Index:

```text
repository: sethkarten/continual-harness
review_ref: bbab97ad73e460b7cd7c08527d10ced30cc03fbe
catalog_position: 235
status: included
S4=A
```

The ownership result was established from the upstream runtime. Adaptive Auto-Harness paper performance was explicitly excluded from the standalone VSM grade.

This closes one earlier uncertainty:

```text
Does a separately assessed canonical S4 system exist
behind the paper's "Continual Harness" method-family name?

Yes.
```

It does **not** close the next question:

```text
Did the paper's PolyBench row execute that native system,
or an adapter-preserved immutable revision of it?

Not established from public primary evidence.
```

## Paper-level membrane

Historical #538 already establishes:

```text
same chronological task order: yes
same batch loop: yes
PolyBench batch size: 100
solver policy: Claude Sonnet 4.6 unless specified
evolver: Claude Opus 4.6
solver/evolver temperature: 0
common PolyBench Accuracy / Return surface: yes
```

So the remaining blocker is no longer the public experiment membrane.

## Narrowed provenance blocker

The public record currently gives three independent negative checks:

1. `sethkarten/continual-harness@bbab97ad...` contains no `PolyBench`, `Adaptive Auto-Harness`, or A-Evolve binding.
2. The released AdaptiveHarness artifact explicitly does not ship the Continual Harness comparison implementation and does not publish the producing result artifacts.
3. The inspected public A-Evolve pre-release tree `pr/adaptive-auto-harness@e4f70b949989e0abf08532e8223cb9eab447e971` recovers some comparison implementations, but contains no `continual_harness` / `continual*` implementation path.

Therefore:

```text
paper-level matching: satisfied
canonical Continual Harness identity: satisfied
canonical Continual Harness S4 ownership: satisfied
row -> implementation/revision binding: blocked
native S4 path in that evaluated row: not reached
matched canonical S4 cell: not admitted
S4 primary baseline: gap
```

## Why the method name is insufficient

The paper explicitly cites Continual Harness as an existing auto-harness baseline. That is strong evidence for the intended method family, but it is not enough for Opensiro's narrower capability attribution rule.

The missing edge is:

```text
published result row
      ↓
exact evaluated implementation / adapter
      ↓
immutable revision
      ↓
native S4 path proven active
      ↓
canonical harness observation
```

Without that edge, joining the paper row directly to catalog 235 would make organizational identity depend on vocabulary/citation similarity rather than executable provenance.

## Recovery condition

The blocker can be cleared by any primary evidence that unambiguously provides all of:

1. the implementation used for the paper's `Continual Harness` row;
2. its immutable revision/package version;
3. the adapter/launch path used on PolyBench;
4. proof that the native reset-free HarnessEvolver S4 path, or an adapter-preserved equivalent, actually ran;
5. no material substitution of the S4 decision owner.

A public authors' release of baseline code/results, a reproducible commit/tag, or an explicit first-party mapping from the paper row to the upstream implementation could satisfy this.

## Non-goals

This refinement does not:

- create a new benchmark run;
- treat `AdaptiveHarness` mirror as an independent harness;
- infer S4 from the label `Continual Harness`;
- claim the paper row used `bbab97ad...`;
- compare or rank the reported methods;
- modify canonical assessment semantics;
- promote the S4 primary baseline from `gap`.
