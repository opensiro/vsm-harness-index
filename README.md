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

| State | Meaning |
| --- | --- |
| `A` | Ready agent-owned enactment of the mapped VSM function. |
| `C` | A first-party primitive specifically exposes the relevant decision/feedback path, but the autonomous role or closure loop still requires composition. |
| `P` | Parent-assisted runtime closure; valid only for S5. |
| `—` | No material first-party path is supplied inside the reviewed boundary. |
| `?` | Primary evidence is insufficient for a positive or defensible no-path conclusion. |

### Interpreting `A`, `C`, and `P`

`A`, `C`, and `P` represent different ownership and product trade-offs, not a universal better/worse ordering.

- `A` is more useful when the adopter wants the VSM function to operate autonomously out of the box. This is often desirable in applied harnesses whose operational domain is already known and bounded, for example coding, research, chemistry, finance, or another domain-specific agent system.
- `C` can be more useful when the adopter wants to compose, replace, or specialize the responsible role themselves. This is often desirable in base, platform, or governance harnesses that expose a first-party decision/feedback path but deliberately leave the final autonomous role or closure loop to the application builder.
- `P` is specific to S5 and is useful when ultimate policy or identity authority is intentionally retained by a parent system, human, institution, or higher recursion level. The closure path already exists at runtime, but the final decision right remains outside agent ownership.

Accordingly, a harness with more `A` states is not necessarily a better platform, and a harness with more `C` or `P` states is not necessarily less capable. `A` measures ready agent-owned autonomy at the reviewed boundary; `C` measures a supported composition path for that function; `P` measures an operational S5 closure path whose final authority belongs to a parent. The preferred state depends on whether the system is intended to provide an opinionated autonomous organization, reusable organizational primitives, or explicit higher-level policy authority.

`P` is not a weaker form of `A`, and it is not equivalent to `C`. With `C`, the adopter still needs to compose the autonomous role or closure loop. With `P`, the closure loop is already operational: the harness can detect or escalate an identity-level issue, transfer it to the designated parent authority, receive the decision, and continue under that decision. What remains outside the harness is the ultimate S5 authority itself.

This distinction is especially important in high-stakes applied systems. A chemistry, healthcare, finance, or government harness may intentionally provide autonomous S1-S4 functions while keeping S5 closure with a scientist, clinician, institution, regulator, or other legitimate parent authority. In such a design, a vector ending in `P` may be preferable to one ending in `A` because preserving parent-owned policy and identity is an architectural requirement rather than an autonomy deficit.

This is also why the states should not be read as a maturity ladder such as `— < C < P < A`. They describe different ownership arrangements for an established VSM function or path: autonomous ownership (`A`), composable ownership (`C`), and, for S5 only, parent-owned closure (`P`).

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
