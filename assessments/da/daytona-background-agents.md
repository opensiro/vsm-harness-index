---
harness_id: daytona-background-agents
project_name: Daytona Background Agents
repository: https://github.com/jamesmurdza/background-agents
review_ref: 1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3
reviewed_at: 2026-11-16
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.8
profile_version: 0.2.4
assessment_procedure_version: 0.3.8
status: included
autonomy_s1: A
autonomy_s2: C
autonomy_s3: P
autonomy_s3_star: —
autonomy_s4: P
autonomy_s5: —
---

# Daytona Background Agents

## Review boundary

- System in focus: The account-level Background Agents application and its packaged SDK and sandbox adapters.
- Purpose and identity: Run and observe separate coding chats and recurring or external-event task jobs.
- Relevant environment: Authorized account owner, Git repositories, external trigger providers, Daytona sandboxes and installed model/CLI backends.
- Standard-distribution boundary: Documented web deployment and desktop wrapper, with first-party provider launch, scheduling, per-run Git isolation and repo-scoped skills.
- Credited operating / distribution surfaces: Web job and chat lifecycle, SDK session wrapper, sandbox job/branch support, account controls and repo-scoped skills.
- Adjacent first-party surfaces excluded from ownership: External provider implementations, developed repositories, GitHub approvals, development tests, docs examples and deployment billing operations.
- First-party operating / deployment modes considered: Interactive sandbox chat, inbound webhook and interval jobs, scheduled branch checkout and optional PR output, user-managed skills.
- Recursion level: One account's managed chat and scheduled-job portfolio, with separately acting coding sessions as operational units.
- Reviewed revision: `1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3`.
- Observation date: 2026-11-16.
- Generated Profile version: 0.2.4.
- Generated Methodology version: 0.3.8.
- Current Profile version: 0.2.4.
- Current Methodology version: 0.3.8.

## Repository architecture

