---
harness_id: beastron
project_name: Beastron
repository: https://github.com/baokhang83/beastron
review_ref: 6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561
reviewed_at: 2026-11-28
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# Beastron

## Review boundary

- System in focus: The Beastron terminal coding CLI and its installed one-shot and interactive coding runtime.
- Purpose and identity: Complete repository tasks with a local-model-oriented, observable coding loop.
- Relevant environment: A local project, a configured inference endpoint, project instructions and user permissions.
- Standard-distribution boundary: Shipped CLI, provider client, agent loop, tool set, permissions, task checkpoint, verification and trace.
- Credited operating / distribution surfaces: Interactive and one-shot control, auto and ask permission modes, local context sizing and tool evidence feedback.
- Adjacent first-party surfaces excluded from ownership: Eval/reference commands, benchmark refitting, test fixtures, upstream GitHub and model services.
- First-party operating / deployment modes considered: Default locally hosted model configuration and compatible-provider modes, with one-shot or interactive operation.
- Recursion level: A single Beastron instance serving one focal project's turn stream.
- Reviewed revision: 6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561
- Observation date: 2026-11-28
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.8
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.8

## Repository architecture

The CLI instantiates one native agent over an OpenAI-compatible client, workspace, tool registry and approval callback. It records checkpoints and trace events. Verification code observes writes and results, nudges incomplete responses and sometimes blocks a success status. Separate evaluation and replay commands run suites and reference agents.

## Operational model

The conversational model drives individual coding or investigation turns. It selects tools, sees results and decides the next operation or final answer. Deterministic evidence rules constrain completion, and the operator may explicitly choose an approval mode.

## S1 — Operations

