---
harness_id: novacode
project_name: NovaCode
repository: https://github.com/gczhuang-cmd/NovaCode
review_ref: 34a2d555a530120fd6241f7065d49390e52f3573
reviewed_at: 2026-10-30
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: A
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# NovaCode

## Review boundary

- System in focus: the packaged NovaCode terminal coding harness, including its optional first-party Team/Coordinator and built-in skill modes.
- Purpose and identity: perform repository coding work with model-directed tools and collaborating operational agents.
- Relevant environment: local Git repositories, filesystem and shell, model providers, MCP servers and a terminal operator.
- Standard-distribution boundary: the Python package installed through pyproject.toml and launched through novacode.cli; optional shipped modes count when wired by its CLI, not hypothetical third-party agents.
- Credited operating / distribution surfaces: src/novacode/agent, cli.py, team, coordinator, worktree, skills, command and tui. The built-in review skill is packaged by pyproject.toml.
- Adjacent first-party surfaces excluded from ownership: tests and chapter development plans/checklists corroborate implementation but do not supply external owners; upstream contributor governance and future development are outside the installed harness.
- First-party operating / deployment modes considered: ordinary interactive single-agent run, foreground/background subagents, Team with in-process or terminal-pane backends, opt-in Coordinator, built-in fork review, operator permission/plan modes.
- Recursion level: one NovaCode session/team; workers are operational cells, not automatically recursively viable systems.
- Reviewed revision: `34a2d555a530120fd6241f7065d49390e52f3573`.
- Observation date: 2026-10-30.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

Python/asyncio joins a provider stream, conversation, registered filesystem/shell/MCP tools, permission engine, compaction and session persistence. The model requests actions; tool results return to its conversation before the next request. Subagents can run in fresh or inherited contexts and background tasks. Team extends this into independent conversations and worktrees, persistent membership/task state and file mailboxes with atomic updates. Lead notifications wake a new model turn. Optional Coordinator restricts direct editing while retaining team control and shell. Plan-required members remain restricted until the Lead's returned approval. Skill execution supports a separate model conversation and tool whitelist; the packaged review skill uses that path with no parent context. Memory is session/working-context maintenance, not a future-facing adaptation authority.

