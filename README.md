# Machina Nexus

Machina Nexus is a texture-only graphics overhaul for Mindustry. Its visual direction is a vast autonomous machine city: black-alloy structures, deep mechanical cavities, heat cores, cable arteries, layered pipes, and colored energy networks.

The project begins again from a clean repository. It does not reuse the previous BetterGraphicMod sprite set.

## Visual direction

- Strict top-down readability for buildings, moving parts, and effects
- Smooth, angular shapes without a visible pixel grid
- Dark graphite and gunmetal machinery with controlled metallic highlights
- Orange furnace heat, cyan power flow, and violet data or high-energy channels
- Strong depth through light, shadow, recesses, and overlapping mechanical layers
- Every structure should still communicate its gameplay role at normal zoom

The theme is inspired by the broad idea of a future autonomous machine metropolis. It does not reproduce designs, symbols, characters, or imagery from any film or other franchise.

## Current status

Version 0.7.0 contains the complete Serpulo and Erekir factory sets, all eight floor, beam, and burst drills, all 26 item-transport buildings, and all 19 liquid-transport buildings: 87 buildings, 350 gameplay layers, and 68 matching factory UI/database icons. Furnace chambers, compression jaws, centrifugal rotors, pistons, liquid wells, heat channels, gas outlets, drill rotors, directional emitters, transport lanes, crossing decks, bridge machinery, routing gates, pumps, pressure valves, reservoirs, cargo clamps, and impact rams are separated according to the original build 159.7 draw order. Tiny cables and decorative surface noise were removed so each structure is identified by one dominant mechanism at gameplay zoom.

The Erekir set adds 15 machines, including the silicon arc furnace, electrolyzer, atmospheric concentrator, oxidation chamber, all heater and heat-routing blocks, both crucibles, and the cyanogen and phase synthesizers. Directional heat flow, liquid masks, gas outputs, vents, and weave animation layers remain distinct so the original effects and motion can be retained.

The drill set covers the mechanical, pneumatic, laser, blast, plasma, large plasma, impact, and eruption drills. Eight-fold cutting silhouettes keep the two small spinning rotors visually continuous, plasma emitters match their two- and three-beam mining widths, and burst drills retain separate ram, arrow, glow, impact, and mined-item layers. Floor drills use bevel-shaded, drill-specific mined-item top layers without cartoon outlines. The laser drill keeps a full angular turntable and violet guide rails below its rotating emitters. Manual drill UI/database overrides are intentionally omitted while their iOS atlas behavior is being verified.

The transport set covers all 15 Serpulo and 11 Erekir item-moving structures. Version 0.7.0 no longer treats the source sprite as artwork to recolor. The original build 159.7 files define only the runtime contract: canvas, pivot, frame count, rotation, connection state, draw order, and tint behavior. Within that contract the visible machinery is rebuilt as broad interlocking conveyor plates, recessed transfer lanes, raised crossing decks, bridge ports, phase apertures, radial routing hubs, sliding gates, cargo sockets, and a separate mass-driver launcher. The 22 one-tile structures are authored around their 32-pixel gameplay footprint, while the larger distributor, cargo blocks, and mass driver retain more secondary structure. Manual transport UI/database overrides remain omitted to avoid the previously observed iOS menu-atlas corruption.

Conveyor families keep all five connection states and four animation frames, but the old painted chevrons are replaced by moving metal plates and thin structural rails. Duct and conduit covers are reconstructed from their lower routing paths, leaving open channels for engine-drawn items and fluids instead of preserving the old full-tile glyph artwork. Stack-conveyor move/load/unload states, bridge spans, directional caps, item-color masks, and additive power-glow masks remain independent.

The liquid set covers all 19 Serpulo and Erekir pumps, conduits, junctions, bridges, routers, containers, and tanks with 68 exact-name layers. Mechanical, rotary, impulse, and reinforced pumps now expose intake manifolds, pressure rings, and central impeller apertures. Junctions use visibly separated over-under channels, storage blocks use recessed octagonal reservoirs, and bridge endpoints use repeatable channel ports. The seven renderer-tinted liquid masks remain byte-for-byte equivalent to their 4x vanilla sources.

The mandatory source-code and layer-comparison procedure is documented in `SPRITE_RENDERING_WORKFLOW.md`. It records which layers rotate, animate, glow additively, receive runtime item or liquid colors, or open a channel for engine-drawn fluid frames.

Sprites are authored at four times the vanilla raster size and rendered at the original world scale with `texturescale: 0.25`.

The mod is hidden from the in-game browser while it is incomplete.

## Installation

1. Download this repository as a ZIP from GitHub.
2. In Mindustry, open **Mods** and choose **Import Mod**.
3. Select the downloaded ZIP and restart the game if requested.

This project intentionally contains no Java or JavaScript runtime code, keeping the initial build suitable for iOS/iPadOS texture replacement.

## Repository layout

- `icon.png` — in-game mod icon
- `preview.png` — project cover and visual target
- `sprites-override/` — replacement sprites using Mindustry's original atlas names
- `STYLE_GUIDE.md` — production rules for every sprite category
- `MANIFEST.md` — version and scope record
