---
harness_id: quickcode
project_name: QuickCode
repository: https://github.com/devincii-io/QuickCode
review_ref: ac776f76b0243e248ff389c4b2dbdfc70475cce2
reviewed_at: 2026-11-06
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: —
autonomy_s4: —
autonomy_s5: —
---

# QuickCode

## Review boundary

- System in focus: the shipped QuickCode 2.7 local-first Python coding-agent backend, user-facing loopback web application and headless runner, including the first-party agent loop, built-in/custom child-agent delegation, optional background jobs and git-worktree isolation, tools, permissions, task board, session replay, hooks, plugin composition and review UI.
- Purpose and identity: carry out operator-directed repository analysis, edits, commands, testing and iterative coding tasks through model-selected local tools while exposing auditable interactions and protecting user authority.
- Relevant environment: developer instructions, project files and branches, concurrent coding children, tool/test errors, model-provider responses, tool/plugin configuration, human approvals and context/permission constraints.
- Standard-distribution boundary: `quickcode/cli.py` and `webapp.py` start first-party FastAPI/pywebview or headless sessions; `session/assemble.py` wires `AgentInstance` and `core/loop.py` to first-party registered tools, configured provider and optional agent children. OpenRouter/Anthropic/OpenAI-compatible inference, external MCP servers, the user's target project, Git itself and the human operator are environment, not outsourced agent-harness owners.
- Credited operating / distribution surfaces: `quickcode/core/{agent,loop,permissions,history,hooks,tasks}.py`, `subagents/{runner,worktree,jobs,definitions}.py`, `tools/{agent,agent_jobs,send_message,task,plan,read,write,edit,bash}.py`, `kernel/`, `session/`, `server/`, `security/`, `checkpoints/`, and supported CLI/web UI paths.
- Adjacent first-party surfaces excluded from ownership: GitHub CI, PyInstaller/installer and release scripts, project-development tests, docs/archive plans and future teammate-mode concepts. Tests corroborate the shipped worktree collision guard but are not a separate S3* auditor in an end-user agent session.
- First-party operating modes considered: interactive multi-project local web UI with independent conversation panes; single-turn headless `-p`; `plan/ask/auto-edit/dontask/yolo` authorization; built-in `explore` and `general` children, optional user-defined agents, background collection, `send_message` resumes and opt-in per-writer `isolation: worktree`.
- Recursion level: one coding conversation with its delegated operational children, whose overlapping project edits may interfere; independent user conversations and the product's maintainer team are not part of a hypothetical shared higher-level viable organization.
- Reviewed revision: `ac776f76b0243e248ff389c4b2dbdfc70475cce2`.
- Observation date: 2026-11-06.
- Generated Profile version: `0.2.4`.
- Generated Methodology version: `0.3.7`.
- Current Profile version: `0.2.4`.
- Current Methodology version: `0.3.7`.

## Repository architecture

The first-party `AgentInstance` owns a context/history, tool registry, ledger and event bus. Its asynchronous turn loop sends task/system context to a configurable model, receives tool calls, validates/authorizes/executes them, pushes results back and repeats. Read-only tool calls can run in parallel; writes and side-effecting tools form execution barriers. A local FastAPI server and vanilla-JavaScript web UI present chat, trajectory, approvals, sessions, agent panes and tools. The same session assembly feeds a headless entry point; append-only JSONL events support resume/replay.

Delegation creates child `AgentInstance` loops with fresh contexts, chosen model, permissions capped by the parent and agent definition, depth/count bounds and sanitized summarized results. A child may run detached; its persistent in-process job handle can be observed via `agent_status`, collected by `agent_result`, and resumed by `send_message`. These are genuine subordinate operating loops rather than merely named tool functions.

