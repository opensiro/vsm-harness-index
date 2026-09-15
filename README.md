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

## Assessments

An assessment is the primary research artifact. It describes the reviewed GitHub repository, review boundary, operational model, evidence for each VSM function, evidence gaps, recursion/variety context, and the out-of-box autonomy states `A/C/P/—/?`.

Assessments are **repository-relative**: adding another harness must not change an existing assessment unless its own reviewed evidence changes.

The VSM function definitions come only from [vsm-harness-profile](https://github.com/opensiro/vsm-harness-profile). The evidence/classification procedure comes from [`assess-vsm-harness`](https://github.com/opensiro/vsm-skills/tree/main/skills/assess-vsm-harness).

## TLDR signatures

`TLDR.md` is a cohort-relative comparison view. Assessments are processed by ascending `catalog_position`. For each harness, `data/signatures.psv` records the smallest evidence-backed organizational distinction that is informative relative to all earlier completed assessments. Identical autonomy vectors are allowed; states are never changed merely to make signatures unique.

## Rankings

`RANKINGS.md` is a deterministic autonomy-coverage table derived from assessment states. It reports agent-owned functions, agent-owned metasystem functions, composable paths, parent-assisted closure, and unknowns.

It is **not** a product-quality, maturity, or VSM-viability ranking. `C`, `P`, and `?` receive no fractional score.

## Autonomy states

The categorical states also have product-facing properties. These properties describe how a harness exposes a VSM function to an adopter; they are not additional scores.

| State | Property | Meaning |
| --- | --- | --- |
| `A` | **Autonomous** | Ready agent-owned enactment of the mapped VSM function. |
| `C` | **Constructor** | A first-party primitive specifically exposes the relevant decision/feedback path, but the autonomous role or closure loop still requires composition. |
| `P` | **Parent-governed** | Parent-assisted runtime closure; valid only for S5. The closure path is operational, while ultimate authority remains with a parent system, human, institution, or higher recursion level. |
| `—` | **No-path** | No material first-party path is supplied inside the reviewed boundary. This is boundary-relative, not a claim that the function is impossible to add. |
| `?` | **Unknown** | Primary evidence is insufficient for a positive or defensible no-path conclusion. |

### Interpreting `A`, `C`, and `P`

`A`, `C`, and `P` represent different ownership and product trade-offs, not a universal better/worse ordering.

- **Autonomous (`A`)** is more useful when the adopter wants the VSM function to operate autonomously out of the box. This is often desirable in applied harnesses whose operational domain is already known and bounded, for example coding, research, chemistry, finance, or another domain-specific agent system.
- **Constructor (`C`)** can be more useful when the adopter wants to compose, replace, or specialize the responsible role themselves. This is often desirable in base, platform, or governance harnesses that expose a first-party decision/feedback path but deliberately leave the final autonomous role or closure loop to the application builder.
- **Parent-governed (`P`)** is specific to S5 and is useful when ultimate policy or identity authority is intentionally retained by a parent system, human, institution, or higher recursion level. The closure path already exists at runtime, but the final decision right remains outside agent ownership.

Accordingly, a harness with more `A` states is not necessarily a better platform, and a harness with more `C` or `P` states is not necessarily less capable. `A` measures ready agent-owned autonomy at the reviewed boundary; `C` measures a supported composition path for that function; `P` measures an operational S5 closure path whose final authority belongs to a parent. The preferred state depends on whether the system is intended to provide an opinionated autonomous organization, reusable organizational primitives, or explicit higher-level policy authority.

`P` is not a weaker form of `A`, and it is not equivalent to `C`. With `C`, the adopter still needs to compose the autonomous role or closure loop. With `P`, the closure loop is already operational: the harness can detect or escalate an identity-level issue, transfer it to the designated parent authority, receive the decision, and continue under that decision. What remains outside the harness is the ultimate S5 authority itself.

This distinction is especially important in high-stakes applied systems. A chemistry, healthcare, finance, or government harness may intentionally provide autonomous S1-S4 functions while keeping S5 closure with a scientist, clinician, institution, regulator, or other legitimate parent authority. In such a design, a vector ending in `P` may be preferable to one ending in `A` because preserving parent-owned policy and identity is an architectural requirement rather than an autonomy deficit.

This is also why the states should not be read as a maturity ladder such as `— < C < P < A`. They describe different ownership arrangements for an established VSM function or path: autonomous ownership (`A`), composable ownership (`C`), and, for S5 only, parent-owned closure (`P`). `—` and `?` are different cases: respectively no material first-party path inside the reviewed boundary, and insufficient evidence to classify that path.

### Harness properties and transformation

The properties can also describe how a harness is intentionally shaped for reuse.

A **Constructor harness** is primarily an upstream base platform. It intentionally exposes one or more organizational functions as composable `C` paths so downstream users can build their own autonomous or parent-governed harnesses on top. The constructor provides first-party interfaces, feedback channels, decision points, state transitions, or control hooks needed to realize a function, while leaving the concrete role, policy, model, authority, or closure logic to the adopter. In this sense, `C` is not an incomplete `A`; it can be the desired product surface of the base harness itself.

An **Autonomous harness** is commonly a downstream specialization of that constructor surface. A team can fork or configure the constructor, choose concrete implementations for its open decision rights, and close selected `C` paths with ready agent-owned roles. When a constructor S3 interface receives a concrete autonomous regulator with the required whole-system view and authority, for example, that downstream harness may legitimately move from `S3=C` to `S3=A`.

A **Parent-governed harness** is another downstream closure choice, specific to S5. Instead of replacing the constructor S5 path with an autonomous ultimate authority, the derived harness can wire that path to a scientist, clinician, institution, regulator, human operator, or higher recursion level. The resulting S5 may become `P`: the escalation and return path is operational, but legitimate ultimate authority remains outside the agent-owned boundary.

`No-path` and `Unknown` should not be treated as product strategies in the same sense. `No-path` records that the reviewed standard distribution does not materially expose the VSM function at that boundary; a fork may add either an Autonomous, Constructor, or, for S5, Parent-governed path. `Unknown` records an evidence limitation and should be resolved by additional primary evidence rather than interpreted as either capability or absence.

The canonical relationship is therefore constructor-first:

```text
Constructor / base harness
        ↓ fork or configure for a concrete domain and organization
Applied / domain-specific harness
        ↓ close each `C` composition point with a concrete owner
Autonomous (`A`) and/or Parent-governed (`P`) harness
        ↓ deploy
Operational system
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

Different users can fork the same constructor base and close those paths differently. A chemistry fork might implement autonomous chemistry-aware S2-S4 roles and connect S5 to a scientist or institution, producing something like `A A A A A P` if the evidence supports each function. A software-engineering fork could use different agents, tools, policies, and authority while inheriting the same constructor contracts. The value of the constructor is therefore that it standardizes where organizational decision rights and feedback paths exist without prescribing every downstream owner.

The intended direction is thus usually:

```text
Constructor (`C`)
        ↓ specialization
Autonomous (`A`) or Parent-governed (`P`)
```

not `A → C`. It is still possible to refactor an existing autonomous harness into a constructor by extracting a fixed role behind a stable interface, but that is a reverse-engineering path for creating a reusable base, not the defining lifecycle of a Constructor harness.

These transformations never preserve assessment states automatically. Every fork or configured downstream harness is a separate system-in-focus and must be assessed from its own reviewed evidence. Specializing a constructor path into a ready autonomous role can change `C` to `A`; wiring S5 to an actual parent authority can change `C` to `P`; extracting a fixed autonomous role into a reusable extension point can change `A` to `C`. These transitions describe changes in ownership and closure, not a monotonic maturity progression.

## Corrections and re-reviews

Assessment corrections are normal contributions. Open an `[Assessment re-review]` issue when stronger first-party evidence may change a mapping, or when a newer upstream revision materially changes the harness.

- **Same-ref correction:** re-evaluate the existing pinned commit; the catalog row does not change.
- **New-ref reassessment:** pin a newer commit; update the catalog `review_ref`/`pinned_at` only when the new assessment boundary is accepted.

The issue should identify the disputed VSM function, current interpretation, exact primary evidence, counter-evidence, and the reason re-review is needed. A proposed replacement grade is optional and is never authoritative. Contributors may claim the issue and submit the assessment change as a normal PR; final review should independently re-check the disputed function.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full acceptance contract.

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
python scripts/check_index.py
```

`data/catalog.psv` remains the discovery/order registry; `assessments/` owns repository-relative findings; `data/signatures.psv` owns cohort-relative signatures; `TLDR.md` and `RANKINGS.md` are generated views.

## License

Repository code and original documentation are licensed under [Apache License 2.0](LICENSE). The adapted discovery dataset and generated comparative views retain the licensing described in [SOURCES.md](SOURCES.md). Linked projects retain their own terms.
