---
harness_id: macher-agent
project_name: macher-agent
repository: https://github.com/elij/macher-agent
review_ref: f60786359a175d6c7f0c56ec3faeb74ae2bda22d
reviewed_at: 2026-10-27
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# macher-agent

## Review boundary

- System in focus: An installed macher-agent Emacs project workspace integrated with gptel and macher, including shipped programmatic tools, child contexts and optional first-party Zero-Mem module.
- Purpose and identity: Execute autonomous workspace tasks and return staged file/buffer changes to the user or calling agent.
- Relevant environment: Emacs buffers, project files, external gptel model backends, concurrent child tasks, rsync/git and user diff review.
- Standard-distribution boundary: An installed macher-agent Emacs project workspace integrated with gptel and macher, including shipped programmatic tools, child contexts and optional first-party Zero-Mem module.
- Credited operating / distribution surfaces: macher-agent install/gptel hooks, A2A orchestration, VFS synchronization and shipped skills/scripts tool definitions; the first-party Zero-Mem module when enabled.
- Adjacent first-party surfaces excluded from ownership: README example code and recall benchmark are corroboration, not a separately deployed coordinating, audit or strategic actor; upstream gptel/macher internals beyond the integration are dependency assumptions.
- First-party operating / deployment modes considered: Supported local self-hosted runtime and operator-supervised configuration; no custom external composition is credited.
- Recursion level: One runtime/project deployment; nested task agents are not presumed recursively viable.
- Reviewed revision: f60786359a175d6c7f0c56ec3faeb74ae2bda22d
- Observation date: 2026-10-27
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

The package installs gptel FSM/prompt/tool hooks and wraps macher tools with a persistent workspace context. Provider-backed agents operate in separate Emacs buffers, with buffer-local model/backend/preset settings. A2A callbacks route concurrent delegation, persistent specialists and submitted results; child VFS contexts are cloned and merged into the parent at submission. Ordered pipelines compose presets, transmission and artifact/merge handling. VFS tracks original/current text, synchronizes external changes, can invalidate stale staged edits, exposes path locks and callbacks, and presents patches for user application. Zero-Mem retrieves older conversation traces with graph/PageRank mechanisms. Skill loading, sandbox restrictions and tool scoping are developer/configuration constraints, not autonomous governance.

## Operational model

Agents select tools, delegate and decide task completion through the gptel integration. S2-specific concurrency machinery protects separate work contexts and feeds invalidated/current file state back to future calls, but coordinating discretion and full lock/merge policy still require developer composition. Basic child lifecycle ownership and result aggregation do not provide a whole-workspace resource/current-control regulator.

## S1 — Operations

- State: A
- Function: Autonomous workspace transformation
- Disturbance / variety regulated: Unknown source/buffer state and tool outcomes
- Decisive decision or feedback right: Choose tool calls, child tasks and final submit_task_result
- Decision owner: gptel model-backed parent or child agent
- Supporting / enforcement mechanisms: gptel transmission/FSM hooks, sandbox, VFS and A2A callbacks
- Closure path: Tool results re-enter the agent; submitted artifact/diff returns through the callback and parent-context merge
- Why this is / is not agent-owned: gptel model-backed parent or child agent; Dependent on configured gptel backend and macher; no model/Emacs runtime execution was performed.
- Evidence: [macher-agent-gptel.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-gptel.el) transmission and submit directives; [macher-agent-orchestration.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-orchestration.el); [skills/scripts/submit_task_result.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/skills/scripts/submit_task_result.el); [README.md](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/README.md) installation
- Basis: structural
- Confidence: high
- Caveats: Dependent on configured gptel backend and macher; no model/Emacs runtime execution was performed.
- Boundary reachability: macher-agent install/gptel hooks, A2A orchestration, VFS synchronization and shipped skills/scripts tool definitions; the first-party Zero-Mem module when enabled. The cited decision path is shipped in this mode and returns through gptel transmission/FSM hooks, sandbox, VFS and A2A callbacks.

## S2 — Coordination