Most distinctive is the optional worktree isolation path. The code identifies a concrete inter-agent failure mode: concurrent writers of the same working-tree file can overwrite or observe each other's half-edited state. With `isolation: worktree`, the harness creates a separate Git checkout and permission root per child, runs its tools there, settles the result into its own branch and returns that branch to the spawner. The user's working tree is unchanged until a later authorized integration. The repository has a direct two-parallel-writer test where both children edit `a.txt` independently and the parent file retains its initial value. The controlling choice to request isolation may be model-selected or baked into an agent definition, but the decisive anti-collision relation is implemented by deterministic worktree separation: S2 is credited at **C** rather than automatically transferring autonomous S2 ownership from the model's task delegation.

The documented teammate mode (peer messaging, file-locked task claims, lead review and coordinated task-board agents) is expressly **not shipped** at the frozen ref. The persisted task board currently serves solo work and dependency blocking; it does not donate a second future coordination design to this assessment.

Primary source:

- [Shipped vs planned boundary](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/docs/ROADMAP.md)
- [Agent/tool feedback loop](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/core/loop.py)
- [Subagent execution and permission ceilings](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/subagents/runner.py)
- [Inter-agent worktree isolation](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/subagents/worktree.py)
- [Two-writer conflict isolation test](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/tests/test_subagent_worktree.py)
- [Product subagent design with built/planned flags](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/docs/AGENTS.md)

## Operational model

A primary model-backed coding agent responds to a developer task by selecting code/tool actions, observing their results and changing course. It can run one or several children on separate model contexts for parallel research or coding. A background job may complete later and be collected with a status/result tool; the same child can receive follow-up work. Deterministic policy gates every concrete side effect, while the human may approve protected actions and plan transitions. Isolation of writer children is an actual optional inter-S1 anti-collision operation, not an entire team-governance layer or automatically agent-owned S3.

## S1 — Operations

- State: A
- Function: conduct iterative software development tasks against real project files, process output and external task observations, through main and subordinate model-directed loops.
- Disturbance / variety regulated: changing user goals, unknown source code, tool/test errors, provider inconsistencies, large context, side-effect refusals and delegated subtask results.
- Decisive decision or feedback right: select the next concrete tool/arguments, child task/model, correction after failed observations and whether the task is answered.
- Decision owner: the main model-backed `AgentInstance` and genuinely separate child model-backed `AgentInstance` loops for their delegated local outcomes.
- Supporting / enforcement mechanisms: provider adapters, tool registry/schema, permissions and hook narrowing, execution barriers, event bus, context compaction, session log, child caps and result sanitization.
- Closure path: user's task and project state → model-selected tool or child request → authorized execution → actual tool/child result → model replanning, additional action or final output.
- Boundary reachability: the shipped web/headless session assembler starts `AgentInstance` and the first-party loop, while `subagents/runner.py` constructs real child loops from its `agent` tool.
- Why this is / is not agent-owned: with model actors removed, the scripted tool/provider adapters and permission engine cannot select task-specific edits or iterative steps; the agent performs that decision work.
- Evidence: [`core/loop.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/core/loop.py); [`core/agent.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/core/agent.py); [`subagents/runner.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/subagents/runner.py).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: external provider credentials are needed for live inference; the operator may deny side effects and sibling writing needs a deliberate scope/cap.

## S2 — Coordination

- State: C
- Function: attenuate a concrete interference mode between multiple simultaneous S1 child writers working against a shared project's files.
- Distinct S1 units: at least two independently running `general` model-backed child agents, each selecting edits in its local project view; the integration test exercises `general-1` and `general-2` simultaneously.
- Inter-S1 disturbance: both autonomous writers would otherwise edit the same `a.txt` checkout, with lost/overwritten content and unstable builds from intermediate state.
- Attenuating coordination relation: optional worktree mode allocates a separate checked-out Git tree, tool cwd and permission root to each child, retaining its changes on a distinct branch instead of writing to a shared working tree.
- Feedback into subsequent S1 behaviour: each child executes and verifies against its isolated state; its settled branch and summary return to the spawner, which can decide when/how to merge reviewed changes. Concurrent child work ceases to corrupt the parent's active checkout.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: it is a first-party, tested mitigation of the specific interference arising **between two autonomous file-writing work cells**, not just message transport or assignment. The two-writer test establishes the avoided collision and surviving independent branch outcomes.
- Disturbance / variety regulated: two children reading/editing the same file in one working tree could trample one another or run tests against incomplete edits, producing oscillating or inconsistent shared state.
- Decisive decision or feedback right: select whether a writer works in a separate checkout and whether its settled branch should later be integrated. The spawner or agent definition chooses the isolation option, but the direct interference-attenuating state separation is deterministic worktree ownership.
- Decision owner: the spawner/model or configured agent definition supplies the requested work mode; first-party `worktree.py` constructs the actual distinct checkout and stable branch result. The autonomous degree of the S2 conflict regulation is not promoted beyond constructor-supported C on delegation alone.
- Supporting / enforcement mechanisms: `isolation: worktree` allow/require settings, per-child `cwd` and permission root, Git worktree setup/cleanup, protected `.quickcode/worktrees`, compare-and-swap branch settling and branch-result envelope.
- Closure path: concurrent writer work is identified as collision-prone → opt-in isolation gives each writer a separate checkout → both child modifications settle as separate branches → parent receives branch identities and can choose reviewed integration rather than having interleaved edits corrupt its working tree.
- Boundary reachability: `subagents/runner.py::_prepare_child` invokes worktree probe/plan; child execution uses the worktree environment; `worktree.py` opens and settles it. `tests/test_subagent_worktree.py::test_parallel_writers_to_the_same_file_cannot_trample_each_other` tests two real concurrent writers and asserts two branch outcomes plus an unchanged parent file.
- Why this is / is not agent-owned: the model can elect isolation; removing that agent while preserving a configured `isolation: worktree` definition retains the collision-attenuating checkout mechanics. This is a positive S2 function with deterministic/constructor-owned enforcement, not evidence of agent negotiation or team-level autonomous policy.
- Evidence: [`worktree.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/subagents/worktree.py); [`runner.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/subagents/runner.py); [`test_subagent_worktree.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/tests/test_subagent_worktree.py); [`docs/AGENTS.md`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/docs/AGENTS.md).
- Basis: explicit + tested structural.
- Confidence: high for the supported opt-in path.
- Caveats: no automatic merge or general multi-agent negotiation is claimed; the isolation is optional, requires a Git repository and does not OS-sandbox external plugins/MCP/hooks. Teammate-mode file-locked claims are unbuilt.

