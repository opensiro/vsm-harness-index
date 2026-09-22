---
harness_id: atlias
project_name: atlias
repository: https://github.com/ridelink0/atlias
review_ref: 270eb980b32bc05278183aaf10af85ef35de2bc3
reviewed_at: 2026-09-23
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-09-23
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: C
autonomy_s4: —
autonomy_s5: —
---

# atlias

## Review boundary

- System in focus: one first-party atlias installation at pinned revision `270eb980b32bc05278183aaf10af85ef35de2bc3`, including the standalone `atlias agent` path and the shipped cross-host hook/MCP machinery: local-model tool loop, routing/brief/guard/gate/progress/Dream services, shared memory, graph access and host integration surfaces.
- Purpose and identity: augment supported coding-agent hosts with durable context, guards, verification and memory, while also providing a directly executable terminal-agent mode whose local Ollama engine is driven by atlias's own model/tool loop.
- Relevant environment: human user; project workspace and Git state; Claude Code, Codex, Antigravity, Gemini CLI and other external hosts; optional local Ollama model; graphify companion; shell/tool results; shared memory files; session transcripts; host hook events.
- Standard-distribution boundary: repository-shipped CLI, hooks, MCP server/tools and `lib/*` runtime. External host harness reasoning/model-tool loops remain separate and are not inherited. In standalone Ollama mode the atlias-owned tool loop is inside the first-party boundary; Claude/Codex engine modes still invoke external host runtimes.
- Credited operating / distribution surfaces: `README.md`; `bin/atlias.mjs`; `hooks/hooks.json`; `lib/agent.mjs`; `lib/gate.mjs`; `lib/guard.mjs`; `lib/hooks.mjs`; `lib/dream.mjs`; `lib/progress.mjs`; `lib/graph.mjs`; `mcp/tools.mjs`; `skills/double-check/SKILL.md`.
- Adjacent first-party surfaces excluded from ownership: repository CI/release/contributor governance; tests except as corroboration; generated `graphify-out/` reports/artifacts; external host internals; graphify's own implementation; upstream nanobot design/history.
- First-party operating / deployment modes considered: cross-host sub-harness mode through registered hooks/MCP; standalone `atlias agent` with Claude, Codex or Ollama engine; specifically the first-party Ollama model/tool loop; interactive human confirmation for destructive shell/out-of-project writes; Dream session-end consolidation; Stop verification gate.
- Recursion level: one atlias-supported agent session is the operational system-in-focus. Tool calls, hooks, memory entries, graph queries and Dream workers are subordinate mechanisms. Multiple installed host sessions are not silently aggregated into a higher-recursion organization merely because they share memory.
- Reviewed revision: `270eb980b32bc05278183aaf10af85ef35de2bc3`.
- Observation date: 2026-09-23.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.6`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.6`.

## Repository architecture

atlias has two standard-distribution roles. In sub-harness mode it installs first-party hooks and an MCP server into supported external agent hosts. Those paths inject a deterministic session brief and graph answers, guard repeated/destructive tool use, record edits/checks, preserve a handoff note across compaction, run a Stop verification gate and distil ended sessions into shared memory candidates. The host's own model/tool loop remains external.

In standalone `atlias agent` mode, the same guard/gate/graph/progress/Dream machinery wraps one of several engines. Claude and Codex are invoked as external CLI engines. The Ollama mode is materially different: `lib/agent.mjs` constructs an atlias-specific system prompt, sends model turns, parses `atlias` tool-call blocks, executes first-party read/write/list/grep/shell/recall/remember/graph tools, returns results into the model context and repeats up to a configured tool-round limit. This is a first-party operational agent loop rather than only an integration layer.

The verification gate observes actual changed files from atlias edit events plus Git status for shell-made changes. Before a reply ends it independently syntax-checks supported code and can block completion with concrete parser errors. It can also require a second adversarial pass when code changed and the reply has not evidenced one. In standalone mode a block reason is fed into another model turn; in host mode the shipped Stop hook returns the block to the host. This is a complementary verification path, but its audit ownership is mixed: syntax judgment is deterministic, while the adversarial re-read is performed by the same operational model rather than a materially independent autonomous reviewer.

Dream is durable internal consolidation. A detached SessionEnd worker records prompts/files/checks/tool usage into append-only history and produces a digest; at a later natural pause the model selects durable facts and writes them through `harness_remember`. This improves continuity but does not supply an outside-and-future sensing/adaptation loop.

## Operational model

