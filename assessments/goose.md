---
harness_id: goose
project_name: Goose
repository: https://github.com/aaif-goose/goose
review_ref: 50666ae0b9a51e260b52b7efbab2e4e020346e94
reviewed_at: 2026-09-15
profile_version: 0.2.1
assessment_procedure_version: 0.3.1
last_checked_ref: d213a3b13545b4e85524a572ac695b2181728e3b
last_checked_at: 2026-09-17
assessment_changed_at: 2026-09-17
last_reassessment_round: R2
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Goose

## Review boundary
Same-ref correction of Goose at the accepted revision `50666ae0b9a51e260b52b7efbab2e4e020346e94`, with a freshness check through `d213a3b13545b4e85524a572ac695b2181728e3b`. The system-in-focus is the first-party Goose agent runtime including supported platform-extension modes. The decisive S3 evidence described below already exists at the accepted revision; later upstream preserves the same organizational path, so the accepted `review_ref` does not advance.

## Repository architecture
Goose is an autonomous tool-using agent harness whose core agent owns the model/tool turn loop, extension access, state and execution feedback. Subagent and session-fork paths provide operational decomposition. Separately, the first-party platform extension `orchestrator` exposes a model-visible cross-session control surface over independent top-level Goose sessions. The extension is hidden from extension discovery and disabled by default, but it is a registered first-party platform extension and can be enabled through Goose's normal extension configuration; no custom organizational actor or closure code is required once that supported mode is selected.

## Primary evidence
- `crates/goose/src/agents/agent.rs`: defines the operational Goose agent, provider/tool iteration, extension access, retries/compaction and agent configuration.
- `crates/goose/src/agents/platform_extensions/mod.rs` at the accepted ref registers the first-party `orchestrator` platform extension. It is `default_enabled: false` and `hidden: true`; those are availability/discovery defaults, not ownership evidence.
- `crates/goose/src/config/extensions.rs` plus session extension-state handling accept registered platform extensions as first-party enabled configuration, establishing that the orchestrator is a supported runtime mode rather than dead/example code.
- `crates/goose/src/agents/platform_extensions/orchestrator.rs` at the accepted ref exposes `list_sessions`, `view_session`, `start_agent`, `send_message`, and `interrupt_agent` directly to the model. `list_sessions` reports cross-session status; `start_agent` creates an independent top-level `SessionType::User` session; `send_message` instructs and executes another session; `interrupt_agent` cancels its current operation. Delegated `SubAgent` sessions cannot create new top-level sessions, while top-level sessions may control peer top-level sessions.
- The accepted-ref orchestrator authorization tests distinguish parent/peer session relationships, showing that these capabilities are deliberate first-party authority boundaries rather than generic MCP transport.
- The accepted-to-current upstream delta through `d213a3b13545b4e85524a572ac695b2181728e3b` changes orchestrator plumbing only materially enough for freshness, not the S3 function or ownership conclusion.

## Operational model
In the ordinary single-session path, a Goose agent receives a task, invokes the model, executes requested tools/extensions and continues from execution feedback. Subagents remain delegated operational work. In the supported orchestrator mode, the autonomous top-level Goose agent can inspect the current set of sessions and their status/conversations, create new independent top-level work sessions, change their current commitments by sending new instructions, and interrupt active work. The same model that observes the whole-session state chooses which of those control actions to invoke; the first-party runtime then closes the decision into subsequent session operation.

## S1 — Operations
`A`: the standard runtime autonomously selects and executes actions/tools within configured bounds and iterates from results. Confidence: high.

## S2 — Coordination
`—`: no first-party S2 witness was established. The orchestrator permits top-level cross-session messages and permits delegated subagents to message siblings with the same parent, but generic communication does not identify a specific inter-S1 interference, conflict or oscillation together with a relation that attenuates it and feeds the result back into later S1 behavior. Subagent/fork support remains delegation rather than sufficient S2 evidence.

## S3 — Inside-and-now control
`A`: the first-party orchestrator mode gives the autonomous top-level Goose agent a whole-system current view across sessions (`list_sessions` / `view_session`) and actual intervention authority over current commitments and operational capacity (`start_agent`, `send_message`, `interrupt_agent`). These tools are directly model-visible and their effects are closed by the runtime; once the supported mode is enabled, a developer does not need to compose a separate autonomous actor, S3 decision authority, or closure loop. `default_enabled: false` and `hidden: true` do not convert an otherwise closed agent-owned mode into `C`. The decisive evidence was already present at the accepted review ref, making this a same-ref correction rather than a new-ref architectural change. Confidence: high.

## S3* — Complementary audit
`—`: no alternative, sufficiently independent complementary audit path with materially different access to operational reality was established. Session viewing is part of the same S3 current-control surface, not a distinct audit relation.

## S4 — Outside-and-then intelligence
`—`: context management, retries and task reasoning concern current execution; no distinct externally and prospectively oriented intelligence loop that develops adaptation options and returns them into current capability was found.

## S5 — Policy and identity
`—`: system prompts, permissions, extensions and runtime configuration remain developer/user supplied rather than an autonomous legitimate identity/ultimate-policy decision path.

## Recursion, variety, escalation
Subagents and session forks increase operational variety but do not by themselves establish viable recursion. The orchestrator adds autonomous whole-system current regulation over multiple top-level sessions, establishing S3 at this boundary. No qualifying S2 interference-regulation relation, complementary S3* audit, S4 adaptation loop, or S5 identity/policy closure was established.