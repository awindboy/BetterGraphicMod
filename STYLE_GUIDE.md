# Machina Nexus Sprite Style Guide

## 1. Camera and silhouette

- Every gameplay sprite is designed for Mindustry's strict top-down camera.
- A building's primary function must remain legible at normal gameplay zoom.
- Rotators, barrels, belts, pumps, drills, and other moving layers must make physical sense around their actual pivot.
- Silhouettes are angular and engineered. Avoid soft toy-like rounding and ornamental complexity that obscures function.

## 2. Surface language

- Use smooth, clean raster shapes without a visible pixel grid.
- Separate parts primarily with value, reflected light, cast shadow, and recess depth—not thick colored outlines.
- Outer edges may use a restrained dark contact edge, but internal parts should read through lighting and overlap.
- Major panels are broad enough to remain readable; fine details support them rather than competing with them.

## 3. Palette

| Role | Reference color | Use |
| --- | --- | --- |
| Deep recess | `#0b0e12` | Open shafts, vents, gaps, underside shadow |
| Black alloy | `#151a20` | Main chassis and heavy armor |
| Gunmetal | `#2a3139` | Structural frames and mechanical panels |
| Steel | `#59636d` | Moving interfaces, rails, clamps, wear surfaces |
| Edge reflection | `#aeb8c2` | Small controlled highlights only |
| Furnace orange | `#e26b2d` / `#ffad45` | Heat, smelting, high-load machinery |
| Energy cyan | `#4bbbd2` | Power flow, cooling, stable energy |
| Data violet | `#7d55b6` | Logic, phase, high-energy processing |

Base content colors may shift within this system, but a resource, team, or functional cue must not become ambiguous.

## 4. Depth stack

Sprites should read as five physical depth bands:

1. Floor contact and deep occlusion
2. Recesses, channels, cavities, and under-structure
3. Main chassis and load-bearing frame
4. Functional moving assembly or exposed mechanism
5. Emissive material, heat, beams, and temporary effects

Highlights come from the upper-left; contact shadow accumulates toward the lower-right. Emissive parts illuminate nearby metal subtly instead of being painted as flat saturated shapes.

## 5. Dynamic layers

- Preserve the original canvas size, transparent bounds, pivot, frame count, and layer naming unless the game code is verified to use a different contract.
- A moving layer must not contain a baked-in copy of the static base.
- Rotational symmetry must match animation speed so motion does not visibly stutter.
- Muzzle flashes, heat, liquid, item, glow, and effect masks stay on their intended layers.
- Validate each sprite both isolated and composited in original draw order.

## 6. Functional design rules

- Conveyors expose a believable belt surface, guide rails, rollers, and direction while preserving tile connectivity.
- Pipes expose channel depth, joints, pressure hardware, and flow readability without becoming visually heavier than buildings.
- Drills emphasize the cutting or energy-delivery mechanism and the force path into the ground.
- Turrets separate base, traverse body, weapon mount, and moving barrel through depth and shadow.
- Factories reveal only the machinery needed to explain their process: intake, transformation chamber, energy source, and output.
- Power buildings show generation, storage, transfer, or conversion as distinct mechanisms rather than generic glowing boxes.

## 7. Prohibited shortcuts

- No direct reproduction of Matrix imagery, green code rain, franchise symbols, or recognizable film machinery
- No excessive bloom, neon wash, or contrast that hides gameplay state
- No photorealistic textures that clash with Mindustry's clean sprite language
- No thick cartoon outlines around every internal component
- No generic circular ornament placed where a working mechanism should be
- No changes to gameplay data merely to support a visual idea
