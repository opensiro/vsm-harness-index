---
harness_id: phuryn-mini-harness
project_name: Mini Harness
repository: https://github.com/phuryn/mini-harness
review_ref: 7ae9fca8221c55bd3c38697a61075357e1a94c26
reviewed_at: 2026-11-05
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Mini Harness

## Review boundary

- System in focus: The installed `mini` Python task agent, including optional `/goal` mode, subagents, runtime permission gate and MCP; not the vendor model, benchmark platforms or the human user's organization.
- Purpose and identity: Small educational but runnable coding/task harness with model-directed tools, session/compaction, delegated reading and separately checked goal completion.
- Relevant environment: User task and goal, workspace files, shell command results, tool failures, MCP replies, token/cost budgets, reviewer observations and operator approval.
- Standard-distribution boundary: `src/mini/{cli,loop,tools,session,ext,context}.py`, built-in tool descriptions and supported CLI goal mode. Bench harness, external provider implementations and operator configuration excluded from first-party governance claims.
- Credited operating / distribution surfaces: [loop](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/loop.py), [permissions/tools](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/tools.py), [session](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/session.py), [goal fixtures](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/tests/test_mini.py).
- Adjacent first-party surfaces excluded from ownership: Benchmark results, fixture models, default prompts as autonomous policy makers, offline tests, user-selected `verify` commands and the external permission judge service. They are evidence or enforcement rather than distinct installed strategic authority.
- First-party modes inspected: Interactive main model/tool continuation, delegated fresh-context subagent, append-only session/compaction, permissions and `/goal` command verification followed by a fresh reviewer with local workspace read tools.
- Recursion level: One task-working agent plus bounded fresh-context reviewer/subagent run; optional subagents do not automatically create an independently governed S1 portfolio.
- Reviewed revision: `phuryn/mini-harness@7ae9fca8221c55bd3c38697a61075357e1a94c26` (first-party MIT source).
- Observation date: 2026-11-05.
- Generated Profile version: 0.2.4
- Generated Methodology version: 0.3.7
- Current Profile version: 0.2.4
- Current Methodology version: 0.3.7

## Repository architecture

`Agent.turn` receives a model response, dispatches first-party read/write/edit/bash/find or MCP tools, appends observations and continues inference. `run_subagent` constructs a separate `Agent` and session with a fresh transcript, returns its text and accounts for cost. In optional `/goal`, the main agent's `goal_done` is only a claim: `run_goal` executes an independent configured shell `verify` command when present, invokes `verify` to launch a fresh-context reviewer with the objective and claim, accepts only its terminal `VERDICT: DONE`, and feeds disagreement back to the worker for repair. The reviewer explicitly can read actual working-directory files rather than merely reciting the worker's result. [loop](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/loop.py), [tests](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/tests/test_mini.py).

## Operational model

The model owns next tool selection in a task and receives tool results. The goal harness owns deterministic acceptance control, not a second discretionary task manager. The optional reviewer is a separate model invocation with fresh context and actual workspace tools; its own independent inspection and negative verdict influence acceptance and renewed action. This narrower complementary audit role does not import an organization-wide S3/S4/S5 or an externally validated quality guarantee.

## S1 — Operations

- State: A
- Function: Model-guided local work with iterative tool-result feedback.
- Disturbance / variety regulated: Changing files, shell command outputs, tool errors, user objectives and MCP responses.
- Decisive decision or feedback right: Model chooses next tool and arguments after observations, can stop or delegate a bounded reading task.
- Decision owner: Model executing in first-party `Agent.turn`/`dispatch`; installed harness executes selected calls.
- Supporting / enforcement mechanisms: LocalTools, approvals, MCP hub, append-only session, context compaction and goal mode.
- Closure path: User/goal → model inference → selected local/MCP tool → real result → appended observation → another model choice or answer.
- Boundary reachability: Supported CLI instantiates an actual model client and supplies tools; fake-model tests exercise the same loop, but paid-provider operation was not replayed here.
- Why this is / is not agent-owned: Model is able to choose an action and change it from observations; tool runtime and permissions do not own the choice.
- Evidence: [loop and dispatch](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/loop.py), [tools](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/tools.py), [session](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/session.py).
- Basis: First-party model→tool→observation→redecision implementation and reachable CLI.
- Confidence: High for code path; no paid-provider E2E claim.
- Caveats: Provider behavior, external MCP cognition and human permission remain outside first-party ownership.

## S2 — Coordination

