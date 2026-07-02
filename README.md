# Takeoff Agent — Concrete Polishing & Epoxy Systems

This repo is the working channel for building construction takeoffs for **polished concrete**
(CSI 03 35 43) and **epoxy / resinous flooring systems** (CSI 09 67 23).

## How this channel works

1. **Upload documents** — spec sheets, drawings/plans, finish schedules, addenda, RFI responses,
   geotech/slab info, or anything else for a bid — into the `uploads/` folder, ideally under a
   per-project subfolder (e.g. `uploads/2026-riverside-warehouse/`).
2. **Ask for a takeoff.** The agent reads the documents, extracts scope using the knowledge base,
   quantifies everything, and produces a completed takeoff in `takeoffs/<project-name>/`.
3. **Review the output** — quantity sheet, scope letter (inclusions/exclusions), and RFI list.

## Repo layout

| Path | Purpose |
|---|---|
| `knowledge-base/` | Deep-dive reference docs on what belongs on a takeoff for each trade |
| `checklists/` | Master takeoff checklist and scope letter template |
| `templates/` | Blank quantity-sheet templates to copy per project |
| `uploads/` | Drop zone for specs, plans, and bid documents (one subfolder per project) |
| `takeoffs/` | Completed takeoffs, one subfolder per project |
| `CLAUDE.md` | Instructions the agent follows when processing uploads |

## Knowledge base index

1. [Takeoff fundamentals](knowledge-base/01-takeoff-fundamentals.md) — what a takeoff is, units, process, waste factors
2. [Polished concrete](knowledge-base/02-polished-concrete.md) — exposure classes, gloss levels, grit sequences, densifiers, quantities
3. [Epoxy & resinous systems](knowledge-base/03-epoxy-resinous-systems.md) — system types, mil builds, coverage rates, cove base
4. [Surface prep & moisture](knowledge-base/04-surface-prep-and-moisture.md) — CSP profiles, shot blast vs. grind, ASTM moisture testing, mitigation
5. [Reading plans & specs](knowledge-base/05-reading-plans-and-specs.md) — where scope hides in bid documents, finish schedules, RFI triggers
6. [Measurement rules](knowledge-base/06-measurement-rules.md) — how to quantify SF/LF/EA, deducts, edges, joints, mobilizations
