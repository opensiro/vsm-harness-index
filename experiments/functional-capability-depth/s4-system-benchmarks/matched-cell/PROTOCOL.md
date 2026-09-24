# Matched canonical S4 preflight

Status: experimental, non-normative.

Tracking issue: #527.

## Question

Can two canonical systems exercise their **own** ordinary-S4 adaptation path under one materially matched evaluation membrane without replacing the organizational function being measured?

The first candidate pair is:

```text
a-evolve @ 18ba996dac9843f2759b2cdf8a94022f58fbfeb9  S4=A
exo      @ 6164288895a5851b2118492c880fb37b543e2ac6  S4=A(P)
```

The proposed first common target is persistent **skills** on a pinned SkillsBench task/evaluator surface.

This document freezes the admissibility rules for the preflight. It does not authorize execution and it does not promote an S4 primary baseline.

## Why `skills`

A-Evolve's pinned SkillsBench integration already treats persistent skills as a first-party evolvable layer. Its benchmark adapter loads a pinned public SkillsBench checkout and returns task/evaluator feedback to the native evolution loop.

Exo's pinned harness exposes `install_skill`, which writes durable agentskills.io-style skill artifacts. Those skills persist across conversations and sandbox rewinds and are loaded through the ordinary harness on later turns.

This supplies a plausible shared functional shape:

```text
external task / outcome evidence
        ↓
native S4 decision path
        ↓
persistent skill delta
        ↓
later operation consumes changed skill state
```

The equality required for a matched cell is at the evaluation membrane, not at the internal organizational topology. A-Evolve may retain a separated solver/evolver organization while Exo retains its own long-running-agent topology.

## Candidate benchmark membrane

The candidate task source is the public SkillsBench repository pinned by A-Evolve:

```text
benchflow-ai/skillsbench
828bb921fb94dc065bfefd6bac4e8938be3f71e0
```

A valid execution protocol would have to freeze before any result is inspected:

- exact task IDs and B0/A/H/R split membership;
- task order and random seeds;
- evaluator implementation and score mode;
- environment/container/tool surface;
- exact model provider, model revision/ID and inference settings;
- per-role token/call/time budgets;
- initial persistent state;
- allowed adaptation target;
- protected S4-regulator paths and their hashes.

The external membrane may supply tasks, environment observations, evaluator outcomes, budgets and stop conditions. It may not write the skills, choose their contents, substitute an external evolver, or otherwise make the adaptation decision for either system.

## Ordinary-S4 freeze boundary

Only persistent skill state may change.

### A-Evolve

The measured run may use the native evolver to change the declared skill workspace. The evolution algorithm, evolver prompt/template, benchmark adapter, solver implementation, provider configuration and other S4-regulator surfaces must remain frozen.

### Exo

The measured run may use native `install_skill` / skill-update behavior. It must not persist changes to core source, identity/policy prompts, model configuration, guardian/self-maintenance policy, benchmark/evaluator machinery, or the code that decides how adaptation is performed.

At minimum the protected Exo surfaces include:

```text
exo/harness.ts
exo/prompts/me.md
exo/tools/guardian-tools.ts
exoharness/typescript/model-runtime/
exoharness/typescript/harness/skill-tools.ts
```

A run that changes the S4 regulator itself belongs to the separate self-organizing-`S` evidence class and is invalid for this ordinary-S4 matched cell.

## Model/provider equality gate

A matched cell requires one exact underlying model/provider configuration wherever a model owns task-solving or S4 adaptation decisions.

Preferred equality form:

```text
A-Evolve solver model  = M
A-Evolve evolver model = M
Exo runtime model      = M
```

Different internal role topology is allowed. Different underlying model/provider cells are not.

### Current pinned-route finding

The built-in A-Evolve SkillsBench reference solver does **not** share the generic evolver provider surface:

- native execution constructs a Strands `Agent` backed by `BedrockModel(model_id=...)`;
- the Harbor route carries a separate Vertex-style model name;
- A-Evolve's generic evolver can use other providers, but that does not change the provider contract of the pinned SkillsBench reference solver.

Pinned Exo supports OpenAI/OpenRouter and native Anthropic model bindings, but its model runtime explicitly treats provider-prefixed Bedrock/Vertex Anthropic IDs as **not** native Anthropic IDs.

Therefore the built-in A-Evolve SkillsBench route and pinned Exo do not currently establish one exact common model/provider membrane.

This is a fail-closed blocker. Do not repair it by silently comparing different models or by rewriting either harness inside the measurement transaction.

## Current disposition

```text
candidate: A-Evolve × Exo / SkillsBench / skills-only
preflight: blocked
execution authorized: no
S4 primary baseline: gap
```

The blocker is specifically the exact common model/provider gate for the pinned built-in SkillsBench route. Other runtime gates are not promoted to pass merely because they look implementable; they remain `not_reached` until a provider-compatible route is established and reviewed.

A future attempt may reopen this cell if primary evidence establishes an adapter-preserved common model route. That must be a new preflight revision; it must not rewrite this negative finding retroactively.

## Why KADATH is not substituted

KADATH is already a canonical direct S4 observation, but its native Architect generates and locks the run benchmark from a user goal and explicitly forbids dependence on a user-authored benchmark file or script. Forcing an externally authored SkillsBench contract into that path would introduce a separate intervention whose adapter-preservation is not established.

KADATH therefore remains useful heterogeneous S4 evidence, not a shortcut around the matched-cell gate.

## Result vocabulary

The preflight uses only:

- `satisfied` — primary evidence closes the gate at the pinned revisions;
- `blocked` — primary evidence establishes an incompatibility that prevents execution;
- `not_reached` — the gate remains intentionally unevaluated because an earlier blocking gate prevents a valid execution surface.

`not_reached` must not be interpreted as pass or failure.

## Promotion rule

A matched S4 observation may be created only after every execution gate is `satisfied` and a separately frozen execution transaction produces results under that membrane.

A preflight artifact alone can never change:

```text
S4 primary baseline = gap
```

## Non-goals

This experiment does not:

- change canonical VSM ownership;
- change A-Evolve or Exo assessments;
- rank the two systems;
- derive a global S4 score;
- mix self-organizing-S evidence into ordinary S4;
- treat KADATH's heterogeneous native observation as matched evidence;
- modify catalog, signatures, TLDR, rankings, Full-A, Profile or Skills.
