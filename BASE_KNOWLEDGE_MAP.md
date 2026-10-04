# Website Builder Base Knowledge Map

This file is the retrieval index for the knowledge base. Load modules by the active decision, uncertainty, risk, or failure mode rather than loading everything at once.

## Foundation and multisensory evidence

| Module | Purpose |
|---|---|
| `references/00-KONSEP-DAN-METODE.md` | Evidence quality, causal discipline, applicability, and methods for multisensory psychology. |
| `references/01-PENGLIHATAN.md` | Visual hierarchy, complexity, motion, color, light, and visual perception. |
| `references/02-PENDENGARAN.md` | Audio as controlled, informative, optional interaction rather than forced decoration. |
| `references/03-PENCIUMAN.md` | Smell, memory, contextual effects, air quality, and limits of screen-based representation. |
| `references/04-PENGECAPAN.md` | Taste/flavor representation, food choice, honesty, and safety boundaries. |
| `references/05-SENTUHAN-DAN-PERSEPSI-TUBUH.md` | Touch, haptics, texture, temperature, movement, embodiment, and device limitations. |

## Product, UX, and interface foundation

| Module | Purpose |
|---|---|
| `references/01-analisis-kebutuhan.md` | User job, constraints, facts, assumptions, risks, and definition of done. |
| `references/02-arsitektur-informasi.md` | Navigation, hierarchy, URL structure, discoverability, and information scent. |
| `references/03-desain-ui.md` | Interface composition, controls, state, hierarchy, consistency, and usability. |
| `references/04-riset-ux.md` | Research questions, usability studies, evidence, bias control, and interpretation. |

## Core web engineering

| Module | Purpose |
|---|---|
| `references/05-html.md` | Semantic HTML, forms, document structure, and native platform behavior. |
| `references/06-css.md` | Layout, responsive design, cascade, sizing, and adaptive presentation. |
| `references/07-javascript.md` | Browser interaction, state, asynchronous behavior, and client logic. |
| `references/08-backend.md` | Server boundaries, business logic, services, and application architecture. |
| `references/09-basis-data.md` | Data modeling, transactions, consistency, concurrency, and persistence. |
| `references/10-http-api.md` | HTTP semantics, URLs, APIs, integration contracts, and error behavior. |
| `references/11-keamanan-web.md` | Threat modeling, authorization, validation, secrets, dependencies, and secure development. |
| `references/12-pengujian.md` | Testing strategy, QA, behavior verification, and evidence boundaries. |
| `references/13-deployment-hosting.md` | Hosting, release, environments, configuration, and deployment verification. |
| `references/14-pemeliharaan.md` | Observability, incidents, reliability, maintenance, and lifecycle ownership. |
| `references/15-logika-pemrograman.md` | Programming logic, decomposition, algorithms, data flow, and correctness. |
| `references/16-git-kolaborasi.md` | Version control, change isolation, collaboration, and source history. |

## Quality, content, growth, and governance

| Module | Purpose |
|---|---|
| `references/17-aksesibilitas.md` | WCAG-oriented accessibility, keyboard/focus, media, reflow, and inclusive design. |
| `references/18-penulisan-konten.md` | Content design, microcopy, clarity, tone, content governance, and truthful communication. |
| `references/19-seo.md` | Search discoverability, indexing, structured content, and non-guaranteed ranking practices. |
| `references/20-performa-web.md` | Web performance, Core Web Vitals, measurement, budgets, and optimization. |
| `references/21-analitik.md` | Product measurement, event design, metrics, experimentation boundaries, and privacy-aware analytics. |
| `references/22-aset-visual.md` | Images, icons, media, responsive assets, visual quality, provenance, and optimization. |
| `references/23-dns-domain-jaringan.md` | DNS, domains, TLS, networking basics, and operational boundaries. |
| `references/24-privasi-hukum.md` | Data protection, privacy principles, legal-risk mapping, and limits of legal claims. |
| `references/25-manajemen-proyek.md` | Scope, priorities, milestones, ownership, risk, and team coordination. |

## Advanced architecture and AI workflow

| Module | Purpose |
|---|---|
| `references/26-arsitektur-frontend-dan-konten.md` | Frontend architecture, TypeScript, rendering, client/server boundaries, state, locale, and content systems. |
| `references/27-arah-artistik-dan-sistem-desain.md` | Artistic direction, identity, typography, composition, design systems, and avoiding generic AI-template output. |
| `references/28-protokol-multisensori-website.md` | Decision protocol for applying multisensory knowledge specifically to websites. |
| `references/29-gerbang-mutu-dan-bukti-penerimaan.md` | Acceptance gates, verification evidence, pass/fail/untested states, and stopping rules. |
| `references/30-alur-ai-dan-pemeliharaan-pengetahuan.md` | AI workflow, handoffs, source ownership, selective retrieval, and knowledge maintenance. |
| `references/31-register-sumber-dan-pemutakhiran.md` | Source registry, evidence classes, freshness, access limits, and update protocol. |

## Retrieval shortcuts

- New site / major redesign → `01-analisis-kebutuhan`, `27`, `28`, `29`, then relevant engineering modules.
- Navigation/content structure → `02-arsitektur-informasi`, `18-penulisan-konten`, `19-seo`.
- Visual redesign → `03-desain-ui`, `01-PENGLIHATAN`, `22-aset-visual`, `27`.
- Interaction bug → `07-javascript`, `12-pengujian`, plus `17-aksesibilitas` when input/focus/state is involved.
- Data or transaction workflow → `08-backend`, `09-basis-data`, `10-http-api`, `11-keamanan-web`, `12-pengujian`.
- Performance → `20-performa-web`, `22-aset-visual`, relevant frontend/backend modules.
- Accessibility → `17-aksesibilitas` plus HTML/CSS/JS and media-specific modules.
- Audio/haptic/multisensory feature → `00`, corresponding sensory module, `28`, and `29`.
- Release/hosting → `13-deployment-hosting`, `14-pemeliharaan`, `23-dns-domain-jaringan`, `29`.
- AI-generated website quality / maintenance → `27`, `29`, `30`, `31`.
