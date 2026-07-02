# SOP — Takeoff Channel

The standard way every takeoff runs here (concrete polishing + epoxy/resinous flooring).

## 1. Upload plans & specs
Drop the documents in — ideally into `uploads/<project>/` (drawings, spec sections, finish
schedule, addenda, anything). The agent reads all of it: renders and inspects the drawings, reads
the specs, and lists what's present vs. missing.

## 2. The agent asks any questions it needs
Before building anything, the agent surfaces whatever would otherwise force a guess and asks you —
e.g. which scope is ours, whether a dimensioned/CAD plan exists to measure from, known
site/slab conditions, or spec-vs-plan conflicts. Answer what you can; anything still open becomes a
documented RFI. If nothing blocks it, the agent states its assumptions and proceeds.

## 3. The agent builds the takeoff
Delivered in `takeoffs/<project>/`:
- **Quantity sheet** (`takeoff-quantity-sheet.csv`) — SF/LF/EA by system, with sources
- **Scope letter** (`scope-letter.md`) — inclusions, exclusions, clarifications, unit prices
- **RFI list** (`rfi-list.md`) — numbered questions for the design team
- **Marked-up-plan diagram** (`*-takeoff-diagram.png`) — the real drawing with our scope
  highlighted, square footage badged on it, and spec/measurement/quantity/risk/RFI panels

Then you price it into the estimate.

---
*House style and the repeatable diagram workflow: `knowledge-base/07-visual-plan-markup.md`.
Style exemplar: `uploads/_examples-templates/` (Camp Bow Wow). Agent behavior: `CLAUDE.md`.*
