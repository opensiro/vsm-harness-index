---
harness_id: oxi
project_name: Oxi
repository: https://github.com/maziluiosif/oxi
review_ref: da693ad021667ce2a2360182f572bb73b6812add
reviewed_at: 2026-11-07
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

# Oxi

## Review boundary

- System in focus: the first-party Rust/egui `oxi` local-first desktop coding agent, using its **native** model/tool loop with its workspace-rooted file/shell/search/Git/web/MCP tools, model configurations, user approval bridge and durable local chat sessions.
- Purpose and identity: fulfill a user's code investigation/editing request through a local interactive agent whose configured model can select workspace actions, observe their outcomes and adapt during the same goal.
- Relevant environment: local repositories, file changes, command/test outcomes, user approvals/interruptions, provider availability, local/remote inference resources, web findings and changing agent-session context.
- Standard-distribution boundary: native executable `src/main.rs`, UI/session integration, `src/agent/{runner,openai,anthropic,codex_responses,loop_ctx,tools,history,approval}.rs` and first-party tool bodies. Support for hosted and self-managed inference is an LLM backend choice; model providers are not separate organization units.
- Credited operating / distribution surfaces: `src/agent/runner.rs`, `src/agent/{openai,anthropic,codex_responses}.rs`, `src/agent/tools/{mod,file_ops,web,paths}.rs`, `src/agent/{approval,history,prompt,events}.rs`, `src/session_store.rs`, `src/main.rs` and native workspace/UI event routing.
- Adjacent first-party surfaces excluded from ownership: the `src/agent/acp.rs` / `src/agent/acp/*` ACP **client** adapter used to run external Claude Code, Cursor or Codex processes; one-shot `src/agent/complete.rs` commit-message completion without tools; GUI editor/Git panes independent of the agent; contributor scripts, demo, tests and release automation.
- First-party modes considered: native local/OpenAI-compatible/provider-backed model agent with full first-party tools; manual provider switches and authorization settings; read-only web-search and code exploration; persistence of workspace chat history. ACP handoff is a separate boundary and cannot donate another harness's planner, subagents or reviewers to Oxi.
- Recursion level: one local coding goal/model-tool agent loop. A user may open distinct workspace sessions, but no first-party inter-session coordination or parent management recursion is thereby implied.
- Reviewed source: `maziluiosif/oxi@da693ad021667ce2a2360182f572bb73b6812add`, stable GitHub repo ID `1208079274`; Profile `0.2.4`, Methodology `0.3.7`; reviewed 2026-11-07.

## Repository architecture

`spawn_agent_run` constructs a native first-party workspace system prompt, bounded provider context, tool definitions, `ToolEnv` and `ApprovalGate`, then selects one of the Rust-owned OpenAI, Azure, Anthropic or Codex Responses agent loops. The model can request first-party tools; the runner mediates side effects and records returned tool outcomes into later model turns. Shell, read/search, workspace files, Git and optional web search are real executable tool paths, with capability/approval conditions configured by the user. The chat is retained per workspace and can be resumed with context compaction.

Crucially, `runner.rs` checks `cfg.is_acp()` **before building** Oxi's own agent prompt, tool definitions or provider loop. That branch invokes `run_acp_turn` and hands the agentic work to an external subprocess; Oxi acts as an ACP client and UI/control surface, **not** the owner of the external agent's organization. This assessment credits the native alternative only. Local voice, model installer/SSH tunnel, code editor, git pane, diff view and commit-message helper do not establish additional organizational decisions by themselves.

Frozen first-party sources:

- [Native product and precise ACP distinction](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/README.md)
- [Native runner, explicit ACP early exit, and provider/tool wiring](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/runner.rs)
- [First-party model/tool iteration](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/openai.rs), [Anthropic loop](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/anthropic.rs), [Responses loop](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/codex_responses.rs)
- [Tool registry and execution](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/tools/mod.rs), [source/file operations](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/tools/file_ops.rs)
- [Operator effect-approval decisions](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/approval.rs)
- [History/context and persisted sessions](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/history.rs), [session store](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/session_store.rs)
- [ACP client adapter boundary](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/acp.rs), [no-tool completion helper](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/complete.rs)

## Operational model

