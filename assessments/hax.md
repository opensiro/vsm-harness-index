---
harness_id: hax
project_name: Hax
repository: https://github.com/OleksandrChekhovskyi/hax
review_ref: 6753f30e5f79c01b47925f690b90daaa4630b409
reviewed_at: 2026-10-13
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Hax

## Review boundary

- System in focus: shipped native C terminal coding agent `hax`, including its single-session model/tool loop, local read/edit/write/bash tools, optional background shell job observation, and session persistence.
- Purpose and identity: respond to a developer's prompt by inspecting and changing local repository files through model-selected tools, rendering results and continuing in a terminal or one-shot mode.
- Relevant environment: local filesystem and shell, user's task and terminal, configured or auto-discovered model service and credentials, and operator-invoked external subprocesses.
- Standard-distribution boundary: compiled binary and its first-party model/tool dispatch, terminal REPL and `-p` mode, XDG configuration/session/transcript and built-in coding tools. External process compositions and model-provider management beyond requests are not included.
- Credited operating / distribution surfaces: [README.md](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/README.md); [philosophy.md](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/docs/philosophy.md); [agent_loop.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent_loop.c); [agent.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent.c); [agent_dispatch.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent_dispatch.c); [agent_tool.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent_tool.c); [tool_schema.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tool_schema.c); [read.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/read.c); [write.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/write.c); [edit.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/edit.c); [bash.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/bash.c); [task_registry.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/task_registry.c); [task_wait.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/task_wait.c); [session.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/session.c); [transcript.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/transcript.c); [provider.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/provider.c); [config.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/config.c); [compact.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/compact.c); [oneshot.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/oneshot.c).
- Adjacent first-party surfaces excluded from ownership: development contributor practices and CI/tests, screenshot/demo art, external model servers (including llama.cpp), shells/scripts launched by an operator, hypothetical plugins/MCP/orchestrators explicitly omitted by the distribution, and unrelated consumer systems embedding the process.
- First-party operating / deployment modes considered: interactive REPL, one-shot `hax -p`, resume of a prior single conversation, selectable provider/model, built-in tool calls and background shell jobs.
- Recursion level: one local coding-agent session, not a separate organization of autonomous coding workers and not the human's development organization.
- Reviewed revision: `6753f30e5f79c01b47925f690b90daaa4630b409`.
- Observation date: 2026-10-13.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

[README.md](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/README.md) describes a deliberately minimal native C binary for terminal-native coding. [agent_loop.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent_loop.c) defines the model-response/tool dispatch loop: active provider output can request tools; `loop_run_tool` invokes the selected tool (or returns refused/skipped outcomes) and appends result provenance back into the session so a later model request can react. [agent_tool.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent_tool.c) and [tool_schema.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tool_schema.c) implement the supported tool contracts, including direct file reads and edits ([read.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/read.c), [edit.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/edit.c), [write.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/write.c)) and shell execution ([bash.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/bash.c)). Provider selection and local-model auto-discovery ([provider.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/provider.c), [config.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/config.c)) choose which external model can fulfill the same agent loop, rather than running multiple autonomous coding employees.

[task_registry.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/task_registry.c) and [task_wait.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/task_wait.c) maintain background shell-task state. These are non-agent terminal command jobs: their lifecycle can be inspected but they do not own independent model/task/coding decision loops. [session.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/session.c), [transcript.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/transcript.c) and [compact.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/compact.c) preserve/reduce interaction history and aid diagnosis; a human can inspect a transcript, but no independent auditor or organizational control plane is wired. README explicitly rejects integrated plugin/MCP marketplaces and per-command approval prompts; it advocates Unix process composition outside this binary rather than bundling another multi-agent coordination layer.

## Operational model

One model-led coding loop chooses reads, edits or shell commands and observes the results before subsequent steps. Deterministic adapters execute tools, interrupt/skip unsafe/aborted operations, cap output and preserve sessions. The developer selects project goal, provider and model and owns project policy. Commands spawned in the shell or parallel terminal sessions are independent external composition, not in-boundary multi-S1 task organization.

## S1 — Operations