A standalone Ollama session receives user input, optionally augments it through graph routing, and sends it to a local model with atlias's tool protocol. The model chooses task-level reasoning and tool calls. atlias executes those calls and returns results, including guard refusals and syntax outcomes, into later turns. When the model attempts to finish after code changes, `gate.stop` independently inspects the changed state and may force a corrective turn before completion.

In sub-harness mode, the same supporting machinery is attached to external host lifecycle events. atlias can regulate or enrich those hosts, but does not acquire ownership of their internal S1/S2/S3-S5 functions. Shared memory across hosts is common state, not evidence that the hosts form sibling S1 units under an atlias metasystem.

## S1 — Operations

- State: A
- Function: perform a user's coding/task objective through an autonomous model-driven tool loop, reading and modifying project state, running shell/check commands, consulting durable memory/graph context and continuing from tool feedback.
- Disturbance / variety regulated: uncertain task requirements, project/file state, shell and parser outcomes, missing context, repeated tool-call loops, destructive actions, graph/memory results and user confirmations.
- Decisive decision or feedback right: choose the substantive next reasoning/action and which first-party tool to invoke in response to the user goal and returned tool evidence.
- Decision owner: the autonomous model actor in the standard standalone agent relation; most clearly the local Ollama model driven by atlias's own first-party loop.
- Supporting / enforcement mechanisms: system prompt/tool protocol, guard threshold, destructive-action confirmation, project-boundary write guard, tool-round limit, syntax floor, graph routing, recall/remember, progress note and Dream persistence.
- Closure path: user prompt → atlias model request → autonomous model selects tool/action → atlias executes tool → result/guard evidence returns into model context → later model action/reply → gate may return corrective evidence → operation continues until a plain-text completion is accepted.
- Boundary reachability: `README.md` exposes `atlias agent` as a normal mode and `lib/agent.mjs` implements the local Ollama model/tool loop directly, including first-party tools and repeated result-return turns.
- Why this is / is not agent-owned: deterministic runtime machinery executes and constrains actions, but the model owns the goal-directed choice among possible actions. Removing the model leaves tools/guards/storage but no substantive task solution loop.
- Evidence: [`README.md`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/README.md); [`lib/agent.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/lib/agent.mjs); [`mcp/tools.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/mcp/tools.mjs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: Claude/Codex/Gemini host internals are not inherited. The positive state is independently established by the standard standalone local-model path.

## S2 — Coordination

- State: —
- Function: no installation-level mutual-adjustment function among distinct sibling S1 units is established at the reviewed boundary.
- Disturbance / variety regulated: atlias shares memory/history and can observe `SubagentStop`, while multiple hosts can use the same memory; however, the inspected standard paths do not define those host sessions as sibling S1 units under one atlias organization or regulate a concrete interaction-generated conflict/oscillation among them.
- Decisive decision or feedback right: not established for an S2-specific relation.
- Decision owner: not established.
- Supporting / enforcement mechanisms: shared memory, append-only history, graph state, handoff notes, locks around Dream housekeeping and loop guards provide common context/state safety without independently satisfying S2.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no qualifying S2 path was found in the shipped modes.
- Why this is / is not agent-owned: no S2 function is established, so no S2-specific ownership state is classified.
- Evidence: [`README.md`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/README.md); [`lib/dream.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/lib/dream.mjs); [`mcp/tools.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/mcp/tools.mjs).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: a downstream organization can use shared memory as part of S2, but that would be a separate system-in-focus requiring an actual disturbance/attenuation witness.

### Absence scope

- Surfaces inspected: standalone agent loop; host integration; shared memory/recall; Dream history/digest; graph state; `SubagentStop`; loop guard; progress/handoff; host installer topology.
- Plausible first-party paths checked: multiple supported hosts sharing memory; concurrent sessions ending into Dream; subagent-stop tracking; shared graph; handoff notes; repeated tool-call attenuation.
- Why no material first-party path remains: repeated tool-call control regulates one S1's own action loop, while cross-host/shared-memory paths exchange state without establishing distinct sibling S1 interaction disturbance plus S2-specific adjustment fed back into those siblings.

## S3 — Inside-and-now control

- State: —
- Function: no distinct metasystemic whole-system current-control function is established above the single operational agent session.
- Disturbance / variety regulated: guards can block destructive or repeated actions, the gate can hold completion, and status/progress tools expose harness state, but these paths regulate local execution quality/safety rather than shared current resources, commitments, priorities, accountability or synergy across multiple S1 operations.
- Decisive decision or feedback right: no whole-system current-control discretion at the declared recursion is established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: loop threshold, destructive confirmation, write boundary, progress note, harness status, tool-round cap, host diagnostics and gate flags are execution constraints/observability rather than S3 ownership.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no qualifying first-party S3 mode was found.
- Why this is / is not agent-owned: the operational model owns S1 task choices; guard/gate/status machinery constrains or reports those choices. No separate current-control organizational decision right is evidenced.
- Evidence: [`lib/agent.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/lib/agent.mjs); [`mcp/tools.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/mcp/tools.mjs); [`README.md`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: human confirmation for an out-of-project write or destructive command is a local S1 safety decision, not whole-system S3 parent governance.

### Absence scope

- Surfaces inspected: standalone REPL/control commands; guard and gate; progress/handoff state; `harness_status`; host diagnostics; config; Dream/graph workers; host integration lifecycle.
- Plausible first-party paths checked: destructive-action approvals, `/hosts`/doctor/status, loop guard, gate holds, progress next-step control, Dream lock and graph update.
- Why no material first-party path remains: all inspected decisions are local task execution constraints, audit corrections or maintenance state. No whole-system current view plus discretionary regulation of shared S1 resources/commitments is established.

## S3* — Complementary audit

- State: C
- Function: challenge a model's ordinary completion claim with complementary inspection of the actual changed repository state and return failures/review requirements before the reply is allowed to finish.
- Disturbance / variety regulated: an operational model may claim completion despite syntax-invalid files, shell-created changes it did not explicitly track, insufficient checking or missed adversarial edge cases.
- Decisive decision or feedback right: the first-party Stop gate can independently inspect changed files, run syntax validation and return a blocking finding; it also requires evidence of a second adversarial review pass before accepting a changed-code completion.
- Decision owner: constructor path. Deterministic parser/gate logic owns fixed verification/enforcement; the same operational model performs the adversarial second pass. No materially independent autonomous audit actor owns the full audit judgment in the standard setup.
- Supporting / enforcement mechanisms: edit-event tracking, `git status` recovery of shell-made changes, parseable-language checks, per-prompt gate flags, `PASS_RE`, registered Stop hook, `harness_verify`, double-check skill and standalone corrective second turn.
- Closure path: model produces changed state and an ordinary completion reply → gate reconstructs actual changed files independently of the reply → parser/adversarial-evidence checks run → gate blocks with concrete finding when required → host or standalone agent receives that finding → subsequent model turn repairs/reviews → later completion is retried.
- Boundary reachability: host-mode `hooks/hooks.json` registers the Stop hook and `lib/hooks.mjs` dispatches it to `gate.stop`; standalone `lib/agent.mjs` invokes the same gate after each engine reply and feeds a block reason into another engine turn.
- Why this is / is not agent-owned: the complementary path is real and function-specific, but deterministic validation is enforcement/evidence rather than autonomous organizational discretion, while the adversarial review is performed by the same S1 actor whose work is being checked. The first-party primitive therefore establishes a constructor audit path rather than `A`.
- Evidence: [`hooks/hooks.json`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/hooks/hooks.json); [`lib/hooks.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/lib/hooks.mjs); [`lib/gate.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/lib/gate.mjs); [`lib/agent.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/lib/agent.mjs); [`skills/double-check/SKILL.md`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/skills/double-check/SKILL.md); [`mcp/tools.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/mcp/tools.mjs).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: `C` does not credit the deterministic parser as an autonomous auditor. A downstream composition with a materially independent reviewer could close the exposed audit path differently and would require its own assessment.
- Claim being audited: the operational model's claim that a code-changing turn is ready to finish and sufficiently verified.
- Ordinary reporting path: model's final assistant reply plus ordinary edit/shell/tool history produced during the operational turn.
- Complementary access path: gate reconstructs changed files from first-party edit events and Git status, then reads/parses the actual files and recorded verification commands rather than trusting the completion text.
- Independence boundary: complementary evidence collection/checking is implemented outside the model's ordinary response path; however, the second adversarial reading itself is assigned back to the same operational model, so autonomous audit independence is incomplete.
- Who acts on findings: the host/standalone control path returns the block reason to the operational model, which must repair or perform the requested adversarial review before a later completion attempt.

## S4 — Outside-and-then intelligence

- State: —
- Function: no externally oriented prospective adaptation loop is established in the reviewed standard distribution.
- Disturbance / variety regulated: Dream consolidates past internal session traces into durable facts and the graph updates after code changes; these mechanisms improve future context but react to internal operational history/current repository state rather than sensing external/future distinctions and developing adaptation options.
- Decisive decision or feedback right: no prospective adaptation judgment over harness capability is established.
- Decision owner: not established.
- Supporting / enforcement mechanisms: SessionEnd distillation, `DIGEST.md`, history cursor, `harness_remember`, graph update/query, shared memory and session handoff provide learning/continuity without S4 closure.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no qualifying first-party S4 path was found.
- Why this is / is not agent-owned: the model decides which internal historical facts are worth remembering, but this is memory curation rather than outside-and-then organizational adaptation.
- Evidence: [`lib/dream.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/lib/dream.mjs); [`mcp/tools.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/mcp/tools.mjs); [`README.md`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/README.md).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: durable learning can support S4 in a larger organization, but persistence and retrospective consolidation alone do not satisfy the Profile's external/future distinctions.

### Absence scope

- Surfaces inspected: Dream Stage 1/2; append-only history; digest/ack; graph rebuild/update; shared memory; recall; host status/doctor; configuration and benchmark claims.
- Plausible first-party paths checked: model-driven memory consolidation, graph refresh after changed code, cross-host recalled facts, benchmark/cost measurements, companion status.
- Why no material first-party path remains: inspected paths summarize internal past/current state. They do not sense future-relevant external change, develop an adaptation option from that distinction and return an adaptation decision into current organizational capability/S3.

## S5 — Policy and identity

- State: —
- Function: no identity/ultimate-policy closure is established at the assessed recursion.
- Disturbance / variety regulated: configuration selects verification, guard, graph, memory and Dream behavior; the standalone system prompt defines task behavior and the human confirms some destructive actions, but these are operational constraints rather than adjudication of organizational identity or ultimate policy.
- Decisive decision or feedback right: no function-specific identity/ultimate-policy decision right is established.
- Decision owner: not established within the assessed system.
- Supporting / enforcement mechanisms: config file, fixed system prompt, tool set, destructive/write confirmations, host installation instructions and memory type rules constrain behavior without creating S5.
- Closure path: not applicable for the negative finding.
- Boundary reachability: no qualifying first-party S5 path was found.
- Why this is / is not agent-owned: the operational model follows supplied policy and can write memories, but does not own legitimate authority to redefine atlias's identity/ultimate policy; ordinary human confirmations are lower-level safety choices.
- Evidence: [`README.md`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/README.md); [`lib/agent.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/lib/agent.mjs); [`mcp/tools.mjs`](https://github.com/ridelink0/atlias/blob/270eb980b32bc05278183aaf10af85ef35de2bc3/mcp/tools.mjs).
- Basis: explicit + structural negative search.
- Confidence: high.
- Caveats: developer/operator configuration authority is not promoted to S5 without an identity-level issue and authoritative return-to-operation loop.

### Absence scope

- Surfaces inspected: runtime config; standalone system prompt; host integration instructions; guard confirmations; memory/digest rules; installer/versioning behavior; MCP tool definitions.
- Plausible first-party paths checked: config changes, model/engine selection, user confirmation of destructive actions, memory policy, host selection and versioning/release semantics.
- Why no material first-party path remains: these mechanisms set operational parameters or release behavior but do not expose a runtime identity/ultimate-policy controversy, legitimate ultimate authority and returned governing decision.

## Recursion

No positive VSM recursion is established. The standalone agent is one S1 loop with subordinate tools. Multiple external host sessions can share atlias memory, but the reviewed first-party paths do not organize them as viable sibling units under a parent atlias metasystem. `SubagentStop` tracking and handoff notes preserve context rather than proving nested viable-system closure.

## Variety and escalation

atlias materially attenuates operational variety around one agent: repeated identical tool calls are interrupted with a reason to change approach; destructive shell operations and out-of-project writes require human confirmation; parser failures stop a premature completion; unparseable languages are explicitly reported as unchecked; shared memory and graph retrieval reduce context-search variety; handoff/Dream preserve continuity across compaction and sessions.

Escalation remains mostly local to the operational loop. A guard denial or gate finding is returned to the same agent for correction; destructive operations can escalate to the human user. Those paths are useful safety/audit controls but do not imply S3 or S5 at a higher organizational recursion.

## Evidence gaps

- Extra host integrations beyond the first-class documented hosts are explicitly marked unverified by the project; they are not required for the positive findings here.
- The benchmark reports context/token measurements but explicitly says it has not measured whether guard/gate mechanisms improve task success; no effectiveness claim is inferred.
- A downstream organization could compose multiple atlias-supported host sessions, a separate verifier or prospective adaptation process. Those compositions are separate systems-in-focus and would require their own evidence before S2/S3/S4/S5 or autonomous S3* is credited.
