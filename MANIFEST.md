# v0.8.2 Sprite Batch Manifest

- Target: Mindustry v8 Build 159.7
- Texture scale: `0.125` (256 source pixels per tile)
- Scope: Complete Build 159.7 drill family plus Duo

## Conventional drills

Runtime IDs: `mechanical-drill`, `pneumatic-drill`, `laser-drill`, `blast-drill`  
Class/profile: `Drill` / P08

| File | Role | Runtime behavior |
|---|---|---|
| `<id>.png` | static chassis | drawn first |
| `<id>-rotator.png` | drill head | continuous 360-degree rotation |
| `<id>-top.png` | retaining structure | static top layer |
| `<id>-item.png` | mined-material mask | tinted by dominant item at runtime |
| `blast-drill-rim.png` | heat rim | additive warmup pulse |

Per-block item masks are used. Shared `drill-item-2/3/4` regions remain untouched.

### v0.8.2 Serpulo drill identities

- `mechanical-drill`: intermeshed brass gear train, five shallow spiral cutter tiers, and small brass wedge teeth
- `pneumatic-drill`: valved air reservoirs, readable hoses, five shallow spiral cutter tiers, and small silver wedge teeth
- `laser-drill`: four pointer emitters and four thick beams in the rotating region
- `blast-drill`: furnace base, additive heat rim, layered static armor, and a red blast-wall rotor

## Beam drills

Runtime IDs: `plasma-bore`, `large-plasma-bore`  
Class/profile: `BeamDrill` / P09

| File pattern | Role | Runtime behavior |
|---|---|---|
| `<id>.png` | static chassis | drawn first |
| `<id>-top.png` | directional emitter | rotates in 90-degree build directions |
| `<id>-glow.png` | emitter glow | additive warmup and boost tint |
| `drill-laser*.png` | beam family | normal and boosted beam/body/end regions |

## Burst drills

Runtime IDs: `impact-drill`, `eruption-drill`  
Class/profile: `BurstDrill` / P10

| File pattern | Role | Runtime behavior |
|---|---|---|
| `<id>.png` | static chassis | drawn first |
| `<id>-top.png` | impact mechanism | static top layer |
| `<id>-top-invert.png` | impact flash plate | timed inversion overlay when present |
| `<id>-item.png` | mined-material mask | tinted by dominant item at runtime |
| `<id>-arrow.png` | progress indicator | four-way staged motion |
| `<id>-arrow-blur.png` | impact highlight | additive completion pulse |
| `<id>-glow.png` | chamber glow | additive progress glow when present |

All drill sprites use the original Build 159.7 geometry and palette as their
source. The 8x source resolution removes visible pixel staircases and adds
restrained directional shading without changing pivots or runtime motion.

## Duo

Runtime ID: `duo`  
Class/profile: `ItemTurret` + `DrawTurret` / P24

| File | Role | Runtime behavior |
|---|---|---|
| `duo-base.png` | static foundation | replaces the shared vanilla `block-1` fallback |
| `duo.png` | rotating turret body | follows target rotation |
| `duo-barrel-l.png` | left cannon | independent recoil index 0 |
| `duo-barrel-r.png` | right cannon | independent recoil index 1 |
| `duo-outline.png` | turret-body under-outline | replaces the generated vanilla body outline |
| `duo-barrel-l-outline.png` | left-cannon under-outline | follows the left cannon layer |
| `duo-barrel-r-outline.png` | right-cannon under-outline | follows the right cannon layer |
| `duo-preview.png` | neutral upper assembly | supplies build preview and runtime shadow silhouette |

Every visible or silhouette-producing Duo region is overridden. This prevents
the vanilla shared base, generated outlines, or preview shadow from remaining
behind the custom rotating assembly. The upper assembly occupies roughly 80%
of the tile width at neutral recoil while preserving the original pivot and
the two independent recoil indices.
