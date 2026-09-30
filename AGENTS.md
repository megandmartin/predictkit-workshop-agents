# PredictKit workshop agent instructions

This repository is a Markdown-only workshop kit. Do not claim its files install an orchestrator, run AI jobs, deploy to Solana, or publish an app. Work in an ignored `runs/<slug>/` directory within this repository. Never commit participant data, secrets, wallet material, or generated runs.

Read `WORKSHOP.md` for the fixed phases and `PROMPTS.md` for exact starter prompts. Use the detailed role instructions in `agents/` with all skills mapped in `README.md` from `.agents/skills/` (Codex) or `.claude/skills/` (Claude Code). Claude Code also has optional `.claude/agents/pk-*.md` subagents with those skills preloaded. In Codex, these role files are playbooks; whether separate agents can be delegated depends on the session’s available tools. Sequential execution is valid.

Freeze the founder brief before discovery. Roles research, product, and architect each receive the brief; chief reconciles their outputs. Stop after `decisions/build-memo.md` for human review. Build only after approval. Frontend, domain, and submission follow the approved brief and memo. Reviewer reads the final outputs and reports defects without inventing tests. Preserve exact question, resolution rule, and VOID policy through every phase.

Keep evidence levels distinct: proposed, source-inspected, locally executed, browser-observed, live AI response, chain read-back, public deployment, and measured participant outcome. A public repository proves publication of files, not live execution or user success.
