# v0.5.0 Sprite Batch Manifest

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
| `duo.png` | rotating turret body | follows target rotation |
| `duo-barrel-l.png` | left cannon | independent recoil index 0 |
| `duo-barrel-r.png` | right cannon | independent recoil index 1 |

`duo-base.png` is intentionally absent. Duo uses the shared vanilla
`block-1` base fallback; this keeps the static foundation visually quiet and
leaves the cannon body and recoil layers as the readable functional elements.
