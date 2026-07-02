# Agent instructions — Takeoff channel

This repo produces construction takeoffs for **concrete polishing** and **epoxy/resinous flooring**.

## SOP (the standard for this channel)

Every job runs these three steps, in order:

1. **Upload plans & specs.** The user drops documents (into `uploads/<project>/` when possible).
   Read everything: rasterize/inspect the drawings, read the spec sections word-for-word, and
   inventory what's present vs. missing.
2. **Ask any questions you need — before building.** This is a required gate, not optional. After
   the document inventory, surface anything that blocks an accurate takeoff and ask the user
   (use `AskUserQuestion` for real decisions; batch questions, don't dribble them). Typical:
   which trade/scope is ours, is there a dimensioned/CAD plan to measure from, known site/slab
   conditions, spec↔plan conflicts, or missing documents the user may have. If nothing genuinely
   blocks you, say what you're assuming and proceed. Distinguish **questions to the user** (to
   proceed) from **RFIs** (formal bid questions to the design team) — you still produce the RFI
   list in step 3.
3. **Build out the takeoff.** Produce the full package in `takeoffs/<project>/`:
   - `takeoff-quantity-sheet.csv` — completed from `templates/`
   - `scope-letter.md` — inclusions / exclusions / clarifications
   - `rfi-list.md` — numbered bid questions
   - **the marked-up-plan diagram** (`*-takeoff-diagram.html` + rendered `.png`) — the actual
     drawing with our scope highlighted, SF badged on it, and spec/measurement/quantity/risk/RFI
     panels. This is a required deliverable. Build it per `knowledge-base/07-visual-plan-markup.md`
     using the tooling in `templates/` (`rasterize-plan.py` → `takeoff-diagram-template.html` →
     `render-diagram.js`). Send the PNG to the user and commit/push everything.

The detailed per-bid workflow below expands step 3.

## Workflow for a new bid

1. **Inventory the documents.** List everything in the project's `uploads/` subfolder. Note what is
   present (specs, floor plans, finish schedule, room finish legend, details, addenda) and what is
   missing. Missing documents become RFI items, not assumptions.
2. **Read the spec sections first.** Look for:
   - 03 35 43 (Polished Concrete Finishing) and any 03 35 xx variants
   - 09 67 23 (Resinous Flooring) and sub-sections (.13, .15, .16, VA/UFGS variants)
   - 03 30 00 (Cast-in-Place Concrete) for slab mix, cure method, flatness — these affect polishing
   - 07 92 00 (Joint Sealants) and 03 01 30 (concrete repair) if joint fill/repair is in our scope
   - Division 01 for mock-ups, phasing, work hours, LEED/submittal burdens
3. **Extract the system requirements** using `knowledge-base/02` and `03`: exposure class, gloss
   level, system build/mil thickness, colors, cove base, slip additive, moisture limits, warranty.
4. **Quantify from the plans** using `knowledge-base/06-measurement-rules.md`: SF by area/system,
   LF of joints, cove base, edges and terminations, EA counts (drains, penetrations, mock-ups,
   mobilizations). State the drawing sheet and scale used for every quantity.
5. **Fill out the takeoff** by copying `templates/takeoff-quantity-sheet.csv` into
   `takeoffs/<project>/` and completing it. Also produce:
   - `scope-letter.md` from `checklists/scope-letter-template.md` (inclusions/exclusions/clarifications)
   - `rfi-list.md` — every ambiguity, conflict, or missing document as a numbered question
   - **the marked-up-plan diagram** — required; see `knowledge-base/07-visual-plan-markup.md` and
     `templates/` (rasterize the plan, copy the diagram template, render to PNG, send + commit).
6. **Run the master checklist** (`checklists/takeoff-checklist.md`) before calling it done.

## Rules

- **Never invent a quantity.** If an area can't be measured from the documents, list it as an RFI
  or a clearly-labeled allowance.
- **Flag spec/plan conflicts** (e.g., finish schedule says "sealed concrete" but spec includes
  03 35 43) instead of silently picking one.
- **Always separate polishing scope from epoxy scope** — different crews, materials, and pricing.
- **Moisture testing and mitigation are money items.** Always state whether MVER/RH limits appear
  in the spec and whether mitigation is included, excluded, or an add-alternate.
- **Surface prep is its own line.** Never bury grinding/shot blasting inside the coating line item.
- Quantities in US units: SF, LF, EA, gallons, kits. Round SF up to the nearest 5; LF to nearest 1.
- Keep every project self-contained in its `takeoffs/<project>/` folder.
