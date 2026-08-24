# v0.5.1 Sprite Batch Manifest

- Target: Mindustry v8 Build 159.7
- Texture scale: `0.125` (256 source pixels per tile)
- Scope: Mechanical Drill and Duo only

## Mechanical Drill

Runtime ID: `mechanical-drill`  
Class/profile: `Drill` / P08

| File | Role | Runtime behavior |
|---|---|---|
| `mechanical-drill.png` | static chassis | drawn first |
| `mechanical-drill-rotator.png` | drill bit | continuous 360-degree rotation |
| `mechanical-drill-top.png` | retaining brackets | static top layer |
| `mechanical-drill-item.png` | mined-material mask | tinted by dominant item at runtime |

The shared `drill-item-2.png` override is intentionally absent so other size-2
drills retain their vanilla item-mask behavior.

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
