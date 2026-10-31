---
harness_id: sd0x-dev-flow
project_name: sd0x-dev-flow
repository: https://github.com/sd0xdev/sd0x-harness
review_ref: 04e8a5e3f5d9c482937c2ad2170fab5fbd02b630
reviewed_at: 2026-10-31
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-31
status: proposed
autonomy_s1: A
autonomy_s2: —
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: A
autonomy_s5: —
---

# sd0x-dev-flow

## Review boundary

- System in focus: the installable sd0x-dev-flow Claude Code plugin/harness, including its bundled instructions, 16 specialist agent definitions, skills, rule and hook surfaces, and supported full Claude Code plugin mode.
- Purpose and identity: bounded software-engineering delivery with independently reviewed changes, configurable model discretion and completion evidence.
- Relevant environment: user project repository, Claude Code host session, optional Codex CLI reviewer, shell/git/test tools, user-provided work and corrections.
- Standard-distribution boundary: the documented full Claude Code plugin installation and project setup. The separate Codex/Cursor/Windsurf/Aider **skills-only** installation is not credited as having the same active hooks or review loop.
- Credited operating / distribution surfaces: installed rules/skills/agents; Claude session invocation of specialist skills, independent Codex review dispatch, local completion/review-state feedback, project-installed rules and self-improvement lessons.
- Adjacent first-party surfaces excluded from ownership: repository author/contributor governance, test suite, GitHub release/CI pipelines, example feature documents and unattached proof-of-concept orchestration. External Claude Code and Codex executables supply model/agent execution and independent review; their internal subsystems are not attributed to this repository.
- First-party operating / deployment modes considered: full Claude Code plugin with project setup, model-directed work and review, optional read-only `/orchestrate --execute`, project-local lesson/rule promotion; skills-only installation considered separately for scope.
- Recursion level: one configured project engineering session with optional specialists and verification, not sd0xdev's developer organization or Codex/Claude as separate organizations.
- Reviewed revision: `04e8a5e3f5d9c482937c2ad2170fab5fbd02b630`.
- Observation date: 2026-10-31.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.7.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.7.

## Repository architecture

This is not a proprietary replacement for Claude Code's model/tool executor. Its `package.json` publishes the scripts, skills, agents, hooks and rules; `/project-setup` installs local CLAUDE instructions, relevant rules/hooks and scripts. `hooks/hooks.json` registers start, tool, stop and prompt events. The Stop hook explicitly **never blocks**: it prints review-state reminders while model-facing `rules/auto-loop.md` requires fresh code/doc review and precommit evidence before completion. `scripts/review-state.js` persists digest-bound verdict slots; `scripts/codex-exec.js` dispatches read-only reviewer work to an external Codex CLI. The review skill freezes changes, requests an independently researched verdict and directs correction/re-review. The project supports specialist-agent definitions and an `/orchestrate` report-only read-only fanout, not an arbitrary always-on parallel coding fleet. Project-specific human setup and final irreversible actions remain operator-governed. The bundled lesson rule can promote recurring user corrections to subsequently loaded local rules. No provider-backed execution or empirical quality claim was made in this source-only assessment.

## Operational model

The installed Claude session is the operational software-work actor. It chooses concrete implementation actions while the sd0x harness supplies method, specialist prompts, review obligations and feedback records. Codex is a separate audit actor, not the owner of production code decisions. The model chooses work timing, risk tier escalation and repairs; deterministic hooks and digest checks transport and enforce/check conditions. The user supplies the task and controls privileged or identity-shaping modifications. Removing the model agents while retaining only hooks and rules leaves no discretionary implementation or independent audit judgment.

## S1 — Operations

- State: A
- Function: implement and verify a requested software change or investigation in a user project through model-directed project work.
- Disturbance / variety regulated: unfamiliar project context, failing tests, faulty edits, changed requirements and review findings.
- Decisive decision or feedback right: choose inspections, edits, tests, delegated specialist assistance and repairs in response to evidence.
- Decision owner: model-driven Claude Code engineering actor using the installed first-party project rules and specialist skills; the external Claude host executes tool calls.
- Supporting / enforcement mechanisms: plugin rules, installed project setup, hooks, review-state digest, git guards and verification scripts.
- Closure path: user task → actor work and tools → test/review evidence or failure → actor correction/re-verification → project changes and report.
- Boundary reachability: the documented full Claude plugin mode installs skills/rules/hooks and the session imports them; unlike skills-only mode, the full mode supplies the completion and review path.
- Why this is / is not agent-owned: the actor selects engineering actions, whereas scripts record and gate outcomes without choosing code changes; external host internals are not credited as first-party decisions.
- Evidence: [installation and ownership model](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/README.md), [active session rules](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/CLAUDE.md), [project setup and installed surfaces](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/skills/project-setup/SKILL.md), [hook wiring](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/hooks/hooks.json).
- Basis: structural.
- Confidence: medium-high.
- Caveats: source demonstrates a supported installed mode, not deployment frequency or measured task success; first-party credit is for the composed plugin mode, not the external host's general autonomous capabilities.