- State: —
- Function: No ongoing regulation of contention between multiple autonomous operational S1 units is installed.
- Disturbance / variety regulated: Parallel demands or access conflict among distinct workers could arise, but `task` delegates a standalone reading request rather than balancing competing S1 commitments.
- Decisive decision or feedback right: Main agent may delegate; no independent conflict arbitration loop decides inter-worker priorities.
- Decision owner: Main S1 model for delegation and operator for permission; none for a separate S2.
- Supporting / enforcement mechanisms: Fresh-session `task` subagents, tool approval and session separation.
- Closure path: Main model→child task→child text→main model; no discovered contention→S2 arbitration→corrected peer commitments path.
- Why this is / is not agent-owned: Sequential or concurrent delegation is not itself feedback regulation between S1 units.
- Evidence: [subagent invocation](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/loop.py), [session](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/session.py).
- Basis: Bounded absence review of installed delegate and tool gates.
- Confidence: High.
- Caveats: User-built external MCP servers might coordinate their own agents outside this boundary.

### Absence scope

- Surfaces inspected: Child construction, parent dispatch, tools, permission gate, session lifecycle.
- Plausible first-party paths checked: Subagents as peers, concurrent tool contention, tool permission decision as arbitration, goal acceptance as conflict resolution.
- Why no material first-party path remains: The shipped path lacks observed inter-S1 disturbance and corrective balancing feedback between autonomous workers.

## S3 — Inside-and-now control

- State: —
- Function: No discretionary control of present resources, priorities and commitments across a whole set of autonomous S1 operating units.
- Disturbance / variety regulated: Goal turn/budget exhaustion, failed verification, tool risk and paused work.
- Decisive decision or feedback right: `/goal` performs fixed turn/budget/status gates and deterministic pass-or-retry; users choose the verification command and budget.
- Decision owner: Human operator owns scope/budgets; code enforces fixed conditions. Main model still owns task steps.
- Supporting / enforcement mechanisms: `run_goal` turn limit, spend meter, `verify`, permission approval and pause/resume.
- Closure path: Claimed completion→verification/reviewer gate→accept or return disagreement to same S1; no discretionary cross-unit resources/commitment management.
- Why this is / is not agent-owned: Strong operational gating does not itself imply a separate S3 decision authority over an S1 portfolio.
- Evidence: [goal and verification](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/loop.py), [permission gate](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/tools.py).
- Basis: Bounded current-control absence despite a real goal-acceptance gate.
- Confidence: Medium-high.
- Caveats: A separately deployed fleet supervisor could add S3, but is not a first-party standard mode here.

### Absence scope

- Surfaces inspected: Goal controller, reviewer return, step budget, subagent dispatcher and tool permission enforcement.
- Plausible first-party paths checked: Goal loop as S3 manager, cost limit as allocation, parent-delegation as portfolio supervision and reviewer gate as general manager.
- Why no material first-party path remains: These regulate one bounded task goal without a first-party autonomous owner able to revise whole-system resources and commitments across independently governed operations.

## S3* — Complementary audit

- State: A
- Function: Separate fresh-context inspection of a worker's completion claim using additional operational evidence before accepting a goal.
- Claim being audited: The main model declares that the current `/goal` objective is fully complete and supplies `goal_done` evidence.
- Ordinary reporting path: The worker's tool observations and self-reported completion argument arrive through its existing session and goal claim.
- Complementary access path: Fresh-context reviewer receives the objective and claim and can directly inspect current working-directory files using its own tool calls; optional shell verifier independently executes user-specified checks.
- Independence boundary: Distinct reviewer session and tool calls but the same first-party code/provider client and host permission policy; reviewer is not a separately governed institution.
- Who acts on findings: `Agent.run_goal` rejects unapproved completions, returns negative reviewer findings to worker and repeats until accepted or stopped.
- Disturbance / variety regulated: False self-reported completion, missing/incorrect local artifacts and a worker's biased summary.
- Decisive decision or feedback right: Reviewer independently reads working-directory evidence and returns `VERDICT: DONE` or rejection; goal controller accepts only a positive verdict after optional independent shell verification.
- Decision owner: Fresh reviewer model for the audit judgment; harness for deterministic acceptance and rework routing; operator for optional `verify` definition.
- Supporting / enforcement mechanisms: New reviewer session, actual LocalTools read/bash access, distinct review instructions, optional shell `verify`, literal verdict parser and rework prompt.
- Closure path: Worker `goal_done` claim→independent shell check when configured→new reviewer reads workspace→review judgment→goal controller acceptance or discrepancy returned to worker→corrective next turn.
- Why this is / is not agent-owned: Reviewer receives the goal and claim but has a genuinely separate workspace observation path and can reject the claim, rather than merely grading its prose; the gate only enforces the decision.
- Evidence: [REVIEW, `run_subagent`, `run_goal`, `verify`](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/loop.py), [reviewer false-claim test](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/tests/test_mini.py).
- Boundary reachability: Supported `/goal` invokes `verify` on `goal_done`; bundled tests cover rejection, retry and fresh reviewer tools, without requiring a hypothetical external plugin.
- Basis: Source-traced complementary evidence access, separate judgment, explicit corrective return in supported `/goal` mode.
- Confidence: Medium-high for installed bounded path, not independent external audit quality.
- Caveats: Same provider/client and workspace permissions; reviewer may be wrong, can be influenced by claim text, and is triggered by worker's completion claim. Independence is complementary to the worker's ordinary report, not organizational or institutional independence.

