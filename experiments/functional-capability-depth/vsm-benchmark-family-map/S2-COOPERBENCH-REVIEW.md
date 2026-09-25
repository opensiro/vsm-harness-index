# CooperBench S2 public-evidence review

Status: **direct family; no observation admitted**

Tracking issue: #633

Reviewed upstream revision:

```text
cooperbench/CooperBench@63b9d44d9f39a02fccf5bf0052db48a917a011fd
```

## Functional boundary

CooperBench's `team` setting contains a first-party `team_harness` with an always-on lead/member role split plus independently toggleable coordination mechanisms: an atomic Redis-backed shared task list, shared scratchpad/code exchange, MCP waiting, automatic state refresh and a typed request/response protocol.

Its coding task pairs assign independently useful feature work whose patches are evaluated together on one composed tree. Interaction among the workers can therefore create integration-specific variety that is absent from either feature in isolation. The team-harness relation supplies shared claims/state/code surfaces intended to attenuate that interference.

That is a direct S2 shape at the **benchmark-defined CooperBench team boundary**:

```text
multiple coding S1 workers
        ↓
independently useful feature work
        ↓
integration interference / stale or incompatible combined state
        ↓
team-harness coordination and shared state/code surfaces
        ↓
changed composed result
```

The family is classified `direct` and `benchmark-scaffolded`. This does not create a canonical harness identity.

## Committed ablation report

`docs/team_harness_ablation_report.html` is committed at the reviewed revision. It reports one seed over the same 50 `flash` task pairs with Codex / `gpt-5.5` and Docker. Among the reported rows:

- messaging-only coop: 13/50;
- coop + git: 28/50;
- all-features team: 31/50;
- team without task list: 20/50;
- team without scratchpad: 15/50;
- team without protocol: 35/50.

The report generator binds those rows to named run directories and a one-feature-off bit matrix. This supports the semantic family review, including the fact that task-list and scratchpad surfaces materially alter the composed-team result in that reported campaign.

## Why no observation is admitted

The report generator reads `logs/<run>/.../summary.json` and per-task `result.json` files. The exact flash-run logs used to generate the committed 50-pair report are not pinned as immutable repository artifacts at the reviewed revision.

CooperBench also publishes full-dataset trajectory archives through a separate public dataset. Those trajectories are useful public evidence, but they are a **different evaluation surface** from the 50-pair flash ablation. They must not be silently substituted for the missing flash-run provenance.

Accordingly:

```text
direct family:                  yes
observation admission:          no
canonical harness linkage:      no
canonical direct observation:   no
primary S2 baseline:            gap
```

A future provenance review may admit a CooperBench observation if the exact reported run artifacts become publicly and immutably recoverable, or may separately review the full-dataset trajectory surface as its own observation.

## Sources

- `https://github.com/cooperbench/CooperBench/tree/63b9d44d9f39a02fccf5bf0052db48a917a011fd`
- `https://github.com/cooperbench/CooperBench/blob/63b9d44d9f39a02fccf5bf0052db48a917a011fd/src/cooperbench/team_harness/__init__.py`
- `https://github.com/cooperbench/CooperBench/blob/63b9d44d9f39a02fccf5bf0052db48a917a011fd/docs/team_harness_ablation_report.html`
- `https://github.com/cooperbench/CooperBench/blob/63b9d44d9f39a02fccf5bf0052db48a917a011fd/scripts/gen_ablation_report.py`
