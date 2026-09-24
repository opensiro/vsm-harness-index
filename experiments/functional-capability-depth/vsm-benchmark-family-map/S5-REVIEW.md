# S5 benchmark semantic review

Status: experimental, non-normative.

Initial issue: #399  
Direct-family update: #472

This review maps public benchmark families against **S5 — Policy and identity** under the current `vsm-harness-profile`. It does not change canonical assessments or autonomy ownership.

## Current result

```text
reviewed direct S5 benchmark families: 1
first direct family: GovSim-SelfGovern
system linkage: benchmark-scaffolded
canonical native direct S5 observations: 0
matched canonical S5 primary: gap
```

The earlier zero-direct-family gap was valid for the public evidence reviewed through 2026-09-24. GovSim-SelfGovern (`arXiv:2609.22600v1`) now supplies a direct S5 witness at a **benchmark-defined society boundary**.

## Direct-S5 gate

A `direct` family must establish all of the following at its declared benchmark boundary:

1. a real mission, identity, ethos, constitutional-rule or ultimate-policy issue;
2. a lower-level tension that is not merely routine S1/S2/S3/S4 control;
3. a legitimate ultimate authority at that recursion level;
4. an actual decision, ratification, adjudication or amendment by that authority;
5. return of the newly decided policy into later operation;
6. evidence that separates policy ownership from enforcement of a pre-existing rule.

The authority may be autonomous, collective or Parent-governed. Direct S5 measurement does not require autonomous S5.

A matched primary has an additional requirement: two or more canonical native or adapter-preserved S5 paths must be compared under a materially matched benchmark/model/configuration cell.

## GovSim-SelfGovern — `direct`, benchmark-scaffolded

Primary source: https://arxiv.org/abs/2609.22600

GovSim-SelfGovern extends the five-agent fishing commons with executable law authorship. Agents propose Python laws over a constrained World API, receive sandbox validation, vote on valid proposals and execute enacted laws across rounds.

The direct S5 witness is specifically the **membership/identity path**:

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

The paper explicitly defines `agent.active = False` as exile. Valid proposals are voted on, majority-approved laws are executed, and expelled members are removed before subsequent round activity. In pooled results, non-thinking democratic agents enact 8 of 460 exile proposals (1.7%), while thinking agents enact 31 of 122 (25.4%).

This satisfies the S5 direct gate at the declared society recursion because legitimate current-member authority makes and enacts a membership decision that changes who belongs to the system and the changed membership persists into later operation.

The classification is nevertheless `benchmark-scaffolded`:

- the sandbox, voting procedure, game physics and API are benchmark-defined;
- the benchmark society, not an underlying model, owns the measured authority relation;
- no canonical Index harness is linked to this observation as a native or adapter-preserved S5 implementation;
- no authoritative public code repository/revision for GovSim-SelfGovern was recovered in this review.

Do not attach another GovSim repository merely by name similarity.

### Scope boundary

Not every enacted GovSim law is S5. Catch caps, penalties, taxation and treasury operations regulate current operation below the ultimate identity layer. They are not promoted to S5 merely because they are legislated.

Likewise, the paper's aggregate G1 governance gain (ICS 45.0% → 72.5%) combines mechanisms and is not an S5-only capability effect.

## Reviewed non-direct candidates

### AgentGovBench — `unsuitable`

Primary source: https://github.com/agentic-control-plane/agentgovbench

AgentGovBench exercises identity propagation, policy enforcement, delegation provenance, rate limits, audit completeness, tenant isolation and fail-mode behavior. Policy begins already decided, so it does not test legitimate ultimate-policy ownership or creation of a new policy decision.

### RoleCDE — `proxy`

Primary sources:

- https://arxiv.org/abs/2606.01552
- https://github.com/rabbitrose/RoleCDE

RoleCDE exposes conflicts between role-specific values and alignment constraints, but the evaluated model is not established as the legitimate ultimate authority of an organization and no adopted policy must govern later operation.

### Agent-ValueBench — `proxy`

Reviewed repository: `ValueByte-AI/Agent-ValueBench@3527b4a4ea8fc9dde6fbe27cd371c4ba7df76ac1`.

It provides executable value-conflict tasks, but measures expressed value choice rather than legitimate organizational authority to settle identity/ultimate policy and bind subsequent operation.

### AgentCity — `proxy`

AgentCity includes operational agent legislation, but foundational contracts and key constitutional parameters remain human-authored/agent-immutable. The benchmarked legislation therefore remains below the ultimate foundational layer.

### Constitutional AI Governance Stress Test — `proxy`

`CognitiveThoughtEngine/cgst-framework@a70dd1ffd4b2c462a9c0680b6aa6d6b9ad788cdf` provides strong governance/conformance evidence, but does not itself execute an identity-level conflict through legitimate ratification and later operation under a changed policy.

## Important adjacent non-benchmark evidence

`Constitutional Governance in Metric Spaces` defines an end-to-end governance/amendment process, and Agent Parliament publishes actual constitutional ratification/amendment history. These are useful S5-shaped governance-process evidence, but not reusable agent-harness capability benchmarks.

The Human Escalation Mechanism specifies a non-bypassable human decision path relevant to Parent-governed S5, but is a protocol rather than a benchmark result.

`constitutional-agent-governance` exercises proposer/ratifier separation, tiered authority and constitution mutation in first-party tests. That is strong mechanism/conformance evidence, not a matched capability benchmark.

MAC performs measurable constitution optimization, but task-reward optimization does not establish legitimate ultimate organizational authority.

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

GovSim-SelfGovern differs because the benchmark-defined authority actually ratifies and enacts a membership decision and later operation occurs after the boundary change.

## Canonical-system consequence

The direct-family hole is now closed, but the canonical-primary hole is not:

```text
direct benchmark-defined S5 organization exists
        !=
canonical native direct S5 observation exists
        !=
matched canonical S5 primary exists
```

Canonical ownership states remain repository-derived and heterogeneous (`A`, `P`, `A(P)`, `C(P)`, etc.). GovSim-SelfGovern does not change, weaken or reorder those states.

The companion `../s5-system-benchmarks/` layer stores the composed observation, current coverage and canonical native-path gap.
