# AgentRoom — S2 public-evidence review

Status: **admit direct paper-backed non-canonical observation**

Tracking issue: #647  
Paper: `AgentRoom: Concurrent Multi-Agent Coding in a CRDT-Backed Shared Workspace`  
arXiv: `2608.23740`  
Published: 2026-08-24

## Decision

AgentRoom provides **direct S2 evidence at the system boundary defined by the public paper**.

The relevant organization is not inferred from the word “coordination”. The reported system supplies a recurring relation among concurrent coding workers:

```text
concurrent coding S1s
→ shared mutable workspace
→ file / semantic collision risk from interaction
→ atomic file claims + shared room state + broadcast/read coordination
→ workers revise ownership / task choice after claim conflicts
→ continued concurrent coding on the shared workspace
```

That is an S2 relation: otherwise useful concurrent S1 activity creates interaction-specific variety, and the first-party coordination relation constrains that interaction and changes subsequent worker behavior.

## Strongest direct comparison

The paper's strongest direct S2 comparison is the T4 Sonnet 4.6 matched-compute contrast between `parallel-merge` and AgentRoom.

`parallel-merge` retains two concurrent coding workers while removing the AgentRoom shared coordination relation: the two agents work independently and their outputs are unioned after execution.

AgentRoom keeps the concurrent two-worker organization but adds the CRDT-backed shared workspace plus the MCP coordination relation and collaboration protocol.

The paper reports:

| Condition | Mean quality | n | sigma |
| --- | ---: | ---: | ---: |
| `parallel-merge` | 0.456 | 12 | 0.178 |
| `AgentRoom` | 0.669 | 14 | 0.140 |

Reported comparison:

- mean difference: `+0.213`;
- Welch `t = 3.35`;
- `p = 0.003`.

Both cells use Sonnet 4.6 on the same T4 financial-ledger task, under the same 600-second task budget and the paper's budget-fair 30–700 second analysis pool.

This is direct S2 evidence because the control preserves concurrency and therefore preserves the interaction-generated disturbance surface rather than replacing the organization with a single worker.

## Bundle-treatment limitation

The comparison does **not** isolate one implementation primitive. AgentRoom is a bundle treatment containing:

- CRDT-backed shared workspace;
- explicit MCP coordination tools;
- collaboration instructions / protocol.

The paper separately reports a six-condition T4 Sonnet 4.6 ordering:

| Condition | Mean quality | n |
| --- | ---: | ---: |
| ChatDev-style | 0.333 | 6 |
| parallel-merge | 0.456 | 12 |
| solo | 0.544 | 32 |
| shared-only | 0.575 | 11 |
| shared + collaboration prompt without MCP | 0.588 | 7 |
| AgentRoom | 0.669 | 14 |

The no-MCP component probe is small and the paper notes that its interval spans zero. This review therefore does not assign a component-level causal percentage to the MCP layer, CRDT layer, or prompt layer separately.

The admitted comparison is the effect of the **reported AgentRoom coordination bundle at its paper-defined boundary**, not a decomposition of that bundle.

## Native coordination path

The paper defines first-party coordination operations including:

- `room_claim(path)` — atomic file claim with conflict rejection;
- `room_release`;
- `room_state` — shared peer / claim state;
- `room_broadcast` and `room_read` — append-only room communication;
- CRDT-mediated shared filesystem state.

The collaboration protocol requires agents to inspect room state before writing, claim files, revise their plan when a claim conflicts, poll teammate updates, and broadcast completion.

That establishes the organizational function at the paper-defined AgentRoom boundary independently of the measured task-quality result.

## Public provenance

The immutable public experimental record used here is the paper itself.

The paper reports the task conditions, model identities, command-line client versions, wall-clock budgets, per-cell sample counts and statistical comparison. It also reports the relevant coordination mechanism and ablation definitions.

The paper cites a software repository at:

`https://github.com/seonglae/AgentRoom`

At review time, that repository returns `404` through the public GitHub API. Therefore this transaction does **not** invent or infer:

- a software repository revision;
- commit-level implementation provenance;
- a current public repository identity;
- an Index canonical harness identity.

If a public source repository later becomes recoverable, it may add implementation provenance without rewriting this historical paper-backed observation.

## Evidence classification

This observation is recorded as:

- function: `S2`;
- benchmark fit: `direct`;
- evidence source: `first-party-reported`;
- system compatibility: `native-system` at the paper-defined AgentRoom boundary;
- comparison class: `partially-matched`;
- canonical harness: none.

`partially-matched` is used instead of a stronger cross-harness class because the treatment changes the full AgentRoom coordination bundle, not a single isolated primitive, and there is no canonical harness identity to compare against another canonical native S2 implementation.

## Effect on S2 depth

AgentRoom adds:

- one direct S2 family;
- one direct non-canonical paper-backed observation.

It does **not** add:

- a canonical native S2 observation;
- a matched comparison across canonical harnesses;
- a canonical autonomy state;
- a global S2 score.

The S2 primary therefore remains `gap`.

## Primary sources

- `https://arxiv.org/abs/2608.23740`
- `https://arxiv.org/abs/2608.23740v1`
