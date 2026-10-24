---
harness_id: ucode
project_name: ucode
repository: https://github.com/sppideey/ucode-agent
review_ref: be41840d1219ea45490ac8c61ba84fa48d3119a6
reviewed_at: 2026-10-24
generated_profile_version: 0.2.4
generated_assessment_procedure_version: 0.3.7
profile_version: 0.2.4
assessment_procedure_version: 0.3.7
assessment_changed_at: 2026-10-24
status: proposed
autonomy_s1: A
autonomy_s2: C
autonomy_s3: —
autonomy_s3_star: A
autonomy_s4: —
autonomy_s5: —
---

# ucode

## Review boundary

- System in focus: the first-party Node.js ucode terminal coding harness and its main model/tool execution loop, optional parallel coding workers, shared mutation lock, checked app tool paths, user-triggered visual review, provider fallback, project/session tooling and standing skills.
- Purpose and identity: build and revise code/app artifacts using Gemini and local tool results, optionally split independent work into worker tasks, test produced files and report outcomes.
- Relevant environment: repository source and tool failures, edits from simultaneously progressing workers, project test/typecheck outputs, running browser application, screenshot evidence, model/provider outages, changing task instructions and operator interventions.
- Standard-distribution boundary: shipped ucode.js, src/core/*.js, src/tools/*.js, src/ui/*.js, bundled skills/templates and pinned package manifest. Playwright and external provider API implement I/O but are only credited where instantiated by first-party calls and prompts.
- Credited operating / distribution surfaces: main coding mode, model-selected delegate tool with up to three separately model-backed workers, serialized file writes and commands, automatic type/tests/live-app checks, operator /look with independent visual reviewer, provider failover, project-scoped memory/history and deployment controls.
- Adjacent first-party surfaces excluded from ownership: test/ suite and developer benchmarks/trace-guided improvements as product-development evaluation, user-authored or externally hosted reviewer services, Vercel's deployment organization and external model-provider behavior.
- First-party modes checked: main tool calls, plan mode and file operations; parallel worker execution and lock; scripted type/related tests; automated browser functional checks without visual critique; opt-in /look which enables independent screenshot critique and returns evidence to main model; provider failover and persistent project memory.
- Recursion level: one ucode operating organization with main coding Agent and transient separately progressing worker model loops as bounded S1 units. Workers cannot delegate onward or update plans, and no full independent metasystem for a worker is inferred.
- Reviewed revision: be41840d1219ea45490ac8c61ba84fa48d3119a6 (batch #1013 row 6), observed 2026-10-24. LICENSE at this frozen revision is MIT; current live GitHub license metadata may have evolved and is not imported into the frozen assessment.

## Repository architecture

The main loop in src/core/loop.js sends model-visible tool schemas through src/core/provider.js, executes first-party workspace changes, checks their actual outcomes and returns observations for further model choices. src/tools/index.js wires repository reads/edits, local commands, app scaffolding, optional browser inspections and web search. A turn also runs source-native syntax/type, related-test and live-log checks, and can inspect running apps in a real browser. That automatic verification is ordinary same-operation feedback rather than independent review.

The advertised delegate tool spawns up to three separate concurrent worker loops through runWorker, each with its own model messages, assigned instructions and actual repository tools. Workers share one project and may edit real files. The parent fileLock Promise chain serializes all worker file writes and run_command(s) calls so their effects do not interleave, and worker reports list touched files and changed outcomes. The coordination mechanism is a fixed first-party lock, not a model-selected S2 arbitration decision. Worker instructions ask them to own distinct file scopes but this is prompt guidance rather than a lock-enforced scope allocation.

The opt-in /look command drives a real local app in browser at phone and desktop widths, records console/functional/accessibility/layout observations and screenshots, and calls a separate vision-capable model with a specialist product-designer critique prompt. It returns visual findings to the operator and appends them to the primary Agent's conversation, making follow-up corrections reachable. Automatic look-on-write explicitly uses review:false after the developer observed bad automatic restyling outcomes. This distinction matters: S3*=A is credited **only to the user-triggered /look path** with the independent semantic visual reviewer, not automatic tests or browser probes.

Source anchors: [main loop and worker execution](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/core/loop.js), [tool registry](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/tools/index.js), [browser evidence/review](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/tools/browser.js), [related tests](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/core/tests.js), [provider](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/core/provider.js).

## Operational model

The main model selects tools and optionally delegates independent project components to multiple model-backed child loops. Children work concurrently but serialize shared writes/shell commands through the parent lock, then return actual summaries and touched files. The main coding model can integrate those results. For an explicitly requested visual check, a separate model inspects browser screenshots and returns critique as evidence for later coding; routine automatic app checks have no separate visual judge. No live LLM-agent/provider/Browser quality test was performed for this assessment.

## S1 — Operations

- State: A
- Function: adapt coding and app-construction decisions to actual source files, tests, tool outputs and user feedback.
- Disturbance / variety regulated: changing code structure, runtime errors, missing dependencies, edit conflicts, provider interruptions, generated-app behavior and requested features.
- Decisive decision or feedback right: select tool calls, concrete file modifications, task decomposition and follow-on fixes based on returned current evidence.
- Decision owner: primary ucode model-backed agent; each optional worker separately chooses its assigned coding actions in its own model/tool loop.
- Supporting / enforcement mechanisms: source tools, project memory/session, typecheck/tests, app browser, fallback policy, permissions/confirmations, tool time bounds, plan UI and worker summaries.
- Closure path: coding objective + source context → main or worker model selects actions → first-party tool execution → result/type/test/error feedback → model revises or ends.
- Boundary reachability: src/core/loop.js and advertised first-party tool schemas reach real file/shell actions in the normal CLI and supported worker mode, rather than relying solely on prompt assertions.
- Why this is / is not agent-owned: deterministic tools can execute a requested command but cannot independently choose and revise open-ended code against varied task evidence; that right belongs to model turns.
- Evidence: [core/loop.js](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/core/loop.js), [tools/index.js](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/tools/index.js), [core/provider.js](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/core/provider.js).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: script tests establish wiring but do not measure live provider reliability or code quality.

## S2 — Coordination

- State: C
- Function: attenuate concurrent worker interference over one mutable project filesystem and local command/process resources.
- Disturbance / variety regulated: multiple coding S1 workers may simultaneously rewrite files or start conflicting install/server commands in the same workspace, causing interleaved writes, dependency-state conflicts or shared-port races.
- Distinct S1 units: up to three independent worker model/tool loops, each with a separate task, context, model response sequence and concrete shared-workspace actions.
- Inter-S1 disturbance: a worker's file or shell effects can invalidate another's expected state, shared command sequence or running process resource.
- Attenuating coordination relation: the common Agent.fileLock Promise chain serializes FILE_WRITES and run_command(s) for all workers while allowing independent read/investigation work to proceed.
- Feedback into subsequent S1 behaviour: each child receives its tool result after the lock-held operation and revises subsequent model steps; parent receives touched-file lists, child status and warnings if a worker wrote nothing.
- Why this is S2-specific rather than generic communication / routing / sequencing / shared state / delegation: a shared exclusive effect domain across concurrently acting independent worker models is actively attenuated, not merely a sequential one-model tool batch or message queue.
- Decisive decision or feedback right: decide the specific inter-worker effect-order policy and release conditions; the shipped deterministic lock implements that fixed right.
- Decision owner: developers' fixed source-code lock policy; no autonomous S2 actor observes conflicts and renegotiates write scopes or resource priorities.
- Supporting / enforcement mechanisms: MAX_WORKERS=3, worker-only tool restriction, Promise.all child execution, exclusive fileLock for writes/shell, worker result receipts and post-worker touched-file reconciliation.
- Closure path: simultaneous worker effects → shared lock queues mutation/shell operations → actual serial outcome/error returns per child → worker actions adapt; aggregate outcomes return to lead for integration.
- Boundary reachability: delegate is an advertised main tool; worker loops and fileLock are connected through shipped normal coding execution, not a test harness.
- Why this is / is not agent-owned: parent model selects decomposition, but fixed shared-effect exclusion is imposed deterministically; model choice of worker tasks does not make allocation/lock arbitration autonomous.
- Evidence: [fileLock/delegate/runWorker in core/loop.js](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/core/loop.js).
- Basis: explicit + structural.
- Confidence: high.
- Caveats: lock serializes file writes and certain commands, not all possible side effects; prompt-only file ownership can fail, and actual protection against conflicting high-level edits is not empirically measured.

## S3 — Inside-and-now control

- State: —
- Function: no distinct whole-current resource/commitment authority over a durable population of independently accountable operational projects is established.
- Disturbance / variety regulated: delegation, worker summaries and user-visible plans relate to the currently assigned coding task, not a whole-current portfolio of independent operating commitments.
- Whole-system current view: the main model constructs a task split, gets worker summaries after Promise.all, and sees touched files; the UI shows task status, but no persistent whole-current performance/resource model across separate viable S1 jobs.
- Current-control decision scope: the main model chooses file/task decomposition and integrates completed output; resource reallocation during independent worker execution is limited to fixed concurrency/lock and operator cancellation.
- Decisive decision or feedback right: no distinct S3 resource bargain or whole-current commitment-management right established apart from S1 task composition.
- Decision owner: primary operational coding model for current task; operator may stop/steer; no separate S3 owner.
- Supporting / enforcement mechanisms: update_plan, worker task name/result summaries, touched-file receipts, MAX_WORKERS, shared lock and user UI.
- Closure path: model task split → child work → parent integration exists; independent whole-current operation performance → central resource/commitment decisions → returned corrective operating controls is not established.
- Why this is / is not agent-owned: the lead model is autonomous at task planning, but this alone does not establish an independent viable-system S3 over a standing operational population.
- Evidence: [delegate/updatePlan and runWorker](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/core/loop.js), [README.md](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/README.md).
- Basis: structural bounded absence review.
- Confidence: medium.
- Caveats: a different recursion boundary treating a single transient build as an entire multi-worker operating organization might expose S3-like lead behavior; the published claim does not inflate current task delegation into independent whole-current control.

### Absence scope

- Surfaces inspected: main model planning, worker launch and live tool status, bounded concurrency, fileLock, parent result integration, plan UI, session and operator controls.
- Plausible first-party paths checked: lead model as S3 manager, update_plan board as S3 current view, worker result summaries as resource regulation and user task supervision as parent S3.
- Why no material first-party path remains: no separate ongoing cross-task/current performance resource view and autonomous or parent resource-allocation closure beyond one delegated coding turn was found.

## S3* — Complementary audit

- State: A
- Function: independently challenge a generated application's visible usability/design claims through first-party browser evidence and a separately prompted visual model reviewer.
- Disturbance / variety regulated: visual layout defects, weak hierarchy, inaccessible controls or broken user flows that ordinary code writing and test output can miss.
- Claim being audited: the working coding Agent's app should look and behave acceptably on desktop and phone screens.
- Ordinary reporting path: main Agent reads source, build/type/test outputs and automatic browser probes; it may describe its own app.
- Complementary access path: the /look tool opens the running local app in Playwright browser, captures real phone/desktop screenshots and diagnostics, then a separate vision-capable model judges visual problems from screenshots under an independent designer prompt.
- Independence boundary: the visual reviewer sees image evidence and its own review prompt, not merely the author's text; it cannot edit the source and is invoked in a separate provider model call. This is product-internal complementary independence, not an external human audit.
- Audit judgment / decisive feedback right: identify and prioritize specific visual/design issues and fixes from observed screenshots, not just parse routine test exit status.
- Decisive decision or feedback right: the separately instantiated vision review model owns the semantic visual critique; deterministic browser probes provide additional direct observations.
- Decision owner: the built-in visual review model on the opt-in /look path, constrained by product prompt and model time budget.
- Supporting / enforcement mechanisms: Playwright local browser, width-specific captures, console/layout/a11y probes, 60-second independent review budget, per-URL retry limiter, output formatting.
- How findings enter subsequent control: cmdLook writes the report for the user and pushes it as a user-message evidence entry to the primary Agent history; the coding model can respond and repair on following turns.
- Who acts on findings: main coding Agent under user task direction; visual reviewer itself cannot directly mutate the app.
- Closure path: produced app → browser screenshot and usage/console probes → separate vision-model critique → cmdLook injects findings into main conversation → subsequent implementation/repair can use that complementary evidence.
- Boundary reachability: /look is a shipped first-party user command invoking lookAtApp with default review:true. Automatic handOver/lookOnceThisTurn paths explicitly request review:false, so the credited S3* mode is **optional and user-triggered**.
- Why this is / is not agent-owned: the semantic design judgment belongs to a distinct vision model; fixed DOM checks alone are routine verification, and the author model does not produce the reviewer prompt answer.
- Evidence: [browser.js](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/tools/browser.js), [cmdLook and lookOnceThisTurn in loop.js](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/core/loop.js).
- Basis: explicit + structural.
- Confidence: medium-high.
- Caveats: opt-in only, depends on local Chrome/Edge, Playwright and provider availability; failed review is skipped, reviewer effectiveness is not measured and the main model is not forced to adopt recommendations.

## S4 — Outside-and-then intelligence

- State: —
- Function: no product-owned horizon-sensing and prospective organizational capability choice/adoption loop is established.
- Disturbance / variety regulated: provider stalls, task context size, past session records and developer performance-tracing evidence are handled for immediate reliability or by maintainers outside the shipped runtime.
- Decisive decision or feedback right: no first-party strategy for changing future capabilities using assessed environment options and adoption closure.
- Decision owner: developers configure model/tool features and standing skills; a static runtime fallback handles current failed providers.
- Supporting / enforcement mechanisms: UCODE_TRACE, model fallbacks, stuck watch, project memory, auto-update and developer measured before/after accounts.
- Closure path: current task/provider feedback → retry/fallback and context/tool control exists; horizon sensing → evaluated future option → adopted capability/policy feedback inside the product is absent.
- Why this is / is not agent-owned: model failover and retrospective maintainer performance improvements do not turn the coding Agent into an organizational strategy owner.
- Evidence: [provider.js](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/core/provider.js), [context.js](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/core/context.js), [README.md](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/README.md).
- Basis: structural bounded absence review.
- Confidence: medium-high.
- Caveats: developer experiments and trace-driven engineering should not be imported as autonomous S4 ownership of the frozen installed harness.

### Absence scope

- Surfaces inspected: current provider fallback, stuck detector, session memory, tool offerings, updater, design review, developer trace/performance metrics and bundled skill catalogue.
- Plausible first-party paths checked: provider choice as S4, self-improving worker process, persistent memory as strategic adaptation, skill/load/tool adjustment and external app-test feedback as organizational development.
- Why no material first-party path remains: each is current coding feedback, configured catalog or adjacent maintenance; no independent prospective capability adoption loop was found.

## S5 — Policy and identity

- State: —
- Function: no first-party legitimate ultimate-identity and purpose policy adjudication with authoritative organizational return.
- Disturbance / variety regulated: file risks, model modes, secret scanning before deployment and user action confirmations constrain specific coding operations, not ultimate viable-system identity.
- Decisive decision or feedback right: no constitutional organizational decision beyond task-specific tool approvals and supplied instructions.
- Decision owner: user/developer determine configuration, deploy initiation and skill policy; main model executes bounded tasks.
- Supporting / enforcement mechanisms: scoped project paths, tool offering/plan-mode refusals, protected deploy command, secret checks and human confirmation path.
- Closure path: external task permission → allow/deny and ordinary workflow updates exists; purpose/identity controversy → authoritative S5 adjudication → organization-wide decision return is absent.
- Why this is / is not agent-owned: deployment approval and secret protection are important safety operations, but do not constitute a legitimate ultimate-policy governing authority.
- Evidence: [core/scope.js](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/core/scope.js), [tools/deploy.js](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/tools/deploy.js), [core/loop.js](https://github.com/sppideey/ucode-agent/blob/be41840d1219ea45490ac8c61ba84fa48d3119a6/src/core/loop.js).
- Basis: structural bounded absence review.
- Confidence: high.
- Caveats: ultimate human governance of an actual development team is outside the assessed ucode product boundary.

### Absence scope

- Surfaces inspected: tool offering and plan-mode limits, scope approvals, secret-scanning deployment flow, skills, project memory, runtime configuration and operator commands.
- Plausible first-party paths checked: deploy approval as S5, built-in security skill as constitution, tool permission gate as identity policy and developer standards as first-party organizational S5.
- Why no material first-party path remains: none establishes a legitimate ultimate policy-decision institution and returned binding identity-level judgment at product recursion.

## Recursion

The main coding model and up to three parallel worker model loops are distinguishable S1 operating units for one project, sharing files and a deterministic lock. Worker loops have restricted tool catalogs and cannot delegate further. Their operational agency does not give each an independent full viable-system metasystem. External models, browser driver, Vercel and maintainers are dependencies or outside organizations.

## Variety and escalation

ucode amplifies operational variety through broad repository tools, parallel agent investigators/builders, optional direct browser observations and a separate vision-model visual critique. It attenuates contention with a shared write/command lock and execution caps, and constrains coding actions through scope, model retry, type/test checks and deployment confirmations. Worker results and independent optional visual findings return into main task control, but no larger S3/S4/S5 organization is established.

## Evidence gaps

- S2=C is bounded to deterministic serialization of writes/commands among concurrently active worker model loops, not agent-owned conflict arbitration or empirically proven safe parallel editing.
- S3*=A exists only on the user-triggered visual /look reviewer path; automatic browser/test checks use review:false and remain routine operational feedback. No live review-quality benchmark was executed.
- The lead model's delegation and plan updates are not elevated to a separate durable whole-current S3 management function without a portfolio-level resource/control closure.
- Frozen LICENSE at this exact commit is MIT, despite potentially changed current repository license metadata. No source repin or current-code import was used.
- No live LLM-agent, model-provider or Browser quality test was performed.