## S2 — Coordination

- State: —
- Function: no distinct inter-S1 interference regulation is established for the assessed standard coding session.
- Disturbance / variety regulated: read-only fanout and specialist handoffs are present, but no concrete conflicting changes between autonomous S1 work cells are regulated by a specified returned coordination decision.
- Decisive decision or feedback right: no S2-specific decisive right established.
- Decision owner: not established; planner/executor role dispatch and report ordering do not themselves decide collision attenuation.
- Supporting / enforcement mechanisms: report-only workflow planning, bounded read-only fanout and sequential specialist skill calls.
- Closure path: workflow reports return to the caller; no evidenced change to later competing S1 behaviour from conflict regulation.
- Why this is / is not agent-owned: model-driven orchestration of independent read-only findings alone is not S2.
- Evidence: [read-only orchestrate contract](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/skills/orchestrate/SKILL.md), [single reviewer default](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/rules/auto-loop.md), [specialist definition](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/agents/strict-reviewer.md).
- Basis: structural.
- Confidence: medium.
- Caveats: other user-composed multi-agent modes are possible but are not credited without a shipped interference-specific return loop.

### Absence scope

- Surfaces inspected: installed agent/skills list, read-only `orchestrate` contract, default single-review dispatch and plugin hook registry.
- Plausible first-party paths checked: concurrent fanout, plan preview, report collection, specialist review and sequential handoffs.
- Why no material first-party path remains: the shipped fanout is report-only and prevents writes, while the remaining invocation paths do not show an actual shared-resource conflict between distinct operational S1 units and an S2-specific feedback path.

## S3 — Inside-and-now control

- State: —
- Function: no separate whole-system current-control relation is established at the configured project-session boundary.
- Disturbance / variety regulated: risk severity, code/doc dirtiness and review failures are constrained by local quality gates, not shown as current resource bargaining across operational units.
- Decisive decision or feedback right: risk tier and gate obligations operate on task/change evidence without an evidenced whole-system allocation or corrective control decision.
- Decision owner: model and user choose execution/review details within static policy; digest-state scripts enforce/report.
- Supporting / enforcement mechanisms: Anchor Register, tier selection, review slots, hook reminders, scoped guards and human exits.
- Closure path: review failures cause local work/review retries; no independently evidenced S3 current-control feedback loop.
- Why this is / is not agent-owned: an agent-owned local repair and deterministic completion invariant do not themselves establish S3.
- Evidence: [review tiers and loop](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/rules/auto-loop.md), [policy tiers and ownership](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/rules/discretion.md), [digest-bound state](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/scripts/review-state.js), [nonblocking hook](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/hooks/stop-guard.sh).
- Basis: structural.
- Confidence: medium-high.
- Caveats: risk-scaled verification is important but cannot substitute for a whole-system current view.

### Absence scope

- Surfaces inspected: project rules, Hook registry, review-state implementation, verification script, agent dispatch and human exit rules.
- Plausible first-party paths checked: risk-tier escalation, round caps, project overrides, QA gating and the read-only workflow planner.
- Why no material first-party path remains: none demonstrates an owner selecting or revising shared current resources/commitments for a multi-unit whole; these regulate task quality or enforce preselected limits.

## S3* — Complementary audit

- State: A
- Function: independently challenge an implementer's completion/correctness claim by inspecting actual changed project artifacts.
- Disturbance / variety regulated: a producer may falsely declare completion or miss faults not visible in its own summary/checks.
- Decisive decision or feedback right: give a separate severity-scoped audit verdict from raw code/diff access and determine whether corrective work is owed.
- Decision owner: the separately dispatched Codex reviewer model makes the audit judgment; the producing Claude actor owns subsequent repairs; no digest parser is credited as auditor.
- Supporting / enforcement mechanisms: read-only `codex exec` transport, frozen changed-file metadata, review-state verdict slot, risk thresholds and fallback validation.
- Closure path: after code changes, `/codex-review-fast` → independent reviewer source investigation → Ready/Blocked findings → producing actor fixes blocking issues → re-review → fresh pass records a digest-bound slot required before completion.
- Boundary reachability: the full plugin installs the review skill, transport and model-facing auto-loop obligations, and hooks remind after edits; the review is a documented first-party supported optional tool path, not a CI-only or developer-dogfood audit.
- Why this is / is not agent-owned: a different model agent reads the actual diff/source and decides findings; transport, severity parser and receipt record do not substitute for its judgment.
- Claim being audited: project change is correct enough under the configured risk tier to be complete.
- Ordinary reporting path: producer's change summary, tests and its own verification.
- Complementary access path: separate Codex sandbox source/diff inspection and independent review prompt; fallback reviewers are controlled by recorded transport failure semantics.
- Independence boundary: read-only external Codex session receives frozen task and changed-file metadata but reads source itself; it is not the producer's self-verification. Both hosted tools remain outside first-party implementation ownership.
- Who acts on findings: producing Claude actor performs scoped fixes and re-dispatches; human is reserved for explicitly enumerated exits.
- Evidence: [independent source review and fix loop](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/skills/codex-code-review/SKILL.md), [severity/scope gate](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/skills/codex-code-review/references/review-common.md), [separate reviewer transport](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/scripts/codex-exec.js), [repeat-until-current-pass contract](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/rules/auto-loop.md), [digest-bound return](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/scripts/review-state.js).
- Basis: structural.
- Confidence: medium.
- Caveats: evidence is shipped protocol/code, not a captured successful live independent audit; review may be blocked by missing external Codex credentials or human exits in particular installations.