- State: C
- Function: Attenuate concurrent workspace modification interference
- Disturbance / variety regulated: Sibling agents and outside edits can produce stale or conflicting file/buffer versions
- Decisive decision or feedback right: Expose isolated child contexts, per-path lock callbacks and stale-edit invalidation to a composed coordination owner
- Decision owner: First-party deterministic VFS primitives; developer must compose agent coordination authority/policy
- Supporting / enforcement mechanisms: VFS original/current entries, lock table/queues, semaphore tool and payload-merge pipeline
- Closure path: External modifications reset stale staged entries and warn to re-read/re-apply; resource notifications resume waiting calls with updated content; child results merge into later parent context
- Why this is / is not agent-owned: First-party deterministic VFS primitives; developer must compose agent coordination authority/policy; C is limited to this concrete concurrency-specific construction path, not generic A2A. The clean-merge verifier is a stub returning t (VFS lines 284–291), and parent merge writes child current text; no automatic semantic conflict resolution or autonomous coordinator is credited.
- Evidence: [macher-agent-vfs.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-vfs.el) lines 16–143, 513–623, 1109–1209; [skills/scripts/wait_for_vfs_semaphore.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/skills/scripts/wait_for_vfs_semaphore.el); [macher-agent-gptel.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-gptel.el) context synchronization
- Basis: structural
- Confidence: medium
- Caveats: C is limited to this concrete concurrency-specific construction path, not generic A2A. The clean-merge verifier is a stub returning t (VFS lines 284–291), and parent merge writes child current text; no automatic semantic conflict resolution or autonomous coordinator is credited.
- Boundary reachability: macher-agent install/gptel hooks, A2A orchestration, VFS synchronization and shipped skills/scripts tool definitions; the first-party Zero-Mem module when enabled. The cited decision path is shipped in this mode and returns through VFS original/current entries, lock table/queues, semaphore tool and payload-merge pipeline.
- Distinct S1 units: Concurrent task agents producing separate operational outcomes.
- Inter-S1 disturbance: Sibling agents and outside edits can produce stale or conflicting file/buffer versions
- Attenuating coordination relation: Expose isolated child contexts, per-path lock callbacks and stale-edit invalidation to a composed coordination owner
- Feedback into subsequent S1 behaviour: External modifications reset stale staged entries and warn to re-read/re-apply; resource notifications resume waiting calls with updated content; child results merge into later parent context
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: C is limited to this concrete concurrency-specific construction path, not generic A2A. The clean-merge verifier is a stub returning t (VFS lines 284–291), and parent merge writes child current text; no automatic semantic conflict resolution or autonomous coordinator is credited. Attenuate concurrent workspace modification interference

## S3 — Inside-and-now control

- State: —
- Function: No whole-workspace current-control function supplied
- Disturbance / variety regulated: Cross-unit resource/commitment decisions beyond basic task dispatch
- Decisive decision or feedback right: No shipped whole-team regulator with current view and discretionary intervention scope established
- Decision owner: No qualifying S3 owner established
- Supporting / enforcement mechanisms: A2A parent/child registries, preset/model settings, reaping and user patch review
- Closure path: Registries route results and collect child processes; diff acceptance changes artifacts without an evidenced whole-system resource/priority regulation loop
- Why this is / is not agent-owned: No qualifying S3 owner established; Neither parent-buffer identity nor user review alone establishes S3. A custom supervisor would require additional organization-specific composition.
- Evidence: [macher-agent-orchestration.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-orchestration.el) ownership registry/result aggregation; [macher-agent-gptel.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-gptel.el) reap/sweep functions; [macher-agent-api.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-api.el); [README.md](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/README.md)
- Basis: structural
- Confidence: medium
- Caveats: Neither parent-buffer identity nor user review alone establishes S3. A custom supervisor would require additional organization-specific composition.

### Absence scope

- Surfaces inspected: [macher-agent-orchestration.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-orchestration.el) ownership registry/result aggregation; [macher-agent-gptel.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-gptel.el) reap/sweep functions; [macher-agent-api.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-api.el); [README.md](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/README.md); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: A2A parent/child registries, preset/model settings, reaping and user patch review; autonomous and operator-governed alternatives were checked for no whole-workspace current-control function supplied.
- Why no material first-party path remains: Registries route results and collect child processes; diff acceptance changes artifacts without an evidenced whole-system resource/priority regulation loop Neither parent-buffer identity nor user review alone establishes S3. A custom supervisor would require additional organization-specific composition. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S3* — Complementary audit

- State: —
- Function: No complementary independent audit loop supplied
- Disturbance / variety regulated: Trustworthiness of action/completion claims
- Decisive decision or feedback right: No separate audit judgment with returned corrective control established
- Decision owner: None established
- Supporting / enforcement mechanisms: Context audit log, tool-intent logging, forced review and patch UI
- Closure path: Logs expose the same operational intents; diff review is routine artifact acceptance, with no separately controlled complementary audit decision path
- Why this is / is not agent-owned: None established; A tool named audit log does not create an independent auditor or a function-specific audit constructor.
- Evidence: [macher-agent-api.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-api.el) lines 162–205; [skills/scripts/read_context_audit_log.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/skills/scripts/read_context_audit_log.el); [macher-agent-gptel.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-gptel.el) pre-tool log hook; [macher-agent-vfs.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-vfs.el) review/flush
- Basis: structural
- Confidence: medium
- Caveats: A tool named audit log does not create an independent auditor or a function-specific audit constructor.

### Absence scope

- Surfaces inspected: [macher-agent-api.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-api.el) lines 162–205; [skills/scripts/read_context_audit_log.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/skills/scripts/read_context_audit_log.el); [macher-agent-gptel.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-gptel.el) pre-tool log hook; [macher-agent-vfs.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-vfs.el) review/flush; runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Context audit log, tool-intent logging, forced review and patch UI; autonomous and operator-governed alternatives were checked for no complementary independent audit loop supplied.
- Why no material first-party path remains: Logs expose the same operational intents; diff review is routine artifact acceptance, with no separately controlled complementary audit decision path A tool named audit log does not create an independent auditor or a function-specific audit constructor. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S4 — Outside-and-then intelligence

