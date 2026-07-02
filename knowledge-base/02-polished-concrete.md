# 02 — Polished Concrete Takeoff Deep Dive

**Spec section:** 03 35 43 Polished Concrete Finishing (also seen as 03 35 10 / 03 35 00 variants,
or buried inside 03 30 00 finishes). Industry framework: ASCC/CPC (Concrete Polishing Council)
classifications.

Polished concrete is a **mechanical process**: successively finer diamond abrasives grind, hone,
and polish the slab surface, with a chemical **densifier** (lithium/sodium/potassium silicate)
applied mid-process to harden the paste. The takeoff must capture the *specified appearance* —
because appearance class dictates the number of passes, and passes are the cost.

## 1. The two numbers that define every polished concrete spec

### Aggregate exposure class (CPC Class A–D)

| Class | Name | Surface cut depth | What it means for cost |
|---|---|---|---|
| A | Cream | Very little — polish the troweled paste | Fewest grinding steps; needs a flat, well-finished slab |
| B | Fine aggregate (salt & pepper) | ~1/16" | 1–2 initial cutting passes |
| C | Medium aggregate | ~1/8" | Aggressive metal-bond grinding; more tooling |
| D | Large/coarse aggregate | ~1/4" | Deepest cut, most passes, most tooling — most expensive |

### Gloss / appearance level (CPC Level 1–4)

| Level | Finish | Image clarity (ASTM D5767) | Typical final resin grit |
|---|---|---|---|
| 1 | Flat (ground) | 0–9 | ~100 |
| 2 | Satin (honed) | 10–39 | 200–400 |
| 3 | Semi-polished | 40–69 | 800 |
| 4 | Highly polished | 70–100 | 1500–3000+ |

Specs cite gloss by **image clarity/DOI (ASTM D5767)** and **specular gloss (ASTM D523)**, haze per
ASTM D4039. If the spec gives only a marketing description ("high gloss"), RFI for the class/level.

A takeoff line for polish is therefore always **"SF of Class __ / Level __"** — e.g.,
"38,400 SF — Class B exposure, Level 3 gloss." Different class/level combos in different rooms are
**separate line items**.

## 2. Grit sequence (drives passes, tooling, and labor)

Typical progression (varies by slab hardness and target level):

- **Metal-bond diamonds** (cutting): 16/30 → 40 → 80 → 150 — number of metal steps set by exposure class
- **Densifier application** — usually after last metal or first resin step
- **Transitional/hybrids**: 50/100/200
- **Resin-bond diamonds** (polishing): 100 → 200 → 400 (Level 2 stop) → 800 (Level 3 stop) → 1500 → 3000 (Level 4)
- **Optional**: stain guard / burnished guard topcoat, high-speed burnish pass

Rule of thumb: each grit step over the full area ≈ one full-machine pass. Class D / Level 4 can be
10+ passes; Class A / Level 2 can be 5–6. Count the passes implied by the spec — that's the labor.

## 3. Everything that belongs on a polished concrete takeoff

### Floor quantities (SF)
- [ ] SF per class/level combination, per area/room, with sheet reference
- [ ] SF of **existing slab** vs **new slab** (existing = unknown prep, coating removal risk)
- [ ] SF of any **topping slab or overlay** to be polished (polishable overlays are their own system)
- [ ] SF requiring **coating/mastic/curing-compound removal** before polishing (existing buildings — separate prep line)
- [ ] SF of **dyed/stained** polish (dye is a separate material + labor pass; color count matters)
- [ ] SF of stain guard / protective topcoat if specified

### Linear quantities (LF)
- [ ] **Edge work / hand grinding** — perimeter LF at walls, columns, cases where the big machine can't reach (typically a 6–8" band done with hand grinders; slow and expensive)
- [ ] **Joint fill** — LF of construction + sawcut contraction joints, semi-rigid polyurea/epoxy filler (spec section may be 03 35 43 or 07 92 00 — verify whose scope)
- [ ] **Crack repair / routing and filling** — LF (existing slabs: carry allowance + unit price)
- [ ] Transition terminations at other flooring, doorways (LF or EA)

### Each / lump items
- [ ] **Mock-up(s)** — spec usually requires 10'×10' (often divided in 4 zones for class/level/color selection); count, size, and whether it can be in final work
- [ ] **Mobilizations** — phases, areas released separately, night work
- [ ] Columns/penetrations requiring hand work (EA)
- [ ] Floor drains / slopes (polishing machines and slopes don't mix — flag slopes > 1%)
- [ ] Gloss/DOI testing and reporting if spec requires measured verification
- [ ] Final cleaning, protection of finished floor (SF of protection board/cover if we own it)

### Materials check (sanity-check against SF)
| Material | Typical coverage |
|---|---|
| Lithium silicate densifier | 200–400 SF/gal (porous/soft slab = low end) |
| Dye | 200–400 SF/gal per coat |
| Stain guard | 1000–2000 SF/gal per coat (thin film) |
| Semi-rigid joint filler | ~100 LF/gal at 1/8" × 2" joint (varies with joint size) |

## 4. Slab conditions that change the price (pull from 03 30 00 + structural notes)

- **Cure method** — curing compounds must be ground off (adds a pass); wet cure or cure blankets are cleaner
- **Hard trowel / burnished finish** — surface hardness affects tooling choice and speed
- **Flatness (FF numbers)** — CPC recommends FF 50+ for cream finishes; a wavy slab polished to high gloss telegraphs every wave. Low spec FF + Class A = RFI
- **Mix design** — hard aggregate (granite/trap rock) vs soft (limestone) changes tooling consumption; supplementary cementitious content affects densifier uptake
- **Steel fibers** — polish over fiber-reinforced slabs exposes fibers; flag it
- **Slab age** — spec usually requires 28-day (min 14-day) cure before polishing; schedule item
- **Protection responsibility** — who protects the slab from trade damage between pour and polish, and after final polish? (Big dollar item; must be in scope letter)

## 5. Common polish scope traps

1. **"Sealed concrete" vs "polished concrete"** — finish schedules often say "SC" or "sealed" while
   a 03 35 43 spec exists. Completely different price. Always RFI the conflict.
2. **Who fills the joints** — joint fill may live in our section, in 07 92 00 (caulking sub), or
   in 03 30 00 (concrete sub). Never assume.
3. **Two-stage polishing** — grind/densify early in the project, final polish at the end = 2
   mobilizations and interim protection. Look for phasing language.
4. **Patching color mismatch** — patched areas polish differently. Carry a qualification.
5. **Under-racking areas in warehouses** — sometimes only aisles get Level 3; under-rack gets
   Level 1. Huge SF/price difference; measure aisles from the racking layout.
