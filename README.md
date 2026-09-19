# VSM Harness Index

VSM Harness Index is an evidence-backed corpus of real agent-harness assessments using the [VSM Harness Profile](https://github.com/opensiro/vsm-harness-profile/blob/main/PROFILE.md).

The repository separates three artifacts that were previously collapsed into one compact fingerprint:

```text
primary repository @ pinned revision
        ↓
assessments/<harness_id>.md
        ↓
        ├── ordered comparison → TLDR.md
        └── deterministic states → RANKINGS.md
```

`data/catalog.psv` is deliberately separate from those artifacts. It is the discovery/order/provenance registry and contains no VSM grades.

<!-- VSM INDEX METRICS:START -->
## Corpus snapshot

| Included | Catalog | Reassessments | Full-A |
| ---: | ---: | ---: | ---: |
| **138** | 139 | 80 | 0 |

**Next corpus milestone:** 138/250 (55.2%).

Active semantic contract: **Profile 0.2.3 / Methodology 0.3.5**.

[Full metrics](METRICS.md) · [Machine-readable metrics](data/metrics.json)
<!-- VSM INDEX METRICS:END -->

## Assessments

An assessment is the primary research artifact. It describes the reviewed GitHub repository, review boundary, operational model, evidence for each VSM function, evidence gaps, recursion/variety context, and the first-party ownership states `A/A(P)/C/C(P)/P/—/?`.

Assessments are **repository-relative**: adding another harness must not change an existing assessment unless its own reviewed evidence changes.

The VSM function definitions come only from [vsm-harness-profile](https://github.com/opensiro/vsm-harness-profile). The evidence/classification procedure comes from [`assess-vsm-harness`](https://github.com/opensiro/vsm-harness-skills/tree/main/skills/assess-vsm-harness).

## TLDR signatures

`TLDR.md` is a cohort-relative comparison view. Assessments are processed by ascending `catalog_position`. For each harness, `data/signatures.psv` records the smallest evidence-backed organizational distinction that is informative relative to all earlier completed assessments. Identical autonomy vectors are allowed; states are never changed merely to make signatures unique.

## Rankings

`RANKINGS.md` is a deterministic autonomy-coverage table derived from assessment states. It reports agent-owned functions, agent-owned metasystem functions, composable paths, supported parent-governed modes, and unknowns.

It is **not** a product-quality, maturity, or VSM-viability ranking. `C`, parent-mode presence, and `?` receive no fractional score.

For ranking, `A(P)` has base state `A` and counts exactly like `A`; `C(P)` has base state `C` and counts exactly like `C`. The `(P)` modifier is descriptive and never increases the ranking key.

## Autonomy / ownership states

The categorical states also have product-facing properties. These properties describe how a harness exposes a VSM function to an adopter; they are not additional scores.

| State | Property | Meaning |
| --- | --- | --- |
| `A` | **Autonomous** | Ready agent-owned enactment of the mapped VSM function. |
| `A(P)` | **Autonomous + Parent mode** | `A` is established and the same S3/S4/S5 function also has a distinct first-party parent-governed mode that is operationally closed. |
| `C` | **Constructor** | A first-party primitive specifically exposes the relevant decision/feedback path, but the autonomous role or closure loop still requires composition. |
| `C(P)` | **Constructor + Parent mode** | `C` is established and the same S3/S4/S5 function also has a distinct first-party parent-governed mode that is operationally closed. |
| `P` | **Parent-governed** | For S3/S4/S5, the function is operationally closed through legitimate parent authority, while no first-party `A` or `C` autonomous mode is established at the reviewed boundary. |
| `—` | **No-path** | No material first-party path is supplied inside the reviewed boundary. This is boundary-relative, not a claim that the function is impossible to add. |
| `?` | **Unknown** | Primary evidence is insufficient for a positive or defensible no-path conclusion. |

### Interpreting `A`, `C`, and parent modes

The states represent ownership arrangements and supported first-party modes, not a universal better/worse ordering.

- **Autonomous (`A`)** is useful when the adopter wants the VSM function to operate autonomously through a first-party mode.
- **Constructor (`C`)** is useful when the adopter wants to compose, replace, or specialize the responsible role themselves while retaining a first-party function-specific decision/feedback path.
- **Parent-governed (`P`)** records an operational mode where the decisive right for S3, S4, or S5 belongs to a legitimate parent human, institution, higher recursion, or evidenced distributed parent arrangement and returns to govern subsequent operation.
- **`A(P)` / `C(P)`** record that the harness supports both the base autonomous/constructor mode and a separately evidenced parent-governed mode for the same function.

`A(P)` and `C(P)` do **not** mean two actors simultaneously own one decisive right. They are multi-mode capability notation. A concrete deployment/run must still have one reconstructable owner for the relevant organizational decision at a time.

Accordingly, a self-hosted harness can legitimately expose operator-governed S3/S4/S5 modes without losing its autonomous mode. Conversely, a deliberately non-human organization such as a swarm can remain plain `A` for S3/S4/S5 when those functions close autonomously and no qualifying parent mode is established.

The `(P)` modifier is not earned by generic human involvement. A stop button, approval hook, merge review, configuration file, dashboard, or extension point does not establish a parent-governed VSM function by itself. The assessment must first establish the actual S3/S4/S5 function and then reconstruct the parent-owned decisive right plus the return/closure path.

This is also why the states must not be read as a maturity ladder such as `— < C < P < A`. `A(P)` is not better than `A`, and `C(P)` is not halfway between `C` and `A`; the modifier exposes an additional supported ownership configuration.

### Function-specific parent modes

For **S3**, a parent mode requires a whole-system current view and a parent-owned decision over resources, commitments, priorities, constraints, accountability, synergy, or intervention whose result changes subsequent current operation.

For **S4**, a parent mode requires an outside-and-then adaptation loop: external/prospective distinctions produce adaptation options, a parent owns the decisive adaptation judgment in that mode, and the result returns into current capability/S3.

For **S5**, a parent mode remains identity/ultimate-policy specific: the issue reaches legitimate parent authority, that authority decides, and the decision returns to govern subsequent operation. `S5=A(P)` is possible when the harness genuinely exposes both an internally agent-owned S5 closure mode and a distinct parent-governed S5 mode; those are alternative ownership configurations, not simultaneous ultimate authorities.

Methodology `0.3.0` deliberately does not apply `(P)` or standalone `P` to S2 or S3*.

### Harness properties and transformation

A **Constructor harness** is primarily an upstream base platform. It intentionally exposes one or more organizational functions as composable `C` paths so downstream users can build their own autonomous or parent-governed harnesses on top. The constructor provides first-party interfaces, feedback channels, decision points, state transitions, or control hooks needed to realize a function, while leaving the concrete role, policy, model, authority, or closure logic to the adopter.

An **Autonomous harness** is commonly a downstream specialization of that constructor surface. A team can fork or configure the constructor, choose concrete implementations for its open decision rights, and close selected `C` paths with ready agent-owned roles. When a constructor S3 interface receives a concrete autonomous regulator with the required whole-system view and authority, for example, that downstream harness may legitimately move from `S3=C` to `S3=A`.

A **Parent-governed mode** is another closure arrangement. A self-hosted or institutionally governed harness may wire an established S3, S4, or S5 path to an operator, maintainer arrangement, scientist, clinician, institution, regulator, or higher recursion. If the same standard distribution also retains an autonomous or constructor path, the resulting state may be `A(P)` or `C(P)` rather than replacing the base mode.

`No-path` and `Unknown` should not be treated as product strategies in the same sense. `No-path` records that the reviewed standard distribution does not materially expose the VSM function at that boundary; a fork may add Autonomous, Constructor, or qualifying parent-governed modes. `Unknown` records an evidence limitation and should be resolved by additional primary evidence rather than interpreted as either capability or absence.

The canonical relationship is therefore not a maturity chain but a set of ownership closures around an established function:

```text
Constructor (`C`)
        ↓ compose autonomous owner
Autonomous (`A`)

Constructor (`C`)
        + complete parent mode
        ↓
Constructor + Parent (`C(P)`)

Autonomous (`A`)
        + complete parent mode
        ↓
Autonomous + Parent (`A(P)`)

Parent-only first-party closure
        ↓
Parent-governed (`P`)
```

For example, a reusable constructor base may keep S1 as a working operational runtime while exposing metasystem functions as replaceable primitives:

```text
S1   A   operational runtime remains ready
S2   C   coordination / conflict-regulation interface
S3   C   regulator / budget / priority interface
S3*  C   independent audit-provider interface
S4   C   environment / prospective-intelligence interface
S5   C   policy / authority / escalation interface
```

A downstream self-hosted specialization might establish autonomous S3 while retaining a first-party operator mode, producing `S3=A(P)`. Another could leave the autonomous S4 role composable while shipping a complete operator-owned adaptation loop, producing `S4=C(P)`. A non-human specialization could instead close S3-S5 autonomously and remain plain `A` with no parent modifier.

These transformations never preserve assessment states automatically. Every fork, configured downstream harness, or materially different standard-distribution mode is assessed from evidence at the declared boundary. Methodology `0.3.0` allows one assessment state to record multiple first-party ownership modes only when both belong to the reviewed standard distribution and both are independently evidenced.

## Corrections and re-reviews

Assessment corrections are normal contributions. Open an `[Assessment re-review]` issue when stronger first-party evidence may change a mapping, or when a newer upstream revision materially changes the harness.

- **Same-ref correction:** re-evaluate the existing pinned commit; the catalog row does not change.
- **New-ref reassessment:** pin a newer commit; update the catalog `review_ref`/`pinned_at` only when the new assessment boundary is accepted.

The issue should identify the disputed VSM function, current interpretation, exact primary evidence, counter-evidence, and the reason re-review is needed. A proposed replacement grade is optional and is never authoritative. Contributors may claim the issue and submit the assessment change as a normal PR; final review should independently re-check the disputed function.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full acceptance contract.

## Contributing and organization

Use this repository for harness discovery/intake, evidence-backed assessments and reassessments, catalog/provenance maintenance, signatures, and generated Index views.

For questions or proposals about **the organization shared by Profile, Skills, Index, and Awesome** — contributor roles, authority boundaries, cross-repository control/coordination, escalation, milestone sequencing, or the shared contribution control plane — use [`opensiro/vsm-oss-organization`](https://github.com/opensiro/vsm-oss-organization). Canonical assessment facts and Index-local research work remain here.

## Continuous index

The historical ordered deep-review migration through catalog position 82 is complete. New candidates now follow the continuous lifecycle:

```text
discover → queue → pin → assess → admit → regenerate → validate
```

`data/catalog.psv` now contains only discovery/order/provenance fields. Historical compact `vsm_tldr` classifications were removed because they duplicated and could contradict the authoritative standalone assessments.

## Validation

```bash
python scripts/validate_tldr.py
python scripts/render_tldr.py
python scripts/render_metrics.py
python scripts/sync_metrics_readme.py
python scripts/check_index.py
```

`data/catalog.psv` remains the discovery/order registry; `assessments/` owns repository-relative findings; `data/signatures.psv` owns cohort-relative signatures; `TLDR.md` and `RANKINGS.md` are generated views.

## License

Repository code and original documentation are licensed under [Apache License 2.0](LICENSE). The adapted discovery dataset and generated comparative views retain the licensing described in [SOURCES.md](SOURCES.md). Linked projects retain their own terms.