The Next.js app stores chats, scheduled jobs and runs in Postgres. The agent SDK launches installed model-backed CLIs as detached Daytona jobs, reconnects to poll output and translates provider events. Web routes manage task submission, monitoring and cancellation. Scheduled jobs create fresh sandboxes on run-specific branches and can publish the result branch. The repo skills panel searches external procedures and returns selected skills to subsequent sessions. [`README.md`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/README.md), [`packages/sdk/README.md`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/sdk/README.md#L290-L305), [`packages/web/app/api/cron/agent-lifecycle/_lib/scheduled.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/cron/agent-lifecycle/_lib/scheduled.ts#L196-L244), [`packages/web/app/api/cron/agent-lifecycle/route.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/cron/agent-lifecycle/route.ts#L62-L125), [`packages/docs/public/content/feature-skills.md`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/docs/public/content/feature-skills.md).

## Operational model

Interactive chats and independently triggered jobs hand prompts to model-backed coding agents. Agents choose code and tool actions inside their execution boundary. The application transports events, supplies checkout/branch isolation and manages run state. The owner determines work commitments and adopts repo-level procedures.

## S1 — Operations

- State: A
- Function: Perform model-directed coding and return code or task output.
- Disturbance / variety regulated: Variable prompts, repository content, external tool results and runtime conditions.
- Decisive decision or feedback right: Select and operate coding actions in the agent loop.
- Decision owner: The configured coding agent in the standard CLI session.
- Supporting / enforcement mechanisms: SDK provider adapters, sandboxed process, job log polling, JSON event parsers and app run lifecycle.
- Closure path: The wrapper starts a prompt-driven session, reads model and tool events and persists the result. A later input can continue the session or open subsequent work.
- Why this is / is not agent-owned: The app delivers input and supervises lifecycle. Removing the model-backed CLI removes discretionary coding work.
- Evidence: [`packages/sdk/README.md`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/sdk/README.md#L178-L230), [`packages/sdk/README.md`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/sdk/README.md#L292-L305), [`packages/web/lib/agent-session.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/lib/agent-session.ts), [`packages/web/app/api/cron/agent-lifecycle/_lib/scheduled.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/cron/agent-lifecycle/_lib/scheduled.ts#L236-L250)
- Basis: structural
- Confidence: High
- Caveats: Model and sandbox availability depend on configured providers.
- Boundary reachability: The shipped app calls its own session wrapper in both chat and scheduled job flows; the SDK has packaged provider adapters and Daytona execution support.

## S2 — Coordination

- State: C
- Function: Isolate simultaneous scheduled writers that target the same repository and base ref.
- Disturbance / variety regulated: Distinct job agents can propose incompatible work from the same base. Their working-tree state and branch writes would interfere if they shared one checkout or one output ref.
- Decisive decision or feedback right: Choose the conflict policy beyond branch separation, such as how to reconcile incompatible changes across jobs.
- Decision owner: The app supplies separation by job/run context. A user or integrator owns any cross-branch conflict resolution.
- Supporting / enforcement mechanisms: Fresh sandbox provisioning, generated job-specific output branches, clone and push logic, and per-job overlap control.
- Closure path: Each agent receives its own checkout and branch. Committing/pushing returns its changes through that branch, with optional PR against the chosen base. Other agents can continue their independent branches.
- Why this is / is not agent-owned: The runtime implements isolation. No model decides the branch coordination policy or arbitrates which competing change wins.
- Evidence: [`packages/web/app/api/cron/agent-lifecycle/_lib/scheduled.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/cron/agent-lifecycle/_lib/scheduled.ts#L197-L226), [`packages/web/app/api/cron/agent-lifecycle/_lib/scheduled.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/cron/agent-lifecycle/_lib/scheduled.ts#L417-L433), [`packages/web/app/api/cron/agent-lifecycle/_lib/scheduled.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/cron/agent-lifecycle/_lib/scheduled.ts#L518-L557), [`packages/web/lib/sandbox.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/lib/sandbox.ts#L262-L323), [`packages/web/app/api/cron/agent-lifecycle/route.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/cron/agent-lifecycle/route.ts#L62-L93)
- Basis: structural
- Confidence: High
- Caveats: The claim covers distinct scheduled jobs in the same repository. It does not establish cross-branch semantic conflict negotiation.
- Boundary reachability: The shipped scheduled repo-job path calls fresh sandbox creation with the configured base and generated output branch.
- Distinct S1 units: Model-backed sessions of separately configured scheduled jobs in one account, including jobs on the same repo.
- Inter-S1 disturbance: Simultaneous writes to the same project and base can contend for checkout state and branch HEAD if conducted through the same branch, even when they originate from different jobs.
- Attenuating coordination relation: Fresh checkout per run and a branch namespace keyed by job ID and run time. Scheduling also filters already-running executions of the same job.
- Feedback into subsequent S1 behaviour: Git starts in the selected job checkout, so tool edits and result publishing are directed into that job branch while other jobs remain on separate refs.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: Dedicated writable checkout and output ref change where each concurrent coding unit can write, addressing concrete working-tree and ref interference.

## S3 — Inside-and-now control

- State: P
- Function: Regulate a running and recurring job portfolio in the account.
- Disturbance / variety regulated: An unwanted executing turn or an outdated recurring job can continue spending resources or producing new work.
- Decisive decision or feedback right: Select existing jobs to enable/disable or run, and stop a chosen running turn using its identity.
- Decision owner: The authenticated account owner.
- Supporting / enforcement mechanisms: Portfolio list, run histories, server ownership checks, turn claims, queue controls and cron eligibility.
- Closure path: The job enable decision changes eligibility on subsequent scheduler ticks. A valid Stop obtains the exact turn claim, pauses the queue, cancels the run and records terminal state.
- Why this is / is not agent-owned: Cron and the stop handler enforce decisions. The model-backed worker does not own portfolio commitments.
- Evidence: [`packages/web/components/search-palette/TriggersModal.tsx`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/components/search-palette/TriggersModal.tsx#L115-L201), [`packages/web/components/scheduled-jobs/ScheduledJobActionsMenu.tsx`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/components/scheduled-jobs/ScheduledJobActionsMenu.tsx#L65-L85), [`packages/web/app/api/scheduled-jobs/[id]/route.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/scheduled-jobs/[id]/route.ts#L184-L218), [`packages/web/app/api/cron/agent-lifecycle/route.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/cron/agent-lifecycle/route.ts#L62-L125), [`packages/web/app/api/agent/stop/route.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/agent/stop/route.ts#L46-L143)
- Basis: structural
- Confidence: High
- Caveats: This is account-level user control of job eligibility and chosen turns. Stopping a turn and disabling its future schedule are distinct controls.
- Boundary reachability: The user-facing triggers view and chat stop action call these shipped routes for a signed-in account.
- Whole-system current view: The triggers view lists the account's jobs and links to run histories, while running chats expose their current turn.
- Current-control decision scope: Select which jobs are eligible to run, dispatch a current commitment, or pause and cancel a chosen in-progress turn.

## S3* — Complementary audit

- State: —
- Function: Obtain independent evidence about run claims and return corrective findings into control.
- Disturbance / variety regulated: A reported completion can hide incorrect actual code or a misleading final summary.
- Decisive decision or feedback right: No shipped independent evaluator or alternative audit-to-correction loop.
- Decision owner: The user can inspect branch artifacts and external GitHub review. The runtime observes routine SDK/process reports.
- Supporting / enforcement mechanisms: Branch preview, tool streams, commit-count checks, user-accessible output and external review options.
- Closure path: Scheduled completion may push a PR branch and expose it to a user. The first-party flow does not consume a separate audit verdict to regulate the run.
- Why this is / is not agent-owned: Status polling verifies lifecycle. Artifact access supports ad hoc external review, without a shipped independent audit role and return path.
- Evidence: [`packages/web/app/api/cron/agent-lifecycle/_lib/scheduled.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/cron/agent-lifecycle/_lib/scheduled.ts#L436-L555), [`packages/web/app/api/github/compare/route.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/github/compare/route.ts), [`packages/web/app/api/sandbox/git/route.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/sandbox/git/route.ts), [`packages/docs/public/content/feature-jobs.md`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/docs/public/content/feature-jobs.md)
- Basis: structural
- Confidence: Medium
- Caveats: A caller can author an independent reviewer job or install a review skill under a different operating boundary.

### Absence scope

- Surfaces inspected: Scheduled finalize and PR output, SDK status/agent streams, Git operations, Jobs and Skills documentation.
- Plausible first-party paths checked: An independent reader of actual code, distinct external review result, and corrective feedback into scheduled lifecycle.
- Why no material first-party path remains: The available first-party Git checks characterize refs and progress. External PR reviews and configured skills are not wired as independent audit decisions that drive subsequent job control in the standard path.

## S4 — Outside-and-then intelligence

- State: P
- Function: Adopt new repeatable operating procedures for future repository work.
- Disturbance / variety regulated: The project's future task needs can exceed installed procedures, while an external registry exposes alternative capabilities.
- Decisive decision or feedback right: Select a durable repo-level skill addition or removal in response to a prospective task need.
- Decision owner: The authenticated user authorized to manage that repository's skills.
- Supporting / enforcement mechanisms: Registry search, repo-scoped storage, sandbox install/reinstall and skill discovery for model sessions.
- Closure path: Search returns concrete external options. User adoption persists the selected skill for the repo; sandbox setup and later agent use make the adopted procedure available in subsequent work.
- Why this is / is not agent-owned: The user decides what the future operating capability should include. The runtime applies that decision and offers available skills to the agent.
- Evidence: [`packages/docs/public/content/feature-skills.md`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/docs/public/content/feature-skills.md), [`packages/web/app/api/skills/search/route.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/skills/search/route.ts), [`packages/web/app/api/skills/route.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/skills/route.ts#L64-L121), [`packages/web/app/api/skills/install/route.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/skills/install/route.ts), [`packages/web/lib/sandbox.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/lib/sandbox.ts#L587-L655)
- Basis: structural
- Confidence: High
- Caveats: The claim covers repo-scoped procedure adoption. It does not extend to automated portfolio adaptation or to a marketed third-party skill's internal claims.
- Boundary reachability: The first-party application exposes market search and manage/install flows. The sandbox lifecycle reinstalls enabled repo procedures so later sessions can use them.
- External distinction: Available external skills are retrieved from the skills.sh registry and compared with what the repo can currently do.
- Future / prospective distinction: A user can adopt a repeatable procedure for later tasks and chats in the repo, beyond the current turn.
- Adaptation option generated: Installed-state and external registry results form concrete alternatives that the repo owner can adopt or remove.
- Path back into current capability / S3: The selected option is persisted at repo scope, installed into the sandbox and discovered for model use in later sessions.

## S5 — Policy and identity

- State: —
- Function: Close account-level identity and ultimate policy decisions.
- Disturbance / variety regulated: Owners set job goals, repository scope and selectable provider/tool permissions.
- Decisive decision or feedback right: No surfaced resolution path over account-level purpose or governing mandate.
- Decision owner: Account owners choose job settings and external project maintainers control their repositories.
- Supporting / enforcement mechanisms: Access controls, job prompt/trigger config, git policy and plan settings.
- Closure path: Stored job settings constrain future runs. These are operational commitments and settings.
- Why this is / is not agent-owned: The first-party flows set, restrict and dispatch tasks. They do not surface an ultimate-policy matter and return a governing decision at this recursion.
- Evidence: [`packages/web/app/api/scheduled-jobs/[id]/route.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/app/api/scheduled-jobs/[id]/route.ts), [`packages/web/lib/git-policy.ts`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/lib/git-policy.ts), [`packages/docs/public/content/feature-jobs.md`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/docs/public/content/feature-jobs.md), [`packages/web/README.md`](https://github.com/jamesmurdza/background-agents/blob/1b4d4d76be8e3e9bedec77ac0fc4f6124715d4e3/packages/web/README.md)
- Basis: structural
- Confidence: High
- Caveats: A particular deployment may have governance outside this repository's documented app boundary.

### Absence scope

- Surfaces inspected: Account and job controls, Git effect rules, scheduling configuration, repo skills and deployment docs.
- Plausible first-party paths checked: Persistent job prompts as identity, scope permissions as policy, and an owner path for revising a conflicting account mandate.
- Why no material first-party path remains: The target of changes is an individual run/job, capability, or configured scope. No first-party process resolves or returns an ultimate account mandate.

## Recursion

The managed portfolio contains distinct chats and scheduled runs with local model discretion and separate workspaces. External provider services and project governance are neighboring systems.

## Variety and escalation

Tool-backed model sessions handle task variation, while branch namespaces and cron guards attenuate operational interference. An authorized user can intervene in a chosen active turn. Ordinary run status and failure messages were assessed as operational feedback.

## Evidence gaps

Source and tests were reviewed at the pinned revision. No Daytona session or model provider execution was performed. Credit for the repo skills adaptation path concerns parent-owned adoption against a concrete repo need and its documented return into later sessions.