## S3 — Inside-and-now control

- State: —
- Function: no established whole-system current resource/priority/commitment regulation across independent operational units beyond one conversation's task-decomposition and job housekeeping.
- Disturbance / variety regulated: detached child lifecycle, limits and missed reports are tracked locally; no shared portfolio of S1 operational commitments governed by a distinct whole-system controller is demonstrated.
- Decisive decision or feedback right: main agent can inspect child statuses and send follow-ups; no evidenced whole-system resource bargaining, exception intervention or cross-unit accountability mandate distinct from current task assignment.
- Decision owner: not established at S3.
- Supporting / enforcement mechanisms: `agent_status`, `agent_result`, `send_message`, max-depth/total/parallel caps, uncollected-job reminders, usage ledger and solo task board.
- Closure path: child status/results feed the parent's next coding decision; job caps constrain active work. The loop is local orchestration rather than a demonstrated metasystem-wide performance/resource control relation.
- Why this is / is not agent-owned: actor-chosen delegation and follow-up can be useful operational steering, but the current shipped system lacks teammate leadership, atomic joint claims and a distinct whole-system current-control decision right; static caps do not transfer S3 autonomy.
- Evidence: [`tools/agent_jobs.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/tools/agent_jobs.py); [`tools/send_message.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/tools/send_message.py); [`subagents/jobs.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/subagents/jobs.py); [`core/tasks.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/core/tasks.py).
- Basis: explicit + structural absence review.
- Confidence: medium-high.
- Caveats: partial worker status and follow-up control are present; neither should be erased or elevated into an unshipped whole-system governance capability.

### Absence scope

