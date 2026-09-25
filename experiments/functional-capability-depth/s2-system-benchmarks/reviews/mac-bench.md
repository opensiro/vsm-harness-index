# MAC-Bench S2 public-evidence review

Status: **reviewed candidate; not admitted**  
Tracking issue: #654  
Function: `S2`  
Reviewed repository: `HaaswithSai/MAC-Bench-Multi-Agent-Coordination-Failure-Benchmark`  
Reviewed revision: `69cac6981cbaeb0203351b6860692e4c9f950ada`

## Disposition

MAC-Bench is useful public evidence about coordination failure modes in benchmark-authored multi-agent organizations, but the reviewed revision is **not admitted as a counted direct S2 benchmark family** and creates no observation row.

The decision rests on the organizational boundary, the lack of an isolated attenuation treatment, and inconsistent published result provenance. It is not a claim that the benchmark is generally invalid or uninformative.

## What MAC-Bench measures

The repository defines five multi-agent task archetypes:

- role-locked work;
- sequential handoff;
- verification gauntlet;
- debate/deliberation;
- resource contention.

It records task outcomes, turn/token/latency telemetry and detector-labelled coordination failure modes such as loops, stagnation, siloing, handoff corruption, unresolved conflict and coordination overhead.

Resource-contention tasks in particular create real S2-relevant variety inside the benchmark-defined organization: multiple role holders negotiate scarce resources while holding local constraints, dependencies and timing information.

That makes MAC-Bench relevant to S2 research, but relevance alone is not enough for direct-family admission.

## Boundary review

### The tested organization is benchmark-authored

The framework adapters do more than transport a task into an existing harness organization.

For example, `backend/harness/adapters/langgraph_adapter.py` constructs:

- the agent set from benchmark task contexts;
- a benchmark-authored supervisor;
- isolated per-agent memories;
- supervisor routing history;
- explicit `@agent` cross-talk delivery;
- completion/synthesis logic.

The benchmark therefore owns the relevant organizational structure. Running that structure on LangGraph does not make the result evidence for canonical LangGraph S2; canonical LangGraph's own S2 state must be established separately from first-party evidence.

The same identity rule applies to AutoGen and CrewAI rows: a framework display label is not proof that the benchmark exercised a canonical native S2 path.

## No direct attenuation treatment

The benchmark exposes coordination failures and final task outcomes across framework/model configurations, but it does not provide a paired intervention of the form:

```text
same organization + same disturbance
        ↓
coordination mechanism disabled / enabled
        ↓
measured attenuation of that disturbance
```

A resource-contention task may produce a deadlock or successful negotiation, but the benchmark does not isolate which first-party S2 mechanism attenuated the disturbance relative to a matched control.

The resulting rows are therefore broader coordination-diagnostic/team-performance evidence rather than a direct S2 disturbance-to-attenuation family under the current capability-depth contract.

## Result-provenance discrepancy

The reviewed repository commits result JSON files, but the README leaderboard is not consistent with those pinned artifacts.

Examples at the reviewed revision:

- README: LangGraph / Claude Opus 4.7 = `26/30`, `86.7%` success.
- committed `backend/results/langgraph_anthropic_claude-opus-4-7_20260430_213302.json`: `5/30`, `16.67%` success.

And:

- README: LangGraph / GPT-4o = `22/30`, `73.3%` success.
- committed `backend/results/langgraph_gpt-4o_20260430_192913.json`: `0/21`, `0%` success.

The review does not attempt to decide which set is newer or intended. The discrepancy is sufficient to prevent using the README table as an immutable result source without an upstream provenance explanation.

## Relationship to current S2 evidence

This review changes no experimental counts:

```text
direct benchmark families:        7
direct observations:              3
canonical direct observations:    0
native proxy projections:         2
primary baseline:                 gap
```

MAC-Bench is not added to `vsm-benchmark-family-map/map.json`, `coverage.json` or `observations.json` by this review.

## Reopen conditions

Re-review for direct-family admission if upstream publishes a provenance-consistent public experiment that satisfies at least one of these paths:

1. a paired mechanism ablation holding task, model, benchmark organization and evaluator fixed while enabling/disabling a concrete coordination attenuation path;
2. an explicit disturbance variable plus a recoverable before/after or control/treatment attenuation result;
3. a canonical harness row where the evaluated system demonstrably exercises that harness's own native or adapter-preserved S2 path rather than benchmark-authored routing/topology;
4. corrected immutable result artifacts that resolve the README-versus-committed-result discrepancy and support one of the function-valid designs above.

Do not reopen merely because another framework/model row is added to the same benchmark-authored organization.

## Non-claims

- This review does not run or reproduce MAC-Bench.
- It does not claim that MAC-Bench's failure detectors are incorrect.
- It does not infer S2 from benchmark vocabulary such as `coordination`, `resource contention`, or `handoff` alone.
- It does not modify canonical assessments, observations, rankings, catalog or primary baselines.