The human picks an active provider/model, a workspace and whether particular effects need approval. On the native path, the model chooses actions and tool arguments, observes workspace/command results, and can correct direction before producing a response. Deterministic Rust code enforces scope, tool schemas, timeout/cancellation and operator approval; the approval outcome is fed to the same model as action feedback. The native loop is one operational agent, not a team with a shared current-control owner or separate auditor. ACP integration can expose powerful agentic features, but those belong to the external program that actually owns the agent loop.

## S1 — Operations

- State: A
- Function: perform coding, source investigation and bounded workspace operations selected by the model against real tool feedback.
- Disturbance / variety regulated: incomplete task descriptions, source ambiguity, unknown symbols, failing commands, provider transport errors, permissions, workspace state changes and context limits.
- Decisive decision or feedback right: the configured LLM decides which first-party read/search/edit/shell/Git/web tool to call, how to change code, what failure to investigate and how to proceed after the tool returns.
- Decision owner: native Oxi model-driven tool loop; first-party Rust orchestrates dispatch, context and effect restrictions but not semantic code editing choices.
- Supporting / enforcement mechanisms: `spawn_agent_run`, built-in provider-specific loops, `ToolEnv`, file/path/shell tools, MCP transport, workspace context, session store and `ApprovalGate`.
- Closure path: user coding goal → native model tool request → first-party effect after applicable approval → returned command/file observation or refusal → model correction/retry or final response.
- Boundary reachability: the non-ACP `spawn_agent_run` path builds native tool definitions, history and `ToolEnv` before calling `run_chat_loop`/`run_anthropic_loop`/`run_codex_responses_loop`; these are supplied by the shipped executable.
- Why this is / is not agent-owned: removing model goal-directed selection leaves a versatile but passive code editor and tools; only the model decides which actions solve the user's coding objective.
- Evidence: [native runner](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/runner.rs), [tool registry](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/tools/mod.rs), [provider loop](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/openai.rs).
- Basis: explicit + structural.
- Confidence: high for the native code path.
- Caveats: no real inference/model-backed source-edit run was executed; ACP-only deployments must be assessed at the external agent's own boundary.

## S2 — Coordination

