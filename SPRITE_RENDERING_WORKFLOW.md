# Sprite Rendering Workflow

Machina Nexus sprites must be designed from Mindustry build 159.7 runtime behavior, not from a single flattened preview. A source-shaped alpha mask alone is not proof that a replacement behaves correctly.

## Required audit before drawing

1. Read the block declaration in `mindustry.content.Blocks`.
   Record block size, rotation, placement direction, consumed resources, produced resources, power state, liquid or gas behavior, and any custom drawer.
2. Read the block class and every `DrawBlock` used by that declaration.
   Record each `@Load` atlas name, draw order, rotation, animation index, additive blend, runtime tint, liquid frame, and generated effect.
3. Lay out every original sprite as an individual layer.
   Also produce a runtime-order composite, all connection variants, all animation frames, and all four rotations where applicable.
4. Resprite each layer according to its role.
   Never flatten an animated, tinted, rotating, or connection-dependent set into one finished illustration.
5. Compare original and replacement at both 4x production resolution and `texturescale: 0.25` gameplay resolution.
6. Validate exact canvas and alpha contracts, then validate semantic contracts such as distinct animation frames, preserved connection luminance, and unmodified runtime masks.
7. Only after the comparison sheets pass may the result be committed and tested in-game.

## Build 159.7 transport contracts

| System | Runtime behavior | Required sprite treatment |
| --- | --- | --- |
| Standard, titanium, armored conveyors | Five raw connection shapes are selected by autotiling. Four frames are advanced by `Time.time`, then the selected image is rotated to placement direction. Items are drawn above it. | Preserve the mechanism in every connection/frame image. Color and metal changes may not cover the chevrons, bends, merges, or side-entry shapes. |
| Plastanium and surge stack conveyors | Three images represent move, load, and unload states. Edge pieces close disconnected sides. The stack image moves between tiles and rotates. Surge glow and edge glow are drawn additively and multiplied by runtime power color. | Keep all three states visually distinct. Keep stack separate. Glow images remain neutral runtime masks. |
| Duct and armored duct | Five lower and five upper connection layers are independently selected and rotated. Items pass between the two visual levels. | Preserve openings and routing marks in both levels. Never bake an item sprite into either layer. |
| Bridges and phase bridges | Endpoint, bridge span, end cap, and arrow images are repeated dynamically between linked blocks. Phase bridges pulse their arrow treatment. | Design each repeated segment independently and keep its horizontal alignment and repeat seam exact. |
| Duct bridge and reinforced liquid bridge | Static body and rotated direction cap are cached. Bridge bottom, bridge top, arrows, and optional liquid mask are stretched or repeated between endpoints. | Preserve direction cap orientation, stretch-safe center sections, and runtime liquid masks. |
| Sorters | With no selected item, a cross layer is drawn. With an item selected, the game fills the tile with the item color and draws the sorter cover above it. | The cover must retain a clear window. Do not pre-color the selected-item area. |
| Unloaders and cargo unload points | Center or top layers are multiplied by the configured item color at runtime. | These layers remain neutral masks so copper, lead, coal, and every other item retain their real colors. |
| Duct router and directional unloader | The body is fixed. The top or arrow is rotated by installation direction. Selected-item center masks replace the normal directional top. | Keep body, rotated top, arrow, and item mask separate. |
| Mass driver | Base is fixed. The complete upper launcher rotates toward its target and moves backward under recoil; a separate engine shadow is generated. | The upper sprite must read correctly through 360 degrees and must not include the fixed base or a baked shadow. |
| Conduits | Five lower and five upper connection layers are selected and rotated. Animated liquid or gas frames are drawn between them, with special corner cropping and end caps. | Keep the central channel transparent/open for runtime fluid. Preserve every cap and connection shape. |
| Pumps | The normal pump sprite is drawn first. `DrawPumpLiquid` then draws `name-liquid` over it, tinted to the liquid being pumped and filled according to stored amount. | The liquid layer is a neutral fill mask. The pump body must remain legible both empty and with the tinted mask over it. |
| Liquid routers, containers, and tanks | Bottom is drawn first, animated liquid/gas tiles are drawn inside the configured padding, and the normal region is drawn last as the cover. | Preserve the viewing opening and padding. Do not paint a fixed liquid into the body or close the opening. |

## Automated checks for the current set

- 134 item-transport layers: exact source-relative path, 4x canvas size, and alpha geometry.
- 68 liquid-transport layers: exact source-relative path, 4x canvas size, and alpha geometry.
- 15 conveyor connection/frame sets: four distinct frames per set and source-luminance correlation of at least 0.70.
- 30 duct and conduit upper connection layers: source-luminance correlation of at least 0.90.
- 14 runtime-tinted or additive layers: exact 4x source values, with no baked accent color.

These checks do not replace an in-game test. They prevent the specific failure where a visually finished overlay hides the original motion or connection mechanism while still passing a size and alpha test.
