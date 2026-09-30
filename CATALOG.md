# Agent and skill catalog

This workshop preserves the eight detailed role prompts and ten packaged skills from the [full PredictKit source](https://github.com/megandmartin/predictkit), adapted so a coding assistant can write files directly in `runs/<slug>/`. The original Python coordinator, structured response wrapper, implicit reference HTML, and scripted rehearsal are not part of this repository. Each role file explains its inputs, output, work, handoff, and limits. Each skill file contains the concrete decision rules or implementation checks for that work.

## Agents

| Agent | Read its complete instructions | Skills to use | Owned output under `runs/<slug>/` |
|---|---|---|---|
| Evidence lead | [research.md](agents/research.md) | `frame-opportunity`, `collect-evidence` | `research/market.md` |
| Product lead | [product.md](agents/product.md) | `frame-opportunity`, `specify-market` | `product/spec.md` |
| Solana architect | [architect.md](agents/architect.md) | `select-solana-adapter`, `specify-market` | `architecture/plan.md` |
| Chief of staff | [chief.md](agents/chief.md) | `parallel-build` | `decisions/build-memo.md` |
| App engineer | [frontend.md](agents/frontend.md) | `build-prediction-ui`, `parallel-build` | `app/index.html` |
| Market designer | [domain.md](agents/domain.md) | `specify-market`, `verify-outcome` | `app/market.json`, `domain/resolution.md` |
| Submission lead | [submission.md](agents/submission.md) | `prepare-submission`, `collect-evidence` | Three drafts under `submission/` |
| Review lead | [reviewer.md](agents/reviewer.md) | `verify-outcome`, `collect-evidence` | `qa/review.md` |

Claude Code has native project subagent definitions in `.claude/agents/pk-*.md`; each wrapper preloads the listed skills and points to the complete role file. In Codex, `agents/*.md` are explicit playbooks; Codex may delegate to separate agents when available, but a sequential run is valid. The chief memo is always a human stop point. Only a separate fresh-context pass should be called independent review.

## Skills

The two trees below are intentionally byte-identical. The Codex link is the full text; the matching Claude Code file sits at `.claude/skills/<name>/SKILL.md`.

| Skill | Full instruction | Used by |
|---|---|---|
| `frame-opportunity` | [Open](.agents/skills/frame-opportunity/SKILL.md) | Evidence lead, product lead |
| `collect-evidence` | [Open](.agents/skills/collect-evidence/SKILL.md) | Evidence lead, submission lead, review lead |
| `specify-market` | [Open](.agents/skills/specify-market/SKILL.md) | Product lead, Solana architect, market designer |
| `select-solana-adapter` | [Open](.agents/skills/select-solana-adapter/SKILL.md) | Solana architect |
| `parallel-build` | [Open](.agents/skills/parallel-build/SKILL.md) | Chief of staff, app engineer |
| `build-prediction-ui` | [Open](.agents/skills/build-prediction-ui/SKILL.md) | App engineer |
| `verify-outcome` | [Open](.agents/skills/verify-outcome/SKILL.md) | Market designer, review lead |
| `prepare-submission` | [Open](.agents/skills/prepare-submission/SKILL.md) | Submission lead |
| `run-workshop` | [Open](.agents/skills/run-workshop/SKILL.md) | Facilitator; no agent role assignment |
| `continue-sprint` | [Open](.agents/skills/continue-sprint/SKILL.md) | Participant resuming after the workshop |

## How the instructions become work

Opening the cloned folder in Codex or Claude Code makes the project skill directories discoverable according to each tool's setup. Discovery is not execution. The [copy-ready prompts](PROMPTS.md) explicitly tell the assistant which role files to read, what to write, and where to stop. A Claude Code custom subagent has its named skill content preloaded; a Codex session can read the mapped skill files or delegate when available. The assistant's actual tool access and subscription still determine what it can run. No instruction file grants blockchain access, provider spend, publication, or proof of participant outcomes.
