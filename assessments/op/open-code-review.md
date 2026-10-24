---
harness_id: open-code-review
project_name: OpenCodeReview
repository: https://github.com/alibaba/open-code-review
review_ref: 7a571b78d3493b249f6ad14d835c6a79a0a67d2e
reviewed_at: 2026-09-18
generated_profile_version: 0.2.2
generated_assessment_procedure_version: 0.3.1
profile_version: 0.2.2
assessment_procedure_version: 0.3.1
assessment_changed_at: 2026-09-18
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# OpenCodeReview

## Review boundary

- System in focus: OpenCodeReview's first-party review CLI/runtime at pinned revision `7a571b78d3493b249f6ad14d835c6a79a0a67d2e`, including deterministic review orchestration and the OCR-managed tool-using LLM review agents.
- Purpose and identity: inspect code changes or full files and produce precise, context-aware review findings through a hybrid deterministic + agent architecture.
- Relevant environment: Git repositories/diffs, source files, review rules, model providers, CI/plugin hosts and human developers consuming findings.
- Standard-distribution boundary: OCR-managed review mode, bundled prompts/tools, file selection/bundling/rule matching and comment post-processing. Delegation mode using an external coding agent is a separate host path and is not used to inherit external-agent organization.
- First-party operating/deployment modes considered: workspace/range/commit review, full-file scan and OCR-managed LLM execution.
- Recursion level: one code-review organization. Per-file/group review subagents are work units inside the review operation, not automatically viable recursive systems.
- Reviewed revision: `7a571b78d3493b249f6ad14d835c6a79a0a67d2e`.
- Observation date: 2026-09-18.
- Generated/current Profile / Methodology: `0.2.2` / `0.3.1`.

## Repository architecture

OCR combines deterministic selection, file grouping, rule matching, line anchoring and scheduling with model-driven review agents. A subtask is one file group in diff review or one file in scan. The agent can read source/diff context, search the repository and emit structured `code_comment` calls. Comment processing is dispatched to a first-party worker pool for tracking/re-tracking, reflection and suggestion validation while the main tool-use loop continues.

The documentation describes positioning and reflection as independent modules that improve line/content accuracy, but the pinned implementation places reflection inside the ordinary asynchronous `code_comment` post-processing path. That is useful QA but, on the reviewed evidence, not enough to establish the complementary organizational access/feedback required for S3*.

## Primary evidence

- [`README.md`](https://github.com/alibaba/open-code-review/blob/7a571b78d3493b249f6ad14d835c6a79a0a67d2e/README.md) — hybrid architecture, isolated file-group subagents, deterministic constraints and reflection/positioning claims.
- [`pages/src/content/docs/en/tools.md`](https://github.com/alibaba/open-code-review/blob/7a571b78d3493b249f6ad14d835c6a79a0a67d2e/pages/src/content/docs/en/tools.md) — review-agent tool loop, read-only context tools, `code_comment` behaviour and ordinary asynchronous line-resolution/reflection path.
- [`internal/llmloop/pool.go`](https://github.com/alibaba/open-code-review/blob/7a571b78d3493b249f6ad14d835c6a79a0a67d2e/internal/llmloop/pool.go) — CommentWorkerPool as comment post-processing machinery for tracking, re-tracking, reflection and suggestion validation.

## Operational model

The primary operation is autonomous semantic code review. Deterministic machinery defines which source material is presented and how findings are anchored, while the LLM review agent decides which risks/issues are substantively reportable and retrieves additional context as needed. Multiple bundle agents divide the changeset, but isolation/concurrency is a scaling strategy rather than demonstrated regulation of mutual S1 interference.

## S1 — Operations

- State: `A`.
- Function: inspect assigned code/diff material and produce substantive review findings.
- Disturbance / variety regulated: language/framework variation, repository context, defect/risk ambiguity, cross-file evidence and changing source content.
- Decisive decision or feedback right: the review agent decides which potential issues warrant comments and which context/tools to use before finishing its subtask.
- Decision owner: model-driven OCR-managed review agent.
- Supporting / enforcement mechanisms: deterministic file selection, bundling, rules, tool registry, line anchoring and comment worker pool.
- Closure path: agent inspection/tool results change subsequent reasoning; accepted `code_comment` results become the delivered review output.
- Basis / confidence: explicit + structural; high.

## S2 — Coordination

- State: `—`.
- Multiple file-group subagents can run with isolated contexts and concurrency, but the pinned evidence does not establish a specific mutual interference/conflict/oscillation among operational S1 units plus a feedback relation that regulates it. Divide-and-conquer bundling and asynchronous scheduling alone are not S2.
- Confidence: high.

## S3 — Inside-and-now control

- State: `—`.
- Deterministic orchestration controls selection, grouping, rule application and scheduling, but no distinct autonomous actor has both a current whole-review view and discretionary authority over shared organizational resources, commitments or priorities. Pipeline control is not promoted to S3.
- Confidence: high.

## S3* — Complementary audit

- State: `—`.
- The reflection/positioning machinery is separate in implementation but runs as part of the ordinary `code_comment` production/post-processing path. The reviewed evidence does not reconstruct a sufficiently independent complementary access path that challenges normal operational reporting and returns findings to a distinct current-control owner.
- Put differently, “independent module” is not sufficient by itself: reflection here is routine quality processing of the review product, and no separate corrective organizational loop is established at this boundary.
- Confidence: medium-high.

## S4 — Outside-and-then intelligence

- State: `—`.
- Repository search, dynamic context retrieval and production-derived tool tuning improve review execution but do not form an external-and-prospective environmental intelligence loop with adaptation options returned into current organizational capability.
- Confidence: high.

## S5 — Policy and identity

- State: `—`.
- Review rules, configured models/providers and operator-selected execution modes constrain the product, but no runtime identity/ultimate-policy authority and return loop is established. Human consumption/disposition of review comments is outside the supplied harness governance path.
- Confidence: high.

## Recursion

Per-bundle subagents are bounded review work units. Isolation and parallel execution do not establish VSM recursion without independent viable-system evidence.

## Variety and escalation

OCR attenuates large-change variety through file selection, bundling and rule matching, while agent tools amplify context access. Failed anchoring can trigger re-location and comments may degrade to unpositioned output; these are production recovery paths rather than metasystem escalation states.

## Evidence gaps

The documentation's broad “independent reflection” description is recorded but not converted to S3* without stronger evidence of complementary access, independent judgment and corrective return beyond the routine comment-processing path.

## Admission conclusion

Canonical vector: `A — — — — —`.
