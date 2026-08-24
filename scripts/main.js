// Draw the actual mined material in the center of the mechanical drill.
// The item sprites are also overridden globally, so conveyors and item UI use
// the same readable material shapes.
const Drill = Packages.mindustry.world.blocks.production.Drill;
const Blocks = Packages.mindustry.content.Blocks;
const Draw = Packages.arc.graphics.g2d.Draw;

const mechanicalDrill = Blocks.mechanicalDrill;

// Disable Drill's single shared drill-item-2 region. It is only a fallback
// sprite and cannot distinguish copper from lead, coal, or other materials.
mechanicalDrill.drawMineItem = false;

// Keep the vanilla drill simulation and animation, replacing only its draw
// hook with a per-item icon at one tile (32 world units) in the drill center.
mechanicalDrill.buildType = () => extend(Drill.DrillBuild, {
    draw(){
        this.super$draw();

        if(this.dominantItem != null){
            // The replacement icons already contain their material colors;
            // avoid tinting them with the flatter vanilla item color.
            Draw.color();
            Draw.rect(this.dominantItem.fullIcon, this.x, this.y);
            Draw.color();
        }
    }
});
