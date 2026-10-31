---
harness_id: your-claude-engineer
project_name: Your Claude Engineer
repository: https://github.com/coleam00/your-claude-engineer
review_ref: e7c064ac915cfeb29496c558795efa125a121863
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-31
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# Your Claude Engineer

## Review boundary

- System in focus: the first-party Python Claude Agent SDK long-running coding harness: entry point, iterative session/controller loop, orchestrator prompt, Linear/coding/GitHub/Slack subagent definitions, continuation state, security hooks and generated-project workspace.
- Purpose and identity: turn a user app specification into a sequence of tracked, implemented and browser-verified Linear features with optional GitHub/Slack updates.
- Relevant environment: human-provided app_spec.txt, Linear issue portfolio and META session issue, local git project, browser-rendered app, Claude Agent SDK/CLI and model provider, Arcade OAuth MCP gateway, optional GitHub/Slack.
- Standard-distribution boundary: documented Linux/macOS (or WSL) SDK client and Arcade/Linear configuration. GitHub and Slack are optional; their general external account features are not counted as first-party executive or policy ownership. No undocumented background fleet is assumed.
- Credited operating / distribution surfaces: first-party run_autonomous_agent fresh-session loop; client-registered subagent definitions and Task-tool delegation; whole-project Linear status return; mandatory next-session feature retest; model-directed implementation, correction and completion signaling.
- Adjacent first-party surfaces excluded from ownership: upstream SDK/Task dispatcher internals, external Linear/Arcade/Playwright servers, product/repo owner governance, demo screenshots and documentation-only capabilities. A separate independent S3* assessor is not inferred from local tests; the first-party source's cross-session browser retest is evaluated on its own actual path.
- First-party modes considered: first-run project bootstrap, continuation sessions until PROJECT_COMPLETE, app code work via coding subagent, optional GitHub/Slack notifications, and user-defined max iteration/security settings.
- Recursion level: one user-generated project with its Linear issue portfolio and coordinated coding/status tasks, not the business organization of the user or the external Linear service.
- Reviewed revision: e7c064ac915cfeb29496c558795efa125a121863.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

The executable demo calls agent.py run_autonomous_agent. Each iteration creates a fresh Claude SDK client, selects initializer or continuation prompt and invokes one orchestrator session, interpreting the model-emitted PROJECT_COMPLETE signal or restarting after an error. client.py registers four specialized SDK AgentDefinitions, places the orchestrator prompt into the live client and grants the Task interface through the SDK configuration. The orchestrator uses a Linear agent to obtain an issue-status/META account, a coding agent to work the project and run Playwright, and optionally GitHub/Slack agents for release/reporting. Critically, the shipped prompt requires browser retests of previously completed features **before** accepting new feature work, and returns failures to a fix step. This is a source-backed model-led executive/control and complementary sensing composition, but not proof that the broad Claude SDK or Linear itself is governed by this repository. The prompt explicitly enforces one issue at a time. A generated-project local git repo and sandbox/allowlist guard the work; no source-specific prospective organization redesign or ultimate identity-policy authority is shipped.

## Operational model

The main orchestrator model can choose and sequence project-wide issue work using current Linear counts, a next issue with full details and feedback from specialized agents. A separately invoked coding subagent independently sees the live application through Playwright and can reject an earlier Done claim before the orchestrator permits new work. The same coding role also implements features and fixes regressions, so independence here is a new Task context versus the prior session's reported state—not a third-party audit institution or different supplier. Context is explicitly handed between subagents by the orchestrator. The SDK implements generic tool execution; this repository specifies the model-facing role, current-state retrieval, retest obligation and rework return. Local security settings, Arcade OAuth and user specification provide boundaries and dependencies rather than self-authorized constitutional decisions.

## S1 — Operations

