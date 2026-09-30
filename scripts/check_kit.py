#!/usr/bin/env python3
"""Dependency-free structure check for the Markdown-only workshop kit."""
from html import unescape
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
ROLE_SKILLS = {
    "research": ("frame-opportunity", "collect-evidence"),
    "product": ("frame-opportunity", "specify-market"),
    "architect": ("select-solana-adapter", "specify-market"),
    "chief": ("parallel-build",),
    "frontend": ("build-prediction-ui", "parallel-build"),
    "domain": ("specify-market", "verify-outcome"),
    "submission": ("prepare-submission", "collect-evidence"),
    "reviewer": ("verify-outcome", "collect-evidence"),
}
OPERATOR_SKILLS = {"run-workshop", "continue-sprint"}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(f"FAIL: {message}")


for role, skills in ROLE_SKILLS.items():
    role_file = ROOT / "agents" / f"{role}.md"
    wrapper_file = ROOT / ".claude" / "agents" / f"pk-{role}.md"
    require(role_file.is_file(), f"missing role {role}")
    require(wrapper_file.is_file(), f"missing Claude subagent {role}")
    role_text = role_file.read_text()
    require(len(role_text.split()) >= 180, f"role {role} lost its detailed guidance")
    require("runs/<slug>/" in role_text, f"role {role} has no standalone output path")
    wrapper_text = wrapper_file.read_text()
    require(wrapper_text.startswith("---\n") and "\n---\n" in wrapper_text[4:], f"invalid wrapper {role}")
    listed = tuple(re.findall(r"^  - ([\w-]+)$", wrapper_text, re.M))
    require(listed == skills, f"wrong preloaded skills for {role}: {listed}")
    for skill in skills:
        require(f"`{skill}`" in (ROOT / "CATALOG.md").read_text(), f"catalog missing {skill}")

expected = set().union(*[set(v) for v in ROLE_SKILLS.values()], OPERATOR_SKILLS)
for tree in (".agents", ".claude"):
    skill_root = ROOT / tree / "skills"
    names = {path.name for path in skill_root.iterdir() if path.is_dir()}
    require(names == expected, f"{tree} skill inventory mismatch: {names ^ expected}")
    for name in names:
        source = skill_root / name / "SKILL.md"
        require(source.is_file(), f"missing {tree}/{name}/SKILL.md")
        text = source.read_text()
        require(re.match(rf"^---\nname: {re.escape(name)}\ndescription: .+\n---\n", text), f"invalid skill frontmatter: {tree}/{name}")
        if tree == ".claude":
            require(source.read_bytes() == (ROOT / ".agents" / "skills" / name / "SKILL.md").read_bytes(), f"skill trees differ: {name}")

html = (ROOT / "docs" / "index.html").read_text()
markdown = (ROOT / "PROMPTS.md").read_text()
require(html.count("data-copy") == 9, "expected eight copy buttons plus one selector reference")
for platform, start, end in (
    ("Codex", '<div id="panel-codex"', '<div id="panel-claude"'),
    ("Claude Code", '<div id="panel-claude"', '</div></div><p class="note">'),
):
    panel = html.split(start, 1)[1].split(end, 1)[0]
    prompts = re.findall(r"<pre>(.*?)</pre>", panel, re.S)
    require(len(prompts) == 4, f"{platform} must have four prompts")
    for prompt in prompts:
        require(unescape(prompt).strip() in markdown, f"{platform} visual prompt differs from PROMPTS.md")
for asset in ("docs/favicon.svg", "docs/fonts/spacegrotesk-variable.ttf", "docs/fonts/spacegrotesk-OFL.txt"):
    require((ROOT / asset).is_file(), f"missing visual guide asset: {asset}")
for doc in ROOT.rglob("*.md"):
    if any(part in {"runs", ".local", ".git", ".playwright-cli"} for part in doc.parts):
        continue
    content = doc.read_text()
    require("/Users/" not in content, f"private local path in {doc}")
    for target in re.findall(r"\]\(([^)]+)\)", content):
        if target.startswith(("https://", "http://", "#")):
            continue
        require((doc.parent / target).exists(), f"broken local link {target} in {doc}")
print("PASS: 8 detailed roles, 10 mirrored skills, Claude mappings, prompts, assets, and local links")