- Surfaces inspected: delegated-job status and collection, follow-ups, caps/ledger, solo board, teammate design/roadmap, per-session permissions and orchestration prompt.
- Plausible first-party paths checked: aggregate current work commitments, resource bargaining, priority changes across active independent workers, automatic exception escalation and current-system managerial intervention.
- Why no material first-party path remains: all shipped controls either serve the parent conversation's ongoing task or enforce static resource limits; design-only teammate coordination is not credited.

## S3* — Complementary audit

- State: —
- Function: no independent complementary audit channel challenging ordinary S1/S3 claims and returning a distinct corrective supervisory finding is established.
- Disturbance / variety regulated: code errors and risky side effects are observable through ordinary tests, trajectory logs, review panes, checkpoints and operator approvals, not through an independently governed spot-audit path.
- Decisive decision or feedback right: no dedicated independent auditor adjudicating evidence against producer claims with controlled correction return.
- Decision owner: not established.
- Supporting / enforcement mechanisms: full transcript/Trajectory, permission traces, command hooks, test execution, diff/rewind, read-only `explore` children and ordinary model feedback.
- Closure path: ordinary tool/test results inform the same coding loop; user can inspect records and manually act. A child may be prompted to review, but the supported design supplies generic subordinate operations, not a production-wired independent complementary audit and supervisory closure.
- Why this is / is not agent-owned: user-visible observability and a possible generic reviewer task are not independent audit ownership; the producer still frames/delegates the child task and receives a routine report.
- Evidence: [`core/loop.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/core/loop.py); [`subagents/runner.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/subagents/runner.py); [`docs/AGENTS.md`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/docs/AGENTS.md); [`README.md`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/README.md).
- Basis: structural absence review.
- Confidence: medium-high.
- Caveats: transparent event capture and safe rewind are valuable safety controls; they do not become S3* because they are richly displayed.

### Absence scope

- Surfaces inspected: trajectory/session log, hooks, model and child tasks, optional agent definitions, tests/Git views and checkpoint recovery.
- Plausible first-party paths checked: a separate raw-artifact reviewer of producer claims, independent adversarial sampling, audit findings and return path into a supervisory correction.
- Why no material first-party path remains: no such first-party complementary audit role/independent sampling contract is wired to the production loop; task-level verification remains on the normal producer path.

## S4 — Outside-and-then intelligence

