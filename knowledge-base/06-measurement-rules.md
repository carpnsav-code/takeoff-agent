# 06 — Measurement Rules

Consistent measurement rules make takeoffs auditable and comparable across bids. Every quantity
carries its **source** (sheet number + scale, or schedule reference) and its **rule**.

## Area (SF)

1. Measure to **face of wall** (gross room area). Flooring is installed wall-to-wall; do not net
   out partitions' thickness beyond the room boundary.
2. **Deduct** only fixed built-ins ≥ 25 SF footprint that sit on bare slab (islands set before
   flooring, pits, curbs, equipment pads). Do **not** deduct columns < 4 SF, floor boxes, or
   drains — the cutting/detailing around them costs more than the saved material.
3. Coating **under movable equipment** (kitchen equipment on legs, racking) is included unless the
   spec says otherwise — note the assumption.
4. Separate SF subtotals by: system, room/area, floor level, phase, and new vs. existing slab.
5. Round each area line **up to nearest 5 SF**; sum then; don't round the total twice.
6. Sloped areas: take plan (horizontal) SF; slopes ≤ 2% ignore; ramps measure along the slope.
7. If plans are not to scale or dimension strings conflict, quantity = RFI, not a guess.

## Linear (LF)

1. **Cove base:** measure room perimeter minus door openings; add door jamb returns (~2× wall
   thickness each door). Record height (4"/6"/other) — LF at 4" and LF at 6" are separate lines.
   Count inside and outside corners (EA) if > 20 total.
2. **Joints:** from the structural joint layout plan (not architectural). If no layout given,
   estimate sawcut joints at spacing = 2–3× slab thickness in feet (e.g., 5" slab → 10–15 ft grid)
   and label it "estimated — layout not provided."
3. **Edge/hand-grind band (polish):** perimeter LF of all polished rooms + column perimeters.
4. **Terminations/keyways (epoxy):** LF at every doorway to unlike flooring, trench drain edge,
   dock edge, and exposed slab edge.
5. Round LF lines up to nearest 1 LF.

## Counts (EA)

- Floor drains, trench drains (also LF), cleanouts — from plumbing plans, verified against
  enlarged plans
- Columns within polished/coated areas
- Penetrations/sleeves in the field of the floor
- Doorway transitions by type
- Mock-ups (with size), moisture tests (F2170: 3 + 1/1000 SF), adhesion tests
- Mobilizations: 1 + (number of separately-released phases) + night/weekend premium noted

## Conversions & quick math

| Need | Formula |
|---|---|
| Resin gallons | SF × mils ÷ 1604 × (1 + waste %) — per layer, then sum |
| Broadcast aggregate | SF × lb/SF retained × 2 (broadcast-to-excess) − recovered |
| Densifier gallons | SF ÷ coverage (200–400 SF/gal) |
| Joint filler gallons | LF × joint width(in) × depth(in) ÷ 231 × (1+10%) |
| Cove base "SF equivalent" | LF × height(ft) — for material only; labor stays per-LF |
| Mortar/urethane cement kits | SF ÷ per-kit yield at spec thickness (from TDS) |

## Documentation standard for every takeoff line

```
| ID | Area/Room | System | Qty | Unit | Source (sheet/scale/schedule) | Notes/assumptions |
```

- One assumption per Notes cell, stated plainly ("racking area polished Level 1 per keynote 7").
- Anything not measurable = RFI reference in the Qty column ("RFI-03"), never a silent guess.
- Subtotals by system, then grand total SF, with a reconciliation line vs. gross building SF as a
  sanity check (flooring SF wildly above building footprint = measurement error).
