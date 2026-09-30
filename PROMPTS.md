# Copy-ready workshop prompts

Open the cloned repository as the workspace in Codex or Claude Code. Use the four prompts for your tool in order. Each prompt writes only inside the ignored `runs/workshop/` folder. Replace the example brief with a real idea before discovery, or keep it clearly labeled as a practice exercise.

The discovery prompt deliberately stops at a human approval gate. Do not send the build prompt until you have reviewed and approved the memo.

## Codex

### Prepare your brief

```text
Read AGENTS.md and WORKSHOP.md. Create runs/workshop/brief.md by copying examples/brief.md. Show me the user decision, market question, resolution rule, and VOID policy I need to edit. Ask me for my workshop idea, then stop. Do not start discovery or build anything yet.
```

### Discover and decide

```text
Read AGENTS.md, WORKSHOP.md, and runs/workshop/brief.md. Treat that brief as frozen. Run the discovery roles sequentially using agents/research.md, agents/product.md, agents/architect.md, and agents/chief.md. Read every skill assigned to each role in the README map from .agents/skills/. Write runs/workshop/research/market.md, runs/workshop/product/spec.md, runs/workshop/architecture/plan.md, and runs/workshop/decisions/build-memo.md. Keep claims at their evidence level. Stop for my review of the memo. Do not create app or submission files yet.
```

### Build the local demo

```text
I have reviewed runs/workshop/decisions/build-memo.md and approve its specific scoped off-chain simulation. If that memo recommends revising the brief or lacks an implementable contract, stop and ask me to resolve it before building. Read the frozen brief, approved memo, discovery files, and agents/frontend.md, agents/domain.md, and agents/submission.md. Run these build roles sequentially, reading every mapped skill from .agents/skills/. Write the prototype, market contract, resolution guide, and three submission drafts under runs/workshop/. Preserve the exact question, resolution rule, and VOID policy. No wallet, trade, public deployment, or official submission.
```

### Verify the result

```text
Read agents/reviewer.md, .agents/skills/verify-outcome/SKILL.md, and .agents/skills/collect-evidence/SKILL.md. Review every file under runs/workshop/ against the frozen brief and approved memo. Open the local HTML in a browser if a browser tool is available; test probability input, invalid values, close, YES, NO, VOID, repeat resolution, reload, and keyboard use. Validate market.json. Write runs/workshop/qa/review.md with what you actually executed versus only inspected. Call this independent only if a separate fresh context performs the review.
```

## Claude Code

### Prepare your brief

```text
Read AGENTS.md, CLAUDE.md, and WORKSHOP.md. Create runs/workshop/brief.md by copying examples/brief.md. Show me the user decision, market question, resolution rule, and VOID policy I need to edit. Ask me for my workshop idea, then stop. Do not start discovery or build anything yet.
```

### Discover and decide

```text
Read AGENTS.md, CLAUDE.md, WORKSHOP.md, and runs/workshop/brief.md. Treat that brief as frozen. Run pk-research, pk-product, and pk-architect from .claude/agents/ on the frozen brief when available; each has its mapped .claude/skills/ skills preloaded. Wait for all three discovery files before invoking pk-chief with those files. If subagents are unavailable, follow agents/research.md, agents/product.md, agents/architect.md, then agents/chief.md sequentially with all mapped skills. Write runs/workshop/research/market.md, runs/workshop/product/spec.md, runs/workshop/architecture/plan.md, and runs/workshop/decisions/build-memo.md. Keep claims at their evidence level. Stop for my review of the memo. Do not create app or submission files yet.
```

### Build the local demo

```text
I have reviewed runs/workshop/decisions/build-memo.md and approve its specific scoped off-chain simulation. If that memo recommends revising the brief or lacks an implementable contract, stop and ask me to resolve it before building. Read the frozen brief, approved memo, and discovery files. Use pk-frontend, pk-domain, and pk-submission in .claude/agents/ with their preloaded skills when available; otherwise use agents/frontend.md, agents/domain.md, and agents/submission.md with matching .claude/skills/. Write the prototype, market contract, resolution guide, and three submission drafts under runs/workshop/. Preserve the exact question, resolution rule, and VOID policy. No wallet, trade, public deployment, or official submission.
```

### Verify the result

```text
Use the pk-reviewer subagent in .claude/agents/ if available; otherwise follow agents/reviewer.md and .claude/skills/verify-outcome/SKILL.md. Review every file under runs/workshop/ against the frozen brief and approved memo. Open the local HTML in a browser if a browser tool is available; test probability input, invalid values, close, YES, NO, VOID, repeat resolution, reload, and keyboard use. Validate market.json. Write runs/workshop/qa/review.md with what you actually executed versus only inspected. Call this independent only if a separate fresh context performs the review.
```
