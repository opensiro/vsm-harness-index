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

An **Autonomous harness** fixes one or more organizational roles as ready agent-owned behavior. This is valuable when the domain is sufficiently known that the harness can make useful decisions without requiring the adopter to design those roles first. Applied systems often move in this direction because the expected environment, tools, risks, and decision rights are narrower and can be encoded directly.

A **Constructor harness** intentionally exposes one or more organizational functions as composable `C` paths rather than fixing their autonomous implementation. The harness provides the first-party interfaces, feedback channels, decision points, state transitions, or control hooks needed to realize the function, while allowing the adopter to supply the actual role, policy, model, authority, or closure logic. In this sense, `C` is not an incomplete `A`; it can be the desired product surface for a reusable base harness.

A fork of an autonomous or applied harness may therefore deliberately move selected functions from `A` to `C`. For example, an upstream harness may ship an autonomous S3 regulator, while a constructor-oriented fork replaces that fixed regulator with a stable regulation interface and explicit resource, priority, exception, and feedback contracts. The resulting autonomy score may decrease, but the fork can become more useful as a platform because the adopter gains control over who owns the decision right and how the function is implemented.

A **Parent-governed harness** keeps S5 closure operational while locating ultimate identity or policy authority outside the agent-owned boundary. This is useful when the system should autonomously detect, escalate, suspend, resume, or apply policy decisions but must not itself become the legitimate source of those decisions. Parent governance is therefore a deliberate ownership design, especially in regulated or high-stakes deployments, rather than merely a fallback for missing autonomy.

`No-path` and `Unknown` should not be treated as product strategies in the same sense. `No-path` records that the reviewed standard distribution does not materially expose the VSM function at that boundary; a fork may add either an Autonomous, Constructor, or, for S5, Parent-governed path. `Unknown` records an evidence limitation and should be resolved by additional primary evidence rather than interpreted as either capability or absence.

A common transformation path is therefore:

```text
Applied / autonomous harness
        ↓ decompose selected decision rights
Constructor fork
        ↓ specialize roles, policies, models, and authority
Domain-specific harness
        ↓ close each function according to deployment needs
Autonomous (`A`) and/or Parent-governed (`P`) deployment
```

For example, a constructor-oriented base may keep S1 as a working operational runtime while exposing metasystem functions as replaceable primitives:

```text
S1   A   operational runtime remains ready
S2   C   coordination / conflict-regulation interface
S3   C   regulator / budget / priority interface
S3*  C   independent audit-provider interface
S4   C   environment / prospective-intelligence interface
S5   C   policy / authority / escalation interface
```

An adopter can then specialize those constructor paths into a domain-specific organization. A chemistry deployment might close S2-S4 with autonomous domain roles while closing S5 through a scientist or institution, producing an `A/P`-oriented applied system from the same reusable constructor base.

This transformation does not preserve assessment states automatically. A fork is a separate system-in-focus and must be assessed from its own reviewed evidence. Turning an upstream autonomous role into an extension point can legitimately change a state from `A` to `C`; specializing a constructor path into a ready autonomous role can change `C` to `A`; wiring S5 to an actual parent authority can change `C` to `P`. These transitions describe changes in ownership and closure, not a monotonic maturity progression.

## Migration

The discovery cohort remains in `data/catalog.psv`. The legacy `vsm_tldr` column is retained temporarily as migration history but is no longer authoritative for v2. Standalone assessments are rebuilt from pinned primary evidence in ascending catalog order. The validator requires completed assessments to form a contiguous prefix `1..N`.

The v2 migration currently covers positions `1..3` (Rasa, Botpress, n8n). The generated TLDR and rankings intentionally include only completed assessments.

## Validation

```bash
python scripts/validate_tldr.py
python scripts/render_tldr.py
python scripts/check_index.py
```

`data/catalog.psv` remains the discovery/order registry; `assessments/` owns repository-relative findings; `data/signatures.psv` owns cohort-relative signatures; `TLDR.md` and `RANKINGS.md` are generated views.

## License

Repository code and original documentation are licensed under [Apache License 2.0](LICENSE). The adapted discovery dataset and generated comparative views retain the licensing described in [SOURCES.md](SOURCES.md). Linked projects retain their own terms.