- State: A
- Function: perform task-aware repository investigation/modification through tool calls chosen by a coding model.
- Disturbance / variety regulated: unknown repository layout, errors from shell commands and edits, incomplete investigation and changing observable tool outcomes.
- Decisive decision or feedback right: the active coding model selects tool calls and continuation or final reply after feedback.
- Decision owner: model-driven Hax coding agent in terminal or one-shot session.
- Supporting / enforcement mechanisms: streaming provider transport, tool schema, native dispatcher, local read/write/edit/bash tools, cancellation and history.
- Closure path: model call → read/edit/bash tool dispatch → actual output/refusal/error stored in history → next model choice or final answer.
- Boundary reachability: first-party hax binary directly exposes the model/tool loop in interactive and one-shot modes; no extra developer-assembled host required.
- Why this is / is not agent-owned: a static C dispatcher cannot decide repository-specific next actions without model tool requests; the model's choices supply S1 agency.
- Evidence: [README.md](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/README.md); [agent_loop.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent_loop.c); [agent.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent.c); [agent_tool.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent_tool.c); [read.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/read.c); [edit.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/edit.c); [bash.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/bash.c)
- Basis: explicit and structural
- Confidence: high on source-wired loop, no credentialed end-to-end task executed
- Caveats: runtime tooling implements, but does not own, discretionary coding decisions.

## S2 — Coordination

- State: —
- Function: no in-boundary mechanism regulates a specific interference between distinct autonomous S1 coding operations.
- Disturbance / variety regulated: possible shell subprocess contention, not evidenced independently autonomous sibling coding-unit conflict.
- Decisive decision or feedback right: none at the cross-S1 interference relation in the distributed single-session product.
- Decision owner: no first-party S2 owner demonstrated; only current agent has coding decisions.
- Supporting / enforcement mechanisms: shell job registry, waiting and terminal-side control.
- Closure path: a background command completes or is observed, but no correction to another independent coding S1 is returned.
- Why this is / is not agent-owned: background shell jobs execute specified commands, not model-powered operating cells; ordinary serial tool calls and Unix composition do not form an S2 relationship.
- Evidence: [agent_loop.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent_loop.c); [task_registry.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/task_registry.c); [task_wait.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/task_wait.c); [bash.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/bash.c); [philosophy.md](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/docs/philosophy.md)
- Basis: structural and explicit distribution intent
- Confidence: high within compiled default distribution
- Caveats: external concurrent hax processes could conflict but have no bundled mutual coordination.

### Absence scope

- Surfaces inspected: agent/model loop, tool registry, terminal shell-job lifecycle, documented subprocess composition
- Plausible first-party paths checked: independently active coding workers, real resource-write interference, dedicated attenuation and corrective return
- Why no material first-party path remains: no packaged second model-led S1 or cross-S1 conflict detector; jobs are tools, not agentic siblings.

## S3 — Inside-and-now control

- State: —
- Function: no whole-current managerial control across a population of distinct agent-operated S1s is shipped.
- Disturbance / variety regulated: task progress and current shell/session state, not competing organizational commitments.
- Decisive decision or feedback right: agent selects its own next coding step; user chooses session/provider settings; no whole-system prioritization/assignment owner.
- Decision owner: none for S3 at declared recursion.
- Supporting / enforcement mechanisms: session history, tool pipeline, background job registry, terminal input.
- Closure path: tool/job feedback informs a single coding loop; no whole-operating-system resource/commitment regulation among multiple S1s.
- Why this is / is not agent-owned: a running transcript, provider picker or shell process registry is not an agentic S3 supervisor of distinct autonomous units.
- Evidence: [agent.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent.c); [agent_loop.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent_loop.c); [task_registry.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/task_registry.c); [session.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/session.c); [config.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/config.c)
- Basis: structural
- Confidence: medium-high
- Caveats: human may externally manage multiple processes, which is outside evaluated binary.

### Absence scope

- Surfaces inspected: operating loop, session/job registry, provider selection and documentation
- Plausible first-party paths checked: whole-current operating worker roster and adaptive budget/priority/commitment authority with returned changes
- Why no material first-party path remains: no bundled coordinating multi-agent operational population or discretionary S3 manager.

## S3* — Complementary audit

- State: —
- Function: no independently commissioned auditor with direct reality inspection and corrected management feedback is built in.
- Disturbance / variety regulated: agent's mistaken completion claim or defects that a separate review would challenge.
- Decisive decision or feedback right: no independent source-access reviewer judgment and corrective S3 return owner.
- Decision owner: ordinary coding agent and external human reviewer of transcript/output.
- Supporting / enforcement mechanisms: visible terminal transcript, detailed wire trace, same-agent read/test calls, regular operator inspection.
- Closure path: operator reads transcript or model inspects tool output; no separate-first-party auditor verdict to managerial correction is wired.
- Why this is / is not agent-owned: user-accessible trace is evidence but not itself an independent auditor; reviewing a file within the same coding-agent loop does not establish S3*.
- Evidence: [transcript.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/transcript.c); [agent_loop.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent_loop.c); [read.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/tools/read.c); [agent.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent.c); [README.md](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/README.md)
- Basis: structural
- Confidence: medium-high
- Caveats: a user could compose a second independent process auditor outside this product.

