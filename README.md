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

Version 0.1.0 is the clean project foundation. Branding, metadata, installation structure, and the visual production rules are in place. Gameplay sprites will be rebuilt by category and added only after their layer structure and animation behavior are accounted for.

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