- State: A
- Function: Close individual coding or investigative tasks in the standard CLI.
- Disturbance / variety regulated: Varied requests, incomplete plans, tool errors and project constraints.
- Decisive decision or feedback right: Select tool calls, repair unsuccessful work and formulate the terminal response.
- Decision owner: The configured model in Beastron's native loop.
- Supporting / enforcement mechanisms: Project briefing, filtered tool schemas, approve callback, deterministic verification, checkpoints and trace.
- Closure path: Executed tool outcomes reenter model history. The agent can continue after a nudge and the CLI records done, incomplete, denied or error.
- Boundary reachability: The bundled executable constructs the tool-bearing Agent and directly runs it in one-shot or interactive mode.
- Why this is / is not agent-owned: The model owns the practical choice of action. Approval and evidence checks constrain the turn without replacing its discretion.
- Evidence: [src/beastron/cli.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/cli.py#L120-L151), [src/beastron/agent.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/agent.py#L380-L411), [src/beastron/agent.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/agent.py#L478-L529), [README.md](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/README.md#L33-L47)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: The default auto mode supports agent closure. Ask mode can return approval decisions to the operator.

## S2 — Coordination

- State: —
- Function: No distinct cross-unit coordination path was established.
- Disturbance / variety regulated: A turn can issue multiple tool calls and interact with ambient project changes.
- Decisive decision or feedback right: No distinct decision right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Single-model loop, sequential tool results, workspace checkpoint and undo.
- Closure path: Tool results enter the same conversation. A failed checkpoint or denied action ends the current turn.
- Why this is / is not agent-owned: The system has one coding decision loop; concurrent commands do not independently own work commitments.
- Evidence: [src/beastron/cli.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/cli.py#L131-L148), [src/beastron/agent.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/agent.py#L380-L409), [src/beastron/agent.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/agent.py#L510-L529), [src/beastron/checkpoint.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/checkpoint.py#L95-L134)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: This conclusion addresses the installed coding runtime.

### Absence scope

- Surfaces inspected: Agent and CLI entry points, tool execution, background process surfaces and checkpoint conflicts.
- Plausible first-party paths checked: Distinct concurrent coding actors with a supported relation to resolve inter-unit interference.
- Why no material first-party path remains: The normal product has a single task agent and mechanical command/checkpoint controls. Reference agents execute separately through the eval path.

## S3 — Inside-and-now control

- State: —
- Function: No portfolio-level current-control decision was established.
- Disturbance / variety regulated: The active turn can hit stale changes, failed checks, denial or interruption.
- Decisive decision or feedback right: No distinct decision right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Foreground callback, checkpoint restore, step limits and stalled-work nudges.
- Closure path: The configured guard can delay or terminate the current turn. The user can interrupt or restore the latest checkpoint.
- Why this is / is not agent-owned: These paths regulate one active task. They do not inspect and allocate resources or commitments across independent operational cells.
- Evidence: [src/beastron/agent.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/agent.py#L373-L409), [src/beastron/agent.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/agent.py#L478-L543), [src/beastron/cli.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/cli.py#L269-L310), [README.md](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/README.md#L33-L47)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Runtime termination and permissions are relevant task-level control.

### Absence scope

- Surfaces inspected: Foreground task lifecycle, checkpoint recovery, policy modes, guard and trace.
- Plausible first-party paths checked: Agent or operator commitment/resource intervention based on a whole-deployment current picture.
- Why no material first-party path remains: No portfolio with an influential control actor exists in this boundary. The observability mechanisms report turn-level events.

## S3* — Complementary audit

- State: —
- Function: No separate organizational audit decision loop was established.
- Disturbance / variety regulated: A coding model can claim completion without tests or coverage evidence.
- Decisive decision or feedback right: No distinct decision right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Deterministic test and coverage witness rules, direct mergeability read, and event traces.
- Closure path: The current loop receives corrective nudges or a fixed incomplete finish. Recorded traces can be inspected after completion.
- Why this is / is not agent-owned: Direct checks provide meaningful evidence, but the supplied audit-like paths do not assign an independent agent an evidence verdict over operational reporting.
- Evidence: [src/beastron/agent.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/agent.py#L478-L509), [src/beastron/verification.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/verification.py#L308-L383), [src/beastron/verification.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/verification.py#L761-L815), [README.md](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/README.md#L68-L78)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: This does not discount the supplied deterministic evidence guards.

### Absence scope

- Surfaces inspected: Coverage and test gates, direct GitHub query, trace replay and separate eval/reference CLI commands.
- Plausible first-party paths checked: A separately supplied actor independently acquiring evidence and returning an audit judgment to a current portfolio controller.
- Why no material first-party path remains: The current loop consumes predefined task evidence conditions. Evaluation compares performance on a separate benchmark surface.

## S4 — Outside-and-then intelligence

- State: —
- Function: No prospective organizational capability-adoption loop was established.
- Disturbance / variety regulated: Host memory, external model fit or the user's technology mix can change.
- Decisive decision or feedback right: No distinct decision right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Local context measurement, model picker, and developer-side suite refitting.
- Closure path: The measured context fit configures the current client or reports a sizing failure. Refitting alters the suite used to measure the product.
- Why this is / is not agent-owned: Sizing applies a predefined fit policy to available execution resources. Benchmark-driven changes are made through the development/refit surface.
- Evidence: [src/beastron/cli.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/cli.py#L120-L127), [src/beastron/cli.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/cli.py#L309-L329), [src/beastron/auto_context.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/auto_context.py#L53-L115), [docs/refitting.md](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/docs/refitting.md#L1-L22), [docs/refitting.md](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/docs/refitting.md#L58-L77)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Maintainer design and model-selection decisions are outside this operating recursion.

### Absence scope

- Surfaces inspected: Ollama context probing, context resize, configurable model profile and documented evaluation refit.
- Plausible first-party paths checked: Prospective evaluation of a new capability followed by an operating adoption decision, including parent return.
- Why no material first-party path remains: The runtime closes immediate context fitting. Changing the reference task suite does not change the installed agent's operating repertoire.

## S5 — Policy and identity

- State: —
- Function: No ultimate-policy or identity dispute and return was established.
- Disturbance / variety regulated: The user may require approval for mutations or provide instructions for the current project.
- Decisive decision or feedback right: No distinct decision right was established.
- Decision owner: No distinct owner at the declared recursion.
- Supporting / enforcement mechanisms: Auto/ask modes, project briefing and action-level approval callbacks.
- Closure path: The next action is allowed or denied under the selected mode and a denial returns control to the user.
- Why this is / is not agent-owned: The permission menu and task policy preserve the installed project's authority structure rather than adjudicating its ultimate purpose or authority.
- Evidence: [src/beastron/permissions.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/permissions.py#L6-L24), [src/beastron/ui.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/ui.py#L436-L465), [src/beastron/agent.py](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/src/beastron/agent.py#L510-L520), [README.md](https://github.com/baokhang83/beastron/blob/6fc36dcef46ee2b000e7c1fee07ad1d2b24b7561/README.md#L39-L47)
- Basis: Structural evidence from the pinned first-party source.
- Confidence: high
- Caveats: Ordinary per-action approval is outside this finding.

### Absence scope

- Surfaces inspected: Approval modes, permission policy, project instructions and CLI state transitions.
- Plausible first-party paths checked: An identity or authority conflict escalated to the legitimate owner and returned as a governing settlement.
- Why no material first-party path remains: The supplied path decides a proposed action and switches among predefined run settings. It exposes no higher-level settlement loop.

## Recursion

The unit of analysis is an installed CLI instance. The user workspace, model endpoint and reference-agent evaluations have independent boundaries.

## Variety and escalation

The runtime handles read-only scope, explicit approval, tool refusals, failed checks, context fit and checkpoint recovery with distinct outcomes.

## Evidence gaps

Pinned source only. No model-backed, benchmark, external API or user-workspace run was performed for this assessment.