Primary architecture evidence: [README](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/README.md), [CLI wiring](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/cli.py#L150-L245), [agent loop](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/agent/__init__.py#L260-L518).

## Operational model

The main coding agent and independently executing Team workers produce repository changes and investigations. Providers infer decisions; Python, Git, mailboxes, locks and permissions execute or constrain them. The installed Team Lead can inspect current tasks, assign/revise commitments and send returned plan decisions. Worktree isolation supplies a specific deterministic construction path for attenuation of concurrent worker edits. The independent-context review skill checks raw current code rather than inheriting the producer's narrative. The operator chooses credentials, tasks and modes; these choices alone are not higher-function parent governance.

## S1 — Operations

- State: A
- Function: autonomous repository investigation and modification.
- Disturbance / variety regulated: code defects, command results and changing local file contents.
- Decisive decision or feedback right: choose the next tool action or final response after observing prior results.
- Decision owner: the main or worker model agent.
- Supporting / enforcement mechanisms: provider adapters, tool registry, permission engine, shell and conversation storage.
- Closure path: model tool calls execute and results are appended to the conversation for the next request.
- Boundary reachability: installed CLI registers the tools and constructs the first-party Agent; Team launches use that same implementation.
- Why this is / is not agent-owned: removing model discretion leaves execution/permission machinery without the coding decisions.
- Evidence: [loop and result feedback](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/agent/__init__.py#L385-L518), [worker construction](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/agent/agent_tool.py#L179-L274).
- Basis: structural.
- Confidence: high.
- Caveats: source-backed availability, not successful provider-backed execution or coding performance.

## S2 — Coordination

- State: C
- Function: keep independent coding cells from overwriting one another's working files.
- Disturbance / variety regulated: concurrent agents editing a shared checkout and reading stale parent paths.
- Decisive decision or feedback right: select isolated worker execution and a later integration/conflict-resolution policy.
- Decision owner: shipped worktree construction policy establishes separate execution contexts; a developer/operator must compose the discretionary coordination/integration actor beyond the enforced isolation path.
- Supporting / enforcement mechanisms: Git worktrees, per-agent cwd injection, branch naming, change-preserving cleanup and mailbox/file locks.
- Closure path: creation gives the worker a separate checkout and explicit local reread instruction; its tools run in that cwd and retained changes/branch return to the parent.
- Boundary reachability: AgentTool's worktree branch and Team spawn explicitly call the supplied Worktree Manager; this is not a generic mailbox inference.
- Why this is / is not agent-owned: worker isolation follows a preselected implementation/definition; no independent agent is shown owning the full interference-specific coordination policy merely because a Lead delegates.
- Distinct S1 units: concurrently runnable Team members or parent and background operational agents.
- Inter-S1 disturbance: shared-file write collision and stale reads between their repository operations.
- Attenuating coordination relation: separate per-worker Git worktrees with cwd-context injection and preserved-result reporting.
- Feedback into subsequent S1 behaviour: each worker is told to reread locally and operates in the isolated directory; the parent receives the retained worktree identity.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: the implementation changes the actual editing substrate to prevent cross-worker overwrite; task dependencies and messaging alone are not credited.
- Evidence: [worktree execution and notices](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/agent/agent_worktree.py#L16-L48), [Team worktree creation](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/team/spawn.py#L91-L148), [stated concurrency purpose and integration boundary](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/docs/ch15/spec.md#L7-L31).
- Basis: structural.
- Confidence: medium.
- Caveats: worktrees do not resolve semantic merge conflicts; specification claims of autonomous convergence are not promoted into an independently established S2=A loop.

## S3 — Inside-and-now control

- State: A
- Function: regulate current team commitments and permit or withhold worker implementation on behalf of the session.
- Disturbance / variety regulated: unfinished/blocked team work, member readiness and proposed plans that need revision before changing code.
- Decisive decision or feedback right: the Lead reads team state, changes assignment/status/dependencies and approves or rejects a member plan with feedback.
- Decision owner: the model-driven Team Lead.
- Supporting / enforcement mechanisms: persistent task store, mailbox delivery, wakeup, lead-only approval check and worker permission/tool filtering.
- Closure path: task/member notifications reach a Lead turn; its structured approval returns through the mailbox and changes worker permission mode/tools, while rejection requests a revised plan.
- Boundary reachability: CLI registers TeamTask*/TeamSendMessage and Team Agent spawn; TUI starts lead-mail consumption and wakeup. Optional Coordinator is supplied with these same tools.
- Why this is / is not agent-owned: Python enforces who may approve and applies the result; it does not choose whether a plan should be approved or what current commitment should change.
- Whole-system current view: current Team tasks/status/assignees/dependencies, membership and member messages/idle notifications.
- Current-control decision scope: current team work allocation and implementation permission, not identity or prospective strategic policy.
- Evidence: [CLI registration](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/cli.py#L150-L175), [task revision](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/team/tools/team_task_update.py#L24-L90), [Lead authority and delivery](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/team/tools/team_send_message.py#L90-L148), [returned plan effect](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/agent/team_mailbox.py#L31-L78), [Lead feedback](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/tui/leadmail.py#L15-L37).
- Basis: structural.
- Confidence: medium.
- Caveats: cooperative agent judgment with bounded telemetry, not proof of global optimization; generic user approval and /team kill do not independently establish a parent S3 mode.

## S3* — Complementary audit

- State: A
- Function: optional source-grounded challenge to the coding session's changes.
- Disturbance / variety regulated: errors/security defects omitted from the producer's account.
- Decisive decision or feedback right: select and inspect raw changed files and judge defects in an independent-context review.
- Decision owner: the forked review model agent.
- Supporting / enforcement mechanisms: built-in skill catalog, fork executor, fresh Conversation, tool whitelist and report insertion.
- Closure path: the review agent's final findings are inserted into the main conversation, available to subsequent coding turns and operator control.
- Boundary reachability: the packaged built-in review skill is registered through the CLI skills path and executed by the shipped fork executor; no custom external reviewer must be built.
- Why this is / is not agent-owned: deterministic fork/return machinery transports the independently reasoned findings rather than choosing defects or severity.
- Claim being audited: the correctness and safety of repository changes made by the coding session.
- Ordinary reporting path: the producer's main conversation/final narrative and tool reports.
- Complementary access path: fresh reviewer uses git diff/status and direct file/reference reads.
- Independence boundary: fork_context none, separate conversation, explicit no-modification instruction; same provider/host is not a blind external audit.
- Who acts on findings: parent coding session/operator; report enters subsequent control without automatic acceptance or guaranteed remediation.
- Evidence: [packaged review definition](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/skills/builtin/review/SKILL.md#L1-L22), [fresh fork and return](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/skills/executor.py#L46-L117).
- Basis: structural.
- Confidence: medium.
- Caveats: optional bounded code audit; bash whitelist is not a security sandbox, and no independent human audit is claimed.

## S4 — Outside-and-then intelligence

- State: —
- Function: no supplied external/prospective adaptation loop into present harness capability established.
- Disturbance / variety regulated: memory/context and current task information, rather than future environmental change at this recursion.
- Decisive decision or feedback right: none evidenced for prospective capability adaptation.
- Decision owner: not established for S4.
- Supporting / enforcement mechanisms: memory storage, compaction, skills/MCP loading and task planning.
- Closure path: local context reuse is present; external distinction to adaptation option to current capability closure is absent.
- Why this is / is not agent-owned: research/plan roles and persistence are not sufficient evidence of that organizational function.
- Evidence: [runtime context state](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/agent/runtime.py#L20-L66), [Coordinator current-task phases](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/coordinator/__init__.py#L26-L38), [architecture](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: an operator can extend skills or choose new providers; that is not a shipped S4 loop.

### Absence scope

- Surfaces inspected: CLI, agent/runtime, Coordinator, memory/skills architecture, configuration and chapter scope.
- Plausible first-party paths checked: research phase, long-term memory, skill installation, provider configuration, custom hooks and operator contribution/development paths.
- Why no material first-party path remains: these supply current-task processing or extension/configuration mechanisms, without a shipped external/future model, adaptation-option decision and returned current-capability loop; neither autonomous nor parent S4 closure is supplied at the session boundary.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy closure established.
- Disturbance / variety regulated: ordinary action permissions and task plans.
- Decisive decision or feedback right: no identity-level right routed and returned in the supplied mode.
- Decision owner: operator/developer configures rules; Lead approves operational plans.
- Supporting / enforcement mechanisms: blacklist, sandbox, permission modes, hooks and Coordinator feature gates.
- Closure path: action/plan permissions affect tools, but are not identity/ultimate-policy deliberation.
- Why this is / is not agent-owned: neither static safety rules nor Lead operational approval establishes S5.
- Evidence: [mode configuration](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/config.py#L38-L58), [plan return](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/src/novacode/agent/team_mailbox.py#L31-L78), [permission architecture](https://github.com/gczhuang-cmd/NovaCode/blob/34a2d555a530120fd6241f7065d49390e52f3573/README.md).
- Basis: structural.
- Confidence: medium.
- Caveats: users legitimately own their tasks; no general claim about their wider organization follows.

### Absence scope

- Surfaces inspected: CLI/operator controls, config, permission pipeline, Team plan authority and Coordinator gates.
- Plausible first-party paths checked: user approvals, plan approve/reject, tool restrictions, prompts/instructions and upstream maintainer policy.
- Why no material first-party path remains: inspected paths regulate operational actions/configuration; no identity/ultimate-policy matter reaches a legitimate S5 authority and returns as binding governance through the assessed harness. Adjacent OSS maintainers are not installed session owners.

## Distributed OSS parent arrangement

Public contributors develop the package, while users run local sessions. Contributor governance is adjacent; no organization-level parent S3/S4/S5 loop is borrowed. Operator permissions are considered above without assigning P automatically.

## Self-hosted and non-human modes

Local self-hosted operation, Team backends, opt-in Coordinator and ordinary operator permissions are included. Team Lead is non-human current control; operator kill/configuration affordances do not add parent modifiers without function-specific evidence.

## Recursion

Independent contexts, nested tasks and worker sessions establish operational decomposition. Their complete local metasystems/viability are not established.

## Variety and escalation

Tool observations, mailboxes and idle notifications carry local variety. Permission rejection, bounded turns/timeouts, worktree retention and reports preserve some exceptions; they do not by themselves prove algedonic escalation or S5.

## Evidence gaps

Frozen source compileall and 34 native worktree slug/create/lifecycle tests pass; pytest warned that its installed configuration does not recognize asyncio_mode. No live model/provider tasks or performance experiments. Team semantics depend on enabled features, available Git and backend. No claim of hard reviewer isolation, conflict-free semantic integration or guaranteed response to findings. S2 C deliberately bounds deterministic isolation support rather than assuming an autonomous coordination actor from Team labels.