- State: —
- Function: No externally prospective adaptation loop supplied
- Disturbance / variety regulated: Future environmental/tool capability changes
- Decisive decision or feedback right: No environmental-futures to present-capability adaptation judgment established
- Decision owner: None established
- Supporting / enforcement mechanisms: Zero-Mem recall, skill/preset reload and configurable pipelines
- Closure path: Recall injects past conversation context and skill reload applies configuration; neither generates future-oriented adaptation options linked to present control
- Why this is / is not agent-owned: None established; Generic skills could implement research but no S4-specific first-party loop is shipped.
- Evidence: [macher-agent-zero-mem.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-zero-mem.el); [macher-agent-presets.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-presets.el); [README.md](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/README.md) memory and plugins
- Basis: structural
- Confidence: medium
- Caveats: Generic skills could implement research but no S4-specific first-party loop is shipped.

### Absence scope

- Surfaces inspected: [macher-agent-zero-mem.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-zero-mem.el); [macher-agent-presets.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-presets.el); [README.md](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/README.md) memory and plugins; runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Zero-Mem recall, skill/preset reload and configurable pipelines; autonomous and operator-governed alternatives were checked for no externally prospective adaptation loop supplied.
- Why no material first-party path remains: Recall injects past conversation context and skill reload applies configuration; neither generates future-oriented adaptation options linked to present control Generic skills could implement research but no S4-specific first-party loop is shipped. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## S5 — Policy and identity

- State: —
- Function: No identity/ultimate-policy closure supplied
- Disturbance / variety regulated: Identity or ultimate-policy dispute at workspace recursion
- Decisive decision or feedback right: No legitimate ultimate-authority issue/decision/return protocol established
- Decision owner: User/developer chooses presets and permissions; no qualifying S5 loop
- Supporting / enforcement mechanisms: Buffer-local prompts, sandbox AST validation, tool scope and diff approvals
- Closure path: These constrain execution and apply patches; no identity-level matter is routed to authority and returned as ultimate policy
- Why this is / is not agent-owned: User/developer chooses presets and permissions; no qualifying S5 loop; Operator configuration and ordinary approval were inspected as parent candidates; they do not alone establish S5.
- Evidence: [macher-agent-presets.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-presets.el); [macher-agent-sandbox.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-sandbox.el); [macher-agent-gptel.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-gptel.el) tool enforcement; [macher-agent-api.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-api.el)
- Basis: structural
- Confidence: medium
- Caveats: Operator configuration and ordinary approval were inspected as parent candidates; they do not alone establish S5.

### Absence scope

- Surfaces inspected: [macher-agent-presets.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-presets.el); [macher-agent-sandbox.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-sandbox.el); [macher-agent-gptel.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-gptel.el) tool enforcement; [macher-agent-api.el](https://github.com/elij/macher-agent/blob/f60786359a175d6c7f0c56ec3faeb74ae2bda22d/macher-agent-api.el); runtime entry, roles/tools, supported configuration and operating documentation within the declared boundary.
- Plausible first-party paths checked: Buffer-local prompts, sandbox AST validation, tool scope and diff approvals; autonomous and operator-governed alternatives were checked for no identity/ultimate-policy closure supplied.
- Why no material first-party path remains: These constrain execution and apply patches; no identity-level matter is routed to authority and returned as ultimate policy Operator configuration and ordinary approval were inspected as parent candidates; they do not alone establish S5. This is a bounded shipped-distribution conclusion, not impossibility of an extension.

## Distributed OSS parent arrangement

Public contributors and maintainers are outside this deployed-runtime recursion. Local operator decisions do not imply project-wide or organization-wide parent governance.

## Self-hosted and non-human modes

Self-hosted operation is the assessed mode; parent notation is used only for the explicitly established function-specific loop, if any. No intentionally non-human governing organization is supplied.

## Recursion

Agents, tasks and sessions may be nested, but this does not establish independent viable systems with their own complete metasystem.

## Variety and escalation

Emacs buffers, project files, external gptel model backends, concurrent child tasks, rsync/git and user diff review. Agents select tools, delegate and decide task completion through the gptel integration. S2-specific concurrency machinery protects separate work contexts and feeds invalidated/current file state back to future calls, but coordinating discretion and full lock/merge policy still require developer composition. Basic child lifecycle ownership and result aggregation do not provide a whole-workspace resource/current-control regulator.

## Evidence gaps

Static frozen-source review. Host lacks Emacs, so native byte compilation/ERT and gptel integration were not run; no live model execution or independent semantic review. The VFS clean-merge verifier is explicitly a stub and child merge semantics do not substantiate README's broad automatic-resolution claim. S2=C does not promise conflict-free concurrent execution.
