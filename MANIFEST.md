# Machina Nexus Manifest

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