- State: —
- Function: no first-party anti-interference loop among distinct simultaneously operating S1 units is evidenced in the native Oxi coding system.
- Disturbance / variety regulated: separate chats/workspaces, cancellation, approval waits and GUI/source-file updates affect one operating session but do not constitute a concrete inter-S1 collision protocol.
- Distinct S1 units: the native loop serves one coding goal per run; concurrent local chats are isolated workspace histories, not a shipped collaborating multi-worker team with shared commitments.
- Inter-S1 disturbance: no specific competing model-operated native S1 writers/readers or oscillating commitments are structurally coupled by a first-party coordination relation.
- Attenuating coordination relation: not applicable; session storage, tool order and GUI synchronization regulate one run or display, not cross-S1 collisions.
- Feedback into subsequent S1 behaviour: tool results and approvals feed the current S1, without a returned inter-unit conflict/settlement signal.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: a provider option or one-at-a-time tool dispatcher does not supply two interfering operating units; external ACP agent coordination stays outside the owned boundary.
- Decisive decision or feedback right: no first-party native inter-S1 conflict choice.
- Decision owner: none evidenced; sequential tool handling and UI display are coded support for S1.
- Supporting / enforcement mechanisms: session history, UI events, native model tool loop and per-action approvals.
- Closure path: local tool outcome → same coding model; no competing S1 feedback arbitration.
- Why this is / is not agent-owned: no first-party team or inter-unit disagreement selection exists beyond the external ACP delegation boundary.
- Evidence: [runner including ACP split](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/runner.rs), [session histories](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/session_store.rs), [product modes](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/README.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: hosting other agents under ACP does not confer their internal S2 rights on Oxi.

### Absence scope

- Surfaces inspected: native agent runner and provider loops, tool execution, workspace/session persistence, UI event routing, ACP integration, operator approvals.
- Plausible first-party paths checked: spawned native child coding loops, common file-write reservations, cross-run conflict detection, returned reallocation and settlement.
- Why no material first-party path remains: the credited native runtime has one directly operating model/tool session and no verified first-party cross-agent interference/attenuation loop.

## S3 — Inside-and-now control

- State: —
- Function: no agent-owned or constructor-owned whole-current resource/commitment manager across multiple native S1 operational units was established.
- Disturbance / variety regulated: tool-round ceilings, timeouts, provider changes and permission denials bound current operations but are per-run reliability or user setup decisions.
- Decisive decision or feedback right: no distinct whole-run allocation/prioritization/exception intervention across a portfolio of operating S1 cells; the model selects task actions and the user can stop/reconfigure its run.
- Decision owner: user for task/model/settings/approval; current S1 model for its task; fixed Rust for execution limits.
- Supporting / enforcement mechanisms: `max_tool_rounds`, context history compaction, provider switch and cancellation, local model/SSH management, session UI and approvals.
- Closure path: a failed command returns to its own model; human can cancel or switch providers, without a first-party whole-current S3 policy and returned multi-unit reallocation.
- Why this is / is not agent-owned: a running user task and hard watchdog do not make S3 merely because their execution is managed by a Tokio runtime.
- Evidence: [native execution and limits](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/runner.rs), [loop parameters](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/loop_ctx.rs), [approval right](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/approval.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: manual workspace/user scheduling is external human operation, not a first-party parent-mode S3 at a clearly established multi-unit recursion.

### Absence scope

- Surfaces inspected: runner/setup, Tokio executor, provider selection, per-run budgets/cancellation, workspace switch, session storage and GUI state.
- Plausible first-party paths checked: whole-current view of distinct operations, binding cross-unit budget/priority allocation, exception intervention and feedback into other current S1 commitments.
- Why no material first-party path remains: reviewed controls affect the same native coding run or user-visible application settings; no autonomous cross-operation current-control authority is provided.

## S3* — Complementary audit

- State: —
- Function: no separate complementary evidence path with sufficiently independent direct audit judgment and returned corrective control was found.
- Disturbance / variety regulated: commands can be run to test edits and the UI shows diffs, but these normally remain self-selected operational feedback or human inspection rather than an independent audit path.
- Decisive decision or feedback right: native Oxi does not ship a distinct read-only reviewer agent, independent verifier or raw-source contradiction gate over the producing model's completion report.
- Decision owner: same operating model can voluntarily run checks; user can inspect editor/Git panes, but no internal independent audit judgment is returned to current agent control.
- Supporting / enforcement mechanisms: `bash`, `git_diff`, file reads, undo journal, UI diff display and existing session result logs.
- Claim being audited: potential claim that a coding edit succeeded; no separate first-party actor is wired to challenge it after production.
- Ordinary reporting path: same model's chosen commands, tool results and final assistant answer.
- Complementary access path: GUI diff/terminal display is available to the user, but not a separate first-party audit feedback decision and return route to the coding model.
- Independence boundary: ordinary verification commands are invoked in the same production context; screen display and tests as development assets are not a separate audit organization.
- Who acts on findings: operating model reacts to its own tool results, or human manually reviews; no distinct audit finding-to-control loop shown.
- Closure path: model observes testing/shell response and may repair; independent S3* verdict absent.
- Why this is / is not agent-owned: a model checking its own output or a GUI showing diffs does not constitute independently grounded challenge of routine production reporting.
- Evidence: [first-party tools](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/tools/mod.rs), [agent loop](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/openai.rs), [diff UI](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/ui/diff.rs).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: external ACP agents may expose their own audits, which are explicitly not imported.

### Absence scope

- Surfaces inspected: native completion branches, first-party tool interfaces and result handling, UI diff/Git views, tests, ACP adapter and user approvals.
- Plausible first-party paths checked: separate raw source reader, independent failure reconstruction, corrective reviewer verdict/veto and returned repair action.
- Why no material first-party path remains: only the same model's operational checks and external human UI inspection were evidenced, not a complementary independent first-party audit route.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective external-environment modelling, future adaptation-option selection and controlled return into coding capability is established.
- Disturbance / variety regulated: present model availability, future model downloads, workspace task changes, local hardware resources and web search may influence existing operations but are not assembled into a forward-looking adaptation loop.
- Decisive decision or feedback right: human selects providers/prompts; source updates are developer work; no supported S4 actor decides prospective changes to the agent's future policy/skills/tools as a function of sensed external trends.
- Decision owner: user for model/download/settings choice; model for immediate task/web research; external maintainers for product evolution.
- Supporting / enforcement mechanisms: local GGUF model installer, SSH compute tunnel, provider catalog, keyless search, editable system prompt and software updater.
- Closure path: user picks a presently available model or agent uses web search → current task receives more capability/information. No future-option model, strategy judgement and returned new operational capability loop.
- Why this is / is not agent-owned: search, model switching, general learning and updating a binary are insufficient for S4 without external-and-prospective option creation and closure.
- Evidence: [product options](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/README.md), [local-model management](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/local_models.rs), [web tool](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/tools/web.rs), [updater](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/update.rs).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: manually selecting a stronger provider for future use is a user preference, not sufficient evidence of a separate adaptive S4 function.

### Absence scope

- Surfaces inspected: model/remote-compute configuration, workspace agent prompt, web search, saved context/history, updater and relevant UI settings.
- Plausible first-party paths checked: environmental trend/prospect sensing, future scenario evaluation, alternate capability generation, authority to ratify and return the selected adaptation into current operation.
- Why no material first-party path remains: the shipped control surfaces are present inference/configuration and current task information access, without a closed prospective organizational strategy/update choice.

## S5 — Policy and identity

- State: —
- Function: no distinct legitimate ultimate identity/policy decision path and returned binding organizational charter closure is evidenced.
- Disturbance / variety regulated: unsafe shell commands, out-of-scope paths, MCP side effects and user tool consent are effect-risk controls rather than disputes over Oxi's organizational mission or ethos.
- Decisive decision or feedback right: no identity- or ultimate-policy issue traverses an authorized parent deliberation/ratification path and returns as a durable direction governing subsequent agent operation.
- Decision owner: human user owns per-command approval and existing application settings; constructor owns hardcoded limits; neither is demonstrated as a function-specific S5 parent mode.
- Supporting / enforcement mechanisms: `ApprovalPolicy`, `ApprovalGate`, optional `ApproveRest`, disabled/risky tools, path fences, user prompt and settings.
- Closure path: requested mutating tool → user approves/denies → result returned to same model; no mission-level policy change/return is established.
- Why this is / is not agent-owned: capability restriction and static guardrails do not themselves choose ultimate purpose; an operator confirming an edit is not ratification of a new organizational identity.
- Evidence: [approval implementation](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/approval.rs), [system prompt](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/prompt.rs), [tool limits](https://github.com/maziluiosif/oxi/blob/da693ad021667ce2a2360182f572bb73b6812add/src/agent/tools/paths.rs).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a real team's policy could govern a human using Oxi externally, but is not a shipped first-party closed S5 mode.

### Absence scope

- Surfaces inspected: system prompt, settings, approval policies and UI, MCP approval, workspace path confinement and session history.
- Plausible first-party paths checked: identity disagreement, parent ultimate authority and charter revision, ratification, durable returned policy affecting subsequent operations.
- Why no material first-party path remains: all evidenced human/operator decisions are task permissions or configuration under a fixed coding-assistant purpose; no identity-specific conflict-and-resolution path exists.

## Recursion

One native Rust model/tool coding session is the credited operating S1. The UI can manage multiple independent workspaces and tasks, but is not evidence of a recursively managed organization of collaborating autonomous work cells. For ACP providers the application becomes a client to another agent process; that process's internal VSM functions must be separately assessed at its own boundary. Infrastructure (remote inference, OAuth, terminals) and the user's local operational supervision are not automatically parent S3/S4/S5.

## Variety and escalation

The native model can choose code tools, rerun commands and adjust to source results. Tool permissions, path checks, optional approval and limited model rounds constrain side effects; denial is returned to the same S1. Local model/remote-SSH options alter where inference runs without producing independent metasystem ownership. No first-party competing S1 collaboration, whole-current allocation, independent audit, future strategy or identity-governance closure was evidenced; ACP alternatives are deliberate external boundaries.

## Evidence gaps

Frozen source SHA and current public GitHub repository identity verified. Native provider/tool loop, explicit external ACP early return, approval mechanism, session storage, GUI tooling and application setup inspected at the pinned source. `cargo` and the requisite Rust 1.92 toolchain were unavailable, so no upstream compile/test or live model-backed tool run was executed; repository test source is corroboration, not observed pass evidence. Classification reflects first-party wired code, not ACP-subprocess capability, release quality, agent performance or security assurance.

## Assessment summary

Oxi includes a substantive autonomous native coding agent that owns first-party source/tool operations (**S1=A**). Its other supported facilities are user configuration, approval/enforcement, session storage, model hosting, a code editor and an **ACP client of external agent programs**. None closes the specific inter-agent coordination, whole-current management, complementary audit, prospective adaptation or ultimate-policy feedback path (**S2/S3/S3*/S4/S5=—**). This is a frozen-source organizational mapping, not a judgement about the external agents Oxi can connect to.

Proposed vector: **`A · — · — · — · — · —`**.
