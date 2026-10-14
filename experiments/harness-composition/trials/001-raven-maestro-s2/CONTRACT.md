# Trial 001 — Raven + Maestro S2 ownership lift

Status: **preregistered / not yet executed**.

Governing issue: `opensiro/vsm-harness-index#950`.

This trial is experiment-local and non-canonical. It does not change either component's standalone assessment.

## Research question

Can Raven's constructor-owned S2 coordination become agent-owned at a newly declared composed boundary when Maestro's model-driven Group Chat moderator owns participant/round selection, while Raven and Maestro deterministic mechanisms remain enforcement/support?

## Frozen baseline

| Component | Frozen revision | Canonical standalone state relevant here |
| --- | --- | --- |
| Raven | `e6c0344cb7ce00db25d554e4bb671ec1909a8f9f` | `S2=C` |
| Maestro | `32ecbc14fe832138e9a7af4f263d1026a8aa8a5b` | `S2=A` |

Raven is canonical Index #316. Maestro is canonical Index #128.

## Declared composed boundary

Inside the trial system:

- at least two distinct Raven/Raven-Code workers are S1 units;
- Maestro Group Chat moderator is the candidate S2 decision owner;
- Maestro busy/free routing may enforce dispatch timing;
- Raven stale-edit/read-ledger mechanisms may provide additional deterministic enforcement;
- the human/operator supplies the initial task and trial setup but must not choose each binding coordination decision if the trial is to support `S2=A`.

No standalone vector is added or inherited mechanically.

## Phase A — interface preflight

Before running an ownership trial, establish a real Raven↔Maestro seam.

Required observations:

1. Raven can appear as a Maestro-governed participant, directly or through an experiment-local adapter.
2. The seam exposes stable worker identity.
3. Maestro can dispatch a task/message to that Raven worker.
4. Busy/free and completion state are visible to the coordination layer.
5. Project/worktree identity is sufficient to reason about shared-work interference.
6. The moderator's selected participant/round causes actual Raven invocation without a human re-selecting the binding target.

### Phase-A pass

All six observations are evidenced with frozen refs and a reviewable adapter if needed.

### Phase-A fail

Record `interface-not-closed` and stop if Raven cannot be made a real Maestro-governed participant without replacing the tested organizational relation with a manual/synthetic proxy.

## Phase B — S2 closure trial

Exercise a concrete inter-S1 disturbance, preferably two Raven coding workers operating against shared repository state where concurrent/stale work can matter.

Required closure path:

```text
>=2 Raven S1 workers
        ↓
concrete inter-S1 interference risk
        ↓
Maestro moderator receives participant/work state
        ↓
moderator chooses participant(s) and/or another round
        ↓
deterministic machinery makes the decision govern dispatch
        ↓
Raven worker operation occurs
        ↓
result/state returns to moderator
        ↓
moderator can continue, reroute or stop based on returned state
```

Generic fan-out, message passing or fixed round-robin scheduling is insufficient.

## Ownership counterfactuals

### CF-1 — remove moderator ownership

Keep Raven and deterministic enforcement available but remove the model-driven Maestro moderator from the decisive participant/round selection.

Expected for a genuine ownership lift: the same discretionary coordination choice disappears or becomes constructor/parent-owned.

### CF-2 — remove deterministic enforcement

Keep the moderator's decision visible while disabling one deterministic coordination safeguard where safely possible.

Expected: the discretionary decision remains observable, while reliable/safe realization weakens. This separates decision ownership from enforcement.

## Evidence requirements

Execution must preserve:

- exact component revisions;
- exact experiment adapter revision, if any;
- configuration/environment sufficient to reproduce the seam;
- raw moderator decision trace;
- worker identity/state trace;
- dispatch timestamps/events;
- Raven result/working-state evidence;
- counterfactual trace(s);
- any failure/stop reason.

Do not use prose reconstruction as a substitute for raw execution evidence.

## Allowed findings

`FINDING.md` may conclude only:

- `supports-S2-A-at-composed-boundary`
- `supports-S2-C-only-at-composed-boundary`
- `interface-not-closed`
- `inconclusive`

The finding applies only to the frozen composed trial boundary.

## Fail-closed stop conditions

Stop without an `S2=A` finding if:

- fewer than two distinct S1 workers participate;
- no concrete inter-S1 disturbance is present;
- Raven is not actually governed by Maestro dispatch;
- the moderator only recommends while a human/Raven owner chooses the binding target;
- traces do not distinguish model decision from deterministic routing;
- the tested path bypasses the relevant busy/stale-state relation;
- evidence cannot be frozen/reviewed;
- execution would require modifying canonical assessment state or methodology.

## Non-goals

This trial does not:

- reassess standalone Raven or Maestro;
- test S3, S3*, S4 or S5 lift;
- establish generic plug compatibility;
- claim that every Raven+Maestro deployment has S2=A;
- compare product quality or benchmark performance.
