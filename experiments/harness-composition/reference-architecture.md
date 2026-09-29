# Hypothetical composable harness organization

Status: **experimental / architecture hypothesis only**.

This note sketches what the OpenSiro harness-composition idea could look like if separate OSS projects are treated as function-specific organizational components rather than compared only as complete standalone products.

Nothing here is a claim of plug compatibility or a positive composed VSM assessment.

## Core idea

Keep the application harness replaceable while moving selected metasystem responsibilities into explicit surrounding components.

```text
                    legitimate parent authority
                    purpose / identity / limits
                              |
                              v
                  policy / authority boundary
                     OpenShell-like enforcement
                              |
                              v
        +---------------------------------------------+
        |          composed agent organization        |
        |                                             |
        |   S4 candidate          S3/S3* support      |
        |   A-Evolve              ACP / LH / reviewer |
        |        \                    /               |
        |         \                  /                |
        |          v                v                 |
        |        shared evidence / control state      |
        |                   |                         |
        |                   v                         |
        |          S2 coordination candidate          |
        |                 Grit                        |
        |                   |                         |
        |                   v                         |
        |          interchangeable S1 workers         |
        |       Codex / other application harness     |
        +---------------------------------------------+
                              |
                              v
                         environment
```

A compatibility layer such as HarnessRouter can sit between the organization and replaceable S1 harnesses when a stable lifecycle/API boundary is useful.

## Function-by-function interpretation

### S1 — interchangeable application harness

Seed: **Codex**.

The application harness owns the substantive task loop: interpret the task, choose actions/tools, consume feedback and produce the operational result.

The architectural hypothesis is that this layer should be replaceable without silently moving ownership of the surrounding organizational functions.

Possible later substitutes include other coding, browser, research or domain-specific harnesses from the Index.

### S2 — external coordination substrate

Seed: **Grit** for coding organizations.

Potential role:

- expose worker identity;
- reserve concrete shared work surfaces;
- attenuate competing edits/merges;
- return block/queue/release state into later worker admission.

This is domain-specific to shared code/repository work. A different domain would likely need a different S2 component.

### S3 — current-control / governance support

Seeds: **Agent Control Plane**, or integrated control mechanisms from systems such as Chump/Tandem used as references.

Potential responsibilities:

- current budgets and constraints;
- approval/intervention gates;
- risk accumulation;
- cancellation / kill-switch / recovery;
- current organizational state.

A deterministic control plane can enforce an S3 decision without necessarily owning the discretionary S3 judgment. The composed assessment must preserve that distinction.

### S3* — complementary audit

Potential seeds:

- LongHorizon-Harness role-separated Auditor structure;
- Harmonist reviewer protocol/gates;
- Agent Control Plane evaluator/check surfaces;
- a dedicated independent verifier if a cleaner component appears in the Index.

The audit path should not merely repeat the S1 report. A future implementation would need a genuinely complementary evidence path and a corrective return into operation/current control.

### S4 — future capability adaptation

Seed: **A-Evolve**.

This is currently the clearest hypothetical external adaptation layer because its native organization already maps operational evidence into persistent changes to an agent workspace that are reloaded for later operation.

The composition question is whether another harness can be exposed through that contract while preserving the external harness as the S1 owner.

### S5 — legitimate identity / policy authority

Do **not** assign S5 to a security/policy engine merely because it enforces policy.

For the first constructor hypothesis, keep ultimate purpose/identity authority explicit as a legitimate parent (for example the human/operator or another separately evidenced authority owner).

**OpenShell** is interesting here as the enforcement boundary around the operational agent:

```text
parent authority decides / approves policy
        -> OpenShell stores / validates / enforces boundary
        -> constrained operation
```

That can be excellent S5-supporting machinery without making OpenShell itself the ultimate S5 owner.

## Composition glue

### HarnessRouter

HarnessRouter is particularly interesting as a neutral interchange/lifecycle layer because its repository-relative boundary explicitly keeps the selected upstream harness as the autonomous task actor.

Hypothetical use:

```text
organization
    -> stable HarnessRouter lifecycle/API
        -> selected S1 harness
            Codex / OpenHands / OpenCode / ...
```

This would make replaceability visible as an architectural property rather than merely a claim.

### LongHorizon-Harness

LongHorizon-Harness is a different kind of wrapper: it keeps external agent CLIs as semantic actors while supplying durable rounds, checkpoints, Manager/Executor/Auditor role structure, audit gates and recovery.

That makes it a useful example of a metasystem-like wrapper whose repository-relative assessment can be excluded standalone while the wider composition remains highly agentic.

## Three constructor levels

### Level 1 — two-piece composition

```text
S1 harness + one missing organizational function
```

Examples:

- Codex + Grit
- Codex + OpenShell
- Codex + A-Evolve
- Codex + LongHorizon-Harness

Purpose: make one functional addition legible.

### Level 2 — replaceable worker organization

```text
parent authority
      |
policy/runtime boundary
      |
coordination
      |
HarnessRouter
      |
replaceable S1 harness
```

Purpose: demonstrate the OpenSiro thesis that implementations can change while the organizational boundary stays legible.

### Level 3 — explicit metasystem constructor

```text
S5 parent authority
    -> policy enforcement
    -> S3 / S3* control and audit
    -> S4 adaptation
    -> S2 coordination
    -> replaceable S1 population
```

Purpose: use the Index as a search space for function-specific OSS components and then assess the resulting organization as its own system-in-focus.

## What the current Index enables

The Index is useful here for more than finding a project with the largest number of positive cells.

It can expose:

1. **complete organizations** — broad integrated systems such as Tandem, KADATH, Chump or `gh-aw`;
2. **operational cores** — strong S1 harnesses with missing metasystem functions;
3. **specialized substrates** — projects excluded standalone but useful for coordination, policy, control, audit or lifecycle in a wider boundary;
4. **adaptation systems** — projects whose strongest differentiator is a real S4 loop;
5. **reference patterns** — integrated projects showing how a function closes when it is not externally composed.

This creates a different search question:

> Given a target organizational contour, which assessed OSS components plausibly supply the missing responsibilities, and what interface/authority boundaries would have to connect them?

That question is the current experiment. Execution and composed reassessment are deliberately deferred.
