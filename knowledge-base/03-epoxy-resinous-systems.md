# 03 — Epoxy & Resinous Flooring Takeoff Deep Dive

**Spec section:** 09 67 23 Resinous Flooring (sub-sections .13 thin-set/troweled epoxy toppings,
.15/.16 fuel-resistive systems, VA/UFGS agency variants). Related: 09 61 36 static-resistive
flooring, 09 96 23 concrete coatings, 07 18 00 traffic coatings (if decks show up).

Resinous flooring is a **build-up of liquid-applied layers**. The takeoff must identify the exact
**system build** — every layer, its material, and its thickness — because material cost scales
directly with mils, and labor scales with the number of passes and broadcasts.

## 1. Know the system types (and their tells in a spec)

| System | Nominal thickness | Build | Where it shows up |
|---|---|---|---|
| Thin-film / high-perf coating | 10–20 mils | primer + 1–2 coats epoxy/urethane | Mechanical rooms, storage, light traffic |
| Self-leveling (SL) epoxy | 20–40 mils (up to 1/8") | primer + pigmented SL body + topcoat | Labs, clean mfg, corridors |
| **Double-broadcast quartz** | 1/8" (125 mils) | primer + body coat/broadcast ×2 + grout + topcoat | Kitchens, restrooms, kennels, locker rooms |
| Decorative flake/chip | 40–90 mils | primer + body + flake to rejection + 1–2 clear coats | Retail, corridors, garages |
| Troweled epoxy mortar | 1/4" (250 mils) | primer + troweled mortar + grout coat + topcoat | Heavy industrial, impact areas |
| **Urethane cement (cementitious urethane)** | 1/4"–3/8" SL or troweled | often self-priming; broadcast option; topcoat | Commercial kitchens, breweries, food plants, thermal-shock/wash-down areas |
| ESD / conductive | ~30–40 mils | conductive primer + ground straps + static-dissipative topcoat | Electronics, ordnance, operating rooms |
| MMA (methyl methacrylate) | 1/8"–1/4" | fast-cure acrylic equivalent of broadcast systems | Coolers/freezers, fast-turnaround retail |
| Chemical-resistant Novolac | varies | Novolac epoxy body/topcoat | Battery rooms, secondary containment |
| Moisture vapor barrier (MVB) epoxy | 16–20 mils | 100%-solids moisture-tolerant epoxy | Under any system when RH/MVER exceeds limits |

**Takeoff rule:** every distinct system = separate line item. A job with kitchen urethane cement +
restroom quartz + mechanical-room thin-film is three systems, three crews' worth of passes, three
material sets — even if it's all "epoxy" to the GC.

## 2. Coverage math (the material half of the takeoff)

Theoretical coverage of 100%-solids resin: **1 gallon = 1604 SF at 1 mil** (1604 ÷ mils = SF/gal).

| Layer | Typical spread rate |
|---|---|
| Epoxy primer (8–10 mils) | 160–200 SF/gal |
| SL body coat (~25 mils neat) | ~64 SF/gal |
| Broadcast body coat (~12–16 mils before sand) | 100–130 SF/gal |
| Grout/seal coat over broadcast | 60–100 SF/gal (texture eats material) |
| Urethane or polyaspartic topcoat (2–3 mils) | 300–500 SF/gal |
| Urethane cement SL @ 1/4" | per-kit yield, ~20–25 SF/kit typical (verify TDS) |
| Quartz/sand broadcast | 0.5–1.0 lb/SF stays in floor per broadcast (broadcast to excess ~2×) |
| Flake to rejection | 0.15–0.25 lb/SF retained |

Add 5–10% waste; more on rough/porous prep profiles. Always reconcile spec mils vs. manufacturer
TDS spread rates — when the spec says "1/4 inch nominal" the takeoff carries 1/4", not the cheaper
TDS minimum.

## 3. Everything that belongs on an epoxy/resinous takeoff

### Floor quantities (SF)
- [ ] SF per system, per area, with sheet reference and system ID from the finish legend
- [ ] SF of surface prep by method (see doc 04) — **always its own line**
- [ ] SF of moisture mitigation (in / out / unit price — never silent)
- [ ] SF of slip-resistant texture zones vs smooth (aggregate additive changes topcoat coverage)
- [ ] SF under equipment/coolers/pits that may need different or no coating
- [ ] Sloped floors to drains (SL systems can't hold a slope — mortar/urethane cement zones around drains)
- [ ] Existing coating removal SF (existing buildings; separate from profiling)

### Linear quantities (LF)
- [ ] **Integral cove base** — LF × height (4" and 6" standard); cove is hand-troweled and priced
      per LF, often ≥ the cost of several SF of field floor. Count inside/outside corners (EA) too
- [ ] **Termination details** — keyed/saw-cut joints ("keyways") at doorways, trench drains, slab
      edges, transitions to other flooring (LF)
- [ ] **Joint treatment** — which joints get filled and coated over vs. honored (reflected up
      through the system and sealed)? LF each way; moving joints get flexible sealant (07 92 00 —
      whose scope?)
- [ ] **Crack treatment** — routed/filled, or fiberglass-scrim detailed (LF + allowance)
- [ ] Trench drain edges, dock edges, ramps (LF)

### Each / lump items
- [ ] **Floor drains and cleanouts** (EA) — each one is hand detail work, slope-to-drain, and a
      termination
- [ ] Penetrations, bollards, column bases, equipment pads (EA)
- [ ] Mock-up(s) / sample area (size and count per spec)
- [ ] Moisture testing (EA tests — F2170 rule: 3 probes for first 1000 SF + 1 per additional 1000 SF)
- [ ] Adhesion/pull-off tests if spec requires (ASTM D7234)
- [ ] Mobilizations / phases / night-work premiums
- [ ] Ventilation/containment for odor-sensitive occupied buildings (MMA especially)
- [ ] ESD systems: ground straps (EA) and post-install resistance testing

### Spec attributes that change price (extract every one)
- [ ] Exact **system thickness** and layer count
- [ ] **Manufacturer basis-of-design** and "or equal" allowance (sole-source = no material leverage)
- [ ] **Color(s)** — customs and multi-color layouts with tape lines cost more; count colors and LF of demarcation/striping
- [ ] **Chemical exposure** requirements (Novolac vs standard epoxy ≈ big material delta)
- [ ] **Slip resistance** (DCOF/ANSI A326.3 or "broadcast to texture") 
- [ ] **Temperature/thermal shock** (drives urethane cement)
- [ ] **Cure/turnaround requirements** (fast-track = MMA or polyaspartic = $$)
- [ ] **Warranty** — 5-year single-source labor+material warranties carry cost
- [ ] USDA/FDA/ESD certifications, submittal and QC burden

## 4. Common epoxy scope traps

1. **Cove base buried in a wall detail.** Finish plans show floor SF; cove shows up only in
   interior elevations or detail sheets. Missing 800 LF of 6" cove is a five-figure error.
2. **"Prep by others."** Almost never true in practice. Own the prep or exclude it in writing.
3. **Moisture mitigation ambiguity.** If the spec lists an MVB "where required by testing," bid it
   as a unit-price add — never lump it in silently, never omit it silently.
4. **New concrete cure time.** 28-day minimum before coating (some urethane cements allow 7–10).
   If schedule shows coating at day 14, RFI — or price a moisture-tolerant primer.
5. **Drains set high/low.** Slope-to-drain rework is not in a coating bid; qualify that drains and
   slab slopes are by others.
6. **Existing floor demo.** "Remove existing VCT/epoxy/tile" — is mastic removal ours? Abatement
   (asbestos mastic) is NEVER ours; qualify it.
7. **Wall protection & overspray.** Occupied kitchens: masking, equipment moving, refrigeration
   downtime — clarify who moves what.
