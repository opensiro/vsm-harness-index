---
harness_id: continue
project_name: Continue
repository: https://github.com/continuedev/continue
review_ref: 5522c6f44ca0ac3528b37244818fbfa39b5af470
reviewed_at: 2026-09-15
status: included
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: 5522c6f44ca0ac3528b37244818fbfa39b5af470
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-15
last_reassessment_round: R2
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Continue

## Review boundary
Continue at the pinned revision as the coding-agent implementation delivered through CLI/VS Code/JetBrains surfaces, including the CLI streaming/tool loop and permission service. Client packaging is support infrastructure rather than a separate organizational layer.

## Repository architecture
The CLI runs a model/tool loop over workspace context and records tool-call state/results. `ToolPermissionService` compiles user, agent-file, mode and runtime policies into allow/ask/exclude decisions. Plan/auto/normal modes change constraints but remain runtime/configuration controls around the same coding operation.

## Primary evidence
- `extensions/cli/src/stream/streamChatResponse.ts`: iterative model response/tool-result path.
- `extensions/cli/src/stream/handleToolCalls.ts`: preprocesses and executes model-selected tools, records results, enforces permission checks and stops headless execution on rejected calls.
- `extensions/cli/src/services/ToolPermissionService.ts`: centralizes tool permissions from agent files, plan/auto mode, command-line and personal settings.

## Operational model
The coding loop is one S1. Permission modes attenuate its action variety while IDE/CLI services supply state and channels; no separate agent-owned organizational regulator is introduced.

## S1 — Operations
`A`: the coding agent autonomously selects tools and iterates on workspace results inside configured permissions. Confidence: high.

## S2 — Coordination
`—`: no first-party mechanism regulates interference among multiple S1 units. Tool dispatch and client/service coordination are not S2. Confidence: high.

## S3 — Inside-and-now control
`—`: permission compilation and mode switching constrain one S1 and are runtime/user owned; no agent has a whole-system current view plus authority over shared resources or commitments. Confidence: high.

## S3* — Complementary audit
`—`: preprocessing, history state and permission checks stay on the normal execution path and do not provide materially independent access to operational reality. Confidence: high.

## S4 — Outside-and-then intelligence
`—`: workspace/context updates inform the current task, but no distinct external-and-prospective adaptation loop coupled to S3 is supplied. Confidence: high.

## S5 — Policy and identity
`—`: plan/auto policies, agent files, personal settings and CLI overrides are parent/user-authored constraints rather than agent-owned ultimate policy/identity closure. Confidence: high.

## Recursion, variety, escalation
IDE and CLI surfaces wrap the same operational agent. Permission precedence and tool filtering attenuate action variety without creating recursive viable systems.

## Deep-review result
`S3`, `S3*`, `S4` and `S5` resolve from `?` to `—`; `S1 A` and `S2 —` are confirmed by runtime and policy implementation.