- State: —
- Function: no prospective external-environment intelligence / future-option development linked back into current organizational capability control is established.
- Disturbance / variety regulated: changing model providers, network information, plugins and available updates are handled through current configuration or task tools, not an autonomous future capacity program.
- Decisive decision or feedback right: no agent-owned future strategy or option/adaptation decision returned to S3.
- Decision owner: not established.
- Supporting / enforcement mechanisms: pluggable providers/tools, user- and project-authored prompt/agent/tool definitions, WebFetch/search, plugin composition and six-hour update polling.
- Closure path: user may change plugins/models or install an update; an agent may search for present task facts. No externally prospective option → approved future capability change → current-operation feedback path is shown.
- Why this is / is not agent-owned: external search, editable prompts, context compaction, adaptive task planning and release checks alone are not S4 organizational future intelligence.
- Evidence: [`kernel/registry.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/kernel/registry.py); [`kernel/composition.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/kernel/composition.py); [`update.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/update.py); [`docs/ROADMAP.md`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/docs/ROADMAP.md).
- Basis: structural absence review.
- Confidence: high.
- Caveats: a user can extend capabilities with plugins; this is customization, not a demonstrated agent-owned organizational adaptation loop.

### Absence scope

- Surfaces inspected: plugin kernel, authored agent/provider/tool settings, runtime/model choice, update checker, web search, context and governance of composition.
- Plausible first-party paths checked: autonomous trend monitoring, future option development, self-reconfiguration proposals with feedback into current capability control.
- Why no material first-party path remains: the shipped mechanisms execute present tasks or implement human-configured capability settings; no S4 prospective governance loop closes.

## S5 — Policy and identity

- State: —
- Function: no ultimate organizational identity/mission policy decision, nor legitimate parent-ratified durable change to that policy, is established in the standard runtime.
- Disturbance / variety regulated: risky tools, project trust, protected paths, privileged shell syntax, agent capability ceilings and untrusted plugin declarations are bounded by human consent and static code constraints.
- Decisive decision or feedback right: operator grants individual actions/trust and writes configuration; no agent or legitimate parent makes an identity-level policy judgment and returns it to govern future mission.
- Decision owner: not established for S5; human operator and authored policy are current-action/permission authorities.
- Supporting / enforcement mechanisms: `plan/ask/auto-edit/dontask/yolo`, deny-first `PermissionEngine`, locked mutability tiers, plugin and project trust, child cap inheritance, protected-path prompts and command circuit breakers.
- Closure path: requested risky action or project code execution → deterministic rule evaluation/trust check → user approval or denial → this action permitted/blocked. No identity-level constitutional issue returns as a durable governing S5 decision.
- Why this is / is not agent-owned: the model cannot override locked policy or elevate its own capability; removing it leaves the static/human authorization path intact. Prompt sections and metadata called policy are not mission/identity adjudication.
- Evidence: [`permissions.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/core/permissions.py); [`kernel/spec.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/kernel/spec.py); [`security/trust.py`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/quickcode/security/trust.py); [`docs/PERMISSIONS.md`](https://github.com/devincii-io/QuickCode/blob/ac776f76b0243e248ff389c4b2dbdfc70475cce2/docs/PERMISSIONS.md).
- Basis: explicit + structural absence review.
- Confidence: high.
- Caveats: action approval and strong policy enforcement are real and valuable but do not automatically meet S5 at this recursion level.

### Absence scope

- Surfaces inspected: authorization modes, user/project trust, plugin mutability, composition ceilings, human plan/tool approvals, model/system prompt and runtime event log.
- Plausible first-party paths checked: constitutional/identity change, legitimate parent deciding an ultimate-policy issue, durable policy return, and identity-bound self-governance.
- Why no material first-party path remains: shipped paths are action/configuration authorization under static policy, not ultimate purpose/identity deliberation with parent-level decision closure.

## Recursion

The primary conversation can instantiate independent-context subagent work cells, including concurrent writer children. The optional worktree isolation forms an evidenced local S2 anti-interference channel; it does not imply that the whole conversation has established distinct S3/S4/S5 or that it is a recursively viable team. Other independent web panes belong to user-directed sessions, while the planned peer-team layer is not shipped.

## Variety and escalation

The agentic tool loop, plugins, model selection, parallel child fan-out, background jobs and web access amplify task response variety. Permission rules, project trust, tool validation, child scopes, report sanitization, depth/count/parallel caps, context management and user approvals attenuate risk. The opt-in separate Git worktrees directly attenuate a verified inter-S1 shared-file disturbance; child status/results return to the spawner. None of these automatically confers ultimate policy authority or independent audit rights.

## Evidence gaps

Source-first static review of the frozen Python code and shipped modes, including the actual worktree-collision integration test, not a live OpenRouter/Anthropic inference task. The test file is source evidence; it was not executed as part of this assessment. Worktree isolation requires the option to be selected or set by an agent definition and a suitable Git repository; no default isolation for every child or automatic merge is claimed. Peer teammate mailboxes/atomic claiming and lead review are explicitly unimplemented and excluded. No distinct producer-independent reviewer, future capability adaptation or ultimate-policy decision loop was found in the bounded standard distribution.

## Assessment summary

QuickCode has a genuine first-party coding-agent tool/observation loop and real subordinate model-directed operations (**S1=A**). Its opt-in, tested worktree isolation prevents concrete concurrent-writer interference (**S2=C**), while neither that constructor mechanism nor background-job controls establish whole-current S3, independent S3*, prospective S4 or identity-policy S5 closure at this boundary.

Proposed vector: **`A · C · — · — · — · —`**.
