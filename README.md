# experiment-ideas (Claude Code skill)

Turns a store's research into a prioritised list of CRO experiments, drawn from a library of 200+ canonical ideas with the public test evidence behind each one. Interviews you about the data you have (analytics funnel, surveys, heatmaps, reviews, past tests), diagnoses where the store leaks revenue, maps ideas onto the leaks, and tells you which research to run next.

## Install
1. Copy this folder to `~/.claude/skills/experiment-ideas/` (so `SKILL.md` sits at `~/.claude/skills/experiment-ideas/SKILL.md`).
2. Add to `~/.claude/CLAUDE.md`:
   ```
   - **experiment-ideas** (`~/.claude/skills/experiment-ideas/SKILL.md`) - prioritised CRO experiments from research. Trigger: `/experiment-ideas`
   When the user types `/experiment-ideas`, invoke the Skill tool with `skill: "experiment-ideas"` before doing anything else.
   ```
3. In Claude Code, type `/experiment-ideas` and answer the questions. Paste CSVs, screenshots, or "don't have it".

## What is inside
- `SKILL.md` — the workflow (intake, research gaps, diagnosis, mapping, output).
- `research-playbook.md` — the research to run and the exact questions.
- `library/library.json` — 207 ideas with grades, win/loss counts, effort, risk, industry fit, plus 310 public case-study evidence rows.
- `scripts/query.py` — filter and rank the library: `python3 scripts/query.py --page pdp,cart --lever friction --industry consumables --min-grade B --top 20`.

Third-party results in the library are benchmarks from public case studies (Conversion Rate Experts, Blend Commerce, Conversion.com, SplitBase, MECLABS, Optimizely, Evidoo free tier). They are not this library's own results; treat them as priors, not promises. Grade D ideas are the ones that reliably lose; the skill will tell you not to run them.
