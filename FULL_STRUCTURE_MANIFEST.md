# Load-safe Build 159.7 structure chassis batch

- Target: Mindustry v8 Build 159.7
- Texture contract: `texturescale: 0.125` (8x source dimensions)
- Player-buildable primary chassis and explicit foundation regions: 256
- Hand-authored pre-existing Drill/Duo regions retained: 71 source regions
- Total decoded override budget: approximately 595 MiB before atlas packing

All runtime secondary layers not already hand-authored remain vanilla. This
preserves animation, recoil, team tint, liquid tint, heat and glow behavior
while avoiding the multi-gigabyte decoded atlas cost of overriding every frame.
