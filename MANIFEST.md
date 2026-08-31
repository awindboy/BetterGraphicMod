# Machina Nexus Manifest

## 0.4.1 — Drill layer separation and atlas safety

- Reduced the rotating area of the mechanical, pneumatic, laser, and blast drills so fixed cylinders, clamps, and blast shields remain on the base.
- Added a recessed, angular bearing cavity and fixed top bezel to make the stationary chassis, moving cutter, and upper socket visibly separate.
- Replaced the shared `drill-item-2/3/4` overrides with block-specific mined-item layers for the mechanical, pneumatic, laser, and blast drills.
- Refined the existing impact and eruption mined-item layers for their central ram chamber and deep extraction shaft.
- Removed all 16 manually supplied drill UI/database icons to isolate the reported iOS menu-atlas corruption; built-in drill menu icons remain as the safe fallback.
- Verified 35 drill gameplay layers, exact 4x canvases, centered item markers, and 0.999 45-degree rotor silhouette overlap for the two small rotary drills.

## 0.4.0 — Extraction machinery

- Rebuilt all eight Serpulo and Erekir drill buildings: mechanical, pneumatic, laser, blast, plasma, large plasma, impact, and eruption.
- Added 34 exact-name gameplay sprites covering bases, rotating cutters, fixed hubs, heat rims, directional beam tops, glow masks, burst rams, impact inversion, arrows, and mined-item masks.
- Gave the mechanical and pneumatic rotors eight-fold cutting silhouettes; both retain 0.992 alpha-silhouette overlap after a 45-degree rotation.
- Matched the directional plasma-bore heads to the engine's two- and three-beam arrays instead of treating them as floor-drill rotors.
- Kept impact and eruption drills mechanically distinct with four inward-facing rams, separate charge indicators, and a deep central extraction shaft.
- Verified exact 4x build 159.7 dimensions, centered base footprints, non-empty RGBA data, and matching build-menu/database icons for every drill.

## 0.3.0 — Erekir factories and heat processing

- Rebuilt all 15 non-debug Erekir production and heat-processing buildings around one dominant, readable mechanism per structure.
- Added 70 gameplay sprites covering chassis, underlays, active tops, directional heat masks, liquid masks, gas outlets, vents, and weave layers.
- Preserved every build 159.7 atlas name, layer contract, canvas ratio, and draw alignment at 4x raster resolution.
- Added matching UI and database icons for all 15 buildings.
- Verified centered base footprints, at least 93% canvas occupancy, exact 4x dimensions, and non-empty RGBA data for every layer.
- Kept small cables, trim, bolts, and ornamental surface noise subordinate to the arc chamber, paired electrolyzer cells, intake turbine, heat channels, crucibles, cyanogen vessel, and phase spindle.

## 0.2.1 — Factory scale and readability correction

- Recentered every factory alpha footprint exactly on the vanilla canvas center.
- Expanded visible factory bounds from the inconsistent 74–94% range to approximately 95–100% of the matching tile canvas.
- Replaced dense wires, micro-pipes, bolts, and ornamental panel noise with broad structural planes.
- Enlarged each factory's defining mechanism so it remains legible at vanilla raster size.
- Rebuilt all dynamic center cutouts and moving layers from the simplified designs.
- Verified zero center offset for all 19 factory base sprites.

## 0.2.0 — Serpulo machine-city factories

- Rebuilt all 19 Serpulo production factories in the Machina Nexus machine-city style.
- Added 43 gameplay sprites covering static chassis, underlays, rotors, pistons, active tops, liquid masks, and cultivation layers.
- Preserved the build 159.7 canvas ratio and original atlas names at 4x raster resolution.
- Added matching `ui/block-*-ui.png` and `generated-icons/block-*-full.png` files so build menus and database entries use the new designs.
- Kept liquid tiles and engine-drawn flames compatible with the original block drawers.
- Added `texturescale: 0.25` so high-resolution sprites retain their vanilla world footprint.

## 0.1.0 — Clean reboot

- Removed the previous BetterGraphicMod working set from the active branch.
- Established the new internal identity `machina-nexus`.
- Added new machine-city branding and production rules.
- Kept the project texture-only and iOS/iPadOS compatible.
- Reserved `sprites-override/` for atlas-name-compatible replacements.
- Hid the mod from the in-game browser until a coherent first sprite release exists.

The previous tracked project remains recoverable from Git history. It is not part of the Machina Nexus active tree.

## Planned production order

1. Environment floors, walls, and ore integration
2. Conveyors, routers, bridges, junctions, and item transport
3. Pipes, pumps, conduits, and liquid handling
4. Drills and extraction machinery with correct moving layers
5. Power generation, storage, and distribution
6. Factories and processing buildings
7. Turrets, projectiles, heat, recoil, and muzzle effects
8. Units, weapons, engines, and animation layers
9. UI icons and database parity for all replaced content
