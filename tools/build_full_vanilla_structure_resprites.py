"""Build a complete high-resolution override set for Mindustry v159.7 blocks.

This is intentionally source-driven: every filename comes from Blocks.java and
the pinned raw assets, so moving, tinted, mirrored and animated regions retain
their original runtime contract. Static chassis regions receive restrained
top-left highlight / lower-right shadow treatment; semantic animation masks are
only scaled and smoothed.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path

from PIL import Image, ImageChops, ImageEnhance, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "sprites-override"
SCALE = 8

# These are renderer-owned masks or independently animated pieces. Changing
# their illumination would change runtime tint, additive heat or recoil cues.
DYNAMIC_TOKENS = {
    "team", "item", "liquid", "heat", "glow", "light", "laser", "beam",
    "arrow", "blur", "top", "bottom", "out", "in", "side", "barrel",
    "front", "back", "mid", "rotator", "piston", "weave", "vent", "cap",
    "end", "edge", "stack", "over", "nozzle", "blade", "spine", "mouth",
    "missile", "center", "thruster", "pod", "preview", "open", "cross",
}

SHARED_PREFIXES = (
    "block-", "reinforced-block-", "factory-", "duct-bottom-", "conduit-bottom-",
    "drill-laser", "laser", "launchpod", "cross-full",
)

# `Blocks.java` also declares world floors, props and other map decoration.
# Only these raw-sprite categories correspond to player-installable structures.
BUILDING_DIRECTORIES = {
    "campaign", "defense", "distribution", "drills", "liquid", "logic",
    "payload", "power", "production", "sandbox", "storage", "turrets",
    "units", "walls",
}


def runtime_ids(blocks_java: Path) -> set[str]:
    text = blocks_java.read_text(encoding="utf-8")
    # Block declarations are the source of truth. This avoids accidentally
    # including environmental sprites that happen to live under blocks/.
    return set(re.findall(r'^\s*\w+\s*=\s*new\s+\w+\("([^"]+)"\)', text, re.M))


def belongs_to_block(stem: str, ids: set[str]) -> bool:
    return any(stem == block_id or stem.startswith(block_id + "-") for block_id in ids)


def include_shared(stem: str) -> bool:
    return stem.startswith(SHARED_PREFIXES)


def is_dynamic_region(stem: str) -> bool:
    if stem.startswith(("block-", "reinforced-block-")):
        return False
    tokens = stem.split("-")[1:]
    return any(token in DYNAMIC_TOKENS or token.isdigit() for token in tokens)


def scaled(source: Image.Image) -> Image.Image:
    return source.resize((source.width * SCALE, source.height * SCALE), Image.Resampling.LANCZOS)


def enhance_static(source: Image.Image) -> Image.Image:
    """Add only restrained material depth; preserve silhouette and palette."""
    image = scaled(source.convert("RGBA"))
    alpha = image.getchannel("A")
    # Existing Mindustry sprites already encode their colour identity. A very
    # small contrast/saturation lift and clipped directional value gradient
    # adds readable metal/ceramic planes without changing faction/material hue.
    rgb = ImageEnhance.Contrast(image.convert("RGB")).enhance(1.045)
    rgb = ImageEnhance.Color(rgb).enhance(1.025).convert("RGBA")
    rgb.putalpha(alpha)

    gradient = Image.linear_gradient("L").resize(image.size, Image.Resampling.BILINEAR)
    highlight_alpha = gradient.point(lambda value: max(0, 18 - value // 14))
    shadow_alpha = gradient.point(lambda value: max(0, value // 14 - 2))
    highlight_alpha = ImageChops.multiply(highlight_alpha, alpha)
    shadow_alpha = ImageChops.multiply(shadow_alpha, alpha)
    highlight = Image.new("RGBA", image.size, (255, 255, 255, 0))
    shadow = Image.new("RGBA", image.size, (0, 0, 0, 0))
    highlight.putalpha(highlight_alpha)
    shadow.putalpha(shadow_alpha)
    rgb.alpha_composite(highlight)
    rgb.alpha_composite(shadow)
    return rgb.filter(ImageFilter.UnsharpMask(radius=1.2, percent=70, threshold=3))


def gather_assets(raw_root: Path, ids: set[str]) -> list[Path]:
    chosen: dict[str, Path] = {}
    for path in raw_root.rglob("*.png"):
        if path.relative_to(raw_root).parts[0] not in BUILDING_DIRECTORIES:
            continue
        stem = path.stem
        if not (belongs_to_block(stem, ids) or include_shared(stem)):
            continue
        previous = chosen.get(path.name)
        if previous is not None and previous.read_bytes() != path.read_bytes():
            raise RuntimeError(f"atlas-name collision with different data: {previous} / {path}")
        chosen[path.name] = path
    return [chosen[name] for name in sorted(chosen)]


def hand_authored_region_names() -> set[str]:
    """Only preserve assets tracked before this generated full-coverage pass."""
    completed = subprocess.run(
        ["git", "ls-files", "sprites-override"], cwd=ROOT, check=True,
        capture_output=True, text=True,
    )
    return {Path(line).name for line in completed.stdout.splitlines() if line}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--blocks-java", type=Path, required=True)
    parser.add_argument("--raw-sprites", type=Path, required=True)
    parser.add_argument("--overwrite-existing", action="store_true")
    args = parser.parse_args()

    ids = runtime_ids(args.blocks_java)
    assets = gather_assets(args.raw_sprites, ids)
    if len(ids) < 300 or len(assets) < 800:
        raise RuntimeError(f"unexpected source coverage: {len(ids)} block ids, {len(assets)} assets")

    OUT.mkdir(parents=True, exist_ok=True)
    hand_authored = hand_authored_region_names()
    copied = enhanced = preserved = 0
    for source_path in assets:
        destination = OUT / source_path.name
        if destination.name in hand_authored and not args.overwrite_existing:
            preserved += 1
            continue
        with Image.open(source_path) as source:
            source = source.convert("RGBA")
            result = scaled(source) if is_dynamic_region(source_path.stem) else enhance_static(source)
        result.save(destination, optimize=True)
        if is_dynamic_region(source_path.stem):
            copied += 1
        else:
            enhanced += 1

    manifest = ROOT / "FULL_STRUCTURE_MANIFEST.md"
    manifest.write_text(
        "# Full v159.7 structure resprite batch\n\n"
        f"- Buildable runtime IDs parsed from `Blocks.java`: {len(ids)}\n"
        f"- Overridden atlas regions: {len(assets)}\n"
        f"- Static chassis regions with restrained directional material shading: {enhanced}\n"
        f"- Runtime-owned animated/tint/recoil/heat/liquid regions scaled only: {copied}\n"
        f"- Previously hand-authored regions intentionally preserved: {preserved}\n"
        "- Source: `Anuken/Mindustry@v159.7` raw block sprites\n"
        "- Texture contract: `texturescale: 0.125`, source assets at 8x vanilla dimensions\n\n"
        "All filenames are preserved exactly. No block behavior, item, liquid, projectile,\n"
        "payload, beam, smoke, particle or procedural runtime effect is replaced.\n",
        encoding="utf-8",
    )
    print(f"Generated {enhanced + copied} overrides: {enhanced} enhanced static, {copied} runtime layers, {preserved} preserved.")


if __name__ == "__main__":
    main()
