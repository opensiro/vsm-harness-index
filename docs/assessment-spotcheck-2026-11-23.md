# Five proposed assessments — source-boundary spot check (2026-11-23)

**Status:** review packet only; **not** an independent complete semantic adjudication, admission or reassessment event. Source: [Profile 0.2.4](https://github.com/opensiro/vsm-harness-profile/blob/v0.2.4/PROFILE.md) and [Skills Methodology v0.3.9](https://github.com/opensiro/vsm-harness-skills/releases/tag/v0.3.9). Read the frozen controller/issue and the source-pinned assessment before any transition.

## Contract compatibility

Index active contract advances **Profile 0.2.4 / Skills Methodology 0.3.8 → 0.3.9**. This is the released compatible S1 ownership calibration, not an assessment migration. It distinguishes developer configuration of an operational first-party autonomous actor from developer construction of the actor/authority/action–observation–next-action loop. In a challenged `S1=C` case, name the missing autonomous owner/decision/closure and a **function-specific** first-party constructor; neither automatic promotion of agent-in-workflow to `A` nor a downgrade merely for instantiation is warranted.

No historical `generated_profile_version`, `generated_assessment_procedure_version`, `review_ref`, `reviewed_at`, or current semantic `assessment_procedure_version` is edited. Advance a particular assessment's current version only upon a successful source-first revalidation, through its owning gate. No changes to S2–S5 thresholds, symbols, synthesis or ranking projection.

## Source-pinned proposed cases

| Harness / assessment | Frozen upstream `review_ref` | Recorded S1 S2 S3 S3* S4 S5 | Governed disposition |
| --- | --- | --- | --- |
| [aero](../assessments/ae/aero.md) | `b66c50df07b1fbe5915e398fb5e7e9807b3d23a3` | `A — — — — —` | [Index #987](https://github.com/opensiro/vsm-harness-index/issues/987), row 1 `NEXT`; plausible S1 autonomous tool/action/feedback path in `agent.py`, no new canonical action |
| [afc-runtime](../assessments/af/afc-runtime.md) | `204647311304ca0f40334a27ac3a152700144a4f` | `C — — — — —` | [Index #1780](https://github.com/opensiro/vsm-harness-index/issues/1780) **TERMINAL / not admitted**: source-specific queue/supervisor constructor lacks the externally configured model/agent decision owner; Index inclusion requires `S1=A`; do not alter state to force inclusion |
| [bb](../assessments/bb/bb.md) | `c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf` | `A A A A — —` | [Index #1300](https://github.com/opensiro/vsm-harness-index/issues/1300) row 1 `NEXT`; **existing [#1382](https://github.com/opensiro/vsm-harness-index/issues/1382)** owns S3* evidence dispute; no duplicate regrade |
| [deepsec](../assessments/de/deepsec.md) | `42ed66efd3fc039767312e1b3aa66db6e173c850` | `A C — A — —` | [Index #968](https://github.com/opensiro/vsm-harness-index/issues/968), row 1 review merged; admission pending controller gate; `S2=C` deserves function-specific constructor recheck before admission |
| [embabel](../assessments/em/embabel.md) | `45c70d4051f758034b213f1c730c64ec190dc6fe` | `A — — — — —` | [Index #973](https://github.com/opensiro/vsm-harness-index/issues/973), row 1 review merged; admission pending controller gate; shipped `Autonomy` and `LlmRanker` warrant source-first `S1=A` path verification under 0.3.9 |

All five records are still `status: proposed` in the inspected Index main state. Under [assessment lifecycle](assessment-lifecycle.md), no proposal belongs in canonical signatures, rankings or reassessment history. This spot check found their six S-function sections, positive boundary-reachability fields, negative absence scopes, and source-linked pinned blob URLs structurally present; it is **not** a successful run of the Methodology checker or independent runtime execution.

## Evidence and unresolved questions

### bb: S3* ownership — existing issue #1382

Original source: [first-party blog reviewer example](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/apps/web/src/blog/posts/building-a-restrained-software-factory.md), [CLI thread creation](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/plugins/bb-guide/skills/bb-cli/references/thread-creation.md), [child notifications](https://github.com/get-bb/bb/blob/c41e0bb485f8ec3fb5b002c1aa151cd66e531aaf/apps/server/src/services/threads/child-thread-notifications.ts). Shipped separate child and parent result-return paths exist. The documented use case is to **ask** an ordinary child coding thread to review the parent; it does not alone identify a first-party audit-specific complementary primary-evidence role or verify a corrective control path. This is exactly [Skills positive-evidence calibration R6](https://github.com/opensiro/vsm-harness-skills/blob/v0.3.9/skills/assess-vsm-harness/references/positive-evidence-calibration.md), marked unresolved, not a preapproved regrade.

**Acceptance question:** identify the supported first-party configuration, claim audited, reviewer-controlled primary evidence, independent judgment and findings-to-control closure. Conclude `NO_CHANGE_EVIDENCED`, `CORRECTION_REQUIRED`, or `INSUFFICIENT` **in #1382**, without treating a generic worker/second provider as automatic S3*. No canonical bb admission until the governing issue's review boundary is resolved.

### deepsec: S2=C versus deterministic collision prevention — controller #968

Original source: [processor](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/packages/processor/src/index.ts) and [architecture](https://github.com/vercel-labs/deepsec/blob/42ed66efd3fc039767312e1b3aa66db6e173c850/docs/architecture.md). The code documents two competing runs attempting to claim and overwrite the same FileRecord; `acquireProcessLock`, `lockedByRunId`, stale-lock reclaim and later release attenuate that concrete disturbance. But a deterministic lock is not by itself an autonomous S2 decision owner or necessarily an **S2-specific constructor of an autonomous coordination right**.

**Acceptance question:** identify distinct S1 units at the chosen recursion; the exact S2-specific constructed decision/feedback seam, missing autonomous owner and operational return to subsequent S1 behaviour. If only fixed exclusion is shown, do not infer `C` from concurrency alone. Do not change `S2=C` merely because it is questioned: route a separately evidenced disposition through #968's still-frozen row and gates.

### Other S1 compatibility spot checks

- **aero:** [`agent.py`](https://github.com/ronak-create/aero/blob/b66c50df07b1fbe5915e398fb5e7e9807b3d23a3/agent.py) exposes model-selected tool calls, execution/result messages and next iterations. A developer-supplied provider or approvals do not make the supported S1 constructor-only.
- **afc-runtime:** [supervisor](https://github.com/philngt/afc-runtime/blob/204647311304ca0f40334a27ac3a152700144a4f/wo_runtime/runtime/supervisor.py) is a specific headless-agent launch/receipt seam; task-specific model actor/policy are supplied by an external instance. `S1=C` still fits the 0.3.9 distinction at the reviewed boundary; **not eligible for canonical inclusion under existing S1=A gate**.
- **embabel:** [`Autonomy.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/api/common/autonomy/Autonomy.kt), [`LlmRanker.kt`](https://github.com/embabel/embabel-agent/blob/45c70d4051f758034b213f1c730c64ec190dc6fe/embabel-agent-api/src/main/kotlin/com/embabel/agent/spi/support/LlmRanker.kt) and supported supervisor execution provide a plausible first-party autonomous selection/execution loop; application-defined goals and model configuration alone must not downgrade `A` to `C`.

## Boundaries and acceptance

- This packet is **read-only evidence organization**, not a second independent reviewer, semantic revalidation, new freeze, revision repin, canonical admission/exclusion, or permission to jump a `NEXT` board.
- Structural source inspection is not provider-backed execution, whole-source coverage, validated independent agreement, or CI success.
- The contract switch changes only future active validation routing. CI's active-version structural checker will check v0.3.9 assessments only; existing older-version artifacts keep their recorded provenance. All deterministic metrics/views must reflect the new active contract.
- Revisit bb and deepsec only in their existing Index-owned controls; record outcome and actual next step there, not by editing the proposed vector in this cross-case report.