## S4 — Outside-and-then intelligence

- State: —
- Function: No autonomous prospective environment-scanning and strategy/adaptation cycle for the harness organization.
- Disturbance / variety regulated: Model availability, new skills and MCP sources, changing user needs and context size.
- Decisive decision or feedback right: Human configures external services and models; compaction summarizes current conversation and goal remains a current task.
- Decision owner: Operator for future capability selection, present S1 for ordinary research within user request.
- Supporting / enforcement mechanisms: Skills, MCP discovery, model presets, compaction, session resume and subagent research.
- Closure path: Updated config or task findings may change next operation; no future-environment forecast→strategic selection→adopted change in S3 operations.
- Why this is / is not agent-owned: Compaction/memory and delegated investigation support present tasks without autonomous mandate to reconfigure future capacity.
- Evidence: [loop/model config](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/loop.py), [external service hooks](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/ext.py).
- Basis: Bounded absence review.
- Confidence: High.
- Caveats: Individual agent may discuss future scenarios as an S1 user task.

### Absence scope

- Surfaces inspected: Model config, MCP and skill extensions, compaction, goal mode and subagent requests.
- Plausible first-party paths checked: Subagent as future scanner, memory as strategic learning, dynamic model choice as adaptation, compaction as future planning.
- Why no material first-party path remains: None owns prospective environmental intelligence and an authority-backed alteration of future organizational operating capacity.

## S5 — Policy and identity

- State: —
- Function: No distinct ultimate identity-policy or parent-governed mandate cycle in the installed task harness.
- Disturbance / variety regulated: Permission-sensitive requests, unsafe tool invocations and operator goal changes.
- Decisive decision or feedback right: Operator approves/denies risky actions and sets goal; optional cheap-model permission judge recommends local allowances under a fixed gate.
- Decision owner: External user and static permission rules; no independent legitimate S5 authority.
- Supporting / enforcement mechanisms: Approval prompts, optional permission judge, goal entry and local policy/configuration.
- Closure path: User/permission decision→tool allow/deny; no identity-level conflict→legitimate policy decision→returned organizational mandate.
- Why this is / is not agent-owned: Permission vetting is a task action constraint, not constitutive identity governance.
- Evidence: [permissions](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/tools.py), [goal setup](https://github.com/phuryn/mini-harness/blob/7ae9fca8221c55bd3c38697a61075357e1a94c26/src/mini/loop.py).
- Basis: Bounded absence review, including model-assisted permission path.
- Confidence: High.
- Caveats: External organization or human can exercise S5 outside this first-party product.

### Absence scope

- Surfaces inspected: Operator goal and permission interfaces, optional judge, core system prompt and configuration.
- Plausible first-party paths checked: `/goal` as mission policy, permission judge as guardian, static system prompt as constitution, human approvals as parent-assisted S5.
- Why no material first-party path remains: No first-party legitimate ultimate policy owner evaluates organizational identity conflicts and closes enforceable long-horizon mandates.

## Recursion

One model-directed task S1 can launch fresh subagent reading and independent reviewer runs, but the shipped runtime lacks a full higher-level set of governed S1 units. The S3* verdict is specifically the `/goal` audit-of-claims relation, not evidence of recursion or S3 control.

## Variety and escalation

Local/MCP tools and delegated reading amplify S1 variety. Permission gates, bounded steps, verification and an external reviewer attenuate unsafe/unverified completion. Negative reviewer findings return to the same S1 via rework; out-of-budget and blocked states pause for the human rather than enter a separate S4/S5 system.

## Evidence gaps

- Source and fake-model tests confirm installed wiring; provider-backed E2E and actual reviewer effectiveness were not run in this assessment.
- Reviewer independence is bounded: fresh context and workspace inspection, but shared provider/client and tool permissions; an independent human audit is not claimed.
- No operational evidence of autonomous inter-S1 balancing, S3 portfolio decision ownership, prospective adaptation or S5 legitimacy was identified within the pinned distribution.