- State: A
- Function: implement a selected app feature through model-selected coding actions, browser tests and correction from tool feedback.
- Disturbance / variety regulated: incomplete feature requirements, changing code context, failing browser flows, runtime errors and interrupted long-running model sessions.
- Decisive decision or feedback right: coding model chooses concrete edits, commands, browser inspections and repairs from the orchestrator's issue context and observed tool outcomes.
- Decision owner: model-backed coding subagent executed through Claude Agent SDK; the first-party harness supplies role/prompt/tool configuration and continuity, not the SDK model's entire general capability.
- Supporting / enforcement mechanisms: generated project directory, first-party subagent definitions, Arcade tools, sandbox, bash pretool hook and retry/session boundaries.
- Closure path: app specification and Linear issue → orchestrator delegates detailed work → coding model inspects/edits/tests → Playwright or tool result → fix and verification → implementation evidence returned to orchestrator/Linear.
- Boundary reachability: autonomous_agent_demo.py invokes the first-party run loop; client.py wires AGENT_DEFINITIONS and built-in/Playwright tools into the SDK client; coding prompt directs real code/test actions.
- Why this is / is not agent-owned: implementation and repair actions depend on model interpretation of evidence; the shell allowlist, iteration delay and state markers cannot make those decisions alone.
- Evidence: [entry/session loop](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/agent.py#L173-L291), [SDK client and tool wiring](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/client.py#L146-L219), [specialized coding definition](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/agents/definitions.py#L100-L136), [coding prompt](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/prompts/coding_agent_prompt.md).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a live provider/Arcade/Playwright session was not run; SDK authentication and third-party success remain outside the evidence.

## S2 — Coordination

- State: —
- Function: no distinct mechanism is shown for attenuating a concrete disturbance between independently viable, competing operational S1 coding units.
- Disturbance / variety regulated: Linear, coding, GitHub and Slack agents exchange messages and roles, but no competing source-changing S1 claims or resource-contention disturbance is evidenced in the default sequential one-issue flow.
- Decisive decision or feedback right: no S2-specific allocation, negotiated conflict-resolution or revised reciprocal S1 commitments.
- Decision owner: none shown; orchestrator transfers context and orders specialized tasks, while SDK Task dispatch executes bounded child work.
- Supporting / enforcement mechanisms: role separation, Linear statuses, one-issue sequencing, local generated-project git and task handoff summaries.
- Closure path: orchestrator orders a single implementation issue and passes results to Linear/GitHub/Slack; this is cross-role task routing, not a source-backed interference-damping return between contending operational cells.
- Why this is / is not agent-owned: a model-chosen next issue belongs to whole-current S3 at this recursion; it does not itself close S2 competition among independent parallel work units.
- Evidence: [explicit one-issue-at-a-time rule and context transfer](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/prompts/orchestrator_prompt.md#L19-L46), [sequential feature workflow](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/prompts/orchestrator_prompt.md#L95-L149), [role definitions](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/agents/definitions.py#L100-L132).
- Basis: structural.
- Confidence: medium-high.
- Caveats: external SDK may support parallel Task calls, but this source does not demonstrate a distinct concrete S2 attenuation path for the shipped project workflow.

### Absence scope

- Surfaces inspected: orchestrator prompt, SDK agent registration, coding/Linear task roles, iteration loop and local project layout.
- Plausible first-party paths checked: concurrent delegation, shared Linear status, Git branch actions, handoff sequencing, duplicated assignments and cross-agent feedback.
- Why no material first-party path remains: context relay and one-at-a-time work remove the claimed simultaneous collision mode rather than instantiate an S2 policy/feedback owner.

## S3 — Inside-and-now control

- State: A
- Function: regulate the current **whole project** backlog, work priority and resumed progress across many feature issues/sessions.
- Disturbance / variety regulated: stale issue status, wrong next-work choice, incomplete previously Done features, session context resets and missing acceptance evidence.
- Whole-system current view: the model orchestrator requests Linear META context, counts across Done/In Progress/Todo and full details of the next issue, and reads the generated project's current state before deciding its continuation.
- Current-control decision scope: model selects whether to stop and repair regression or proceed to the next feature, delegates the issue and decides when to mark it Done based on required browser evidence.
- Decisive decision or feedback right: choose which pending portfolio issue should be worked next and overturn current progress when verification fails; issue transitions/continuation return to Linear and next fresh session.
- Decision owner: first-party prompted model orchestrator with live Linear agent and coding-agent feedback; neither static CLI loop nor Linear SaaS is credited with the model's project-wide decision.
- Supporting / enforcement mechanisms: META issue, .linear_project.json continuation marker, project progress summary, subagent tools, status counts, completion signal.
- Closure path: fresh session reads project/Linear whole-current status → orchestrator asks for retest → if failed directs correction, else chooses next issue → dispatches code and evidence → updates Linear Done/next state → next session refreshes the picture.
- Boundary reachability: the active client loads orchestrator_prompt.md and the iteration loop recreates a client per session, so this is not an unused design diagram.
- Why this is / is not agent-owned: the prompt gives the model discretion to choose/reprioritize actual current work and act on regression findings; the deterministic loop only reopens sessions and recognizes the completion token.
- Evidence: [orchestrator continuation and priority/verification steps](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/prompts/orchestrator_prompt.md#L95-L149), [whole-project completion decision](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/prompts/orchestrator_prompt.md#L219-L247), [fresh-session state and rerun](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/agent.py#L203-L291), [live prompt registration](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/client.py#L186-L219).
- Basis: structural.
- Confidence: medium.
- Caveats: the whole here is the one generated app's issue portfolio, not all of an enterprise's projects; the Linear account's actual data/permissions were not accessed.

## S3* — Complementary audit

- State: A
- Function: test prior completed-feature claims against actual running UI/interaction evidence before the S3 orchestrator takes new work.
- Disturbance / variety regulated: Linear may say Done while a previously working feature has regressed; summary or screenshot receipts can be stale or misleading.
- Decisive decision or feedback right: the model-driven coding subagent runs a fresh browser verification for 1–2 completed features and can return FAIL plus screenshots; orchestrator must suspend new work and request regression fixing.
- Decision owner: separately invoked coding verifier model for direct Playwright observations; orchestrator owns current feature plan and the fix order. This is the same coding **role** as producers, but a distinct subsequent Task invocation, not a third-party auditor.
- Supporting / enforcement mechanisms: mandatory pre-work verification gate, browser navigation/click/snapshot/screenshot tools, structured PASS/FAIL report, no-Done-without-screenshot rule.
- Closure path: prior Linear Done claim → new continuation requests browser retest → independent current app UI observations → FAIL evidence → orchestrator orders fix and re-test before new task → updated issue/current project status.
- Boundary reachability: orchestrator prompt makes retest mandatory on every continuation/new feature; coding subagent prompt defines a dedicated Verification Test task; Playwright tools are registered in the normal SDK client.
- Why this is / is not agent-owned: the model verifier decides whether the live UI corroborates the prior completion account; neither the prior producer's summary nor a deterministic status parser supplies this judgment.
- Claim being audited: previously marked-Done project features still work and are fit to leave closed.
- Ordinary reporting path: Linear Done status, prior implementation/test summary and saved project/meta issue context.
- Complementary access path: fresh coding verifier goes to running app via Playwright, exercises 1–2 completed features, observes screenshots/browser state and reports PASS/FAIL.
- Independence boundary: verifier is a fresh delegated Task/subagent context relative to prior iteration and S3 issue status, but reuses the 'coding' role/provider and is not organizationally independent; that narrower evidence-based independence is the claim credited.
- Who acts on findings: S3 orchestrator blocks next feature and asks coding agent to repair a reproduced regression; verification repeats before onward progress.
- Evidence: [mandatory verification and remedial gate](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/prompts/orchestrator_prompt.md#L50-L69), [continuation's direct retest and failure return](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/prompts/orchestrator_prompt.md#L95-L115), [coding agent browser verification protocol](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/prompts/coding_agent_prompt.md#L38-L75), [tool registry](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/client.py#L55-L75).
- Basis: structural.
- Confidence: medium.
- Caveats: prompts specify behavior; no captured live regression was reproduced in this review. The same coding agent role is reused, so independence is bounded to fresh contextual sensing versus S3/earlier Done account, not external independent peer review.

## S4 — Outside-and-then intelligence

- State: —
- Function: no shipped organizational loop selects durable prospective changes to the harness's future capabilities from external environmental intelligence.
- Disturbance / variety regulated: user-specified app goals and task regressions are operations/current control, not an ongoing externally informed future adaptation mandate.
- Decisive decision or feedback right: none beyond issue-by-issue project implementation and user-edited prompts/spec/config.
- Decision owner: user supplies app specification and permission settings; orchestrator chooses present feature priority but does not autonomously revise the harness's strategic operating design.
- Supporting / enforcement mechanisms: app_spec.txt, developer-editable prompt files, Linear backlog, META continuation memory and model configuration flags.
- Closure path: spec/backlog → present coding and feature selection; no external change signal → strategic option → selected lasting future operating-capability shift is shown.
- Why this is / is not agent-owned: long-running context and future work items are ordinary S1/S3 continuity, not independent S4 environmental search/adaptation.
- External distinction: third-party project requirements and Linear status are task inputs, not autonomous environmental foresight.
- Future / prospective distinction: an unfinished backlog is a plan for task execution, not adaptation of the executing organization's future structure.
- Evidence: [project specification and prompt customization](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/README.md), [current issue workflow](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/prompts/orchestrator_prompt.md#L95-L149), [session continuity](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/agent.py#L203-L291).
- Basis: structural.
- Confidence: medium-high.
- Caveats: a user can change the prompts or request a different application; that is external reconfiguration, not a built-in strategic return.

### Absence scope

- Surfaces inspected: app specification/initializer, continuation prompts, agent definitions, session state, config and external integration setup.
- Plausible first-party paths checked: planning of future Linear issues, META memory, user prompt customization, model switching and progress learning.
- Why no material first-party path remains: all paths serve current task delivery or human customization without a distinct outside-future intelligence decision/adoption loop.

## S5 — Policy and identity

- State: —
- Function: no first-party autonomous ultimate-policy or legitimate organizational identity owner closes an S5 constitutional return.
- Disturbance / variety regulated: tool permission, command safety, OAuth authorization and product scope are externally pre-set restrictions.
- Decisive decision or feedback right: none for determining the project's ultimate legitimate purpose or amendments to binding identity/policy.
- Decision owner: project owner, external credentials administrator and fixed script/security policies govern these matters.
- Supporting / enforcement mechanisms: Claude SDK sandbox, file tool allowlist, bash PreToolUse hook, Arcade OAuth, fixed app_spec and allowed-command list.
- Closure path: configuration constrains tool execution; no first-party deliberation over constitutional goals and downward reauthorization is shipped.
- Why this is / is not agent-owned: enforcement of static user/configuration rights is not policy-identity formation.
- Evidence: [security and permission construction](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/client.py#L86-L113), [SDK tool/hook invocation](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/client.py#L146-L219), [first-party bash guard](https://github.com/coleam00/your-claude-engineer/blob/e7c064ac915cfeb29496c558795efa125a121863/security.py).
- Basis: structural.
- Confidence: high within reviewed boundary.
- Caveats: external user/organization policy is excluded from this system in focus.

### Absence scope

- Surfaces inspected: security hook, allowed commands, SDK permissions, app spec, model settings and integration authentication.
- Plausible first-party paths checked: sandboxing, OAuth grants, identity/config changes, issue acceptance and completion signal.
- Why no material first-party path remains: they constrain task operations but do not decide constitutional identity or ultimate legitimate policy.

## Recursion

The viable unit is the one project portfolio. Coding Task calls perform S1 operations; the orchestrator's Linear-wide issue-status/prioritization is S3 at this recursion. A new session's coding verifier independently challenges previously Done issues from actual UI evidence for S3*. Linear, GitHub and Slack delegates are differentiated support roles; their mere existence does not supply competing independently viable S1 units for S2. The parent/user fixes task purpose and tool rights. Other projects, the Claude SDK platform and the provider organization are outside this recursion.

## Variety and escalation

- Prior completion status is treated as revisable: mandatory browser retests can block next work and call for correction.
- The orchestrator chooses a next issue from whole current Linear status and passes full context rather than asking children to reconstruct inaccessible memory.
- Fresh SDK sessions bound context exhaustion; errors cause an ordinary retry in the next session, and max_iterations is user-controlled.
- GitHub/Slack functions are optional and gated by Arcade OAuth/account configuration; missing credentials do not authorize workaround.
- Sandbox/allowlist constrains shell actions without becoming S5 governance.
- No model/Arcade/Playwright execution or external side-effect was performed during this assessment.

## Evidence gaps

- Source-first review at the exact pinned public commit. No external Claude SDK credentials, Linear/Arcade workspace, browser app or independent agent E2E run were available or invoked.
- The source-only security unit test was attempted but could not import claude_agent_sdk (dependency absent in review environment); no test pass is claimed.
- S3* is bounded: current-task coder self-tests do not count; the credited path is a new continuation's direct Playwright retest of an earlier Done issue against the S3/Linear progress account.
- Public source and prompt wiring establish reachability; they do not prove the actual frequency or quality of regression detection in deployments.
- Upstream SDK/Arcade/Linear internals and human ultimate-purpose decisions are outside first-party ownership.
