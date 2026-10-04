# Website Builder

`website-builder` is a reusable AI skill for designing, building, auditing, repairing, validating, and maintaining websites with an integrated view of user goals, visual identity, web engineering, accessibility, performance, security, content, and evidence-aware multisensory psychology.

## Repository role

This repository is the canonical source for two layers:

1. **Runtime skill** — `SKILL.md`, `agents/openai.yaml`, and runtime assets.
2. **Base knowledge** — the domain modules in `references/`, loaded selectively according to the active website decision or failure mode.

The skill deliberately avoids loading the entire knowledge base for every task. It starts from the runtime workflow, then retrieves only the modules needed for the current problem.

## Structure

```text
website-builder/
├── SKILL.md
├── README.md
├── BASE_KNOWLEDGE_MAP.md
├── PROVENANCE.md
├── CHANGELOG.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── icon.svg
├── references/
│   ├── 00-KONSEP-DAN-METODE.md
│   ├── 01-PENGLIHATAN.md ... 05-SENTUHAN-DAN-PERSEPSI-TUBUH.md
│   ├── 01-analisis-kebutuhan.md ... 25-manajemen-proyek.md
│   └── 26-arsitektur-frontend-dan-konten.md ... 31-register-sumber-dan-pemutakhiran.md
├── scripts/
│   └── validate_repo.py
└── .github/workflows/
    └── validate.yml
```

## Base knowledge domains

The base knowledge combines four connected layers:

- **Human perception & multisensory psychology** — evidence discipline plus vision, hearing, smell, taste, touch, body perception, haptics, temperature, and movement.
- **Website product & UX** — requirements, information architecture, UI, UX research, accessibility, content, SEO, analytics, project management, and quality acceptance.
- **Web engineering** — HTML, CSS, JavaScript, backend, databases, HTTP/API, security, testing, deployment, maintenance, programming logic, Git, frontend architecture, and performance.
- **AI operating system for website work** — artistic direction, multisensory protocol, quality gates, AI handoff/maintenance, and source/freshness governance.

See [`BASE_KNOWLEDGE_MAP.md`](BASE_KNOWLEDGE_MAP.md) for the complete retrieval map.

## Design principles

- User job and factual truth come before decoration.
- Architecture should be the minimum needed for the task, not the maximum available stack.
- Visual identity should be distinctive without sacrificing legibility, accessibility, reliability, or task completion.
- Psychology and multisensory ideas are applied through evidence-aware hypotheses, not universal formulas.
- Website claims, integrations, performance, accessibility, security, and publication status are verified by evidence rather than confidence.
- Host permissions, deployment rights, and external-system access are never implied by skill instructions.

## Validation

Run:

```bash
python scripts/validate_repo.py
```

The validator checks the runtime skill, metadata, reference inventory, internal Markdown links, and required knowledge modules. GitHub Actions runs the same validation on pushes and pull requests.

## Source of truth

The repository should remain the canonical released source. Research updates should be made in the relevant reference module and tracked in the source register rather than copied into unrelated files.