### Absence scope

- Surfaces inspected: stream transcript, debug/tracing, file/shell tools and standard model loop
- Plausible first-party paths checked: distinct complementary audit actor, direct source verification, finding adjudication and return to S3 current management
- Why no material first-party path remains: existing first-party mechanisms provide diagnostics or ordinary S1 verification, not independent auditor commissioning and closure.

## S4 — Outside-and-then intelligence

- State: —
- Function: no outside-and-future capability adaptation loop is shipped for this coding-session organization.
- Disturbance / variety regulated: changes in local model/server capabilities or longer-term development environment.
- Decisive decision or feedback right: no agent-owned choice of prospective operating capability adjustment, adoption and returned S3 regulation.
- Decision owner: human chooses provider/model/configuration; runtime autodiscovers a currently served local model.
- Supporting / enforcement mechanisms: provider registry, capability detection, model picker and persistence, session compaction.
- Closure path: provider detection allows present task requests, but no future-outlook intelligence/adaptation decision loop changes organizational capability.
- Why this is / is not agent-owned: discovering the model served now is an immediate interface configuration, not autonomous prospective adaptation.
- Evidence: [README.md](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/README.md); [provider.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/provider.c); [config.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/config.c); [compact.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/compact.c); [philosophy.md](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/docs/philosophy.md)
- Basis: explicit and structural
- Confidence: medium-high
- Caveats: Unix scripts and maintainer releases could change future system capability externally.

### Absence scope

- Surfaces inspected: provider discovery/configuration, compaction, session state, scripting philosophy
- Plausible first-party paths checked: prospective environmental intelligence, options for future operating capacity and agent/parent adaptation decision returned to active organizational control
- Why no material first-party path remains: mechanisms are static choice, immediate capability detection and task continuity, not forward-looking organizational adaptation.

## S5 — Policy and identity

- State: —
- Function: no ultimate organizational purpose/identity adjudication and binding return loop in compiled Hax.
- Disturbance / variety regulated: disagreements over constitutional mission or governing principles, not command execution flags.
- Decisive decision or feedback right: none for S5 inside assessed session; developer chooses goal, model, surrounding safety/organization.
- Decision owner: human outside system for ultimate identity and policy.
- Supporting / enforcement mechanisms: config flags, request-level refusals/cancellation, tool schema validation and human operating environment.
- Closure path: tool execution may be refused or skipped and operator chooses settings; no identity-level question moves to authority and returns a governing policy change.
- Why this is / is not agent-owned: safety and configuration enforcement do not decide enterprise or persistent system identity.
- Evidence: [README.md](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/README.md); [config.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/config.c); [agent_loop.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent_loop.c); [agent_tool.c](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/src/agent_tool.c); [philosophy.md](https://github.com/OleksandrChekhovskyi/hax/blob/6753f30e5f79c01b47925f690b90daaa4630b409/docs/philosophy.md)
- Basis: structural
- Confidence: medium-high
- Caveats: README notes absence of per-command approval prompt, making even ordinary policy external/operator-controlled.

### Absence scope

- Surfaces inspected: binary config/providers/tool constraints, external operator instruction and repository maintainer governance
- Plausible first-party paths checked: internal identity adjudication or authorized parent decision/return determining ultimate purpose
- Why no material first-party path remains: only current-task and tool settings are available; no first-party S5 owner/decision closure.

## Recursion

One executable coding session is the system-in-focus; shell subprocesses and resumed chat histories are tools/state, not further recursively viable autonomous S1s. The developer and Unix environment are external, not a counted parent organizational metasystem.

## Variety and escalation

The model adapts coding choices to live tool observations. Native tool dispatch/refusals and output caps constrain action effects and preserve diagnostics. This is useful S1 regulation without evidence of internal multi-S1 coordination, current metasystem, complementary independent audit or higher adaptation/governance.

## Evidence gaps

Pinned-source static review, not a credentialed live model-provider run. No survey of arbitrary user-built Unix orchestrations; they are excluded. Negative states use bounded first-party evidence, not a claim that developers cannot compose other Hax processes into a larger system.
