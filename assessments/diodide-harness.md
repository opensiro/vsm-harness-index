---
harness_id: diodide-harness
project_name: Harness
repository: https://github.com/DIodide/Harness
review_ref: 471b22a2214dc0e4d056ecb05cf2ca48801384ac
reviewed_at: 2026-10-03
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.6
profile_version: 0.2.4
assessment_procedure_version: 0.3.6
assessment_changed_at: 2026-10-03
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Harness

## Review boundary

- System in focus: the first-party Harness web/Convex/FastAPI control plane at frozen revision `471b22a2214dc0e4d056ecb05cf2ca48801384ac`, including its built-in OpenRouter chat/tool loop, sandbox/MCP tool execution, harness configuration, collaborative sharing, persistent conversation/workspace state and external ACP-agent control surfaces.
- Purpose and identity: provide collaborative, sandboxed AI work sessions that can either run Harness's own model/tool loop or drive external coding agents such as Claude Code, Codex and Cursor.
- Relevant environment: user prompts, configured model/provider responses, MCP servers, Daytona sandboxes/files/repos, collaborators, credentials, and external ACP coding-agent processes.
- Standard-distribution boundary: the first-party OpenRouter agentic loop and directly owned sandbox/MCP tool execution are inside. Claude Code, Codex CLI, Cursor and their ACP adapters/processes are external agent runtimes; their internal organizational functions are not imported.
- Credited operating / distribution surfaces: `README.md`; `packages/fastapi/app/routes/chat.py`; `packages/fastapi/app/services/openrouter.py`; sandbox-tool and MCP execution paths; Convex/FastAPI session, sharing and harness-configuration surfaces.
- Adjacent first-party surfaces excluded from ownership: repository CI/development governance, tests/screenshots/marketing, and the external ACP agent binaries/wrappers provisioned by `packages/fastapi/app/services/agents/registry.py`.
- First-party operating / deployment modes considered: built-in OpenRouter chat with model-selected MCP/sandbox/skill tools; hosted external ACP agent sessions; owner/editor collaborative sessions; persistent workspace/harness configuration.
- Recursion level: one Harness-managed work/conversation organization. The built-in OpenRouter model/tool loop is the credited first-party operational S1 path; external ACP agents remain environment/dependencies at this assessment boundary.
- Reviewed revision: `471b22a2214dc0e4d056ecb05cf2ca48801384ac`.
- Observation date: 2026-10-03.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.6.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.6.

## Repository architecture

Harness is a three-tier application with a realtime Convex state layer and a FastAPI agent gateway. Its external-agent lane provisions Claude Code/Codex/Cursor ACP processes in Daytona sandboxes and communicates with them through an ACP shim; those processes own their own reasoning loops.

Separately, `routes/chat.py` contains a first-party agentic loop for Harness's built-in model mode. It constructs the prompt and available skill/MCP/sandbox tools, calls the selected OpenRouter model, accumulates model-selected tool calls, executes those calls through first-party handlers, returns tool results to the transcript, and repeats for up to `MAX_TOOL_ITERATIONS`. This is not merely transport around another agent runtime: Harness itself closes the model→tool→result→next-model-turn loop.

Counterfactual owner test for S1: remove external Claude/Codex/Cursor processes while retaining the built-in OpenRouter loop and its first-party tool dispatch. Harness still accepts an open-ended task, lets the model select supported tools, executes them, feeds observations back and continues until completion. Remove the model-backed actor from that first-party loop while leaving transport/storage/enforcement and the same semantic action sequence no longer occurs.

Primary evidence:

- [README.md](https://github.com/DIodide/Harness/blob/471b22a2214dc0e4d056ecb05cf2ca48801384ac/README.md)
- [built-in chat loop](https://github.com/DIodide/Harness/blob/471b22a2214dc0e4d056ecb05cf2ca48801384ac/packages/fastapi/app/routes/chat.py)
- [OpenRouter transport](https://github.com/DIodide/Harness/blob/471b22a2214dc0e4d056ecb05cf2ca48801384ac/packages/fastapi/app/services/openrouter.py)
- [external-agent registry](https://github.com/DIodide/Harness/blob/471b22a2214dc0e4d056ecb05cf2ca48801384ac/packages/fastapi/app/services/agents/registry.py)
- [ACP client](https://github.com/DIodide/Harness/blob/471b22a2214dc0e4d056ecb05cf2ca48801384ac/packages/fastapi/app/services/agents/acp_client.py)

## Operational model

In the built-in mode, a user/editor submits a turn against a configured harness. FastAPI resolves permissions, tools, skills, sandbox and MCP context, calls the selected model and executes the model's tool calls. Tool results are appended to later model context and the loop repeats until normal completion or a bounded stop condition. In external-agent mode, Harness instead provisions and controls a separate ACP coding-agent process; those external reasoning loops are not credited to Harness.

## S1 — Operations

- State: A
- Function: perform open-ended model-guided work in the configured conversation/workspace by selecting and invoking first-party-exposed tools, observing results and revising later actions.
- Disturbance / variety regulated: user-task ambiguity, model/tool results, sandbox/repository state, MCP responses, skill instructions, upstream failures, context/output limits and permission/budget constraints.
- Decisive decision or feedback right: choose the next task-specific tool/action from the current transcript and observations and decide when to continue or return a final result.
- Decision owner: the selected model actor inside Harness's first-party `chat.py` loop.
- Supporting / enforcement mechanisms: OpenRouter transport; tool schemas; sandbox/MCP/skill handlers; budgets; auth/access checks; persistent transcript; max-iteration/truncation bounds.
- Closure path: user task/current transcript → model chooses content/tool call → first-party handler executes → result is appended to model context → model selects the next action or completes.
- Boundary reachability: the standard built-in chat mode directly invokes this first-party loop through `/api/chat/stream`; no external Claude/Codex/Cursor agent process is required for the credited S1 path.
- Why this is / is not agent-owned: deterministic gateway/tool code cannot choose the semantic task sequence by itself; the model actor supplies the task-specific discretionary action selection across iterations.
- Evidence: `packages/fastapi/app/routes/chat.py`; `packages/fastapi/app/services/openrouter.py`; README built-in chat description.
- Basis: explicit + structural.
- Confidence: high.
- Caveats: this S1 claim is limited to the built-in Harness model/tool path. External ACP coding agents are separate actors and are not imported.

## S2 — Coordination

- State: —
- Function: no material first-party inter-S1 interference attenuation loop is established at the assessed recursion.
- Disturbance / variety regulated: Harness can host multiple conversations, collaborators and external agent sessions, but plurality/sharing/routing does not by itself establish S2.
- Decisive decision or feedback right: choose a coordination response to a concrete conflict/oscillation among distinct internal S1 units and feed the result back into their behaviour.
- Decision owner: not established.
- Supporting / enforcement mechanisms: isolated sandboxes, sharing grants, stream fan-out, session routing and external-agent process separation.
- Closure path: no first-party interference-specific judgment/constraint → subsequent S1 behaviour loop is evidenced for distinct first-party S1 units.
- Why this is / is not agent-owned: workspace/process isolation and message routing are support topology unless tied to a specific inter-S1 disturbance and feedback relation.
- Evidence: README architecture; `routes/chat.py`; ACP registry/client.
- Basis: structural absence review.
- Confidence: high.
- Caveats: external coding agents may coordinate their own subagents; that is outside the first-party Harness boundary.

### Absence scope

- Surfaces inspected: built-in chat loop, external-agent registry/runtime, sharing/collaboration, sandboxes/workspaces, message routing and persistent state.
- Plausible first-party paths checked: collaborative editors; multiple agent sessions; background-agent observability; isolated sandboxes; shared conversation state.
- Why no material first-party path remains: the reviewed first-party autonomous operational path is a single model/tool loop, while multi-session/collaboration mechanisms do not evidence an interference-specific S2 closure among distinct first-party S1 units.

## S3 — Inside-and-now control

- State: —
- Function: budget/access/session/process enforcement exists without a first-party autonomous whole-system current-control owner over operational units.
- Disturbance / variety regulated: usage budgets, permissions, session lifecycle, sandbox/process state, collaborators and credential boundaries.
- Decisive decision or feedback right: discretionary current allocation/prioritization/intervention across an active internal S1 population using a whole-system view.
- Decision owner: users/configuration for current supervisory choices; deterministic services enforce selected limits.
- Supporting / enforcement mechanisms: budget checks, approval cards, session lifecycle, sandbox control, access verification and collaboration grants.
- Closure path: current facts → preset rule or human/application choice → enforcement; no autonomous whole-system allocation judgment loop is packaged.
- Why this is / is not agent-owned: hard limits and approvals regulate execution but do not own S3 discretion.
- Evidence: README; `routes/chat.py`; sandbox/session control surfaces.
- Basis: structural absence review.
- Confidence: high.
- Caveats: the built-in S1 model chooses task actions, not organization-wide current resource policy.

### Absence scope

- Surfaces inspected: budgets, approvals, workspace/session/sandbox lifecycle, usage ledger, collaboration and external-agent runtime control.
- Plausible first-party paths checked: budget manager; approval flow; session manager; background-agent view; workspace control.
- Why no material first-party path remains: no first-party autonomous actor combines a whole-system current picture with authority to revise shared priorities/resources/commitments.

## S3* — Complementary audit

- State: —
- Function: approvals, plans, transcripts, task cards and diff/status visibility exist without a separately owned first-party semantic audit/challenge loop.
- Disturbance / variety regulated: sensitive commands can be approval-gated and execution evidence is observable.
- Decisive decision or feedback right: independently judge an operational claim/result from complementary access and return corrective findings into later work.
- Decision owner: user/editor or external reviewer agent when used.
- Supporting / enforcement mechanisms: approval cards, live transcript, background-agent observability, git/diff/terminal surfaces and persistence.
- Closure path: evidence → human/external review → optional follow-up; no first-party autonomous auditor is packaged in the credited built-in mode.
- Why this is / is not agent-owned: approval and observability are not independent semantic audit ownership.
- Evidence: README; built-in chat and collaboration surfaces.
- Basis: structural absence review.
- Confidence: high.
- Caveats: an external ACP agent or another user may review, but that judgment is not a first-party Harness S3* owner.

### Absence scope

- Surfaces inspected: approvals, transcript/history, background-agent cards, plans, git/diff/terminal UI and collaborative sharing.
- Plausible first-party paths checked: approval cards; plan review; observable subagents; fork/rewind; git review.
- Why no material first-party path remains: no independent first-party evaluator with complementary evidence access and corrective feedback ownership is established.

## S4 — Outside-and-then intelligence

- State: —
- Function: skills, harness/model/MCP configuration and persistent workspaces provide adaptable capability inputs but no autonomous prospective adaptation loop.
- Disturbance / variety regulated: users may change models, tools, skills, prompts, MCP servers and workspace configuration.
- Decisive decision or feedback right: interpret external/prospective change and select a persistent capability/organizational adaptation.
- Decision owner: user/editor/maintainer; the built-in task model consumes configured capabilities but does not own their durable selection.
- Supporting / enforcement mechanisms: harness configuration, skill packs, model picker, MCP configuration, workspaces, persistent conversation state.
- Closure path: external/user choice → persisted harness configuration → later runs use it.
- Why this is / is not agent-owned: configurable capability is not an autonomous future/environment intelligence owner.
- Evidence: README; harness/skill configuration; `routes/chat.py`.
- Basis: structural absence review.
- Confidence: high.
- Caveats: skills can influence later model behaviour after users attach them, but the persistent adaptation choice is externally owned.

### Absence scope

- Surfaces inspected: harness configuration, skills/skill packs, models, MCP servers, persistent workspace/conversation state and external-agent provisioning.
- Plausible first-party paths checked: skills as learning; model switching; dynamic harness swap; persistent memory/history.
- Why no material first-party path remains: no first-party actor autonomously evaluates prospective environmental change and commits a durable capability adaptation.

## S5 — Policy and identity

- State: —
- Function: strong authentication, credential, approval and collaboration policy enforcement exists without autonomous identity/ultimate-policy resolution.
- Disturbance / variety regulated: owner/editor authority, secret access, tool approval, sandbox trust and billing/credential scope.
- Decisive decision or feedback right: resolve ultimate identity/policy tensions for the work organization and authoritatively return that policy into operation.
- Decision owner: users/owners and configured platform policy.
- Supporting / enforcement mechanisms: Clerk auth, share grants, credential encryption, approval gates, server-side secret handling and authorization checks.
- Closure path: externally established owner/admin policy → first-party enforcement → later agent operation.
- Why this is / is not agent-owned: Harness strongly enforces identity/security choices but does not autonomously resolve ultimate policy.
- Evidence: README; `routes/chat.py`; collaboration/auth boundaries.
- Basis: structural absence review.
- Confidence: high.
- Caveats: owner/editor role enforcement is important governance but not autonomous S5 ownership.

### Absence scope

- Surfaces inspected: auth/access, owner/editor grants, approvals, credentials/secrets, budgets and harness configuration.
- Plausible first-party paths checked: collaboration roles; credential boundaries; approval policy; billing/budget limits.
- Why no material first-party path remains: policy choices originate with users/platform configuration; no first-party autonomous identity/ultimate-policy decision loop is established.

## Recursion

Harness is assessed at one managed work/conversation boundary. Its built-in OpenRouter loop supplies one first-party operational S1 path. External ACP agent processes remain separate systems; repository-managed provisioning/transport does not donate their internal VSM functions to Harness.

## Variety and escalation

Harness attenuates variety through tool schemas, sandbox isolation, MCP relays, skills, access control, persistent state, bounded model/tool loops, usage budgets and collaborative controls. Permission/user-input questions escalate to users; external-agent semantic variety remains with the external agent runtime in that mode.

## Evidence gaps

- Frozen revision only.
- Hosted infrastructure not represented in the repository is not credited.
- External Claude/Codex/Cursor agent functions are not imported.
- Multiple concurrent conversations alone are not treated as a coordinated S1 population.

## Assessment summary

At the frozen revision, Harness has a genuine first-party autonomous operational path: its built-in OpenRouter loop repeatedly lets the model choose supported tools, executes them and returns observations for later model decisions. That supports S1=A. The reviewed distribution does not establish first-party autonomous S2, S3, complementary S3*, S4 or S5 ownership at this recursion.

**Vector:** A · — · — · — · — · —
