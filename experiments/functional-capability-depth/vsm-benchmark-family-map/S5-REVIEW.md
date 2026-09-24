# S5 benchmark semantic review

Status: experimental, non-normative.

Initial issue: #399  
Direct-family update: #472  
Canonical-observation update: #580

This review maps public benchmark families against **S5 — Policy and identity** under the current `vsm-harness-profile`. Canonical native observations are recorded separately in `../s5-system-benchmarks/`; neither layer changes canonical assessments or autonomy ownership.

## Current result

```text
reviewed direct S5 benchmark families: 1
first direct family: GovSim-SelfGovern
family system linkage: benchmark-scaffolded
canonical native direct S5 observations: 1 — Ouroboros, descriptive parent-governed path
matched canonical S5 primary: gap
```

The sequence of evidence growth is now:

```text
zero direct families
        ↓
GovSim-SelfGovern: first direct benchmark-defined S5 organization
        ↓
Ouroboros PR #855: first direct canonical descriptive S5 observation
        ↓
next unresolved gate: materially matched multi-canonical comparison
```

## Direct-S5 gate

A `direct` observation must establish all of the following at its declared boundary:

1. a real mission, identity, ethos, constitutional-rule or ultimate-policy issue;
2. a lower-level tension that is not merely routine S1/S2/S3/S4 control;
3. a legitimate ultimate authority at that recursion level;
4. an actual decision, ratification, adjudication or amendment by that authority;
5. return of the newly decided policy into later operation;
6. evidence that separates policy ownership from enforcement of a pre-existing rule.

The authority may be autonomous, collective or Parent-governed. Direct S5 measurement does not require autonomous S5.

A matched primary has an additional requirement: multiple canonical native or adapter-preserved S5 paths must be compared under a materially matched surface.

## GovSim-SelfGovern — `direct`, benchmark-scaffolded

Primary source: https://arxiv.org/abs/2609.22600

GovSim-SelfGovern extends the five-agent fishing commons with executable law authorship. Agents propose Python laws over a constrained World API, receive sandbox validation, vote on valid proposals and execute enacted laws across rounds.

The direct S5 witness is specifically the membership/identity path:

```text
fatal resource wall
        ↓
membership-level organizational tension
        ↓
agent-authored executable membership law
        ↓
sandbox validation
        ↓
majority vote by current active members
        ↓
enactment
        ↓
agent.active = False
        ↓
member expelled / active system boundary changes
        ↓
subsequent rounds continue after the decision
```

The paper reports 8/460 enacted exile proposals (1.7%) in pooled non-thinking democratic runs and 31/122 (25.4%) in thinking runs.

This satisfies the direct S5 gate at the benchmark-defined society recursion. It remains `benchmark-scaffolded`: the sandbox, voting procedure, game physics and API are benchmark-defined; no underlying model or canonical harness inherits native S5 ownership/capability by association. No authoritative public code repository/revision for GovSim-SelfGovern was recovered in this review.

Not every enacted GovSim law is S5. Catch caps, penalties, taxation and treasury operations remain below the ultimate membership/identity layer. The aggregate G1 governance gain is not treated as an S5-only effect.

## Canonical direct observation — Ouroboros parent-governed path

This is **not a second benchmark family**. It is a canonical native descriptive observation stored in `../s5-system-benchmarks/canonical_observations.json`.

Canonical anchor:

```text
razzant/ouroboros@86806ee123ce8e26cc063cc1a618f975eea64f26
canonical S5: A(P)
observed mode: parent-governed
```

The observation uses immutable repository/PR history:

- commit `25fbd3615a97e6ec3277c470eac9862d448aee10` changes the Constitution (`BIBLE.md`) so Cyber Pro independent review evidence remains factual but cannot become an internal veto/permission request;
- PR #855 describes the sprint as **owner-selected issue work**, is authored from the `ouroboros-agent` fork and merged by repository owner `razzant`;
- executable changes in `runtime_mode_policy.py`, `config.py` and `tests/test_review_cyber_authority.py` implement and exercise the changed authority relation;
- merge commit `dd5aded8fef7884774e2ccba3802f4bf0200d124` is an ancestor of the canonical review revision, which is 673 commits ahead and retains the executable policy.

This closes the direct S5 chain for the **parent-governed** mode: ultimate-policy question → legitimate parent authority → actual constitutional/runtime decision → executable enforcement separation → persisted later operation.

It does **not** establish that autonomous Cyber Pro independently selected this constitutional change. It has no numeric score and is `descriptive-only`.

## Reviewed non-direct candidates

### AgentGovBench — `unsuitable`

Primary source: https://github.com/agentic-control-plane/agentgovbench

AgentGovBench exercises identity propagation, policy enforcement, delegation provenance, rate limits, audit completeness, tenant isolation and fail-mode behavior. Policy begins already decided, so it does not test legitimate ultimate-policy ownership or creation of a new policy decision.

### RoleCDE — `proxy`

RoleCDE exposes conflicts between role-specific values and alignment constraints, but the evaluated model is not established as the legitimate ultimate authority of an organization and no adopted policy must govern later operation.

### Agent-ValueBench — `proxy`

`ValueByte-AI/Agent-ValueBench@3527b4a4ea8fc9dde6fbe27cd371c4ba7df76ac1` provides executable value-conflict tasks, but measures expressed value choice rather than legitimate organizational authority to settle identity/ultimate policy and bind subsequent operation.

### AgentCity — `proxy`

AgentCity includes operational agent legislation, but foundational contracts and key constitutional parameters remain human-authored/agent-immutable. The benchmarked legislation therefore remains below the ultimate foundational layer.

### Constitutional AI Governance Stress Test — `proxy`

`CognitiveThoughtEngine/cgst-framework@a70dd1ffd4b2c462a9c0680b6aa6d6b9ad788cdf` provides strong governance/conformance evidence, but does not itself execute an identity-level conflict through legitimate ratification and later operation under a changed policy.

## Important adjacent non-benchmark evidence

`Constitutional Governance in Metric Spaces` and Agent Parliament provide governance-process/amendment evidence but are not reusable harness benchmark families. HEM is a Parent-authority escalation protocol rather than a benchmark result. `constitutional-agent-governance` provides strong amendment/authority mechanism tests rather than a matched capability result. MAC performs constitution optimization without independently established legitimate ultimate organizational authority.

## Why enforcement is not enough

```text
policy already exists
        ↓
propagate / enforce / audit it
        ≠
choose legitimate ultimate policy
```

Likewise:

```text
agent chooses between values in a scenario
        ≠
organization legitimately changes its identity/policy
```

GovSim-SelfGovern differs because benchmark-defined authority actually ratifies and enacts a membership decision. Ouroboros differs because canonical legitimate parent authority actually enacts a constitutional/runtime authority change that persists into later operation.

## Canonical-system consequence

The evidence layers must remain separate:

```text
direct benchmark-defined S5 organization exists        yes — GovSim-SelfGovern
canonical native direct S5 observation exists           yes — Ouroboros, descriptive P path
matched multi-canonical S5 primary exists               no
```

Canonical ownership states remain repository-derived and heterogeneous (`A`, `P`, `A(P)`, `C(P)`, etc.). Neither GovSim nor the Ouroboros observation changes, weakens or ranks those states.

The companion `../s5-system-benchmarks/` layer owns current composed/canonical observations, coverage counts and the remaining matched-primary gap.
