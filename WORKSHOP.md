# Run a 90-minute workshop

**Audience:** builders first; product and trading-curious participants can pair with a builder. **Outcome:** a specific brief, bounded off-chain prototype, explicit market contract, demo draft, and honest review. This is a suggested exercise, not a claim of completed participant testing.

## Before the session

Have participants clone this repository and open **this folder** in Codex or Claude Code. They work in an ignored `runs/<slug>/` folder so the project skills and role files remain discoverable. Confirm they can ask the assistant to read `AGENTS.md`; do not assume eight parallel agents are available. No API key, wallet, RPC, or trading funds are required for the Markdown kit. Prepare an example brief only as a fallback. Do not put secrets or personal participant notes in Git.

| Time | Activity | Visible result |
|---|---|---|
| 0–10 min | Fill and freeze one brief. | Exact question, resolution rule, VOID policy, user decision. |
| 10–30 min | Run research, product, architect. Sequential execution is fine. | Three discovery artifacts with uncertainty labeled. |
| 30–40 min | Chief reconciles; human reviews. | Approved or revised `decisions/build-memo.md`. Stop here until approved. |
| 40–70 min | Build prototype, market contract, story. | Local HTML, JSON/rules, pitch/demo/application drafts. |
| 70–85 min | Review and exercise the local flow. | `qa/review.md` plus observed browser checks; label a same-context pass second self-review. |
| 85–90 min | Show one honest demo and next proof. | Known working scope and one next experiment. |

## Phase handoffs

Research, product, and architect receive only the frozen brief. Chief receives the brief and all three discovery files. Frontend, domain, and submission receive the brief, approved chief memo, and discovery files. Reviewer receives every final artifact and any actual verification notes. When roles run sequentially, tell them to ignore other roles’ unapproved new output until the phase boundary. Call the review independent only if a separate fresh context or agent performs it.

Use this start prompt:

> Read `AGENTS.md`, `WORKSHOP.md`, and my brief. Produce `research/market.md`, `product/spec.md`, and `architecture/plan.md` using the role files and mapped skills. Reconcile them into `decisions/build-memo.md`. Stop for my review before the build phase. Label proposed or unverified claims.

After approving the memo:

> Use the approved brief and memo to create the prototype, market contract and resolution guide, and submission drafts. Run the reviewer role. Make the local demo observable, record actual checks, and distinguish simulation from connected Solana or live AI behavior.

## Operator checks

Open the HTML in a browser and record whether a probability can be entered, stored, and viewed. Test invalid input, 0%, 100%, close, refusal of post-close forecasts, YES, NO, VOID, second resolution, reset, and a reload. Check a narrow viewport and keyboard focus. For 70% YES, Brier score is 0.09 on YES or 0.49 on NO; VOID has no score. Check that `market.json` preserves the three brief fields verbatim and parses as JSON. Mark any check not actually run as pending. No local check proves genuine model generation, chain execution, public deployment, or three independent builders completing the workshop.

## Pilot observation sheet

For each of three **new** builders, record consent and task definition, environment, whether they used sequential or native subagents, start/end time, completion of brief/memo/prototype/review, number and type of interventions, blockers, and direct observations. Do not count facilitator-made artifacts as independent completion. Report the denominator and failures. Remove personal data before sharing findings.
