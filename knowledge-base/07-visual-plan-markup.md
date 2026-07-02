# 07 — Visual Plan Markup (the takeoff diagram standard)

Every takeoff ends in a **one-sheet marked-up plan**: the *actual* architectural drawing as the
base, with our scope highlighted, measurements badged on top, and the estimate-critical info
(spec, quantities, risks, RFIs) in side panels. This is the format the shop already uses — see the
Camp Bow Wow exemplar in `uploads/_examples-templates/`.

## The Camp Bow Wow convention (our house style)

That takeoff marks up sheet A2.0 (Finish Floor Plan) by **color-flooding each finish system on the
real plan** and boxing the SF total per finish code, tied to the finish legend:

| Color | Finish code | What | SF total |
|---|---|---|---|
| Red | **F6 — Permatek "Tempset" epoxy** | kennels/yards/groom/prep/corridor (our resinous scope) | **5,615 SF** |
| Green | F1 — 12×24 porcelain tile | iso/lux suites | 120 SF |
| Blue | F5 — vinyl plank | lobby/office/reception/restrooms | 890 SF |

Rules we copy from it:
- **Color = finish system**, one accent per system, keyed to the finish legend.
- **Box the SF total per system** right on the plan; sum matches the finish schedule.
- **Call out conflicts on the sheet** ("Flooring callout conflicts at Kennel Yard 117 & 119 —
  pricing reflects F6").
- Leave other trades' areas visible but uncolored (or lightly washed) so scope reads at a glance.

## Our extension for these bids

On top of the color-flood we add, because polish/epoxy money hides there:
- **SF badges per area** read straight off the plan tags (or scaled), plus a **net vs. gross**
  reconciliation (departments vs. departments+circulation).
- **Gray wash** on out-of-scope BOH / adjacent-tenant areas, and **carved cores** (stairs,
  escalators, elevators, pits) that don't get floor finish.
- **Side panels**: finish spec, measurements, key quantities, excluded/unit-price items, top RFIs —
  so the sheet is a self-contained bid brief.
- Every diagram states its **basis** (sheet + rev + scale) and, when the plan is schematic/undimensioned,
  says so and flags the SF as estimated pending CAD.

## Repeatable workflow (tools live in `templates/`)

1. **Rasterize the plan page/crop to PNG:**
   `pip install pymupdf` then
   `python3 templates/rasterize-plan.py <plan.pdf> <out.png> --clip X0 Y0 X1 Y1 --zoom 3.2`
   (Render once at `--zoom 1` with no clip, read the floor-plan pixel box off the image, divide by
   zoom → PDF points, re-run with `--clip`.)
2. **Copy** `templates/takeoff-diagram-template.html` into `takeoffs/<project>/` and point the
   `<image href>` at the PNG; match the `<image>`/inner-`<svg>` width:height to the crop's aspect.
3. **Trace the scope polygon** in the 1500-wide overlay space: pixel corner ÷ (crop_px_width/1500),
   clockwise. Use the translucent-fill + dashed-white-edge pair so linework shows through.
4. **Place SF badges**, gray-wash out-of-scope, carve cores, drop marker symbols.
5. **Fill the side panels** from `takeoff-quantity-sheet.csv`, the spec, and `rfi-list.md`.
6. **Render to PNG:**
   `NODE_PATH=$(npm root -g) node templates/render-diagram.js <that.html> <out.png>`
7. Deliver the PNG (render inline) alongside the HTML.

## Honesty rules on the diagram

- If the plan is **schematic/undimensioned**, the scope outline is *approximate* — say so on the
  sheet and make "confirm SF via CAD/dimensioned plan" the #1 RFI. Never present an estimated SF as
  measured.
- Badge only numbers you can source: plan tags, finish-schedule areas, or scaled measurements with
  the scale noted. Anything else is an allowance or an RFI.
- Colors are scope communication, not a substitute for the quantity sheet — the CSV remains the
  system of record.
