#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
issues = []

required = [
    "SKILL.md",
    "agents/openai.yaml",
    "assets/icon.svg",
    "README.md",
    "BASE_KNOWLEDGE_MAP.md",
    "PROVENANCE.md",
    "references/00-KONSEP-DAN-METODE.md",
    "references/26-arsitektur-frontend-dan-konten.md",
    "references/27-arah-artistik-dan-sistem-desain.md",
    "references/28-protokol-multisensori-website.md",
    "references/29-gerbang-mutu-dan-bukti-penerimaan.md",
    "references/30-alur-ai-dan-pemeliharaan-pengetahuan.md",
    "references/31-register-sumber-dan-pemutakhiran.md",
]
for rel in required:
    if not (ROOT / rel).is_file():
        issues.append(f"missing required file: {rel}")

refs = sorted((ROOT / "references").glob("*.md"))
if len(refs) != 37:
    issues.append(f"expected 37 reference modules, found {len(refs)}")

skill = (ROOT / "SKILL.md").read_text(encoding="utf-8") if (ROOT / "SKILL.md").is_file() else ""
if not skill.startswith("---\n"):
    issues.append("SKILL.md: missing YAML frontmatter")
if "name: website-builder" not in skill:
    issues.append("SKILL.md: expected name website-builder")
if "description:" not in skill[:1200]:
    issues.append("SKILL.md: description missing from frontmatter")

# Validate relative Markdown links from all Markdown files.
link_re = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
for md in [ROOT / "SKILL.md", ROOT / "README.md", ROOT / "BASE_KNOWLEDGE_MAP.md", *refs]:
    if not md.is_file():
        continue
    text = md.read_text(encoding="utf-8", errors="replace")
    for target in link_re.findall(text):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        candidate = (md.parent / target).resolve()
        try:
            candidate.relative_to(ROOT.resolve())
        except ValueError:
            issues.append(f"{md.relative_to(ROOT)}: link escapes repository: {target}")
            continue
        if not candidate.exists():
            issues.append(f"{md.relative_to(ROOT)}: broken relative link: {target}")

# Each reference should have a title.
for md in refs:
    text = md.read_text(encoding="utf-8", errors="replace")
    if not re.search(r"^#\s+\S", text, flags=re.M):
        issues.append(f"{md.relative_to(ROOT)}: missing H1 title")

print("Website Builder repository validation: " + ("PASS" if not issues else "FAIL"))
for issue in issues:
    print("- " + issue)
sys.exit(1 if issues else 0)