## S4 — Outside-and-then intelligence

- State: A
- Function: adapt subsequent project-engineering guidance from recurring external/user corrections.
- Disturbance / variety regulated: repeated user-observed failures whose recurrence is not prevented by current rules.
- Decisive decision or feedback right: distinguish a reusable error pattern and, after repetition, update project-local operational guidance for future sessions.
- Decision owner: the model-driven engineering actor following the first-party self-improvement rule; the user can originate corrections and decide version-control inclusion.
- Supporting / enforcement mechanisms: namespaced lesson log, repeated-pattern criterion, rule-file update and normal doc review.
- Closure path: user correction on a recurrent failure → actor writes a structured lesson with prevention signal → pattern reaches promotion criterion → actor promotes guidance to project rules → future sessions read updated rules and act differently.
- Boundary reachability: the published self-improvement rule is installed via standard full-plugin project setup and imported by session guidance; the namespaced lesson file is provisioned on first occurrence and later local rules are loaded.
- Why this is / is not agent-owned: the model must recognize the pattern, select the prevention and write/publish the operational rule; file persistence alone is not the adaptation judgment.
- External distinction: user correction provides external feedback about unmet project expectations, not solely internal planning.
- Future / prospective distinction: lesson/rule promotion addresses future recurrence across tasks and sessions.
- Adaptation option generated: prevention rule and detection signal reusable for later work.
- Path back into current capability / S3: project-installed rules govern later Claude sessions, closing adaptation into operational capability; no distinct S3 is claimed.
- Evidence: [correction-to-rule procedure](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/rules/self-improvement.md), [rule installation](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/skills/project-setup/SKILL.md), [project rule imports](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/CLAUDE.md).
- Basis: structural.
- Confidence: medium.
- Caveats: contingent on actual recurring correction and session-level rule promotion; source does not establish measured improvement or autonomous change to the plugin's published universal anchors.

## S5 — Policy and identity

- State: —
- Function: no runtime identity/ultimate-policy decision-and-return loop is established in the supported project engineering session.
- Disturbance / variety regulated: local configuration, security anchors, scope requests and approval/merge risks.
- Decisive decision or feedback right: no in-boundary identity-level decision is returned through an established S5 channel.
- Decision owner: developer and user set framework identity and non-negotiable rules; model may deviate from defaults only inside those constraints.
- Supporting / enforcement mechanisms: fixed Anchor Register, project overrides, user confirmation and protected git/review gates.
- Closure path: local tasks use preselected rules; no evidenced policy-level proposal → legitimate parent judgment → returned change to the session's identity/ultimate policy.
- Why this is / is not agent-owned: static constraint hierarchy and user approval of ordinary actions do not create S5 closure.
- Evidence: [Anchor/Default boundaries](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/rules/discretion.md), [fixed security policy](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/rules/security.md), [scope and developer role](https://github.com/sd0xdev/sd0x-harness/blob/04e8a5e3f5d9c482937c2ad2170fab5fbd02b630/CLAUDE.md).
- Basis: structural.
- Confidence: medium.
- Caveats: project maintainers can change the published plugin policy in a different recursion, which is explicitly excluded here.

### Absence scope

- Surfaces inspected: managed and project rule precedence, anchor register, project setup, approval exceptions and session guidance.
- Plausible first-party paths checked: human exits for ordinary work, user project overrides, anchor conflict/proposal channel and default policy revisions.
- Why no material first-party path remains: normal operator approval and developer governance concern execution or the *adjacent development organization*, not an operational identity/ultimate-policy matter returned into this installed-session recursion.

## Recursion

Specialist agents and read-only fanout have assigned scopes and separate prompts but do not demonstrate independent durable viable subsystems. The review actor is a complementary audit relation; no nested VSM recursion grade follows merely from agent spawning. The user project session is the reviewed recursion; plugin developer governance and external host/providers are separate.

## Variety and escalation

The plugin attenuates risk with immutable policy anchors and review severity thresholds while preserving model discretion over local engineering methods. Digest-bound review-state detects changes that invalidate prior passes. Stop hooks are advisory; the model must honor the completion invariant. Hard human exits cover unresolved architecture/security/data-integrity or exhaustion cases. Missing Codex transport is not automatically an auditor verdict.

## Evidence gaps

The assessment is static/source-based. It does not prove real-world installation completeness, independent reviewer outcomes, recurrence-triggered rule promotion or benefit from adaptation. Clarify whether full deployed Claude host/skill invocation semantics always return review findings into the producing actor, and whether project user policies can disable reviewed paths, before interpreting this as measured continuous control.
